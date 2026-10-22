---
title: "Perception-and-Energy-aware Motion Planning for UAV using Learning-based Model under Heteroscedastic Uncertainty"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: hardware
source: http://arxiv.org/abs/2309.14272v1
authors: "Reiya Takemura, Genya Ishigami"
published: "2023-09-25"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/perception-and-energy-aware-motion-planning-for-uav-using-le.html
attachment_type: html
attachment_sha256: 0fa1344669fe078f2d9a4b187e15ee94af3730715ec71e1b360acc90c6c66240
---

# Perception-and-Energy-aware Motion Planning for UAV using Learning-based Model under Heteroscedastic Uncertainty

**Authors**: Reiya Takemura, Genya Ishigami
**Published**: 2023-09-25
**arXiv**: http://arxiv.org/abs/2309.14272v1

## Abstract

Global navigation satellite systems (GNSS) denied environments/conditions require unmanned aerial vehicles (UAVs) to energy-efficiently and reliably fly. To this end, this study presents perception-and-energy-aware motion planning for UAVs in GNSS-denied environments. The proposed planner solves the trajectory planning problem by optimizing a cost function consisting of two indices: the total energy consumption of a UAV and the perception quality of light detection and ranging (LiDAR) sensor mounted on the UAV. Before online navigation, a high-fidelity simulator acquires a flight dataset to learn energy consumption for the UAV and heteroscedastic uncertainty associated with LiDAR measurements, both as functions of the horizontal velocity of the UAV. The learned models enable the online planner to estimate energy consumption and perception quality, reducing UAV battery usage and localization errors. Simulation experiments in a photorealistic environment confirm that the proposed planner can address the trade-off between energy efficiency and perception quality under heteroscedastic uncertainty. The open-source code is released at https://gitlab.com/ReI08/perception-energy-planner.
