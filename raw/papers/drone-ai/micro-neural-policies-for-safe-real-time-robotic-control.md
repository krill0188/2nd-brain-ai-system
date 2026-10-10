---
title: "Micro Neural Policies for Safe Real-Time Robotic Control"
created: 2026-10-10
updated: 2026-10-10
type: paper
item_type: preprint
authors: "Cao, Hongpeng; Curcio, Riccardo; Ottaviano, Daniele; Caccamo, Marco"
year: "2026"
doi: "10.48550/arXiv.2610.08541"
url: "http://arxiv.org/abs/2610.08541v1"
zotero_key: QINAHB4A
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/micro-neural-policies-for-safe-real-time-robotic-control.pdf
attachment_sha256: 0644451708aa60ea4b0e4c5b78def3bf3f22f90a1d44584f6e5f8b2cb94d5442
sha256: 8e6b985dd2a12e72
---

# Micro Neural Policies for Safe Real-Time Robotic Control

**Authors**: Cao, Hongpeng; Curcio, Riccardo; Ottaviano, Daniele; Caccamo, Marco  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2610.08541  
**URL**: http://arxiv.org/abs/2610.08541v1

## Abstract

In this paper, we investigate the synthesis of Micro Neural Policies (MNP) to enable safe and robust real-time robotic control on computationally constrained embedded devices. We demonstrate that integrating Evolution Strategy (ES) and Statistical Model Checking (SMC)-based verification for policy search can drastically reduce neural network size without compromising safety and robustness. We conduct a large-scale training and evaluation of MNP on Cartpole and Quadrotor control tasks, varying control frequencies and network architectures. After validating these policies in simulation, we evaluate their deployability through zero-shot transfer to physical systems. Our experiments show that MNP can successfully achieve safe sim-to-real transfer without sacrificing control performance. We then show that the policies' memory footprint, ranging from 0.5 to 7.5 kB, allows deployment on microcontrollers, where they achieve real-time inference latency with under 25 ns of jitter while leaving the chip idle for over 97% of the time for additional workloads. This makes them a highly practical solution for severely resource-constrained robotic systems.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
