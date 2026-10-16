---
title: "멀티로터 전력·에너지 소비 모델 연구"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: hardware
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-paper-multirotor-power-model-gong-2022.md, inbox/processed/fetch-2026-10-16-hw-paper-forward-flight-efficiency-patnaik-2025.md, inbox/processed/fetch-2026-10-16-hw-paper-quadrotor-electrical-energy-model-honcharenko-2026.md, inbox/processed/fetch-2026-10-16-hw-paper-multicopter-energy-aware-framework-gasche-2025.md, inbox/processed/fetch-2026-10-16-hw-paper-battery-discharge-model-validation-di-nisio-2023.md]
confidence: medium
contested: false
contradictions: []
---

# 멀티로터 전력·에너지 소비 모델 연구

비행 모드별 전력 모델, 파워트레인 모델, 배터리 방전 모델을 다룬 논문 5편의 종합이다.

## 비행 역학 수준
- Gong 외(2022): 전진·수직 상승·수직 하강의 폐쇄형 전력 모델을 유도하고 DJI M210 + Mobile SDK 실비행으로 검증했다. 호버링이 최적 속도 전진보다 전력이 더 높고, 고속(>15 m/s)·강풍·ESC 손실 포함 여부는 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-multirotor-power-model-gong-2022.md]
- Patnaik 외(2025): 옥토로터에서 에너지 최적 전진 속도 v*의 에너지 효율 지수와 피치각이 페이로드 포함 질량과 무관하게 일정하다는 해석적 결과. 실비행 검증 없음.^[inbox/processed/fetch-2026-10-16-hw-paper-forward-flight-efficiency-patnaik-2025.md]

## 파워트레인·배터리 수준
- Honcharenko & Yesilevskyi(2026): 2차 Thevenin 배터리 + ESC + 1차 모터 모델을 결합해 상수 전압 기준 대비 최대 21% 에너지 감소를 보고(초록 기재). 오차 지표는 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-quadrotor-electrical-energy-model-honcharenko-2026.md]
- Gasche 외(2025): 동역학·에너지·파워트레인(Li-ion, ESC, BLDC)을 모듈화한 프레임워크를 시험비행 데이터로 검증했다고 초록에 기술. 오차 수치는 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-multicopter-energy-aware-framework-gasche-2025.md]
- Di Nisio 외(2023): Multistar 10 Ah 4S LiPo의 경험적 방전 모델을 정전력(50~125 W)·2단계·APRBS 부하로 검증, 예측 방전 용량 정규화 오차 0.7% 미만, 내부저항 평균 20.68 mΩ. 단일 제품 시험이라 다른 화학계 일반화는 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-battery-discharge-model-validation-di-nisio-2023.md]

## 시사점
체공시간 견적을 정격 용량 ÷ 평균 전력으로 단순화하면 고전력 구간에서 가용 용량을 과대평가할 수 있다. 배터리 내부저항과 ESC 손실을 포함한 모델이 초기 견적에 유리하다.

관련: [[drone-power-battery]], [[bldc-motor-esc-characterization-research]], [[multirotor-propulsion-sizing-methods]], [[uav-battery-replacement-planner]].
