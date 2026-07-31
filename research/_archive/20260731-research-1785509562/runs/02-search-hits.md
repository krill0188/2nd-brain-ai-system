# 기계 검색 결과 (Retriever — LLM 미사용)

### 검색: 통신 두절/저대역 환경에서 군집 드론이 사용하는 자율 협조 알고리즘(분산 합의, 스웜 알고리즘)에는 어떤 것들이 있는가?

**canonical 검색 결과**
- [7] `concepts/swarm-coordination.md` — Swarm Drone Coordination (slug: `swarm-coordination`, layer: concepts)
  발췌: 스웜 드론은 여러 대의 UAV가 협력하여 공통 목표를 달성하는 다중 기체 시스템이다. Leader-Follower 구조, 분산 제어, 자율 협력 등 다양한 아키텍처가 존재한다.^[raw/articles/mastervault-swarm-architecture.md]

## 시스템 아키텍처

```
┌─────────────────────────────────────────────────┐
│              Ground Station                      │
│    ┌───────────┐  ┌───────────┐  ┌────────┐   │
│    │ Swarm GCS │  │ QGC Custom│  │ Web GCS│   │
│    └─────┬─────┘  └─────┬─────┘  └───┬────┘   │
└──────────┼──────────────┼────────────┼────────┘
           │              │            │
           └──────────────┼────────────┘
                          │ MAVLink
            ┌─────────────┼──────────────┐
            ▼             ▼              ▼
      ┌─────────┐   ┌─────────┐   ┌─────────┐
      │ Leader  │   │Follower │   │Follower │
      │         │◄──►│         │◄──►│         │
      └─────────┘   └─────────┘   └─────────┘
```

## 통신 구조

| 링크 | 프로토콜 | 용도 |
|----
- [7] `concepts/swarm-modes.md` — Swarm Modes — 군집 드론 운용 모드 (slug: `swarm-modes`, layer: concepts)
  발췌: 군집 드론 시스템의 운용 모드 정의. Leader-Follower 구조 기반의 4가지 주요 모드.

## 시스템 구조

```
┌─────────────────────────────────────────────────┐
│                  Ground Station                  │
│  ┌───────────┐  ┌───────────┐  ┌────────────┐  │
│  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │
│  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │
└────────┼───────────────┼──────────────┼─────────┘
         │               │              │
         └───────────────┼──────────────┘
                         │ MAVLink
         ┌───────────────┼──────────────┐
         ▼               ▼              ▼
   ┌──────────┐    ┌──────────┐   ┌──────────┐
   │ Leader   │    │ Follower │   │ Follower │
   │ (CUAV)   │◄──►│ (Holybro)│◄──►│ (Holybro)│
   └──────────┘    └──────────┘   └──────────┘
     V7+ #1009       6C #1041       6C #xxxx
```

## 통신 구조

| 링크 | 프로토콜 | 용도 |
|------|----------|------|
| GCS ↔ Leader | MAVL
- [6] `concepts/decentralized-swarm-gps-denied.md` — Decentralized UAV Swarms in GPS/Communication-Denied Environments (slug: `decentralized-swarm-gps-denied`, layer: concepts)
  발췌: GPS 및 통신 차단 환경에서 지상 표적 보호를 위한 분산형 UAV 군집 시스템. 온보드 센서만을 활용하여 표적을 추적하고 군집으로 협업하며, 칼만 필터로 상대 측정만으로 UAV 및 표적 상태를 추정한다.

## 핵심 개념

### 분산 군집 포위 기법
- **Target Tracking**: 온보드 센서 기반 미지 표적 상태 추정
- **Kalman Filters**: 상대 측정만으로 UAV 위치 및 표적 상태 추정
- **Encirclement Strategy**: 표적 운동에 적응하는 분산 포위 기법

### 환경 가정
- GPS 차단 (GPS-denied)
- UAV 간 통신 불가
- 온보드 센서만 의존

### 응용 시나리오
- 군사 표적 방어
- 적대적 UAV 탐지 및 요격
- 실제 로봇 검증 완료

## 관련 페이지

- [[swarm-coordination]] — 군집 드론 운용 모드 및 편대 비행
- [[datalink-communication]] — RF, LTE, WiFi 등 데이터링크 통신
- [[drone-ai-agents]] — 다중 에이전트 협력 및 합의 알고리즘

## 출처

- Silveria et al., "Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments", arXiv:2607.20710, 2026.
- [6] `concepts/recon-swarm-project.md` — Recon Swarm Project — 지능형 자율 군집정찰드론 (slug: `recon-swarm-project`, layer: concepts)
  발췌: 지능형 자율 군집정찰 시스템 개발 프로젝트. 학술연구 기반의 4단계 로드맵을 통해 단일 기체 자율비행에서 GPS-denied 실내 군집까지 단계적 확장.

## 프로젝트 개요

- **목표**: 학술연구 기반 자율 군집정찰 시스템
- **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041)
- **펌웨어**: ArduPilot (커스텀)

## 4단계 로드맵

| 단계 | 내용 | 상태 |
|:----:|------|:----:|
| 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 |
| 2 | 2기 편대비행 + 통신 검증 | 계획 |
| 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 |
| 4 | GPS-denied + 실내 군집 | 계획 |

## 센서 스택

| 센서 | 용도 | 인터페이스 |
|------|------|-----------|
| LiDAR | 장애물 감지/매핑 | UART/I2C |
| 카메라 (RGB) | 정찰/객체 인식 | CSI/USB |
| Radar | 전방위 감지 | SPI |
| Optical Flow | GPS-denied 위치추정 | I2C |
| RTK GPS | 정밀 위치 | UART |

## 안전 시스템

- Geofence (하드웨어+소프트웨어 이중)
- 배터리 페일세이프 (자동 RTL)
- 통신 두절 대응 (독립 귀환)
- 충돌 회피 (최소 이격거리 유지)

## SITL 테스트 환경

```bash
# ArduPilot SITL 멀티 기체
sim_vehicle.py -v ArduCopter --instance 0 -L HOME_LAT,HOME_LNG,ALT,HDG
sim_vehicle.py -v ArduCopter --instance 1 -L HOME_LAT,HOME_LNG,ALT,HDG
``
- [5] `concepts/federated-lightweight-intrusion-detection.md` — Federated Lightweight Intrusion Detection in Drone Swarms (slug: `federated-lightweight-intrusion-detection`, layer: concepts)
  발췌: 지식 증류(Knowledge Distillation, KD)를 활용한 드론 스웜용 경량 연합학습(FL) 기반 침입 탐지 시스템(IDS). 리소스 제약 환경에서 효율성과 탐지 성능의 균형을 달성한다.

## 배경

드론 스웜은 감시, 재난 대응, 인프라 모니터링 등 중요한 애플리케이션에 배포되지만:
- 개방형 통신 채널에 의존
- 제한된 계산 리소스
- 다양한 사이버 위협에 취약

## 기존 방식의 한계

| 방식 | 한계 |
|------|------|
| 중앙집중식 ML | 모든 데이터 수집 필요, 프라이버시 문제 |
| 기존 FL | 통신 및 계산 오버헤드 |
| 리소스 제약 | 효율성과 탐지 성능 균형 어려움 |

## 제안 프레임워크

### 핵심 기술
- **Deep Neural Networks (DNN)**: 복잡한 패턴 학습
- **Knowledge Distillation (KD)**: 모델 복잡성 및 통신 비용 감소
- **Federated Learning**: 분산 학습 및 프라이버시 보존

### 성능 결과

| 지표 | 결과 |
|------|------|
| 탐지 정확도 | 약 98.6% |
| 통신 비용 감소 | 약 70% |
| 계산 오버헤드 감소 | 29% |

## 실험 환경

- **하드웨어**: Raspberry Pi 4
- **데이터셋**: 실제 드론 네트워크 데이터셋
- **평가**: 리소스 제약 조건에서의 실용성 검증

## 시사점

FL과 KD의 결합은 리소스 제약 드론 네트워크에서 안전하고 효율적인 배포를 위한 실용적이고 적합한 솔루션임을 입증한다.

## 관련 페이지

- [[chained-attacks-drone-fl]] — 드론 FL 체인 공격 분석
- [[swarm-coordination]] — 스웜 협업 및 보안
- [[drone-ai

**raw 검색 결과**
- [4] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [3] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [3] `raw/articles/mastervault-swarm-architecture.md` — --- source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4" tags: [swarm, datalink] ---  # 스웜 드론 아키텍처  ## 시스템 구조  ``` ┌─────────────────────────────────────────────────┐ │                  Ground Station                  │ │  ┌───────────┐  ┌───────────┐  ┌────────────┐  │ │  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │ │  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │ └────────┼───────────────┼──────────────┼─────────┘          │               │              │          └───────────────┼──────────────┘                          │ MAVLink          ┌───────────────┼──────────────┐          ▼               ▼              ▼    ┌──────────┐    ┌──────────┐   ┌──────────┐    │ Leader   │    │ Follower │   │ Followe
- [2] `raw/articles/entity-pixhawk-hardware.md` — --- title: "Pixhawk Flight Controller — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/flight_controller/" author: "Pixhawk / PX4 Docs / Master" sha256: "" tags: [drone-hw, drone-sw] ---  # Pixhawk Flight Controller — Entity Reference  ## 개요  Pixhawk는 PX4 프로젝트와 함께 개발된 오픈 하드웨어 비행 제어기(FC) 플랫폼이다. Holybro, mRo, CubePilot 등 다수 제조사가 공식 Pixhawk 표준 호환 제품을 생산한다.  - **표준 문서**: https://github.com/pixhawk/Pixhawk-Standards - **주요 제조사**: Holybro (공식), CubePilot, mRo Technology - **버스 표준**: UAVCAN/DroneCAN, UART, SPI, I2C, CAN  ## 주요 모델 비교  | 모델 | MCU | RAM | 플래시 | 특징 | |---|---|---|---|---| | Pixhawk 1 | STM32F427 | 168MHz / 256KB | 2MB | 초기 레퍼런스, 단종 | | Pixhawk 4 | STM32F765 | 216MHz / 512KB | 2MB | Holybro 공식, 현 주력 | | Pixhawk 6C | STM32H743 | 480MHz / 1MB | 2MB | 최신 고성능 | | Pixhawk 6X | STM32H753 | 480MHz / 1MB | 2MB | 6C 상위 (이중화) | | Cub
- [2] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,

**뉴스 검색 결과**
- [1] 옛날통닭·닭강정·커피·땅콩빵 드론이 배송…무료 서비스 — https://news.google.com/rss/articles/CBMiYEFVX3lxTE43MXo1TlE3cmg3QTBSUFdNdlFrMWpYVzVGRklLYWtJVER3UkpDUUQ4RUFybmFZX20tZS1XSjh3VTEyUC1HeHBESkQ0VlJudDlqdlVuVnlqTDM5anNUNnZOX9IBeEFVX3lxTE5VYTdvYWJ0Vl9CcWJocjZCS2hkTHFqMHhEQkloVXdkZVB5NmdIRmhGNjkxUkJCY2JQSnpxMDBxaml0enI0YlB2ZFpJaENGR0swOHdWYVZjQS1jTE9lMldaZG5yaVAtbVBjM3JLX1RYbWMtSEctSVJfMw?oc=5
- [1] 드론이 흔든 전장, 방산 돈줄도 바꿨다…M&A·투자 경쟁 가열 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE9vZ1NkbkxhdEVyZC1qZHd6S2lwdUd6cXpIUE1tTHNoeUplUUJIcG00RlhZMU0wS3hYRGJ4UlRVVWVPcmZNYkxaMC1ta3VjeGc?oc=5
- [1] 영주 서천에서 주문하면 드론이 배달합니다 — https://news.google.com/rss/articles/CBMiY0FVX3lxTFBFbWdHT2otYnhjSVZ0cFdRQUkxNzNFN0RuOGF3WWdZNGNtZndmalpnQVZ2Z3YtTWJQMEI0YTRZcTVCb2R2RFJfUjduLXVvUTZ1cEIwWHBwT0VKbVhQcml2cVpkcw?oc=5
- [1] 옛날통닭·닭강정·커피·땅콩빵 드론이 배송…무료 서비스 — https://news.google.com/rss/articles/CBMieEFVX3lxTE5VYTdvYWJ0Vl9CcWJocjZCS2hkTHFqMHhEQkloVXdkZVB5NmdIRmhGNjkxUkJCY2JQSnpxMDBxaml0enI0YlB2ZFpJaENGR0swOHdWYVZjQS1jTE9lMldaZG5yaVAtbVBjM3JLX1RYbWMtSEctSVJfM9IBeEFVX3lxTE5VYTdvYWJ0Vl9CcWJocjZCS2hkTHFqMHhEQkloVXdkZVB5NmdIRmhGNjkxUkJCY2JQSnpxMDBxaml0enI0YlB2ZFpJaENGR0swOHdWYVZjQS1jTE9lMldaZG5yaVAtbVBjM3JLX1RYbWMtSEctSVJfMw?oc=5

**그래프 인접 슬러그** (1-hop): `ardupilot-architecture`, `chained-attacks-drone-fl`, `computer-vision-drone`, `cross-layered-medical-drone-coordination`, `datalink-communication`, `distributed-aerial-surveillance-swarm`

### 검색: 온디바이스 AI(엣지 컴퓨팅) 기반 드론의 연산·전력 제약이 자율 임무 수행 성능에 어떤 영향을 미치는가?

**canonical 검색 결과**
- [5] `concepts/ai-personal-knowledge-management.md` — AI 개인 지식관리 (slug: `ai-personal-knowledge-management`, layer: concepts)
  발췌: AI 개인 지식관리는 자료를 많이 저장하는 일이 아니라, 원본과 해석의 경계를 보존하면서 검증된 지식을 반복해서 재사용할 수 있게 만드는 운영 체계다.

핵심 단위는 특정 앱이 아니라 추적 가능한 원본, 상호 연결된 Markdown, 명시적인 품질 규칙이다. ^[raw/youtube/📺 How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md]

## 지식의 세 층

| 층 | 목적 | 보존 원칙 |
| --- | --- | --- |
| 원본 | 논문·웹·영상과 메타데이터 보존 | 수정하지 않고 출처와 수집 시점을 남긴다. |
| 컴파일된 지식 | 개념·비교·질의를 재사용 가능하게 정리 | 출처, 링크, 갱신일과 신뢰도를 유지한다. |
| 집중 탐색 | 제한된 소스 묶음에 질문하고 가설 생성 | 생성 답변을 확정 지식과 구분한다. |

원본 도서관, 컴파일된 위키, 소스 기반 질의 공간을 분리하면 대용량 원본을 Markdown 저장소에 모두 복제하지 않으면서도 근거로 돌아갈 수 있다.

한 도구의 대화 기록이나 독점 형식이 사라져도 핵심 지식과 출처 관계가 남는다는 점도 중요하다. ^[raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md]

## 운영 순환

1. 원본과 메타데이터를 먼저 보존한다.
2. 반복해서 쓸 가치가 있는 내용만 개념·비교·질의 문서로 컴파일한다.
3. 새 문서를 기존 지식과 연결하고 중복·모순·출처 누락을 검사한다.
4. 지식그래프로 군집, 브리지, 고립 문서와 약한 연결을 탐색한다.
5. 그래프가 제안한 관계를 원본 또는 제한된 소스 묶음으로 검증한다.

- [5] `concepts/recon-swarm-project.md` — Recon Swarm Project — 지능형 자율 군집정찰드론 (slug: `recon-swarm-project`, layer: concepts)
  발췌: 지능형 자율 군집정찰 시스템 개발 프로젝트. 학술연구 기반의 4단계 로드맵을 통해 단일 기체 자율비행에서 GPS-denied 실내 군집까지 단계적 확장.

## 프로젝트 개요

- **목표**: 학술연구 기반 자율 군집정찰 시스템
- **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041)
- **펌웨어**: ArduPilot (커스텀)

## 4단계 로드맵

| 단계 | 내용 | 상태 |
|:----:|------|:----:|
| 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 |
| 2 | 2기 편대비행 + 통신 검증 | 계획 |
| 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 |
| 4 | GPS-denied + 실내 군집 | 계획 |

## 센서 스택

| 센서 | 용도 | 인터페이스 |
|------|------|-----------|
| LiDAR | 장애물 감지/매핑 | UART/I2C |
| 카메라 (RGB) | 정찰/객체 인식 | CSI/USB |
| Radar | 전방위 감지 | SPI |
| Optical Flow | GPS-denied 위치추정 | I2C |
| RTK GPS | 정밀 위치 | UART |

## 안전 시스템

- Geofence (하드웨어+소프트웨어 이중)
- 배터리 페일세이프 (자동 RTL)
- 통신 두절 대응 (독립 귀환)
- 충돌 회피 (최소 이격거리 유지)

## SITL 테스트 환경

```bash
# ArduPilot SITL 멀티 기체
sim_vehicle.py -v ArduCopter --instance 0 -L HOME_LAT,HOME_LNG,ALT,HDG
sim_vehicle.py -v ArduCopter --instance 1 -L HOME_LAT,HOME_LNG,ALT,HDG
``
- [5] `entities/xtend-ai-robotics.md` — XTEND AI Robotics (slug: `xtend-ai-robotics`, layer: entities)
  발췌: 이스라엘 방위 기술 기업 XTEND와 미국 JFB Construction Holdings의 합병으로 설립된 방위 로봇 기업. 2026년 7월 $15억 전량주식 거래로 합병 발표.

## 합병 정보

- **거래 규모**: $15억 (전량주식)
- **상장**: 나스닥 (티커: XTND 예정)
- **완료 예정**: 2026년 중반
- **합병 대상**: XTEND + JFB Construction Holdings (Nasdaq: JFB)

## 사업 영역

- 방위용 드론 및 로봇 시스템
- AI 기반 자율 로봇 기술
- 군용 무인 시스템

## 관련 항목

- [[ai-agent]] — AI 에이전트 기술
- [[drone-ai-agents]] — 드론 AI 에이전트
- [[drone-sw]] — 드론 소프트웨어
- [4] `concepts/chained-attacks-drone-fl.md` — Chained Attacks on Drone-Based Federated Learning (slug: `chained-attacks-drone-fl`, layer: concepts)
  발췌: 드론 기반 연합학습(Federated Learning, FL) 시스템에 대한 체인 공격 연구. 네트워크 계층의 DoS 공격과 자격 증명 기반 사칭을 결합한 공격 체인을 분석한다.

## 개요

Edge Intelligence(EI)는 드론 스웜과 같은 미션 크리티컬 무인 플랫폼에 협업적 모델 학습을 가능하게 하는 변혁적 모델이다. 그러나 FL 배포의 보안은 네트워크 가용성과 강력한 클라이언트 인증 메커니즘 모두에 의존한다.

## 공격 벡터

### 1. 네트워크 계층 DoS 공격
- **802.11 deauthentication 공격**: 합법적인 드론을 오프라인으로 강제 종료
- 무선 연결 중단을 통한 가용성 저해

### 2. 자격 증명 기반 사칭
- 연결 해제된 드론의 추출된 자격 증명을 사용한 사칭
- 단일 요소 인증이 연결 해제 후 사칭을 허용함

## 영향 분석

| 조건 | 영향 |
|------|------|
| IID 데이터 분포 | 상대적으로 안정적인 학습 |
| Non-IID 데이터 분포 | 상당한 학습 불안정성 |
| 단기 무선 중단 | 장기적인 학습 품질 저하로 확대 |

## 실험 검증

- **프레임워크**: Flower 프레임워크
- **테스트베드**: Raspberry Pi 및 Jetson 장비
- **데이터 분포**: IID 및 Non-IID 조건 모두 테스트

## 시사점

미션 크리티컬 드론 배포에서 가용성과 인증 취약점을 동시에 해결하는 방어 방향 필요:
- 다중 요소 인증(MFA) 도입
- 무선 연결 복원 메커니즘 강화
- 비정상 노드 탐지 및 격리

## 관련 페이지

- [[federated-lightweight-intrusion-detection]] — 지식 증류를 활용한 FL 기반 IDS
- [[swarm-coordination]] — 
- [4] `concepts/drone-ai-agents.md` — Drone AI Agents (slug: `drone-ai-agents`, layer: concepts)
  발췌: 드론 AI 에이전트는 자율적 의사결정, 환경 인식, 목표 달성을 수행하는 지능형 소프트웨어 시스템이다. 단일 에이전트에서 다중 에이전트 협업까지 다양한 형태가 있다.

## 에이전트 유형

| 유형 | 설명 | 예시 |
|------|------|------|
| **Reactive Agent** | 간단한 조건-행동 매핑 | 장애물 회피 |
| **Deliberative Agent** | 계획 및 추론 | 미션 계획 |
| **Hybrid Agent** | 반응 + 의도 결합 | 현실용 시스템 |
| **Multi-Agent System** | 다중 에이전트 협력 | 스웜 드론 |

## 아키텍처 패턴

### 1. Perception-Action Loop

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│ Sensors │───▶│  Brain  │───▶│ Actuators│
└─────────┘    └─────────┘    └─────────┘
       ▲           │                │
       │           ▼                │
       └────┌──────────────┐◄──────┘
            │   Memory/KB    │
            └────────────────┘
```

### 2. BDI (Belief-Desire-Intention)

| 구성요소 | 설명 |
|----------|------|
| **Beliefs** | 환경에 대한 지식 |
| **Desires** | 목표/원하는 상태 |
| **Intentions** | 실행 중인 계획 |

### 3. Reinforcement Learning Agent

```
State ──▶ Polic

**raw 검색 결과**
- [3] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [3] `raw/papers/voice-control/lim2025-taking-flight-with-dialogue.md` — --- title: "Taking Flight with Dialogue: Enabling Natural Language Control for PX4-based Drone Agent" authors:   - Shoon Kit Lim   - Melissa Jia Ying Chong   - Jing Huey Khor   - Ting Yang Ling venue: arXiv year: 2025 doi: "10.48550/arXiv.2506.07509" url: "https://arxiv.org/abs/2506.07509" pdf: "https://arxiv.org/pdf/2506.07509" topics: [drone-sw, voice-control, ai-agent, ros2] abstract: |   Recent advances in agentic and physical artificial intelligence (AI) have largely focused    on ground-based platforms such as humanoid and wheeled robots, leaving aerial robots relatively    underexplored. Meanwhile, state-of-the-art unmanned aerial vehicle (UAV) multimodal vision-language    systems typically rely on closed-source models accessible only to well-resourced organizations.    To democratize natural language control of autonomous drones, we present an open-source agentic    framework th
- [2] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,
- [2] `raw/articles/ros2-devnotes.md` — --- source_url: "file://MasterVault/Drone/ROS/ROS2-DevNotes.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3f7a9c4e8d2b5a7f3c6e9d4b8a2f5c7e1d9a6b3f8c4e7d2a5b9f6c3d8e4a7b2f5" tags: [drone-sw] ---  # ROS2 개발 노트  ## 지원 버전  | 배포판 | EOL | 비고 | |--------|-----|------| | Humble | 2027-05 | LTS, 현재 메인 | | Jazzy | 2029-05 | LTS, 차기 이전 | | Kilted | 2025-12 | Rolling 기반 |  ## 드론 연동 스택  ``` ┌──────────────────────────────────────┐ │          ROS2 Application            │ │  Nav2 │ SLAM │ Planning │ Vision     │ ├──────────────────────────────────────┤ │          MAVROS2 / micro-ROS         │ ├──────────────────────────────────────┤ │          MAVLink / DDS               │ ├──────────────────────────────────────┤ │          PX4 / ArduPilot             │ └──────────────────────────────────────┘ ```  ## PX4 + ROS2 연결  ```bash # PX4 SITL with R
- [2] `raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md` — --- title: "UAV-assisted Visual SLAM Generating Reconstructed 3D Scene Graphs in GPS-denied Environments" authors:   - Ahmed Radwan   - Ali Tourani   - Hriday Bavle   - Holger Voos   - Jose Luis Sanchez-Lopez venue: "IEEE ICUAS 2024" year: 2024 arxiv: "2402.07537" doi: "10.1109/ICUAS60882.2024.10556948" url: "https://arxiv.org/abs/2402.07537" pdf: "https://arxiv.org/pdf/2402.07537" topics: [drone-ai, slam, 3d-reconstruction, gps-denied, computer-vision] abstract: |   This paper presents a UAV-assisted visual SLAM system that generates reconstructed    3D scene graphs in GPS-denied environments. The system enables autonomous navigation    and mapping without relying on GPS signals, making it suitable for indoor and denied    environments. The approach combines visual SLAM with 3D reconstruction to build    semantic scene graphs. ingested: 2026-07-27 ---  # UAV-assisted Visual SLAM Generat

**뉴스 검색 결과**
- [2] [핑크랩 PinkLAB] 핑크랩 PL2M 공개! ROS 2 기반 주행형 양팔로봇 플랫폼 — https://www.youtube.com/watch?v=-i5dSTGDHhI
- [1] [IPO 총정리] 8월 공모주 청약 시장 '후끈'... AI 드론부터 탄탄한 실적주까지 — https://news.google.com/rss/articles/CBMiZEFVX3lxTE14VW16NGNqbGFSbXo5R2Ntbm9aY0lsbm5vb2M2YzVOamo0REVFbXR3NGR0MmpWaFdsbGo5V3lGNlpJZDNMRzhmTFRBU3hYcURFY3I4SnNYQWpGcmhORFFySzRyMWQ?oc=5
- [1] 국산 방산 AI 상용화 ‘한뜻’...퀀텀에어로·전남TP, 드론 신뢰성 검증 돌입 — https://news.google.com/rss/articles/CBMiX0FVX3lxTE1YUDZSRjY3T01vNGNvVWpKQ0ozLThYTnRrTmVWVGZITDg1R0VZQmFzWnhPNDZlUWJTUlNLSWcxSmx2YzlnUzlFenRvT3JlX3pZcVFlVF9rdXlub29oTlRj?oc=5
- [1] [freeCodeCamp.org] Agentic AI – Complete Course for Beginners — https://www.youtube.com/watch?v=Zy7EXDONlTY

**그래프 인접 슬러그** (1-hop): `ai-agent`, `ai-knowledge-workflow`, `computer-vision-drone`, `cross-layered-medical-drone-coordination`, `decentralized-swarm-gps-denied`, `digital-twin-intent-drone-networks`

### 검색: GPS/통신이 제한된 환경에서 드론이 사용하는 대체 위치추정·항법 기법(SLAM, 시각-관성 항법 등)은 무엇인가?

**canonical 검색 결과**
- [5] `concepts/decentralized-swarm-gps-denied.md` — Decentralized UAV Swarms in GPS/Communication-Denied Environments (slug: `decentralized-swarm-gps-denied`, layer: concepts)
  발췌: GPS 및 통신 차단 환경에서 지상 표적 보호를 위한 분산형 UAV 군집 시스템. 온보드 센서만을 활용하여 표적을 추적하고 군집으로 협업하며, 칼만 필터로 상대 측정만으로 UAV 및 표적 상태를 추정한다.

## 핵심 개념

### 분산 군집 포위 기법
- **Target Tracking**: 온보드 센서 기반 미지 표적 상태 추정
- **Kalman Filters**: 상대 측정만으로 UAV 위치 및 표적 상태 추정
- **Encirclement Strategy**: 표적 운동에 적응하는 분산 포위 기법

### 환경 가정
- GPS 차단 (GPS-denied)
- UAV 간 통신 불가
- 온보드 센서만 의존

### 응용 시나리오
- 군사 표적 방어
- 적대적 UAV 탐지 및 요격
- 실제 로봇 검증 완료

## 관련 페이지

- [[swarm-coordination]] — 군집 드론 운용 모드 및 편대 비행
- [[datalink-communication]] — RF, LTE, WiFi 등 데이터링크 통신
- [[drone-ai-agents]] — 다중 에이전트 협력 및 합의 알고리즘

## 출처

- Silveria et al., "Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments", arXiv:2607.20710, 2026.
- [3] `concepts/rtk-gps-precise-landing.md` — RTK GPS & Precise Landing (slug: `rtk-gps-precise-landing`, layer: concepts)
  발췌: RTK(Real-Time Kinematic) GPS는 정밀 측위를 위한 차등 GPS 기술로 수 센티미터 수준의 정확도를 제공한다. 드론의 정밀 착륙과 비행 경로 관리에 필수적이다.

## GPS vs RTK

| 특성 | Standard GPS | RTK GPS |
|------|--------------|---------|
| **Accuracy** | 2-5m | 2-3cm + 1ppm |
| **Constellation** | GPS, GLONASS | GPS, GLONASS, Galileo, Beidou |
| **Correction** | 없음 | Base station 필요 |
| **Latency** | <1s | 1-2s |
| **Cost** | $20-100 | $300-1000+ |
| **Setup** | 간단 | Base station 필요 |

## RTK Principle

### 기본 개념

```
Base Station (Known position)
    │
    │ GNSS raw observations
    │
    ▼ Correction calculation
    │
    ▼ RTCM/Radiopacket
    │
    ▼ Rover (Drone)
         │
         ▼ Corrected position
```

### 오차 소스

| 오차 | Standard GPS | RTK 후 |
|------|-------------|---------|
| **Satellite clocks** | ~2m | 제거됨 |
| **Ionospheric delay** | ~5m | 제거됨 |
| **Tropospheric delay** | ~0.5m | 감소됨 |
| **Multipath** | ~0.5m | 남음 |
| **Receiv
- [3] `concepts/visual-positioning-odometry.md` — Visual Positioning & Odometry (slug: `visual-positioning-odometry`, layer: concepts)
  발췌: Visual Odometry(VO)와 Visual-Inertial Odometry(VIO)는 카메라와 IMU를 사용하여 드론의 위치와 자세를 추정하는 기술이다. GPS가 없거나 신뢰할 수 없은 환경에서 필수적이다.

## VIO 시스템 아키텍처

```
┌─────────────────────────────────────────┐
│         Camera + IMU Sensors          │
│      (Raw images + IMU readings)      │
└───────────────────┬───────────────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
┌────────┐   ┌──────────┐   ┌──────────┐
│ Feature│   │ Optical  │   │ Direct   │
│ Matcher│   │ Flow     │   │ Method   │
└────┬───┘   └────┬─────┘   └────┬─────┘
     │            │              │
     └────────────┼──────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  Fusion Core   │
         │ (MSCKF/OKVIS)│
         └───────┬────────┘
                 │
                 ▼
    ┌─────────────────────────
- [2] `concepts/computer-vision-drone.md` — Computer Vision for Drones (slug: `computer-vision-drone`, layer: concepts)
  발췌: 드론 컴퓨터 비전은 탑재된 카메라와 AI 알고리즘을 활용하여 환경을 인식, 분석, 이해하는 기술이다. 객체 감지, SLAM, 추적 등 다양한 응용이 있다.

## 핵심 기술 영역

### 1. Object Detection (객체 감지)

| 모델 | 특성 | FPS (Jetson) |
|------|------|-------------|
| **YOLOv5/v8/v10** | 범용, 빠름 | 30-60+ |
| **YOLO-NAS** | AutoNAC 최적화 | 40-80 |
| **RT-DETR** | Transformer 기반 | 20-40 |

**드론 특화:**
- 작은 객체 감지 최적화
- 동적 배경 대응
- 실시간 요구사항

### 2. SLAM (Simultaneous Localization And Mapping)

SLAM은 실시간으로 지도를 생성하고 동시에 위치를 추정하는 기술이다.

| 알고리즘 | 타입 | 특성 |
|---------|------|------|
| **ORB-SLAM3** | Visual | 가볍고, 정확 |
| **VINS-Fusion** | Visual-Inertial | IMU 융합 |
| **RTAB-Map** | LIDAR+Visual | 메모리 효율 |
| **LIO-SAM** | LIDAR-Inertial | 실외 강력 |

**입력 모달리티:**
- **Visual SLAM**: 카메라만
- **VIO (Visual-Inertial)**: 카메라 + IMU
- **LIDAR SLAM**: LiDAR
- **Multi-modal**: 융합

### 3. Visual Odometry (VO)

| 방법 | 설명 |
|------|------|
| **Feature-based** | 특징점 매칭 (ORB, SIFT) |
| **Direct
- [2] `concepts/drone-ai-agents.md` — Drone AI Agents (slug: `drone-ai-agents`, layer: concepts)
  발췌: 드론 AI 에이전트는 자율적 의사결정, 환경 인식, 목표 달성을 수행하는 지능형 소프트웨어 시스템이다. 단일 에이전트에서 다중 에이전트 협업까지 다양한 형태가 있다.

## 에이전트 유형

| 유형 | 설명 | 예시 |
|------|------|------|
| **Reactive Agent** | 간단한 조건-행동 매핑 | 장애물 회피 |
| **Deliberative Agent** | 계획 및 추론 | 미션 계획 |
| **Hybrid Agent** | 반응 + 의도 결합 | 현실용 시스템 |
| **Multi-Agent System** | 다중 에이전트 협력 | 스웜 드론 |

## 아키텍처 패턴

### 1. Perception-Action Loop

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│ Sensors │───▶│  Brain  │───▶│ Actuators│
└─────────┘    └─────────┘    └─────────┘
       ▲           │                │
       │           ▼                │
       └────┌──────────────┐◄──────┘
            │   Memory/KB    │
            └────────────────┘
```

### 2. BDI (Belief-Desire-Intention)

| 구성요소 | 설명 |
|----------|------|
| **Beliefs** | 환경에 대한 지식 |
| **Desires** | 목표/원하는 상태 |
| **Intentions** | 실행 중인 계획 |

### 3. Reinforcement Learning Agent

```
State ──▶ Polic

**raw 검색 결과**
- [4] `raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md` — --- title: "UAV-assisted Visual SLAM Generating Reconstructed 3D Scene Graphs in GPS-denied Environments" authors:   - Ahmed Radwan   - Ali Tourani   - Hriday Bavle   - Holger Voos   - Jose Luis Sanchez-Lopez venue: "IEEE ICUAS 2024" year: 2024 arxiv: "2402.07537" doi: "10.1109/ICUAS60882.2024.10556948" url: "https://arxiv.org/abs/2402.07537" pdf: "https://arxiv.org/pdf/2402.07537" topics: [drone-ai, slam, 3d-reconstruction, gps-denied, computer-vision] abstract: |   This paper presents a UAV-assisted visual SLAM system that generates reconstructed    3D scene graphs in GPS-denied environments. The system enables autonomous navigation    and mapping without relying on GPS signals, making it suitable for indoor and denied    environments. The approach combines visual SLAM with 3D reconstruction to build    semantic scene graphs. ingested: 2026-07-27 ---  # UAV-assisted Visual SLAM Generat
- [4] `raw/papers/drone-ai/shapira2025-icdnet.md` — --- title: "ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM" authors:   - Tali Orlev Shapira   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2512.00037" url: "https://arxiv.org/abs/2512.00037" pdf: "https://arxiv.org/pdf/2512.00037" topics: [drone-ai, slam, visual-inertial, deep-learning, computer-vision] abstract: |   This paper introduces ICD-Net, a deep learning-based approach for visual-inertial    SLAM in drones. The method uses inertial covariance displacement networks to improve    state estimation accuracy in challenging environments. The network learns to predict    covariance matrices for inertial measurements, enabling better fusion with visual    observations. ingested: 2026-07-27 ---  # ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM  ## Metadata  | 항목 | 내용 | |------|------| | **저자** | Tali Orlev Sh
- [3] `raw/papers/drone-hw/danial2025-microdrone-slam.md` — --- title: "Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors" authors:   - Jeryes Danial   - Yosi Ben Asher   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2511.14335" url: "https://arxiv.org/abs/2511.14335" pdf: "https://arxiv.org/pdf/2511.14335" topics: [drone-ai, drone-hw, micro-drone, slam, monocular, imu] abstract: |   This paper presents a SLAM system for micro drones using only a monocular camera and    inertial sensors. The system achieves simultaneous localization and 3D semi-dense mapping    suitable for resource-constrained micro aerial vehicles. The approach demonstrates that    accurate SLAM is possible on micro drones without stereo cameras or depth sensors. ingested: 2026-07-27 ---  # Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors  ##
- [2] `raw/articles/px4-system-architecture.md` — --- source_url: "https://docs.px4.io/main/en/concept/px4_systems_architecture.html" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "PX4 Dev Team" sha256: "7a8f3c2d1e5b9a6f4c8d2e1b5a9f6c3d7e8b2a4f5c9d1e6b3a8f4c7d2e5b9a6f" tags: [drone-sw, drone] ---  # PX4 System Architecture  ## Overview  PX4 provides a comprehensive autopilot system for unmanned aerial vehicles with two primary system configurations: flight controller-only and flight controller combined with companion computer.  ## Flight Controller System  A basic PX4 system centers on a flight controller running the PX4 flight stack.  Hardware components: - **Flight Controller**: Contains internal sensors (IMUs, compass, barometer) - **Motor Control**: ESCs connected via PWM, DroneCAN, or other interfaces - **Sensors**: GPS, compass, distance sensors, optical flow, ADSB transponders - **Payloads**: Cameras and other e
- [1] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18

**뉴스 검색 결과**
- [1] 옛날통닭·닭강정·커피·땅콩빵 드론이 배송…무료 서비스 — https://news.google.com/rss/articles/CBMiYEFVX3lxTE43MXo1TlE3cmg3QTBSUFdNdlFrMWpYVzVGRklLYWtJVER3UkpDUUQ4RUFybmFZX20tZS1XSjh3VTEyUC1HeHBESkQ0VlJudDlqdlVuVnlqTDM5anNUNnZOX9IBeEFVX3lxTE5VYTdvYWJ0Vl9CcWJocjZCS2hkTHFqMHhEQkloVXdkZVB5NmdIRmhGNjkxUkJCY2JQSnpxMDBxaml0enI0YlB2ZFpJaENGR0swOHdWYVZjQS1jTE9lMldaZG5yaVAtbVBjM3JLX1RYbWMtSEctSVJfMw?oc=5
- [1] 드론이 흔든 전장, 방산 돈줄도 바꿨다…M&A·투자 경쟁 가열 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE9vZ1NkbkxhdEVyZC1qZHd6S2lwdUd6cXpIUE1tTHNoeUplUUJIcG00RlhZMU0wS3hYRGJ4UlRVVWVPcmZNYkxaMC1ta3VjeGc?oc=5
- [1] 영주 서천에서 주문하면 드론이 배달합니다 — https://news.google.com/rss/articles/CBMiY0FVX3lxTFBFbWdHT2otYnhjSVZ0cFdRQUkxNzNFN0RuOGF3WWdZNGNtZndmalpnQVZ2Z3YtTWJQMEI0YTRZcTVCb2R2RFJfUjduLXVvUTZ1cEIwWHBwT0VKbVhQcml2cVpkcw?oc=5
- [1] 옛날통닭·닭강정·커피·땅콩빵 드론이 배송…무료 서비스 — https://news.google.com/rss/articles/CBMieEFVX3lxTE5VYTdvYWJ0Vl9CcWJocjZCS2hkTHFqMHhEQkloVXdkZVB5NmdIRmhGNjkxUkJCY2JQSnpxMDBxaml0enI0YlB2ZFpJaENGR0swOHdWYVZjQS1jTE9lMldaZG5yaVAtbVBjM3JLX1RYbWMtSEctSVJfM9IBeEFVX3lxTE5VYTdvYWJ0Vl9CcWJocjZCS2hkTHFqMHhEQkloVXdkZVB5NmdIRmhGNjkxUkJCY2JQSnpxMDBxaml0enI0YlB2ZFpJaENGR0swOHdWYVZjQS1jTE9lMldaZG5yaVAtbVBjM3JLX1RYbWMtSEctSVJfMw?oc=5

**그래프 인접 슬러그** (1-hop): `chained-attacks-drone-fl`, `cross-layered-medical-drone-coordination`, `datalink-communication`, `digital-twin-intent-drone-networks`, `drone-payload-systems`, `drone-simulation`

### 검색: 군집 드론 간 통신이 완전 단절되었을 때(무통신) 임무 지속을 가능하게 하는 사전 계획 기반 자율 실행 방식은 어떻게 설계되는가?

**canonical 검색 결과**
- [9] `concepts/swarm-modes.md` — Swarm Modes — 군집 드론 운용 모드 (slug: `swarm-modes`, layer: concepts)
  발췌: 군집 드론 시스템의 운용 모드 정의. Leader-Follower 구조 기반의 4가지 주요 모드.

## 시스템 구조

```
┌─────────────────────────────────────────────────┐
│                  Ground Station                  │
│  ┌───────────┐  ┌───────────┐  ┌────────────┐  │
│  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │
│  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │
└────────┼───────────────┼──────────────┼─────────┘
         │               │              │
         └───────────────┼──────────────┘
                         │ MAVLink
         ┌───────────────┼──────────────┐
         ▼               ▼              ▼
   ┌──────────┐    ┌──────────┐   ┌──────────┐
   │ Leader   │    │ Follower │   │ Follower │
   │ (CUAV)   │◄──►│ (Holybro)│◄──►│ (Holybro)│
   └──────────┘    └──────────┘   └──────────┘
     V7+ #1009       6C #1041       6C #xxxx
```

## 통신 구조

| 링크 | 프로토콜 | 용도 |
|------|----------|------|
| GCS ↔ Leader | MAVL
- [6] `concepts/drone-news-ops.md` — 드론 운용 및 미션 동향 2026-07 (slug: `drone-news-ops`, layer: concepts)
  발췌: 2026년 7월 드론 운용 및 미션 관련 최신 동향. 재난 대응, 공공 안전, 화물 운송, 카운터-UAS 등 다양한 응용 분야의 소식을 다룬다.

## 재난 대응 및 평가

### FlyGuys & TerraFort AI 재난 평가

- **성과**: 슈퍼 태풍 Sinlaku 이후 북마리아나 제도 대규모 재난 평가 완료
- **접근법**: 드론 기반 항공 데이터 수집 + AI 기반 피해 평가
- **효과**: 기존 수개월 소요 평가를 10일로 단축

### JOUAV 실시간 매핑

- **사례**: 2026년 7월 17일 중국 충칭 펑수이 현 산사태
- **기술**: 실시간 드론 매핑으로 응급 관리자가 위험 평가 및 구조 계획 수립
- **효과**: 구조대 투입 전 3D 지도 제공으로 안전한 작전 계획 가능

## 공공 안전

### Public Safety Drone Review

- **일정**: 2026년 8월 4일
- **주최**: DRONELIFE 및 DRONERESPONDERS
- **내용**: 공공 안전 드론 운용 관련 월간 라이브스트림

### 인종 공동체 드론 프로그램

- **배경**: 실종자 수색 성공으로 드론 프로그램 수용
- **효과**: 응급 상황 대응 시간을 1시간에서 수초로 단축

## 화물 및 운송

### PyroDelta Energy 중량 화물 드론

- **기술**: Capillary Casting 공정 특허
- **에너지원**: 폐열 활용
- **도전**: DARPA 드론 경쟁 참가

### Archer Halo 자율 VTOL

- **특징**: 하이브리드 전기 VTOL, 장거리 화물 미션용
- **운용**: 무인으로 헬리콥터처럼 이륙, 비행기처럼 장거리 비행

## Counter-UAS

### DroneShield RfAI-3

- **기술**
- [6] `concepts/recon-swarm-project.md` — Recon Swarm Project — 지능형 자율 군집정찰드론 (slug: `recon-swarm-project`, layer: concepts)
  발췌: 지능형 자율 군집정찰 시스템 개발 프로젝트. 학술연구 기반의 4단계 로드맵을 통해 단일 기체 자율비행에서 GPS-denied 실내 군집까지 단계적 확장.

## 프로젝트 개요

- **목표**: 학술연구 기반 자율 군집정찰 시스템
- **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041)
- **펌웨어**: ArduPilot (커스텀)

## 4단계 로드맵

| 단계 | 내용 | 상태 |
|:----:|------|:----:|
| 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 |
| 2 | 2기 편대비행 + 통신 검증 | 계획 |
| 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 |
| 4 | GPS-denied + 실내 군집 | 계획 |

## 센서 스택

| 센서 | 용도 | 인터페이스 |
|------|------|-----------|
| LiDAR | 장애물 감지/매핑 | UART/I2C |
| 카메라 (RGB) | 정찰/객체 인식 | CSI/USB |
| Radar | 전방위 감지 | SPI |
| Optical Flow | GPS-denied 위치추정 | I2C |
| RTK GPS | 정밀 위치 | UART |

## 안전 시스템

- Geofence (하드웨어+소프트웨어 이중)
- 배터리 페일세이프 (자동 RTL)
- 통신 두절 대응 (독립 귀환)
- 충돌 회피 (최소 이격거리 유지)

## SITL 테스트 환경

```bash
# ArduPilot SITL 멀티 기체
sim_vehicle.py -v ArduCopter --instance 0 -L HOME_LAT,HOME_LNG,ALT,HDG
sim_vehicle.py -v ArduCopter --instance 1 -L HOME_LAT,HOME_LNG,ALT,HDG
``
- [5] `concepts/chained-attacks-drone-fl.md` — Chained Attacks on Drone-Based Federated Learning (slug: `chained-attacks-drone-fl`, layer: concepts)
  발췌: 드론 기반 연합학습(Federated Learning, FL) 시스템에 대한 체인 공격 연구. 네트워크 계층의 DoS 공격과 자격 증명 기반 사칭을 결합한 공격 체인을 분석한다.

## 개요

Edge Intelligence(EI)는 드론 스웜과 같은 미션 크리티컬 무인 플랫폼에 협업적 모델 학습을 가능하게 하는 변혁적 모델이다. 그러나 FL 배포의 보안은 네트워크 가용성과 강력한 클라이언트 인증 메커니즘 모두에 의존한다.

## 공격 벡터

### 1. 네트워크 계층 DoS 공격
- **802.11 deauthentication 공격**: 합법적인 드론을 오프라인으로 강제 종료
- 무선 연결 중단을 통한 가용성 저해

### 2. 자격 증명 기반 사칭
- 연결 해제된 드론의 추출된 자격 증명을 사용한 사칭
- 단일 요소 인증이 연결 해제 후 사칭을 허용함

## 영향 분석

| 조건 | 영향 |
|------|------|
| IID 데이터 분포 | 상대적으로 안정적인 학습 |
| Non-IID 데이터 분포 | 상당한 학습 불안정성 |
| 단기 무선 중단 | 장기적인 학습 품질 저하로 확대 |

## 실험 검증

- **프레임워크**: Flower 프레임워크
- **테스트베드**: Raspberry Pi 및 Jetson 장비
- **데이터 분포**: IID 및 Non-IID 조건 모두 테스트

## 시사점

미션 크리티컬 드론 배포에서 가용성과 인증 취약점을 동시에 해결하는 방어 방향 필요:
- 다중 요소 인증(MFA) 도입
- 무선 연결 복원 메커니즘 강화
- 비정상 노드 탐지 및 격리

## 관련 페이지

- [[federated-lightweight-intrusion-detection]] — 지식 증류를 활용한 FL 기반 IDS
- [[swarm-coordination]] — 
- [5] `concepts/cross-layered-medical-drone-coordination.md` — Cross-Layered Multi-Drone Coordination for Medical Supply Delivery (slug: `cross-layered-medical-drone-coordination`, layer: concepts)
  발췌: 재난 대응 상황에서 의료 물품 배달을 위한 다중 드론 협업 시스템. CTDE(Centralized Training Decentralized Execution) 기반 Deep Q-Network 알고리즘(CEDA)을 활용하여 트리아지 우선순위 기반 라우팅, 다중 에이전트 협업, 에너지 효율적 내비게이션을 동시에 최적화한다.

## 핵심 개념

### CEDA 알고리즘
- **CTDE (Centralized Training Decentralized Execution)**: 중앙 집중식 학습, 분산 실행
- **Priority-Preserving Fair Scheduling**: 트리아지 가중치와 공정성 메커니즘을 결합한 보상 함수
- **PX4 SITL 검증**: X500 쿼드로터 2대로 MAVSDK 오프보드 위치 제어 모드 검증

### 성능 지표
- 배달 완료율: 85% 이상
- 장애물 충돌 감소: 90% 이상
- 평균 환자 처리: 에피소드당 6명
- 트리아지 효율성: 0.82

## 관련 페이지

- [[swarm-coordination]] — 군집 드론 운용 모드 및 편대 비행
- [[px4-flight-stack]] — PX4 오픈소스 비행 제어 소프트웨어
- [[mavsdk]] — MAVLink 기반 고수준 드론 제어 SDK
- [[drone-ai-agents]] — 자율 의사결정 및 다중 에이전트 협력

## 출처

- Calyam et al., "A Cross-Layered Multi-Drone Coordination for Medical Supply Delivery during Disaster Response Management", arXiv:2605.09342, 2026.

**raw 검색 결과**
- [5] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [5] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,
- [4] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [3] `raw/articles/mastervault-swarm-architecture.md` — --- source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4" tags: [swarm, datalink] ---  # 스웜 드론 아키텍처  ## 시스템 구조  ``` ┌─────────────────────────────────────────────────┐ │                  Ground Station                  │ │  ┌───────────┐  ┌───────────┐  ┌────────────┐  │ │  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │ │  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │ └────────┼───────────────┼──────────────┼─────────┘          │               │              │          └───────────────┼──────────────┘                          │ MAVLink          ┌───────────────┼──────────────┐          ▼               ▼              ▼    ┌──────────┐    ┌──────────┐   ┌──────────┐    │ Leader   │    │ Follower │   │ Followe
- [3] `raw/articles/ros2-devnotes.md` — --- source_url: "file://MasterVault/Drone/ROS/ROS2-DevNotes.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3f7a9c4e8d2b5a7f3c6e9d4b8a2f5c7e1d9a6b3f8c4e7d2a5b9f6c3d8e4a7b2f5" tags: [drone-sw] ---  # ROS2 개발 노트  ## 지원 버전  | 배포판 | EOL | 비고 | |--------|-----|------| | Humble | 2027-05 | LTS, 현재 메인 | | Jazzy | 2029-05 | LTS, 차기 이전 | | Kilted | 2025-12 | Rolling 기반 |  ## 드론 연동 스택  ``` ┌──────────────────────────────────────┐ │          ROS2 Application            │ │  Nav2 │ SLAM │ Planning │ Vision     │ ├──────────────────────────────────────┤ │          MAVROS2 / micro-ROS         │ ├──────────────────────────────────────┤ │          MAVLink / DDS               │ ├──────────────────────────────────────┤ │          PX4 / ArduPilot             │ └──────────────────────────────────────┘ ```  ## PX4 + ROS2 연결  ```bash # PX4 SITL with R

**뉴스 검색 결과**
- [1] [기자문답] 미국 드론 시장, 한국에 손 내미는 이유 — https://news.google.com/rss/articles/CBMibEFVX3lxTE9JeUJSRDgxWDhnRlZ4dlprbHlQTllDOHpVZ1lsUVZTbkl1SGlVWVhFRE5uRGpibnZPOXNaR0xKWVlPeU41X2pJUUNuUTV2U25ZUmtmUHd0RjdVd1k1bmI4VEZOVnQzOVZxRFNya9IBb0FVX3lxTFBDVTNkVnpKVEtoU2dFa1ZVWk84bzYwX2hsUDQ4ZEJSZXFxUEo0YlE1QW5kVWgyWGw2ajJXcFN2OV83TDhad2tKOUYxRWdVRGZXSFAzUTE2ZF9IT25Pb01mTmlwV29nSk5NYWp1WGpCWQ?oc=5
- [1] 이집트까지 드론 피격… 중동대전으로 번지나 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5pVGNVeWo5d0oxYWRKUWhFTHRUbWtyOEI4MHFkdlh1NmFOdmt3V3ltN0VoOEU4OU9xNzJsa2U0TzJoSzZyMkRTd25SYVZ3ZkU?oc=5
- [1] "이집트서 미국 소유 LNG 설비 드론 공격에 화재" — https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1qYXlfWmpTOEwtdjJFWVV5cHFWUGNvUWhBSTJCUWVfRlUtRmFBb0thSTNUZDBOTlFuUV9wb1VDVmhpQVU5MGowTGYtSWRZUDlaWkZVMWR2Vkg5azJPOXpGNjZLMmV1OWc?oc=5
- [1] 경기 북부서 '미확인 비행체' 해프닝…알고보니 한미 훈련 드론 — https://news.google.com/rss/articles/CBMia0FVX3lxTFB5Qmtac2NsM3M1a3l2SzlHYy10LUJLUXZsUndLdTlObW1IMlFZSmhLT1lvbTRfY3lBQTZUZFFPN3FLdTRxMXN0NmswMEJUUVA5UWNzeTUwUklVOW81R2Jlbi1ibEpwcGhQeHdz?oc=5

**그래프 인접 슬러그** (1-hop): `computer-vision-drone`, `datalink-communication`, `distributed-aerial-surveillance-swarm`, `drone-ai-agents`, `drone-payload-systems`, `drone-safety-failsafe`

### 검색: 군집 드론의 온디바이스 AI 자율 임무 수행이 실제로 검증된 실증/실험 사례(군사·상업)는 어떤 것이 있는가?

**canonical 검색 결과**
- [7] `concepts/ai-personal-knowledge-management.md` — AI 개인 지식관리 (slug: `ai-personal-knowledge-management`, layer: concepts)
  발췌: AI 개인 지식관리는 자료를 많이 저장하는 일이 아니라, 원본과 해석의 경계를 보존하면서 검증된 지식을 반복해서 재사용할 수 있게 만드는 운영 체계다.

핵심 단위는 특정 앱이 아니라 추적 가능한 원본, 상호 연결된 Markdown, 명시적인 품질 규칙이다. ^[raw/youtube/📺 How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md]

## 지식의 세 층

| 층 | 목적 | 보존 원칙 |
| --- | --- | --- |
| 원본 | 논문·웹·영상과 메타데이터 보존 | 수정하지 않고 출처와 수집 시점을 남긴다. |
| 컴파일된 지식 | 개념·비교·질의를 재사용 가능하게 정리 | 출처, 링크, 갱신일과 신뢰도를 유지한다. |
| 집중 탐색 | 제한된 소스 묶음에 질문하고 가설 생성 | 생성 답변을 확정 지식과 구분한다. |

원본 도서관, 컴파일된 위키, 소스 기반 질의 공간을 분리하면 대용량 원본을 Markdown 저장소에 모두 복제하지 않으면서도 근거로 돌아갈 수 있다.

한 도구의 대화 기록이나 독점 형식이 사라져도 핵심 지식과 출처 관계가 남는다는 점도 중요하다. ^[raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md]

## 운영 순환

1. 원본과 메타데이터를 먼저 보존한다.
2. 반복해서 쓸 가치가 있는 내용만 개념·비교·질의 문서로 컴파일한다.
3. 새 문서를 기존 지식과 연결하고 중복·모순·출처 누락을 검사한다.
4. 지식그래프로 군집, 브리지, 고립 문서와 약한 연결을 탐색한다.
5. 그래프가 제안한 관계를 원본 또는 제한된 소스 묶음으로 검증한다.

- [5] `concepts/recon-swarm-project.md` — Recon Swarm Project — 지능형 자율 군집정찰드론 (slug: `recon-swarm-project`, layer: concepts)
  발췌: 지능형 자율 군집정찰 시스템 개발 프로젝트. 학술연구 기반의 4단계 로드맵을 통해 단일 기체 자율비행에서 GPS-denied 실내 군집까지 단계적 확장.

## 프로젝트 개요

- **목표**: 학술연구 기반 자율 군집정찰 시스템
- **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041)
- **펌웨어**: ArduPilot (커스텀)

## 4단계 로드맵

| 단계 | 내용 | 상태 |
|:----:|------|:----:|
| 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 |
| 2 | 2기 편대비행 + 통신 검증 | 계획 |
| 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 |
| 4 | GPS-denied + 실내 군집 | 계획 |

## 센서 스택

| 센서 | 용도 | 인터페이스 |
|------|------|-----------|
| LiDAR | 장애물 감지/매핑 | UART/I2C |
| 카메라 (RGB) | 정찰/객체 인식 | CSI/USB |
| Radar | 전방위 감지 | SPI |
| Optical Flow | GPS-denied 위치추정 | I2C |
| RTK GPS | 정밀 위치 | UART |

## 안전 시스템

- Geofence (하드웨어+소프트웨어 이중)
- 배터리 페일세이프 (자동 RTL)
- 통신 두절 대응 (독립 귀환)
- 충돌 회피 (최소 이격거리 유지)

## SITL 테스트 환경

```bash
# ArduPilot SITL 멀티 기체
sim_vehicle.py -v ArduCopter --instance 0 -L HOME_LAT,HOME_LNG,ALT,HDG
sim_vehicle.py -v ArduCopter --instance 1 -L HOME_LAT,HOME_LNG,ALT,HDG
``
- [5] `concepts/swarm-modes.md` — Swarm Modes — 군집 드론 운용 모드 (slug: `swarm-modes`, layer: concepts)
  발췌: 군집 드론 시스템의 운용 모드 정의. Leader-Follower 구조 기반의 4가지 주요 모드.

## 시스템 구조

```
┌─────────────────────────────────────────────────┐
│                  Ground Station                  │
│  ┌───────────┐  ┌───────────┐  ┌────────────┐  │
│  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │
│  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │
└────────┼───────────────┼──────────────┼─────────┘
         │               │              │
         └───────────────┼──────────────┘
                         │ MAVLink
         ┌───────────────┼──────────────┐
         ▼               ▼              ▼
   ┌──────────┐    ┌──────────┐   ┌──────────┐
   │ Leader   │    │ Follower │   │ Follower │
   │ (CUAV)   │◄──►│ (Holybro)│◄──►│ (Holybro)│
   └──────────┘    └──────────┘   └──────────┘
     V7+ #1009       6C #1041       6C #xxxx
```

## 통신 구조

| 링크 | 프로토콜 | 용도 |
|------|----------|------|
| GCS ↔ Leader | MAVL
- [5] `comparisons/knowledge-tool-roles.md` — AI 지식관리 도구 역할 비교 (slug: `knowledge-tool-roles`, layer: comparisons)
  발췌: 이 비교는 어느 도구가 “최고”인지보다 [[ai-knowledge-workflow]]에서 각 도구가 맡는 책임과 교체 가능한 경계를 보여준다.

| 도구 | 주된 역할 | 지속성 | 강점 | 주의점 |
| --- | --- | --- | --- | --- |
| Zotero·Zotero MCP | 원본·서지정보 관리와 자동 수집 | 높음 | 출처와 첨부 파일 보존 | 개념 합성은 별도 계층이 필요하다. |
| NotebookLM·notebooklm-py | 선택한 소스 묶음 탐색 | 중간 | 범위가 정해진 질의·요약 | 결과를 장기 지식으로 다시 편입해야 한다. |
| LLM Wiki | 검토된 지식 컴파일 | 높음 | 연결·모순·출처 누적 | 지속적인 유지보수와 lint가 필요하다. |
| Obsidian | 사람이 읽고 편집하는 인터페이스 | 높음 | 로컬 Markdown과 링크 탐색 | 대형 원본·서지는 전문 도구가 유리하다. |
| Understand Anything | 지식 관계 분석 | 재생성 가능 | 군집·경로·공백 후보 탐색 | 그래프 해석을 원문으로 검증해야 한다. |

Zotero 계층은 원본을 보존하고, NotebookLM 계층은 제한된 소스를 질의하며, LLM Wiki 계층은 검증된 장기 지식을 유지한다.

Understand Anything은 이 지식의 구조적 품질을 관찰한다. 이들은 대체재보다 계층별 보완재에 가깝다. ^[raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md]

## 선택 기준

- 원본과 서지정보를 잃지 않는가?
- 결과를 공개 형식으로 내보낼 수 있는가?
- 출처를 canonical 지식까지 추적할 수 있는가?
- [4] `concepts/ai-knowledge-workflow.md` — AI 지식 워크플로 (slug: `ai-knowledge-workflow`, layer: concepts)
  발췌: AI 지식 워크플로는 원본 수집부터 검토된 지식과 산출물 생성까지를 역할별 계층으로 나누는 운영 방식이다. 개인 지식관리 체계 전체에서 이 흐름이 갖는 의미는 [[ai-personal-knowledge-management]]에 정리한다.

## 기본 흐름

    수집 → 원본 보존 → 탐색·질의 → 위키 컴파일 → 검증 → 산출

- Zotero와 브라우저 클리퍼는 원본과 서지정보를 수집한다.
- NotebookLM은 선택한 소스 묶음을 탐색하고 질문한다.
- LLM Wiki와 Obsidian은 장기 지식과 관계를 Markdown으로 유지한다.
- Understand Anything은 지식 연결과 공백 후보를 그래프로 탐색한다.
- 검토된 지식은 글, 보고서, 프레젠테이션 같은 산출물로 변환한다.

한 도구가 모든 책임을 갖지 않도록 원본 보존, 지식 합성, 구조 분석, 결과 표현을 분리하면 도구를 교체해도 축적된 Markdown과 출처 관계를 유지할 수 있다. ^[raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md]

## 검증 관문

1. 원본과 요약이 분리되어 있는가?
2. 모든 핵심 주장에 추적 가능한 출처가 있는가?
3. 기존 문서와 중복되거나 충돌하지 않는가?
4. 내부 링크가 실제 문서를 가리키는가?
5. 산출물이 목적에 맞는 형식으로 직접 열리고 사용되는가?

## 위험과 제어

- 여러 에이전트가 같은 문서를 서로 다르게 해석할 수 있다.
- 프로젝트 README나 소개 영상의 홍보성 주장이 검증 없이 굳어질 수 있다.
- 자동화가 늘수록 잘못된 메타데이터가 빠르게 전파될 수 있다.

따라서 생성 속도는 출처, 링크, 스키마와 일관성 

**raw 검색 결과**
- [3] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [2] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [2] `raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md` — --- title: "UAV-assisted Visual SLAM Generating Reconstructed 3D Scene Graphs in GPS-denied Environments" authors:   - Ahmed Radwan   - Ali Tourani   - Hriday Bavle   - Holger Voos   - Jose Luis Sanchez-Lopez venue: "IEEE ICUAS 2024" year: 2024 arxiv: "2402.07537" doi: "10.1109/ICUAS60882.2024.10556948" url: "https://arxiv.org/abs/2402.07537" pdf: "https://arxiv.org/pdf/2402.07537" topics: [drone-ai, slam, 3d-reconstruction, gps-denied, computer-vision] abstract: |   This paper presents a UAV-assisted visual SLAM system that generates reconstructed    3D scene graphs in GPS-denied environments. The system enables autonomous navigation    and mapping without relying on GPS signals, making it suitable for indoor and denied    environments. The approach combines visual SLAM with 3D reconstruction to build    semantic scene graphs. ingested: 2026-07-27 ---  # UAV-assisted Visual SLAM Generat
- [2] `raw/papers/voice-control/lim2025-taking-flight-with-dialogue.md` — --- title: "Taking Flight with Dialogue: Enabling Natural Language Control for PX4-based Drone Agent" authors:   - Shoon Kit Lim   - Melissa Jia Ying Chong   - Jing Huey Khor   - Ting Yang Ling venue: arXiv year: 2025 doi: "10.48550/arXiv.2506.07509" url: "https://arxiv.org/abs/2506.07509" pdf: "https://arxiv.org/pdf/2506.07509" topics: [drone-sw, voice-control, ai-agent, ros2] abstract: |   Recent advances in agentic and physical artificial intelligence (AI) have largely focused    on ground-based platforms such as humanoid and wheeled robots, leaving aerial robots relatively    underexplored. Meanwhile, state-of-the-art unmanned aerial vehicle (UAV) multimodal vision-language    systems typically rely on closed-source models accessible only to well-resourced organizations.    To democratize natural language control of autonomous drones, we present an open-source agentic    framework th
- [1] `raw/articles/entity-pixhawk-hardware.md` — --- title: "Pixhawk Flight Controller — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/flight_controller/" author: "Pixhawk / PX4 Docs / Master" sha256: "" tags: [drone-hw, drone-sw] ---  # Pixhawk Flight Controller — Entity Reference  ## 개요  Pixhawk는 PX4 프로젝트와 함께 개발된 오픈 하드웨어 비행 제어기(FC) 플랫폼이다. Holybro, mRo, CubePilot 등 다수 제조사가 공식 Pixhawk 표준 호환 제품을 생산한다.  - **표준 문서**: https://github.com/pixhawk/Pixhawk-Standards - **주요 제조사**: Holybro (공식), CubePilot, mRo Technology - **버스 표준**: UAVCAN/DroneCAN, UART, SPI, I2C, CAN  ## 주요 모델 비교  | 모델 | MCU | RAM | 플래시 | 특징 | |---|---|---|---|---| | Pixhawk 1 | STM32F427 | 168MHz / 256KB | 2MB | 초기 레퍼런스, 단종 | | Pixhawk 4 | STM32F765 | 216MHz / 512KB | 2MB | Holybro 공식, 현 주력 | | Pixhawk 6C | STM32H743 | 480MHz / 1MB | 2MB | 최신 고성능 | | Pixhawk 6X | STM32H753 | 480MHz / 1MB | 2MB | 6C 상위 (이중화) | | Cub

**뉴스 검색 결과**
- [1] [IPO 총정리] 8월 공모주 청약 시장 '후끈'... AI 드론부터 탄탄한 실적주까지 — https://news.google.com/rss/articles/CBMiZEFVX3lxTE14VW16NGNqbGFSbXo5R2Ntbm9aY0lsbm5vb2M2YzVOamo0REVFbXR3NGR0MmpWaFdsbGo5V3lGNlpJZDNMRzhmTFRBU3hYcURFY3I4SnNYQWpGcmhORFFySzRyMWQ?oc=5
- [1] 국산 방산 AI 상용화 ‘한뜻’...퀀텀에어로·전남TP, 드론 신뢰성 검증 돌입 — https://news.google.com/rss/articles/CBMiX0FVX3lxTE1YUDZSRjY3T01vNGNvVWpKQ0ozLThYTnRrTmVWVGZITDg1R0VZQmFzWnhPNDZlUWJTUlNLSWcxSmx2YzlnUzlFenRvT3JlX3pZcVFlVF9rdXlub29oTlRj?oc=5
- [1] [freeCodeCamp.org] Agentic AI – Complete Course for Beginners — https://www.youtube.com/watch?v=Zy7EXDONlTY
- [1] [freeCodeCamp.org] Behind the popular AI tools lies a crucial bit of tech called a transformer. — https://www.youtube.com/watch?v=lFXt6mBEiTQ

**그래프 인접 슬러그** (1-hop): `computer-vision-drone`, `datalink-communication`, `distributed-aerial-surveillance-swarm`, `drone-ai-agents`, `drone-safety-failsafe`, `flight-controller-hardware`

### 검색: 통신 제한 환경에서 군집 드론 운용에 관한 각국의 규제 및 정책 동향은 어떠한가?

**canonical 검색 결과**
- [7] `concepts/swarm-modes.md` — Swarm Modes — 군집 드론 운용 모드 (slug: `swarm-modes`, layer: concepts)
  발췌: 군집 드론 시스템의 운용 모드 정의. Leader-Follower 구조 기반의 4가지 주요 모드.

## 시스템 구조

```
┌─────────────────────────────────────────────────┐
│                  Ground Station                  │
│  ┌───────────┐  ┌───────────┐  ┌────────────┐  │
│  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │
│  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │
└────────┼───────────────┼──────────────┼─────────┘
         │               │              │
         └───────────────┼──────────────┘
                         │ MAVLink
         ┌───────────────┼──────────────┐
         ▼               ▼              ▼
   ┌──────────┐    ┌──────────┐   ┌──────────┐
   │ Leader   │    │ Follower │   │ Follower │
   │ (CUAV)   │◄──►│ (Holybro)│◄──►│ (Holybro)│
   └──────────┘    └──────────┘   └──────────┘
     V7+ #1009       6C #1041       6C #xxxx
```

## 통신 구조

| 링크 | 프로토콜 | 용도 |
|------|----------|------|
| GCS ↔ Leader | MAVL
- [6] `concepts/drone-news-regulations.md` — 드론 규제 동향 2026-07 (slug: `drone-news-regulations`, layer: concepts)
  발췌: 2026년 7월 글로벌 드론 규제 관련 주요 소식들. 영국 CAA(Civil Aviation Authority)의 Electronic Conspicuity 의무화 논의와 SESAR의 미래 항공 교통 관제 플랫폼 개발이 주요하다.

## 주요 규제 동향

### 영국 Electronic Conspicuity 의무화

- **상태**: CAA가 Electronic Conspicuity(전자적 가시성) 의무화에 대한 협의 진행 중
- **대상**: General Aviation 커뮤니티를 위한 웨비나 개최
- **목적**: 저고도 공역에서의 충돌 방지 및 상황 인식 향상

### UK SORA General Operations Manual (GOM)

- **권고**: 모든 UK SORA UAS 운용자가 운용 매뉴얼 보유 권고
- **목적**: 규제 준수 및 안전한 운용 절차 확립

### SESAR 미래 항공 교통 관제 플랫폼

- **프로젝트**: HAVEN 프로젝트
- **기술**: 자동화, AI, 클라우드 기술, 서비스 지향 아키텍처
- **목표**: 미래 항공 교통 관제 플랫폼 구축

### BVLOS Detect-and-Avoid

- **High Lander & Thirdeye**: 다중 항공기 Detect-and-Avoid 기술 현장 테스트
- **목표**: 대규모 BVLOS(Beyond Visual Line of Sight) 운용을 위한 경로 확보

## 관련 개념

- [[drone-regulations]] — 드론 규제 개요
- [[drone-safety-failsafe]] — 안전 및 failsafe 시스템
- [4] `concepts/decentralized-swarm-gps-denied.md` — Decentralized UAV Swarms in GPS/Communication-Denied Environments (slug: `decentralized-swarm-gps-denied`, layer: concepts)
  발췌: GPS 및 통신 차단 환경에서 지상 표적 보호를 위한 분산형 UAV 군집 시스템. 온보드 센서만을 활용하여 표적을 추적하고 군집으로 협업하며, 칼만 필터로 상대 측정만으로 UAV 및 표적 상태를 추정한다.

## 핵심 개념

### 분산 군집 포위 기법
- **Target Tracking**: 온보드 센서 기반 미지 표적 상태 추정
- **Kalman Filters**: 상대 측정만으로 UAV 위치 및 표적 상태 추정
- **Encirclement Strategy**: 표적 운동에 적응하는 분산 포위 기법

### 환경 가정
- GPS 차단 (GPS-denied)
- UAV 간 통신 불가
- 온보드 센서만 의존

### 응용 시나리오
- 군사 표적 방어
- 적대적 UAV 탐지 및 요격
- 실제 로봇 검증 완료

## 관련 페이지

- [[swarm-coordination]] — 군집 드론 운용 모드 및 편대 비행
- [[datalink-communication]] — RF, LTE, WiFi 등 데이터링크 통신
- [[drone-ai-agents]] — 다중 에이전트 협력 및 합의 알고리즘

## 출처

- Silveria et al., "Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments", arXiv:2607.20710, 2026.
- [4] `concepts/drone-news-hardware.md` — 드론 하드웨어 및 제조사 동향 2026-07 (slug: `drone-news-hardware`, layer: concepts)
  발췌: 2026년 7월 드론 하드웨어 및 제조사 관련 최신 동향. DJI 펌웨어 업데이트, Archer의 신규 VTOL, FCC 외국 드론 금지 관련 소식 등을 다룬다.

## 주요 하드웨어 동향

### DJI Mini 5 Pro 펌웨어 업데이트

- **날짜**: 2026년 7월 29일
- **내용**: 새로운 기능은 아니지만 비행 전 설치 권고

### DJI Flip

- **특징**: 일상 가방에 들어가는 휴대성, 손바닥 이륙, 자동 촬영
- **가격**: 할인 중

### Archer Halo 자율 VTOL

- **설계**: 장거리 화물 미션용 자율 하이브리드 전기 VTOL
- **특징**: 헬리콥터처럼 VTOL, 비행기처럼 장거리 비행, 무인 운용

### FCC 외국 드론 금지 예외

- **배경**: 2025년 12월 FCC의 Covered List 추가 발표
- **현황**: 7개월 후 예외 승인 사례 발생, 더 미묘한 상황
- **의미**: 외국 제조 드론의 완전한 차단은 아님

## 관련 개념

- [[flight-controller-hardware]] — FC 하드웨어 개요
- [[drone-payload-systems]] — 페이로드 통합
- [[drone-regulations]] — 규제 환경
- [4] `concepts/drone-regulations.md` — Drone Regulations (slug: `drone-regulations`, layer: concepts)
  발췌: 드론 규제는 안전한 공역 운용을 위해 국가/지역별로 시행되는 법적 프레임워크다. FAA(미국), EASA(유럽), 국토교통부(한국) 등 각국 기관이 관리한다.

## 규제 프레임워크

### 국제 기구

| 기구 | 지역 | 역할 |
|------|------|------|
| **ICAO** | 국제 | 국제민간항공기구, 표준 권고 |
| **FAA** | 미국 | Federal Aviation Administration |
| **EASA** | 유럽 | European Union Aviation Safety Agency |
| **CAA** | 영국 | Civil Aviation Authority |
| **국토교통부** | 한국 | 한국교통안전공단 |

## FAA Part 107 (미국)

상업용 드론 운용을 위한 규정.

### 요구사항

| 항목 | 요구사항 |
|------|----------|
| **Remote Pilot Certificate** | FAA 인증 시험 통과 |
| **Age** | 16세 이상 |
| **English** | 영어 능통 |
| **TSA Check** | 보안 심사 |

### 운용 제한

| 제한 | 규정 |
|------|------|
| **고도** | 400ft AGL 이하 |
| **속도** | 100mph 이하 |
| **시야** | VLOS (Visual Line of Sight) |
| **시간** | 일출~일몰 |
| **인원** | 조종자 1명 |

### Part 107 vs Part 91

| 규정 | 용도 |
|------|------|
| **Part 107** | 상업용 드론 (<55lbs) |
| **Part 91** | 일반 항공 |
| **Part 135** | 공중 택시/화물 |

## EASA (유럽

**raw 검색 결과**
- [3] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [3] `raw/papers/datalink/koubaa2019-mavlink-survey.md` — --- title: "Micro Air Vehicle Link (MAVLink) in a Nutshell: A Survey" authors:   - Anis Koubaa   - Azza Allouch   - Maram Alajlan   - Yasir Javed   - Abdelfettah Belghith   - Mohamed Khalgui venue: "IEEE Access" year: 2019 doi: "10.1109/ACCESS.2019.2924350" arxiv: "1906.10641" url: "https://arxiv.org/abs/1906.10641" pdf: "https://arxiv.org/pdf/1906.10641" topics: [datalink, mavlink, communication, survey, px4, ardupilot] abstract: |   This paper provides a comprehensive survey of the Micro Air Vehicle Link (MAVLink)    protocol, which is widely used for communication between unmanned aerial vehicles (UAVs)    and ground control stations. MAVLink is a lightweight messaging protocol that is designed    for resource-constrained systems. It supports both PX4 and ArduPilot autopilot systems    and has become the de facto standard for drone communication. The paper covers the    protocol archi
- [2] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생
- [2] `raw/articles/entity-pixhawk-hardware.md` — --- title: "Pixhawk Flight Controller — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/flight_controller/" author: "Pixhawk / PX4 Docs / Master" sha256: "" tags: [drone-hw, drone-sw] ---  # Pixhawk Flight Controller — Entity Reference  ## 개요  Pixhawk는 PX4 프로젝트와 함께 개발된 오픈 하드웨어 비행 제어기(FC) 플랫폼이다. Holybro, mRo, CubePilot 등 다수 제조사가 공식 Pixhawk 표준 호환 제품을 생산한다.  - **표준 문서**: https://github.com/pixhawk/Pixhawk-Standards - **주요 제조사**: Holybro (공식), CubePilot, mRo Technology - **버스 표준**: UAVCAN/DroneCAN, UART, SPI, I2C, CAN  ## 주요 모델 비교  | 모델 | MCU | RAM | 플래시 | 특징 | |---|---|---|---|---| | Pixhawk 1 | STM32F427 | 168MHz / 256KB | 2MB | 초기 레퍼런스, 단종 | | Pixhawk 4 | STM32F765 | 216MHz / 512KB | 2MB | Holybro 공식, 현 주력 | | Pixhawk 6C | STM32H743 | 480MHz / 1MB | 2MB | 최신 고성능 | | Pixhawk 6X | STM32H753 | 480MHz / 1MB | 2MB | 6C 상위 (이중화) | | Cub
- [2] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,

**뉴스 검색 결과**
- [1] [기자문답] 미국 드론 시장, 한국에 손 내미는 이유 — https://news.google.com/rss/articles/CBMibEFVX3lxTE9JeUJSRDgxWDhnRlZ4dlprbHlQTllDOHpVZ1lsUVZTbkl1SGlVWVhFRE5uRGpibnZPOXNaR0xKWVlPeU41X2pJUUNuUTV2U25ZUmtmUHd0RjdVd1k1bmI4VEZOVnQzOVZxRFNya9IBb0FVX3lxTFBDVTNkVnpKVEtoU2dFa1ZVWk84bzYwX2hsUDQ4ZEJSZXFxUEo0YlE1QW5kVWgyWGw2ajJXcFN2OV83TDhad2tKOUYxRWdVRGZXSFAzUTE2ZF9IT25Pb01mTmlwV29nSk5NYWp1WGpCWQ?oc=5
- [1] 이집트까지 드론 피격… 중동대전으로 번지나 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5pVGNVeWo5d0oxYWRKUWhFTHRUbWtyOEI4MHFkdlh1NmFOdmt3V3ltN0VoOEU4OU9xNzJsa2U0TzJoSzZyMkRTd25SYVZ3ZkU?oc=5
- [1] "이집트서 미국 소유 LNG 설비 드론 공격에 화재" — https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1qYXlfWmpTOEwtdjJFWVV5cHFWUGNvUWhBSTJCUWVfRlUtRmFBb0thSTNUZDBOTlFuUV9wb1VDVmhpQVU5MGowTGYtSWRZUDlaWkZVMWR2Vkg5azJPOXpGNjZLMmV1OWc?oc=5
- [1] 경기 북부서 '미확인 비행체' 해프닝…알고보니 한미 훈련 드론 — https://news.google.com/rss/articles/CBMia0FVX3lxTFB5Qmtac2NsM3M1a3l2SzlHYy10LUJLUXZsUndLdTlObW1IMlFZSmhLT1lvbTRfY3lBQTZUZFFPN3FLdTRxMXN0NmswMEJUUVA5UWNzeTUwUklVOW81R2Jlbi1ibEpwcGhQeHdz?oc=5

**그래프 인접 슬러그** (1-hop): `amazon-mk30-safety-incident`, `brinc-emergency-drone-funding`, `datalink-communication`, `dji-easa-sail-bvlos`, `doordash-air`, `drone-ai-agents`

### 검색: 군집 내 일부 드론의 고장 또는 통신 두절이 전체 임무 신뢰성에 미치는 영향과 이를 완화하는 결함 허용(fault tolerance) 기법은 무엇인가?

**canonical 검색 결과**
- [5] `queries/ua-knowledge-graph-workflow.md` — UA 위키 지식그래프 전체 워크플로 (slug: `ua-knowledge-graph-workflow`, layer: queries)
  발췌: ## 질의

위키 문서가 이미 생성되었다고 가정할 때 Understand Anything의 스킬은 어떤 역할을 하며, 지식그래프 생성부터 분석·활용·갱신까지 어떤 순서로 실행해야 하는가?

## 핵심 결론

Karpathy 패턴의 [[llm-wiki]]가 이미 존재한다면 시작점은 일반 코드 분석용 `understand`가 아니라 위키 전용 `understand-knowledge`다.

이 스킬로 지식그래프를 생성한 뒤 대시보드, 그래프 질의, 도메인 분석을 수행한다. 발견한 공백과 오류를 위키에 반영한 다음 그래프를 다시 생성한다. ^[raw/notebooklm/understand-anything-github.md]

    LLM Wiki 문서·index.md·wikilink
      → understand-knowledge
      → .ua/knowledge-graph.json
      → dashboard·chat·domain 분석
      → 위키 보강
      → understand-knowledge 재실행

## 코드 그래프와 지식그래프

`understand`는 파일·함수·클래스·서비스의 구조와 호출·의존 관계를 중심으로 코드 아키텍처를 만든다. `understand-knowledge`는 문서 제목, frontmatter, 위키링크를 추출하고 암시적 관계, 엔티티와 핵심 주장을 보강한다.

- 코드 그래프의 질문: 무엇이 무엇을 호출하고 의존하는가?
- 지식그래프의 질문: 어떤 개념과 주장이 연결되고 어떤 주제 군집을 이루는가?

## 권장 실행 순서

1. 위키의 `index.md`, canonical 문서와 wikilink가 유효한지 lint한다.
2. `understand-knowledge`로 `.ua/knowledge-graph.json`과 메타데이터를 
- [4] `concepts/drone-payload-systems.md` — Drone Payload Systems (slug: `drone-payload-systems`, layer: concepts)
  발췌: 페이로드는 드론의 임무 목표를 달성하는 장비로, 카메라, 센서, 화물 등을 포함한다. PX4는 다양한 페이로드 타입을 자동/수동으로 트리거할 수 있다.^[raw/articles/px4-basic-concepts.md]

## 페이로드 타입

| 타입 | 설명 | 예시 |
|------|------|------|
| **Camera** | 정지/동영상 촬영 | RGB, Thermal, Multispectral |
| **Gimbal** | 안정화된 카메라 마운트 | 2축, 3축 |
| **LiDAR** | 레이저 스캐닝 | 3D 매핑 |
| **Sensor** | 환경 측정 | 가스, 방사선 |
| **Gripper** | 물체 파지 | 화물 배달 |
| **Parachute** | 비상 낙하산 | 안전 시스템 |

## Camera Systems

### 카메라 트리거

| 방법 | 설명 |
|------|------|
| **RC Switch** | 리모컨 스위치로 촬영 |
| **Mission Command** | 미션 중 자동 촬영 |
| **MAVLink** | `MAV_CMD_DO_DIGICAM_CONTROL` |
| **Distance Trigger** | 이동 거리 기반 촬영 |

### Camera MAVLink 메시지

```
MAV_CMD_DO_DIGICAM_CONTROL
- Param 1: Session control
- Param 2: Zoom level
- Param 3: Focus lock
- Param 4: Shutter command
- Param 5: Command identity
```

## Gimbal Systems

카메라 안정화를 위한 자동화된 마운트.

| 축수 | 설명 |
|------|------|
| **2-axis** | Roll, Pi
- [4] `concepts/dronecan-deep.md` — DroneCAN Deep Dive — CAN 버스 통신 프로토콜 (slug: `dronecan-deep`, layer: concepts)
  발췌: DroneCAN은 FC와 주변기기를 연결하는 오픈소스 CAN 버스 통신 프로토콜. 2022년 UAVCAN v0에서 재브랜딩.

## 핵심 이점

- 대규모 하드웨어 생태계 (센서, 액추에이터, ESC)
- CAN 버스: 장거리 케이블에서도 강력한 통신
- 양방향 메시징 → 상태 모니터링 및 진단
- ESC와 주변기기용 단일 버스 아키텍처 (배선 간소화)
- PX4를 통한 중앙 집중식 펌웨어 업데이트 및 장치 구성
- 자동 장치 메타데이터 추적 (플릿 관리)

## 지원 하드웨어 카테고리

| 카테고리 | 예시 |
|---|---|
| ESC 및 모터 컨트롤러 | 다양한 DroneCAN 변형 |
| GNSS 수신기 | ARK, CUAV, Holybro, RaccoonLab, Zubax |
| 전력 모니터링 | CAN 인터페이스 배터리 모니터 |
| 센서 | 자력계, 대기속도, 거리측정기, optical flow, 기압계 |

## 설정

### 활성화

파라미터: `UAVCAN_ENABLE` (값 0-3, 동적 노드 할당을 위해 2 또는 3 권장)

### 메시지 구독

- `UAVCAN_SUB_*` — 인바운드 구독 (예: `UAVCAN_SUB_GPS`, `UAVCAN_SUB_FLOW`)
- `UAVCAN_PUB_*` — 아웃바운드 발행

구독 제어로 불필요한 버스 혼잡 방지.

### 펌웨어 업데이트

PX4는 APDescriptor(보드 ID + 버전 메타데이터)로 유효한 펌웨어 바이너리(`.bin`)를 식별. 부팅 전 SD 카드 디렉토리(`/fs/microsd/` 또는 `/fs/microsd/ufw_staging/`)에 펌웨어 파일 배치.

## 문제 해결

| 증상 | 해결책 |
|---|---|
| 장치 감지 안 됨 | `UAVCAN_ENABLE` 설정 확인 |
| DNA 서
- [4] `concepts/swarm-modes.md` — Swarm Modes — 군집 드론 운용 모드 (slug: `swarm-modes`, layer: concepts)
  발췌: 군집 드론 시스템의 운용 모드 정의. Leader-Follower 구조 기반의 4가지 주요 모드.

## 시스템 구조

```
┌─────────────────────────────────────────────────┐
│                  Ground Station                  │
│  ┌───────────┐  ┌───────────┐  ┌────────────┐  │
│  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │
│  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │
└────────┼───────────────┼──────────────┼─────────┘
         │               │              │
         └───────────────┼──────────────┘
                         │ MAVLink
         ┌───────────────┼──────────────┐
         ▼               ▼              ▼
   ┌──────────┐    ┌──────────┐   ┌──────────┐
   │ Leader   │    │ Follower │   │ Follower │
   │ (CUAV)   │◄──►│ (Holybro)│◄──►│ (Holybro)│
   └──────────┘    └──────────┘   └──────────┘
     V7+ #1009       6C #1041       6C #xxxx
```

## 통신 구조

| 링크 | 프로토콜 | 용도 |
|------|----------|------|
| GCS ↔ Leader | MAVL
- [3] `concepts/active-sensing-uav-communication.md` — Active Sensing-Assisted UAV Communications with Jittering (slug: `active-sensing-uav-communication`, layer: concepts)
  발췌: UAV 지터링으로 인한 빔 불일치 문제를 해결하기 위한 통합 감지 및 통신(ISAC) 기반 2단계 프레임워크. 통신 중심 및 감지 중심 두 가지 방식으로 AoA(Angle-of-Arrival) 획득 및 통신 성능을 균형 있게 최적화한다.

## 핵심 개념

### 2단계 프레임워크
- **Stage 1 (Sensing)**: 결정적 신호로 AoA 획득 (감지 중심) 또는 가우시안 신호로 AoA 추정 (통신 중심)
- **Stage 2 (Communication)**: 추정된 AoA를 활용한 순수 통신 서비스

### 성능 분석
- **Cramér-Rao Bound**: AoA 추정의 이론적 한계
- **Achievable Rates**: 폐형식 달성 가능 전송률
- **Time Allocation**: 전체 전송률을 최대화하는 최적 시간 할당

### 트레이드오프
- 감지와 통신 품질 간 근본적 트레이드오프
- 높은 전송 전력에서 지터 프리 상한 대비 성능 손실이 0에 수렴

## 관련 페이지

- [[datalink-communication]] — RF, LTE, WiFi 등 드론 데이터링크 기술
- [[mavlink-protocol]] — MAVLink 메시지 구조 및 마이크로서비스
- [[drone-hw]] — 안테나 및 RF 하드웨어

## 출처

- Chen et al., "Active Sensing-assisted UAV Communications with Jittering: Framework and Performance Analysis", arXiv:2606.13036, 2026.

**raw 검색 결과**
- [2] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [2] `raw/articles/entity-pixhawk-hardware.md` — --- title: "Pixhawk Flight Controller — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/flight_controller/" author: "Pixhawk / PX4 Docs / Master" sha256: "" tags: [drone-hw, drone-sw] ---  # Pixhawk Flight Controller — Entity Reference  ## 개요  Pixhawk는 PX4 프로젝트와 함께 개발된 오픈 하드웨어 비행 제어기(FC) 플랫폼이다. Holybro, mRo, CubePilot 등 다수 제조사가 공식 Pixhawk 표준 호환 제품을 생산한다.  - **표준 문서**: https://github.com/pixhawk/Pixhawk-Standards - **주요 제조사**: Holybro (공식), CubePilot, mRo Technology - **버스 표준**: UAVCAN/DroneCAN, UART, SPI, I2C, CAN  ## 주요 모델 비교  | 모델 | MCU | RAM | 플래시 | 특징 | |---|---|---|---|---| | Pixhawk 1 | STM32F427 | 168MHz / 256KB | 2MB | 초기 레퍼런스, 단종 | | Pixhawk 4 | STM32F765 | 216MHz / 512KB | 2MB | Holybro 공식, 현 주력 | | Pixhawk 6C | STM32H743 | 480MHz / 1MB | 2MB | 최신 고성능 | | Pixhawk 6X | STM32H753 | 480MHz / 1MB | 2MB | 6C 상위 (이중화) | | Cub
- [2] `raw/articles/mastervault-ardupilot-devnotes.md` — --- source_url: "file://MasterVault/Drone/ArduPilot/ArduPilot-DevNotes.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "5c8d3e7f9a2b6c4d8e1f5a9b3c7d2e6f1a5b9c3d7e2f6a1b5c9d3e7f2a6b1c5" tags: [drone-sw] ---  # ArduPilot 개발 노트  ## 핵심 아키텍처  ``` ┌─────────────────────────────────────────┐ │            Vehicle Code                 │ │  Copter │ Plane │ Rover │ Sub           │ ├─────────────────────────────────────────┤ │            Libraries                    │ │  AP_AHRS │ AP_GPS │ AP_Motors │ AC_PID  │ ├─────────────────────────────────────────┤ │            AP_HAL (하드웨어 추상화)      │ ├─────────────────────────────────────────┤ │  ChibiOS │ Linux │ SITL                 │ └─────────────────────────────────────────┘ ```  ## SITL 빠른 시작  ```bash # Copter sim_vehicle.py -v ArduCopter --map --console  # 특정 위치 sim_vehicle.py -v ArduCopter -L
- [2] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [1] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생

**뉴스 검색 결과**
- [1] MARS-Dragonfly: Agile and Robust Flight Control of Modular Aerial Robot Systems — http://arxiv.org/abs/2604.05499v1
- [1] Glitch in the Sky: Exploiting Voltage Fault Injection in UAV Flight Controllers — http://arxiv.org/abs/2604.16699v1
- [1] [광화문에서/하정민]드론의 신 vs 백전노장… 우크라이나軍 분열의 교훈 — https://news.google.com/rss/articles/CBMidkFVX3lxTE0yZFhUYW5EX25xNXN0MURXNlo0TnlndklHdVE1UTdfQVFJUEw4NEJ1cUdHT29iSTdiWUpVTEpUbURJNzJvV2V0THNLX00tb3pRMDlwX2FYSFhUdmR1cjlfYlp3R0E2OV9VeXJZNm9mQ3BLZ2g4UEHSAWZBVV95cUxNRW5PZVlPLWNGcjBrVGJFMWQ1bkJReDl2RlBHWWxXdEVVMGhra1JQNXZmb1BadmlpWUF3anljbFg1Nlc5LTg2Q1A3NzllOHhkdDZGR2doZHhiMEQ5MGxnVC04ZkhWRkE?oc=5

**그래프 인접 슬러그** (1-hop): `ai-knowledge-workflow`, `ai-personal-knowledge-management`, `computer-vision-drone`, `datalink-communication`, `digital-twin-intent-drone-networks`, `drone-ai-agents`

