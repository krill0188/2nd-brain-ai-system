---
title: "DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control"
created: 2026-10-24
updated: 2026-10-24
type: paper
item_type: preprint
authors: "Li, Fanxing; Huang, Yuxiang; Wang, Shengyang; Sun, Fangyu; Wu, Shuyu; Zhang, Tianbao; Zuo, Dexin; Yufei, Yan; Zou, Danping; Yu, Wenxian"
year: "2026"
doi: "10.48550/arXiv.2610.31617"
url: "http://arxiv.org/abs/2610.31617v1"
zotero_key: PZP3A48T
tags: ["auto:2nd-brain"]
sha256: 6fa53428a5082aab
---

# DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control

**Authors**: Li, Fanxing; Huang, Yuxiang; Wang, Shengyang; Sun, Fangyu; Wu, Shuyu; Zhang, Tianbao; Zuo, Dexin; Yufei, Yan; Zou, Danping; Yu, Wenxian  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2610.31617  
**URL**: http://arxiv.org/abs/2610.31617v1

## Abstract

Tasks such as quadrotor dynamic-gate racing require agents to anticipate external motion while maintaining precise high-frequency control. World-model-based reinforcement learning provides a natural solution by learning latent dynamics for future imagination, yet it often entangles environmental evolution and the robot's own dynamics in a single learned rollout, where model bias can affect policy optimization efficiency. We propose DiffDreamer, a differentiable reinforcement learning framework that tightly couples a learned world model with differentiable simulation for actor optimization. In one optimization step, the learned world model propagates latent states that capture external dynamics and history-dependent features, while the differentiable simulator propagates the robot's explicit physical state. We further decompose the actor objective into a critic-driven pathway for non-differentiable task rewards and a simulator-driven pathway for differentiable motion rewards. Experiments on aggressive tracking and dynamic-gate racing show that DiffDreamer improves training convergence over the model-free, model-based, and differentiable-RL baselines, and final performance over these baselines and classical planning and control methods. Additional experiments assess reward decomposition and the odometry-conditioned relative-state representation through ablations. We also provide proof-of-concept real-world flight experiments for validation.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
