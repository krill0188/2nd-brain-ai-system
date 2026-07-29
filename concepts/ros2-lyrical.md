---
title: ROS 2 Lyrical Luth
created: 2026-07-29
updated: 2026-07-29
type: concept
tags: [drone, drone-sw, gcs-software]
sources: [inbox/fetch-2026-07-29-ros2.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# ROS 2 Lyrical Luth

ROS 2 Lyrical Luth는 2026년 6월 23일에 릴리스된 ROS 2의 배포판이다. 드론 시스템 개발에서 PX4/ArduPilot과의 통합을 위한 주요 미들웨어 플랫폼으로 사용된다.

## 릴리스 정보

- **릴리스 날짜**: 2026년 6월 23일
- **버전**: Lyrical Luth Patch Release 1
- **이진 패키지**: 플랫폼별 바이너리 패키지 제공

## 드론 통합

- **PX4 연동**: [[px4-offboard-control]]을 통한 ROS2 기반 제어
- **ArduPilot 연동**: [[ros2-drone-integration]]에서 MAVROS/MAVROS2 활용
- **uXRCE-DDS**: PX4와의 DDS 기반 통신 브리지

## 관련 개념

- [[ros2-drone-integration]] — ROS2 기반 드론 연동 스택
- [[px4-offboard-control]] — ROS2를 통한 PX4 Offboard 제어
- [[mavros]] — MAVLink와 ROS2 간의 브리지
