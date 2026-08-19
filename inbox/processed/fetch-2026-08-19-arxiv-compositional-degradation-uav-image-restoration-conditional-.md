---
title: "Compositional-Degradation UAV Image Restoration: Conditional Decoupled MoE Network and A Benchmark"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2604.09313v1
authors: "Jinquan Yan, Zhicheng Zhao, Zhengzheng Tu, Chenglong Li, Jin Tang, Bin Luo"
published: "2026-04-10"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Compositional-Degradation UAV Image Restoration: Conditional Decoupled MoE Network and A Benchmark

**Authors**: Jinquan Yan, Zhicheng Zhao, Zhengzheng Tu, Chenglong Li, Jin Tang, Bin Luo
**Published**: 2026-04-10
**arXiv**: http://arxiv.org/abs/2604.09313v1

## Abstract

UAV images are critical for applications such as large-area mapping, infrastructure inspection, and emergency response. However, in real-world flight environments, a single image is often affected by multiple degradation factors, including rain, haze, and noise, undermining downstream task performance. Current unified restoration approaches typically rely on implicit degradation representations that entangle multiple factors into a single condition, causing mutual interference among heterogeneous corrections. To this end, we propose DAME-Net, a Degradation-Aware Mixture-of-Experts Network that decouples explicit degradation perception from degradation-conditioned reconstruction for compositional UAV image restoration. Specifically, we design a Factor-wise Degradation Perception module(FDPM) to provide explicit per-factor degradation cues for the restoration stage through multi-label prediction with label-similarity-guided soft alignment, replacing implicit entangled conditions with interpretable and generalizable degradation descriptions. Moreover, we develop a Conditioned Decoupled MoE module(CDMM) that leverages these cues for stage-wise conditioning, spatial-frequency hybrid processing, and mask-constrained decoupled expert routing, enabling selective factor-specific correction while suppressing irrelevant interference. In addition, we construct the Multi-Degradation UAV Restoration benchmark (MDUR), the first large-scale UAV benchmark for compositional UAV image restoration, with 43 degradation configurations from single degradations to four-factor composites and standardized seen/unseen splits.Extensive experiments on MDUR demonstrate consistent improvements over representative unified restoration methods, with greater gains on unseen and higher-order composite degradations. Downstream experiments further validate benefits for UAV object detection.
