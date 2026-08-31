---
title: Drone Wildfire Monitoring RT-DETR
created: 2026-09-01
updated: 2026-09-01
type: concept
tags: [drone, drone-ai, wildfire, detection, rt-detr, kci]
sources: [inbox/fetch-2026-09-01-kci-드론-영상-기반-실시간-산불-감시를-위한-연기-특화-rt-detr-개선-모델-설계-및-성능-분석.md]
confidence: high
contested: false
contradictions: []
---

# 드론 영상 기반 실시간 산불 감시 RT-DETR 개선 모델

드론 영상을 활용한 산불 연기 조기 감지를 위한 RT-DETR 기반 개선 모델. 국립경국대학교 조영복 연구.

## 문제 정의

드론 특유의 도전 과제:
- **고도 변화**: 다양한 고도에서의 촬영
- **시점 다양성**: 여러 각도에서의 영상
- **소형 연기 객체**: 작은 연기 입자 탐지

## 제안 모델 구조

### 백본 개선: SCPConvBlock

- **SCPConv**: 채널 중요도 기반 선택적 합성곱 모듈
- **EMA**: 효율적 다중 스케일 어텐션(Efficient Multi-scale Attention)
- **결합**: SCPConv + EMA로 SCPConvBlock 구성

### 특징 피라미드: MSFFPN

- **MSFFPN**: 전경집중 다중 스케일 피라미드 네트워크
- **목적**: 소형·희박 연기의 배경 혼동 문제 해소

## 성능 결과

| 지표 | RT-DETR 대비 개선 |
|------|------------------|
| **Precision** | 0.883 (+0.7%p) |
| **Recall** | 0.800 (+2.4%p) |
| **mAP50** | 0.862 (+3.8%p) |
| **mAP95** | 0.539 (+2.2%p) |

## 학습 효율성

- **수렴 에포크**: 125 → 25 (약 80% 단축)

## 관련 개념

- [[rt-detr]] — RT-DETR 객체 검출
- [[computer-vision-drone]] — 드론 컴퓨터 비전
- [[wildfire-monitoring]] — 산불 감시
