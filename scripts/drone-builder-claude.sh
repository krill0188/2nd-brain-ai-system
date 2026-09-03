#!/usr/bin/env bash
# 로컬 AI 드론빌더 — Claude Pro 구독(claude -p) 기반 (2026-09-03 신규).
#
# drone-wiki-web의 웹 버전(app/api/drone-builder/route.ts, OpenRouter+haiku)과 달리:
#   - Claude Pro 구독으로 실행 → OpenRouter 비용 0
#   - ~/2nd 위키를 에이전트가 직접 검색(고정 top-K RAG 스니펫이 아니라 필요한 만큼 탐색)
#   - 결과를 research/designs/에 파일로 남겨 지식베이스에 축적된다
#
# 설계 지침은 scripts/drone-builder-prompt.md 한 곳에만 둔다 — 텔레그램 경로
# (~/.claude/skills/drone_builder/SKILL.md, claudeclaw)도 같은 파일을 참조하므로
# 지침을 바꿀 땐 그 파일만 고치면 두 경로에 동시에 반영된다.
#
# 사용법:  bash scripts/drone-builder-claude.sh "정찰용 소형 VTOL 드론"
set -euo pipefail
cd "$HOME/2nd"

CONCEPT="${1:-}"
if [[ -z "$CONCEPT" ]]; then
  echo "사용법: $0 \"드론 컨셉\"" >&2
  exit 1
fi

GUIDE="scripts/drone-builder-prompt.md"
if [[ ! -f "$GUIDE" ]]; then
  echo "설계 지침 파일이 없습니다: $GUIDE" >&2
  exit 1
fi

DATE=$(date +%Y%m%d)
SLUG=$(printf '%s' "$CONCEPT" \
  | tr '[:upper:]' '[:lower:]' \
  | sed 's/[^[:alnum:]가-힣]\{1,\}/-/g; s/^-//' \
  | cut -c1-40 \
  | sed 's/-$//')
OUT="research/designs/${DATE}-${SLUG}.md"
mkdir -p research/designs

claude -p "설계 지침 파일 ${GUIDE} 를 먼저 읽고, 거기 적힌 절차와 규칙을 그대로 따라라.

컨셉: ${CONCEPT}
출력 파일: ${OUT}
created 날짜: $(date +%Y-%m-%d)

작업이 끝나면 생성한 파일 경로 한 줄만 출력해라." \
  --dangerously-skip-permissions \
  --add-dir "$HOME/2nd"

# 결과 확인 후 텔레그램 요약 발송 (발송은 LLM 불필요 — OpenRouter 크레딧과 무관)
if [[ -f "$OUT" ]]; then
  LINES=$(wc -l < "$OUT" | tr -d ' ')
  echo ""
  echo "✅ 저장 완료: $OUT (${LINES}줄)"
  hermes send -t telegram "🚁 AI 드론빌더 설계안 생성 완료

컨셉: ${CONCEPT}
저장: ${OUT} (${LINES}줄)

⚠️ 미검증 초안입니다 — 검토 후 가치 있는 부분만 canonical로 승격하세요." 2>/dev/null || true
else
  echo "⚠️ 파일이 생성되지 않았습니다: $OUT" >&2
  exit 1
fi
