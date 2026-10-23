---
title: "Vision-only UAV State Estimation for Fast Flights Without External Localization Systems: A2RL Drone Racing Finalist Approach"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: navigation-gnss-denied
ontology_class: GNSSDeniedNavigation
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]
confidence: medium
contested: false
contradictions: []
---

# Vision-only UAV State Estimation for Fast Flights Without External Localization Systems: A2RL Drone Racing Finalist Approach

- 원문: https://arxiv.org/abs/2602.01860^[inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]
- 저자: Filip Novak, Matej Petrlik, Matej Novosad, Parakh M. Gupta, Robert Penicka, Martin Saska^[inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]
- 발행: 2026-02-02 (arXiv, cs.RO)^[inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]

## 핵심 내용
단안 RGB 카메라 1대와 IMU만으로 고속 비행 상태를 추정한다. VIO, 랜드마크 기반 카메라 측정, IMU를 융합하고 드리프트 모델로 VIO 드리프트(위치·자세·선속도·각속도)를 보정한다. A2RL Drone Racing Challenge 2025에서 210팀 중 4강.^[inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 1,600회 시뮬레이션과 실비행으로 검증(초록)^[inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]
- 센서: 단안 RGB 1대 + IMU 1개^[inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]
- 외부 측위(GNSS/모캡) 없이 고속 비행 가능성을 보인 사례(레이싱 환경 한정)^[inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]

## 한계·미확인
초록에 드리프트 % 등 정량 수치 없음. 레이싱 코스(랜드마크 존재) 한정이라 광역 비행 일반화 불가.^[inbox/processed/hw-20261021-gnss-denied-vio-novak-2602.01860.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
