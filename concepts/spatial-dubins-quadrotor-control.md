---
title: "Spatial Dubins Airplane-Based Reference Smoothing for Quadrotor Control"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, flight-control, path-planning, dubins, quadrotor]
sources: [inbox/fetch-2026-07-30-arxiv-high-level-spatial-dubins-airplane-based-reference-smoothing.md]
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# Spatial Dubins Airplane-Based Reference Smoothing for Quadrotor Control

쿼드로터 제어를 위한 고수준 공간적 Dubins 비행기 기반 참조 스무딩과 저수준 기하학적 추적의 결합. 경로 제약 조건 하에서 참조 추적을 위한 방법론.

## 시스템 아키텍처

### 고수준: 참조 스무딩
- **Dubins 비행기 모델** 활용
- 차원 축소 및 계산 복잡성 감소
- 구조적 분리, 공간 모델링
- 소형 선형 프로그램 공식화

### 저수준: 참조 추적
- **기하학적 추적 컨트롤러** 활용
- 완전한 쿼드로터 모델 기반

## 운용 모드

| 모드 | 설명 |
|------|------|
| 오프라인 | 고수준 계획 단계를 한 번 수행 |
| 온라인 | 제한된 공간 예측 수평에서 재귀적으로 수행 |

## 응용 시나리오

- 장애물 외곽을 따라 참조 추적
- 경로 기반 측방 제약 조건 존재 시
- 복잡한 환경에서의 자유 비행

## 기술적 장점

- 계산 효율성: Dubins 모델을 통한 차원 축소
- 유연성: 오프라인/온라인 모드 모두 지원
- 정확성: 완전한 쿼드로터 동역학을 반영한 저수준 추적

## 관련 페이지

- [[mission-planning]] — 미션 계획 및 경로 생성
- [[px4-flight-modes]] — PX4 비행 모드 및 제어
- [[drone-simulation]] — 드론 시뮬레이션 및 검증
