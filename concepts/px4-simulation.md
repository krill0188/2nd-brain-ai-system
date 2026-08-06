---
title: PX4 Simulation (SITL)
created: 2026-08-06
updated: 2026-08-06
type: concept
tags: [drone-sw, PX4]
sources: []
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# PX4 Simulation (SITL)

PX4 SITL(Software-In-The-Loop)은 실제 비행 하드웨어 없이 PX4 flight stack 전체를 컴퓨터에서 실행해 제어 로직·튜닝·미션을 검증하는 시뮬레이션 환경이다. Gazebo 등 물리 엔진과 연동해 센서 데이터를 가상으로 생성한다.

## 활용

- **제어 파라미터 튜닝**: 실기 비행 전 PID/제어 게인 검증
- **미션 로직 테스트**: Offboard/자율 미션 코드 검증
- **CI/CD**: 펌웨어 변경 시 자동 회귀 테스트

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 구성
- [[px4-tuning-control]] — SITL 기반 제어 튜닝
