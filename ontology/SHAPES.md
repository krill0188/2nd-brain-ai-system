# SHAPES.md — 제약(SHACL 동등물) 통합 참조

> G4(`ONTOLOGY_GUIDED_GRAPHRAG_PLAN.md`), 2026-08-02. 이 저장소는 정식
> SHACL 엔진을 쓰지 않는다(현 규모에서 과설계 — `GRAPH_SCHEMA.md`와 동일
> 판단). 대신 손으로 구현한 검증 규칙들이 사실상 SHACL의 "shape 제약"
> 역할을 이미 하고 있다. 이 문서는 그 규칙들을 재정의하지 않고, 어디에
> 정의돼 있는지 한곳에서 찾을 수 있게 인덱싱만 한다. **새 제약을 추가할
때 따를 체크리스트도 아래에 둔다.**

## 현재 시행 중인 제약(Shape) 목록

| 제약 | 적용 대상 | 정의 위치 | 강제 방식 |
|---|---|---|---|
| 9개 필수 frontmatter 필드 | canonical 4계층 전체 | `SCHEMA.md` §File and frontmatter rules | 수동 검토(자동 검증기 없음) |
| `claim_type` 선택적 10번째 필드 | research-promote.py 산출 페이지만 | `SCHEMA.md` 동일 절, `RESEARCH_SCHEMA.md` | `research-promote.py`가 생성 시 부여 |
| wikilink 최소 2개(non-self, resolvable) | canonical 페이지(집합이 비지 않을 때) | `SCHEMA.md` §Canonical link validity | `research-promote.py::validate_item()`가 승격 시점에 강제 |
| raw 출처 1건 이상 | 연구 루프 승격 클레임 | `RESEARCH_SCHEMA.md` §Promotion | `research-promote.py::validate_item()` |
| `evidence_tier: non-primary-reconstruction` 단독 불가 | 연구 루프 승격 클레임 | `RESEARCH_SCHEMA.md` §Promotion(2026-08-02 추가) | `research-promote.py::raw_evidence_tier()` + `validate_item()` |
| `claim_type: fact` 승격 거부 | 연구 루프 승격 클레임 | `RESEARCH_SCHEMA.md` §Promotion | `research-promote.py::validate_item()` |
| `verification_status: insufficient_evidence` 승격 거부 | 연구 루프 승격 클레임 | `RESEARCH_SCHEMA.md` §Promotion | `research-promote.py::validate_item()` |
| raw 불변성(sha256 무결성) | `raw/` 전체 | `SCHEMA.md` §Raw source integrity | 수동 검토 + 커밋 시 sha256 재계산 관행 |
| 태그 사전 등록제 | canonical 태그 전체 | `SCHEMA.md` §Tag taxonomy | 수동 검토 |

## 새 제약을 추가할 때 체크리스트

1. 이 표에 행을 추가한다(제약/적용대상/정의위치/강제방식).
2. 정의는 이 파일이 아니라 SCHEMA.md 또는 RESEARCH_SCHEMA.md 본문에 쓴다 —
   이 파일은 인덱스일 뿐, 제약의 1차 정의처가 아니다(중복 정의로 인한
   드리프트 방지).
3. "강제 방식"이 "수동 검토"뿐이라면, 코드로 강제할 가치가 있는지 판단한다
   — evidence_tier 사례(문서 경고만 있다가 나중에 코드로 강제)처럼, 중요한
   제약은 결국 코드화되는 게 낫다.
4. 새 제약이 기존 canonical 페이지를 무효화하지 않는지 확인한다(소급 적용
   여부는 항상 명시적으로 결정 — 자동 소급 금지, Phase O2 claim_type
   사례와 동일 원칙).
