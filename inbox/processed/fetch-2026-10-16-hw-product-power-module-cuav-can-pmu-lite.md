---
title: "CAN PMU Lite Power Management Module"
created: 2026-10-16
captured: 2026-10-16
type: product
domain: hardware
ontology_class: Battery
category: power-module
manufacturer: CUAV
source: https://store.cuav.net/shop/can-pmu-lite/
tags: [drone, hardware, product, power-module]
---

# CAN PMU Lite Power Management Module — CUAV

## 핵심 사양 (공식 페이지 게재값)

| 항목 | 값 |
|---|---|
| 입력 전압 | 10–60V (두 번째 사양표 기재: 10–62V, 2–15S LiPo) |
| 5V 출력 | Maximum 5A, stable 4A |
| 출력 전력 | 5.2V/4A, 최대 21W |
| 최대 전류 | 90A (기능 목록: 최대 110A) |
| 전압 정확도 | ±0.15V |
| 전류 정확도 | ±0.2A (80A 이내) |
| 분해능 | 0.01A/V |
| 최대 출력 전력 | 4200W/90S |
| 최대 안정 출력 전력 | 3600W |
| 크기 | 140 × 25 × 13mm |
| 무게 | 미확인 |
| 동작 온도 | -20 ~ 100℃ |
| 프로세서 | STM32F103CEU6 (본문: STM32F412) |

## 용도

- CAN 버스 기반 전원 관리·전압·전류 측정 (UAVCAN 프로토콜)

## 호환·인터페이스

- 프로토콜: UAVCAN
- 커넥터: IN/OUT XT60-M / XT60-F, Power/CAN 502585-0670, Other SM06B-GHS-TB
- ArduPilot: Rover 3.5.1+, Copter 3.7+, Plane 3.10+, Heli 3.7+
- PX4: PX4 Pro V1.10.1 이상

## 비고

- 페이지 표기 "Out of stock" (수집 시점 재고 없음)
- 사양이 페이지 내에서 상충: 입력 전압, 최대 전류, 프로세서 → 구매 전 제조사(info@cuav.net) 확인 권장
- 수집 방식: 공식 스토어 페이지 확인(2026-10-16). WebFetch 요약 기준.
- 출처 신뢰도: 중간 (수치 상충)
