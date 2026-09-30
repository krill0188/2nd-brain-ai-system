#!/usr/bin/env bash
# research-cron.sh <wiki-refactor|weekly-synthesis|gap-miner|idea-generator>
# Claude Pro 구독(claude -p) 기반. 공유 파이프라인 락 하에서 실행한다.
#   wiki-refactor    : canonical 갱신 허용(최대 MAX_PAGES 페이지). lint 실패/초과/raw 변경 시 백업으로 롤백.
#   나머지 3개       : research/ 스테이징에만 쓴다. canonical·raw가 바뀌면 롤백/경고.
# Human Approval(AGENTS.md): staging 산출물은 자동 승격되지 않는다.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCK_WRAPPER="$SCRIPT_DIR/with-pipeline-lock.py"
if ! python3 "$LOCK_WRAPPER" --check-inherited; then
  exec python3 "$LOCK_WRAPPER" -- bash "$0" "$@"
fi
set -euo pipefail

MODE="${1:-}"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"
MAX_PAGES="${RESEARCH_CRON_MAX_PAGES:-15}"
TODAY="$(date +%F)"
WEEK="$(date +%G-W%V)"
BACKUP="$ROOT/.ua/research-cron-backup"
MARKER="$ROOT/.ua/research-cron-$MODE.marker"
CANON=(concepts entities comparisons queries)
log() { echo "[research-cron:$MODE $(date '+%F %T')] $*"; }

case "$MODE" in
  wiki-refactor)
    SKILL=wiki-refactor
    ALLOW_CANON=1
    since_file="$MARKER"; [ -f "$since_file" ] || since_file=""
    if [ -n "$since_file" ]; then
      TOUCHED="$(find raw "${CANON[@]}" -type f -name '*.md' -newer "$since_file" 2>/dev/null | head -200)"
    else
      TOUCHED="$(find raw "${CANON[@]}" -type f -name '*.md' -mtime -1 2>/dev/null | head -200)"
    fi
    if [ -z "$TOUCHED" ]; then log "no new evidence since last run; nothing to do"; touch "$MARKER"; exit 0; fi
    PROMPT="wiki-refactor 스킬(.claude/skills/wiki-refactor/SKILL.md)과 SCHEMA.md를 읽고 절차대로 실행해라.
오늘($TODAY) 새로 들어온/바뀐 파일 목록:
$TOUCHED

이 목록의 근거가 기존 canonical 페이지를 어떻게 바꾸는지 반영해라. 수정 페이지는 최대 ${MAX_PAGES}개.
raw/ 수정 금지. 마지막 줄에 스킬이 지정한 요약 한 줄을 출력해라." ;;
  weekly-synthesis)
    SKILL=weekly-synthesis; ALLOW_CANON=0
    OUT="research/synthesis/$WEEK.md"
    PROMPT="log.md와 지난 7일간 바뀐 canonical 페이지(git log --since='7 days ago' -- concepts entities comparisons queries 와 각 페이지의 updated 필드)를 읽고,
'이번 주 논문 N편 요약'이 아니라 '어떤 지식이 바뀌었는가'를 분석해 $OUT 을 작성해라(이미 있으면 덮어쓴다).
frontmatter: title, week: $WEEK, status: draft, created: $TODAY. 본문 첫 줄에 '> ⚠ 스테이징 산출물 — canonical 아님'.
섹션(정확히 이 순서): ## 강화된 주장 / ## 약해진 주장 / ## Emerging Topic / ## 반복되는 한계 / ## 새로운 Research Gap.
모든 항목은 [[canonical 페이지]]와 ^[raw/...] 근거를 붙이고, 변화가 없으면 '해당 없음'이라고 쓴다. 추측 금지.
index.md, log.md, canonical, raw는 수정하지 마라. 마지막 줄에 '작성: $OUT' 출력." ;;
  gap-miner)
    SKILL=research-gap-miner; ALLOW_CANON=0
    PROMPT="research-gap-miner 스킬(.claude/skills/research-gap-miner/SKILL.md)을 읽고 절차대로 실행해 research/gaps/research-gaps.md 를 갱신해라(없으면 frontmatter status: draft와 '> ⚠ 스테이징 산출물 — canonical 아님'으로 새로 만든다).
canonical, raw, index.md, log.md는 수정 금지. 마지막 줄에 스킬이 지정한 요약 한 줄을 출력해라." ;;
  idea-generator)
    SKILL=research-idea-generator; ALLOW_CANON=0
    PROMPT="research-idea-generator 스킬(.claude/skills/research-idea-generator/SKILL.md)을 읽고 절차대로 실행해라. 기존 idea 재평가를 먼저 하고, 신규 idea는 최대 3개.
research/ideas/ 밖에는 쓰지 마라(canonical, raw, index.md, log.md 수정 금지). 마지막 줄에 스킬이 지정한 요약 한 줄을 출력해라." ;;
  *) echo "usage: $0 <wiki-refactor|weekly-synthesis|gap-miner|idea-generator>" >&2; exit 64 ;;
esac

# 실행 전 스냅샷 (canonical + index/log). 이 시스템의 롤백 기준선.
rm -rf "$BACKUP"; mkdir -p "$BACKUP"
cp -Rp "${CANON[@]}" index.md log.md "$BACKUP"/
touch "$BACKUP/.start"; sleep 1

rollback() {
  log "ROLLBACK: $1"
  for d in "${CANON[@]}"; do rsync -a --delete "$BACKUP/$d/" "$d/"; done
  cp -p "$BACKUP/index.md" index.md; cp -p "$BACKUP/log.md" log.md
}

set +e
claude -p "$PROMPT" --dangerously-skip-permissions --add-dir "$ROOT"
RC=$?
set -e
if [ $RC -ne 0 ]; then rollback "claude exit $RC"; exit $RC; fi

# raw/ 는 어떤 모드에서도 불변
if [ -n "$(find raw -type f -newer "$BACKUP/.start" 2>/dev/null | head -1)" ]; then
  log "ALERT: raw/ modified during run — manual review required (not auto-restored)"
  find raw -type f -newer "$BACKUP/.start" | head -20
  rollback "raw modified"; exit 3
fi

NCHANGED=0
for d in "${CANON[@]}"; do
  NCHANGED=$((NCHANGED + $(diff -rq "$BACKUP/$d" "$d" 2>/dev/null | wc -l)))
done
if [ "$ALLOW_CANON" = 0 ]; then
  if [ "$NCHANGED" -ne 0 ] || ! cmp -s "$BACKUP/index.md" index.md || ! cmp -s "$BACKUP/log.md" log.md; then
    rollback "staging-only mode touched canonical/index/log ($NCHANGED files)"; exit 4
  fi
else
  if [ "$NCHANGED" -gt "$MAX_PAGES" ]; then rollback "changed $NCHANGED > cap $MAX_PAGES"; exit 5; fi
  if ! python3 scripts/lint-knowledge.py --full --quiet; then rollback "lint-knowledge failed"; exit 6; fi
fi

touch "$MARKER"
log "done (canonical files changed: $NCHANGED)"
