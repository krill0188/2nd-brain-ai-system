# MULTI_AGENT.md — 다중 역할(Multi-Role) 아키텍처 명세

> 작성: 2026-08-02 | 성격: **설계 문서 — 구현하지 않았다** (단, 아래 9개 역할 중
> 8개는 이미 실제로 구현·검증되어 있음을 실측 확인했다 — 이 문서는 새 역할을
> 발명하는 게 아니라 이미 있는 것을 공식 계약으로 정리하는 작업이다).

---

## 0. 용어부터 바로잡는다 — "Multi-Agent"가 아니라 "Multi-Role"

이 시스템은 **서로 독립적으로 실행되는 다중 에이전트 프로세스가 아니다.**
`research-run.sh`는 **단일 `claude -p` 세션이 역할 프롬프트를 바꿔가며
순차적으로 호출되는 bash 상태 머신**이다(이미 `AI_RESEARCHER_ARCHITECTURE.md`
§4에서 확정된 설계이자 실사용 검증됨). 마스터가 이전에 명시적으로 금지한
"대규모 멀티에이전트 프레임워크"(2026-08-01, Phase 1 비범위)를 이 문서가
몰래 다시 들여오지 않기 위해, 아래 9개 역할을 **독립 프로세스가 아니라
역할(role) 계약**으로 정의한다.

**역할 간 통신 방식**: 메시지 패싱이나 API 호출이 아니라 **공유 파일
시스템**이다. 역할 A가 파일을 쓰면 역할 B가 그 파일을 읽는다. 이게
이 시스템의 유일한 "통신 프로토콜"이며, 이미 그렇게 동작 중이다.

---

## 1. 역할 ↔ 실제 구현 대응표

| 요청된 역할 | 실행 주체 | 성격 | 구현 상태 |
|---|---|---|---|
| **Researcher** | `scripts/research-run.sh` | bash 상태 머신(LLM 아님) — 전체 워크플로 조율 | ✅ 구현·검증됨 |
| **Planner** | `claude -p` + `research/prompts/planner.md` | LLM 역할 | ✅ 구현·검증됨 |
| **Retriever** | `scripts/research-search.py` | 기계(LLM 없음) — 하이브리드 검색 | ✅ 구현·검증됨 |
| **Graph Manager** | `scripts/update-graph.sh` | 기계(LLM 없음) — 그래프 갱신 + Phase O1 온톨로지 라벨링 | ✅ 구현·검증됨 |
| **Scientist** | `claude -p` + `research/prompts/hypothesis.md` | LLM 역할 — 클레임/가설 생성 | ✅ 구현·검증됨 (Relationship/Reasoning 심화는 `RESEARCH_ENGINE.md` 제안, 미구현) |
| **Critic** | `claude -p` + `research/prompts/critic.md` | LLM 역할, 독립 컨텍스트 | ✅ 구현·검증됨 |
| **Validator** | `claude -p` + `research/prompts/verifier.md` (기존 명칭: Evidence Verifier) | LLM 역할 | ✅ 구현·검증됨 |
| **Writer** | `claude -p` + `research/prompts/report.md` (기존 명칭: Report Writer) | LLM 역할 | ✅ 구현·검증됨 |
| **Knowledge Manager** | `scripts/research-promote.py` | 기계 검증 + 파일 쓰기(LLM 없음) — canonical 승격 | ✅ 구현·검증됨 |

**8/9 역할이 이미 구현되어 있다.** 유일하게 완전히 새로운 건 없다 — 이
문서의 가치는 "발명"이 아니라 "계약 명세화"에 있다.

---

## 2. 역할별 입력·출력·상태·통신 계약

### Researcher (Orchestrator)
| | 내용 |
|---|---|
| 입력 | 마스터의 연구 목표 텍스트, `runs/<id>/state.json`(재개 시) |
| 출력 | 다음 역할 호출 결정, `state.json` 갱신 |
| 상태 | `state.json`의 `status` 필드(9종, `RESEARCH_SCHEMA.md` 정의) |
| 통신 | 각 역할에게 컨텍스트 파일을 stdin으로 조립해 전달, 결과 파일을 받아 다음 상태로 전이 |

### Planner
| | 내용 |
|---|---|
| 입력 | `00-goal.md` |
| 출력 | `01-questions.md`(하위 질문 3~8개) |
| 상태 | 무상태(stateless) — 매 호출이 독립 |
| 통신 | Researcher로부터 목표 텍스트를 stdin으로 수신, 결과를 stdout으로 반환 → Researcher가 파일로 저장 |

### Retriever
| | 내용 |
|---|---|
| 입력 | `01-questions.md`, `knowledge-graph.json`, `embeddings.json`(있으면) |
| 출력 | `02-search-hits.md` |
| 상태 | 무상태(기계 스크립트, 매 실행이 독립) |
| 통신 | 파일 읽기/쓰기만 — LLM 호출 없음 |

### Graph Manager
| | 내용 |
|---|---|
| 입력 | canonical 4계층 전체(`entities/concepts/comparisons/queries`) |
| 출력 | `knowledge-graph.json`(노드·엣지·`ontologyClass` 갱신) |
| 상태 | 누적형(기존 그래프를 읽어 증분 갱신) — 유일하게 "기억을 유지하는" 역할 |
| 통신 | Researcher의 파이프라인과 비동기 — 수동 또는 별도 트리거로 실행, Retriever가 그 결과를 소비 |

### Scientist (Hypothesis Generator)
| | 내용 |
|---|---|
| 입력 | `01-questions.md`, `02-search-hits.md` |
| 출력 | `hypotheses/<id>.md`(claim/claim_type/supporting_sources) |
| 상태 | 무상태 |
| 통신 | Retriever의 출력을 stdin으로 수신 |

### Critic
| | 내용 |
|---|---|
| 입력 | `hypotheses/<id>.md`, `02-search-hits.md` |
| 출력 | `reviews/<id>.md`(opposing_sources/limitations/confidence, 신규 작성) |
| 상태 | 무상태, **의도적으로 Scientist의 컨텍스트를 이어받지 않음**(독립적 회의) |
| 통신 | Scientist의 출력 파일만 읽음 — Scientist 호출 시 사용된 프롬프트/추론 과정은 전달받지 않음(설계상 의도) |

### Validator (Evidence Verifier)
| | 내용 |
|---|---|
| 입력 | `hypotheses/<id>.md`, `reviews/<id>.md`, `02-search-hits.md` |
| 출력 | `reviews/<id>.md`(verification_status 추가, 덮어씀) |
| 상태 | 무상태 |
| 통신 | Critic이 작성한 파일을 읽어 같은 파일에 필드만 추가 — `opposing_sources`/`limitations` 텍스트는 절대 고치지 않음(계약으로 강제) |

### Writer (Report Writer)
| | 내용 |
|---|---|
| 입력 | `00-goal.md`, `01-questions.md`, `02-search-hits.md`, `hypotheses/<id>.md`, `reviews/<id>.md` |
| 출력 | `drafts/<id>.md`(13개 섹션) |
| 상태 | 무상태 |
| 통신 | 전 단계 산출물 전부를 조인 — 새 사실을 추가하지 않고 종합만 함(계약) |

### Knowledge Manager (research-promote.py)
| | 내용 |
|---|---|
| 입력 | 마스터의 `approve` 명령 + 클레임 ID 지정(`--items`) |
| 출력 | canonical 신규 페이지 + `index.md`/`log.md` 원자적 갱신 |
| 상태 | canonical 자체가 상태(영구 저장) |
| 통신 | `hypotheses/`+`reviews/` 두 파일을 조인해 검증, all-or-nothing으로 canonical에 씀 — 유일하게 `research/` 밖(canonical)에 쓰는 역할 |

---

## 3. Workflow (전체 결합)

```
Researcher(오케스트레이터)
  │
  ├─▶ Planner ──────────────▶ 01-questions.md
  │
  ├─▶ Retriever(기계) ───────▶ 02-search-hits.md   ◀── Graph Manager(비동기, 별도 트리거)가
  │                                                     미리 갱신해 둔 knowledge-graph.json 소비
  ├─▶ Scientist ─────────────▶ hypotheses/<id>.md
  │
  ├─▶ Critic ────────────────▶ reviews/<id>.md (신규)
  │
  ├─▶ Validator ─────────────▶ reviews/<id>.md (덮어씀, 필드 추가)
  │
  ├─▶ Writer ────────────────▶ drafts/<id>.md
  │
  ├─▶ [마스터 승인 대기]
  │
  └─▶ Knowledge Manager ─────▶ canonical 신규 페이지 (승인된 클레임만)
```

`RESEARCH_ENGINE.md`가 이미 이 워크플로를 11단계로 상세 기술했다 — 이
문서의 Workflow는 그 요약이며 새로운 내용을 추가하지 않는다.

---

## 4. Failure & Recovery (역할별)

| 역할 | 실패 모드 | 복구 |
|---|---|---|
| Researcher | 하위 역할 2회 연속 실패 | `state.json.status=failed`, 텔레그램 보고, `resume`으로 재개 |
| Planner/Scientist/Critic/Validator/Writer | `claude -p` 호출 실패/빈 응답 | 동일 단계 1회 재시도(총 2회) 후 실패 처리(공통 규칙) |
| Retriever | 임베딩 venv 없음/embeddings.json 없음 | 자동으로 키워드 전용 폴백(무회귀, 이미 검증됨) |
| Graph Manager | Gate C가 만든 `article:` 중복 노드 | 매 실행마다 자동 정규화 병합(이미 구현됨) |
| Knowledge Manager | 클레임 검증 실패(배치 중 1건이라도) | all-or-nothing 전체 중단, 파일 변화 0건(실측 검증됨) |
| 세션 반려(모든 역할 결과물 포함) | 마스터가 `reject` | 세션 전체를 `_archive/`로 이동, canonical/raw 무변경(T3로 실측 검증됨) |

이 표는 `AI_RESEARCHER_ARCHITECTURE.md` §6의 내용을 역할 단위로 재배열한
것이며, 새로운 실패 모드를 추가하지 않는다 — 이미 실사용 중 발생했던
것만 표에 남긴다.

---

## 5. 이 문서가 바꾸지 않는 것

- 역할이 9개로 명명됐다고 해서 `claude -p` 호출 횟수가 늘지 않는다 — 여전히
  세션당 5회(Planner/Scientist/Critic/Validator/Writer)이고, Researcher/
  Retriever/Graph Manager/Knowledge Manager는 LLM 호출이 아니다.
- 역할 간 실시간 통신(메시지 큐, pub/sub 등)을 도입하지 않는다 — 파일
  기반 핸드오프가 이미 충분히 작동하고 있고(`AI_RESEARCHER_ARCHITECTURE.md`
  원칙 2), 규모가 이를 바꿀 근거를 아직 만들지 않았다.
