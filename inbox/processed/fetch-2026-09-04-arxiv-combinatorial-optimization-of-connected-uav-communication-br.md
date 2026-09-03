---
title: "Combinatorial optimization of connected UAV communication bridges for emergency response"
created: 2026-09-04
captured: 2026-09-04
type: paper
domain: comms-protocol
source: http://arxiv.org/abs/2609.02562v1
authors: "Matteo Vandelli, Daniele Dragoni"
published: "2026-09-02"
tags: [drone, comms-protocol, paper, arxiv]
---

# Combinatorial optimization of connected UAV communication bridges for emergency response

**Authors**: Matteo Vandelli, Daniele Dragoni
**Published**: 2026-09-02
**arXiv**: http://arxiv.org/abs/2609.02562v1

## Abstract

We present a combinatorial optimization problem for the strategic deployment of UAVs equipped with 5G antennas to assist rescue operations in regions hit by natural disasters. Our goal is to optimize the placement of UAVs to provide coverage in flying ad-hoc networks among given candidate sites. Our formulation aims to maximize signal coverage and minimize interference while ensuring network connectivity. To mitigate interference effects, we incorporate the use of multiple frequencies. We formulate this problem as an integer quadratic program (IQP). We present numerical solutions obtained via the CPLEX solver and conduct a preliminary analysis of the problem's scalability in realistic network configurations. Our findings reveal a significant exponential increase in Time-to-Solution (TTS) as the number of sites grows, which poses a critical challenge in urgent, time-sensitive scenarios. To address this issue, approximate suboptimal solutions can be produced by enforcing a time limit on the solver. Although these solutions are not optimal, they preserve connectivity in most cases, providing a practical trade-off between solution quality and computational times that remain within feasible limits for real-time UAV redeployment. Recognizing the limitations of classical solvers in these contexts, we explore quantum computing as a promising alternative. Specifically, we reformulate the problem as a quadratic unconstrained binary optimization (QUBO) problem, suitable for most quantum algorithms. Through high-performance computing emulation, we show that the quantum adiabatic algorithm (QAA) can accurately solve small-scale instances, paving the way for future application of quantum computing to large-scale, time-critical optimization problems in disaster response.
