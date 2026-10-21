---
title: "Qwen2.5-VL Technical Report"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: AIModel
tags: [drone, ai, vlm, grounding, video]
sources: [inbox/processed/hw-20261021-model-qwen2-5-vl.md]
confidence: medium
contested: false
contradictions: []
---

# Qwen2.5-VL Technical Report

- 원문: https://arxiv.org/abs/2502.13923^[inbox/processed/hw-20261021-model-qwen2-5-vl.md]
- 제작: Alibaba Qwen (Shuai Bai 외 26명)^[inbox/processed/hw-20261021-model-qwen2-5-vl.md]

## 핵심 사양 (초록)
- 3개 크기, 초록은 플래그십 Qwen2.5-VL-72B만 명시(나머지 파라미터 수는 초록에 없음).^[inbox/processed/hw-20261021-model-qwen2-5-vl.md]
- 72B가 'matches state-of-the-art models like GPT-4o and Claude 3.5 Sonnet'이라고 주장(문서·도표 이해에 강점).^[inbox/processed/hw-20261021-model-qwen2-5-vl.md]
- 바운딩 박스/점으로 객체 위치 지정(grounding), 동적 해상도 ViT(Window Attention), 최대 수 시간 영상과 초 단위 이벤트 위치 지정(절대 시간 인코딩).^[inbox/processed/hw-20261021-model-qwen2-5-vl.md]
- 제출 2025-02-19.^[inbox/processed/hw-20261021-model-qwen2-5-vl.md]
## 비고(미확인)
라이선스, 엣지 속도, 양자화 수치 초록에 없음(미확인). 드론 적용 사례 없음(미확인). VLM 항법은 ~/2nd/concepts vlm-* 문서와 인접(보강).^[inbox/processed/hw-20261021-model-qwen2-5-vl.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
