"""Offline pipeline boundary tests; no generators, model calls or messages."""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


def load(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pipeline = load('knowledge-pipeline')
kinetic = load('apply-kinetic-rules')


class PipelineSafetyTests(unittest.TestCase):
    def test_existing_mode_never_generates_and_failure_stops_publish(self):
        for code in (0, 2):
            with self.subTest(code=code), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp) / 'source'
                root.mkdir()
                candidate = Path(tmp) / 'candidate'
                seen = []
                def execute(items):
                    seen.extend(name for name, _ in items)
                    return [{'step': name, 'exit_code': code} for name, _ in items]
                with patch.object(pipeline, 'ROOT', root), patch.object(pipeline, 'WEB', Path(tmp) / 'web'), \
                     patch.object(pipeline.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout='')), \
                     patch.object(pipeline, 'run_steps', side_effect=execute), \
                     patch('sys.argv', ['pipeline', '--validate-existing', '--candidate', str(candidate)]):
                    self.assertEqual(pipeline.main(), code)
                self.assertFalse(any(name.startswith('Generate:') for name in seen))
                publication = [
                    'Publish:policy-candidate',
                    'Publish:version-candidate',
                    'Publish:reconcile-candidates',
                    'Publish:derived-projection',
                ]
                self.assertEqual(
                    [name for name in seen if name.startswith('Publish:')],
                    publication if code == 0 else [],
                )

    def test_news_change_invalidates_stable_source(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(pipeline, 'ROOT', Path(tmp)):
            (Path(tmp) / '.ua').mkdir()
            news = Path(tmp) / '.ua/news-feed.json'
            news.write_text('[]')
            old = pipeline.source_fingerprint()
            news.write_text('[{"title":"new"}]')
            self.assertNotEqual(old, pipeline.source_fingerprint())

    def test_manifest_change_invalidates_stable_source(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(pipeline, 'ROOT', Path(tmp)):
            publication = Path(tmp) / 'publication'
            publication.mkdir()
            manifest = publication / 'publication-manifest.json'
            manifest.write_text('{"version": 1}')
            old = pipeline.source_fingerprint()
            manifest.write_text('{"version": 1, "revoked_paths": ["concepts/a.md"]}')
            self.assertNotEqual(old, pipeline.source_fingerprint())

    def test_publication_order_requires_policy_version_reconcile(self):
        candidate = Path('/tmp/final-publication-candidate')
        names = [name for name, _ in pipeline.steps(candidate)]
        self.assertEqual(
            names[-5:],
            [
                'Validate:all',
                'Publish:policy-candidate',
                'Publish:version-candidate',
                'Publish:reconcile-candidates',
                'Publish:derived-projection',
            ],
        )

        version_command = dict(pipeline.steps(candidate))['Publish:version-candidate']
        self.assertNotIn('--strict', version_command)

    def test_kinetic_no_notify_keeps_rule_application(self):
        with patch.object(kinetic, 'rule4_slm_llm_classification', return_value=[{'slug': 'fixture', 'aiModelClass': 'SLM'}]) as r4, \
             patch.object(kinetic, 'rule6_unapproved_hypothesis_audit', return_value={'violations': [], 'clean_sessions': []}) as r6, \
             patch.object(kinetic, 'notify_telegram') as notify, \
             patch('sys.argv', ['kinetic', '--no-notify']):
            self.assertEqual(kinetic.main(), 0)
            self.assertFalse(kinetic.CHECK_ONLY)
            r4.assert_called_once()
            r6.assert_called_once()
            notify.assert_not_called()


class LegacyJobGuardTests(unittest.TestCase):
    """겹침 가드: 락 없이 도는 로드된 옛 작업은 막고, 공유 락 래퍼로 실행되는 작업은 통과(2026-11-06)."""

    def plist(self, d, label, args):
        import plistlib
        with open(Path(d) / f'ai.2nd.{label}.plist', 'wb') as fh:
            plistlib.dump({'Label': f'ai.2nd.{label}', 'ProgramArguments': args}, fh)

    def test_shares_lock_detection(self):
        with tempfile.TemporaryDirectory() as d:
            self.plist(d, 'daily-fetch', ['/bin/bash', '/x/hermes-wrap.sh', 'job', 'python3 /x/with-pipeline-lock.py -- bash y.sh'])  # hermes-wrap 이 bash -c 로 실행하는 명령 문자열 안의 래퍼도 락 공유
            self.plist(d, 'mention-only', ['/bin/bash', '/x/old.sh', '--note', 'no-with-pipeline-lock.pyx'])  # 이름만 비슷한 문자열은 아님
            self.plist(d, 'daily-ingest', ['/usr/bin/python3', '/Users/a/2nd/scripts/with-pipeline-lock.py', '--', '/bin/bash', 'x.sh'])
            self.plist(d, 'sync-dronewiki', ['/bin/bash', '/x/old-generator.sh'])
            home = Path(d)
            self.assertTrue(pipeline.shares_pipeline_lock('daily-ingest', home))
            self.assertFalse(pipeline.shares_pipeline_lock('sync-dronewiki', home))
            self.assertTrue(pipeline.shares_pipeline_lock('daily-fetch', home))
            self.assertFalse(pipeline.shares_pipeline_lock('mention-only', home))
            self.assertFalse(pipeline.shares_pipeline_lock('no-such-job', home))   # plist 없음 → 막는 쪽
            (home / 'ai.2nd.broken.plist').write_text('not a plist')
            self.assertFalse(pipeline.shares_pipeline_lock('broken', home))

    def run_main(self, loaded, shares):
        import contextlib, io
        calls = []
        def fake_run(cmd, **kw):
            label = cmd[-1].removeprefix('ai.2nd.')
            return subprocess.CompletedProcess(cmd, 0 if label in loaded else 113, '', '')
        out = io.StringIO()
        old = (pipeline.subprocess.run, pipeline.shares_pipeline_lock, sys.argv)
        pipeline.subprocess.run, pipeline.shares_pipeline_lock = fake_run, (lambda label, *a: label in shares)
        sys.argv = ['knowledge-pipeline.py', '--refresh-derived']  # 후보 경로가 없어 가드 통과 뒤 'isolated --candidate' 로 멈춘다
        try:
            with contextlib.redirect_stdout(out):
                code = pipeline.main()
        finally:
            pipeline.subprocess.run, pipeline.shares_pipeline_lock, sys.argv = old
        return code, out.getvalue()

    def test_loaded_lock_sharing_jobs_do_not_block(self):
        code, out = self.run_main(loaded={'daily-fetch', 'daily-ingest'}, shares={'daily-fetch', 'daily-ingest'})
        self.assertNotIn('overlapping legacy', out); self.assertIn('isolated --candidate', out)

    def test_loaded_job_without_lock_still_blocks(self):
        code, out = self.run_main(loaded={'daily-ingest', 'sync-dronewiki'}, shares={'daily-ingest'})
        self.assertEqual(code, 2); self.assertIn('overlapping legacy', out)

    def test_nothing_loaded_passes_guard(self):
        code, out = self.run_main(loaded=set(), shares=set())
        self.assertNotIn('overlapping legacy', out)


class DiscoveryDrainTests(unittest.TestCase):
    def test_remaining_pending_parse(self):
        self.assertEqual(pipeline.remaining_pending('처리 결과: 성공 10 / 실패 0 / 남은 미처리 5개'), 5)
        self.assertEqual(pipeline.remaining_pending('✅ 신규/변경된 raw 문서가 없습니다. 처리할 것이 없습니다.'), 0)
        self.assertIsNone(pipeline.remaining_pending('알 수 없는 출력'))

    def test_drain_until_empty(self):
        outs = iter([(0, '남은 미처리 10개'), (0, '남은 미처리 0개')])
        r = pipeline.drain_discovery(lambda: next(outs), '남은 미처리 20개')
        self.assertEqual((r['stopped'], r['remaining'], r['rounds']), ('DONE', 0, 3))

    def test_drain_stops_without_progress(self):
        r = pipeline.drain_discovery(lambda: (0, '남은 미처리 5개'), '남은 미처리 5개')
        self.assertEqual((r['stopped'], r['remaining']), ('NO_PROGRESS', 5))

    def test_drain_stops_on_failure(self):
        r = pipeline.drain_discovery(lambda: (1, ''), '남은 미처리 5개')
        self.assertEqual((r['stopped'], r['remaining']), ('EXTRACTION_FAILED', 5))

    def test_drain_respects_budget(self):
        ticks = iter([0, 5000])
        r = pipeline.drain_discovery(lambda: self.fail('예산 소진 뒤에는 호출하지 않는다'), '남은 미처리 5개', budget_sec=1200, clock=lambda: next(ticks))
        self.assertEqual((r['stopped'], r['remaining']), ('BUDGET_EXHAUSTED', 5))

    def test_nothing_pending_makes_no_extra_call(self):
        r = pipeline.drain_discovery(lambda: self.fail('호출 금지'), '남은 미처리 0개')
        self.assertEqual((r['stopped'], r['rounds']), ('DONE', 1))


if __name__ == '__main__':
    unittest.main()
