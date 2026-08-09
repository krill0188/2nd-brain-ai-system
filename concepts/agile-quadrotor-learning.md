---
title: "Agile Quadrotor Flight Learning"
created: 2026-07-31
updated: 2026-08-10
type: concept
tags: [drone, ai-autonomy, drone-sw]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# Agile Quadrotor Flight Learning

실제 환경에서의 민첩한 쿼드로터 비행 학습. RSS 2026 연구.

## Problem

- 기존 학습 기반 컨트롤러는 대규모 시뮬레이션 학습에 의존
- 정확한 시스템 식별이 sim-to-real 전송에 필요
- 고정 정책은 외부 공역학적 외란 및 내부 하드웨어 열화에 취약

## Approach

- 실제 환경에서의 직접 학습
- 진화하는 불확실성에 대한 안전성 보장
- 분포 외 시나리오 처리

## Institution

- UZH Robotics and Perception Group (취리히 대학)

## References

- [[drone-ai]]
- [[px4-flight-stack]]
- [[drone-simulation]]
