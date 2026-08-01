# ONTOLOGY_SPEC.md — 드론 AI 연구원 온톨로지 설계

> 작성: 2026-08-01 | 역할: Ontology Engineer | 성격: **설계 문서 — 구현하지 않았다.**
> 전제: 이 시스템은 텍스트 검색 시스템이 아니라 **온톨로지 기반 AI 연구원**이다.
> `SCHEMA.md`의 `tags`/`domain` 프론트매터는 평면적 라벨일 뿐, 클래스 간 관계·제약·
> 추론을 표현하지 못한다. 이 문서는 그 위에 놓일 형식 온톨로지를 설계한다.
> 대상 어휘: 드론 · AI · 음성인식 · Mission · ROS2 · PX4 · Drone · SLM · LLM · Task · Sensor.

---

## 0. 왜 온톨로지인가 (검색 시스템과의 차이)

현재 `research-search.py`/`lib/rag.ts`는 "이 문서가 이 질의와 얼마나 비슷한 텍스트인가"만
답한다. 온톨로지는 다른 질문에 답한다: **"이 Task가 실행 가능한가?", "이 Mission이
왜 실패했는가?", "이 Sensor의 정확도로 이 Task를 수행할 자격이 있는가?"** — 관계와
제약을 명시적으로 모델링해야만 답할 수 있는 질문이다. 검색은 유사도를 반환하지만,
온톨로지는 **추론(reasoning)**을 반환한다.

이 온톨로지는 canonical 문서(`concepts/`, `entities/`)의 frontmatter(`domain`,
`tags`)를 대체하지 않는다 — 그 위에서 인스턴스를 분류하고 관계를 부여하는
**의미 계층**으로 설계한다.

---

## 1. 클래스 계층 (Class Hierarchy)

```
Thing
├── PhysicalEntity
│   ├── Drone                        # UAV 기체 자체
│   │   ├── Multirotor
│   │   ├── FixedWing
│   │   └── VTOL
│   ├── Sensor
│   │   ├── IMU
│   │   ├── GNSS                     # GPS/GNSS 수신기
│   │   ├── Camera
│   │   ├── LiDAR
│   │   ├── Barometer
│   │   ├── Magnetometer
│   │   └── Microphone               # 음성 입력 하드웨어
│   ├── Actuator
│   │   ├── Motor
│   │   ├── ESC
│   │   └── Gimbal
│   └── ComputeUnit
│       ├── FlightController         # PX4/ArduPilot 실행 하드웨어
│       └── CompanionComputer        # ROS2 + SLM 추론 실행 하드웨어
│
├── SoftwareSystem
│   ├── FlightStack
│   │   ├── PX4
│   │   └── ArduPilot
│   ├── MiddlewareFramework
│   │   └── ROS2
│   │       ├── ROS2Node
│   │       ├── ROS2Topic
│   │       └── ROS2Service
│   ├── AIModel
│   │   ├── SLM                      # 온보드 저지연 소형 모델
│   │   ├── LLM                      # 클라우드/고성능 대형 모델
│   │   └── PerceptionModel          # CV/SLAM 등 지각 모델(언어모델 아님)
│   └── VoiceRecognitionModule       # ASR — 음성을 텍스트로 변환하는 프런트엔드
│
├── AbstractProcess
│   ├── Mission
│   │   ├── MissionPlan              # 계획(설계 시점)
│   │   └── MissionExecution         # 실행 인스턴스(런타임)
│   ├── Task                         # Mission을 구성하는 실행 단위
│   │   ├── PerceptionTask
│   │   ├── NavigationTask
│   │   ├── CommunicationTask
│   │   └── DecisionTask             # 예: "음성 명령 해석", "행동 계획 생성"
│   └── VoiceCommand                 # 발화 캡처~해석까지의 이벤트
│
├── DataArtifact
│   ├── SensorReading                # 타임스탬프가 있는 센서 원시값
│   ├── Telemetry                    # MAVLink 메시지 / uORB 토픽
│   └── KnowledgeClaim                # ★ 2nd-brain research/ 스키마와의 연결점
│       └── (claim_type: fact | inference | hypothesis — RESEARCH_SCHEMA.md와 동일 값)
│
└── Agent
    ├── HumanOperator                # 마스터
    ├── AIAgent                      # SLM/LLM이 주도하는 의사결정자
    └── SwarmCoordinator
```

**용어 대응(요청된 어휘 전부 1급 클래스로 반영)**: 드론=`Drone`, AI=`AIModel`/`AIAgent`,
음성인식=`VoiceRecognitionModule`+`VoiceCommand`, Mission=`Mission`, ROS2=`ROS2`,
PX4=`PX4`(FlightStack 하위), SLM=`SLM`, LLM=`LLM`, Task=`Task`, Sensor=`Sensor`.

---

## 2. 관계(Object Properties)

| 관계 | Domain | Range | 의미 | 역관계 |
|---|---|---|---|---|
| `hasSensor` | Drone | Sensor | 기체가 탑재한 센서 | `mountedOn` |
| `hasActuator` | Drone | Actuator | 기체가 탑재한 구동기 | `mountedOn` |
| `hasComputeUnit` | Drone | ComputeUnit | 기체의 연산 유닛 | `installedIn` |
| `runsOn` | FlightStack | FlightController | 비행스택이 실행되는 하드웨어 | `hosts` |
| `runsOn` | ROS2 \| AIModel | CompanionComputer | ROS2/모델이 실행되는 하드웨어 | `hosts` |
| `controls` | FlightController | Actuator | 실시간 구동 제어 | `controlledBy` |
| `publishesTo` / `subscribesTo` | ROS2Node | ROS2Topic | pub/sub 관계 | — |
| `partOfMission` | Task | Mission | Task가 속한 Mission | `hasTask` |
| `dependsOn` | Task | Task | 선행 Task 의존성 | `blocks` |
| `performedBy` | Task | Drone \| AIAgent | 실행 주체 | `executesTask` |
| `triggeredBy` | Task | VoiceCommand | 음성 명령으로 촉발된 Task | `triggers` |
| `interpretedBy` | VoiceCommand | VoiceRecognitionModule | ASR 처리 주체 | `interprets` |
| `reasonedBy` | VoiceCommand \| DecisionTask | SLM \| LLM | 해석/계획을 수행한 모델 | `reasonsAbout` |
| `delegatesTo` | LLM | SLM | 클라우드→온보드 위임(연결 단절 시 등) | `delegatedFrom` |
| `consumes` | AIModel \| PerceptionModel | SensorReading | 모델의 입력 | `consumedBy` |
| `produces` | Task | Telemetry | Task 실행 산출물 | `producedBy` |
| `coordinates` | SwarmCoordinator | Drone | 군집 내 개별 기체 통제 | `coordinatedBy` |
| `justifiedBy` | Mission \| Task | KnowledgeClaim | 의사결정의 지식적 근거 | `justifies` |
| `hasConfidence` | KnowledgeClaim | xsd:string(`low`\|`medium`\|`high`) | RESEARCH_SCHEMA.md와 동일 값역 | — |
| `approvedBy` | KnowledgeClaim | HumanOperator | 승인 주체(research/ 승인 모델과 연결) | `approves` |
| `blockedBy` | Task | FailureCondition | 실행 차단 사유 | `blocks` |

---

## 3. 속성(Data Properties)

| 클래스 | 속성 | 타입 | 비고 |
|---|---|---|---|
| `Drone` | `droneId`, `model`, `weightKg`, `maxPayloadKg`, `flightMode`, `batteryPercent` | string/float/enum | `flightMode`는 PX4/ArduPilot 실제 모드 값과 동일 값역 사용 권장 |
| `Sensor` | `sensorType`, `updateRateHz`, `accuracy`, `unit` | string/float | Task 배정 가능 여부 판단에 사용(§4 규칙 3) |
| `Task` | `taskId`, `status`(`pending`\|`running`\|`completed`\|`failed`\|`blocked`), `priority`(`low`\|`normal`\|`critical`), `startTime`, `endTime` | string/enum/datetime | |
| `Mission` | `missionId`, `status`, `geofence` | string/enum/geo | |
| `VoiceCommand` | `rawAudioRef`, `transcript`, `language`, `asrConfidence`(0.0–1.0), `timestamp` | string/float/datetime | |
| `AIModel` | `modelName`, `parameterCount`, `latencyMs`, `deploymentLocation`(`onboard`\|`cloud`) | string/int/enum | `SLM`/`LLM` 구분은 `deploymentLocation`+`parameterCount` 조합으로 판별(§4 규칙 4) |
| `KnowledgeClaim` | `claimType`(`fact`\|`inference`\|`hypothesis`), `verificationStatus`(`grounded`\|`insufficient_evidence`) | enum | **RESEARCH_SCHEMA.md의 클레임 스키마와 값역을 그대로 공유** — 새 값역을 만들지 않는다 |

---

## 4. 추론 규칙 (Reasoning Rules)

SWRL 스타일 의사코드로 표기(구현 시 실제 SWRL/규칙 엔진으로 옮길 수 있는 형태로).

**규칙 1 — 저신뢰 음성 명령 차단 (안전)**
```
VoiceCommand(?vc) ∧ asrConfidence(?vc, ?c) ∧ swrlb:lessThan(?c, 0.7)
∧ triggeredBy(?t, ?vc)
→ status(?t, "blocked")
```
근거 부족한 음성 인식 결과로 Task를 실행하지 않는다 — `research/`의 `verification_status:
insufficient_evidence` 거부 원칙과 동일한 사상을 실시간 제어 계층에 적용한 것.

**규칙 2 — Task 의존성 차단**
```
Task(?t1) ∧ dependsOn(?t1, ?t2) ∧ status(?t2, ?s) ∧ swrlb:notEqual(?s, "completed")
→ status(?t1, "blocked")
```

**규칙 3 — 센서 능력 부적합**
```
Task(?t) ∧ requiresSensorType(?t, ?type) ∧ requiresMinRate(?t, ?minRate)
∧ performedBy(?t, ?drone) ∧ hasSensor(?drone, ?s) ∧ sensorType(?s, ?type)
∧ updateRateHz(?s, ?rate) ∧ swrlb:lessThan(?rate, ?minRate)
→ status(?t, "blocked") ∧ blockedBy(?t, "InsufficientSensorCapability")
```

**규칙 4 — SLM/LLM 판별(온톨로지 분류 규칙, 상태 전이 아님)**
```
AIModel(?m) ∧ deploymentLocation(?m, "onboard") ∧ parameterCount(?m, ?p)
∧ swrlb:lessThan(?p, 3000000000)   # 예시 임계값 — 실제 온보드 메모리 한계에 맞춰 조정
→ SLM(?m)

AIModel(?m) ∧ deploymentLocation(?m, "cloud")
→ LLM(?m)
```

**규칙 5 — 통신 단절 시 LLM→SLM 위임(안전 폴백)**
```
DecisionTask(?t) ∧ reasonedBy(?t, ?llm) ∧ LLM(?llm)
∧ Drone(?d) ∧ performedBy(?t, ?d) ∧ datalinkStatus(?d, "lost")
∧ delegatesTo(?llm, ?slm) ∧ SLM(?slm)
→ reasonedBy(?t, ?slm)
```
클라우드 LLM에 접근할 수 없을 때 온보드 SLM으로 실시간 위임 — 실제 드론 시스템의
통신 단절 현실(`decentralized-swarm-gps-denied` 등 기존 canonical 문서가 이미
다루는 문제)을 온톨로지 규칙으로 형식화한 것.

**규칙 6 — 미승인 가설로 Mission 근거 금지 (연구 루프 승인 모델과의 결합)**
```
Mission(?m) ∧ justifiedBy(?m, ?k) ∧ KnowledgeClaim(?k)
∧ claimType(?k, "hypothesis") ∧ NOT approvedBy(?k, ?human)
→ INVALID(?m)   # 이 Mission은 온톨로지 상 "정당화되지 않음"으로 표시
```
이 규칙이 `AI_RESEARCHER_ARCHITECTURE.md` §5(Human Approval 두 갈래 모델)를
온톨로지 차원에서 강제한다 — **승인 안 된 가설은 그 자체로 존재할 수 있지만
(discovery candidate), Mission의 근거로 채택되는 순간 온톨로지 추론이 이를
무효로 표시한다.**

**규칙 7 — 치명적 Task 실패 시 Mission 중단**
```
Mission(?m) ∧ hasTask(?m, ?t) ∧ status(?t, "failed") ∧ priority(?t, "critical")
→ status(?m, "aborted")
```

**규칙 8 — 군집 안전(데이터링크 없는 기체 제외)**
```
SwarmCoordinator(?sc) ∧ coordinates(?sc, ?d) ∧ datalinkStatus(?d, "lost")
→ excludedFromFormation(?d, true)
```

---

## 5. 기존 SCHEMA.md와의 관계 (호환성 — 마이그레이션 미실행)

실측 확인(2026-08-01): 현재 canonical 문서는 **두 개의 서로 다른, 완전히 정렬되지
않은 평면 태그 체계**를 병행 사용 중이다.

- `SCHEMA.md` 등록 `tags`: `drone, datalink, swarm, voice-control, drone-hw, drone-sw, drone-ai, ai-agent` (8개)
- 실제 문서의 `domain` 필드값: `flight-control(30), ai-autonomy(25), comms-protocol(19), hardware(18), ops-mission(14), gcs-software(11), regulations(4), ai-agent(2)` (8개, 서로 다른 이름)

이 온톨로지는 두 체계를 **대체하지 않고 상위에서 통합 매핑**한다(제안, 미실행):

| SCHEMA `domain` 값 | 온톨로지 클래스(들) |
|---|---|
| `flight-control` | `FlightStack`, `FlightController` |
| `ai-autonomy` | `AIModel`, `PerceptionModel`, `DecisionTask` |
| `comms-protocol` | `ROS2Topic`(통신 부분), `Telemetry`, datalink 관련 관계 |
| `hardware` | `Sensor`, `Actuator`, `ComputeUnit` |
| `ops-mission` | `Mission`, `Task` |
| `gcs-software` | `ROS2`, `SwarmCoordinator`(지상국 통제 측면) |
| `regulations` | (이 온톨로지 범위 밖 — 별도 RegulatoryConstraint 클래스는 후속 설계 과제로 남김) |
| `ai-agent` | `AIAgent`, `SLM`, `LLM` |

`tags`의 `voice-control`/`swarm`은 domain 실측값에 없었다 — 이는 온톨로지 설계
과정에서 우연히 발견한 **기존 태그 체계 자체의 커버리지 공백**이다(태그는
등록돼 있는데 실제로 그 도메인 값을 쓴 문서가 없다는 뜻). 이 온톨로지의
`Drone`(하위 Multirotor 등 군집 시나리오 포함)과 `VoiceRecognitionModule`
클래스가 이 공백을 명시적으로 메운다.

---

## 6. 예시 인스턴스 시나리오 (검증용 워크스루)

```
:reconDrone_01 a :Multirotor ;
    :hasSensor :lidar_01, :mic_01 ;
    :hasComputeUnit :companion_01 .

:mic_01 a :Microphone .
:companion_01 a :CompanionComputer ;
    :runsOn :ros2_instance_01, :onboardSLM_01 .

:onboardSLM_01 a :SLM ;
    :deploymentLocation "onboard" ;
    :parameterCount 1500000000 .

:cloudLLM_01 a :LLM ;
    :deploymentLocation "cloud" ;
    :delegatesTo :onboardSLM_01 .

:vc_001 a :VoiceCommand ;
    :transcript "정찰 구역으로 이동해" ;
    :asrConfidence 0.92 ;
    :interpretedBy :asrModule_01 ;
    :reasonedBy :cloudLLM_01 .

:task_navigate_01 a :NavigationTask ;
    :triggeredBy :vc_001 ;
    :performedBy :reconDrone_01 ;
    :partOfMission :mission_recon_01 .
```

이 인스턴스에서 규칙 1(신뢰도 0.92 > 0.7 → 차단 안 됨), 규칙 5(datalink 정상이면
LLM 유지, 끊기면 SLM으로 위임)가 실제로 평가 가능하다 — 이것이 텍스트 검색으로는
얻을 수 없는, 온톨로지가 제공하는 차별점이다.

---

## 7. 구현 시 고려사항 (설계만, 지금 만들지 않음)

- **저장 형식**: OWL/Turtle 전체 도입은 과설계 가능성 있음(현 코퍼스 규모 대비) —
  1차로는 `.ua/knowledge-graph.json`의 엣지에 이미 추가된 `type` 필드(Phase 2,
  `wikilink`/`contradicts`)를 확장해 위 관계 어휘(`hasSensor`, `dependsOn` 등)를
  점진적으로 편입하는 것이 `TECHNOLOGY_DECISION_RECORD.md`의 "실측 병목 후 도입"
  원칙에 부합한다. Neo4j/RDF 트리플스토어는 §4 규칙 같은 다중 홉 추론이 실제로
  텍스트/그래프 방식으로 병목을 일으킬 때 재검토(이미 `TECHNOLOGY_DECISION_RECORD.md`
  #6·#8에 KuzuDB 재검토 트리거로 명시됨).
- **추론 엔진**: SWRL 규칙을 실제로 돌리려면 별도 추론기(예: HermiT, Pellet)가
  필요하다 — 지금 구조(파일 기반, Vercel 서버리스)와의 통합 방법은 별도 설계 필요.
  대안으로, §4 규칙들을 **`research-promote.py`의 검증 로직과 유사한 방식으로 파이썬
  함수로 직접 구현**하는 경량 접근도 가능(정식 온톨로지 엔진 없이 규칙 1·2·6은
  이미 이번 세션에서 유사한 검증 로직으로 구현된 전례가 있음 — `research-promote.py`의
  all-or-nothing 검증이 사실상 규칙 6의 축소판).
- **KnowledgeClaim 연결**: `research/hypotheses/*.md`의 `claim_type`/
  `verification_status` 값역을 그대로 재사용하도록 설계했다(§3) — 새 값역을 만들면
  두 시스템(연구 루프, 온톨로지)이 또 다른 형태로 갈라질 위험(기존에 이미
  실측한 "하이브리드 검색 로직 2중 구현" 기술부채와 같은 패턴)이 있기 때문.
