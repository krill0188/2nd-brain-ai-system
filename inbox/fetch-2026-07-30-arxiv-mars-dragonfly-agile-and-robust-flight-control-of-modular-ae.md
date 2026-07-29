---
title: "MARS-Dragonfly: Agile and Robust Flight Control of Modular Aerial Robot Systems"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2604.05499v1
authors: "Rui Huang, Zhiqian Cai, Siyu Tang, Pengxuan Wei, Lidong Li, Xin Chen, Wenhan Cao, Zhenyu Zhang, Lin Zhao"
published: "2026-04-07"
tags: [drone, flight-control, paper, arxiv]
---

# MARS-Dragonfly: Agile and Robust Flight Control of Modular Aerial Robot Systems

**Authors**: Rui Huang, Zhiqian Cai, Siyu Tang, Pengxuan Wei, Lidong Li, Xin Chen, Wenhan Cao, Zhenyu Zhang, Lin Zhao
**Published**: 2026-04-07
**arXiv**: http://arxiv.org/abs/2604.05499v1

## Abstract

Modular Aerial Robot Systems (MARS) comprise multiple drone units with reconfigurable connected formations, providing high adaptability to diverse mission scenarios, fault conditions, and payload capacities. However, existing control algorithms for MARS rely on simplified quasi-static models and rule-based allocation, which generate discontinuous and unbounded motor commands. This leads to attitude error accumulation as the number of drone units scales, ultimately causing severe oscillations during docking, separation, and waypoint tracking. To address these limitations, we first design a compact mechanical system that enables passive docking, detection-free passive locking, and magnetic-assisted separation using a single micro servo. Second, we introduce a force-torque-equivalent and polytope-constraint virtual quadrotor that explicitly models feasible wrench sets. Together, these abstractions capture the full MARS dynamics and enable existing quadrotor controllers to be applied across different configurations. We further optimize the yaw angle that maximizes control authority to enhance agility. Third, building on this abstraction, we design a two-stage predictive-allocation pipeline: a constrained predictive tracker computes virtual inputs while respecting force/torque bounds, and a dynamic allocator maps these inputs to individual modules with balanced objectives to produce smooth, trackable motor commands. Simulations across over 10 configurations and real-world experiments demonstrate stable docking, locking, and separation, as well as effective control performance. To our knowledge, this is the first real-world demonstration of MARS achieving agile flight and transport with 40 deg peak pitch while maintaining an average position error of 0.0896 m. The video is available at: https://youtu.be/yqjccrIpz5o
