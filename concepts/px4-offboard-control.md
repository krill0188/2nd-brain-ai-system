---
title: PX4 Offboard Control
created: 2026-07-27
updated: 2026-08-10
type: concept
tags: [drone-sw, ai-agent, offboard, companion-computer, autonomous]
sources: [raw/articles/px4-offboard-control.md]
confidence: high
domain: flight-control
contested: false
contradictions: []
---

# PX4 Offboard Control

Offboard 모드는 **Companion Computer**가 Flight Controller의 비행 제어를 외부에서 직접 제어할 수 있게 하는 모드다. PX4는 오프보드 명령을 받아 실행하면서도 안전 장치(페일세이프)는 유지한다.^[raw/articles/px4-ros2-offboard-control.md]

> **⚠️ 경고**: Offboard 제어는 위험하다. 실제 기체에서는 항상 수동 제어로 회귀할 방법을 확보하라.

## 핵심 개념

PX4는 **OffboardControlMode** 메시지를 수신해야 offboard 모드로 시동한다. 메시지 스트림이 약 **2Hz** 아래로 떨어지면 PX4는 offboard 모드를 종료한다.^[raw/articles/px4-ros2-offboard-control.md]

## 시스템 아키텍처

```
┌────────────────────────┐         ┌─────────────────┐
│  Companion Computer   │         │   Flight Ctrl  │
│  (Linux + ROS2)       │◄───────►│   (PX4/NuttX)  │
│                       │  uXRCE  │                │
│  • OffboardControlMode│  DDS    │  • Core flight │
│  • TrajectorySetpoint │         │  • Safety      │
│  • VehicleCommand     │         │  • Actuators   │
└────────────────────────┘         └─────────────────┘
```

## ROS2 Offboard 제어 예시

### 환경 설정

```bash
mkdir -p ~/ws_offboard_control/src/
cd ~/ws_offboard_control/src/
git clone https://github.com/PX4/px4_msgs.git
git clone https://github.com/PX4/px4_ros_com.git
cd ..
source /opt/ros/humble/setup.bash
colcon build
source install/local_setup.bash
ros2 run px4_ros_com offboard_control
```

### 메인 루프 구조

```cpp
auto timer_callback = [this]() -> void {
    if (offboard_setpoint_counter_ == 10) {
        // 10개 setpoint 후 Offboard 모드로 전환
        this->publish_vehicle_command(
            VehicleCommand::VEHICLE_CMD_DO_SET_MODE, 1, 6);
        this->arm();
    }
    publish_offboard_control_mode();
    publish_trajectory_setpoint();
    if (offboard_setpoint_counter_ < 11) {
        offboard_setpoint_counter_++;
    }
};
timer_ = this->create_wall_timer(100ms, timer_callback);
```

## 주요 메시지 타입

### OffboardControlMode

```cpp
void OffboardControl::publish_offboard_control_mode() {
    OffboardControlMode msg{};
    msg.position = true;      // 위치 제어 활성화
    msg.velocity = false;
    msg.acceleration = false;
    msg.attitude = false;
    msg.body_rate = false;
    msg.timestamp = this->get_clock()->now().nanoseconds() / 1000;
    offboard_control_mode_publisher_->publish(msg);
}
```

### TrajectorySetpoint (NED 좌표계)

```cpp
void OffboardControl::publish_trajectory_setpoint() {
    TrajectorySetpoint msg{};
    // NED: Negative Z = 위쪽 (고도 5m)
    msg.position = {0.0, 0.0, -5.0};
    msg.yaw = -3.14;  // [-PI:PI]
    msg.timestamp = this->get_clock()->now().nanoseconds() / 1000;
    trajectory_setpoint_publisher_->publish(msg);
}
```

### VehicleCommand

```cpp
void OffboardControl::publish_vehicle_command(
    uint16_t command, float param1, float param2) {
    VehicleCommand msg{};
    msg.param1 = param1;
    msg.param2 = param2;
    msg.command = command;
    msg.target_system = 1;
    msg.target_component = 1;
    msg.source_system = 1;
    msg.source_component = 1;
    msg.from_external = true;
    msg.timestamp = this->get_clock()->now().nanoseconds() / 1000;
    vehicle_command_publisher_->publish(msg);
}
```

## 좌표계 변환

| 시스템 | 월드 프레임 | 바디 프레임 |
|--------|------------|------------|
| **PX4** | NED (North-East-Down) | FRD (Forward-Right-Down) |
| **ROS2** | ENU (East-North-Up) | FLU (Forward-Left-Up) |

> **중요**: PX4 토픽에 퍼블리시하기 전에 벡터 변환 필요

## Offboard 시퀀스

```
1. OffboardControlMode 메시지 연속 전송 (10회)
2. Offboard 모드로 전환 명령 (VEHICLE_CMD_DO_SET_MODE)
3. 시동 명령 (ARM)
4. TrajectorySetpoint 메시지로 위치/속도/가속도 제어
5. (안전 장치 작동 시 자동 복귀)
```

## 중요 참고사항

| 항목 | 설명 |
|------|------|
| **VehicleCommand** | MAVLink 명령에 매핑 |
| **VehicleCommandAck** | 명령 성공 확인 구독 필요 |
| **QGC 연결** | 노드 실행 전 QGC 또는 RC 연결 필요 |
| **실패 시** | 페일세이프로 수동 모드 복귀 |

## 참고 자료

- **C++ 예시**: [px4_ros_com/src/examples/offboard/offboard_control.cpp](https://github.com/PX4/px4_ros_com)
- **Python 예시**: [Jaeyoung-Lim/px4-offboard](https://github.com/Jaeyoung-Lim/px4-offboard)

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 구성 (Companion 연동)
- [[ros2-drone-integration]] — ROS2 연동 스택
- [[companion-computer]] — 컴패니언 컴퓨터 설정
