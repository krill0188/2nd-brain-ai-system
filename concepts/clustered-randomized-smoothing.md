---
title: Clustered Randomized Smoothing for Stochastic Prediction
created: 2026-08-13
updated: 2026-08-13
type: concept
domain: flight-control
tags: [drone, flight-control, ai, robustness, safety, paper]
sources: [inbox/fetch-2026-08-13-arxiv-clustered-randomized-smoothing-for-stochastic-prediction-fun.md]
confidence: high
contested: false
contradictions: []
---

# Clustered Randomized Smoothing for Stochastic Prediction Functions

arXiv 2608.12037 (2026-08-12). 다중 모드 예측의 강건성을 위한 클러스터 기반 랜덤 스무딩 프레임워크.

## 저자

Eduardo Figueiredo, Frederik Mathiesen, Julian Schumann, Jens Kober, Arkady Zgonnikov, Luca Laurenti

## 핵심 기여

- **클러스터 기반 α-스무딩**: 노이즈 샘플을 클러스터링 후 각 클러스터 내에서 로컬 스무딩 적용
- **혼합 분포 결합**: 여러 모드의 예측을 혼합 분포로 통합
- **안전 임계**: 스무된 예측이 컴팩트 영역 내에 있을 확률의 하한 도출

## 드론 응용 결과

- **쿼드로터 제어**: 목표까지의 서로 다른 경로(모드)에 해당
- **충돌률 감소**: 기존 랜덤 스무딩 대비 **81% 충돌률 감소**

## 의의

안전 필수 도메인에서 확률적 예측의 강건성 향상.

## 관련 페이지

- [[px4-control-tuning]] — PX4 제어 튜닝
- [[rl-quadrotor-tunable-control]] — RL 기반 쿼드로터 제어
- [[ai-knowledge-workflow]] — AI 지식 워크플로
