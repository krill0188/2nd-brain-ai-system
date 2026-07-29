---
title: "SkyJEPA: Long-Horizon World Models for Quadrotor Control"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, flight-control, ai-autonomy, world-models, sim-to-real]
sources: [raw/papers/flight-control/skyjepa-world-models.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# SkyJEPA: Long-Horizon World Models for Quadrotor Control

실시간 쿼드로터 제어를 위한 JEPA(Joint Embedding Predictive Architecture) 스타일 세계 모델. 잠재 공간에서 역학을 모델링하고 물리 기반 프로버를 결합하여 장기 예측을 가능하게 하며, 샘플링 기반 최적 제어와 통합하여 임베디드 하드웨어에서 실시간 제어를 달성한다.

## 핵심 개념

### JEPA-Style Model
- **Latent Dynamics Model**: 잠재 공간에서의 역학 모델
- **Physics-Inspired Prober**: 고정된 잠재 변수를 해석 가능한 상태로 매핑
- **Long-Horizon Prediction**: 물리적 기반 장기 예측

### 제어 통합
- **Sampling-Based Optimal Control**: 샘플링 기반 최적 제어 솔루션
- **Real-Time Control**: 임베디드 하드웨어에서 실시간 제어
- **Automated Dataset Generation**: 자동화된 데이터셋 생성 파이프라인

### 성능
- 정확한 예측 (open-loop 실험)
- 견고한 제로샷 sim-to-real 전송
- 다양한 운영 조건에서 강력한 일반화

## 관련 페이지

- [[e2e-fly-end-to-end-quadrotor]] — 종단간 쿼드로터 자율 시스템
- [[drone-simulation]] — Gazebo, SITL 기반 시뮬레이션
- [[drone-ai-agents]] — 자율 의사결정 및 세계 모델

## 출처

- Rao et al., "SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors", arXiv:2606.23444, 2026.
