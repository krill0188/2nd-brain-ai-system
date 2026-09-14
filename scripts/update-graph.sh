#!/usr/bin/env bash
# Compatibility command: regenerate only the derived canonical graph.
# Legacy .ua/knowledge-graph.json is untouched; no raw/canonical/public writes.
set -euo pipefail
GRAPH_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec "$GRAPH_ROOT/.venv/bin/python" "$GRAPH_ROOT/scripts/build-canonical-graph.py" --write "$@"
