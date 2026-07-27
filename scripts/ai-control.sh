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

# ── 상수 ─────────────────────────────────────────────────────
JOB_INGEST="b1a360fce35d"
JOB_LINT="91acb1c73884"
JOB_SUMMARY="bd81d81bca5f"
GAP_SCRIPT="$HOME/2nd/scripts/gate-c-analyze.sh"
REPORT_DIR="$HOME/2nd/.ua"

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
send_telegram() {
  local msg="$1"
  if hermes send --to telegram "$msg" 2>/dev/null; then
    info "Telegram 전송 완료"
  else
    warn "Telegram 전송 실패 (hermes send 오류)"
  fi
}

# ── 명령어별 함수 ─────────────────────────────────────────────

cmd_status() {
  local telegram=false
  [[ "${1:-}" == "--telegram" ]] && telegram=true

  local report=""
  report+="🤖 *AI 플랫폼 상태 리포트*\n"
  report+="📅 $(date '+%Y-%m-%d %H:%M')\n\n"

  sect "Hermes Gateway"
  local gw_pid gw_line
  gw_line=$(hermes gateway status 2>/dev/null | grep "PID" | head -1 || true)
  if [[ -n "$gw_line" ]]; then
    gw_pid=$(echo "$gw_line" | grep -oE '[0-9]+' | head -1)
    ok "Gateway 실행 중 (PID $gw_pid)"
    report+="✅ Hermes Gateway: PID $gw_pid\n"
  else
    fail "Gateway 응답 없음"
    report+="❌ Hermes Gateway: 응답 없음\n"
  fi

  sect "Hermes Cron Jobs"
  local cron_out
  cron_out=$(hermes cron list 2>/dev/null)

  for job_name in "2nd-daily-ingest" "2nd-weekly-lint" "2nd-weekly-summary"; do
    local last_run
    last_run=$(echo "$cron_out" | grep -A15 "Name:.*$job_name" | grep "Last run:" | head -1 | sed 's/.*Last run: *//' || true)
    if [[ -n "$last_run" ]]; then
      ok "$job_name: $last_run"
      report+="✅ $job_name: $last_run\n"
    else
      warn "$job_name: 실행 이력 없음"
      report+="⚠️  $job_name: 이력 없음\n"
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
  t_start=$(date +%s%3N)
  result=$(echo "ping" | claude -p "respond with the single word PONG and nothing else" 2>/dev/null) || {
    fail "claude -p 실패 (로그인 상태 확인 필요)"
    exit 1
  }
  t_end=$(date +%s%3N)
  elapsed=$(( t_end - t_start ))
  if echo "$result" | grep -qi "pong"; then
    ok "응답: $result (${elapsed}ms)"
  else
    warn "예상 외 응답: $result (${elapsed}ms)"
  fi
}

cmd_run_ingest() {
  sect "Daily Ingest 즉시 실행"
  info "Job: $JOB_INGEST (2nd-daily-ingest)"
  info "inbox/ 파일을 지금 처리합니다..."
  hermes cron run "$JOB_INGEST" --accept-hooks
  ok "트리거 완료 — Telegram으로 결과 수신 대기"
}

cmd_run_lint() {
  sect "Weekly Lint 즉시 실행"
  info "Job: $JOB_LINT (2nd-weekly-lint)"
  hermes cron run "$JOB_LINT" --accept-hooks
  ok "트리거 완료 — Telegram으로 결과 수신 대기"
}

cmd_run_summary() {
  sect "Weekly Summary 즉시 실행"
  info "Job: $JOB_SUMMARY (2nd-weekly-summary)"
  hermes cron run "$JOB_SUMMARY" --accept-hooks
  ok "트리거 완료 — Telegram으로 결과 수신 대기"
}

cmd_run_gap() {
  local telegram=false
  [[ "${1:-}" == "--telegram" ]] && telegram=true

  sect "Gate C v2 — AI 공백 분석"
  if [[ ! -f "$GAP_SCRIPT" ]]; then
    fail "gate-c-analyze.sh 없음: $GAP_SCRIPT"
    exit 1
  fi

  if $telegram; then
    bash "$GAP_SCRIPT" --deliver
  else
    bash "$GAP_SCRIPT"
  fi
}

cmd_history() {
  local job_filter="${1:-}"
  sect "Cron 실행 이력 (최근 10건)"
  if [[ -n "$job_filter" ]]; then
    hermes cron runs "$job_filter" --limit 10
  else
    info "=== daily-ingest ==="
    hermes cron runs "$JOB_INGEST" --limit 5 2>/dev/null || true
    info "=== weekly-lint ==="
    hermes cron runs "$JOB_LINT" --limit 3 2>/dev/null || true
    info "=== weekly-summary ==="
    hermes cron runs "$JOB_SUMMARY" --limit 3 2>/dev/null || true
  fi
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
  ✅ Hermes 3 cron 잡 (ingest·lint·summary) — 즉시 트리거 가능
  ✅ claude -p — ping 테스트 및 gate-c-analyze.sh에서 사용
  ✅ Gate C gap analysis — 직접 실행 + Telegram 전송
  ✅ Telegram 상태 보고 — hermes send telegram
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
