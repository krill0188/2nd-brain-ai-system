#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCK_WRAPPER="$SCRIPT_DIR/with-pipeline-lock.py"

# Direct execution acquires the shared writer lock.
# Nested pipeline execution reuses the inherited lock descriptor.
if ! python3 "$LOCK_WRAPPER" --check-inherited; then
  exec python3 "$LOCK_WRAPPER" -- bash "$0" "$@"
fi
# 2nd-daily-ingest — Claude Pro 구독(claude -p) 기반 실행.
# OpenRouter(hermes 자체 에이전트 실행) 크레딧 소진 대응으로 2026-09-02 전환.
# 이전 동작(custom/llm-wiki-ains 스킬, hermes cron b1a360fce35d)과 동일한 작업을
# ~/2nd 프로젝트 자체의 CLAUDE.md + .claude/skills/{summarize-note,publish-entry}로 수행한다.
set -euo pipefail
cd "$HOME/2nd"

PROMPT='SCHEMA.md와 index.md를 먼저 읽고 orient한 뒤 inbox/ 폴더(inbox/processed/ 제외)를 스캔해라.
새 파일이 없으면 "inbox empty no action" 한 줄만 출력하고 끝내라.

새 파일이 있으면 각 파일에 대해 summarize-note 스킬 절차로 canonical 후보(entity/concept/comparison/query)를
작성하고, 완료 후 publish-entry 스킬 절차(표준 경로)로 index.md/log.md에 반영해라. 각 페이지 frontmatter에
domain 필드를 반드시 포함한다 (flight-control | comms-protocol | hardware | gcs-software | ops-mission |
regulations | ai-autonomy 중 하나). 처리에 성공한 inbox 원본 파일은 inbox/processed/로 이동해라.
raw/ 파일은 절대 수정하지 마라. 사소한 언급 하나로는 새 페이지를 만들지 마라.
YouTube 파일은 frontmatter에 transcript: true 이면 "## 자막" 섹션(자동 추출, 최대 8000자)이 있다. 설명란이
아니라 자막 내용을 기준으로 가치를 판단해라: 절차·사양·버그 원인·측정/테스트 결과 같은 구체적 기술 정보가
있으면 컴파일 대상(신규 또는 기존 페이지 보강)이고, 프로모/잡담/도메인 외 영상만 skip해 log.md에 사유를 남겨라.
자막 내용을 근거로 쓸 때는 자막에 없는 사실을 덧붙이지 마라.

작업이 끝나면 "수집 N개, 컴파일 N개, 실패 N개" 형식의 한 줄 요약을 마지막에 출력해라.'

# 2026-10-04: ai_router.py 경유(공용 로깅·kill-switch). 핵심 canonical 컴파일 작업이라
# tier=high 고정(동작 변경 없음) — 레이트리밋일 때만 저가치로 강등되는데, 이 작업은
# .claude/skills(summarize-note 등) 기반이라 저가치 경로(codex-lb/Hermes)에선 그 스킬
# 자체를 못 쓴다. 강등되면 품질이 아니라 "스킬을 아예 못 따름"이 되므로, 실패시 그냥
# 에러로 드러나 다음 launchd 스케줄에서 재시도되는 기존 동작이 더 안전하다 — --no-fallback
# 으로 레이트리밋이어도 폴백 자체를 막는다(--sensitive와 효과는 같지만 로그에 "PII라서"가
# 아니라 "스킬 의존이라서"로 정확히 남는다).
exec python3 "$HOME/projectm/scripts/ai_router.py" -p "$PROMPT" --tier high --project 2nd-daily-ingest --workdir "$HOME/2nd" --no-fallback \
  --claude-arg=--dangerously-skip-permissions \
  --claude-arg=--add-dir --claude-arg="$HOME/2nd"
