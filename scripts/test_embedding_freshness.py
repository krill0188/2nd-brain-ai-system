"""Offline fixtures for freshness and failure-safe writes; no model execution."""
import importlib.util
import fcntl
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('embed_docs', Path(__file__).with_name('embed-docs.py'))
embed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(embed)


class EmbeddingTests(unittest.TestCase):
    def test_content_change_is_stale_and_corruption_rejected(self):
        docs = [{'path': 'concepts/a.md', 'text': 'old'}]
        fingerprint = embed.input_fingerprint(docs)
        with tempfile.TemporaryDirectory() as tmp, patch.object(embed, 'OUT_PATH', Path(tmp) / 'embeddings.json'):
            payload = {'input_fingerprint': fingerprint, 'model': embed.MODEL_NAME,
                       'generation_contract': embed.generation_contract(),
                       'dim': 768, 'doc_count': 1, 'docs': [{'path': docs[0]['path'], 'vector': [0.1] * 768}]}
            embed.atomic_write(payload)
            self.assertTrue(embed.artifact_is_fresh(docs, fingerprint))
            self.assertNotEqual(fingerprint, embed.input_fingerprint([{'path': docs[0]['path'], 'text': 'new'}]))
            payload['docs'][0]['vector'] = [0.1]
            embed.atomic_write(payload)
            self.assertFalse(embed.artifact_is_fresh(docs, fingerprint))

    def test_check_and_fresh_skip_do_not_load_model(self):
        docs = [{"path": "concepts/a.md", "text": "old"}]
        with patch.object(embed, 'collect_canonical', return_value=docs), \
             patch.object(embed, 'collect_raw', return_value=[]), \
             patch.object(embed, 'collect_news', return_value=[]), \
             patch.object(embed, 'artifact_is_fresh', return_value=True), \
             patch.dict('sys.modules', {'fastembed': None}):
            with patch('sys.argv', ['embed-docs.py', '--check']):
                self.assertEqual(embed.main(), 0)
            with patch('sys.argv', ['embed-docs.py', '--if-stale']):
                self.assertEqual(embed.main(), 0)

    def test_failed_atomic_write_preserves_previous_file(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(embed, 'OUT_PATH', Path(tmp) / 'embeddings.json'):
            embed.OUT_PATH.write_text('previous')
            with self.assertRaises(ValueError):
                embed.atomic_write({'bad': float('nan')})
            self.assertEqual(embed.OUT_PATH.read_text(), 'previous')
            self.assertEqual(list(Path(tmp).iterdir()), [embed.OUT_PATH])

    def test_changed_input_only_and_version_mismatch(self):
        a = {'path': 'raw/a.md', 'text': 'a', 'slug': 'a'}
        b = {'path': 'raw/b.md', 'text': 'b', 'slug': 'b'}
        with tempfile.TemporaryDirectory() as tmp, patch.object(embed, 'OUT_PATH', Path(tmp) / 'embeddings.json'):
            payload = {'generation_contract': embed.generation_contract(), 'docs': [
                {'input_hash': embed.document_fingerprint(d), 'vector': [0.1] * 768} for d in (a, b)]}
            embed.atomic_write(payload)
            cache = embed.reusable_vectors()
            self.assertIn(embed.document_fingerprint(a), cache)
            self.assertNotIn(embed.document_fingerprint({**b, 'text': 'changed'}), cache)
            payload['generation_contract'] = {'fastembed': 'different'}
            embed.atomic_write(payload)
            self.assertEqual(embed.reusable_vectors(), {})

    def test_concurrent_generation_is_rejected_before_model_work(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(embed, 'OUT_PATH', Path(tmp) / 'embeddings.json'):
            with embed.OUT_PATH.with_suffix('.lock').open('a') as lock:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                with patch.object(embed, 'generate') as generate, patch('sys.argv', ['embed-docs.py', '--if-stale']):
                    self.assertEqual(embed.main(), 2)
                    generate.assert_not_called()


if __name__ == '__main__':
    unittest.main()
