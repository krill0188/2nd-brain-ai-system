---
title: "ZoomDet: Adaptive Image Zoom-in for UAV Object Detection"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-ai, ai-autonomy, computer-vision, object-detection]
sources: [raw/papers/drone-ai/zoomdet-adaptive-image-zoom-uav-object-detection.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# ZoomDet: Adaptive Image Zoom-in for UAV Object Detection

UAV 촬영 이미지의 작은 객체 탐지를 위한 적응형 줌인 프레임워크. 비전경 객체가 일반 장면 대비 작고 희소한 특성을 활용해 효율적인 줌인 변환을 학습한다.

## 핵심 기여

1. **경량 오프셋 예측 체계**: 비균일 줌인을 위한 경량화된 오프셋 예측
2. **박스 기반 줌인 목적함수**: 모서리 정렬 바운딩 박스 변환 방법
3. **아키텍처 독립성**: Faster R-CNN 등 임의 탐지기에 적용 가능

## 성능

- SeaDronesSee 데이터셋: Faster R-CNN 대비 **mAP 8.4% 향상**
- 추가 지연: 약 **3ms**
- VisDrone, UAVDT, SeaDronesSee 벤치마크 검증

## 관련 개념

- [[uav-detr-anti-drone-detection]] — WTConv 및 SWSA 기반 대드론 탐지
- [[pt-detr-small-target-detection]] — 부분 인식 디테일 포커스 기반 소형 객체 탐지
- [[computer-vision-drone]] — 드론 컴퓨터 비전 개요

## 출처

Tao Wang et al., "Adaptive Image Zoom-in with Bounding Box Transformation for UAV Object Detection", arXiv:2602.07512, 2026. ^[raw/papers/drone-ai/zoomdet-adaptive-image-zoom-uav-object-detection.md]
