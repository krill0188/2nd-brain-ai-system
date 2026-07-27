---
source_url: "file://MasterVault/Drone/PX4/PX4-DevNotes.md"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "Master (personal dev notes)"
sha256: "6d0i2f5h8g1b4e7f0a3d6e9c2f5a8d1e4f7a9b2c5d8e1f4a7b9c2d5e8f1a4b7"
tags: [drone-sw]
---

# PX4 개발 노트

## 핵심 아키텍처

```
┌──────────────────────────────────────────┐
│              Applications                │
│  Commander │ Navigator │ MC_Control      │
├──────────────────────────────────────────┤
│              uORB (메시지 버스)           │
├──────────────────────────────────────────┤
│              Middleware                   │
│  EKF2 │ Sensors │ MAVLink │ Logger       │
├──────────────────────────────────────────┤
│              Drivers                     │
│  IMU │ Baro │ GPS │ RC │ PWM            │
├──────────────────────────────────────────┤
│              NuttX RTOS                  │
└──────────────────────────────────────────┘
```

## SITL 빠른 시작

```bash
# 빌드 + 시뮬레이션
make px4_sitl gazebo-classic

# jMAVSim (가벼움)
make px4_sitl jmavsim

# 멀티 기체
Tools/simulation/gazebo-classic/sitl_multiple_run.sh -n 3
```

## 자주 쓰는 파라미터

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| SYS_AUTOSTART | 기체 프레임 | 4001 (쿼드) |
| EKF2_AID_MASK | EKF 센서 소스 | 1 (GPS) |
| NAV_RCL_ACT | RC Loss 동작 | 2 (RTL) |
| COM_ARM_EKF | EKF 시동 기준 | 0.8 |
| MPC_XY_VEL_MAX | 최대 수평 속도 | 12 m/s |

## 커스텀 모듈 템플릿

```cpp
// src/modules/my_module/my_module.cpp
#include <px4_platform_common/module.h>
#include <uORB/topics/vehicle_status.h>

class MyModule : public ModuleBase<MyModule> {
public:
    static int task_spawn(int argc, char *argv[]);
    void run() override;
};
```
