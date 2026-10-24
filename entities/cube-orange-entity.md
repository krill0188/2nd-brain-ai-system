---
title: "Cube Orange+"
created: 2026-10-24
updated: 2026-10-24
type: entity
tags: [hardware, pixhawk, flight-controller, imu, cube-orange]
sources: ["raw/articles/entity-pixhawk-hardware.md"]
confidence: medium
contradictions: []
domain: hardware
contested: false
---

# Cube Orange+

Cube Orange+는 CubePilot에 의해 생산된 비행 제어기로, 군집 운용과 방산용으로 검증된 **Cube Orange** 모델의 변종입니다. IMU가 3중화된 것이 특징이며, 고성능 STM32H757 기반의 오픈 하드웨어 비행 제어기입니다.

## 개요

Cube Orange+는 PX4 프로젝트와 호환되는 Pixhawk 표준 비행 제어기이며, CubePilot社에서 생산한 모델입니다. **IMU 3중화** 구조를 통해 신뢰성을 높였고, 군집(swarm) 운용 및 방산 분야에서 활용됩니다. Holybro, mRo, CubePilot 등 다양한 제조사가 Pixhawk 표준 호환 제품을 생산하는 가운데, Cube Orange+는 그중에서도 방산 및 고신뢰성 요구 사항을 충족하는 모델로 구분됩니다.

## 핵심 파라미터

| 사양 | 내용 |
|---|---|
| MCU | STM32H757 |
| 클럭 속도 | 480MHz |
| RAM | 1MB |
| 플래시 | 2MB |
| IMU 구조 | 3중화 |
| 주요 칩셋 | ICM-42688-P, ICM-20689 (가속도/자이로) |
| 자력계 | IST8310, RM3100 |
| 기압계 | MS5611, BMP388 |
| 전원 입력 | 4.75V ~ 5.25V |

## 활용처

- **군집(UAV Swarm) 운용**: 다체 협력 비행에 적합한 신뢰성 구조를 보유
- **방산용**: 검증된 성능으로 군용 및 방위 분야 적용
- **고신뢰성 임무**: IMU 3중화로 인한 데이터 신뢰성 요구 사항이 높은 상황

## 관련 페이지

- [[Cube Orange]] — Cube Orange+의 기반이 되는 기본 모델
- [[Pixhawk]] — Cube Orange+가 호환되는 비행 제어기 플랫폼 전체

## 출처

- (사용자 재확인 필요) original: raw/articles/entity-pixhawk-hardware.md

## 분류

- [[auto-hub-hardware]] — 자동 추출 분류
- [[auto-hub-source-articles]] — 출처 유형
