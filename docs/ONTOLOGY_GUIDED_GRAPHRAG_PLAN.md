# ONTOLOGY_GUIDED_GRAPHRAG_PLAN.md — DIKW/온톨로지-가이드 GraphRAG 업그레이드 계획

> 작성: 2026-08-02 | 원 성격: 계획 문서. **같은 날 마스터 지시("구현해
> 주세요")로 G0~G5 전부 구현 완료** — 아래 §6 "구현 결과"에 실제 반영
> 내용을 기록한다. 근거 자료:
> https://groou.com/ontology/2026/07/31/dikw-graph-knowledge-graph-ontology/
> (DIKW 4단계: Data→Information→Knowledge→Wisdom, 기술 3단계: Graph→
> Knowledge Graph→Ontology, RAG 3단계: Vector RAG→GraphRAG→Ontology-guided
> GraphRAG)

## 6. 구현 결과 (2026-08-02, 계획 대비 실제)

| Phase | 계획 | 실제 구현 | 차이 이유 |
|---|---|---|---|
| G0 | 노드 스키마 통합(article:/topic: 분리) | **구현 중 더 큰 문제 발견 — 별도 대응**: `~/2nd`에 설치된 서드파티 플러그인 "understand-anything"이 정확히 같은 파일(`~/2nd/.ua/knowledge-graph.json`)에 자기 코드베이스 구조 그래프를 쓰고 있었다(우연한 파일명 충돌). article:/topic: 17개 노드의 정체가 바로 그 플러그인 산출물이었다. 우리 그래프를 `drone-knowledge-graph.json`으로 완전히 분리하고, understand-anything의 파일은 손대지 않았다(마이그레이션: canonical 139노드+474엣지만 필터링 시드). | 스키마 통합보다 파일 분리가 근본 해결책이었음 |
| G1 | wikilink 엣지에 의미 부여 | **섹션 맥락 기반 3분류 구현**: "## 근거/출처/Evidence/Reference" 헤딩 아래 링크 → `evidences`, "## 관련/Related/See Also" 아래 → `related`, 헤딩 밖 산문 언급 → `wikilink`(기존과 동일, 관계를 지어내지 않음). 실측: 무의미 `wikilink` 비율 92%→49%로 개선(엣지 897개 중 441개). 기존 474개 엣지는 소급 재분류하지 않음(계획대로) | `implements`/`dependsOn` 등 ONTOLOGY_SPEC.md 런타임 object property는 **적용하지 않음** — 그건 실제 드론 인스턴스 간 관계용이지 위키 문서 간 관계가 아니어서 그대로 쓰면 범주 오류(카테고리 에러)가 됨. 문서 관계 전용의 더 작은, 구조적으로 뒷받침되는 어휘로 대체 |
| G2 | 클래스 계층 조회 테이블 | `ontology/class-hierarchy.json`(ONTOLOGY_SPEC.md §1 전체 45개 클래스 그대로 전사) + `scripts/ontology_lib.py`(get_ancestors/get_descendants) | 계획대로 |
| G3 | 검색 확장(상위→하위 클래스 포함) | **범위를 "노드 재분류"에서 "질의 확장"으로 좁힘**: 139페이지 전부를 세밀 클래스로 재분류하는 건 근거 없는 분류를 새로 만드는 리스크라 하지 않음. 대신 질의어에 클래스명이 있으면(예: "FlightStack") 하위 클래스명(PX4/ArduPilot)을 검색 토큰에 추가하는 질의 확장 사전으로 구현. Python(`research-search.py`)·TypeScript(`lib/rag.ts`) 양쪽에 적용, 실질의 테스트로 검증(“FlightStack 아키텍처 비교” → ardupilot-architecture.md 등 실제로 상위권 진입) | 근거 없는 소급 분류를 피하기 위한 의도적 범위 축소 |
| G4 | 제약 문서 통합 | `ontology/SHAPES.md` — 기존 9곳에 흩어진 제약을 재정의 없이 인덱싱, 체크리스트 추가 | 계획대로 |
| G5 | 정식 스택 재검토 임계치 | `GRAPH_SCHEMA.md` §5에 추가 — canonical 500페이지 / 엣지 3,000개 / 실제 오분류 3건 중 하나라도 도달 시 재검토(그래프 DB 임계치 5,000엣지와는 별개 트리거) | 계획대로 |

**테스트**: `test_graph_lib.py`(6/6), `test_ontology_lib.py`(7/7),
`test-ontology.mjs`(TS, 4/4) — 전부 신규 통과. 기존 `update-graph.sh` 재실행
결과 노드/엣지 수 무손실(idempotent 확인, 2회 연속 실행 결과 동일).

---

## 0. 전제 — 무엇을 만들고 무엇을 안 만드는가

직전 대화에서 이미 결론 냈듯, 원문이 제시하는 고신뢰성 스택(Protégé+
Apache Jena+ELK/HermiT+pySHACL)은 **도입하지 않는다** — 156노드 규모에서
정식 DL(Description Logic) 추론기는 과설계이고, 잘못 작성된 공리는
"틀린 말을 하지 않는다"는 목표를 정확히 반대 방향으로 해칠 수 있다
(`GRAPH_SCHEMA.md`가 이미 같은 논리로 Neo4j/RDF를 "486엣지 << 5000
임계치"로 보류한 전례와 동일 원칙).

이 계획이 만드는 것은 **경량 버전**이다 — 정식 온톨로지 엔진 없이,
이미 설계된 `ONTOLOGY_SPEC.md`의 클래스 계층을 실제로 "쓰이는" 상태로
바꾸고, 그래프 엣지에 진짜 의미(predicate)를 부여하고, 이미 손으로
구현 중인 검증 규칙(SCHEMA.md/evidence_tier)을 SHACL의 정신에 맞게
한곳에 정리하는 것.

---

## 1. 실측 현황 진단 (2026-08-02, 실제 `knowledge-graph.json` 확인)

추측 없이 직접 로드해서 확인한 수치:

| 항목 | 실측치 | 의미 |
|---|---|---|
| 총 노드 | 156개 | |
| 총 엣지 | 515개 | |
| 엣지 relation 분포 | `wikilink` 474(92%) / `related` 33(6%) / `categorized_under` 8(2%) | **엣지 대부분이 의미 없는 "연결됨"뿐 — RDF 트리플의 predicate에 해당하는 게 사실상 없다** |
| `ontologyClass` 보유 노드 | 139/156 | 나머지 17개는 필드 자체가 없음 |
| `ontologyClass` 실값 | Technology 78 / AIModel 29 / Mission 17 / **None 15** | None 15개는 Phase O1 매핑 표(`ONTOLOGY_CLASS_MAP`)가 커버 못 하는 domain(예: regulations) |
| 노드 스키마 | **2종 혼재** | (a) canonical 노드: `id/name/layer/domain/tags/confidence/status/ontologyClass` (update-graph.sh 작성) — (b) `article:*` 노드 17개: `id/type/name/filePath/summary/knowledgeMeta(전문 임베딩)` (다른 도구, 아마 Gate C/llm-wiki 스킬 작성) — **필드 집합이 다른 두 종류가 같은 파일에 공존** |

**결론**: 원문의 DIKW 기준으로 우리는 "Knowledge Graph" 단계에 있다고
자평했지만, 실측하니 엣지의 92%가 predicate 없는 순수 위상 연결
(`wikilink`)이다. 이건 원문이 정의하는 "Graph"(순수 위상 용기) 단계에
더 가깝다 — Knowledge Graph로 완전히 승급하지 못한 상태다. 또한
스키마 두 종류가 말없이 혼재하는 건 그 위에 TBox/RBox를 올리기 전에
먼저 정리해야 할 기초 결함이다.

---

## 2. 업그레이드 단계 (Phase G0~G5)

### Phase G0 — 그래프 노드 스키마 통합 (선행 필수)

**왜 먼저**: RBox/TBox를 의미 있게 올리려면 그 아래 노드 구조부터
일관돼야 한다. 지금처럼 두 스키마가 섞인 채로 관계 타입을 정교화하면
어느 노드엔 있고 어느 노드엔 없는 혼란만 커진다.

- **Directory/Schema**: `ontology/GRAPH_NODE_SCHEMA.md` 신설 — canonical
  노드와 `article:*` 메타 노드를 **같은 파일, 다른 `kind` 필드**로
  구분할지, 아니면 애초에 두 그래프를 분리할지 결정.
  (`GRAPH_SCHEMA.md`가 이미 제안한 `kind` 필드 재사용 후보.)
- **API 영향**: `expandGraphNeighbors()`/`getSubgraph()`(drone-wiki-web
  `lib/rag.ts`)가 두 스키마를 암묵적으로 관대하게 처리 중(`n.name ||
  n.id`) — 스키마 통합 후 이 관대한 처리를 명시적 분기로 교체.
- **Migration**: `article:*` 17개 노드를 새 스키마로 재작성하거나,
  Q&A 그래프 확장 대상에서 제외(둘 중 하나를 마스터가 결정).
- **Rollback**: 노드 재작성 실패 시 원본 `knowledge-graph.json` 백업본
  복원(단순 파일 교체, 스크립트 롤백 아님).
- **Test**: 통합 전/후 canonical 노드 139개의 필드가 무손실인지 diff.

### Phase G1 — 엣지 관계타입 세분화 (RBox 경량화, 예상 최고 가치)

**왜 이게 가장 시급**: 원문 기준 "Information→Knowledge" 승급의 핵심이
바로 이거다 — predicate 없는 연결은 아직 Knowledge가 아니다.

- **Schema**: `ONTOLOGY_SPEC.md`가 이미 정의한 20개 object property 중,
  그래프 엣지로 표현 가능한 것부터 선별(예: `implements`, `dependsOn`,
  `partOf`, `contradicts`, `supersedes`) — 전부 한 번에 도입하지 않고
  실제 canonical 본문에서 근거를 찾을 수 있는 관계부터.
- **API**: `update-graph.sh`의 엣지 생성 로직에 relation 추론 규칙 추가
  (예: frontmatter `contradictions` 필드 → `contradicts` 엣지는 이미
  구현돼 있음 — 이 패턴을 다른 관계로 확장).
- **Migration**: 기존 474개 `wikilink` 엣지는 **일괄 재분류하지 않는다**
  — "그냥 링크됨"과 "명시적 관계 있음"은 다른 신뢰도이므로, 새 관계
  타입은 새로 생성되는 엣지에만 적용하고 기존 wikilink는 그대로 둔 채
  점진적으로 보강(무회귀 원칙).
- **Rollback**: relation 필드는 추가 정보이므로 제거해도 그래프 자체는
  깨지지 않음 — 필드 삭제만으로 원상복구.
- **Test**: 신규 relation 생성 로직에 대해 canonical 샘플 5~10개로
  기대 relation과 실제 생성 relation 일치 여부 확인.

### Phase G2 — 클래스 계층 조회 테이블 (TBox 경량화)

- **Schema**: `ontology/class-hierarchy.json` 신설 — `ONTOLOGY_SPEC.md`의
  클래스 계층(PhysicalEntity/SoftwareSystem/AbstractProcess/DataArtifact/
  Agent 및 하위 클래스)을 실제 조회 가능한 트리로 코드화. 정식 OWL이
  아니라 단순 부모-자식 딕셔너리(`{"PX4": "FlightController",
  "FlightController": "SoftwareSystem", ...}`).
- **API**: `get_ancestors(cls)`/`get_descendants(cls)` 헬퍼 2개 —
  Python(`scripts/`)과 TypeScript(`lib/`) 양쪽에 필요(기존 하이브리드
  검색이 두 언어로 중복 구현된 기술부채와 같은 패턴, 이미 알려진 리스크).
- **부가 작업**: 현재 `ontologyClass: None`인 15개 노드의 원인
  domain(예: `regulations`)을 `ONTOLOGY_CLASS_MAP`에 추가해 커버리지
  갭 보완(Phase O1 당시 88.7%였던 커버리지를 재계산해 목표치 설정).
- **Rollback**: 조회 테이블 파일 삭제 시 기존 검색 로직은 계층 확장
  없이 이전처럼 동작(하위 호환 — 계층 조회는 옵션 기능으로 설계).
- **Test**: 계층 조회 함수 단위 테스트(예: `get_ancestors("PX4")` ==
  `["FlightController", "SoftwareSystem"]`), 순환 참조 없음 검증.

### Phase G3 — 검색 확장 로직 업그레이드 (GraphRAG → 온톨로지-가이드)

- **API**: `drone-wiki-web/lib/rag.ts`의 `expandGraphNeighbors()`를
  확장 — 현재는 1-hop 이웃만 반환. Phase G2의 계층 조회를 추가해,
  질문이 상위 클래스를 가리키면 하위 클래스 개체도 후보에 포함(예:
  "비행 컨트롤러"질문 → PX4/ArduPilot 자동 포함).
- **Migration**: 기존 `/api/chat/route.ts` 응답 스키마(`sources`/
  `newsSources`/`mode`)는 변경하지 않음 — `neighbors` 계산 로직 내부만
  교체(API 계약 무변경, 프론트엔드 영향 없음).
- **Rollback**: 계층 확장 로직에 실패 시 기존 1-hop 확장으로 즉시
  폴백(이미 확립된 이 저장소의 표준 패턴 — 임베딩 없으면 키워드 폴백
  하듯 동일 원칙 적용).
- **Test**: "비행 컨트롤러" 같은 상위개념 질의로 PX4/ArduPilot이
  실제로 `sources`에 포함되는지 E2E 확인(기존 하이브리드 검색 검증
  때 썼던 "위치 인식 불가 상황..." 같은 실질의 테스트 질의 패턴 재사용).

### Phase G4 — 제약(SHACL 동등물) 통합 문서화

- 지금 SCHEMA.md 9필드 계약, wikilink 2개 강제, evidence_tier 검증이
  전부 사실상 SHACL shape 역할을 손으로 구현한 것 — 이걸 하나의
  참조 문서(`ontology/SHAPES.md` 또는 SCHEMA.md 내 전용 절)로 모아
  "새 제약을 추가할 때 따라야 할 체크리스트" 형태로 명문화.
- 새 코드를 추가하지 않는 순수 문서화 작업이라 리스크 최소.

### Phase G5 — 정식 스택 재검토 임계치 (장기, 조건부)

- `GRAPH_SCHEMA.md`의 "5000엣지 임계치" 선례를 계승해, **언제
  Protégé/Jena/HermiT 같은 정식 스택을 재검토할지 미리 숫자로
  정의**(예: canonical 500페이지 또는 엣지 3000개 초과, 또는 정식
  추론이 없어 발생한 실제 오류 사례가 N건 누적).
- 트리거 도달 전에는 이 논의를 재소집하지 않는다 — 매번 재판단하는
  비용을 없앤다.

---

## 3. 우선순위와 의존관계

```
G0(스키마 통합) ──▶ G1(엣지 관계타입) ──┬──▶ G3(검색 확장)
                └──▶ G2(클래스 계층)  ──┘
G4(제약 문서화)는 독립적, 아무 때나 가능
G5는 트리거 조건부, 지금 착수 안 함
```

G0가 선행되지 않으면 G1/G2가 두 스키마 중 어느 쪽을 대상으로 하는지
모호해진다. G3는 G1과 G2 둘 다(또는 최소 하나)를 전제로 한다.

---

## 4. 하지 않을 것 (명시적 결정)

- Protégé/Apache Jena/ELK·HermiT/pySHACL 등 정식 온톨로지 스택 도입 —
  G5 트리거 전까지 재론하지 않음.
- 기존 474개 `wikilink` 엣지 일괄 재분류 — 점진적 보강만, 소급 없음.
- Neo4j/KuzuDB 등 그래프 전용 DB 전환 — `GRAPH_SCHEMA.md` 기존 결정
  유지(정적 JSON + 파일 기반 유지).
- Weapon System 관련 자동 추론/분류 확장 — `INNOVATION_ENGINE.md`가
  이미 정한 "지식 분류 전용" 제한을 그대로 유지, 이번 계획과 무관.

---

## 5. 마스터 결정이 필요한 지점

1. Phase G0에서 `article:*` 메타 노드를 Q&A 그래프에 남길지, 제외할지.
2. Phase G1에서 어떤 관계타입부터 시작할지(전부 한 번에 하지 않음 —
   `implements`/`dependsOn`/`partOf` 중 우선순위).
3. Phase G2 클래스 계층 조회를 Python/TypeScript 양쪽에 중복 구현할지,
   아니면 이번 기회에 하이브리드 검색처럼 중복 구현되는 기술부채를
   해소할 방법(예: 공유 JSON을 두 언어가 각자 파싱)을 택할지.

이 계획은 설계만 완료됐고, 위 결정 및 마스터의 "진행해줘" 지시 전까지
구현하지 않는다.
