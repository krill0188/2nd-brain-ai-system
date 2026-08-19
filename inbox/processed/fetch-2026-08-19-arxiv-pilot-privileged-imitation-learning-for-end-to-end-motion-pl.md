---
title: "PILOT: Privileged Imitation Learning for End-to-End Motion Planning of Autonomous UAVs under Partial Observability"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2608.14082v1
authors: "Qingrui Zhang, Feng Xue, Xiang Zhou, Chenghao Yu"
published: "2026-08-14"
tags: [drone, ai-autonomy, paper, arxiv]
---

# PILOT: Privileged Imitation Learning for End-to-End Motion Planning of Autonomous UAVs under Partial Observability

**Authors**: Qingrui Zhang, Feng Xue, Xiang Zhou, Chenghao Yu
**Published**: 2026-08-14
**arXiv**: http://arxiv.org/abs/2608.14082v1

## Abstract

Autonomous navigation in cluttered environments is hampered by partial observability and dynamic constraints. This paper presents PILOT, a constraint-aware privileged imitation learning framework for vision-based end-to-end UAV motion planning under partial observability. The framework distills planning strategies from a computationally intensive optimal control expert into a student policy regularized toward safety and dynamic requirements via a dual-objective loss function. To mitigate partial observability, a spatiotemporal perception fusion module using a Temporal Convolutional Network (TCN) is developed to integrate historical depth images and odometry. This module infers task-relevant latent context from historical observations, enhancing spatial awareness beyond the instantaneous FOV without maintaining persistent map memory. A trajectory parameterization layer mapping network outputs to a structured trajectory, while enabling explicit continuity, dynamic-consistency, and obstacle soft penalties during training, encouraging constraint satisfaction for unseen observations without formal guarantees. Simulations on quadrotor and fixed-wing aircraft demonstrate that PILOT achieves performance comparable to the privileged expert while reducing computational overhead by over 80\%. Successful indoor and outdoor zero-shot deployment confirms the practical feasibility and cross-domain generalization of the planner.
