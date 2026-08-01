# ONTOLOGY_IMPLEMENTATION_ROADMAP.md — 온톨로지 실제 구현 계획

> 작성: 2026-08-01 | 전제: `ONTOLOGY_SPEC.md` 설계 완료
> 성격: **계획 문서 — 이 문서 작성으로 아무것도 구현하지 않았다.** 개별 Phase 착수는
> 마스터의 별도 지시가 있을 때 진행한다.
> 원칙: 최소 변경 · 기존 스키마 하위호환 · 각 Phase 독립 롤백 가능 · 과설계 금지.

---

## 0. 가장 먼저 할 일 — 범위를 둘로 쪼갠다

`ONTOLOGY_SPEC.md`의 클래스·규칙을 그대로 "구현 계획"으로 옮기면 실현 불가능한
로드맵이 된다. 왜냐하면 규칙 8개 중 성격이 완전히 다른 두 그룹이 섞여 있기 때문이다.

| 트랙 | 대상 클래스/규칙 | 지금 구현 가능한가 |
|---|---|---|
| **Track A — 지식 온톨로지** | `KnowledgeClaim`, `AIModel`(SLM/LLM 분류), canonical 문서 자체의 클래스·관계 | ✅ 가능. `2nd-brain-ai-system`은 이미 파일 기반 지식 저장소이므로 클래스 라벨·관계 어휘를 얹는 것은 자연스러운 확장 |
| **Track B — 드론 런타임 온톨로지** | `Drone`, `Sensor`, `Task`, `Mission`, `VoiceCommand`의 규칙 1·2·3·5·7·8 | ❌ 지금은 불가능. 이 규칙들은 **실제로 비행 중이거나 시뮬레이션 중인 드론의 실시간 상태**(센서 값, 통신 상태, 배터리)를 전제로 한다. `2nd-brain-ai-system`은 그런 실시간 시스템을 갖고 있지 않다 — 가장 가까운 후보는 별도 프로젝트인 Swarm OPS GCS이지만, 이 로드맵의 스코프 밖이다 |

**결론**: 이 로드맵은 **Track A만** 단계별로 계획한다. Track B는 §5에서 "왜 지금
하지 않는지"와 "하려면 무엇이 먼저 필요한지"만 기록하고 Phase를 만들지 않는다 —
존재하지 않는 실시간 시스템을 위한 가짜 완료 기준을 세우지 않기 위해서다.

---

## Phase O0 — 매핑 검증 (반나절, 코드 변경 없음)

**작업**: `ONTOLOGY_SPEC.md` §5의 `domain`→온톨로지 클래스 매핑표를 실제 canonical
134편에 수작업/스크립트로 대입해보고, 매핑이 안 되거나 애매한 문서를 목록화한다.

**예상 변경 파일**: 없음(조사 스크립트는 1회성 스크래치, 저장소에 커밋 안 함)
**완료 기준**: 134편 중 몇 %가 8개 매핑 규칙 중 하나로 명확히 분류되는지 수치화. 70% 미만이면 Phase O1 착수 전 매핑표 자체를 재검토.
**위험**: 없음(읽기 전용)
**롤백**: 불필요

---

## Phase O1 — 그래프 노드에 온톨로지 클래스 라벨 추가 (문서 미변경)

**작업**: `scripts/update-graph.sh`가 각 canonical 문서를 스캔할 때, 기존
`domain`/`tags` 필드를 `ONTOLOGY_SPEC.md` §5 매핑표로 온톨로지 클래스에 대응시켜
`knowledge-graph.json` 노드에 `ontologyClass` 필드를 **추가로만** 기록한다.

- canonical 문서의 frontmatter(`domain`, `tags`)는 **전혀 건드리지 않는다** — 순수
  파생 데이터(그래프)에만 추가.
- 매핑 안 되는 문서는 `ontologyClass: null`로 두고 목록에 남긴다(억지로 분류하지
  않는다 — SCHEMA.md의 "억지로 페이지를 만들지 않는다" 원칙과 같은 사상).

**예상 변경 파일**: `scripts/update-graph.sh`만
**완료 기준**: 재실행 후 `ontologyClass`가 있는 노드 비율이 Phase O0 수치와 일치, 기존 그래프 소비자(`lib/wiki.ts`의 `getKnowledgeGraph()`, `research-search.py`)가 새 필드 무시하고 무회귀 동작
**위험**: 낮음 — 필드 추가는 기존 소비자 코드에 영향 없음(둘 다 필요한 필드만 읽음, 실측 확인됨)
**롤백**: `ontologyClass` 필드 제거 스크립트 1줄, 또는 그래프 재생성

---

## Phase O2 — KnowledgeClaim을 실제 frontmatter 필드로 승격

**현재 상태(실측)**: `research-promote.py`로 승격된 canonical 페이지 2건을 확인한
결과, `claim_type`(fact/inference/hypothesis)은 **본문 텍스트("승격된 inference
클레임")에만 있고 frontmatter에는 없다** — 즉 지금은 기계가 "이 페이지가
KnowledgeClaim의 어떤 서브타입인지" 질의할 방법이 없다. 이건 온톨로지 설계
과정에서 발견한 실제 구현 갭이다.

**작업**: `research-promote.py`의 `build_page()`가 frontmatter에 `claim_type`
필드를 추가로 기록하도록 수정. 값역은 `RESEARCH_SCHEMA.md`의 `fact|inference|
hypothesis`를 그대로 재사용(§ ONTOLOGY_SPEC.md 7 "값역 재사용" 원칙).

- `SCHEMA.md`의 필수 9필드 계약은 그대로 유지 — `claim_type`은 **research-promote
  경로로 생성된 페이지에만 붙는 선택적 10번째 필드**로 등록(SCHEMA.md 갱신 필요,
  기존 페이지들의 필수 9필드 검증 로직에는 영향 없음).

**예상 변경 파일**: `scripts/research-promote.py`, `SCHEMA.md`(필드 문서화 1개 추가)
**위험**: 기존 승격 페이지 2건에는 소급 적용 안 됨(별도 결정 필요 — 수동으로 2건만 추가할지, 그냥 다음 승격부터 적용할지는 마스터 판단)
**완료 기준**: 신규 승격 시 `claim_type` frontmatter 필드 존재 확인, `weekly-lint`가 이 필드를 필수 위반으로 오탐하지 않음 확인
**롤백**: `build_page()` 해당 줄 제거

---

## Phase O3 — 관계 어휘 확장 (옵트인, 하위호환)

**작업**: 현재 `update-graph.sh`는 모든 `[[wikilink]]`를 `type: "wikilink"`로만
기록한다(Phase 2에서 `contradicts`만 예외로 추가됨). Phase O3는 문서 작성자가
**원할 때만** 더 구체적인 관계를 명시할 수 있는 옵트인 문법을 추가한다.

제안 문법(예시, 확정 전 검토 필요):
```markdown
관련 개념: [[ros2-drone-deep]]{rel=dependsOn} [[px4-architecture-deep]]{rel=partOf}
```
문법이 없는 기존 `[[slug]]`는 그대로 `wikilink`로 처리(무회귀).

**예상 변경 파일**: `scripts/update-graph.sh`(정규식 확장), `SCHEMA.md`(문법 등록)
**위험**: 중간 — 이 문법이 Obsidian 등 다른 Markdown 도구에서 깨지지 않는지 확인 필요(중괄호가 일반 텍스트로 보이는지, 렌더링 깨지는지 실제 Obsidian에서 테스트 필요)
**완료 기준**: 최소 5개 문서에 수동으로 관계 태그 부여 → 그래프에 정확한 `type`으로 반영 확인, Obsidian에서 정상 렌더링 확인
**롤백**: 정규식 되돌리기(기존 동작으로 복귀), 이미 태그된 문서는 텍스트만 남아 있어 깨지지 않음

---

## Phase O4 — 규칙 재확인 및 문서화 (구현 아님, 이미 존재하는 것 인정)

`ONTOLOGY_SPEC.md` 규칙 6("미승인 가설로 Mission 근거 금지")은 **이미 사실상
구현되어 있다** — `research-promote.py`의 `fact` 거부·`insufficient_evidence`
거부·all-or-nothing 검증이 이 규칙의 정신을 그대로 실행 중이다. Phase O4는 새
코드를 만들지 않고, `research-promote.py`의 검증 함수 docstring에 "이 함수는
ONTOLOGY_SPEC.md 규칙 6을 구현한다"는 상호 참조만 추가한다(문서 간 추적성).

**예상 변경 파일**: `research-promote.py`(주석 1~2줄), `ONTOLOGY_SPEC.md`(§4 규칙 6에 "구현됨" 표시)
**완료 기준**: 상호 참조 추가
**위험**: 없음
**롤백**: 불필요

---

## Phase O5 (선택) — 온톨로지 클래스 기반 검색 필터

**작업**: `research-search.py --ontology-class SLM` 같은 옵션을 추가해 Phase O1의
`ontologyClass` 라벨로 검색 범위를 좁힐 수 있게 한다. 순수 검색 편의 기능.

**예상 변경 파일**: `scripts/research-search.py`
**완료 기준**: 온톨로지 클래스로 필터링한 검색 결과가 실제로 해당 클래스 노드만 반환
**위험**: 낮음 — 기존 옵션과 병행 사용 가능, 필터 미지정 시 기존 동작 그대로
**롤백**: 옵션 제거

---

## 전체 순서 요약

```
Phase O0  매핑 검증 (반나절, 코드 변경 없음)
Phase O1  그래프 노드 ontologyClass 라벨 (update-graph.sh만)
Phase O2  KnowledgeClaim claim_type frontmatter화 (research-promote.py)
Phase O3  관계 어휘 확장, 옵트인 (update-graph.sh + SCHEMA.md)
Phase O4  규칙 6 상호 참조 문서화 (주석만)
Phase O5  (선택) 온톨로지 클래스 검색 필터
```

각 Phase는 이전 Phase 완료 없이도 독립적으로 롤백 가능하다(서로 다른 파일,
서로 다른 데이터 위치를 건드리기 때문). 순서상 O1이 O5의 전제조건이라는 점만
의존관계다.

---

## 5. Track B(드론 런타임 온톨로지)를 지금 계획하지 않는 이유

`ONTOLOGY_SPEC.md`의 규칙 1(음성명령 신뢰도 차단)·2(Task 의존성)·3(센서 능력
부적합)·5(통신단절 시 LLM→SLM 위임)·7(치명적 실패 시 Mission 중단)·8(군집
안전 제외)은 전부 **런타임 상태**(현재 배터리량, 현재 데이터링크 상태, 현재
센서 판독값)를 필요로 한다. `2nd-brain-ai-system`은 정적 Markdown 지식
저장소이지 실시간 텔레메트리 시스템이 아니다.

이걸 실제로 구현하려면 먼저 답해야 할 질문들이 있고, 이 로드맵은 그 질문에
대신 답하지 않는다:

1. **어느 시스템에 연결할 것인가?** — 마스터의 다른 프로젝트 중 Swarm OPS GCS가
   실제 MAVLink 텔레메트리를 다루는 유일한 후보로 보이나, 확인이 필요하다.
2. **추론 엔진을 어디서 돌릴 것인가?** — 실시간 규칙 평가는 파일 기반 스크립트로는
   부적합하다(매번 파일을 읽는 지금 구조로는 밀리초 단위 응답이 불가능).
3. **이게 정말 "2nd Brain"의 책임 범위인가?** — 지식 관리 시스템에 실시간 비행
   안전 로직을 넣는 것이 아키텍처적으로 맞는지, 아니면 완전히 별도 프로젝트로
   분리해야 하는지부터 마스터의 판단이 필요하다.

**권고**: Track B는 별도 프로젝트로 스코프를 정의할 때(예: Swarm OPS GCS와의
연동을 실제로 착수할 때) 그때 가서 이 온톨로지의 클래스·규칙을 참조 자료로
재사용하는 것을 권장한다 — 지금 이 로드맵에 억지로 Phase를 만들지 않는다.
