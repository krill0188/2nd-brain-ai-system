---
title: "RMWorld: Task-Aware Radio World Models for Multi-UAV Communication Control"
created: 2026-08-23
updated: 2026-08-23
type: concept
tags: [drone, comms-protocol, radio-world-models, multi-uav, reinforcement-learning]
sources: [inbox/fetch-2026-08-23-arxiv-rmworld-task-aware-radio-world-models-with-value-of-informat.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# RMWorld: Task-Aware Radio World Models

ArXiv paper (2026-08-20) presenting RMWorld, a task-aware radio world model framework for multi-UAV communication control.

## Problem

Reliable multi-UAV communication requires predicting aerial links before measurements are available. Radio world models have non-uniform errors — globally accurate models may fail along high-demand corridors or association boundaries.

## RMWorld Framework

Couples two key components:
1. **Value-of-information channel calibration**
2. **Credibility-diversity multi-trial selection**

## Technical Approach

- Biased propagation formula corrected by Bayesian residual
- Link valued by exact one-label reduction in locally linearized task-integrated posterior rate variance
- Counterfactual branches selected by task-gated log-determinant objective
- Conflict projection and fixed-batch validation

## Theoretical Results

- Variance-reduction identity derived
- Posterior task-risk equivalence proven
- Submodular greedy guarantee established
- Scoped first-order non-interference result

## Performance

- **3GPP trials**: 0.949 bit/s/Hz task-weighted RMSE
- **DeepMIMO trials**: 0.967 median backlog reduction vs Ensemble UCB at 37.5% more offline rollouts

## Related

- [[datalink-communication]] — Drone datalink communication
- [[swarm-coordination]] — UAV swarm coordination
- [[drone-ai-agents]] — AI agents for UAV control

## 📰 최근 관련 소식
- RMWorld: Task-Aware Radio World Models with Value-of-Information Guided Multi-Trial Learning for Multi-UAV Communication Control (arxiv.org, 2026-08-20) — http://arxiv.org/abs/2608.20126v1
