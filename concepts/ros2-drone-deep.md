---
title: "ROS2 Drone Integration Deep — PX4/ArduPilot 연동 상세"
created: 2026-07-28
updated: 2026-07-28
type: concept
tags: [drone-sw, ai-agent]
sources:
  - inbox/processed/mastervault-ros2-devnotes.md
  - inbox/processed/px4-ros2-offboard-control.md
  - inbox/processed/px4-ros2-user-guide.md
confidence: high
domain: gcs-software
contested: false
contradictions: []
---

# ROS2 Drone Integration Deep

ROS2와 PX4/ArduPilot의 통합 아키텍처, Offboard 제어, uXRCE-DDS 미들웨어 상세 분석.

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

## PX4 + ROS2 연결 (uXRCE-DDS)

```bash
# PX4 SITL with ROS2 bridge
make px4_sitl ros2

# micro XRCE-DDS Agent
MicroXRCEAgent udp4 -p 8888
```

아키텍처: 클라이언트가 PX4에서 실행되고 에이전트가 컴패니언 컴퓨터에서 실행. 직렬, UDP, TCP 또는 커스텀 링크로 양방향 데이터 교환.

## ArduPilot + ROS2 연결 (MAVROS2)

```bash
# MAVROS2
ros2 launch mavros mavros.launch.py fcu_url:=udp://127.0.0.1:14550@
```

## Offboard 제어 예시

PX4는 Offboard 모드에서 시동하려면 `OffboardControlMode` 메시지를 수신해야 함. 스트림 레이트가 ~2Hz 아래로 떨어지면 Offboard 모드에서 빠져나옴.

### 핵심 메시지 타입

```cpp
// OffboardControlMode
void OffboardControl::publish_offboard_control_mode() {
    OffboardControlMode msg{};
    msg.position = true;
    msg.velocity = false;
    msg.acceleration = false;
    msg.attitude = false;
    msg.body_rate = false;
    msg.timestamp = this->get_clock()->now().nanoseconds() / 1000;
    offboard_control_mode_publisher_->publish(msg);
}

// TrajectorySetpoint (NED frame)
void OffboardControl::publish_trajectory_setpoint() {
    TrajectorySetpoint msg{};
    msg.position = {0.0, 0.0, -5.0};  // 5m altitude in NED
    msg.yaw = -3.14;
    msg.timestamp = this->get_clock()->now().nanoseconds() / 1000;
    trajectory_setpoint_publisher_->publish(msg);
}
```

## 좌표계 변환

| 시스템 | 월드 프레임 | 바디 프레임 |
|--------|-------------|-------------|
| PX4 | NED (North-East-Down) | FRD (Forward-Right-Down) |
| ROS2 | ENU (East-North-Up) | FLU (Forward-Left-Up) |

PX4 토픽에 발행하기 전에 벡터 변환 필요.

## 자주 쓰는 패키지

| 패키지 | 용도 |
|--------|------|
| mavros | MAVLink↔ROS 브릿지 |
| nav2 | 자율 내비게이션 |
| slam_toolbox | SLAM 매핑 |
| image_transport | 카메라 스트리밍 |
| tf2 | 좌표 변환 |
| micro_ros_agent | MCU 연결 |

## QoS 설정

ROS2 구독자는 센서 데이터 QoS 프로파일을 사용해야 함. 기본 ROS2 QoS 설정은 PX4의 퍼블리셔 구성과 충돌함.

```cpp
// SensorDataQoS 사용
rclcpp::SensorDataQoS()
```

## 관련 페이지

- [[ros2-drone-integration]] — ROS2 연동 개요
- [[px4-offboard-control]] — Offboard 제어
- [[mavsdk]] — MAVSDK 대안
