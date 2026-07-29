---
title: "Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2607.22145v1
authors: "Alvaro J. Gaona, David Perez-Saura, Francisco J. Anguita, Pascual Campoy"
published: "2026-07-24"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms

**Authors**: Alvaro J. Gaona, David Perez-Saura, Francisco J. Anguita, Pascual Campoy
**Published**: 2026-07-24
**arXiv**: http://arxiv.org/abs/2607.22145v1

## Abstract

Open-source LiDAR-inertial odometry (LIO) systems have achieved remarkable benchmark accuracy, yet current state-of-the-art implementations are primarily optimized for evaluation performance rather than the requirements of real-time closed-loop aerial control. When deployed onboard UAVs, this can introduce limitations that degrade flight performance. In this work, we identify five architectural deficiencies in a representative tightly coupled IESKF-based LIO implementation: odometry publishing tied to the LiDAR rate (10 Hz instead of the IMU's 200 Hz), missing velocity outputs, execution bottlenecks that block IMU processing, mutex contention, and synchronization race conditions. We introduce corresponding modifications including IMU-rate forward propagation, direct body-frame velocity publishing, SLERP-based smoothing, dual-executor isolation, and explicit synchronization protection. The resulting system increases odometry output from ~10 Hz to a stable 200 Hz, provides a complete Twist state at every IMU sample, and preserves continuity during transient LiDAR loss. Experiments on a Livox Mid-360 / Pixhawk 4 Mini autonomous UAV with motion-capture ground truth validate the approach. Since the underlying estimator (IESKF + ikd-Tree) remains unchanged, the proposed improvements can be directly applied to FAST-LIO2-derived implementations.
