---
title: "YOLOv12: Attention-Centric Real-Time Object Detectors"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: PerceptionModel
tags: [drone, ai, object-detection, yolo, attention]
sources: [inbox/processed/hw-20261021-model-yolov12.md]
confidence: medium
contested: false
contradictions: []
---

# YOLOv12: Attention-Centric Real-Time Object Detectors

- 원문: https://arxiv.org/abs/2502.12524^[inbox/processed/hw-20261021-model-yolov12.md]
- 제작: Yunjie Tian, Qixiang Ye, David Doermann (논문 저자)^[inbox/processed/hw-20261021-model-yolov12.md]

## 핵심 사양 (초록 기준)
| 항목 | 값 |
|---|---|
| 제출 | 2025-02-18 (arXiv:2502.12524 v1) |
| YOLOv12-N | 40.6% mAP, T4 GPU 1.64 ms 지연; YOLOv10-N/YOLOv11-N 대비 +2.1% / +1.2% mAP (유사 속도) |
| YOLOv12-S | RT-DETR-R18, RT-DETRv2-R18 대비 42% 빠르고, 연산 36%, 파라미터 45% |
## 용도
어텐션 중심 구조이면서 CNN급 속도를 목표로 하는 실시간 검출.^[inbox/processed/hw-20261021-model-yolov12.md]
## 비고(미확인)
입력 해상도·라이선스·Jetson 수치·내보내기 지원은 초록 페이지에 없음(미확인). 원문 초록 전문은 도구의 인용 길이 제한(125자)으로 요약 인용만 확인.^[inbox/processed/hw-20261021-model-yolov12.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
