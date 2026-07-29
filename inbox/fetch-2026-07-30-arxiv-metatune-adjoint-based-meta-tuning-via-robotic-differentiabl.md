---
title: "MetaTune: Adjoint-based Meta-tuning via Robotic Differentiable Dynamics"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2603.27313v2
authors: "Xiexin Peng, Bingheng Wang, Tao Zhang, Que Dong, Ying Zheng"
published: "2026-03-28"
tags: [drone, flight-control, paper, arxiv]
---

# MetaTune: Adjoint-based Meta-tuning via Robotic Differentiable Dynamics

**Authors**: Xiexin Peng, Bingheng Wang, Tao Zhang, Que Dong, Ying Zheng
**Published**: 2026-03-28
**arXiv**: http://arxiv.org/abs/2603.27313v2

## Abstract

Disturbance observer-based control has shown promise in robustifying robotic systems against uncertainties. However, tuning such systems remains challenging due to the strong coupling between controller gains and observer parameters. In this work, we propose MetaTune, a unified framework for joint auto-tuning of feedback controllers and disturbance observers through differentiable closed-loop meta-learning. MetaTune integrates a portable neural policy with physics-informed gradients derived from differentiable system dynamics, enabling adaptive gains across tasks and operating conditions. We develop an adjoint method that efficiently computes the meta-gradients with respect to adaptive gains backward in time to directly minimize the cost-to-go. Compared to existing forward methods, our approach reduces the computational complexity to be linear in the data horizon. On quadrotor control tasks, MetaTune achieves competitive or improved tracking performance while reducing gradient computation time by more than 50\%. In PX4-Gazebo hardware-in-the-loop simulation, the learned policy transfers zero-shot and reduces tracking RMSE by about 15--20\% in aggressive flight and up to 40\% under strong disturbances.
