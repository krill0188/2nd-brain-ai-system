---
title: "SCORE: Shape-Conforming Regions for UAV Flight"
created: 2026-08-19
updated: 2026-08-19
type: concept
domain: ai-autonomy
tags: [drone, ai-autonomy, conformal-prediction, navigation, enclosed-environment, slam]
sources: [inbox/fetch-2026-08-19-arxiv-score-shape-conforming-regions-for-flight-in-enclosed-degrad.md]
confidence: high
contested: false
contradictions: []
---

# SCORE: Shape-Conforming Regions for UAV Flight

Distribution-free shape-conforming keep-out regions for autonomous UAV flight in enclosed, degraded environments using conformal prediction on signed distance fields.

## Problem Statement

Autonomous UAVs entering enclosed environments (caves, collapsed structures) face:
- Confined vehicle maneuvering space
- Degraded perception conditions
- Need for certified obstacle avoidance

Traditional convex keep-out regions bulge into narrow passages and grow as perception degrades.

## Key Innovation

### Nonconformity Score on SDF
- Defines nonconformity score on signed distance field (SDF)
- Produces non-convex keep-out that tightly follows obstacle geometry
- Avoids unnecessary bulging of equal-margin convex regions

## Supporting Components

### 1. Voxelwise Union of Sensor Observations
- Certifies voxels that any single sensor misses
- Complementary sensor fusion at voxel level

### 2. Adaptive Margin
- Margin around obstacle adapts to measured visibility
- No weather labels required
- No online ground-truth feedback needed (unlike single-pass flight)

## Results

- Retains more usable free space than convex baselines at same certified coverage
- Produces safer closed-loop flight
- Validated on real subterranean data

## Related Concepts

- [[micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m]] — SLAM platform comparison
- [[lightweight-safe-rl-uav]] — Dense environment RL navigation
- [[visual-positioning-odometry]] — GPS-denied positioning
- [[neurosymland-landing-assessment]] — Neural-symbolic landing assessment

## Sources

- Kim & Kim, "SCORE: Shape-Conforming Regions for Flight in Enclosed, Degraded Environments", arXiv:2608.15289, 2026-08-15
