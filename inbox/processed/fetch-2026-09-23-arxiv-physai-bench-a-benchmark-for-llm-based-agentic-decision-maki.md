---
title: "PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI"
created: 2026-09-23
captured: 2026-09-23
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2609.23695v1
authors: "Mohamed Amine Ferrag, Merouane Debbah, Abderrahmane Lakas, Manu Perumkunnil, Norbert Tihanyi"
published: "2026-09-20"
tags: [drone, ai-autonomy, paper, arxiv]
---

# PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI

**Authors**: Mohamed Amine Ferrag, Merouane Debbah, Abderrahmane Lakas, Manu Perumkunnil, Norbert Tihanyi
**Published**: 2026-09-20
**arXiv**: http://arxiv.org/abs/2609.23695v1

## Abstract

Recent advances in Physical AI have accelerated the use of foundation models in autonomous systems such as unmanned aerial vehicles (UAVs), which must perceive, reason, plan, and act in dynamic environments. Existing benchmarks assess physical perception, intuitive physics, embodied navigation, and collaborative reasoning, but rarely evaluate the agentic decision-making required for reliable autonomy. We introduce \textit{PhysAI-Bench}, a benchmark for evaluating this capability. It contains 10,178 standardized decision instances automatically extracted from conversational traces of autonomous UAV missions. Each instance preserves mission context, temporal dependencies, physical constraints, Model Context Protocol (MCP) tool calls, Agent-to-Agent (A2A) interactions, sensor observations, and AI-native 6G network conditions, including latency, packet loss, throughput, edge load, and network slicing. We expose only information preceding each decision, preventing future-event leakage and approximating online decision-making. We evaluate 29 foundation models using a two-stage protocol. We select model-specific configurations from 12 combinations of zero-, three-, and five-shot prompting and four temperatures, tested in three runs on a 35-instance, human-verified development set. We then freeze each selected configuration and evaluate it in three runs on a fixed, episode-disjoint set of 500 instances. GPT-5.3 achieves the highest accuracy (52.00%), followed by GPT-5.2 (49.40%) and Grok~4.5 (49.07%). Few-shot prompting generally improves performance, while temperature has limited influence. The results demonstrate that reliable agentic decision-making in Physical AI remains an open challenge. The dataset is available at https://github.com/maferrag/physai-bench
