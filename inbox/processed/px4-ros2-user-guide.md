---
title: "ROS 2 User Guide for PX4"
created: 2026-07-27
captured: 2026-07-27
type: article
url: "https://docs.px4.io/main/en/ros2/user_guide.html"
author: "PX4 Dev Team"
sha256: ""
tags: [drone-sw, ai-agent]
---

# ROS 2 User Guide for PX4

## Architecture Overview

The ROS 2-PX4 integration leverages uXRCE-DDS middleware to enable deep connections between ROS 2 nodes and PX4's internal uORB topics. A client runs on PX4 while an agent operates on the companion computer, exchanging data bidirectionally across serial, UDP, TCP, or custom links.

The agent acts as a "proxy for the client to publish and subscribe to topics in the global DDS data space." Message definitions from PX4's source tree generate code for the client at build time.

## Installation Requirements

### PX4 Setup

```bash
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```

### ROS 2 Installation

Recommended: ROS 2 Humble LTS on Ubuntu 22.04. Install ROS repository and packages including development tools and Python dependencies (`empy==3.3.4`).

### Micro XRCE-DDS Agent Setup

```bash
git clone -b v2.4.3 https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
MicroXRCEAgent udp4 -p 8888
```

The simulator starts the client automatically, connecting to UDP port 8888 on localhost.

## Key Compatibility Considerations

### QoS Settings

ROS 2 subscribers must use sensor data QoS profiles. Nodes should subscribe using `rclcpp::SensorDataQoS()` because default ROS 2 QoS settings conflict with PX4's publisher configuration.

### Frame Conventions

PX4 uses FRD (Forward-Right-Down) body frames and NED (North-East-Down) world frames, while ROS employs FLU (Forward-Left-Up) and ENU conventions. Vector transformations are necessary before publishing trajectory or thrust setpoints to PX4.

### Time Synchronization

The uXRCE-DDS middleware automatically manages time synchronization between ROS 2 and PX4. For Gazebo simulations, configure via `use_sim_time` parameter.

## Building Workspaces

```bash
mkdir -p ~/ws_sensor_combined/src/
cd ~/ws_sensor_combined/src/
git clone https://github.com/PX4/px4_msgs.git
git clone https://github.com/PX4/px4_ros_com.git
```

Build using colcon with sourced ROS environment. Version branches in px4_msgs correspond to PX4 releases.

## Example Applications

The px4_ros_com repository provides:
- `sensor_combined_listener` — subscribing to PX4 telemetry
- Advertiser examples — publishing commands to PX4
- Offboard control examples — commanding takeoff, landing, and vehicle actions

## Hardware Integration

Running on actual flight controller hardware requires starting both agent and client with hardware-specific connection parameters (USB serial, telemetry radio, or Ethernet) instead of UDP localhost.
