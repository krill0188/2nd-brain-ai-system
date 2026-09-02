#!/usr/bin/env bash
# 2nd-weekly-lint — Claude Pro 구독(claude -p) 기반 실행.
# OpenRouter(hermes 자체 에이전트 실행) 크레딧 소진 대응으로 2026-09-02 전환.
set -euo pipefail
cd "$HOME/2nd"

PROMPT='~/2nd 위키 전체 canonical 문서를 점검해라. 점검 항목: 고아 페이지, 끊긴 wikilink, frontmatter 누락
필드, updated 날짜 오류. SCHEMA.md 계약 기준으로 위반 항목을 파일명과 이유 목록으로 출력해라. 절대 파일을
수정하지 마라(자동 수정 없음, 보고만). 문제 없으면 "lint passed N pages checked"를 출력해라.'

exec claude -p "$PROMPT" \
  --dangerously-skip-permissions \
  --disallowedTools "Write,Edit" \
  --add-dir "$HOME/2nd"
