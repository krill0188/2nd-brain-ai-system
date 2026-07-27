---
title: ROS2 Advanced Integration
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, ros2, micro-ros, dds, qos, advanced, middleware]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# ROS2 Advanced Integration

ROS2는 DDS(Data Distribution Service) 기반 미들웨어로 PX4와의 고성능 통합을 제공한다. micro-ROS, QoS 튜닝, DDS 설정 등 고급 기능을 활용하면 실시간 성능을 극대화할 수 있다.

## ROS2 vs ROS1

| Feature | ROS1 | ROS2 |
|---------|------|------|
| **Middleware** | TCPROS/UDPROS | DDS |
| **Real-time** | Limited | Native support |
| **Security** | None | SROS2 |
| **Embedded** | No | micro-ROS |
| **Build system** | catkin | colcon |
| **Node lifecycle** | Simple | Managed |

## DDS Fundamentals

### DDS Architecture

```
┌─────────────────────────────────────────┐
│           ROS2 Application            │
│         (rclcpp/rclpy)               │
└───────────────────┬───────────────────┘
                    │ RMW (ROS Middleware)
                    ▼
┌─────────────────────────────────────────┐
│              DDS Layer                │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│  │ Domain  │ │ Topic   │ │ QoS     │ │
│  │ (0-232) │ │         │ │ Policy  │ │
│  └─────────┘ └─────────┘ └─────────┘ │
└─────────────────────────────────────────┘
```

### DDS Implementations

| Implementation | Vendor | Performance | Notes |
|---------------|--------|-------------|-------|
| **Fast DDS** | eProsima | Good | Default in ROS2 |
| **Cyclone DDS** | Eclipse | Excellent | Lightweight |
| **RTI Connext** | RTI | Commercial | Enterprise |
| **Iceoryx** | Eclipse | Ultra-low latency | Shared memory |

## QoS (Quality of Service)

### QoS Policies

| Policy | Description | Use Case |
|--------|-------------|----------|
| **Reliability** | Best effort / Reliable | Sensor data vs commands |
| **Durability** | Volatile / Transient local | Last known state |
| **History** | Keep last / Keep all | Buffer size |
| **Deadline** | Expected update rate | Real-time monitoring |
| **Lifespan** | Message expiration | Time-sensitive data |

### PX4 QoS Profile

```cpp
// Sensor data (high frequency, can drop)
rmw_qos_profile_t sensor_qos = {
    RMW_QOS_POLICY_HISTORY_KEEP_LAST,
    1,  // depth
    RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT,
    RMW_QOS_POLICY_DURABILITY_VOLATILE,
    RMW_QOS_DEADLINE_DEFAULT,
    RMW_QOS_LIFESPAN_DEFAULT,
    RMW_QOS_POLICY_LIVELINESS_SYSTEM_DEFAULT,
    RMW_QOS_LIVELINESS_LEASE_DURATION_DEFAULT,
    false  // avoid_ros_namespace_conventions
};

// Control commands (must arrive)
rmw_qos_profile_t command_qos = {
    RMW_QOS_POLICY_HISTORY_KEEP_LAST,
    1,
    RMW_QOS_POLICY_RELIABILITY_RELIABLE,
    RMW_QOS_POLICY_DURABILITY_VOLATILE,
    // ...
};
```

### Python QoS

```python
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

# Sensor QoS
sensor_qos = QoSProfile(
    reliability=ReliabilityPolicy.BEST_EFFORT,
    history=HistoryPolicy.KEEP_LAST,
    depth=1
)

# Command QoS
cmd_qos = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    history=HistoryPolicy.KEEP_LAST,
    depth=1
)

# Subscription
self.create_subscription(
    SensorCombined,
    '/fmu/out/sensor_combined',
    callback,
    sensor_qos
)
```

## micro-ROS

### Architecture

```
┌─────────────────────────────────────────┐
│           micro-ROS Client            │
│         (PX4, embedded)               │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│  │ RCLC    │ │ RMW     │ │ XRCE    │ │
│  │ (API)   │ │ (impl)  │ │ (DDS)   │ │
│  └─────────┘ └─────────┘ └─────────┘ │
└───────────────────┬───────────────────┘
                    │ Serial/UDP
                    ▼
┌─────────────────────────────────────────┐
│           XRCE-DDS Agent              │
│         (Companion PC)              │
└───────────────────┬───────────────────┘
                    │ DDS
                    ▼
┌─────────────────────────────────────────┐
│           ROS2 Ecosystem                │
│         (Full DDS stack)              │
└─────────────────────────────────────────┘
```

### micro-ROS Client Setup

```c
// PX4 micro-ROS initialization
#include <rclc/rclc.h>
#include <rclc/executor.h>

rcl_allocator_t allocator = rcl_get_default_allocator();
rclc_support_t support;

// Initialize with transport
rclc_support_init(&support, 0, NULL, &allocator);

// Create node
rcl_node_t node;
rclc_node_init_default(&node, "px4_node", "", &support);

// Create publisher
rcl_publisher_t publisher;
rclc_publisher_init_default(
    &publisher,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int32),
    "micro_ros_publisher"
);
```

### Agent Setup

```bash
# Install micro-ROS Agent
sudo apt install ros-humble-micro-ros-agent

# Run with serial
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0

# Run with UDP
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
```

## DDS Tuning

### Fast DDS Configuration

```xml
<!-- fastdds.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<dds xmlns="http://www.omg.org/dds/">
    <profiles>
        <participant profile_name="px4_profile">
            <rtps>
                <builtin>
                    <discovery_config>
                        <leaseDuration>10</leaseDuration>
                        <leaseDuration_announcementperiod>3</leaseDuration_announcementperiod>
                    </discovery_config>
                </builtin>
                <sendSocketBufferSize>65536</sendSocketBufferSize>
                <listenSocketBufferSize>65536</listenSocketBufferSize>
            </rtps>
        </participant>
    </profiles>
</dds>
```

### Environment Variables

```bash
# Select DDS implementation
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
# export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Load QoS profile
export FASTRTPS_DEFAULT_PROFILES_FILE=~/fastdds.xml

# Increase buffer sizes
export ROS2_DOMAIN_ID=0
```

## Time Synchronization

### ROS2 Time

```python
from rclpy.time import Time
from builtin_interfaces.msg import Time as TimeMsg

# Current time
now = self.get_clock().now()

# Convert to message
time_msg = TimeMsg()
time_msg.sec = now.seconds_nanoseconds()[0]
time_msg.nanosec = now.seconds_nanoseconds()[1]

# From PX4 timestamp (microseconds)
px4_time_us = vehicle_timestamp
ros_time = Time(seconds=px4_time_us / 1e6)
```

### Synchronization Strategy

```
PX4 monotonic time (boot time)
    ↓
uXRCE-DDS timestamp
    ↓
ROS2 time (system time or sim time)

Note: Use steady clock for control loops
```

## Multi-Threading

### Executor Types

| Executor | Use Case |
|----------|----------|
| **SingleThreaded** | Simple applications |
| **MultiThreaded** | Concurrent callbacks |
| **StaticSingleThreaded** | Real-time, deterministic |

### MultiThreaded Example

```cpp
#include <rclcpp/rclcpp.hpp>
#include <rclcpp/executors/multi_threaded_executor.hpp>

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);
    
    auto node = std::make_shared<DroneNode>();
    
    // Multi-threaded executor
    rclcpp::executors::MultiThreadedExecutor executor;
    executor.add_node(node);
    
    // Spin with 4 threads
    executor.spin();
    
    rclcpp::shutdown();
    return 0;
}
```

### Callback Groups

```cpp
// Mutually exclusive callbacks
auto callback_group = node->create_callback_group(
    rclcpp::CallbackGroupType::MutuallyExclusive
);

// Reentrant callbacks
auto reentrant_group = node->create_callback_group(
    rclcpp::CallbackGroupType::Reentrant
);

// Subscription with callback group
subscription_ = node->create_subscription<msg_type>(
    "topic",
    qos,
    callback,
    rclcpp::SubscriptionOptions().callback_group = callback_group
);
```

## Component Composition

### Component Node

```cpp
// drone_component.hpp
#include <rclcpp/rclcpp.hpp>
#include <rclcpp_components/register_node_macro.hpp>

namespace drone_composition {

class DroneComponent : public rclcpp::Node {
public:
    explicit DroneComponent(const rclcpp::NodeOptions& options)
        : Node("drone_component", options) {
        // Component initialization
    }
};

} // namespace drone_composition

RCLCPP_COMPONENTS_REGISTER_NODE(drone_composition::DroneComponent)
```

### Launch File

```python
# drone_composition.launch.py
from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    return LaunchDescription([
        ComposableNodeContainer(
            name='drone_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='drone_pkg',
                    plugin='drone_composition::DroneComponent',
                    name='drone_component'
                ),
            ],
        ),
    ])
```

## Security (SROS2)

### Security Setup

```bash
# Generate security artifacts
ros2 security create_keystore ~/sros2_keystore
ros2 security create_key ~/sros2_keystore px4_node
ros2 security create_key ~/sros2_keystore gcs_node

# Enable security
export ROS_SECURITY_ENABLE=true
export ROS_SECURITY_KEYSTORE=~/sros2_keystore
export ROS_SECURITY_STRATEGY=Enforce
```

### Access Control

```xml
<!-- policies.xml -->
<policy version="0.1.0">
    <enclaves>
        <enclave path="/px4_node">
            <profiles>
                <profile ns="/" node="px4_node">
                    <topics publish="ALLOW" subscribe="DENY">
                        <topic>fmu/out/*</topic>
                    </topics>
                </profile>
            </profiles>
        </enclave>
    </enclaves>
</policy>
```

## Performance Optimization

### Zero-Copy

```cpp
// Loaned messages (Fast DDS)
auto loaned_msg = publisher->borrow_loaned_message();
loaned_msg.get().data = 42;
publisher->publish(std::move(loaned_msg));
```

### Intra-Process

```cpp
// Same process optimization
rclcpp::NodeOptions options;
options.use_intra_process_comms(true);

auto node = std::make_shared<rclcpp::Node>("node", options);
```

### Memory Pools

```cpp
// Pre-allocated memory
rclcpp::PublisherOptions pub_options;
pub_options.allocator = rclcpp::allocator::Allocator<my_allocator>;

auto pub = node->create_publisher<Msg>(
    "topic",
    qos,
    pub_options
);
```

## Monitoring

### ROS2 Doctor

```bash
# System health check
ros2 doctor --report

# Topic statistics
ros2 topic statistics /fmu/out/vehicle_attitude
```

### Performance Test

```bash
# Throughput test
ros2 run performance_test perf_test -t test_topic --rate 1000

# Latency test
ros2 run performance_test perf_test -t test_topic --rate 100 --reliable
```

## Troubleshooting

| Issue | Diagnostic | Fix |
|-------|------------|-----|
| **High latency** | DDS tuning | Buffer sizes, thread priority |
| **Message loss** | QoS mismatch | Match reliability settings |
| **Discovery fail** | Network config | Check multicast, domain ID |
| **Memory growth** | Allocation | Use loaned messages |
| **CPU spike** | Executor type | Use StaticSingleThreaded |

## 관련 개념

- [[ros2-drone-integration]] — Basic ROS2-PX4
- [[px4-offboard-control]] — Control implementation
- [[mavlink-protocol]] — Alternative to ROS2
- [[drone-simulation]] — Gazebo + ROS2

## 수집 대상

- ROS2 real-time performance benchmarks
- PX4 micro-ROS production deployments
- DDS tuning for high-frequency sensors
