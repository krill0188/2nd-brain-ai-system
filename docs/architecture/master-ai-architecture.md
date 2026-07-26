# 마스터 2nd Brain AI System — 시스템 아키텍처

> 문서 상태: v2.0  
> 작성일: 2026-07-26  
> 기반: ains-lab/2nd-brain-template v1.1 아키텍처 원칙 준수  
> 적용 대상: ~/2nd (krill0188/2nd-brain-ai-system)

핵심 목표는 자료를 많이 저장하는 것이 아니라, **원본으로 돌아갈 수 있고, 검증된 지식을 반복 재사용하며, AI 도구가 바뀌어도 핵심 자산이 남는 2nd Brain**을 만드는 것이다.

---

## 1. 아키텍처 결정 요약

이 시스템은 하나의 AI 도구에 모든 책임을 맡기지 않는다. 데이터의 신뢰 수준과 수명을 기준으로 다음 네 계층을 분리한다.

1. **Evidence** — 원본과 출처 메타데이터를 변경하지 않고 보존한다.
2. **Canonical Memory** — 반복 사용할 가치가 있는 지식을 출처가 연결된 Markdown으로 컴파일한다.
3. **Discovery** — 제한된 소스 질의와 AI 분석으로 가설·브리지·공백 후보를 찾는다.
4. **Decision** — 사람이 원문·중복·모순·신뢰도와 재사용 가치를 검토해 지식 승격 여부를 결정한다.

이 네 계층을 가로지르는 **AI Control Plane**은 5개 도구가 역할을 분담한다.

| 도구 | Control Plane 역할 |
|---|---|
| OpenCode + Kimi K2 | Compile 단계 — llm-wiki 컴파일, 문서 정리, 반복 초안 |
| Claude Code | Review/Judge 단계 — Gate B 검토, 아키텍처 판단, 모순 분석 |
| Codex | Code Explore 단계 — 드론 펌웨어·ROS 코드 탐색, Git 분석 |
| Gemini Code Assist | Cross-Validate 단계 — 편집 중 교차검증, 대안 탐색 |
| GitHub Copilot | Assist 단계 — Markdown·코드 인라인 자동완성 |

자동화 계층은 새로운 신뢰 계층이 아니며, 각 단계는 기존 Evidence·Governance·Decision 관문을 통과해야 한다.

운영의 중심 자산은 특정 AI 제품의 데이터베이스가 아니라 다음 세 가지다.

- 공개 형식으로 보존된 원본 또는 원본을 가리키는 안정적인 메타데이터
- YAML frontmatter와 위키링크를 가진 Markdown 문서
- 출처·변경 이력·품질 규칙을 명시한 거버넌스 계약

AI 분석 결과는 유용한 **가설**이지만 그 자체로 canonical 지식이 아니다. 사람이 검증하고 출처를 연결한 내용만 Canonical Memory로 승격한다.

---

## 2. 설계 원칙

### 2.1 Evidence First

요약이나 해석보다 원본 보존이 먼저다. `raw/`에 들어간 원본 본문은 수정하지 않고, 오류 정정과 해석은 canonical 문서에서 수행한다. 수집 시점·출처 식별자·SHA-256은 원문으로 돌아가기 위한 복구 경로다.

### 2.2 원본과 해석의 분리

외부 출처의 주장, AI의 합성, 개인의 경험과 판단을 같은 층에 섞지 않는다. 각 문장은 어느 계층에서 왔는지 식별할 수 있어야 한다. AI가 생성한 내용을 raw 증거처럼 기록하지 않는다.

### 2.3 컴파일된 장기 기억

Canonical Memory는 원본 전체를 복사한 저장소가 아니다. 자주 재사용할 개념·엔티티·비교·검증된 질의를 구조화한 지식 계층이다. 기존 문서를 갱신할 수 있다면 동의어 페이지를 새로 만들지 않는다.

### 2.4 재생성 가능한 파생 상태

지식그래프·검색 색인·대시보드·AI 분석 산출물은 원본과 canonical Markdown에서 다시 만들 수 있는 파생 상태다. 이를 정본으로 취급하거나 canonical 문서를 역으로 덮어쓰지 않는다.

### 2.5 사람 승인 관문

자동화는 수집·후보 생성·형식 검사를 돕는다. 다음 판단은 사람이 소유한다.

- 새 지식이 실제로 재사용할 가치가 있는가?
- 주장의 출처가 충분하고 원문과 일치하는가?
- 기존 문서와 중복되거나 충돌하지 않는가?
- AI 합성·외부 주장·개인 판단이 분리되어 있는가?
- 빠르게 변하는 정보에 날짜와 적절한 신뢰도를 부여했는가?

---

## 3. 논리 아키텍처

```text
허용된 외부 자료 (드론 기술 8개 도메인)
  → 수집 (Web Clipper·Zotero·YouTube·수동)
  → inbox/ 후보 또는 raw/ 불변 원본
  → Gate A: raw 무결성 검증
  → OpenCode + Kimi K2: llm-wiki 컴파일
  → canonical Markdown + index.md + log.md
  → Gate B: wiki lint·frontmatter·source 경로 검증
  → Claude Code: 모순 검토·아키텍처 판단 (필요 시)
  → Gate C: graph/freshness 검증 (지식그래프 도입 후)
  → 사람 검토 → Accepted·Contested·Deferred·Rejected
                  │
                  └→ canonical 갱신 → lint → index/log 동기화
```

### 3.1 계층별 책임

| 계층 | 책임 | 주요 입력 | 지속 데이터 | 출력 | 신뢰 경계 |
|---|---|---|---|---|---|
| Evidence | 원본과 서지정보 보존 | 논문·웹·영상·회의록 | `raw/**`, Zotero 라이브러리 | 추적 가능한 원본 레코드 | 원본 본문은 불변 |
| Canonical Memory | 지식을 선별·요약·비교·연결 | raw 레코드 | `entities/`, `concepts/`, `comparisons/`, `queries/` | 재사용 가능한 Markdown | 출처·링크·스키마 검증 필요 |
| Governance | 형식과 변경 이력 통제 | 저장소 변경 | `SCHEMA.md`, `index.md`, `log.md` | 유효성 판정과 감사 이력 | `SCHEMA.md`가 최종 계약 |
| AI Control Plane | 컴파일·검증·탐색·코드 분석 | raw 레코드·canonical·코드 | 각 도구 로컬 세션 (vault 외부) | canonical 변경안·검증 보고·가설 | 품질 관문과 사람 승인 우회 불가 |
| Discovery | 관계와 가설 탐색 | 선택한 원본·canonical 문서 | NotebookLM 작업공간 | 질의 결과·군집·브리지·공백 후보 | 결과는 가설, 재검증 필요 |
| Decision & Reuse | 승인·보류·산출물화 | 탐색 결과와 원문 | 승인된 canonical 갱신·`docs/` 산출물 | 의사결정·글·다이어그램 | 사람이 최종 승인 |

### 3.2 제어 평면과 데이터 평면

데이터 평면은 `raw/`와 canonical Markdown이다. 제어 평면은 `SCHEMA.md`·`index.md`·`log.md`·검증기·사람 검토다. AI 도구가 쓰기 작업을 수행하려면 데이터 평면만 바꾸는 것이 아니라 제어 평면까지 같은 트랜잭션에서 동기화해야 한다.

```text
OpenCode(Kimi K2) ── 컴파일·정리 ─────────────────────┐
Claude Code        ── 검증·판단 ──┐                   │
SCHEMA.md          ── 규칙 ────────┼→ canonical Markdown
index.md           ── 탐색 ────────┤           ↑
log.md             ── 감사 ────────┘           │
raw/**             ── 근거 ────────────────────┘
```

---

## 4. 저장소와 데이터 모델

### 4.1 기준 디렉터리

```text
~/2nd/
├── inbox/                    # 미분류 임시 입력; evidence도 canonical도 아님
├── raw/
│   ├── articles/             # 불변 기사·웹 클리핑
│   ├── notebooklm/           # NotebookLM 소스 레코드
│   ├── papers/
│   │   └── files/            # 논문 첨부 파일 (.gitkeep)
│   ├── transcripts/          # 불변 강의·회의 전사
│   ├── web/                  # 웹 캡처 (원본 경로 보존)
│   ├── youtube/              # YouTube 메타데이터·트랜스크립트
│   └── assets/               # raw 레코드가 참조하는 이미지·자산
├── entities/                 # 고유 개체 (인물·조직·도구·시스템)
├── concepts/                 # 개념·원리·메커니즘·활용
├── comparisons/              # 목적과 기준이 명시된 비교
├── queries/                  # 출처 검증을 통과한 재사용 질의 결과
├── docs/                     # 기술문서와 전달용 산출물
│   ├── architecture/         # 이 문서 포함 아키텍처 산출물
│   ├── domain/               # 드론 도메인 수집 가이드
│   ├── tech-stack/           # 기술 스택 다이어그램
│   └── workflow/             # 운영 워크플로 다이어그램
├── templates/                # 검증된 frontmatter 템플릿
├── _archive/                 # 완전히 대체된 canonical 페이지
├── AGENTS.md                 # AI 도구 역할 정의 + 도메인 포커스
├── CLAUDE.md                 # Claude Code 전용 지침
├── SCHEMA.md                 # 데이터 계약 (최종 권위 문서)
├── index.md                  # 활성 canonical 지식 전체 목록
└── log.md                    # append-only 작업 이력
```

이 저장소의 권위 있는 구조는 `SCHEMA.md`다. 폴더를 임의로 재구성하지 않는다.

### 4.2 데이터 수명 분류

| 분류 | 예시 | 변경 정책 | 백업 우선순위 |
|---|---|---|---|
| 불변 evidence | `raw/articles/*.md`, `raw/web/*.md` | 본문 수정 금지 | 최상 |
| 장기 canonical | `concepts/*.md`, `queries/*.md` | 검증된 트랜잭션으로 갱신 | 최상 |
| 거버넌스 | `SCHEMA.md`, `index.md`, `log.md` | 규칙에 따라 동기화, log는 append-only | 최상 |
| 임시 입력 | `inbox/` | 처리 후 보존·승격·폐기 결정 | 중간 |
| 파생 상태 | 지식그래프 캐시·검색 색인·AI 분석 산출물 | 원천 데이터에서 재생성 | 낮음 |
| 전달 산출물 | `docs/*.md`, PNG, HTML | 원천과 생성 시점 기록 | 요구에 따라 결정 |

### 4.3 Canonical 문서 계약

모든 canonical 페이지는 byte zero에서 시작하는 YAML frontmatter를 갖는다.

```yaml
---
title: 문서 제목
created: 2026-07-26
updated: 2026-07-26
type: entity | concept | comparison | query
tags: [drone, drone-sw]
sources:
  - "raw/articles/2026-07-26-px4-architecture.md"
confidence: medium
contested: false
contradictions: []
---
```

필수 규칙:

- 파일명은 소문자 kebab-case + `.md` 사용.
- `type`은 디렉터리와 일치해야 한다.
- `sources`는 실제로 존재하는 raw Markdown 경로만 기록한다.
- 여러 출처 합성·논쟁적 주장에는 claim-level provenance(`^[raw/...md]`)를 추가한다.
- canonical 집합이 비어 있지 않다면 각 페이지는 서로 다른 두 canonical 문서로 연결한다.
- 새 태그는 먼저 `SCHEMA.md` taxonomy에 등록한다.
- canonical 변경은 `index.md`와 `log.md`를 함께 갱신한다.

---

## 5. 기술 스택

도구는 고정 제품 목록이 아니라 교체 가능한 역할로 선택한다.

| 영역 | 선택 기술 | 채택 수준 | 역할 | 교체 가능 조건 |
|---|---|---|---|---|
| 저장 형식 | Markdown, YAML, UTF-8, 위키링크 | 필수 | 사람이 읽고 AI가 수정할 수 있는 장기 자산 | 동일한 공개 형식과 링크 보존 |
| 버전 관리 | Git | 필수 | 변경 이력·diff·복구·리뷰 | 파일 단위 이력과 복구 지원 |
| 거버넌스 | `SCHEMA.md`, `index.md`, `log.md` | 필수 | 계약·탐색·감사 | 동일 검증 규칙 재현 |
| 사람 인터페이스 | Obsidian | 권장 | Markdown 편집·역링크·Graph View | 파일을 원형 그대로 다루는 편집기 |
| 개발 환경 | VS Code | 권장 | AI 도구 통합·코드 탐색·편집 보조 | - |
| 원본·서지 관리 | Zotero + Connector | 연구 자료에 권장 | 드론 논문·웹 원본과 서지정보 관리 | 안정적인 식별자와 내보내기 지원 |
| **Compile** | OpenCode + Kimi K2 (OpenRouter) | 권장 | llm-wiki 역할, raw → canonical 후보 생성·정리 | SCHEMA.md·provenance 계약 준수 |
| **Review/Judge** | Claude Code (Claude Max) | 권장 | Gate B 검토·아키텍처 판단·모순 분석·최종 검토 | 동일 수준의 reasoning 능력 |
| **Code Explore** | Codex (ChatGPT Plus) | 권장 | 드론 코드(PX4·ArduPilot·ROS2) 탐색·구현 | - |
| **Cross-Validate** | Gemini Code Assist (무료) | 권장 | 편집 중 교차검증·요약·대안 탐색 | - |
| **Inline Assist** | GitHub Copilot (built-in) | 권장 | Markdown·코드 인라인 자동완성 | - |
| 집중 탐색 | NotebookLM | 선택 | 선택한 소스 묶음의 질의·요약·가설 생성 | 소스 범위와 인용 반환 필수 |
| 지식그래프 | Understand Anything (`understand-knowledge`) | 운영 중 | 문서·엔티티·관계를 파생 그래프로 생성 → `.ua/knowledge-graph.json` | canonical을 덮어쓰지 않고 재생성 가능 |
| 무결성 검사 | SHA-256, frontmatter·링크 검사 | 필수 | 원본 드리프트와 문서 계약 위반 감지 | 결정론적으로 재실행 가능 |

### 5.1 AI Control Plane 설계 원칙

5개 AI 도구는 역할이 분리되어 있다. 어떤 도구도 다른 도구의 역할을 대체하거나 합치지 않는다.

```text
Kimi K2 (OpenCode) ── 반복·컴파일 ───────────────────────┐
Claude Code        ── 판단·검증 ──┐                      │
Codex              ── 코드 탐색 ──┤                      │
Gemini             ── 교차검증 ───┼→ canonical 변경안     │
Copilot            ── 인라인 보조─┘         ↑            │
                                            │            │
SCHEMA.md / index.md / log.md ──────────────┴────────────┘
raw/** ─────────────────────────────────────────────────┘
```

Kimi K2는 비용이 저렴한 반복 작업에 집중하고, Claude는 비용이 발생하는 심층 판단에만 사용한다. Gemini·Copilot은 무료이므로 편집 중 자유롭게 활용한다.

### 5.2 최소 운영 스택

가장 작은 실용 구성은 `Git + Markdown + SCHEMA/index/log + 수동 검증`이다. AI 도구는 책임이 생길 때 순차적으로 추가한다.

---

## 6. 핵심 워크플로우

### 6.1 수집과 원본 보존

```text
수동 발견 또는 예약 수집
  → 허용 소스·드론 도메인 8태그 범위 확인
  → Web Clipper(웹) · Zotero(논문) · 수동(전사·YouTube)
  → URL·식별자 기준 중복 확인
  → 분류 미완료: inbox/ 후보 저장
  → 분류 완료: raw 종류 결정 (articles/web/papers/transcripts/youtube)
  → 출처·식별자·수집 시점 확보
  → templates/raw-article.md 기준 Markdown 레코드 생성
  → 본문 SHA-256 계산·기록
  → raw 무결성·원문 재현 가능성 확인 (Gate A)
  → ingest 결과 log.md 기록
```

완료 조건:

- raw 레코드와 자산의 역할이 구분되어 있다.
- 원본 식별자와 출처가 있으며 본문 해시를 재계산할 수 있다.
- 메타데이터 누락을 숨긴 채 canonical 작업으로 넘어가지 않는다.
- inbox 항목은 raw 보존과 canonical 반영이 모두 성공한 뒤에만 처리 완료로 본다.

### 6.2 Canonical 지식 컴파일

```text
수동 요청 또는 새 raw 감지
  → SCHEMA.md·index.md·최근 log.md 확인
  → 검증된 새 raw 확인
  → index와 canonical 전체에서 주제 검색
  → 기존 페이지 갱신 또는 새 페이지 임계값 판정
  → OpenCode(Kimi K2)로 출처 기반 변경안 작성
  → 위키링크·신뢰도·모순 기록
  → index·backlink·log 동기화
  → frontmatter·source 경로·링크 lint (Gate B)
  → 필요 시 Claude Code로 모순·아키텍처 검토
  → 변경안과 검증 결과 사람에게 보고
```

새 페이지는 한 원본의 중심 주제이거나 둘 이상의 원본에서 반복되는 개념일 때만 만든다. 단순 언급과 기존 페이지 동의어는 만들지 않는다.

### 6.3 집중 질의와 지식 증분

NotebookLM은 전체 위키의 영구 저장소가 아니라 선택한 소스 묶음을 집중 탐색하는 작업공간으로 사용한다.

```text
질문과 소스 범위 정의
  → NotebookLM에 raw 소스 업로드 (드론 도메인 한정)
  → 인용·source ID 포함 질의 결과 확보
  → 재사용 가치 판정
  → source ID를 로컬 raw 레코드에 매핑
  → 기존 canonical 검색
  → Gemini Code Assist 또는 Claude Code로 원문 교차검증
  → queries/ 생성 또는 기존 페이지 갱신
  → index·log·backlink 갱신
  → lint (Gate B)
```

다음 결과만 장기 지식 후보로 삼는다.

- 여러 소스를 결합한 비교와 종합
- 반복 가능한 연구·개발 절차
- 재사용 가능한 의사결정 기준
- 검증 계획이 있는 연구 가설과 지식 공백
- 기존 문서 여러 개를 새롭게 연결하는 분석

### 6.4 드론 코드 탐색 (마스터 특화)

```text
Codex 실행 (cd ~/2nd && codex)
  → 드론 코드 탐색 (PX4·ArduPilot·ROS2·MAVROS2·MAVSDK)
  → 코드 구조·API·동작 원리 분석
  → 분석 결과 → raw/articles/ 또는 raw/transcripts/ 저장
  → 6.2 컴파일 워크플로우로 canonical 승격
```

코드 탐색 결과를 직접 canonical에 넣지 않는다. raw 레코드를 거쳐야 한다.

### 6.5 사람 검증과 환류

탐색 결과는 다음 상태 중 하나로 결정한다.

| 상태 | 의미 | 후속 조치 |
|---|---|---|
| Accepted | 출처와 재사용 가치가 검증됨 | canonical 생성 또는 갱신 |
| Contested | 근거가 충돌하고 해결되지 않음 | 양쪽 주장·날짜·출처와 `contested: true` 기록 |
| Deferred | 가치가 있으나 근거가 부족함 | query 또는 inbox 후보로 보류 |
| Rejected | 중복·저품질·재사용 가치 없음 | canonical 편입 금지 |

Accepted 변경 후에는 lint를 다시 실행하고, 지식그래프가 있으면 재생성한다.

### 6.6 재사용과 산출물화

블로그·기술 문서·드론 설계 보고서는 canonical 지식을 소비한다. 산출물 작성 중 발견한 오류나 누락은 산출물에만 고치지 말고 raw 근거를 확인해 canonical에 환류한다.

---

## 7. 자동화 설계

원본 시스템의 Hermes Agent 역할을 마스터 도구 체계로 대응한다.

| 원본 (Hermes) | 마스터 대응 | 상태 |
|---|---|---|
| Hermes Agent 수집 | Obsidian Web Clipper + Zotero (수동) | 운영 중 |
| Hermes Cron 컴파일 | OpenCode(Kimi K2) 수동 실행 | 운영 중 |
| llm-wiki 스킬 | OpenCode + Kimi K2 (역할 동일) | 운영 중 |
| Gate B lint | Claude Code 검토 | 운영 중 |
| Understand Anything | `understand-knowledge` 스킬 설치 완료 (v0.19.0) | **운영 중** |
| Gate C graph 검증 | `.ua/knowledge-graph.json` 생성 완료 (25 노드, 41 엣지) | **운영 중** |
| Hermes Cron 예약 | macOS launchd (기존 인프라 활용 가능) | 향후 |

### 7.1 실행 토폴로지

```text
수동 수집 / 예약 수집 (향후 launchd)
  ├─ collect-evidence
  │    ├─ Web Clipper · Zotero · 수동
  │    └─ Gate A: 중복·메타데이터·SHA-256·raw 경로 검증
  │
  ├─ compile-wiki
  │    ├─ OpenCode + Kimi K2로 canonical 변경안 생성
  │    └─ Gate B: schema·source·link·index·log·lint 검증
  │         └─ 필요 시 Claude Code로 심층 검토
  │
  └─ build-knowledge-graph (향후)
       ├─ Gate B 통과 revision에서 선택 도구 실행
       └─ Gate C: graph 구조·freshness·dangling edge 검증
                          │
                          └→ 사람에게 diff·lint·graph 보고
```

### 7.2 자동화 가능한 작업

- 허용된 웹·Zotero 소스 검색·콘텐츠 추출·중복 후보 판정
- 새 raw 레코드의 필수 메타데이터·SHA-256 검사 (스크립트)
- OpenCode(Kimi K2)를 이용한 canonical 후보 생성·갱신과 index·log 동기화
- canonical frontmatter·날짜·type·tag·source 경로·위키링크 검사
- 변경 파일·검증 결과를 요약한 보고서 전달

### 7.3 자동화하지 않을 결정

- AI가 제안한 관계를 사실로 확정하는 일
- 충돌하는 출처 중 하나를 근거 없이 폐기하는 일
- 개인 판단을 외부 근거와 같은 신뢰도로 승격하는 일
- raw 본문을 정규화하거나 조용히 수정하는 일
- lint 실패를 성공으로 병합하는 일
- 대규모 canonical 변경을 사람의 diff 검토 없이 반영하는 일

---

## 8. 품질, 보안, 복구

### 8.1 품질 지표

페이지 수보다 다음 지표를 우선한다.

- source 경로가 실제로 존재하는 canonical 문서 비율
- raw SHA-256 검증 통과율
- 깨진 canonical 링크와 orphan 페이지 수
- index 누락과 중복 페이지 수
- 출처 없는 claim 수
- canonical 변경안 중 Accepted·Contested·Deferred·Rejected 비율
- 드론 도메인 8태그별 raw 소스 수·canonical 페이지 수

### 8.2 보안 경계

- API 키·OAuth 토큰·개인 식별자는 vault에 저장하지 않는다.
- `opencode.jsonc`·`.claude/`·`.codex/` 는 `.gitignore`로 추적 제외.
- NotebookLM 같은 외부 서비스에 민감한 원본을 보내기 전 데이터 정책 확인.
- `.obsidian/workspace.json`·캐시·플러그인은 공개 저장소에 포함하지 않는다.
- Git push 전 raw와 docs에 개인정보·비공개 원문이 없는지 검토한다.

### 8.3 장애 대응

| 증상 | 우선 조치 | 복구 기준 |
|---|---|---|
| raw 해시 불일치 | 쓰기 중단, 신뢰 가능한 원본과 diff 확인 | 변경 원인 설명 + 무결성 재확립 |
| source 경로 누락 | canonical 승격 중단 | 실제 raw Markdown으로 매핑 완료 |
| 깨진 위키링크 | 대상 복원 또는 유효한 canonical로 수정 | 링크 검사 0건 |
| 중복 주제 | 대표 페이지 선택 후 관계 통합 | index에 하나의 활성 주제만 존재 |
| NotebookLM 인용 매핑 실패 | confidence 낮추거나 편입 보류 | 핵심 인용이 로컬 source와 연결됨 |
| OpenCode 컴파일 실패 | 이전 canonical 유지, 원인 분석 후 재시도 | lint 통과한 변경안 확보 |
| Claude Code Gate B 실패 | canonical 병합 중단, lint 보고 보존 | 동일 revision의 schema·source·link 검증 통과 |

---

## 9. 단계별 도입안

### 단계 0: 저장소 계약 고정 ✅ 완료

- `SCHEMA.md`·`index.md`·`log.md`·Git 운영.
- canonical 0개 초기 상태를 정상으로 인정.
- 드론 도메인 8개 태그 등록 완료.

### 단계 1: 수동 Evidence-to-Wiki 루프 (현재 단계)

- 소수의 신뢰 가능한 드론 자료로 capture와 canonical 컴파일 연습.
- 자동화 전 사람이 source 경로·중복·링크·index/log 동기화를 반복 검증.
- Obsidian은 편집·탐색 인터페이스로만 추가.

### 단계 2: AI 도구 연결 (현재 단계)

- OpenCode + Kimi K2로 llm-wiki 컴파일 연습.
- Claude Code로 Gate B 검토 연습.
- Codex로 드론 코드 탐색 후 raw 저장.

### 단계 3: 연구 도구 연결

- 드론 논문이 늘면 Zotero를 원본 도서관으로 사용.
- 한정된 드론 소스 묶음의 복합 질문이 생길 때 NotebookLM 추가.
- NotebookLM 결과는 검증된 query 하나로만 환류.

### 단계 4: 지식그래프 관측 계층 (향후)

- canonical 문서와 링크가 충분히 쌓인 뒤 지식그래프 도구 도입.
- 그래프 결과를 원문 검증 없이 canonical에 자동 반영하지 않는다.
- Gate C 구성.

### 단계 5: 자동화 파이프라인 (향후)

- macOS launchd 또는 스크립트로 수집·컴파일 예약 실행.
- Gate A → B → C 자동 직렬 실행.
- 처음에는 사람이 diff를 승인하고, 무인 반영 범위는 작은 변경으로 제한.

---

## 10. 운영 완료 기준

하나의 지식 작업은 다음 조건을 모두 만족할 때 완료된다.

- 원본과 메타데이터가 `raw/` 또는 Zotero에서 추적 가능하다.
- raw 본문 무결성이 보존되었다.
- 기존 canonical 중복 검색을 거쳤다.
- 생성 또는 갱신된 문서가 schema·source·link·provenance 규칙을 만족한다.
- `index.md`와 `log.md`가 같은 트랜잭션에서 동기화되었다.
- frontmatter-aware wiki health check (Gate B)가 통과했다.
- 지식그래프가 있으면 새로 생성되었고 graph/meta가 검증되었다.
- 가설과 확정 지식, 외부 주장과 개인 판단이 구분되어 있다.
- 최종 산출물을 Obsidian에서 열어 링크와 이미지가 작동하는지 확인했다.

---

## 부록 A. AI 도구 역할 매핑 (원본 Hermes → 마스터)

| 원본 역할 | 원본 도구 | 마스터 도구 | 비고 |
|---|---|---|---|
| 수집 자동화 | Hermes Agent (web·browser·MCP) | Obsidian Web Clipper + Zotero | 현재 수동 |
| 예약 오케스트레이션 | Hermes Scheduled Tasks (Cron) | macOS launchd | 향후 |
| 지식 컴파일 | llm-wiki 스킬 | OpenCode + Kimi K2 | 운영 중 |
| 심층 판단·Gate B | (사람) | Claude Code | 운영 중 |
| 코드 탐색 | — | Codex (ChatGPT Plus) | 마스터 특화 추가 |
| 교차검증 | — | Gemini Code Assist | 마스터 특화 추가 |
| 인라인 보조 | — | GitHub Copilot | 마스터 특화 추가 |
| 집중 탐색 | NotebookLM | NotebookLM | 동일 |
| 지식그래프 | Understand Anything | 운영 중 | `~/.hermes/skills/understand-anything/` 설치, Gate C 활성 |

## 부록 B. 도메인 특화 — 드론 기술 8개 태그

모든 수집·컴파일 작업은 다음 8개 태그 범위를 우선으로 한다 (상세: `docs/domain/drone-domain-guide.md`).

| 태그 | 범위 | 수집 우선순위 |
|---|---|---|
| `drone` | 기체·비행·규정·임무 설계 | 3 |
| `datalink` | RF·LTE·MAVLink·C2 링크 | 2 |
| `swarm` | 편대비행·합의 알고리즘 | 4 |
| `voice-control` | 음성 명령 인터페이스 | 5 |
| `drone-hw` | FC·ESC·배터리·센서·카메라 | 5 |
| `drone-sw` | PX4·ArduPilot·GCS·ROS/ROS2·MAVROS/MAVROS2 | 1 |
| `drone-ai` | 컴퓨터 비전·SLAM·자율비행 | 3 |
| `ai-agent` | AI 에이전트·자율 의사결정 | 4 |
