---
title: "Say the Mission, Execute the Swarm: Agent-Enhanced LLM Reasoning in the Web-of-Drones"
created: 2026-08-19
updated: 2026-08-19
type: paper
item_type: preprint
authors: "Iannoli, Andrea; Gigli, Lorenzo; Sciullo, Luca; Trotta, Angelo; Felice, Marco Di"
year: "2026"
doi: "10.48550/arXiv.2605.03788"
url: "http://arxiv.org/abs/2605.03788v1"
zotero_key: X3H7CFPH
tags: ["auto:2nd-brain", "swarm"]
attachment_path: raw/papers/files/swarm/say-the-mission-execute-the-swarm-agent-enhanced-llm-reasoning-in-the-web-of-dro.pdf
attachment_sha256: 5ef40b01b231f48ad697afd33b8d7e546e0f0de800b1d61dbe0885856d6cf6c4
sha256: e583001df6ad2568
---

# Say the Mission, Execute the Swarm: Agent-Enhanced LLM Reasoning in the Web-of-Drones

**Authors**: Iannoli, Andrea; Gigli, Lorenzo; Sciullo, Luca; Trotta, Angelo; Felice, Marco Di  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2605.03788  
**URL**: http://arxiv.org/abs/2605.03788v1

## Abstract

Large Language Models (LLMs) are increasingly explored as high-level reasoning engines for cyber-physical systems, yet their application to real-time UAV swarm management remains challenging due to heterogeneous interfaces, limited grounding, and the need for long-running closed-loop execution. This paper presents a mission-agnostic, agent-enhanced LLM framework for UAV swarm control, where users express mission objectives in natural language and the system autonomously executes them through grounded, real-time interactions. The proposed architecture combines an LLM-based Agent Core with a Model Context Protocol (MCP) gateway and a Web-of-Drones abstraction based on W3C Web of Things (WoT) standards. By exposing drones, sensors, and services as standardized WoT Things, the framework enables structured tool-based interaction, continuous state observation, and safe actuation without relying on code generation. We evaluate the framework using ArduPilot-based simulation across four swarm missions and six state-of-the-art LLMs. Results show that, despite strong reasoning abilities, current general-purpose LLMs still struggle to achieve reliable execution - even for simple swarm tasks - when operating without explicit grounding and execution support. Task-specific planning tools and runtime guardrails substantially improve robustness, while token consumption alone is not indicative of execution quality or reliability.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
