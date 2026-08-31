---
title: "RMWorld: Task-Aware Radio World Models with Value-of-Information Guided Multi-Trial Learning for Multi-UAV Communication Control"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Wang, Xiucheng; Cheng, Nan; Huan, Junxi"
year: "2026"
doi: "10.48550/arXiv.2608.20126"
url: "http://arxiv.org/abs/2608.20126v1"
zotero_key: R3WUXM48
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/swarm/rmworld-task-aware-radio-world-models-with-value-of-information-guided-multi-tri.pdf
attachment_sha256: 4f550e4a7f84e0381b01493049d749bde683889809d0291af3dfd3f9a828d7ee
sha256: 231abcecaf7d6889
---

# RMWorld: Task-Aware Radio World Models with Value-of-Information Guided Multi-Trial Learning for Multi-UAV Communication Control

**Authors**: Wang, Xiucheng; Cheng, Nan; Huan, Junxi  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.20126  
**URL**: http://arxiv.org/abs/2608.20126v1

## Abstract

Reliable multi-UAV communication control depends on predicting which aerial links will serve traffic before measurements are available. Radio world models (radio WMs) make such planning tractable, but their errors are nonuniform: a globally accurate model may still fail along high-demand corridors or association boundaries where rate errors reverse control decisions. This mismatch creates a learning challenge. Link queries must reduce decision-relevant channel uncertainty, while counterfactual trials must be filtered so that biased rollouts do not corrupt the policy. Existing acquisition and model-based control treat these budgets separately, valuing uncertainty, coverage, or optimistic return rather than risk reduction. We present RMWorld, a task-aware radio-WM framework that couples value-of-information channel calibration with credibility-diversity multi-trial selection. A biased propagation formula is corrected by a Bayesian residual, and each link is valued by its exact one-label reduction in locally linearized task-integrated posterior rate variance. Counterfactual branches are selected by a task-gated log-determinant objective, followed by conflict projection and fixed-batch validation. We derive the variance-reduction identity, prove posterior task-risk equivalence and the submodular greedy guarantee, and establish a scoped first-order non-interference result. Across 100 paired 3GPP trials RMWorld reaches 0.949~bit/s/Hz task-weighted RMSE, and across 30 severe-load DeepMIMO trials it reduces median backlog by 0.967 versus Ensemble UCB at 37.5\% more offline rollouts.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
