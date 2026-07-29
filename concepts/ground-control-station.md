---
title: Ground Control Station
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, GCS, QGroundControl, MAVLink, ground-control]
sources: [raw/articles/px4-basic-concepts.md]
confidence: high
domain: gcs-software
contested: false
contradictions: []
---

# Ground Control Station (GCS)

GCS(Ground Control Station)는 드론과 지상에서 통신하여 실시간 텔레메트리 모니터링, 기체 제어, 미션 계획을 수행하는 소프트웨어다. UAS(Unmanned Aerial System)의 핵심 구성요소다.^[raw/articles/px4-basic-concepts.md]

## 주요 GCS 소프트웨어

### QGroundControl (QGC)

Dronecode 프로젝트의 공식 GCS 소프트웨어.^[raw/articles/px4-basic-concepts.md]

| 특성 | 설명 |
|------|------|
| **플랫폼** | Windows, Android, macOS, Linux |
| **통신** | 양방향 텔레메트리 라디오 링크 via MAVLink |
| **주요 기능** | 실시간 텔레메트리, 기체 제어, 미션 계획, 지오펜싱, 펌웨어 설치 |
| **호환 펌웨어** | PX4, ArduPilot |
| **하드웨어** | Pixhawk 계열, 다양한 FC 지원 |

**핵심 기능:**
- 실시간 비행 데이터 모니터링 (고도, 속도, 배터리, GPS 등)
- 비행 중 미션 수정 및 업로드
- 지오펜싱 (안전 영역 설정)
- 펌웨어 설치 및 업데이트
- 센서 캘리브레이션
- 액추에이터 설정 (MAIN/AUX 포트 할당)

### Auterion Mission Control (AMC)

비행 작업에 최적화된 파일럿 중심 GCS.^[raw/articles/px4-basic-concepts.md]

| 특성 | 설명 |
|------|------|
| **포커스** | 비행 작업 (설정 작업보다 비행 중심) |
| **호환성** | Auterion 및 표준 PX4 시스템 |
| **UI** | 파일럿 친화적 인터페이스 |

### Mission Planner

ArduPilot 생태계의 주요 GCS (Windows 기반).

| 특성 | 설명 |
|------|------|
| **플랫폼** | Windows (주력) |
| **호환 펌웨어** | ArduPilot (Copter/Plane/Rover/Sub) |
| **특징** | 풍부한 설정 옵션, 고급 튜닝 기능 |

## GCS 연결 아키텍처

```
┌─────────────────┐     MAVLink     ┌─────────────────┐
│   GCS (QGC)     │ ←─────────────→ │  Flight Controller│
│  (Windows/Linux)│   (Telemetry)   │  (PX4/ArduPilot)  │
└─────────────────┘                 └─────────────────┘
         │                                   │
         │                          ┌──────────────┐
         │                          │   Sensors    │
         │                          │  GPS, IMU... │
         │                          └──────────────┘
         ▼
┌─────────────────┐
│  Mission Plan   │
│  - Waypoints    │
│  - Geofence     │
│  - Rally Points │
└─────────────────┘
```

## 텔레메트리 라디오

GCS와 FC 간 무선 MAVLink 연결을 제공.^[raw/articles/px4-basic-concepts.md]

| 용도 | 설명 |
|------|------|
| 파라미터 튜닝 | 비행 중 실시간 파라미터 조정 |
| 텔레메트리 검사 | 실시간 비행 데이터 확인 |
| 미션 수정 | 비행 중 웨이포인트 수정 |
| 범위 | 일반적으로 1-10km (장거리 버전 가능) |

## RC vs GCS 조종

| 방식 | 특성 | 사용 시나리오 |
|------|------|--------------|
| **RC (Radio Control)** | 저지연, 전용 송신기 | 레이싱, 정밀 조종 |
| **GCS (Joystick)** | 텔레메트리 채널 경유, MAVLink 명령 | 대부분의 비레이싱 응용 |

## QGC 주요 설정 영역

### 1. Airframe (기체 설정)
- 프레임 타입 선택 (쿼드, 헥사, 고정익 등)

### 2. Sensors (센서 캘리브레이션)
- Compass, Gyroscope, Accelerometer, Level Horizon

### 3. Radio (RC 설정)
- 송신기 바인딩, 채널 매핑

### 4. Flight Modes (비행 모드)
- 스위치별 비행 모드 할당

### 5. Power (전원 설정)
- 배터리 셀 수, 전압 캘리브레이션

### 6. Safety (안전 설정)
- Failsafe 동작, Geofence

### 7. Parameters (고급 파라미터)
- 모든 펌웨어 파라미터 접근

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 구성
- [[px4-flight-modes]] — PX4 비행 모드
- [[ardupilot-architecture]] — ArduPilot 아키텍처
- [[dronecan-protocol]] — CAN 버스 통신
- [[ros2-drone-integration]] — Companion 연동
