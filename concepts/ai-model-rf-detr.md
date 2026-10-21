---
title: "RF-DETR (Roboflow)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: PerceptionModel
tags: [drone, ai, object-detection, segmentation, detr]
sources: [inbox/processed/hw-20261021-model-rf-detr.md]
confidence: medium
contested: false
contradictions: []
---

# RF-DETR (Roboflow)

- 원문: https://github.com/roboflow/rf-detr^[inbox/processed/hw-20261021-model-rf-detr.md]
- 제작: Roboflow^[inbox/processed/hw-20261021-model-rf-detr.md]

## 핵심 사양 (README, COCO val2017, T4 TensorRT FP16, batch 1)
| 크기 | AP50:95 | 지연(ms) | 파라미터(M) | 해상도 | 라이선스 |
|---|---|---|---|---|---|
| Nano | 48.4 | 2.3 | 30.5 | 384x384 | Apache 2.0 |
| Small | 53.0 | 3.5 | 32.1 | 512x512 | Apache 2.0 |
| Medium | 54.7 | 4.4 | 33.7 | 576x576 | Apache 2.0 |
| Large | 56.5 | 6.8 | 33.9 | 704x704 | Apache 2.0 |
| 2XLarge (plus) | 60.1 | 17.2 | 126.9 | 880x880 | PML 1.0 |
(Atto 30.5 AP/1.0 ms/7.4M, Femto 37.8/1.4/7.9, Pico 41.6/1.7/8.4, XLarge 58.6/11.5/126.4 도 README에 있음, plus 패키지·PML 1.0)^[inbox/processed/hw-20261021-model-rf-detr.md]
인스턴스 분할: SegNano 40.3 AP / 3.4 ms / 33.6M(312x312) ~ Seg2XL 49.9 / 21.8 / 38.6(768x768). 키포인트 Preview: AP50:95 71.8, 9.7 ms, 40.7M.^[inbox/processed/hw-20261021-model-rf-detr.md]
## 비고
측정 조건: 지연은 T4 TensorRT FP16 batch 1, 정확도는 pycocotools 전체 5000장 val2017, 파라미터는 fused 배포 모듈 기준. README에 ONNX 내보내기 설명 없음, Jetson 수치 미확인. 드론 적용 사례 미확인.^[inbox/processed/hw-20261021-model-rf-detr.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
