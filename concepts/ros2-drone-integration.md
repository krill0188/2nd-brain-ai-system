---
title: ROS2 Drone Integration
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, ROS2, MAVROS, micro-ROS, middleware]
sources: [raw/articles/mastervault-ros2-devnotes.md]
confidence: high
contested: false
contradictions: []
---

# ROS2 Drone Integration

ROS2는 Flight Controller와 연동하여 고급 자율 기능을 구현하는 메인 **middleware** 스택이다. Companion Computer에서 실행되며 PX4/ArduPilot과 브릿지 연결된다.^[raw/articles/mastervault-ros2-devnotes.md]

## 지원 배포판

| 배포판 | EOL | 비고 |
|--------|-----|------|
| **Humble** | 2027-05 | LTS, 현재 메인 |
| **Jazzy** | 2029-05 | LTS, 차기 이전 |
| **Kilted** | 2025-12 | Rolling 기반 |

## 드론 연동 스택 아키텍처

```
┌──────────────────────────────────────┐
│          ROS2 Application            │
│  Nav2 │ SLAM │ Planning │ Vision     │
├──────────────────────────────────────┤
│          MAVROS2 / micro-ROS         │
├──────────────────────────────────────┤
│          MAVLink / DDS               │
├──────────────────────────────────────┤
│          PX4 / ArduPilot             │
└──────────────────────────────────────┘
```

## PX4 + ROS2 연결

### PX4 SITL with ROS2 bridge

```bash
make px4_sitl ros2
```

### micro XRCE-DDS Agent

```bash
MicroXRCEAgent udp4 -p 8888
```

## ArduPilot + ROS2 연결

### MAVROS2 실행

```bash
ros2 launch mavros mavros.launch.py fcu_url:=udp://127.0.0.1:14550@
```

> **참고:** PX4와 ArduPilot 모두 MAVROS2를 통해 ROS2와 연결되나, 파라미터와 메시지 매핑에 차이가 있다.

## 자주 사용하는 패키지

| 패키지 | 용도 |
|--------|------|
| **mavros** | MAVLink↔ROS 브릿지 |
| **nav2** | 자율 내비게이션 |
| **slam_toolbox** | SLAM 매핑 |
| **image_transport** | 카메라 스트리밍 |
| **tf2** | 좌표 변환 |
| **micro_ros_agent** | MCU 연결 (micro-ROS) |

## ROS2 vs ROS1

| 특성 | ROS1 | ROS2 |
|------|------|------|
| 통신 | TCP/IP 기반 | DDS 기반 |
| 실시간 | 제한적 | 향상된 실시간 지원 |
| 보안 | 미흡 | 보안 기능 내장 |
| 드론 연동 | MAVROS | MAVROS2 / micro-ROS |

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 구성
- [[px4-flight-modes]] — PX4 비행 모드
- [[dronecan-protocol]] — FC-주변기기 통신
