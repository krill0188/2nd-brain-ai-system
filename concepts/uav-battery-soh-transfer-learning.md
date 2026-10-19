---
title: "UAV 배터리 SoH 예측: 전이학습 기반 예지 정비"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: hardware
tags: [drone, drone-hw, drone-ai]
sources: [inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 배터리 SoH 예측 (전이학습)

**출처**: arXiv 2607.06791 (2026-07-07)

UAV 배터리 SoH(state of health)는 데이터가 부족하고 변동이 커 연구가 적은 영역이다. 배터리 종류가 다양하고 경량화 요구로 센서 입력도 제한된다.^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md]

## 방법
- 2200 mAh LiPo 342회, 1100 mAh LiPo 289회 비행 실험으로 운용 데이터를 수집했다. 입력 특징은 전압·전류·스로틀이며, 10회 실험마다 잔여 용량을 측정해 라벨링했다.^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md]
- 시계열을 이미지로 변환해 사전학습 ResNet-50의 특징 추출 능력을 활용하고, 두 배터리 종류 간 전이학습으로 데이터 부족을 완화했다.^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md]
- 결과적으로 정확한 SoH 예측 모델을 얻었다고 보고한다(구체 오차 수치는 초록에 없음).^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-based-battery-state-of-health-prediction-fo.md]

## 관련
배터리 일반은 [[drone-power-battery]], 전기 파라미터 추정 연구는 [[kci-uav-battery-ecm-parameter-estimation]] 참조.
