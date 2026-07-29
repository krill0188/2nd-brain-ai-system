---
title: MAVSDK v3.17.2
created: 2026-07-29
updated: 2026-07-29
type: concept
tags: [drone, drone-sw, datalink]
sources: [inbox/fetch-2026-07-29-mavsdk.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# MAVSDK v3.17.2

MAVSDK는 MAVLink 프로토콜 기반의 고수준 드론 제어 SDK이다. Python, C++, Java 등 다양한 언어로 드론 애플리케이션을 개발할 수 있게 해준다.

## 핵심 특징

- **고수준 API**: MAVLink 메시지의 저수준 세부사항 추상화
- **크로스 플랫폼**: Linux, macOS, Windows, Android, iOS 지원
- **다중 언어**: C++, Python, Java, Swift, C# 등 바인딩 제공
- **비동기 지원**: async/await 패턴을 활용한 효율적인 제어

## 최신 릴리스: v3.17.2 (2026-07-17)

### 주요 변경사항

- v3 브랜치에 다양한 버그 수정 백포트

## 관련 개념

- [[mavlink-protocol]] — MAVSDK가 기반하는 프로토콜
- [[pymavlink]] — MAVLink의 Python 구현체
- [[px4-offboard-control]] — MAVSDK를 활용한 Offboard 제어
- [[mavros]] — ROS2와 MAVLink 간 브리지
