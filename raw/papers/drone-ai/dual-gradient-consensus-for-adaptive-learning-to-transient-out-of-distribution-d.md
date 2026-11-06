---
title: "Dual Gradient Consensus for Adaptive Learning to Transient Out-of-Distribution Disturbances in Quadrotor Control"
created: 2026-10-28
updated: 2026-10-28
type: paper
item_type: preprint
authors: "Tan, Mingtian; Tzoumas, Vasileios"
year: "2026"
doi: "10.48550/arXiv.2610.34538"
url: "http://arxiv.org/abs/2610.34538v1"
zotero_key: TJCQAT98
tags: ["auto:2nd-brain"]
sha256: 76e93edc5f5b71bf
---

# Dual Gradient Consensus for Adaptive Learning to Transient Out-of-Distribution Disturbances in Quadrotor Control

**Authors**: Tan, Mingtian; Tzoumas, Vasileios  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2610.34538  
**URL**: http://arxiv.org/abs/2610.34538v1

## Abstract

Quadrotor trajectory tracking under unmodeled disturbances often relies on online residual adaptation, but short out-domain residuals can corrupt the learned disturbance model when constant-step updates treat every residual gradient uniformly. We propose Dual Gradient Consensus (DGC), an adaptive-learning method for mixed in-domain/out-domain disturbances that retains the random Fourier feature model, offline BPTT policy, and least-squares adaptation of a prior domain-adaptive residual policy (DAPL) while modifying the online update step size. DGC compares each residual gradient with long- and short-term gradient memories, classifies the current adaptation regime, and uses a confidence map to suppress unreliable updates while recovering adaptation after persistent domain shifts. We evaluate DGC in numerical quadrotor trajectory tracking under four residuals that mix an in-domain component with short out-domain events. Compared with $L_1$-augmented MPC, RFF-based MPC, constant-step DAPL, and a frozen-parameter baseline, DGC achieves the lowest mean position RMSE in all four cases.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
