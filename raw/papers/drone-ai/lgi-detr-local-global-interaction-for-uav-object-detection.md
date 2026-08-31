---
title: "LGI-DETR: Local-Global Interaction for UAV Object Detection"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Chen, Zifa"
year: "2025"
doi: "10.48550/arXiv.2503.18785"
url: "http://arxiv.org/abs/2503.18785v1"
zotero_key: 84V4R36P
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/lgi-detr-local-global-interaction-for-uav-object-detection.pdf
attachment_sha256: 83757ad8be718bed6b0ab38eed2632ec7e0125292f41e814349a0955079c805a
sha256: fba315f120cde3d2
---

# LGI-DETR: Local-Global Interaction for UAV Object Detection

**Authors**: Chen, Zifa  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2503.18785  
**URL**: http://arxiv.org/abs/2503.18785v1

## Abstract

UAV has been widely used in various fields. However, most of the existing object detectors used in drones are not end-to-end and require the design of various complex components and careful fine-tuning. Most of the existing end-to-end object detectors are designed for natural scenes. It is not ideal to apply them directly to UAV images. In order to solve the above challenges, we design an local-global information interaction DETR for UAVs, namely LGI-DETR. Cross-layer bidirectional low-level and high-level feature information enhancement, this fusion method is effective especially in the field of small objection detection. At the initial stage of encoder, we propose a local spatial enhancement module (LSE), which enhances the low-level rich local spatial information into the high-level feature, and reduces the loss of local information in the transmission process of high-level information. At the final stage of the encoder, we propose a novel global information injection module (GII) designed to integrate rich high-level global semantic representations with low-level feature maps. This hierarchical fusion mechanism effectively addresses the inherent limitations of local receptive fields by propagating contextual information across the feature hierarchy. Experimental results on two challenging UAV image object detection benchmarks, VisDrone2019 and UAVDT, show that our proposed model outperforms the SOTA model. Compared to the baseline model, AP and AP50 improved by 1.9% and 2.4%, respectively.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
