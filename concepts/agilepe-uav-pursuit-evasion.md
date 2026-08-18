---
title: "AgilePE: UAV Pursuit-Evasion via Self-Play RL"
created: 2026-08-19
updated: 2026-08-19
type: concept
domain: ai-autonomy
tags: [drone, ai-autonomy, reinforcement-learning, sim-to-real, pursuit-evasion]
sources: [inbox/fetch-2026-08-19-arxiv-agilepe-autonomous-uav-pursuit-evasion-via-self-play-reinfor.md]
confidence: high
contested: false
contradictions: []
---

# AgilePE: UAV Pursuit-Evasion via Self-Play RL

End-to-end autonomous pursuit-evasion system for UAVs using competitive self-play reinforcement learning with zero-shot sim-to-real transfer.

## Overview

AgilePE addresses the fundamental challenge of autonomous pursuit-evasion for UAVs, requiring rapid decision-making under tightly coupled dynamics and continuously changing opponent behaviors. Traditional rule-based or differential-game approaches struggle with high-dimensional aerial interactions and agile maneuvering.

## Key Components

### Low-Level Control
- Policy directly maps onboard state observations to Collective Thrust and Body Rates (CTBR) commands
- End-to-end agile maneuvering without intermediate trajectory planners or waypoint controllers

### Training Methodology
- **Prioritized Fictitious Self-Play (PFSP)**: Competitive self-play with diversified opponent pool
- Agents improve against historical policies while stabilizing optimization
- Reduces policy oscillation and enables emergence of sophisticated pursuit/evasion strategies

### Sim-to-Real Pipeline
- Hardware-aligned simulation modeling:
  - Actuator-response dynamics
  - Communication latency
  - Domain randomization
- Learned policies transfer zero-shot to real quadrotors without task-specific tuning

## Real-World Results

- Reproduces pursuit-evasion tactics observed in simulation
- Includes rapid dodging and flanking maneuvers
- Demonstrates interactive two-agent zero-shot deployment

## Related Concepts

- [[reinforcement-learning-drone]] — RL techniques for drone control
- [[sim-to-real-transfer]] — Simulation to real-world policy transfer
- [[swarm-coordination]] — Multi-drone coordination strategies
- [[ai-agent-drone-navigation]] — LLM/agent-based drone navigation

## Sources

- Tang et al., "AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning", arXiv:2608.14135, 2026-08-14
