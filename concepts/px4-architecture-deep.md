---
title: PX4 Architecture Deep Dive
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, PX4, architecture, uORB, middleware]
sources: [raw/articles/px4-architecture.md, raw/articles/mastervault-px4-devnotes.md]
confidence: high
contested: false
contradictions: []
---

# PX4 Architecture Deep Dive

PX4는 비행 스택(estimation & control)과 미들웨어(robotics layer)의 두 계층으로 구성된다. 모든 기체 유형(드론, 보트, 로버, 잠수정)이 단일 코드베이스를 공유하며, 반응형 설계와 비동기 메시지 전달을 채택한다.^[raw/articles/px4-architecture.md]

## 소프트웨어 아키텍처

```
┌──────────────────────────────────────────┐
│              Applications                │
│  Commander │ Navigator │ MC_Control     │
├──────────────────────────────────────────┤
│              Flight Stack                │
│  Estimators │ Controllers │ Mixers      │
├──────────────────────────────────────────┤
│              uORB (메시지 버스)          │
├──────────────────────────────────────────┤
│              Middleware                  │
│  EKF2 │ Sensors │ MAVLink │ Logger     │
├──────────────────────────────────────────┤
│              Drivers                   │
│  IMU │ Baro │ GPS │ RC │ PWM           │
├──────────────────────────────────────────┤
│              NuttX RTOS                │
└──────────────────────────────────────────┘
```

## 두 개의 메인 레이어

### 1. Flight Stack

자율 드론을 위한 guidance, navigation, control 알고리즘.^[raw/articles/px4-architecture.md]

| 컴포넌트 | 설명 | 예시 |
|---------|------|------|
| **Controllers** | 공기역학 제어기 | 고정익, 멀티로터, VTOL |
| **Estimators** | 상태 추정 | EKF2 (attitude & position) |
| **Sensor Pipeline** | 센서 처리 흐름 | 센서 → 추정 → 제어 → 액추에이터 |
| **Mixers** | 모터 명령 변환 | 힘/토크 → PWM/DroneCAN |

### 2. Middleware

일반 로보틱스 지원 계층.^[raw/articles/px4-architecture.md]

| 컴포넌트 | 설명 |
|---------|------|
| **Device Drivers** | 임베디드 센서 드라이버 |
| **External Comm** | Companion computer, GCS 통신 |
| **uORB** | Publish-subscribe 메시지 버스 |
| **Simulation** | 데스크탑 테스트 레이어 |

## uORB: 메시지 버스

Publish-subscribe 방식의 반응형 메시지 전달.^[raw/articles/px4-architecture.md]

| 특성 | 설명 |
|------|------|
| **Asynchronous** | 데이터 도착 시 즉시 업데이트 |
| **Parallel** | 완전한 병렬 처리 |
| **Thread-safe** | 컴포넌트 데이터 소비 안전 |

### 핵심 원칙
> Any building block can be rapidly replaced, even during runtime.

## 모듈 실행 방식

| 방식 | 특성 | 장단점 |
|------|------|--------|
| **Tasks** | 독립적 실행, 개별 스택 | RAM 많음, 유연함 |
| **Work Queue** | 공유 큐/스택/우선순위 | RAM 절약, 협력적 동작 필요 |

### Work Queue 특성

- 잠들 수 없음 (no sleep)
- 메시지 폴링 불가
- Blocking I/O 불가
- `work_queue status`로 확인

## 업데이트 속도

| 모듈 | 주파수 | 설명 |
|------|--------|------|
| IMU 드라이버 | 1kHz 샘플링 → 250Hz 발행 | 고속 센서 |
| Navigator | 더 낮음 | 저속 모듈 |

```bash
# 실시간 메시지 레이트 확인
uorb top
```

## 런타임 환경

| OS | 특성 |
|----|------|
| **NuttX** | 주력 flight-control RTOS |
| **Linux/macOS** | POSIX compliant, SITL |
| **QuRT** | Snapdragon |

### NuttX 세부사항

- Apache BSD-licensed RTOS
- 가볍고, 효율적이며, 안정적
- Tasks: 개별 파일 디스크립터
- Threads: 파일 디스크립터 공유
- 고정 크기 스택: 주기적 여유 공간 모니터링

## 실행 스택 흐름

```
Sensors → Estimators → Controllers → Mixers → Actuators
   1kHz      250Hz        250Hz       250Hz      PWM
```

## 주요 기술 개념

| 개념 | 설명 |
|------|------|
| **Reactive Architecture** | 비동기, 논블로킹 통신 |
| **Module Communication** | uORB만으로 모든 모듈 간 메시징 |
| **Priority Levels** | 중요한 비행 제어 루프가 높은 우선순위 |

## 주요 파라미터

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `SYS_AUTOSTART` | 기체 프레임 | 4001 (쿼드) |
| `EKF2_AID_MASK` | EKF 센서 소스 | 1 (GPS) |
| `NAV_RCL_ACT` | RC Loss 동작 | 2 (RTL) |
| `COM_ARM_EKF` | EKF 시동 기준 | 0.8 |
| `MPC_XY_VEL_MAX` | 최대 수평 속도 | 12 m/s |

## SITL 빠른 시작

```bash
# Gazebo Classic
make px4_sitl gazebo-classic

# jMAVSim (경량)
make px4_sitl jmavsim
```

## 커스텀 모듈 템플릿

```cpp
// src/modules/my_module/my_module.cpp
#include <px4_platform_common/module.h>
#include <uORB/topics/vehicle_status.h>

class MyModule : public ModuleBase<MyModule> {
public:
    static int task_spawn(int argc, char *argv[]);
    void run() override;
};
```

## 관련 개념

- [[px4-system-architecture]] — 시스템 레벨 구성
- [[px4-flight-modes]] — 비행 모드
- [[uorb-messaging]] — 메시지 버스 상세
- [[ros2-drone-integration]] — ROS2 연동
- [[dronecan-protocol]] — CAN 통신
