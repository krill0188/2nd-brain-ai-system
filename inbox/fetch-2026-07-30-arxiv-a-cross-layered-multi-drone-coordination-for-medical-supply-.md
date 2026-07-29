---
title: "A Cross-Layered Multi-Drone Coordination for Medical Supply Delivery during Disaster Response Management"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2605.09342v1
authors: "Aneesh Calyam, Subrahmanya Chandra Bhamidipati, Zack Murry, Sharan Srinivas"
published: "2026-05-10"
tags: [drone, flight-control, paper, arxiv]
---

# A Cross-Layered Multi-Drone Coordination for Medical Supply Delivery during Disaster Response Management

**Authors**: Aneesh Calyam, Subrahmanya Chandra Bhamidipati, Zack Murry, Sharan Srinivas
**Published**: 2026-05-10
**arXiv**: http://arxiv.org/abs/2605.09342v1

## Abstract

Autonomous drone fleets have immense potential in medical supply delivery during disaster incident response. However, coordinating multiple drones in such settings introduces compounding challenges: dynamic environmental hazards such as wind, obstacles, and intermittent network connectivity, constrained energy budgets, and the need to serve patient locations fairly under deadlines and triage-based priority while optimizing schedule utilization. In this paper, we present CEDA, a novel CTDE Deep Q-Network algorithm for cooperative multi-drone medical delivery, designed to jointly optimize triage-priority-aware routing, multi-agent coordination, and energy-efficient navigation under dynamic uncertainty. CEDA introduces a Priority-Preserving Fair Scheduling strategy, in which a structured reward function encodes both triage weights and complementary fairness mechanisms ensuring no patient class is starved of service. We evaluate CEDA in a simulated grid environment featuring dynamic hazard zones, stochastic action failures, and dynamically spawning patients across three triage priority levels, as well as in a PX4 SITL validation using two X500 quadrotors controlled via MAVSDK in offboard position mode. Simulation results demonstrate that CEDA achieves a delivery completion rate above 85%, reduces obstacle collisions by over 90% across training, and delivers an average of 6 patients per episode with a triage efficiency of 0.82. CEDA preserves clinical priority ordering, Critical patients are served first, while achieving near-zero mortality across lower-triage classes, confirming that priority-weighted routing does not condemn Stable or Urgent patients to neglect. PX4 SITL validation further demonstrates that the learned policy remains executable and triage-coherent under practical communication constraints and realistic multi-drone coordination in disaster response settings.
