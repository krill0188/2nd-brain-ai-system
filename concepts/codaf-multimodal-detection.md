---
title: "CoDAF: Cross-modal Offset-guided Dynamic Alignment and Fusion"
created: 2026-08-24
updated: 2026-08-24
type: concept
tags: [drone, ai-autonomy, computer-vision, multimodal, yolo]
sources: [inbox/fetch-2026-08-24-arxiv-cross-modal-offset-guided-dynamic-alignment-and-fusion-for-w.md]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# CoDAF: Cross-modal Offset-guided Dynamic Alignment and Fusion

CoDAF is a unified framework for weakly aligned UAV-based object detection that jointly addresses spatial misalignment between RGB and infrared imagery through offset-guided semantic alignment and dynamic attention-guided fusion.

## Problem Statement

UAV platform motion and asynchronous imaging cause spatial misalignment between visible (RGB) and infrared (IR) modalities, leading to:
- Semantic inconsistency at corresponding spatial locations
- Modality conflict during feature fusion

## Architecture

### Offset-guided Semantic Alignment (OSA)
- Estimates attention-based spatial offsets
- Uses deformable convolution guided by shared semantic space
- Precisely aligns features across modalities

### Dynamic Attention-guided Fusion Module (DAFM)
- Adaptively balances modality contributions through gating
- Refines fused features via spatial-channel dual attention
- Integrates alignment and fusion in unified design

## Performance

- **Dataset**: DroneVehicle
- **mAP**: 78.6%
- Superior performance over state-of-the-art methods

## Applications

- Environmental monitoring
- Urban security
- Aerial surveillance

## Related Topics

- [[yolo]] — Real-time object detection architecture
- [[computer-vision-drone]] — Drone computer vision systems
- [[rgb-ir-fusion-uav-detection]] — RGB-IR fusion for UAV detection
- [[uavd-mamba-multimodal-detection]] — Multimodal UAV detection

## Source

^[inbox/fetch-2026-08-24-arxiv-cross-modal-offset-guided-dynamic-alignment-and-fusion-for-w.md]

## 📰 최근 관련 소식
- Cross-modal Offset-guided Dynamic Alignment and Fusion for Weakly Aligned UAV Object Detection (arxiv.org, 2025-06-20) — http://arxiv.org/abs/2506.16737v1
- Powerus Secures $22.3 Million Commercial Contract to Protect U.S. Oil Interests and Critical Energy Infrastructure in the Middle East (www.suasnews.com, Fri, 21 Au) — https://www.suasnews.com/2026/08/powerus-secures-22-3-million-commercial-contract-to-protect-u-s-oil-interests-and-critical-energy-infrastructure-in-the-middle-east/
