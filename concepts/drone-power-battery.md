---
title: Drone Power & Battery
created: 2026-07-27
updated: 2026-10-18
type: concept
tags: [drone-hw, battery, power, ESC, motor, LiPo]
sources: [raw/articles/px4-basic-concepts.md, raw/articles/px4-hardware-overview.md, raw/papers/_unclassified/소형-무인항공기용-리튬이온-배터리-등가회로모델-파라미터-추정에-관한-연구.md, raw/papers/_unclassified/전기-추진-시스템을-이용하는-고정익-무인기를-위한-복귀-가능-여부-판단-로직-설계.md, inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md, inbox/processed/fetch-2026-10-18-yt-i-exploded-a-lipo-in-a-600-safe-it-shot-flames.md]
confidence: high
domain: hardware
ontology_class: Battery
contested: true
contradictions: [lipo-charging-cabinet-fire-test]
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

## 차세대 셀 화학: 실리콘 음극

상용 LiPo 에너지 밀도(약 250–300 Wh/kg)를 넘어서는 차세대 경로로, 실리콘 음극(silicon
anode) 기반 셀이 부상하고 있다. 자세한 사양과 미국 정부 생산 보조금 동향은
[[amprius-sicore-battery]] 참조.

## 배터리 모델링과 잔여 에너지 예측 (KCI 2026)

소형 UAV용 Li-ion 등가회로모델(ECM)은 평형전위와 총 내부저항 파라미터의 정확도에 좌우되며, 가우스과정 회귀 대리모델로
30~50 V 검증 데이터에서 MAE 약 0.3 V·MAPE 1% 미만을 보고한 연구가 있다(저자 주장, 초록 기준).^[raw/papers/_unclassified/소형-무인항공기용-리튬이온-배터리-등가회로모델-파라미터-추정에-관한-연구.md]
고정익 UAV에서는 복귀점까지의 예상 에너지 소모로 도착 시 잔여 전압을 예측해 복귀 가능 여부를 판단하는 로직이 제안되었다.
^[raw/papers/_unclassified/전기-추진-시스템을-이용하는-고정익-무인기를-위한-복귀-가능-여부-판단-로직-설계.md] 단순 전압 임계값 failsafe를 넘어서는 예측형 접근이며, 두 논문의 결합은 해석이다. 상세는
[[kci-uav-battery-ecm-parameter-estimation]], [[kci-fixed-wing-return-feasibility-logic]] 참조.

## 관련 개념

- [[drone-safety-failsafe]] — 배터리 기반 failsafe
- [[kci-uav-battery-ecm-parameter-estimation]] — ECM 파라미터 추정(가우스과정 회귀)
- [[flight-controller-hardware]] — Power module 선택
- [[dronecan-protocol]] — CAN 기반 ESC
- [[amprius-sicore-battery]] — 차세대 실리콘-음극 셀(500 Wh/kg), LiPo 대비 1.5–2배 비행시간 연장 가능성

## 최신 근거 연결 (2026-10-17)

- 2200 mAh 342회·1100 mAh 289회 비행 데이터로 시계열을 이미지화해 ResNet-50 전이학습으로 SoH를 예측한 연구(구체 오차는 초록에 없음): [[uav-battery-soh-transfer-learning]]^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md]

## 상충 (2026-10-18)

- 위 "Fire Safe: 금속 상자" 항목에 대해, 충전 중 LiPo를 의도적으로 발화시킨 단일 시연에서 진행자는 금속 캐비닛만으로는 LiPo 화재를 막지 못하며 열이 금속을 통해 인접 물체를 발화시킬 수 있다고 설명했다. 이중 벽·온도 팬·소화 포드를 갖춘 캐비닛에서도 폭발이 반복되고 문 앞쪽으로 불꽃이 샜으며, 외부 온도는 약 57~60°C였다(자막 기반, 단일 제품·단일 시연, 일반화 곤란): [[lipo-charging-cabinet-fire-test]]^[inbox/processed/fetch-2026-10-18-yt-i-exploded-a-lipo-in-a-600-safe-it-shot-flames.md]
- 해석: 금속 상자 자체를 부정하는 근거는 아니다. 진행자도 이 캐비닛이 일반적인 사용자 방식보다 낫다고 결론 냈으며, 단일 시연이라 기존 기술을 뒤집지 않고 `contested`로만 표시한다.

## 📰 최근 관련 소식
- How to Choose FPV Drone Motors – Considerations and Best Motor Recommendations (oscarliang.com, Thu, 13 Au) — https://oscarliang.com/motors/
- How to Fix a Broken LiPo Battery Balance Connector Safely (oscarliang.com, Sat, 22 Au) — https://oscarliang.com/fix-balance-plug-lipo-replace/
- [Painless360] ToolkitRC B50 Battery Warming Bag, a perfect accessory for winter flying (youtube.com, 2026-09-09) — https://www.youtube.com/watch?v=HkTC_oOoIb4
