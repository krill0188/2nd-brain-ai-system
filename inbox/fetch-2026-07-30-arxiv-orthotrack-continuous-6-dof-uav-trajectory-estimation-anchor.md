---
title: "OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2606.25245v2
authors: "Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier, Olaf Wysocki, Marc Pollefeys, Daniel Cremers"
published: "2026-06-24"
tags: [drone, ai-autonomy, paper, arxiv]
---

# OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos

**Authors**: Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier, Olaf Wysocki, Marc Pollefeys, Daniel Cremers
**Published**: 2026-06-24
**arXiv**: http://arxiv.org/abs/2606.25245v2

## Abstract

Continuous 6-DoF pose estimation is essential for autonomous UAV operations. Yet, existing visual odometry and SLAM methods accumulate drift and yield only relative, up-to-scale trajectories. Single-frame geo-localization, in turn, discards temporal continuity and remains too slow for real-time use. We present OrthoTrack, a training-free system that estimates continuous 6-DoF UAV trajectories using only publicly available orthophotos and surface models as a map prior. OrthoTrack matches keyframes against the orthophoto and lifts correspondences to metric 3D via the surface model. It then propagates these map-anchored correspondences to intermediate frames with optical flow, producing absolute, metrically scaled poses at every frame without GPS or post-hoc alignment. We also introduce the MovingDrone Dataset, a large-scale benchmark pairing photorealistic UAV sequences with dense 6-DoF ground truth and co-registered multi-modal geodata including multi-temporal orthophotos. On MovingDrone and real-world benchmarks, OrthoTrack runs in real time on a single GPU. It outperforms all baselines by a large margin, even those receiving oracle scale and alignment. By relying on publicly available geodata, OrthoTrack enables deployment to new regions without site-specific adaptation.
