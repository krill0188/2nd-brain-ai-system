---
title: "RT-DETR++ for UAV Object Detection"
created: 2026-08-23
updated: 2026-08-23
type: concept
tags: [drone, ai-autonomy, computer-vision, detr, transformer]
sources: [inbox/fetch-2026-08-23-arxiv-rt-detr-for-uav-object-detection.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# RT-DETR++ for UAV Object Detection

ArXiv paper (2025-09-11) introducing RT-DETR++ with enhanced encoder for UAV imagery object detection.

## Challenges in UAV Object Detection

- Densely packed small objects
- Scale variations
- Occlusion

## Key Improvements

### Channel-Gated Attention-based Upsampling/Downsampling (AU/AD)

- Dual-path system minimizing errors
- Preserves details during feature layer propagation

### CSP-PAC Feature Fusion

- Parallel hollow convolutions processing local and contextual information
- Facilitates multi-scale feature integration within the same layer

## Performance

- Superior detection of small and densely packed objects
- Maintains real-time detection speed
- No increase in computational complexity

## Related

- [[computer-vision-drone]] — Drone computer vision applications
- [[yolo]] — YOLO detection architecture
- [[pt-detr-small-target-detection]] — RT-DETR for small target detection

## 📰 최근 관련 소식
- RT-DETR++ for UAV Object Detection (arxiv.org, 2025-09-11) — http://arxiv.org/abs/2509.09157v1
