#!/usr/bin/env bash
# innovation-run.sh — Innovation Engine Orchestrator (첫 구현, 2026-08-02)
#
# INNOVATION_ENGINE.md 설계를 실행하되, 마스터 지시("질문→답변→답변 안에서
# 완전 새로운 질문→...")에 따라 **5라운드 고정 체인**으로 만든다 — 각
# 라운드의 제안(proposal.md)이 다음 라운드 Combination 단계의 시드가 된다.
# research-run.sh와 동일한 안전 패턴(--tools "" --safe-mode, 재시도 2회,
# LLM 호출 상한)을 그대로 재사용한다.
#
# 산출물은 canonical에 절대 쓰지 않는다 — innovations/registry/에만 쌓인다
# (INNOVATION_ENGINE.md §5, 마스터 확인: "별도 레지스트리만, canonical 안 씀").
# 5라운드 전부 자동 실행 후 정지한다(마스터가 배치 완료 후 한 번에 검토).
#
# 사용법:
#   scripts/innovation-run.sh start "<초기 시드 — Research Engine 후속조사대상 또는 마스터 프롬프트>"
#   scripts/innovation-run.sh status <run-id>

set -euo pipefail

WIKI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INNOV_DIR="$WIKI_ROOT/innovations"
RUNS_DIR="$INNOV_DIR/runs"
REGISTRY_DIR="$INNOV_DIR/registry"
PROMPTS_DIR="$INNOV_DIR/prompts"
SEARCH_PY="$WIKI_ROOT/scripts/research-search.py"
PICK_PY="$WIKI_ROOT/scripts/innovation-pick.py"

MAX_ROUNDS="${INNOVATION_MAX_ROUNDS:-5}"  # 테스트 시 INNOVATION_MAX_ROUNDS=1로 비용 제한
LLM_CALL_LIMIT=22   # 4단계 × 5라운드 = 20 + 재시도 여유
MAX_ATTEMPTS=2

log() { echo "[innovation-run $(date '+%H:%M:%S')] $*"; }
die() { log "ERROR: $*"; exit 1; }

report_master() {
  local msg="$1"
  log "$msg"
  if command -v hermes >/dev/null 2>&1; then
    hermes send -t telegram "[Innovation] $msg" >/dev/null 2>&1 || true
  fi
}

slugify() {
  local text="$1"
  local ascii
  ascii="$(printf '%s' "$text" | iconv -t ascii//TRANSLIT 2>/dev/null || true)"
  local slug
  slug="$(printf '%s' "$ascii" | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g' | cut -c1-40)"
  if [[ -z "$slug" ]]; then
    slug="innovation-$(date +%s)"
  fi
  printf '%s' "$slug"
}

state_file() { echo "$RUNS_DIR/$1/state.json"; }
state_get() { jq -r "$2" "$(state_file "$1")"; }

state_set() {
  local sid="$1" jq_expr="$2"; shift 2
  local sf; sf="$(state_file "$sid")"
  local tmp; tmp="$(mktemp)"
  jq "$jq_expr" "$@" "$sf" > "$tmp" && mv "$tmp" "$sf"
}

# ---- claude -p 호출 (research-run.sh와 동일 안전 패턴) -------------------

call_claude_stage() {
  local sid="$1" stage="$2" prompt_file="$3" context_file="$4" out_file="$5"

  local calls; calls="$(state_get "$sid" '.llm_calls')"
  if (( calls >= LLM_CALL_LIMIT )); then
    report_master "런 $sid: LLM 호출 상한($LLM_CALL_LIMIT) 도달 — 중단"
    state_set "$sid" '.status="failed"'
    exit 1
  fi

  local combined; combined="$(mktemp)"
  cat "$prompt_file" > "$combined"
  echo -e "\n---\n" >> "$combined"
  cat "$context_file" >> "$combined"

  local attempt=1
  local err_file; err_file="$(mktemp)"
  while (( attempt <= MAX_ATTEMPTS )); do
    log "[$stage] claude -p 호출 (attempt $attempt/$MAX_ATTEMPTS)"
    if claude -p --tools "" --safe-mode < "$combined" > "$out_file.tmp" 2> "$err_file"; then
      if [[ -s "$out_file.tmp" ]]; then
        sed -e '1{/^```/d;}' -e '$ {/^```$/d;}' "$out_file.tmp" > "$out_file.tmp2" && mv "$out_file.tmp2" "$out_file.tmp"
        mv "$out_file.tmp" "$out_file"
        state_set "$sid" '.llm_calls += 1'
        rm -f "$combined" "$err_file"
        return 0
      fi
      echo "empty output" > "$err_file"
    fi
    attempt=$((attempt + 1))
  done

  rm -f "$combined" "$out_file.tmp"
  report_master "런 $sid: [$stage] 단계 ${MAX_ATTEMPTS}회 연속 실패 — 중단. 원인: $(tail -c 200 "$err_file" | tr '\n' ' ')"
  rm -f "$err_file"
  state_set "$sid" '.status="failed"'
  exit 1
}

# ---- start: 5라운드 체인 실행 --------------------------------------------

cmd_start() {
  local seed_text="$1"
  [[ -n "$seed_text" ]] || die "초기 시드가 비어 있습니다"

  local slug; slug="$(slugify "$seed_text")"
  local run_id; run_id="$(date +%Y%m%d)-innovation-$slug"
  local rdir_base="$RUNS_DIR/$run_id"
  if [[ -d "$rdir_base" ]]; then
    run_id="${run_id}-$(date +%H%M%S)"
    rdir_base="$RUNS_DIR/$run_id"
  fi
  mkdir -p "$rdir_base"
  printf '%s\n' "$seed_text" > "$rdir_base/00-seed.md"

  jq -n --arg id "$run_id" --arg now "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
     '{run_id:$id, status:"running", current_round:0, max_rounds:5,
       llm_calls:0, created:$now, updated:$now}' \
     > "$rdir_base/state.json"

  log "런 시작: $run_id (최대 ${MAX_ROUNDS}라운드)"

  local prev_seed_file="$rdir_base/00-seed.md"
  local reg_file="$REGISTRY_DIR/$run_id.md"
  echo "# Innovation Registry — $run_id" > "$reg_file"
  echo "" >> "$reg_file"
  echo "**초기 시드**: $seed_text" >> "$reg_file"
  echo "" >> "$reg_file"

  local round
  for round in $(seq 1 "$MAX_ROUNDS"); do
    local rdir="$rdir_base/round-$round"
    mkdir -p "$rdir"
    log "── 라운드 $round/$MAX_ROUNDS ──"

    # 기계: cross-domain 노드쌍 선택(이번 런에서 이미 쓴 쌍은 제외)
    if ! python3 "$PICK_PY" "$run_id" > "$rdir/00-pair.md" 2> "$rdir/_pick.err"; then
      log "노드쌍 후보 소진 — 라운드 $round에서 체인 조기 종료: $(cat "$rdir/_pick.err")"
      break
    fi

    # 1) Combination — 이전 라운드 제안(또는 초기 시드)을 함께 컨텍스트로 제공
    cat "$rdir/00-pair.md" "$prev_seed_file" > "$rdir/_ctx1.md"
    call_claude_stage "$run_id" "combination" "$PROMPTS_DIR/combination.md" "$rdir/_ctx1.md" "$rdir/01-combination.md"

    # 2) Critique — 기계 검색으로 중복 여부 대조 자료 제공(Novelty Check 근거)
    python3 "$SEARCH_PY" --query "$(head -c 200 "$rdir/01-combination.md" | tr '\n' ' ')" --top-k 5 \
      > "$rdir/_search.md" 2>/dev/null || echo "(검색 결과 없음)" > "$rdir/_search.md"
    cat "$rdir/01-combination.md" "$rdir/_search.md" > "$rdir/_ctx2.md"
    call_claude_stage "$run_id" "critique" "$PROMPTS_DIR/critique.md" "$rdir/_ctx2.md" "$rdir/02-critique.md"

    # 3) Risk & Classification
    cat "$rdir/01-combination.md" "$rdir/02-critique.md" > "$rdir/_ctx3.md"
    call_claude_stage "$run_id" "risk-classify" "$PROMPTS_DIR/risk-classify.md" "$rdir/_ctx3.md" "$rdir/03-risk-classify.md"

    # 4) Proposal — 다음 라운드 시드 생성
    cat "$rdir/01-combination.md" "$rdir/02-critique.md" "$rdir/03-risk-classify.md" > "$rdir/_ctx4.md"
    call_claude_stage "$run_id" "proposal" "$PROMPTS_DIR/proposal.md" "$rdir/_ctx4.md" "$rdir/04-proposal.md"

    {
      echo "## Round $round"
      echo
      cat "$rdir/04-proposal.md"
      echo
      echo "---"
      echo
    } >> "$reg_file"

    rm -f "$rdir"/_ctx*.md "$rdir/_search.md" "$rdir/_pick.err"
    prev_seed_file="$rdir/04-proposal.md"
    state_set "$run_id" '.current_round = $r' --argjson r "$round"
  done

  state_set "$run_id" '.status="awaiting_review" | .updated=$now' --arg now "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  report_master "런 $run_id 완료 — 레지스트리: innovations/registry/$run_id.md (마스터 검토 대기, GO/HOLD/DISCARD)"
  log "완료. 레지스트리: $reg_file"
}

cmd_status() {
  local run_id="$1"
  [[ -f "$(state_file "$run_id")" ]] || die "런 없음: $run_id"
  cat "$(state_file "$run_id")"
}

main() {
  local cmd="${1:-}"; shift || true
  case "$cmd" in
    start) cmd_start "${1:-}" ;;
    status) cmd_status "${1:-}" ;;
    *) die "사용법: $0 {start \"<시드>\"|status <run-id>}" ;;
  esac
}

main "$@"
