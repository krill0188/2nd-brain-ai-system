---
title: "RALLY: Role-Adaptive LLM-Driven Yoked Navigation for Agentic UAV Swarms"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: swarm-multiagent
ontology_class: SwarmResearch
tags: [drone, swarm, llm, marl, decision]
sources: [inbox/processed/hw-20261021-conv-swarm-llm-rally-wang-2025.md]
confidence: medium
contested: false
contradictions: []
---

# RALLY: Role-Adaptive LLM-Driven Yoked Navigation for Agentic UAV Swarms

- 원문: arXiv:2507.01378^[inbox/processed/hw-20261021-conv-swarm-llm-rally-wang-2025.md]
- 저자: Ziyao Wang, Rongpeng Li, Sizhao Li, Yuming Xiang, Haiping Wang, Zhifeng Zhao, Honggang Zhang^[inbox/processed/hw-20261021-conv-swarm-llm-rally-wang-2025.md]
- 발행: 2025-07-02 (v2 2025-09-01)^[inbox/processed/hw-20261021-conv-swarm-llm-rally-wang-2025.md]

## 핵심 내용
드론 군집의 항법, 장애물 회피, 다중 목표 커버리지를 다룬다. 기존 MARL은 통신과 경직된 역할 구조에 약하고 LLM 기반 방식은 온라인 학습이 없고 정적 사전지식에 과의존한다고 본다. RALLY는 LLM 기반 의미 의사결정, 동적 역할 전환, LLM 오프라인 사전지식과 온라인 강화학습을 합치는 RMIX 기반 할당 전략을 결합한다. Multi-Agent Particle Environment와 SITL 플랫폼에서 커버리지, 수렴 속도, 일반화가 기존 방법보다 좋다고 보고.^[inbox/processed/hw-20261021-conv-swarm-llm-rally-wang-2025.md]
원문 인용: "semi-offline training of role selection strategies"^[inbox/processed/hw-20261021-conv-swarm-llm-rally-wang-2025.md]

## 설계·운용에 쓸 수 있는 지침
- LLM은 역할 사전지식, 실시간 선택은 RL이 맡는 분업 구조의 참고.^[inbox/processed/hw-20261021-conv-swarm-llm-rally-wang-2025.md]

## 한계·미확인
- 초록에 수치 없음. 실기 비행 검증 미확인(SITL까지).^[inbox/processed/hw-20261021-conv-swarm-llm-rally-wang-2025.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[swarm-coordination]]
