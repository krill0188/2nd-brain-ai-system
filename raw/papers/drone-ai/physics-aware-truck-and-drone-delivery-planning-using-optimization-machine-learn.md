---
title: "Physics-aware Truck and Drone Delivery Planning Using Optimization & Machine Learning"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Sun, Yineng; F\u00fcgenschuh, Armin; Vaze, Vikrant"
year: "2025"
doi: "10.48550/arXiv.2507.16259"
url: "http://arxiv.org/abs/2507.16259v1"
zotero_key: PFJ7Z5GN
tags: ["auto:2nd-brain"]
sha256: 9188d30c3a925b74
---

# Physics-aware Truck and Drone Delivery Planning Using Optimization & Machine Learning

**Authors**: Sun, Yineng; Fügenschuh, Armin; Vaze, Vikrant  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2507.16259  
**URL**: http://arxiv.org/abs/2507.16259v1

## Abstract

Combining an energy-efficient drone with a high-capacity truck for last-mile package delivery can benefit operators and customers by reducing delivery times and environmental impact. However, directly integrating drone flight dynamics into the combinatorially hard truck route planning problem is challenging. Simplified models that ignore drone flight physics can lead to suboptimal delivery plans. We propose an integrated formulation for the joint problem of truck route and drone trajectory planning and a new end-to-end solution approach that combines optimization and machine learning to generate high-quality solutions in practical online runtimes. Our solution method trains neural network predictors based on offline solutions to the drone trajectory optimization problem instances to approximate drone flight times, and uses these approximations to optimize the overall truck-and-drone delivery plan by augmenting an existing order-first-split-second heuristic. Our method explicitly incorporates key kinematics and energy equations in drone trajectory optimization, and thereby outperforms state-of-the-art benchmarks that ignore drone flight physics. Extensive experimentation using synthetic datasets and real-world case studies shows that the integration of drone trajectories into package delivery planning substantially improves system performance in terms of tour duration and drone energy consumption. Our modeling and computational framework can help delivery planners achieve annual savings worth millions of dollars while also benefiting the environment.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
