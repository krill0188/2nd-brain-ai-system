---
title: "Jailbreaking LLM-Controlled Robots"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, ai, llm-agent, safety, jailbreak, robot]
sources: [inbox/processed/hw-20261021-ai-agent-safety-robopair-robey-2024.md]
confidence: medium
contested: false
contradictions: []
---

# Jailbreaking LLM-Controlled Robots

- 원문: https://arxiv.org/abs/2410.13691^[inbox/processed/hw-20261021-ai-agent-safety-robopair-robey-2024.md]
- 저자: Alexander Robey, Zachary Ravichandran, Vijay Kumar, Hamed Hassani, George J. Pappas^[inbox/processed/hw-20261021-ai-agent-safety-robopair-robey-2024.md]
- 발행: 2024-10-17 (v2 2024-11-09)^[inbox/processed/hw-20261021-ai-agent-safety-robopair-robey-2024.md]

## 핵심 내용
LLM으로 제어되는 로봇을 탈옥시켜 유해한 물리 행동을 유도하는 최초의 알고리즘 RoboPAIR를 제안한다. 화이트박스(NVIDIA Dolphins 자율주행 LLM), 그레이박스(Clearpath Jackal UGV + GPT-4o 플래너), 블랙박스(Unitree Go2 + GPT-3.5) 세 설정에서 시험했다. 저자들은 상업 배치 로봇 시스템에 대한 최초의 탈옥 성공이라고 주장.^[inbox/processed/hw-20261021-ai-agent-safety-robopair-robey-2024.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 'often achieving 100% attack success rates' (원문), 플랫폼별 정확한 비율은 초록에 없음.^[inbox/processed/hw-20261021-ai-agent-safety-robopair-robey-2024.md]
- 시사점: LLM 플래너 출력은 텍스트 필터만으로 안전하지 않으므로 물리 행동 단계에 별도 제약 계층이 필요(논문 취지를 요약한 해석이 아니라 원문 결과가 보여주는 위험).^[inbox/processed/hw-20261021-ai-agent-safety-robopair-robey-2024.md]

## 한계·미확인
드론 플랫폼은 시험 대상이 아님(미확인). 플랫폼별 성공률 미확인.^[inbox/processed/hw-20261021-ai-agent-safety-robopair-robey-2024.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
