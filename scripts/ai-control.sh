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

  local report=""
  report+="🤖 *AI 플랫폼 상태 리포트*\n"
  report+="📅 $(date '+%Y-%m-%d %H:%M')\n\n"

  sect "Launchd 스케줄러 (2nd Brain 잡)"
  for job_label in "ai.2nd.daily-ingest" "ai.2nd.weekly-lint" "ai.2nd.weekly-summary"; do
    local plist="$HOME/Library/LaunchAgents/${job_label}.plist"
    if [[ -f "$plist" ]]; then
      local loaded
      loaded=$(launchctl list "$job_label" 2>/dev/null | grep '"PID"' || true)
      if [[ -n "$loaded" ]]; then
        ok "$job_label: 실행 중"
        report+="✅ $job_label: 실행 중\n"
      else
        ok "$job_label: 등록됨 (대기 중)"
        report+="✅ $job_label: 등록됨\n"
      fi
    else
      warn "$job_label: plist 없음"
      report+="⚠️  $job_label: 미등록\n"
    fi
  done

  sect "최근 실행 이력"
  for job in "ingest" "lint" "summary"; do
    local log_file="$LOG_DIR/${job}.log"
    if [[ -f "$log_file" ]]; then
      local last_line
      last_line=$(tail -1 "$log_file" 2>/dev/null || true)
      ok "$job: $last_line"
      report+="✅ $job: $last_line\n"
    else
      warn "$job: 이력 없음"
      report+="⚠️  $job: 이력 없음\n"
    fi
  done

  sect "claude -p (Claude Code CLI)"
  local ping_result
  if ping_result=$(echo "ping" | claude -p "respond with the single word PONG and nothing else" 2>/dev/null); then
    if echo "$ping_result" | grep -qi "pong"; then
      ok "claude -p 응답 정상 ($(claude --version 2>/dev/null | head -1))"
      report+="✅ claude -p: 응답 정상\n"
    else
      warn "claude -p 응답 이상: $ping_result"
      report+="⚠️  claude -p: 응답 이상\n"
    fi
  else
    fail "claude -p 응답 실패"
    report+="❌ claude -p: 응답 실패\n"
  fi

  sect "OpenCode + Kimi K2"
  if command -v opencode &>/dev/null; then
    local oc_ver
    oc_ver=$(opencode --version 2>/dev/null || echo "unknown")
    ok "opencode 설치됨 (v$oc_ver)"
    report+="✅ OpenCode: v$oc_ver (대화형 — 직접 실행 필요)\n"
  else
    fail "opencode 미설치"
    report+="❌ OpenCode: 미설치\n"
  fi

  sect "Codex CLI"
  if command -v codex &>/dev/null; then
    local cdx_ver
    cdx_ver=$(codex --version 2>/dev/null | head -1 || echo "unknown")
    ok "codex 설치됨 ($cdx_ver)"
    report+="✅ Codex: $cdx_ver (대화형 — 직접 실행 필요)\n"
  else
    fail "codex 미설치"
    report+="❌ Codex: 미설치\n"
  fi

  sect "Gate C 파일"
  local graph_json="$REPORT_DIR/knowledge-graph.json"
  local graph_html="$REPORT_DIR/graph.html"
  local gap_report="$REPORT_DIR/gap-report.md"

  if [[ -f "$graph_json" ]]; then
    local node_count
    node_count=$(python3 -c "import json; d=json.load(open('$graph_json')); print(len(d.get('nodes',[])))" 2>/dev/null || echo "?")
    ok "knowledge-graph.json: ${node_count}개 노드 ($(stat -f '%Sm' -t '%Y-%m-%d %H:%M' "$graph_json"))"
    report+="✅ 지식그래프: ${node_count}노드\n"
  else
    warn "knowledge-graph.json 없음 — Gate C 실행 필요"
    report+="⚠️  지식그래프: 없음 (Gate C 실행 필요)\n"
  fi

  [[ -f "$graph_html" ]] && ok "graph.html 존재" || warn "graph.html 없음"
  [[ -f "$gap_report" ]] && ok "gap-report.md 존재 ($(stat -f '%Sm' -t '%Y-%m-%d %H:%M' "$gap_report"))" \
                          || warn "gap-report.md 없음 — run-gap 실행 필요"

  sect "VS Code 연동 (수동 확인 필요)"
  warn "Gemini Code Assist: VS Code 사이드바에서 직접 확인"
  warn "GitHub Copilot: VS Code에서 편집 중 제안 여부 확인"
  report+="⚠️  Gemini/Copilot: VS Code에서 수동 확인 필요\n"

  echo ""
  if $telegram; then
    send_telegram "$(echo -e "$report")"
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
  ✅ launchd 3 잡 (ingest·lint·summary) — 즉시 트리거 가능
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
  run-ingest)  cmd_run_ingest ;;
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
