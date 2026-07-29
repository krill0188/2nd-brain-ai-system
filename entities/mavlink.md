---
title: MAVLink Protocol
created: 2026-07-28
updated: 2026-07-28
type: entity
tags: [datalink, drone-sw]
sources:
  - raw/articles/mavlink-protocol-entity-reference.md
confidence: high
domain: comms-protocol
contested: false
contradictions: []
---

# MAVLink Protocol

MAVLink(Micro Air Vehicle Link)는 드론과 지상국(GCS) 간 통신을 위한 경량 직렬 메시지 프로토콜이다.

## 개요

2009년 Lorenz Meier가 개발했으며, PX4·ArduPilot 양쪽에서 사실상 표준으로 채택됐다.

- **공식 레포**: https://github.com/mavlink/mavlink
- **최신 버전**: MAVLink 2.0 (하위 호환: MAVLink 1.0)
- **라이선스**: MIT (메시지 정의: XML)
- **패킷 최소 크기**: v1 = 8바이트, v2 = 12바이트

## 버전 비교

| 항목 | MAVLink 1.0 | MAVLink 2.0 |
|---|---|---|
| 최대 페이로드 | 255 바이트 | 255 바이트 |
| 메시지 ID 범위 | 0~255 | 0~16,777,215 |
| 서명(Signing) | ❌ | ✅ (HMAC-SHA256) |
| 패킷 손실 감지 | ✅ (seqnum) | ✅ (seqnum) |
| 컴포넌트 타겟팅 | ❌ | ✅ |
| 패킷 헤더 크기 | 6 바이트 | 10 바이트 |

## 핵심 메시지

| Message ID | 이름 | 설명 |
|---|---|---|
| 0 | `HEARTBEAT` | 시스템 생존·타입·모드 전파 (1Hz) |
| 1 | `SYS_STATUS` | 배터리·CPU 부하·센서 상태 |
| 24 | `GPS_RAW_INT` | GPS 위치·속도·정밀도 원시 데이터 |
| 30 | `ATTITUDE` | 롤·피치·요 + 각속도 |
| 32 | `LOCAL_POSITION_NED` | NED 좌표계 위치·속도 |
| 33 | `GLOBAL_POSITION_INT` | WGS84 위도·경도·고도 |
| 74 | `VFR_HUD` | GCS 비행계기판용 요약 데이터 |
| 76 | `COMMAND_LONG` | 단일 명령 전송 (MAV_CMD 기반) |
| 77 | `COMMAND_ACK` | 명령 수신·실행 결과 응답 |
| 83 | `ATTITUDE_TARGET` | 자세 목표값 (Offboard 제어) |
| 84 | `POSITION_TARGET_LOCAL_NED` | 위치 목표값 (NED, Offboard) |
| 87 | `POSITION_TARGET_GLOBAL_INT` | 위치 목표값 (GPS, Offboard) |
| 105 | `HIGHRES_IMU` | 고해상도 IMU 원시 데이터 |
| 141 | `ALTITUDE` | 다중 고도 기준 통합 |
| 242 | `HOME_POSITION` | 홈 포인트 좌표 |
| 253 | `STATUSTEXT` | 텍스트 상태 메시지 (GCS 로그) |

## MAV_CMD 명령 코드

| 코드 | 이름 | 설명 |
|---|---|---|
| 22 | `MAV_CMD_NAV_TAKEOFF` | 이륙 |
| 21 | `MAV_CMD_NAV_LAND` | 착륙 |
| 20 | `MAV_CMD_NAV_RETURN_TO_LAUNCH` | RTL |
| 16 | `MAV_CMD_NAV_WAYPOINT` | 웨이포인트 이동 |
| 400 | `MAV_CMD_COMPONENT_ARM_DISARM` | Arming/Disarming |
| 176 | `MAV_CMD_DO_SET_MODE` | 비행 모드 변경 |
| 115 | `MAV_CMD_DO_SET_SERVO` | 서보 직접 제어 |

## 컴포넌트 ID

| ID | 이름 | 설명 |
|---|---|---|
| 1 | `AUTOPILOT1` | 자동조종장치 (PX4/ArduPilot) |
| 100 | `CAMERA` | 카메라 |
| 154 | `GIMBAL` | 짐벌 |
| 190 | `MISSIONPLANNER` | GCS 미션 플래너 |
| 240 | `UDP_BRIDGE` | MAVLink UDP 브리지 |
| 250 | `SYSTEM_CONTROL` | 시스템 제어 |

## 통신 채널

| 채널 | 프로토콜 | 용도 |
|---|---|---|
| UART/Serial | 직렬 | 비행체↔GCS 직접 연결 |
| UDP | IP | SITL, 온보드 컴퓨터 |
| TCP | IP | 장거리 GCS 연결 |
| Serial over RF | RF 텔레메트리 | SiK 라디오 (433/915MHz) |

## 주요 구현체

| 구현체 | 언어 | 용도 |
|---|---|---|
| MAVSDK | C++/Python/Swift | 드론 앱 개발 SDK |
| pymavlink | Python | 스크립팅·로그 분석 |
| mavros/mavros2 | C++ (ROS) | ROS/ROS2 브리지 |
| QGroundControl | C++ (Qt) | 범용 GCS |
| Mission Planner | C# | ArduPilot 전용 GCS |

## 관련 페이지

- [[px4-flight-stack]] — MAVLink 주요 구현 비행 스택
- [[ardupilot]] — MAVLink 주요 구현 비행 스택
- [[mavsdk]] — 드론 앱 개발을 위한 MAVLink SDK
- [[ground-control-station]] — MAVLink 기반 오픈소스 GCS
