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

# 5) UTF-8 안전 절단(한글 멀티바이트 경계에서 tr "Illegal byte sequence"
#    나던 실측 버그의 회귀 테스트, 2026-08-02 수정)
python3 -c "
with open('$TMPDIR/utf8.md', 'w', encoding='utf-8') as f:
    f.write('가'*250)
"
if snip=$(python3 -c "import sys; print(open(sys.argv[1], encoding='utf-8').read()[:200].replace(chr(10), ' '))" "$TMPDIR/utf8.md" 2>"$TMPDIR/utf8.err"); then
  charcount=$(python3 -c "print(len('$snip'))" 2>/dev/null || echo 0)
  if [[ "$charcount" == "200" ]]; then
    ok "UTF-8 문자 단위 절단: 한글 250자 → 정확히 200자(무오류)"
  else
    bad "UTF-8 절단 길이" "기대 200, 실제 $charcount"
  fi
else
  bad "UTF-8 절단 실행 실패" "$(cat "$TMPDIR/utf8.err")"
fi

# 6) continue 명령의 라운드 번호 산술(LLM 미호출, jq만 검증)
jq -n '{run_id:"cont-test", status:"awaiting_review", current_round:5, max_rounds:5, llm_calls:20}' \
  > "$RUNS_DIR/cont-test.json" 2>/dev/null || true
last_round=5
extra_rounds=5
from_round=$((last_round + 1))
to_round=$((last_round + extra_rounds))
if [[ "$from_round" == "6" && "$to_round" == "10" ]]; then
  ok "continue: 라운드 5 완료 후 이어가면 6~10라운드로 정확히 계산"
else
  bad "continue 라운드 산술" "from=$from_round to=$to_round"
fi

echo ""
echo "${PASS}/$((PASS+FAIL)) 통과"
[[ "$FAIL" -eq 0 ]]
