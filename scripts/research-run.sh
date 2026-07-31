#!/usr/bin/env bash
# research-run.sh — 인간 승인형 AI 연구원 Orchestrator (Phase 1 MVP, v2)
#
# 최소 연구 루프: 질문 입력 → 연구계획(Planner) → 내부 지식 검색(기존 RAG
# 로직 재사용) → 그래프 확장 → 가설 후보(Hypothesis Generator) → 비판
# 검토(Critic) → 출처 검증(Evidence Verifier) → 연구 메모(Report Writer)
# → 마스터 승인 대기.
#
# Orchestrator 자체는 LLM이 아니라 이 bash 상태 머신이다(결정론적 순서 관리).
# 단일 claude CLI(구독) 세션이 역할 프롬프트를 바꿔가며 순차 수행한다.
#
# Phase 1 범위 밖(구현하지 않음): canonical 자동 승격, 자율 웹 크롤링,
# 완전자율 반복. drafts/ 저장까지가 끝 — 승격은 이 스크립트가 하지 않는다.
#
# 사용법:
#   scripts/research-run.sh new "<연구 목표>"
#   scripts/research-run.sh resume <session-id>
#   scripts/research-run.sh status <session-id>
#   scripts/research-run.sh approve <session-id>
#   scripts/research-run.sh reject <session-id> "<사유>"
#
# 계약: research/RESEARCH_SCHEMA.md 참조.
# raw/ 및 canonical 4계층은 이 스크립트에서 절대 읽기만 한다 — 쓰지 않는다.

set -euo pipefail

WIKI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESEARCH_DIR="$WIKI_ROOT/research"
RUNS_DIR="$RESEARCH_DIR/runs"
HYP_DIR="$RESEARCH_DIR/hypotheses"
REVIEWS_DIR="$RESEARCH_DIR/reviews"
DRAFTS_DIR="$RESEARCH_DIR/drafts"
PROMPTS_DIR="$RESEARCH_DIR/prompts"
SEARCH_PY="$WIKI_ROOT/scripts/research-search.py"
ARCHIVE_DIR="$RESEARCH_DIR/_archive"

LLM_CALL_LIMIT=10
MAX_ATTEMPTS=2

log() { echo "[research-run $(date '+%H:%M:%S')] $*"; }
die() { log "ERROR: $*"; exit 1; }

report_master() {
  local msg="$1"
  log "$msg"
  if command -v hermes >/dev/null 2>&1; then
    hermes send -t telegram "[연구] $msg" >/dev/null 2>&1 || true
  fi
}

slugify() {
  # 한국어 등 iconv//TRANSLIT이 변환 못 하는 입력은 파이프 실패로 set -e를
  # 죽이지 않도록 || true 로 흡수하고, 결과가 비면 타임스탬프로 대체한다.
  local text="$1"
  local ascii
  ascii="$(printf '%s' "$text" | iconv -t ascii//TRANSLIT 2>/dev/null || true)"
  local slug
  slug="$(printf '%s' "$ascii" | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g' | cut -c1-48)"
  if [[ -z "$slug" ]]; then
    slug="research-$(date +%s)"
  fi
  printf '%s' "$slug"
}

# ---- state.json 헬퍼 (runs/<id>/state.json) --------------------------

state_file() { echo "$RUNS_DIR/$1/state.json"; }

state_get() { jq -r "$2" "$(state_file "$1")"; }

state_set_status() {
  local sid="$1" status="$2"
  local sf; sf="$(state_file "$sid")"
  local tmp; tmp="$(mktemp)"
  jq --arg s "$status" --arg now "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
     '.status=$s | .updated=$now' "$sf" > "$tmp" && mv "$tmp" "$sf"
}

state_inc_llm_calls() {
  local sf; sf="$(state_file "$1")"
  local tmp; tmp="$(mktemp)"
  jq '.llm_calls += 1' "$sf" > "$tmp" && mv "$tmp" "$sf"
}

state_record_failure() {
  local sid="$1" stage="$2" attempt="$3" err="$4"
  local sf; sf="$(state_file "$sid")"
  local tmp; tmp="$(mktemp)"
  jq --arg stage "$stage" --arg err "$err" --argjson attempt "$attempt" \
     --arg now "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
     '.failures += [{stage:$stage, attempt:$attempt, error:$err, at:$now}]' "$sf" > "$tmp" && mv "$tmp" "$sf"
}

# ---- claude -p 호출 ---------------------------------------------------

call_claude_stage() {
  # $1=session_id $2=stage_name $3=prompt_file $4=context_file $5=out_file
  local sid="$1" stage="$2" prompt_file="$3" context_file="$4" out_file="$5"

  local calls; calls="$(state_get "$sid" '.llm_calls')"
  if (( calls >= LLM_CALL_LIMIT )); then
    report_master "세션 $sid: LLM 호출 상한($LLM_CALL_LIMIT) 도달 — 중단"
    state_set_status "$sid" "failed"
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
    # --tools ""   : 도구(Write/Bash 등) 접근 완전 차단 — raw/canonical/index/log
    #                우발적 쓰기 원천 차단 (스모크 테스트에서 도구 미차단 시
    #                Write로 산출물에 직접 쓰고 stdout엔 대화체 요약만 남기는
    #                문제를 실제로 확인함).
    # --safe-mode  : 프로젝트/전역 CLAUDE.md·hooks·skills·MCP 전부 비활성화.
    #                (--bare는 OAuth 인증을 막아 이 환경—API 키 없는 구독
    #                방식—에서 사용 불가하므로 제외. --safe-mode는 OAuth 유지.)
    #                이게 없으면 마스터의 전역 PM 페르소나 시스템 프롬프트가
    #                섞여 들어와 매 단계 호출이 "PM처럼 도구로 조사부터"
    #                행동을 시도해 순수 텍스트 생성이 깨지는 문제를 확인함.
    if claude -p --tools "" --safe-mode < "$combined" > "$out_file.tmp" 2> "$err_file"; then
      if [[ -s "$out_file.tmp" ]]; then
        # 코드펜스로 감싸 출력하는 경우가 있어 방어적으로 벗겨낸다 (BSD/GNU sed 호환 문법).
        sed -e '1{/^```/d;}' -e '$ {/^```$/d;}' "$out_file.tmp" > "$out_file.tmp2" && mv "$out_file.tmp2" "$out_file.tmp"
        mv "$out_file.tmp" "$out_file"
        state_inc_llm_calls "$sid"
        rm -f "$combined" "$err_file"
        return 0
      fi
      echo "empty output" > "$err_file"
    fi
    state_record_failure "$sid" "$stage" "$attempt" "$(tail -c 300 "$err_file" | tr '\n' ' ')"
    attempt=$((attempt + 1))
  done

  rm -f "$combined" "$out_file.tmp"
  report_master "세션 $sid: [$stage] 단계 ${MAX_ATTEMPTS}회 연속 실패 — 중단. 원인: $(tail -c 200 "$err_file" | tr '\n' ' ')"
  rm -f "$err_file"
  state_set_status "$sid" "failed"
  exit 1
}

# ---- 세션 생성 / 재개 ---------------------------------------------------

cmd_new() {
  local goal="$1"
  [[ -n "$goal" ]] || die "연구 목표가 비어 있습니다"

  local slug; slug="$(slugify "$goal")"
  [[ -n "$slug" ]] || slug="research-session"
  local sid; sid="$(date +%Y%m%d)-$slug"
  local rdir="$RUNS_DIR/$sid"

  if [[ -d "$rdir" ]]; then
    sid="${sid}-$(date +%H%M%S)"
    rdir="$RUNS_DIR/$sid"
  fi

  mkdir -p "$rdir"
  printf '%s\n' "$goal" > "$rdir/00-goal.md"

  jq -n --arg id "$sid" --arg now "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
     '{session_id:$id, status:"new", created:$now, updated:$now,
       llm_calls:0, llm_call_limit:10, failures:[],
       approval:{decision:null, reason:null, at:null}}' \
     > "$rdir/state.json"

  log "세션 생성: $sid"
  run_pipeline "$sid"
}

cmd_resume() {
  local sid="$1"
  [[ -d "$RUNS_DIR/$sid" ]] || die "세션 없음: $sid"
  log "세션 재개: $sid"
  run_pipeline "$sid"
}

cmd_status() {
  local sid="$1"
  local sf; sf="$(state_file "$sid")"
  [[ -f "$sf" ]] || die "세션 없음: $sid"
  jq '.' "$sf"
}

cmd_approve() {
  local sid="$1"
  local sf; sf="$(state_file "$sid")"
  [[ -f "$sf" ]] || die "세션 없음: $sid"
  local status; status="$(jq -r '.status' "$sf")"
  [[ "$status" == "awaiting_approval" ]] || die "세션이 승인 대기 상태가 아님 (현재: $status)"
  local tmp; tmp="$(mktemp)"
  jq --arg now "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
     '.status="approved" | .approval={decision:"approved", reason:null, at:$now} | .updated=$now' \
     "$sf" > "$tmp" && mv "$tmp" "$sf"
  report_master "세션 $sid: 마스터 승인 완료. (참고: Phase 1은 canonical 자동 승격을 구현하지 않음 — 승격은 별도 작업)"
}

cmd_reject() {
  local sid="$1" reason="${2:-사유 미기재}"
  local sf; sf="$(state_file "$sid")"
  [[ -f "$sf" ]] || die "세션 없음: $sid"
  local tmp; tmp="$(mktemp)"
  jq --arg now "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --arg reason "$reason" \
     '.status="rejected" | .approval={decision:"rejected", reason:$reason, at:$now} | .updated=$now' \
     "$sf" > "$tmp" && mv "$tmp" "$sf"

  mkdir -p "$ARCHIVE_DIR/$sid"
  [[ -d "$RUNS_DIR/$sid" ]] && mv "$RUNS_DIR/$sid" "$ARCHIVE_DIR/$sid/runs"
  [[ -f "$HYP_DIR/$sid.md" ]] && mv "$HYP_DIR/$sid.md" "$ARCHIVE_DIR/$sid/hypotheses.md"
  [[ -f "$REVIEWS_DIR/$sid.md" ]] && mv "$REVIEWS_DIR/$sid.md" "$ARCHIVE_DIR/$sid/reviews.md"
  [[ -f "$DRAFTS_DIR/$sid.md" ]] && mv "$DRAFTS_DIR/$sid.md" "$ARCHIVE_DIR/$sid/drafts.md"

  log "세션 반려: $sid → research/_archive/$sid (사유: $reason)"
  log "canonical/index.md/log.md/raw 무변경 (Phase 1은 애초에 쓰지 않음)"
}

# ---- 파이프라인 실행 ----------------------------------------------------

run_pipeline() {
  local sid="$1"
  local rdir="$RUNS_DIR/$sid"
  local sf; sf="$(state_file "$sid")"
  local status; status="$(jq -r '.status' "$sf")"

  # 1. planner → status: planned
  if [[ "$status" == "new" ]]; then
    log "[planner] 연구 질문 분해"
    local ctx; ctx="$(mktemp)"; printf '연구 목표:\n%s\n' "$(cat "$rdir/00-goal.md")" > "$ctx"
    call_claude_stage "$sid" planner "$PROMPTS_DIR/planner.md" "$ctx" "$rdir/01-questions.md"
    rm -f "$ctx"
    state_set_status "$sid" "planned"
    status="planned"
  fi

  # 2. retrieve (기계, 기존 RAG 로직 재사용) → status: retrieving
  if [[ "$status" == "planned" ]]; then
    log "[retrieve] 기계 검색 — 기존 RAG 스코어링 로직 재사용 (research-search.py)"
    python3 "$SEARCH_PY" --questions "$rdir/01-questions.md" --top-k 5 > "$rdir/02-search-hits.md" \
      || die "research-search.py 실패"
    state_set_status "$sid" "retrieving"
    status="retrieving"
  fi

  # 3. hypothesis generator → status: hypothesis_generated
  if [[ "$status" == "retrieving" ]]; then
    log "[hypothesis] 클레임 생성 (fact/inference/hypothesis)"
    local ctx; ctx="$(mktemp)"
    { echo "연구 질문:"; cat "$rdir/01-questions.md"; echo; echo "검색 결과:"; cat "$rdir/02-search-hits.md"; } > "$ctx"
    mkdir -p "$HYP_DIR"
    call_claude_stage "$sid" hypothesis "$PROMPTS_DIR/hypothesis.md" "$ctx" "$HYP_DIR/$sid.md"
    rm -f "$ctx"
    state_set_status "$sid" "hypothesis_generated"
    status="hypothesis_generated"
  fi

  # 4. critic → status: under_critique
  if [[ "$status" == "hypothesis_generated" ]]; then
    log "[critic] 반론·한계 검토"
    local ctx; ctx="$(mktemp)"
    { echo "클레임 목록:"; cat "$HYP_DIR/$sid.md"; echo; echo "검색 결과:"; cat "$rdir/02-search-hits.md"; } > "$ctx"
    mkdir -p "$REVIEWS_DIR"
    call_claude_stage "$sid" critic "$PROMPTS_DIR/critic.md" "$ctx" "$REVIEWS_DIR/$sid.md"
    rm -f "$ctx"
    state_set_status "$sid" "under_critique"
    status="under_critique"
  fi

  # 5. evidence verifier → status: evidence_checked (reviews/<id>.md 덮어씀)
  if [[ "$status" == "under_critique" ]]; then
    log "[verifier] 출처 대조 검증"
    local ctx; ctx="$(mktemp)"
    {
      echo "클레임 목록:"; cat "$HYP_DIR/$sid.md"; echo
      echo "검토(Critic):"; cat "$REVIEWS_DIR/$sid.md"; echo
      echo "검색 결과:"; cat "$rdir/02-search-hits.md"
    } > "$ctx"
    call_claude_stage "$sid" verifier "$PROMPTS_DIR/verifier.md" "$ctx" "$REVIEWS_DIR/$sid.md"
    rm -f "$ctx"
    state_set_status "$sid" "evidence_checked"
    status="evidence_checked"
  fi

  # 6. report writer → status: awaiting_approval
  if [[ "$status" == "evidence_checked" ]]; then
    log "[report] 연구 메모 작성"
    local ctx; ctx="$(mktemp)"
    {
      echo "목표:"; cat "$rdir/00-goal.md"; echo
      echo "질문:"; cat "$rdir/01-questions.md"; echo
      echo "검색 결과:"; cat "$rdir/02-search-hits.md"; echo
      echo "클레임 목록:"; cat "$HYP_DIR/$sid.md"; echo
      echo "검토(Critic+Verifier):"; cat "$REVIEWS_DIR/$sid.md"
    } > "$ctx"
    mkdir -p "$DRAFTS_DIR"
    call_claude_stage "$sid" report "$PROMPTS_DIR/report.md" "$ctx" "$DRAFTS_DIR/$sid.md"
    rm -f "$ctx"

    local missing=0
    for sec in "1. 연구 질문" "2. 하위 질문" "3. 사용한 내부 자료" "4. 관련 그래프 개념" \
               "5. 확인된 사실" "6. AI의 추론" "7. 가설" "8. 반대 근거" \
               "9. 기술적 제약" "10. 근거 부족 사항" "11. 후속 조사 대상" \
               "12. 출처 목록" "13. 마스터 승인 상태"; do
      grep -qF "$sec" "$DRAFTS_DIR/$sid.md" || { log "경고: 필수 섹션 누락 — $sec"; missing=1; }
    done
    [[ "$missing" == "1" ]] && report_master "세션 $sid: 연구 메모에 필수 섹션 누락 — 검토 필요"

    state_set_status "$sid" "awaiting_approval"
    status="awaiting_approval"
  fi

  if [[ "$status" == "awaiting_approval" ]]; then
    report_master "세션 $sid: 연구 메모 완료 — 승인 대기 (research/drafts/$sid.md 확인 후 approve/reject)"
    log "완료 — 연구 메모: $DRAFTS_DIR/$sid.md"
    log "승인: scripts/research-run.sh approve $sid"
    log "반려: scripts/research-run.sh reject $sid \"사유\""
  elif [[ "$status" == "approved" || "$status" == "rejected" ]]; then
    log "세션 $sid 은 이미 $status 상태입니다."
  fi
}

# ---- 진입점 -------------------------------------------------------------

main() {
  local cmd="${1:-}"
  case "$cmd" in
    new) shift; cmd_new "${1:?연구 목표 필요}" ;;
    resume) shift; cmd_resume "${1:?session-id 필요}" ;;
    status) shift; cmd_status "${1:?session-id 필요}" ;;
    approve) shift; cmd_approve "${1:?session-id 필요}" ;;
    reject) shift; cmd_reject "${1:?session-id 필요}" "${2:-}" ;;
    *)
      cat <<EOF
사용법:
  research-run.sh new "<연구 목표>"
  research-run.sh resume <session-id>
  research-run.sh status <session-id>
  research-run.sh approve <session-id>
  research-run.sh reject <session-id> "<사유>"
EOF
      exit 1
      ;;
  esac
}

main "$@"
