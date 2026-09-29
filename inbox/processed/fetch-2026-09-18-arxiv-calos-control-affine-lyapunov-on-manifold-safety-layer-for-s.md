---
title: "CALOS: Control-Affine Lyapunov On-manifold Safety Layer for Safe Deep Reinforcement Learning for Quadrotors"
created: 2026-09-18
captured: 2026-09-18
type: paper
domain: flight-control
source: http://arxiv.org/abs/2609.17758v1
authors: "Fabrizio Cesareo, Sebastiano Mengozzi, Nicola Mimmo, Andrea Acquaviva"
published: "2026-09-15"
tags: [drone, flight-control, paper, arxiv]
---

# CALOS: Control-Affine Lyapunov On-manifold Safety Layer for Safe Deep Reinforcement Learning for Quadrotors

**Authors**: Fabrizio Cesareo, Sebastiano Mengozzi, Nicola Mimmo, Andrea Acquaviva
**Published**: 2026-09-15
**arXiv**: http://arxiv.org/abs/2609.17758v1

## Abstract

Deep Reinforcement Learning has demonstrated remarkable capability in quadrotor control, yet learned policies offer no guarantee of respecting safety constraints during training or deployment. We present CALOS (Control-Affine Lyapunov On-manifold Safety), a runtime safety layer that enforces attitude constraints on a quadrotor without modifying the underlying learning algorithm. CALOS formulates four tilt-angle inequalities and a Lyapunov descent condition as a single quadratic program whose solution is the minimum-norm correction to the nominal torque output of the policy. The quadratic program is solved exactly via active-set enumeration over the three-dimensional torque space, with a computational cost low enough to enforce constraints in real time across thousands of parallel simulation environments, as required by modern massively parallel Deep Reinforcement Learning training. Evaluated on trajectory-tracking tasks in NVIDIA Isaac Lab, CALOS reduces lateral tracking error by 55-60% relative to an unconstrained Proximal Policy Optimization baseline while achieving zero attitude-constraint violations on the training trajectory. By restricting exploration to safe regions of the state space, the safety layer also accelerates training convergence and improves data efficiency without producing suboptimal policies.
