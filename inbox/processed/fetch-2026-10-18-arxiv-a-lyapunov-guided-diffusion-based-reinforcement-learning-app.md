---
title: "A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach for UAV-Assisted Vehicular Networks with Delayed CSI Feedback"
created: 2026-10-18
captured: 2026-10-18
type: paper
domain: hardware
source: http://arxiv.org/abs/2507.20524v1
authors: "Zhang Liu, Lianfen Huang, Zhibin Gao, Xianbin Wang, Dusit Niyato,  Xuemin,  Shen"
published: "2025-07-28"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/a-lyapunov-guided-diffusion-based-reinforcement-learning-app.html
attachment_type: html
attachment_sha256: cb184bad8d41532969b20b2d420bbcfdd316e52492b322df13d5aa2b2eb2a7ef
---

# A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach for UAV-Assisted Vehicular Networks with Delayed CSI Feedback

**Authors**: Zhang Liu, Lianfen Huang, Zhibin Gao, Xianbin Wang, Dusit Niyato,  Xuemin,  Shen
**Published**: 2025-07-28
**arXiv**: http://arxiv.org/abs/2507.20524v1

## Abstract

Low altitude uncrewed aerial vehicles (UAVs) are expected to facilitate the development of aerial-ground integrated intelligent transportation systems and unlocking the potential of the emerging low-altitude economy. However, several critical challenges persist, including the dynamic optimization of network resources and UAV trajectories, limited UAV endurance, and imperfect channel state information (CSI). In this paper, we offer new insights into low-altitude economy networking by exploring intelligent UAV-assisted vehicle-to-everything communication strategies aligned with UAV energy efficiency. Particularly, we formulate an optimization problem of joint channel allocation, power control, and flight altitude adjustment in UAV-assisted vehicular networks. Taking CSI feedback delay into account, our objective is to maximize the vehicle-to-UAV communication sum rate while satisfying the UAV's long-term energy constraint. To this end, we first leverage Lyapunov optimization to decompose the original long-term problem into a series of per-slot deterministic subproblems. We then propose a diffusion-based deep deterministic policy gradient (D3PG) algorithm, which innovatively integrates diffusion models to determine optimal channel allocation, power control, and flight altitude adjustment decisions. Through extensive simulations using real-world vehicle mobility traces, we demonstrate the superior performance of the proposed D3PG algorithm compared to existing benchmark solutions.
