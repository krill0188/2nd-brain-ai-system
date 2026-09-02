---
title: "STL 기반 확산 모델 다중 에이전트 계획"
created: 2026-09-02
updated: 2026-09-02
type: concept
tags: [drone, ai-autonomy, swarm, stl, diffusion, planning]
sources: [inbox/fetch-2026-09-02-arxiv-generalizable-multi-agent-planning-from-signal-temporal-logi.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# STL 기반 확산 모델 다중 에이전트 계획

Signal Temporal Logic(STL) 사양을 활용한 확산 기반 다중 에이전트 계획 방법. 드론 스웜, 자율주행차, 창고 로봇 등 실제 다중 에이전트 시스템에서 시간적 작업 충족 및 충돌 회피를 동시에 달성한다.

## 핵심 기여

- **STL 미분 가능 근사**: STL 그래이언트를 디노이징 프로세스에 통합
- **일반화**: 학습 중 목표 영역 내 어디에나 술어를 배치할 수 있는 새로운 공식으로 일반화
- **확장성**: 기존 학습 기반 방법과 동일한 확장성 달성
- **이질성 지원**: 서로 다른 에이전트에 다른 사양 할당 가능
- **계획 다양성**: 확산 모델을 활용한 자연스러운 계획 다양성 향상

## 안전성 향상

계획 다양성을 통해 에이전트 간 충돌 등 안전 관련 위반을 크게 감소시킨다.

## 관련 개념

- [[swarm-coordination]] — 군집 협업 및 편대 비행
- [[drone-ai-agents]] — 자율 의사결정 에이전트
- [[mavsdk]] — MAVLink 기반 드론 제어 SDK

## 출처

- Joe Eappen et al., "Generalizable Multi-Agent Planning from Signal Temporal Logic Specifications via Diffusion", arXiv:2608.29490, 2026
- 코드: https://github.com/jeappen/diff-ma-stl
