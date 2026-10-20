---
title: "BLDC 모터·ESC 특성 측정·모델링 연구 (효율·열·추력 모델)"
created: 2026-10-16
updated: 2026-10-20
type: concept
domain: hardware
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-paper-esc-motor-efficiency-characterization-brown-2019.md, inbox/processed/fetch-2026-10-16-hw-paper-bldc-inverter-electro-thermal-cheng-2021.md, inbox/processed/fetch-2026-10-16-hw-paper-digital-twin-bldc-gauthier-2023.md, inbox/processed/fetch-2026-10-16-hw-paper-motor-efficiency-estimation-cheng-2025.md, inbox/processed/fetch-2026-10-16-hw-paper-thrust-estimation-bemt-santos-2024.md, inbox/processed/fetch-2026-10-17-arxiv-a-robust-sensorless-controller-observer-strategy-for-pmsms-w.md, inbox/processed/fetch-2026-10-17-arxiv-how-to-model-your-crazyflie-brushless.md, inbox/processed/fetch-2026-10-20-arxiv-digital-twin-of-a-dc-brushless-electric-motor-propeller-syst.md, inbox/processed/fetch-2026-10-19-arxiv-airspeed-estimation-for-uavs-using-only-propeller-feedback.md]
confidence: medium
contested: false
contradictions: []
---

# BLDC 모터·ESC 특성 측정·모델링 연구

추진계 효율에서 ESC 손실, 열, 비선형 추력 응답을 다룬 논문 5편의 종합이다. 대부분 초록 수준 확인이라 정량 오차 값은 인용하지 않았다.

## ESC 효율과 열
- Brown(2019, 학위논문): 동력계로 920~2500 KV 모터, 18/30/40 A ESC, 7.2/11.1/14.8 V 조건을 측정했고 ESC 효율이 65%까지 낮을 수 있다고 보고한다. 동료 심사 논문은 아니다.^[inbox/processed/fetch-2026-10-16-hw-paper-esc-motor-efficiency-characterization-brown-2019.md]
- Cheng 외(2021): 3상 MOSFET 인버터의 전기-열 결합 모델에서 손실이 25 °C 약 99.9 W에서 200 °C 약 108.4 W로 증가하고, 자연대류 접합 온도 약 152~160 °C가 강제대류에서 약 135 °C로 낮아졌다. 소형 드론 ESC가 아닌 일반 BLDC 인버터 대상이다.^[inbox/processed/fetch-2026-10-16-hw-paper-bldc-inverter-electro-thermal-cheng-2021.md]

## 추력 모델
- Gauthier 외(2023): 역기전력, 프로펠러 항력, 권선 L/R 지연을 포함한 정지 추력 디지털 트윈. sensorless ESC에서 추력이 PWM의 비선형 함수이며 저 PWM 영역에서 두드러진다. 열 모델은 미포함.^[inbox/processed/fetch-2026-10-16-hw-paper-digital-twin-bldc-gauthier-2023.md]
- Santos 외(2024): 회전속도² 비례 모델이 비호버 조건에서 부정확하다는 문제를 BEMT 기반 폐루프 추정기로 풀었다. 벤치 1회 실험으로 단일 스케일링 값을 얻고 250/500 mm 플랫폼에서 실외 검증.^[inbox/processed/fetch-2026-10-16-hw-paper-thrust-estimation-bemt-santos-2024.md]
- Cheng & Cheng(2025, 프리프린트): 슬라이딩 윈도우 잔차 최소화로 비행 중 모터 효율을 추정. 시뮬레이션만 수행했고 모터 클리핑 구간에서 EKF보다 스파이크가 작다고 정성적으로 보고한다.^[inbox/processed/fetch-2026-10-16-hw-paper-motor-efficiency-estimation-cheng-2025.md]

## 설계 시사점
추진계 효율은 모터 단독이 아니라 ESC 손실을 별도 항목으로 두고, 추력 보정은 호버점 하나가 아니라 PWM 전 구간에서 해야 한다는 점이 반복된다. 고장 사례는 [[drone-esc-failure-cases]], 에너지 모델은 [[multirotor-energy-power-models]]를 참고한다.

관련: [[drone-hw]], [[fpv-motor-selection-guide]], [[px4-control-tuning]].

## 최신 근거 연결 (2026-10-17)

- 센서리스 PMSM 제어기-관측기 연구는 UAV 프로펠러 제어를 가정했으나 검증이 수치 시뮬레이션에 그쳐 하드웨어 측정 중심인 위 결과와 성격이 다르다: [[pmsm-sensorless-controller-observer]]^[inbox/processed/fetch-2026-10-17-arxiv-a-robust-sensorless-controller-observer-strategy-for-pmsms-w.md]
- Crazyflie Brushless(브러시드 대비 추력 약 50% 큼)의 동역학 모델 식별과 sim-to-real 전이 사례: [[crazyflie-brushless-dynamics-model]]^[inbox/processed/fetch-2026-10-17-arxiv-how-to-model-your-crazyflie-brushless.md]

## 최신 근거 연결 (2026-10-20)

- **강화(같은 논문의 추가 세부)**: 위 Gauthier 외(2023) 항목의 정지 추력 디지털 트윈은 KDE2315XF-885(885 Kv)+945 프로펠러와 Holybro ESC로 구동한 AIR 2216(880 Kv)+1045 프로펠러 실측과 비교했고, 정상상태와 과도 응답 모두 문헌의 선형화 모델과 상당히 어긋났다고 초록이 밝힌다: [[bldc-motor-propeller-digital-twin-static-thrust]]^[^[inbox/processed/fetch-2026-10-20-arxiv-digital-twin-of-a-dc-brushless-electric-motor-propeller-syst.md]] — 동일 논문의 재수집이라 독립 반복 검증이 아니며 `confidence`는 올리지 않는다.
- 최신 ESC가 주는 전력·회전수 피드백만으로 고정익 대기속도를 추정(미학습 비행 데이터 nRMSE 약 5%)하는 연구는 ESC 텔레메트리를 추정 센서로 쓰는 사례다(초록 기준, 고정익 대상): [[propeller-feedback-airspeed-estimation]]^[^[inbox/processed/fetch-2026-10-19-arxiv-airspeed-estimation-for-uavs-using-only-propeller-feedback.md]]
