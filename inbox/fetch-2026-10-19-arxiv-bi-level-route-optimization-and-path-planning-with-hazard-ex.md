---
title: "Bi-Level Route Optimization and Path Planning with Hazard Exploration"
created: 2026-10-19
captured: 2026-10-19
type: paper
domain: hardware
source: http://arxiv.org/abs/2503.24044v2
authors: "Jimin Choi, Grant Stagg, Cameron K. Peterson, Max Z. Li"
published: "2025-03-31"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/bi-level-route-optimization-and-path-planning-with-hazard-ex.html
attachment_type: html
attachment_sha256: 9586ad27cfa1b7e475da54237e10645aa72016f824f5fb1488cf708aac8bb3c9
---

# Bi-Level Route Optimization and Path Planning with Hazard Exploration

**Authors**: Jimin Choi, Grant Stagg, Cameron K. Peterson, Max Z. Li
**Published**: 2025-03-31
**arXiv**: http://arxiv.org/abs/2503.24044v2

## Abstract

Effective risk monitoring in dynamic environments such as disaster zones requires an adaptive exploration strategy to detect hidden threats. We propose a bi-level unmanned aerial vehicle (UAV) monitoring strategy that efficiently integrates high-level route optimization with low-level path planning for known and unknown hazards. At the high level, we formulate the route optimization as a vehicle routing problem (VRP) to determine the optimal sequence for visiting known hazard locations. To strategically incorporate exploration efficiency, we introduce an edge-based centroidal Voronoi tessellation (CVT), which refines baseline routes using pseudo-nodes and allocates path budgets based on the UAV's battery capacity using a line segment Voronoi diagram. At the low level, path planning maximizes information gain within the allocated path budget by generating kinematically feasible B-spline trajectories. Bayesian inference is applied to dynamically update hazard probabilities, enabling the UAVs to prioritize unexplored regions. Simulation results demonstrate that edge-based CVT improves spatial coverage and route uniformity compared to the node-based method. Additionally, our optimized path planning consistently outperforms baselines in hazard discovery rates across a diverse set of scenarios.
