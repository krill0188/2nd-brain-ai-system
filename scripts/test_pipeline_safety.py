"""Offline pipeline boundary tests; no generators, model calls or messages."""
import importlib.util
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
            names[-4:],
            [
                'Validate:all',
                'Publish:policy-candidate',
                'Publish:version-candidate',
                'Publish:reconcile-candidates',
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


if __name__ == '__main__':
    unittest.main()
