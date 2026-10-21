---
title: "MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases"
created: 2026-10-21
captured: 2026-10-21
type: product
category: ai-model
manufacturer: Meta (Zechun Liu 외, ICML 2024)
domain: edge-ai-compute
source: https://arxiv.org/abs/2402.14905
tags: [drone, ai, slm, on-device-llm]
---
## 핵심 사양 (초록)
- 10억 파라미터 미만 LM. deep-thin 구조, embedding sharing, grouped-query attention.
- 기존 125M SOTA 대비 +2.7%, 350M SOTA 대비 +4.3% 정확도. MobileLLM-LS(블록 단위 가중치 공유)는 추가 +0.7%(125M), +0.8%(350M).
- API 호출 과제에서 LLaMA-v2 7B에 근접한 정확도라고 주장. 제출 2024-02-22, v2 2024-06-27.
## 비고(미확인)
라이선스, 실제 기기 지연 수치 초록에 없음(미확인). 드론 적용 미확인.
