---
title: "CALOS: Control-Affine Lyapunov On-manifold Safety Layer for Safe Deep Reinforcement Learning for Quadrotors"
created: 2026-09-18
updated: 2026-09-18
type: paper
item_type: preprint
authors: "Cesareo, Fabrizio; Mengozzi, Sebastiano; Mimmo, Nicola; Acquaviva, Andrea"
year: "2026"
doi: "10.48550/arXiv.2609.17758"
url: "http://arxiv.org/abs/2609.17758v1"
zotero_key: 9TP5FH69
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/calos-control-affine-lyapunov-on-manifold-safety-layer-for-safe-deep-reinforceme.pdf
attachment_sha256: d0d1cc28aff9eb43e4b5e694c7f933a11faf46581e97b5e01e48d89a4d8d834d
sha256: 95313f0e86942919
---

# CALOS: Control-Affine Lyapunov On-manifold Safety Layer for Safe Deep Reinforcement Learning for Quadrotors

**Authors**: Cesareo, Fabrizio; Mengozzi, Sebastiano; Mimmo, Nicola; Acquaviva, Andrea  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2609.17758  
**URL**: http://arxiv.org/abs/2609.17758v1

## Abstract

Deep Reinforcement Learning has demonstrated remarkable capability in quadrotor control, yet learned policies offer no guarantee of respecting safety constraints during training or deployment. We present CALOS (Control-Affine Lyapunov On-manifold Safety), a runtime safety layer that enforces attitude constraints on a quadrotor without modifying the underlying learning algorithm. CALOS formulates four tilt-angle inequalities and a Lyapunov descent condition as a single quadratic program whose solution is the minimum-norm correction to the nominal torque output of the policy. The quadratic program is solved exactly via active-set enumeration over the three-dimensional torque space, with a computational cost low enough to enforce constraints in real time across thousands of parallel simulation environments, as required by modern massively parallel Deep Reinforcement Learning training. Evaluated on trajectory-tracking tasks in NVIDIA Isaac Lab, CALOS reduces lateral tracking error by 55-60% relative to an unconstrained Proximal Policy Optimization baseline while achieving zero attitude-constraint violations on the training trajectory. By restricting exploration to safe regions of the state space, the safety layer also accelerates training convergence and improves data efficiency without producing suboptimal policies.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
