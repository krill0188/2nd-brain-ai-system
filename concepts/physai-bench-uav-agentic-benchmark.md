---
title: "PhysAI-Bench: UAV 중심 물리 AI 에이전트 의사결정 벤치마크"
created: 2026-09-23
updated: 2026-09-23
type: concept
domain: ai-autonomy
tags: [drone, ai-agent]
sources: [inbox/processed/fetch-2026-09-23-arxiv-physai-bench-a-benchmark-for-llm-based-agentic-decision-maki.md]
confidence: medium
contested: false
contradictions: []
---

## Definition

자율 UAV 임무의 대화 트레이스에서 자동 추출한 10,178건의 표준화된 의사결정 인스턴스로 구성된 벤치마크. 각 인스턴스는 임무 맥락, 시간적 의존성, 물리적 제약, MCP 툴 호출, A2A(Agent-to-Agent) 상호작용, 센서 관측, AI-네이티브 6G 네트워크 조건(지연·패킷손실·처리량·에지부하·네트워크 슬라이싱)을 보존한다.^[inbox/processed/fetch-2026-09-23-arxiv-physai-bench-a-benchmark-for-llm-based-agentic-decision-maki.md]

## Why It Matters

기존 벤치마크는 물리적 지각·직관 물리·체화 내비게이션·협업 추론을 평가하지만, 신뢰 가능한 자율성에 필요한 **에이전트적 의사결정**은 거의 평가하지 않는다는 공백을 지적한다. 29개 파운데이션 모델을 2단계(35개 개발셋 → 고정 500개 평가셋) 프로토콜로 평가한 결과 GPT-5.3이 52.00%로 최고 정확도를 기록했고(GPT-5.2 49.40%, Grok 4.5 49.07% 순), few-shot 프롬프팅은 대체로 성능을 개선하나 temperature의 영향은 제한적이었다. 결과는 물리 AI에서 신뢰 가능한 에이전트적 의사결정이 여전히 미해결 과제임을 보여준다.^[inbox/processed/fetch-2026-09-23-arxiv-physai-bench-a-benchmark-for-llm-based-agentic-decision-maki.md]

## Key Properties

- 10,178개 의사결정 인스턴스, 미래 정보 유출 차단(온라인 의사결정 근사)
- MCP 툴 호출·A2A 상호작용·6G 네트워크 조건까지 포함하는 풍부한 맥락
- 29개 파운데이션 모델, 12개 프롬프팅/temperature 조합으로 모델별 최적 설정 선정 후 고정 평가
- 최고 성능(GPT-5.3)도 52% 수준 — 상당한 개선 여지

## Related

- [[drone-ai-agents]]
- [[llm-uav-carrier-tactical-agent]]
