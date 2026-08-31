---
title: "AITester: Automated System-Level Testing for UAS"
created: 2026-08-24
updated: 2026-08-24
type: concept
tags: [drone, gcs-software, testing, automation, px4, ardupilot]
sources: [inbox/fetch-2026-08-24-arxiv-automated-system-level-testing-of-unmanned-aerial-systems.md]
confidence: medium
contested: false
contradictions: []
domain: gcs-software
---

# AITester: Automated System-Level Testing for UAS

AITester is an automated system-level testing approach for unmanned aerial systems (UAS) that utilizes model-based testing and artificial intelligence techniques to automatically generate, execute, and evaluate test scenarios.

## Overview

Current industrial practice for UAS testing involves manually creating test scenarios and evaluating outcomes. AITester addresses this limitation by generating test scenarios dynamically during execution based on environmental context at runtime.

## Key Features

### Automated Test Generation
- AI-driven scenario creation
- Runtime context awareness
- Dynamic adaptation to system state

### Target Components
- UAV autopilot systems
- Ground Control Station (GCS) cockpit display systems (CDS)
- Safety-critical avionics software

## Methodology

1. **Model-Based Testing**: Formal system models guide test generation
2. **AI Techniques**: Machine learning for scenario optimization
3. **Runtime Generation**: Tests created on-the-fly during execution
4. **Automated Evaluation**: Outcome assessment without manual intervention

## Evaluation Results

Empirical evaluation on core UAS components demonstrated effectiveness:
- Successfully generated scenarios causing deviations from expected UAV autopilot behavior
- Revealed potential flaws in GCS-CDS integration

## Related Topics

- [[px4-flight-stack]] — PX4 flight control software
- [[ardupilot]] — ArduPilot open-source autopilot
- [[drone-simulation]] — Simulation environments for testing
- [[ground-control-station]] — GCS software systems

## Source

^[inbox/fetch-2026-08-24-arxiv-automated-system-level-testing-of-unmanned-aerial-systems.md]

## 📰 최근 관련 소식
- Automated System-level Testing of Unmanned Aerial Systems (arxiv.org, 2024-03-23) — http://arxiv.org/abs/2403.15857v2
