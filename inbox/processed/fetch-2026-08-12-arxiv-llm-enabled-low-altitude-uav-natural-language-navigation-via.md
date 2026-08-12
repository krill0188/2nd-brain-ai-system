---
title: "LLM-Enabled Low-Altitude UAV Natural Language Navigation via Signal Temporal Logic Specification Translation and Repair"
created: 2026-08-12
captured: 2026-08-12
type: paper
domain: voice-control
source: http://arxiv.org/abs/2603.27583v1
authors: "Yuqi Ping, Huahao Ding, Tianhao Liang, Longyu Zhou, Guangyu Lei, Xinglin Chen, Junwei Wu, Jieyu Zhou, Tingting Zhang"
published: "2026-03-29"
tags: [drone, voice-control, paper, arxiv]
---

# LLM-Enabled Low-Altitude UAV Natural Language Navigation via Signal Temporal Logic Specification Translation and Repair

**Authors**: Yuqi Ping, Huahao Ding, Tianhao Liang, Longyu Zhou, Guangyu Lei, Xinglin Chen, Junwei Wu, Jieyu Zhou, Tingting Zhang
**Published**: 2026-03-29
**arXiv**: http://arxiv.org/abs/2603.27583v1

## Abstract

Natural language (NL) navigation for low-altitude unmanned aerial vehicles (UAVs) offers an intelligent and convenient solution for low-altitude aerial services by enabling an intuitive interface for non-expert operators. However, deploying this capability in urban environments necessitates the precise grounding of underspecified instructions into safety-critical, dynamically feasible motion plans subject to spatiotemporal constraints. To address this challenge, we propose a unified framework that translates NL instructions into Signal Temporal Logic (STL) specifications and subsequently synthesizes trajectories via mixed-integer linear programming (MILP). Specifically, to generate executable STL formulas from free-form NL, we develop a reasoning-enhanced large language model (LLM) leveraging chain-of-thought (CoT) supervision and group-relative policy optimization (GRPO), which ensures high syntactic validity and semantic consistency. Furthermore, to resolve infeasibilities induced by stringent logical or spatial requirements, we introduce a specification repair mechanism. This module combines MILP-based diagnosis with LLM-guided semantic reasoning to selectively relax task constraints while strictly enforcing safety guarantees. Extensive simulations and real-world flight experiments demonstrate that the proposed closed-loop framework significantly improves NL-to-STL translation robustness, enabling safe, interpretable, and adaptable UAV navigation in complex scenarios.
