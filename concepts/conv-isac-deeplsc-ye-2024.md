---
title: "Integrated Sensing and Communications for Low-Altitude Economy: A Deep Reinforcement Learning Approach"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: rf-datalink-engineering
tags: [drone, isac, drl, beamforming, trajectory]
sources: [inbox/processed/hw-20261021-conv-isac-deeplsc-ye-2024.md]
confidence: medium
contested: false
contradictions: []
---

# Integrated Sensing and Communications for Low-Altitude Economy: A Deep Reinforcement Learning Approach

- 원문: arXiv:2412.04074^[inbox/processed/hw-20261021-conv-isac-deeplsc-ye-2024.md]
- 저자: Xiaowen Ye, Yuyi Mao, Xianghao Yu, Shu Sun, Liqun Fu, Jie Xu^[inbox/processed/hw-20261021-conv-isac-deeplsc-ye-2024.md]
- 발행: 2024-12-05 (v3 2025-01-02)^[inbox/processed/hw-20261021-conv-isac-deeplsc-ye-2024.md]

## 핵심 내용
지상 기지국이 인가 드론에 통신·항법을 제공하며 저고도 공역에서 비인가 표적을 센싱한다. 센싱, 임무, 충돌 회피, 전력 제약 아래 비행 구간 총 통신 속도를 최대화하도록 빔포밍과 궤적을 공동 최적화한다. 에피소드형 MDP로 모델링하고 DeepLSC(Deep LAE-ISAC) 강화학습을 제안한다: 맞춤 보상, 제약 인지 탐험 정책, 계층적 경험 재생, 대칭 경험 증강. 기준선보다 합 속도가 높고 제약을 만족하며 수렴이 빠르고 견고하다고 보고.^[inbox/processed/hw-20261021-conv-isac-deeplsc-ye-2024.md]
원문 인용: "sensing the low-altitude airspace to monitor the unauthorized mobile target"^[inbox/processed/hw-20261021-conv-isac-deeplsc-ye-2024.md]

## 설계·운용에 쓸 수 있는 지침
- 충돌 회피까지 포함한 제약 RL 학습에서 경험 재생·증강으로 학습을 가속하는 방법.^[inbox/processed/hw-20261021-conv-isac-deeplsc-ye-2024.md]

## 한계·미확인
- 초록에 수치 없음.^[inbox/processed/hw-20261021-conv-isac-deeplsc-ye-2024.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[uav-isac-cross-region]]
