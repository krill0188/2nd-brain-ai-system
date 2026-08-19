---
title: "Time-Optimal Planning for Quadrotor Waypoint Flight"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, flight-control, path-planning, optimization]
sources: [inbox/fetch-2026-08-19-arxiv-time-optimal-planning-for-quadrotor-waypoint-flight.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# 쿼드로터 웨이포인트 비행 시간 최적 계획

## 개요

쿼드로터의 민첩성을 최대한 활용한 시간 최적 궤적 계획. 검사, 배송, 구조, 드론 레이싱 등의 응용에 필수적.

## 문제 정의

### 기존 접근법의 한계
- **다항식 궤적**: 고유한 평활성으로 인해 전체 액추에이터 잠재력 활용 불가
- **수치 최적화**: 사전 시간 할당 필요, 진정한 시간 최적 궤적 생성 불가

## 제안 솔루션

### 궤적 진행 공식화
- 시간 할당과 궤적 자체의 동시 최적화 가능
- 진정한 시간 최적 궤적 생성

### 검증
- 대형 모션 캡처 시스템에서의 실제 비행 검증
- 전문 드론 파일럿 대비 우수한 성능 입증

## 관련 개념

- [[mission-planning]] — 미션 계획
- [[agile-quadrotor-learning]] — 민첩한 쿼드로터 비행 학습
- [[e2e-fly-end-to-end-quadrotor]] — 종단간 쿼드로터 자율 시스템

## 참고

Philipp Foehn, Angel Romero, Davide Scaramuzza, arXiv:2108.04537 (2021)
