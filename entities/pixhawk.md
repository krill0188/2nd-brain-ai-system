---
title: Pixhawk
created: 2026-07-28
updated: 2026-07-28
type: entity
tags: [drone-hw, drone-sw]
sources:
  - raw/articles/pixhawk-flight-controller-entity-reference.md
confidence: high
domain: hardware
contested: false
contradictions: []
---

# Pixhawk

Pixhawk는 PX4 프로젝트와 함께 개발된 오픈 하드웨어 비행 제어기(FC) 플랫폼이다.

## 주요 특징

- **표준 문서**: https://github.com/pixhawk/Pixhawk-Standards
- **주요 제조사**: Holybro (공식), CubePilot, mRo Technology
- **버스 표준**: UAVCAN/DroneCAN, UART, SPI, I2C, CAN

## 주요 모델

| 모델 | MCU | RAM | 플래시 | 특징 |
|---|---|---|---|---|
| Pixhawk 1 | STM32F427 | 168MHz / 256KB | 2MB | 초기 레퍼런스, 단종 |
| Pixhawk 4 | STM32F765 | 216MHz / 512KB | 2MB | Holybro 공식, 현 주력 |
| Pixhawk 6C | STM32H743 | 480MHz / 1MB | 2MB | 최신 고성능 |
| Pixhawk 6X | STM32H753 | 480MHz / 1MB | 2MB | 6C 상위 (이중화) |
| Cube Orange | STM32H757 | 480MHz / 1MB | 2MB | CubePilot, 방산 검증 |
| Cube Orange+ | STM32H757 | 480MHz / 1MB | 2MB | IMU 3중화, 군집 사용 |

## 내장 센서

| 센서 | 역할 | 대표 칩 |
|---|---|---|
| IMU (가속도+자이로) | 자세·가속도 측정 | ICM-42688-P, ICM-20689 |
| 자력계(Compass) | 자북 방향 측정 | IST8310, RM3100 |
| 기압계 | 고도 측정 | MS5611, BMP388 |
| 온도 센서 | IMU 열보정 | 내장 |

Pixhawk 6X는 IMU 3개, 자력계 2개 내장 (이중화)한다.

## 커넥터 표준

| 커넥터 | 용도 | 신호 |
|---|---|---|
| TELEM1/2 | MAVLink 텔레메트리 | UART + 5V |
| GPS1/2 | GPS + 나침반 | UART + I2C + 5V |
| I2C | 외부 나침반·거리센서 | I2C |
| CAN1/2 | DroneCAN 장치 | CAN 버스 |
| RC IN | RC 수신기 | PPM/SBUS/DSM |
| MAIN OUT | 주 모터·서보 | PWM |
| AUX OUT | 보조 모터·서보 | PWM / GPIO |
| USB | 설정·펌웨어 업로드 | USB Full Speed |
| SPI | 고속 외부 센서 | SPI |
| POWER1/2 | 전원 모니터 | 전압·전류 ADC |

## 전원 요구사항

| 항목 | 사양 |
|---|---|
| 공급 전압 | 4.75 ~ 5.25V (USB: 4.5~5.5V) |
| 소비 전류 | 약 250~500mA (부하 따라 상이) |
| 배터리 셀 수 | 2~14S (ESC·PDB 경유) |
| 이중 전원 입력 | POWER1 + POWER2 (Pixhawk 6X) |

## DroneCAN 연동

Pixhawk는 DroneCAN을 통해 ESC, GPS, 기타 주변 장치와 통신한다.

## 관련 페이지

- [[px4-flight-stack]] — Pixhawk에서 주로 구동되는 비행 스택
- [[ardupilot]] — Pixhawk에서 실행 가능한 대안 비행 스택
- [[dronecan-protocol]] — Pixhawk CAN 버스 통신 프로토콜
- [[mavlink-protocol]] — 지상국 통신 프로토콜
