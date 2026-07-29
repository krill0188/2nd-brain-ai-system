---
title: "VisFly-Lab: Unified Differentiable Framework for First-Order Reinforcement Learning of Quadrotor Control"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2603.21123v1
authors: "Fanxing Li, Fangyu Sun, Tianbao Zhang, Shuyu Wu, Dexin Zuo, yufei Yan, Wenxian Yu, Danping Zou"
published: "2026-03-22"
tags: [drone, flight-control, paper, arxiv]
---

# VisFly-Lab: Unified Differentiable Framework for First-Order Reinforcement Learning of Quadrotor Control

**Authors**: Fanxing Li, Fangyu Sun, Tianbao Zhang, Shuyu Wu, Dexin Zuo, yufei Yan, Wenxian Yu, Danping Zou
**Published**: 2026-03-22
**arXiv**: http://arxiv.org/abs/2603.21123v1

## Abstract

First-order reinforcement learning with differentiable simulation is promising for quadrotor control, but practical progress remains fragmented across task-specific settings. To support more systematic development and evaluation, we present a unified differentiable framework for multi-task quadrotor control. The framework is wrapped, extensible, and equipped with deployment-oriented dynamics, providing a common interface across four representative tasks: hovering, tracking, landing, and racing. We also present the suite of first-order learning algorithms, where we identify two practical bottlenecks of standard first-order training: limited state coverage caused by horizon initialization and gradient bias caused by partially non-differentiable rewards. To address these issues, we propose Amended Backpropagation Through Time (ABPT), which combines differentiable rollout optimization, a value-based auxiliary objective, and visited-state initialization to improve training robustness. Experimental results show that ABPT yields the clearest gains in tasks with partially non-differentiable rewards, while remaining competitive in fully differentiable settings. We further provide proof-of-concept real-world deployments showing initial transferability of policies learned in the proposed framework beyond simulation.
