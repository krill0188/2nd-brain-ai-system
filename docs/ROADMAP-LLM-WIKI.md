# 2nd Brain → LLM-wiki AI Agent 전환 로드맵

> **비전**: 드론 특화 지식을 AI가 자율 수집·생성·연결·질의응답하는 LLM-wiki 플랫폼
> **기준일**: 2026-07-29
> **영감**: Andrej Karpathy의 LLM-wiki 개념 (AI가 지식을 능동적으로 생성·관리)

---

## 현재 상태 vs 목표 상태

| 항목 | 현재 (2nd Brain v2.1.0) | 목표 (LLM-wiki) |
|---|---|---|
| 지식 수집 | fetch-inbox.sh → raw 파일 | AI가 필요 지식 자율 판단·수집 |
| 지식 생성 | 마스터가 .md 파일 작성 | AI가 릴리즈노트→Concept 페이지 자동 생성 |
| 지식 연결 | 수동 frontmatter links | AI가 신규 지식과 기존 노드 자동 링크 |
| 질의응답 | RAG/GraphRAG (수동 질문) | 질문 자체가 지식 확장 트리거 |
| 시각화 | 타입별 그래프 | 7개 드론 도메인 클러스터 뷰 |
| 접근 | 로컬 Next.js 앱 | 공개 드론 지식 플랫폼 (선택적) |

---

## Karpathy LLM-wiki 핵심 원리

```
기존 Wiki:  사람이 쓴다 → 사람이 읽는다
LLM-wiki:  LLM이 쓴다 → 사람이 읽는다 + LLM이 확장한다
```

- **자기증식**: 새 정보가 들어오면 AI가 지식 페이지를 생성하고, 기존 지식과 연결
- **질의 확장**: 사용자 질문 → AI가 지식 갭을 발견하면 새 페이지 생성
- **지식 일관성**: AI가 중복·충돌·오래된 정보를 자동 감지·정리
- **에이전트 루프**: fetch → generate → link → review → publish → repeat

---

## Phase 1 — Hermes Ingest를 진짜 AI Agent로 전환

> **목표**: 릴리즈 노트 raw 파일이 들어오면 AI가 Concept 페이지를 자동 생성하고 지식 그래프와 연결한다.

### 현재 흐름 (문제)
```
fetch-inbox.sh → inbox/fetch-YYYY-MM-DD-px4.md (raw)
        ↓
Hermes daily-ingest → "파일 처리 완료" 보고 (요약만)
        ↓
concepts/ 에 새 파일 없음 — 지식이 늘지 않음
```

### 목표 흐름
```
fetch-inbox.sh → inbox/fetch-YYYY-MM-DD-px4.md
        ↓
ai-control.sh cmd_run_ingest()
  → call_llm() 프롬프트 개선:
     "이 릴리즈 노트를 분석해서 concepts/ 에 새 지식 페이지를 생성해라.
      기존 노드와 연결 가능한 링크를 frontmatter links에 명시해라."
        ↓
concepts/px4-v1.17.0-features.md (신규 자동 생성)
        ↓
knowledge-graph.json 자동 업데이트 (노드 추가 + 엣지 연결)
```

### 변경 파일

| 파일 | 변경 내용 |
|---|---|
| `~/2nd/scripts/ai-control.sh` | `cmd_run_ingest()` 프롬프트를 "지식 페이지 생성 + 링크" 명령으로 개선 |
| `~/2nd/scripts/generate-concept.sh` | 신규: LLM이 생성한 Concept 페이지를 concepts/ 에 저장 |
| `~/2nd/scripts/update-graph.sh` | 신규: concepts/ 변경 감지 → knowledge-graph.json 자동 업데이트 |

### 완료 기준
- [ ] fetch-inbox.sh 실행 후 Hermes cron 한 번 돌리면 `concepts/` 에 신규 .md 파일이 자동 생성됨
- [ ] 생성된 파일에 frontmatter `links:` 필드가 기존 노드를 참조함
- [ ] knowledge-graph.json 의 nodes 배열에 신규 노드가 추가됨

**예상 소요**: 4~6시간 (ai-control.sh 프롬프트 개선 + 2개 스크립트 신규)

---

## Phase 2 — 7개 도메인 태그 체계 구축

> **목표**: 모든 지식 노드에 `domain` 필드 추가 → 도메인별 분류·필터·시각화 가능

### 드론 도메인 7개 클러스터

| domain 값 | 한글 이름 | 주요 노드 예시 |
|---|---|---|
| `flight-control` | 비행제어 | PX4, ArduPilot, MAVLink, 비행모드 |
| `comms-protocol` | 통신프로토콜 | MAVLink v2, DroneCAN, UAVCAN, RF링크 |
| `hardware` | 하드웨어 | Pixhawk 6X, FC보드, GPS, 배터리 |
| `gcs-software` | GCS/소프트웨어 | QGroundControl, Mission Planner, ROS2 |
| `ops-mission` | 운용/미션 | 웨이포인트, RTL, BVLOS, 페이로드 |
| `regulations` | 법규/안전 | 항공안전법, EASA, 비행승인, 보험 |
| `ai-autonomy` | AI/자율 | SLAM, 객체탐지, 군집제어, OpenCV |

### 변경 파일

| 파일 | 변경 내용 |
|---|---|
| `~/2nd/templates/concept.md` | frontmatter에 `domain:` 필드 추가 |
| `~/2nd/templates/entity.md` | 동일 |
| `~/2nd/scripts/lint-knowledge.sh` | `domain` 필드 누락 시 경고 추가 |
| `~/2nd/scripts/tag-domain.sh` | 신규: 기존 47개 노드에 domain 자동 태깅 (LLM 판단) |
| `~/2nd/knowledge-graph.json` | 각 노드에 `"domain":` 필드 추가 |

### 완료 기준
- [ ] 기존 47개 concepts/entities 파일 모두 `domain:` frontmatter 보유
- [ ] knowledge-graph.json 각 노드에 `domain` 필드 존재
- [ ] lint-knowledge.sh 실행 시 domain 누락 파일 0개

**예상 소요**: 2~3시간 (스크립트 1개 + 기존 파일 일괄 업데이트)

---

## Phase 3 — 지식 그래프 클러스터 뷰 (UI)

> **목표**: 7개 도메인이 색상 클러스터로 구분된 인터랙티브 그래프. 클러스터 클릭 → 해당 도메인 노드만 확대.

### UI 컴포넌트 변경

| 파일 | 변경 내용 |
|---|---|
| `src/app/graph/page.tsx` | 도메인별 색상 매핑 + 클러스터 필터 탭 추가 |
| `src/lib/fs/graph.ts` | `domain` 필드 파싱 + 도메인별 그룹 반환 |
| `src/app/api/graph/route.ts` | `?domain=flight-control` 쿼리 파라미터 지원 |

### 도메인 색상 팔레트

```typescript
const DOMAIN_COLOR = {
  'flight-control': '#3b82f6',  // blue
  'comms-protocol': '#10b981',  // green
  'hardware':       '#f59e0b',  // amber
  'gcs-software':   '#8b5cf6',  // purple
  'ops-mission':    '#ef4444',  // red
  'regulations':    '#6b7280',  // gray
  'ai-autonomy':    '#ec4899',  // pink
}
```

### 완료 기준
- [ ] 그래프 페이지에서 7개 도메인 색상 클러스터 시각화
- [ ] 도메인 필터 탭 클릭 시 해당 도메인 노드만 표시
- [ ] 노드 클릭 → 해당 Concept 상세 페이지 이동

**예상 소요**: 3~4시간 (Phase 2 완료 후)

---

## Phase 4 — 공개 플랫폼 전환 (마스터 결정 필요)

> **마스터가 결정해야 할 사항**

### 옵션 A: 개인 지식 비서 유지 (현재)
- 로컬 실행 / Vercel 비공개 배포
- 추가 작업 없음
- 드론 커뮤니티 기여 없음

### 옵션 B: 드론 특화 공개 위키
- Vercel 공개 배포 (`drone-wiki.vercel.app` 등)
- SEO 최적화 (sitemap, OpenGraph, 구조화 데이터)
- 커뮤니티 기여 게이트 설계 (PR 기반 or 관리자 승인)
- 한국 드론 커뮤니티 타깃팅

### 옵션 C: 드론 AI Agent API 서비스
- REST API 공개 (`/api/rag`, `/api/graph-rag`)
- 타 서비스에서 드론 지식 질의 가능
- 사업화 가능성 있음

**Phase 4는 Phase 1~3 완료 후 결정 권장.**

---

## 전체 타임라인

```
Week 1 (즉시)
└── Phase 1: Hermes AI Agent 전환
    ├── ai-control.sh 프롬프트 개선
    ├── generate-concept.sh 신규
    └── update-graph.sh 신규

Week 2
└── Phase 2: 도메인 태그 체계
    ├── 템플릿 업데이트
    ├── tag-domain.sh 실행 (47개 노드 자동 태깅)
    └── lint 검증

Week 3~4
└── Phase 3: 클러스터 뷰 UI
    ├── graph.ts domain 파싱
    ├── API domain 필터
    └── graph/page.tsx 클러스터 렌더링

Week 5+  (마스터 결정 후)
└── Phase 4: 공개 전환 여부
```

---

## 진행 여부 결정 기준

- Phase 1 단독으로도 즉시 가치 있음 (지식이 자동으로 늘기 시작)
- Phase 2는 Phase 1 없이도 독립 실행 가능 (데이터 준비)
- Phase 3은 Phase 2 필요 (domain 필드가 있어야 클러스터 뷰 가능)
- Phase 4는 Phase 1~3 모두 완료 후 결정

---

*작성: 2026-07-29 | 2nd Brain v2.1.0 기준*
