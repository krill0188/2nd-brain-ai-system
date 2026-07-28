---
title: ArduPilot
created: 2026-07-28
updated: 2026-07-28
type: entity
tags: [drone-sw, drone]
sources:
  - raw/articles/ardupilot-entity-reference.md
confidence: high
contested: false
contradictions: []
---

# ArduPilot

ArduPilot은 멀티콥터·고정익·로버·잠수함 등 다양한 기체를 지원하는 오픈소스 자동조종 소프트웨어다.

## 개요

2009년 Chris Anderson 등이 시작했으며, 현재 ArduPilot Dev Team이 유지 관리한다.

- **공식 레포**: https://github.com/ArduPilot/ardupilot
- **최신 안정 버전**: ArduCopter 4.5.x (2024 기준)
- **라이선스**: GPLv3
- **지원 OS**: ChibiOS, Linux, SITL

## 기체 타입별 빌드

| 기체 타입 | 빌드 이름 | 설명 |
|---|---|---|
| 멀티콥터 | `ArduCopter` | 쿼드·헥사·옥토 등 회전익 |
| 고정익 | `ArduPlane` | 전통 고정익 + VTOL |
| 로버 | `ArduRover` | 지상 무인차량 |
| 잠수함 | `ArduSub` | 수중 드론 |
| 헬리콥터 | `ArduCopter (Heli)` | 전통 헬리콥터 |

## 핵심 파라미터

| 파라미터 | 기본값 | 설명 |
|---|---|---|
| `ATC_RAT_RLL_P` | 0.135 | 롤 비례 게인 |
| `ATC_RAT_PIT_P` | 0.135 | 피치 비례 게인 |
| `ATC_RAT_YAW_P` | 0.180 | 요 비례 게인 |
| `PILOT_SPEED_UP` | 250 cm/s | 수동 최대 상승 속도 |
| `WPNAV_SPEED` | 500 cm/s | 자율 비행 속도 |
| `RTL_ALT` | 1500 cm | RTL 복귀 고도 |
| `FENCE_ENABLE` | 0 | 지오펜스 활성화 |
| `GPS_TYPE` | 1 | GPS 드라이버 유형 (1=Auto) |
| `COMPASS_AUTODEC` | 1 | 자동 지자기 편각 보정 |
| `FS_THR_ENABLE` | 1 | 스로틀 페일세이프 활성화 |
| `EK3_ENABLE` | 1 | EKF3 상태 추정기 활성화 |

## 비행 모드

| 모드 번호 | 이름 | 설명 |
|---|---|---|
| 0 | Stabilize | 자세 안정화 |
| 2 | AltHold | 고도 유지 |
| 3 | Auto | 미션 자율 비행 |
| 4 | Guided | 외부 명령 자율 비행 |
| 5 | Loiter | 위치·고도 유지 |
| 6 | RTL | 홈 복귀 |
| 9 | Land | 착륙 |
| 16 | PosHold | 위치 유지 (Loiter 개선) |
| 20 | ACRO | 완전 수동 (레이싱) |

## 상태 추정기 (EKF3)

ArduPilot은 EKF3(Extended Kalman Filter v3)를 기본 상태 추정기로 사용한다.

- **인풋**: GPS, IMU, 기압계, 나침반, 광학 흐름, 비전 포지셔닝
- **아웃풋**: 위치·속도·자세 추정, 바람 추정, IMU 바이어스 보정
- **특이점**: 여러 EKF 인스턴스를 병렬 실행해 신뢰도 비교 가능 (`EK3_IMU_MASK`)

## PX4와의 비교

| 항목 | ArduPilot | PX4 |
|---|---|---|
| 라이선스 | GPLv3 | BSD |
| 메시지 버스 | 없음 (내부 직접 호출) | uORB |
| 모듈 구조 | 모노리식 코어 | 독립 모듈 |
| 파라미터 수 | ~1000+ | ~900+ |
| GCS 기본 지원 | Mission Planner | QGroundControl |
| ROS2 지원 | MAVROS2 | uXRCE-DDS (네이티브) |
| 군집 비행 | 제한적 (별도 스크립트) | 제한적 (Swarm 실험적) |

## 관련 페이지

- [[px4-flight-stack]] — 대표 경쟁 비행 스택
- [[mavlink-protocol]] — 기본 통신 프로토콜
- [[ground-control-station]] — ArduPilot 전용 GCS Mission Planner
- [[ros2-drone-integration]] — MAVROS2를 통한 ROS2 연동
