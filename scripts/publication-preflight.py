#!/usr/bin/env python3
"""Read-only fail-closed validation. Never generates, publishes, deploys or notifies."""
from __future__ import annotations
import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, default=ROOT / '.ua/publication-preflight.json')
    args = parser.parse_args()
    python = str(ROOT / '.venv/bin/python')
    steps = [
        ('canonical-lint', ['python3', str(ROOT / 'scripts/lint-knowledge.py'), '--full']),
        ('kinetic-static-check', [python, str(ROOT / 'scripts/apply-kinetic-rules.py'), '--check']),
        ('embeddings-freshness', [python, str(ROOT / 'scripts/embed-docs.py'), '--check']),
        ('graph-coverage', [python, str(ROOT / 'scripts/artifact-status.py')]),
        ('publication-policy', [python, str(ROOT / 'scripts/publication-gate.py')]),
    ]
    results = []
    for name, command in steps:
        start = time.monotonic()
        try:
            result = subprocess.run(command, capture_output=True, timeout=120)
            code = result.returncode
        except (OSError, subprocess.TimeoutExpired):
            code = 124
        # Never forward arbitrary child output (could contain source text or secrets).
        results.append({'step': name, 'exit_code': code, 'seconds': round(time.monotonic() - start, 2)})
    report = {'checked_at': datetime.now(timezone.utc).isoformat(), 'steps': results,
              'validation_passed': all(row['exit_code'] == 0 for row in results),
              'publish': 'NOT EXECUTED', 'deploy': 'APPROVAL REQUIRED',
              'ordering': 'UNVERIFIED: legacy independent schedules remain loaded'}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))
    return 0 if report['validation_passed'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
