---
title: "RT-DETR++ for UAV Object Detection"
created: 2026-08-23
captured: 2026-08-23
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2509.09157v1
authors: "Yuan Shufang"
published: "2025-09-11"
tags: [drone, ai-autonomy, paper, arxiv]
---

# RT-DETR++ for UAV Object Detection

**Authors**: Yuan Shufang
**Published**: 2025-09-11
**arXiv**: http://arxiv.org/abs/2509.09157v1

## Abstract

Object detection in unmanned aerial vehicle (UAV) imagery presents significant challenges. Issues such as densely packed small objects, scale variations, and occlusion are commonplace. This paper introduces RT-DETR++, which enhances the encoder component of the RT-DETR model. Our improvements focus on two key aspects. First, we introduce a channel-gated attention-based upsampling/downsampling (AU/AD) mechanism. This dual-path system minimizes errors and preserves details during feature layer propagation. Second, we incorporate CSP-PAC during feature fusion. This technique employs parallel hollow convolutions to process local and contextual information within the same layer, facilitating the integration of multi-scale features. Evaluation demonstrates that our novel neck design achieves superior performance in detecting small and densely packed objects. The model maintains sufficient speed for real-time detection without increasing computational complexity. This study provides an effective approach for feature encoding design in real-time detection systems.
