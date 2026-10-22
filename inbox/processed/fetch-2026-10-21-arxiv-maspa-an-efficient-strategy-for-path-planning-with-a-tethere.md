---
title: "MASPA: An efficient strategy for path planning with a tethered marsupial robotics system"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: hardware
source: http://arxiv.org/abs/2408.02141v3
authors: "Jes\u00fas Capit\u00e1n, Jos\u00e9 M. D\u00edaz-B\u00e1\u00f1ez, Miguel A. P\u00e9rez-Cuti\u00f1o, Fabio Rodr\u00edguez, Inmaculada Ventura"
published: "2024-08-04"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/maspa-an-efficient-strategy-for-path-planning-with-a-tethere.html
attachment_type: html
attachment_sha256: 00c0ecc70da2aeebdc69cb6246bc8521f58d0ddea797482370d86ca860dfec14
---

# MASPA: An efficient strategy for path planning with a tethered marsupial robotics system

**Authors**: Jesús Capitán, José M. Díaz-Báñez, Miguel A. Pérez-Cutiño, Fabio Rodríguez, Inmaculada Ventura
**Published**: 2024-08-04
**arXiv**: http://arxiv.org/abs/2408.02141v3

## Abstract

A tethered marsupial robotics system comprises three components: an Unmanned Ground Vehicle (UGV), an Unmanned Aerial Vehicle (UAV), and a tether connecting both robots. Marsupial systems are highly beneficial in industry as they extend the UAV's battery life during flight. This paper introduces a novel strategy for a specific path planning problem in marsupial systems, where each of the three components must avoid collisions with ground and aerial obstacles modeled as 3D cuboids. Given an initial configuration in which the UAV is positioned atop the UGV, the goal is to reach an aerial target with the UAV. We assume that the UGV first moves to a position from which the UAV can take off and fly through a vertical plane to reach an aerial target. We propose an approach that discretizes the space to approximate an optimal solution, minimizing the sum of the lengths of the ground and air paths. First, we assume a taut tether and use a novel algorithm that leverages the convexity of the tether and the geometry of obstacles to efficiently determine the locus of feasible take-off points for the UAV. We then apply this result to scenarios that involve loose tethers. The simulation test results show that our approach can solve complex situations in seconds, outperforming a baseline planning algorithm based on RRT* (Rapidly exploring Random Trees).
