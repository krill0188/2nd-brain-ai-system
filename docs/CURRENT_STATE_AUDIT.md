# CURRENT_STATE_AUDIT.md — 현재 시스템 실태 감사

> 작성: 2026-07-31 | 작성자: Claude Code (AI 시스템기획 PM)
> 대상: `~/2nd` (krill0188/2nd-brain-ai-system) + `~/projectm/drone-wiki-web` (krill0188/drone-wiki-web)
> 성격: 조사 전용 산출물. 이 문서 작성 과정에서 코드·설정·raw·canonical 무변경.

---

## 0. 감사 방법

- 두 저장소의 README / CLAUDE.md / AGENTS.md / SCHEMA.md 전문 확인
- `lib/rag.ts`, `app/api/{chat,graph,pages}/route.ts`, `lib/wiki.ts` 등 코드 직접 열람
- `.ua/knowledge-graph.json` 구조 파이썬 파싱 (노드/엣지/타입 분포 실측)
- Hermes cron 6잡 상태 실측 (`hermes cron list` — 2026-07-31 실행 성공 로그 확인)
- `scripts/` 자동화 체인 7종 열람
- 하드웨어 실측: Intel i7-7567U (2코어 4스레드, 3.5GHz), RAM 16GB, GPU 없음

## 1. 시스템 한 문장 정의

**출처 무결성 거버넌스(raw 불변·sha256·provenance)가 뛰어난 드론 지식 "수집·정리·발행" 파이프라인이며, "연구(추론·가설·검증)" 계층은 아직 존재하지 않는 시스템.**

## 2. 실측 규모 (2026-07-31 기준)

| 항목 | 수치 |
|---|---|
| canonical 문서 | 120편 (concepts 104 / entities 13 / comparisons 1 / queries 2) |
| raw 증거 | 33편 (articles/papers/transcripts/web/youtube) |
| inbox 대기 | 0편 (새벽 체인 정상 소화 중) |
| 지식그래프 | 137노드 / 421엣지 |
| 뉴스 피드 | 370건 (`.ua/news-feed.json`, sha256 무결성 필드 보유) |
| Hermes cron | 6잡 전부 active, 최근 실행 전부 ok |

## 3. 실제 구현·검증된 기능 ✅

### 3.1 수집 계층
- `scripts/fetch-inbox.sh` (632줄): 드론 7도메인(flight-control/comms-protocol/hardware/gcs-software/ops-mission/regulations/ai-autonomy) 수집. GitHub 릴리즈 13소스 + RSS 5소스 + 방산·정부사업·채용 피드 + arXiv/Crossref/Zotero 학술 + YouTube 27채널(45일 필터). RSS 중복방지(`.rss-seen.txt`), sha256 무결성.
- `scripts/zotero-ingest.py`: Zotero → `raw/papers/<topic>/` 자동 인제스트, SCHEMA 태그 기반 분류.
- `scripts/ko-summarize.sh`: 영문 뉴스 한글 요약 부가 — **원문 무수정**(sha256 보존) 원칙 준수 확인.

### 3.2 정리·거버넌스 계층
- SCHEMA.md 3계층 계약: Layer1 raw 불변 증거 / Layer2 canonical 4디렉터리 / Layer3 index·log 메타.
- canonical frontmatter 9필드 강제: title/created/updated/type/tags/sources/**confidence/contested/contradictions**.
- 원자적 3동작: 페이지 변경 + index.md 동기화 + log.md append (append-only).
- claim-level 출처 마커 규약: `^[raw/<kind>/<file>.md]`.
- Hermes cron `2nd-daily-ingest`(04:00): inbox → canonical 후보 컴파일 → processed 이동.

### 3.3 그래프 계층
- `scripts/update-graph.sh`: frontmatter 파싱 → knowledge-graph.json 갱신.
- Gate C (`gate-c-analyze.sh`, Understand Anything): 구조 분석 + 그래프 공백 탐지, claude -p 실패 시 OpenRouter 폴백.

### 3.4 발행·웹 계층
- `sync-wiki.sh`: canonical 4디렉터리 + 뉴스 + 브리핑 + 그래프를 `data/wiki/` 스냅샷으로 rsync → git push → Vercel CLI 프로덕션 배포. 변경 없으면 스킵.
- 웹 Q&A (`app/api/chat/route.ts`): RAG 검색 5건 + 뉴스 4건 + 그래프 이웃 4건으로 프롬프트 구성 → OpenRouter(claude-haiku-4.5) 1순위 → 로컬 claude CLI 2순위 폴백. 출처 `[1]`/`[N1]` 인용 지침 포함.
- 그래프 뷰어(react-force-graph-2d), 위키/뉴스 페이지.

### 3.5 자동화 체인 (Hermes cron 6잡 — 전부 실측 active)
| 시각 | 잡 | 역할 |
|---|---|---|
| 03:30 | 2nd-daily-fetch | 수집 + 브리핑 |
| 04:00 | 2nd-daily-ingest | inbox → canonical 후보 |
| 04:30 | 2nd-sync-dronewiki | 웹 동기화 + 배포 |
| 07:30 | 2nd-morning-report | 체인 검증 + 브리핑 텔레그램 |
| 월 05:00 | 2nd-weekly-lint | canonical 감사 |
| 월 09:00 | 2nd-weekly-summary | 주간 다이제스트 + 수집 우선순위 제안 |

## 4. 부분 구현된 기능 ⚠️

| 기능 | 문서/명칭상 주장 | 실제 구현 |
|---|---|---|
| "TF-IDF 검색" (`rag.ts`) | TF-IDF | **IDF 가중 없는 hit count** + 제목 매칭 ×2. TF(빈도)도 미반영 — 토큰 집합(Set) 교집합 크기. 청킹 없음(문서 단위), excerpt 앞 600자 고정 |
| GraphRAG | 그래프 결합 검색 | 1-hop 이웃 **나열**만. bare slug 노드(112개)는 정상 매칭(실측 5/5), `article:` prefix 노드(21개)는 seed와 매칭 불가 → 확장에서 고립 |
| 모순 관리 | contested/contradictions | frontmatter **필드만 존재**. 탐지·기록 전부 수동. 자동 대조 없음 |
| 지식 공백 탐지 | Gate C | 그래프 **구조** 공백(고아 노드, 미해결 링크)만. 질문 단위 "무엇을 모르는가"는 미탐지 |
| 조사 계획 | weekly-summary | "수집 우선순위 제안" 수준. 연구 질문 기반 계획 아님 |
| 보고서 | daily-briefing.sh | 뉴스 2장 요약(claude -p). 연구보고서(질문→근거→가설→검증) 아님 |

## 5. 문서에만 존재하는 기능 ❌

1. **인간 승인 워크플로** — AGENTS.md "Human Approval" 섹션에 원칙은 명문화("LLM 제안은 discovery candidate, 인간 검증 없이 승격 금지")되어 있으나, 승인 요청 전달 → 승인/수정/반려 처리 → 승격 실행의 **실행 경로가 없음**. 현재는 마스터가 수작업으로 canonical을 만드는 것이 유일한 경로.
2. **연구 루프** — 목표 해석/질문 분해/가설 생성/반론 탐색/구현가능성 평가에 해당하는 코드·스크립트·데이터 구조 전무.
3. **가설 저장 계층** — AI 산출물(가설·통찰 후보)을 담을 합법적 위치가 스키마에 없음. inbox는 "분류 대기 수집물"이지 가설 스테이징이 아님.

## 6. 위험 요소 🔴

| # | 위험 | 상세 | 심각도 |
|---|---|---|---|
| R1 | rag.ts 무캐시 전체 로드 | 매 요청마다 120편 전부 디스크 재로드+재토큰화. 수백 편 도달 시 Vercel 함수 지연·비용 증가 | 중 (성장 시) |
| R2 | chat 폴백의 dead path | Vercel에는 claude CLI가 없어 `spawn("claude")` 폴백은 항상 실패. OpenRouter 키 문제 시 사용자는 90초 대기 후 실패 메시지 | 하 |
| R3 | 그래프 생성기 2원화 | update-graph.sh(bare slug)와 Understand Anything(`article:` prefix)이 같은 파일에 다른 ID 체계로 기록 — 스키마 드리프트 진행 중. 엣지 타입도 wikilink 380 / related 33 / categorized_under 8로 의미 관계 부재 | 중 |
| R4 | 미승인 콘텐츠 노출 경로 | sync-wiki.sh가 canonical 4디렉터리를 무조건 웹 배포. 가설을 canonical에 두는 순간 자동 공개됨 → **연구 산출물은 반드시 4계층 밖(research/)에 격리해야 함** | 상 (설계로 차단) |
| R5 | 검색 언어 갭 | 한/영 혼용 코퍼스에서 토큰 매칭은 교차 언어 질의 실패 (예: "군집 비행" → `swarm-coordination` 미검색) | 상 |
| R6 | 승인 없는 자동 체인 | daily-ingest가 canonical 후보를 자동 컴파일 — 현재는 "후보" 단계에서 멈추지만, 연구 루프 추가 시 이 경계가 흐려질 수 있음. 승격은 반드시 별도 승인 스크립트로만 | 중 |

## 7. 결론

- 거버넌스·수집·발행은 **성숙 단계** (자동화 체인 실측 정상).
- 연구원 시스템 관점 완성도는 **25/100** — 부족한 것은 "연구 상태 관리 + 가설 스테이징 + 의미 검색 + 의미 관계 그래프 + 승인 실행 워크플로" 5개이며, 전부 기존 기능을 폐기하지 않고 **추가 계층**으로 해결 가능.
- 상세 목표 구조는 `AI_RESEARCHER_ARCHITECTURE.md`, 실행 순서는 `AI_RESEARCHER_ROADMAP.md` 참조.
