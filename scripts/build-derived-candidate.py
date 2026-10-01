#!/usr/bin/env python3
"""Rebuild derived .ua artifacts inside a final publication candidate from approved content only.

Run after Publish:reconcile-candidates:
    .venv/bin/python scripts/build-derived-candidate.py --candidate <final-candidate>
    .venv/bin/python scripts/build-derived-candidate.py --candidate <final-candidate> --verify-only

embeddings.json          vectors reused only when the candidate's own document bytes hash to the
                         same input_hash (live index + previous public copy are just vector pools)
discovery-knowledge-graph.json   live graph filtered to sources/evidence present in the candidate
drone-knowledge-graph.json       regenerated from candidate canonical docs
news-feed / daily-briefing   published from the source .ua/ only after schema + local-path validation
                         (public news metadata; invalid input keeps the retained public copy and warns)
self-update-state               published like the feeds (url -> {processedAt, matchedSlugs} only)
knowledge-graph                 left as retained public copy

Writes only inside the candidate directory. Never deploys, never pushes.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent


def load_script(filename: str):
    name = filename.replace('-', '_').removesuffix('.py')
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def candidate_files(candidate: Path) -> set[str]:
    return {
        str(p.relative_to(candidate))
        for p in candidate.rglob('*')
        if p.is_file() and not p.is_symlink()
    }


def read_json(path: Path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return None


def write_json_atomic(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix='.derived-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


LOCAL_PATH = re.compile(r'(?<![\w:/.~-])(?:/(?:Users|home|private|var|tmp)/|~/)|(?:^|\s)(?:inbox|research|innovations)/\S+\.md')
MAX_FEED_ITEMS = 5000
FEED_FILES = ('news-feed.json', 'daily-briefing.json', 'self-update-state.json')


def feed_problem(name: str, data) -> str | None:
    """Return why a feed artifact is unsafe/malformed, or None when it may be published."""
    if LOCAL_PATH.search(json.dumps(data, ensure_ascii=False)):
        return 'local or internal path string'
    if name == 'news-feed.json':
        if not isinstance(data, list) or not data or len(data) > MAX_FEED_ITEMS:
            return 'expected a non-empty list within the size limit'
        for item in data:
            if (not isinstance(item, dict) or not isinstance(item.get('title'), str)
                    or not str(item.get('url', '')).startswith(('http://', 'https://'))):
                return 'item without title or http(s) url'
    elif name == 'daily-briefing.json':
        if (not isinstance(data, dict) or not isinstance(data.get('date'), str)
                or not isinstance(data.get('cards'), list)
                or any(not isinstance(c, dict) or not isinstance(c.get('body'), str) for c in data['cards'])):
            return 'expected {date, cards:[{body}]}'
    elif name == 'self-update-state.json':
        if not isinstance(data, dict) or not data or len(data) > MAX_FEED_ITEMS:
            return 'expected a non-empty object within the size limit'
        for url, row in data.items():
            if (not url.startswith(('http://', 'https://')) or not isinstance(row, dict)
                    or set(row) != {'processedAt', 'matchedSlugs'}
                    or not isinstance(row['processedAt'], str)
                    or not isinstance(row['matchedSlugs'], list)
                    or any(not isinstance(x, str) for x in row['matchedSlugs'])):
                return 'entry is not url -> {processedAt, matchedSlugs}'
    return None


def publish_feeds(candidate: Path, source_ua: Path) -> dict:
    status = {}
    for name in FEED_FILES:
        data = read_json(source_ua / name)
        reason = 'source unreadable' if data is None else feed_problem(name, data)
        if reason:
            status[name] = f'kept-retained-copy ({reason})'
            print(f'WARNING: {name} not refreshed: {reason}', file=sys.stderr)
        else:
            write_json_atomic(candidate / '.ua' / name, data)
            status[name] = 'refreshed'
    return status


def candidate_embedding_inputs(candidate: Path) -> tuple[object, list[dict]]:
    embed = load_script('embed-docs.py')
    embed.WIKI_ROOT = candidate
    return embed, embed.collect_canonical() + embed.collect_raw() + embed.collect_news()


def cached_embedder(embed, cache_dir: Path):
    def run(texts: list[str]):
        from fastembed import TextEmbedding
        model = TextEmbedding(embed.MODEL_NAME, cache_dir=str(cache_dir), local_files_only=True, threads=2)
        return [[round(float(x), 6) for x in v] for v in model.embed(texts, batch_size=8)]
    return run


def build_embeddings(candidate: Path, pools: list[Path], embedder=None) -> dict:
    embed, docs = candidate_embedding_inputs(candidate)
    vectors: dict[str, list] = {}
    contract = None
    for pool in pools:
        data = read_json(pool)
        if not isinstance(data, dict):
            continue
        contract = contract or data.get('generation_contract')
        for row in data.get('docs', []):
            if row.get('input_hash') and len(row.get('vector', [])) == 768:
                vectors.setdefault(row['input_hash'], row['vector'])

    pending = [d for d in docs if embed.document_fingerprint(d) not in vectors]
    if pending and embedder:
        try:
            for doc, vector in zip(pending, embedder([d['text'] for d in pending])):
                if len(vector) == 768:
                    vectors[embed.document_fingerprint(doc)] = vector
        except Exception:
            pass

    rows, missing = [], 0
    for doc in docs:
        digest = embed.document_fingerprint(doc)
        if digest not in vectors:
            missing += 1
            continue
        rows.append({'kind': doc['kind'], 'layer': doc['layer'], 'slug': doc['slug'], 'path': doc['path'],
                     'title': doc['title'], 'input_hash': digest, 'vector': vectors[digest]})
    payload = {'version': 1, 'input_fingerprint': embed.input_fingerprint(docs)}
    if contract:
        payload['generation_contract'] = contract
    payload.update({'model': embed.MODEL_NAME, 'dim': 768 if rows else 0,
                    'created': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                    'doc_count': len(rows), 'docs': rows})
    return {'payload': payload, 'missing': missing}


def project_discovery(graph: dict, files: set[str]) -> dict:
    nodes, kept = [], set()
    for node in graph.get('nodes', []):
        sources = [s for s in node.get('sources', []) if s in files]
        if sources:
            nodes.append({**node, 'sources': sources})
            kept.add(node['id'])
    edges = []
    for edge in graph.get('edges', []):
        evidence = [e for e in edge.get('evidence', []) if e in files]
        if evidence and edge['source'] in kept and edge['target'] in kept:
            edges.append({**edge, 'evidence': evidence})
    return {**graph, 'nodes': nodes, 'edges': edges}


def build_drone_graph(candidate: Path) -> dict:
    module = load_script('build-canonical-graph.py')
    target = candidate / '.ua/drone-knowledge-graph.json'
    old = read_json(target) or {'nodes': [], 'edges': []}
    return module.reconcile(module.build(candidate), old)


def verify(candidate: Path) -> list[str]:
    problems: list[str] = []
    files = candidate_files(candidate)

    for name in FEED_FILES:
        data = read_json(candidate / '.ua' / name)
        reason = 'unreadable' if data is None else feed_problem(name, data)
        if reason:
            problems.append(f'{name}: {reason}')

    embeddings = read_json(candidate / '.ua/embeddings.json')
    if not isinstance(embeddings, dict):
        problems.append('embeddings unreadable')
    else:
        embed, docs = candidate_embedding_inputs(candidate)
        expected = {embed.document_fingerprint(d): d['path'] for d in docs}
        for row in embeddings.get('docs', []):
            if expected.get(row.get('input_hash')) != row.get('path'):
                problems.append(f"embedding not derived from candidate bytes: {row.get('path')}")

    graph = read_json(candidate / '.ua/discovery-knowledge-graph.json')
    if not isinstance(graph, dict):
        problems.append('discovery graph unreadable')
    else:
        ids = {n['id'] for n in graph.get('nodes', [])}
        for node in graph.get('nodes', []):
            for source in node.get('sources', []):
                if source not in files:
                    problems.append(f"discovery node {node['id']} cites unpublished {source}")
        for edge in graph.get('edges', []):
            if edge['source'] not in ids or edge['target'] not in ids:
                problems.append('discovery edge has missing endpoint')
            for evidence in edge.get('evidence', []):
                if evidence not in files:
                    problems.append(f'discovery edge cites unpublished {evidence}')

    drone = read_json(candidate / '.ua/drone-knowledge-graph.json')
    if not isinstance(drone, dict):
        problems.append('drone graph unreadable')
    else:
        canonical = load_script('build-canonical-graph.py').build(candidate)
        if drone.get('source_fingerprint') != canonical['source_fingerprint']:
            problems.append('drone graph not built from candidate canonical docs')
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--source-root', type=Path, default=ROOT)
    ap.add_argument('--verify-only', action='store_true')
    args = ap.parse_args()

    candidate = args.candidate.resolve()
    if not candidate.is_dir() or candidate == args.source_root.resolve():
        print('BLOCKED: --candidate must be an existing candidate directory, not the source root')
        return 2

    summary: dict = {}
    if not args.verify_only:
        live = args.source_root / '.ua'
        files = candidate_files(candidate)
        feeds = publish_feeds(candidate, live)
        embed = load_script('embed-docs.py')
        embeddings = build_embeddings(candidate, [live / 'embeddings.json', candidate / '.ua/embeddings.json'],
                                      cached_embedder(embed, args.source_root / '.ua/model-cache/fastembed'))
        write_json_atomic(candidate / '.ua/embeddings.json', embeddings['payload'])

        source_graph = read_json(live / 'discovery-knowledge-graph.json') or read_json(
            candidate / '.ua/discovery-knowledge-graph.json') or {'nodes': [], 'edges': []}
        discovery = project_discovery(source_graph, files)
        write_json_atomic(candidate / '.ua/discovery-knowledge-graph.json', discovery)

        drone = build_drone_graph(candidate)
        write_json_atomic(candidate / '.ua/drone-knowledge-graph.json', drone)
        summary = {'feeds': feeds, 'embeddings': embeddings['payload']['doc_count'], 'embeddings_missing': embeddings['missing'],
                   'discovery_nodes': len(discovery['nodes']), 'discovery_edges': len(discovery['edges']),
                   'drone_nodes': len(drone['nodes']), 'drone_edges': len(drone['edges'])}

    problems = verify(candidate)
    print(json.dumps({**summary, 'problems': len(problems)}))
    for line in problems[:20]:
        print('PROBLEM:', line, file=sys.stderr)
    return 1 if problems else 0


if __name__ == '__main__':
    raise SystemExit(main())
