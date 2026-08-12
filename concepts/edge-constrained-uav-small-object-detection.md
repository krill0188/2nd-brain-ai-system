---
title: "Edge-Constrained UAV Small-Object Detection with P2 Enhancement"
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [drone, drone-ai, computer-vision, yolo, hardware]
domain: ai-autonomy
sources: [inbox/fetch-2026-08-12-arxiv-edge-constrained-uav-small-object-detection-with-p2-enhancem.md]
confidence: medium
contested: false
contradictions: []
---

# Edge-Constrained UAV Small-Object Detection with P2 Enhancement

## 개요

온보드 연산 및 메모리 제약 환경에서 UAV 객체 탐지를 위한 경량화 접근법. P2 고해상도 탐지 브랜치와 양자-영감 진화 알고리즘(QIEA)을 결합한 YOLOX-Nano 기반 프레임워크.

## 핵심 기술

### P2 고해상도 탐지 브랜치
- 반복적 다운샘플링으로 인한 공간 정보 손실 방지
- 작은 객체의 세부 정보 보존
- VisDrone 데이터셋에서 AP_small 31.10% 향상

### QIEA (Quantum-Inspired Evolutionary Algorithm)
- 경량 구조 탐색을 위한 양자-영감 진화 알고리즘
- 탐색 공간: 경량 우선순위 + 작업 특이성
- 평가 지표: 정확도, FLOPs, 지연시간, 메모리, 재현율

## 성능 비교

| 모델 | AP_small | AP_medium | 개선점 |
|------|----------|-----------|--------|
| YOLOX-Nano | baseline | baseline | - |
| YOLOX-Nano+P2 | +31.10% | - | 고해상도 브랜치 |
| vs NanoDet-Plus | +17.5% | +44.9% | 유사 모델 크기 |

## 실험 결과

- **P2 브랜치**: AP 중심 최고 성능
- **QIEA**: Recall 중심 후보 선별에 효과적
- **프록시 순위**: 최종 AP 성능으로 직접 전이되지 않음

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 YOLO 통합
- [[yolo]] — 실시간 객체 검출 딥러닝 아키텍처
- [[companion-computer]] — AI/영상처리 오프로드 보조 컴퓨터
- [[drone-hw]] — 드론 하드웨어 도메인 개요

## 출처

Wuming Lei et al., "Edge-Constrained UAV Small-Object Detection with P2 Enhancement and Quantum-Inspired Lightweight Structure Search", arXiv:2606.09081, 2026-06-08.
