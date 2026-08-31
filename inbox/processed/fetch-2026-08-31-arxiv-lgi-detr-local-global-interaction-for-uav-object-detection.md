---
title: "LGI-DETR: Local-Global Interaction for UAV Object Detection"
created: 2026-08-31
captured: 2026-08-31
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2503.18785v1
authors: "Zifa Chen"
published: "2025-03-24"
tags: [drone, ai-autonomy, paper, arxiv]
---

# LGI-DETR: Local-Global Interaction for UAV Object Detection

**Authors**: Zifa Chen
**Published**: 2025-03-24
**arXiv**: http://arxiv.org/abs/2503.18785v1

## Abstract

UAV has been widely used in various fields. However, most of the existing object detectors used in drones are not end-to-end and require the design of various complex components and careful fine-tuning. Most of the existing end-to-end object detectors are designed for natural scenes. It is not ideal to apply them directly to UAV images. In order to solve the above challenges, we design an local-global information interaction DETR for UAVs, namely LGI-DETR. Cross-layer bidirectional low-level and high-level feature information enhancement, this fusion method is effective especially in the field of small objection detection. At the initial stage of encoder, we propose a local spatial enhancement module (LSE), which enhances the low-level rich local spatial information into the high-level feature, and reduces the loss of local information in the transmission process of high-level information. At the final stage of the encoder, we propose a novel global information injection module (GII) designed to integrate rich high-level global semantic representations with low-level feature maps. This hierarchical fusion mechanism effectively addresses the inherent limitations of local receptive fields by propagating contextual information across the feature hierarchy. Experimental results on two challenging UAV image object detection benchmarks, VisDrone2019 and UAVDT, show that our proposed model outperforms the SOTA model. Compared to the baseline model, AP and AP50 improved by 1.9% and 2.4%, respectively.
