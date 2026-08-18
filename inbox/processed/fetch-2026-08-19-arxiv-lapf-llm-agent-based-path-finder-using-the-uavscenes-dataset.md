---
title: "LAPF: LLM-Agent-Based Path Finder Using the UAVScenes Dataset"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2608.15175v1
authors: "Yousef Emami, Mohammadhossein Homaei, Hao Zhou, Miguel Guti\u00e9rrez Gait\u00e1n, Atefeh Hajijamali Arani, Rui Zhang"
published: "2026-08-15"
tags: [drone, ai-autonomy, paper, arxiv]
---

# LAPF: LLM-Agent-Based Path Finder Using the UAVScenes Dataset

**Authors**: Yousef Emami, Mohammadhossein Homaei, Hao Zhou, Miguel Gutiérrez Gaitán, Atefeh Hajijamali Arani, Rui Zhang
**Published**: 2026-08-15
**arXiv**: http://arxiv.org/abs/2608.15175v1

## Abstract

Uncrewed aerial vehicles (UAVs) are increasingly deployed for autonomous navigation in complex outdoor environments, where dynamic conditions and mission requirements require intelligent adaptive decision-making. Existing optimization-based, Machine Learning (ML), and Reinforcement Learning (RL) approaches often rely on predefined models or task-specific training, limiting their generalization and adaptability in uncertain scenarios. Recent Large Language Model (LLM)-assisted approaches offer promising reasoning capabilities but remain constrained by limited agentic functionality, including insufficient memory, planning, and tool interaction mechanisms.This paper proposes an LLM-Agent-Based Path Finder (LAPF) framework for autonomous UAV navigation in town-scale outdoor environments. LAPF extends LLM-assisted navigation by integrating perception, memory, planning, and action modules into a closed-loop cognitive architecture. The proposed agent leverages prior navigation experiences, performs Chain-of-Thought (CoT) reasoning, couples each detected hazard to a bounded corrective action, and dynamically refines waypoint decisions based on environmental feedback.The three independent trials per method demonstrate that LAPF achieves mean path lengths of 512.83 m and 506.37 m, compared to the straight-line optimum of 497.33 m, corresponding to path length reductions of 17.2% and 15.6% relative to CoT prompting and absolute path efficiencies of 97.1% and 98.1% in open-field and obstacle-injected scenarios, respectively. Furthermore, LAPF is the only evaluated approach that couples every detected hazard to a bounded, metric-neutral corrective action while maintaining near-goal stability, with zero clamp events in both scenarios, whereas CoT prompting increases from 9.7 to 14.0 events.
