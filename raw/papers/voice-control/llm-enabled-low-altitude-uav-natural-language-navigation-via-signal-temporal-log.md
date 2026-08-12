---
title: "LLM-Enabled Low-Altitude UAV Natural Language Navigation via Signal Temporal Logic Specification Translation and Repair"
created: 2026-08-12
updated: 2026-08-12
type: paper
item_type: preprint
authors: "Ping, Yuqi; Ding, Huahao; Liang, Tianhao; Zhou, Longyu; Lei, Guangyu; Chen, Xinglin; Wu, Junwei; Zhou, Jieyu; Zhang, Tingting"
year: "2026"
doi: "10.48550/arXiv.2603.27583"
url: "http://arxiv.org/abs/2603.27583v1"
zotero_key: VN6EXCC8
tags: ["auto:2nd-brain", "voice-control"]
attachment_path: raw/papers/files/voice-control/llm-enabled-low-altitude-uav-natural-language-navigation-via-signal-temporal-log.pdf
attachment_sha256: 97ba07996843a1a7b47fcc157d08fa90b5649cb2b2ebe2cd04db7d3d645eb380
sha256: 818606859c502129
---

# LLM-Enabled Low-Altitude UAV Natural Language Navigation via Signal Temporal Logic Specification Translation and Repair

**Authors**: Ping, Yuqi; Ding, Huahao; Liang, Tianhao; Zhou, Longyu; Lei, Guangyu; Chen, Xinglin; Wu, Junwei; Zhou, Jieyu; Zhang, Tingting  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2603.27583  
**URL**: http://arxiv.org/abs/2603.27583v1

## Abstract

Natural language (NL) navigation for low-altitude unmanned aerial vehicles (UAVs) offers an intelligent and convenient solution for low-altitude aerial services by enabling an intuitive interface for non-expert operators. However, deploying this capability in urban environments necessitates the precise grounding of underspecified instructions into safety-critical, dynamically feasible motion plans subject to spatiotemporal constraints. To address this challenge, we propose a unified framework that translates NL instructions into Signal Temporal Logic (STL) specifications and subsequently synthesizes trajectories via mixed-integer linear programming (MILP). Specifically, to generate executable STL formulas from free-form NL, we develop a reasoning-enhanced large language model (LLM) leveraging chain-of-thought (CoT) supervision and group-relative policy optimization (GRPO), which ensures high syntactic validity and semantic consistency. Furthermore, to resolve infeasibilities induced by stringent logical or spatial requirements, we introduce a specification repair mechanism. This module combines MILP-based diagnosis with LLM-guided semantic reasoning to selectively relax task constraints while strictly enforcing safety guarantees. Extensive simulations and real-world flight experiments demonstrate that the proposed closed-loop framework significantly improves NL-to-STL translation robustness, enabling safe, interpretable, and adaptable UAV navigation in complex scenarios.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
