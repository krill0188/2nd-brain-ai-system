---
title: "UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection"
created: 2026-08-23
updated: 2026-08-23
type: concept
tags: [drone, ai-autonomy, computer-vision, mamba, multimodal]
sources: [inbox/fetch-2026-08-23-arxiv-uavd-mamba-deformable-token-fusion-vision-mamba-for-multimod.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# UAVD-Mamba: Multimodal UAV Detection

ArXiv paper (2025-07-01) proposing UAVD-Mamba, a multimodal UAV object detection framework based on Mamba architectures with deformable token fusion.

## Challenges Addressed

UAV object detection faces:
- Occlusions
- Small object sizes
- Irregular shapes

## Architecture

### Deformable Token Mamba Block (DTMB)

- Generates deformable tokens by incorporating adaptive patches from deformable convolutions alongside normal patches
- Improves geometric adaptability

### Multimodal Feature Complementarity

- Two separate DTMBs for RGB and infrared (IR) modalities
- Outputs integrated into Mamba Block for feature extraction
- Fusion Mamba Block for feature fusion

### Multiscale Detection

- Four DTMBs stacked at different scales for multiscale feature representations
- Detection Neck for Mamba (DNM) module inspired by YOLO series
- Modified SPPF and C3K2 from YOLOv11 for multiscale features

### Attention Mechanisms

- Cross-enhanced spatial attention before DTMB
- Cross-channel attention after Fusion Mamba Block

## Results

- Dataset: DroneVehicle
- Performance: +3.6% mAP over baseline OAFA method

## Code

https://github.com/GreatPlum-hnu/UAVD-Mamba.git

## Related

- [[computer-vision-drone]] — Drone computer vision overview
- [[yolo]] — YOLO detection architecture
- [[drone-ai-agents]] — AI agents for drones

## 📰 최근 관련 소식
- UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection (arxiv.org, 2025-07-01) — http://arxiv.org/abs/2507.00849v1
