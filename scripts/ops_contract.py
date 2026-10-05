#!/usr/bin/env python3
"""Shared operational contracts for the DroneWiki pipeline.

This module only writes under ``.ua/runs`` and ``.ua/revisions``. It never
modifies raw evidence, canonical pages, index.md, or log.md.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parent.parent
RUNS_ROOT = ROOT / ".ua" / "runs"
REVISIONS_ROOT = ROOT / ".ua" / "revisions"

STATES = (
    "DISCOVERED", "FETCHED", "HASH_VERIFIED", "QUEUED", "PROCESSING",
    "COMPILED", "LINT_PASSED", "PUBLISHED_CANDIDATE", "PUBLISHED",
    "BLOCKED", "FAILED",
)
TERMINAL_STATES = {"PUBLISHED", "BLOCKED", "FAILED"}
_RETRYABLE = re.compile(r"^(?:retryable_)?failed$", re.IGNORECASE)


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def new_run_id(job: str) -> str:
    safe = re.sub(r"[^a-z0-9._-]+", "-", job.lower()).strip("-") or "run"
    return f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{safe}-{uuid.uuid4().hex[:10]}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_paths() -> Iterable[Path]:
    for dirname in ("entities", "concepts", "comparisons", "queries"):
        root = ROOT / dirname
        if root.exists():
            yield from sorted(root.glob("*.md"))


def page_inventory() -> dict[str, str]:
    return {str(path.relative_to(ROOT)): sha256_file(path) for path in canonical_paths()}


def atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".tmp-{os.getpid()}")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def create_run(job: str, policy: str, **metadata: Any) -> tuple[str, Path]:
    run_id = new_run_id(job)
    directory = RUNS_ROOT / run_id
    directory.mkdir(parents=True, exist_ok=False)
    atomic_json(directory / "manifest.json", {
        "run_id": run_id, "job": job, "policy": policy,
        "status": "DISCOVERED", "started_at": now(), "finished_at": None,
        "metadata": metadata,
    })
    atomic_json(directory / "input-pages.json", page_inventory())
    atomic_json(directory / "results.json", [])
    return run_id, directory


def update_run(directory: Path, *, status: str | None = None,
               results: list[dict[str, Any]] | None = None, **fields: Any) -> None:
    manifest_path = directory / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if status is not None:
        if status not in STATES:
            raise ValueError(f"unknown state: {status}")
        manifest["status"] = status
        if status in TERMINAL_STATES:
            manifest["finished_at"] = now()
    manifest.update(fields)
    atomic_json(manifest_path, manifest)
    if results is not None:
        atomic_json(directory / "results.json", results)


def record_result(directory: Path, result: dict[str, Any]) -> None:
    path = directory / "results.json"
    current = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    current.append(result)
    atomic_json(path, current)


def write_revision(run_id: str, before: dict[str, str], after: dict[str, str], reason: str) -> Path:
    changed = []
    for page in sorted(set(before) | set(after)):
        if before.get(page) != after.get(page):
            changed.append({"path": page, "before_sha256": before.get(page), "after_sha256": after.get(page)})
    path = REVISIONS_ROOT / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{run_id}.json"
    atomic_json(path, {"run_id": run_id, "recorded_at": now(), "reason": reason, "changed": changed})
    return path


def validate_state(value: str) -> bool:
    return value in STATES
