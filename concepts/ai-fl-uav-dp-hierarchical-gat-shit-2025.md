---
title: "Hierarchical Federated Graph Attention Networks for Scalable and Resilient UAV Collision Avoidance"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, differential-privacy, byzantine, collision-avoidance, swarm]
sources: [inbox/processed/hw-20261021-ai-fl-uav-dp-hierarchical-gat-shit-2025.md]
confidence: medium
contested: false
contradictions: []
---

# Hierarchical Federated Graph Attention Networks for Scalable and Resilient UAV Collision Avoidance

- 원문: https://arxiv.org/abs/2511.11616^[inbox/processed/hw-20261021-ai-fl-uav-dp-hierarchical-gat-shit-2025.md]
- 저자: Rathin Chandra Shit, Sharmila Subudhi^[inbox/processed/hw-20261021-ai-fl-uav-dp-hierarchical-gat-shit-2025.md]
- 발행: 2025-11-05^[inbox/processed/hw-20261021-ai-fl-uav-dp-hierarchical-gat-shit-2025.md]

## 핵심 내용 (arXiv 초록)
3계층 구조: 로컬 계층(조밀 graph attention, 지연 "<10 ms"), 지역 계층(sparse attention, O(nk) 복잡도 + 비동기 연합학습 + coordinate-wise trimmed mean 집계), 전역 계층(Hashgraph 계열 경량 프로토콜). 적응형 차등 프라이버시: 노이즈 수준 ε∈[0.1, 1.0]을 실시간 위협 평가에 따라 동적으로 낮춤. 블록체인 합의 대신 DHT 기반 경량 감사 로그 사용. 초록 보고: 95th percentile 결정이 50 ms 이내(원문 표현이 다소 모호), 500기 UAV 규모에서 충돌률 "< 2.0%", 비잔틴 허용 "f < n/3".^[inbox/processed/hw-20261021-ai-fl-uav-dp-hierarchical-gat-shit-2025.md]

## 설계에 쓸 수 있는 지침
- 안전 임계 제어(충돌 회피)는 지연이 큰 연합학습 경로와 분리하고 로컬 추론을 <10 ms 계층에 둔다.^[inbox/processed/hw-20261021-ai-fl-uav-dp-hierarchical-gat-shit-2025.md]
- 집계 단계의 비잔틴 방어(trimmed mean)와 DP 노이즈 ε 범위를 함께 제시한 사례.^[inbox/processed/hw-20261021-ai-fl-uav-dp-hierarchical-gat-shit-2025.md]

## 한계·미확인
- 초록만 열람. 데이터셋, 공격 모델 종류, 정확도 손실 수치, 실제 UAV 하드웨어 실험 여부 미확인(시뮬레이션 추정이나 초록에 명시 없음).^[inbox/processed/hw-20261021-ai-fl-uav-dp-hierarchical-gat-shit-2025.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[swarm-coordination]]
