---
title: "Trajectory Design and Resource Allocation for Multi-UAV-Assisted Sensing, Communication, and Edge Computing Integration"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: rf-datalink-engineering
tags: [drone, isac, mec, multi-uav, marl]
sources: [inbox/processed/hw-20261021-conv-isac-mec-peng-2024.md]
confidence: medium
contested: false
contradictions: []
---

# Trajectory Design and Resource Allocation for Multi-UAV-Assisted Sensing, Communication, and Edge Computing Integration

- 원문: arXiv:2410.04151^[inbox/processed/hw-20261021-conv-isac-mec-peng-2024.md]
- 저자: Sicong Peng, Bin Li, Lei Liu, Zesong Fei, Dusit Niyato^[inbox/processed/hw-20261021-conv-isac-mec-peng-2024.md]
- 발행: 2024-10-05^[inbox/processed/hw-20261021-conv-isac-mec-peng-2024.md]

## 핵심 내용
다수 UAV가 MIMO 어레이로 인근 이동 사용자에게 통신, 엣지 컴퓨팅, 표적 센싱을 동시에 제공하는 네트워크. 사용자는 데이터를 부분 압축한 뒤 오프로딩한다. 센싱 품질 제약 아래 빔포밍, UAV 궤적, 압축·오프로딩 결정, 컴퓨팅 자원 할당을 공동 최적화해 가중 에너지 소비를 최소화한다. 이종 에이전트의 다중 에이전트 MDP로 모델링하고 어텐션을 쓴 다중 에이전트 PPO로 푼다. 시뮬레이션에서 기준선보다 에너지 소비가 낮고 자원 활용과 수렴 속도가 좋다고 보고.^[inbox/processed/hw-20261021-conv-isac-mec-peng-2024.md]
원문 인용: "minimize the weighted energy consumption"^[inbox/processed/hw-20261021-conv-isac-mec-peng-2024.md]

## 설계·운용에 쓸 수 있는 지침
- 센싱 품질 제약을 두고 압축 비율·오프로딩·궤적을 함께 결정하는 변수 구성의 참고 예.^[inbox/processed/hw-20261021-conv-isac-mec-peng-2024.md]

## 한계·미확인
- 초록에 수치 없음. 실기 검증 미확인.^[inbox/processed/hw-20261021-conv-isac-mec-peng-2024.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[uav-isac-cross-region]]

## 📰 최근 관련 소식
- FAA Releases Draft Design Standards for Vertiports and Vertical Flight Facilities (dronelife.com, Fri, 23 Oc) — https://dronelife.com/2026/10/23/faa-vertiport-design-standards-2026/
