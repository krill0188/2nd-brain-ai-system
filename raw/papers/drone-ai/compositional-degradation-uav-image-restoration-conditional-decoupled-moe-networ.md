---
title: "Compositional-Degradation UAV Image Restoration: Conditional Decoupled MoE Network and A Benchmark"
created: 2026-08-20
updated: 2026-08-20
type: paper
item_type: preprint
authors: "Yan, Jinquan; Zhao, Zhicheng; Tu, Zhengzheng; Li, Chenglong; Tang, Jin; Luo, Bin"
year: "2026"
doi: "10.48550/arXiv.2604.09313"
url: "http://arxiv.org/abs/2604.09313v1"
zotero_key: XFQEGI9G
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/compositional-degradation-uav-image-restoration-conditional-decoupled-moe-networ.pdf
attachment_sha256: a2ab58859338853d5f35b2bc7ed8ed5086963e63f167a20df064c52c24ff9fc0
sha256: bf3ca245d4e99a4e
---

# Compositional-Degradation UAV Image Restoration: Conditional Decoupled MoE Network and A Benchmark

**Authors**: Yan, Jinquan; Zhao, Zhicheng; Tu, Zhengzheng; Li, Chenglong; Tang, Jin; Luo, Bin  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2604.09313  
**URL**: http://arxiv.org/abs/2604.09313v1

## Abstract

UAV images are critical for applications such as large-area mapping, infrastructure inspection, and emergency response. However, in real-world flight environments, a single image is often affected by multiple degradation factors, including rain, haze, and noise, undermining downstream task performance. Current unified restoration approaches typically rely on implicit degradation representations that entangle multiple factors into a single condition, causing mutual interference among heterogeneous corrections. To this end, we propose DAME-Net, a Degradation-Aware Mixture-of-Experts Network that decouples explicit degradation perception from degradation-conditioned reconstruction for compositional UAV image restoration. Specifically, we design a Factor-wise Degradation Perception module(FDPM) to provide explicit per-factor degradation cues for the restoration stage through multi-label prediction with label-similarity-guided soft alignment, replacing implicit entangled conditions with interpretable and generalizable degradation descriptions. Moreover, we develop a Conditioned Decoupled MoE module(CDMM) that leverages these cues for stage-wise conditioning, spatial-frequency hybrid processing, and mask-constrained decoupled expert routing, enabling selective factor-specific correction while suppressing irrelevant interference. In addition, we construct the Multi-Degradation UAV Restoration benchmark (MDUR), the first large-scale UAV benchmark for compositional UAV image restoration, with 43 degradation configurations from single degradations to four-factor composites and standardized seen/unseen splits.Extensive experiments on MDUR demonstrate consistent improvements over representative unified restoration methods, with greater gains on unseen and higher-order composite degradations. Downstream experiments further validate benefits for UAV object detection.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
