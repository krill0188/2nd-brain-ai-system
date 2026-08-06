---
title: Drone Software Stack Overview
created: 2026-08-06
updated: 2026-08-06
type: concept
tags: [drone-sw]
sources: []
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# Drone Software Stack Overview

드론 소프트웨어 스택 전반을 아우르는 도메인 개요 페이지. 비행 제어 펌웨어(PX4/ArduPilot), GCS, 미들웨어(MAVLink/ROS2), SDK 계층을 포함한다.

## 계층 구조

| 계층 | 대표 소프트웨어 |
|---|---|
| 비행 제어 펌웨어 | PX4, ArduPilot |
| 통신 프로토콜 | MAVLink, DroneCAN |
| 미들웨어/브릿지 | ROS2, MAVROS, MAVSDK |
| 지상 제어국(GCS) | QGroundControl, Mission Planner |
| 시뮬레이션 | SITL, Gazebo |

## 관련 개념

- [[px4-system-architecture]] — PX4 소프트웨어 아키텍처
- [[ardupilot-architecture]] — ArduPilot 아키텍처
- [[mavros]] — ROS↔MAVLink 브릿지
