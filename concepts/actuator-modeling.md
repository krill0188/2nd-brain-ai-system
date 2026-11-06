---
title: "Actuator modeling"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [mpc, actuator-modeling, quadrotor-controller, tuning, reference-preview]
sources: []
confidence: medium
contested: false
contradictions: []
domain: navigation-gnss-denied
---

# Actuator modeling

Actuator modeling is a control-theoretic approach that represents the dynamic behavior of physical actuators—including rotor gyroscopic coupling, motor lag, and saturation effects—to improve quadrotor controller performance evaluation and design. It enables more accurate simulation of real-world actuator dynamics during controller comparison and tuning.

## 개요

Quadrotor controller comparisons typically report only single tracking error metrics, yet resulting rankings are influenced by multiple factors beyond control law design. These include tuning effort, reference information, actuator prediction, optimizer fallback mechanisms, and command timing. Actuator modeling specifically addresses the dynamic representation of physical actuator constraints such as rotor gyroscopic coupling, motor lag, and saturation effects. This modeling approach was implemented in a reproducible simulation study that evaluated multiple controller types—cascade PID, hover LQR, boundary-layer sliding-mode control (BL-SMC), linear MPC with LQR fallback (LMPC-F), a preview-enabled LMPC-F, and a geometric $SO(3)$ controller—on a common nonlinear plant model.

The study conducted a primary evaluation involving 556 episodes at 50 Hz with twelve candidate tunings, 400 paired evaluation episodes, and a 48-cell MPC factorial analysis. A subsequent confirmation study repeated evaluations across 1462 episodes on five fresh realizations with varying tuning budgets of 12, 24, and 48 candidates. Results demonstrated that a matched twelve-candidate tuning protocol altered the mean-RMSE ordering, moving boundary-layer sliding-mode control (BL-SMC) from last to first position, with this new ordering recurring on fresh realizations. Reference preview functionality substantially reduced MPC tracking error and, on figure-eight tasks, eliminated fallback activity entirely.

## 활용처

- Controller comparison and ranking in quadrotor simulation studies
- MPC controller design and tuning optimization
- Evaluation of fallback policy effectiveness under actuator constraints
- Realistic simulation of physical actuator dynamics for robust controller design

## 관련 페이지

- [[MPC]] — Uses Actuator modeling
- [[SLIDING_MODE_CONTROL]] — Compared with Actuator modeling in controller study

## 출처

- (사용자 재확인 필요)

## 참고

[[mpc]] [[actuator-prediction]]
