---
title: Betaflight
created: 2026-07-29
updated: 2026-07-29
type: concept
tags: [drone, drone-sw, flight-control]
sources: [inbox/fetch-2026-07-29-betaflight.md]
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# Betaflight

Betaflight는 FPV(First Person View) 드론과 소형 레이싱 드론을 위한 오픈소스 비행 제어 소프트웨어이다. 주로 멀티콥터에 사용되며, 직관적인 설정 인터페이스와 높은 커스터마이징 가능성으로 인해 FPV 커뮤니티에서 널리 사용된다.

## 핵심 특징

- **실시간 설정**: Betaflight Configurator를 통해 GUI 기반 설정 가능
- **PID 튜닝**: 고급 PID 제어기 설정으로 비행 특성 미세 조정
- **안전 기능**: Arming 조건, failsafe, 모터 정지 등 다양한 안전 메커니즘
- **하드웨어 호환성**: 다양한 FC(Flight Controller) 보드 지원

## 최신 릴리스 (2025.12.5)

2026년 6월 28일 릴리스된 2025.12.5 버전에서는 다음과 같은 수정사항이 포함되었다:

- UART RXNEIE 활성화 시 ORE(Overrun Error) 클리어 수정
- MSP 프로토콜에서 per-byte lastActivityMs 복원

## 관련 개념

- [[flight-controller-hardware]] — Betaflight가 실행되는 FC 하드웨어
- [[drone-safety-failsafe]] — Arming 및 failsafe 메커니즘
- [[px4-flight-stack]] — Betaflight와 비교되는 다른 오픈소스 비행 스택
