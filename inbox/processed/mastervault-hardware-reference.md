---
title: "드론 하드웨어 레퍼런스"
created: 2026-07-27
captured: 2026-07-27
type: article
url: "file://MasterVault/Drone/Hardware/Hardware-Reference.md"
author: "Master (personal dev notes)"
sha256: ""
tags: [drone-hw]
---

# 드론 하드웨어 레퍼런스

## FC (Flight Controller)

### Holybro

| 모델 | 프로세서 | 특징 | 용도 |
|------|----------|------|------|
| Pixhawk 6X | STM32H753 | 최상위, 산업용 | 대형 드론 |
| Pixhawk 6X Pro | STM32H753 | 6X + 추가 센서 | 정밀 작업 |
| Pixhawk 6C | STM32H743 | 가성비 | 교육/개발 |
| Pixhawk 6C Mini | STM32H743 | 소형 | 레이서/소형기 |
| Kakute H7 | STM32H743 | FPV 특화 | FPV 레이서 |

### CUAV

| 모델 | 프로세서 | 특징 | 용도 |
|------|----------|------|------|
| V7+ | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 |
| X7+ Pro | STM32H753 | 최상위 | 대형/산업 |
| Nora+ | STM32H753 | 방열 우수 | 고온 환경 |
| 7-Nano | STM32H743 | 초소형 | 소형 기체 |

## GPS/RTK

| 제조사 | 모델 | 정밀도 | 비고 |
|--------|------|--------|------|
| Holybro | H-RTK F9P | RTK cm급 | u-blox ZED-F9P |
| Holybro | M9N | 1.5m | 일반용 |
| CUAV | C-RTK 9Ps | RTK cm급 | 기지국+이동국 |
| CUAV | NEO 3X | 1.5m | 일반용 |

## 텔레메트리

| 제조사 | 모델 | 범위 | 주파수 |
|--------|------|------|--------|
| Holybro | SiK V3 | ~1km | 433/915MHz |
| Holybro | Microhard | 수 km | 900MHz |
| CUAV | P9 | ~60km | 900MHz |
| CUAV | LTE Link | 무제한 | 4G LTE |

## 컴패니언 컴퓨터

| 모델 | 용도 | 연결 |
|------|------|------|
| Jetson Orin Nano | AI 추론 (YOLO) | UART/ETH |
| Raspberry Pi 5 | 경량 처리 | UART/USB |
| Holybro Jetson Baseboard | Jetson 마운트 | 전용 캐리어 |
