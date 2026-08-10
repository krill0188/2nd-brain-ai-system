---
title: "Rigid-Covert GNSS Spoofing of UAV Swarms: A Structural Blind Spot, Its Detection Limit, and Absolute-Anchor Defenses"
created: 2026-08-10
updated: 2026-08-10
type: paper
item_type: preprint
authors: "Park, Minseok; Yoo, Joon Soo"
year: "2026"
doi: "10.48550/arXiv.2608.06885"
url: "http://arxiv.org/abs/2608.06885v1"
zotero_key: CTG9FDSD
tags: ["auto:2nd-brain", "swarm"]
attachment_path: raw/papers/files/swarm/rigid-covert-gnss-spoofing-of-uav-swarms-a-structural-blind-spot-its-detection-l.pdf
attachment_sha256: ba78bf1f26c5af2470b56257124e1904ad5cfccf62a2f3a465d0ed40e615f0ba
sha256: c4b8b6361ebe9c61
---

# Rigid-Covert GNSS Spoofing of UAV Swarms: A Structural Blind Spot, Its Detection Limit, and Absolute-Anchor Defenses

**Authors**: Park, Minseok; Yoo, Joon Soo  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.06885  
**URL**: http://arxiv.org/abs/2608.06885v1

## Abstract

Cooperative UAV-swarm defenses commonly cross-check GNSS positions against measured inter-drone geometry. We show that this relative-geometry channel has a structural blind spot: a common, slowly varying translation (a rigid-covert shift, RigidShift) preserves all pairwise distances and is therefore unobservable to any relative-only detector (a gauge-freedom argument). We validate this blindness on distance-verification and semidefinite-feasibility baselines, while explicitly distinguishing it from onboard inertial/GNSS monitors that can raise a bare alarm but cannot recover the swarm's true position. To quantify when an external reference restores observability, we derive the drift-dependent detection floor $2γ/(1-t_s/T)$ for a calibrated anchor-residual detector and empirically identify an additional detector-specific noise floor (measured slope 2.66 vs. predicted 2.67). We then present a centralized anchor-rooted recovery pipeline that reconstructs swarm geometry from inter-drone ranges, aligns it to a trusted-anchor subset with Byzantine-robust fitting, and recovers the absolute positions of non-anchored drones. A segmented estimator jointly estimates anchor drift, attack rate, and onset when no clean-epoch label is available. Across statistical simulations, ArduPilot software-in-the-loop experiments, and Gazebo experiments with rendered vision anchors, the method recovers the positions of non-anchored drones to a median error of 0.39 m (20 seeds) under approximately 10.1 m of GNSS drift, and to 7.1 cm (5 seeds) in the rendered-vision multi-SITL setting. We also characterize the explicit limits imposed by non-collinear anchor geometry, anchor coverage, $τ\to0$ drift-attack aliasing, and majority anchor compromise. All evaluations are simulation-based and use no RF spoofing hardware or physical swarm.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
