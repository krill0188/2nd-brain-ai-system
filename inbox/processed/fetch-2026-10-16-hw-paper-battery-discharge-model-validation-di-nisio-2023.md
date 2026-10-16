---
title: "Battery Testing and Discharge Model Validation for Electric Unmanned Aerial Vehicles (UAV)"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://doi.org/10.3390/s23156937
tags: [drone, hardware, battery, lipo, endurance]
authors: Attilio Di Nisio, Giulio Avanzini, Daniel Lotano, Donato Stigliano, Anna M L Lanzolla
published: 2023-08-04, Sensors (Basel), vol. 23, issue 15, article 6937 (PMID 37571720, PMC10422487)
---

# 요약

리튬폴리머(LiPo) 배터리 팩의 경험적 방전 모델을 제안하고, 측정 장치로 정주파 부하와 가변 부하 방전을 시험해 검증한 논문이다. 모델은 정전력 데이터로 맞추고 가변 전력 방전을 예측하는 구조다.

# 핵심 내용

- 직렬 셀 수에 관계없는 LiPo 팩에 적용 가능한 경험식, 조정 파라미터는 적음.
- 시험 대상: Multistar 10.0 (10 Ah, 4S1P, 14.8 V 공칭).
- 정전력 시험 50/75/100/125 W, 2단계 시험 75/100 W, APRBS 시험 평균 전력 89.4~97.3 W 구간.
- 초록 기재: 예측 방전 용량의 정규화 오차 **0.7% 미만**.
- 내부저항 평균 20.68 mΩ (95% CI 20.07–21.29 mΩ).

# 설계에 쓸 수 있는 지침

- 체공시간 계산을 정격 용량 ÷ 평균 전력으로 단순화하면, 고전력 구간에서 가용 용량을 과대평가할 수 있다. 방전 곡선 기반 모델로 보정하는 근거로 쓸 수 있다.
- 시험 설계(정전력 → 2단계 → 가변 부하) 순서는 자체 배터리 특성화 시험 계획의 참고가 된다.
- 권장 방전 종지 기준(공칭 용량의 약 55%, 셀당 3.5 V 하한)은 본 논문 시험 조건이며 일반 기준이 아니다.

# 한계·미확인

- 셀별 정규화 오차·RMSE 값은 그림으로만 제시되어 **미확인**.
- 개별 시험의 예측/측정 방전 용량(Ah)은 **미확인**.
- 시험 대상이 단일 제품 한 종류라 다른 셀 화학계로의 일반화는 **미확인**.
