---
title: "ZoomDet - Adaptive Image Zoom-in for UAV Object Detection"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-ai, ai-autonomy, computer-vision, object-detection]
sources: [raw/papers/ai-autonomy/zoomdet-adaptive-image-zoom-uav-detection.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# ZoomDet - Adaptive Image Zoom-in for UAV Object Detection

UAV-captured 이미지에서 객체 탐지는 작은 객체 크기로 인해 어려움이 있다. ZoomDet은 적응적 줌인 프레임워크로, 전경 객체가 일반 장면 이미지보다 작고 희소한 특성을 활용해 효과적인 탐지를 지원한다.

## 핵심 설계

### 1. Non-uniform Zooming
- 경량 오프셋 예측 방식
- 박스 기반 줌 목적 함수
- 입력 이미지에서 비균일 줌 변환 학습

### 2. Corner-Aligned Bounding Box Transformation
- 줌된 공간으로 ground-truth 바운딩 박스 왜핑
- 추론 시 예측된 박스를 원본 공간으로 역변환
- 아키텍처 독립적 적용 가능

## 성능

| 데이터셋 | 개선 | 모델 |
|---------|------|------|
| VisDrone | +8.4 mAP | Faster R-CNN |
| UAVDT | 유의미한 개선 | 다양한 모델 |
| SeaDronesSee | +8.4 mAP | Faster R-CNN |

- 추가 지연: 약 3ms
- 아키텍처 독립적: 임의의 객체 탐지 모델에 적용 가능

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 개요
- [[yolo]] — 실시간 객체 검출
- [[uav-detr-anti-drone-detection]] — WTConv 및 SWSA 기반 대드론 탐지
- [[pt-detr-small-target-detection]] — RT-DETR 기반 소형 객체 탐지

## 출처

- Wang et al., "Adaptive Image Zoom-in with Bounding Box Transformation for UAV Object Detection", arXiv:2602.07512, 2026.
