#!/usr/bin/env python3
"""Build a default-deny public knowledge snapshot.

Stage 1 foundation behavior:
- The currently public DroneWiki Git commit is the immutable baseline.
- Baseline bytes are copied from that exact commit, not from the live ~/2nd tree.
- A changed/new source file is publishable only when the manifest approves an
  exact source Git commit for that path.
- Revocation is explicit.
- No source knowledge file is modified.

This script is intentionally NOT wired to production sync yet.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile
import uuid
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = REPO_ROOT / "publication" / "publication-manifest.json"
DEFAULT_OUTPUT = REPO_ROOT / ".ua" / "publication-snapshot"
DEFAULT_REPORT = REPO_ROOT / ".ua" / "publication-report.json"


class PublicationError(RuntimeError):
    pass


def git(repo: Path, *args: str) -> bytes:
    try:
        cp = subprocess.run(
            ["git", "-C", str(repo), *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = ""
        if isinstance(exc, subprocess.CalledProcessError):
            detail = exc.stderr.decode("utf-8", errors="replace").strip()
        raise PublicationError(f"git command failed in {repo}: {' '.join(args)}{': ' + detail if detail else ''}") from exc
    return cp.stdout


def require_full_sha(value: Any, field: str) -> str:
    if not isinstance(value, str) or len(value) != 40 or any(c not in "0123456789abcdefABCDEF" for c in value):
        raise PublicationError(f"{field} must be a full 40-character Git SHA")
    return value.lower()


def normalize_rel_path(value: Any, field: str = "path") -> str:
    if not isinstance(value, str) or not value:
        raise PublicationError(f"{field} must be a non-empty string")
    if "\\" in value or "\x00" in value:
        raise PublicationError(f"{field} contains an unsafe separator")
    p = PurePosixPath(value)
    if p.is_absolute() or any(part in ("", ".", "..") for part in p.parts):
        raise PublicationError(f"{field} must be a normalized relative POSIX path: {value}")
    normalized = p.as_posix()
    if normalized != value.strip("/") or value.startswith("/") or value.endswith("/"):
        raise PublicationError(f"{field} is not normalized: {value}")
    return normalized


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PublicationError(f"cannot read manifest {path}: {exc}") from exc
    if data.get("version") != 1:
        raise PublicationError("manifest version must be 1")
    if data.get("policy") != "default-deny-content-version":
        raise PublicationError("manifest policy must be default-deny-content-version")
    return data


def allowed_namespace(path: str, roots: set[str], derived: set[str]) -> bool:
    first = path.split("/", 1)[0]
    return first in roots or path in derived


def parse_tree_records(raw: bytes) -> list[tuple[str, str, str, str]]:
    out: list[tuple[str, str, str, str]] = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            meta, path_b = record.split(b"\t", 1)
            mode_b, type_b, oid_b = meta.split(b" ", 2)
            out.append((
                mode_b.decode("ascii"),
                type_b.decode("ascii"),
                oid_b.decode("ascii"),
                path_b.decode("utf-8"),
            ))
        except Exception as exc:
            raise PublicationError("unable to parse git ls-tree output") from exc
    return out


def ensure_commit(repo: Path, commit: str) -> None:
    git(repo, "cat-file", "-e", f"{commit}^{{commit}}")


def baseline_entries(repo: Path, commit: str, prefix: str, roots: set[str], derived: set[str]) -> dict[str, tuple[str, str]]:
    ensure_commit(repo, commit)
    prefix = normalize_rel_path(prefix, "baseline.prefix")
    raw = git(repo, "ls-tree", "-r", "-z", "--full-tree", commit, "--", prefix)
    entries: dict[str, tuple[str, str]] = {}
    prefix_slash = prefix + "/"
    for mode, obj_type, oid, full_path in parse_tree_records(raw):
        if obj_type != "blob":
            continue
        if not full_path.startswith(prefix_slash):
            raise PublicationError(f"baseline path escaped prefix: {full_path}")
        rel = normalize_rel_path(full_path[len(prefix_slash):], "baseline path")
        if not allowed_namespace(rel, roots, derived):
            raise PublicationError(f"baseline contains an unapproved namespace: {rel}")
        if mode == "120000":
            raise PublicationError(f"baseline contains a symlink: {rel}")
        entries[rel] = (mode, oid)
    if not entries:
        raise PublicationError("baseline contains no publishable files")
    return entries


def source_entry(repo: Path, commit: str, rel: str) -> tuple[str, str]:
    ensure_commit(repo, commit)
    raw = git(repo, "ls-tree", "-z", "--full-tree", commit, "--", rel)
    records = parse_tree_records(raw)
    exact = [r for r in records if r[3] == rel and r[1] == "blob"]
    if len(exact) != 1:
        raise PublicationError(f"approved source path not found as one blob at {commit}: {rel}")
    mode, _obj_type, oid, _path = exact[0]
    if mode == "120000":
        raise PublicationError(f"approved source path is a symlink: {rel}")
    return mode, oid


def git_blob_oid(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def resolve_baseline_repo(source_root: Path, explicit: Path | None) -> Path:
    candidates: list[Path] = []
    if explicit is not None:
        candidates.append(explicit)
    env = os.environ.get("DRONE_WIKI_REPO")
    if env:
        candidates.append(Path(env).expanduser())
    candidates.append(Path.home() / "projectm" / "drone-wiki-web")
    candidates.append(source_root.parent / "projectm" / "drone-wiki-web")
    for candidate in candidates:
        candidate = candidate.expanduser().resolve()
        if (candidate / ".git").exists():
            return candidate
    raise PublicationError(
        "DroneWiki baseline repository not found. Pass --baseline-repo or set DRONE_WIKI_REPO."
    )


def current_candidates(source_root: Path, roots: set[str], derived: set[str]) -> tuple[dict[str, str], list[str]]:
    found: dict[str, str] = {}
    unsafe: list[str] = []
    for root in sorted(roots):
        root_path = source_root / root
        if not root_path.exists():
            continue
        for path in root_path.rglob("*"):
            if path.is_symlink():
                unsafe.append(path.relative_to(source_root).as_posix())
                continue
            if not path.is_file():
                continue
            rel = path.relative_to(source_root).as_posix()
            found[rel] = git_blob_oid(path.read_bytes())
    for rel in sorted(derived):
        path = source_root / rel
        if path.is_symlink():
            unsafe.append(rel)
        elif path.is_file():
            found[rel] = git_blob_oid(path.read_bytes())
    return found, unsafe


def atomic_replace_dir(staging: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    backup = output.parent / f".{output.name}.backup-{uuid.uuid4().hex}"
    moved_old = False
    try:
        if output.exists():
            os.replace(output, backup)
            moved_old = True
        os.replace(staging, output)
    except Exception:
        if moved_old and backup.exists() and not output.exists():
            os.replace(backup, output)
        raise
    finally:
        if backup.exists():
            shutil.rmtree(backup, ignore_errors=True)


def build_snapshot(
    *,
    source_root: Path,
    baseline_repo: Path,
    manifest_path: Path,
    output: Path,
    report_path: Path,
    dry_run: bool = False,
) -> dict[str, Any]:
    source_root = source_root.resolve()
    baseline_repo = baseline_repo.resolve()
    manifest = load_manifest(manifest_path)

    roots_raw = manifest.get("publication_roots")
    derived_raw = manifest.get("derived_artifacts")
    if not isinstance(roots_raw, list) or not roots_raw:
        raise PublicationError("publication_roots must be a non-empty list")
    if not isinstance(derived_raw, list):
        raise PublicationError("derived_artifacts must be a list")
    roots = {normalize_rel_path(x, "publication_root") for x in roots_raw}
    if any("/" in r for r in roots):
        raise PublicationError("publication_roots must be top-level directories")
    derived = {normalize_rel_path(x, "derived_artifact") for x in derived_raw}

    baseline = manifest.get("baseline")
    if not isinstance(baseline, dict):
        raise PublicationError("baseline must be an object")
    baseline_commit = require_full_sha(baseline.get("commit"), "baseline.commit")
    baseline_prefix = normalize_rel_path(baseline.get("prefix"), "baseline.prefix")

    approved = manifest.get("approved_source_versions", [])
    revoked = manifest.get("revoked_paths", [])
    if not isinstance(approved, list) or not isinstance(revoked, list):
        raise PublicationError("approved_source_versions and revoked_paths must be lists")

    effective = baseline_entries(baseline_repo, baseline_commit, baseline_prefix, roots, derived)
    baseline_count = len(effective)
    approved_meta: dict[str, dict[str, str]] = {}

    for i, item in enumerate(approved):
        if not isinstance(item, dict):
            raise PublicationError(f"approved_source_versions[{i}] must be an object")
        rel = normalize_rel_path(item.get("path"), f"approved_source_versions[{i}].path")
        if not allowed_namespace(rel, roots, derived):
            raise PublicationError(f"approved path is outside publication namespaces: {rel}")
        if rel in derived:
            raise PublicationError(
                f"derived artifact cannot be approved from source Git in v1: {rel}; "
                "it must later be rebuilt from the approved snapshot"
            )
        commit = require_full_sha(item.get("source_commit"), f"approved_source_versions[{i}].source_commit")
        mode, oid = source_entry(source_root, commit, rel)
        effective[rel] = (mode, oid)
        approved_meta[rel] = {"source_commit": commit, "oid": oid}

    revoked_set: set[str] = set()
    for i, value in enumerate(revoked):
        rel = normalize_rel_path(value, f"revoked_paths[{i}]")
        revoked_set.add(rel)
        effective.pop(rel, None)

    current, unsafe = current_candidates(source_root, roots, derived)
    if unsafe:
        raise PublicationError("source publication namespaces contain symlinks: " + ", ".join(sorted(unsafe)))

    approved_oids = {path: oid for path, (_mode, oid) in effective.items()}
    pending_new = sorted(path for path in current if path not in approved_oids and path not in revoked_set)
    pending_changed = sorted(
        path for path, oid in current.items()
        if path in approved_oids and oid != approved_oids[path] and path not in revoked_set
    )
    baseline_only = sorted(path for path in approved_oids if path not in current)

    if not dry_run:
        output.parent.mkdir(parents=True, exist_ok=True)
        temp_parent = Path(tempfile.mkdtemp(prefix=".publication-build-", dir=output.parent))
        staging = temp_parent / "snapshot"
        staging.mkdir()
        try:
            base_entries = baseline_entries(baseline_repo, baseline_commit, baseline_prefix, roots, derived)
            for rel in sorted(effective):
                _mode, oid = effective[rel]
                data: bytes
                if rel in approved_meta:
                    data = git(source_root, "cat-file", "blob", oid)
                else:
                    # If the path came from baseline, preserve the exact public bytes.
                    base = base_entries.get(rel)
                    if base is None:
                        raise PublicationError(f"effective path has no byte source: {rel}")
                    data = git(baseline_repo, "cat-file", "blob", base[1])
                target = staging / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            atomic_replace_dir(staging, output)
        finally:
            shutil.rmtree(temp_parent, ignore_errors=True)

    report = {
        "version": 1,
        "policy": manifest["policy"],
        "baseline_commit": baseline_commit,
        "baseline_prefix": baseline_prefix,
        "baseline_file_count": baseline_count,
        "published_file_count": len(effective),
        "approved_source_version_count": len(approved_meta),
        "revoked_count": len(revoked_set),
        "pending_new_count": len(pending_new),
        "pending_changed_count": len(pending_changed),
        "baseline_only_count": len(baseline_only),
        "pending_new": pending_new,
        "pending_changed": pending_changed,
        "baseline_only": baseline_only,
        "dry_run": dry_run,
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--baseline-repo", type=Path)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--dry-run", action="store_true", help="Validate and report without replacing the snapshot")
    parser.add_argument("--strict", action="store_true", help="Return exit code 3 when unapproved current changes exist")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        baseline_repo = resolve_baseline_repo(args.source_root.resolve(), args.baseline_repo)
        report = build_snapshot(
            source_root=args.source_root,
            baseline_repo=baseline_repo,
            manifest_path=args.manifest,
            output=args.output,
            report_path=args.report,
            dry_run=args.dry_run,
        )
    except PublicationError as exc:
        print(f"PUBLICATION GATE ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.strict and (report["pending_new_count"] or report["pending_changed_count"]):
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
