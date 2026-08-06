---
title: MAVROS
created: 2026-08-06
updated: 2026-08-06
type: concept
tags: [drone-sw, datalink]
sources: []
confidence: medium
contested: false
contradictions: []
domain: gcs-software
---

# MAVROS

MAVROS는 ROS/ROS2와 MAVLink 기반 자동조종장치(PX4, ArduPilot) 사이를 연결하는 브릿지 패키지다. MAVLink 메시지를 ROS 토픽/서비스로 변환해, ROS 노드가 텔레메트리 수신 및 offboard 명령 송신을 할 수 있게 한다.

## 역할

- MAVLink ↔ ROS 토픽 변환 (센서 데이터, 상태, 명령)
- Offboard/Guided 모드 명령 송신
- 여러 자동조종장치 펌웨어(PX4, ArduPilot) 공통 인터페이스 제공

## 관련 개념

- [[mavlink]] — MAVLink 프로토콜
- [[ros2-drone-integration]] — ROS2 드론 통합(MAVROS 포함)
