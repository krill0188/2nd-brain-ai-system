---
title: "PILOT: Privileged Imitation Learning for End-to-End Motion Planning of Autonomous UAVs under Partial Observability"
created: 2026-08-20
updated: 2026-08-20
type: paper
item_type: preprint
authors: "Zhang, Qingrui; Xue, Feng; Zhou, Xiang; Yu, Chenghao"
year: "2026"
doi: "10.48550/arXiv.2608.14082"
url: "http://arxiv.org/abs/2608.14082v1"
zotero_key: MTU4RXDN
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/pilot-privileged-imitation-learning-for-end-to-end-motion-planning-of-autonomous.pdf
attachment_sha256: 716ea406a822e84798c653a012451837a2c5ec359205d39287259a6860c1a8a5
sha256: 5fe7a2b56d0708bd
---

# PILOT: Privileged Imitation Learning for End-to-End Motion Planning of Autonomous UAVs under Partial Observability

**Authors**: Zhang, Qingrui; Xue, Feng; Zhou, Xiang; Yu, Chenghao  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.14082  
**URL**: http://arxiv.org/abs/2608.14082v1

## Abstract

Autonomous navigation in cluttered environments is hampered by partial observability and dynamic constraints. This paper presents PILOT, a constraint-aware privileged imitation learning framework for vision-based end-to-end UAV motion planning under partial observability. The framework distills planning strategies from a computationally intensive optimal control expert into a student policy regularized toward safety and dynamic requirements via a dual-objective loss function. To mitigate partial observability, a spatiotemporal perception fusion module using a Temporal Convolutional Network (TCN) is developed to integrate historical depth images and odometry. This module infers task-relevant latent context from historical observations, enhancing spatial awareness beyond the instantaneous FOV without maintaining persistent map memory. A trajectory parameterization layer mapping network outputs to a structured trajectory, while enabling explicit continuity, dynamic-consistency, and obstacle soft penalties during training, encouraging constraint satisfaction for unseen observations without formal guarantees. Simulations on quadrotor and fixed-wing aircraft demonstrate that PILOT achieves performance comparable to the privileged expert while reducing computational overhead by over 80\%. Successful indoor and outdoor zero-shot deployment confirms the practical feasibility and cross-domain generalization of the planner.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
