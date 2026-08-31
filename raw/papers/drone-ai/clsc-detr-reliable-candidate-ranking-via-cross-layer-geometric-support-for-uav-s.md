---
title: "CLSC DETR: Reliable Candidate Ranking via Cross Layer Geometric Support for UAV Small Object Detection"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Lin, Junyan"
year: "2026"
doi: "10.48550/arXiv.2608.21457"
url: "http://arxiv.org/abs/2608.21457v1"
zotero_key: HAMIWTII
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/clsc-detr-reliable-candidate-ranking-via-cross-layer-geometric-support-for-uav-s.pdf
attachment_sha256: fa870ff106ad68bbc53db159e0dac87ae0d9246f319f1a727c0fbd5c36cb7241
sha256: 9c8b563614ee9c5c
---

# CLSC DETR: Reliable Candidate Ranking via Cross Layer Geometric Support for UAV Small Object Detection

**Authors**: Lin, Junyan  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.21457  
**URL**: http://arxiv.org/abs/2608.21457v1

## Abstract

Unmanned aerial vehicle (UAV) object detection is critical for applications such as target search, where accurate detection of small objects in complex aerial scenes remains challenging. The limited spatial extent, dense distribution, and frequent occlusion of small objects make reliable candidate ranking particularly difficult. Existing Detection Transformer (DETR) based methods improve ranking by estimating localization quality from individual queries and incorporating it into classification scores. However, a single query often lacks sufficient geometric evidence for small objects with weak boundary cues, resulting in unreliable quality estimation and unstable ranking. To address this limitation, we propose Cross Layer Local Support and Consistency Calibration for DETR, termed CLSC DETR. Specifically, the Cross Layer Local Support module establishes correspondences between final layer queries and intermediate layer candidates to aggregate complementary geometric evidence for more reliable localization quality estimation, while the Classification and Localization Consistency Calibration module adaptively adjusts classification scores according to localization quality and classification reliability to improve candidate ranking. Experiments show that CLSC DETR improves AP and AP$_{75}$ over the baseline by 1.5\% and 2.0\% on VisDrone, respectively, while achieving consistent improvements on UAVDT.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
