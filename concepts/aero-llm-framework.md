---
title: "Aero-LLM: Distributed Framework for Secure UAV Communication"
created: 2026-08-24
updated: 2026-08-24
type: concept
tags: [drone, gcs-software, ai-agent, datalink, security]
sources: [inbox/fetch-2026-08-24-arxiv-aero-llm-a-distributed-framework-for-secure-uav-communicatio.md]
confidence: medium
contested: false
contradictions: []
domain: gcs-software
---

# Aero-LLM: Distributed Framework for Secure UAV Communication

Aero-LLM is a distributed framework integrating multiple Large Language Models (LLMs) to enhance UAV mission security and operational efficiency through specialized task allocation across onboard, edge, and cloud systems.

## Overview

Unlike conventional singular LLM approaches, Aero-LLM leverages multiple specialized LLMs for distinct tasks including inferencing, anomaly detection, and forecasting. This dynamic architecture reduces performance bottlenecks and increases security capabilities for UAV-GCS communication.

## Architecture

### Distributed LLM Deployment
- **Onboard systems**: Real-time inference and local decision-making
- **Edge servers**: Anomaly detection and preprocessing
- **Cloud infrastructure**: Forecasting and model training

### Security Features
- Multi-layered defense against cyber threats
- Task-specific LLM isolation
- Enhanced UAV decision-making resilience

## Key Capabilities

1. **Intelligent Decision-Making**: LLM-powered operational choices
2. **Anomaly Detection**: Real-time threat identification
3. **Forecasting**: Predictive mission planning
4. **Secure Communication**: Protected GCS-UAV datalink

## Related Topics

- [[mavlink-protocol]] — Communication protocol for UAV systems
- [[drone-ai-agents]] — Autonomous decision-making architectures
- [[datalink-communication]] — RF and wireless communication systems
- [[px4-flight-stack]] — PX4 flight control software stack

## Source

^[inbox/fetch-2026-08-24-arxiv-aero-llm-a-distributed-framework-for-secure-uav-communicatio.md]

## 📰 최근 관련 소식
- Aero-LLM: A Distributed Framework for Secure UAV Communication and Intelligent Decision-Making (arxiv.org, 2025-02-05) — http://arxiv.org/abs/2502.05220v1
