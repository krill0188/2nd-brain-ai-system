---
title: "Efficient Domain-Adaptive Policy Learning via Kernel Representation with Application to Quadrotor Control under Non-Stationary Disturbances"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2606.13842v2
authors: "Hongyu Zhou, Mingtian Tan, Vasileios Tzoumas"
published: "2026-06-11"
tags: [drone, flight-control, paper, arxiv]
---

# Efficient Domain-Adaptive Policy Learning via Kernel Representation with Application to Quadrotor Control under Non-Stationary Disturbances

**Authors**: Hongyu Zhou, Mingtian Tan, Vasileios Tzoumas
**Published**: 2026-06-11
**arXiv**: http://arxiv.org/abs/2606.13842v2

## Abstract

We present an algorithm for efficient domain-adaptive policy learning via kernel representations. Learning domain-adaptive policies is challenging since it requires an environment representation that is both sufficiently expressive to model complex sim-to-real gaps during offline training, and computationally efficient enough to support rapid online adaptation during deployment. For instance, a quadrotor may encounter time-varying, non-stationary disturbances, such as sudden gusts of wind, payload shifts, or transitions between distinct flight regimes with and without ground effects. To address these challenges, we model unknown disturbances using a differentiable kernel approximation based on random Fourier features. During the offline training phase, we randomly sample kernel coefficients and bandwidth parameters to generate a rich diversity of disturbance profiles. We then optimize the control policy via differentiable simulation with analytical gradients, a process that takes only 50 seconds of training time on an RTX 4090 GPU. During hardware deployment, the policy adapts to non-stationary environments in real time by updating both the kernel coefficients and bandwidth through online least-squares estimation. We evaluate our method on quadrotor trajectory tracking tasks across high-fidelity numerical simulations and hardware experiments using Crazyflie, subjected to various disturbances, including complex aerodynamic effects, wind, ground effects, and payload fluctuations.
