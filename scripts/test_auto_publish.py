"""auto-publish safety fixtures: judging, hash-pinned approvals, and step-failure rollback with a fake runner."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace

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


class RunnerEncodingTests(unittest.TestCase):
    def test_default_run_handles_non_utf8_rsync_style_output(self):
        result = ap.default_run([
            sys.executable, '-c',
            'import sys; sys.stdout.buffer.write(b"ok\\xff\\xfe\\n")',
        ])
        self.assertEqual(result.returncode, 0)
        self.assertIn('ok', result.stdout)
        self.assertIn('\ufffd', result.stdout)


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
        later = time.time() + lib.DECISION_TTL_SECONDS + 10
        self.assertEqual(lib.approved_pairs(ap.load_requests(self.state), later), set())

    def test_approval_outlives_the_next_daily_run(self):
        """회귀(2026-11-06): 요청은 10:30 에 생기고 다음 실행은 24시간 뒤. 알림 직후(4시간 안) 승인한 건이 20시간 TTL 에 걸려 다음 실행 전에 만료되던 결함."""
        req = self.make()
        created = req['created']
        self.assertEqual(ap.decide(self.state, req['id'], 'approved', 'telegram', now=created + 600), 'approved')   # 알림 10분 뒤 승인
        next_run = created + 24 * 3600                                                                               # 다음 날 같은 시각 실행
        self.assertEqual(lib.approved_pairs(ap.load_requests(self.state), next_run), {('concepts/a.md', 'a' * 64)})
        self.assertEqual(lib.approved_pairs(ap.load_requests(self.state), created + 600 + lib.DECISION_TTL_SECONDS + 5), set())  # 그래도 48시간 뒤에는 만료

    def test_pending_still_expires_after_20h_and_cannot_be_decided(self):
        req = self.make()
        late = req['created'] + lib.APPROVAL_TTL_SECONDS + 5
        self.assertEqual(lib.request_state(req, late), 'expired')
        self.assertEqual(ap.decide(self.state, req['id'], 'approved', 'telegram', now=late), 'not-pending:expired')

    def test_rejection_also_uses_the_decision_window(self):
        req = self.make()
        ap.decide(self.state, req['id'], 'rejected', 'telegram', now=req['created'] + 60)
        self.assertEqual(lib.request_state(ap.load_requests(self.state)[0], req['created'] + 30 * 3600), 'rejected')

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


class DeliverTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)
        self.script = self.dir / 'notify.sh'
        self.script.write_text('#!/bin/bash\n')
        self.log = self.dir / 'state' / 'notify.log'

    def send(self, results, **kw):
        calls = []

        def runner(cmd, **_):
            calls.append(cmd)
            result = results[min(len(calls), len(results)) - 1]
            if isinstance(result, Exception):
                raise result
            return subprocess.CompletedProcess(cmd, result, '', 'curl: boom' if result else '')

        sent = ap.deliver('title line\nsecond', runner=runner, notify_path=self.script, log_path=self.log,
                          pause=lambda _s: None, **kw)
        return sent, calls

    def test_success_logs_once(self):
        sent, calls = self.send([0])
        self.assertTrue(sent)
        self.assertEqual(len(calls), 1)
        self.assertIn('SENT', self.log.read_text())

    def test_retries_after_failure_then_succeeds(self):
        sent, calls = self.send([6, 0])
        self.assertTrue(sent)
        self.assertEqual(len(calls), 2)
        self.assertIn('rc=6', self.log.read_text())

    def test_timeout_never_raises_and_is_logged_as_failed(self):
        sent, calls = self.send([subprocess.TimeoutExpired('x', 60)])
        self.assertFalse(sent)
        self.assertEqual(len(calls), 2)
        text = self.log.read_text()
        self.assertIn('FAILED', text)
        self.assertIn('TimeoutExpired', text)

    def test_missing_script_is_logged_as_failed(self):
        sent = ap.deliver('m', notify_path=self.dir / 'nope.sh', log_path=self.log)
        self.assertFalse(sent)
        self.assertIn('notify.sh missing', self.log.read_text())


class WebSyncTests(unittest.TestCase):
    """preflight 의 web 폴더 동기화(sync_web_head): 뒤처지기만 하고 깨끗할 때만 fast-forward."""

    def run_sync(self, head='aaa', remote='bbb', ahead='0', behind='3', branch='main', dirty=''):
        calls = []

        def fake(cmd, cwd=None, timeout=None):
            calls.append(cmd[3:])
            sub = cmd[3]
            out = ''
            if sub == 'rev-parse':
                out = head if cmd[4] == 'HEAD' else remote
            elif sub == 'rev-list':
                out = ahead if cmd[5].startswith(f'{remote}..') else behind
            elif sub == 'branch':
                out = branch
            elif sub == 'status':
                out = dirty
            return subprocess.CompletedProcess([], 0, out, '')

        ctx = ap.Ctx(run=fake, web=Path('/web'), root=Path('/root'))
        ctx.say = lambda m: calls.append(('say', m))
        try:
            ap.sync_web_head(ctx)
            return None, calls
        except ap.Abort as exc:
            return exc, calls

    def merged(self, calls):
        return [c for c in calls if c[0] == 'merge']

    def test_equal_head_does_nothing(self):
        exc, calls = self.run_sync(head='x', remote='x')
        self.assertIsNone(exc); self.assertEqual(self.merged(calls), [])

    def test_behind_only_clean_main_fast_forwards(self):
        exc, calls = self.run_sync()
        self.assertIsNone(exc); self.assertEqual(self.merged(calls), [['merge', '--ff-only', 'origin/main']])
        self.assertTrue(any(c[0] == 'say' and '3 commit' in c[1] for c in calls))

    def test_ahead_or_diverged_aborts_without_merge(self):
        exc, calls = self.run_sync(ahead='2', behind='3')
        self.assertIn('web HEAD differs from origin/main', exc.detail); self.assertIn('ahead 2', exc.detail); self.assertEqual(self.merged(calls), [])
        exc, calls = self.run_sync(ahead='1', behind='0')
        self.assertIsNotNone(exc); self.assertEqual(self.merged(calls), [])

    def test_dirty_tracked_files_or_wrong_branch_abort(self):
        exc, calls = self.run_sync(dirty=' M app/page.tsx')
        self.assertIn('tracked files are modified', exc.detail); self.assertEqual(self.merged(calls), [])
        exc, calls = self.run_sync(branch='')
        self.assertIn('detached', exc.detail); self.assertEqual(self.merged(calls), [])
        exc, calls = self.run_sync(branch='feat/x')
        self.assertIn('feat/x', exc.detail); self.assertEqual(self.merged(calls), [])

    def test_untracked_files_do_not_block(self):
        # status 는 --untracked-files=no 로 부른다(eval-prod-result.json·site-audit/ 같은 미추적 파일은 막지 않는다)
        exc, calls = self.run_sync()
        self.assertTrue(any(c[0] == 'status' and '--untracked-files=no' in c for c in calls))


class ButtonNotifyTests(unittest.TestCase):
    """예외 승인 알림의 인라인 버튼(봇 callback_query 핸들러 publish:<approve|reject>:<id> 와 계약)."""
    BOT_CALLBACK = __import__('re').compile(r'^publish:(approve|reject):[0-9a-f]{12}$')

    def test_inline_keyboard_json_matches_telegram_and_bot_contract(self):
        kb = json.loads(ap.inline_keyboard([('✅ 승인', 'publish:approve:abcdef012345'), ('❌ 거부', 'publish:reject:abcdef012345')]))
        row = kb['inline_keyboard'][0]
        self.assertEqual([b['text'] for b in row], ['✅ 승인', '❌ 거부'])
        for b in row:
            self.assertRegex(b['callback_data'], self.BOT_CALLBACK); self.assertLessEqual(len(b['callback_data'].encode()), 64)   # 텔레그램 한도 64바이트

    def test_deliver_passes_buttons_as_second_arg_and_not_through_telegram_safe(self):
        calls = []
        def runner(cmd, **kw):
            calls.append(cmd); return subprocess.CompletedProcess(cmd, 0, '', '')
        with tempfile.TemporaryDirectory() as d:
            script = Path(d) / 'notify.sh'; script.write_text('#!/bin/bash\n')
            self.assertTrue(ap.deliver('제목 <b> & 100%', runner=runner, notify_path=script, log_path=Path(d) / 'n.log', buttons=[('OK', 'publish:approve:abcdef012345')]))
            self.assertTrue(ap.deliver('plain', runner=runner, notify_path=script, log_path=Path(d) / 'n.log'))
        self.assertEqual(len(calls[0]), 4); self.assertEqual(len(calls[1]), 3)                  # 버튼 있으면 인자 3개, 없으면 기존 호출 그대로
        self.assertNotIn('<', calls[0][2]); json.loads(calls[0][3])                             # 본문만 telegram_safe, 키보드 JSON 은 손대지 않음

    def test_alert_falls_back_to_plain_notify_without_button_sender(self):
        sent, with_buttons = [], []
        ap.Ctx(notify=sent.append).alert('msg', [('a', 'b')])
        self.assertEqual(sent, ['msg'])
        ap.Ctx(notify=sent.append, notify_buttons=lambda m, b: with_buttons.append((m, b))).alert('msg2', [('a', 'b')])
        self.assertEqual(with_buttons, [('msg2', [('a', 'b')])]); self.assertEqual(sent, ['msg'])

    def test_exception_request_notice_carries_approve_and_reject_buttons(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp); (base / 'state').mkdir()
            got = []
            ctx = ap.Ctx(apply=True, state=base / 'state', notify=lambda m: got.append((m, None)), notify_buttons=lambda m, b: got.append((m, b)), now=lambda: 1000.0)
            items = [{'path': 'concepts/a.md', 'sha256': 'a' * 64, 'reasons': ['file-too-large']}]
            with self.assertRaises(ap.Abort):
                ap.raise_exception_request(ctx, items, [], [])
        msg, buttons = got[0]
        self.assertIn('예외 승인 필요', msg); self.assertIn('48시간', msg); self.assertIn('20시간', msg)
        self.assertEqual([b[0] for b in buttons], ['✅ 승인', '❌ 거부'])
        for _, data in buttons: self.assertRegex(data, self.BOT_CALLBACK)
        self.assertEqual(buttons[0][1].split(':')[2], buttons[1][1].split(':')[2])


class ExplainFailureTests(unittest.TestCase):
    def test_known_causes_include_action_and_rerun(self):
        msg = lib.explain_failure('derived', "TimeoutExpired(['x'], 3600)")
        self.assertIn('시간 제한', msg)
        self.assertIn('재실행:', msg)
        self.assertIn('auto-publish.py --apply', msg)

    def test_unknown_cause_still_gives_rerun(self):
        msg = lib.explain_failure('deploy', 'weird')
        self.assertEqual(msg.count('재실행:'), 1)
        self.assertNotIn('원인:', msg)


class DoctorTests(unittest.TestCase):
    def setUp(self):
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import auto_publish_doctor as dr
        self.dr = dr

    def test_busy_processes_detected_but_not_doctor_itself(self):
        ps = "100 1 /py scripts/extract-knowledge-graph.py --limit 10\n200 1 /py scripts/auto-publish.py --doctor\n300 1 /usr/bin/other"
        self.assertEqual(self.dr.check_busy_processes(ps)[1], 'FAIL')
        self.assertEqual(self.dr.check_busy_processes("200 1 /py scripts/auto-publish.py --doctor")[1], 'OK')

    def test_legacy_launchd_overlap(self):
        r = self.dr.check_legacy_launchd(('a', 'b'), lambda l: True, lambda l: l == 'a')
        self.assertEqual(r[1], 'FAIL')
        self.assertIn('b', r[2])
        self.assertEqual(self.dr.check_legacy_launchd(('a',), lambda l: True, lambda l: True)[1], 'OK')
        self.assertEqual(self.dr.check_legacy_launchd(('a',), lambda l: False, lambda l: False)[1], 'OK')

    def test_pending_is_warn_integrity_is_fail(self):
        self.assertEqual(self.dr.check_pending_documents('{"discovery_pending_documents": 5, "canonical_node_source_fresh": true}')[1], 'WARN')
        self.assertEqual(self.dr.check_pending_documents('{"discovery_pending_documents": 0, "canonical_node_source_fresh": true}')[1], 'OK')
        self.assertEqual(self.dr.check_pending_documents('{"missing_nodes": 2, "canonical_node_source_fresh": true}')[1], 'WARN')  # 발행 중 그래프 재생성으로 해결
        self.assertEqual(self.dr.check_pending_documents('garbage')[1], 'WARN')


    def test_approved_files_hash_distinguishes_fail_and_warn(self):
        import hashlib, tempfile
        root = Path(tempfile.mkdtemp())
        (root / 'a.md').write_text('approved content'); (root / 'b.md').write_text('changed after approval')
        pins = {'a.md': hashlib.sha256(b'approved content').hexdigest(), 'b.md': hashlib.sha256(b'original').hexdigest()}
        run = lambda cmd, **kw: SimpleNamespace(stdout=' M a.md\n M b.md\n')
        self.assertEqual(self.dr.check_approved_committed(root, {'approved_files': pins}, run)[1], 'FAIL')  # a.md: 해시 일치+미커밋
        run2 = lambda cmd, **kw: SimpleNamespace(stdout=' M b.md\n')
        self.assertEqual(self.dr.check_approved_committed(root, {'approved_files': pins}, run2)[1], 'WARN')  # b.md 만: 승인 후 변경
        run3 = lambda cmd, **kw: SimpleNamespace(stdout='')
        self.assertEqual(self.dr.check_approved_committed(root, {'approved_files': pins}, run3)[1], 'OK')

    def test_porcelain_leading_space_not_lost_for_first_path(self):
        import hashlib, tempfile
        root = Path(tempfile.mkdtemp()); (root / 'concepts').mkdir()
        (root / 'concepts/x.md').write_text('same')
        pins = {'concepts/x.md': hashlib.sha256(b'same').hexdigest()}
        run = lambda cmd, **kw: SimpleNamespace(stdout=' M concepts/x.md\n')  # 첫 줄이 공백으로 시작
        self.assertEqual(self.dr.check_approved_committed(root, {'approved_files': pins}, run)[1], 'FAIL')

    def test_graph_staleness_is_warn_duplicates_are_fail(self):
        self.assertEqual(self.dr.check_pending_documents('{"missing_nodes": 3, "canonical_node_source_fresh": false}')[1], 'WARN')
        self.assertEqual(self.dr.check_pending_documents('{"duplicate_slugs": 1, "canonical_node_source_fresh": true}')[1], 'FAIL')

    def test_exit_code_and_report(self):
        rows = [('a', 'OK', 'x', ''), ('b', 'FAIL', 'y', '조치')]
        self.assertEqual(self.dr.exit_code(rows), 2)
        self.assertIn('종합: FAIL', self.dr.format_report(rows))
        self.assertEqual(self.dr.exit_code([('a', 'WARN', 'x', '')]), 0)

    def test_progress_in_failure_message(self):
        msg = lib.explain_failure('derived', 'TimeoutExpired', {'done': [{'step': 'Generate:embeddings', 'seconds': 12.0, 'exit_code': 0}], 'current': 'Generate:discovery'})
        self.assertIn('Generate:embeddings 12초', msg)
        self.assertIn('Generate:discovery 진행 중 끊김', msg)


if __name__ == '__main__':
    unittest.main()
