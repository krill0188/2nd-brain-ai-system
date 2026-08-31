---
title: "UAV Resilience Against Stealthy Attacks"
created: 2026-08-23
updated: 2026-08-23
type: concept
tags: [drone, gcs-software, security, sel4, runtime-monitoring]
sources: [inbox/fetch-2026-08-23-arxiv-uav-resilience-against-stealthy-attacks.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# UAV Resilience Against Stealthy Attacks

ArXiv paper (2025-03-21) presenting an architecture for securing UAV software stacks against attackers who compromise GCS or UAV software.

## Problem

UAVs depend on untrusted software components, making them targets for attacks. Existing work addresses either GCS compromise OR UAV software compromise, but not both simultaneously.

## Solution

Architecture with:
- Runtime monitoring
- seL4-based software isolation

## Capabilities

- Prevents attackers from exploiting software bugs
- Prevents stealthy attacks
- Retrofits legacy UAVs
- Secures MAVLink protocol

## Benefits

- Wide adoption possible through MAVLink compatibility
- Protection against both GCS and UAV-side attacks
- Formal verification through seL4 isolation

## Related

- [[mavlink-protocol]] — MAVLink protocol
- [[mavlink2-security]] — MAVLink 2 security
- [[drone-safety-failsafe]] — Drone safety systems

## 📰 최근 관련 소식
- UAV Resilience Against Stealthy Attacks (arxiv.org, 2025-03-21) — http://arxiv.org/abs/2503.17298v2
