---
title: ROS2 Advanced Integration
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, ros2, advanced, micro-ros, dds, qos, companion]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# ROS2 Advanced Integration

PX4와 ROS2의 고급 통합 기술. micro-ROS, DDS 튜닝, QoS 설정, 멀티 에이전트 아키텍처를 다룬다.

## Architecture Overview

```
┌─────────────────────────────────────────┐
│         Companion Computer            │
│  ┌─────────────────────────────────┐  │
│  │         ROS2 Nodes            │  │
│  │  ┌─────┐ ┌─────┐ ┌─────┐      │  │
│  │  │Nav  │ │Vision│ │Control│   │  │
│  │  └─────┘ └─────┘ └─────┘      │  │
│  └─────────────────────────────────┘  │
│              │                        │
│         micro-ROS Agent              │
│              │                        │
└──────────────┼────────────────────────┘
               │ uXRCE-DDS
┌──────────────┼────────────────────────┐
│         PX4 Flight Controller         │
│  ┌───────────┴───────────┐            │
│  │     micro-ROS Client   │            │
│  │         (uORB bridge)    │            │
│  └───────────┬───────────┘            │
│              │                          │
│         uORB Topics                   │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐     │
│  │Sensor│ │Attitude│ │Position│ │Actuator│
│  └─────┘ └─────┘ └─────┘ └─────┘     │
└─────────────────────────────────────────┘
```

## micro-ROS

### micro-ROS vs MAVROS

| 특성 | micro-ROS | MAVROS |
|------|-----------|--------|
| **Protocol** | DDS-XRCE | MAVLink |
| **Latency** | Lower | Higher |
| **Bandwidth** | Higher | Lower |
| **Complexity** | Higher | Lower |
| **Use case** | Companion | GCS |

### micro-ROS Setup

```bash
# Agent build
git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
cd Micro-XRCE-DDS-Agent
mkdir build && cd build
cmake ..
make
sudo make install

# Run agent
MicroXRCEAgent udp4 -p 8888
```

### Client on PX4

```bash
# PX4 with micro-ROS
make px4_fmu-v6x_default
# micro-ROS client 내장
```

## DDS Configuration

### QoS Profiles

| Profile | Use Case | 설정 |
|---------|----------|------|
| **SensorData** | High freq sensors | Best effort, volatile |
| **Parameters** | Config | Reliable, transient-local |
| **Default** | General | Reliable, volatile |
| **Services** | RPC | Reliable, volatile |

### Custom QoS

```python
# Python QoS
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

qos_profile = QoSProfile(
    reliability=ReliabilityPolicy.BEST_EFFORT,
    history=HistoryPolicy.KEEP_LAST,
    depth=10
)

subscription = node.create_subscription(
    SensorCombined,
    '/fmu/out/sensor_combined',
    callback,
    qos_profile
)
```

### C++ QoS

```cpp
// C++ QoS
rclcpp::QoS qos(10);
qos.reliability(RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT);

auto sub = node->create_subscription<px4_msgs::msg::SensorCombined>(
    "/fmu/out/sensor_combined",
    qos,
    callback
);
```

## Topic Mapping

### PX4 → ROS2

| uORB Topic | ROS2 Topic | Type |
|------------|------------|------|
| `sensor_combined` | `/fmu/out/sensor_combined` | SensorCombined |
| `vehicle_attitude` | `/fmu/out/vehicle_attitude` | VehicleAttitude |
| `vehicle_local_position` | `/fmu/out/vehicle_local_position` | VehicleLocalPosition |
| `vehicle_global_position` | `/fmu/out/vehicle_global_position` | VehicleGlobalPosition |

### ROS2 → PX4

| ROS2 Topic | uORB Topic | Type |
|------------|------------|------|
| `/fmu/in/offboard_control_mode` | `offboard_control_mode` | OffboardControlMode |
| `/fmu/in/trajectory_setpoint` | `trajectory_setpoint` | TrajectorySetpoint |
| `/fmu/in/vehicle_command` | `vehicle_command` | VehicleCommand |

## Multi-Agent Setup

### Multiple Drones

```python
# Namespace per drone
drone_0/
  /fmu/out/sensor_combined
  /fmu/in/trajectory_setpoint

drone_1/
  /fmu/out/sensor_combined
  /fmu/in/trajectory_setpoint
```

### Launch File

```python
# multi_drone_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    drones = ['drone_0', 'drone_1', 'drone_2']
    
    return LaunchDescription([
        Node(
            package='px4_ros_com',
            executable='offboard_control',
            namespace=drone,
            parameters=[{'agent_udp_port': 8888 + i}]
        )
        for i, drone in enumerate(drones)
    ])
```

## Time Synchronization

### ROS2 Time

```python
# Use ROS time
node.get_clock().now()

# Sync with PX4
# PX4 timestamp: microseconds since boot
# ROS2 timestamp: nanoseconds

px4_time_us = msg.timestamp
ros_time_ns = px4_time_us * 1000
```

### Sim Time

```bash
# Gazebo sim time
export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=1
```

## Advanced Publishers

### Lifecycle Node

```python
from rclpy.lifecycle import LifecycleNode
from rclpy.lifecycle import State
from rclpy.lifecycle import TransitionCallbackGroup

class DroneController(LifecycleNode):
    def __init__(self):
        super().__init__('drone_controller')
        
    def on_configure(self, state):
        self.pub = self.create_lifecycle_publisher(
            TrajectorySetpoint,
            '/fmu/in/trajectory_setpoint',
            10
        )
        return TransitionCallbackGroup.SUCCESS
```

### Composable Nodes

```cpp
// component_drone_control.cpp
#include <rclcpp/rclcpp.hpp>
#include <rclcpp_components/register_node_macro.hpp>

class DroneControl : public rclcpp::Node {
public:
    explicit DroneControl(const rclcpp::NodeOptions &options)
        : Node("drone_control", options) {
        // Component logic
    }
};

RCLCPP_COMPONENTS_REGISTER_NODE(DroneControl)
```

## Performance Optimization

### Intra-Process Communication

```python
# Same process optimization
from rclpy.executors import SingleThreadedExecutor

executor = SingleThreadedExecutor()
executor.add_node(node1)
executor.add_node(node2)
executor.spin()
```

### Zero-Copy

```cpp
// Loaned messages (zero-copy)
auto loaned_msg = publisher->borrow_loaned_message();
loaned_msg.get().data = value;
publisher->publish(std::move(loaned_msg));
```

### Threading

```python
# Multi-threaded executor
from rclpy.executors import MultiThreadedExecutor

executor = MultiThreadedExecutor(num_threads=4)
executor.add_node(node)
executor.spin()
```

## Debugging Tools

### ros2 topic

```bash
# List topics
ros2 topic list

# Echo topic
ros2 topic echo /fmu/out/vehicle_attitude

# Topic info
ros2 topic info /fmu/out/vehicle_attitude

# Bandwidth
ros2 topic bw /fmu/out/sensor_combined

# Hz
ros2 topic hz /fmu/out/sensor_combined
```

### ros2 node

```bash
# List nodes
ros2 node list

# Node info
ros2 node info /px4_ros_com
```

### rqt_graph

```bash
# Visualize node graph
rqt_graph
```

## Container Deployment

### Docker

```dockerfile
# Dockerfile
FROM ros:humble

WORKDIR /workspace
COPY . .

RUN apt-get update && apt-get install -y \
    ros-humble-px4-msgs \
    ros-humble-px4-ros-com

RUN colcon build

CMD ["ros2", "launch", "px4_ros_com", "px4.launch.py"]
```

### Docker Compose

```yaml
version: '3'
services:
  px4-sitl:
    image: px4io/px4-dev-simulation
    command: make px4_sitl gazebo-classic
    
  ros2-agent:
    image: px4-ros2
    command: MicroXRCEAgent udp4 -p 8888
    network_mode: host
    
  ros2-app:
    image: px4-ros2
    command: ros2 run px4_ros_com offboard_control
    network_mode: host
    depends_on:
      - ros2-agent
```

## Troubleshooting

| 문제 | 원인 | 해결 |
|------|------|------|
| **No topics** | Agent not running | Start MicroXRCEAgent |
| **Old messages** | QoS mismatch | Use SensorDataQoS |
| **High CPU** | Spin rate | Use timers, not loops |
| **Memory leak** | Subscription not cleaned | Proper node cleanup |
| **Sync issues** | Time domains | Use sim_time |

## 관련 개념

- [[ros2-drone-integration]] — ROS2 기본 통합
- [[px4-offboard-control]] — Offboard 제어
- [[mavsdk]] — MAVLink 대안
- [[visual-positioning-odometry]] — VIO 통합

## 수집 대상

- ROS2 Humble → Jazzy 마이그레이션
- Zenoh DDS 통합
- ROS2 Security (SROS2) 실제 적용
