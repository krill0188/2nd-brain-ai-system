#!/usr/bin/env python3
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pathlib import Path
from unittest.mock import patch

import ops_contract


class OpsContractTests(unittest.TestCase):
    def test_states_reject_unknown_values(self):
        self.assertTrue(ops_contract.validate_state("BLOCKED"))
        self.assertFalse(ops_contract.validate_state("SUCCEEDED"))

    def test_run_manifest_records_job_and_initial_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(ops_contract, "RUNS_ROOT", root / "runs"), \
                 patch.object(ops_contract, "REVISIONS_ROOT", root / "revisions"):
                run_id, directory = ops_contract.create_run("test-job", "contract-v1", source="fixture")
                manifest = json.loads((directory / "manifest.json").read_text())
                self.assertEqual(manifest["run_id"], run_id)
                self.assertEqual(manifest["status"], "DISCOVERED")
                self.assertIsNone(manifest["finished_at"])
                self.assertEqual(manifest["metadata"]["source"], "fixture")

    def test_revision_ledger_only_contains_changed_pages(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(ops_contract, "REVISIONS_ROOT", Path(tmp)):
                path = ops_contract.write_revision(
                    "run-1",
                    {"entities/a.md": "old", "entities/b.md": "same"},
                    {"entities/a.md": "new", "entities/b.md": "same"},
                    "test",
                )
                payload = json.loads(path.read_text())
                self.assertEqual([x["path"] for x in payload["changed"]], ["entities/a.md"])


if __name__ == "__main__":
    unittest.main()
