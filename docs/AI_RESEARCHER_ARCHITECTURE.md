# AI_RESEARCHER_ARCHITECTURE.md — AI Research Operating System 아키텍처

> 작성: 2026-08-01 (전면 재작성) | 성격: **설계 문서 — 이 문서 작성으로 아무것도 구현하지 않았다.**
> 전제: `CURRENT_STATE_AUDIT.md`(v2, 2026-08-01 전면 재조사)의 실측 결과를 기반으로,
> 현재 실제로 존재하는 두 저장소(`2nd-brain-ai-system`, `drone-wiki-web`)를 하나의
> "AI Research Operating System"으로 통합 설계한다.
> 이전 버전(v1, 2026-07-31)은 부록에 보존한다 — 실제 Phase 1 구현은 이 문서가 아니라
> `research/RESEARCH_SCHEMA.md`(v2)를 따랐다.

---

## 0. 이 문서가 다루는 범위와 다루지 않는 범위

**다룬다**: 현재 실제로 동작하는 두 저장소의 구조를 있는 그대로 인정하고, 그 위에서
"연구 운영체제"로서 논리적으로 일관되게 만들기 위한 목표 구조를 제시한다.

**다루지 않는다**: 구현. 아래 어떤 섹션도 즉시 실행할 작업지시가 아니다. 마스터가
개별 항목을 골라 구현을 지시할 때까지 설계로만 남는다.

**핵심 전제 하나**: `CURRENT_STATE_AUDIT.md`가 밝힌 대로, daily-ingest 경로는
**사전 승인 게이트가 없다**(README도 이에 맞춰 정정 완료). 이 문서는 그 사실을
숨기거나 사후에 승인 게이트가 있는 것처럼 설계하지 않는다 — 대신 "왜 두 개의 서로
다른 승인 모델이 공존하는 것이 타당한가"를 §5에서 명시적으로 설계한다.

---

## 1. 목표 구조 (Target Architecture)

```
                         ┌─────────────────────────────────────────┐
                         │   2nd-brain-ai-system (지식 백엔드)       │
                         │   — 데이터 권위, 연산, 연구 루프 전담      │
                         └─────────────────────────────────────────┘
                                          │
   ┌──────────────┐   fetch    ┌─────────▼─────────┐  compile   ┌──────────────┐
   │  외부 소스     │──────────▶│      raw/           │──────────▶│  canonical    │
   │ (GitHub/RSS/  │  (불변    │  (불변 증거,         │ (사전승인  │  4계층        │
   │  arXiv/YouTube)│   저장)   │   sha256 무결성)     │  없음★)   │ entities/     │
   └──────────────┘           └─────────────────────┘           │ concepts/     │
                                          │                       │ comparisons/  │
                                          │ 사람이 지시            │ queries/      │
                                          ▼                       └──────┬───────┘
                               ┌─────────────────────┐                  │
                               │   research/          │  승인 후         │
                               │   (연구 루프)         │  개별 클레임      │
                               │   ── 사전승인 있음 ── │──승격───────────▶│
                               └─────────────────────┘                  │
                                                                         │
                                          ┌──────────────────────────────┘
                                          │ 파생 상태 생성(.ua/)
                                          ▼
                      knowledge-graph.json / embeddings.json / news-feed.json
                                          │
                                          │ sync-wiki.sh (수동 또는 04:30 cron)
                                          ▼
                         ┌─────────────────────────────────────────┐
                         │   drone-wiki-web (프레젠테이션 레이어)     │
                         │   — 정적 스냅샷 + 읽기 전용 API + Q&A     │
                         │   Vercel 배포, 상태 없음, venv/research/  │
                         │   절대 미배포                             │
                         └─────────────────────────────────────────┘

★ daily-ingest 경로: 사전 승인 없음(마스터 명시적 결정, 2026-08-01) — 대신
  매일 07:30 사후 통지(morning-report.sh)로 가시성만 확보.
  research/ 경로: 사전 승인 있음 — approve/reject + 클레임별 promote.
  이 두 갈래가 "하나의 시스템, 두 개의 위험도 등급"이라는 게 목표 구조의 핵심이다.
```

**설계 원칙 6가지** (기존 세션에서 실측으로 검증된 것만 원칙으로 승격):
1. raw는 절대 불변 — sha256로 사후 검증 가능해야 한다.
2. canonical 쓰기 경로는 정확히 2개(daily-ingest, research-promote)뿐이어야 한다 — 3번째 경로가 생기면 즉시 이 문서를 갱신한다.
3. 위험도가 다른 지식 생성 경로는 다른 승인 모델을 가져도 된다 — 단, 그 차이는 문서에 명시되어야 한다(암묵적으로 숨기지 않는다).
4. Vercel에 배포되는 것은 "이미 만들어진 정적 지식의 스냅샷"뿐이며, 그 자체로 지식을 생성하지 않는다.
5. 모든 파생 상태(`.ua/*.json`)는 원본(canonical/raw)에서 재생성 가능해야 한다 — 파생 상태 자체를 유일한 진실로 취급하지 않는다.
6. 새 기술 도입은 실측 병목이 확인된 뒤에만 한다(`TECHNOLOGY_DECISION_RECORD.md`의 재검토 트리거 방식 유지).

---

## 2. Data Flow

```
외부 소스
  │ fetch-inbox.sh (03:30 cron)
  ▼
inbox/ (임시, 분류 대기)
  │ llm-wiki 스킬 (04:00 cron) — 사전 승인 없이 즉시 컴파일
  ▼
canonical (entities/concepts/comparisons/queries) ◀────────┐
  │                                                          │ research-promote.py
  │ update-graph.sh (수동/필요시)                             │ (승인된 클레임만,
  ▼                                                          │  all-or-nothing)
.ua/knowledge-graph.json                                     │
                                                              │
raw/, canonical  ──(읽기 전용)──▶  research-search.py ────▶ research/runs/*/02-search-hits.md
                                        (하이브리드: 키워드+임베딩)      │
                                                                        ▼
                                                          research/hypotheses/*.md
                                                                        │ Critic/Verifier
                                                                        ▼
                                                          research/reviews/*.md
                                                                        │ Report Writer
                                                                        ▼
                                                          research/drafts/*.md
                                                                        │ 마스터 approve
                                                                        └──────────────┘
canonical + .ua/*  ──(sync-wiki.sh)──▶  drone-wiki-web/data/wiki/  ──▶  git push ──▶ Vercel
```

핵심 특성: **research/ 는 canonical/raw를 읽기만 하고, 오직 `research-promote.py`를
통해서만(그것도 사람이 클레임 ID를 지정했을 때만) canonical에 쓴다.** 이 화살표
방향이 거꾸로 되는 경로(canonical이 research/를 자동으로 갱신한다거나)는 설계에
없다.

---

## 3. Knowledge Flow (지식의 신뢰도 상태 전이)

```
raw evidence (불변, 신뢰도 없음 — 그냥 사실의 기록)
   │
   ▼
canonical, confidence: low|medium|high (compiled — 사람이 직접 작성했거나
   │                                     daily-ingest가 자동 컴파일)
   │
   │ (선택) research/ 로 재조사
   ▼
research claim, claim_type: fact|inference|hypothesis (discovery candidate —
   │                                                     아직 canonical 아님)
   │ Critic 반론 + Evidence Verifier 검증
   ▼
verification_status: grounded|insufficient_evidence
   │ 마스터 approve + 클레임 개별 지정
   ▼
canonical (신규), confidence: low|medium (승격 시점엔 high 불가 — 다중 출처
   │                                       교차검증 후 사람이 수동으로만 상향)
   │ update-graph.sh
   ▼
knowledge-graph.json 엣지(wikilink/contradicts) — 그래프 관계로 편입
```

`confidence: high`로 가는 유일한 경로는 "여러 독립 출처가 같은 사실을 뒷받침한다"는
것을 **사람이 시간을 두고 확인**하는 것이다 — 어떤 자동화 경로도 high를 즉시
부여하지 않는다(SCHEMA.md 원칙, research-promote.py도 준수).

---

## 4. Research Flow (5단계 파이프라인)

```
연구 목표 입력 (사람)
   │
   ▼
① Planner        (LLM)  — 목표 → 하위 질문 3~8개
   ▼
② Retriever      (기계) — 하이브리드 검색(0.6×코사인+0.4×키워드) + 그래프 이웃
   ▼                       (임베딩 없으면 자동 키워드 폴백 — 무회귀)
③ Hypothesis Gen (LLM)  — 클레임 생성, claim_type 분류(fact/inference/hypothesis)
   ▼
④ Critic         (LLM, 독립 컨텍스트) — 반론·한계·구현가능성
   ▼
⑤ Evidence Verif (LLM)  — 인용 대조, verification_status 부여
   ▼
⑥ Report Writer  (LLM)  — 13개 섹션 연구 메모 초안
   ▼
[G2: 마스터 승인] ── reject ──▶ research/_archive/ (증거로 보존, canonical 무변경)
   │ approve
   ▼
[G3: 클레임별 승격] research-promote.py --items C1,C3
   │  ├─ claim_type:fact 거부 (재진술이라 불필요)
   │  ├─ verification_status:insufficient_evidence 거부
   │  ├─ raw 출처 없으면 거부
   │  └─ wikilink 2개 미만이면 거부(부족분은 세션 내 다른 클레임에서 보충)
   ▼
canonical 신규 페이지 + index.md + log.md (원자적 3동작)
```

세션당 LLM 호출 상한 10회(기본 경로 5회 + 재시도 여유). Retriever는 LLM을 쓰지
않는다 — 기계 검색 + 로컬 임베딩 subprocess 호출뿐.

---

## 5. Human Approval — 두 갈래 위험도 모델 (이번 설계의 핵심)

`CURRENT_STATE_AUDIT.md`가 밝힌 사실: 이 시스템에는 **원래부터 승인 모델이 두 개
존재했고, 하나(daily-ingest)는 문서에 존재하지 않는 척 숨겨져 있었다.** 목표
구조는 이 두 개를 감추지 않고 **의도적으로 구분해서 설계**한다.

| | Tier 1 — 일상 컴파일 (daily-ingest) | Tier 2 — AI 연구 루프 (research/) |
|---|---|---|
| 입력 성격 | 외부 소스의 사실 재구성/요약 | AI가 만든 신규 추론·가설 |
| 승인 시점 | **사후** (생성 후 통지) | **사전** (생성 전 확정 차단) |
| 승인 수단 | 텔레그램 통지(morning-report.sh) — 정보 제공용 | CLI `approve`/`reject` + 클레임별 `--items` 지정 |
| 승인 없을 때 | 자동 확정됨(현재 상태, 마스터 결정으로 유지) | 확정 자체가 안 됨(research/_archive/로 격리) |
| 근거 | 원본 소스 링크가 명확하고, 재진술 위주라 창작 위험이 낮음 | 근거를 넘어서는 새로운 결합/추론이라 창작(환각) 위험이 있음 |
| 되돌리기 | `_archive/`로 수동 이동 (사후 롤백) | 애초에 확정 전이라 롤백 불필요 |

**이 구분이 설계로서 타당한 이유**: 두 경로의 "창작 위험"이 근본적으로 다르다.
daily-ingest는 정해진 스키마에 소스를 채워 넣는 컴파일에 가깝고(위험이 낮음),
research/는 문서에 없는 새로운 연결을 만드는 추론이다(위험이 높음). 위험이
낮은 경로에 사전 승인을 강제하면 매일 대기열이 쌓여 시스템이 무력화된다
(마스터가 Gate A/B 선택지 논의에서 이미 이 트레이드오프를 확인하고 D안을
선택함). 위험이 높은 경로에 사후 통지만 하면 검증 안 된 추론이 조용히
지식베이스에 섞여 들어간다. **따라서 다른 승인 모델을 쓰는 것 자체가
정답이며, 두 경로를 같은 모델로 통일하는 것이 오히려 잘못된 설계다.**

향후 재검토 조건: Tier 1에서 실제로 품질 문제(오정보, 저품질 페이지)가 반복
확인되면, 그때 Tier 1에도 경량 사전 검증(예: 스키마 위반만 자동 차단하는
린트 게이트)을 추가하는 것을 검토한다 — 지금 당장 만들지 않는다.

---

## 6. Failure Recovery

| 실패 유형 | 현재 동작 (실측 확인됨) | 복구 방식 |
|---|---|---|
| research 세션 LLM 호출 실패 | 동일 단계 2회 연속 실패 시 중단, `state.json.status=failed`, 텔레그램 보고 | `research-run.sh resume <id>`로 재개(마지막 완료 단계부터) |
| research 세션 반려 | `research-run.sh reject`가 세션 전체를 `_archive/`로 이동 | raw/canonical 무변경 보장(T3 테스트로 실측 검증) — 되돌릴 필요 자체가 없음 |
| 승격 검증 실패(배치 중 1건이라도) | all-or-nothing — 전체 중단, 파일 변화 0건 | 실패 항목 제외하고 `--items`로 재시도 |
| daily-ingest 자동 실행 중 `claude -p` 실패 | 이번 세션에서 실제 발견: stderr 억제로 원인 불명 상태였음 → stderr 캡처 + `--tools "" --safe-mode` 방어 적용 완료 | 다음 실패 시 로그에 원인 노출, 필요시 수동 재실행(`bash scripts/ko-summarize.sh` 등) |
| 임베딩 신선도 드리프트 | 자동 감지·복구 없음(현재 알려진 갭) | 수동 `~/2nd/.venv/bin/python scripts/embed-docs.py` 재실행 |
| sync-wiki.sh 배포 실패 | git push/vercel 배포 각각 실패 시 로그 문자열로만 알림, 부분 실패 상태 명확한 감지 로직 없음(알려진 갭) | 수동 `bash scripts/sync-wiki.sh` 재실행, `git log`/`vercel ls`로 상태 확인 |
| 노드 ID 불일치(Gate C `article:` prefix) | `update-graph.sh`가 매 실행마다 자동 정규화(병합) | 자동 — 별도 개입 불필요 |

**공통 롤백 철학**: 모든 상태가 git으로 추적되므로, 최악의 경우 `git revert`로
되돌릴 수 있다. `research/_archive/`와 raw sha256는 "무엇이 실제로 일어났는지"의
증거이며, 실패 후에도 삭제하지 않는다(SCHEMA.md append-only 원칙 연장).

---

## 7. Scalability

**현재 한계** (실측, `CURRENT_STATE_AUDIT.md` §1.7 근거):
- 모든 검색이 매 호출마다 canonical(134)+raw(33)+news(300) **전체 스캔** — 문서 수가 늘수록 선형 증가.
- `embed-docs.py`는 **전체 재임베딩만 지원**(증분 없음) — 465건에 405초, 문서가 2배로 늘면 재실행 시간도 2배.
- canonical 검색 발췌 900자 절단 — Phase 1/2 실사용 테스트에서 이미 한계 실증.
- `drone-wiki-web/lib/wiki.ts`의 `getAllPages()`는 캐시 없이 매 요청마다 전체 마크다운 재파싱(`lib/rag.ts`는 Phase 2에서 캐시 추가했지만 `wiki.ts`는 미적용 — 실측 확인된 비일관성).

**단계적 확장 전략** (지금 도입하지 않음 — 트리거 도달 시에만):

| 트리거 | 조치 |
|---|---|
| 임베딩 재생성이 매번 부담될 정도로 느려짐(문서 급증) | 콘텐츠 해시 기반 증분 임베딩(변경분만 재계산) |
| canonical 500편 초과 | reranker 도입 검토(`TECHNOLOGY_DECISION_RECORD.md` #10) |
| canonical 1,000편 초과 | 브루트포스 벡터 검색 → LanceDB(#5) |
| 그래프 엣지 5,000 초과 또는 다중홉 질의가 병목 | KuzuDB 검토(#8) |
| `/api/pages` 응답 지연 체감 | `wiki.ts`에도 `rag.ts`와 동일한 모듈 레벨 캐시 적용(가장 저비용·최우선 후보) |

**Vercel 콜드스타트**: 모듈 레벨 캐시(Phase 2, `rag.ts`만 적용)로 웜 인스턴스
동안의 반복 파일 읽기는 이미 해소됨. 콜드스타트 자체(워커 재시작 시 1회 로드)는
문서 수가 수천 단위가 되기 전까지는 문제가 아니다.

---

## 8. Directory Structure

```
~/2nd/ (2nd-brain-ai-system)
├── raw/{articles,notebooklm,papers/<topic>,transcripts,web,youtube}/   # 불변 증거
├── entities/ concepts/ comparisons/ queries/                          # canonical 4계층
├── inbox/ (+ processed/)                                              # 분류 대기·이력
├── research/
│   ├── runs/<session-id>/        # 과정 파일(goal/questions/search-hits/state)
│   ├── hypotheses/<session-id>.md
│   ├── reviews/<session-id>.md
│   ├── drafts/<session-id>.md
│   ├── prompts/                  # 역할별 고정 프롬프트 5종
│   └── _archive/<session-id>/    # 반려·디버그 세션 보존
├── .ua/ (gitignore)              # 파생 상태: knowledge-graph.json, embeddings.json,
│                                 #   news-feed.json, daily-briefing.json, gap-report.md
├── .venv/ (gitignore, 312MB)     # 임베딩 전용 격리 Python 3.11
├── scripts/                      # 16개 자동화 스크립트
├── docs/                         # 이 문서를 포함한 설계·감사 문서
├── AGENTS.md / SCHEMA.md / README.md / README.ko.md
├── index.md / log.md             # 카탈로그 + append-only 이력
└── _archive/                     # 완전 대체된 canonical 페이지

~/projectm/drone-wiki-web/ (drone-wiki-web)
├── app/
│   ├── api/{chat,graph,pages}/route.ts
│   └── {chat,graph,news,wiki}/page.tsx, page.tsx(홈)
├── lib/{rag,wiki,news,types}.ts
├── data/wiki/                    # sync-wiki.sh가 채우는 정적 스냅샷(git 추적)
│   ├── {entities,concepts,comparisons,queries}/
│   └── .ua/{knowledge-graph,news-feed,daily-briefing,embeddings}.json
├── scripts/sync-wiki.sh
└── vercel.json / package.json
```

---

## 9. API Structure

현재 실제 API 3개(모두 Next.js Route Handler, `drone-wiki-web`):

| 라우트 | 메서드 | 입력 | 출력 | 비고 |
|---|---|---|---|---|
| `/api/chat` | POST | `{question}` | `{answer, sources[], newsSources[], mode}` | OpenRouter 1순위 → 로컬 claude CLI 2순위. `maxDuration: 90` |
| `/api/graph` | GET | 없음 | `{nodes[], edges[]}` | `domain` 없는 노드는 응답에서 제외됨(실측: 19%) |
| `/api/pages` | GET | 없음 | 페이지 메타 배열 | 캐시 없음(§7 스케일링 이슈) |

**목표 구조에서 추가 검토 대상(설계만, 미구현)**: Phase 5 계획대로 `research/`의
**승인 완료 세션만** 노출하는 읽기 전용 API(`/api/research`)를 추가할 수 있다.
단, 이 API는 `state.json.status`가 `approved`인 세션의 `drafts/*.md`만 반환해야
하며, `runs/`/`hypotheses/`/`reviews/`(원자료)는 절대 웹에 노출하지 않는다 —
`research/`가 애초에 `sync-wiki.sh` 대상이 아니라는 원칙(§1 원칙 4)을 API
레벨에서도 유지해야 한다.

---

## 10. Deployment

| | 로컬 Mac (Intel i7-7567U, 16GB) | Vercel |
|---|---|---|
| raw/canonical 쓰기 | ✅ 유일한 쓰기 위치 | ❌ (읽기 전용 스냅샷만) |
| research/ 전체 루프 | ✅ | ❌ (venv/CLAUDE.md 미배포로 원천 차단) |
| 임베딩 생성 | ✅ (.venv, 배치) | ❌ |
| 하이브리드 검색(질의 임베딩 포함) | ✅ | ❌ (venv 없어 자동 키워드 폴백) |
| 위키/그래프/뉴스 열람, AI Q&A | ✅ (dev) | ✅ (프로덕션) |
| 배포 트리거 | `sync-wiki.sh` 수동 또는 04:30 cron | `git push` 후 스크립트 내 `vercel --prod` 직접 호출(Git 연동 자동배포 없음) |

**분리 원칙**: 쓰기와 연구는 로컬에만 존재한다. Vercel은 "이미 승인·확정된
지식의 스냅샷을 보여주는 창구"로 설계를 고정한다 — 이 경계를 허무는 변경
(예: Vercel에서 canonical을 직접 쓰게 하는 것)은 이 문서의 원칙 4·5 위반이다.

---

## 11. Security

- **비밀정보**: `.env`, 인증 파일은 AI가 읽거나 출력하지 않는다(이번 세션 전체에서 준수). `.gitignore`가 `.env*`, `*.credentials.json`, `.venv/` 등을 이미 포괄(실측 확인).
- **무결성**: raw는 sha256로 사후 변조 검증 가능. canonical 프론트매터의 `sources`는 실존 경로만 허용(research-promote.py가 실제로 이를 강제하는 것을 실측 검증함).
- **승격 검증**: `research-promote.py`가 인용 해석·wikilink 개수·raw 출처 존재를 기계적으로 강제 — 그러나 **추론의 논리적 타당성(예: 논리적 비약 여부)까지는 검증하지 않는다.** 이는 Critic의 서술과 사람의 최종 판단에 맡긴다 — 자동화가 대신할 수 없는 지점으로 명시적으로 남겨둔다.
- **알려진 갭(§5와 연결)**: daily-ingest 경로는 콘텐츠 안전성(사실관계 오류, 저품질 요약)에 대한 자동 검증이 없다 — 이는 "버그"가 아니라 마스터가 인지하고 수용한 위험(D안 결정)이다. 이 문서는 그 결정을 재확인만 하고 임의로 게이트를 추가하지 않는다.
- **웹 노출 경계**: `research/`(미승인 포함)는 `sync-wiki.sh` 대상이 아니므로 구조적으로 웹에 노출될 수 없다 — API 신설 시(§9) 이 경계를 API 레벨에서도 재확인해야 한다.

---

## 12. Technology Decision (요지 — 전체는 `TECHNOLOGY_DECISION_RECORD.md`)

| 채택 | 보류(트리거 도달 시) | 제외 |
|---|---|---|
| Hermes Agent, OpenRouter, Claude Code, multilingual-mpnet(로컬 임베딩) | LangGraph, LanceDB, KuzuDB, reranker | LiteLLM, Qdrant, Chroma, Neo4j |

이번 설계에서 추가로 확정한 결정 1건: **프로덕션 웹 Q&A의 임베딩 기반 교차언어
검색은 도입하지 않는다**(2026-08-01 마스터 결정) — OpenRouter 임베딩 API가
실존함을 검증했으나, 로컬 문서 벡터(multilingual-mpnet)와 다른 모델이라 그대로
연결하면 벡터공간이 달라 무의미한 유사도가 나온다는 문제를 발견했고, 이를
해결하려면 매 웹 질문마다 영구적인 유료 API 비용이 발생해 비용 대비 이득이
낮다고 판단했다. 로컬 연구 파이프라인과 로컬 dev는 이미 하이브리드 검색이
작동한다.

---

## 부록 — v1(2026-07-31) 설계안

이전 버전은 세션 단일 폴더 구조, G1/G2/G3 3단 게이트, `status/evidence/counter/
verifier_note` 클레임 필드를 제안했으나, 마스터의 후속 상세 스펙에 따라 위 §4~5의
더 단순한 구조로 실제 구현되었다. v1 전문은 git 이력(`git log -p -- docs/
AI_RESEARCHER_ARCHITECTURE.md`)에서 확인 가능하다.
