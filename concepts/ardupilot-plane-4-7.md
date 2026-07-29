---
title: ArduPilot Plane 4.7.0
created: 2026-07-29
updated: 2026-07-29
type: concept
tags: [drone, drone-sw, flight-control]
sources: [inbox/fetch-2026-07-29-ardupilot.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# ArduPilot Plane 4.7.0

ArduPilot Plane 4.7.0은 2026년 7월 21일에 안정 버전으로 릴리스된 ArduPilot의 고정익 및 VTOL 지원 버전이다.

## 릴리스 정보

- **릴리스 날짜**: 2026년 7월 21일
- **대상 기체**: 고정익(Fixed Wing) 및 VTOL
- **공식 발표**: https://discuss.ardupilot.org/t/plane-4-7-0-released/144663

## 주요 특징

ArduPilot Plane은 다음과 같은 고급 기능을 제공한다:

- **자동 이륙/착륙**: 정밀한 자동 이륙 및 착륙 경로 계획
- **VTOL 지원**: 쿼드플레인, 틸트로터 등 다양한 VTOL 구성
- **항법 시스템**: GPS, INS, 기압계 기반 정확한 위치 추정
- **지상 관제 통합**: [[mavlink-protocol]] 기반 GCS 연동

## 관련 개념

- [[ardupilot]] — ArduPilot 프로젝트 개요
- [[ardupilot-architecture]] — ArduPilot 소프트웨어 아키텍처
- [[mission-planner]] — ArduPilot 공식 GCS
- [[px4-flight-stack]] — ArduPilot의 대안 비행 스택
