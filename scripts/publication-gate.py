#!/usr/bin/env python3
"""Audit publication policy; optionally create a separate, non-deployable candidate.

Never modifies knowledge, the existing public snapshot, policy, Git or deployment.
Existing snapshot hashes authorize retention only. New bytes need explicit policy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parent.parent
LAYERS = ('concepts', 'entities', 'comparisons', 'queries', 'raw', 'ontology', '.ua')
ARTIFACTS = {'.ua/' + name for name in (
    'embeddings.json', 'drone-knowledge-graph.json', 'discovery-knowledge-graph.json',
    'news-feed.json', 'daily-briefing.json')}
HARD_DENY = ('research/', 'inbox/', 'innovations/', 'raw/career-quiz/', 'raw/papers/files/')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_relative(name: str) -> bool:
    p = PurePosixPath(name)
    return bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name


def regular(root: Path, name: str) -> bool:
    p = root / name
    return (safe_relative(name) and p.is_file() and
            all(not root.joinpath(*PurePosixPath(name).parts[:i]).is_symlink()
                for i in range(1, len(PurePosixPath(name).parts) + 1)) and
            p.resolve().is_relative_to(root.resolve()))


def metadata_decision(path: Path) -> str | None:
    if path.suffix != '.md':
        return None
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        return None
    parts = text.split('\n---', 1)
    if len(parts) != 2:
        return 'invalid-metadata'
    try:
        # Reject duplicate metadata keys instead of silently accepting last value.
        class UniqueLoader(yaml.SafeLoader):
            pass
        def mapping(loader, node):
            result = {}
            for key, value in node.value:
                k = loader.construct_object(key)
                if k in result:
                    raise ValueError('duplicate key')
                result[k] = loader.construct_object(value)
            return result
        UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
        fm = yaml.load(parts[0][4:], Loader=UniqueLoader)
    except (yaml.YAMLError, ValueError, TypeError):
        return 'invalid-metadata'
    if not isinstance(fm, dict):
        return 'invalid-metadata'
    found = False
    for key in ('visibility', 'classification', 'publication_status', 'publish_to_web'):
        if key not in fm:
            continue
        found = True
        value = str(fm[key]).lower().strip()
        if value in ('private', 'internal', 'restricted', 'false', 'no', 'deny', 'draft'):
            return 'explicit-deny'
        allowed = ('true', 'yes') if key == 'publish_to_web' else (
            ('public', 'published') if key == 'publication_status' else ('public',))
        if value not in allowed:
            return 'unrecognized-metadata'
    return 'explicit-public' if found else None


def directory_rule(name: str, policy: dict) -> str:
    matches = [(len(prefix), value) for prefix, value in policy['directories'].items()
               if name.startswith(prefix)]
    return max(matches)[1] if matches else policy['default']


def audit(source: Path, snapshot: Path, policy: dict) -> dict:
    if policy.get('version') != 1 or policy.get('default') != 'review':
        raise ValueError('unsupported policy')
    for name, mode in policy['directories'].items():
        if not safe_relative(name) or not name.endswith('/') or mode not in ('public', 'review', 'deny'):
            raise ValueError('invalid directory policy')
    baseline = policy['baseline']['files']
    for name in [*baseline, *policy['approved_files']]:
        if not safe_relative(name):
            raise ValueError('unsafe policy path')
    names = set(baseline)
    snapshot_extras = {p.relative_to(snapshot).as_posix() for p in snapshot.rglob('*')
                       if (p.is_file() or p.is_symlink()) and p.relative_to(snapshot).as_posix() not in baseline}
    names.update(snapshot_extras)
    for layer in LAYERS:
        for p in (source / layer).rglob('*'):
            rel = p.relative_to(source).as_posix()
            if p.is_symlink() or (p.is_file() and ((p.suffix == '.md' and layer != '.ua') or rel in ARTIFACTS or layer == 'ontology')):
                names.add(rel)
    rows = []
    for name in sorted(names):
        src = source / name
        present = name in baseline
        action, reason = 'hold', 'unapproved-new-or-changed'
        source_hash = None
        if name in snapshot_extras:
            action, reason = 'block', 'unreviewed-snapshot-extra'
        elif present and (not regular(snapshot, name) or digest(snapshot / name) != baseline[name]):
            action, reason = 'block', 'baseline-snapshot-drift'
        elif not safe_relative(name) or src.is_symlink():
            action, reason = 'block', 'unsafe-path'
        elif (any(part.startswith('.env') or part in ('.git', '.venv', 'node_modules')
                  for part in PurePosixPath(name).parts)
              or Path(name).suffix.lower() in ('.pem', '.key', '.p12')):
            action, reason = ('block' if present else 'exclude'), 'credential-file-policy'
        elif name.startswith(HARD_DENY) or directory_rule(name, policy) == 'deny':
            action, reason = ('block' if present else 'exclude'), 'directory-deny'
        elif not src.exists():
            action, reason = ('retain' if present else 'exclude'), 'source-missing-no-delete'
        elif not regular(source, name):
            action, reason = 'block', 'unsafe-path'
        else:
            source_hash = digest(src)
            decision = metadata_decision(src)
            if decision in ('explicit-deny', 'invalid-metadata', 'unrecognized-metadata'):
                action, reason = ('block' if present else 'exclude'), decision
            elif present and source_hash == baseline[name]:
                action, reason = 'retain', 'baseline-identical'
            elif policy['approved_files'].get(name) == source_hash:
                action, reason = 'approve', 'explicit-file-sha256'
            elif src.suffix == '.md' and (decision == 'explicit-public' or directory_rule(name, policy) == 'public'):
                action, reason = 'approve', 'explicit-document-or-directory'
        row = {'path': name, 'action': action, 'reason': reason}
        if action == 'retain':
            row['sha256'] = baseline[name]
        elif action == 'approve':
            row['sha256'] = source_hash
        if source_hash is not None and digest(src) != source_hash:
            row.update(action='block', reason='source-changed-during-audit')
        rows.append(row)
    # Derived payloads contain titles/text/provenance too: no automatic bulk copy.
    # Even explicitly reviewed artifact hashes cannot bypass unapproved source bytes.
    held = any(r['action'] in ('hold', 'block', 'exclude') and r['path'].endswith('.md') and
               not r['path'].startswith(HARD_DENY) for r in rows)
    if held:
        for row in rows:
            if row['path'] in ARTIFACTS and row['action'] == 'approve':
                row.update(action='block', reason='derived-source-review-required')
    counts = dict(Counter(r['action'] for r in rows))
    return {'mode': 'audit', 'counts': counts, 'deletions': 0,
            'ready': not any(r['action'] in ('block', 'hold') for r in rows), 'files': rows}


def stage(source: Path, snapshot: Path, target: Path, report: dict) -> None:
    target = target.resolve()
    if target.exists() or any(target.is_relative_to(p.resolve()) or p.resolve().is_relative_to(target)
                              for p in (source, snapshot)):
        raise ValueError('candidate must be a new directory outside source and snapshot')
    if not report['ready']:
        raise ValueError('publication review unresolved; candidate not created')
    target.mkdir(parents=True)
    try:
        for row in report['files']:
            if row['action'] not in ('approve', 'retain'):
                continue
            origin = source if row['action'] == 'approve' else snapshot
            if not regular(origin, row['path']) or digest(origin / row['path']) != row['sha256']:
                raise ValueError('input changed after audit')
            dst = target / row['path']
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(origin / row['path'], dst)
            if digest(dst) != row['sha256']:
                raise ValueError('input changed during copy')
        (target / 'PUBLICATION-CANDIDATE.json').write_text(json.dumps(report, indent=2) + '\n')
    except Exception:
        shutil.rmtree(target)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT)
    parser.add_argument('--snapshot', type=Path, default=Path.home() / 'projectm/drone-wiki-web/data/wiki')
    parser.add_argument('--policy', type=Path, default=ROOT / 'publication/policy.json')
    parser.add_argument('--report', type=Path)
    parser.add_argument('--stage', type=Path)
    args = parser.parse_args()
    try:
        report = audit(args.source, args.snapshot, json.loads(args.policy.read_text()))
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({k: v for k, v in report.items() if k != 'files'}))
        if args.stage:
            stage(args.source, args.snapshot, args.stage, report)
        return 0 if report['ready'] else 2
    except (ValueError, OSError):
        print('publication gate failed; source/snapshot unchanged')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
