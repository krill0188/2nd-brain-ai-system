---
title: "UAV-DETR: DETR for Anti-Drone Target Detection"
created: 2026-08-12
updated: 2026-08-12
type: paper
item_type: preprint
authors: "Yang, Jun; Wang, Dong; Yin, Hongxu; Li, Hongpeng; Yu, Jianxiong"
year: "2026"
doi: "10.48550/arXiv.2603.22841"
url: "http://arxiv.org/abs/2603.22841v1"
zotero_key: VQEH9QME
tags: ["auto:2nd-brain", "drone-ai"]
attachment_path: raw/papers/files/drone-ai/uav-detr-detr-for-anti-drone-target-detection.pdf
attachment_sha256: a607497c67fc2a23cd1980d65968206468ba21c1f8a3ebf6cfb50c75af2c44a2
sha256: 03d9ec40f1028e29
---

# UAV-DETR: DETR for Anti-Drone Target Detection

**Authors**: Yang, Jun; Wang, Dong; Yin, Hongxu; Li, Hongpeng; Yu, Jianxiong  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2603.22841  
**URL**: http://arxiv.org/abs/2603.22841v1

## Abstract

Drone detection is pivotal in numerous security and counter-UAV applications. However, existing deep learning-based methods typically struggle to balance robust feature representation with computational efficiency. This challenge is particularly acute when detecting miniature drones against complex backgrounds under severe environmental interference. To address these issues, we introduce UAV-DETR, a novel framework that integrates a small-target-friendly architecture with real-time detection capabilities. Specifically, UAV-DETR features a WTConv-enhanced backbone and a Sliding Window Self-Attention (SWSA-IFI) encoder, capturing the high-frequency structural details of tiny targets while drastically reducing parameter overhead. Furthermore, we propose an Efficient Cross-Scale Feature Recalibration and Fusion Network (ECFRFN) to suppress background noise and aggregate multi-scale semantics. To further enhance accuracy, UAV-DETR incorporates a hybrid Inner-CIoU and NWD loss strategy, mitigating the extreme sensitivity of standard IoU metrics to minor positional deviations in small objects. Extensive experiments demonstrate that UAV-DETR significantly outperforms the baseline RT-DETR on our custom UAV dataset (+6.61% in mAP50:95, with a 39.8% reduction in parameters) and the public DUT-ANTI-UAV benchmark (+1.4% in Precision, +1.0% in F1-Score). These results establish UAV-DETR as a superior trade-off between efficiency and precision in counter-UAV object detection. The code is available at https://github.com/wd-sir/UAVDETR.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
