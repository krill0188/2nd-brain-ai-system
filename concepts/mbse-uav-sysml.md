---
title: "Model-Based Systems Engineering for UAVs with SysML"
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [drone, ai-agent, ai-autonomy, sysml, mbse, ros2, systems-engineering]
domain: ai-autonomy
sources: [inbox/fetch-2026-08-12-arxiv-model-based-systems-engineering-framework-for-sysml-driven-d.md]
confidence: medium
contested: false
contradictions: []
---

# Model-Based Systems Engineering for UAVs with SysML

Model-Based Systems Engineering (MBSE) provides a formal design framework for autonomous UAV development using the Systems Modeling Language (SysML) as a backbone. This approach addresses limitations of document-centric workflows that can lead to ambiguity, interface inconsistencies, and weak traceability.

## Four-Layer Framework

The SysML-driven development spans four connected layers:

1. **Stakeholder requirements** — captured via requirement diagrams
2. **Functional decomposition** — activity diagrams for behavior
3. **Logical architecture** — block definition diagrams and internal block diagrams
4. **Physical/software allocation** — parametric diagrams for performance constraints

## SysML Diagram Types Used

| Diagram Type | Purpose |
|-------------|---------|
| Requirement diagrams | Stakeholder needs and traceability |
| Activity diagrams | Functional behavior flows |
| Block definition diagrams | System structure and components |
| Internal block diagrams | Internal connections and interfaces |
| State machine diagrams | Behavioral modes and transitions |
| Parametric diagrams | Performance constraints and analysis |

## ROS 2 Mapping

The logical architecture maps systematically to ROS 2 software architecture:

- **SysML blocks** → ROS 2 nodes
- **Flow ports and connectors** → ROS 2 topics
- **Request-response interactions** → ROS 2 services
- **Goal-oriented behaviors** → ROS 2 actions

## Mission Scenarios Covered

Representative autonomous UAV missions in the framework:

- Autonomous take-off
- Waypoint navigation
- Hover stabilization
- Obstacle avoidance
- Return-to-home (RTH)
- Emergency handling

## Benefits

The model supports requirement allocation, interface definition, subsystem responsibility assignment, and verification planning before simulation or physical deployment.

## Related Concepts

- [[ros2-drone-integration]] — ROS 2 drone software stack
- [[px4-system-architecture]] — PX4 flight control architecture
- [[ardupilot-architecture]] — ArduPilot architecture
- [[drone-ai-agents]] — Autonomous decision-making systems

## 📰 최근 관련 소식
- JTF-SB Marines Put Eyes in the Sky with VXE30 Stalker and Skydio X10 [Image 7 of 7] - DVIDS (news.google.com, Mon, 10 Au) — https://news.google.com/rss/articles/CBMiogFBVV95cUxNd0FhQk5fTVVqVGZVc1luOU41MFlJVHpMeGRKT25vZ1pGMEhteFo0YVRhTjA3RWhKdjlncmtSMGFYbW9NRkRFdk1RaFlURHpocTliVExsWmZJYzJTejZ3VlBPcU5ydEg5RWdpZ29KYkxjclRYOTQtaldHeksyS3J1djk3cHJOaXBScFkzMEZWajhlTlJwYW44MG05TE1mcElIdGc?oc=5
