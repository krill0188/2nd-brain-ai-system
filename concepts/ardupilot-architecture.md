---
title: ArduPilot Architecture
created: 2026-07-27
updated: 2026-08-06
type: concept
tags: [drone-sw, ArduPilot, flight-controller, HAL]
sources: [raw/articles/ardupilot-architecture.md, raw/articles/mastervault-ardupilot-devnotes.md]
confidence: high
domain: flight-control
contested: false
contradictions: []
---

# ArduPilot Architecture

ArduPilot은 HAL(Hardware Abstraction Layer) 기반의 모듈식 아키텍처로 설계된 오픈소스 자동조종장치 펌웨어다. PX4와 함께 가장 널리 사용되는 드론 펌웨어 중 하나다.^[raw/articles/ardupilot-architecture.md]

## 5가지 핵심 구성요소

```
┌─────────────────────────────────────────┐
│            Vehicle Code                 │
│  Copter │ Plane │ Rover │ Sub │ Blimp   │
├─────────────────────────────────────────┤
│            Shared Libraries             │
│  AP_AHRS │ AP_GPS │ AP_Motors │ AC_PID │
├─────────────────────────────────────────┤
│            AP_HAL (하드웨어 추상화)      │
├─────────────────────────────────────────┤
│  ChibiOS │ Linux │ ESP32 │ SITL         │
└─────────────────────────────────────────┘
```

### 1. Vehicle Code

기체 타입별 최상위 펌웨어 디렉토리. 각 기체의 동작을 정의한다.^[raw/articles/ardupilot-architecture.md]

| 기체 타입 | 설명 |
|----------|------|
| **Copter** | 멀티콥터 (쿼드, 헥사, 옥토 등) |
| **Plane** | 고정익 |
| **Rover** | 지상 로봇 |
| **Sub** | 수중 드론 |
| **Blimp** | 비행선 |
| **AntennaTracker** | 안테나 추적 |

### 2. Shared Libraries

모든 기체 타입에서 공유하는 라이브러리.^[raw/articles/ardupilot-architecture.md]

| 라이브러리 | 기능 |
|-----------|------|
| **AP_AHRS** | 자세 및 방향 추정 |
| **AP_GPS** | GNSS/GPS 처리 |
| **AP_Motors** | 모터 제어 |
| **AC_PID** | PID 제어기 |
| **AP_InertialSensor** | IMU 센서 드라이버 |
| **AP_Baro** | 기압계 드라이버 |
| **EKF** | Extended Kalman Filter (상태 추정) |

### 3. AP_HAL (Hardware Abstraction Layer)

플랫폼별 구현을 추상화하여 다양한 하드웨어 지원.^[raw/articles/ardupilot-architecture.md]

| HAL 구현 | 대상 플랫폼 |
|----------|-----------|
| **AP_HAL_ChibiOS** | STM32 기반 보드 (Pixhawk 등) |
| **AP_HAL_ESP32** | ESP32 보드 |
| **AP_HAL_Linux** | Linux 플랫폼 (Raspberry Pi 등) |
| **AP_HAL_SITL** | 소프트웨어 인더 루프 시뮬레이션 |

### 4. Tools Directories

- Autotest 인프라스트럭처
- 로그 리플레이 유틸리티

### 5. External Support Code (Git Submodules)

| 서브모듈 | 용도 |
|---------|------|
| **ChibiOS** | STM32용 RTOS |
| **DroneCAN** | CANBUS 프로토콜 구현 |
| **MAVLink** | 통신 프로토콜 및 코드 생성기 |

## SITL (Software In The Loop)

ArduPilot의 강력한 시뮬레이션 환경.^[raw/articles/mastervault-ardupilot-devnotes.md]

```bash
# Copter 시뮬레이션
sim_vehicle.py -v ArduCopter --map --console

# 특정 위치
sim_vehicle.py -v ArduCopter -L Seoul

# 멀티 기체
sim_vehicle.py -v ArduCopter -n 3

# 프레임 지정 (헥사콥터)
sim_vehicle.py -v ArduCopter -f hexa
```

## Lua 스크립팅

임무 자동화를 위한 Lua 스크립트 지원.^[raw/articles/mastervault-ardupilot-devnotes.md]

```lua
-- scripts/my_script.lua
function update()
    local pos = ahrs:get_position()
    if pos then
        gcs:send_text(6, string.format("Lat: %.6f", pos:lat()))
    end
    return update, 1000 -- 1초마다 실행
end
return update, 1000
```

## 주요 파라미터

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `FRAME_CLASS` | 프레임 타입 | 1 (쿼드) |
| `ARMING_CHECK` | 시동 체크 | 1 (전체) |
| `FS_THR_ENABLE` | 스로틀 페일세이프 | 1 |
| `WPNAV_SPEED` | 웨이포인트 속도 | 500 cm/s |
| `ATC_RAT_PIT_P` | 피치 PID P | 0.135 |

## 비행로그 분석

| 로그 타입 | 설명 | 분석 도구 |
|----------|------|----------|
| `.bin` | DataFlash 로그 | MAVExplorer |
| `.tlog` | 텔레메트리 로그 | UAV Log Viewer |

## PX4와의 비교

| 특성 | ArduPilot | PX4 |
|------|-----------|-----|
| **아키텍처** | HAL 기반, 기체별 코드 | uORB pub/sub, 통합 코드베이스 |
| **RTOS** | ChibiOS (STM32), NuttX 대안 | NuttX (주력) |
| **언어** | C++ | C++ |
| **커뮤니티** | 대규모, 다양한 기체 지원 | Dronecode 생태계 중심 |
| **ROS 통합** | MAVROS/ROS2 via MAVLink | Native uXRCE-DDS / ROS2 |

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 아키텍처 비교
- [[px4-flight-modes]] — PX4 비행 모드
- [[dronecan-protocol]] — CAN 버스 통신 프로토콜
- [[ros2-drone-integration]] — ROS2 연동 스택

## 세부 기체/제어 연구

- [[ardupilot-plane-4-7]] — ArduPilot Plane 4.7 릴리스
- [[indi-stability-tilt-rotor-vtol]] — INDI 틸트로터 VTOL 안정성 제어
- [[mars-dragonfly-modular-aerial]] — 화성 드래곤플라이 모듈형 비행체
- [[spatial-dubins-quadrotor-control]] — Dubins 경로 기반 쿼드로터 제어

## 📰 최근 관련 소식
- 고령층 많은 농업 현장이 폭염에 가장 취약…드론 띄워서 살핀다 (연합뉴스, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTFBLdElwUE03UmVsRlpCcEpNSHRBQmtBTGw3ZnFDbEduWTZTbTRZMXk4ZlBwcHYwMi1uQlA3eDR6QjRPT0xOa3l2QVF0NmVUbm5lWG1iQnRNa21lNTDSAWBBVV95cUxQZXFtT1l1WHRQRUFoR1J4amtHeFV6eEJxVjFTSkhzTFYwT1c3dEg0NkZ1RTROZkt1U1FoNHBHZUlJSnBZMmt2bkRxUWc4R1hVWmF2Smo2bzllcDI5RUhsRF8?oc=5
