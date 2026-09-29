---
title: "OA-MPPI: Occlusion-Aware Model Predictive Path Integral Control for UAV Flight"
created: 2026-09-26
updated: 2026-09-26
type: paper
item_type: preprint
authors: "Palladino, Vittorio; Yang, Teaya; Zhang, Ruiqi; Mueller, Mark W."
year: "2026"
doi: "10.48550/arXiv.2609.28709"
url: "http://arxiv.org/abs/2609.28709v1"
zotero_key: SCQKRVRU
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/_unclassified/oa-mppi-occlusion-aware-model-predictive-path-integral-control-for-uav-flight.pdf
attachment_sha256: dc9966cdf40c2a45d8cfd08245b36703f4eb7c5edad29a5b40cfd15751bdf0f6
sha256: 783f249cf5d15f57
---

# OA-MPPI: Occlusion-Aware Model Predictive Path Integral Control for UAV Flight

**Authors**: Palladino, Vittorio; Yang, Teaya; Zhang, Ruiqi; Mueller, Mark W.  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2609.28709  
**URL**: http://arxiv.org/abs/2609.28709v1

## Abstract

Autonomous UAV flight through cluttered and partially unknown environments requires reasoning not only about observed obstacles but also about occluded regions that the sensor cannot observe. We present OA-MPPI, an obstacle- and occlusion-aware extension of Model Predictive Path Integral (MPPI) control for quadrotor flight that accounts for potential moving agents emerging from these regions into the vehicle's path. At every planning step, we extract a 3D occlusion boundary from the online occupancy map and use it to model the regions that hidden agents could reach over the prediction horizon. We penalize trajectories that enter these expanding regions within MPPI rollouts generated using nonlinear quadrotor dynamics and accounting for individual rotor thrust limits. We validate the proposed approach in simulation and hardware flight experiments, with the complete pipeline running onboard the vehicle in real time. Results show increased clearance from occlusion boundaries compared to baseline MPPI in both settings, as well as avoidance of an agent emerging from occlusion in simulation.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
