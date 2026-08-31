---
title: "WAVE-DETR: Multi-Modal Visible and Acoustic Real-Life Drone Detector"
created: 2026-08-23
updated: 2026-08-23
type: concept
tags: [drone, ai-autonomy, computer-vision, acoustic, multimodal, detr]
sources: [inbox/fetch-2026-08-23-arxiv-wave-detr-multi-modal-visible-and-acoustic-real-life-drone-d.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# WAVE-DETR: Multi-Modal Drone Detector

ArXiv paper (2025-09-11) introducing WAVE-DETR, combining visible RGB and acoustic signals for robust real-life UAV detection.

## Approach

Fuses visual and acoustic features in a unified object detector using:
- Deformable DETR architecture
- Wav2Vec2 acoustic embeddings

## Datasets

- Drone-vs-Bird dataset (existing)
- ARDrone dataset (new, 7,500+ synchronized images and audio segments)

## Fusion Configurations

Four fusion approaches tested:
1. Gated mechanism (best performer)
2. Linear layer
3. MLP
4. Cross attention

## Results

**Gated fusion improvements over Deformable DETR baseline:**
- Small drones: +11.1% to +15.3% mAP (IoU 0.5-0.9)
- Medium and large drones: Enhanced mAP scores
- Overall gains: +3.27% to +5.84% across all drone sizes

## Architecture

- Wav2Vec2 acoustic embeddings fused with multi-resolution feature mappings from Deformable DETR
- Enhances object detection across all drone dimensions

## Related

- [[computer-vision-drone]] — Drone computer vision overview
- [[rt-detr-plus-uav-detection]] — RT-DETR for UAV detection
- [[uav-detr-anti-drone-detection]] — UAV DETR anti-drone detection

## 📰 최근 관련 소식
- WAVE-DETR Multi-Modal Visible and Acoustic Real-Life Drone Detector (arxiv.org, 2025-09-11) — http://arxiv.org/abs/2509.09859v1
