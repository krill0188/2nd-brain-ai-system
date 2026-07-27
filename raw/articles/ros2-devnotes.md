---
source_url: "file://MasterVault/Drone/ROS/ROS2-DevNotes.md"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "Master (personal dev notes)"
sha256: "3f7a9c4e8d2b5a7f3c6e9d4b8a2f5c7e1d9a6b3f8c4e7d2a5b9f6c3d8e4a7b2f5"
tags: [drone-sw]
---

# ROS2 개발 노트

## 지원 버전

| 배포판 | EOL | 비고 |
|--------|-----|------|
| Humble | 2027-05 | LTS, 현재 메인 |
| Jazzy | 2029-05 | LTS, 차기 이전 |
| Kilted | 2025-12 | Rolling 기반 |

## 드론 연동 스택

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

```bash
# PX4 SITL with ROS2 bridge
make px4_sitl ros2

# micro XRCE-DDS Agent
MicroXRCEAgent udp4 -p 8888
```

## ArduPilot + ROS2 연결

```bash
# MAVROS2
ros2 launch mavros mavros.launch.py fcu_url:=udp://127.0.0.1:14550@
```

## 자주 쓰는 패키지

| 패키지 | 용도 |
|--------|------|
| mavros | MAVLink↔ROS 브릿지 |
| nav2 | 자율 내비게이션 |
| slam_toolbox | SLAM 매핑 |
| image_transport | 카메라 스트리밍 |
| tf2 | 좌표 변환 |
| micro_ros_agent | MCU 연결 |
