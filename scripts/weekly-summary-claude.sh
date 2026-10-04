#!/usr/bin/env bash
# 2nd-weekly-summary — Claude Pro 구독(claude -p) 기반 실행.
# OpenRouter(hermes 자체 에이전트 실행) 크레딧 소진 대응으로 2026-09-02 전환.
set -euo pipefail
cd "$HOME/2nd"

PROMPT='~/2nd/log.md 에서 이번 주(최근 7일) 변경 이력을 읽어 요약해라. 형식: 새 문서 N개 / 업데이트 N개 /
lint 결과 한 줄. 주요 토픽 최대 3개 소개. 다음 주 수집 우선순위(drone-sw → datalink → drone-ai) 한 줄 제안.
파일을 새로 만들 필요는 없다 — 텍스트 요약만 출력해라.'

# 2026-10-04: ai_router.py 경유. 이름만 보면 "요약"이라 저가치 후보 같지만, 이 프롬프트는
# log.md를 Claude가 직접 Read 도구로 읽는 걸 전제로 한다(프롬프트 안에 내용이 미리 안 담김) —
# codex-lb/Hermes 저가치 경로는 파일시스템 접근이 아예 없어서 이 방식으론 저가치로 못 내림.
# 그래서 tier=high 유지(내용을 프롬프트에 미리 박아넣는 재작업은 이번엔 범위 밖).
exec python3 "$HOME/projectm/scripts/ai_router.py" -p "$PROMPT" --tier high --project 2nd-weekly-summary --workdir "$HOME/2nd" \
  --claude-arg=--dangerously-skip-permissions \
  --claude-arg=--disallowedTools --claude-arg=Write,Edit \
  --claude-arg=--add-dir --claude-arg="$HOME/2nd"
