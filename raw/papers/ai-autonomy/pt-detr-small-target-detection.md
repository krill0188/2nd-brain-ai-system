---
title: "PT-DETR: Small Target Detection Based on Partially-Aware Detail Focus"
created: 2026-08-20
captured: 2026-08-20
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2510.26630v1
authors: "Bingcong Huo, Zhiming Wang"
published: "2025-10-30"
tags: [drone, ai-autonomy, paper, arxiv]
---

# PT-DETR: Small Target Detection Based on Partially-Aware Detail Focus

**Authors**: Bingcong Huo, Zhiming Wang
**Published**: 2025-10-30
**arXiv**: http://arxiv.org/abs/2510.26630v1

## Abstract

To address the challenges in UAV object detection, such as complex backgrounds, severe occlusion, dense small objects, and varying lighting conditions,this paper proposes PT-DETR based on RT-DETR, a novel detection algorithm specifically designed for small objects in UAV imagery. In the backbone network, we introduce the Partially-Aware Detail Focus (PADF) Module to enhance feature extraction for small objects. Additionally,we design the Median-Frequency Feature Fusion (MFFF) module,which effectively improves the model's ability to capture small-object details and contextual information. Furthermore,we incorporate Focaler-SIoU to strengthen the model's bounding box matching capability and increase its sensitivity to small-object features, thereby further enhancing detection accuracy and robustness. Compared with RT-DETR, our PT-DETR achieves mAP improvements of 1.6% and 1.7% on the VisDrone2019 dataset with lower computational complexity and fewer parameters, demonstrating its robustness and feasibility for small-object detection tasks.
