#!/usr/bin/env python3
"""Create a final publication candidate only when both publication gates agree exactly."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import tempfile
from pathlib import Path


POLICY_METADATA = {"PUBLICATION-CANDIDATE.json"}


class ReconciliationError(RuntimeError):
    pass


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def payload(root: Path, *, ignore: set[str] | None = None) -> dict[str, str]:
    ignore = ignore or set()

    if not root.is_dir() or root.is_symlink():
        raise ReconciliationError(f"candidate is not a safe directory: {root}")

    result: dict[str, str] = {}

    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root).as_posix()

        if path.is_symlink():
            raise ReconciliationError(f"symlink rejected: {rel}")

        if path.is_dir():
            continue

        if not path.is_file():
            raise ReconciliationError(f"non-regular file rejected: {rel}")

        if rel in ignore:
            continue

        result[rel] = digest(path)

    return result


def ensure_isolated(target: Path, candidates: tuple[Path, ...]) -> None:
    resolved_target = target.resolve()

    if target.exists():
        raise ReconciliationError("final candidate already exists")

    for candidate in candidates:
        resolved_candidate = candidate.resolve()
        if (
            resolved_target.is_relative_to(resolved_candidate)
            or resolved_candidate.is_relative_to(resolved_target)
        ):
            raise ReconciliationError("final candidate must be isolated")


def reconcile(policy_candidate: Path, version_candidate: Path, output: Path) -> dict:
    policy_candidate = policy_candidate.resolve()
    version_candidate = version_candidate.resolve()
    output = output.resolve()

    ensure_isolated(output, (policy_candidate, version_candidate))

    policy_before = payload(policy_candidate, ignore=POLICY_METADATA)
    version_before = payload(version_candidate)

    if policy_before.keys() != version_before.keys():
        only_policy = sorted(policy_before.keys() - version_before.keys())
        only_version = sorted(version_before.keys() - policy_before.keys())
        raise ReconciliationError(
            "candidate file sets differ: "
            f"policy_only={only_policy[:10]} version_only={only_version[:10]}"
        )

    mismatched = sorted(
        path
        for path in policy_before
        if policy_before[path] != version_before[path]
    )
    if mismatched:
        raise ReconciliationError(
            f"candidate content differs: {mismatched[:10]}"
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(
        tempfile.mkdtemp(
            prefix=f".{output.name}.reconcile-",
            dir=output.parent,
        )
    )

    try:
        for rel, expected_hash in version_before.items():
            source = version_candidate / rel

            if source.is_symlink() or not source.is_file():
                raise ReconciliationError(
                    f"version candidate changed during reconciliation: {rel}"
                )

            if digest(source) != expected_hash:
                raise ReconciliationError(
                    f"version candidate changed during reconciliation: {rel}"
                )

            destination = staging / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

            if digest(destination) != expected_hash:
                raise ReconciliationError(
                    f"copied candidate failed verification: {rel}"
                )

        # Re-check both gate outputs before final promotion.
        policy_after = payload(policy_candidate, ignore=POLICY_METADATA)
        version_after = payload(version_candidate)

        if policy_after != policy_before or version_after != version_before:
            raise ReconciliationError(
                "candidate changed during reconciliation"
            )

        final_payload = payload(staging)

        if final_payload != version_before:
            raise ReconciliationError(
                "final candidate verification failed"
            )

        os.replace(staging, output)

        return {
            "status": "matched",
            "file_count": len(version_before),
            "output": str(output),
        }

    except Exception:
        if staging.exists():
            shutil.rmtree(staging)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy-candidate", type=Path, required=True)
    parser.add_argument("--version-candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    try:
        report = reconcile(
            args.policy_candidate,
            args.version_candidate,
            args.output,
        )
    except (OSError, ReconciliationError) as exc:
        print(json.dumps({
            "status": "blocked",
            "reason": str(exc),
        }))
        return 2

    print(json.dumps(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
