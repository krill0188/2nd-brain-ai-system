---
title: "UAV 다중분광 영상 기반 사과 수확 전 당도(SSC) 예측"
created: 2026-10-06
updated: 2026-10-06
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, drone-sw]
sources:
  - raw/papers/_unclassified/pre-harvest-prediction-of-apple-soluble-solids-content-using-uav-based-multispec.md
confidence: low
contested: false
contradictions: []
---

# UAV 다중분광 영상 기반 사과 수확 전 당도(SSC) 예측

정밀농업과학기술지(2026) 게재 논문(Chang-Hyeok Park, 경상국립대). UAV 다중분광 영상에서 얻은 식생지수만으로 사과의 수확 전 가용성 고형물 함량(SSC)을 예측하는 머신러닝 모델을 개발·검증했다. 원문은 비공개이고 초록이 중간에 절단되어 있어, 아래는 초록에 명시된 범위만 정리한다. ^[raw/papers/_unclassified/pre-harvest-prediction-of-apple-soluble-solids-content-using-uav-based-multispec.md]

## 데이터 수집 조건

- 대상: 경북 안동 10개 과수원의 '후지' 사과나무 39주, 2개 재배 시즌(2024–2025)
- 촬영일: 2024-09-17, 2025-09-16 정오
- 플랫폼/센서: Trinity F90+ 고정익 UAV + Altum-PT 다중분광 센서
- 비행 설정: 고도 150 m, 중복도 75%, 지상표본거리(GSD) 3.17 cm/pixel
- 전처리: 방사 보정 → 모자이킹 → 팬샤프닝 → NDVI로 식생/배경 분리, 이후 ARI·GLI·NDVI rededge 등 지수를 개체목 단위로 추출

## 의의와 한계

- 입력을 식생지수로만 제한해 센서 외 부가 계측 없이 개체목 단위 품질 예측이 가능한지를 검증하는 설계다.
- 모델 종류, 정확도(R², RMSE 등)는 초록 절단으로 확인되지 않아 성능 수치는 기록하지 않는다. 신뢰도 low.

## 관련 페이지

- [[drone-rice-heading-detection]] — 드론 영상 기반 벼 출수 판별(농업 분야 드론 AI 사례)
- [[kci-lightweight-uav-precision-imaging]] — 경량 UAV 정밀 영상 촬영
- [[drone-lidar-forest-boundary]] — 드론 LiDAR 기반 산림 경계 분석
