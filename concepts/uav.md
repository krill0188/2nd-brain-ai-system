---
title: "Uav"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [drone, autopilot, px4, unmanned-aerial-vehicle, multicopter, fixed-wing]
sources: [px4-basic-concepts.md]
confidence: medium
contested: false
contradictions: []
domain: hardware
---

# Uav

**Uav(Unmanned Aerial Vehicle)**는 사람이 직접 조종하거나 자율 비행 모드로 운영되는 무인 비행 로봇 항공기를 의미하며, PX4 기반 자율비행 시스템의 핵심 플랫폼이 됩니다.

Uav은 multicopter, helicopter, fixed-wing aircraft 등 비행 형태에 따라 다양한 유형으로 분류되며, 멀티콥터는 정밀한 호버링과 수직 이륙이 가능하지만 비행 지속 시간이 제한되는 반면, 고정익 항공기는 지상 조사에 적합한 장거리·고속 비행을 지원하지만 정지 비행이 어렵습니다. 또한 VTOL은 multicopter의 호버링과 고정익의 효율을 결합한 하이브리드 시스템입니다. Uav은 GPS 신호가 차단된 환경에서도 시각 SLAM, 지피디(Double-denied Navigation) 등 다양한 네비게이션 기술을 활용해 운용될 수 있습니다.

## 활용처

- 항공 사진 촬영 및 측량
- 화물 수송
- 레이스 및 서치 앤드 레스큐(SAR) 작전
- 드론 스웜(무인기 군집) 운영

## 관련 페이지

- [[Visual Slam]] — Uav이 GPS-Denied 환경에서 위치 추정 및 네비게이션에 활용되는 기술
- [[Gps-Denied Navigation]] — GPS 신호가 없는 환경에서 Uav이 자율 비행하는 네비게이션 기법
- [[Fpga]] — Uav onboard 시스템에 통합되어 실시간 신호 처리 및 제어에 사용되는 하드웨어 플랫폼
- [[Rf Channel]] — Uav 간 및 GCS(지상국) 간의 통신에 사용되는 무선 주파수 링크
- [[Multi-Agent System]] — 다수의 Uav이 협력하여 임무를 수행하는 시스템 구조

## 출처

- (사용자 재확인 필요) original: px4-basic-concepts.md

## 분류

- [[auto-hub-concept]] — 자동 추출 분류
- [[auto-hub-source-articles]] — 출처 유형
