---
title: "PT-DETR - Partially-Aware Detail Focus for Small Target Detection"
created: 2026-08-20
updated: 2026-10-01
type: concept
tags: [drone-ai, ai-autonomy, object-detection, detr]
sources: [raw/papers/ai-autonomy/pt-detr-small-target-detection.md, raw/papers/_unclassified/드론-탐지를-위한-효과적인-특징-기반-후처리-기법.md, raw/papers/_unclassified/감시-드론을-위한-심층-신경망-기반-지상-표적-추적-기법.md]
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

PT-DETR은 영상(RGB) 기반 소형 객체 탐지 계열이다. 같은 "소형 표적 탐지" 문제를 다른 센서
모달리티로 접근한 국내 연구 두 편이 있다: 레이더 도플러 스펙트럼 특징을 CFAR 후처리에
결합해 낮은 SCR 환경의 오경보율을 낮추는 기법^[raw/papers/_unclassified/드론-탐지를-위한-효과적인-특징-기반-후처리-기법.md],
그리고 RetinaNet 탐지에 칼만 필터를 결합해 지상 표적 추적 정확도를 높이는 기법이다
^[raw/papers/_unclassified/감시-드론을-위한-심층-신경망-기반-지상-표적-추적-기법.md].
두 연구 모두 "탐지만으로는 부족하며 후처리/추적 단계 결합이 성능을 좌우한다"는 PT-DETR의
문제의식과 접근 방향을 공유한다.

## 관련 개념

- [[yolo]] — 실시간 객체 검출
- [[uav-detr-anti-drone-detection]] — WTConv 및 SWSA 기반 대드론 탐지
- [[zoomdet-uav-adaptive-detection]] — 적응적 줌인 UAV 객체 탐지
- [[computer-vision-drone]] — 드론 컴퓨터 비전 개요
- [[kci-drone-detection-cfar-feature-postprocessing]] — 레이더 CFAR 특징 기반 드론 탐지 후처리(대비 모달리티)
- [[kci-ground-target-tracking-retinanet-kalman]] — RetinaNet+칼만필터 기반 지상 표적 추적(탐지+추적 결합)

## 출처

- Huo & Wang, "PT-DETR: Small Target Detection Based on Partially-Aware Detail Focus", arXiv:2510.26630, 2025.
