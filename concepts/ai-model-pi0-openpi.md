---
title: "pi0 / pi0-FAST / pi0.5 (openpi)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: AIModel
tags: [drone, ai, vla, flow-matching, robot-policy]
sources: [inbox/processed/hw-20261021-model-pi0-openpi.md]
confidence: medium
contested: false
contradictions: []
---

# pi0 / pi0-FAST / pi0.5 (openpi)

- 원문: https://github.com/Physical-Intelligence/openpi^[inbox/processed/hw-20261021-model-pi0-openpi.md]
- 제작: Physical Intelligence^[inbox/processed/hw-20261021-model-pi0-openpi.md]

## 핵심 사양 (README)
| 모델 | 설명(원문) |
|---|---|
| pi0 | flow-based vision-language-action model |
| pi0-FAST | autoregressive VLA based on the FAST action tokenizer (PyTorch 미지원) |
| pi0.5 | upgraded pi0, better open-world generalization trained with knowledge insulation |
| 요구 GPU 메모리 | 추론 > 8 GB (RTX 4090 예), LoRA 미세조정 > 22.5 GB, 전체 미세조정 > 70 GB (A100 80GB / H100) |
라이선스: 저장소 Apache-2.0 (LICENSE_GEMMA.txt 별도 포함, 내용 README에 설명 없음). 웹소켓 원격 추론 지원. DROID/ALOHA/LIBERO용 미세조정 체크포인트 존재.^[inbox/processed/hw-20261021-model-pi0-openpi.md]
## 비고(미확인)
파라미터 수는 README에 없음(미확인). Jetson 속도·드론 적용 사례 미확인. 로봇 팔 조작 정책이며 드론 항법용 아님.^[inbox/processed/hw-20261021-model-pi0-openpi.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
