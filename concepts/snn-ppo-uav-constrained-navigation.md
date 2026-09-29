---
title: "스파이킹 신경망 액터-크리틱 PPO 기반 UAV 협소구간 자율비행"
created: 2026-09-23
updated: 2026-09-23
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-09-23-arxiv-spiking-neural-network-actor-critic-proximal-policy-optimiza.md]
confidence: medium
contested: false
contradictions: []
---

## Definition

교량·터널·구조물 점검처럼 3차원 제약 환경에서 UAV가 좁은 개구부(창문 등)를 통과하도록, 스파이킹 신경망(SNN) 기반 액터-크리틱 강화학습을 PPO(Proximal Policy Optimization)와 결합한 자율 내비게이션 알고리즘. 확률적 가우시안 정책을 사용한다.^[inbox/processed/fetch-2026-09-23-arxiv-spiking-neural-network-actor-critic-proximal-policy-optimiza.md]

## Why It Matters

기존 심층 강화학습 기반 UAV 내비게이션은 협소 환경에서 성공적이었지만 연산 비용이 커 온보드 적용이 제한적이었다. SNN 기반 접근은 이 연산 비용 문제를 겨냥한다. 3,000회 이상 에피소드 중 1,913회를 완주했고, 에피소드당 평균 2.10개 창문을 통과했으며 전체 성공률 63.77%을 달성했다. 학습 후반부에는 성공률이 90% 이상으로 상승했다.^[inbox/processed/fetch-2026-09-23-arxiv-spiking-neural-network-actor-critic-proximal-policy-optimiza.md]

## Key Properties

- 스파이크 기반 액터-크리틱 RL + PPO 결합, 확률적 가우시안 정책
- 목표: 연산 비용을 낮춰 온보드(임베디드) UAV 배포 가능성 확보
- 학습 후반 성공률 90%+ (전체 평균은 63.77%)
- 적용 분야: 교량/터널/구조물 점검용 협소구간 통과

## Related

- [[lightweight-safe-rl-uav]]
- [[rl-quadrotor-tunable-control]]
