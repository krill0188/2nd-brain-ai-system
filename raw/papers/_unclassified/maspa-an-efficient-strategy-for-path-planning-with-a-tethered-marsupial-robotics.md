---
title: "MASPA: An efficient strategy for path planning with a tethered marsupial robotics system"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Capit\u00e1n, Jes\u00fas; D\u00edaz-B\u00e1\u00f1ez, Jos\u00e9 M.; P\u00e9rez-Cuti\u00f1o, Miguel A.; Rodr\u00edguez, Fabio; Ventura, Inmaculada"
year: "2024"
doi: "10.48550/arXiv.2408.02141"
url: "http://arxiv.org/abs/2408.02141v3"
zotero_key: U4FVUNP5
tags: ["auto:2nd-brain"]
sha256: 6b06cf59b3e75425
---

# MASPA: An efficient strategy for path planning with a tethered marsupial robotics system

**Authors**: Capitán, Jesús; Díaz-Báñez, José M.; Pérez-Cutiño, Miguel A.; Rodríguez, Fabio; Ventura, Inmaculada  
**Year**: 2024  
**DOI**: 10.48550/arXiv.2408.02141  
**URL**: http://arxiv.org/abs/2408.02141v3

## Abstract

A tethered marsupial robotics system comprises three components: an Unmanned Ground Vehicle (UGV), an Unmanned Aerial Vehicle (UAV), and a tether connecting both robots. Marsupial systems are highly beneficial in industry as they extend the UAV's battery life during flight. This paper introduces a novel strategy for a specific path planning problem in marsupial systems, where each of the three components must avoid collisions with ground and aerial obstacles modeled as 3D cuboids. Given an initial configuration in which the UAV is positioned atop the UGV, the goal is to reach an aerial target with the UAV. We assume that the UGV first moves to a position from which the UAV can take off and fly through a vertical plane to reach an aerial target. We propose an approach that discretizes the space to approximate an optimal solution, minimizing the sum of the lengths of the ground and air paths. First, we assume a taut tether and use a novel algorithm that leverages the convexity of the tether and the geometry of obstacles to efficiently determine the locus of feasible take-off points for the UAV. We then apply this result to scenarios that involve loose tethers. The simulation test results show that our approach can solve complex situations in seconds, outperforming a baseline planning algorithm based on RRT* (Rapidly exploring Random Trees).

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
