---
title: "E2E-Fly: An Integrated Training-to-Deployment System for End-to-End Quadrotor Autonomy"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2604.12916v1
authors: "Fangyu Sun, Fanxing Li, Linzuo Zhang, Yu Hu, Renbiao Jin, Shuyu Wu, Wenxian Yu, Danping Zou"
published: "2026-04-14"
tags: [drone, flight-control, paper, arxiv]
---

# E2E-Fly: An Integrated Training-to-Deployment System for End-to-End Quadrotor Autonomy

**Authors**: Fangyu Sun, Fanxing Li, Linzuo Zhang, Yu Hu, Renbiao Jin, Shuyu Wu, Wenxian Yu, Danping Zou
**Published**: 2026-04-14
**arXiv**: http://arxiv.org/abs/2604.12916v1

## Abstract

Training and transferring learning-based policies for quadrotors from simulation to reality remains challenging due to inefficient visual rendering, physical modeling inaccuracies, unmodeled sensor discrepancies, and the absence of a unified platform integrating differentiable physics learning into end-to-end training. While recent work has demonstrated various end-to-end quadrotor control tasks, few systems provide a systematic, zero-shot transfer pipeline, hindering reproducibility and real-world deployment. To bridge this gap, we introduce E2E-Fly, an integrated framework featuring an agile quadrotor platform coupled with a full-stack training, validation, and deployment workflow. The training framework incorporates a high-performance simulator with support for differentiable physics learning and reinforcement learning, alongside structured reward design tailored to common quadrotor tasks. We further introduce a two-stage validation strategy using sim-to-sim transfer and hardware-in-the-loop testing, and deploy policies onto two physical quadrotor platforms via a dedicated low-level control interface and a comprehensive sim-to-real alignment methodology, encompassing system identification, domain randomization, latency compensation, and noise modeling. To the best of our knowledge, this is the first work to systematically unify differentiable physical learning with training, validation, and real-world deployment for quadrotors. Finally, we demonstrate the effectiveness of our framework for training six end-to-end control tasks and deploy them in the real world.
