---
title: "MROPE: Multi-Robot Safe Cooperative Strategy"
created: 2026-08-04
updated: 2026-08-04
type: concept
tags: [swarm, drone-ai, ai-agent, safety]
domain: ai-autonomy
sources: [inbox/fetch-2026-08-04-arxiv-mrope-a-multi-robot-safe-cooperative-strategy-via-combined-p.md]
confidence: high
contested: false
contradictions: []
---

# MROPE: Multi-Robot Safe Cooperative Strategy

**MROPE** (Multi-Robot Safe Cooperative Strategy via combined Predictive Safety Filters and Ellipse-based Constraint Compression)는 복잡한 환경에서 동적 표적을 추적하는 드론 스웜을 위한 계층적 안전 전략이다.

## 핵심 개념

### 아키텍처
MROPE는 협력 감시 미션과 엄격한 로컬 안전 요구사항을 분리하는 계층적 접근법을 사용한다:

1. **고수준 스웜 조정**: 분산 집합 최적화(distributed aggregative optimization)를 사용
2. **안전 영역 계산**: 분산 합의 방식(decentralized consensus scheme)으로 안전한 타원 영역 계산
3. **로컬 충돌 회피**: 예측 안전 필터(Predictive Safety Filters, PSF)로 실시간 충돌 방지

### 타원 기반 제약 압축
복잡한 장애물 형상을 각 드론에 대해 단일 안전 경계 타원으로 동적으로 집계하여 계산 병목 현상을 극복한다.

## 검증

가상 및 실제 실험을 통해 중앙 집중식 접근법 대비 우수한 실시간 효율성과 확장성을 입증했다.

## 관련 개념

- [[swarm-coordination]] — 스웜 조정 및 편대 비행
- [[drone-ai-agents]] — 자율 의사결정 및 다중 에이전트 협력
- [[decentralized-swarm-gps-denied]] — 분산형 스웜 제어

## 📰 최근 관련 소식
- MROPE: A Multi-Robot Safe Cooperative Strategy via combined Predictive Safety Filters and Ellipse-based Constraint Compression (arxiv.org, 2026-07-31) — http://arxiv.org/abs/2607.29203v1
