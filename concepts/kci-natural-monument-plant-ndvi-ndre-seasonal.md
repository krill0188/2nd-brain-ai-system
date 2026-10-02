---
title: "다분광 드론 영상 기반 천연기념물 식물유산의 기능형별 NDVI·NDRE 계절 변동 분석"
created: 2026-10-02
updated: 2026-10-02
type: concept
domain: ops-mission
tags: [drone, ops-mission]
sources: [inbox/processed/fetch-2026-10-02-kci-다분광-드론-영상-기반-천연기념물-식물유산의-기능형별-ndvindre-계절-변동-분석.md]
confidence: medium
contested: false
contradictions: []
---

# 다분광 드론 영상 기반 천연기념물 식물유산의 기능형별 NDVI·NDRE 계절 변동 분석

정수호(전남광주통합특별시농업기술원)가 스마트미디어저널(2026)에 발표한 연구로, 천연기념물
식물유산을 반복 UAV 다분광 영상으로 관측해 낙엽성·상록성 기능형의 계절 변동을
분석했다.^[inbox/processed/fetch-2026-10-02-kci-다분광-드론-영상-기반-천연기념물-식물유산의-기능형별-ndvindre-계절-변동-분석.md]

## 방법

- 2025년 9개 대상지에서 74회 UAV 촬영으로 NDVI·NDRE 시계열 구축.
- 대상지별 기준수준과 연중일수(DOY)의 비선형 변화를 반영한 **cubic spline 모형**으로 계절궤적·
  계절진폭 추정.
- 기능형(낙엽성/상록성) 간 차이는 대상지 수준 정확 순열검정(exact permutation test)으로 평가.

## 결과

- 낙엽성 기능형은 계절에 따라 식생지수가 크게 증가·감소한 반면, 상록성 기능형은 상대적으로
  작은 변동을 보임 — 이 차이는 다양한 분석조건에서도 동일한 방향으로 유지되었고, 2026년
  초기생육기에도 유사하게 재현됨.
- 동일한 식생지수 값이라도 기능형과 관측시기에 따라 다르게 해석될 수 있음을 시사.
- 결론적으로 식물유산 장기 모니터링에는 단일 시점 지수나 일률적 기준보다 **기능형별 계절궤적과
  변동범위**를 함께 고려해야 한다고 제안.

## 관련 개념

- [[kci-hallasan-fir-ndvi-vitality-assessment]] — 드론 다중분광 NDVI 기반 한라산 구상나무 고도·
  사면향별 활력도 평가(유사 모니터링 방법론)
- [[kci-barley-wet-stress-hyperspectral-detection]] — UAV 초분광 영상 기반 작물 스트레스 조기
  탐지(식생지수 응용 사례)
