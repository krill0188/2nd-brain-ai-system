#!/usr/bin/env bash
# Compatibility command: regenerate only the derived canonical graph.
# Legacy .ua/knowledge-graph.json is untouched; no raw/canonical/public writes.
set -euo pipefail
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/build-canonical-graph.py" --write "$@"
