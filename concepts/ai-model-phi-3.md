---
title: "Phi-3 (phi-3-mini 3.8B) / Phi-3.5"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: SLM
tags: [drone, ai, slm, on-device-llm]
sources: [inbox/processed/hw-20261021-model-phi-3.md]
confidence: medium
contested: false
contradictions: []
---

# Phi-3 (phi-3-mini 3.8B) / Phi-3.5

- 원문: https://arxiv.org/abs/2404.14219^[inbox/processed/hw-20261021-model-phi-3.md]
- 제작: Microsoft^[inbox/processed/hw-20261021-model-phi-3.md]

## 핵심 사양 (초록)
| 모델 | 파라미터 | 학습 토큰 | MMLU | MT-bench |
|---|---|---|---|---|
| phi-3-mini | 3.8B | 3.3T | 69% | 8.38 |
| phi-3-small | 7B | 4.8T | 75% | 8.7 |
| phi-3-medium | 14B | 4.8T | 78% | 8.9 |
phi-3.5-MoE: 16 x 3.8B, 활성 파라미터 6.6B. phi-3.5-Vision: 4.2B, 단일·다중 이미지 입력. 원문: phi-3-mini는 'small enough to be deployed on a phone'.^[inbox/processed/hw-20261021-model-phi-3.md]
제출 2024-04-22, v4 2024-08-30.^[inbox/processed/hw-20261021-model-phi-3.md]
## 비고(미확인)
양자화 수치, 라이선스, Jetson 속도 초록에 없음(미확인). 드론 적용 사례 미확인.^[inbox/processed/hw-20261021-model-phi-3.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[companion-computer]]
