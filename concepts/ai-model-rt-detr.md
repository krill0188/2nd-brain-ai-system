---
title: "RT-DETR: DETRs Beat YOLOs on Real-time Object Detection"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: PerceptionModel
tags: [drone, ai, object-detection, detr, transformer]
sources: [inbox/processed/hw-20261021-model-rt-detr.md]
confidence: medium
contested: false
contradictions: []
---

# RT-DETR: DETRs Beat YOLOs on Real-time Object Detection

- 원문: https://arxiv.org/abs/2304.08069^[inbox/processed/hw-20261021-model-rt-detr.md]
- 제작: Baidu 계열 저자 (Yian Zhao, Wenyu Lv 외)^[inbox/processed/hw-20261021-model-rt-detr.md]

## 핵심 사양 (초록)
| 항목 | 값 |
|---|---|
| 제출 | 2023-04-17 (v1), v3 2024-04-03 |
| RT-DETR-R50 / R101 | "53.1% / 54.3% AP on COCO and 108 / 74 FPS on T4 GPU" |
| 대비 | DINO-R50 보다 +2.2% AP, 약 21배 FPS |
| Objects365 사전학습 후 | R50 / R101 = 55.3% / 56.2% AP |
## 구조
efficient hybrid encoder(intra-scale 상호작용과 cross-scale 융합 분리), uncertainty-minimal query selection. 디코더 층 수를 조정해 재학습 없이 속도-정확도 조절 가능.^[inbox/processed/hw-20261021-model-rt-detr.md]
## 비고(미확인)
파라미터 수, 라이선스, Jetson 수치, TensorRT/ONNX 문구는 초록에 없음(미확인). 드론 적용은 ~/2nd/concepts의 rt-detr-plus-uav-detection, drone-wildfire-rt-detr 등과 중복(보강).^[inbox/processed/hw-20261021-model-rt-detr.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
