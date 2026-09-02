#!/usr/bin/env bash
# 2nd-weekly-summary — Claude Pro 구독(claude -p) 기반 실행.
# OpenRouter(hermes 자체 에이전트 실행) 크레딧 소진 대응으로 2026-09-02 전환.
set -euo pipefail
cd "$HOME/2nd"

PROMPT='~/2nd/log.md 에서 이번 주(최근 7일) 변경 이력을 읽어 요약해라. 형식: 새 문서 N개 / 업데이트 N개 /
lint 결과 한 줄. 주요 토픽 최대 3개 소개. 다음 주 수집 우선순위(drone-sw → datalink → drone-ai) 한 줄 제안.
파일을 새로 만들 필요는 없다 — 텍스트 요약만 출력해라.'

exec claude -p "$PROMPT" \
  --dangerously-skip-permissions \
  --disallowedTools "Write,Edit" \
  --add-dir "$HOME/2nd"
