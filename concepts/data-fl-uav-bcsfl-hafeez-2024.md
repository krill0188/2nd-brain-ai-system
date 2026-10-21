---
title: "Blockchain-enabled Clustered and Scalable Federated Learning (BCS-FL) Framework in UAV Networks"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, blockchain, clustering]
sources: [inbox/processed/hw-20261021-data-fl-uav-bcsfl-hafeez-2024.md]
confidence: medium
contested: false
contradictions: []
---

# Blockchain-enabled Clustered and Scalable Federated Learning (BCS-FL) Framework in UAV Networks

- 원문: arXiv:2402.05973^[inbox/processed/hw-20261021-data-fl-uav-bcsfl-hafeez-2024.md]
- 저자: Sana Hafeez, Lina Mohjazi, Muhammad Ali Imran, Yao Sun^[inbox/processed/hw-20261021-data-fl-uav-bcsfl-hafeez-2024.md]
- 발행: 2024-02-07 (v2 2024-02-15)^[inbox/processed/hw-20261021-data-fl-uav-bcsfl-hafeez-2024.md]

## 핵심 내용
UAV 네트워크 연합학습의 프라이버시, 확장성, 신뢰성(통신 오버헤드, 동기화 문제)을 다룬다. UAV를 클러스터헤드가 이끄는 클러스터로 묶어 연결 그래프를 만들고, 클러스터 간/내 모델 집계를 결합해 라운드마다 전역 모델을 만든다. 수렴을 보이며 학습 효과와 통신 효율 사이의 트레이드오프가 있다고 기술한다.^[inbox/processed/hw-20261021-data-fl-uav-bcsfl-hafeez-2024.md]
원문 인용: "Clustering enables efficient coordination of updates to the ML model."^[inbox/processed/hw-20261021-data-fl-uav-bcsfl-hafeez-2024.md]

## 설계·운용에 쓸 수 있는 지침
- 군집을 클러스터로 나눠 통신량을 줄이되 학습 효과가 저하되는 트레이드오프를 설계 변수로 고려.^[inbox/processed/hw-20261021-data-fl-uav-bcsfl-hafeez-2024.md]

## 한계·미확인
- 초록에 수치 없음. 블록체인의 실제 오버헤드는 미확인.^[inbox/processed/hw-20261021-data-fl-uav-bcsfl-hafeez-2024.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[swarm-coordination]]
