---
title: "Towards Effcient Low Altitude Sensing: A Dual Heterogeneous Graph Learning Method for UAV Task Allocation"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2607.04255v1
authors: "Guangyu Lei, Tianhao Liang, Bingyan Xie, Tingting Zhang"
published: "2026-07-05"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Towards Effcient Low Altitude Sensing: A Dual Heterogeneous Graph Learning Method for UAV Task Allocation

**Authors**: Guangyu Lei, Tianhao Liang, Bingyan Xie, Tingting Zhang
**Published**: 2026-07-05
**arXiv**: http://arxiv.org/abs/2607.04255v1

## Abstract

With the development of low altitude intelligent systems, multiple unmanned aerial vehicles (UAVs) can collaboratively execute more complex tasks. Conventional task allocation methods usually regard tasks and UAVs as isolated entities, making it difficult to capture task dependencies and UAV communication relationships. To address this issue, this paper proposes a dual heterogeneous graph learning based UAV task allocation method. A directed task graph is constructed to represent task dependencies and encode task resource requirements, while an undirected UAV communication graph is built to model communication relationships and encode UAV resource states. The task allocation problem is formulated as a structural matching problem between the task graph and the UAV communication graph. A graph attention network based feature extraction method is introduced to learn structural representations from both graphs through message passing. A cross attention mechanism is further integrated with proximal policy optimization to optimize the matching between task nodes and UAV nodes for task allocation. Simulation results demonstrate that the proposed method achieves a higher task completion rate and shorter task completion time than benchmark methods under different evaluation settings. Furthermore, a UAV sensing and computing application is developed on the AirSim simulation platform. A large language model is employed to convert natural language task requirements into a structured task graph for autonomous UAV task execution, demonstrating the potential of the proposed framework for natural language driven UAV mission planning and execution.
