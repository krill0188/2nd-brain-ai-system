---
title: Flight Controller Hardware
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-hw, flight-controller, FC, hardware, Pixhawk]
sources: [raw/articles/mastervault-hardware-reference.md, raw/articles/px4-hardware-overview.md]
confidence: high
domain: hardware
contested: false
contradictions: []
---

# Flight Controller Hardware

Flight Controller(FC)는 드론의 "두뇌"로, RTOS에서 비행 스택 소프트웨어를 실행하는 전용 하드웨어다. 센서를 통해 상태를 판단하고 액추에이터로 기체를 제어한다.^[raw/articles/px4-hardware-overview.md]

## 구성요소 카테고리

| 카테고리 | 구성요소 |
|---------|---------|
| **Flight Systems** | FC, 펌웨어, 부트로더 |
| **Sensing** | IMU, Compass, Barometer, GPS, RTK, Optical Flow |
| **Motor & Control** | ESC, 모터, 서보, 액추에이터 |
| **Communication** | RC 수신기, 텔레메트리 라디오, 조이스틱 |
| **Power** | LiPo 배터리, PDB, 스마트 배터리 |
| **Payload** | 카메라, 짐벌, 그리퍼, 낙하산 |

## 주요 FC 제조사

### Holybro

| 모델 | 프로세서 | 특징 | 용도 |
|------|----------|------|------|
| **Pixhawk 6X** | STM32H753 | 최상위, 산업용 | 대형 드론 |
| **Pixhawk 6X Pro** | STM32H753 | 6X + 추가 센서 | 정밀 작업 |
| **Pixhawk 6C** | STM32H743 | 가성비 | 교육/개발 |
| **Pixhawk 6C Mini** | STM32H743 | 소형 | 레이서/소형기 |
| **Kakute H7** | STM32H743 | FPV 특화 | FPV 레이서 |

### CUAV

| 모델 | 프로세서 | 특징 | 용도 |
|------|----------|------|------|
| **V7+** | STM32H753 | 3중 IMU, 산업용 | 군집정찰 메인 |
| **X7+ Pro** | STM32H753 | 최상위 | 대형/산업 |
| **Nora+** | STM32H753 | 방열 우수 | 고온 환경 |
| **7-Nano** | STM32H743 | 초소형 | 소형 기체 |

## 필수 센서

### IMU (Inertial Measurement Unit)

| 센서 | 기능 |
|------|------|
| **Accelerometer** | 가속도 측정 |
| **Gyroscope** | 각속도 측정 |
| **Compass (Magnetometer)** | 방향/자기북 측정 |
| **Barometer** | 고도 측정 (기압) |

> **참고**: Pixhawk 보드에 내장됨

## GPS/내비게이션

| 제조사 | 모델 | 정밀도 | 특징 |
|--------|------|--------|------|
| **Holybro** | H-RTK F9P | RTK cm급 | u-blox ZED-F9P |
| **Holybro** | M9N | 1.5m | 일반용 |
| **CUAV** | C-RTK 9Ps | RTK cm급 | 기지국+이동국 |
| **CUAV** | NEO 3X | 1.5m | 일반용 |

## 텔레메트리 라디오

| 제조사 | 모델 | 범위 | 주파수 |
|--------|------|------|--------|
| **Holybro** | SiK V3 | ~1km | 433/915MHz |
| **Holybro** | Microhard | 수 km | 900MHz |
| **CUAV** | P9 | ~60km | 900MHz |
| **CUAV** | LTE Link | 무제한 | 4G LTE |

## 컴패니언 컴퓨터

| 모델 | 용도 | 연결 |
|------|------|------|
| **Jetson Orin Nano** | AI 추론 (YOLO) | UART/ETH |
| **Raspberry Pi 5** | 경량 처리 | UART/USB |
| **Holybro Jetson Baseboard** | Jetson 마운트 | 전용 캐리어 |

## 출력 포트

Flight Controller는 **MAIN**과 **AUX** 출력 포트를 갖는다 (일반적으로 6-8개씩).^[raw/articles/mastervault-hardware-reference.md]

| 출력 | 용도 |
|------|------|
| **MAIN** | 주 모터/서보 |
| **AUX** | 보조 기능 (짐벌, 페이로드 등) |

**연결 방식**:
- PWM 포트
- DroneCAN 노드

## ESC & 모터

- **BLDC 모터**: 무블러시 DC 모터
- **ESC**: FC 신호를 모터 전력 레벨로 변환
- **연결**: PWM, DroneCAN

## 전원 시스템

```
LiPo Battery → Power Module/Board → FC
                        ↓
                     ESCs → Motors
```

| 구성요소 | 설명 |
|---------|------|
| **LiPo** | 리튬 폴리머 배터리 |
| **Power Module** | 배터리→FC/ESC 전원 분배 |
| **Smart Battery** | BMS 내장, 상태 모니터링 |

## FC 선택 가이드

| 요구사항 | 권장 FC |
|---------|---------|
| 산업/대형 드론 | Pixhawk 6X, CUAV X7+ Pro |
| 교육/개발 | Pixhawk 6C |
| FPV/레이서 | Kakute H7, Pixhawk 6C Mini |
| 고온 환경 | CUAV Nora+ |
| 군집 비행 | CUAV V7+ |

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 구성
- [[ardupilot-architecture]] — ArduPilot 지원 하드웨어
- [[dronecan-protocol]] — CAN 버스 주변기기 연결
- [[companion-computer]] — 고급 처리용 보조 컴퓨터
