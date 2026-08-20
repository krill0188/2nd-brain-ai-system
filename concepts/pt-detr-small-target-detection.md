---
title: "PT-DETR - Partially-Aware Detail Focus for Small Target Detection"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-ai, ai-autonomy, object-detection, detr]
sources: [raw/papers/ai-autonomy/pt-detr-small-target-detection.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# PT-DETR - Partially-Aware Detail Focus for Small Target Detection

RT-DETR 기반 UAV 영상 소형 객체 탐지 알고리즘. 복잡한 배경, 심각한 occlusion, 밀집 소형 객체, 변화하는 조명 조건에 특화.

## 핵심 모듈

### 1. PADF (Partially-Aware Detail Focus)
- 백본 네트워크에 통합
- 소형 객체 특징 추출 강화

### 2. MFFF (Median-Frequency Feature Fusion)
- 소형 객체 디테일 및 문맥 정보 캡처 능력 향상
- 중간 주파수 특징 융합

### 3. Focaler-SIoU
- 바운딩 박스 매칭 능력 강화
- 소형 객체 특징에 대한 민감도 증가

## 성능

| 데이터셋 | 개선 | 비고 |
|---------|------|------|
| VisDrone2019 | +1.6% mAP | 더 낮은 계산 복잡도 |
| VisDrone2019 | +1.7% mAP | 더 적은 파라미터 |

## 관련 개념

- [[yolo]] — 실시간 객체 검출
- [[uav-detr-anti-drone-detection]] — WTConv 및 SWSA 기반 대드론 탐지
- [[zoomdet-uav-adaptive-detection]] — 적응적 줌인 UAV 객체 탐지
- [[computer-vision-drone]] — 드론 컴퓨터 비전 개요

## 출처

- Huo & Wang, "PT-DETR: Small Target Detection Based on Partially-Aware Detail Focus", arXiv:2510.26630, 2025.
