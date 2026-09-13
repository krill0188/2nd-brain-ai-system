#!/usr/bin/env python3
"""Sequential local pipeline candidate. Default is plan-only; never deploys.

Install schedule only after retiring overlapping legacy calendar triggers together.
--run-local invokes existing generation tools and therefore is intentionally opt-in.
"""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = Path.home() / 'projectm/drone-wiki-web'


def source_fingerprint() -> str:
    h = hashlib.sha256()
    for layer in ('concepts', 'entities', 'comparisons', 'queries', 'raw', 'ontology'):
        for p in sorted((ROOT / layer).rglob('*')):
            if p.is_file() and not p.is_symlink() and p.suffix in ('.md', '.json'):
                h.update(str(p.relative_to(ROOT)).encode())
                h.update(p.read_bytes())
    return h.hexdigest()


def steps(candidate: Path) -> list[tuple[str, list[str]]]:
    py = str(ROOT / '.venv/bin/python')
    return [
        ('Generate:fetch', ['bash', str(ROOT / 'scripts/fetch-inbox.sh')]),
        ('Generate:ingest', ['bash', str(ROOT / 'scripts/daily-ingest-claude.sh')]),
        ('Generate:self-update-canonical', [str(WEB / 'node_modules/.bin/tsx'), str(WEB / 'scripts/self-update-pipeline.ts'), '--apply']),
        ('Validate:canonical-lint-before-generation', ['python3', str(ROOT / 'scripts/lint-knowledge.py'), '--full']),
        ('Generate:embeddings', [py, str(ROOT / 'scripts/embed-docs.py'), '--if-stale']),
        ('Generate:discovery', ['bash', str(ROOT / 'scripts/extract-knowledge-graph.sh'), '--limit', '15']),
        ('Generate:canonical-graph', ['bash', str(ROOT / 'scripts/update-graph.sh')]),
        ('Validate:all', ['python3', str(ROOT / 'scripts/publication-preflight.py')]),
        ('Publish:isolated-candidate', ['python3', str(ROOT / 'scripts/publication-gate.py'), '--stage', str(candidate)]),
    ]


def run_steps(items, execute=subprocess.run) -> list[dict]:
    results = []
    for name, command in items:
        result = execute(command, cwd=WEB, capture_output=True, timeout=7200)
        results.append({'step': name, 'exit_code': result.returncode})
        if result.returncode:
            break
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-local', action='store_true')
    parser.add_argument('--candidate', type=Path)
    args = parser.parse_args()
    candidate = args.candidate or Path('/tmp/dronewiki-reviewed-candidate')
    plan = steps(candidate)
    if not args.run_local:
        print(json.dumps({'steps': [name for name, _ in plan], 'Deploy': 'manual approval required',
                          'Report': 'local .ua/pipeline-result.json; no messages',
                          'activation': 'NOT ACTIVE; replace overlapping launchd triggers before running'}, indent=2))
        return 0
    # Fail closed while legacy independent generators are installed. A new lock alone
    # cannot coordinate old jobs that do not share that lock.
    labels = ('daily-fetch', 'daily-ingest', 'dronewiki-self-update', 'lint-knowledge',
              'extract-knowledge-graph', 'update-knowledge-graph', 'apply-kinetic-rules', 'sync-dronewiki')
    for label in labels:
        if subprocess.run(['launchctl', 'list', 'ai.2nd.' + label], capture_output=True).returncode == 0:
            print('BLOCKED: overlapping legacy launchd jobs remain loaded; schedule migration required')
            return 2
    if not args.candidate or candidate.exists() or any(
        candidate.resolve().is_relative_to(p.resolve()) or p.resolve().is_relative_to(candidate.resolve())
        for p in (ROOT, WEB)
    ):
        print('BLOCKED: provide a new isolated --candidate directory')
        return 2
    lock_path = ROOT / '.ua/knowledge-pipeline.lock'
    lock_path.parent.mkdir(exist_ok=True)
    with lock_path.open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('BLOCKED: another pipeline is running')
            return 2
        results = []
        try:
            # Ingest may change source; freeze its fingerprint after lint.
            results = run_steps(plan[:4])
            before = source_fingerprint()
            if all(r['exit_code'] == 0 for r in results):
                results += run_steps(plan[4:-1])
            if source_fingerprint() != before:
                results.append({'step': 'Validate:source-stability', 'exit_code': 2})
            if all(r['exit_code'] == 0 for r in results):
                results += run_steps(plan[-1:])
        except (OSError, subprocess.TimeoutExpired):
            results.append({'step': 'execution-error', 'exit_code': 124})
        report = {'at': datetime.now(timezone.utc).isoformat(), 'steps': results,
                  'deploy': 'NOT EXECUTED: approval required'}
        (ROOT / '.ua/pipeline-result.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps(report))
        return 0 if results and all(r['exit_code'] == 0 for r in results) else 2


if __name__ == '__main__':
    raise SystemExit(main())
