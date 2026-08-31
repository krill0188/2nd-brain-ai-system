---
title: "WAVE-DETR Multi-Modal Visible and Acoustic Real-Life Drone Detector"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Stefanescu, Razvan; Oh, Ethan; Vazquez, Ruben; Mesterharm, Chris; Serban, Constantin; Chadha, Ritu"
year: "2025"
doi: "10.48550/arXiv.2509.09859"
url: "http://arxiv.org/abs/2509.09859v1"
zotero_key: S9MQ5DFS
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/wave-detr-multi-modal-visible-and-acoustic-real-life-drone-detector.pdf
attachment_sha256: 53aa6d0b62f33f801cd82e407c2d3cf6a2d5d0e1a984b274671153523bb765ef
sha256: 7e04adca2e65f7d4
---

# WAVE-DETR Multi-Modal Visible and Acoustic Real-Life Drone Detector

**Authors**: Stefanescu, Razvan; Oh, Ethan; Vazquez, Ruben; Mesterharm, Chris; Serban, Constantin; Chadha, Ritu  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2509.09859  
**URL**: http://arxiv.org/abs/2509.09859v1

## Abstract

We introduce a multi-modal WAVE-DETR drone detector combining visible RGB and acoustic signals for robust real-life UAV object detection. Our approach fuses visual and acoustic features in a unified object detector model relying on the Deformable DETR and Wav2Vec2 architectures, achieving strong performance under challenging environmental conditions. Our work leverage the existing Drone-vs-Bird dataset and the newly generated ARDrone dataset containing more than 7,500 synchronized images and audio segments. We show how the acoustic information is used to improve the performance of the Deformable DETR object detector on the real ARDrone dataset. We developed, trained and tested four different fusion configurations based on a gated mechanism, linear layer, MLP and cross attention. The Wav2Vec2 acoustic embeddings are fused with the multi resolution feature mappings of the Deformable DETR and enhance the object detection performance over all drones dimensions. The best performer is the gated fusion approach, which improves the mAP of the Deformable DETR object detector on our in-distribution and out-of-distribution ARDrone datasets by 11.1% to 15.3% for small drones across all IoU thresholds between 0.5 and 0.9. The mAP scores for medium and large drones are also enhanced, with overall gains across all drone sizes ranging from 3.27% to 5.84%.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
