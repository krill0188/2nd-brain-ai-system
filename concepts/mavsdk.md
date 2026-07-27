---
title: MAVSDK
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, MAVSDK, SDK, API, offboard]
sources: []
confidence: medium
contested: false
contradictions: []
---

# MAVSDK

MAVSDK는 MAVLink 프로토콜을 기반으로 하는 고수준 드론 제어 SDK다. C++, Python, Java, Swift 등 다양한 언어 바인딩을 제공하며, PX4와 ArduPilot 모두와 호환된다.

## 개요

MAVSDK는 복잡한 MAVLink 프로토콜을 단순화한 API를 제공하여 드론 애플리케이션 개발을 가속화한다.

| 특성 | 설명 |
|------|------|
| **언어** | C++, Python, Java, Swift, C# |
| **프로토콜** | MAVLink |
| **호환 펌웨어** | PX4, ArduPilot |
| **플랫폼** | Linux, macOS, Windows, Android, iOS |

## 아키텍처

```
┌─────────────────────────────────────────┐
│         Application (Your Code)         │
│         Python / C++ / Java            │
├─────────────────────────────────────────┤
│              MAVSDK API                 │
│  Action │ Mission │ Telemetry │ Offboard│
├─────────────────────────────────────────┤
│              MAVLink Core               │
├─────────────────────────────────────────┤
│           UDP/TCP/Serial                │
└─────────────────────────────────────────┘
```

## 핵심 모듈

| 모듈 | 설명 |
|------|------|
| **Action** | 고수준 동작 (이륙, 착륙, 복귀) |
| **Mission** | 미션 계획 및 실행 |
| **Telemetry** | 실시간 텔레메트리 구독 |
| **Offboard** | 위치/속도/가속도 제어 |
| **Calibration** | 센서 캘리브레이션 |
| **Param** | 파라미터 읽기/쓰기 |

## Python 예시

```python
import asyncio
from mavsdk import System

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")
    
    # 연결 대기
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone connected!")
            break
    
    # 이륙
    await drone.action.arm()
    await drone.action.takeoff()
    await asyncio.sleep(10)
    
    # 착륙
    await drone.action.land()

asyncio.run(run())
```

## Offboard 제어

```python
# 위치 제어
await drone.offboard.set_position_ned(
    PositionNedYaw(0.0, 0.0, -5.0, 0.0))

# 속도 제어
await drone.offboard.set_velocity_ned(
    VelocityNedYaw(1.0, 0.0, 0.0, 0.0))
```

## 연결 방식

| 방식 | 주소 형식 | 용도 |
|------|----------|------|
| **UDP** | `udp://:14540` | SITL, WiFi |
| **TCP** | `tcp://192.168.1.10:5760` | Ethernet |
| **Serial** | `serial:///dev/ttyUSB0:921600` | 직렬 연결 |

## PX4 vs ROS2 Offboard

| 특성 | MAVSDK | ROS2 |
|------|--------|------|
| **수준** | 고수준 API | 저수준 메시지 |
| **구현** | 간단 | 복잡 |
| **유연성** | 제한적 | 높음 |
| **실시간** | 제한적 | 지원 |
| **사용 사례** | 프로토타입, GCS | 자율비행, SLAM |

## 관련 개념

- [[mavlink-protocol]] — 하위 프로토콜
- [[px4-offboard-control]] — ROS2 Offboard 제어 비교
- [[ground-control-station]] — GCS 연동
