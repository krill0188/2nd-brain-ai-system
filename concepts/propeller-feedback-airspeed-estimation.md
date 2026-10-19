---
title: "프로펠러 피드백만으로 고정익 대기속도 추정 (Ntouros 외, 2025)"
created: 2026-10-19
updated: 2026-10-19
type: concept
domain: flight-control
tags: [drone, drone-hw, drone-sw]
sources: [inbox/processed/fetch-2026-10-19-arxiv-airspeed-estimation-for-uavs-using-only-propeller-feedback.md]
confidence: medium
contested: false
contradictions: []
---

# 프로펠러 피드백 기반 대기속도 추정

피토관 없이 프로펠러 전력과 회전속도만으로 고정익 UAV의 대기속도를 추정하는 해석 모델이다(arXiv 2507.03456, 2025-07). 초록 기준 요약이다.^[inbox/processed/fetch-2026-10-19-arxiv-airspeed-estimation-for-uavs-using-only-propeller-feedback.md]

## 핵심 내용
- 기체 동역학 모델이 필요 없고 계산이 가볍다. 입력은 최신 ESC가 제공하는 전력·회전수 피드백이다.
- BEM(블레이드 요소 운동량) 시뮬레이션, 풍동, 비행시험 데이터에 최소제곱·정규화를 적용해 모델 구조를 유도했다.
- 미학습 비행 데이터에서 nRMSE 약 5%를 보고한다.
- 파라미터는 대기속도가 있는 비행로그로 오프라인 식별하거나, GPS 속도만으로 비행 중 식별할 수 있다.
- 피토관 대체 또는 중복(redundancy) 용도로 제안된다.

## 연결
프로펠러 시험 근거는 [[multirotor-propeller-test-research]], ESC 특성은 [[bldc-motor-esc-characterization-research]] 참조.
