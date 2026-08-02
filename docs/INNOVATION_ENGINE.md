# INNOVATION_ENGINE.md — Innovation Engine 설계

> 작성: 2026-08-02 | 성격: **설계 문서 — 구현하지 않았다.**
> 전제: `RESEARCH_ENGINE.md`가 다룬 것은 "이미 존재하는 근거로부터 참인 것을
> 찾는" 수렴적(convergent) 엔진이다. Innovation Engine은 그 반대 — "아직
> 존재하지 않는 것을 근거들의 조합으로부터 제안하는" 발산적(divergent)
> 엔진이다. 둘을 같은 파이프라인으로 착각하고 설계하면 잘못된다 — 이 문서는
> 그 차이를 먼저 명확히 한 뒤 설계한다.

---

## 1. Research Engine과의 근본적 차이

| | Research Engine | Innovation Engine |
|---|---|---|
| 사고 방향 | 수렴(convergent) — 여러 근거를 좁혀서 하나의 검증된 결론으로 | 발산(divergent) — 서로 먼 것들을 넓혀서 새로운 조합으로 |
| 판정 기준 | 참/거짓에 가까움(`grounded`/`insufficient_evidence`) | 참/거짓이 아님 — **실현가능성(feasibility) × 신규성(novelty) × 가치(value)** 3축 |
| 성공한 산출물 | "이 주장은 근거로 뒷받침된다" | "이 조합은 아직 아무도 안 해봤고, 만들 수 있고, 쓸모가 있다" |
| 실패 모드 | 근거 없이 결론을 냄(환각) | **이것도 환각이지만 더 위험하다** — 그럴듯한 신규 아이디어는 검증하기 훨씬 어렵다(비교할 "참"이 아직 없음) |
| canonical 반영 | 승인 시 `concepts/`로 직접 승격 (사실/추론) | **canonical에 절대 직접 쓰지 않는다** — 아래 §5 참조 |

**결론적으로**: Innovation Engine을 Research Engine의 프롬프트만 바꿔서
만들면 안 된다. 검증 기준 자체가 다르고, 안전장치의 위치도 달라야 한다.

---

## 2. 목적

기존 지식(canonical)을 재진술하지 않고, **서로 다른 온톨로지 도메인의 기존
지식을 의도적으로 조합**해 새로운 기술 방향을 발견한다. 산출물은 단일
형태가 아니라 **성숙도에 따라 4가지 후보 타입 중 하나로 분류**된다(§3.2).

예: `Technology`(SLM, 온보드 소형 모델) + `Technology`(voice-control, 음성
인터페이스) + `Mission`(recon-swarm-project, 정찰 임무) → "통신 두절 시
음성 명령만으로 개별 기체를 재편성하는 온보드 SLM 인터페이스" 같은 제안.
이 세 요소는 지금 그래프에 각각 존재하지만, 지금까지 하나로 묶인 적이 없다.

---

## 3. 파이프라인

### 3.1 생성 단계 (Knowledge Gap → Future Technology)

```
1. Knowledge Gap (입력/시드)
     — Research Engine 보고서의 "11. 후속 조사 대상"을 1차 시드로 삼는다
       (이미 실사용 검증된 산출물 재활용 — 새 수집 파이프라인 불필요).
       보조 시드: 명시적 미해결 Risk, 마스터의 직접 프롬프트.
   ▼
2. Novel Combination (기계 스캔 + LLM 발산)
     — 기계: knowledge-graph.json에서 ontologyClass가 서로 다른 노드 쌍을
       의도적으로 선택(같은 클래스끼리 묶는 Research Engine의 Relationship
       단계와 정반대 방향의 그래프 순회).
     — LLM: 선택된 조합 후보 3~5개를 병렬 생성. "그럴듯함"이 아니라
       "얼마나 안 해본 조합인가"를 1차 기준으로 프롬프트 설계.
   ▼
3. Novelty Check (기계 + LLM) — **여기로 앞당김**
     — 기존 canonical/raw에 이미 같은 조합이 있는지 대조해서 살아남은
       후보만 다음 단계로 넘긴다(Research Engine의 "fact 재진술 승격
       거부"와 같은 철학). 뒤(4·5단계)에서 시간을 들여 추세를 외삽하기
       전에, 이미 존재하는 조합에 헛수고하지 않도록 먼저 거른다.
```

### 3.2 심화·검증 단계 (Technology Evolution → 후보 타입 결정)

```
4. Technology Evolution (기계 + LLM)
     — Novelty Check를 통과한 조합에 포함된 각 Technology 노드의 **시간에
       따른 변화 이력**을 본다. 이미 존재하는 재료가 있다: `scripts/
       param-diff.py`가 PX4/ArduPilot 버전 간 파라미터 diff를 자동 생성
       중 — 이게 사실상 "Technology Evolution"의 첫 실측 사례다(새 인프라
       아님, 이미 있는 것 재해석).
   ▼
5. Future Technology (LLM, 추세 외삽)
     — Technology Evolution의 추세를 앞으로 연장했을 때 "다음에 나올 법한
       기술 방향"을 추정. 이 단계 산출물은 명시적으로 **추측(hypothesis급
       이하)**으로 표시 — Research Engine의 claim_type 3단계보다 낮은
       확실성임을 라벨로 명시(§4 안전장치 참조).
   ▼
6. Feasibility Critique (LLM, 독립 컨텍스트)
     — 사실 여부가 아니라 "지금 있는 하드웨어/기술/예산으로 만들 수
       있는가"만 본다.
   ▼
7. Risk & Regulation Check (LLM)
     — GRAPH_SCHEMA.md의 `Risk` 타입과 연결. 안전·법적·규제·**이중용도
       (dual-use) 문제**를 명시(방산 응용 후보는 이 단계에서 반드시
       규제·윤리 검토를 거친다 — §3.3 참조).
   ▼
8. 후보 타입 분류 (LLM, 4택1 또는 미해당)
     Novelty·Feasibility·Risk 평가 결과를 종합해 아래 중 하나로 분류한다.
     여러 타입에 걸치면 주된 것 하나만 선택(모호하면 Research Theme로
     보수적으로 분류).
```

### 3.3 후보 타입 (Candidate Types)

| 타입 | 기준 | canonical 온톨로지와의 관계 |
|---|---|---|
| **Patent Candidate** | 신규성 높음 + 실현가능성 높음 + 구체적 청구항 수준으로 좁혀짐 | `GRAPH_SCHEMA.md`의 `Patent`(현재 인스턴스 0건)의 첫 실제 소비처 |
| **Mission Candidate** | 실현가능성 높음 + 명확한 운용 목적 있음(정찰/배송/점검 등) | `Mission` 온톨로지 클래스로 이어짐(§5, 사람이 수동 승격) |
| **Weapon System Candidate** | 방산/보안 응용 성격이 명확함 | ⚠️ **아래 별도 원칙 적용** |
| **Research Theme** | 위 셋 중 무엇도 아직 아님 — 더 조사가 필요 | **Research Engine으로 되돌려 보낸다**(새 연구 목표 시드로 순환 — 이게 유일하게 자동 루프가 닫히는 지점) |

**`Weapon System Candidate`에 대한 원칙**: 이 타입은 **무기를 설계·제안하는
기능이 아니다.** 이 지식베이스가 이미 다루고 있는 방산 관련 공개 정보
(`fcc-drone-regulations`, `drone-news-regulations`, `recon-swarm-project` 등
기존 canonical 문서)의 연장선에서, **"이 조합이 방산/보안 분야의 공개된
기술 동향과 관련된 주제로 분류된다"는 지식 카테고리 라벨일 뿐**이다.
- 이 타입으로 분류된 항목은 구체적 설계·사양·구현 방법을 생성하지 않는다
  — Research Theme와 동일하게 "이 방향은 조사할 가치가 있다"는 수준에서
  멈춘다.
- `GO` 판정이 나더라도 §5의 원칙(사람이 수동으로 다음 단계를 만든다)이
  **더 엄격하게** 적용된다 — 자동으로 어떤 문서도 생성하지 않고, 마스터가
  직접 검토·기록 여부를 결정한다.
- 이 원칙은 설계 문서 차원의 안전장치이며, 실제 구현 시에도 완화하지 않는다.

---

## 3.4 Innovation Score

4개 세부 점수(0~10)의 가중합으로 우선순위를 매긴다 — 단일 뭉뚱그린 "혁신
점수"가 아니라 요소별로 나눠서, 왜 그 점수인지 추적 가능하게 한다.

```
InnovationScore = 0.3×Novelty + 0.3×Feasibility + 0.25×Value − 0.15×RiskPenalty
```

| 요소 | 산출 근거 | 비고 |
|---|---|---|
| `Novelty` | Novelty Check(3단계) 결과 — 기존 canonical/raw와의 거리 | 0 = 이미 존재, 10 = 완전 신규 조합 |
| `Feasibility` | Feasibility Critique(6단계) — 현재 하드웨어/기술 수준 대비 | 0 = 현재 기술로 불가능, 10 = 기존 부품 조합만으로 가능 |
| `Value` | Value Framing — 누가 왜 필요로 하는가의 구체성과 근거 | 근거 없이 "혁신적"이라 쓰면 자동 감점(Report Writer 검증) |
| `RiskPenalty` | Risk & Regulation Check(7단계) | 규제/안전 문제가 클수록 높음. `Weapon System Candidate`는 이중용도 리스크가 구조적으로 가산됨 |

점수는 **우선순위 정렬용이지 승인 여부를 자동 결정하지 않는다** — 최종
GO/HOLD/DISCARD는 항상 사람이 한다(§3.5). 점수가 높아도 사람이 DISCARD할
수 있고, 낮아도 GO할 수 있다.

### 3.5 최종 단계

```
9. Proposal Report
     — 구조: 조합 요소 / 후보 타입 / Innovation Score(4요소 분해) /
       왜 지금까지 없었는가 / 만들 수 있는가 / 무엇이 위험한가 /
       누구에게 가치 있는가 / 다음 단계
   ▼
10. Human Decision — 3지선다:
     GO(추가 개발 가치 있음) / HOLD(흥미롭지만 지금 아님) / DISCARD(폐기)
     Research Theme 타입은 GO 시 Research Engine의 새 연구 목표로 자동
     시드(유일한 자동 순환 지점 — 나머지 타입은 전부 사람이 다음 단계를
     수동으로 결정).
   ▼
11. Innovation Registry (canonical 아님 — §5)
```

---

## 4. 안전장치 — Research Engine보다 더 엄격해야 하는 이유

발산적 생성은 수렴적 검증보다 환각 위험이 구조적으로 크다. 비교 대상인
"이미 알려진 참"이 없기 때문에 Evidence Verifier 같은 대조 검증이 원리적으로
약해진다. 따라서:

1. **Idea Generation은 반드시 복수 후보를 내야 한다**(단일 답이면 "이게
   유일한 정답"처럼 보이는 착시 위험).
2. **Feasibility Critique는 독립 컨텍스트**(Research Engine의 Critic과
   동일 원칙) — 아이디어를 낸 맥락을 이어받지 않고 회의적으로 재검토.
3. **Novelty Check가 Technology Evolution/Future Technology 이전**(3단계,
   §3.1) — 추세를 외삽하기 전에 먼저 "이미 있는 것"부터 걸러내 헛된
   추정에 시간을 쓰지 않는다.
4. **세션당 LLM 호출 상한을 Research Engine(10회)보다 낮게 잡지 않는다**
   — 오히려 후보가 여러 개(3~5)라 호출이 더 많이 필요할 수 있다. 상한은
   구현 시 재산정 필요.

---

## 5. canonical에 절대 직접 쓰지 않는 이유 (구조적 결정)

Research Engine의 `KnowledgeClaim`은 "참일 가능성이 있는 것"이고,
`research-promote.py`가 `fact`/`insufficient_evidence`를 걸러내면 canonical에
반영해도 SCHEMA.md의 "증거 기반 지식"이라는 성격이 유지된다.

Innovation Engine의 산출물은 **참/거짓 판정 대상이 아니다** — "아직 안
만들어진 것에 대한 제안"이다. 이걸 `concepts/`에 넣으면 SCHEMA.md의
근본 계약(canonical = 출처가 있는 검증된 지식)이 깨진다. 그래서:

- Innovation 산출물은 `research/`와 나란한 **새 최상위 영역** `innovations/`
  (제안만, RESEARCH_SCHEMA.md의 `research/`와 동일한 격리 원칙: canonical/raw
  읽기 전용, 쓰기는 이 영역 안에서만)에 보관한다(설계만, 미생성).
- `GO` 판정을 받은 제안이 실제로 프로젝트로 채택되면, 그때 비로소 사람이
  `Mission`(ontology class, ops-mission domain)으로 **수동으로** 새 canonical
  문서를 작성한다 — Innovation Engine이 자동으로 Mission을 만들지 않는다.
  이 지점이 "제안"에서 "실제 프로젝트"로 넘어가는 유일한 다리이며, 반드시
  사람이 건넌다.

---

## 6. 다른 설계 문서와의 관계

- Cross-Domain Scan(§3.2)은 `GRAPH_SCHEMA.md`가 제안한 `kind`/`ontologyClass`
  분류가 있어야 "서로 다른 도메인"을 기계적으로 구분할 수 있다 — Phase O1이
  이미 구현되어 있어 이 설계는 즉시 그 위에 얹을 수 있는 상태다.
- `Risk`, `Mission` 타입은 `GRAPH_SCHEMA.md` §3.1에서 이미 예약해뒀지만
  인스턴스가 0건이었다 — Innovation Engine이 실제로 가동되면 이 타입들이
  처음으로 채워질 첫 소비처가 된다.
- `RESEARCH_ENGINE.md`의 Relationship 단계(같은 도메인 내 관계 찾기)와
  Innovation Engine의 Cross-Domain Scan(다른 도메인 간 의도적 연결)은
  **정반대 방향의 그래프 순회**라는 점을 명시적으로 구분해서 구현해야
  한다 — 같은 코드를 재사용하려는 유혹이 있겠지만, "가까운 것 찾기"와
  "먼 것 찾기"는 다른 알고리즘이다.

---

## 7. 구현 착수 전 결정 필요 사항

1. `innovations/` 디렉터리 구조를 `research/`와 완전히 대칭으로 할지(runs/
   drafts/ 등), 아니면 더 단순한 단일 폴더로 할지.
2. Idea Generation의 후보 수(3? 5?)와 그만큼 늘어나는 LLM 호출 비용을
   구독 한도 내에서 감당 가능한지 사전 확인.
3. Cross-Domain Scan의 "의도적으로 먼 조합"을 고를 기준 — 완전 무작위인지,
   아니면 "그래프 거리가 N-hop 이상인 것 중 confidence가 낮지 않은 것"
   같은 최소 필터가 있는지(무작위면 대부분 무의미한 조합이 나올 위험).
4. `GO` 판정 후 Mission 전환을 어느 정도까지 반자동화할지(완전 수동 vs
   Mission 문서 초안까지는 자동 생성해서 사람이 다듬기만 하게 할지).
