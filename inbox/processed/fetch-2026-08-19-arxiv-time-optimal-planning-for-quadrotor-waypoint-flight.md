---
title: "Time-Optimal Planning for Quadrotor Waypoint Flight"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: hardware
source: http://arxiv.org/abs/2108.04537v3
authors: "Philipp Foehn, Angel Romero, Davide Scaramuzza"
published: "2021-08-10"
tags: [drone, hardware, paper, arxiv]
---

# Time-Optimal Planning for Quadrotor Waypoint Flight

**Authors**: Philipp Foehn, Angel Romero, Davide Scaramuzza
**Published**: 2021-08-10
**arXiv**: http://arxiv.org/abs/2108.04537v3

## Abstract

Quadrotors are among the most agile flying robots. However, planning time-optimal trajectories at the actuation limit through multiple waypoints remains an open problem. This is crucial for applications such as inspection, delivery, search and rescue, and drone racing. Early works used polynomial trajectory formulations, which do not exploit the full actuator potential because of their inherent smoothness. Recent works resorted to numerical optimization but require waypoints to be allocated as costs or constraints at specific discrete times. However, this time allocation is a priori unknown and renders previous works incapable of producing truly time-optimal trajectories. To generate truly time-optimal trajectories, we propose a solution to the time allocation problem while exploiting the full quadrotor's actuator potential. We achieve this by introducing a formulation of progress along the trajectory, which enables the simultaneous optimization of the time allocation and the trajectory itself. We compare our method against related approaches and validate it in real-world flights in one of the world's largest motion-capture systems, where we outperform human expert drone pilots in a drone-racing task.
