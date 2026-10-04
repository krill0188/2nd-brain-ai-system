#!/usr/bin/env bash
# 2nd-weekly-lint — Claude Pro 구독(claude -p) 기반 실행.
# OpenRouter(hermes 자체 에이전트 실행) 크레딧 소진 대응으로 2026-09-02 전환.
set -euo pipefail
cd "$HOME/2nd"

PROMPT='~/2nd 위키 전체 canonical 문서를 점검해라. 점검 항목: 고아 페이지, 끊긴 wikilink, frontmatter 누락
필드, updated 날짜 오류. SCHEMA.md 계약 기준으로 위반 항목을 파일명과 이유 목록으로 출력해라. 절대 파일을
수정하지 마라(자동 수정 없음, 보고만). 문제 없으면 "lint passed N pages checked"를 출력해라.'

# 2026-10-04: ai_router.py 경유(공용 로깅·kill-switch) — Claude 전용 플래그는
# --claude-arg로 그대로 전달한다(라우터는 의미를 모르고 전달만 함, 동작 그대로 유지).
exec python3 "$HOME/projectm/scripts/ai_router.py" -p "$PROMPT" --tier high --project 2nd-weekly-lint --workdir "$HOME/2nd" \
  --claude-arg=--dangerously-skip-permissions \
  --claude-arg=--disallowedTools --claude-arg=Write,Edit \
  --claude-arg=--add-dir --claude-arg="$HOME/2nd"
