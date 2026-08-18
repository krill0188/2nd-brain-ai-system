---
title: "LAPF: LLM-Agent-Based Path Finder for UAVs"
created: 2026-08-19
updated: 2026-08-19
type: concept
domain: ai-autonomy
tags: [drone, ai-autonomy, llm-agent, path-planning, uavscenes, navigation]
sources: [inbox/fetch-2026-08-19-arxiv-lapf-llm-agent-based-path-finder-using-the-uavscenes-dataset.md]
confidence: high
contested: false
contradictions: []
---

# LAPF: LLM-Agent-Based Path Finder for UAVs

LLM-Agent-Based Path Finder (LAPF) framework for autonomous UAV navigation in town-scale outdoor environments, integrating perception, memory, planning, and action modules into a closed-loop cognitive architecture.

## Overview

Existing optimization-based, ML, and RL approaches often rely on predefined models or task-specific training, limiting generalization in uncertain scenarios. LLM-assisted approaches offer reasoning capabilities but remain constrained by insufficient agentic functionality.

## Architecture Components

### Core Modules
1. **Perception** — Environmental sensing and hazard detection
2. **Memory** — Prior navigation experience storage and retrieval
3. **Planning** — Chain-of-Thought (CoT) reasoning for waypoint decisions
4. **Action** — Bounded corrective actions coupled to detected hazards

### Key Features
- Leverages prior navigation experiences
- Performs Chain-of-Thought reasoning
- Couples each detected hazard to bounded corrective action
- Dynamically refines waypoint decisions based on environmental feedback

## Performance Results

| Metric | Open-Field | Obstacle-Injected |
|--------|-----------|-------------------|
| Mean Path Length | 512.83 m | 506.37 m |
| Straight-Line Optimum | 497.33 m | 497.33 m |
| Path Efficiency | 97.1% | 98.1% |
| Improvement vs CoT | 17.2% | 15.6% |
| Clamp Events | 0 | 0 |

*CoT prompting had 9.7→14.0 clamp events*

## Advantages

- Only evaluated approach coupling every detected hazard to bounded, metric-neutral corrective action
- Maintains near-goal stability
- Zero clamp events in both scenarios

## Related Concepts

- [[llm-enabled-uav-natural-language-navigation]] — STL-based LLM navigation
- [[drone-ai-agents]] — Autonomous decision-making and multi-agent systems
- [[mission-planning]] — QGC waypoint and MAVSDK mission planning
- [[visual-positioning-odometry]] — GPS-denied navigation

## Sources

- Emami et al., "LAPF: LLM-Agent-Based Path Finder Using the UAVScenes Dataset", arXiv:2608.15175, 2026-08-15
