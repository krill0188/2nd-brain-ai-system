---
title: "TypeFly: Flying Drones with Large Language Model"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, ai, llm-agent, latency, real-time, drone-control]
sources: [inbox/processed/hw-20261021-ai-agent-safety-latency-typefly-chen-2023.md]
confidence: medium
contested: false
contradictions: []
---

# TypeFly: Flying Drones with Large Language Model

- 원문: https://arxiv.org/abs/2312.14950^[inbox/processed/hw-20261021-ai-agent-safety-latency-typefly-chen-2023.md]
- 저자: Guojun Chen, Xiaojing Yu, Neiwen Ling, Lin Zhong^[inbox/processed/hw-20261021-ai-agent-safety-latency-typefly-chen-2023.md]
- 발행: 2023-12-08 (v2 2024-09-26)^[inbox/processed/hw-20261021-ai-agent-safety-latency-typefly-chen-2023.md]

## 핵심 내용
LLM이 토큰 단위로 출력하기 때문에 실시간 드론 제어용 계획 생성의 지연이 크다는 문제를 다룬다. 장황한 Python 대신 토큰 효율적이고 스트림 해석이 가능한 맞춤 언어 MiniSpec으로 계획을 생성하고 런타임이 실행한다.^[inbox/processed/hw-20261021-ai-agent-safety-latency-typefly-chen-2023.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 어려운 드론 과제 집합에서 응답 시간 'up to 62%' 감소.^[inbox/processed/hw-20261021-ai-agent-safety-latency-typefly-chen-2023.md]
- 토큰 절감 수치는 초록에 없음(미확인).^[inbox/processed/hw-20261021-ai-agent-safety-latency-typefly-chen-2023.md]

## 한계·미확인
초록에 'ChatFly' 표기가 혼재. 사용 LLM·하드웨어 미확인. ~/2nd/concepts의 llm-enabled-uav-natural-language-navigation 등과 주제 인접(보강).^[inbox/processed/hw-20261021-ai-agent-safety-latency-typefly-chen-2023.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
