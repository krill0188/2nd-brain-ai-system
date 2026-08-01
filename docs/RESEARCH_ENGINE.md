# RESEARCH_ENGINE.md — Research Engine 설계

> 작성: 2026-08-01 | 성격: **설계 문서 — 구현하지 않았다** (단, 이미 구현·검증된
> 기존 파이프라인과의 정확한 대응관계를 실측으로 확인했다).
> 전제: "NotebookLM은 검색한다. 우리 프로젝트는 연구한다"는 구분을 구체적
> 기준으로 정의하고, 그 기준에 맞는 Research Engine의 목표 구조를 설계한다.

---

## 1. 검색(Search)과 연구(Research)의 경계 — NotebookLM과의 구체적 차이

| | NotebookLM (검색형) | 이 프로젝트의 Research Engine (연구형) |
|---|---|---|
| 입력 | 질문 | 연구 목표(더 넓고 개방형) |
| 처리 | 관련 문서 검색 → 요약 생성 | 질문 분해 → 근거 수집 → **관계 분석** → **추론 과정 명시** → 가설 생성 |
| 반론 | 없음 | 독립 컨텍스트의 Critic이 반론·모순·과장을 전담 탐색 |
| 검증 | 없음(요약이 곧 최종 산출물) | Evidence Verifier가 인용-주장 대조, `grounded`/`insufficient_evidence` 판정 |
| 산출물의 신뢰도 표시 | 없음(모든 문장이 동급) | 클레임마다 `claim_type`(fact/inference/hypothesis) + `confidence` 명시 |
| 지식 반영 | 반영 안 됨(세션 종료 시 소멸) | 사람이 승인한 것만 canonical에 **영구 반영**, 미승인분은 증거로 보존 |
| 실패 시 | 조용히 다른 답을 다시 생성 | 세션 상태(`state.json`)로 실패 이력 추적, 2회 연속 실패 시 중단·보고 |

**한 문장 정의**: NotebookLM은 "이미 아는 것을 빨리 찾아 요약"하고, Research
Engine은 "아는 것과 모르는 것의 경계를 그리고, 그 경계에서 새 주장을 만들고,
그 주장을 스스로 의심한 뒤, 사람이 확인한 것만 기억으로 남긴다."

---

## 2. 11단계 파이프라인과 현재 구현의 실측 대응

요청된 흐름: **Research Goal → Research Plan → Evidence → Relationship →
Reasoning → Hypothesis → Counter Evidence → Validation → Report → Approval
→ Knowledge**

| # | 단계 | 현재 구현 상태 (실측) |
|---|---|---|
| 1 | Research Goal | ✅ `research-run.sh new "<목표>"` → `00-goal.md` |
| 2 | Research Plan | ✅ Planner(LLM) → `01-questions.md`(하위 질문 3~8개) |
| 3 | Evidence | ✅ Retriever(기계, 하이브리드 검색) → `02-search-hits.md` |
| 4 | **Relationship** | ⚠️ **명시적 단계 없음** — 그래프 관계가 존재하지만(§3에서 상세) 별도 산출물로 추출되지 않고 Hypothesis Generator의 프롬프트 컨텍스트에 섞여 들어갈 뿐 |
| 5 | **Reasoning** | ⚠️ **명시적 단계 없음** — 클레임과 근거는 기록되지만 "근거에서 클레임까지의 추론 과정 자체"는 별도로 기록되지 않음(LLM 내부에서만 일어나고 사라짐) |
| 6 | Hypothesis | ✅ Hypothesis Generator(LLM) → `hypotheses/<id>.md` (claim/claim_type/supporting_sources) |
| 7 | Counter Evidence | ✅ Critic(독립 컨텍스트 LLM) → `reviews/<id>.md`의 `opposing_sources`/`limitations` |
| 8 | Validation | ✅ Evidence Verifier(LLM) → `reviews/<id>.md`의 `verification_status` |
| 9 | Report | ✅ Report Writer(LLM) → `drafts/<id>.md`(13개 섹션) |
| 10 | Approval | ✅ `research-run.sh approve/reject` |
| 11 | Knowledge | ✅ `research-promote.py --items` → canonical 신규 페이지(13단계 완성, 실사용 검증됨) |

**결론**: 11단계 중 9단계는 이미 실제로 구현·테스트되어 있다. 진짜 설계 과제는
4번(Relationship)과 5번(Reasoning) 두 개뿐이다 — 이 문서는 이 두 개에 집중한다.

---

## 3. 왜 Relationship과 Reasoning이 지금 "숨어있는" 상태인가

Phase 1 구현 당시(§ `research-run.sh` 커밋 이력) Analyst/Gap Detector를
별도 단계로 두지 않고 Hypothesis Generator에 통합하기로 마스터가 결정했다
(스코프 최소화). 그 결과 "여러 근거를 어떻게 연결했는가"와 "그 연결에서 왜
이 결론이 나왔는가"가 **하나의 LLM 호출 안에서 암묵적으로 처리되고 결과만
남는다.** 이게 실제로 문제였던 사례가 이미 있다 — T1 세션 C4 클레임에서
Critic이 "단일 기체 SLAM 논문 2건을 군집 상대위치추정과 동일시하는 논리적
비약"을 지적했는데, 이건 애초에 Relationship 단계(두 논문이 정말 같은
문제를 다루는지 먼저 확인)가 있었다면 Hypothesis 생성 시점에 방지될 수도
있었던 종류의 오류다.

즉 이 두 단계를 명시화하는 것은 새 기능 추가가 아니라 **이미 한 번 실제로
발생한 실패 패턴(근거 없는 결합)에 대한 대응**이다.

---

## 4. 제안 설계 (미구현)

### 4.1 Relationship 단계 — 기계적, LLM 불필요

Phase O1(온톨로지 클래스)과 Phase 2(그래프 evidence/confidence)로 이미
`knowledge-graph.json`이 풍부해졌다. Retriever가 찾은 검색 결과의 노드
ID들을 가지고, **그래프에서 이미 존재하는 관계만 추출**하면 된다 — 새로
추론하지 않는다.

```
research-search.py 결과의 canonical 슬러그 집합 S
  │
  ▼
knowledge-graph.json에서 S 내부 엣지 + S↔1-hop 이웃 엣지 조회
  │
  ▼
research/runs/<id>/03-relationships.md
  "swarm-coordination ──wikilink──▶ decentralized-swarm-gps-denied"
  "recon-swarm-project ──ontologyClass:Mission──"
  (같은 ontologyClass인 노드끼리는 "동일 범주" 태그도 함께 표시)
```

이 파일은 Hypothesis Generator 프롬프트에 "검색 결과:" 다음에 "확인된 관계:"
섹션으로 추가된다. **LLM 호출이 늘지 않는다** — Retriever처럼 순수 기계
단계다.

### 4.2 Reasoning 단계 — Hypothesis Generator 프롬프트 확장(LLM 호출 안 늘어남)

새 LLM 호출을 추가하는 대신, 기존 Hypothesis Generator의 출력 스키마에
필드 하나를 추가한다:

```markdown
## C1

- claim: <한 줄 주장>
- claim_type: fact | inference | hypothesis
- reasoning: <근거에서 이 주장까지 어떻게 연결했는지, 1~2문장 — 이게
  비어있거나 "그냥 그럴 것 같다"면 claim_type을 hypothesis로 낮춰야 한다는
  신호>
- supporting_sources:
  - [[슬러그]]
```

`reasoning` 필드가 명시적으로 요구되면, Critic이 검토할 대상이 "결론"뿐
아니라 "결론에 이른 논리" 자체가 되어 T1 C4 같은 비약을 더 일찍(Hypothesis
생성 시점에 자기 점검, 또는 Critic 단계에서 더 정확히) 잡을 수 있다.

### 4.3 왜 이걸 "설계만" 하고 지금 코드를 안 고치는가

`research-run.sh`/`hypothesis.md` 프롬프트/`RESEARCH_SCHEMA.md`를 동시에
고쳐야 하는 변경이고, 클레임 스키마가 바뀌면 `research-promote.py`의 파서도
같이 바뀌어야 한다(현재 실사용 중인 시스템). 세 파일을 한 번에 안전하게
바꾸려면 별도 승인과 회귀 테스트(T1~T3 재실행)가 필요하다 — 이 문서는 그
작업을 위한 설계 근거이지, 그 자체가 승인은 아니다.

---

## 5. 이 설계가 다른 문서와 맞물리는 지점

- §4.1의 Relationship 추출은 `GRAPH_SCHEMA.md`가 제안한 `ontologyClass`
  필드(Phase O1, 이미 구현됨)를 실제로 소비하는 첫 사례가 된다 — 지금까지는
  라벨만 붙이고 아무도 읽지 않았다.
- §4.2의 `reasoning` 필드는 `ONTOLOGY_SPEC.md`의 `KnowledgeClaim`을 더
  풍부하게 만든다 — 온톨로지 인스턴스가 "무엇을 주장하는가"뿐 아니라
  "왜 그렇게 주장하는가"까지 갖게 된다.
- 두 제안 모두 `AI_RESEARCHER_ARCHITECTURE.md`의 원칙 6("실측 병목이 확인된
  뒤에만 새 기술 도입")과 다르다는 점을 분명히 한다 — 이건 새 기술 도입이
  아니라 **이미 있는 데이터(그래프)를 더 쓰고, 이미 있는 필드(클레임 스키마)를
  하나 늘리는 것**이라 같은 원칙의 "무료 확장" 범주에 속한다.

---

## 6. 다음 결정 필요 사항 (구현 착수 전)

1. `reasoning` 필드를 **모든 클레임에 필수**로 할지, `inference`/`hypothesis`
   타입에만 요구할지(fact는 재진술이라 reasoning이 무의미할 수 있음).
2. Relationship 산출물(§4.1)을 별도 파일로 만들지, `02-search-hits.md`에
   그냥 섹션을 추가할지(파일 수를 늘리지 않는 절충안).
3. 회귀 테스트 범위 — T1~T3를 다시 돌릴지, 아니면 새 테스트 케이스(T4:
   "Relationship 단계가 실제로 근거 없는 결합을 사전에 걸러내는가")를
   추가할지.
