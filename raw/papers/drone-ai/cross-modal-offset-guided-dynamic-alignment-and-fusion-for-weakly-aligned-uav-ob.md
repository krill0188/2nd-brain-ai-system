---
title: "Cross-modal Offset-guided Dynamic Alignment and Fusion for Weakly Aligned UAV Object Detection"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Zongzhen, Liu; Hui, Luo; Zhixing, Wang; Yuxing, Wei; Haorui, Zuo; Jianlin, Zhang"
year: "2025"
doi: "10.48550/arXiv.2506.16737"
url: "http://arxiv.org/abs/2506.16737v1"
zotero_key: NMWH2UX8
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/cross-modal-offset-guided-dynamic-alignment-and-fusion-for-weakly-aligned-uav-ob.pdf
attachment_sha256: 43e5d60bbef87eadf762c0b2fbdc9bd84a3fcd6dcd468dbe242b23b56ae1b847
sha256: a1de82a8d2528ae0
---

# Cross-modal Offset-guided Dynamic Alignment and Fusion for Weakly Aligned UAV Object Detection

**Authors**: Zongzhen, Liu; Hui, Luo; Zhixing, Wang; Yuxing, Wei; Haorui, Zuo; Jianlin, Zhang  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2506.16737  
**URL**: http://arxiv.org/abs/2506.16737v1

## Abstract

Unmanned aerial vehicle (UAV) object detection plays a vital role in applications such as environmental monitoring and urban security. To improve robustness, recent studies have explored multimodal detection by fusing visible (RGB) and infrared (IR) imagery. However, due to UAV platform motion and asynchronous imaging, spatial misalignment frequently occurs between modalities, leading to weak alignment. This introduces two major challenges: semantic inconsistency at corresponding spatial locations and modality conflict during feature fusion. Existing methods often address these issues in isolation, limiting their effectiveness. In this paper, we propose Cross-modal Offset-guided Dynamic Alignment and Fusion (CoDAF), a unified framework that jointly tackles both challenges in weakly aligned UAV-based object detection. CoDAF comprises two novel modules: the Offset-guided Semantic Alignment (OSA), which estimates attention-based spatial offsets and uses deformable convolution guided by a shared semantic space to align features more precisely; and the Dynamic Attention-guided Fusion Module (DAFM), which adaptively balances modality contributions through gating and refines fused features via spatial-channel dual attention. By integrating alignment and fusion in a unified design, CoDAF enables robust UAV object detection. Experiments on standard benchmarks validate the effectiveness of our approach, with CoDAF achieving a mAP of 78.6% on the DroneVehicle dataset.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
