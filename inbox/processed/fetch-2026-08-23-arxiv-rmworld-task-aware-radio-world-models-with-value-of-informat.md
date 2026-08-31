---
title: "RMWorld: Task-Aware Radio World Models with Value-of-Information Guided Multi-Trial Learning for Multi-UAV Communication Control"
created: 2026-08-23
captured: 2026-08-23
type: paper
domain: comms-protocol
source: http://arxiv.org/abs/2608.20126v1
authors: "Xiucheng Wang, Nan Cheng, Junxi Huan"
published: "2026-08-20"
tags: [drone, comms-protocol, paper, arxiv]
---

# RMWorld: Task-Aware Radio World Models with Value-of-Information Guided Multi-Trial Learning for Multi-UAV Communication Control

**Authors**: Xiucheng Wang, Nan Cheng, Junxi Huan
**Published**: 2026-08-20
**arXiv**: http://arxiv.org/abs/2608.20126v1

## Abstract

Reliable multi-UAV communication control depends on predicting which aerial links will serve traffic before measurements are available. Radio world models (radio WMs) make such planning tractable, but their errors are nonuniform: a globally accurate model may still fail along high-demand corridors or association boundaries where rate errors reverse control decisions. This mismatch creates a learning challenge. Link queries must reduce decision-relevant channel uncertainty, while counterfactual trials must be filtered so that biased rollouts do not corrupt the policy. Existing acquisition and model-based control treat these budgets separately, valuing uncertainty, coverage, or optimistic return rather than risk reduction. We present RMWorld, a task-aware radio-WM framework that couples value-of-information channel calibration with credibility-diversity multi-trial selection. A biased propagation formula is corrected by a Bayesian residual, and each link is valued by its exact one-label reduction in locally linearized task-integrated posterior rate variance. Counterfactual branches are selected by a task-gated log-determinant objective, followed by conflict projection and fixed-batch validation. We derive the variance-reduction identity, prove posterior task-risk equivalence and the submodular greedy guarantee, and establish a scoped first-order non-interference result. Across 100 paired 3GPP trials RMWorld reaches 0.949~bit/s/Hz task-weighted RMSE, and across 30 severe-load DeepMIMO trials it reduces median backlog by 0.967 versus Ensemble UCB at 37.5\% more offline rollouts.
