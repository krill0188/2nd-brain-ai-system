---
title: "PATH: Continuous Target Sensing among Autonomous Cooperative Drones"
created: 2026-09-15
updated: 2026-09-15
type: paper
item_type: preprint
authors: "Kim, Heegyeong; James, Alice; Seth, Avishkar; Kuantama, Endrowednes; Williamson, Jane; Feng, Yimeng; Han, Richard"
year: "2026"
doi: "10.48550/arXiv.2609.12456"
url: "http://arxiv.org/abs/2609.12456v1"
zotero_key: D7X4QUCQ
tags: ["auto:2nd-brain"]
sha256: 12a29594e0369fe9
---

# PATH: Continuous Target Sensing among Autonomous Cooperative Drones

**Authors**: Kim, Heegyeong; James, Alice; Seth, Avishkar; Kuantama, Endrowednes; Williamson, Jane; Feng, Yimeng; Han, Richard  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2609.12456  
**URL**: http://arxiv.org/abs/2609.12456v1

## Abstract

Continuous target sensing by uncrewed aerial vehicles (UAVs) is constrained by limited flight endurance, motivating the transfer of tracking responsibility between cooperating UAVs. Such a handoff requires the receiver to identify the same physical target currently tracked by the sender despite differences in viewpoint, scale, and target appearance. Existing approaches based on global target localization or appearance-based cross-view association are limited by positioning uncertainty or ambiguous visual features. This paper presents Perspective Alignment \& Tracking Handoff (\textbf{PATH}), a platform-agnostic, geometry-assisted sensing and verification framework for target handoff between two moving UAVs. The sender reconstructs the tracked target as a metric 3D point using RGB-D sensing, while the receiver estimates its relative pose from a fiducial observation and projects the transmitted target point into its own image as a spatial prior for target acquisition. The receiver-generated candidate is then returned to the sender and verified through a cross-view Mutual Agreement Handshake before tracking responsibility is transferred. Real-world UAV experiments show mean relative-position and target-position errors of 0.047~m and 0.030~m, respectively. Under visually ambiguous conditions, PATH achieves 96.0\% frame-level receiver-side target acquisition accuracy, with 2.0\% false-positive and 2.0\% false-negative rates. A sensor-error sensitivity analysis shows that relative-pose uncertainty is the dominant contributor to receiver-view projection error. The implementation operates at video rate with compact inter-UAV communication below 16~kB/s at 60~Hz, demonstrating the feasibility of lightweight geometry-assisted target handoff on resource-constrained UAV platforms.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
