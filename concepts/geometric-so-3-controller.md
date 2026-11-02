---
title: "geometric $SO(3)$ controller"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [flight-control, nonlinear-control, so3-control, quadrotor]
sources: []
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# geometric $SO(3)$ controller

geometric $SO(3)$ controller는 비선형 플랜트에서 로터 자이로스코픽 커플링, 모터 래깅, 포화 상태를 고려한 큐드로터 제어 전략으로, 텐서플로우 기반 시뮬레이션 연구에서 PID, LQR, 슬라이딩 모드 제어, MPC 대안들과 비교되었다. 이 컨트롤러는 보드리즌 기준 12개 후보 튜닝 프로토콜 적용 후 평균 RMSE 순위에서 슬라이딩 모드 제어(BL-SMC)를 앞질러 첫 번째로 도약하였으며, 신선한 50개 실현에서도 동일한 순위가 재현되었다. 48개 후보 예산 적용 시 순위가 변하지 않았음이 확인되었다.

## 개요

본 연구(2026년 아카이브)는 큐드로터 컨트롤러 비교 시 단일 추적 오차 외에 튜닝 노력, 레퍼런스 정보, 액추이터 예측, 옵티마이저 폴백, 명령 타이밍 등의 요인이 순위에 미치는 영향을 정량화하였다. 연구팀은 캐스케이드 PID, 호버 LQR, 경계층 슬라이딩 모드 제어(BL-SMC), LQR 폴백이 있는 선형 MPC(LMPC-F), 레퍼런스 프리뷰가 포함된 LMPC-F, 그리고 기하학적 $SO(3)$ 컨트롤러를 동일한 비선형 플랜트 위에서 비교했다. 이 플랜트 모델은 로터 자이로스코픽 커플링, 모터 래깅, 입력을 포화시키는 제약 조건을 포함한다. 연구는 556개의 에피소드(50Hz)로 구성된 주요 연구와, 튜닝 예산 12, 24, 48개로 평가된 1462개의 에피소드를 반복한 확인 연구 두 단계로 진행되었다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| 컨트롤러 유형 | 기하학적 $SO(3)$ 기반 비선형 제어 |
| 비교 대상 | 캐스케이드 PID, 호버 LQR, BL-SMC, LMPC-F, 프리뷰 LMPC-F |
| 플랜트 특이사항 | 로터 자이로스코픽 커플링, 모터 래깅, 입력 포화 |
| 평가 지표 | 평균 RMSE, 폴백 활동 여부 |
| 튜닝 예산 영향 | 12·24·48 후보 모두에서 BL-SMC 제치고 첫 번째 순위 유지 |

## 활용처

- 큐드로터의 고정밀 추적 제어가 필요한 시나리오에서 기존 PID/LQR 대비 우수함을 보임
- 레퍼런스 프리뷰와 결합할 경우 MPC의 추적 오차 감소 및 폴백 활동 억제 효과 기대
- 자이로스코픽 효과와 모터 래깅이 중요한 비선형 플랜트 환경에서 적용 가능

## 관련 페이지

- [[tuning protocol]] — IMPACTS: geometric $SO(3)$ controller
- [[boundary-layer sliding-mode control (BL-SMC)]] — 이동된 순위 경쟁자

## 출처

- (사용자 재확인 필요)

## 참고

[[quadrotor]] [[backflip-controller]]
