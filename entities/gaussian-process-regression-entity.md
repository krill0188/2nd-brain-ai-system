---
title: "Gaussian process regression"
created: 2026-10-24
updated: 2026-10-24
type: entity
tags: [ai-autonomy, navigation-gnss-denied, sensing-perception]
sources: []
confidence: medium
contradictions: []
domain: ai-autonomy
contested: false
---

# Gaussian process regression

Gaussian process regression (GPR)는 스페클트럼 감지 및 3차원 라디오 환경 지도(REM) 재구성에 사용되는 공간 예측 모델입니다. 단순한 크기쾅(Kriging) 변종들에 비해 샘플 수가 증가할수록 안정적인 성능을 보이며, REM 재구성의 전체적인 베이스라인(baseline) 모델로 활용됩니다.

## 개요

본 문서에서 인용된 원문(Rahman et al., 2026)에 따르면, Gaussian process regression(GPR)은 크기쾅(Kriging) 및 그 변형 모델들과 비교하여 REM 재구성 정확도에서 가장 안정적인 전체 베이스라인 모델로 평가되었습니다. simple Kriging(SK)과 trans-Gaussian Kriging은 샘플이 매우 드문 극한 조건에서는 높은 정확도를 보이나, ordinary Kriging(OK)은 샘플 수가 증가할수록 성능이 향상되는 반면, GPR은 다양한 조건에서 일관된 성능을 제공합니다. 이는 UAV 기반의 3D 스펙트럼 센싱 환경에서 측정 데이터의 불일치성과 공중기체(airframe) 영향으로 인한 안테나 패턴 왜곡을 보정하는 데 적합한 모델로 활용됩니다.

## 활용처

- UAV 기반 3D 라디오 환경 지도(REM) 재구성에서 공간 예측 모델로 활용됩니다.
- 동적인 UAV 비행 행동으로 인한 측정 불일치를 보정하는 데 기여합니다.

## 관련 페이지

- [[Radio Environment Map (REM)]] — Gaussian process regression이 재구성 정확도를 높이는 대상 모델
- [[Spectrum Sensing]] — GPR이 적용되는 주요 기술 분야

## 출처

- (사용자 재확인 필요)

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
