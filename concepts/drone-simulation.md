---
title: Drone Simulation
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, simulation, gazebo, sitl, jmavsim, testing]
sources: [raw/articles/mastervault-px4-devnotes.md, raw/articles/px4-architecture.md]
confidence: high
contested: false
contradictions: []
---

# Drone Simulation

PX4 SITL(Software In The Loop)은 실제 하드웨어 없이 데스크톱에서 PX4 펌웨어를 실행하는 시뮬레이션 환경이다. Gazebo, jMAVSim, AirSim 등 다양한 시뮬레이터를 지원한다.^[raw/articles/mastervault-px4-devnotes.md]

## SITL 아키텍처

```
┌─────────────────────────────────────────┐
│           PX4 SITL (NuttX/Linux)      │
│         Flight Stack + Middleware     │
└───────────────────┬─────────────────────┘
                    │ UDP/MAVLink
┌───────────────────┴─────────────────────┐
│           Simulator (Gazebo/jMAVSim) │
│         Physics + Sensors (IMU, GPS) │
└─────────────────────────────────────────┘
```

## Gazebo Classic

현재 PX4의 주력 시뮬레이터.

### 실행

```bash
# PX4 SITL + Gazebo
make px4_sitl gazebo-classic

# 특정 기체
make px4_sitl gazebo-classic_iris
make px4_sitl gazebo-classic_standard_vtol
```

### Gazebo 특징

| 특성 | 설명 |
|------|------|
| **Physics** | ODE, Bullet, DART |
| **Sensors** | IMU, GPS, Baro, Lidar, Camera |
| **Scenarios** | 월드 파일 (.world) |
| **Plugins** | C++ 기반 확장 |

### Gazebo 월드

```bash
# 커스텀 월드
export GAZEBO_WORLD=~/my_world.world
make px4_sitl gazebo-classic
```

## jMAVSim

가벼운 자바 기반 시뮬레이터.

### 실행

```bash
make px4_sitl jmavsim
```

### 특징

| 특성 | 설명 |
|------|------|
| **Lightweight** | 빠른 시작, 낮은 리소스 |
| **Portability** | Java, 크로스 플랫폼 |
| **Basic Sensors** | 기본 IMU, GPS, Baro |
| **Limitations** | 고급 센서 미지원 |

## 멀티 기체 시뮬레이션

여러 대의 드론을 동시에 시뮬레이션.

```bash
# Gazebo Classic 멀티 기체
Tools/simulation/gazebo-classic/sitl_multiple_run.sh -n 3

# 개별 포트
Instance 0: UDP 14540
Instance 1: UDP 14541
Instance 2: UDP 14542
```

### MAVSDK 연결

```python
# Instance 0
drone0 = System()
await drone0.connect(system_address="udp://:14540")

# Instance 1
drone1 = System()
await drone1.connect(system_address="udp://:14541")
```

## ROS2 + SITL

ROS2와 통합된 시뮬레이션.^[raw/articles/mastervault-px4-devnotes.md]

```bash
# ROS2 SITL
make px4_sitl ros2

# uXRCE-DDS Agent
MicroXRCEAgent udp4 -p 8888
```

### QoS 설정

ROS2 구독자는 `SensorDataQoS`를 사용해야 PX4와 호환된다.

```cpp
subscription_ = this->create_subscription<px4_msgs::msg::SensorCombined>(
    "/fmu/out/sensor_combined", rclcpp::SensorDataQoS(), callback);
```

## 시뮬레이션 vs 실제

| 측면 | SITL | 실제 |
|------|------|------|
| **센서 노이즈** | 시뮬레이션 | 실제 환경 |
| **지연** | 거의 없음 | 통신 지연 |
| **날씨** | 제어 가능 | 불확실 |
| **GPS** | 완벽 | 멀티패스, 차단 |
| **바람** | 설정 가능 | 예측 불가 |
| **안전** | 안전 | 위험 |

## 테스트 시나리오

### 자동 테스트

```bash
# PX4 자동 테스트
make tests

# 특정 테스트
make test_MulticopterPositionControl
```

### CI/CD 통합

```yaml
# .github/workflows/ci.yml
- name: Run SITL Tests
  run: |
    make px4_sitl gazebo-classic
    test/simulation/run_tests.sh
```

## 시뮬레이션 파라미터

| 파라미터 | 설명 |
|----------|------|
| `SIM_GPS_DELAY` | GPS 지연 시뮬레이션 |
| `SIM_GPS_NOISE` | GPS 노이즈 |
| `SIM_GPS_GLITCH` | GPS 글리치 |
| `SIM_BARO_NOISE` | 기압계 노이즈 |
| `SIM_ACC_RND` | 가속도계 노이즈 |
| `SIM_GYR_RND** | 자이로 노이즈 |

## AirSim (선택)

Microsoft의 Unreal Engine 기반 시뮬레이터.

### 특징

| 특성 | 설명 |
|------|------|
| **Visual** | 고품질 그래픽 |
| **Sensors** | Camera, Lidar, Radar |
| **API** | Python, C++, C# |
| **ROS** | rosbridge 통합 |

## 관련 개념

- [[px4-offboard-control]] — SITL에서 Offboard 테스트
- [[ros2-drone-integration]] — ROS2 시뮬레이션 연동
- [[mavsdk]] — MAVSDK SITL 연결
- [[computer-vision-drone]] — 비전 시뮬레이션
