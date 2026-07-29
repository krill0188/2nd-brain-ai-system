---
title: "Online Reinforcement Learning for Safe Gain Scheduling in Nonlinear Quadrotor Control"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2604.16819v1
authors: "Muhammad Junayed Hasan Zahed, Chieh Tsai, Salim Hariri, Hossein Rastgoftar"
published: "2026-04-18"
tags: [drone, flight-control, paper, arxiv]
---

# Online Reinforcement Learning for Safe Gain Scheduling in Nonlinear Quadrotor Control

**Authors**: Muhammad Junayed Hasan Zahed, Chieh Tsai, Salim Hariri, Hossein Rastgoftar
**Published**: 2026-04-18
**arXiv**: http://arxiv.org/abs/2604.16819v1

## Abstract

This paper presents an online reinforcement-learning framework for safe gain scheduling of a nonlinear quadcopter controller. Rather than learning thrust and torque commands directly, the proposed method selects gain vectors online from a finite library of pre-certified stabilizing controllers, thereby preserving the structure of the underlying snap-based control law. Safety is enforced by restricting the policy to admissible gains that maintain forward invariance of a prescribed safe state set, while dwell-time constraints prevent excessively fast switching. To reduce the action-space dimension, translational gains are shared across spatial axes by exploiting the isotropic structure of the translational dynamics, whereas yaw gains are scheduled independently. A deep Q-network learns to adjust feedback authority according to the current flight condition, using aggressive gains during large transients and milder gains near hover. High-fidelity nonlinear simulations demonstrate accurate trajectory tracking, bounded attitude motion, reduced control effort near convergence, and stable hover regulation under online safe gain scheduling.
