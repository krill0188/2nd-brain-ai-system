---
title: "UAV-DETR - DETR for Anti-Drone Target Detection"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-ai, ai-autonomy, object-detection, detr, counter-uav]
sources: [raw/papers/ai-autonomy/uav-detr-anti-drone-detection.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# UAV-DETR - DETR for Anti-Drone Target Detection

실시간 대드론 탐지를 위한 DETR 기반 프레임워크. WTConv 강화 백본과 Sliding Window Self-Attention을 활용해 소형 드론을 복잡한 배경에서 탐지.

## 핵심 구성요소

### 1. WTConv-Enhanced Backbone
- Wavelet Transform 기반 Convolution
- 소형 대상의 고주파 구조적 디테일 캡처
- 파라미터 오버헤드 대폭 감소

### 2. SWSA-IFI (Sliding Window Self-Attention)
- 인코더에 통합된 슬라이딩 윈도우 자기 주의
- 효율적인 특징 표현 학습

### 3. ECFRFN (Efficient Cross-Scale Feature Recalibration and Fusion Network)
- 배경 노이즈 억제
- 다중 스케일 의미론적 정보 집계

### 4. Hybrid Loss Strategy
- Inner-CIoU + NWD (Normalized Wasserstein Distance) 손실
- 소형 객체의 미세 위치 편차에 대한 IoU 민감도 완화

## 성능

| 데이터셋 | mAP50:95 | Precision | F1-Score | 파라미터 |
|---------|----------|-----------|----------|----------|
| Custom UAV | +6.61% | - | - | -39.8% |
| DUT-ANTI-UAV | - | +1.4% | +1.0% | - |

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 개요
- [[yolo]] — 실시간 객체 검출
- [[pt-detr-small-target-detection]] — RT-DETR 기반 소형 객체 탐지
- [[zoomdet-uav-adaptive-detection]] — 적응적 줌인 UAV 객체 탐지

## 출처

- Yang et al., "UAV-DETR: DETR for Anti-Drone Target Detection", arXiv:2603.22841, 2026.
- Code: https://github.com/wd-sir/UAVDETR
