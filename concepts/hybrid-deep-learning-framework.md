---
title: "Hybrid Deep Learning Framework for Real-Time UAV Navigation with Adaptive Smoothness Control"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [deep-learning, uav-navigation, federated-learning, reinforcement-learning, cellular-signals]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Hybrid Deep Learning Framework for Real-Time UAV Navigation with Adaptive Smoothness Control

이 연구는 GPS 저하, 국소화 오차, 동적 장애물, 그리고 비효율적인 비행 경로 등 문제를 극복할 수 있는 신뢰성 있고 에너지 효율적인 도시 UAV 항법 시스템을 개발하는 것을 목표로 합니다. 본 연구는 세포 네트워크 신호를 활용한 하이브리드 딥러닝 기반 항법 시스템을 도입하여 UAV 신뢰성을 향상시킵니다. 복합 비용 함수를 설계하여 움직임의 불확실성, 경로의 부드러움, 이동 거리, 그리고 충돌 회피를 최적화합니다. three-dimensional geometry-based channel propagation model(3DGCPM)을 사용하여 세포 간 간섭의 양을 감소시킵니다. 연방 메타 멀티 에이전트 그래프 딥 강화 학습(F2MGDRL) 프레임워크는센서 데이터 융합과 의사 결정 최적화를 통해 UAV의 자율 항법 능력을 향상시킵니다.

## 개요

본 프레임워크는 실시간 UAV 항법에서 GPS 의존도를 낮추고 환경을 정확하게 인지하기 위해 세포 네트워크 신호와 고급 딥러닝 기법을 결합합니다. 특히, 다목적 비용 함수를 통해 비행 경로의 부드러움과 에너지 효율성, 그리고 충돌 회피를 동시에 최적화하는 것이 핵심 특징입니다. 3DGCPM 모델은 세포 간 간섭을 억제하여 통신 신뢰성을 높이며, F2MGDRL 프레임워크는 에이전트 간 협업을 통해 복잡한 도시 환경을 효율적으로 항법합니다.

## 핵심 파라미터

| Parameter | Description |
| :--- | :--- |
| Navigation System | Hybrid deep learning-based UAV navigation with adaptive smoothness control |
| Cost Function | Multi-objective optimization targeting uncertainty, smoothness, distance, and collision avoidance |
| Interference Model | 3D geometry-based channel propagation model (3DGCPM) for reducing inter-cellular interference |
| Learning Architecture | Federated meta multi-agent graph deep reinforcement learning (F2MGDRL) |
| Signal Source | Cellular network signals (e.g., 5G) for positioning and communication |

## 활용처

- GPS가 불량하거나 사용 불가능한 도시 환경 및 실내 환경에서의 UAV 자율 항법
- 에너지 효율적인 비행 경로 최적화가 필요한 물류 배송, 감시, 매핑 임무
- 세포 네트워크 신호를 활용한 실시간 위치 추정 및 통신 환경이 제한된 지역에서 운영되는 드론

## 관련 페이지

- [[F2MGDRL]] — 연방 메타 멀티 에이전트 그래프 딥 강화 학습 프레임워크
- [[3DGCPM]] — three-dimensional geometry-based channel propagation model
- [[Cellular Network Signals]] — UAV 항법 및 통신에 활용되는 세포 네트워크 신호

## 출처

- (사용자 재확인 필요) original paper: "Hybrid Deep Learning Framework for Real-Time UAV Navigation with Adaptive Smoothness Control," P. Tamilselvi, 2026, Sathyabama Institute of Science and Technology.
