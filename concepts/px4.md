---
title: "Px4"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [px4, flight-control, middleware, nuttx, mavlink]
sources: ["raw/articles/ardupilot-architecture.md"]
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# Px4

Px4는 NuttX RTOS 위에서 실행되며, ROS 2와 통합되고 Dronecode 프로젝트 하에 관리되는 오픈소스 비행 제어 시스템이다. MAVlink 프로토콜을 기반으로 하며, DroneCAN과 uORCE-DDS를 사용해 통신하고 QGroundcontrol을 지원한다.

## 개요

ArduPilot과 비교해 **uORB publish/subscribe 기반의 통합된 코드베이스**를 특징으로 한다. Px4는 NuttX RTOS를 기반으로 하며, ChibiOS와는 다른 RTOS 선택을 하고 있다. 라이선스는 BSD이며, Dronecode 재단에 의해 관리된다.

## 핵심 파라미터

| 구분 | 내용 |
|------|------|
| RTOS | NuttX (primary) |
| 코드 언어 | C++ |
| 라이선스 | BSD |
| 통신 프로토콜 | MAVLink |
| 통합 프레임워크 | ROS 2 (uXRCE-DDS) |
| 운영체제 포팅 | NuttX 기반 플랫폼 |
| 주요 의존성 | DroneCAN, uORB |

## 활용처

- 민간 드론 및 산업용 무인기 플랫폼
- 연구 및 교육용 비행 제어 연구
- Dronecode 생태계 내 연동 개발

## 관련 페이지

- [[ArduPilot]] — HAL 기반, vehicle-specific code 구조를 가짐
- [[MAVLink]] — Px4가 구현하는 프로토콜
- [[Dronecode]] — Px4를 관리하는 오픈소스 재단

## 출처

- (사용자 재확인 필요) original: raw/articles/ardupilot-architecture.md

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-articles]] — 출처 유형
