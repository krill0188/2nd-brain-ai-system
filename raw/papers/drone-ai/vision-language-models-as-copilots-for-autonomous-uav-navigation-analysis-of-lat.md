---
title: "Vision-Language Models as copilots for Autonomous UAV Navigation: Analysis of Latency and Reliability in Degraded Environments"
created: 2026-09-24
updated: 2026-09-24
type: paper
item_type: preprint
authors: "Sodre, Hiago; Barcelona, Sebastian; Sandin, Vincent; Moraes, Pablo; Mazondo, Ahilen; Nunes, Igor; Moraes, William; Kelbouscas, Andr\u00e9; Grando, Ricardo"
year: "2026"
doi: "10.48550/arXiv.2609.26084"
url: "http://arxiv.org/abs/2609.26084v1"
zotero_key: EGS94IXA
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/vision-language-models-as-copilots-for-autonomous-uav-navigation-analysis-of-lat.pdf
attachment_sha256: 1b1c63d1972d2f79b559fb7d67dabc00ca5ce2764d6abbf62f23dc0161034f84
sha256: 8e3130f4c3b97d00
---

# Vision-Language Models as copilots for Autonomous UAV Navigation: Analysis of Latency and Reliability in Degraded Environments

**Authors**: Sodre, Hiago; Barcelona, Sebastian; Sandin, Vincent; Moraes, Pablo; Mazondo, Ahilen; Nunes, Igor; Moraes, William; Kelbouscas, André; Grando, Ricardo  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2609.26084  
**URL**: http://arxiv.org/abs/2609.26084v1

## Abstract

The integration of Vision-Language Models (VLMs) in autonomous Unmanned Aerial Vehicles (UAVs) offers unprecedented semantic reasoning capabilities. However, real-time closed-loop navigation requires not only low inference latency but also obedience to structured flight commands. This paper proposes a hybrid FSM-VLM control architecture for UAVs in GPS-free environments. The system combines a deterministic Finite State Machine (FSM) for low-level physical control with an asynchronous VLM copilot for high-level semantic pathfinding. We evaluate three models with different parameter scales in a Software-In-The-Loop (SITL) simulation. The framework isolates and measures syntax errors at the format level versus semantic hallucinations at the logic level in a normal and degraded scenario. This study demonstrates that parameter scaling, and not pure latency, remains the primary bottleneck for the safe and compatible integration of VLM into autonomous flights.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
