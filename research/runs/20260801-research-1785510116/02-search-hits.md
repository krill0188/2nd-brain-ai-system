# 기계 검색 결과 (Retriever — LLM 미사용)

### 검색: 국내(대한민국) 전파법상 LTE 기반 드론 C2 링크에 적용되는 주파수 할당·인증 체계는 무엇인가

**canonical 검색 결과**
- [4] `concepts/datalink-communication.md` — Datalink Communication (slug: `datalink-communication`, layer: concepts)
  발췌: Datalink은 드론과 지상국(GCS) 또는 타 드론 간 데이터 통신을 담당하는 물리/링크 계층 시스템이다. C2(Command & Control) 링크와 텔레메트리를 포함한다.

## 통신 계층

```
┌─────────────────────────────────────────┐
│           Application Layer           │
│         MAVLink / Custom API          │
├─────────────────────────────────────────┤
│           Transport Layer             │
│         UDP / TCP / Serial            │
├─────────────────────────────────────────┤
│            Link Layer                 │
│   Radio / WiFi / LTE / Satellite      │
├─────────────────────────────────────────┤
│           Physical Layer              │
│   RF / Optical / Wired / Acoustic     │
└─────────────────────────────────────────┘
```

## 무선 통신 기술

### 1. RF Radio (전통적 텔레메트리)

| 특성 | 설명 |
|------|------|
| **주파수 대역** | 433MHz, 915MHz, 2.4GHz |
| **범위** | 1km ~ 60km (장비에 따라) |
| **속도** | 57.6kbps ~ 250kbps |
| **지연** | 10-100ms |
| **비용** | 저렴 |

**제품 예시:*
- [4] `concepts/drone-news-ops.md` — 드론 운용 및 미션 동향 2026-07 (slug: `drone-news-ops`, layer: concepts)
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
- [3] `concepts/decentralized-swarm-gps-denied.md` — Decentralized UAV Swarms in GPS/Communication-Denied Environments (slug: `decentralized-swarm-gps-denied`, layer: concepts)
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

**raw 검색 결과**
- [3] `raw/articles/mastervault-hardware-reference.md` — --- source_url: "file://MasterVault/Drone/Hardware/Hardware-Reference.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "1b5e9c2d6a8f3b6d9e2f5a8c1d4e7f9a2b5c8d1e4f7a9b2c5d8e1f4a7b9c2d5" tags: [drone-hw] ---  # 드론 하드웨어 레퍼런스  ## FC (Flight Controller)  ### Holybro  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || Pixhawk 6X | STM32H753 | 최상위, 산업용 | 대형 드론 | || Pixhawk 6X Pro | STM32H753 | 6X + 추가 센서 | 정밀 작업 | || Pixhawk 6C | STM32H743 | 가성비 | 교육/개발 | || Pixhawk 6C Mini | STM32H743 | 소형 | 레이서/소형기 | || Kakute H7 | STM32H743 | FPV 특화 | FPV 레이서 |  ### CUAV  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || V7+ | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 | || X7+ Pro | STM32H753 | 최상위 | 대형/산업 | || Nora+ | STM32H753 | 방열 우수 | 고온 환경 | || 7-Nano | STM32H743 | 초소형 | 소형 기체 |  ## GPS/RTK  || 제조사 | 모델 | 정밀도 | 비고 | ||--------|---
- [2] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생
- [2] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,
- [2] `raw/articles/mastervault-swarm-architecture.md` — --- source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4" tags: [swarm, datalink] ---  # 스웜 드론 아키텍처  ## 시스템 구조  ``` ┌─────────────────────────────────────────────────┐ │                  Ground Station                  │ │  ┌───────────┐  ┌───────────┐  ┌────────────┐  │ │  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │ │  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │ └────────┼───────────────┼──────────────┼─────────┘          │               │              │          └───────────────┼──────────────┘                          │ MAVLink          ┌───────────────┼──────────────┐          ▼               ▼              ▼    ┌──────────┐    ┌──────────┐   ┌──────────┐    │ Leader   │    │ Follower │   │ Followe
- [2] `raw/articles/ros2-devnotes.md` — --- source_url: "file://MasterVault/Drone/ROS/ROS2-DevNotes.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3f7a9c4e8d2b5a7f3c6e9d4b8a2f5c7e1d9a6b3f8c4e7d2a5b9f6c3d8e4a7b2f5" tags: [drone-sw] ---  # ROS2 개발 노트  ## 지원 버전  | 배포판 | EOL | 비고 | |--------|-----|------| | Humble | 2027-05 | LTS, 현재 메인 | | Jazzy | 2029-05 | LTS, 차기 이전 | | Kilted | 2025-12 | Rolling 기반 |  ## 드론 연동 스택  ``` ┌──────────────────────────────────────┐ │          ROS2 Application            │ │  Nav2 │ SLAM │ Planning │ Vision     │ ├──────────────────────────────────────┤ │          MAVROS2 / micro-ROS         │ ├──────────────────────────────────────┤ │          MAVLink / DDS               │ ├──────────────────────────────────────┤ │          PX4 / ArduPilot             │ └──────────────────────────────────────┘ ```  ## PX4 + ROS2 연결  ```bash # PX4 SITL with R

**뉴스 검색 결과**
- [1] [기자문답] 미국 드론 시장, 한국에 손 내미는 이유 — https://news.google.com/rss/articles/CBMibEFVX3lxTE9JeUJSRDgxWDhnRlZ4dlprbHlQTllDOHpVZ1lsUVZTbkl1SGlVWVhFRE5uRGpibnZPOXNaR0xKWVlPeU41X2pJUUNuUTV2U25ZUmtmUHd0RjdVd1k1bmI4VEZOVnQzOVZxRFNya9IBb0FVX3lxTFBDVTNkVnpKVEtoU2dFa1ZVWk84bzYwX2hsUDQ4ZEJSZXFxUEo0YlE1QW5kVWgyWGw2ajJXcFN2OV83TDhad2tKOUYxRWdVRGZXSFAzUTE2ZF9IT25Pb01mTmlwV29nSk5NYWp1WGpCWQ?oc=5
- [1] 이집트까지 드론 피격… 중동대전으로 번지나 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5pVGNVeWo5d0oxYWRKUWhFTHRUbWtyOEI4MHFkdlh1NmFOdmt3V3ltN0VoOEU4OU9xNzJsa2U0TzJoSzZyMkRTd25SYVZ3ZkU?oc=5
- [1] "이집트서 미국 소유 LNG 설비 드론 공격에 화재" — https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1qYXlfWmpTOEwtdjJFWVV5cHFWUGNvUWhBSTJCUWVfRlUtRmFBb0thSTNUZDBOTlFuUV9wb1VDVmhpQVU5MGowTGYtSWRZUDlaWkZVMWR2Vkg5azJPOXpGNjZLMmV1OWc?oc=5
- [1] 경기 북부서 '미확인 비행체' 해프닝…알고보니 한미 훈련 드론 — https://news.google.com/rss/articles/CBMia0FVX3lxTFB5Qmtac2NsM3M1a3l2SzlHYy10LUJLUXZsUndLdTlObW1IMlFZSmhLT1lvbTRfY3lBQTZUZFFPN3FLdTRxMXN0NmswMEJUUVA5UWNzeTUwUklVOW81R2Jlbi1ibEpwcGhQeHdz?oc=5

**그래프 인접 슬러그** (1-hop): `advanced-mavlink`, `digital-twin-intent-drone-networks`, `drone-ai-agents`, `drone-hw`, `drone-payload-systems`, `drone-regulations`

### 검색: 국내 ISM 대역(예: 900MHz, 2.4GHz, 5.8GHz)에서 RF 메시 네트워크형 C2 링크에 적용되는 출력·대역폭 제한은 무엇인가

**canonical 검색 결과**
- [3] `concepts/datalink-communication.md` — Datalink Communication (slug: `datalink-communication`, layer: concepts)
  발췌: Datalink은 드론과 지상국(GCS) 또는 타 드론 간 데이터 통신을 담당하는 물리/링크 계층 시스템이다. C2(Command & Control) 링크와 텔레메트리를 포함한다.

## 통신 계층

```
┌─────────────────────────────────────────┐
│           Application Layer           │
│         MAVLink / Custom API          │
├─────────────────────────────────────────┤
│           Transport Layer             │
│         UDP / TCP / Serial            │
├─────────────────────────────────────────┤
│            Link Layer                 │
│   Radio / WiFi / LTE / Satellite      │
├─────────────────────────────────────────┤
│           Physical Layer              │
│   RF / Optical / Wired / Acoustic     │
└─────────────────────────────────────────┘
```

## 무선 통신 기술

### 1. RF Radio (전통적 텔레메트리)

| 특성 | 설명 |
|------|------|
| **주파수 대역** | 433MHz, 915MHz, 2.4GHz |
| **범위** | 1km ~ 60km (장비에 따라) |
| **속도** | 57.6kbps ~ 250kbps |
| **지연** | 10-100ms |
| **비용** | 저렴 |

**제품 예시:*
- [1] `concepts/active-sensing-uav-communication.md` — Active Sensing-Assisted UAV Communications with Jittering (slug: `active-sensing-uav-communication`, layer: concepts)
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
- [1] `concepts/decentralized-swarm-gps-denied.md` — Decentralized UAV Swarms in GPS/Communication-Denied Environments (slug: `decentralized-swarm-gps-denied`, layer: concepts)
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
- [1] `concepts/digital-twin-intent-drone-networks.md` — Digital Twin for Intent-Based Drone Networks (slug: `digital-twin-intent-drone-networks`, layer: concepts)
  발췌: 의도 기반 드론 네트워크를 위한 역강화 학습 기반 디지털 트윈 시스템. DBS(Drone Base Station)의 의도를 명시적으로 알지 못하는 상황에서도 IRL(Inverse Reinforcement Learning)을 활용하여 궤적을 최적화하고 우선순위 사용자 서비스 비율을 극대화한다.

## 핵심 개념

### 디지털 트윈 시스템
- **Virtual Representation**: 물리적 무선 네트워크 환경의 가상 표현
- **Simulation & Prediction**: 관련 변화 시뮬레이션 및 예측
- **Trajectory Adjustment**: DBS 궤적 조정 제안

### 역강화 학습 (IRL)
- **Unknown Intent Handling**: 알려지지 않은 DBS 의도 하에서 궤적 최적화
- **Unpredictable Environment**: 예측 불가능한 환경 변화 대응
- **Performance**: 기존 RL 대비 약 85% 성능 손실 감소

### 네트워크 성능
- **Near-Real-Time Adjustment**: 근실시간 궤적 조정
- **2.5x Enhancement**: 표준 드론 네트워크 대비 최대 2.5배 성능 향상
- **On-Board vs DT**: DBS 온보드 제어 대비 DT 기반 솔루션의 우수성

## 관련 페이지

- [[datalink-communication]] — RF, LTE, WiFi 등 데이터링크 기술
- [[drone-ai-agents]] — 자율 의사결정 및 에이전트 아키텍처
- [[active-sensing-uav-communication]] — 감지 지원 UAV 통신

## 출처

- Wang et al., "Inverse-Reinforcement Learning Enabled Digital Twi
- [1] `concepts/drone-ai-agents.md` — Drone AI Agents (slug: `drone-ai-agents`, layer: concepts)
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
- [1] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생
- [1] `raw/articles/mastervault-hardware-reference.md` — --- source_url: "file://MasterVault/Drone/Hardware/Hardware-Reference.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "1b5e9c2d6a8f3b6d9e2f5a8c1d4e7f9a2b5c8d1e4f7a9b2c5d8e1f4a7b9c2d5" tags: [drone-hw] ---  # 드론 하드웨어 레퍼런스  ## FC (Flight Controller)  ### Holybro  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || Pixhawk 6X | STM32H753 | 최상위, 산업용 | 대형 드론 | || Pixhawk 6X Pro | STM32H753 | 6X + 추가 센서 | 정밀 작업 | || Pixhawk 6C | STM32H743 | 가성비 | 교육/개발 | || Pixhawk 6C Mini | STM32H743 | 소형 | 레이서/소형기 | || Kakute H7 | STM32H743 | FPV 특화 | FPV 레이서 |  ### CUAV  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || V7+ | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 | || X7+ Pro | STM32H753 | 최상위 | 대형/산업 | || Nora+ | STM32H753 | 방열 우수 | 고온 환경 | || 7-Nano | STM32H743 | 초소형 | 소형 기체 |  ## GPS/RTK  || 제조사 | 모델 | 정밀도 | 비고 | ||--------|---

**뉴스 검색 결과**
- [1] [Auterion] Marine Corps fiber-optic live fire strike at Camp Pendleton | Auterion — https://www.youtube.com/watch?v=p_4k97SzLWk
- [1] Design and Performance Evaluation of Secure RF and WiFi-Based Communication in Drone Swarms via Testbed Implementation — http://arxiv.org/abs/2606.27028v1

**그래프 인접 슬러그** (1-hop): `advanced-mavlink`, `chained-attacks-drone-fl`, `computer-vision-drone`, `cross-layered-medical-drone-coordination`, `drone-hw`, `drone-regulations`

### 검색: LTE 기반 C2 링크와 RF 메시 네트워크의 지연시간·통달거리·핸드오버 특성 비교는 어떠한가

**canonical 검색 결과**
- [5] `concepts/datalink-communication.md` — Datalink Communication (slug: `datalink-communication`, layer: concepts)
  발췌: Datalink은 드론과 지상국(GCS) 또는 타 드론 간 데이터 통신을 담당하는 물리/링크 계층 시스템이다. C2(Command & Control) 링크와 텔레메트리를 포함한다.

## 통신 계층

```
┌─────────────────────────────────────────┐
│           Application Layer           │
│         MAVLink / Custom API          │
├─────────────────────────────────────────┤
│           Transport Layer             │
│         UDP / TCP / Serial            │
├─────────────────────────────────────────┤
│            Link Layer                 │
│   Radio / WiFi / LTE / Satellite      │
├─────────────────────────────────────────┤
│           Physical Layer              │
│   RF / Optical / Wired / Acoustic     │
└─────────────────────────────────────────┘
```

## 무선 통신 기술

### 1. RF Radio (전통적 텔레메트리)

| 특성 | 설명 |
|------|------|
| **주파수 대역** | 433MHz, 915MHz, 2.4GHz |
| **범위** | 1km ~ 60km (장비에 따라) |
| **속도** | 57.6kbps ~ 250kbps |
| **지연** | 10-100ms |
| **비용** | 저렴 |

**제품 예시:*
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
- [3] `concepts/decentralized-swarm-gps-denied.md` — Decentralized UAV Swarms in GPS/Communication-Denied Environments (slug: `decentralized-swarm-gps-denied`, layer: concepts)
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
- [3] `concepts/digital-twin-intent-drone-networks.md` — Digital Twin for Intent-Based Drone Networks (slug: `digital-twin-intent-drone-networks`, layer: concepts)
  발췌: 의도 기반 드론 네트워크를 위한 역강화 학습 기반 디지털 트윈 시스템. DBS(Drone Base Station)의 의도를 명시적으로 알지 못하는 상황에서도 IRL(Inverse Reinforcement Learning)을 활용하여 궤적을 최적화하고 우선순위 사용자 서비스 비율을 극대화한다.

## 핵심 개념

### 디지털 트윈 시스템
- **Virtual Representation**: 물리적 무선 네트워크 환경의 가상 표현
- **Simulation & Prediction**: 관련 변화 시뮬레이션 및 예측
- **Trajectory Adjustment**: DBS 궤적 조정 제안

### 역강화 학습 (IRL)
- **Unknown Intent Handling**: 알려지지 않은 DBS 의도 하에서 궤적 최적화
- **Unpredictable Environment**: 예측 불가능한 환경 변화 대응
- **Performance**: 기존 RL 대비 약 85% 성능 손실 감소

### 네트워크 성능
- **Near-Real-Time Adjustment**: 근실시간 궤적 조정
- **2.5x Enhancement**: 표준 드론 네트워크 대비 최대 2.5배 성능 향상
- **On-Board vs DT**: DBS 온보드 제어 대비 DT 기반 솔루션의 우수성

## 관련 페이지

- [[datalink-communication]] — RF, LTE, WiFi 등 데이터링크 기술
- [[drone-ai-agents]] — 자율 의사결정 및 에이전트 아키텍처
- [[active-sensing-uav-communication]] — 감지 지원 UAV 통신

## 출처

- Wang et al., "Inverse-Reinforcement Learning Enabled Digital Twi
- [3] `concepts/stacked-intelligent-metasurfaces.md` — Stacked Intelligent Metasurfaces Assisted UAV Communications (slug: `stacked-intelligent-metasurfaces`, layer: concepts)
  발췌: Stacked Intelligent Metasurfaces(SIM)를 활용한 UAV 통신 시스템. 다층 캐스케이드 메타표면을 통해 전자기 도메인에서 프로그래머블 파형 신호 처리를 가능하게 한다.

## SIM 아키텍처

### 핵심 특성
- **다층 캐스케이드 메타표면**: 여러 층의 메타표면이 연속적으로 신호 처리
- **전자기 도메인 처리**: RF/디지털 도메인에서 전자기 도메인으로 일부 빔포밍 기능 이전
- **에너지 효율성**: 저전력 하이브리드 빔포밍 아키텍처 실현

### 장점
- 낮은 하드웨어 복잡성
- 높은 스펙트럼 효율성
- UAV 플랫폼에 적합한 에너지 효율

## 최적화 문제

### 목표
다중 사용자 다운링크 합속률 최대화를 위한:
- 디지털 프리코딩 설계
- SIM 위상 구성
- UAV 위치 선정

### 해결 방법
**교대 최적화 프레임워크**: 목적 함수의 단조적 개선 보장

## 성능 분석

| 요소 | 영향 |
|------|------|
| 메타표면 층 수 | 시스템 성능에 직접적 영향 |
| 각 층 크기 | 커버리지 및 이득 결정 |
| 스펙트럼 효율 | 기존 방식 대비 향상 |

## 응용 분야

- UAV-to-Ground 통신
- UAV-to-UAV 통신
- 5G/6G 통합 UAV 네트워크

## 관련 페이지

- [[emnn-doa-estimation]] — EMNN 기반 DOA 추정
- [[vertical-pinching-antenna-systems]] — V-PAS 기반 UAV 통신
- [[datalink-communication]] — 드론 데이터링크 통신 기술

**raw 검색 결과**
- [2] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생
- [1] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,
- [1] `raw/articles/mastervault-hardware-reference.md` — --- source_url: "file://MasterVault/Drone/Hardware/Hardware-Reference.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "1b5e9c2d6a8f3b6d9e2f5a8c1d4e7f9a2b5c8d1e4f7a9b2c5d8e1f4a7b9c2d5" tags: [drone-hw] ---  # 드론 하드웨어 레퍼런스  ## FC (Flight Controller)  ### Holybro  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || Pixhawk 6X | STM32H753 | 최상위, 산업용 | 대형 드론 | || Pixhawk 6X Pro | STM32H753 | 6X + 추가 센서 | 정밀 작업 | || Pixhawk 6C | STM32H743 | 가성비 | 교육/개발 | || Pixhawk 6C Mini | STM32H743 | 소형 | 레이서/소형기 | || Kakute H7 | STM32H743 | FPV 특화 | FPV 레이서 |  ### CUAV  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || V7+ | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 | || X7+ Pro | STM32H753 | 최상위 | 대형/산업 | || Nora+ | STM32H753 | 방열 우수 | 고온 환경 | || 7-Nano | STM32H743 | 초소형 | 소형 기체 |  ## GPS/RTK  || 제조사 | 모델 | 정밀도 | 비고 | ||--------|---
- [1] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [1] `raw/articles/mastervault-swarm-architecture.md` — --- source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4" tags: [swarm, datalink] ---  # 스웜 드론 아키텍처  ## 시스템 구조  ``` ┌─────────────────────────────────────────────────┐ │                  Ground Station                  │ │  ┌───────────┐  ┌───────────┐  ┌────────────┐  │ │  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │ │  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │ └────────┼───────────────┼──────────────┼─────────┘          │               │              │          └───────────────┼──────────────┘                          │ MAVLink          ┌───────────────┼──────────────┐          ▼               ▼              ▼    ┌──────────┐    ┌──────────┐   ┌──────────┐    │ Leader   │    │ Follower │   │ Followe

**뉴스 검색 결과**
- [1] [Auterion] Marine Corps fiber-optic live fire strike at Camp Pendleton | Auterion — https://www.youtube.com/watch?v=p_4k97SzLWk
- [1] [핑크랩 PinkLAB] 핑크랩 PL2M 공개! ROS 2 기반 주행형 양팔로봇 플랫폼 — https://www.youtube.com/watch?v=-i5dSTGDHhI
- [1] [핑크랩 PinkLAB] [R2R Moveit] 쪼랩회사 대표의 고민, 그리고 ROS 2 그리퍼 제어 강의 — https://www.youtube.com/watch?v=K_FYZC1ezRo
- [1] Design and Performance Evaluation of Secure RF and WiFi-Based Communication in Drone Swarms via Testbed Implementation — http://arxiv.org/abs/2606.27028v1

**그래프 인접 슬러그** (1-hop): `advanced-mavlink`, `drone-ai-agents`, `drone-hw`, `drone-regulations`, `dronecan-protocol`, `emnn-doa-estimation`

### 검색: 국내에서 드론 C2 링크용으로 LTE 망을 사용할 경우 통신사 회선 임대 및 망 이용대가 관련 제도적 제약은 무엇인가

**canonical 검색 결과**
- [4] `concepts/datalink-communication.md` — Datalink Communication (slug: `datalink-communication`, layer: concepts)
  발췌: Datalink은 드론과 지상국(GCS) 또는 타 드론 간 데이터 통신을 담당하는 물리/링크 계층 시스템이다. C2(Command & Control) 링크와 텔레메트리를 포함한다.

## 통신 계층

```
┌─────────────────────────────────────────┐
│           Application Layer           │
│         MAVLink / Custom API          │
├─────────────────────────────────────────┤
│           Transport Layer             │
│         UDP / TCP / Serial            │
├─────────────────────────────────────────┤
│            Link Layer                 │
│   Radio / WiFi / LTE / Satellite      │
├─────────────────────────────────────────┤
│           Physical Layer              │
│   RF / Optical / Wired / Acoustic     │
└─────────────────────────────────────────┘
```

## 무선 통신 기술

### 1. RF Radio (전통적 텔레메트리)

| 특성 | 설명 |
|------|------|
| **주파수 대역** | 433MHz, 915MHz, 2.4GHz |
| **범위** | 1km ~ 60km (장비에 따라) |
| **속도** | 57.6kbps ~ 250kbps |
| **지연** | 10-100ms |
| **비용** | 저렴 |

**제품 예시:*
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
- [4] `concepts/drone-news-ops.md` — 드론 운용 및 미션 동향 2026-07 (slug: `drone-news-ops`, layer: concepts)
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
- [4] `concepts/drone-news-regulations.md` — 드론 규제 동향 2026-07 (slug: `drone-news-regulations`, layer: concepts)
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
- [4] `concepts/fpv-hardware.md` — FPV 드론 하드웨어 동향 (slug: `fpv-hardware`, layer: concepts)
  발췌: 2026년 7월 FPV 드론 하드웨어 시장의 최신 동향. DJI, BetaFPV, HGLRC 등 주요 제조사의 신제품과 기술 발전을 다룬다.

## 주요 하드웨어 동향

### DJI O4 Wide Air Unit

- **개선된 시야각(FOV)**: 내장 와이드 앵글 렌즈로 기존 O4의 좁은 FOV 문제 해결
- **시장 반응**: FPV 커뮤니티에서 가장 요구되던 기능 중 하나

### BetaFPV Meteor75 Pro II

- **DJI O4 Wide 지원**: 최초로 DJI O4 Wide Air Unit을 지원하는 BNF(Bind-N-Fly) Tiny Whoop
- **타겟**: 실내 FPV 입문자 및 마이크로 드론 애호가

### HGLRC Talon Pro 3-Inch Cinewhoop

- **분리형 카메라 케이지**: 다른 쿼드콥터로 이식 가능한 모듈형 설계
- **타겟**: 시네마틱 촬영용 마이크로 드론

### Betaflight Arming 문제

- **일반적인 문제**: 초보자가 가장 많이 겪는 Betaflight 드론 Arming 실패
- **원인**: 대부분 설정 문제이며 하드웨어 고장은 아님
- **해결책**: Betaflight Configurator를 통한 안전 조건 확인

### USB 포트 손상

- **흔한 고장**: 비행 컨트롤러의 USB 포트 탈락
- **대안**: UART를 통한 펌웨어 플래싱 방법 존재

## 관련 개념

- [[betaflight]] — FPV 드론용 비행 제어 소프트웨어
- [[flight-controller-hardware]] — FC 하드웨어 개요
- [[drone-payload-systems]] — 카메라 및 페이로드 통합

**raw 검색 결과**
- [2] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [2] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생
- [2] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,
- [2] `raw/articles/mastervault-hardware-reference.md` — --- source_url: "file://MasterVault/Drone/Hardware/Hardware-Reference.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "1b5e9c2d6a8f3b6d9e2f5a8c1d4e7f9a2b5c8d1e4f7a9b2c5d8e1f4a7b9c2d5" tags: [drone-hw] ---  # 드론 하드웨어 레퍼런스  ## FC (Flight Controller)  ### Holybro  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || Pixhawk 6X | STM32H753 | 최상위, 산업용 | 대형 드론 | || Pixhawk 6X Pro | STM32H753 | 6X + 추가 센서 | 정밀 작업 | || Pixhawk 6C | STM32H743 | 가성비 | 교육/개발 | || Pixhawk 6C Mini | STM32H743 | 소형 | 레이서/소형기 | || Kakute H7 | STM32H743 | FPV 특화 | FPV 레이서 |  ### CUAV  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || V7+ | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 | || X7+ Pro | STM32H753 | 최상위 | 대형/산업 | || Nora+ | STM32H753 | 방열 우수 | 고온 환경 | || 7-Nano | STM32H743 | 초소형 | 소형 기체 |  ## GPS/RTK  || 제조사 | 모델 | 정밀도 | 비고 | ||--------|---
- [2] `raw/articles/mastervault-swarm-architecture.md` — --- source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4" tags: [swarm, datalink] ---  # 스웜 드론 아키텍처  ## 시스템 구조  ``` ┌─────────────────────────────────────────────────┐ │                  Ground Station                  │ │  ┌───────────┐  ┌───────────┐  ┌────────────┐  │ │  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │ │  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │ └────────┼───────────────┼──────────────┼─────────┘          │               │              │          └───────────────┼──────────────┘                          │ MAVLink          ┌───────────────┼──────────────┐          ▼               ▼              ▼    ┌──────────┐    ┌──────────┐   ┌──────────┐    │ Leader   │    │ Follower │   │ Followe

**뉴스 검색 결과**
- [1] [기자문답] 미국 드론 시장, 한국에 손 내미는 이유 — https://news.google.com/rss/articles/CBMibEFVX3lxTE9JeUJSRDgxWDhnRlZ4dlprbHlQTllDOHpVZ1lsUVZTbkl1SGlVWVhFRE5uRGpibnZPOXNaR0xKWVlPeU41X2pJUUNuUTV2U25ZUmtmUHd0RjdVd1k1bmI4VEZOVnQzOVZxRFNya9IBb0FVX3lxTFBDVTNkVnpKVEtoU2dFa1ZVWk84bzYwX2hsUDQ4ZEJSZXFxUEo0YlE1QW5kVWgyWGw2ajJXcFN2OV83TDhad2tKOUYxRWdVRGZXSFAzUTE2ZF9IT25Pb01mTmlwV29nSk5NYWp1WGpCWQ?oc=5
- [1] 이집트까지 드론 피격… 중동대전으로 번지나 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5pVGNVeWo5d0oxYWRKUWhFTHRUbWtyOEI4MHFkdlh1NmFOdmt3V3ltN0VoOEU4OU9xNzJsa2U0TzJoSzZyMkRTd25SYVZ3ZkU?oc=5
- [1] "이집트서 미국 소유 LNG 설비 드론 공격에 화재" — https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1qYXlfWmpTOEwtdjJFWVV5cHFWUGNvUWhBSTJCUWVfRlUtRmFBb0thSTNUZDBOTlFuUV9wb1VDVmhpQVU5MGowTGYtSWRZUDlaWkZVMWR2Vkg5azJPOXpGNjZLMmV1OWc?oc=5
- [1] 경기 북부서 '미확인 비행체' 해프닝…알고보니 한미 훈련 드론 — https://news.google.com/rss/articles/CBMia0FVX3lxTFB5Qmtac2NsM3M1a3l2SzlHYy10LUJLUXZsUndLdTlObW1IMlFZSmhLT1lvbTRfY3lBQTZUZFFPN3FLdTRxMXN0NmswMEJUUVA5UWNzeTUwUklVOW81R2Jlbi1ibEpwcGhQeHdz?oc=5

**그래프 인접 슬러그** (1-hop): `active-sensing-uav-communication`, `advanced-mavlink`, `betaflight`, `decentralized-swarm-gps-denied`, `digital-twin-intent-drone-networks`, `drone-payload-systems`

### 검색: RF 메시 네트워크형 C2 링크가 다중 드론 군집 운용 시 갖는 주파수 간섭·혼신 문제와 국내 규제 대응 사례는 무엇인가

**canonical 검색 결과**
- [10] `concepts/swarm-modes.md` — Swarm Modes — 군집 드론 운용 모드 (slug: `swarm-modes`, layer: concepts)
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
- [9] `concepts/drone-news-ops.md` — 드론 운용 및 미션 동향 2026-07 (slug: `drone-news-ops`, layer: concepts)
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
- [8] `concepts/drone-news-regulations.md` — 드론 규제 동향 2026-07 (slug: `drone-news-regulations`, layer: concepts)
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
- [6] `concepts/drone-regulations.md` — Drone Regulations (slug: `drone-regulations`, layer: concepts)
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
- [3] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생
- [2] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [2] `raw/articles/mastervault-hardware-reference.md` — --- source_url: "file://MasterVault/Drone/Hardware/Hardware-Reference.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "1b5e9c2d6a8f3b6d9e2f5a8c1d4e7f9a2b5c8d1e4f7a9b2c5d8e1f4a7b9c2d5" tags: [drone-hw] ---  # 드론 하드웨어 레퍼런스  ## FC (Flight Controller)  ### Holybro  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || Pixhawk 6X | STM32H753 | 최상위, 산업용 | 대형 드론 | || Pixhawk 6X Pro | STM32H753 | 6X + 추가 센서 | 정밀 작업 | || Pixhawk 6C | STM32H743 | 가성비 | 교육/개발 | || Pixhawk 6C Mini | STM32H743 | 소형 | 레이서/소형기 | || Kakute H7 | STM32H743 | FPV 특화 | FPV 레이서 |  ### CUAV  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || V7+ | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 | || X7+ Pro | STM32H753 | 최상위 | 대형/산업 | || Nora+ | STM32H753 | 방열 우수 | 고온 환경 | || 7-Nano | STM32H743 | 초소형 | 소형 기체 |  ## GPS/RTK  || 제조사 | 모델 | 정밀도 | 비고 | ||--------|---
- [2] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [2] `raw/articles/mastervault-swarm-architecture.md` — --- source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4" tags: [swarm, datalink] ---  # 스웜 드론 아키텍처  ## 시스템 구조  ``` ┌─────────────────────────────────────────────────┐ │                  Ground Station                  │ │  ┌───────────┐  ┌───────────┐  ┌────────────┐  │ │  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │ │  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │ └────────┼───────────────┼──────────────┼─────────┘          │               │              │          └───────────────┼──────────────┘                          │ MAVLink          ┌───────────────┼──────────────┐          ▼               ▼              ▼    ┌──────────┐    ┌──────────┐   ┌──────────┐    │ Leader   │    │ Follower │   │ Followe

**뉴스 검색 결과**
- [1] [기자문답] 미국 드론 시장, 한국에 손 내미는 이유 — https://news.google.com/rss/articles/CBMibEFVX3lxTE9JeUJSRDgxWDhnRlZ4dlprbHlQTllDOHpVZ1lsUVZTbkl1SGlVWVhFRE5uRGpibnZPOXNaR0xKWVlPeU41X2pJUUNuUTV2U25ZUmtmUHd0RjdVd1k1bmI4VEZOVnQzOVZxRFNya9IBb0FVX3lxTFBDVTNkVnpKVEtoU2dFa1ZVWk84bzYwX2hsUDQ4ZEJSZXFxUEo0YlE1QW5kVWgyWGw2ajJXcFN2OV83TDhad2tKOUYxRWdVRGZXSFAzUTE2ZF9IT25Pb01mTmlwV29nSk5NYWp1WGpCWQ?oc=5
- [1] 이집트까지 드론 피격… 중동대전으로 번지나 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5pVGNVeWo5d0oxYWRKUWhFTHRUbWtyOEI4MHFkdlh1NmFOdmt3V3ltN0VoOEU4OU9xNzJsa2U0TzJoSzZyMkRTd25SYVZ3ZkU?oc=5
- [1] "이집트서 미국 소유 LNG 설비 드론 공격에 화재" — https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1qYXlfWmpTOEwtdjJFWVV5cHFWUGNvUWhBSTJCUWVfRlUtRmFBb0thSTNUZDBOTlFuUV9wb1VDVmhpQVU5MGowTGYtSWRZUDlaWkZVMWR2Vkg5azJPOXpGNjZLMmV1OWc?oc=5
- [1] 경기 북부서 '미확인 비행체' 해프닝…알고보니 한미 훈련 드론 — https://news.google.com/rss/articles/CBMia0FVX3lxTFB5Qmtac2NsM3M1a3l2SzlHYy10LUJLUXZsUndLdTlObW1IMlFZSmhLT1lvbTRfY3lBQTZUZFFPN3FLdTRxMXN0NmswMEJUUVA5UWNzeTUwUklVOW81R2Jlbi1ibEpwcGhQeHdz?oc=5

**그래프 인접 슬러그** (1-hop): `amazon-mk30-safety-incident`, `brinc-emergency-drone-funding`, `datalink-communication`, `dji-easa-sail-bvlos`, `doordash-air`, `drone-ai-agents`

### 검색: 저고도 드론 C2 링크에 대한 국내 UAM/드론 특별법 또는 항공안전법상 통신방식별 인증·안전 요건 차이는 무엇인가

**canonical 검색 결과**
- [5] `concepts/drone-news-regulations.md` — 드론 규제 동향 2026-07 (slug: `drone-news-regulations`, layer: concepts)
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
- [3] `concepts/datalink-communication.md` — Datalink Communication (slug: `datalink-communication`, layer: concepts)
  발췌: Datalink은 드론과 지상국(GCS) 또는 타 드론 간 데이터 통신을 담당하는 물리/링크 계층 시스템이다. C2(Command & Control) 링크와 텔레메트리를 포함한다.

## 통신 계층

```
┌─────────────────────────────────────────┐
│           Application Layer           │
│         MAVLink / Custom API          │
├─────────────────────────────────────────┤
│           Transport Layer             │
│         UDP / TCP / Serial            │
├─────────────────────────────────────────┤
│            Link Layer                 │
│   Radio / WiFi / LTE / Satellite      │
├─────────────────────────────────────────┤
│           Physical Layer              │
│   RF / Optical / Wired / Acoustic     │
└─────────────────────────────────────────┘
```

## 무선 통신 기술

### 1. RF Radio (전통적 텔레메트리)

| 특성 | 설명 |
|------|------|
| **주파수 대역** | 433MHz, 915MHz, 2.4GHz |
| **범위** | 1km ~ 60km (장비에 따라) |
| **속도** | 57.6kbps ~ 250kbps |
| **지연** | 10-100ms |
| **비용** | 저렴 |

**제품 예시:*
- [3] `concepts/drone-news-hardware.md` — 드론 하드웨어 및 제조사 동향 2026-07 (slug: `drone-news-hardware`, layer: concepts)
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
- [3] `concepts/drone-news-ops.md` — 드론 운용 및 미션 동향 2026-07 (slug: `drone-news-ops`, layer: concepts)
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
- [3] `concepts/drone-regulations.md` — Drone Regulations (slug: `drone-regulations`, layer: concepts)
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
- [1] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [1] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생
- [1] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,
- [1] `raw/articles/mastervault-hardware-reference.md` — --- source_url: "file://MasterVault/Drone/Hardware/Hardware-Reference.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "1b5e9c2d6a8f3b6d9e2f5a8c1d4e7f9a2b5c8d1e4f7a9b2c5d8e1f4a7b9c2d5" tags: [drone-hw] ---  # 드론 하드웨어 레퍼런스  ## FC (Flight Controller)  ### Holybro  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || Pixhawk 6X | STM32H753 | 최상위, 산업용 | 대형 드론 | || Pixhawk 6X Pro | STM32H753 | 6X + 추가 센서 | 정밀 작업 | || Pixhawk 6C | STM32H743 | 가성비 | 교육/개발 | || Pixhawk 6C Mini | STM32H743 | 소형 | 레이서/소형기 | || Kakute H7 | STM32H743 | FPV 특화 | FPV 레이서 |  ### CUAV  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || V7+ | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 | || X7+ Pro | STM32H753 | 최상위 | 대형/산업 | || Nora+ | STM32H753 | 방열 우수 | 고온 환경 | || 7-Nano | STM32H743 | 초소형 | 소형 기체 |  ## GPS/RTK  || 제조사 | 모델 | 정밀도 | 비고 | ||--------|---
- [1] `raw/articles/mastervault-swarm-architecture.md` — --- source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4" tags: [swarm, datalink] ---  # 스웜 드론 아키텍처  ## 시스템 구조  ``` ┌─────────────────────────────────────────────────┐ │                  Ground Station                  │ │  ┌───────────┐  ┌───────────┐  ┌────────────┐  │ │  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │ │  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │ └────────┼───────────────┼──────────────┼─────────┘          │               │              │          └───────────────┼──────────────┘                          │ MAVLink          ┌───────────────┼──────────────┐          ▼               ▼              ▼    ┌──────────┐    ┌──────────┐   ┌──────────┐    │ Leader   │    │ Follower │   │ Followe

**뉴스 검색 결과**
- [1] [기자문답] 미국 드론 시장, 한국에 손 내미는 이유 — https://news.google.com/rss/articles/CBMibEFVX3lxTE9JeUJSRDgxWDhnRlZ4dlprbHlQTllDOHpVZ1lsUVZTbkl1SGlVWVhFRE5uRGpibnZPOXNaR0xKWVlPeU41X2pJUUNuUTV2U25ZUmtmUHd0RjdVd1k1bmI4VEZOVnQzOVZxRFNya9IBb0FVX3lxTFBDVTNkVnpKVEtoU2dFa1ZVWk84bzYwX2hsUDQ4ZEJSZXFxUEo0YlE1QW5kVWgyWGw2ajJXcFN2OV83TDhad2tKOUYxRWdVRGZXSFAzUTE2ZF9IT25Pb01mTmlwV29nSk5NYWp1WGpCWQ?oc=5
- [1] 이집트까지 드론 피격… 중동대전으로 번지나 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5pVGNVeWo5d0oxYWRKUWhFTHRUbWtyOEI4MHFkdlh1NmFOdmt3V3ltN0VoOEU4OU9xNzJsa2U0TzJoSzZyMkRTd25SYVZ3ZkU?oc=5
- [1] "이집트서 미국 소유 LNG 설비 드론 공격에 화재" — https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1qYXlfWmpTOEwtdjJFWVV5cHFWUGNvUWhBSTJCUWVfRlUtRmFBb0thSTNUZDBOTlFuUV9wb1VDVmhpQVU5MGowTGYtSWRZUDlaWkZVMWR2Vkg5azJPOXpGNjZLMmV1OWc?oc=5
- [1] 경기 북부서 '미확인 비행체' 해프닝…알고보니 한미 훈련 드론 — https://news.google.com/rss/articles/CBMia0FVX3lxTFB5Qmtac2NsM3M1a3l2SzlHYy10LUJLUXZsUndLdTlObW1IMlFZSmhLT1lvbTRfY3lBQTZUZFFPN3FLdTRxMXN0NmswMEJUUVA5UWNzeTUwUklVOW81R2Jlbi1ibEpwcGhQeHdz?oc=5

**그래프 인접 슬러그** (1-hop): `active-sensing-uav-communication`, `advanced-mavlink`, `amazon-mk30-safety-incident`, `brinc-emergency-drone-funding`, `decentralized-swarm-gps-denied`, `digital-twin-intent-drone-networks`

### 검색: 해외(미국 FCC, 유럽 ETSI 등)의 드론 C2 링크 주파수 정책과 국내 정책의 차이는 무엇이며 국내 규제에 시사하는 바는 무엇인가

**canonical 검색 결과**
- [6] `concepts/fcc-drone-regulations.md` — FCC Drone Regulations (slug: `fcc-drone-regulations`, layer: concepts)
  발췌: 미국 연방통신위원회(FCC)의 드론 관련 규제 정책. 2026년 7월 Covered List 제한 강화 및 외국 제조 드론 수입/판매 금지 추진.

## 주요 정책 변화

### Covered List 제한
- 특정 외국 제조 드론의 상업적 수입 및 판매 금안
- DJI 관련 쉘 컴퍼니(SkyRover, Specta 등) 규제 강화
- Odyssey Robotics 등 DJI 연계 의심 기기 승인 취소 시도

### Conditional Approval
- 신뢰할 수 있는 제조사에 대한 장기적 규제 프레임워크
- Onshoring(국내 생산) 우대 정책

## 영향

- NDAA(국방수권법) 준수 요구 증가
- 미국 내 드론 제조 생태계 변화
- 소비자 선택지 제한 가능성

## 관련 항목

- [[drone-regulations]] — 드론 규제 종합
- [[drone-hw]] — 드론 하드웨어
- [[terra-drone]] — 일본 배터리 사업 진출 사례
- [5] `concepts/drone-regulations.md` — Drone Regulations (slug: `drone-regulations`, layer: concepts)
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
- [4] `concepts/datalink-communication.md` — Datalink Communication (slug: `datalink-communication`, layer: concepts)
  발췌: Datalink은 드론과 지상국(GCS) 또는 타 드론 간 데이터 통신을 담당하는 물리/링크 계층 시스템이다. C2(Command & Control) 링크와 텔레메트리를 포함한다.

## 통신 계층

```
┌─────────────────────────────────────────┐
│           Application Layer           │
│         MAVLink / Custom API          │
├─────────────────────────────────────────┤
│           Transport Layer             │
│         UDP / TCP / Serial            │
├─────────────────────────────────────────┤
│            Link Layer                 │
│   Radio / WiFi / LTE / Satellite      │
├─────────────────────────────────────────┤
│           Physical Layer              │
│   RF / Optical / Wired / Acoustic     │
└─────────────────────────────────────────┘
```

## 무선 통신 기술

### 1. RF Radio (전통적 텔레메트리)

| 특성 | 설명 |
|------|------|
| **주파수 대역** | 433MHz, 915MHz, 2.4GHz |
| **범위** | 1km ~ 60km (장비에 따라) |
| **속도** | 57.6kbps ~ 250kbps |
| **지연** | 10-100ms |
| **비용** | 저렴 |

**제품 예시:*
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

**raw 검색 결과**
- [2] `raw/articles/mastervault-hardware-reference.md` — --- source_url: "file://MasterVault/Drone/Hardware/Hardware-Reference.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "1b5e9c2d6a8f3b6d9e2f5a8c1d4e7f9a2b5c8d1e4f7a9b2c5d8e1f4a7b9c2d5" tags: [drone-hw] ---  # 드론 하드웨어 레퍼런스  ## FC (Flight Controller)  ### Holybro  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || Pixhawk 6X | STM32H753 | 최상위, 산업용 | 대형 드론 | || Pixhawk 6X Pro | STM32H753 | 6X + 추가 센서 | 정밀 작업 | || Pixhawk 6C | STM32H743 | 가성비 | 교육/개발 | || Pixhawk 6C Mini | STM32H743 | 소형 | 레이서/소형기 | || Kakute H7 | STM32H743 | FPV 특화 | FPV 레이서 |  ### CUAV  || 모델 | 프로세서 | 특징 | 용도 | ||------|----------|------|------| || V7+ | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 | || X7+ Pro | STM32H753 | 최상위 | 대형/산업 | || Nora+ | STM32H753 | 방열 우수 | 고온 환경 | || 7-Nano | STM32H743 | 초소형 | 소형 기체 |  ## GPS/RTK  || 제조사 | 모델 | 정밀도 | 비고 | ||--------|---
- [2] `raw/articles/mastervault-swarm-architecture.md` — --- source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4" tags: [swarm, datalink] ---  # 스웜 드론 아키텍처  ## 시스템 구조  ``` ┌─────────────────────────────────────────────────┐ │                  Ground Station                  │ │  ┌───────────┐  ┌───────────┐  ┌────────────┐  │ │  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │ │  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │ └────────┼───────────────┼──────────────┼─────────┘          │               │              │          └───────────────┼──────────────┘                          │ MAVLink          ┌───────────────┼──────────────┐          ▼               ▼              ▼    ┌──────────┐    ┌──────────┐   ┌──────────┐    │ Leader   │    │ Follower │   │ Followe
- [1] `raw/articles/entity-ardupilot.md` — --- title: "ArduPilot — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://ardupilot.org/ardupilot/" author: "ArduPilot Dev Team / Master" sha256: "" tags: [drone-sw] ---  # ArduPilot — Entity Reference  ## 개요  ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다. 2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.  - **공식 레포**: https://github.com/ArduPilot/ardupilot - **최신 안정 버전**: ArduCopter 4.5.x (2024 기준) - **라이선스**: GPLv3 - **지원 OS**: ChibiOS, Linux, SITL  ## 기체 타입별 빌드 이름  | 기체 타입 | 빌드 이름 | 설명 | |---|---|---| | 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 | | 고정익 | `ArduPlane` | 전통 고정익 + VTOL | | 로버 | `ArduRover` | 지상 무인차량 | | 잠수함 | `ArduSub` | 수중 드론 | | 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |  ## 핵심 파라미터  | 파라미터 | 기본값 | 설명 | |---|---|---| | `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 | | `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 | | `ATC_RAT_YAW_P` | 0.18
- [1] `raw/articles/entity-mavlink-protocol.md` — --- title: "MAVLink Protocol — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://mavlink.io/en/" author: "MAVLink Dev Team / Master" sha256: "" tags: [datalink, drone-sw] ---  # MAVLink Protocol — Entity Reference  ## 개요  MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다. Lorenz Meier가 2009년 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.  - **공식 레포**: https://github.com/mavlink/mavlink - **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0) - **라이선스**: MIT (메시지 정의: XML) - **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트  ## 버전 비교  | 항목 | MAVLink 1.0 | MAVLink 2.0 | |---|---|---| | 최대 페이로드 | 255 바이트 | 255 바이트 | | 메시지 ID 범위 | 0–255 | 0–16,777,215 | | 서명(Signing) | ❌ | ✅ (HMAC-SHA256) | | 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) | | 컴포넌트 타겟팅 | ❌ | ✅ | | 패킷 헤더 크기 | 6 바이트 | 10 바이트 |  ## 핵심 메시지 (Messages)  | Message ID | 이름 | 설명 | |---|---|---| | 0 | `HEARTBEAT` | 시스템 생
- [1] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,

**뉴스 검색 결과**
- [2] [기자문답] 미국 드론 시장, 한국에 손 내미는 이유 — https://news.google.com/rss/articles/CBMibEFVX3lxTE9JeUJSRDgxWDhnRlZ4dlprbHlQTllDOHpVZ1lsUVZTbkl1SGlVWVhFRE5uRGpibnZPOXNaR0xKWVlPeU41X2pJUUNuUTV2U25ZUmtmUHd0RjdVd1k1bmI4VEZOVnQzOVZxRFNya9IBb0FVX3lxTFBDVTNkVnpKVEtoU2dFa1ZVWk84bzYwX2hsUDQ4ZEJSZXFxUEo0YlE1QW5kVWgyWGw2ajJXcFN2OV83TDhad2tKOUYxRWdVRGZXSFAzUTE2ZF9IT25Pb01mTmlwV29nSk5NYWp1WGpCWQ?oc=5
- [2] "이집트서 미국 소유 LNG 설비 드론 공격에 화재" — https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1qYXlfWmpTOEwtdjJFWVV5cHFWUGNvUWhBSTJCUWVfRlUtRmFBb0thSTNUZDBOTlFuUV9wb1VDVmhpQVU5MGowTGYtSWRZUDlaWkZVMWR2Vkg5azJPOXpGNjZLMmV1OWc?oc=5
- [2] "이집트서 미국 소유 LNG 설비 드론 공격에 화재" — https://news.google.com/rss/articles/CBMiT0FVX3lxTE9aY1ptTEhxQkt6dnF2R0tuTGZ2WjlVams5OW1vQVktcnN3TmZrVWI3OFFEd01UMndXR0o0WXFFbjZLZnBDMFVZdUlBaTNhdWs?oc=5
- [2] [미국 특징주] 도어대시, FAA 인증 획득 후 자체 드론 배송 프로그램 출시 — https://news.google.com/rss/articles/CBMiXEFVX3lxTE4xSWIyY3ZJdk1MMFNEVmMwU0gtT1lqSm1rUjhId0VBXzlGM1YtZkdNZkNJZ2p3WlRrNHNERUFBYlNpT3ZFOEItbXdBd2p6WVRudUdscjdWSWFyc0Qz?oc=5

**그래프 인접 슬러그** (1-hop): `active-sensing-uav-communication`, `advanced-mavlink`, `amazon-mk30-safety-incident`, `brinc-emergency-drone-funding`, `decentralized-swarm-gps-denied`, `digital-twin-intent-drone-networks`

