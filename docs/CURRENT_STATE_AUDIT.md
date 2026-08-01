# CURRENT_STATE_AUDIT.md — 현재 시스템 실태 감사 (v2, 전면 재조사)

> 작성: 2026-08-01 | 작성자: Claude Code (AI CTO 역할)
> 대상: `~/2nd` (krill0188/2nd-brain-ai-system) + `~/projectm/drone-wiki-web` (krill0188/drone-wiki-web)
> 성격: **조사 전용.** 이 문서 작성 과정에서 코드·설정·raw·canonical을 일절 수정하지 않았다.
> 전제: v1(2026-07-31 작성)은 이후 Phase 0~2 구현·13단계 연구루프 완성·그래프 스키마
> 확장 등 대규모 변경을 전혀 반영하지 못한 상태라 폐기하고 처음부터 재조사했다.
> 원칙: 문서·커밋 메시지·이전 로드맵의 "완료" 주장을 그대로 믿지 않고, 실제 파일과
> 로그를 직접 열어 재검증했다.

---

## 0. 한 문단 요약

**2nd-brain-ai-system**은 수집(자동)·정리(자동)·연구(반자동, 인간 승인)·발행(자동) 파이프라인이 실제로 돌아가는 성숙한 시스템이지만, **README가 명시적으로 주장하는 핵심 거버넌스 장치("Gate B 텔레그램 승인 없이는 어떤 정식 변경도 확정되지 않는다")가 실제로는 존재하지 않는다** — 이것이 이번 재조사에서 발견한 가장 중요한 사실이다. **drone-wiki-web**은 그 지식을 보여주는 정적 스냅샷 기반 웹뷰로, 코드 품질은 양호하나 캐시 부재·죽은 의존성·그래프 데이터 손실 등 자잘한 기술부채가 있다. 두 저장소 모두 **자동화된 테스트가 전무**하다.

---

## 1. 2nd-brain-ai-system

### 1.1 실측 규모 (2026-08-01 재확인)

| 항목 | 수치 |
|---|---|
| canonical 문서 | 134편 (concepts 114 / entities 17 / comparisons 1 / queries 2) |
| raw 증거 | 33편 |
| inbox 처리 이력 | 174건 (`inbox/processed/`), 미처리 잔량 0건 |
| research/ 세션 | 완료 3건(성공 2·반려 1 보존) + 디버그 실패 5건(증거 보존) |
| knowledge-graph.json | 150노드 / 486엣지 |
| embeddings.json | 465건, 3.83MB, **2026-07-31 23:20 생성 — 이후 승격된 canonical 2편은 미포함(신선도 드리프트)** |
| `.venv` (임베딩 전용) | 312MB |
| scripts/ 총량 | 16개 파일, 3,663줄 |
| 자동화 테스트 | **0건** |

### 1.2 실제 구현되어 동작 확인된 기능

- **수집**: `fetch-inbox.sh`(632줄) — 7도메인, GitHub 릴리즈/RSS/arXiv·Crossref/YouTube. 오늘 아침(08-01 03:31) 정상 실행 로그 확인.
- **한글 요약·브리핑**: `ko-summarize.sh`/`daily-briefing.sh` — **재조사 중 실제 장애 발견**: 08-01 새벽 자동실행에서 `claude -p` 호출이 stderr 없이 실패해 영문기사 20건의 한글요약이 누락되어 있었음(로그: `ko-summarize: claude 호출 실패`, `briefing: claude 호출 실패`). 이번 세션에서 수동 처리 + stderr 캡처 + `--tools "" --safe-mode` 방어 수정을 적용했으나, **자동실행 환경에서 왜 실패했는지 근본 원인은 확인하지 못했다**(수동 실행은 항상 성공). 내일 새벽 실행 로그로 재확인 필요.
- **정리(Gate C만)**: `gate-c-analyze.sh` — 그래프 구조 통계 + `claude -p` 해석, `.ua/gap-report.md` 생성. 실존 확인.
- **그래프**: `update-graph.sh` — 노드(confidence/status 포함)·엣지(evidence/confidence/type 포함, contradicts 자동 생성) 갱신 + Gate C `article:` prefix 중복 자동 병합. 재실행 검증 완료(8건 병합, 445개 기존 엣지 필드 백필 확인).
- **임베딩**: `embed-docs.py` — 격리 Python 3.11 venv(시스템 3.14는 onnxruntime 미지원)로 canonical+raw+news 465건 다국어 임베딩. **자동 재생성 크론 없음 — 수동 실행 전제**.
- **연구 루프(Phase 1)**: `research-run.sh` — Planner→Retriever(하이브리드 검색)→Hypothesis→Critic→Verifier→Report, 5회 LLM 호출. 실제 세션 3건으로 검증(성공 2, 반려 1).
- **canonical 승격(13단계)**: `research-promote.py` — `claim_type:fact` 거부, `insufficient_evidence` 거부, wikilink/provenance 검증, all-or-nothing. 실제로 canonical 페이지 2건이 이 경로로 생성됨(`concepts/gps-uav-imu.md`, `concepts/micro-drone-slam-imu-vio-lidar-*.md`) — **이 세션 최초로 AI가 생성한 지식이 인간 승인을 거쳐 정식 지식베이스에 실제로 반영된 사례**.
- **웹 동기화**: `sync-wiki.sh`(drone-wiki-web 내) — canonical+뉴스+그래프+임베딩을 정적 스냅샷으로 복사 후 git commit+push+Vercel 배포. 수동/cron 실행 모두 성공 확인.

### 1.3 문서상에만 존재하는 기능 (실제로 없음을 확인) 🔴

**가장 중요한 발견: Gate A/B 및 텔레그램 HITL 승인 게이트가 실제로 존재하지 않는다.**

- `README.ko.md`는 다음을 명시적으로 주장한다:
  > "운영 워크플로우는 **캡처 → Hermes Cron → Gate A/B/C → 텔레그램 승인 → 정식화** 순서로 진행됩니다... **명시적 `approve` 답변 없이는 어떤 정식 변경도 확정되지 않습니다.**"
- 실측 결과:
  - `Gate A`, `Gate B`에 해당하는 스크립트/설정이 저장소 어디에도 없다(`gate-c-analyze.sh`만 실존).
  - 실제 자동화를 실행하는 `~/.hermes/skills/research/llm-wiki/SKILL.md`(507줄)를 전문 검색한 결과 telegram·approval·HITL 관련 언급이 **전혀 없다** — 이 스킬은 조건에 맞으면 바로 canonical 페이지를 생성·컴파일한다.
  - `log.md` 전체(수십 건의 `ingest` 항목)에 "approve", "텔레그램 승인" 언급이 **0건**이다.
  - 실제로 지난 며칠간 새 canonical 페이지 20여 건(auterion.md, bitcraze.md, kite-gcs.md 등)이 **어떤 승인 절차도 거치지 않고** 자동 생성되었다(이번 세션에서 그 상태 그대로 커밋한 이력으로 직접 확인).
  - 결론: **일상적인 daily-ingest 파이프라인은 AGENTS.md 자신의 원칙("사람 검증 없이 가설을 정식 지식으로 승격하지 않는다")을 실제로는 지키지 않고 있다.** 이는 이 세션에서 새로 만든 `research/` 경로(진짜로 인간 승인 게이트가 있음)와는 별개의, 기존부터 있던 daily-ingest 경로의 문제다.
- **위험도**: 상 — 문서가 약속하는 핵심 안전장치가 실제로 없다는 것은, 그 문서를 신뢰해 의사결정하면 안 된다는 뜻이다. README 수정 또는 실제 Gate A/B 구현 중 하나가 필요하다(이번 조사에서는 수정하지 않음, 보고만).

### 1.4 부분 구현/미완성 기능

| 기능 | 상태 |
|---|---|
| 임베딩 신선도 | 자동 재생성 없음 — 현재 이미 2편 누락된 채로 드리프트 시작됨. Phase 2가 "배치 사전계산"까지만 하고 "언제 재계산할지" 정책을 정하지 않음 |
| 프로덕션 웹 하이브리드 검색 | 로컬 dev·연구 파이프라인만 활성. Vercel은 여전히 키워드 전용(마스터가 비용 이유로 명시적 보류) |
| Phase 3(텔레그램 양방향 연구 승인) | 조사만 하고 미착수(구현 경로 불명확, 라이브 인프라 리스크로 보류) |
| Phase 4(검증 자동화 심화) | 착수 안 함 |
| Phase 5(웹 연구 탭) | 착수 안 함 |
| `research-promote.py`의 confidence 산정 | inference→medium, hypothesis→low 고정 매핑 — Critic의 실제 반론 강도(예: T1 C4처럼 "논리적 비약"이라는 강한 지적)를 반영하지 않음. 기계적 검증(인용 해석 가능 여부)만 하고, 추론의 질적 타당성은 전적으로 사람 판단에 위임 |

### 1.5 기술 부채 (중복 코드)

- **frontmatter 파서가 최소 3곳에 독립적으로 존재**: `scripts/embed-docs.py`, `scripts/research-search.py`(거의 동일한 코드 복붙), `scripts/update-graph.sh`(별도의 더 단순한 정규식 버전). 공유 모듈(`scripts/lib/`) 없음 — 한 곳에서 버그를 고쳐도 나머지에 반영 안 될 위험이 상존(실제로 이번 세션에서 research-promote.py의 YAML 이스케이프 버그를 고쳤지만 embed-docs.py/research-search.py의 파서는 같은 취약점을 안 고친 채로 남아있음 — 제목에 큰따옴표가 있는 문서를 이 스크립트들이 다시 쓰는 경우는 없어서 지금 당장 터지진 않지만 잠재적 위험).
- **하이브리드 검색 스코어링 로직이 언어를 넘어 2중 구현**: `scripts/research-search.py`(Python)와 `lib/rag.ts`(TypeScript)가 동일한 공식(0.6×코사인+0.4×정규화 키워드, MIN_COSINE_INCLUDE=0.35)을 각각 독립적으로 구현. 이번 세션엔 둘을 수동으로 동기화했지만, 공유 스펙 문서나 자동 동기화 장치가 없어 다음 변경에서 둘이 갈라질 위험이 있다.
- **slugify 로직 중복**: `research-promote.py`와 `zotero-ingest.py`에 유사 로직 별도 존재.

### 1.6 구조적 문제

- **그래프 API의 domain 필터로 인한 데이터 손실**: `drone-wiki-web/lib/wiki.ts`의 `getKnowledgeGraph()`가 `n.domain` 값이 없는 노드를 통째로 걸러낸다 — 실측 결과 150개 노드 중 **28개(19%)**가 domain 미설정으로 웹 그래프 뷰에서 보이지 않는다. 버그라기보다는 암묵적 설계 결정인데, 문서화되어 있지 않아 "그래프에 뭔가 빠져 보인다"는 향후 혼란의 소지.
- **동기화 지연**: canonical 승격/생성이 `sync-wiki.sh` 실행(수동 또는 04:30 cron) 전까지 웹에 반영 안 됨 — 실측: 오늘 09:27경 승격한 페이지 2건이 08:49 마지막 동기화 스냅샷에는 없음(정상이지만, 최대 24시간 지연이 있을 수 있다는 점은 문서화 안 됨).
- **`.ua/` 파생 상태 파일들이 서로 다른 스크립트가 각자 다른 시점에 갱신** — knowledge-graph.json, embeddings.json, news-feed.json이 서로 다른 cron/수동 트리거로 갱신되어 상호 정합성을 보장하는 장치가 없다(예: 임베딩이 그래프보다 최신일 수도, 반대일 수도 있음).

### 1.7 확장성 문제

- 모든 검색이 매 호출마다 **디스크 전체 스캔**(canonical 134 + raw 33 + news 300) 방식 — 현재는 수백 ms대지만, 문서 수가 수천 단위로 늘면 선형으로 느려진다. 인덱싱/캐싱 계층 없음.
- `embed-docs.py`는 **전체 재임베딩만 지원**(증분 없음) — 문서가 늘수록 재실행 시간이 선형 증가(현재 465건에 405초).
- canonical 검색 스니펫이 문서당 900자(raw)/900자(canonical 발췌)로 절단됨 — Phase 1/2 실사용 테스트에서 이미 "스니펫 밖 근거를 못 본다"는 한계가 실증됨(`RESEARCH_SCHEMA.md` § 알려진 한계에 기록됨).

---

## 2. drone-wiki-web

### 2.1 구조

```
app/
  api/{chat,graph,pages}/route.ts   — 3개 API 라우트
  {chat,graph,news,wiki}/page.tsx   — 4개 페이지 + 홈
lib/
  rag.ts (290줄) — 검색(하이브리드) + 그래프 이웃 확장
  wiki.ts (115줄) — 페이지 로딩 + 마크다운 렌더링 + 그래프 API
  news.ts (82줄) — 뉴스/브리핑 로딩
  types.ts (52줄)
```

의존성: Next.js 16.2.12, React 19.2.4, gray-matter, remark 계열, react-force-graph-2d, **@anthropic-ai/sdk(사용 안 함 — 죽은 의존성)**.

### 2.2 실제 동작 확인된 기능

- 위키 목록/상세 페이지, 그래프 뷰, 뉴스 피드, AI Q&A(OpenRouter 1순위 → 로컬 claude CLI 2순위 폴백).
- `npm run build` 정상(142페이지 생성, 이번 세션에서 재확인), TypeScript 컴파일 에러 0건.
- 하이브리드 검색: `.venv` 존재 여부로 자동 분기(로컬만 활성) — 이번 세션 tsx로 직접 실행 검증.

### 2.3 문서상에만 존재하거나 확인 안 되는 것

- 별도의 "AGENTS.md"는 Next.js 16 버전 경고문 한 줄뿐, 이 저장소 고유의 아키텍처 설명 문서가 없다(README.md는 있으나 이번 조사에서 상세 대조는 안 함 — 2nd 저장소만큼 정교한 거버넌스 문서 자체가 애초에 없음, 이건 "거짓 주장"이 아니라 "문서 자체가 얇다"는 것).

### 2.4 기술 부채

- **`@anthropic-ai/sdk` 완전 미사용**: `grep` 결과 코드베이스 어디에서도 import되지 않음. package.json에만 존재 — 불필요한 설치 용량 + 감사 대상만 늘림.
- **`lib/wiki.ts`의 `getAllPages()`가 캐시 없이 매 호출마다 전체 재파싱**: `/api/pages` 호출마다 134개(+증가 중) 파일을 다시 읽고 remark로 마크다운을 다시 HTML 변환한다. `lib/rag.ts`는 이번 세션에 모듈 레벨 캐시를 추가했지만 `wiki.ts`는 그대로 방치됨 — 같은 저장소 안에서 캐싱 정책이 파일마다 다르다.
- **테스트 코드 전무**.

### 2.5 구조적 문제

- `getKnowledgeGraph()`의 domain 필터 문제는 §1.6에서 이미 지적(이 저장소의 코드가 원인).
- `sync-wiki.sh`가 `git commit`+`git push`+`vercel --prod`를 한 스크립트 안에서 전부 수행 — 실패 지점이 여러 곳(git 인증, Vercel CLI, 네트워크)인데 부분 실패 시 상태를 알기 어려움(로그 문자열 매칭에 의존).

---

## 3. 두 저장소 공통 문제

1. **자동화 테스트 0건** — 2nd-brain(Python/bash 16개 스크립트, 3,663줄)과 drone-wiki-web(TypeScript, ~540줄 lib) 어디에도 단위/통합 테스트가 없다. `MVP_ACCEPTANCE_TESTS.md`의 T1~T3는 사람이 수동으로 실행하고 눈으로 확인하는 절차이지, CI에서 자동 재현되는 테스트가 아니다.
2. **핵심 알고리즘(하이브리드 검색)의 언어 간 중복** — 앞서 기술.
3. **관측 가능성 부재** — 두 저장소 모두 구조화된 로그·메트릭 수집 없이, 텍스트 로그 파일과 `grep`에 의존해 문제를 진단한다(이번 감사에서 ko-summarize 실패를 찾은 방법도 결국 로그 파일을 직접 열어본 것).

---

## 4. 총평

- **강점**: 수집·정리·검색·연구·승격·발행까지 전 과정이 실제로 동작하는 것으로 확인됐고, 이번 세션에서 처음으로 "AI가 만든 지식이 인간 승인을 거쳐 실제 지식베이스에 반영"되는 전체 루프가 검증됨.
- **가장 심각한 문제**: README가 약속하는 daily-ingest의 텔레그램 승인 게이트(Gate A/B)가 실재하지 않는다 — 이는 코드 품질 문제가 아니라 **거버넌스 문서와 실제 시스템 동작의 불일치**이며, 마스터가 "승인 없이는 안 바뀐다"고 믿고 있다면 그 믿음은 현재 사실이 아니다.
- **두 번째로 심각한 문제**: 자동화된 테스트가 전혀 없어, 이번 세션에서 발견한 것과 같은 회귀(ko-summarize 자동실행 실패 등)가 사람이 우연히 로그를 열어보기 전까지 감지되지 않는다.
- 나머지(중복 코드, 캐시 부재, 도메인 필터로 인한 그래프 데이터 손실, 임베딩 신선도 드리프트)는 지금 당장 장애를 일으키지는 않지만, 코퍼스가 계속 자동으로 늘어나는 구조(매일 신규 canonical 생성)라 방치하면 누적된다.

이 문서는 조사 결과만 기록한다. 위 발견에 대한 대응(설계·구현)은 마스터의 별도 지시가 있을 때 진행한다.
