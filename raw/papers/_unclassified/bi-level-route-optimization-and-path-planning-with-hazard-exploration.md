---
title: "Bi-Level Route Optimization and Path Planning with Hazard Exploration"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Choi, Jimin; Stagg, Grant; Peterson, Cameron K.; Li, Max Z."
year: "2025"
doi: "10.48550/arXiv.2503.24044"
url: "http://arxiv.org/abs/2503.24044v2"
zotero_key: Z9IFGZD4
tags: ["auto:2nd-brain"]
sha256: 481cd6fefe081dc3
---

# Bi-Level Route Optimization and Path Planning with Hazard Exploration

**Authors**: Choi, Jimin; Stagg, Grant; Peterson, Cameron K.; Li, Max Z.  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2503.24044  
**URL**: http://arxiv.org/abs/2503.24044v2

## Abstract

Effective risk monitoring in dynamic environments such as disaster zones requires an adaptive exploration strategy to detect hidden threats. We propose a bi-level unmanned aerial vehicle (UAV) monitoring strategy that efficiently integrates high-level route optimization with low-level path planning for known and unknown hazards. At the high level, we formulate the route optimization as a vehicle routing problem (VRP) to determine the optimal sequence for visiting known hazard locations. To strategically incorporate exploration efficiency, we introduce an edge-based centroidal Voronoi tessellation (CVT), which refines baseline routes using pseudo-nodes and allocates path budgets based on the UAV's battery capacity using a line segment Voronoi diagram. At the low level, path planning maximizes information gain within the allocated path budget by generating kinematically feasible B-spline trajectories. Bayesian inference is applied to dynamically update hazard probabilities, enabling the UAVs to prioritize unexplored regions. Simulation results demonstrate that edge-based CVT improves spatial coverage and route uniformity compared to the node-based method. Additionally, our optimized path planning consistently outperforms baselines in hazard discovery rates across a diverse set of scenarios.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
