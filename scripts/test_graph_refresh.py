"""Isolated regressions for graph reconciliation and extraction failure tracking."""
import importlib.util
import json
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


build = load('build-canonical-graph')
extract = load('extract-knowledge-graph')


class GraphTests(unittest.TestCase):
    def test_refresh_metadata_and_retain_legacy_relationship(self):
        candidate = {'nodes': [{'id': 'a', 'name': 'new'}, {'id': 'b'}], 'edges': []}
        old = {'nodes': [{'id': 'a', 'name': 'old'}, {'id': 'removed'}], 'edges': [
            {'source': 'a', 'target': 'b', 'type': 'related'},
            {'source': 'a', 'target': 'removed', 'type': 'related'}]}
        result = build.reconcile(candidate, old)
        self.assertEqual(result['nodes'][0]['name'], 'new')
        self.assertEqual(len(result['edges']), 1)
        self.assertEqual(result['edges'][0]['review_status'], 'legacy-source-review-required')

    def test_duplicate_slug_fails_before_artifact_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'ontology').mkdir()
            (root / 'ontology/class-hierarchy.json').write_text('{"classes": {}}')
            for layer in ('concepts', 'entities'):
                (root / layer).mkdir()
                (root / layer / 'same.md').write_text('---\ntitle: same\n---\nx')
            with self.assertRaisesRegex(ValueError, 'duplicate'):
                build.build(root)
            self.assertFalse((root / '.ua/drone-knowledge-graph.json').exists())

    def test_nested_documents_and_legacy_endpoint_are_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'ontology').mkdir()
            (root / 'ontology/class-hierarchy.json').write_text('{"classes": {}}')
            (root / 'concepts/nested').mkdir(parents=True)
            for slug in ('a', 'b'):
                (root / 'concepts/nested' / (slug + '.md')).write_text('---\ntitle: ' + slug + '\n---\nx')
            candidate = build.build(root)
            result = build.reconcile(candidate, {'edges': [
                {'source': 'article:a', 'target': 'b', 'type': 'related'}]})
            self.assertEqual(len(result['nodes']), 2)
            self.assertEqual(result['edges'][0]['source'], 'a')

    def test_partial_extraction_failure_is_retryable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a, b = root / 'a.md', root / 'b.md'
            def fake_extract(title, body):
                if body == 'ok':
                    return extract.GDoc([], [])
                raise RuntimeError('SECRET')
            with patch.object(extract, 'WIKI_ROOT', root), \
                 patch.object(extract, 'STATE_PATH', root / 'state.json'), \
                 patch.object(extract, 'DISCOVERY_GRAPH_PATH', root / 'graph.json'), \
                 patch.object(extract, 'discover_files', return_value=[a, b]), \
                 patch.object(extract, 'pending_files', return_value=[(a, 'ok', 'good-hash'), (b, 'fail', 'bad-hash')]), \
                 patch.object(extract, 'extract_with_claude', side_effect=fake_extract), \
                 patch.object(extract, 'sync_to_neo4j', return_value=0), \
                 patch('sys.argv', ['extract', '--limit', '2']):
                self.assertEqual(extract.main(), 1)
                self.assertEqual(json.loads((root / 'state.json').read_text()), {'a.md': 'good-hash'})

    def test_parse_graph_json_validates_schema(self):
        text = 'noise ' + json.dumps({
            'nodes': [{'id': 'PX4', 'type': 'Technology'}, {'id': 'X', 'type': 'Bogus'},
                      {'id': 'MAVLink', 'type': 'Protocol'}],
            'relationships': [{'source': 'PX4', 'target': 'MAVLink', 'type': 'uses'},
                              {'source': 'PX4', 'target': 'X', 'type': 'USES'},
                              {'source': 'PX4', 'target': 'MAVLink', 'type': 'bad type!'}]}) + ' tail'
        gd = extract.parse_graph_json(text)
        self.assertEqual([n.id for n in gd.nodes], ['PX4', 'MAVLink'])
        self.assertEqual([(r.source.id, r.target.id, r.type) for r in gd.relationships], [('PX4', 'MAVLink', 'USES')])
        with self.assertRaises(ValueError):
            extract.parse_graph_json('no json here')

    def test_failure_log_never_echoes_exception_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a = root / 'a.md'
            with patch.object(extract, 'WIKI_ROOT', root), \
                 patch.object(extract, 'STATE_PATH', root / 'state.json'), \
                 patch.object(extract, 'DISCOVERY_GRAPH_PATH', root / 'graph.json'), \
                 patch.object(extract, 'discover_files', return_value=[a]), \
                 patch.object(extract, 'pending_files', return_value=[(a, 'x', 'h')]), \
                 patch.object(extract, 'extract_with_claude', side_effect=RuntimeError('SECRET-TOKEN')), \
                 patch('sys.argv', ['extract']), \
                 patch('sys.stderr') as err:
                extract.main()
            self.assertNotIn('SECRET', ''.join(str(c) for c in err.write.call_args_list))


if __name__ == '__main__':
    unittest.main()
