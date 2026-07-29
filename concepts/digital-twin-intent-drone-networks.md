---
title: "Digital Twin for Intent-Based Drone Networks"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, datalink, comms-protocol, digital-twin, reinforcement-learning]
sources: [raw/papers/datalink/digital-twin-intent-drone-networks.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# Digital Twin for Intent-Based Drone Networks

의도 기반 드론 네트워크를 위한 역강화 학습 기반 디지털 트윈 시스템. DBS(Drone Base Station)의 의도를 명시적으로 알지 못하는 상황에서도 IRL(Inverse Reinforcement Learning)을 활용하여 궤적을 최적화하고 우선순위 사용자 서비스 비율을 극대화한다.

## 핵심 개념

### 디지털 트윈 시스템
- **Virtual Representation**: 물리적 무선 네트워크 환경의 가상 표현
- **Simulation & Prediction**: 관련 변화 시뮬레이션 및 예측
- **Trajectory Adjustment**: DBS 궤적 조정 제안

### 역강화 학습 (IRL)
- **Unknown Intent Handling**: 알려지지 않은 DBS 의도 하에서 궤적 최적화
- **Unpredictable Environment**: 예측 불가능한 환경 변화 대응
- **Performance**: 기존 RL 대비 약 85% 성능 손실 감소

### 네트워크 성능
- **Near-Real-Time Adjustment**: 근실시간 궤적 조정
- **2.5x Enhancement**: 표준 드론 네트워크 대비 최대 2.5배 성능 향상
- **On-Board vs DT**: DBS 온보드 제어 대비 DT 기반 솔루션의 우수성

## 관련 페이지

- [[datalink-communication]] — RF, LTE, WiFi 등 데이터링크 기술
- [[drone-ai-agents]] — 자율 의사결정 및 에이전트 아키텍처
- [[active-sensing-uav-communication]] — 감지 지원 UAV 통신

## 출처

- Wang et al., "Inverse-Reinforcement Learning Enabled Digital Twin for Intent-based Drone Networks", arXiv:2607.17186, 2026.
