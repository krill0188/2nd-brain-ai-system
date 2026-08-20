---
title: "UAV-DETR: DETR for Anti-Drone Target Detection"
created: 2026-08-20
captured: 2026-08-20
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2603.22841v1
authors: "Jun Yang, Dong Wang, Hongxu Yin, Hongpeng Li, Jianxiong Yu"
published: "2026-03-24"
tags: [drone, ai-autonomy, paper, arxiv]
---

# UAV-DETR: DETR for Anti-Drone Target Detection

**Authors**: Jun Yang, Dong Wang, Hongxu Yin, Hongpeng Li, Jianxiong Yu
**Published**: 2026-03-24
**arXiv**: http://arxiv.org/abs/2603.22841v1

## Abstract

Drone detection is pivotal in numerous security and counter-UAV applications. However, existing deep learning-based methods typically struggle to balance robust feature representation with computational efficiency. This challenge is particularly acute when detecting miniature drones against complex backgrounds under severe environmental interference. To address these issues, we introduce UAV-DETR, a novel framework that integrates a small-target-friendly architecture with real-time detection capabilities. Specifically, UAV-DETR features a WTConv-enhanced backbone and a Sliding Window Self-Attention (SWSA-IFI) encoder, capturing the high-frequency structural details of tiny targets while drastically reducing parameter overhead. Furthermore, we propose an Efficient Cross-Scale Feature Recalibration and Fusion Network (ECFRFN) to suppress background noise and aggregate multi-scale semantics. To further enhance accuracy, UAV-DETR incorporates a hybrid Inner-CIoU and NWD loss strategy, mitigating the extreme sensitivity of standard IoU metrics to minor positional deviations in small objects. Extensive experiments demonstrate that UAV-DETR significantly outperforms the baseline RT-DETR on our custom UAV dataset (+6.61% in mAP50:95, with a 39.8% reduction in parameters) and the public DUT-ANTI-UAV benchmark (+1.4% in Precision, +1.0% in F1-Score). These results establish UAV-DETR as a superior trade-off between efficiency and precision in counter-UAV object detection. The code is available at https://github.com/wd-sir/UAVDETR.
