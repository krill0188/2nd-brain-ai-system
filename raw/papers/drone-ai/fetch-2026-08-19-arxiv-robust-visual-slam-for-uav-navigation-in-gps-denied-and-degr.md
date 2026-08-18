---
title: "Robust Visual SLAM for UAV Navigation in GPS-Denied and Degraded Environments: A Multi-Paradigm Evaluation and Deployment Study"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: drone-ai
source: http://arxiv.org/abs/2605.03678v1
authors: "Prasoon Kumar, Akshay Deepak, Sandeep Kumar"
published: "2026-05-05"
tags: [drone, drone-ai, paper, arxiv]
---

# Robust Visual SLAM for UAV Navigation in GPS-Denied and Degraded Environments: A Multi-Paradigm Evaluation and Deployment Study

**Authors**: Prasoon Kumar, Akshay Deepak, Sandeep Kumar
**Published**: 2026-05-05
**arXiv**: http://arxiv.org/abs/2605.03678v1

## Abstract

Reliable localization in GPS-denied, visually degraded environments is critical for autonomous UAV opera- tions. This paper presents a systematic comparative evaluation of five V-SLAM systems ORB-SLAM3, DPVO, DROID-SLAM, DUSt3R, and MASt3R spanning classical, deep learning, recurrent, and Vision Transformer (ViT) paradigms. Experiments are conducted on curated sequences from four public benchmarks (TUM RGB-D, EuRoC MAV, UMA-VI, SubT-MRS) and a custom monocular indoor dataset under five controlled degradation conditions (normal, low light, dust haze, motion blur, and combined), with sub-millimeter Vicon ground truth. Results show that ORB-SLAM3 fails critically under severe degradation (62.4% overall TSR; 0% under dense haze), while learning-based methods remain robust: MASt3R achieves the lowest degraded ATE (0.027 m) and DUSt3R the highest tracking success (96.5%). DPVO offers the best efficiency robustness trade-off (18.6 FPS, 3.1 GB GPU memory, 86.1% TSR), making it the preferred choice for memory-constrained embedded platforms. Embedded deployment analysis across NVIDIA Jetson platforms provides actionable guidelines for SLAM selection under SWaP-constrained UAV scenarios.
