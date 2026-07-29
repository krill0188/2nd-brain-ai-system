---
title: Drone Power & Battery
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-hw, battery, power, ESC, motor, LiPo]
sources: [raw/articles/px4-basic-concepts.md, raw/articles/px4-hardware-overview.md]
confidence: high
domain: hardware
contested: false
contradictions: []
---

# Drone Power & Battery

드론 전원 시스템은 LiPo 배터리에서 시작하여 ESC, 모터, FC에 분배되는 전력 인프라다. 안전하고 효율적인 전원 관리는 비행 시간과 기체 안전에 직접적인 영향을 미친다.

## 시스템 구성

```
┌─────────────────────────────────────────┐
│           LiPo Battery               │
│        3S/4S/6S (11.1V-22.2V)         │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴───────┐
       ▼               ▼
┌─────────────┐   ┌─────────────┐
│ Power Module│   │   ESCs      │
│ (BEC 5V)    │   │ (Motor)     │
└──────┬──────┘   └─────────────┘
       │
┌──────┴──────┐
│ Flight      │
│ Controller  │
│ (5V)        │
└─────────────┘
```

## LiPo Battery

Lithium-Polymer 배터리는 대부분의 PX4 드론에 사용된다.^[raw/articles/px4-basic-concepts.md]

### 셀 구성

| 구성 | 전압 | 용도 |
|------|------|------|
| **2S** | 7.4V | 소형 드론 |
| **3S** | 11.1V | 450-550mm 쿼드 |
| **4S** | 14.8V | 550-650mm, 레이서 |
| **6S** | 22.2V | 대형 드론, X8 |

### 용량 & C-rate

| 파라미터 | 설명 | 예시 |
|----------|------|------|
| **Capacity** | mAh 단위 저장 용량 | 5000mAh |
| **C-rate** | 방전률 (배수) | 25C, 50C |
| **Burst C** | 순간 최대 방전 | 100C |

**최대 전류 계산**: 5000mAh × 50C = 250A

## ESC (Electronic Speed Controller)

BLDC 모터를 제어하는 전자식 속도 제어기.^[raw/articles/px4-basic-concepts.md]

| 특성 | 설명 |
|------|------|
| **Input** | PWM / DroneCAN / DShot |
| **Output** | 3상 AC (모터) |
| **BEC** | 5V/12V 출력 (FC/서보용) |
| **Rating** | 지속 전류 (A) |

### ESC 선택

| 모터 크기 | 추천 ESC |
|-----------|----------|
| 22xx | 20-30A |
| 28xx | 30-40A |
| 35xx | 40-60A |
| X8 | 60A+ |

### ESC 프로토콜

| 프로토콜 | 특성 |
|----------|------|
| **PWM** | 기본, 50-400Hz |
| **OneShot** | 125μs, 저지연 |
| **DShot** | 디지털, 150-1200 |
| **DroneCAN** | CAN 버스, 양방향 |

## Power Module

배터리 전원을 분배하고 전류/전압을 측정하는 모듈.^[raw/articles/px4-hardware-overview.md]

| 기능 | 설명 |
|------|------|
| **Power Distribution** | ESC/FC에 전원 분배 |
| **Voltage Sensing** | 배터리 전압 ADC |
| **Current Sensing** | 소비 전류 측정 |
| **BEC** | 5V/12V 정전압 출력 |

### Holybro PM02/PM06/PM07

| 모델 | 최대 전류 | BEC |
|------|-----------|-----|
| PM02 | 60A | 5V 3A |
| PM06 | 120A | 5V 5A |
| PM07 | 120A | 5V 5A, 12V 2A |

## Battery Estimation

PX4는 전압 기반 + 전류 기반 추정을 결합한다.

```
Remaining % = f(Voltage, Current, Temperature, Cycle count)
```

### 파라미터 튜닝

| 파라미터 | 설명 |
|----------|------|
| `BAT_V_DIV` | 전압 분배기 비율 |
| `BAT_A_PER_V` | 전류 센서 스케일 |
| `BAT_CAPACITY` | 배터리 용량 (mAh) |
| `BAT_CRIT_THR` | Critical threshold |
| `BAT_LOW_THR` | Low threshold |
| `BAT_EMERGEN_THR` | Emergency threshold |

## Smart Battery

SMBus/I2C 통신을 통한 지능형 배터리 관리.

| 기능 | 설명 |
|------|------|
| **Cycle Count** | 충방전 사이클 |
| **State of Health** | 배터리 건강도 |
| **Remaining Capacity** | 정확한 잔량 |
| **Temperature** | 셀 온도 |

## 충전 & 보관

### 충전

| 단계 | 전압 | 전류 |
|------|------|------|
| **CC** | 상승 중 | 1C |
| **CV** | 4.2V/cell | 감소 |
| **Cutoff** | 4.2V/cell | 0.1C |

### 보관

- **Storage Voltage**: 3.8V/cell (약 50%)
- **Temperature**: 15-25°C
- **Humidity**: 낮은 습도
- **Fire Safe**: 금속 상자 또는 LiPo bag

## 안전 고려사항

| 위험 | 대응 |
|------|------|
| **Over-discharge** | 3.0V/cell 이하 방지 |
| **Over-charge** | 4.2V/cell 이상 방지 |
| **Short circuit** | 보호 회로, fuse |
| **Thermal runaway** | 방화 케이스, 감시 |

## 관련 개념

- [[drone-safety-failsafe]] — 배터리 기반 failsafe
- [[flight-controller-hardware]] — Power module 선택
- [[dronecan-protocol]] — CAN 기반 ESC
