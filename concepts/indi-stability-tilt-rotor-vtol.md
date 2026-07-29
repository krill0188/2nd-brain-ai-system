---
title: "INDI Pitch-Rate Controller Stability Analysis for Tilt-Rotor VTOL UAV"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, flight-control, indi, tilt-rotor, vtol, stability]
sources: [inbox/fetch-2026-07-30-arxiv-linear-stability-analysis-of-an-indi-pitch-rate-controller-u.md]
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# INDI Pitch-Rate Controller Stability Analysis for Tilt-Rotor VTOL UAV

틸트로터 수직 이착륙(VTOL) UAV를 위한 증분 비선형 동적 역전(INDI) 피치 레이트 컨트롤러의 모델 불일치 하에서의 선형 안정성 분석. Routh-Hurwitz 기준을 통한 매개변수 명시적 안정성 특성화.

## INDI의 장점

- **완전한 공기역학 모델에 대한 의존성 감소**
- **강력한 외란 제거 능력 유지**

## 연구 범위

기존 캐스케이드 INDI 컨트롤러의 피치 레이트/엘리베이터 서브채널 격리 분석:
- 선형 안정성 특성화
- 매개변수 명시적 안정성 영역 도출

## 안정성 분석 방법

### 1. 전달 함수 도출
- 5차 전달 함수 (컨트롤러-추정기-액추에이터-플랜트 상호연결)
- Routh-Hurwitz 기준 적용

### 2. 매개변수 스윕
- 3개 매개변수 조합에 대한 해석 가능한 안정성 영역 생성

## 주요 발견

| 불일치 유형 | 안정성 영향 |
|-------------|-------------|
| 액추에이터 지연 | 비교적 양호 (정격 이득에서) |
| 관성 불일치 | 비교적 양호 (정격 이득에서) |
| 제어 효과 불일치 | **가장 위험한 비안정화 요인** |
| 부호 오류 | 치명적 (할당에서) |

## 튜닝 절차 제안

### 1. 견고성 중심 설계
- 최소 이득 여유 및 위상 여유의 가중 최악 조합 최대화

### 2. 성능 중심 설계
- 여유 제약 조건 하에서 최악 케이스 폐쇄 루프 대역폭 최대화

## 시사점

- 보수적 운용 조건을 위한 구체적인 튜닝 권장사항
- 공격적 운용 조건을 위한 구체적인 튜닝 권장사항

## 관련 페이지

- [[px4-flight-modes]] — PX4 비행 모드 및 제어 파라미터
- [[px4-architecture-deep]] — PX4 아키텍처 및 제어 시스템
- [[drone-safety-failsafe]] — 드론 안전 및 페일세이프 시스템
