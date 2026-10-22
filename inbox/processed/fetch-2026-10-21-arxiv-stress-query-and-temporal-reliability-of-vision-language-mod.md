---
title: "Stress-Query and Temporal Reliability of Vision-Language Models as copilots in Autonomous UAV Navigation"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2610.23877v1
authors: "Hiago Sodre, Sebastian Barcelona, Vincent Sandin, Pablo Moraes, Andre S. Kelbouscas, Ricardo B. Grando"
published: "2026-09-21"
tags: [drone, ai-autonomy, paper, arxiv]
attachment_path: raw/papers/files/ai-autonomy/stress-query-and-temporal-reliability-of-vision-language-mod.html
attachment_type: html
attachment_sha256: c829393eb23c018d412f239ff4bf500674db904679689dd008d5ec986022575e
---

# Stress-Query and Temporal Reliability of Vision-Language Models as copilots in Autonomous UAV Navigation

**Authors**: Hiago Sodre, Sebastian Barcelona, Vincent Sandin, Pablo Moraes, Andre S. Kelbouscas, Ricardo B. Grando
**Published**: 2026-09-21
**arXiv**: http://arxiv.org/abs/2610.23877v1

## Abstract

Integrating Vision-Language Models (VLMs) into autonomous UAV navigation enables high-level semantic reasoning but introduces critical temporal bottlenecks that can destabilize flight control. This paper presents a systematic benchmark that evaluates the operational trade-offs among model scale, hardware constraints, and flight reliability. By subjecting the system to extensive stress tests on both a high-performance workstation and a constrained integrated-graphics laptop, we isolate the kinetic impact of inference latency against reasoning accuracy. Our findings reveal a performance dichotomy: lightweight models struggle with structural hallucinations that break deterministic state machines, while heavyweight models induce trajectory overcorrections due to inference lag. We demonstrate that a mid-weight architecture strikes the optimal balance, successfully rehabilitating navigation in degraded environments without compromising real-time stability across different hardware profiles.
