# GRAPH_SCHEMA.md — 지식 그래프 스키마 설계

> 작성: 2026-08-01 | 성격: **설계 문서 — 구현하지 않았다.**
> 전제: `ONTOLOGY_SPEC.md`(클래스·관계 정의)를 그래프 자료구조로 어떻게 담을지
> 설계한다. 현재 `.ua/knowledge-graph.json`을 직접 분석한 실측 데이터를 근거로 삼는다.

---

## 1. 현재 그래프 분석 (실측, 2026-08-01)

```
노드: 150개 / 엣지: 486개
노드 layer 분포: Concepts 114, Entities 16, Comparisons 1, Queries 2, (layer 없음) 17
엣지 type 분포: wikilink 445, related 33, categorized_under 8, contradicts 0
confidence 있는 노드: 133/150
evidence 필드 있는 엣지: 445/486 (wikilink만 — related/categorized_under는 0)
```

**중요 사실**: 이 그래프는 **두 개의 독립된 쓰기 주체**가 만든다 —
1. `scripts/update-graph.sh` (이 세션에서 작성) — `wikilink`/`contradicts` 엣지, 노드에 `confidence`/`status` 부여
2. Gate C(`Understand Anything`의 `merge-knowledge-graph.py`, 별도 Hermes 스킬) — `related`/`categorized_under` 엣지, `article:` prefix 노드 생성

이 둘은 **서로 다른 스키마 어휘를 쓰면서 같은 파일에 쓴다** — 이것이 아래 §2의
1번 문제다.

---

## 2. 현재 그래프의 문제점

1. **두 독립 쓰기 주체의 스키마 비정합**: `update-graph.sh`가 부여한 `evidence`/
   `confidence`는 `wikilink` 엣지 445건에만 있고, Gate C가 만든 `related`(33)/
   `categorized_under`(8) 엣지 41건에는 없다. 같은 그래프 안에서 "이 관계에 근거가
   있는지"를 물으면 41건은 항상 답할 수 없다.
2. **노드 정체성 이원화(부분 해결)**: Phase 2에서 `article:<slug>` 중복 8건을
   병합했으나, 남은 13건(`article:README`, `article:SCHEMA` 등)은 canonical
   4계층 밖의 저장소 문서(README, docs/*)라 병합 대상이 아니다 — 그런데 이 둘을
   구분하는 명시적 필드(`nodeKind` 같은)가 없어서, 그래프 소비자가 "이게
   canonical 지식 노드인지 저장소 문서 노드인지"를 ID 문자열 접두사로만
   추측해야 한다.
3. **`layer`는 컨텐츠 타입이 아니라 저장 위치다**: 노드의 유일한 분류축인
   `layer`(Entities/Concepts/Comparisons/Queries)는 "어느 디렉터리에 저장했는가"를
   나타낼 뿐, "이게 기술 설명인지, 논문인지, 프로젝트인지, 리스크인지"는
   구분하지 못한다. 실측 결과 concepts 114개 전부가 하나의 `layer` 값 아래
   뭉뚱그려져 있다 — 논문 요약, 기술 개념, 규제 동향, 뉴스 다이제스트가
   그래프상 구분 없이 전부 "Concepts"다.
4. **Evidence가 1급 노드가 아니다**: canonical 노드의 근거는 frontmatter
   `sources: []`(문자열 경로 목록)와 엣지의 `evidence: [path][:1]`(첫 항목만)로만
   존재한다. "이 근거 자체의 신뢰도·수집일·무결성(sha256)"을 그래프에서 직접
   질의할 방법이 없다 — raw 파일을 별도로 열어야 한다.
5. **Contradiction이 사실상 죽어있는 필드**: frontmatter `contradictions: []`와
   엣지 `type: contradicts`가 스키마에는 있지만 실측 사용 건수는 **0건**이다.
   모순을 발견해도 기록할 그릇은 있지만 아무도(자동화도, 사람도) 채운 적이
   없다 — 필드가 존재하는 것과 실제로 쓰이는 것은 다르다는 걸 보여주는 사례.
6. **요청된 도메인 객체 타입이 전혀 표현되지 않음**: `Technology`, `Patent`,
   `Paper`, `Mission`, `Requirement`, `Risk`, `Code`가 그래프 스키마에 존재하지
   않는다.
   - `Paper`: `raw/papers/*.md` 9편이 존재하지만 **그래프 노드가 아니다** — raw는
     canonical만 스캔하는 `update-graph.sh` 대상이 아니기 때문에, 논문 간
     인용 관계·논문↔개념 관계가 그래프에 전혀 나타나지 않는다.
   - `Technology`: PX4/ROS2/SLM 등은 전부 `Concepts` 층에 평평하게 섞여 있어
     "기술 스택"이라는 범주로 따로 질의할 수 없다.
   - `Patent`, `Mission`, `Requirement`, `Risk`, `Code`: 지금 이 지식베이스에
     해당 콘텐츠 자체가 거의/전혀 없다(예: `recon-swarm-project.md`는 사실상
     Mission 성격이지만 `Concept`로만 존재). 타입이 없다기보다, **콘텐츠도
     타입도 둘 다 없는 상태**다.

---

## 3. 제안 스키마

### 3.1 노드 종류 (`kind` — 신규 필드, `layer`는 유지)

`layer`(저장 위치)와 `kind`(도메인 객체 타입)를 **분리**한다. 하나의 `layer`
안에 여러 `kind`가 섞일 수 있다(예: `concepts/`에 `Technology`도, `Risk`도
있을 수 있다).

| kind | 설명 | 현재 대응 |
|---|---|---|
| `Entity` | 구체적 개체(기업·제품·표준) | 기존 `entities/` 그대로 |
| `Technology` | 기술/프로토콜/스택 개념 | 기존 `concepts/`의 부분집합(PX4/ROS2/SLM 등) |
| `Paper` | 학술 논문 | **신규** — `raw/papers/*.md`를 그래프 노드로 승격 |
| `Patent` | 특허 | **신규, 현재 인스턴스 0건** — 스키마만 예약 |
| `Mission` | 프로젝트/임무 단위 서술 | **신규** — `recon-swarm-project.md` 같은 문서 재분류 |
| `Requirement` | 요구사항 | **신규, 현재 인스턴스 0건** |
| `Risk` | 위험 요소 | **신규** — 현재 canonical 본문에 산발적으로만 서술(예: FCC 규제 리스크), 별도 노드화 안 됨 |
| `Code` | 코드 모듈/함수 단위 지식 | **신규, 현재 인스턴스 0건** — Codex 탐색 결과가 raw/inbox 텍스트로만 남고 그래프 노드가 안 됨 |
| `Concept` | 위 어디에도 안 맞는 일반 개념 | 기존 `concepts/`의 나머지 |
| `Comparison` / `Query` | 기존 그대로 | 변경 없음 |
| `RepoDocument` | README/SCHEMA/docs 등 canonical 아닌 저장소 문서 | **신규** — 현재 `article:` prefix로만 암묵 구분되던 13개 노드에 명시적 kind 부여 |

### 3.2 Evidence를 1급 노드로 승격

```json
{
  "id": "evidence:raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md",
  "kind": "Evidence",
  "sourceType": "paper",
  "sha256": "...",
  "capturedDate": "2026-07-27",
  "url": "https://arxiv.org/abs/2402.07537"
}
```
canonical 노드는 `sources: []`(문자열) 대신 `derivedFrom` 엣지로 Evidence
노드를 가리킨다. 이러면 "이 Evidence가 몇 개의 canonical 주장에 쓰였는가",
"이 Evidence의 sha256이 raw 파일과 여전히 일치하는가"를 그래프 질의로 answer할
수 있다(지금은 각 raw 파일을 열어야만 확인 가능).

### 3.3 Confidence — 노드로 승격하지 않는다 (의도적 결정)

Confidence를 별도 노드 타입으로 만드는 안도 검토했으나 **기각**한다. Confidence는
`low|medium|high` 3값 스칼라이며, 이를 노드로 reify하면 모든 canonical 노드가
Confidence 노드에 엣지로 연결되는 과설계가 된다(노드 수만 늘고 질의는 오히려
복잡해짐). **노드/엣지의 속성(attribute)으로 유지**하는 현재 방식이 맞다 — 이건
"모든 것을 노드로 만들지 않는다"는 온톨로지 설계의 흔한 함정을 피하는 결정이다.

### 3.4 Contradiction을 구조화된 엣지로

```json
{
  "source": "concept-a",
  "target": "concept-b",
  "type": "contradicts",
  "description": "A는 X라 주장하나 B는 반대 근거를 제시",
  "evidence": ["raw/..."],
  "resolvedBy": null,
  "resolvedDate": null
}
```
지금처럼 `type: contradicts`만 있는 빈 엣지가 아니라, 왜 모순인지·누가
해소했는지까지 담는다. (실사용 0건인 이유가 "쓸 곳이 없어서"가 아니라
"채울 필드가 없어서"였을 가능성도 있다 — 구조를 갖추면 실제 사용이 늘어날지
지켜볼 대상.)

### 3.5 관계 어휘 확장 (Phase O3와 연동)

`ONTOLOGY_SPEC.md` §2의 관계 20개 중 지식 그래프에 즉시 유효한 것만 채택:

`wikilink`(범용, 기존 유지) · `contradicts`(구조화, §3.4) · `derivedFrom`
(canonical→Evidence) · `cites`(Paper→Paper, Concept→Paper) · `dependsOn`
(Technology→Technology) · `partOf`(Component→Mission/System) · `mitigates`
(Technology→Risk) · `implements`(Code→Requirement) · `comparesTo`
(Comparison↔Concept)

이 어휘 확장은 `ONTOLOGY_IMPLEMENTATION_ROADMAP.md`의 **Phase O3(옵트인 관계
태그)**와 동일한 메커니즘으로 도입한다 — 새 스키마이지만 새 인프라는 아니다.

---

## 4. 기술 선택 — Neo4j를 반드시 쓸 필요는 없다는 전제로 비교

| 방식 | 이 저장소 구조와의 적합성 | 다중홉 질의 | Vercel 정적 배포 | 신규 의존성 | 판정 |
|---|---|---|---|---|---|
| **현행 JSON 확장**(§3안 그대로 JSON에 반영) | ✅ 기존 `update-graph.sh`/`lib/wiki.ts`와 100% 호환, git으로 추적 가능 | ❌ 직접 순회 코드 필요(2-3홉까지는 이미 `expandGraphNeighbors`로 실증됨) | ✅ 파일 그대로 커밋 | 없음 | **채택** |
| **KuzuDB**(임베디드, Cypher 유사) | 🟡 단일 `.db` 파일이라 git 추적은 되나, JSON export 단계가 추가로 필요(Vercel엔 여전히 JSON 스냅샷을 내보내야 함) | ✅ 진짜 그래프 질의 가능 | 🟡 export 필요 | 있음(Python 바인딩) | 보류 — 486엣지는 `TECHNOLOGY_DECISION_RECORD.md` #8의 재검토 트리거(5,000엣지)에 한참 못 미침 |
| **Neo4j** | ❌ 서버 프로세스 필요, 이 저장소는 서버리스+정적파일 아키텍처 | ✅ | ❌ 서버 필요, Vercel과 근본적으로 안 맞음 | 있음(서버 운영) | **제외** — 마스터도 "반드시 쓰라는 뜻 아님"이라 명시, 실제로 이 구조에 안 맞음 |
| **RDF/OWL 트리플스토어**(rdflib 등) | 🟡 `ONTOLOGY_SPEC.md`의 클래스·프로퍼티와 개념적으로 가장 잘 맞음(SPARQL, SWRL 추론 가능) | ✅✅ (추론 포함) | 🟡 export 필요 | 있음, 학습곡선 최대 | 보류 — 지금 아무도 3홉 이상 추론이 필요한 실제 질의를 해본 적이 없다(실측 병목 없음) |

**결론**: 지금은 **JSON 확장**을 채택한다. 이유는 세 가지 실측 근거 때문이다 —
(1) 486엣지는 어떤 재검토 트리거에도 도달하지 않았고, (2) Vercel 정적 배포
요구사항이 그래프 DB 채택 시 매번 "export 단계"라는 새 실패 지점을 추가하며,
(3) `expandGraphNeighbors`(1-hop)와 `getSubgraph`(seed+1-hop)가 지금 요구를
이미 충족하고 있어 다중홉 질의가 실제로 막힌 사례가 아직 없다. 재검토 조건은
`TECHNOLOGY_DECISION_RECORD.md`의 기존 트리거표를 그대로 따른다.

---

## 5. 이 스키마와 다른 설계 문서의 관계

- `kind` 필드는 `ONTOLOGY_IMPLEMENTATION_ROADMAP.md` **Phase O1**(`ontologyClass`
  라벨링)과 사실상 같은 작업이다 — 이름을 통일할지(`kind` vs `ontologyClass`)는
  실제 구현 착수 시 결정.
- Evidence 노드 승격(§3.2)은 Phase O2(KnowledgeClaim frontmatter화)와 함께
  진행하면 효율적이다 — 둘 다 "지금 텍스트/리스트로만 있는 것을 그래프 1급
  개체로 승격"하는 같은 성격의 작업.
- Mission/Requirement/Risk/Code/Patent는 **콘텐츠 자체가 없다** — 스키마를
  먼저 만들어도 실제로 채워질지는 마스터가 그런 문서를 만들기 시작해야 알 수
  있다. 빈 스키마를 미리 준비해두는 것과, 없는 콘텐츠를 위해 파이프라인을
  만드는 것은 다른 우선순위다 — 이 문서는 전자(스키마 준비)까지만 하고
  후자(수집 파이프라인 신설)는 다루지 않는다.
