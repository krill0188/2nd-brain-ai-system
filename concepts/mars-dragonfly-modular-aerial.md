---
title: "MARS-Dragonfly Modular Aerial Robot Systems"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, flight-control, hardware, modular-robotics, swarm]
sources: [raw/papers/flight-control/mars-dragonfly-modular-aerial.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# MARS-Dragonfly Modular Aerial Robot Systems

재구성 가능한 연결 형태를 가진 다중 드론 단위로 구성된 모듈형 항공 로봇 시스템(MARS). 수동 도킹, 감지 없는 수동 잠금, 자기 보조 분리를 위한 컴팩트한 기계 시스템과 예측 할당 파이프라인을 통해 안정적인 비행 및 운송을 달성한다.

## 핵심 개념

### 기계 시스템
- **Passive Docking**: 수동 도킹 메커니즘
- **Detection-Free Passive Locking**: 감지 없는 수동 잠금
- **Magnetic-Assisted Separation**: 자기 보조 분리 (단일 마이크로 서보 사용)

### 가상 쿼드로터 추상화
- **Force-Torque-Equivalent**: 힘-토크 등가 모델
- **Polytope Constraint**: 다면체 제약을 명시적으로 모델링
- **Feasible Wrench Sets**: 실행 가능한 렌치 집합 포착

### 2단계 예측 할당 파이프라인
1. **Constrained Predictive Tracker**: 힘/토크 경계를 존중하는 가상 입력 계산
2. **Dynamic Allocator**: 균형 목표로 개별 모듈에 입력 매핑

### 성능
- 40도 피크 피치에서 민첩한 비행
- 평균 위치 오차: 0.0896m
- 10개 이상 구성에서 시뮬레이션 검증
- 실제 로봇 실험 완료

## 관련 페이지

- [[swarm-coordination]] — 군집 드론 운용 모드 및 편대 비행
- [[drone-hw]] — 드론 하드웨어 구성요소
- [[flight-controller-hardware]] — 비행 제어기 및 GPS

## 출처

- Huang et al., "MARS-Dragonfly: Agile and Robust Flight Control of Modular Aerial Robot Systems", arXiv:2604.05499, 2026.
