# INNOVATION_ENGINE_ROADMAP.md — Innovation Engine 구현 계획

> 작성: 2026-08-02 | 전제: `INNOVATION_ENGINE.md` 설계 완료
> 성격: **계획 문서 — 이 문서 작성으로 아무것도 구현하지 않았다.**
> 원칙: 최소 변경 · `research-run.sh` 기존 자산 최대 재사용 · 각 Phase 독립 롤백.

---

## 0. 재사용 vs 신규 — 처음부터 구분

Innovation Engine은 Research Engine과 파이프라인 형태(bash 상태 머신 +
claude -p 역할 순차 호출)가 같다. **처음부터 새로 만들지 않는다** —
`research-run.sh`/`research-search.py`의 검증된 안전장치(`--tools ""
--safe-mode`, all-or-nothing, LLM 호출 상한, 실패 시 아카이브)를 그대로
재사용하고, **프롬프트와 분기 로직만 다르게** 만든다.

| 요소 | Research Engine에서 가져옴 | Innovation Engine 고유 |
|---|---|---|
| bash 상태 머신 구조 | ✅ 그대로 | 상태 이름만 다름(§2) |
| `claude -p --tools "" --safe-mode` 호출 방식 | ✅ 그대로(이미 검증된 버그 수정 포함) | — |
| 기계 검색(하이브리드) | ✅ `research-search.py` 그대로 재사용 가능(Knowledge Gap 텍스트로 관련 문서 찾을 때) | Cross-Domain Scan은 신규(§3, 검색이 아니라 "먼 것 찾기") |
| 승인 명령 구조 | ✅ CLI 기반 | GO/HOLD/DISCARD 3지선다로 확장 |
| all-or-nothing 검증 | ✅ 원칙 재사용 | 검증 기준이 다름(진실 여부 아님, §4) |

---

## Phase I0 — Knowledge Gap 시드 파싱 검증 (반나절, 코드 변경 없음)

**작업**: 기존 완료된 research 세션 3건(`research/drafts/*.md`)의 "11. 후속
조사 대상" 섹션을 실제로 파싱해보고, Innovation Engine의 입력으로 쓸 수
있는 형태인지 확인한다.

**완료 기준**: 최소 2개 세션에서 "후속 조사 대상" 텍스트를 구조화된
Knowledge Gap 항목으로 추출 가능함을 확인.
**위험**: 없음(읽기 전용). **롤백**: 불필요.

---

## Phase I1 — Cross-Domain Scan (기계, LLM 없음)

**작업**: `scripts/innovation-scan.py` 신규 — `knowledge-graph.json`에서
`ontologyClass`(Phase O1, 이미 구현됨)가 **서로 다른** 노드 쌍을 골라낸다.
완전 무작위가 아니라 최소 필터를 둔다(설계 문서 §7의 결정 사항 3 반영):
그래프 거리(hop) 2 이상 & 두 노드 모두 `confidence`가 `low`만은 아닌 것.

**예상 변경 파일**: `scripts/innovation-scan.py`(신규)만.
**위험**: 낮음 — 읽기 전용 스캔, 그래프/canonical 무변경.
**완료 기준**: 실행 시 최소 10쌍의 후보 조합 출력, 수작업 검토로 "말이 되는
조합 후보"가 절반 이상인지 확인(무작위 조합이 대부분 무의미하면 필터 강화).
**롤백**: 스크립트 삭제.

---

## Phase I2 — Technology Evolution 커넥터 (신규 인프라 최소화)

**작업**: `scripts/param-diff.py`가 이미 만들어 둔 `.ua/param-cache/`와
`param-diff-*` 페이지를 Innovation Engine 프롬프트에 컨텍스트로 주입하는
얇은 커넥터 함수. **새로운 버전 추적 로직을 만들지 않는다** — 이미 있는
결과물을 읽기만 한다.

**예상 변경 파일**: `scripts/innovation-scan.py`에 함수 추가(신규 파일 아님).
**위험**: 낮음. **완료 기준**: 조합에 PX4/ArduPilot 관련 노드가 포함될 때
param-diff 결과가 컨텍스트에 실제로 포함됨을 확인.
**롤백**: 함수 제거.

---

## Phase I3 — 파이프라인 본체 (`innovation-run.sh`)

**작업**: `research-run.sh`를 템플릿으로 새 스크립트 작성. 상태 이름은
Innovation Engine 고유로: `scanned → combined → novelty_checked →
evolved → projected → feasibility_checked → risk_checked → classified →
awaiting_decision → go|hold|discard`.

LLM 호출 6회(Novel Combination, Future Technology, Feasibility, Risk,
분류, Report) — Cross-Domain Scan(I1)과 Novelty Check 1차 필터는 기계.
Novelty Check의 LLM 보조 판단까지 포함하면 최대 7회. Research Engine
(5회)보다 많지만 후보가 여러 개(3~5)라 세션당 호출 상한을 **15회**로
별도 산정(설계 문서 §4의 "낮게 잡지 않는다" 반영, 정확한 수치는 이 Phase
에서 확정).

**Weapon System Candidate 정책은 코드가 아니라 프롬프트로 구현**한다 —
Report Writer 프롬프트에 "이 타입으로 분류되면 구체적 설계·사양·구현
방법을 절대 생성하지 말고 조사 방향 수준에서 멈출 것"을 하드코딩된 지시로
포함시킨다. 별도 필터 스크립트를 만들지 않는 이유: 사후 필터보다 생성
단계에서부터 막는 것이 더 안전하다(생성된 뒤 걸러내면 이미 생성이라는
행위 자체가 일어난 것).

**예상 변경 파일**: `scripts/innovation-run.sh`(신규), `innovations/prompts/`
(신규, 7개 역할 프롬프트).
**위험**: 중간 — 새 프롬프트 세트라 Research Engine 때처럼 자기완결성
문제(파일 경로 언급 시 도구 접근 시도)가 재발할 수 있음 — Research Engine
경험을 그대로 적용해 처음부터 "도구 접근 권한 없음" 명시.
**완료 기준**: 후보 3개 생성 → Novelty Check로 최소 1개 탈락 → 나머지가
Feasibility/Risk 검토를 거쳐 4개 타입 중 하나로 분류됨을 실제 실행으로 확인.
**롤백**: `innovation-run.sh` + `innovations/prompts/` 삭제.

---

## Phase I4 — `innovations/` 저장구조 + Human Decision

**작업**: `research/`와 나란한 신규 최상위 영역 `innovations/{runs,
combinations,reports}/` (설계 문서 §5, §7 결정 사항 1 반영 — `research/`와
완전 대칭 대신 더 단순한 3분류로 시작, 필요시 나중에 세분화).

`innovation-run.sh decide <id> go|hold|discard` 명령 추가 — `research-run.sh
approve/reject`와 동일한 패턴, 3지선다로 확장.

**예상 변경 파일**: `scripts/innovation-run.sh`(decide 커맨드 추가).
**위험**: 낮음(canonical/raw 미접촉 — Innovation Engine은 설계상 canonical에
절대 안 씀, §5 원칙 그대로 코드에 반영).
**완료 기준**: `go`/`hold`/`discard` 각각 실행 시 세션 상태가 올바르게
기록되고 `innovations/`에만 남음(canonical/index.md/log.md 무변경 — T3와
동일한 방식으로 검증).
**롤백**: 디렉터리 삭제.

---

## Phase I5 — Research Theme 자동 순환

**작업**: `Research Theme` 타입으로 분류되고 `go` 판정을 받은 항목만,
`research-run.sh new "<Research Theme 내용>"`을 자동 호출해 새 연구 세션을
시드한다. **이게 유일한 두 엔진 간 자동 연결점**이다(설계 문서 §3.5) —
나머지 3개 타입(Patent/Mission/Weapon System Candidate)은 사람이 다음
단계를 수동으로 결정.

**예상 변경 파일**: `scripts/innovation-run.sh`(decide 커맨드에 분기 추가).
**위험**: 중간 — 자동으로 새 연구 세션이 계속 생성되면 LLM 호출이 눈덩이처럼
불어날 수 있음 → **세션당이 아니라 하루 단위 신규 연구 세션 생성 상한**을
별도로 두는 것을 이 Phase에서 결정해야 함(예: 하루 3건).
**완료 기준**: Research Theme go 판정 1건이 실제로 새 research 세션을
만들고, 그 세션이 정상적으로 Planner부터 시작함을 확인.
**롤백**: 자동 호출 코드 제거, 수동 트리거로 대체.

---

## 전체 순서 요약

```
Phase I0  Knowledge Gap 시드 검증 (반나절)
Phase I1  Cross-Domain Scan (기계, innovation-scan.py)
Phase I2  Technology Evolution 커넥터 (param-diff.py 재사용)
Phase I3  파이프라인 본체 (innovation-run.sh, LLM 6~7회)
Phase I4  innovations/ 저장구조 + GO/HOLD/DISCARD
Phase I5  Research Theme → Research Engine 자동 순환 (하루 상한 필요)
```

I1·I2는 서로 독립, I3는 I1·I2에 의존, I4는 I3 완료 후, I5는 I4 완료 후.

---

## 착수 전 확인 필요 사항 (설계 문서 §7과 동일, 재확인)

1. `innovations/` 구조: 3분류(runs/combinations/reports)로 시작 제안 — 확정 필요.
2. LLM 호출 상한: 세션당 15회 제안 — 실제 구독 한도 대비 확정 필요.
3. Cross-Domain Scan 필터: hop≥2 & confidence≠low만 제외 — 실행 결과 보고 조정.
4. Phase I5의 일일 신규 연구 세션 상한 — 숫자 확정 필요(제안: 3건/일).
