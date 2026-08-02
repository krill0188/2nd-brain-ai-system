#!/usr/bin/env bash
# test_innovation_run.sh — innovation-run.sh의 LLM 미호출 결정론적 부분만
# 검증한다(비용 없음). claude -p 호출 자체는 1라운드 라이브 스모크
# 테스트로 이미 실증됨(2026-08-02, innovations/registry/*.md 참조).
set -uo pipefail

SCRIPT="$HOME/2nd/scripts/innovation-run.sh"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

PASS=0; FAIL=0
ok()  { PASS=$((PASS+1)); echo "PASS: $1"; }
bad() { FAIL=$((FAIL+1)); echo "FAIL: $1"; }

# 0) 문법 검증
if bash -n "$SCRIPT" 2>"$TMPDIR/synerr"; then
  ok "innovation-run.sh 문법 검증 통과"
else
  bad "문법 오류: $(cat "$TMPDIR/synerr")"
fi

extract_fn() { sed -n "/^${1}() {/,/^}\$/p" "$SCRIPT"; }

# 1) slugify — 한국어 입력에도 안전하게 슬러그 생성(research-run.sh와 동일 패턴)
eval "$(extract_fn slugify)"
slug=$(slugify "드론 군집 비행과 음성 인식")
if [[ -n "$slug" && "$slug" =~ ^[a-z0-9-]+$ ]]; then
  ok "slugify: 한국어 입력 → 안전한 슬러그($slug)"
else
  bad "slugify" "결과: '$slug'"
fi

empty_slug=$(slugify "!!!")
if [[ "$empty_slug" == innovation-* ]]; then
  ok "slugify: 빈 결과 시 타임스탬프 폴백"
else
  bad "slugify 폴백" "결과: '$empty_slug'"
fi

# 2) state.json 생성/갱신 (jq 기반, run 디렉터리 격리)
RUNS_DIR="$TMPDIR/runs"
mkdir -p "$RUNS_DIR/test-run"
jq -n '{run_id:"test-run", status:"running", current_round:0, max_rounds:5, llm_calls:0}' \
  > "$RUNS_DIR/test-run/state.json"

state_file() { echo "$RUNS_DIR/$1/state.json"; }
state_get() { jq -r "$2" "$(state_file "$1")"; }
state_set() {
  local sid="$1" jq_expr="$2"; shift 2
  local sf; sf="$(state_file "$sid")"
  local tmp; tmp="$(mktemp)"
  jq "$jq_expr" "$@" "$sf" > "$tmp" && mv "$tmp" "$sf"
}

state_set "test-run" '.llm_calls += 1'
state_set "test-run" '.current_round = $r' --argjson r 3
calls=$(state_get "test-run" '.llm_calls')
round=$(state_get "test-run" '.current_round')
if [[ "$calls" == "1" && "$round" == "3" ]]; then
  ok "state.json: llm_calls/current_round 갱신 정상"
else
  bad "state.json 갱신" "calls=$calls round=$round"
fi

# 3) LLM 호출 상한 체크 로직(call_claude_stage 내부 조건과 동일 조건식)
LLM_CALL_LIMIT=22
state_set "test-run" '.llm_calls = 22'
calls=$(state_get "test-run" '.llm_calls')
if (( calls >= LLM_CALL_LIMIT )); then
  ok "LLM 호출 상한(22) 도달 조건 정상 판정"
else
  bad "LLM 호출 상한 판정" "calls=$calls"
fi

# 4) innovation-pick.py 연동 확인 — 실제 그래프로 노드쌍이 실제로 나오는지
if python3 "$HOME/2nd/scripts/innovation-pick.py" "__test_pick_only__" >"$TMPDIR/pick.out" 2>"$TMPDIR/pick.err"; then
  if grep -q "^- A:" "$TMPDIR/pick.out" && grep -q "^- B:" "$TMPDIR/pick.out"; then
    ok "innovation-pick.py: 실제 그래프에서 cross-domain 노드쌍 정상 생성"
  else
    bad "innovation-pick.py 출력 형식" "$(cat "$TMPDIR/pick.out")"
  fi
  rm -rf "$HOME/2nd/innovations/runs/__test_pick_only__"
else
  bad "innovation-pick.py 실행 실패" "$(cat "$TMPDIR/pick.err")"
fi

echo ""
echo "${PASS}/$((PASS+FAIL)) 통과"
[[ "$FAIL" -eq 0 ]]
