---
title: "CLSC DETR: Reliable Candidate Ranking via Cross Layer Geometric Support for UAV Small Object Detection"
created: 2026-08-31
captured: 2026-08-31
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2608.21457v1
authors: "Junyan Lin"
published: "2026-08-20"
tags: [drone, ai-autonomy, paper, arxiv]
---

# CLSC DETR: Reliable Candidate Ranking via Cross Layer Geometric Support for UAV Small Object Detection

**Authors**: Junyan Lin
**Published**: 2026-08-20
**arXiv**: http://arxiv.org/abs/2608.21457v1

## Abstract

Unmanned aerial vehicle (UAV) object detection is critical for applications such as target search, where accurate detection of small objects in complex aerial scenes remains challenging. The limited spatial extent, dense distribution, and frequent occlusion of small objects make reliable candidate ranking particularly difficult. Existing Detection Transformer (DETR) based methods improve ranking by estimating localization quality from individual queries and incorporating it into classification scores. However, a single query often lacks sufficient geometric evidence for small objects with weak boundary cues, resulting in unreliable quality estimation and unstable ranking. To address this limitation, we propose Cross Layer Local Support and Consistency Calibration for DETR, termed CLSC DETR. Specifically, the Cross Layer Local Support module establishes correspondences between final layer queries and intermediate layer candidates to aggregate complementary geometric evidence for more reliable localization quality estimation, while the Classification and Localization Consistency Calibration module adaptively adjusts classification scores according to localization quality and classification reliability to improve candidate ranking. Experiments show that CLSC DETR improves AP and AP$_{75}$ over the baseline by 1.5\% and 2.0\% on VisDrone, respectively, while achieving consistent improvements on UAVDT.
