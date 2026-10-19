---
title: "SPINNER: 자가 회전 트라이로터 UAV"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: hardware
tags: [drone, drone-hw]
sources: [inbox/processed/fetch-2026-10-17-arxiv-a-self-rotating-tri-rotor-uav-for-field-of-view-expansion-an.md]
confidence: medium
contested: false
contradictions: []
---

# SPINNER: 자가 회전 트라이로터 UAV

**출처**: arXiv 2603.28581 (2026-03-30)

카메라·LiDAR 같은 탑재 센서의 좁은 화각(FoV)을 기체의 연속 회전(spin)으로 넓히는 트라이로터 SPINNER(Self-Perception INertial Navigation Enabled Rotorcraft)를 제안한다. 센서나 에너지 소비를 추가하지 않는다.^[inbox/processed/fetch-2026-10-17-arxiv-a-self-rotating-tri-rotor-uav-for-field-of-view-expansion-an.md]

## 설계·제어
- 브러시리스 모터 3개만으로 3차원 위치와 롤·피치 자세를 제어하고, 안티토크 플레이트로 회전 속도를 조절한다.^[inbox/processed/fetch-2026-10-17-arxiv-a-self-rotating-tri-rotor-uav-for-field-of-view-expansion-an.md]
- 회전 비행의 강한 결합·비선형성·외란은 비선형 MPC와 증분형 비선형 동적 역변환(INDI)을 결합한 외란 보상 제어로 다룬다.^[inbox/processed/fetch-2026-10-17-arxiv-a-self-rotating-tri-rotor-uav-for-field-of-view-expansion-an.md]

## 실험 결과
- 풍속 4.8 m/s까지 안정 비행, 최대 2.0 m/s 속도에서 고정밀 궤적 추종.^[inbox/processed/fetch-2026-10-17-arxiv-a-self-rotating-tri-rotor-uav-for-field-of-view-expansion-an.md]
- 주차장·숲 시험에서 회전 인식 방식이 FoV 커버리지와 인식 능력을 크게 개선했다.^[inbox/processed/fetch-2026-10-17-arxiv-a-self-rotating-tri-rotor-uav-for-field-of-view-expansion-an.md]

## 관련
INDI 안정성 사례는 [[indi-stability-tilt-rotor-vtol]], 기체·센서 하드웨어는 [[flight-controller-hardware]] 참조.
