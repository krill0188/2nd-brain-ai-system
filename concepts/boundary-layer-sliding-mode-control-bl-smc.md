---
title: "boundary-layer sliding-mode control (BL-SMC)"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [control-theory, sliding-mode-control, quadrotor, robust-control, actuator-modeling]
sources: []
confidence: medium
contradictions: []
domain: flight-control
---

# boundary-layer sliding-mode control (BL-SMC)

Boundary-layer sliding-mode control (BL-SMC) is a variant of sliding-mode control that introduces a boundary layer around the sliding surface to reduce chattering—a high-frequency oscillatory behavior inherent in classical sliding-mode controllers. In quadrotor flight control, BL-SMC is employed to achieve robust tracking under nonlinear plant dynamics, including rotor gyroscopic coupling, motor lag, and actuator saturation.

## 개요

일반적인 쿼드롯터 컨트롤러 비교 연구에서 BL-SMC는 고전적인 슬라이딩 모드 제어(SMC)의 단점인 채터링(chattering)을 완화하면서도 강력한 강인성을 제공하는 방식으로 설계된 슬라이딩 모드 제어의 변형입니다. 최근 재현성 있는 시뮬레이션 연구에 따르면, 매칭된 12가지 후보 튜닝 프로토콜 하에서 BL-SMC는 고정 베이스라인 설정 하에서는 최하위 등급이었으나, 튜닝이 최적화됨에 따라 평균 RMSE 지표에서 1위로 도약하는 순위 변동이 확인되었습니다. 이 순위는 신선한 50개 실재화(fresh realizations)에서도 재현되었으며, 48개 후보 예산에서도 순위가 변하지 않았습니다. 이는 BL-SMC가 적절히 튜닝될 경우 쿼드롯터의 트래킹 성능에서 최적의 대안이 될 수 있음을 시사합니다.

## 스펙

| 파라미터 | 설명 |
|---|---|
| 제어 방식 | 슬라이딩 모드 제어(SMC) 기반, 경계층(boundary-layer) 적용 |
| 주요 특징 | 채터링(chattering) 저감, 강력한 강인성 |
| 적용 가능성 | 회전자 지로스코픽 커플링, 모터 랙(motor lag), 액추에이터 포화(nonlinear plant 포함)하에서 효과적 |

## 활용처

- 쿼드롯터의 고강인 트래킹 제어가 필요한 비행 임무
- actuator modeling과 fallback policy가 중요한 시뮬레이션 기반 컨트롤러 비교 연구
- MPC 및 LQR 기반 컨트롤러 대비 다양한 튜닝 조건 하에서의 성능 평가

## 관련 페이지

- [[sliding-mode-control]] — 슬라이딩 모드 제어의 기본 개념과 변형에 대한 문서
- [[quadrotor-controller-comparison]] — 컨트롤러 비교 연구 전반에 관한 문서

## 출처

- (사용자 재확인 필요) — 위 내용은 arXiv 사전 인쇄 논문(Dao et al., 2026) 원문 발췌 기반이며, 그래프 관계(tuning protocol --[IMPACTS]--> BL-SMC) 외에는 검증되지 않은 자동 추출 정보입니다.
