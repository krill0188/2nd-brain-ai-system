---
title: "WONDER: A Radio World Model-based Negotiation Framework for Multi-Agent UAV Coverage Optimization"
created: 2026-08-20
updated: 2026-08-20
type: paper
item_type: preprint
authors: "Huang, Jiahao; Li, Rongpeng; Zhao, Zhifeng; Ding, Guoru; Zhang, Honggang"
year: "2026"
doi: "10.48550/arXiv.2608.16955"
url: "http://arxiv.org/abs/2608.16955v1"
zotero_key: 6PJGWXE6
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/swarm/wonder-a-radio-world-model-based-negotiation-framework-for-multi-agent-uav-cover.pdf
attachment_sha256: c2bf3ec7781f508d9d3dfdc52d336acdad190d6bea1a104161b07ed26e60701f
sha256: 4bcd2eb26f2bf539
---

# WONDER: A Radio World Model-based Negotiation Framework for Multi-Agent UAV Coverage Optimization

**Authors**: Huang, Jiahao; Li, Rongpeng; Zhao, Zhifeng; Ding, Guoru; Zhang, Honggang  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.16955  
**URL**: http://arxiv.org/abs/2608.16955v1

## Abstract

Post-disaster damage to terrestrial infrastructure can disrupt wireless coverage,while Uncrewed Aerial Vehicle (UAV) swarms provide a promising solution for rapid restoration.However, due to the limitations in local geometry observations hidden radio impact,and inter-UAV communication,there exists a significant gap between locally visible movement choices and swarm-level coverage outcomes.To combat this gap,we propose a raido World-model-based Optimized Negotiation framework for Distributed UAV covERage (WONDER).Particularly, to tackle the unavailability of the future radio field from onboard observations, WONDER uses a Joint-Embedding Predictive Architecture (JEPA)-based radio world model to learn and predict the incremental radio effect of each candidate trajectory from deployment-available information.Multi-round negotiation in WONDER then coordinates ranked proposals by committing one trajectory at a time and re-evaluating the remaining proposals under the updated context. Our theoretical analyses further validate the effectiveness of such a world model-based framework. WONDER also adopts a Proximal Policy Optimization (PPO)-style Actor and alternates between updating the world model and the actor. Furthermore,we build RadioDynamics,a comprehensive simulation environment that integrates UAV mobility,radio propagation, inter-UAV communication modeling,and digital-twin geometry with ray-traced fields in $62$ metropolitan scenes.Experiments on $11$ testing scenes in RadioDynamics show that WONDER achieves the highest balanced score among seven evaluated methods,reaching $0.870$ with a $0.162$ coverage advantage over STACCA, while maintaining $100\%$ connectivity between UAVs.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
