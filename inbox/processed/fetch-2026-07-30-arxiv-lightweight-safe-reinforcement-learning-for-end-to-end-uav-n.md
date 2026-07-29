---
title: "Lightweight Safe Reinforcement Learning for End-to-End UAV Navigation"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2607.01794v1
authors: "Shenghui Zhang, YuXuan Gao, Songwei Zhao, Jifeng Hu, Zijing Zhang, Hechang Chen"
published: "2026-07-02"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Lightweight Safe Reinforcement Learning for End-to-End UAV Navigation

**Authors**: Shenghui Zhang, YuXuan Gao, Songwei Zhao, Jifeng Hu, Zijing Zhang, Hechang Chen
**Published**: 2026-07-02
**arXiv**: http://arxiv.org/abs/2607.01794v1

## Abstract

With the rapid development of autonomous aerial systems, Unmanned Aerial Vehicles (UAVs) are increasingly deployed in applications such as inspection, environmental monitoring, and rescue, creating growing demand for reliable autonomous navigation. However, autonomous UAV navigation in dense environments remains challenging under sparse perception and dynamic constraints. Most reinforcement learning (RL) methods lack explicit safety mechanisms, leading to unsafe exploration, unstable training, and risky behaviors, especially during high-speed flight. Even in safe RL approaches, safety is often enforced by projecting policy outputs onto a safe action set, which may introduce instability. Meanwhile, many learning-based methods rely on dense inputs or large networks, increasing computational burden and limiting lightweight onboard deployment. Facing the above challenges, we propose a safety-constrained perception-control integrated framework for UAV navigation. A lightweight network encodes sparse observations into collision-risk-aware features using asymmetric and depthwise separable convolutions. We formulate the task as a constrained Markov decision process within a hierarchical control architecture and solve it using a Lagrangian-based safe PPO algorithm. Curriculum learning further improves training stability. Experiments with varying obstacle densities and flight speeds demonstrate higher success rates, improved safety, and better efficiency than existing reinforcement learning baselines.
