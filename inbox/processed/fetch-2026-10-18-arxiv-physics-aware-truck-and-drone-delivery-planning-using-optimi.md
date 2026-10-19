---
title: "Physics-aware Truck and Drone Delivery Planning Using Optimization & Machine Learning"
created: 2026-10-18
captured: 2026-10-18
type: paper
domain: hardware
source: http://arxiv.org/abs/2507.16259v1
authors: "Yineng Sun, Armin F\u00fcgenschuh, Vikrant Vaze"
published: "2025-07-22"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/physics-aware-truck-and-drone-delivery-planning-using-optimi.html
attachment_type: html
attachment_sha256: e29e2325caf92bc86622149218b3cf92647dc27c980e379752cfcf6781a9ea3b
---

# Physics-aware Truck and Drone Delivery Planning Using Optimization & Machine Learning

**Authors**: Yineng Sun, Armin Fügenschuh, Vikrant Vaze
**Published**: 2025-07-22
**arXiv**: http://arxiv.org/abs/2507.16259v1

## Abstract

Combining an energy-efficient drone with a high-capacity truck for last-mile package delivery can benefit operators and customers by reducing delivery times and environmental impact. However, directly integrating drone flight dynamics into the combinatorially hard truck route planning problem is challenging. Simplified models that ignore drone flight physics can lead to suboptimal delivery plans. We propose an integrated formulation for the joint problem of truck route and drone trajectory planning and a new end-to-end solution approach that combines optimization and machine learning to generate high-quality solutions in practical online runtimes. Our solution method trains neural network predictors based on offline solutions to the drone trajectory optimization problem instances to approximate drone flight times, and uses these approximations to optimize the overall truck-and-drone delivery plan by augmenting an existing order-first-split-second heuristic. Our method explicitly incorporates key kinematics and energy equations in drone trajectory optimization, and thereby outperforms state-of-the-art benchmarks that ignore drone flight physics. Extensive experimentation using synthetic datasets and real-world case studies shows that the integration of drone trajectories into package delivery planning substantially improves system performance in terms of tour duration and drone energy consumption. Our modeling and computational framework can help delivery planners achieve annual savings worth millions of dollars while also benefiting the environment.
