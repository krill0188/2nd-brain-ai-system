---
title: "YOLOv10: Real-Time End-to-End Object Detection"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: PerceptionModel
tags: [drone, ai, object-detection, yolo, nms-free]
sources: [inbox/processed/hw-20261021-model-yolov10.md]
confidence: medium
contested: false
contradictions: []
---

# YOLOv10: Real-Time End-to-End Object Detection

- 원문: https://arxiv.org/abs/2405.14458^[inbox/processed/hw-20261021-model-yolov10.md]
- 제작: Tsinghua University (THU-MIG)^[inbox/processed/hw-20261021-model-yolov10.md]

## 핵심 사양
| 항목 | 값 (초록 기준) |
|---|---|
| 저자 | Ao Wang, Hui Chen, Lihao Liu, Kai Chen, Zijia Lin, Jungong Han, Guiguang Ding |
| 제출 | 2024-05-23 (v1), v2 2024-10-30 (NeurIPS 2024 camera-ready) |
| 핵심 기법 | consistent dual assignments for NMS-free training, holistic efficiency-accuracy driven design |
| 비교 1 | YOLOv10-S는 RT-DETR-R18 대비 약 1.8x 빠르고 파라미터·FLOPs 약 2.8x 적음(유사 AP, COCO) |
| 비교 2 | YOLOv10-B는 YOLOv9-C 대비 지연 약 46% 감소, 파라미터 25% 감소(동일 성능) |
## 용도
NMS 후처리가 없어 지연 변동이 작은 end-to-end 검출. 코드: github.com/THU-MIG/yolov10 (초록에 링크).^[inbox/processed/hw-20261021-model-yolov10.md]
## 비고(미확인)
파라미터 절대값, 입력 해상도, 라이선스, Jetson 속도, TensorRT/ONNX 문구는 초록 페이지에서 미확인. 드론 적용 사례 미확인.^[inbox/processed/hw-20261021-model-yolov10.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
