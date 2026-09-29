---
title: "Vision-Language Models as copilots for Autonomous UAV Navigation: Analysis of Latency and Reliability in Degraded Environments"
created: 2026-09-24
captured: 2026-09-24
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2609.26084v1
authors: "Hiago Sodre, Sebastian Barcelona, Vincent Sandin, Pablo Moraes, Ahilen Mazondo, Igor Nunes, William Moraes, Andr\u00e9 Kelbouscas, Ricardo Grando"
published: "2026-08-10"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Vision-Language Models as copilots for Autonomous UAV Navigation: Analysis of Latency and Reliability in Degraded Environments

**Authors**: Hiago Sodre, Sebastian Barcelona, Vincent Sandin, Pablo Moraes, Ahilen Mazondo, Igor Nunes, William Moraes, André Kelbouscas, Ricardo Grando
**Published**: 2026-08-10
**arXiv**: http://arxiv.org/abs/2609.26084v1

## Abstract

The integration of Vision-Language Models (VLMs) in autonomous Unmanned Aerial Vehicles (UAVs) offers unprecedented semantic reasoning capabilities. However, real-time closed-loop navigation requires not only low inference latency but also obedience to structured flight commands. This paper proposes a hybrid FSM-VLM control architecture for UAVs in GPS-free environments. The system combines a deterministic Finite State Machine (FSM) for low-level physical control with an asynchronous VLM copilot for high-level semantic pathfinding. We evaluate three models with different parameter scales in a Software-In-The-Loop (SITL) simulation. The framework isolates and measures syntax errors at the format level versus semantic hallucinations at the logic level in a normal and degraded scenario. This study demonstrates that parameter scaling, and not pure latency, remains the primary bottleneck for the safe and compatible integration of VLM into autonomous flights.
