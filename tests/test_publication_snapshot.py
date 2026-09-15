from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build-publication-snapshot.py"
spec = importlib.util.spec_from_file_location("publication_gate", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


def run(*args: str, cwd: Path | None = None) -> str:
    cp = subprocess.run(args, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return cp.stdout.strip()


def init_repo(path: Path) -> None:
    path.mkdir(parents=True)
    run("git", "init", "-q", cwd=path)
    run("git", "config", "user.email", "test@example.com", cwd=path)
    run("git", "config", "user.name", "Publication Test", cwd=path)


def commit_all(path: Path, message: str) -> str:
    run("git", "add", "-A", cwd=path)
    run("git", "commit", "-q", "-m", message, cwd=path)
    return run("git", "rev-parse", "HEAD", cwd=path)


class PublicationGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "source"
        self.web = self.root / "web"
        init_repo(self.source)
        init_repo(self.web)

        (self.source / "concepts").mkdir()
        (self.source / "raw" / "papers").mkdir(parents=True)
        (self.source / "concepts" / "a.md").write_text("approved v1\n", encoding="utf-8")
        (self.source / "raw" / "papers" / "p.md").write_text("paper v1\n", encoding="utf-8")
        self.source_v1 = commit_all(self.source, "source v1")

        (self.web / "data" / "wiki" / "concepts").mkdir(parents=True)
        (self.web / "data" / "wiki" / "raw" / "papers").mkdir(parents=True)
        (self.web / "data" / "wiki" / ".ua").mkdir(parents=True)
        (self.web / "data" / "wiki" / "concepts" / "a.md").write_text("approved v1\n", encoding="utf-8")
        (self.web / "data" / "wiki" / "raw" / "papers" / "p.md").write_text("paper v1\n", encoding="utf-8")
        (self.web / "data" / "wiki" / ".ua" / "news-feed.json").write_text("[]\n", encoding="utf-8")
        self.baseline = commit_all(self.web, "public baseline")

        self.manifest = self.root / "manifest.json"
        self.output = self.root / "snapshot"
        self.report = self.root / "report.json"
        self.write_manifest()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write_manifest(self, *, approved=None, revoked=None, roots=None) -> None:
        data = {
            "version": 1,
            "policy": "default-deny-content-version",
            "baseline": {
                "repository": "test/web",
                "commit": self.baseline,
                "prefix": "data/wiki"
            },
            "publication_roots": roots or ["concepts", "raw"],
            "derived_artifacts": [".ua/news-feed.json"],
            "approved_source_versions": approved or [],
            "revoked_paths": revoked or [],
        }
        self.manifest.write_text(json.dumps(data), encoding="utf-8")

    def build(self, dry_run=False):
        return mod.build_snapshot(
            source_root=self.source,
            baseline_repo=self.web,
            manifest_path=self.manifest,
            output=self.output,
            report_path=self.report,
            dry_run=dry_run,
        )

    def test_changed_source_does_not_replace_baseline(self):
        (self.source / "concepts" / "a.md").write_text("UNAPPROVED v2\n", encoding="utf-8")
        report = self.build()
        self.assertEqual((self.output / "concepts" / "a.md").read_text(), "approved v1\n")
        self.assertIn("concepts/a.md", report["pending_changed"])

    def test_new_source_file_is_denied_and_reported(self):
        (self.source / "concepts" / "new.md").write_text("secret-ish new content\n", encoding="utf-8")
        report = self.build()
        self.assertFalse((self.output / "concepts" / "new.md").exists())
        self.assertIn("concepts/new.md", report["pending_new"])

    def test_exact_source_commit_approval_publishes_reviewed_version(self):
        (self.source / "concepts" / "a.md").write_text("reviewed v2\n", encoding="utf-8")
        source_v2 = commit_all(self.source, "reviewed v2")
        self.write_manifest(approved=[{"path": "concepts/a.md", "source_commit": source_v2}])
        report = self.build()
        self.assertEqual((self.output / "concepts" / "a.md").read_text(), "reviewed v2\n")
        self.assertEqual(report["approved_source_version_count"], 1)
        self.assertNotIn("concepts/a.md", report["pending_changed"])

    def test_revocation_removes_baseline_path(self):
        self.write_manifest(revoked=["raw/papers/p.md"])
        report = self.build()
        self.assertFalse((self.output / "raw" / "papers" / "p.md").exists())
        self.assertEqual(report["revoked_count"], 1)

    def test_traversal_is_rejected(self):
        self.write_manifest(approved=[{"path": "../escape.md", "source_commit": self.source_v1}])
        with self.assertRaises(mod.PublicationError):
            self.build(dry_run=True)

    def test_unexpected_baseline_namespace_fails_closed(self):
        (self.web / "data" / "wiki" / "unexpected").mkdir(parents=True)
        (self.web / "data" / "wiki" / "unexpected" / "x.txt").write_text("x")
        self.baseline = commit_all(self.web, "unexpected namespace")
        self.write_manifest()
        with self.assertRaises(mod.PublicationError):
            self.build(dry_run=True)

    def test_source_symlink_in_publication_root_fails_closed(self):
        target = self.root / "outside.txt"
        target.write_text("outside")
        (self.source / "concepts" / "link.md").symlink_to(target)
        with self.assertRaises(mod.PublicationError):
            self.build(dry_run=True)


if __name__ == "__main__":
    unittest.main()
