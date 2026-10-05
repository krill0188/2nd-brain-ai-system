---
title: "전기 추진 고정익 무인기 복귀 가능 여부 판단 로직 (KCI)"
created: 2026-10-05
updated: 2026-10-05
type: concept
domain: flight-control
tags: [drone, research]
sources: [raw/papers/_unclassified/전기-추진-시스템을-이용하는-고정익-무인기를-위한-복귀-가능-여부-판단-로직-설계.md]
confidence: low
contested: false
contradictions: []
---

# 전기 추진 고정익 무인기 복귀 가능 여부 판단 로직

전선재(국방과학연구소)가 한국군사과학기술학회지(2026)에 발표. 원문 비공개이고 초록이 절단되어 비행시험 비교 결과는
확인하지 못했다.^[raw/papers/_unclassified/전기-추진-시스템을-이용하는-고정익-무인기를-위한-복귀-가능-여부-판단-로직-설계.md]

- 목적: 임무 중 돌발 중단 시 안전한 RTB(복귀) 가능 여부를 실시간 판단.
- 로직: 복귀점까지의 수직·수평 비행 거리로 예상 에너지 소모를 계산하고, 이로부터 **복귀점 도착 시 잔여 전압**을 예측해 판단.
- 예측 잔여 전압이 기준 이하이면 잔여 비행 가능 거리를 계산해 복귀점을 동적으로 조정한다.
- 검증: 비행시험 결과와 예측값을 비교(결과 수치는 초록 절단).

## 관련 개념

- [[drone-safety-failsafe]] — 페일세이프 일반
- [[kci-uav-battery-ecm-parameter-estimation]] — 전압 예측에 쓸 수 있는 배터리 모델
- [[drone-power-battery]] — 전원·배터리 맥락
