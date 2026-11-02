---
title: "Cellular network signals"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [comm-protocol, rf-datalink, cellular-network, uav-navigation, deep-learning]
sources: []
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Cellular network signals

Urban UAV navigation systems leverage cellular network signals as a reliable positioning and communication alternative to GPS, particularly in GPS-denied environments. These signals are utilized to overcome localization errors and dynamic obstacles through advanced deep learning strategies.

## 개요

The study introduces cellular network signals as a core component for developing energy-efficient UAV navigation in urban areas. A multi-objective cost function optimizes uncertainty in motion, trajectory smoothness, distance traveled, and collision avoidance. To enhance signal reliability, a three-dimensional geometry-based channel propagation model (3DGCPM) is applied to reduce inter-cellular interference. Cellular signals serve as the foundation for the hybrid deep learning framework that enables adaptive smoothness control and real-time trajectory planning.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| 신호 원천 | Cellular network signals (LTE/5G 등) |
| 적용 목적 | GPS degradation 극복, 로컬라이제이션 오류 보정, 동적 장애물 회피 |
| 간섭 저감 | 3차원 기하 기반 채널 프로파게이션 모델(3DGCPM)을 이용한 간섭 감소 |
| 최적화 대상 | 모션 불확실성,_trajectory smoothness, 이동 거리, 충돌 회피 |

## 활용처

- Urban UAV navigation in GPS-denied environments
- Real-time trajectory planning with adaptive smoothness control
- Hybrid deep learning-based reliability enhancement for flight operations

## 관련 페이지

- [[Hybrid Deep Learning Framework for Real-Time UAV Navigation with Adaptive Smoothness Control]] — Cellular network signals를 활용하는 하이브리드 딥러닝 네비게이션 시스템
- [[3DGCPM (3D Geometry-based Channel Propagation Model)]] — 간섭 감소 모델

## 출처

- (사용자 재확인 필요) original paper: "Hybrid Deep Learning Framework for Real-Time UAV Navigation with Adaptive Smoothness Control" (2026)
- https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003396172

## 참고

[[ad-hoc-network]] [[ad-hoc-wireless-networks]]
