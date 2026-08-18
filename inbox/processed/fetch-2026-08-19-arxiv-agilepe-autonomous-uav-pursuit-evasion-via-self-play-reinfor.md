---
title: "AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2608.14135v1
authors: "Wenhao Tang, Tianyang Chen, Zhejun Cui, Boyuan An, Jiayu Chen, Ruize Zhang, Huidong Liu, Tianyue Wu, Qingmin Liao, Fei Gao, Yu Wang, Chao Yu"
published: "2026-08-14"
tags: [drone, ai-autonomy, paper, arxiv]
---

# AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning

**Authors**: Wenhao Tang, Tianyang Chen, Zhejun Cui, Boyuan An, Jiayu Chen, Ruize Zhang, Huidong Liu, Tianyue Wu, Qingmin Liao, Fei Gao, Yu Wang, Chao Yu
**Published**: 2026-08-14
**arXiv**: http://arxiv.org/abs/2608.14135v1

## Abstract

Autonomous pursuit-evasion is a fundamental challenge for Unmanned Aerial Vehicles (UAVs), requiring rapid decision-making under tightly coupled dynamics and continuously changing opponent behaviors. Traditional rule-based or differential-game approaches often struggle with high-dimensional aerial interactions and agile maneuvering. We present AgilePE, a complete system for autonomous UAV pursuit-evasion via self-play reinforcement learning. AgilePE integrates agile low-level control, competitive policy optimization, and sim-to-real deployment in a unified framework. The policy directly maps onboard state observations to Collective Thrust and Body Rates (CTBR) commands, enabling end-to-end agile maneuvering without intermediate trajectory planners or waypoint controllers. For training, we use competitive self-play with Prioritized Fictitious Self-Play (PFSP) and a diversified opponent pool, enabling agents to improve against historical policies while stabilizing optimization and reducing policy oscillation. This process leads to the emergence of sophisticated pursuit and evasion strategies. For real-world deployment, we develop a hardware-aligned simulation pipeline that models actuator-response dynamics, communication latency, and domain randomization. The learned policies transfer zero-shot to real quadrotors without task-specific tuning. Real-world experiments reproduce pursuit-evasion tactics observed in simulation, including rapid dodging and flanking, and demonstrate interactive two-agent zero-shot deployment.
