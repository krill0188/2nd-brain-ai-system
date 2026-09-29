"""Derived artifact projection fixtures, isolated from real knowledge and the embedding model."""
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), HERE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


derived = load('build-derived-candidate')
embed = load('embed-docs')

CONCEPT = '---\ntitle: Alpha\ntags: [x]\ndomain: drone\n---\nAlpha body\n'


def vec(seed):
    return [seed] * 768


class DerivedCandidateTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        base = Path(temp.name)
        self.cand, self.live = base / 'candidate', base / 'live'
        (self.cand / 'concepts').mkdir(parents=True)
        (self.cand / 'ontology').mkdir()
        (self.cand / 'raw/articles').mkdir(parents=True)
        (self.cand / '.ua').mkdir()
        (self.live / '.ua').mkdir(parents=True)
        shutil.copy(HERE.parent / 'ontology/class-hierarchy.json', self.cand / 'ontology/class-hierarchy.json')
        (self.cand / 'concepts/alpha.md').write_text(CONCEPT)
        (self.cand / 'raw/articles/ok.md').write_text('---\ntitle: Ok\n---\nokay text\n')
        (self.cand / '.ua/news-feed.json').write_text('[]')

    def hashes(self):
        _, docs = derived.candidate_embedding_inputs(self.cand)
        return {d['path']: embed.document_fingerprint(d) for d in docs}

    def write_pool(self, rows):
        path = self.live / '.ua/embeddings.json'
        path.write_text(json.dumps({'docs': rows}))
        return path

    def run_main(self, *argv):
        old, sys.argv = sys.argv, ['x', *argv]
        try:
            return derived.main()
        finally:
            sys.argv = old

    def test_vectors_reused_only_for_matching_bytes(self):
        hashes = self.hashes()
        pool = self.write_pool([
            {'input_hash': hashes['concepts/alpha.md'], 'vector': vec(1.0)},
            {'input_hash': 'stale-hash-of-old-bytes', 'vector': vec(2.0)},
        ])
        result = derived.build_embeddings(self.cand, [pool])
        self.assertEqual([r['path'] for r in result['payload']['docs']], ['concepts/alpha.md'])
        self.assertEqual(result['missing'], 1)

    def test_pending_documents_use_embedder(self):
        seen = []

        def fake(texts):
            seen.extend(texts)
            return [vec(3.0) for _ in texts]

        result = derived.build_embeddings(self.cand, [], fake)
        self.assertEqual(result['missing'], 0)
        self.assertEqual(result['payload']['doc_count'], 2)
        self.assertEqual(len(seen), 2)

    def test_embedder_failure_leaves_documents_missing_not_stale(self):
        def broken(texts):
            raise RuntimeError('no model')

        result = derived.build_embeddings(self.cand, [], broken)
        self.assertEqual(result['payload']['doc_count'], 0)
        self.assertEqual(result['missing'], 2)

    def test_discovery_projection_drops_unpublished_sources(self):
        files = {'raw/articles/ok.md'}
        graph = {'nodes': [
            {'id': 'A', 'sources': ['raw/articles/ok.md', 'raw/articles/private.md']},
            {'id': 'B', 'sources': ['raw/articles/private.md']},
            {'id': 'C', 'sources': ['raw/articles/ok.md']},
        ], 'edges': [
            {'source': 'A', 'target': 'C', 'evidence': ['raw/articles/ok.md', 'raw/articles/private.md']},
            {'source': 'A', 'target': 'B', 'evidence': ['raw/articles/ok.md']},
            {'source': 'A', 'target': 'C', 'evidence': ['raw/articles/private.md']},
        ]}
        out = derived.project_discovery(graph, files)
        self.assertEqual([n['id'] for n in out['nodes']], ['A', 'C'])
        self.assertEqual(out['nodes'][0]['sources'], ['raw/articles/ok.md'])
        self.assertEqual(len(out['edges']), 1)
        self.assertEqual(out['edges'][0]['evidence'], ['raw/articles/ok.md'])

    def test_end_to_end_and_verify_detects_tampering(self):
        self.write_pool([{'input_hash': h, 'vector': vec(1.0)} for h in self.hashes().values()])
        (self.live / '.ua/discovery-knowledge-graph.json').write_text(json.dumps({
            'nodes': [{'id': 'A', 'sources': ['raw/articles/ok.md', 'raw/articles/private.md']}], 'edges': []}))
        derived.cached_embedder = lambda *a: None
        self.assertEqual(self.run_main('--candidate', str(self.cand), '--source-root', str(self.live)), 0)
        self.assertEqual(derived.verify(self.cand), [])

        path = self.cand / '.ua/discovery-knowledge-graph.json'
        graph = json.loads(path.read_text())
        self.assertEqual(graph['nodes'][0]['sources'], ['raw/articles/ok.md'])
        graph['nodes'][0]['sources'].append('raw/articles/private.md')
        path.write_text(json.dumps(graph))
        self.assertTrue(any('unpublished' in p for p in derived.verify(self.cand)))

        path = self.cand / '.ua/embeddings.json'
        emb = json.loads(path.read_text())
        emb['docs'][0]['input_hash'] = 'forged'
        path.write_text(json.dumps(emb))
        self.assertTrue(any('not derived' in p for p in derived.verify(self.cand)))

    def test_refuses_source_root_as_candidate(self):
        self.assertEqual(self.run_main('--candidate', str(self.live), '--source-root', str(self.live)), 2)


if __name__ == '__main__':
    unittest.main()
