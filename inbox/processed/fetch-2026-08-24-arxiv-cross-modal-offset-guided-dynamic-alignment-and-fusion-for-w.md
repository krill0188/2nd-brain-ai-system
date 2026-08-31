---
title: "Cross-modal Offset-guided Dynamic Alignment and Fusion for Weakly Aligned UAV Object Detection"
created: 2026-08-24
captured: 2026-08-24
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2506.16737v1
authors: "Liu Zongzhen, Luo Hui, Wang Zhixing, Wei Yuxing, Zuo Haorui, Zhang Jianlin"
published: "2025-06-20"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Cross-modal Offset-guided Dynamic Alignment and Fusion for Weakly Aligned UAV Object Detection

**Authors**: Liu Zongzhen, Luo Hui, Wang Zhixing, Wei Yuxing, Zuo Haorui, Zhang Jianlin
**Published**: 2025-06-20
**arXiv**: http://arxiv.org/abs/2506.16737v1

## Abstract

Unmanned aerial vehicle (UAV) object detection plays a vital role in applications such as environmental monitoring and urban security. To improve robustness, recent studies have explored multimodal detection by fusing visible (RGB) and infrared (IR) imagery. However, due to UAV platform motion and asynchronous imaging, spatial misalignment frequently occurs between modalities, leading to weak alignment. This introduces two major challenges: semantic inconsistency at corresponding spatial locations and modality conflict during feature fusion. Existing methods often address these issues in isolation, limiting their effectiveness. In this paper, we propose Cross-modal Offset-guided Dynamic Alignment and Fusion (CoDAF), a unified framework that jointly tackles both challenges in weakly aligned UAV-based object detection. CoDAF comprises two novel modules: the Offset-guided Semantic Alignment (OSA), which estimates attention-based spatial offsets and uses deformable convolution guided by a shared semantic space to align features more precisely; and the Dynamic Attention-guided Fusion Module (DAFM), which adaptively balances modality contributions through gating and refines fused features via spatial-channel dual attention. By integrating alignment and fusion in a unified design, CoDAF enables robust UAV object detection. Experiments on standard benchmarks validate the effectiveness of our approach, with CoDAF achieving a mAP of 78.6% on the DroneVehicle dataset.
