---
title: "Joint Resource Management for Energy-efficient UAV-assisted SWIPT-MEC: A Deep Reinforcement Learning Approach"
created: 2026-10-19
captured: 2026-10-19
type: paper
domain: hardware
source: http://arxiv.org/abs/2505.03230v2
authors: "Yue Chen, Hui Kang, Jiahui Li, Geng Sun, Boxiong Wang, Jiacheng Wang, Cong Liang, Shuang Liang, Dusit Niyato"
published: "2025-05-06"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/joint-resource-management-for-energy-efficient-uav-assisted-.html
attachment_type: html
attachment_sha256: e2fa3db03d1cde0507f51addb690d156ea63d7b81785c5d5b19623722704f74d
---

# Joint Resource Management for Energy-efficient UAV-assisted SWIPT-MEC: A Deep Reinforcement Learning Approach

**Authors**: Yue Chen, Hui Kang, Jiahui Li, Geng Sun, Boxiong Wang, Jiacheng Wang, Cong Liang, Shuang Liang, Dusit Niyato
**Published**: 2025-05-06
**arXiv**: http://arxiv.org/abs/2505.03230v2

## Abstract

The integration of simultaneous wireless information and power transfer (SWIPT) technology in 6G Internet of Things (IoT) networks faces significant challenges in remote areas and disaster scenarios where ground infrastructure is unavailable. This paper proposes a novel unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) system enhanced by directional antennas to provide both computational resources and energy support for ground IoT terminals. However, such systems require multiple trade-off policies to balance UAV energy consumption, terminal battery levels, and computational resource allocation under various constraints, including limited UAV battery capacity, non-linear energy harvesting characteristics, and dynamic task arrivals. To address these challenges comprehensively, we formulate a bi-objective optimization problem that simultaneously considers system energy efficiency and terminal battery sustainability. We then reformulate this non-convex problem with a hybrid solution space as a Markov decision process (MDP) and propose an improved soft actor-critic (SAC) algorithm with an action simplification mechanism to enhance its convergence and generalization capabilities. Simulation results have demonstrated that our proposed approach outperforms various baselines in different scenarios, achieving efficient energy management while maintaining high computational performance. Furthermore, our method shows strong generalization ability across different scenarios, particularly in complex environments, validating the effectiveness of our designed boundary penalty and charging reward mechanisms.
