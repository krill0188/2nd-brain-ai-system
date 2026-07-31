# Research Session Schema (v2 — 카테고리 기반)

> Governs `research/` — the fourth top-level area alongside `raw/`, canonical
> (`entities/`, `concepts/`, `comparisons/`, `queries/`), and `inbox/`.
> See `AGENTS.md` § Research Layer and `SCHEMA.md` directory table.
>
> v2는 `SCHEMA.md`의 기존 원칙(raw는 종류별, canonical은 타입별로 분리 —
> 세션 단위가 아님)과의 정합성을 위해 카테고리 기반 구조로 재설계되었다.
> v1(세션 단위 단일 폴더)은 폐기.

## Purpose

A research session is a bounded, human-approved investigation loop:
interpret a goal → decompose questions → search internal knowledge (existing
RAG scoring logic, reused) → expand via graph neighbors → generate claim
candidates → critique → verify against sources → draft a markdown report →
request approval. Research output is a **discovery candidate**, never
canonical knowledge, until a human approves it (AGENTS.md § Human Approval).
Phase 1 does **not** implement automatic promotion to canonical — that is
an explicit non-goal.

## Directory layout

```
research/
├── runs/<session-id>/     # 과정 파일 — 세션 전체를 한 번에 archive 가능
│   ├── state.json
│   ├── 00-goal.md
│   ├── 01-questions.md
│   └── 02-search-hits.md   # 기존 RAG 스코어링 로직 재사용 (research-search.py)
├── hypotheses/<session-id>.md   # 클레임 목록 (fact | inference | hypothesis)
├── reviews/<session-id>.md      # Critic + Evidence Verifier 결과
├── drafts/<session-id>.md       # 마스터 승인 대상 연구 메모 (승인 전용 draft 저장소)
├── prompts/                     # 역할별 시스템 프롬프트 (세션 무관, 고정 자산)
└── _archive/<session-id>/       # 반려/종료 세션 — runs/hypotheses/reviews/drafts 4곳에서 이동 보관
```

- 세션 식별자: `<YYYYMMDD-slug>` (log.md 날짜 관례와 정합).
- 4개 카테고리 디렉터리는 같은 session-id로 대응된다 — 파일명이 곧 조인 키.
- `_archive/<session-id>/`는 4개 카테고리에서 이동해온 파일을 한 곳에 모은
  디렉터리다(runs/, hypotheses.md, reviews.md, drafts.md를 그대로 옮김).

## Read/write contract (변경 없음)

| Area | Research loop access |
|---|---|
| `raw/` | Read-only. Never modified. |
| canonical 4계층 | Read-only. Phase 1에서는 **쓰기 자체가 없다** — 자동 승격 비구현. |
| `index.md`, `log.md` | Phase 1에서 손대지 않음. |
| `research/` | Read-write, `research-run.sh`만. |

## Session status (9종 — 세션 단위, 마스터 지정)

```
planned → retrieving → hypothesis_generated → under_critique
        → evidence_checked → awaiting_approval → approved | rejected
                                                 → failed (모든 단계에서 전이 가능)
```

| 상태 | 의미 | 산출물 |
|---|---|---|
| `planned` | 목표 입력 + 질문 분해 완료 | `00-goal.md`, `01-questions.md` |
| `retrieving` | 내부 검색(기존 RAG 로직 재사용) + 그래프 확장 완료 | `02-search-hits.md` |
| `hypothesis_generated` | 클레임 후보 생성 완료 | `hypotheses/<id>.md` |
| `under_critique` | Critic 반론 검토 완료 | `reviews/<id>.md` (critic 파트) |
| `evidence_checked` | Evidence Verifier 대조 완료 | `reviews/<id>.md` (verifier 파트로 덮어씀) |
| `awaiting_approval` | 연구 메모 초안 작성 완료, 마스터 승인 대기 | `drafts/<id>.md` |
| `approved` | 마스터가 draft를 승인 (canonical 승격은 Phase 1 범위 밖 — 승인은 "연구 결과를 신뢰할 수 있다"는 기록일 뿐) | state.json |
| `rejected` | 마스터가 반려 | state.json + `_archive/`로 이동 |
| `failed` | 동일 단계 연속 2회 LLM 실패로 중단 | state.json + 마스터 보고 |

`state.json`은 `runs/<session-id>/state.json`에 위치하며 최소 다음 키를 갖는다:

```json
{
  "session_id": "20260731-...",
  "status": "planned",
  "created": "...", "updated": "...",
  "llm_calls": 0, "llm_call_limit": 10,
  "failures": [],
  "approval": { "decision": null, "reason": null, "at": null }
}
```

## 파이프라인 (5회 LLM 호출 — 마스터 지정 범위 1~10번에 정확히 대응)

Analyst/Gap Detector는 별도 단계로 두지 않는다(마스터의 "최소 연구 루프"
범위에 없음). 근거 종합은 Hypothesis Generator가, 공백/후속조사 식별은
Report Writer가 검색 결과를 직접 읽어 겸한다.

| # | 단계 | 유형 | 입력 | 출력 |
|---|---|---|---|---|
| 1 | Planner | LLM | `00-goal.md` | `runs/<id>/01-questions.md` |
| 2 | Retriever | 기계 (기존 RAG 로직 재사용) | `01-questions.md` | `runs/<id>/02-search-hits.md` |
| 3 | Hypothesis Generator | LLM | `01-questions.md` + `02-search-hits.md` | `hypotheses/<id>.md` |
| 4 | Critic | LLM (독립 컨텍스트) | `hypotheses/<id>.md` + `02-search-hits.md` | `reviews/<id>.md` (신규 작성) |
| 5 | Evidence Verifier | LLM | `hypotheses/<id>.md` + `reviews/<id>.md` + `02-search-hits.md` | `reviews/<id>.md` (같은 파일에 verification_status 추가 — 덮어씀) |
| 6 | Report Writer | LLM | 위 전체 | `drafts/<id>.md` |

## Claim schema — 두 파일로 책임 분리

**`hypotheses/<session-id>.md`** — Hypothesis Generator가 1회 작성 후 불변
(Critic/Verifier가 재기록하지 않는다):

```markdown
## C1

- claim: <한 줄 주장>
- claim_type: fact | inference | hypothesis
- supporting_sources:
  - [[슬러그]]
  - ^[raw/<kind>/<file>.md]
```

**`reviews/<session-id>.md`** — Critic이 먼저 작성(클레임 ID별 1블록), 이어서
Evidence Verifier가 같은 파일을 다시 읽어 `verification_status`를 채워
재작성한다:

```markdown
## C1

- opposing_sources: (Critic이 채움 — 없으면 "없음")
- limitations: (Critic이 채움 — 구현/기술/데이터 제약)
- confidence: high | medium | low (Critic 초기 판단, Verifier가 하향 조정 가능)
- verification_status: grounded | insufficient_evidence (Verifier가 채움)
```

- `claim_type` 판단 기준: **fact** = 근거 문서에 직접 명시된 사실 재진술,
  **inference** = 근거 여러 개를 종합해야 도출되는 논리적 귀결,
  **hypothesis** = 근거를 넘어서는 신규 통찰 후보(가장 낮은 확실성). "이
  주제에 대한 직접 근거가 검색되지 않았다"는 **공백 인지 클레임**도
  `hypothesis`로 분류한다.
- **`verification_status`와 "공백 인지 클레임"의 관계 (실사용 테스트에서
  드러난 모호점 — 명시적으로 고정)**: 공백 인지 클레임(예: "Q2에 대한 직접
  근거 없음")의 `verification_status`는, 그 부재 판단 자체가 제공된 검색
  결과 범위 내에서 사실이면 `grounded`다. `insufficient_evidence`는 오직
  `supporting_sources`에 나열된 인용이 (a) 해석 불가능하거나 (b) 클레임을
  실제로 뒷받침하지 않을 때만 쓴다. 즉 "근거가 없다는 클레임 자체의 신뢰성"과
  "그 클레임이 인용한 소스가 타당한가"는 서로 다른 축이며 혼동하지 않는다.
- **알려진 한계 — 스니펫 절단**: 검색 결과(canonical 발췌·raw 스니펫)는
  전체 문서가 아니라 잘린 발췌본이다. Hypothesis Generator·Critic·Evidence
  Verifier는 전부 이 같은 잘린 발췌본만 보고 판단하므로, 스니펫 범위 밖에
  실제로 존재하는 반박/보강 근거를 원리적으로 발견할 수 없다. 이는 Phase 1의
  구조적 한계이며(Phase 2 임베딩 기반 검색으로 완화 예정), 승인 시 마스터가
  감안해야 한다.
- `supporting_sources`는 최소 1개 이상, 전부 실제 경로/슬러그로 해석 가능해야
  한다. 해석 불가능한 인용이 있으면 Evidence Verifier가 해당 클레임을
  `verification_status: insufficient_evidence`로 표시한다.
- `hypotheses/<id>.md`와 `reviews/<id>.md`는 클레임 ID(`## C1`, `## C2`, …)로
  1:1 대응한다. Report Writer가 두 파일을 조인해서 최종 draft를 만든다.

## `drafts/<session-id>.md` 필수 구성 (13개 요소)

1. 연구 질문
2. 하위 질문
3. 사용한 내부 자료
4. 관련 그래프 개념
5. 확인된 사실 (`claim_type: fact`인 클레임들)
6. AI의 추론 (`claim_type: inference`)
7. 가설 (`claim_type: hypothesis`)
8. 반대 근거 (`opposing_sources` 종합)
9. 기술적 제약 (`limitations` 종합)
10. 근거 부족 사항 (`verification_status: insufficient_evidence`인 클레임)
11. 후속 조사 대상
12. 출처 목록 (모든 `supporting_sources` 합집합)
13. 마스터 승인 상태 (작성 시점엔 `awaiting_approval`로 고정 표기)

## Citation rules (변경 없음)

`SCHEMA.md` § Provenance와 동일: canonical은 `[[slug]]`, raw는
`^[raw/<kind>/<file>.md]`. 해석 불가능한 인용을 만들어내지 않는다.

## LLM call budget (변경 없음)

세션당 `claude -p` 호출 최대 10회. Phase 1 기본 파이프라인은 5회
(Planner/Hypothesis Generator/Critic/Evidence Verifier/Report Writer) —
Retriever는 기계 검색(기존 RAG 로직 재사용)이라 LLM 호출이 아니다.

## Deployment boundary (변경 없음)

`research/`는 `scripts/sync-wiki.sh`나 Vercel 배포에 절대 포함되지 않는다.

## Phase 1 명시적 비범위

- canonical 자동 승격 (승인은 기록되지만 승격 스크립트는 Phase 1에 없음)
- 자율 웹 크롤링
- Neo4j 등 그래프 DB 도입
- 대규모 멀티에이전트 프레임워크
- 기존 RAG(`lib/rag.ts`) 완전 교체 — 로직만 재사용
- 유료 API 무제한 반복 호출 — LLM 호출 상한 10회로 강제
- Vercel 운영환경 비밀정보 변경
