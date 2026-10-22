---
title: "Coverage-Preserving Self-Healing in Partially Observable 3D UAV Swarm Networks via an Advection-Diffusion Graph Transformer"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Jiao, Dongbin; Li, Zhihao; Geng, Zongsheng; Zhao, Dongdong; Liu, Shengcai; Yan, Shi"
year: "2026"
doi: "10.48550/arXiv.2610.22085"
url: "http://arxiv.org/abs/2610.22085v1"
zotero_key: 58EF2TCS
tags: ["auto:2nd-brain"]
sha256: efb201ebba55c534
---

# Coverage-Preserving Self-Healing in Partially Observable 3D UAV Swarm Networks via an Advection-Diffusion Graph Transformer

**Authors**: Jiao, Dongbin; Li, Zhihao; Geng, Zongsheng; Zhao, Dongdong; Liu, Shengcai; Yan, Shi  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2610.22085  
**URL**: http://arxiv.org/abs/2610.22085v1

## Abstract

This paper investigates the resilience and self-healing of unmanned aerial vehicle swarm communication networks under severe network partitioning in complex and adversarial environments. To address limited global observability after damage, we develop a damage-state inference mechanism that enables the ground control station (GCS) to infer global failures from sparse local reports without transmitting location-sensitive coordinates. To recover multi-cluster partitioned topologies, we then propose AdDiff-GT, a physics-inspired graph Transformer that incorporates advection-diffusion dynamics into a node-supernode hybrid graph. Local message propagation captures intra-cluster structural relationships, while global attention models inter-cluster interactions. A weighted composite loss jointly considers connectivity restoration, maneuvering cost, motion consistency, inter-cluster coordination, and spatial preservation during model training. We further develop a meta-learning strategy for transferable initialization across damage patterns and swarm scales, enabling efficient online GCS adaptation and distributed airborne inference. Simulations on 8,000 partitioned scenarios, including 5,000 large-scale cases, show that AdDiff-GT achieves effective topology recovery and spatial preservation over six representative baselines. Meta-learning reduces online planning overhead with a minor increase in recovery steps, balancing prior knowledge transfer and online adaptation.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
