---
title: "Coverage-Preserving Self-Healing in Partially Observable 3D UAV Swarm Networks via an Advection-Diffusion Graph Transformer"
created: 2026-10-17
captured: 2026-10-17
type: paper
domain: gcs-software
source: http://arxiv.org/abs/2610.22085v1
authors: "Dongbin Jiao, Zhihao Li, Zongsheng Geng, Dongdong Zhao, Shengcai Liu, Shi Yan"
published: "2026-10-15"
tags: [drone, gcs-software, paper, arxiv]
attachment_path: raw/papers/files/gcs-software/coverage-preserving-self-healing-in-partially-observable-3d-.html
attachment_type: html
attachment_sha256: 7205f282220b7a209e3d2862915efc10fd99307173b97cd99b78bea74c6296ca
---

# Coverage-Preserving Self-Healing in Partially Observable 3D UAV Swarm Networks via an Advection-Diffusion Graph Transformer

**Authors**: Dongbin Jiao, Zhihao Li, Zongsheng Geng, Dongdong Zhao, Shengcai Liu, Shi Yan
**Published**: 2026-10-15
**arXiv**: http://arxiv.org/abs/2610.22085v1

## Abstract

This paper investigates the resilience and self-healing of unmanned aerial vehicle swarm communication networks under severe network partitioning in complex and adversarial environments. To address limited global observability after damage, we develop a damage-state inference mechanism that enables the ground control station (GCS) to infer global failures from sparse local reports without transmitting location-sensitive coordinates. To recover multi-cluster partitioned topologies, we then propose AdDiff-GT, a physics-inspired graph Transformer that incorporates advection-diffusion dynamics into a node-supernode hybrid graph. Local message propagation captures intra-cluster structural relationships, while global attention models inter-cluster interactions. A weighted composite loss jointly considers connectivity restoration, maneuvering cost, motion consistency, inter-cluster coordination, and spatial preservation during model training. We further develop a meta-learning strategy for transferable initialization across damage patterns and swarm scales, enabling efficient online GCS adaptation and distributed airborne inference. Simulations on 8,000 partitioned scenarios, including 5,000 large-scale cases, show that AdDiff-GT achieves effective topology recovery and spatial preservation over six representative baselines. Meta-learning reduces online planning overhead with a minor increase in recovery steps, balancing prior knowledge transfer and online adaptation.
