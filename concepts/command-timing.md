---
title: "Command timing"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [controller-comparison, tuning, mpc, pid, sliding-mode-control]
sources: []
confidence: medium
contested: false
contradictions: []
domain: navigation-gnss-denied
---

# Command timing

Quadrotor controller comparisons commonly report a single tracking error, although the resulting ranking also depends on tuning effort, reference information, actuator prediction, optimizer fallback, and **command timing**. This concept quantifies how the timing of command inputs affects controller performance, particularly in the context of Model Predictive Control (MPC) variants and other flight control strategies. The study demonstrates that command timing significantly influences mean-RMSE ordering and tracking error outcomes across different controller types on a common nonlinear plant model incorporating rotor gyroscopic coupling, motor lag, and saturation effects.
