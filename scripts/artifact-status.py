#!/usr/bin/env python3
"""Read-only structural and coverage checks for generated graph artifacts."""
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    counts = Counter(p.stem for layer in ('concepts', 'entities', 'comparisons', 'queries')
                     for p in (ROOT / layer).rglob('*.md'))
    try:
        graph = json.loads((ROOT / '.ua/drone-knowledge-graph.json').read_text())
        discovery = json.loads((ROOT / '.ua/discovery-knowledge-graph.json').read_text())
        ids = {n['id'] for n in graph['nodes']}
        spec = importlib.util.spec_from_file_location('discovery_check', ROOT / 'scripts/extract-knowledge-graph.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # import only; no LLM/Neo4j calls
        pending = module.pending_files(module.discover_files(None), module.load_state())
        builder_spec = importlib.util.spec_from_file_location('canonical_check', ROOT / 'scripts/build-canonical-graph.py')
        builder = importlib.util.module_from_spec(builder_spec)
        builder_spec.loader.exec_module(builder)
        node_fresh = graph.get('source_fingerprint') == builder.build(ROOT)['source_fingerprint']
        report = {'canonical_documents': sum(counts.values()), 'canonical_unique_slugs': len(counts),
                  'duplicate_slugs': sum(n - 1 for n in counts.values()),
                  'canonical_nodes': len(graph['nodes']), 'canonical_edges': len(graph['edges']),
                  'missing_nodes': len(set(counts) - ids), 'extra_nodes': len(ids - set(counts)),
                  'discovery_nodes': len(discovery['nodes']), 'discovery_edges': len(discovery['edges']),
                  'discovery_pending_documents': len(pending),
                  'canonical_node_source_fresh': node_fresh,
                  'legacy_edges_pending_review': graph.get('legacy_edges_pending_review', 0),
                  'discovery_historical_extraction_success': 'UNKNOWN: old state predates failure-safe tracking'}
        print(json.dumps(report))
        return 2 if not node_fresh or any(report[k] for k in ('duplicate_slugs', 'missing_nodes', 'extra_nodes', 'discovery_pending_documents')) else 0
    except (OSError, ValueError, KeyError, TypeError):
        print('Graph artifact validation failed; no files changed')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
