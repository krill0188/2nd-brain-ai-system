---
title: "Networked ISAC for Low-Altitude Economy: Coordinated Transmit Beamforming and UAV Trajectory Design"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: rf-datalink-engineering
tags: [drone, isac, beamforming, trajectory, low-altitude]
sources: [inbox/processed/hw-20261021-conv-isac-networked-cheng-2024.md]
confidence: medium
contested: false
contradictions: []
---

# Networked ISAC for Low-Altitude Economy: Coordinated Transmit Beamforming and UAV Trajectory Design

- 원문: arXiv:2406.16946^[inbox/processed/hw-20261021-conv-isac-networked-cheng-2024.md]
- 저자: Gaoyuan Cheng, Xianxin Song, Zhonghao Lyu, Jie Xu^[inbox/processed/hw-20261021-conv-isac-networked-cheng-2024.md]
- 발행: 2024-06-19^[inbox/processed/hw-20261021-conv-isac-networked-cheng-2024.md]

## 핵심 내용
여러 지상 기지국이 통신·센싱 신호를 함께 보내 인가 UAV에 서비스하고 3차원 영역의 비인가 물체를 탐지한다. 센싱 간섭을 제거할 수 있는 UAV 수신기와 없는 수신기 두 경우에 대해 협조 빔포밍, UAV 궤적, UAV-기지국 연계를 공동 최적화해 인가 UAV의 평균 합 속도를 최대화한다. 제약은 최소 센싱 조사 전력, 기지국별 전력, 비행 제약. 비볼록 문제를 교대 최적화, SCA, 세미정의 완화로 푼다. 수치 결과에서 기준 방식보다 센싱-통신 절충이 우수하다고 보고.^[inbox/processed/hw-20261021-conv-isac-networked-cheng-2024.md]
원문 인용: "maximize the average sum rate of authorized UAVs"^[inbox/processed/hw-20261021-conv-isac-networked-cheng-2024.md]

## 설계·운용에 쓸 수 있는 지침
- 센싱 조사 전력 하한을 제약으로 두고 통신 합 속도를 최대화하는 ISAC 공식.^[inbox/processed/hw-20261021-conv-isac-networked-cheng-2024.md]

## 한계·미확인
- 초록에 수치 없음. 검색 요약상 수평 어레이가 유리하다는 서술은 초록에서 확인하지 못함(미확인).^[inbox/processed/hw-20261021-conv-isac-networked-cheng-2024.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[uav-isac-cross-region]]
