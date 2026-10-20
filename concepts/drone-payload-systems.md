---
title: Drone Payload Systems
created: 2026-07-27
updated: 2026-10-20
type: concept
tags: [drone-hw, payload, gimbal, camera, gripper]
sources: [raw/articles/px4-basic-concepts.md, raw/articles/px4-hardware-overview.md, inbox/processed/fetch-2026-10-17-arxiv-fam-dq-a-dual-quadrotor-based-fully-actuated-aerial-manipula.md, inbox/processed/fetch-2026-10-17-arxiv-compact-force-sensor-for-dual-uav-cable-suspended-payload-tr.md, inbox/processed/fetch-2026-10-17-arxiv-speech-enhancement-using-ego-noise-references-with-a-microph.md, inbox/processed/fetch-2026-10-18-arxiv-autotrans-a-complete-planning-and-control-framework-for-auto.md, inbox/processed/fetch-2026-10-19-arxiv-an-input-output-feedback-linearization-based-exponentially-s.md, inbox/processed/fetch-2026-10-20-arxiv-autonomous-agricultural-monitoring-with-aerial-drones-and-rf.md]
confidence: high
domain: hardware
contested: false
contradictions: []
---

# Drone Payload Systems

페이로드는 드론의 임무 목표를 달성하는 장비로, 카메라, 센서, 화물 등을 포함한다. PX4는 다양한 페이로드 타입을 자동/수동으로 트리거할 수 있다.^[raw/articles/px4-basic-concepts.md]

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
| **2-axis** | Roll, Pitch |
| **3-axis** | Roll, Pitch, Yaw |

### Gimbal 제어

| 모드 | 설명 |
|------|------|
| **Angle Mode** | 절대 각도 지정 |
| **Rate Mode** | 회전 속도 지정 |
| **Follow Mode** | 기체 움직임 추적 |
| **Lock Mode** | 지향 각도 고정 |

### MAVLink Gimbal Protocol v2

```
GIMBAL_DEVICE_SET_ATTITUDE
- Target system/component
- Quaternion (attitude)
- Angular velocity
- Flags
```

## Gripper / Cargo

화물 파지 및 배달 시스템.

### Gripper MAVLink

```
MAV_CMD_DO_GRIPPER
- Param 1: Gripper ID
- Param 2: Action (0=release, 1=grab)
```

### 배달 미션 예시

```
1. TAKEOFF
2. WAYPOINT (배달 지점)
3. DO_GRIPPER (release)
4. RTL
```

## Parachute Systems

비상 상황에서 기체를 보호하는 낙하산.

### 작동 조건

| 조건 | 설명 |
|------|------|
| **Manual** | RC 스위치 또는 GCS 명령 |
| **Critical Failure** | 자동 감지 (자이로, 가속도) |
| **Flight Termination** | 비행 종료 명령 |

### MAVLink Parachute

```
MAV_CMD_DO_PARACHUTE
- Param 1: Action (0=disable, 1=enable, 2=release)
```

## Payload Integration

### 하드웨어 연결

| 인터페이스 | 용도 |
|----------|------|
| **PWM/AUX** | 서보, 릴레이 |
| **GPIO** | 디지털 트리거 |
| **UART** | 직렬 통신 (카메라) |
| **I2C** | 센서, 스마트 배터리 |
| **CAN** | DroneCAN 페이로드 |

### 페이로드 파라미터

| 파라미터 | 설명 |
|----------|------|
| `MNT_MODE_IN` | Gimbal 입력 모드 |
| `MNT_MODE_OUT` | Gimbal 출력 모드 |
| `MNT_RANGE_PITCH` | Pitch 범위 |
| `MNT_RANGE_ROLL` | Roll 범위 |
| `MNT_RANGE_YAW` | Yaw 범위 |
| `TRIG_MODE` | 트리거 모드 |
| `TRIG_PINS` | 트리거 핀 |

## 무게 중심 & 성능

### 페이로드 영향

| 요소 | 설명 |
|------|------|
| **CG Shift** | 무게 중심 변화 |
| **Moment** | 모멘트 증가 |
| **Power** | 소비 전력 증가 |
| **Endurance** | 비행 시간 감소 |

### 페이로드 계산

```
Hover Throttle % = (Takeoff Weight / Max Thrust) × 100

Recommended: < 70% for stable flight
```

## 관련 개념

- [[computer-vision-drone]] — 카메라 기반 비전 시스템
- [[dronecan-protocol]] — CAN 기반 페이로드
- [[drone-power-battery]] — 페이로드 전원 요구사항
- [[drone-safety-failsafe]] — 페이로드 안전

## 최신 근거 연결 (2026-10-17)

- 듀얼 쿼드로터 완전구동 매니퓰레이터는 총 질량 0.447 kg에 최대 토크 1.019 N·m(2.28 N·m/kg): [[fam-dq-dual-quadrotor-aerial-manipulator]]^[inbox/processed/fetch-2026-10-17-arxiv-fam-dq-a-dual-quadrotor-based-fully-actuated-aerial-manipula.md]
- 케이블 매달림 페이로드 협업 운송의 힘 센싱·유도·입력 성형 연구(초록 수준): [[uav-cable-payload-cooperative-transport-research]]^[inbox/processed/fetch-2026-10-17-arxiv-compact-force-sensor-for-dual-uav-cable-suspended-payload-tr.md]
- 프로펠러 근처 에고노이즈 참조 마이크를 이용한 음성 향상: [[uav-ego-noise-speech-enhancement]]^[inbox/processed/fetch-2026-10-17-arxiv-speech-enhancement-using-ego-noise-references-with-a-microph.md]

## 최신 근거 연결 (2026-10-18)

- 줄로 매단 페이로드 UAV를 위해 전신 안전과 동역학 실현 가능성을 보장하는 실시간 궤적 계획과, 계층적 외란 보상을 쓰는 적응형 NMPC를 결합한 프레임워크(초록 수준, 정량 지표 없음): [[autotrans-uav-suspended-payload-planning-control]]^[inbox/processed/fetch-2026-10-18-arxiv-autotrans-a-complete-planning-and-control-framework-for-auto.md]

## 최신 근거 연결 (2026-10-20)

- 다중 UAV가 조인트로 연결된 강체 페이로드를 운송하는 제어 연구(피드백 선형화 추적, Gazebo 시뮬레이션): [[multi-uav-payload-transport-rao-controllers]]^[^[inbox/processed/fetch-2026-10-19-arxiv-an-input-output-feedback-linearization-based-exponentially-s.md]]
- 센서 태그 구동용 RF 비콘 페이로드는 지상 시험에서 동작했으나 공중에서는 무선 간섭으로 태그 데이터 검출에 실패해, 무선 페이로드의 기체 탑재 간섭 검증이 필요함을 보여준다: [[rf-energy-harvesting-sensor-tags-drone-agriculture]]^[^[inbox/processed/fetch-2026-10-20-arxiv-autonomous-agricultural-monitoring-with-aerial-drones-and-rf.md]]
