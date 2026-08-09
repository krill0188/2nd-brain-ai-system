---
title: PX4 Flight Stack
created: 2026-07-28
updated: 2026-08-10
type: entity
tags: [drone-sw, drone]
sources:
  - raw/articles/entity-px4-flight-stack.md
confidence: high
domain: flight-control
contested: false
contradictions: []
---

# PX4 Flight Stack

PX4는 Dronecode 재단이 관리하는 오픈소스 드론 비행 제어 소프트웨어(펌웨어)다.

## 개요

픽스호크(Pixhawk) 계열 하드웨어에서 주로 구동되며, SITL(Software In The Loop) 시뮬레이션도 지원한다.

- **공식 레포**: https://github.com/PX4/PX4-Autopilot
- **최신 안정 버전**: v1.15.x (2024 기준)
- **라이선스**: BSD 3-Clause
- **지원 RTOS**: NuttX (하드웨어), Linux (POSIX SITL)

## 핵심 모듈

| 모듈 | 역할 | uORB 토픽 |
|---|---|---|
| `commander` | 비행 모드 전환, Arming/Disarming, 안전 체크 | `vehicle_status`, `commander_state` |
| `navigator` | 미션 계획 실행, 웨이포인트 이동, RTL | `position_setpoint_triplet`, `mission` |
| `mc_pos_control` | 멀티콥터 위치 제어 루프 | `vehicle_local_position_setpoint` |
| `mc_att_control` | 멀티콥터 자세 제어 루프 | `vehicle_attitude_setpoint`, `actuator_controls` |
| `ekf2` | 확장 칼만 필터 기반 상태 추정 | `vehicle_local_position`, `vehicle_attitude` |
| `sensors` | 센서 데이터 수집·캘리브레이션 | `sensor_combined`, `sensor_gyro` |
| `mavlink` | MAVLink 프로토콜 통신 | `mavlink_log`, `telemetry_status` |
| `logger` | 비행 로그 기록 (ULog 포맷) | `ulog_stream` |
| `mixer` | 제어 출력 믹싱 → 모터/서보 신호 변환 | `actuator_outputs` |

## 주요 파라미터

| 파라미터 | 기본값 | 설명 |
|---|---|---|
| `MC_ROLL_P` | 6.5 | 멀티콥터 롤 비례 게인 |
| `MC_PITCH_P` | 6.5 | 멀티콥터 피치 비례 게인 |
| `MC_YAW_P` | 2.8 | 멀티콥터 요 비례 게인 |
| `MPC_Z_VEL_MAX_UP` | 3.0 m/s | 최대 상승 속도 |
| `MPC_Z_VEL_MAX_DN` | 1.0 m/s | 최대 하강 속도 |
| `MPC_XY_VEL_MAX` | 12.0 m/s | 최대 수평 속도 |
| `EKF2_AID_MASK` | 1 | EKF2 보조 센서 마스크 (GPS=1, 광류=2, 비전=4) |
| `NAV_RCL_ACT` | 2 | RC 신호 손실 시 동작 |
| `COM_DISARM_LAND` | 2.0 s | 착륙 후 자동 Disarm 시간 |
| `SYS_AUTOSTART` | 4001 | 기체 프레임 자동 설정 |

## 비행 모드

| 모드 | 코드 | 설명 |
|---|---|---|
| Manual | MANUAL | RC 직접 조종, 안정화 없음 |
| Stabilized | STAB | 자세 안정화, 고도 비안정 |
| Altitude | ALTCTL | 고도 유지, 수평 비안정 |
| Position | POSCTL | 위치·고도 유지 (GPS 필요) |
| Mission | AUTO_MISSION | 웨이포인트 자율 비행 |
| Hold | AUTO_LOITER | 현재 위치 호버링 |
| Return | AUTO_RTL | 홈 포인트 자동 복귀 |
| Offboard | OFFBOARD | 외부 컴퓨터 제어 |

## uORB 핵심 토픽

| 토픽 | 게시자 | 구독자 | 설명 |
|---|---|---|---|
| `vehicle_attitude` | ekf2 | mc_att_control, navigator | 쿼터니언 자세 |
| `vehicle_local_position` | ekf2 | mc_pos_control, navigator | NED 좌표계 위치·속도 |
| `sensor_combined` | sensors | ekf2 | IMU 통합 데이터 |
| `actuator_controls_0` | mc_att_control | mixer | 제어 출력 |
| `vehicle_command` | commander, GCS | navigator, modules | MAVLink 명령 래퍼 |

## SITL 실행

```bash
# Gazebo Classic 시뮬레이션
make px4_sitl gazebo-classic

# jMAVSim (경량)
make px4_sitl jmavsim

# MAVSDK Python 연결
pip install mavsdk
```

## 관련 페이지

- [[ardupilot]] — 대표적인 경쟁/대안 비행 스택
- [[mavlink-protocol]] — 지상국-비행체 통신 프로토콜
- [[pixhawk]] — PX4 주요 구동 하드웨어 플랫폼
- [[ros2-drone-integration]] — ROS2 연동 인터페이스 (uXRCE-DDS)
