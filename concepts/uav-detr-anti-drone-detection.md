---
title: "UAV-DETR: DETR for Anti-Drone Target Detection"
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [drone, drone-ai, computer-vision, detection, c-uas]
domain: ai-autonomy
sources: [inbox/fetch-2026-08-12-arxiv-uav-detr-detr-for-anti-drone-target-detection.md]
confidence: medium
contested: false
contradictions: []
---

# UAV-DETR: DETR for Anti-Drone Target Detection

## 개요

대드론(C-UAS) 응용을 위한 실시간 객체 탐지 프레임워크. WTConv 강화 백본과 Sliding Window Self-Attention 인코더를 통합한 DETR 기반 아키텍처.

## 핵심 기술

### WTConv-Enhanced Backbone
- 작은 표적의 고주파 구조적 세부 정보 포착
- 파라미터 오버헤드 대폭 감소

### SWSA-IFI (Sliding Window Self-Attention)
- 효율적인 Self-Attention 메커니즘
- 작은 객체 탐지에 최적화

### ECFRFN (Efficient Cross-Scale Feature Recalibration and Fusion Network)
- 배경 노이즈 억제
- 다중 스케일 의미 정보 집계

### 손실 함수
- **Hybrid Inner-CIoU + NWD Loss**: 작은 객체의 미세 위치 편차에 대한 표준 IoU 메트릭의 극단적 민감성 완화

## 성능 결과

| 데이터셋 | 지표 | 개선 |
|----------|------|------|
| Custom UAV | mAP50:95 | +6.61% |
| Custom UAV | 파라미터 | -39.8% |
| DUT-ANTI-UAV | Precision | +1.4% |
| DUT-ANTI-UAV | F1-Score | +1.0% |

## 특징

- **효율성**: RT-DETR 대비 39.8% 파라미터 감소
- **정확도**: 복잡한 배경 및 열악한 환경에서 소형 드론 탐지
- **실시간**: 보안 및 대드론 응용에 적합한 실시간 성능

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 객체 추적
- [[yolo]] — 실시간 객체 검출 딥러닝 아키텍처
- [[droneshield]] — 대드론 탐지/방어 기업 및 RfAI-3 엔진
- [[dfend-counter-drone-worldcup]] — 대드론 작전 및 보안 응용

## 출처

Jun Yang et al., "UAV-DETR: DETR for Anti-Drone Target Detection", arXiv:2603.22841, 2026-03-24.

## 📰 최근 관련 소식
- Pennsylvania National Guard Becomes Hub for Pentagon’s Drone Dominance Program (dronelife.com, Fri, 14 Au) — https://dronelife.com/2026/08/14/pennsylvania-national-guard-drone-dominance/
