---
title: "PILOT: Privileged Imitation Learning for UAV Motion Planning"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, ai-autonomy, imitation-learning, motion-planning, navigation]
sources: [inbox/fetch-2026-08-19-arxiv-pilot-privileged-imitation-learning-for-end-to-end-motion-pl.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# PILOT: 부분 관측 하 UAV 모션 플래닝 특권 모방 학습

## 개요

부분 관측 및 동적 제약 하에서의 자율 내비게이션을 위한 제약 인식 특권 모방 학습 프레임워크.

## 핵심 구성 요소

### 특권 전문가로부터의 증류
- 계산 집약적 최적 제어 전문가에서 학생 정책으로
- 이중 목적 손실 함수를 통한 안전 및 동적 요구사항 정규화

### 시공간 지각 융합 모듈
- TCN(Temporal Convolutional Network) 활용
- 역사적 깊이 이미지 및 주행 거리 통합
- 지속적 맵 메모리 없이 FOV 너머 공간 인식 향상

### 궤적 매개변수화 레이어
- 네트워크 출력을 구조화된 궤적에 매핑
- 연속성, 동적 일관성, 장애물 소프트 페널티 명시적 허용

## 성능

### 시뮬레이션 결과
- 특권 전문가 대비 동등한 성능
- 계산 오버헤드 80% 이상 감소

### 실제 배포
- 실내 및 실외 제로샷 배포 성공
- 교차 도메인 일반화 확인

## 관련 개념

- [[e2e-fly-end-to-end-quadrotor]] — 종단간 쿼드로터 자율
- [[agile-quadrotor-learning]] — 민첩한 쿼드로터 학습
- [[skyjepa-world-models]] — JEPA 세계 모델

## 참고

Qingrui Zhang et al., arXiv:2608.14082 (2026)
