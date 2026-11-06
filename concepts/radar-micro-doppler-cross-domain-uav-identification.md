---
title: "레이다 마이크로 도플러 신호 증강 기반 교차 도메인 UAV 식별"
created: 2026-11-05
updated: 2026-11-05
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, datalink]
sources:
  - inbox/fetch-2026-11-05-kci-딥러닝-기반-교차-도메인-uav-식별을-위한-레이다-마이크로-도플러-신호-증강-전략.md
confidence: low
contested: false
contradictions: []
---

# 레이다 마이크로 도플러 신호 증강 기반 교차 도메인 UAV 식별

한국전자파학회 논문지(2026) 게재 논문 초록 기준 요약이다. 원문은 비공개(페이월)다.^[inbox/fetch-2026-11-05-kci-딥러닝-기반-교차-도메인-uav-식별을-위한-레이다-마이크로-도플러-신호-증강-전략.md]

## 문제 정의
기존 딥러닝 분류기는 호버링(hovering) 데이터에 과적합되어 기동, 측정환경, 레이다 파라미터가 변화하는 교차 도메인(cross-domain) 환경에서 성능이 크게 저하된다.

## 제안 기법: 계층적 물리 기반 데이터 증강
1. **1차원 복소 시계열 레벨**: 표적 동역학·잡음·시스템 파라미터 변동을 물리 모델 기반으로 모사
2. **2차원 스펙트로그램 레벨**: 무작위 마스킹(random masking)을 결합하여 특징 벡터의 가변성 극대화

## 검증 결과
- 실제 기동 및 환경 변화, 상이한 펄스 반복 주파수(PRF)가 적용된 독립 실측 데이터셋으로 검증
- **교차 도메인 식별 정확도**: 99.56% 달성
- 도메인 간극(domain gap)을 효과적으로 극복함 실증

## 의의
운용 조건 변화에 강건한 레이다 기반 UAV 식별을 위한 물리 모델 기반 데이터 증강 전략의 유효성을 입증함.

## 관련
대드론 탐지 기술은 [[uav-detr-anti-drone-detection]], [[wave-detr-multimodal-drone-detector]], 마이크로 도플러 기초는 [[kci-cepstrum-single-microphone-drone-distance]], 레이다 기반 통신은 [[rf-datalink-engineering]] 참조.