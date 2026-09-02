#!/usr/bin/env bash
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

작업이 끝나면 "수집 N개, 컴파일 N개, 실패 N개" 형식의 한 줄 요약을 마지막에 출력해라.'

exec claude -p "$PROMPT" \
  --dangerously-skip-permissions \
  --add-dir "$HOME/2nd"
