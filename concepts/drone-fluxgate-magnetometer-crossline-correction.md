---
title: "드론 탑재 삼성분 플럭스게이트 자력탐사 교차점 오차 보정"
created: 2026-09-05
updated: 2026-09-05
type: concept
domain: hardware
tags: [drone, hardware, drone-hw]
sources: [raw/papers/_unclassified/드론-탑재-삼성분-플럭스게이트-자력탐사자료의-교차점-오차-분석-및-보정.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 탑재 삼성분 플럭스게이트 자력탐사 교차점 오차 보정

무인 멀티콥터에 탑재한 벡터 자력계(삼성분 플럭스게이트)로 자력탐사를 수행할 때 발생하는 측선 간
교차점(crossline) 오차의 원인을 분석하고 보정하는 연구다. 플럭스게이트 자력계는 소형 이동체 탑재가
용이하지만 잡음이 크고 측선 간 오차가 뚜렷하다 ^[raw/papers/_unclassified/드론-탑재-삼성분-플럭스게이트-자력탐사자료의-교차점-오차-분석-및-보정.md].

## 핵심 발견

- 드론 탐사는 비행 시간이 1~2시간으로 짧고 플랫폼이 상자성체 위주라 점성자화 영향이 미미해
  선형 오차가 크게 나타나지 않음.
- 측선 간 레벨링 보정만으로 교차점 오차가 효과적으로 보정됨을 확인.
- 벡터 성분이상의 교차점 오차가 스칼라 이상의 교차점 오차보다 크며, 이는 자세 센서 내재 오차에서
  기인 — 회전 불변량인 스칼라 오차와는 본질적으로 원인이 다름을 정량적으로 규명.

## 관련 개념

- [[drone-payload-systems]] — 카메라, 짐벌, 페이로드 트리거 등 드론 페이로드 통합
- [[sensor-calibration]] — Accel/Gyro/Compass/Baro 등 센서 캘리브레이션
