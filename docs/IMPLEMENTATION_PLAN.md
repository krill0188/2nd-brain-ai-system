# IMPLEMENTATION_PLAN.md — 통합 개발 계획

> 작성: 2026-08-02 | 성격: **계획 문서 — 절대 구현하지 않았다.**
> 전제: 이번 세션에서 작성된 모든 설계 문서(`ONTOLOGY_SPEC.md`,
> `ONTOLOGY_IMPLEMENTATION_ROADMAP.md`, `GRAPH_SCHEMA.md`, `RESEARCH_ENGINE.md`,
> `INNOVATION_ENGINE.md`, `INNOVATION_ENGINE_ROADMAP.md`, `MULTI_AGENT.md`)를
> 하나의 실행 계획으로 통합한다. 개별 로드맵을 대체하지 않는다 — 저 문서들의
> "무엇을 왜"를 이 문서가 "어떤 파일을 어떻게"로 한 번 더 교차정리한다.
> 착수는 개별 Phase 단위로 마스터가 지시할 때만 한다.

---

## 0. 지금까지 실제로 구현된 것 (기준점)

이 계획은 백지에서 시작하지 않는다. 이미 커밋된 것:
- Phase O1(그래프 `ontologyClass` 라벨링) — `scripts/update-graph.sh`
- Research Engine 5단계 전체(Planner~Report) + 13단계(canonical 승격) — 실사용 검증 완료
- Phase 2(하이브리드 검색, 그래프 evidence/confidence, 노드 ID 정규화)
- README Gate A/B 정정 + 사후 가시성(morning-report.sh)

아래 계획은 **이 기준점 위에 얹는 증분**만 다룬다.

---

## 1. Directory (디렉터리 변경 계획)

```
~/2nd/
├── innovations/                    # 신규 최상위 (research/와 나란히)
│   ├── runs/<id>/                  #   과정 파일(input/combination/state.json)
│   ├── combinations/<id>.md        #   생성된 조합 후보(Scientist 역할 산출물에 대응)
│   ├── reports/<id>.md             #   Proposal Report + 후보 타입 + Innovation Score
│   └── prompts/                    #   역할 프롬프트 7종(Research Engine 패턴 재사용)
├── scripts/
│   ├── innovation-scan.py          # 신규 — Cross-Domain Scan(기계) + Technology Evolution 커넥터
│   ├── innovation-run.sh           # 신규 — Innovation Engine 오케스트레이터(research-run.sh 템플릿)
│   └── update-graph.sh             # 수정 — kind 필드 추가(GRAPH_SCHEMA.md §3.1), Evidence 노드 승격(§3.2)
├── research/
│   └── prompts/hypothesis.md       # 수정 — reasoning 필드 추가(RESEARCH_ENGINE.md §4.2)
└── docs/                           # 변경 없음(이미 이번 세션 산출물로 채워짐)
```

`drone-wiki-web`은 **이 계획으로 변경되지 않는다** — `innovations/`도
`research/`와 동일하게 `sync-wiki.sh` 대상이 아니다(설계 원칙, `INNOVATION_
ENGINE.md` §5 그대로 적용).

---

## 2. API (인터페이스 변경 계획)

이 시스템에 HTTP API 변경은 없다 — 전부 CLI다.

| 인터페이스 | 현재 | 계획된 추가 |
|---|---|---|
| `research-run.sh` | `new/resume/status/approve/reject` | 변경 없음(Relationship/Reasoning은 내부 프롬프트만 확장, CLI 계약 불변) |
| `research-promote.py` | `--items C1,C3` | 변경 없음 |
| `update-graph.sh` | 인자 없음, 전체 스캔 | 변경 없음(내부 로직만 확장) |
| **`innovation-run.sh`** | 없음 | **신규**: `new "<goal>"`, `resume <id>`, `status <id>`, `decide <id> go\|hold\|discard` |
| `innovation-scan.py` | 없음 | **신규**: 인자 없음(전체 그래프 스캔), 향후 `--min-hop`/`--filter` 옵션 여지만 남김(지금 구현 안 함) |
| `drone-wiki-web` REST API(`/api/chat,graph,pages`) | 3개 | **변경 없음** — 이 계획 전체가 2nd-brain 쪽 백엔드에만 있고 웹 API 계약을 건드리지 않음 |

---

## 3. Schema (데이터 스키마 변경 계획)

### 3.1 `knowledge-graph.json`

| 필드 | 대상 | 상태 |
|---|---|---|
| `node.ontologyClass` | 노드 | ✅ 이미 구현됨(Phase O1) |
| `node.kind` | 노드 | 계획 — `GRAPH_SCHEMA.md` §3.1(Entity/Technology/Paper/Patent/Mission/Requirement/Risk/Code/Concept/RepoDocument). `ontologyClass`와 통합할지 별도 필드로 둘지 **구현 시 결정 필요**(현재 둘 다 "분류"라는 같은 목적이라 중복 위험) |
| `evidence:<path>` 노드(1급) | 신규 노드 kind | 계획 — `GRAPH_SCHEMA.md` §3.2, canonical의 `sources: []`를 `derivedFrom` 엣지로 대체하는 큰 변경이라 **별도 Phase로 분리 권장**(이 계획에서는 설계만, 착수 순서 최하위) |
| `edge.type: contradicts` 구조화 | 엣지 | 계획 — `description`/`resolvedBy`/`resolvedDate` 필드 추가(`GRAPH_SCHEMA.md` §3.4). 현재 실사용 0건이라 **우선순위 낮음** |

### 3.2 `research/hypotheses/<id>.md`

| 필드 | 상태 |
|---|---|
| `claim`, `claim_type`, `supporting_sources` | ✅ 구현됨 |
| `reasoning`(신규) | 계획 — `RESEARCH_ENGINE.md` §4.2. **결정 필요**: 전체 클레임 필수 vs `inference`/`hypothesis`만 필수(fact는 재진술이라 생략 가능) |

### 3.3 canonical frontmatter (research-promote 경로만)

| 필드 | 상태 |
|---|---|
| 기존 9필드(title/created/updated/type/tags/sources/confidence/contested/contradictions) | ✅ 불변(SCHEMA.md 계약) |
| `claim_type`(신규, 선택적 10번째) | 계획 — `ONTOLOGY_IMPLEMENTATION_ROADMAP.md` Phase O2. **기존 승격 2건(`gps-uav-imu.md`, `micro-drone-slam-*.md`)에 소급 적용할지는 미결정** — 이 계획에서 마스터 결정 요청 사항으로 남김 |

### 3.4 `innovations/` 신규 스키마

```markdown
## Combination C1
- elements: [[slug-a]], [[slug-b]]   # 서로 다른 ontologyClass
- noveltyScore: 0-10
- feasibilityScore: 0-10
- valueScore: 0-10
- riskPenalty: 0-10
- innovationScore: (가중합, INNOVATION_ENGINE.md §3.4 공식)
- candidateType: patent | mission | weapon_system | research_theme
- decision: pending | go | hold | discard
```

### 3.5 `SCHEMA.md` 문서 갱신 필요 항목

- `research/`, `innovations/` 두 최상위 영역을 디렉터리 역할 표에 등록(이미
  `research/`는 등록됨 — `innovations/` 추가 필요)
- `claim_type` 필드를 "canonical 페이지의 선택적 10번째 필드"로 문서화
- `kind`/`ontologyClass` 필드를 그래프 파생 데이터 설명에 추가(canonical
  frontmatter 계약과는 무관함을 명시 — 그래프 전용 필드임을 혼동하지 않게)

---

## 4. Migration (기존 데이터 이관 계획)

| 대상 | 이관 필요한가 | 방법 |
|---|---|---|
| 기존 canonical 134편 | ❌ 불필요 | `ontologyClass`는 그래프에만 붙는 파생 데이터 — 원본 문서 무변경 |
| 기존 승격 페이지 2건의 `claim_type` | ⚠️ **결정 필요** | 소급 적용 시: 두 페이지의 본문("승격된 inference 클레임")에서 타입을 그대로 읽어 frontmatter에 수동 추가(스크립트 불필요, 2건뿐) |
| 기존 그래프 엣지 445건(evidence/confidence 있음) | ❌ 불필요 | `kind`/구조화 contradicts 추가는 신규 필드라 기존 엣지는 `update-graph.sh` 재실행 시 자동 백필(Phase 2와 동일 패턴, 이미 검증된 방식) |
| Gate C `article:` prefix 잔존 13건 | ❌ 불필요 | 이미 "canonical 4계층 밖 문서"로 정상 분류됨(Phase 2 결론 재확인) |

**이관 스크립트는 필요 없다** — 모든 신규 필드가 추가적(additive)이고,
`update-graph.sh`/`research-promote.py` 재실행이 곧 이관이다.

---

## 5. Rollback (롤백 계획)

| 변경 단위 | 롤백 방법 | 위험도 |
|---|---|---|
| `innovations/` 디렉터리 전체 | 디렉터리 삭제 | 없음 — canonical/raw 미접촉 설계이므로 삭제해도 다른 곳에 영향 없음 |
| `innovation-scan.py`/`innovation-run.sh` | 파일 삭제 | 없음 |
| `update-graph.sh`의 `kind`/Evidence 노드 확장 | 이전 커밋으로 되돌리기 + 그래프 재생성 | 낮음 — 그래프는 항상 canonical에서 재생성 가능(원칙 5, `AI_RESEARCHER_ARCHITECTURE.md`) |
| `hypothesis.md`의 `reasoning` 필드 | 프롬프트 파일 되돌리기 | 낮음 — 다음 세션부터 필드 없이 생성됨, 기존 세션 파일은 그대로 유효(구버전 필드 없어도 파서가 허용해야 함 — **구현 시 하위호환 파서 필수 조건**) |
| canonical `claim_type` 필드(신규 승격분) | frontmatter 필드 제거 | 낮음 — SCHEMA.md 9필수 필드에 영향 없음 |
| 기존 승격 2건 소급 적용 | 프론트매터 필드 삭제 | 없음 |

**공통 원칙**(`AI_RESEARCHER_ARCHITECTURE.md` 원칙 5 재확인): raw/canonical
이외 모든 것(그래프, 임베딩, innovations/)은 원본에서 재생성 가능해야 한다
— 이 계획의 모든 항목이 이 조건을 만족한다.

---

## 6. Test (테스트 계획)

기존 `MVP_ACCEPTANCE_TESTS.md`(T1~T3, 통과 완료)에 아래를 추가한다.

| # | 테스트 | 검증 대상 | 실패 시 |
|---|---|---|---|
| T4 | `ontologyClass` 매핑 정확성 | Phase O1(이미 구현) — canonical 표본 20편 수동 대조 | 매핑표 재검토(`ONTOLOGY_SPEC.md` §5) |
| T5 | `reasoning` 필드 회귀 | 필드 추가 후 기존 hypotheses 파일(필드 없음) 파서가 깨지지 않는지 | 파서 하위호환 처리 |
| T6 | Innovation Engine E2E(양성) | Novel Combination → Novelty Check 통과 → 4개 타입 중 하나로 분류 완료 | 파이프라인 단계별 로그로 원인 추적(Research Engine 디버깅 패턴 재사용) |
| T7 | Innovation Engine E2E(음성 — Novelty 탈락) | 이미 존재하는 조합을 강제 입력했을 때 실제로 폐기되는지 | Novelty Check 로직 점검 |
| **T8** | **Weapon System Candidate 안전 테스트 (필수, 최우선)** | 이 타입으로 분류된 산출물에 구체적 설계·사양·구현 방법이 **한 글자도** 없는지 전수 검사 | **실패 시 배포 보류** — 이 테스트는 다른 어떤 테스트보다 우선하며, 통과 못하면 Innovation Engine 전체를 릴리스하지 않는다 |
| T9 | canonical 무오염 | Innovation Engine 실행 전후 `git status -- concepts entities comparisons queries index.md log.md`가 T3와 동일하게 무변경 | T3와 동일한 방법으로 검증 |
| T10 | `innovation-run.sh decide` 3지선다 정확성 | go/hold/discard 각각 상태가 올바르게 `state.json`에 기록되는지 | 상태 전이 로직 점검 |

**T8을 최우선 필수로 지정한 이유**: 이 계획의 다른 실패는 되돌리면 그만이지만
(§5), Weapon System Candidate 분류에서 구체적 사양이 실제로 생성되어
`innovations/`에 파일로 남는 순간, 그 파일이 삭제되기 전까지 존재했다는
사실 자체가 되돌릴 수 없는 사건이다. 따라서 이 테스트는 "통과하면 출시"가
아니라 "통과가 출시의 전제조건"으로 취급한다.

---

## 7. 착수 순서 권고 (기존 개별 로드맵 종합)

```
1. Phase O2 (claim_type frontmatter화) — 가장 작고 안전, Innovation Engine과 무관하게 독립 가치 있음
2. RESEARCH_ENGINE.md §4 (Relationship/Reasoning) — 기존 파이프라인 소폭 확장, 회귀 테스트(T5) 필요
3. Innovation Engine Phase I0~I2 (검증+기계 스크립트만, LLM 파이프라인 이전 단계)
4. Innovation Engine Phase I3 (파이프라인 본체) — T8 통과 전까지 릴리스 보류
5. Innovation Engine Phase I4~I5 (저장구조+자동순환)
6. GRAPH_SCHEMA.md §3.2 Evidence 노드 승격 — 가장 큰 변경이라 최후순위
```

이 순서는 "위험이 작고 독립적인 것부터"라는 원칙을 따른다 — Innovation
Engine의 안전장치(T8)가 완성되기 전까지 그 이후 항목(4~6)에 마스터가
착수 승인을 내주지 않는 것을 권고한다.
