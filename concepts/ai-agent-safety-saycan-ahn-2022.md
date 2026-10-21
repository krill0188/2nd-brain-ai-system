---
title: "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, ai, llm-agent, safety, affordance, grounding]
sources: [inbox/processed/hw-20261021-ai-agent-safety-saycan-ahn-2022.md]
confidence: medium
contested: false
contradictions: []
---

# Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

- 원문: https://arxiv.org/abs/2204.01691^[inbox/processed/hw-20261021-ai-agent-safety-saycan-ahn-2022.md]
- 저자: Michael Ahn 외 44명^[inbox/processed/hw-20261021-ai-agent-safety-saycan-ahn-2022.md]
- 발행: 2022-04-04 (v2 2022-08-16)^[inbox/processed/hw-20261021-ai-agent-safety-saycan-ahn-2022.md]

## 핵심 내용
LLM은 실세계 경험이 없어 특정 로봇·환경에 맞지 않는 행동을 제안할 수 있다. 사전학습된 스킬과 그 가치함수(value function)로 LLM을 grounding해 실행 가능하고 맥락에 맞는 행동만 제안하게 한다. 이동 매니퓰레이터의 실세계 장기 추상 지시 수행으로 평가.^[inbox/processed/hw-20261021-ai-agent-safety-saycan-ahn-2022.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 수치는 초록에 없음(미확인).^[inbox/processed/hw-20261021-ai-agent-safety-saycan-ahn-2022.md]
- 시사점: LLM 제안을 로봇이 실행 가능한 스킬 집합으로 제한하고 가치함수로 필터링하는 구조.^[inbox/processed/hw-20261021-ai-agent-safety-saycan-ahn-2022.md]

## 한계·미확인
드론 적용 없음. 성공률 미확인.^[inbox/processed/hw-20261021-ai-agent-safety-saycan-ahn-2022.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
