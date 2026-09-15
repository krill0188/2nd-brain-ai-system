#!/usr/bin/env bash
# ai-control.sh — 2nd Brain AI 플랫폼 통제 스크립트
#
# Usage:
#   ./scripts/ai-control.sh status              # 전체 상태 확인
#   ./scripts/ai-control.sh status --telegram   # 상태 + Telegram 전송
#   ./scripts/ai-control.sh ping                # claude -p 응답 테스트
#   ./scripts/ai-control.sh run-ingest          # daily-ingest 즉시 실행
#   ./scripts/ai-control.sh run-lint            # weekly-lint 즉시 실행
#   ./scripts/ai-control.sh run-summary         # weekly-summary 즉시 실행
#   ./scripts/ai-control.sh run-gap             # Gate C 공백 분석 실행
#   ./scripts/ai-control.sh run-gap --telegram  # Gate C + Telegram 전송
#   ./scripts/ai-control.sh history             # 최근 cron 실행 이력
#   ./scripts/ai-control.sh help                # 사용법

set -eo pipefail

# VS Code / cron 등 비대화형 환경에서 PATH 보장
export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:/usr/local/bin:$PATH"
[ -f "$HOME/.local/bin/env" ] && . "$HOME/.local/bin/env"

# ── 상수 ─────────────────────────────────────────────────────
SCRIPT_INGEST="$HOME/2nd/scripts/daily-ingest-claude.sh"
SCRIPT_LINT="$HOME/2nd/scripts/weekly-lint-claude.sh"
SCRIPT_SUMMARY="$HOME/2nd/scripts/weekly-summary-claude.sh"
GAP_SCRIPT="$HOME/2nd/scripts/gate-c-analyze.sh"
REPORT_DIR="$HOME/2nd/.ua"
LOG_DIR="$HOME/2nd/.ua/logs"
mkdir -p "$LOG_DIR"

# ── 색상 (TTY에서만 적용) ─────────────────────────────────────
if [[ -t 1 ]]; then
  G="\033[0;32m"; R="\033[0;31m"; Y="\033[0;33m"
  B="\033[0;34m"; C="\033[0;36m"; W="\033[1;37m"; N="\033[0m"
else
  G=""; R=""; Y=""; B=""; C=""; W=""; N=""
fi

ok()   { echo -e "${G}✅ $*${N}"; }
fail() { echo -e "${R}❌ $*${N}"; }
warn() { echo -e "${Y}⚠️  $*${N}"; }
info() { echo -e "${C}ℹ  $*${N}"; }
sect() { echo -e "\n${W}── $* ──────────────────────────────${N}"; }

# ── Telegram 전송 ─────────────────────────────────────────────
NOTIFY_SH="/Users/amaster/claudeclaw/scripts/notify.sh"
send_telegram() {
  local msg="$1"
  if [[ -x "$NOTIFY_SH" ]] && bash "$NOTIFY_SH" "$msg" 2>/dev/null; then
    info "Telegram 전송 완료"
  else
    warn "Telegram 전송 실패 (notify.sh 오류)"
  fi
}

# ── LLM 호출 (claude -p 실패 시 openrouter fallback) ─────────
call_llm() {
  local prompt="$1"

  # 1차: claude -p (최대 2회)
  for i in 1 2; do
    local result
    if result=$(echo "$prompt" | claude -p 2>/dev/null) && [[ -n "$result" ]]; then
      echo "$result"; return 0
    fi
    [[ $i -eq 1 ]] && { warn "claude -p 1차 실패 → 5초 후 재시도"; sleep 5; }
  done

  warn "claude -p offline → OpenRouter fallback 시도"
  local or_key=""
  [[ -f "$HOME/.hermes/.env" ]] && \
    or_key=$(grep -E '^OPENROUTER_API_KEY=' "$HOME/.hermes/.env" | cut -d= -f2- | tr -d '"' | tr -d "'")

  if [[ -n "$or_key" ]]; then
    local body
    body=$(python3 -c "
import json, sys
prompt = sys.argv[1]
print(json.dumps({'model':'openai/gpt-4o-mini','messages':[{'role':'user','content':prompt}]}))
" "$prompt" 2>/dev/null)
    local resp
    resp=$(curl -sf --max-time 30 "https://openrouter.ai/api/v1/chat/completions" \
      -H "Authorization: Bearer $or_key" \
      -H "Content-Type: application/json" \
      -d "$body" 2>/dev/null \
      | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['choices'][0]['message']['content'])" 2>/dev/null)
    if [[ -n "$resp" ]]; then
      ok "OpenRouter fallback 성공"
      echo "$resp"; return 0
    fi
  else
    warn "OPENROUTER_API_KEY 없음 (~/.hermes/.env)"
  fi

  echo "❌ LLM 응답 실패 (claude -p offline, openrouter 불가)"
  return 1
}

# ── 커스텀 프롬프트 읽기 ─────────────────────────────────────
PROMPTS_FILE="$HOME/.2nd-brain-ui/hermes-prompts.json"

read_hermes_prompt() {
  local job="$1"   # ingest | lint | summary | gap
  if [[ ! -f "$PROMPTS_FILE" ]]; then echo ""; return; fi
  python3 -c "
import json, sys
try:
    d = json.load(open('$PROMPTS_FILE'))
    print(d.get('$job', {}).get('systemPrompt', '').strip())
except:
    print('')
" 2>/dev/null || echo ""
}

# ── 명령어별 함수 ─────────────────────────────────────────────

cmd_status() {
  local telegram=false
  [[ "${1:-}" == "--telegram" ]] && telegram=true

  local report
  report=$(python3 "$HOME/2nd/scripts/ai-control-status.py") || return $?
  printf '%s\n' "$report"
  if $telegram; then
    send_telegram "$report"
  fi
}

cmd_ping() {
  sect "claude -p 응답 테스트"
  info "전송 중..."
  local t_start t_end elapsed result
  t_start=$(python3 -c "import time; print(int(time.time()*1000))")
  result=$(echo "ping" | claude -p "respond with the single word PONG and nothing else" 2>/dev/null) || {
    fail "claude -p 실패 (로그인 상태 확인 필요)"
    exit 1
  }
  t_end=$(python3 -c "import time; print(int(time.time()*1000))")
  elapsed=$(( t_end - t_start ))
  if echo "$result" | grep -qi "pong"; then
    ok "응답: $result (${elapsed}ms)"
  else
    warn "예상 외 응답: $result (${elapsed}ms)"
  fi
}

cmd_run_ingest() {
  sect "Daily Ingest 즉시 실행"
  info "Script: daily-ingest-claude.sh"

  # inbox/ 비어 있으면 자동 수집 먼저 실행
  local inbox_count
  inbox_count=$(ls "$HOME/2nd/inbox/"*.md 2>/dev/null | wc -l | tr -d ' ')
  if [[ "$inbox_count" -eq 0 ]]; then
    info "inbox/ 비어 있음 → fetch-inbox.sh 자동 수집 실행"
    "$HOME/2nd/scripts/fetch-inbox.sh" 2>/dev/null || warn "fetch-inbox.sh 실패 (계속 진행)"
  else
    info "inbox/ ${inbox_count}개 파일 발견 → 처리 시작"
  fi

  bash "$SCRIPT_INGEST" 2>&1 | tee -a "$LOG_DIR/ingest.log"
  echo "[$(date '+%Y-%m-%d %H:%M')] ingest 완료" >> "$LOG_DIR/ingest.log"
  ok "ingest 완료"

  # knowledge-graph.json 자동 갱신
  if [[ -f "$HOME/2nd/scripts/update-graph.sh" ]]; then
    info "knowledge-graph.json 갱신 중..."
    bash "$HOME/2nd/scripts/update-graph.sh" 2>/dev/null && ok "그래프 갱신 완료" || warn "그래프 갱신 실패 (ingest는 정상 완료)"
  fi

  # SCHEMA.md 9필드 계약 검증
  if [[ -f "$HOME/2nd/scripts/lint-knowledge.py" ]]; then
    info "SCHEMA.md 9필드 계약 검증 중 (lint-knowledge.py)..."
    local lint_output
    if lint_output=$(python3 "$HOME/2nd/scripts/lint-knowledge.py" 2>&1); then
      ok "lint-knowledge 통과 — 이번 ingest에서 SCHEMA 위반 없음"
    else
      warn "lint-knowledge 위반 발견 (아래 목록 — 텔레그램 보고 후 마스터 확인 필요):"
      printf '%s\n' "$lint_output" | while IFS= read -r line; do warn "  $line"; done
    fi
  fi
}

cmd_run_lint() {
  sect "Weekly Lint 즉시 실행"
  info "Script: weekly-lint-claude.sh"

  bash "$SCRIPT_LINT" 2>&1 | tee -a "$LOG_DIR/lint.log"
  echo "[$(date '+%Y-%m-%d %H:%M')] lint 완료" >> "$LOG_DIR/lint.log"
  ok "lint 완료"
}

cmd_run_summary() {
  sect "Weekly Summary 즉시 실행"
  info "Script: weekly-summary-claude.sh"

  bash "$SCRIPT_SUMMARY" 2>&1 | tee -a "$LOG_DIR/summary.log"
  echo "[$(date '+%Y-%m-%d %H:%M')] summary 완료" >> "$LOG_DIR/summary.log"
  ok "summary 완료"
}

cmd_run_gap() {
  local telegram=false
  [[ "${1:-}" == "--telegram" ]] && telegram=true

  sect "Gate C v2 — AI 공백 분석"
  if [[ ! -f "$GAP_SCRIPT" ]]; then
    fail "gate-c-analyze.sh 없음: $GAP_SCRIPT"
    exit 1
  fi

  local custom_prompt
  custom_prompt=$(read_hermes_prompt "gap")
  if [[ -n "$custom_prompt" ]]; then
    info "커스텀 시스템 프롬프트 적용됨 (UI Settings → Hermes → 갭 분석)"
    export GATE_C_SYSTEM_PROMPT="$custom_prompt"
  fi

  if $telegram; then
    bash "$GAP_SCRIPT" --deliver
  else
    bash "$GAP_SCRIPT"
  fi
}

cmd_history() {
  local job_filter="${1:-}"
  sect "실행 이력 (로그 파일)"
  for job in "ingest" "lint" "summary"; do
    local log_file="$LOG_DIR/${job}.log"
    if [[ -n "$job_filter" ]] && [[ "$job" != *"$job_filter"* ]]; then continue; fi
    info "=== $job ==="
    if [[ -f "$log_file" ]]; then
      tail -10 "$log_file"
    else
      warn "이력 없음"
    fi
  done
}

cmd_help() {
  cat <<'EOF'

ai-control.sh — 2nd Brain AI 플랫폼 통제 스크립트

사용법:
  status [--telegram]   전체 AI 플랫폼 상태 확인 (--telegram: Telegram 전송)
  ping                  claude -p 응답 속도 테스트
  run-ingest            daily-ingest 즉시 실행 (inbox → canonical)
  run-lint              weekly-lint 즉시 실행
  run-summary           weekly-summary 즉시 실행
  run-gap [--telegram]  Gate C AI 공백 분석 실행 (--telegram: Telegram 전송)
  history [job_id]      cron 실행 이력 조회
  help                  이 도움말

통제 가능 범위:
  ✅ status: 전체 ai.2nd.* 관찰 / 기존 ingest·lint·summary 즉시 실행 명령 유지
  ✅ claude -p — ping 테스트 및 gate-c-analyze.sh에서 사용
  ✅ Gate C gap analysis — 직접 실행 + Telegram 전송
  ✅ Telegram 상태 보고 — claudeclaw notify.sh
  ⚠️  OpenCode / Codex — 설치 확인만 가능 (대화형 도구)
  ❌ Gemini Code Assist / GitHub Copilot — VS Code 전용, 프로그래밍 통제 불가

EOF
}

# ── 메인 ─────────────────────────────────────────────────────
COMMAND="${1:-help}"
shift || true

case "$COMMAND" in
  status)      cmd_status "${@}" ;;
  ping)        cmd_ping ;;
  run-ingest)
    # 자동화 체인(fetch/ingest/self-update/kinetic/discovery/graph)과 같은 lock을
    # 공유한다 — 수동 실행이 자동 스케줄과 겹치면 exec로 전체를 락 래퍼에 넘겨
    # 자식이 부모 락을 물려받게 한다(교착 방지 위해 재진입 시엔 바로 통과).
    if [[ "${PIPELINE_LOCK_HELD:-}" != "1" ]]; then
      export PIPELINE_LOCK_HELD=1
      exec python3 "$HOME/2nd/scripts/with-pipeline-lock.py" -- "$0" run-ingest
    fi
    cmd_run_ingest
    ;;
  run-lint)    cmd_run_lint ;;
  run-summary) cmd_run_summary ;;
  run-gap)     cmd_run_gap "${@}" ;;
  history)     cmd_history "${@}" ;;
  help|--help|-h) cmd_help ;;
  *)
    fail "알 수 없는 명령어: $COMMAND"
    cmd_help
    exit 1
    ;;
esac
