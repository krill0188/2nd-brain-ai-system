---
title: "Teaching in adverse scenes: a statistically feedback-driven threshold and mask adjustment teacher-student framework for object detection in UAV images under adverse scenes"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Chen, Hongyu; Liu, Jiping; Wang, Yong; Zhu, Jun; Feng, Dejun; Xie, Yakun"
year: "2025"
doi: "10.48550/arXiv.2506.11175"
url: "http://arxiv.org/abs/2506.11175v1"
zotero_key: FKQ27DKZ
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/teaching-in-adverse-scenes-a-statistically-feedback-driven-threshold-and-mask-ad.pdf
attachment_sha256: e04515a8eeaae49d82633cc5c74ba2f49659b8ea73b1a5b4c0d16d91c9b8cadb
sha256: 221f279241cb61db
---

# Teaching in adverse scenes: a statistically feedback-driven threshold and mask adjustment teacher-student framework for object detection in UAV images under adverse scenes

**Authors**: Chen, Hongyu; Liu, Jiping; Wang, Yong; Zhu, Jun; Feng, Dejun; Xie, Yakun  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2506.11175  
**URL**: http://arxiv.org/abs/2506.11175v1

## Abstract

Unsupervised Domain Adaptation (UDA) has shown promise in effectively alleviating the performance degradation caused by domain gaps between source and target domains, and it can potentially be generalized to UAV object detection in adverse scenes. However, existing UDA studies are based on natural images or clear UAV imagery, and research focused on UAV imagery in adverse conditions is still in its infancy. Moreover, due to the unique perspective of UAVs and the interference from adverse conditions, these methods often fail to accurately align features and are influenced by limited or noisy pseudo-labels. To address this, we propose the first benchmark for UAV object detection in adverse scenes, the Statistical Feedback-Driven Threshold and Mask Adjustment Teacher-Student Framework (SF-TMAT). Specifically, SF-TMAT introduces a design called Dynamic Step Feedback Mask Adjustment Autoencoder (DSFMA), which dynamically adjusts the mask ratio and reconstructs feature maps by integrating training progress and loss feedback. This approach dynamically adjusts the learning focus at different training stages to meet the model's needs for learning features at varying levels of granularity. Additionally, we propose a unique Variance Feedback Smoothing Threshold (VFST) strategy, which statistically computes the mean confidence of each class and dynamically adjusts the selection threshold by incorporating a variance penalty term. This strategy improves the quality of pseudo-labels and uncovers potentially valid labels, thus mitigating domain bias. Extensive experiments demonstrate the superiority and generalization capability of the proposed SF-TMAT in UAV object detection under adverse scene conditions. The Code is released at https://github.com/ChenHuyoo .

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
