---
title: Drone Payload Systems
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-hw, payload, gimbal, camera, gripper]
sources: [raw/articles/px4-basic-concepts.md, raw/articles/px4-hardware-overview.md]
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
