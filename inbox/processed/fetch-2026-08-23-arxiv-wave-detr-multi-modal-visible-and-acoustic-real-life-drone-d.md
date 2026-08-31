---
title: "WAVE-DETR Multi-Modal Visible and Acoustic Real-Life Drone Detector"
created: 2026-08-23
captured: 2026-08-23
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2509.09859v1
authors: "Razvan Stefanescu, Ethan Oh, Ruben Vazquez, Chris Mesterharm, Constantin Serban, Ritu Chadha"
published: "2025-09-11"
tags: [drone, ai-autonomy, paper, arxiv]
---

# WAVE-DETR Multi-Modal Visible and Acoustic Real-Life Drone Detector

**Authors**: Razvan Stefanescu, Ethan Oh, Ruben Vazquez, Chris Mesterharm, Constantin Serban, Ritu Chadha
**Published**: 2025-09-11
**arXiv**: http://arxiv.org/abs/2509.09859v1

## Abstract

We introduce a multi-modal WAVE-DETR drone detector combining visible RGB and acoustic signals for robust real-life UAV object detection. Our approach fuses visual and acoustic features in a unified object detector model relying on the Deformable DETR and Wav2Vec2 architectures, achieving strong performance under challenging environmental conditions. Our work leverage the existing Drone-vs-Bird dataset and the newly generated ARDrone dataset containing more than 7,500 synchronized images and audio segments. We show how the acoustic information is used to improve the performance of the Deformable DETR object detector on the real ARDrone dataset. We developed, trained and tested four different fusion configurations based on a gated mechanism, linear layer, MLP and cross attention. The Wav2Vec2 acoustic embeddings are fused with the multi resolution feature mappings of the Deformable DETR and enhance the object detection performance over all drones dimensions. The best performer is the gated fusion approach, which improves the mAP of the Deformable DETR object detector on our in-distribution and out-of-distribution ARDrone datasets by 11.1% to 15.3% for small drones across all IoU thresholds between 0.5 and 0.9. The mAP scores for medium and large drones are also enhanced, with overall gains across all drone sizes ranging from 3.27% to 5.84%.
