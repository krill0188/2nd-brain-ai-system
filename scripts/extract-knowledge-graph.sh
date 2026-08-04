#!/usr/bin/env bash
# extract-knowledge-graph.sh — extract-knowledge-graph.py 실행 래퍼.
# raw/ 원시 문서에서 LangChain 기반으로 개념(Entity)·관계(Relation)를 자동
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

# launchd로 실행되면 대화형 셸 프로필(.zshrc 등)을 안 거치므로 OPENROUTER_API_KEY가
# 비어있다. ai-control.sh와 동일하게 ~/.hermes/.env에서 런타임에만 읽어 프로세스
# 환경변수로 세팅한다 — 이 스크립트나 다른 어떤 파일에도 값을 기록하지 않는다.
if [ -z "${OPENROUTER_API_KEY:-}" ] && [ -f "$HOME/.hermes/.env" ]; then
  OPENROUTER_API_KEY="$(grep -E '^OPENROUTER_API_KEY=' "$HOME/.hermes/.env" | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")"
  export OPENROUTER_API_KEY
fi

exec .venv/bin/python scripts/extract-knowledge-graph.py "$@"
