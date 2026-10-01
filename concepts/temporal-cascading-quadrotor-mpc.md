---
title: "Temporal Cascading of Planning and Control for Quadrotor MPC"
created: 2026-10-01
updated: 2026-10-01
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-01-yt-temporal-cascading-of-planning-and-control-for-quadrotor-mpc.md]
confidence: low
contested: false
contradictions: []
---

# Temporal Cascading of Planning and Control for Quadrotor MPC

UZH Robotics and Perception Group의 T-RO 2026 연구. 쿼드로터의 민첩한 공중 임무(장애물 회피,
에너지 효율, 궤적 추종)는 즉각적인 반응성과 장기 계획을 동시에 요구하는데, 고신뢰도(High-fidelity)
모델은 정밀 제어에는 유리하지만 장기 호라이즌 계산에는 너무 느리고, 저신뢰도(Low-fidelity)
플래너는 확장성은 있지만 시스템을 직접 제어할 수 없어 계층적(Cascaded) 구조가 필요하다는 문제를
제기한다.^[inbox/processed/fetch-2026-10-01-yt-temporal-cascading-of-planning-and-control-for-quadrotor-mpc.md]

## 핵심 문제의식

- **기존 계층적 접근**: 단순화된 모델로 계획(plan)하고, 고신뢰도 컨트롤러로 그 결과를 추종
  (track)하는 방식이 일반적이나, 이 분해(decomposition) 자체에 구조적 한계가 내재한다고 지적.
- **대안 방향**: 계획과 제어를 시간축(temporal)으로 캐스케이딩하는 구조를 제안(영상 설명이
  중간에 끊겨 구체적 알고리즘 세부는 원문 미확보).

## 주의

- YouTube 설명 텍스트가 도중에 잘려("yet this decomposition is inherent") 이후 제안 기법의
  구체적 구현은 확인되지 않음 — 단일 출처, confidence low로 유지.

## Related

- [[px4-control-tuning]] — PX4 Rate→Attitude→Velocity→Position 계층적 제어 아키텍처(유사한
  계층 구조 문제의식)
- [[time-optimal-quadrotor-waypoints]] — 쿼드로터 웨이포인트 시간 최적 궤적 계획
- [[spatial-dubins-quadrotor-control]] — 쿼드로터 제어를 위한 궤적 참조 스무딩
