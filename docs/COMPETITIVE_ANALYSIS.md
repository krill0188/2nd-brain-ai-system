# COMPETITIVE_ANALYSIS.md — AI 연구원 경쟁 비교 분석

> 작성: 2026-08-02 | 성격: **분석 문서 — 구현하지 않았다.**
> 비교 대상: NotebookLM, ChatGPT(Deep Research/Agent Mode), Gemini(Deep
> Research), Perplexity(Labs/Computer), Claude(Projects/Science Workbench).
> 방법론: 각 제품 공식 발표·리뷰 매체의 2026년 시점 공개 자료를 웹검색으로
> 확인했다(§8 참고자료). 각 사의 비공개 내부 구조는 추측하지 않고, 공개된
> 기능 설명만 근거로 삼는다 — 이 저장소의 기존 원칙(추측 대신 증거)을 그대로
> 적용한다.

---

## 1. 비교 축

경쟁사 5개는 전부 "검색 후 종합"이 핵심이다. 이 저장소가 이미
`RESEARCH_ENGINE.md`에서 정의한 구분("NotebookLM은 검색한다, 우리는
연구한다")을 5개 전부로 확장해 다음 6개 축으로 비교한다.

1. **증거 기반(Evidence)**: 어디서 근거를 가져오는가 — 사용자 제공 자료만? 실시간 웹 전체?
2. **지속성(Persistence)**: 결과가 세션이 끝난 뒤에도 구조화된 형태로 남는가?
3. **주장 유형화(Claim Typing)**: 사실/추론/가설을 구분하고 각각 다르게 검증하는가?
4. **반증 절차(Counter-Evidence)**: 자기 주장에 반대되는 근거를 독립적으로 찾는 단계가 있는가?
5. **인간 승인 게이트(Human Approval)**: 결과가 영구 지식으로 편입되기 전에 사람이 막을 수 있는가?
6. **도메인 특화(Domain Ontology)**: 특정 전문 분야(우리는 드론/AI 에이전트)에 맞춘 개념 구조가 있는가?

---

## 2. 시스템별 요약 (2026-08 기준 공개 정보)

### NotebookLM (Google)
2025년 11월 "Deep Research" 도입으로 "RAG 도구"에서 "에이전틱 리서처"로
전환했고, 2026년 6월 Gemini 3.5 업그레이드로 자체 소스 탐색, 코드 실행용
클라우드 컴퓨터, 차트/PDF/스프레드시트/PPT 출력까지 확장했다. 유료 등급은
월 500개 소스, 일일 75건 Deep Research 리포트까지 지원한다.
- 강점: 멀티모달 출력(오디오/비디오 오버뷰), 대규모 소스 처리, 사용 편의성.
- 한계: 노트북 단위로 격리(노트북 간 지식이 누적되지 않음), 주장 유형(사실/추론/가설) 구분 없음, 승인 게이트 없음.

### ChatGPT — Deep Research / Agent Mode (OpenAI)
Deep Research는 5~30분간 수백 개 출처를 자율 탐색해 인용 포함 구조화
리포트를 만든다. 2026년 2월부터 MCP/앱 연결, 신뢰 사이트 제한 검색을
지원한다. Agent Mode는 웹 클릭·스크롤·입력까지 수행하는 행동형 에이전트로
Deep Research와 통합됐다.
- 강점: 실시간 웹 전체 탐색, 웹 행동(클릭/입력)까지 가능, 계획 검토·중간 개입 가능.
- 한계: 리포트가 세션 산출물로 끝남(구조화된 영구 지식그래프로 축적되지 않음), 반증 단계가 명시적 역할로 분리되어 있지 않음.

### Gemini Deep Research (Google)
2026년 기준 5~10분 내 완료(출시 초 15~20분에서 단축), 25개 이상 언어
지원, SEO 저품질 소스 필터링 개선. Workspace 연동으로 Google Docs로 바로
출력된다.
- 강점: 속도, 다국어, 협업 도구 통합.
- 한계: NotebookLM/ChatGPT와 동일하게 세션형 리포트 — 지속적 지식베이스가 아님.

### Perplexity Labs / Computer (Perplexity)
Labs는 리서치·코드 실행·차트/대시보드 생성을 자율 워크플로로 수행한다.
2026년 2월 출시된 Perplexity Computer는 19개 AI 모델과 서브에이전트를
동원해 목표를 프로젝트 단위로 완성한다. 메모리 엔진은 95% 정확도로 맥락을
재호출하고, 예약 검색(scheduled search)으로 세션 간 지속 실행이 가능하다.
- 강점: 멀티 에이전트 오케스트레이션, 세션 간 메모리, 샌드박스 코드 실행, 에이전트 보안 도구(Numbat).
- 한계: 메모리는 사용자 맥락 재호출이지, 우리 시스템처럼 승인 게이트를 통과한 canonical 지식 축적이 아니다. 주장 유형·반증 역할 분리 없음.

### Claude Science Workbench / Projects (Anthropic)
Claude Science는 60개 이상 과학 데이터베이스에 연결되는 연구 워크벤치로,
게놈학·구조생물학 등 특정 과학 도메인에 특화됐다. 코드와 함께 재현 가능한
그림을 생성하고, 프로젝트 매니저 역할의 AI가 작업을 조율한다. Projects는
팀의 반복 작업을 위한 지속적 컨텍스트 공간이다.
- 강점: 도메인 특화 워크벤치(과학 데이터베이스 연결), 재현성(코드+그림), 대형 신뢰 기관(Anthropic) 신뢰도.
- 한계: 도메인이 생명과학/화학에 특화되어 있고 드론/AI 에이전트 도메인은 다루지 않음. 온톨로지가 공개되어 있지 않고, 주장 유형·반증·승인 게이트 구조가 공개 문서에 없음.

---

## 3. 비교 매트릭스

| 축 | NotebookLM | ChatGPT | Gemini | Perplexity | Claude Science | **우리 시스템** |
|---|---|---|---|---|---|---|
| 증거 기반 | 사용자 자료 + 실시간 웹 | 실시간 웹 전체 | 실시간 웹 전체 | 실시간 웹 + 19모델 | 60+ 과학 DB | 로컬 raw/canonical만(웹 미탐색, 의도적 범위 제한) |
| 지속성 | 노트북 단위(부분적) | 세션 리포트만 | 세션 리포트만 | 메모리 엔진(세션 간 맥락) | 프로젝트 단위 | **canonical 4계층 + index/log 영구 축적** |
| 주장 유형화 | 없음 | 없음 | 없음 | 없음 | 공개 안 됨 | **fact/inference/hypothesis 명시 필드** |
| 반증 절차 | 없음 | 계획 검토는 가능, 반증 역할 분리 없음 | 없음 | 없음 | 공개 안 됨 | **Critic이 독립 컨텍스트로 반증 전담(설계상 강제)** |
| 인간 승인 게이트 | 없음(생성 즉시 노트북에 반영) | 없음(리포트 즉시 완결) | 없음 | 없음 | 공개 안 됨 | **2단계 승인(Tier1 사후통지/Tier2 사전승인), all-or-nothing 승격** |
| 도메인 온톨로지 | 범용 | 범용 | 범용 | 범용 | 과학(생명과학/화학) 특화 | **드론/AI 에이전트 특화(`ONTOLOGY_SPEC.md`)** |
| 실시간 웹 탐색 | ✅ | ✅ | ✅ | ✅ | 부분적(DB 연결) | ❌ (Phase 1 명시적 비범위) |
| 멀티모달 출력 | ✅✅(오디오/비디오/차트) | 부분적 | ✅(문서) | ✅(차트/대시보드/미니앱) | ✅(그림+코드) | ❌ (마크다운만) |
| 웹 행동(클릭/입력) | ❌ | ✅(Agent Mode) | ❌ | ✅(Computer) | ❌ | ❌ |
| 세션 중 개입 | 제한적 | ✅(계획 검토·중단) | 제한적 | ✅ | ✅ | ❌ (배치 실행 후 승인/반려만) |

---

## 4. 우리 시스템만 가진 것 (5개 전부에 없는 것)

정직하게 확인한 결과, 아래 4가지는 5개 경쟁사 공개 자료 어디에서도
동일한 형태로 발견되지 않았다:

1. **주장 유형(claim_type) 명시 + 유형별 다른 검증 기준** — "사실 재진술은
   승격 거부"(`research-promote.py`의 `validate_item()`) 같은 규칙은
   경쟁사 어디에도 없다. 이들은 전부 "얼마나 잘 찾았나"를 최적화하지,
   "이게 새 지식인지 이미 아는 사실의 재포장인지"를 구분하지 않는다.
2. **Critic의 구조적 독립성** — 반증 담당자가 가설 생성자의 사고 과정을
   전달받지 않도록 의도적으로 차단한 설계(`MULTI_AGENT.md` §2)는 확인된
   경쟁사 문서에 없다. ChatGPT Deep Research의 "계획 검토"는 사용자가
   실행 전 계획을 보는 것이지, AI 내부에 독립적 반증자가 있는 게 아니다.
3. **승인 전/후 두 티어가 다른 권한을 갖는 구조** — 일상 수집은 사후
   통보, 연구 결과는 사전 승인이라는 차등 게이트(`AI_RESEARCHER_ARCHITECTURE.md`
   §5)는 5개 경쟁사 모두 "생성 즉시 반영" 또는 "세션 종료 즉시 완결" 모델이다.
4. **wikilink 기반 자기검증 지식그래프(≥2 링크 강제)** — 새 canonical
   페이지가 기존 지식과 최소 2개 이상 연결되지 않으면 무효로 처리하는
   구조적 제약(`SCHEMA.md`)은 경쟁사 어디에도 없다. 이들의 "메모리"는
   재호출 가능한 컨텍스트이지, 상호 연결이 강제되는 그래프가 아니다.

**결론**: 우리 시스템은 "더 빠르게 더 많이 찾는" 경쟁에서는 원천적으로
불리하다(경쟁사는 실시간 웹 전체 + 대규모 인프라, 우리는 로컬 코퍼스
~465문서). 대신 "찾은 것을 얼마나 책임 있게 지식으로 편입시키는가"라는
축에서는 공개 정보 기준으로 유일한 포지션에 있다.

---

## 5. 우리 시스템이 부족한 점 (보수적으로 평가)

경쟁사가 갖고 우리가 안 갖춘 것 중, "의도적 범위 제외"와 "진짜 결핍"을
구분한다.

### 5.1 의도적 범위 제외 (Phase 1에서 이미 결정, 재론하지 않음)
- 자율 웹 크롤링 — `Phase 1 목표` 문서에서 명시적으로 비범위 처리.
- 대규모 멀티에이전트 프레임워크 — 동일 문서에서 비범위, `MULTI_AGENT.md`가 재확인.

### 5.2 진짜 결핍 (경쟁 열위, 개선 여지 있음)
1. **실시간 웹 근거 부재**: 로컬 raw/canonical에 없는 질문에는 원천적으로
   답할 수 없다. 경쟁사 5개 전부 실시간 웹 탐색이 기본이다. 우리는 매일
   06시대 자동 수집(GitHub/RSS/arXiv 등)으로 커버하지만, "지금 이 순간"
   질문에는 약하다.
2. **세션 중 개입 불가**: 우리 파이프라인은 배치 상태 머신이라 5단계가
   끝날 때까지 마스터가 중간에 방향을 바꿀 수 없다(승인/반려만 가능).
   ChatGPT/Perplexity는 계획 단계에서 사용자가 수정할 수 있다.
3. **멀티모달 출력 없음**: 산출물이 마크다운 텍스트뿐이다. NotebookLM의
   오디오/비디오 오버뷰, Perplexity의 대시보드/미니앱 같은 형태가 없다.
4. **속도 미측정·미최적화**: 경쟁사는 5~10분대로 명시 최적화됐다. 우리는
   `claude -p` 순차 호출 5회 방식으로, 실측 소요시간을 별도로 측정한
   적이 없다(T1-T3 테스트는 통과 여부만 확인, 소요시간 기록 안 함).
5. **코드 실행 샌드박스 없음**: NotebookLM/Perplexity/Claude Science는
   코드를 실행해 재현 가능한 산출물을 만든다. 우리는 텍스트 종합만 한다.
6. **소규모 코퍼스**: ~465문서(canonical+raw+news) vs 경쟁사의 실질적
   웹 스케일. 이건 도메인 특화 시스템의 구조적 트레이드오프이지 결함은
   아니지만, "커버리지" 질문에는 명백히 열위다.

---

## 6. 개선 계획 (우선순위순)

기존 로드맵(`IMPLEMENTATION_PLAN.md`, `ONTOLOGY_IMPLEMENTATION_ROADMAP.md`,
`INNOVATION_ENGINE_ROADMAP.md`)과 충돌하지 않도록, 이미 계획된 항목은
참조만 하고 중복 제안하지 않는다.

### 우선순위 1 — 낮은 비용, 우리 강점을 더 굳히는 항목
- **claim_type 소급 적용 여부 결정**: 이미 승격된 2개 페이지에 claim_type을
  소급할지 마스터 결정 대기 중(Phase O2 완료 시점 기준 미결).
- **Relationship/Reasoning 필드 추가**: `RESEARCH_ENGINE.md` §4에서 이미
  제안됨(신규 LLM 호출 없이 기존 단계에 필드만 추가) — 우선순위 유지.

### 우선순위 2 — 중간 비용, 진짜 결핍 중 리스크 낮은 것부터
- **소요시간 계측**: `research-run.sh`에 단계별 타임스탬프 로깅 추가(신규
  LLM 호출 없음, 순수 계측). 경쟁사 대비 우리 파이프라인의 실제 소요시간을
  숫자로 확보 — 그 다음에야 "느리다/충분하다" 판단이 가능하다.
- **세션 중 경량 개입**: 전체를 대화형으로 바꾸지 않고, `01-questions.md`
  생성 직후 한 번(Planner→Retriever 사이) 마스터가 하위 질문을 수정할 수
  있는 선택적 정지점 추가. 상태 머신 구조는 유지(대규모 재설계 아님).

### 우선순위 3 — 높은 비용/리스크, 마스터 재승인 필요
- **제한적 실시간 웹 검증**: "자율 웹 크롤링"을 되살리자는 게 아니라,
  Verifier 단계에서 로컬 근거가 `insufficient_evidence`로 판정될 때만
  단일 검색 쿼리로 보강 검색을 허용하는 좁은 옵션. **이건 Phase 1의
  명시적 비범위를 부분적으로 재론하는 것이므로 구현 전 마스터 승인
  필수** — 이 문서는 제안만 하고 구현하지 않는다.
- **멀티모달 출력(오디오/비디오 오버뷰 등)**: ROI가 불확실하고(청중이
  마스터 1인), 비용 대비 이 시스템의 핵심 가치(신뢰 가능한 텍스트 지식)와
  방향이 다르다. **권장하지 않음** — 우선순위표에는 올리되 낮게 유지.

### 하지 않을 것 (명시적 결정)
- Perplexity Computer식 웹 행동(클릭/입력) 에이전트 — 이 시스템의 목적은
  "행동"이 아니라 "지식 축적"이다. 목적이 다른 걸 따라가는 건 방향 이탈.
- 경쟁사 규모의 코퍼스 확장(웹 스케일) — 도메인 특화 시스템의 정의 자체와
  충돌한다. 대신 "좁고 깊고 검증된" 포지션을 유지한다.

---

## 7. 전략적 결론

`RESEARCH_ENGINE.md`에서 세운 구분("NotebookLM은 검색한다, 우리는
연구한다")은 5개 경쟁사 전부로 확장해도 유지된다 — 다섯 개 모두 압도적인
증거 수집 능력을 갖췄지만, 수집한 것을 사실/추론/가설로 유형화하고,
독립적으로 반증하고, 사람이 승인해야만 영구 지식이 되는 구조는 공개 정보
기준으로 우리 시스템에만 있다.

이건 "우리가 더 낫다"는 뜻이 아니라 **다른 문제를 푼다는 뜻**이다.
경쟁사는 "지금 이 질문에 빨리 답하기"를 풀고, 우리는 "드론/AI 에이전트
도메인에 대해 시간이 지나도 신뢰할 수 있는 지식을 쌓기"를 푼다. 개선
계획도 이 방향에 맞춰야 한다 — 경쟁사를 따라 속도·규모·멀티모달을
쫓기보다, 우리 구조의 결핍(§5.2)을 우리 철학 안에서 메우는 쪽이
낫다는 것이 이 분석의 결론이다.

---

## 8. 참고자료

- [NotebookLM Update 2026: Every New Feature Explained](https://felloai.com/notebooklm-update-1m-token-chat-goals-saved-history/)
- [Google NotebookLM Update June 8, 2026: Agentic Research, Gemini 3.5](https://nerova.ai/news/google-notebooklm-june-8-2026-agentic-research-update)
- [NotebookLM Is Now an Agentic Research Workstation Tool](https://www.digitalapplied.com/blog/notebooklm-agentic-research-workstation-marketing-strategy-guide)
- [Introducing deep research | OpenAI](https://openai.com/index/introducing-deep-research/)
- [Introducing ChatGPT agent: bridging research and action | OpenAI](https://openai.com/index/introducing-chatgpt-agent/)
- [ChatGPT Deep Research Feature: How It Works in 2026](https://aiinsider.in/ai-learning/chatgpt-deep-research-feature-2026/)
- [Gemini Deep Research 2026: Features, Use Cases & Stats](https://chatboq.com/blogs/google-gemini-deep-research)
- [Gemini Deep Research Agent | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/deep-research)
- [Perplexity Labs Review 2026: AI Research Tool Tested](https://www.nocode.mba/articles/perplexity-labs-review)
- [Perplexity Computer Launch 2026: Full Review](https://medium.com/illumination/perplexity-computer-launch-2026-full-review-of-the-new-agentic-ai-tool-df227eb61c36)
- [Perplexity April 2026: Every New Feature and Update](https://leadershipinchange.com/p/ai-research-201-10-perplexity-features)
- [Anthropic Launches Claude Science AI Workbench for Scientific Research](https://www.hpcwire.com/aiwire/2026/06/30/anthropic-launches-claude-science-ai-workbench-for-scientific-research/)
- [Collaborate with Claude on Projects | Anthropic](https://www.anthropic.com/news/projects)
