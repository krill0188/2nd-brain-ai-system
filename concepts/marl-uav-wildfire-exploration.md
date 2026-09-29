---
title: "산불 대응 자율 UAV 탐색을 위한 다중 에이전트 강화학습"
created: 2026-09-11
updated: 2026-09-11
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, ai-autonomy]
sources: [raw/papers/drone-ai/multi-agent-reinforcement-learning-for-autonomous-uav-exploration-in-wildfire-re.md]
confidence: medium
contested: false
contradictions: []
---

# 산불 대응 자율 UAV 탐색을 위한 다중 에이전트 강화학습

시뮬레이션된 산불 환경에서 UAV 에이전트가 자율적으로 항법·감시를 수행하도록 학습시키는 심층
강화학습(DRL) 프레임워크를 개발한 연구다
^[raw/papers/drone-ai/multi-agent-reinforcement-learning-for-autonomous-uav-exploration-in-wildfire-re.md].

## 방법

- 다중 UAV 에이전트가 산불 시뮬레이션 환경을 탐색하며 화재 경계를 추적하도록 다중 에이전트 강화학습
  정책을 훈련.
- 보상 설계와 환경 구조가 정책 효과에 미치는 영향을 함께 검토.

## 결과

- 손실 수렴, 보상 신호 개선, 화재 경계 추적 등 일관된 항법 패턴으로 나타나는 안정적·효과적인
  에이전트 행동이 시간이 지날수록 향상됨을 확인.
- 환경 구조와 보상 설계가 정책 효과성에 영향을 미친다는 점을 시사, DRL 기반 UAV 시스템이 자율
  산불 모니터링에 활용될 잠재력을 뒷받침.

## 관련 개념

- [[thermal-drone-wildfire-monitoring]] — 열화상 드론 기반 산불 모니터링
- [[drone-wildfire-rt-detr]] — RT-DETR 기반 산불 탐지 드론 비전 파이프라인
- [[hierarchical-rl-uav-navigation]] — 계층적 강화학습 기반 UAV 자율 내비게이션(동일 RL 계열)
