---
title: "Robust Visual SLAM for UAV Navigation in GPS-Denied and Degraded Environments: A Multi-Paradigm Evaluation and Deployment Study"
created: 2026-08-19
updated: 2026-08-19
type: paper
item_type: preprint
authors: "Kumar, Prasoon; Deepak, Akshay; Kumar, Sandeep"
year: "2026"
doi: "10.48550/arXiv.2605.03678"
url: "http://arxiv.org/abs/2605.03678v1"
zotero_key: MZEPSR8B
tags: ["auto:2nd-brain", "drone-ai"]
attachment_path: raw/papers/files/drone-ai/robust-visual-slam-for-uav-navigation-in-gps-denied-and-degraded-environments-a-.pdf
attachment_sha256: 2010aa85b8a7fca7e38455ef722adee6d927b9ba47d9e88345ad4395ca6350ce
sha256: 87948eed6d3d6b25
---

# Robust Visual SLAM for UAV Navigation in GPS-Denied and Degraded Environments: A Multi-Paradigm Evaluation and Deployment Study

**Authors**: Kumar, Prasoon; Deepak, Akshay; Kumar, Sandeep  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2605.03678  
**URL**: http://arxiv.org/abs/2605.03678v1

## Abstract

Reliable localization in GPS-denied, visually degraded environments is critical for autonomous UAV opera- tions. This paper presents a systematic comparative evaluation of five V-SLAM systems ORB-SLAM3, DPVO, DROID-SLAM, DUSt3R, and MASt3R spanning classical, deep learning, recurrent, and Vision Transformer (ViT) paradigms. Experiments are conducted on curated sequences from four public benchmarks (TUM RGB-D, EuRoC MAV, UMA-VI, SubT-MRS) and a custom monocular indoor dataset under five controlled degradation conditions (normal, low light, dust haze, motion blur, and combined), with sub-millimeter Vicon ground truth. Results show that ORB-SLAM3 fails critically under severe degradation (62.4% overall TSR; 0% under dense haze), while learning-based methods remain robust: MASt3R achieves the lowest degraded ATE (0.027 m) and DUSt3R the highest tracking success (96.5%). DPVO offers the best efficiency robustness trade-off (18.6 FPS, 3.1 GB GPU memory, 86.1% TSR), making it the preferred choice for memory-constrained embedded platforms. Embedded deployment analysis across NVIDIA Jetson platforms provides actionable guidelines for SLAM selection under SWaP-constrained UAV scenarios.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
