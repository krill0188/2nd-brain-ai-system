---
title: "EKF"
created: 2026-10-24
updated: 2026-10-24
type: entity
tags: [localization, uwb, swarm, kalman-filter]
sources: []
confidence: medium
contested: false
contradictions: []
domain: navigation-gnss-denied
---

# EKF

Extended Kalman Filter. GNSS가 제한된 환경에서 UAV 군집의 위치 오차 누적을 완화하고 정확도를 유지하는 핵심 필터링 기법으로, UWB(Ultra Wideband) 측정값과 LSTM 기반 드리프트 보정 모델을 결합하여 운용된다.

## 개요

GPS 신호가 불충분하거나 단절되는 GNSS 무시환경(denied)에서는 UAV의 위치 추정 오차가 시간이 지날수록 누적되는 문제가 발생한다. EKF는 센서 퓨전(Sensor Fusion) 기법의 하나로, UWB로부터 거리를 측정하고 Drift-Correction LSTM 모델의 보정값을 입력으로 받아 최적의 상태 추정을 수행한다. 본 논문에서는 이러한 EKF를 기반으로 한 UWB/EKF 기반 군집 측위 기법의 성능 한계와 최소 운용조건을 정량적으로 분석하였다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| 필터 종류 | Extended Kalman Filter (비선형 시스템 연장 칼만 필터) |
| 연동 센서 | UWB 거리 측정, Drift-Correction LSTM 보정값 |
| 목표 | GNSS 제한 환경에서의 위치 정확도 유지 및 오차 누적 방지 |
| 적용 대상 | UAV 군집 측위 |

## 활용처

- GPS 이용이 어려운 실내·도시 협소 환경 UAV 운용
- UAV 군집의 협동 자율비행 및 지역 측정
- UWB 기반 실시간 위치 추정 시스템

## 관련 페이지

- [[Swarm Localization]] — EKF가 적용되는 대상 체계
- [[Drift-Correction LSTM]] — EKF가 활용하는 보정 모델
- [[UWB]] — EKF와 함께 센서 퓨전의 다른 당사자

## 출처

- (사용자 재확인 필요) — 원문 발췌 기반 작성이며, 세부 수치 및 공식 검증 필요

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
