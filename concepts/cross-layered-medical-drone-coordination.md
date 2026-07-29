---
title: "Cross-Layered Multi-Drone Coordination for Medical Supply Delivery"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, swarm, flight-control, ai-autonomy, medical-delivery, disaster-response]
sources: [raw/papers/swarm/cross-layered-medical-drone-coordination.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# Cross-Layered Multi-Drone Coordination for Medical Supply Delivery

재난 대응 상황에서 의료 물품 배달을 위한 다중 드론 협업 시스템. CTDE(Centralized Training Decentralized Execution) 기반 Deep Q-Network 알고리즘(CEDA)을 활용하여 트리아지 우선순위 기반 라우팅, 다중 에이전트 협업, 에너지 효율적 내비게이션을 동시에 최적화한다.

## 핵심 개념

### CEDA 알고리즘
- **CTDE (Centralized Training Decentralized Execution)**: 중앙 집중식 학습, 분산 실행
- **Priority-Preserving Fair Scheduling**: 트리아지 가중치와 공정성 메커니즘을 결합한 보상 함수
- **PX4 SITL 검증**: X500 쿼드로터 2대로 MAVSDK 오프보드 위치 제어 모드 검증

### 성능 지표
- 배달 완료율: 85% 이상
- 장애물 충돌 감소: 90% 이상
- 평균 환자 처리: 에피소드당 6명
- 트리아지 효율성: 0.82

## 관련 페이지

- [[swarm-coordination]] — 군집 드론 운용 모드 및 편대 비행
- [[px4-flight-stack]] — PX4 오픈소스 비행 제어 소프트웨어
- [[mavsdk]] — MAVLink 기반 고수준 드론 제어 SDK
- [[drone-ai-agents]] — 자율 의사결정 및 다중 에이전트 협력

## 출처

- Calyam et al., "A Cross-Layered Multi-Drone Coordination for Medical Supply Delivery during Disaster Response Management", arXiv:2605.09342, 2026.
