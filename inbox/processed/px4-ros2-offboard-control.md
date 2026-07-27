---
title: "ROS 2 Offboard Control Example for PX4"
created: 2026-07-27
captured: 2026-07-27
type: article
url: "https://docs.px4.io/main/en/ros2/offboard_control.html"
author: "PX4 Dev Team"
sha256: ""
tags: [drone-sw, ai-agent]
---

# ROS 2 Offboard Control Example

This C++ example demonstrates multicopter position control in offboard mode from a ROS 2 node. The example starts sending setpoints, enters offboard mode, arms, ascends to 5 metres, and waits. Tested on Ubuntu 20.04 with ROS 2 Foxy and PX4 v1.14.

**WARNING**: Offboard control is dangerous. On a real vehicle, always have a way to regain manual control.

## Key Concepts

PX4 requires receiving `OffboardControlMode` messages before it will arm in offboard mode. PX4 switches out of offboard mode if the stream rate of `OffboardControlMode` messages drops below ~2Hz.

## Setup

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

## Main Loop

```cpp
auto timer_callback = [this]() -> void {
    if (offboard_setpoint_counter_ == 10) {
        // Change to Offboard mode after 10 setpoints
        this->publish_vehicle_command(VehicleCommand::VEHICLE_CMD_DO_SET_MODE, 1, 6);
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

## Key Message Types

### OffboardControlMode
```cpp
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
```

### TrajectorySetpoint (NED frame)
```cpp
void OffboardControl::publish_trajectory_setpoint() {
    TrajectorySetpoint msg{};
    msg.position = {0.0, 0.0, -5.0};  // 5m altitude in NED (negative Z = up)
    msg.yaw = -3.14;  // [-PI:PI]
    msg.timestamp = this->get_clock()->now().nanoseconds() / 1000;
    trajectory_setpoint_publisher_->publish(msg);
}
```

### VehicleCommand
```cpp
void OffboardControl::publish_vehicle_command(uint16_t command, float param1, float param2) {
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

## Frame Conventions

- PX4 uses NED (North-East-Down) world frame and FRD (Forward-Right-Down) body frame
- ROS 2 uses ENU world frame and FLU body frame
- Must transform vectors before publishing to PX4 topics

## Important Notes

- `VehicleCommand` maps to MAVLink commands
- Subscribe to `VehicleCommandAck` to confirm command success
- QGC must be connected before running the node (or RC connection established)
- Source: [px4_ros_com/src/examples/offboard/offboard_control.cpp](https://github.com/PX4/px4_ros_com)
- Python offboard examples: [Jaeyoung-Lim/px4-offboard](https://github.com/Jaeyoung-Lim/px4-offboard)
