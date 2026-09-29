#!/usr/bin/env bash
# extract-knowledge-graph.sh — extract-knowledge-graph.py 실행 래퍼.
# raw/ 원시 문서에서 Claude(claude -p) 기반으로 개념(Entity)·관계(Relation)를 자동
# 추출해 .ua/discovery-knowledge-graph.json에 쌓는다(canonical 그래프와 분리된
# 사람 검토 대기 레이어). NEO4J_PASSWORD가 설정돼 있으면 로컬 Neo4j에도 동기화.
#
# 사용법:
#   scripts/extract-knowledge-graph.sh                    # 기본 8개 신규 문서 처리
#   scripts/extract-knowledge-graph.sh --limit 20          # 더 많이 처리
#   scripts/extract-knowledge-graph.sh --source raw/papers # 특정 소스만
#   scripts/extract-knowledge-graph.sh --dry-run           # 저장 없이 추출만 확인
set -euo pipefail
export PATH="$HOME/.local/bin:/usr/local/bin:$PATH"

WIKI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$WIKI_ROOT"

# LLM 추출은 Claude Pro 구독(claude -p)으로 수행한다. API 키/외부 .env 의존 없음.

exec .venv/bin/python scripts/extract-knowledge-graph.py "$@"
