---
title: "SLEI3D: Simultaneous Exploration and Inspection via Heterogeneous Fleets under Limited Communication"
created: 2026-08-20
captured: 2026-08-20
type: paper
domain: gcs-software
source: http://arxiv.org/abs/2601.00163v1
authors: "Junfeng Chen, Yuxiao Zhu, Xintong Zhang, Bing Luo, Meng Guo"
published: "2026-01-01"
tags: [drone, gcs-software, paper, arxiv]
---

# SLEI3D: Simultaneous Exploration and Inspection via Heterogeneous Fleets under Limited Communication

**Authors**: Junfeng Chen, Yuxiao Zhu, Xintong Zhang, Bing Luo, Meng Guo
**Published**: 2026-01-01
**arXiv**: http://arxiv.org/abs/2601.00163v1

## Abstract

Robotic fleets such as unmanned aerial and ground vehicles have been widely used for routine inspections of static environments, where the areas of interest are known and planned in advance. However, in many applications, such areas of interest are unknown and should be identified online during exploration. Thus, this paper considers the problem of simultaneous exploration, inspection of unknown environments and then real-time communication to a mobile ground control station to report the findings. The heterogeneous robots are equipped with different sensors, e.g., long-range lidars for fast exploration and close-range cameras for detailed inspection. Furthermore, global communication is often unavailable in such environments, where the robots can only communicate with each other via ad-hoc wireless networks when they are in close proximity and free of obstruction. This work proposes a novel planning and coordination framework (SLEI3D) that integrates the online strategies for collaborative 3D exploration, adaptive inspection and timely communication (via the intermit-tent or proactive protocols). To account for uncertainties w.r.t. the number and location of features, a multi-layer and multi-rate planning mechanism is developed for inter-and-intra robot subgroups, to actively meet and coordinate their local plans. The proposed framework is validated extensively via high-fidelity simulations of numerous large-scale missions with up to 48 robots and 384 thousand cubic meters. Hardware experiments of 7 robots are also conducted. Project website is available at https://junfengchen-robotics.github.io/SLEI3D/.
