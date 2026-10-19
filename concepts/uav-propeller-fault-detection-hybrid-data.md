---
title: "UAV 프로펠러 고장 탐지: 하이브리드 데이터 생성 모델"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: hardware
tags: [drone, drone-hw, drone-ai]
sources: [inbox/processed/fetch-2026-10-17-arxiv-machine-learning-for-uav-propeller-fault-detection-based-on-.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 프로펠러 고장 탐지 (하이브리드 데이터 생성)

**출처**: arXiv 2302.01556 (2023-02-03)

쿼드로터의 고장 위치와 손상 정도를 온보드에서 데이터 기반으로 판별하는 시스템이다.^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-for-uav-propeller-fault-detection-based-on-.md]

## 방법
- 오프라인 학습 데이터를 데이터 기반 모델과 기구학/동역학 모델을 결합한 하이브리드 가상 생성 모델로 만든다. RPM을 입력으로 고장 상태별 추력·토크를 추정하는 LSTM 프로펠러 모델을 쓴다.^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-for-uav-propeller-fault-detection-based-on-.md]
- 시뮬레이션으로 생성한 비행 데이터로 CNN 고장 분류기를 학습해 고장 위치와 손상 정도를 구분한다.^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-for-uav-propeller-fault-detection-based-on-.md]
- 실내 실제 비행 데이터로 sim-to-real를 검증했고, 기체 제작 편차 때문에 시뮬레이션 모델의 약식 보정을 추가했다. 테스트 세트 진단 정확도는 80% 이상이다.^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-for-uav-propeller-fault-detection-based-on-.md]

## 관련
프로펠러 시험 연구는 [[multirotor-propeller-test-research]], 복합 고장 수용 제어는 [[kci-quadrotor-compound-fault-accommodation]] 참조.
