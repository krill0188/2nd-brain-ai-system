#!/usr/bin/env bash
# morning-report-send.sh — 모닝리포트 실행 + @dronewiki_bot 전송 전용 래퍼
set -uo pipefail
export PATH="/Users/amaster/.npm-global/bin:/Users/amaster/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

NOTIFY="/Users/amaster/claudeclaw/scripts/notify-dronewiki.sh"
LOG="/Users/amaster/2nd/.ua/logs/2nd-morning-report.log"
SCRIPT="/Users/amaster/.hermes/scripts/2nd-morning-report.sh"

mkdir -p "$(dirname "$LOG")"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] === START 2nd-morning-report ===" >> "$LOG"

set +e
OUTPUT=$(bash "$SCRIPT" 2>&1)
EXIT_CODE=$?
set -e

if [[ -n "$OUTPUT" ]]; then
    echo "$OUTPUT" >> "$LOG"
    if [[ ${#OUTPUT} -gt 3800 ]]; then
        bash "$NOTIFY" "${OUTPUT:0:3800}"$'\n\n...(이하 생략)' 2>/dev/null || true
    else
        bash "$NOTIFY" "$OUTPUT" 2>/dev/null || true
    fi
fi

if [[ $EXIT_CODE -ne 0 ]]; then
    bash "$NOTIFY" "❌ [2nd-morning-report] 실행 실패 (exit=$EXIT_CODE)" 2>/dev/null || true
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] === END 2nd-morning-report (exit=$EXIT_CODE) ===" >> "$LOG"
exit $EXIT_CODE
