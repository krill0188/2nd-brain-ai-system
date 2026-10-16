---
title: "Efficient Multimodal Beam Prediction for Real-World 6G UAV Communications via Image-Position-Synthetic Fusion"
created: 2026-10-15
captured: 2026-10-15
type: paper
domain: comms-protocol
source: http://arxiv.org/abs/2610.14593v1
authors: "Rifat Bin Reza, Md Ahadul Haque Suvo, Jia Uddin, Saifur Rahman Sabuj"
published: "2026-10-10"
tags: [drone, comms-protocol, paper, arxiv]
attachment_path: raw/papers/files/comms-protocol/efficient-multimodal-beam-prediction-for-real-world-6g-uav-c.html
attachment_type: html
attachment_sha256: 81782d48598e03d08022cfdb379de2608e0b75862f8a8dbb3f9e1af4ebdfda55
---

# Efficient Multimodal Beam Prediction for Real-World 6G UAV Communications via Image-Position-Synthetic Fusion

**Authors**: Rifat Bin Reza, Md Ahadul Haque Suvo, Jia Uddin, Saifur Rahman Sabuj
**Published**: 2026-10-10
**arXiv**: http://arxiv.org/abs/2610.14593v1

## Abstract

Camera-based beam selection can reduce the need for exhaustive channel measurement in highly mobile millimeter-wave UAV links, but the complementary value of visual and position-derived representations and their behavior under modality degradation require further investigation. This paper develops a staged multimodal framework for current-beam prediction using real-world UAV measurements. The proposed 32-beam classifier combines an ImageNet-pretrained EfficientNet-B3 visual encoder with two deterministic position-derived representations: an explicit Geometric-Kinematic vector and a nonlinear synthetic feature basis constructed from position. The image and synthetic representations are fused first, followed by late fusion with the geometry representation. Experiments on DeepSense 6G Scenario 23 show that Image-Synthetic fusion achieves 86.92% Top-1, 99.03% Top-3, and 99.56% Top-5 accuracy, improving Top-1 performance by 2.64 percentage points over image-only inference and outperforming the 60.71% Top-1 accuracy of synthetic-only inference. Adding the Geometric-Kinematic branch yields the highest measured performance, reaching 87.14% Top-1, 99.12% Top-3, and 99.60% Top-5 accuracy. Controlled input interventions further demonstrate complementary behavior under visual degradation and strong sensitivity to severe synthetic-input corruption. Position-derived nonlinear features provide complementary information to visual context and improve current-beam prediction in the evaluated real-world UAV setting.
