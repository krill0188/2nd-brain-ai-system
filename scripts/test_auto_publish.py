"""auto-publish safety fixtures: judging, hash-pinned approvals, and step-failure rollback with a fake runner."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import auto_publish_lib as lib  # noqa: E402

spec = importlib.util.spec_from_file_location('auto_publish', HERE / 'auto-publish.py')
ap = importlib.util.module_from_spec(spec)
sys.modules['auto_publish'] = ap
spec.loader.exec_module(ap)

GOOD = b'---\ntitle: Test page\n---\nbody line\n'


def doc(body='body', extra=''):
    return f'---\ntitle: T\n{extra}---\n{body}\n'.encode()


class JudgeTests(unittest.TestCase):
    def test_clean_page_passes(self):
        self.assertEqual(lib.judge_file('concepts/a.md', GOOD), [])

    def test_sensitive_patterns_fail(self):
        cases = {
            'local-path': 'see /Users/amaster/secrets/x',
            'api-key': 'key sk-abcdefghijklmnopqrstuvwxyz123456',
            'email': 'contact someone@company.io',
            'private-key': '-----BEGIN RSA PRIVATE KEY-----',
            'secret-assignment': 'password: hunter2hunter2',
        }
        for name, text in cases.items():
            reasons = lib.judge_file('concepts/a.md', doc(text))
            self.assertIn(f'sensitive-{name}', reasons, name)

    def test_example_email_allowed(self):
        self.assertEqual(lib.judge_file('concepts/a.md', doc('mail me@example.com')), [])

    def test_disallowed_and_denied_paths(self):
        self.assertIn('path-not-allowed', lib.judge_file('scripts/x.md', GOOD))
        self.assertEqual(lib.judge_file('research/ideas/x.md', GOOD), ['hard-deny-dir'])
        self.assertEqual(lib.judge_file('raw/career-quiz/x.md', GOOD), ['hard-deny-dir'])
        self.assertEqual(lib.judge_file('concepts/../../etc/x.md', GOOD), ['path-escape'])
        self.assertIn('not-markdown', lib.judge_file('concepts/a.json', GOOD))

    def test_metadata_and_frontmatter(self):
        self.assertIn('metadata-visibility-private', lib.judge_file('concepts/a.md', doc(extra='visibility: private\n')))
        self.assertIn('metadata-status-draft', lib.judge_file('concepts/a.md', doc(extra='status: draft\n')))
        self.assertIn('no-frontmatter', lib.judge_file('concepts/a.md', b'just text'))
        self.assertIn('no-title', lib.judge_file('concepts/a.md', b'---\nx: y\n---\nbody'))

    def test_oversized_and_binary(self):
        self.assertIn('file-too-large', lib.judge_file('concepts/a.md', GOOD + b'x' * 300_000))
        self.assertIn('not-utf8', lib.judge_file('concepts/a.md', b'\xff\xfe\x00'))

    def test_batch_caps(self):
        self.assertEqual(lib.judge_batch(45, 715), [])
        self.assertTrue(lib.judge_batch(101, 10))
        self.assertTrue(lib.judge_batch(10, 1501))

    def test_changed_lines(self):
        self.assertEqual(lib.count_changed_lines(None, b'a\nb\n'), 2)
        self.assertEqual(lib.count_changed_lines(b'a\nb\n', b'a\nc\n'), 2)
        self.assertEqual(lib.count_changed_lines(b'a\n', b'a\n'), 0)

    def test_web_and_live_checks(self):
        self.assertTrue(lib.web_sync_ok(6, 3))
        self.assertEqual(lib.web_sync_ok(0, 0), ['no-change'])
        self.assertTrue(lib.live_check_ok({'/': 200, '/news': 500}, 460, 463))
        self.assertTrue(lib.live_check_ok({'/': 200}, 450, 463))
        self.assertEqual(lib.live_check_ok({'/': 200, '/wiki': 200}, 461, 463), [])


class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.state = Path(self.tmp.name)
        self.items = [{'path': 'concepts/a.md', 'sha256': 'a' * 64, 'reasons': ['sensitive-email']}]

    def make(self):
        req = lib.new_request(self.items, [])
        ap.save_request(self.state, req)
        return req

    def test_pending_does_not_approve(self):
        self.make()
        self.assertEqual(lib.approved_pairs(ap.load_requests(self.state)), set())

    def test_approved_pins_path_and_hash(self):
        req = self.make()
        self.assertEqual(ap.decide(self.state, req['id'], 'approved', 'telegram'), 'approved')
        pairs = lib.approved_pairs(ap.load_requests(self.state))
        self.assertIn(('concepts/a.md', 'a' * 64), pairs)
        self.assertNotIn(('concepts/a.md', 'b' * 64), pairs)

    def test_content_edit_changes_request_id(self):
        other = [{**self.items[0], 'sha256': 'b' * 64}]
        self.assertNotEqual(lib.request_id(self.items), lib.request_id(other))

    def test_expiry_and_double_decision(self):
        req = self.make()
        self.assertEqual(ap.decide(self.state, req['id'], 'approved', 'cli'), 'approved')
        self.assertTrue(ap.decide(self.state, req['id'], 'rejected', 'cli').startswith('not-pending'))
        later = time.time() + lib.APPROVAL_TTL_SECONDS + 10
        self.assertEqual(lib.approved_pairs(ap.load_requests(self.state), later), set())

    def test_decide_rejects_bad_ids(self):
        self.assertEqual(ap.decide(self.state, '../../etc/passwd', 'approved', 'x'), 'invalid-id')
        self.assertEqual(ap.decide(self.state, 'abcdef123456', 'approved', 'x'), 'not-found')

    def test_hand_edited_approval_without_decider_ignored(self):
        req = self.make()
        raw = json.loads((self.state / 'approvals' / f"{req['id']}.json").read_text())
        raw['status'] = 'approved'
        self.assertEqual(lib.approved_pairs([raw]), set())

    def test_hash_mismatch_is_exception_even_if_content_clean(self):
        row = {'path': 'concepts/a.md', 'source_sha256': 'f' * 64}
        ok, exc, _ = lib.decide_hold_rows([row], lambda p: GOOD, lambda p: None, set())
        self.assertEqual(ok, [])
        self.assertIn('hash-mismatch', exc[0]['reasons'])

    def test_human_approval_overrides_content_rule_only_for_same_hash(self):
        data = doc('mail someone@company.io')
        sha = lib.sha256_text(data)
        row = {'path': 'concepts/a.md', 'source_sha256': sha}
        ok, exc, _ = lib.decide_hold_rows([row], lambda p: data, lambda p: None, {('concepts/a.md', sha)})
        self.assertEqual((len(ok), exc), (1, []))
        ok, exc, _ = lib.decide_hold_rows([row], lambda p: data, lambda p: None, {('concepts/a.md', 'z' * 64)})
        self.assertEqual((ok, len(exc)), ([], 1))


class FakeRun:
    """Scriptable subprocess stand-in with a tiny in-memory git (staged set, commits, pushes)."""

    def __init__(self, root, rows, fail=None, alias_after='new-deploy.vercel.app'):
        self.root, self.rows, self.fail = root, rows, fail or {}
        self.calls, self.staged, self.commits, self.pushes, self.alias_sets = [], [], [], [], []
        self.alias, self.alias_after = 'old-deploy.vercel.app', alias_after
        self.gate_calls = 0

    def result(self, out='', code=0, err=''):
        return subprocess.CompletedProcess([], code, out, err)

    def __call__(self, cmd, cwd=None, timeout=None):
        self.calls.append(cmd)
        text = ' '.join(map(str, cmd))
        for key, code in self.fail.items():
            if key in text:
                return self.result(code=code, err=f'{key} failed')
        if cmd[0] == 'git':
            sub = cmd[3]
            if sub == 'status' or (sub == 'rev-parse' and False):
                return self.result('')
            if sub == 'rev-parse':
                return self.result('abc')
            if sub == 'add':
                self.staged = [a for a in cmd[5:] if not a.startswith('-')]
                return self.result()
            if sub == 'diff':
                return self.result('\n'.join(self.staged))
            if sub == 'commit':
                self.commits.append(list(self.staged))
                self.staged = []
                return self.result()
            if sub == 'push':
                self.pushes.append(text)
            return self.result()
        if 'publication-gate.py' in text:
            report = Path(cmd[cmd.index('--report') + 1])
            self.gate_calls += 1
            rows = self.rows if self.gate_calls == 1 else [dict(r, action='approve') for r in self.rows]
            report.write_text(json.dumps({'ready': self.gate_calls > 1 and not any(r['action'] == 'block' for r in rows),
                                          'counts': {}, 'files': rows}))
            return self.result(code=0 if self.gate_calls > 1 else 2)
        if 'knowledge-pipeline.py' in text:
            (Path(self.root) / 'cands/20261001T000000Z-x').mkdir(parents=True, exist_ok=True)
            return self.result()
        if cmd[:3] == ['vercel', 'alias', 'ls']:
            return self.result(f'  {self.alias}   drone-wiki-web.vercel.app   1d\n')
        if cmd[:3] == ['vercel', 'alias', 'set']:
            self.alias_sets.append(cmd[3])
            self.alias = cmd[3]
            return self.result()
        if cmd[:2] == ['vercel', '--prod']:
            self.alias = self.alias_after
            return self.result('Production: https://drone-wiki-abc123xyz-jon-kkm-s-projects.vercel.app\n')
        if cmd[0] == 'rsync' and '-rcn' in cmd:
            return self.result('>f.st...... concepts/a.md\n')
        return self.result()


class ExecuteTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        for d in ('root/publication', 'root/concepts', 'root/scripts', 'web/data/wiki', 'cands'):
            (self.base / d).mkdir(parents=True)
        (self.base / 'root/publication/policy.json').write_text(json.dumps({'approved_files': {}, 'baseline': {'files': {}}}))
        self.write('concepts/a.md', GOOD)
        self.messages = []

    def write(self, rel, data):
        (self.base / 'root' / rel).write_bytes(data)
        return lib.sha256_text(data)

    def ctx(self, fake, apply=True, fetch=None):
        return ap.Ctx(apply=apply, root=self.base / 'root', web=self.base / 'web', candidates=self.base / 'cands',
                      state=self.base / 'state', run=fake, notify=self.messages.append,
                      fetch=fetch or self.healthy_fetch, sleep=lambda s: None)

    @staticmethod
    def healthy_fetch(url):
        if url.endswith('/api/pages'):
            return 200, json.dumps([{}] * 463).encode()
        return 200, b'ok'

    def rows(self, path='concepts/a.md'):
        data = (self.base / 'root' / path).read_bytes()
        return [{'path': path, 'action': 'hold', 'source_sha256': lib.sha256_text(data)}]

    def test_happy_path_pushes_only_after_live_check(self):
        fake = FakeRun(self.base, self.rows())
        code = ap.execute(self.ctx(fake))
        self.assertEqual(code, 0, self.messages)
        self.assertEqual(len(fake.pushes), 2)
        self.assertIn(['concepts/a.md', 'publication/policy.json'], fake.commits)
        order = [' '.join(map(str, c)) for c in fake.calls]
        self.assertLess(next(i for i, c in enumerate(order) if 'vercel --prod' in c),
                        next(i for i, c in enumerate(order) if 'push' in c))
        self.assertTrue(any('배포 완료' in m for m in self.messages))

    def test_dry_run_changes_nothing(self):
        fake = FakeRun(self.base, self.rows())
        self.assertEqual(ap.execute(self.ctx(fake, apply=False)), 0)
        self.assertEqual((fake.commits, fake.pushes, fake.alias_sets), ([], [], []))
        self.assertFalse(any(c[0] == 'rsync' and '-rcn' not in c for c in fake.calls))
        self.assertFalse((self.base / 'state/approvals').exists())

    def test_gate_block_stops_before_any_write(self):
        rows = [{'path': 'x.md', 'action': 'block', 'reason': 'baseline-snapshot-drift'}]
        fake = FakeRun(self.base, rows)
        self.assertEqual(ap.execute(self.ctx(fake)), 4)
        self.assertEqual((fake.commits, fake.pushes), ([], []))
        self.assertTrue(any('실패' in m for m in self.messages))

    def test_sensitive_content_becomes_pinned_request_not_publication(self):
        sha = self.write('concepts/a.md', doc('see /Users/amaster/.env'))
        fake = FakeRun(self.base, [{'path': 'concepts/a.md', 'action': 'hold', 'source_sha256': sha}])
        self.assertEqual(ap.execute(self.ctx(fake)), 5)
        self.assertEqual((fake.commits, fake.pushes), ([], []))
        saved = list((self.base / 'state/approvals').glob('*.json'))
        self.assertEqual(len(saved), 1)
        req = json.loads(saved[0].read_text())
        self.assertEqual((req['status'], req['items'][0]['sha256']), ('pending', sha))
        self.assertIn('/publish approve', self.messages[0])
        self.assertFalse(any(c[0] == 'rsync' for c in fake.calls))

    def test_same_pending_request_is_not_renotified(self):
        sha = self.write('concepts/a.md', doc('mail someone@company.io'))
        rows = [{'path': 'concepts/a.md', 'action': 'hold', 'source_sha256': sha}]
        ap.execute(self.ctx(FakeRun(self.base, rows)))
        ap.execute(self.ctx(FakeRun(self.base, rows)))
        self.assertEqual(len(self.messages), 1)

    def test_approved_exception_publishes(self):
        data = doc('mail someone@company.io')
        sha = self.write('concepts/a.md', data)
        rows = [{'path': 'concepts/a.md', 'action': 'hold', 'source_sha256': sha}]
        ap.execute(self.ctx(FakeRun(self.base, rows)))
        req_id = next((self.base / 'state/approvals').glob('*.json')).stem
        ap.decide(self.base / 'state', req_id, 'approved', 'telegram')
        fake = FakeRun(self.base, rows)
        self.assertEqual(ap.execute(self.ctx(fake)), 0)
        self.assertEqual(len(fake.pushes), 2)

    def test_edit_after_approval_requires_new_approval(self):
        sha = self.write('concepts/a.md', doc('mail someone@company.io'))
        rows = [{'path': 'concepts/a.md', 'action': 'hold', 'source_sha256': sha}]
        ap.execute(self.ctx(FakeRun(self.base, rows)))
        ap.decide(self.base / 'state', next((self.base / 'state/approvals').glob('*.json')).stem, 'approved', 'telegram')
        sha2 = self.write('concepts/a.md', doc('mail other@company.io'))
        fake = FakeRun(self.base, [{'path': 'concepts/a.md', 'action': 'hold', 'source_sha256': sha2}])
        self.assertEqual(ap.execute(self.ctx(fake)), 5)
        self.assertEqual(fake.pushes, [])

    def test_oversized_batch_needs_approval(self):
        rows = []
        for i in range(101):
            self.write('concepts/a.md', GOOD)
            rows.append({'path': 'concepts/a.md', 'action': 'hold', 'source_sha256': lib.sha256_text(GOOD)})
        fake = FakeRun(self.base, rows)
        self.assertEqual(ap.execute(self.ctx(fake)), 5)
        self.assertEqual(fake.commits, [])

    def test_file_changed_between_judgement_and_approval_aborts(self):
        rows = self.rows()
        fake = FakeRun(self.base, rows)
        original = ap.approve_and_commit

        def tamper(ctx, selected):
            self.write('concepts/a.md', doc('evil /Users/amaster/x'))
            return original(ctx, selected)
        ap.approve_and_commit = tamper
        self.addCleanup(setattr, ap, 'approve_and_commit', original)
        self.assertEqual(ap.execute(self.ctx(fake)), 3)
        self.assertEqual((fake.commits, fake.pushes), ([], []))

    def test_build_failure_restores_web_and_never_deploys(self):
        fake = FakeRun(self.base, self.rows(), fail={'next build': 1})
        self.assertEqual(ap.execute(self.ctx(fake)), 3)
        text = [' '.join(map(str, c)) for c in fake.calls]
        self.assertTrue(any('restore --source=origin/main' in c for c in text))
        self.assertFalse(any('vercel --prod' in c for c in text))
        self.assertEqual(fake.pushes, [])

    def test_live_check_failure_rolls_alias_back_and_does_not_push(self):
        def broken(url):
            return (200, json.dumps([{}] * 463).encode()) if url.endswith('/api/pages') else (500, b'')
        fake = FakeRun(self.base, self.rows())
        self.assertEqual(ap.execute(self.ctx(fake, fetch=broken)), 6)
        self.assertEqual(fake.alias, 'old-deploy.vercel.app')
        self.assertEqual(fake.pushes, [])
        self.assertTrue(any('restore --source=origin/main' in ' '.join(map(str, c)) for c in fake.calls))

    def test_cannot_determine_alias_refuses_to_deploy(self):
        class NoAlias(FakeRun):
            def __call__(self, cmd, cwd=None, timeout=None):
                if cmd[:3] == ['vercel', 'alias', 'ls']:
                    self.calls.append(cmd)
                    return self.result('')
                return super().__call__(cmd, cwd, timeout)
        fake = NoAlias(self.base, self.rows())
        self.assertEqual(ap.execute(self.ctx(fake)), 3)
        self.assertFalse(any(c[:2] == ['vercel', '--prod'] for c in fake.calls))

    def test_web_deletion_cap(self):
        class ManyDeletes(FakeRun):
            def __call__(self, cmd, cwd=None, timeout=None):
                if cmd[0] == 'rsync' and '-rcn' in cmd:
                    self.calls.append(cmd)
                    return self.result('\n'.join(f'*deleting   old{i}.md' for i in range(6)) + '\n')
                return super().__call__(cmd, cwd, timeout)
        fake = ManyDeletes(self.base, self.rows())
        self.assertEqual(ap.execute(self.ctx(fake)), 3)
        self.assertFalse(any(c[0] == 'rsync' and '-rcn' not in c for c in fake.calls))

    def test_preflight_refuses_dirty_publication(self):
        class Dirty(FakeRun):
            def __call__(self, cmd, cwd=None, timeout=None):
                if cmd[0] == 'git' and cmd[3] == 'status' and 'publication/' in cmd:
                    self.calls.append(cmd)
                    return self.result(' M publication/policy.json')
                return super().__call__(cmd, cwd, timeout)
        fake = Dirty(self.base, self.rows())
        self.assertEqual(ap.execute(self.ctx(fake)), 3)
        self.assertEqual(fake.commits, [])

    def test_telegram_text_is_form_safe(self):
        self.assertEqual(ap.telegram_safe('a<b>&c 50%'), 'a(b)+c 50pct')


if __name__ == '__main__':
    unittest.main()
