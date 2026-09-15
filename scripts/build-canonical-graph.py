#!/usr/bin/env python3
"""Rebuild only the derived canonical graph from current source documents.

Default is a read-only impact report. --write atomically replaces the local artifact.
Raw evidence, canonical documents, the legacy graph and public snapshot are untouched.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import yaml
from graph_lib import extract_links_by_section, ontology_class_for_domain

ROOT = Path(__file__).resolve().parent.parent
LAYERS = ('concepts', 'entities', 'comparisons', 'queries')


def build(root: Path) -> dict:
    classes = json.loads((root / 'ontology/class-hierarchy.json').read_text())['classes']
    docs = {}
    fingerprint = hashlib.sha256()
    for layer in LAYERS:
        for p in sorted((root / layer).rglob('*.md')):
            if p.is_symlink():
                raise ValueError('symlink canonical source')
            if p.stem in docs:
                raise ValueError('duplicate canonical slug')
            text = p.read_text()
            parts = text.split('\n---', 1)
            fm = yaml.safe_load(parts[0][4:]) if text.startswith('---\n') and len(parts) == 2 else None
            if not isinstance(fm, dict) or not fm.get('title'):
                raise ValueError('invalid canonical frontmatter')
            fingerprint.update(str(p.relative_to(root)).encode() + b'\0' + text.encode())
            docs[p.stem] = (layer, text, fm)
    fingerprint.update((root / 'ontology/class-hierarchy.json').read_bytes())
    nodes, edges = [], {}
    for slug, (layer, text, fm) in docs.items():
        explicit = fm.get('ontology_class')
        confidence = fm.get('confidence', '')
        sources = fm.get('sources', []) if isinstance(fm.get('sources'), list) else []
        nodes.append({'id': slug, 'name': str(fm['title']), 'layer': layer.capitalize(),
                      'domain': fm.get('domain', ''), 'tags': fm.get('tags', []) if isinstance(fm.get('tags'), list) else [],
                      'updated': str(fm.get('updated', fm.get('created', ''))),
                      'confidence': confidence if confidence in ('low', 'medium', 'high') else '',
                      'status': 'canonical', 'ontologyClass': explicit if explicit in classes else ontology_class_for_domain(fm.get('domain', ''))})
        links = extract_links_by_section(text)
        links += [(target, 'contradicts') for target in fm.get('contradictions', [])] if isinstance(fm.get('contradictions'), list) else []
        for target, kind in links:
            target = str(target).split('#', 1)[0].removesuffix('.md').rsplit('/', 1)[-1]
            if target not in docs or target == slug:
                continue
            edges[(slug, target, kind)] = {'source': slug, 'target': target, 'type': kind,
                                         'evidence': sources[:1], 'confidence': confidence}
    return {'version': 2, 'source_fingerprint': fingerprint.hexdigest(), 'nodes': nodes, 'edges': list(edges.values())}


def write_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix='.canonical-graph-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def reconcile(candidate: dict, old: dict) -> dict:
    """Retain existing valid-endpoint relationships until their provenance is reviewed."""
    ids = {n['id'] for n in candidate['nodes']}
    keys = {(e['source'], e['target'], e.get('type', 'wikilink')) for e in candidate['edges']}
    kept = 0
    for edge in old.get('edges', []):
        edge = dict(edge)
        for endpoint in ('source', 'target'):
            value = edge[endpoint]
            if value.startswith('article:'):
                slug = value.split(':', 1)[1].rsplit('/', 1)[-1]
                if slug in ids:
                    edge[endpoint] = slug
        key = (edge['source'], edge['target'], edge.get('type', 'wikilink'))
        if edge['source'] in ids and edge['target'] in ids and key not in keys:
            candidate['edges'].append({**edge, 'review_status': 'legacy-source-review-required'})
            keys.add(key)
            kept += 1
    candidate['edge_policy'] = 'retain-existing-valid-endpoints'
    candidate['legacy_edges_pending_review'] = kept
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    try:
        candidate = build(args.root)
        path = args.root / '.ua/drone-knowledge-graph.json'
        old = json.loads(path.read_text()) if path.exists() else {'nodes': [], 'edges': []}
        legacy = args.root / '.ua/knowledge-graph.json'
        if not path.exists() and legacy.exists():
            previous = json.loads(legacy.read_text())
            canonical_ids = {n['id'] for n in previous.get('nodes', []) if 'ontologyClass' in n}
            old = {'nodes': [n for n in previous.get('nodes', []) if n['id'] in canonical_ids],
                   'edges': [e for e in previous.get('edges', [])
                             if e['source'] in canonical_ids and e['target'] in canonical_ids]}
        candidate = reconcile(candidate, old)
        old_ids = {n['id'] for n in old['nodes']}
        new_ids = {n['id'] for n in candidate['nodes']}
        print(json.dumps({'mode': 'write' if args.write else 'audit', 'nodes': len(new_ids),
                          'edges': len(candidate['edges']), 'removed_nodes': len(old_ids - new_ids),
                          'previous_edges': len(old['edges']), 'legacy_edges_pending_review': candidate['legacy_edges_pending_review'],
                          'source_fingerprint': candidate['source_fingerprint']}))
        if args.write and any(old.get(k) != candidate[k] for k in candidate):
            candidate['generated_at'] = datetime.now(timezone.utc).isoformat()
            write_atomic(path, candidate)
        return 0
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError):
        print('canonical graph validation failed; previous artifact preserved')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
