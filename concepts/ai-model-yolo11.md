---
title: "Ultralytics YOLO11"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: PerceptionModel
tags: [drone, ai, object-detection, yolo, edge-inference]
sources: [inbox/processed/hw-20261021-model-yolo11.md]
confidence: medium
contested: false
contradictions: []
---

# Ultralytics YOLO11

- 원문: https://docs.ultralytics.com/models/yolo11/^[inbox/processed/hw-20261021-model-yolo11.md]
- 제작: Ultralytics^[inbox/processed/hw-20261021-model-yolo11.md]

## 핵심 사양 (공식 문서 표, COCO, 입력 640 px)
| 모델 | mAP val 50-95 | CPU ONNX (ms) | T4 TensorRT10 (ms) | 파라미터 (M) | FLOPs (B) |
|---|---|---|---|---|---|
| YOLO11n | 39.5 | 56.1 ± 0.8 | 1.5 ± 0.0 | 2.6 | 6.5 |
| YOLO11s | 47.0 | 90.0 ± 1.2 | 2.5 ± 0.0 | 9.4 | 21.6 |
| YOLO11m | 51.5 | 183.2 ± 2.0 | 4.7 ± 0.1 | 20.1 | 68.1 |
| YOLO11l | 53.4 | 238.6 ± 1.4 | 6.2 ± 0.1 | 25.3 | 87.2 |
| YOLO11x | 54.7 | 462.8 ± 6.7 | 11.3 ± 0.2 | 56.9 | 195.3 |

## 용도
검출, 인스턴스 분할(-seg), 분류(-cls), 포즈(-pose), 회전 박스 OBB(-obb) 태스크 지원. 드론 영상 검출·추적의 기본 후보.^[inbox/processed/hw-20261021-model-yolo11.md]
## 라이선스 / 지원
AGPL-3.0 및 Enterprise 라이선스. 벤치마크는 CPU ONNX와 T4 TensorRT10 기준으로 측정(엔진 내보내기 형식 전체 목록은 이 페이지에 없음 -> 미확인).^[inbox/processed/hw-20261021-model-yolo11.md]
## 비고(미확인)
Jetson Orin 공식 수치: 이 페이지에 없음(미확인). 페이지는 YOLO11을 "Current stable release"로 소개하며 NMS-free 최신 모델로 YOLO26을 안내함. 드론 적용 사례: 이 페이지에 없음. ~/2nd/concepts/yolo.md 와 주제 중복 가능(보강).^[inbox/processed/hw-20261021-model-yolo11.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
