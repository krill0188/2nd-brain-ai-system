import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "reconcile-publication-candidates.py"
)

spec = importlib.util.spec_from_file_location(
    "publication_reconciliation",
    SCRIPT,
)
reconcile = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reconcile)


class PublicationReconciliationTests(unittest.TestCase):

    def test_exact_match_creates_final_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy = root / "policy"
            version = root / "version"
            output = root / "final"

            (policy / "concepts").mkdir(parents=True)
            (version / "concepts").mkdir(parents=True)

            (policy / "concepts/a.md").write_text("approved\n")
            (version / "concepts/a.md").write_text("approved\n")

            # Policy gate metadata is not public payload.
            (policy / "PUBLICATION-CANDIDATE.json").write_text("{}")

            report = reconcile.reconcile(policy, version, output)

            self.assertEqual(report["status"], "matched")
            self.assertEqual(report["file_count"], 1)
            self.assertEqual(
                (output / "concepts/a.md").read_text(),
                "approved\n",
            )
            self.assertFalse(
                (output / "PUBLICATION-CANDIDATE.json").exists()
            )

    def test_file_set_mismatch_is_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy = root / "policy"
            version = root / "version"
            output = root / "final"

            policy.mkdir()
            version.mkdir()

            (policy / "a.md").write_text("same")
            (version / "a.md").write_text("same")
            (version / "b.md").write_text("extra")

            with self.assertRaises(reconcile.ReconciliationError):
                reconcile.reconcile(policy, version, output)

            self.assertFalse(output.exists())

    def test_content_mismatch_is_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy = root / "policy"
            version = root / "version"
            output = root / "final"

            policy.mkdir()
            version.mkdir()

            (policy / "a.md").write_text("policy")
            (version / "a.md").write_text("version")

            with self.assertRaises(reconcile.ReconciliationError):
                reconcile.reconcile(policy, version, output)

            self.assertFalse(output.exists())

    def test_symlink_is_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy = root / "policy"
            version = root / "version"
            output = root / "final"

            policy.mkdir()
            version.mkdir()

            outside = root / "outside.txt"
            outside.write_text("secret")

            (policy / "a.md").symlink_to(outside)
            (version / "a.md").write_text("secret")

            with self.assertRaises(reconcile.ReconciliationError):
                reconcile.reconcile(policy, version, output)

            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
