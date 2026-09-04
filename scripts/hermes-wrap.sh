#!/usr/bin/env bash
# hermes-wrap.sh — Hermes Gateway 완전 대체 래퍼
# 역할: 스크립트 실행 → stdout 로그 저장 → 비어있지 않으면 Telegram 전송
# Usage: hermes-wrap.sh <job_name> <script_or_cmd> [args...]
#        hermes-wrap.sh <job_name> --bot dronewiki <script_or_cmd> [args...]
#
# Hermes Gateway가 하던 것을 그대로 수행한다:
#   1. 스케줄된 스크립트 실행
#   2. stdout 캡처
#   3. Telegram으로 결과 전달 (4096자 초과 시 앞부분만)

set -uo pipefail
export PATH="$HOME/.npm-global/bin:$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
[ -f "$HOME/.local/bin/env" ] && . "$HOME/.local/bin/env" 2>/dev/null || true

NOTIFY_SH="/Users/amaster/claudeclaw/scripts/notify.sh"
LOG_DIR="$HOME/2nd/.ua/logs"
mkdir -p "$LOG_DIR"

JOB_NAME="${1:?job_name required}"
shift

# --bot 옵션 처리
if [[ "${1:-}" == "--bot" ]]; then
    BOT="${2}"
    shift 2
    if [[ "$BOT" == "dronewiki" ]]; then
        NOTIFY_SH="/Users/amaster/claudeclaw/scripts/notify-dronewiki.sh"
    fi
fi

LOG_FILE="$LOG_DIR/${JOB_NAME}.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$TIMESTAMP] === START $JOB_NAME ===" >> "$LOG_FILE"

# 스크립트 실행 + stdout/stderr 캡처
set +e
OUTPUT=$(bash -c "$*" 2>&1)
EXIT_CODE=$?
set -e

# 로그 저장
if [[ -n "$OUTPUT" ]]; then
    echo "$OUTPUT" >> "$LOG_FILE"
fi
echo "[$(date '+%Y-%m-%d %H:%M:%S')] === END $JOB_NAME (exit=$EXIT_CODE) ===" >> "$LOG_FILE"

# Telegram 전송: 출력 있을 때만 (lint --quiet 같은 경우 정상 시 침묵)
if [[ -n "$OUTPUT" ]] && [[ -x "$NOTIFY_SH" ]]; then
    # Telegram 4096자 제한 처리
    if [[ ${#OUTPUT} -gt 3800 ]]; then
        TRIMMED="${OUTPUT:0:3800}"$'\n\n...(이하 생략, 로그 파일 확인)'
        bash "$NOTIFY_SH" "$TRIMMED" 2>/dev/null || true
    else
        bash "$NOTIFY_SH" "$OUTPUT" 2>/dev/null || true
    fi
fi

# 오류 시 별도 알림
if [[ $EXIT_CODE -ne 0 ]] && [[ -x "$NOTIFY_SH" ]]; then
    bash "$NOTIFY_SH" "❌ [$JOB_NAME] 실행 실패 (exit=$EXIT_CODE)" 2>/dev/null || true
fi

exit $EXIT_CODE
