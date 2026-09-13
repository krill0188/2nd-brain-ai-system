"""Publication boundary regression fixtures, isolated from real knowledge."""
import importlib.util
import tempfile
import unittest
from pathlib import Path


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), Path(__file__).with_name(name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gate = load('publication-gate')
pipeline = load('knowledge-pipeline')


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.src, self.dst = self.base / 'source', self.base / 'snapshot'
        for root in (self.src, self.dst):
            (root / 'raw').mkdir(parents=True)
            (root / 'raw/a.md').write_text('existing evidence')
        self.policy = {'version': 1, 'default': 'review', 'directories': {'raw/': 'review'},
                       'approved_files': {}, 'baseline': {'files': {'raw/a.md': gate.digest(self.dst / 'raw/a.md')}}}

    def audit(self):
        return gate.audit(self.src, self.dst, self.policy)

    def test_baseline_and_new_raw_no_delete(self):
        (self.src / 'raw/new.md').write_text('new evidence')
        report = self.audit()
        self.assertEqual(report['counts'], {'retain': 1, 'hold': 1})
        self.assertEqual(report['deletions'], 0)
        with self.assertRaises(ValueError):
            gate.stage(self.src, self.dst, self.base / 'candidate', report)
        self.assertEqual((self.dst / 'raw/a.md').read_text(), 'existing evidence')

    def test_explicit_deny_overrides_file_and_directory_allow(self):
        p = self.src / 'raw/a.md'
        p.write_text('---\nvisibility: private\npublish_to_web: true\n---\nevidence')
        self.policy['approved_files']['raw/a.md'] = gate.digest(p)
        self.policy['directories']['raw/'] = 'public'
        self.assertEqual(self.audit()['files'][0]['reason'], 'explicit-deny')
        self.assertFalse(self.audit()['ready'])

    def test_duplicate_metadata_is_blocked(self):
        (self.src / 'raw/a.md').write_text('---\nvisibility: private\nvisibility: public\n---\nx')
        self.assertEqual(self.audit()['files'][0]['reason'], 'invalid-metadata')

    def test_wrong_metadata_type_does_not_approve(self):
        (self.src / 'raw/new.md').write_text('---\nclassification: true\n---\nx')
        row = next(r for r in self.audit()['files'] if r['path'] == 'raw/new.md')
        self.assertEqual(row['reason'], 'unrecognized-metadata')

    def test_symlink_and_policy_traversal(self):
        (self.src / 'raw/a.md').unlink()
        (self.src / 'raw/a.md').symlink_to(self.dst / 'raw/a.md')
        self.assertFalse(self.audit()['ready'])
        self.policy['approved_files']['../escape'] = 'hash'
        with self.assertRaises(ValueError):
            self.audit()

    def test_candidate_isolated_and_race_rejected(self):
        report = self.audit()
        gate.stage(self.src, self.dst, self.base / 'candidate', report)
        self.assertEqual((self.base / 'candidate/raw/a.md').read_text(), 'existing evidence')
        (self.dst / 'raw/a.md').write_text('changed after audit')
        with self.assertRaises(ValueError):
            gate.stage(self.src, self.dst, self.base / 'race', report)
        self.assertFalse((self.base / 'race').exists())

    def test_derived_new_bytes_cannot_bypass_unapproved_source(self):
        (self.src / '.ua').mkdir()
        p = self.src / '.ua/embeddings.json'
        p.write_text('{"docs": []}')
        self.policy['approved_files']['.ua/embeddings.json'] = gate.digest(p)
        (self.src / 'raw/new.md').write_text('unapproved')
        self.assertIn('derived-source-review-required', [r['reason'] for r in self.audit()['files']])

    def test_pipeline_failure_never_reaches_publish(self):
        seen = []
        def execute(command, **kwargs):
            seen.append(command)
            return type('Result', (), {'returncode': 1 if command == ['validate'] else 0})()
        result = pipeline.run_steps([('generate', ['generate']), ('validate', ['validate']),
                                     ('publish', ['publish'])], execute)
        self.assertEqual(seen, [['generate'], ['validate']])
        self.assertEqual(result[-1]['exit_code'], 1)


if __name__ == '__main__':
    unittest.main()
