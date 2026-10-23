---
title: "Jetson AI Lab (archived) Benchmarks: Orin Nano vs Orin Nano Super - LLM/VLM/ViT"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson-orin, vlm, sam2, grounding-dino, benchmark]
sources: [inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]
confidence: medium
contested: false
contradictions: []
---

# Jetson AI Lab (archived) Benchmarks: Orin Nano vs Orin Nano Super - LLM/VLM/ViT

- 원문: https://www.jetson-ai-lab.com/archive/benchmarks.html^[inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]
- 제작: NVIDIA^[inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]

## 핵심 사양 (페이지 표 그대로, 단위 미표기 항목은 미표기)
대응 모델 카드: model-sam2, model-grounding-dino, model-smolvlm, model-phi-3, model-qwen2-5-vl.^[inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]
페이지는 "deprecated and no longer maintained" 로 표시된 아카이브.^[inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]

| 구분 | 모델 | Orin Nano(original) | Orin Nano Super | 배율 |
|---|---|---|---|---|
| SLM (INT4, MLC) | Phi 3.5 3B | 24.7 | 38.1 | 1.54 |
| SLM | Llama 3.2 3B | 27.7 | 43.07 | 1.55 |
| SLM | Gemma 2 2B | 21.5 | 34.97 | 1.63 |
| SLM | SmolLM2 | 41 | 64.5 | 1.57 |
| VLM | SmolVLM 2B | 8.1 | 12.9 | 1.59 |
| VLM | Qwen2 VL 2B | 2.8 | 4.4 | 1.57 |
| VLM | VILA 1.5 3B | 0.7 | 1.06 | 1.51 |
| VLM | PaliGemma2 3B | 13.7 | 21.6 | 1.58 |
| ViT | SAM2 base | 4.42 | 6.34 | 1.43 |
| ViT | Grounding DINO | 4.11 | 6.23 | 1.52 |
| ViT | DINOv2-base-patch14 | 75 | 126 | 1.68 |
| ViT | clip-vit-base-patch16 | 95 | 161 | 1.69 |

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- Orin Nano Super는 original 대비 위 표의 1.28~2.04배 값이 기재됨(InternVL2.5 4B 2.04, Gemma 2 9B 1.28).^[inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]
- 소형 VLM/ViT 모델이 Nano급에서 한 자릿수~수십 단위로 돌아가는 값이 기재되어 있어 드론 온보드 후보 선별 근거가 됨(단위 해석은 아래 한계 참조).^[inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]

## 한계·미확인
- VLM/ViT 표의 단위(fps? tokens/s?), 양자화, JetPack, 전력모드는 페이지에 미표기 = 미확인. LLM 표는 INT4 MLC 기준이나 단위도 미표기.^[inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]
- AGX Orin 및 AGX Thor 결과는 이미지(차트)만 있어 수치 미확인.^[inbox/processed/hw-20261021-model-jetson-ai-lab-orin-nano-super.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
