#!/usr/bin/env bash
# research-promote.sh — G3 승격 bash 래퍼 (실제 로직은 research-promote.py)
#
# 사용법:
#   scripts/research-promote.sh <session-id> --approve --items H1,H3
#   scripts/research-promote.sh <session-id> --reject "사유"
#
# 계약: research/RESEARCH_SCHEMA.md § Promotion rules (G3)
# raw/ 파일은 절대 건드리지 않는다. 검증 실패 시 canonical/index.md/log.md
# 어디에도 쓰지 않는다(전체 중단, 부분 기록 없음).

set -euo pipefail

WIKI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

exec python3 "$WIKI_ROOT/scripts/research-promote.py" "$@"
