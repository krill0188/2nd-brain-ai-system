---
title: "멀티로터 전력·에너지 소비 모델 연구"
created: 2026-10-16
updated: 2026-10-21
type: concept
domain: hardware
ontology_class: Multirotor
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-paper-multirotor-power-model-gong-2022.md, inbox/processed/fetch-2026-10-16-hw-paper-forward-flight-efficiency-patnaik-2025.md, inbox/processed/fetch-2026-10-16-hw-paper-quadrotor-electrical-energy-model-honcharenko-2026.md, inbox/processed/fetch-2026-10-16-hw-paper-multicopter-energy-aware-framework-gasche-2025.md, inbox/processed/fetch-2026-10-16-hw-paper-battery-discharge-model-validation-di-nisio-2023.md, inbox/processed/fetch-2026-10-17-arxiv-energy-efficient-drone-logistics-for-last-mile-delivery-impl.md, inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md, inbox/processed/fetch-2026-10-18-arxiv-impact-of-spatial-proximity-on-drone-services.md, inbox/processed/fetch-2026-10-18-arxiv-physics-aware-truck-and-drone-delivery-planning-using-optimi.md, inbox/processed/fetch-2026-10-19-arxiv-a-modular-energy-aware-framework-for-multicopter-modeling-in.md, inbox/processed/fetch-2026-10-20-arxiv-agent-based-simulation-of-uav-battery-recharging-for-iot-app.md, inbox/processed/fetch-2026-10-20-arxiv-capsulebot-a-novel-hybrid-aerial-ground-bi-copter-robot-with.md, inbox/processed/fetch-2026-10-21-arxiv-perception-and-energy-aware-motion-planning-for-uav-using-le.md]
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

## 최신 근거 연결 (2026-10-17)

- 소비 에너지가 거리뿐 아니라 적재 중량에 의존한다는 전제 아래 다중 정차 배송을 최적화하면, 최소 거리 경로 대비 67% 사례에서 평균 2.17%(최대 5.97%) 절감되고 더 긴 경로가 유리할 수도 있다: [[payload-dependent-green-drone-routing]]^[inbox/processed/fetch-2026-10-17-arxiv-energy-efficient-drone-logistics-for-last-mile-delivery-impl.md]
- 방전 모델 외에 운용 데이터(전압·전류·스로틀)만으로 LiPo 잔여 용량(SoH)을 예측하는 전이학습 접근: [[uav-battery-soh-transfer-learning]]^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md]

## 최신 근거 연결 (2026-10-18)

- 드론 간 근접 비행의 위치·이격 거리·풍속 조건에서 스카이웨이 구간 에너지 소비 데이터를 수집하고 상호 에너지 영향을 분석하는 GUI를 만들었다(정량 결과는 초록에 없음): [[drone-proximity-energy-impact-delivery]]^[inbox/processed/fetch-2026-10-18-arxiv-impact-of-spatial-proximity-on-drone-services.md]
- 운동학·에너지 식을 포함한 궤적 최적화 해로 신경망을 학습해 비행 시간을 근사하고 트럭-드론 배송 계획에 넣으면, 비행 물리를 무시한 벤치마크보다 투어 시간과 드론 에너지 소비가 개선된다고 보고했다(초록 기준, 수치 없음): [[physics-aware-truck-drone-delivery-planning]]^[inbox/processed/fetch-2026-10-18-arxiv-physics-aware-truck-and-drone-delivery-planning-using-optimi.md]

## 최신 근거 연결 (2026-10-20)

- Gasche 외(2025)의 모듈식 모델은 수색구조 군집 경로계획 후속 연구의 기반으로 제시되며, 이종 군집의 기체별 모델링을 쉽게 한다고 주장한다(초록 기준, 정량 결과 없음): [[modular-energy-aware-multicopter-model]]^[inbox/processed/fetch-2026-10-19-arxiv-a-modular-energy-aware-framework-for-multicopter-modeling-in.md] — 위 "파워트레인·배터리 수준" 항목과 같은 논문이라 독립 근거가 아니며 `confidence`는 유지한다.
- 배터리 잔량이 아니라 재충전 정책 수준에서는, 드론 간 통신 없이 ChargerThreshold(CT) 정책이 30개 상황·6,000회 시뮬레이션에서 극단적 사용 조건에 더 안정적이었다(시뮬레이션만): [[uav-battery-recharge-agent-based-simulation]]^[inbox/processed/fetch-2026-10-20-arxiv-agent-based-simulation-of-uav-battery-recharging-for-iot-app.md]
- 바이콥터 4개 모터로 공중(틸트 로터)·지상(구동 바퀴) 추진을 겸하는 시제품이 낮은 소비전력을 확인했다고 보고한다(수치는 초록에 없음): [[capsulebot-hybrid-aerial-ground-bicopter]]^[inbox/processed/fetch-2026-10-20-arxiv-capsulebot-a-novel-hybrid-aerial-ground-bi-copter-robot-with.md]

## 최신 근거 연결 (2026-10-21)

- 에너지 모델을 계획에 직접 쓰는 사례: 수평 속도의 함수로 에너지 소비와 탑재 LiDAR 측정의 이분산 불확실성을 비행 전 시뮬레이션 데이터로 학습하고, 온라인 계획에서 배터리 사용량과 위치추정 오차를 함께 줄인다(GNSS 차단 환경, 시뮬레이션 검증, 초록 기준): [[perception-energy-aware-uav-lidar-motion-planning]]^[inbox/processed/fetch-2026-10-21-arxiv-perception-and-energy-aware-motion-planning-for-uav-using-le.md]
