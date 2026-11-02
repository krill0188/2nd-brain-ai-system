---
title: "linear MPC with LQR fallback (LMPC-F)"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [mpc, lqr, controller-comparison, quadrotor, tuning, fallback-policy]
sources: []
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# linear MPC with LQR fallback (LMPC-F)

Linear MPC with LQR fallback is a quadrotor flight control architecture that combines linear model predictive control with an LQR (Linear Quadratic Regulator) fallback policy to ensure stable tracking under varying conditions. The controller uses a predictive optimization horizon for nominal tracking and switches to the LQR controller when the MPC optimizer fails or encounters constraints that cannot be satisfied, providing robustness against modeling uncertainties and computational limitations.

## 개요

LMPC-F는 쿼드롯로 비전 제어에서 발생할 수 있는 최적화 실패 상황(예: 제약 조건 불만족, 계산 시간 초과 등)을 처리하기 위해 MPC와 LQR을 조합한 하이브리드 제어 전략입니다. 기본적으로 선형 MPC를 통해 레퍼런스 트래킹을 수행하며, MPC 최적화기가 실패할 경우 LQR 폴백 정책으로 전환되어 비행의 안정성을 유지합니다. 논문 연구에 따르면 레퍼런스 프리뷰(preview) 기능을 결합하면 MPC의 트래킹 오차를 크게 감소시킬 수 있으며, figure-eight 과제에서는 폴백 활동이 발생하지 않을 정도로 성능이 향상된 것으로 나타났습니다.

## 스펙

| 파라미터 | 내용 |
|---|---|
| 제어 형식 | 선형 MPC + LQR 폴백 |
| 폴백 트리거 | MPC 최적화 실패 또는 제약 조건 불만족 시 |
| 안정성 보장 | LQR 폴백을 통한 안정적인 비상 제어 |
| 연구 적용 | cascade PID, hover LQR, BL-SMC 등와의 비교 실험 |

## 활용처

- 쿼드롯로 trajectorary tracking 수행 시 MPC 최적화 실패 리스크가 있는 환경
- 계산 자원이 제한된 플랫폼에서 안정성 확보가 필요한 경우
- 다양한 튜닝 후보(12, 24, 48 후보 등) 중에서 최적 성능을 찾기 위한 파라미터 탐색 실험

## 관련 페이지

- [[linear MPC]] — MPC의 기본 개념 및 최적화 구조
- [[LQR fallback policy]] — MPC 실패 시 활성화되는 폴백 정책
- [[command timing]] — 제어 명령 시점이 LMPC-F 성능에 미치는 영향
- [[tuning protocol]] — LMPC-F 성능을 결정하는 튜닝 프로토콜

## 출처

- (사용자 재확인 필요) "How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study", Dao et al., 2026, arXiv:2610.35165

---

## 참고

[[mpc]] [[quadrotor]]
