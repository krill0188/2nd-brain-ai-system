# 기계 검색 결과 (Retriever — LLM 미사용, 하이브리드: ON)

### 검색: 마이크로드론 온보드 SLAM에서 주로 사용되는 센서 구성(카메라 단독 vs. 카메라+IMU vs. LiDAR)은 무엇이며 어떤 조합이 가장 빈번하게 언급되는가?

**canonical 검색 결과**
- [0.347, cos=0.466] `concepts/flight-ready-lidar-inertial-odometry.md` — Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms (slug: `flight-ready-lidar-inertial-odometry`, layer: concepts)
  발췌: 실시간 폐쇄 루프 항공 제어에 최적화된 LiDAR-관성 오도메트리(LIO) 시스템. IESKF 기반 LIO의 아키텍처 결함을 해결하여 임베디드 드론 플랫폼에서 실제 비행 준비 상태를 달성한다.

## 기존 LIO의 아키텍처 결함

| 결함 | 문제점 |
|------|--------|
| LiDAR 레이트에 묶인 오도메트리 발행 | 10 Hz (IMU 200 Hz 대비) |
| 누락된 속도 출력 | 완전한 상태 벡터 부재 |
| 실행 병목 현상 | IMU 처리 차단 |
| 뮤텍스 경쟁 | 동기화 문제 |
| 동기화 경쟁 조건 | 데이터 일관성 문제 |

## 개선 사항

### 1. IMU 레이트 전파 (IMU-rate Forward Propagation)
- 오도메트리 출력: ~10 Hz → 안정적인 200 Hz
- 모든 IMU 샘플에서 완전한 Twist 상태 제공

### 2. 직접 바디 프레임 속도 발행
- 완전한 상태 벡터 (위치 + 속도) 출력

### 3. SLERP 기반 스무딩
- LiDAR 손실 시에도 연속성 유지

### 4. 듀얼 실행기 격리
- 실행 병목 현상 제거

### 5. 명시적 동기화 보호
- 뮤텍스 경쟁 및 경쟁 조건 방지

## 검증

- **플랫폼**: Livox Mid-360 / Pixhawk 4 Mini 자율 UAV
- **그라운드 트루스**: 모션 캡처 시스템
- **결과**: 실시간 제어 요구사항 충족 확인

## 적용 가능성

기본 추정기(IESKF + ikd-Tree)를 변경하지 않으므로, FAST-LIO2 파생 구현체에 직접 적용 가능하다.

## 관련 페이지

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 SLAM
- [[px4-offboard-control]] — PX4 오프보드 제어
- [[drone-si
- [0.311, cos=0.444] `concepts/computer-vision-drone.md` — Computer Vision for Drones (slug: `computer-vision-drone`, layer: concepts)
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
- [0.305, cos=0.398] `concepts/recon-swarm-project.md` — Recon Swarm Project — 지능형 자율 군집정찰드론 (slug: `recon-swarm-project`, layer: concepts)
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
- [0.304, cos=0.433] `concepts/opencv.md` — OpenCV (slug: `opencv`, layer: concepts)
  발췌: OpenCV(Open Source Computer Vision Library)은 실시간 컴퓨터 비전을 위한 오픈소스 라이브러리이다. 드론 분야에서는 객체 인식, 추적, SLAM, 이미지 처리 등 다양한 AI 응용에 활용된다.

## 핵심 기능

- **이미지/비디오 처리**: 필터링, 변환, 형태학적 연산
- **객체 검출**: Haar Cascade, HOG, 딥러닝 기반 검출
- **특징점 추출**: SIFT, SURF, ORB 등
- **카메라 캘리브레이션**: 렌즈 왜곡 보정, 스테레오 비전

## 최신 릴리스: OpenCV 5.0.0 (2026-06-06)

2026년 6월 6일 출시된 OpenCV 5.0.0은 메이저 버전 업그레이드이다:

- 4.x에서 5.x로의 마이그레이션 가이드 제공
- Android SDK 16KB 페이지 크기 대응 패키지 제공

## 드론 응용

- **객체 추적**: [[computer-vision-drone]]과 연계하여 실시간 타겟 추적
- **비전 기반 내비게이션**: [[drone-ai-agents]]에서 SLAM 및 장애물 회피
- **페이로드 통합**: [[drone-payload-systems]]의 카메라 시스템과 연동

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
- [[yolo]] — OpenCV와 함께 사용되는 객체 검출 모델
- [[ros2-drone-integration]] — OpenCV가 통합되는 ROS2 환경
- [0.302, cos=0.393] `concepts/drone-simulation.md` — Drone Simulation (slug: `drone-simulation`, layer: concepts)
  발췌: PX4 SITL(Software In The Loop)은 실제 하드웨어 없이 데스크톱에서 PX4 펌웨어를 실행하는 시뮬레이션 환경이다. Gazebo, jMAVSim, AirSim 등 다양한 시뮬레이터를 지원한다.^[raw/articles/mastervault-px4-devnotes.md]

## SITL 아키텍처

```
┌─────────────────────────────────────────┐
│           PX4 SITL (NuttX/Linux)      │
│         Flight Stack + Middleware     │
└───────────────────┬─────────────────────┘
                    │ UDP/MAVLink
┌───────────────────┴─────────────────────┐
│           Simulator (Gazebo/jMAVSim) │
│         Physics + Sensors (IMU, GPS) │
└─────────────────────────────────────────┘
```

## Gazebo Classic

현재 PX4의 주력 시뮬레이터.

### 실행

```bash
# PX4 SITL + Gazebo
make px4_sitl gazebo-classic

# 특정 기체
make px4_sitl gazebo-classic_iris
make px4_sitl gazebo-classic_standard_vtol
```

### Gazebo 특징

| 특성 | 설명 |
|------|------|
| **Physics** | ODE, Bullet, DART |
| **Sensors** | IMU, GPS, Baro, Lidar, Camera |
| **Scenarios** |

**raw 검색 결과**
- [0.324] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [0.314] `raw/papers/drone-hw/danial2025-microdrone-slam.md` — --- title: "Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors" authors:   - Jeryes Danial   - Yosi Ben Asher   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2511.14335" url: "https://arxiv.org/abs/2511.14335" pdf: "https://arxiv.org/pdf/2511.14335" topics: [drone-ai, drone-hw, micro-drone, slam, monocular, imu] abstract: |   This paper presents a SLAM system for micro drones using only a monocular camera and    inertial sensors. The system achieves simultaneous localization and 3D semi-dense mapping    suitable for resource-constrained micro aerial vehicles. The approach demonstrates that    accurate SLAM is possible on micro drones without stereo cameras or depth sensors. ingested: 2026-07-27 ---  # Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors  ##
- [0.255] `raw/articles/px4-hardware-overview.md` — --- source_url: "https://docs.px4.io/main/en/hardware/drone_parts.html" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "PX4 Dev Team" sha256: "2c6f0a3d7b9e4c7f0a3d6e9c2f5a8d1e4f7a9c2d5e8f1a4b7c9d2e5f8a1c4d7" tags: [drone, drone-hw] ---  # Hardware Selection & Setup  This section covers drone component information and configuration procedures for PX4 systems.  ## Major Component Categories  ### Flight Systems - Flight controllers and autopilots (including Pixhawk variants) - Firmware updates and bootloader procedures  ### Sensing Equipment - Inertial measurement (accelerometers, gyroscopes) - Environmental sensors (compass, airspeed, barometric pressure) - Distance measurement (rangefinders, LIDAR) - Navigation systems (GNSS, RTK GNSS, optical flow) - Additional sensors (tachometers, factory calibration, thermal compensation)  ### Motor & Control Systems - Actuator alloca
- [0.244] `raw/papers/drone-ai/shapira2025-icdnet.md` — --- title: "ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM" authors:   - Tali Orlev Shapira   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2512.00037" url: "https://arxiv.org/abs/2512.00037" pdf: "https://arxiv.org/pdf/2512.00037" topics: [drone-ai, slam, visual-inertial, deep-learning, computer-vision] abstract: |   This paper introduces ICD-Net, a deep learning-based approach for visual-inertial    SLAM in drones. The method uses inertial covariance displacement networks to improve    state estimation accuracy in challenging environments. The network learns to predict    covariance matrices for inertial measurements, enabling better fusion with visual    observations. ingested: 2026-07-27 ---  # ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM  ## Metadata  | 항목 | 내용 | |------|------| | **저자** | Tali Orlev Sh
- [0.241] `raw/articles/entity-pixhawk-hardware.md` — --- title: "Pixhawk Flight Controller — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/flight_controller/" author: "Pixhawk / PX4 Docs / Master" sha256: "" tags: [drone-hw, drone-sw] ---  # Pixhawk Flight Controller — Entity Reference  ## 개요  Pixhawk는 PX4 프로젝트와 함께 개발된 오픈 하드웨어 비행 제어기(FC) 플랫폼이다. Holybro, mRo, CubePilot 등 다수 제조사가 공식 Pixhawk 표준 호환 제품을 생산한다.  - **표준 문서**: https://github.com/pixhawk/Pixhawk-Standards - **주요 제조사**: Holybro (공식), CubePilot, mRo Technology - **버스 표준**: UAVCAN/DroneCAN, UART, SPI, I2C, CAN  ## 주요 모델 비교  | 모델 | MCU | RAM | 플래시 | 특징 | |---|---|---|---|---| | Pixhawk 1 | STM32F427 | 168MHz / 256KB | 2MB | 초기 레퍼런스, 단종 | | Pixhawk 4 | STM32F765 | 216MHz / 512KB | 2MB | Holybro 공식, 현 주력 | | Pixhawk 6C | STM32H743 | 480MHz / 1MB | 2MB | 최신 고성능 | | Pixhawk 6X | STM32H753 | 480MHz / 1MB | 2MB | 6C 상위 (이중화) | | Cub

**뉴스 검색 결과**
- [0.273] Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms — http://arxiv.org/abs/2607.22145v1
- [0.243] DJI’s newest gadget may outshine its new camera — https://dronedj.com/2026/07/31/dji-osmo-4p-us-price/
- [0.233] Military or Farm Tool? FCC’s Proposed Drone Categories Blur the Line — https://dronelife.com/2026/07/30/fcc-agricultural-spray-drones-proposal/
- [0.229] “코앞까지 접근”…감시망 뚫고 중국 군함 추적한 미 드론 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5QSGV6eWlpaFNSYUZ3Z3JlRklFUWpaLUNENjNHckJ1RGcybC1UaTNxNkRSYmFXWUhTc0xmamdSd3czakItb1dsTFZsVHZBRVk?oc=5

**그래프 인접 슬러그** (1-hop): `distributed-aerial-surveillance-swarm`, `drone-ai-agents`, `drone-payload-systems`, `drone-safety-failsafe`, `e2e-fly-end-to-end-quadrotor`, `flight-controller-hardware`

### 검색: 연산 자원이 제한된 마이크로드론 환경에서 SLAM 알고리즘의 경량화를 위해 어떤 접근법(특징점 기반 vs. 직접법 vs. 학습 기반)이 주로 채택되는가?

**canonical 검색 결과**
- [0.371, cos=0.47] `concepts/federated-lightweight-intrusion-detection.md` — Federated Lightweight Intrusion Detection in Drone Swarms (slug: `federated-lightweight-intrusion-detection`, layer: concepts)
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
- [0.326, cos=0.469] `concepts/chained-attacks-drone-fl.md` — Chained Attacks on Drone-Based Federated Learning (slug: `chained-attacks-drone-fl`, layer: concepts)
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
- [0.324, cos=0.428] `concepts/lightweight-safe-rl-uav.md` — Lightweight Safe RL for UAV Navigation (slug: `lightweight-safe-rl-uav`, layer: concepts)
  발췌: 밀집 환경에서 안전한 UAV 내비게이션을 위한 경량 안전 강화 학습 프레임워크. 비대칭 및 깊이별 분리 합성곱으로 희소 관측을 충돌 위험 인지 특징으로 인코딩하고, 제약 마르코프 결정 과정과 라그랑주 기반 안전 PPO로 안전성을 보장한다.

## 핵심 개념

### 경량 네트워크
- **Asymmetric Convolutions**: 비대칭 합성곱
- **Depthwise Separable Convolutions**: 깊이별 분리 합성곱
- **Collision-Risk-Aware Features**: 충돌 위험 인지 특징 인코딩

### 안전 메커니즘
- **Constrained MDP**: 제약 마르코프 결정 과정
- **Hierarchical Control Architecture**: 계층적 제어 아키텍처
- **Lagrangian-Based Safe PPO**: 라그랑주 기반 안전 PPO 알고리즘
- **Curriculum Learning**: 커리큘럼 학습으로 훈련 안정성 향상

### 성능
- 다양한 장애물 밀도 및 비행 속도에서 높은 성공률
- 기존 RL 기준선 대비 개선된 안전성 및 효율성
- 경량 온보드 배포 가능

## 관련 페이지

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 객체 검출
- [[drone-safety-failsafe]] — RTL, Geofence 등 안전 장치
- [[rl-quadrotor-tunable-control]] — RL 기반 쿼드로터 제어

## 출처

- Zhang et al., "Lightweight Safe Reinforcement Learning for End-to-End UAV Navigation", arXiv:2607.01794, 2026.
- [0.321, cos=0.425] `concepts/ai-personal-knowledge-management.md` — AI 개인 지식관리 (slug: `ai-personal-knowledge-management`, layer: concepts)
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

- [0.309, cos=0.404] `concepts/digital-twin-intent-drone-networks.md` — Digital Twin for Intent-Based Drone Networks (slug: `digital-twin-intent-drone-networks`, layer: concepts)
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

**raw 검색 결과**
- [0.285] `raw/papers/drone-ai/shapira2025-icdnet.md` — --- title: "ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM" authors:   - Tali Orlev Shapira   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2512.00037" url: "https://arxiv.org/abs/2512.00037" pdf: "https://arxiv.org/pdf/2512.00037" topics: [drone-ai, slam, visual-inertial, deep-learning, computer-vision] abstract: |   This paper introduces ICD-Net, a deep learning-based approach for visual-inertial    SLAM in drones. The method uses inertial covariance displacement networks to improve    state estimation accuracy in challenging environments. The network learns to predict    covariance matrices for inertial measurements, enabling better fusion with visual    observations. ingested: 2026-07-27 ---  # ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM  ## Metadata  | 항목 | 내용 | |------|------| | **저자** | Tali Orlev Sh
- [0.269] `raw/papers/drone-hw/danial2025-microdrone-slam.md` — --- title: "Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors" authors:   - Jeryes Danial   - Yosi Ben Asher   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2511.14335" url: "https://arxiv.org/abs/2511.14335" pdf: "https://arxiv.org/pdf/2511.14335" topics: [drone-ai, drone-hw, micro-drone, slam, monocular, imu] abstract: |   This paper presents a SLAM system for micro drones using only a monocular camera and    inertial sensors. The system achieves simultaneous localization and 3D semi-dense mapping    suitable for resource-constrained micro aerial vehicles. The approach demonstrates that    accurate SLAM is possible on micro drones without stereo cameras or depth sensors. ingested: 2026-07-27 ---  # Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors  ##
- [0.24] `raw/papers/swarm/li2025-airswarm.md` — --- title: "AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones" authors:   - Xiaowei Li   - Kuan Xu   - Fen Liu   - Ruofei Bai   - Shenghai Yuan   - Lihua Xie venue: "arXiv preprint" year: 2025 arxiv: "2503.06890" url: "https://arxiv.org/abs/2503.06890" pdf: "https://arxiv.org/pdf/2503.06890" topics: [swarm, multi-uav, cots, cost-effective, hardware] abstract: |   This paper presents AirSwarm, a cost-effective platform for multi-UAV research    using commercial off-the-shelf (COTS) drones. The platform enables researchers to    conduct swarm experiments without expensive custom hardware. Key features include    modular design, easy deployment, and support for common swarm algorithms including    formation control and task allocation. ingested: 2026-07-27 ---  # AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones  ## Metadata  | 항목 | 내용 | |------|-----
- [0.232] `raw/papers/drone-sw/jacinto2024-pegasus-simulator.md` — --- title: "Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation" authors:   - Marcelo Jacinto   - João Pinto   - Jay Patrikar   - John Keller   - Rita Cunha   - Sebastian Scherer   - António Pascoal venue: "IEEE ICUAS 2024" year: 2024 doi: "10.1109/ICUAS60882.2024.10556959" arxiv: "10.48550/arXiv.2307.05263" url: "https://arxiv.org/abs/2307.05263" pdf: "https://arxiv.org/pdf/2307.05263" topics: [drone-sw, swarm, simulation, px4, ros2, isaac-sim] abstract: |   Developing and testing novel control and motion planning algorithms for aerial    vehicles can be a challenging task, with the robotics community relying more than    ever on 3D simulation technologies to evaluate the performance of new algorithms    in a variety of conditions and environments. In this work, we introduce the    Pegasus Simulator, a modular framework implemented as an NVIDIA Isaac Sim ex
- [0.227] `raw/articles/ros2-devnotes.md` — --- source_url: "file://MasterVault/Drone/ROS/ROS2-DevNotes.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3f7a9c4e8d2b5a7f3c6e9d4b8a2f5c7e1d9a6b3f8c4e7d2a5b9f6c3d8e4a7b2f5" tags: [drone-sw] ---  # ROS2 개발 노트  ## 지원 버전  | 배포판 | EOL | 비고 | |--------|-----|------| | Humble | 2027-05 | LTS, 현재 메인 | | Jazzy | 2029-05 | LTS, 차기 이전 | | Kilted | 2025-12 | Rolling 기반 |  ## 드론 연동 스택  ``` ┌──────────────────────────────────────┐ │          ROS2 Application            │ │  Nav2 │ SLAM │ Planning │ Vision     │ ├──────────────────────────────────────┤ │          MAVROS2 / micro-ROS         │ ├──────────────────────────────────────┤ │          MAVLink / DDS               │ ├──────────────────────────────────────┤ │          PX4 / ArduPilot             │ └──────────────────────────────────────┘ ```  ## PX4 + ROS2 연결  ```bash # PX4 SITL with R

**뉴스 검색 결과**
- [0.288] Efficient Domain-Adaptive Policy Learning via Kernel Representation with Application to Quadrotor Control under Non-Stationary Disturbances — http://arxiv.org/abs/2606.13842v2
- [0.261] VisFly-Lab: Unified Differentiable Framework for First-Order Reinforcement Learning of Quadrotor Control — http://arxiv.org/abs/2603.21123v1
- [0.259] [MATLAB] Scaling Model-Based Design into a Competitive Advantage — https://www.youtube.com/watch?v=5wDuQUSEbJs
- [0.238] A Heuristic Approach for Performance Tuning in RL-based Quadrotor Control via Reward Design and Termination Conditions — http://arxiv.org/abs/2605.19166v1

**그래프 인접 슬러그** (1-hop): `active-sensing-uav-communication`, `ai-knowledge-workflow`, `computer-vision-drone`, `datalink-communication`, `drone-ai-agents`, `drone-safety-failsafe`

### 검색: 딥러닝/뉴럴 네트워크 기반 SLAM 모듈(예: 특징 추출, 깊이 추정, 루프 클로저)이 기존 기하학 기반 SLAM을 얼마나 대체하고 있는가?

**canonical 검색 결과**
- [0.358, cos=0.449] `concepts/lightweight-safe-rl-uav.md` — Lightweight Safe RL for UAV Navigation (slug: `lightweight-safe-rl-uav`, layer: concepts)
  발췌: 밀집 환경에서 안전한 UAV 내비게이션을 위한 경량 안전 강화 학습 프레임워크. 비대칭 및 깊이별 분리 합성곱으로 희소 관측을 충돌 위험 인지 특징으로 인코딩하고, 제약 마르코프 결정 과정과 라그랑주 기반 안전 PPO로 안전성을 보장한다.

## 핵심 개념

### 경량 네트워크
- **Asymmetric Convolutions**: 비대칭 합성곱
- **Depthwise Separable Convolutions**: 깊이별 분리 합성곱
- **Collision-Risk-Aware Features**: 충돌 위험 인지 특징 인코딩

### 안전 메커니즘
- **Constrained MDP**: 제약 마르코프 결정 과정
- **Hierarchical Control Architecture**: 계층적 제어 아키텍처
- **Lagrangian-Based Safe PPO**: 라그랑주 기반 안전 PPO 알고리즘
- **Curriculum Learning**: 커리큘럼 학습으로 훈련 안정성 향상

### 성능
- 다양한 장애물 밀도 및 비행 속도에서 높은 성공률
- 기존 RL 기준선 대비 개선된 안전성 및 효율성
- 경량 온보드 배포 가능

## 관련 페이지

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 객체 검출
- [[drone-safety-failsafe]] — RTL, Geofence 등 안전 장치
- [[rl-quadrotor-tunable-control]] — RL 기반 쿼드로터 제어

## 출처

- Zhang et al., "Lightweight Safe Reinforcement Learning for End-to-End UAV Navigation", arXiv:2607.01794, 2026.
- [0.349, cos=0.397] `concepts/yolo.md` — YOLO (slug: `yolo`, layer: concepts)
  발췌: YOLO는 실시간 객체 검출을 위한 딥러닝 아키텍처이다. 단일 신경망으로 이미지를 한 번만 보고 객체의 위치와 클래스를 동시에 예측하여 빠른 처리 속도를 제공한다.

## 핵심 특징

- **실시간 성능**: 고성능 GPU에서 30~140 FPS 이상 처리
- **단일 단계 검출**: 영역 제안과 분류를 동시에 수행
- **높은 정확도**: COCO 데이터셋에서 우수한 mAP 성능

## 최신 릴리스: Ultralytics v8.4.110 (2026-07-29)

### 주요 변경사항

- **RKNN 내보기 확장**: Rockchip NPU 하드웨어에서 모든 YOLO 태스크 지원
  - 객체 검출, 인스턴스 분할, 분류, 포즈 추정
  - 방향 경계 상자(OBB), 시맨틱 분할, 깊이 추정
- **텐서 기반 플로팅 개선**: GPU 메모리 상에서 마스크 합성 수행, CPU 전송 최소화

## 드론 응용

- **임무 중 객체 검출**: [[computer-vision-drone]]에서 실시간 타겟 인식
- **장애물 회피**: [[drone-ai-agents]]의 자율 비행 시스템
- **페이로드 통합**: [[drone-payload-systems]]의 카메라와 연동

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
- [[opencv]] — YOLO 모델 배포에 사용되는 컴퓨터 비전 라이브러리
- [[drone-ai-agents]] — AI 기반 자율 드론 시스템
- [0.343, cos=0.423] `concepts/emnn-doa-estimation.md` — Electromagnetic Neural Network for DOA Estimation (slug: `emnn-doa-estimation`, layer: concepts)
  발췌: UAV 통신 시스템의 빔포밍을 위한 전자기 신경망(EMNN) 기반 도달 각도(DOA) 추정. 진폭 관측만으로 각도 스펙트럼을 생성하는 저전력 고속 처리 아키텍처.

## 시스템 구성

### 1. Stacked Intelligent Metasurfaces (SIM)
- UAV에 장착된 다층 메타표면
- 각 메타원자가 전자기 도메인에서 신호 처리
- 저에넥지 소비 및 초고속 연산

### 2. 완전 연결 계층
- 수신된 진폭 신호 처리
- EMNN의 비선형 추출 및 표현 능력 향상

## 계층적 DOA 추정 프레임워크

| 단계 | 기능 | 목표 |
|------|------|------|
| 1단계 | Coarse DOA 추정 | 대략적 각도 범위 |
| 2단계 | Fine DOA 추정 | 고해상도 정밀 각도 |

## 성능 개선

- **분류 오류 감소**: 기존 CBF 대비 약 13 dB 개선
- **듀얼 신호 시나리오**: 복수 신호 환경에서 우수한 성능
- **비용 효율성**: 낮은 하드웨어 비용 및 RF 전력 소비

## 응용 분야

- UAV 간 통신 빔포밍
- 방향성 안테나 제어
- 간섭 회피 및 신호 품질 향상

## 관련 페이지

- [[stacked-intelligent-metasurfaces]] — SIM 기반 UAV 통신
- [[datalink-communication]] — 드론 데이터링크 통신 기술
- [[drone-ai-agents]] — AI 기반 자율 시스템
- [0.341, cos=0.458] `concepts/federated-lightweight-intrusion-detection.md` — Federated Lightweight Intrusion Detection in Drone Swarms (slug: `federated-lightweight-intrusion-detection`, layer: concepts)
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
- [0.337, cos=0.414] `concepts/flight-ready-lidar-inertial-odometry.md` — Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms (slug: `flight-ready-lidar-inertial-odometry`, layer: concepts)
  발췌: 실시간 폐쇄 루프 항공 제어에 최적화된 LiDAR-관성 오도메트리(LIO) 시스템. IESKF 기반 LIO의 아키텍처 결함을 해결하여 임베디드 드론 플랫폼에서 실제 비행 준비 상태를 달성한다.

## 기존 LIO의 아키텍처 결함

| 결함 | 문제점 |
|------|--------|
| LiDAR 레이트에 묶인 오도메트리 발행 | 10 Hz (IMU 200 Hz 대비) |
| 누락된 속도 출력 | 완전한 상태 벡터 부재 |
| 실행 병목 현상 | IMU 처리 차단 |
| 뮤텍스 경쟁 | 동기화 문제 |
| 동기화 경쟁 조건 | 데이터 일관성 문제 |

## 개선 사항

### 1. IMU 레이트 전파 (IMU-rate Forward Propagation)
- 오도메트리 출력: ~10 Hz → 안정적인 200 Hz
- 모든 IMU 샘플에서 완전한 Twist 상태 제공

### 2. 직접 바디 프레임 속도 발행
- 완전한 상태 벡터 (위치 + 속도) 출력

### 3. SLERP 기반 스무딩
- LiDAR 손실 시에도 연속성 유지

### 4. 듀얼 실행기 격리
- 실행 병목 현상 제거

### 5. 명시적 동기화 보호
- 뮤텍스 경쟁 및 경쟁 조건 방지

## 검증

- **플랫폼**: Livox Mid-360 / Pixhawk 4 Mini 자율 UAV
- **그라운드 트루스**: 모션 캡처 시스템
- **결과**: 실시간 제어 요구사항 충족 확인

## 적용 가능성

기본 추정기(IESKF + ikd-Tree)를 변경하지 않으므로, FAST-LIO2 파생 구현체에 직접 적용 가능하다.

## 관련 페이지

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 SLAM
- [[px4-offboard-control]] — PX4 오프보드 제어
- [[drone-si

**raw 검색 결과**
- [0.371] `raw/papers/drone-ai/shapira2025-icdnet.md` — --- title: "ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM" authors:   - Tali Orlev Shapira   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2512.00037" url: "https://arxiv.org/abs/2512.00037" pdf: "https://arxiv.org/pdf/2512.00037" topics: [drone-ai, slam, visual-inertial, deep-learning, computer-vision] abstract: |   This paper introduces ICD-Net, a deep learning-based approach for visual-inertial    SLAM in drones. The method uses inertial covariance displacement networks to improve    state estimation accuracy in challenging environments. The network learns to predict    covariance matrices for inertial measurements, enabling better fusion with visual    observations. ingested: 2026-07-27 ---  # ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM  ## Metadata  | 항목 | 내용 | |------|------| | **저자** | Tali Orlev Sh
- [0.318] `raw/papers/drone-hw/danial2025-microdrone-slam.md` — --- title: "Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors" authors:   - Jeryes Danial   - Yosi Ben Asher   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2511.14335" url: "https://arxiv.org/abs/2511.14335" pdf: "https://arxiv.org/pdf/2511.14335" topics: [drone-ai, drone-hw, micro-drone, slam, monocular, imu] abstract: |   This paper presents a SLAM system for micro drones using only a monocular camera and    inertial sensors. The system achieves simultaneous localization and 3D semi-dense mapping    suitable for resource-constrained micro aerial vehicles. The approach demonstrates that    accurate SLAM is possible on micro drones without stereo cameras or depth sensors. ingested: 2026-07-27 ---  # Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors  ##
- [0.281] `raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md` — --- title: "UAV-assisted Visual SLAM Generating Reconstructed 3D Scene Graphs in GPS-denied Environments" authors:   - Ahmed Radwan   - Ali Tourani   - Hriday Bavle   - Holger Voos   - Jose Luis Sanchez-Lopez venue: "IEEE ICUAS 2024" year: 2024 arxiv: "2402.07537" doi: "10.1109/ICUAS60882.2024.10556948" url: "https://arxiv.org/abs/2402.07537" pdf: "https://arxiv.org/pdf/2402.07537" topics: [drone-ai, slam, 3d-reconstruction, gps-denied, computer-vision] abstract: |   This paper presents a UAV-assisted visual SLAM system that generates reconstructed    3D scene graphs in GPS-denied environments. The system enables autonomous navigation    and mapping without relying on GPS signals, making it suitable for indoor and denied    environments. The approach combines visual SLAM with 3D reconstruction to build    semantic scene graphs. ingested: 2026-07-27 ---  # UAV-assisted Visual SLAM Generat
- [0.254] `raw/papers/drone-sw/jacinto2024-pegasus-simulator.md` — --- title: "Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation" authors:   - Marcelo Jacinto   - João Pinto   - Jay Patrikar   - John Keller   - Rita Cunha   - Sebastian Scherer   - António Pascoal venue: "IEEE ICUAS 2024" year: 2024 doi: "10.1109/ICUAS60882.2024.10556959" arxiv: "10.48550/arXiv.2307.05263" url: "https://arxiv.org/abs/2307.05263" pdf: "https://arxiv.org/pdf/2307.05263" topics: [drone-sw, swarm, simulation, px4, ros2, isaac-sim] abstract: |   Developing and testing novel control and motion planning algorithms for aerial    vehicles can be a challenging task, with the robotics community relying more than    ever on 3D simulation technologies to evaluate the performance of new algorithms    in a variety of conditions and environments. In this work, we introduce the    Pegasus Simulator, a modular framework implemented as an NVIDIA Isaac Sim ex
- [0.253] `raw/articles/entity-px4-flight-stack.md` — --- title: "PX4 Flight Stack — Entity Reference" created: 2026-07-28 captured: 2026-07-28 type: article url: "https://docs.px4.io/main/en/" author: "PX4 Dev Team / Master" sha256: "" tags: [drone-sw] ---  # PX4 Flight Stack — Entity Reference  ## 개요  PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다. 픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.  - **공식 레포**: https://github.com/PX4/PX4-Autopilot - **최신 안정 버전**: v1.15.x (2024 기준) - **라이선스**: BSD 3-Clause - **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)  ## 핵심 모듈 (Entity)  | 모듈 | 역할 | uORB 토픽 | |---|---|---| | `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` | | `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` | | `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` | | `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`,

**뉴스 검색 결과**
- [0.255] Efficient Domain-Adaptive Policy Learning via Kernel Representation with Application to Quadrotor Control under Non-Stationary Disturbances — http://arxiv.org/abs/2606.13842v2
- [0.249] VisFly-Lab: Unified Differentiable Framework for First-Order Reinforcement Learning of Quadrotor Control — http://arxiv.org/abs/2603.21123v1
- [0.241] [MATLAB] Scaling Model-Based Design into a Competitive Advantage — https://www.youtube.com/watch?v=5wDuQUSEbJs
- [0.238] SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors — http://arxiv.org/abs/2606.23444v2

**그래프 인접 슬러그** (1-hop): `chained-attacks-drone-fl`, `computer-vision-drone`, `datalink-communication`, `drone-ai-agents`, `drone-payload-systems`, `drone-safety-failsafe`

### 검색: 마이크로드론 SLAM 연구에서 GPS 미수신(실내·협소 공간) 환경에 특화된 기법들의 공통적 특징은 무엇인가?

**canonical 검색 결과**
- [0.357, cos=0.441] `concepts/decentralized-swarm-gps-denied.md` — Decentralized UAV Swarms in GPS/Communication-Denied Environments (slug: `decentralized-swarm-gps-denied`, layer: concepts)
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
- [0.328, cos=0.393] `concepts/rtk-gps-precise-landing.md` — RTK GPS & Precise Landing (slug: `rtk-gps-precise-landing`, layer: concepts)
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
- [0.311, cos=0.468] `concepts/uav-swarm-target-localization.md` — UAV Swarm Target Localization via Detection-Aided Enhanced Reweighted Atomic Norm Minimization (slug: `uav-swarm-target-localization`, layer: concepts)
  발췌: 다중경로 환경에서 UAV 스웜을 이용한 표적 위치 추정을 위한 검출 보조 강화 재가중 원자 노름 최소화 방법.

## 개요

Signal Processing 저널에 게시된 연구로, 다중경로 환경에서 UAV 스웜을 활용한 표적 위치 추정 기법을 제안함.

## 연구 정보

- **저자**: Lv Fan, Zhang Xiaokuan, Zheng Shuyu, Li Ninghui, Gong Jian
- **저널**: Signal Processing
- **발행**: 2027-2
- **DOI**: 10.1016/j.sigpro.2026.110848

## 기술적 접근

- **다중경로 환경**: 신호 반사 및 산란이 존재하는 복잡한 환경
- **UAV 스웜**: 다수 드론을 활용한 협력적 위치 추정
- **원자 노름 최소화**: 희소 신호 복원 기법

## 관련 페이지

- [[swarm-coordination]] — 스웜 협업 및 조정
- [[decentralized-swarm-gps-denied]] — GPS 차단 환경 분산형 스웜
- [[uav-isac-cross-region]] — ISAC 교차 지역 협력
- [0.277, cos=0.359] `concepts/visual-positioning-odometry.md` — Visual Positioning & Odometry (slug: `visual-positioning-odometry`, layer: concepts)
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
- [0.265, cos=0.39] `concepts/mars-dragonfly-modular-aerial.md` — MARS-Dragonfly Modular Aerial Robot Systems (slug: `mars-dragonfly-modular-aerial`, layer: concepts)
  발췌: 재구성 가능한 연결 형태를 가진 다중 드론 단위로 구성된 모듈형 항공 로봇 시스템(MARS). 수동 도킹, 감지 없는 수동 잠금, 자기 보조 분리를 위한 컴팩트한 기계 시스템과 예측 할당 파이프라인을 통해 안정적인 비행 및 운송을 달성한다.

## 핵심 개념

### 기계 시스템
- **Passive Docking**: 수동 도킹 메커니즘
- **Detection-Free Passive Locking**: 감지 없는 수동 잠금
- **Magnetic-Assisted Separation**: 자기 보조 분리 (단일 마이크로 서보 사용)

### 가상 쿼드로터 추상화
- **Force-Torque-Equivalent**: 힘-토크 등가 모델
- **Polytope Constraint**: 다면체 제약을 명시적으로 모델링
- **Feasible Wrench Sets**: 실행 가능한 렌치 집합 포착

### 2단계 예측 할당 파이프라인
1. **Constrained Predictive Tracker**: 힘/토크 경계를 존중하는 가상 입력 계산
2. **Dynamic Allocator**: 균형 목표로 개별 모듈에 입력 매핑

### 성능
- 40도 피크 피치에서 민첩한 비행
- 평균 위치 오차: 0.0896m
- 10개 이상 구성에서 시뮬레이션 검증
- 실제 로봇 실험 완료

## 관련 페이지

- [[swarm-coordination]] — 군집 드론 운용 모드 및 편대 비행
- [[drone-hw]] — 드론 하드웨어 구성요소
- [[flight-controller-hardware]] — 비행 제어기 및 GPS

## 출처

- Huang et al., "MARS-Dragonfly: Agile and Robust Flight Control of Modular Aerial Robot S

**raw 검색 결과**
- [0.28] `raw/papers/drone-hw/danial2025-microdrone-slam.md` — --- title: "Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors" authors:   - Jeryes Danial   - Yosi Ben Asher   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2511.14335" url: "https://arxiv.org/abs/2511.14335" pdf: "https://arxiv.org/pdf/2511.14335" topics: [drone-ai, drone-hw, micro-drone, slam, monocular, imu] abstract: |   This paper presents a SLAM system for micro drones using only a monocular camera and    inertial sensors. The system achieves simultaneous localization and 3D semi-dense mapping    suitable for resource-constrained micro aerial vehicles. The approach demonstrates that    accurate SLAM is possible on micro drones without stereo cameras or depth sensors. ingested: 2026-07-27 ---  # Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors  ##
- [0.26] `raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md` — --- title: "UAV-assisted Visual SLAM Generating Reconstructed 3D Scene Graphs in GPS-denied Environments" authors:   - Ahmed Radwan   - Ali Tourani   - Hriday Bavle   - Holger Voos   - Jose Luis Sanchez-Lopez venue: "IEEE ICUAS 2024" year: 2024 arxiv: "2402.07537" doi: "10.1109/ICUAS60882.2024.10556948" url: "https://arxiv.org/abs/2402.07537" pdf: "https://arxiv.org/pdf/2402.07537" topics: [drone-ai, slam, 3d-reconstruction, gps-denied, computer-vision] abstract: |   This paper presents a UAV-assisted visual SLAM system that generates reconstructed    3D scene graphs in GPS-denied environments. The system enables autonomous navigation    and mapping without relying on GPS signals, making it suitable for indoor and denied    environments. The approach combines visual SLAM with 3D reconstruction to build    semantic scene graphs. ingested: 2026-07-27 ---  # UAV-assisted Visual SLAM Generat
- [0.25] `raw/articles/mastervault-recon-swarm.md` — --- source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2" tags: [swarm, drone-ai, drone] ---  # 지능형 자율 군집정찰드론  ## 프로젝트 개요  - **목표**: 학술연구 기반 자율 군집정찰 시스템 - **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041) - **펌웨어**: ArduPilot (커스텀)  ## 4단계 로드맵  | 단계 | 내용 | 상태 | |:----:|------|:----:| | 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 | | 2 | 2기 편대비행 + 통신 검증 | 계획 | | 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 | | 4 | GPS-denied + 실내 군집 | 계획 |  ## 센서 스택  | 센서 | 용도 | 인터페이스 | |------|------|-----------| | LiDAR | 장애물 감지/매핑 | UART/I2C | | 카메라 (RGB) | 정찰/객체 인식 | CSI/USB | | Radar | 전방위 감지 | SPI | | Optical Flow | GPS-denied 위치추정 | I2C | | RTK GPS | 정밀 위치 | UART |  ## 안전 시스템  - Geofence (하드웨어+소프트웨어 이중) - 배터리 페일세이프 (자동 RTL) - 통신 두절 대응 (독립 귀환) - 충돌 회피
- [0.236] `raw/articles/mastervault-px4-devnotes.md` — --- source_url: "file://MasterVault/Drone/PX4/PX4-DevNotes.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "6d0i2f5h8g1b4e7f0a3d6e9c2f5a8d1e4f7a9b2c5d8e1f4a7b9c2d5e8f1a4b7" tags: [drone-sw] ---  # PX4 개발 노트  ## 핵심 아키텍처  ``` ┌──────────────────────────────────────────┐ │              Applications                │ │  Commander │ Navigator │ MC_Control      │ ├──────────────────────────────────────────┤ │              uORB (메시지 버스)           │ ├──────────────────────────────────────────┤ │              Middleware                   │ │  EKF2 │ Sensors │ MAVLink │ Logger       │ ├──────────────────────────────────────────┤ │              Drivers                     │ │  IMU │ Baro │ GPS │ RC │ PWM            │ ├──────────────────────────────────────────┤ │              NuttX RTOS                  │ └────────────────────────────────────
- [0.226] `raw/articles/ros2-devnotes.md` — --- source_url: "file://MasterVault/Drone/ROS/ROS2-DevNotes.md" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "Master (personal dev notes)" sha256: "3f7a9c4e8d2b5a7f3c6e9d4b8a2f5c7e1d9a6b3f8c4e7d2a5b9f6c3d8e4a7b2f5" tags: [drone-sw] ---  # ROS2 개발 노트  ## 지원 버전  | 배포판 | EOL | 비고 | |--------|-----|------| | Humble | 2027-05 | LTS, 현재 메인 | | Jazzy | 2029-05 | LTS, 차기 이전 | | Kilted | 2025-12 | Rolling 기반 |  ## 드론 연동 스택  ``` ┌──────────────────────────────────────┐ │          ROS2 Application            │ │  Nav2 │ SLAM │ Planning │ Vision     │ ├──────────────────────────────────────┤ │          MAVROS2 / micro-ROS         │ ├──────────────────────────────────────┤ │          MAVLink / DDS               │ ├──────────────────────────────────────┤ │          PX4 / ArduPilot             │ └──────────────────────────────────────┘ ```  ## PX4 + ROS2 연결  ```bash # PX4 SITL with R

**뉴스 검색 결과**
- [0.269] Vertical Pinching Antenna Systems (V-PAS) Aided UAV Communications — http://arxiv.org/abs/2607.23184v1
- [0.252] Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments — http://arxiv.org/abs/2607.20710v1
- [0.244] Measurement-Based Characterization and Statistical Modeling of 6G Urban Low-Altitude A2G Channels across FR1 and FR3 — http://arxiv.org/abs/2607.00541v1
- [0.236] OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos — http://arxiv.org/abs/2606.25245v2

**그래프 인접 슬러그** (1-hop): `computer-vision-drone`, `datalink-communication`, `drone-ai-agents`, `drone-hw`, `flight-controller-hardware`, `mission-planning`

### 검색: SLAM의 정확도-지연시간(latency) 트레이드오프를 다루는 문서들에서 공통적으로 제시하는 최적화 전략은 무엇인가?

**canonical 검색 결과**
- [0.265, cos=0.386] `concepts/distributed-aerial-surveillance-swarm.md` — Distributed Continuous Aerial Surveillance by UAS Swarms (slug: `distributed-aerial-surveillance-swarm`, layer: concepts)
  발췌: 경계 Linear Temporal Logic(LTL) 미션 사양 하에서 분산 지속적 공중 감시를 위한 프레임워크. 다중 무인 항공 시스템(UAS)의 분산 협업과 연속적인 팀 재구성을 다룬다.

## 핵심 개념

### 시스템 아키텍처
- **정지 앵커(Stationary Anchors)**: 기준점 역할 수행
- **모바일 워커(Mobile Workers)**: 순환 교체 모드로 운용
- **DNN 기반 통신 토폴로지**: 완전 분산 협업 가능

### 미션 사양 (Bounded LTL)

| 사양 항목 | 설명 |
|-----------|------|
| 모드 간 참조 일관성 | 모드 전환 시 상태 유지 |
| 순환 팀 순환 | 주기적인 드론 교체 |
| 유한 시간 도달성 | 목표 지점 도달 보장 |
| 궤적 추적 | 계획된 경로 추적 |
| 감시 범위 | 처방된 감시 커버리지 |

## 정보 이론적 최적화

Kullback-Leibler 발산 최소화를 통한 감시 노드 분포와 유도된 커버리지 밀도 간 차이 최소화:

```
min KL(P_surveillance || P_coverage)
```

## 기술적 특징

- **온라인 통신 그래프 최적화 불필요**: 모드 종속적 결정론적 통신 토폴로지
- **분산 쿼드로터 컨트롤러**: 로컬 통신만으로 분산 참조 실현
- **유한 시간 수렴 보장**: 워커 에이전트 협업 역학의 수렴성 증명

## 검증 결과

- 순환 팀 재구성 시뮬레이션
- 분산 통신 토폴로지 합성
- 유한 시간 포메이션 수렴
- 인증된 지속적 감시 커버리지

## 관련 페이지

- [[swarm-coordination]] — 스웜 협업 및 편대 비행
- [[recon-swarm-project]] — 지능형 자율 군집정찰드론 프로젝트
- [[drone-simulatio
- [0.254, cos=0.424] `concepts/ai-knowledge-workflow.md` — AI 지식 워크플로 (slug: `ai-knowledge-workflow`, layer: concepts)
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
- [0.246, cos=0.41] `concepts/research-feedback-loop.md` — 연구 피드백 루프 (slug: `research-feedback-loop`, layer: concepts)
  발췌: 연구 피드백 루프는 원본 수집, 위키 컴파일, 그래프 분석, 집중 합성의 결과가 다시 지식베이스로 돌아오는 반복 구조다.

## 순환 구조

1. 원본과 서지정보를 확보한다.
2. [[llm-wiki]]에서 개념·비교·질의 문서로 컴파일한다.
3. 지식그래프로 브리지·고립·모순 후보를 찾는다.
4. 관련 Markdown과 원본을 제한된 소스 묶음에 모은다.
5. 비판적 질문과 보고서로 가설을 검토한다.
6. 검증된 결과만 출처와 함께 위키에 다시 편입한다.

이 루프의 목표는 산출물 수를 늘리는 것이 아니라 “왜 이 관계가 중요한가”를 반복 검증하는 것이다. NotebookLM의 답변이나 그래프의 연결은 중간 가설이며, 원본을 확인한 뒤에만 장기 지식으로 승격한다. ^[raw/notebooklm/2026-07-16-all-notes.md]

## 환류 가능한 형식

- Markdown 보고서와 질의 결과
- JSON 마인드맵과 지식그래프
- CSV 비교표
- PDF·프레젠테이션·이미지 산출물

장기 보관할 핵심 내용은 공개 형식의 Markdown과 출처 경로로 환원한다. NotebookLM 합성 결과의 증분 편입은 [[notebooklm-query-compounding]], 지식그래프 생성과 재분석은 [[ua-knowledge-graph-workflow]]를 따른다.

이 루프는 [[ai-knowledge-workflow]]의 일회성 단계에 “검증 결과를 다시 입력으로 사용하는” 반복성을 더한다. ^[raw/notebooklm/notebooklm-py-github.md]
- [0.246, cos=0.354] `queries/notebooklm-query-compounding.md` — NotebookLM 질의 지식 증분 워크플로 (slug: `notebooklm-query-compounding`, layer: queries)
  발췌: ## 질의

NotebookLM 질의응답에서 원본 대화 전문을 별도로 저장하지 않으면서, 재사용 가능한 지식만 `queries/`에 편입해 개인 지식베이스를 증분시키려면 어떻게 운영해야 하는가?

## 핵심 결론

NotebookLM 답변은 일시적인 합성 결과이고 `queries/` 문서는 검토를 통과한 장기 지식이다. 두 계층을 구분하되 원본 Q&A 파일은 만들지 않는다.

답변의 가치와 근거를 평가한 뒤 하나의 canonical query 문서만 생성하거나 갱신하고, 실제 raw source와 NotebookLM 대화 식별자를 기록한다. ^[raw/notebooklm/notebooklm-py-github.md]

    NotebookLM 질의
      → JSON 답변과 source ID 확보
      → 저장 가치 판정
      → 기존 위키 문서 검색
      → 근거·사실 교차검증
      → canonical query 생성 또는 갱신
      → index·log·역링크 갱신
      → lint

## 저장 대상 판정

다시 도출하기 어렵고 반복 활용할 수 있는 다음 결과만 저장한다.

- 여러 source를 결합한 비교와 종합
- 반복 가능한 연구·개발 워크플로
- 장기적으로 적용할 의사결정 기준
- 연구 가설, 지식 공백과 검증 계획
- 기존 문서 여러 개를 새롭게 연결하는 분석
- 오류와 제약까지 검토된 심층 설명

단순 명령어, 상태 조회, 기존 페이지와 중복되는 설명, 근거가 불명확한 답변은 저장하지 않는다. 답변 길이가 아니라 가치·검증 가능성·재사용성이 기준이다.

## 출처 매핑

NotebookLM 응답의 source ID는 로컬 `raw/**/*.md`의 `notebooklm_source_id`와 연결한다. UUID가 일치하는 파일만 qu
- [0.236, cos=0.394] `concepts/rl-quadrotor-tunable-control.md` — RL-Based Quadrotor Control with Tunable Performance (slug: `rl-quadrotor-tunable-control`, layer: concepts)
  발췌: 보상 설계와 종료 조건을 통한 RL 기반 쿼드로터 제어의 성능 튜닝 방법론. PPO(Proximal Policy Optimization) 알고리즘과 이중 대역폭 지수 보상 구조를 활용하여 임계 감쇠 응답 기준선을 달성하고, 직관적인 휴리스틱 규칙으로 빠른(곡예) 및 느린(검사) 정착 시간 성능을 조정한다.

## 핵심 개념

### 보상 구조
- **Dual Bandwidth Exponentials**: 임계 감쇠 응답을 달성하는 새로운 보상 구조
- **Setpoint Tracking**: 낮은 정상 상태 오차(~2%) 달성
- **Episode Truncation**: 600만 시간 단계 내 샘플 효율적 학습

### 성능 모드
- **Baseline**: 임계 감쇠 응답, 정상 상태 오차 ~2%
- **Acrobatic**: 빠른 정착 시간, 곡예 비행 성능
- **Inspection**: 느린 정착 시간, 정밀 검사 성능

## 응용 분야

- 인프라 검사 (정밀 제어 필요)
- 드론 레이싱 (속도와 민첩성)
- 숲 상공 검사 (Under-canopy forest inspection)

## 관련 페이지

- [[px4-flight-modes]] — PX4 자동조종장치 비행 모드 분류
- [[drone-simulation]] — Gazebo, SITL 기반 시뮬레이션
- [[ros2-drone-integration]] — ROS2 기반 드론 연동 스택

## 출처

- Lagos Suarez et al., "A Heuristic Approach for Performance Tuning in RL-based Quadrotor Control via Reward Design and Termination Conditions", arXiv:2605.19166, 2026.
- Lagos 

**raw 검색 결과**
- [0.218] `raw/papers/datalink/koubaa2019-mavlink-survey.md` — --- title: "Micro Air Vehicle Link (MAVLink) in a Nutshell: A Survey" authors:   - Anis Koubaa   - Azza Allouch   - Maram Alajlan   - Yasir Javed   - Abdelfettah Belghith   - Mohamed Khalgui venue: "IEEE Access" year: 2019 doi: "10.1109/ACCESS.2019.2924350" arxiv: "1906.10641" url: "https://arxiv.org/abs/1906.10641" pdf: "https://arxiv.org/pdf/1906.10641" topics: [datalink, mavlink, communication, survey, px4, ardupilot] abstract: |   This paper provides a comprehensive survey of the Micro Air Vehicle Link (MAVLink)    protocol, which is widely used for communication between unmanned aerial vehicles (UAVs)    and ground control stations. MAVLink is a lightweight messaging protocol that is designed    for resource-constrained systems. It supports both PX4 and ArduPilot autopilot systems    and has become the de facto standard for drone communication. The paper covers the    protocol archi
- [0.206] `raw/papers/drone-ai/shapira2025-icdnet.md` — --- title: "ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM" authors:   - Tali Orlev Shapira   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2512.00037" url: "https://arxiv.org/abs/2512.00037" pdf: "https://arxiv.org/pdf/2512.00037" topics: [drone-ai, slam, visual-inertial, deep-learning, computer-vision] abstract: |   This paper introduces ICD-Net, a deep learning-based approach for visual-inertial    SLAM in drones. The method uses inertial covariance displacement networks to improve    state estimation accuracy in challenging environments. The network learns to predict    covariance matrices for inertial measurements, enabling better fusion with visual    observations. ingested: 2026-07-27 ---  # ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM  ## Metadata  | 항목 | 내용 | |------|------| | **저자** | Tali Orlev Sh
- [0.142] `raw/articles/px4-basic-concepts.md` — --- source_url: "https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html" ingested: 2026-07-27 captured: 2026-07-27 type: article author: "PX4 Dev Team" sha256: "8e3d7c2f5a9b4e8d1c6f3a7b2e5d9c4f8a3b7e2d5f9c3a6b8e2d7f4c9a3b6e1" tags: [drone, drone-sw] ---  # Basic Concepts - PX4 Guide  ## Overview  This article introduces fundamental drone and PX4 autopilot concepts for users new to unmanned vehicles.  ## What is a Drone?  A drone, or Unmanned Vehicle (UV), is an unmanned robotic vehicle controllable manually or autonomously. These systems operate across multiple environments—air, ground, water surfaces, and underwater—serving applications including aerial photography, cargo transport, racing, search operations, and surveying.  The broader term "Unmanned Aerial System (UAS)" encompasses a UAV plus all supporting components: ground control stations, radio controllers, and data

**뉴스 검색 결과**
- [0.252] [MATLAB] Scaling Model-Based Design into a Competitive Advantage — https://www.youtube.com/watch?v=5wDuQUSEbJs
- [0.237] 드론이 흔든 전장, 방산 돈줄도 바꿨다…M&A·투자 경쟁 가열 — https://news.google.com/rss/articles/CBMiT0FVX3lxTE9vZ1NkbkxhdEVyZC1qZHd6S2lwdUd6cXpIUE1tTHNoeUplUUJIcG00RlhZMU0wS3hYRGJ4UlRVVWVPcmZNYkxaMC1ta3VjeGc?oc=5
- [0.233] A Heuristic Approach for Performance Tuning in RL-based Quadrotor Control via Reward Design and Termination Conditions — http://arxiv.org/abs/2605.19166v1
- [0.223] Stop Chasing the Shiny Object: Focus First on a Comprehensive Counter-UAS Training Program — https://news.google.com/rss/articles/CBMiekFVX3lxTE5MeWtGdWJIQldyUnYteFo4WUhPNU0zOXhnNFR4cktSaFgtSGtkWVJvZERxcU9ZeFpwYVlUVDdyZkVFajU3YUdwWlJKaHNWUU4wT1RQYXVlYzhnVGIyUk9CSFVoNll5Zlg2UkdwWEc4TlFZalNEWUdvSTRR?oc=5

**그래프 인접 슬러그** (1-hop): `ai-personal-knowledge-management`, `drone-simulation`, `e2e-fly-end-to-end-quadrotor`, `knowledge-tool-roles`, `lightweight-safe-rl-uav`, `llm-wiki`

### 검색: 최근(raw/뉴스성) 자료에서 언급되는 마이크로드론 SLAM 관련 신규 프레임워크나 오픈소스 도구의 등장 동향은 어떠한가?

**canonical 검색 결과**
- [0.375, cos=0.492] `concepts/opencv.md` — OpenCV (slug: `opencv`, layer: concepts)
  발췌: OpenCV(Open Source Computer Vision Library)은 실시간 컴퓨터 비전을 위한 오픈소스 라이브러리이다. 드론 분야에서는 객체 인식, 추적, SLAM, 이미지 처리 등 다양한 AI 응용에 활용된다.

## 핵심 기능

- **이미지/비디오 처리**: 필터링, 변환, 형태학적 연산
- **객체 검출**: Haar Cascade, HOG, 딥러닝 기반 검출
- **특징점 추출**: SIFT, SURF, ORB 등
- **카메라 캘리브레이션**: 렌즈 왜곡 보정, 스테레오 비전

## 최신 릴리스: OpenCV 5.0.0 (2026-06-06)

2026년 6월 6일 출시된 OpenCV 5.0.0은 메이저 버전 업그레이드이다:

- 4.x에서 5.x로의 마이그레이션 가이드 제공
- Android SDK 16KB 페이지 크기 대응 패키지 제공

## 드론 응용

- **객체 추적**: [[computer-vision-drone]]과 연계하여 실시간 타겟 추적
- **비전 기반 내비게이션**: [[drone-ai-agents]]에서 SLAM 및 장애물 회피
- **페이로드 통합**: [[drone-payload-systems]]의 카메라 시스템과 연동

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
- [[yolo]] — OpenCV와 함께 사용되는 객체 검출 모델
- [[ros2-drone-integration]] — OpenCV가 통합되는 ROS2 환경
- [0.326, cos=0.499] `concepts/ai-knowledge-workflow.md` — AI 지식 워크플로 (slug: `ai-knowledge-workflow`, layer: concepts)
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
- [0.321, cos=0.491] `concepts/mavlink-m-interoperability.md` — A New Era of Interoperable Payloads Begins at the Dronecode MAVLink-M Integration Hackathon (slug: `mavlink-m-interoperability`, layer: concepts)
  발췌: Dronecode Foundation의 MAVLink-Military 해커톤에서 14개 미국 및 국제 기업이 48시간 만에 비행 제어기, 페이로드, 지상통제소를 하나의 개방형 표준으로 통합한 사례.

## 개요

2026년 7월 말 버지니아 매너서스에서 열린 Dronecode Foundation MAVLink-M Integration Hackathon에서는 경쟁하는 드론 기업들이 상호운용성 문제를 해결하는 데 성공함. 이는 개방형 표준의 힘을 보여주는 중요한 사례.

## 주요 성과

- **14개 기업 참여**: 미국 및 국제 드론 기업들이 협업
- **48시간 통합**: 짧은 시간 내에 비행 제어기, 페이로드, GCS 통합
- **실제 비행 시연**: 정부 및 산업 관계자들 앞에서 작동하는 데모 비행

## MAVLink-M 표준

MAVLink-M은 군사 및 상업용 드론 간의 상호운용성을 위한 확장 표준. 크로스벤더 플러그앤플레이 페이로드 통합을 목표로 함.

## 관련 페이지

- [[mavlink-protocol]] — MAVLink 프로토콜 개요
- [[mavlink-protocol-deep]] — MAVLink 심층 분석
- [[px4-flight-stack]] — PX4 비행 제어 스택
- [[qgroundcontrol]] — QGroundControl GCS
- [0.312, cos=0.43] `concepts/research-feedback-loop.md` — 연구 피드백 루프 (slug: `research-feedback-loop`, layer: concepts)
  발췌: 연구 피드백 루프는 원본 수집, 위키 컴파일, 그래프 분석, 집중 합성의 결과가 다시 지식베이스로 돌아오는 반복 구조다.

## 순환 구조

1. 원본과 서지정보를 확보한다.
2. [[llm-wiki]]에서 개념·비교·질의 문서로 컴파일한다.
3. 지식그래프로 브리지·고립·모순 후보를 찾는다.
4. 관련 Markdown과 원본을 제한된 소스 묶음에 모은다.
5. 비판적 질문과 보고서로 가설을 검토한다.
6. 검증된 결과만 출처와 함께 위키에 다시 편입한다.

이 루프의 목표는 산출물 수를 늘리는 것이 아니라 “왜 이 관계가 중요한가”를 반복 검증하는 것이다. NotebookLM의 답변이나 그래프의 연결은 중간 가설이며, 원본을 확인한 뒤에만 장기 지식으로 승격한다. ^[raw/notebooklm/2026-07-16-all-notes.md]

## 환류 가능한 형식

- Markdown 보고서와 질의 결과
- JSON 마인드맵과 지식그래프
- CSV 비교표
- PDF·프레젠테이션·이미지 산출물

장기 보관할 핵심 내용은 공개 형식의 Markdown과 출처 경로로 환원한다. NotebookLM 합성 결과의 증분 편입은 [[notebooklm-query-compounding]], 지식그래프 생성과 재분석은 [[ua-knowledge-graph-workflow]]를 따른다.

이 루프는 [[ai-knowledge-workflow]]의 일회성 단계에 “검증 결과를 다시 입력으로 사용하는” 반복성을 더한다. ^[raw/notebooklm/notebooklm-py-github.md]
- [0.308, cos=0.424] `concepts/second-brain-research-workflow.md` — 세컨드 브레인 연구 워크플로 (slug: `second-brain-research-workflow`, layer: concepts)
  발췌: 세컨드 브레인 연구 워크플로는 원본 보존, AI 합성, 개인 해석을 분리하면서 하나의 반복 가능한 연구 환경으로 연결하는 방식이다. 이는 [[ai-personal-knowledge-management]]의 계층 원칙을 연구 자료 수집과 검증에 적용한 구현이다.

## 역할 분담

| 단계 | 역할 | 대표 도구 |
| --- | --- | --- |
| 수집 | 논문·웹 자료와 서지정보 보존 | Zotero, 브라우저 클리퍼 |
| 컴파일 | 재사용할 개념·비교·질의 생성 | LLM Wiki |
| 집중 탐색 | 제한된 소스 묶음 질의 | NotebookLM |
| 구조 분석 | 관계, 군집, 고립 문서 후보 탐색 | Understand Anything |
| 장기 편집 | Markdown과 개인 메모 관리 | Obsidian |

역할을 분리하면 각 도구의 생성 결과가 곧바로 확정 지식이 되는 것을 막고, 원문으로 돌아가는 경로를 유지할 수 있다. ^[raw/notebooklm/llm-wiki-zotero-notebooklm-youtube.md]

## 개인 지식과 외부 지식

외부 원본의 요약과 사용자의 경험·판단을 같은 층에서 섞으면 출처와 의견의 경계가 흐려진다. 원본과 컴파일된 지식은 출처를 유지하고, 개인 메모는 별도 섹션이나 문서로 기록하는 편이 안전하다.

## 성공 조건

- 원문으로 돌아갈 수 있다.
- AI가 만든 주장과 개인 판단을 구분할 수 있다.
- 도구가 바뀌어도 Markdown과 메타데이터가 남는다.
- 새 자료가 기존 지식과 연결되거나 모순으로 표시된다.
- 편입 전후에 스키마와 링크를 자동 검증한다.

전체 운영 절차는 [[ai-knowledge-workflow]], 반복적 개선은 [[research-feedback-loop]], 도구 선택 기준은 [[

**raw 검색 결과**
- [0.26] `raw/papers/drone-hw/danial2025-microdrone-slam.md` — --- title: "Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors" authors:   - Jeryes Danial   - Yosi Ben Asher   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2511.14335" url: "https://arxiv.org/abs/2511.14335" pdf: "https://arxiv.org/pdf/2511.14335" topics: [drone-ai, drone-hw, micro-drone, slam, monocular, imu] abstract: |   This paper presents a SLAM system for micro drones using only a monocular camera and    inertial sensors. The system achieves simultaneous localization and 3D semi-dense mapping    suitable for resource-constrained micro aerial vehicles. The approach demonstrates that    accurate SLAM is possible on micro drones without stereo cameras or depth sensors. ingested: 2026-07-27 ---  # Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors  ##
- [0.256] `raw/papers/datalink/koubaa2019-mavlink-survey.md` — --- title: "Micro Air Vehicle Link (MAVLink) in a Nutshell: A Survey" authors:   - Anis Koubaa   - Azza Allouch   - Maram Alajlan   - Yasir Javed   - Abdelfettah Belghith   - Mohamed Khalgui venue: "IEEE Access" year: 2019 doi: "10.1109/ACCESS.2019.2924350" arxiv: "1906.10641" url: "https://arxiv.org/abs/1906.10641" pdf: "https://arxiv.org/pdf/1906.10641" topics: [datalink, mavlink, communication, survey, px4, ardupilot] abstract: |   This paper provides a comprehensive survey of the Micro Air Vehicle Link (MAVLink)    protocol, which is widely used for communication between unmanned aerial vehicles (UAVs)    and ground control stations. MAVLink is a lightweight messaging protocol that is designed    for resource-constrained systems. It supports both PX4 and ArduPilot autopilot systems    and has become the de facto standard for drone communication. The paper covers the    protocol archi
- [0.248] `raw/papers/drone-ai/shapira2025-icdnet.md` — --- title: "ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM" authors:   - Tali Orlev Shapira   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2512.00037" url: "https://arxiv.org/abs/2512.00037" pdf: "https://arxiv.org/pdf/2512.00037" topics: [drone-ai, slam, visual-inertial, deep-learning, computer-vision] abstract: |   This paper introduces ICD-Net, a deep learning-based approach for visual-inertial    SLAM in drones. The method uses inertial covariance displacement networks to improve    state estimation accuracy in challenging environments. The network learns to predict    covariance matrices for inertial measurements, enabling better fusion with visual    observations. ingested: 2026-07-27 ---  # ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM  ## Metadata  | 항목 | 내용 | |------|------| | **저자** | Tali Orlev Sh
- [0.231] `raw/papers/swarm/li2025-airswarm.md` — --- title: "AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones" authors:   - Xiaowei Li   - Kuan Xu   - Fen Liu   - Ruofei Bai   - Shenghai Yuan   - Lihua Xie venue: "arXiv preprint" year: 2025 arxiv: "2503.06890" url: "https://arxiv.org/abs/2503.06890" pdf: "https://arxiv.org/pdf/2503.06890" topics: [swarm, multi-uav, cots, cost-effective, hardware] abstract: |   This paper presents AirSwarm, a cost-effective platform for multi-UAV research    using commercial off-the-shelf (COTS) drones. The platform enables researchers to    conduct swarm experiments without expensive custom hardware. Key features include    modular design, easy deployment, and support for common swarm algorithms including    formation control and task allocation. ingested: 2026-07-27 ---  # AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones  ## Metadata  | 항목 | 내용 | |------|-----
- [0.227] `raw/papers/datalink/allouch2019-mavsec.md` — --- title: "MAVSec: Securing the MAVLink Protocol for Ardupilot/PX4 Unmanned Aerial Systems" authors:   - Azza Allouch   - Omar Cheikhrouhou   - Anis Koubaa   - Mohamed Khalgui   - Tarek Abbes venue: "IWCMC 2019" year: 2019 arxiv: "1905.00265" url: "https://arxiv.org/abs/1905.00265" pdf: "https://arxiv.org/pdf/1905.00265" topics: [datalink, mavlink, security, encryption, px4, ardupilot] abstract: |   This paper proposes MAVSec, a security protocol specifically designed for MAVLink    to address the critical security vulnerabilities in drone communication systems.    MAVSec provides authentication, integrity, and confidentiality for MAVLink messages    while maintaining the lightweight nature of the protocol. The paper presents a    comprehensive security analysis and implementation evaluation for both PX4 and ArduPilot. ingested: 2026-07-27 ---  # MAVSec: Securing the MAVLink Protocol fo

**뉴스 검색 결과**
- [0.277] 자구책을 통한 방산허브로…스타트업-中企가 대안을 제시하다 — https://news.google.com/rss/articles/CBMiZEFVX3lxTE1QQVFka2s3bzlQWnFoakZUNVdKd1EtMXdoWGN1b0t1aTVPTUtEZFA2bUI2cG1sRWVvNUlRRXNqZXN0SXY0OG1GTV9jeE54ZnZNSXBUWEFHUWVLcFFpUHR0TXZOR0Y?oc=5
- [0.263] [핑크랩 PinkLAB] 핑크랩 PL2M 공개! ROS 2 기반 주행형 양팔로봇 플랫폼 — https://www.youtube.com/watch?v=-i5dSTGDHhI
- [0.254] [PX4 Autopilot - Open Source Flight Control.] A New Era of Interoperable Payloads Begins at the Dronecode MAVLink-M Integration Hackathon — https://www.youtube.com/watch?v=iEzH0dfKRwg
- [0.253] Federated Lightweight Intrusion Detection in Drone Swarms with Knowledge Distillation — http://arxiv.org/abs/2607.17025v1

**그래프 인접 슬러그** (1-hop): `ai-personal-knowledge-management`, `computer-vision-drone`, `drone-ai-agents`, `drone-payload-systems`, `knowledge-tool-roles`, `llm-wiki`

### 검색: 마이크로드론 SLAM 상용화 및 규제(예: 실내 비행 안전기준, 자율비행 인증)와 관련된 동향은 무엇인가?

**canonical 검색 결과**
- [0.459, cos=0.598] `concepts/drone-news-regulations.md` — 드론 규제 동향 2026-07 (slug: `drone-news-regulations`, layer: concepts)
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
- [0.43, cos=0.551] `concepts/dji-easa-sail-bvlos.md` — DJI EASA SAIL BVLOS Approval (slug: `dji-easa-sail-bvlos`, layer: concepts)
  발췌: DJI의 유럽항공안전청(EASA) 특정 종류 비행 승인(SAIL)을 통한 BVLOS(시야 밖) 운용 인증 획득. 유럽 전역 드론 배포를 위한 규제 승인 간소화 노력.

## 배경

유럽에서 드론을 배포하는 기업에게 규제 승인은 기술 자체보다 큰 도전 과제. 현대 드론 플랫폼은 이미 복잡한 BVLOS 미션 수행이 가능하지만, 운용자는 여전히 안전한 비행 입증이 필요.

## DJI의 접근 방식

### SAIL 프레임워크 활용
- **특정 종류 비행 승인(Specific Assurance and Integrity Level)**
- EASA의 위험 기반 승인 체계
- 사전 승인된 운용 프로파일 제공

### 효과
- 운용자의 규제 승인 프로세스 간소화
- 표준화된 안전 입증 프레임워크 제공

## 시사점

- 유럽 BVLOS 드론 시장 확대 가속화
- 타 제조사에 대한 선례 효과
- 규제 승인의 산업 표준화 추진

## 관련 페이지

- [[drone-regulations]] — 드론 규제 개요 (FAA, EASA, 한국)
- [[fcc-drone-regulations]] — FCC 외국 제조 드론 규제 정책
- [[doordash-air]] — DoorDash FAA Part 135 인증 드론 배달
- [0.395, cos=0.547] `entities/doordash-air.md` — DoorDash Air (slug: `doordash-air`, layer: entities)
  발췌: DoorDash의 자체 드론 배달 서비스. 2026년 7월 FAA Part 135 항공운송인증 취득. 미국에서 8번째로 인증받은 드론 운영업체.

## 인증 정보

- **인증**: FAA Part 135 Air Carrier Certificate
- **순위**: 미국 8번째 드론 운영 인증
- **시기**: 2026년 7월

## 사업 모델

- **수직 통합**: 자체 항공기, 인증, 배달 플랫폼 보유
- **Amazon 전략 유사**: 전체 생태계 내 통합
- **서비스명**: DoorDash Air

## 관련 항목

- [[drone-regulations]] — 드론 규제
- [[ops-mission]] — 드론 운용 미션
- [[matternet]] — 드론 배달 기업
- [0.387, cos=0.59] `concepts/fcc-drone-regulations.md` — FCC Drone Regulations (slug: `fcc-drone-regulations`, layer: concepts)
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
- [0.368, cos=0.503] `concepts/drone-news-hardware.md` — 드론 하드웨어 및 제조사 동향 2026-07 (slug: `drone-news-hardware`, layer: concepts)
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

**raw 검색 결과**
- [0.305] `raw/papers/swarm/li2025-airswarm.md` — --- title: "AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones" authors:   - Xiaowei Li   - Kuan Xu   - Fen Liu   - Ruofei Bai   - Shenghai Yuan   - Lihua Xie venue: "arXiv preprint" year: 2025 arxiv: "2503.06890" url: "https://arxiv.org/abs/2503.06890" pdf: "https://arxiv.org/pdf/2503.06890" topics: [swarm, multi-uav, cots, cost-effective, hardware] abstract: |   This paper presents AirSwarm, a cost-effective platform for multi-UAV research    using commercial off-the-shelf (COTS) drones. The platform enables researchers to    conduct swarm experiments without expensive custom hardware. Key features include    modular design, easy deployment, and support for common swarm algorithms including    formation control and task allocation. ingested: 2026-07-27 ---  # AirSwarm: Enabling Cost-Effective Multi-UAV Research with COTS drones  ## Metadata  | 항목 | 내용 | |------|-----
- [0.28] `raw/papers/drone-sw/jacinto2024-pegasus-simulator.md` — --- title: "Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation" authors:   - Marcelo Jacinto   - João Pinto   - Jay Patrikar   - John Keller   - Rita Cunha   - Sebastian Scherer   - António Pascoal venue: "IEEE ICUAS 2024" year: 2024 doi: "10.1109/ICUAS60882.2024.10556959" arxiv: "10.48550/arXiv.2307.05263" url: "https://arxiv.org/abs/2307.05263" pdf: "https://arxiv.org/pdf/2307.05263" topics: [drone-sw, swarm, simulation, px4, ros2, isaac-sim] abstract: |   Developing and testing novel control and motion planning algorithms for aerial    vehicles can be a challenging task, with the robotics community relying more than    ever on 3D simulation technologies to evaluate the performance of new algorithms    in a variety of conditions and environments. In this work, we introduce the    Pegasus Simulator, a modular framework implemented as an NVIDIA Isaac Sim ex
- [0.279] `raw/papers/datalink/koubaa2019-mavlink-survey.md` — --- title: "Micro Air Vehicle Link (MAVLink) in a Nutshell: A Survey" authors:   - Anis Koubaa   - Azza Allouch   - Maram Alajlan   - Yasir Javed   - Abdelfettah Belghith   - Mohamed Khalgui venue: "IEEE Access" year: 2019 doi: "10.1109/ACCESS.2019.2924350" arxiv: "1906.10641" url: "https://arxiv.org/abs/1906.10641" pdf: "https://arxiv.org/pdf/1906.10641" topics: [datalink, mavlink, communication, survey, px4, ardupilot] abstract: |   This paper provides a comprehensive survey of the Micro Air Vehicle Link (MAVLink)    protocol, which is widely used for communication between unmanned aerial vehicles (UAVs)    and ground control stations. MAVLink is a lightweight messaging protocol that is designed    for resource-constrained systems. It supports both PX4 and ArduPilot autopilot systems    and has become the de facto standard for drone communication. The paper covers the    protocol archi
- [0.257] `raw/papers/drone-hw/danial2025-microdrone-slam.md` — --- title: "Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors" authors:   - Jeryes Danial   - Yosi Ben Asher   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2511.14335" url: "https://arxiv.org/abs/2511.14335" pdf: "https://arxiv.org/pdf/2511.14335" topics: [drone-ai, drone-hw, micro-drone, slam, monocular, imu] abstract: |   This paper presents a SLAM system for micro drones using only a monocular camera and    inertial sensors. The system achieves simultaneous localization and 3D semi-dense mapping    suitable for resource-constrained micro aerial vehicles. The approach demonstrates that    accurate SLAM is possible on micro drones without stereo cameras or depth sensors. ingested: 2026-07-27 ---  # Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors  ##
- [0.253] `raw/papers/drone-ai/shapira2025-icdnet.md` — --- title: "ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM" authors:   - Tali Orlev Shapira   - Itzik Klein venue: "arXiv preprint" year: 2025 arxiv: "2512.00037" url: "https://arxiv.org/abs/2512.00037" pdf: "https://arxiv.org/pdf/2512.00037" topics: [drone-ai, slam, visual-inertial, deep-learning, computer-vision] abstract: |   This paper introduces ICD-Net, a deep learning-based approach for visual-inertial    SLAM in drones. The method uses inertial covariance displacement networks to improve    state estimation accuracy in challenging environments. The network learns to predict    covariance matrices for inertial measurements, enabling better fusion with visual    observations. ingested: 2026-07-27 ---  # ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM  ## Metadata  | 항목 | 내용 | |------|------| | **저자** | Tali Orlev Sh

**뉴스 검색 결과**
- [0.36] [미국 특징주] 도어대시, FAA 인증 획득 후 자체 드론 배송 프로그램 출시 — https://news.google.com/rss/articles/CBMiXEFVX3lxTE4xSWIyY3ZJdk1MMFNEVmMwU0gtT1lqSm1rUjhId0VBXzlGM1YtZkdNZkNJZ2p3WlRrNHNERUFBYlNpT3ZFOEItbXdBd2p6WVRudUdscjdWSWFyc0Qz?oc=5
- [0.326] Regulator sets out vision for scaling drone operations across UK airspace — https://www.suasnews.com/2026/07/regulator-sets-out-vision-for-scaling-drone-operations-across-uk-airspace/
- [0.323] DoorDash becomes certified drone airline, signaling delivery’s next chapter — https://dronedj.com/2026/07/31/doordash-air-drone-delivery-launch/
- [0.322] 에스엠벡셀, 배송용 드론 배터리팩 개발…"1000회 비행 검증 완료" — https://news.google.com/rss/articles/CBMic0FVX3lxTE1XS01PUXJXa2Q0Y0R6RFk5UFVOQk0zZmQ1NjhTLThJU21BYWgtN0xrQU1WTHNZTWpwS0tpZUowZTdBZF9OMXpORGdCQmZVN3ltM2lKbTBXczRQMWxKdlAxS3ZQWmpaN2F0MlFBVjRKUFpaWnM?oc=5

**그래프 인접 슬러그** (1-hop): `amazon-mk30-safety-incident`, `drone-hw`, `drone-payload-systems`, `drone-regulations`, `drone-safety-failsafe`, `flight-controller-hardware`

