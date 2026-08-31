---
title: "Channel State Information Analysis for Jamming Attack Detection in UAV Networks"
created: 2026-08-23
updated: 2026-08-23
type: concept
tags: [drone, gcs-software, security, jamming, csi, wireless]
sources: [inbox/fetch-2026-08-23-arxiv-channel-state-information-analysis-for-jamming-attack-detect.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# CSI-Based Jamming Detection in UAV Networks

ArXiv paper (2025-04-08) investigating jamming attack detection using Channel State Information in static and dynamic UAV networks.

## Background

IEEE 802.11 networks used for:
- Smart home applications
- Internet of Things (IoT)
- Short-range high throughput static and dynamic inter-vehicular communication

## Channel State Information (CSI)

Provides detailed view of communication channel state, representing:
- Multipath propagation
- Scattering
- Phase shift
- Fading
- Power decay

## Experimental Setup

- **Hardware**: ESP32-S3 modules
- **Network**: UAV to Ground Control Station communication
- **Jammer**: Constant jammer
- **Scenarios**: Static and dynamic communication

## Investigation

Tests combined effects of constant jammer on recorded CSI parameters and feasibility of jamming detection through CSI analysis.

## Related

- [[datalink-communication]] — Drone datalink communication
- [[nc2s-secure-c3-system]] — Secure C3 systems
- [[ris-secure-uav-communications]] — RIS-secured UAV communications

## 📰 최근 관련 소식
- Channel State Information Analysis for Jamming Attack Detection in Static and Dynamic UAV Networks -- An Experimental Study (arxiv.org, 2025-04-08) — http://arxiv.org/abs/2504.05832v1
