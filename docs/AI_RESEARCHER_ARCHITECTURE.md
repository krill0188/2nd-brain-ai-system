# AI_RESEARCHER_ARCHITECTURE.md — 인간 승인형 드론 AI 연구원 아키텍처

> 작성: 2026-07-31 | 전제: `CURRENT_STATE_AUDIT.md` 감사 결과
> 원칙: 기존 기능 무폐기 · raw 불변 · 승인 전 canonical 승격 금지 · 과도한 마이크로서비스 금지

> ## ⚠️ 2026-08-01 갱신 — 이 문서는 초기 설계안(v1)이다. 실제 Phase 1
> 구현은 마스터의 후속 상세 스펙에 따라 아래처럼 **더 단순화**되어
> 구현·검증되었다 (T1~T3 통과, `MVP_ACCEPTANCE_TESTS.md` 참조).
> 이 문서는 설계 의도의 기록으로 보존하고, 실제 구현 기준은
> `research/RESEARCH_SCHEMA.md`(v2)를 따른다.
>
> | 항목 | 이 문서(v1, 설계안) | 실제 구현(v2, `research/RESEARCH_SCHEMA.md`) |
> |---|---|---|
> | 저장 구조 | `research/<session-id>/` 단일 폴더 | `research/{runs,hypotheses,reviews,drafts}/` 카테고리 분리 |
> | 파이프라인 | 8단계(Planner/Retriever/Analyst/Gap/Hypothesis/Critic/Verifier/Report), LLM 7회 | 5단계 LLM 호출(Planner/Hypothesis/Critic/Verifier/Report) + 기계 검색 1회 |
> | 승인 게이트 | G1(계획)/G2(보고서)/G3(항목별 승격) 3단 | G2에 해당하는 단일 승인(`approve`/`reject`)만. G1·G3 제거 |
> | canonical 승격 | Phase 1에 `research-promote.sh` 포함 | Phase 1 범위 밖으로 명시적 이연(`research-promote.py/.sh`는 존재하나 파이프라인에서 미호출) |
> | 클레임 필드 | `status/evidence/counter/verifier_note` | `claim/claim_type(fact\|inference\|hypothesis)/supporting_sources` + 별도 리뷰 파일의 `opposing_sources/limitations/confidence/verification_status` |

---

## 1. 현재 구조 (As-Is)

```
[외부 소스] ──fetch-inbox.sh(03:30)──▶ inbox/
                                        │ llm-wiki daily-ingest (04:00)
                                        ▼
              raw/ (불변 증거) ◀──── zotero-ingest.py
                  │ (사람 수작업 큐레이션 + ingest 후보)
                  ▼
   canonical/ {concepts, entities, comparisons, queries}
                  │ update-graph.sh / Gate C
                  ▼
        .ua/knowledge-graph.json + news-feed.json
                  │ sync-wiki.sh (04:30) → git push → Vercel
                  ▼
   drone-wiki-web: 위키 뷰 + 그래프 뷰 + 뉴스 + RAG Q&A(OpenRouter haiku)
```

특징: **단방향 발행 파이프라인**. 질문→가설→검증의 역방향 루프 없음.

## 2. 목표 구조 (To-Be)

기존 파이프라인을 그대로 두고, **연구 계층(research/)을 옆에 추가**한다.

```
[마스터: 연구 목표 입력]
        │
        ▼
┌─ research-run.sh (Orchestrator = bash 상태 머신, LLM 아님) ─────────┐
│                                                                      │
│  단일 Claude 세션이 역할 프롬프트를 바꿔가며 순차 수행:              │
│                                                                      │
│  ① Planner        → 01-questions.md   (연구 질문·하위 과제 분해)     │
│  ② Retriever      → 02-evidence.md    (canonical+raw+news+graph 검색,│
│                                         모든 근거에 실경로 인용)      │
│  ③ Analyst        → 02-evidence.md 보강 (자료 비교·관계 분석)        │
│  ④ Gap Detector   → 03-gaps.md        (부족 영역 + 추가 조사 계획)   │
│         ── [G1: 조사계획 승인 게이트 — 기본 자동통과, --strict 시 대기] │
│  ⑤ Hypothesis Gen → 04-hypotheses.md  (가설·통찰 후보, status:proposed)│
│  ⑥ Critic         → 05-critique.md    (반론·모순·과장·구현 한계)      │
│  ⑦ Evidence Verif → 04/05 갱신        (주장↔출처 대조, 근거없음 마킹) │
│  ⑧ Report Writer  → 06-report-draft.md (출처 기반 연구보고서 초안)    │
│                                                                      │
│  전 산출물은 research/<session-id>/ 에만 기록                        │
│  (canonical 4계층 밖 → sync-wiki.sh 배포 대상 아님 = 미승인 노출 차단)│
└──────────────────────────────────────────────────────────────────────┘
        │
        ▼
[G2: 보고서 초안 승인 게이트 — 필수]
  MVP: CLI 검토 / Phase 3: Hermes 텔레그램 전달·응답
        │
        ├─ 반려 → state.json=rejected, 세션 _archive (canonical 무변경)
        ├─ 수정 → 지정 단계부터 재실행
        ▼
[G3: canonical 승격 게이트 — 필수]
  research-promote.sh <id> --approve
        │
        ▼
  canonical 페이지 생성 (frontmatter 9필드 + wikilink≥2)
  + index.md 동기화 + log.md append   ← 기존 SCHEMA 원자적 3동작 준수
        │
        ▼
  기존 sync-wiki.sh(04:30)가 웹에 자동 반영  ← 신규 배포 경로 없음
```

## 3. 데이터 흐름과 저장 계약

### 3.1 research/ 세션 구조 (신규 — SCHEMA.md에 1행 등록 필요)

```
~/2nd/research/
  RESEARCH_SCHEMA.md            # 세션 계약 정의 (이 문서의 부록 A가 초안)
  <YYYYMMDD-slug>/              # 세션 ID
    00-goal.md                  # 마스터 입력 원문 (불변)
    01-questions.md             # Planner 산출
    02-evidence.md              # Retriever+Analyst — 근거마다 실경로 인용 필수
    03-gaps.md                  # 공백 + 추가 조사 계획
    04-hypotheses.md            # 가설 후보 목록, 각 항목 status: proposed|approved|rejected
    05-critique.md              # Critic 산출
    06-report-draft.md          # 승인 대상 보고서 초안
    state.json                  # {stage, approvals:{G1,G2,G3}, llm_calls, updated}
  _archive/<session-id>/        # 반려·완료 세션 보관
```

### 3.2 계층별 쓰기 권한

| 계층 | 연구 루프의 권한 |
|---|---|
| `raw/` | **읽기 전용, 절대 불변** (sha256로 사후 검증) |
| `inbox/` | 읽기 전용 (추가 조사 계획이 수집 요청을 낼 수는 있음 — fetch 대상 제안만) |
| canonical 4계층 | 읽기 전용. 쓰기는 **오직 research-promote.sh + G3 승인** 경유 |
| `research/` | 연구 루프 전용 쓰기 영역 |
| `index.md`, `log.md` | promote 시에만 원자적 갱신 |

## 4. 에이전트 역할 ↔ 실행 매핑

**서로 다른 유료 AI 다중 호출 구조가 아니다.** 마스터가 허용한 "단일 모델 순차 역할 수행" 구조를 채택한다.

| 역할 | 실행 주체 | 비용 |
|---|---|---|
| Research Orchestrator | `research-run.sh` bash 상태 머신 (state.json 기반) | 0 |
| Planner / Retriever / Analyst / Hypothesis Generator / Critic / Evidence Verifier / Report Writer | **claude CLI (구독) 1세션**, 역할별 시스템 프롬프트 파일(`research/prompts/*.md`)로 순차 호출 | 구독 내 (한계비용 0) |
| Retriever의 기계 검색 | 로컬 스크립트(grep/rag 로직 재사용) 결과를 프롬프트에 주입 — LLM이 파일시스템을 헤매지 않게 함 | 0 |
| Human Approval Gate | MVP: CLI / Phase 3: Hermes 텔레그램 | 0 |

- Orchestrator를 LLM으로 만들지 않는 이유: 순서 관리는 결정론적 문제. bash 상태 머신이 저렴하고 재현 가능하며 Safety Guard(연속 실패 중단) 구현이 쉽다.
- Critic을 별도 호출로 분리하는 이유: 같은 컨텍스트에서 생성과 비판을 연속 수행하면 자기 가설에 관대해짐 — **컨텍스트를 끊고**(새 `claude -p` 호출) 05-critique를 생성해 독립성 확보. 세션당 총 호출 수는 ≤10회로 제한.

## 5. 인간 승인 지점 (3-게이트)

| 게이트 | 시점 | 기본 동작 | 승인 수단 |
|---|---|---|---|
| **G1** 조사 계획 | 03-gaps.md 산출 후 | 자동 통과 (`--strict` 옵션 시 대기) | CLI |
| **G2** 보고서 초안 | 06-report-draft.md 산출 후 | **필수 대기** | MVP: CLI / Phase 3: 텔레그램 |
| **G3** canonical 승격 | promote 실행 시 | **필수 대기** — 가설 항목 단위 승인 (보고서 승인 ≠ 전체 승격) | `research-promote.sh <id> --approve [--items 1,3]` |

G3가 기존 AGENTS.md "Human Approval" 원칙의 실행 형태다. 승격 시 confidence는 `low` 또는 `medium`으로만 시작(`high`는 다중 출처 교차 검증 후 마스터가 수동 상향 — SCHEMA 규칙 준수).

## 6. 실패 및 복구 방식

| 상황 | 처리 |
|---|---|
| LLM 호출 실패/빈 응답 | 1회 재시도 → 실패 시 state.json에 `failed:<stage>` 기록 후 중단 + 텔레그램 보고 (CLAUDE.md Safety Guard: 연속 2회 실패 즉시 중단 준수) |
| 중단 후 재개 | `research-run.sh <id> --resume` — state.json의 마지막 완료 단계 다음부터. 각 단계 산출물이 독립 파일이라 부분 재실행 안전 |
| 특정 단계 재작업 | `--from <stage>` — 해당 단계 이후 산출물만 재생성 (이전 버전은 `<file>.bak.<ts>`로 보존) |
| 반려 | 세션 전체를 `research/_archive/`로 이동. canonical/index/log/raw **무변경 보장** (사후 `git status` + raw sha256 전수 검증) |
| promote 중 실패 | 3동작(페이지+index+log)을 임시 파일에 준비 → 검증 통과 시에만 일괄 반영. 부분 반영 상태 금지 |
| 롤백 | 승격 취소 = 해당 canonical 페이지 `_archive/` 이동 + index 제거 + log에 취소 기록 append (기존 SCHEMA 아카이브 절차 그대로) |

## 7. Vercel / 로컬 기능 분리

| 기능 | 로컬 Mac (i7 듀얼코어/16GB) | Vercel |
|---|---|---|
| 수집·인제스트·그래프 생성 | ✅ (기존 그대로) | ✗ |
| **연구 루프 전체** | ✅ claude CLI (구독) | ✗ (의도된 분리 — CLI 없음) |
| 승인·승격 | ✅ | ✗ |
| 임베딩 **생성** (Phase 2) | ✅ 밤 배치 (속도 무관) | ✗ |
| 임베딩 **검색** (Phase 2) | ✅ | ✅ (사전계산 벡터 JSON을 스냅샷에 포함, 브루트포스 내적 — 1,000편까지 충분) |
| 위키/그래프/뉴스 열람, Q&A | ✅ dev | ✅ (읽기 전용 스냅샷 + OpenRouter) |
| 연구 세션 열람 (Phase 5) | ✅ | ✅ **승인 완료분만** 스냅샷 포함 |

원칙: **쓰기와 추론은 로컬, Vercel은 읽기 전용 뷰.** 연구 중간 산출물은 절대 배포 스냅샷에 포함하지 않는다.

## 8. 기존 자동화와의 관계 (중복 없음 판정)

| 기존 | 역할 | 연구 루프와의 관계 |
|---|---|---|
| llm-wiki daily-ingest | 수집물 → canonical 후보 정리 (사서) | 연구 루프의 입력 재료를 만들어 줌. 대체·중복 아님 |
| weekly-summary | 운영 다이제스트 | 연구보고서와 텔레그램 채널이 겹침 → 메시지 제목 prefix(`[연구]` vs `[주간]`)로 구분 |
| Gate C | 그래프 구조 공백 | Gap Detector(④)의 입력 소스 중 하나로 활용 |
| daily-briefing | 뉴스 요약 | Retriever(②)의 뉴스 근거 소스로 활용 |

---

## 부록 A — RESEARCH_SCHEMA.md 초안 (Phase 1에서 확정)

- 세션 ID: `YYYYMMDD-<kebab-slug>` (log.md 날짜 형식과 정합)
- state.json 필수 키: `session_id, stage, stages_done[], approvals{G1,G2,G3}, llm_calls, created, updated`
- 04-hypotheses.md 항목 형식: `## H<n>: <제목>` + `status:` + `evidence:` (실경로 목록) + `counter:` (05-critique 참조)
- 06-report-draft.md 필수 섹션: 연구 목표 / 질문 / 근거 요약(출처 인용) / 가설·통찰 / 반론·한계 / 구현 가능성 / 공백·후속 조사 / 승격 후보 목록
- 인용 규칙: canonical은 `[[slug]]`, raw는 `^[raw/...]` — SCHEMA.md 마커 규약 그대로 재사용
- 세션당 LLM 호출 상한: 10회 (초과 시 중단·보고)
