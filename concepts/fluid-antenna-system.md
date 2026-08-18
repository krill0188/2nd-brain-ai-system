---
title: "Fluid Antenna System for UAV Communications"
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [drone, datalink, comms-protocol, antenna, fas, uav, beamforming]
domain: comms-protocol
sources: [inbox/fetch-2026-08-12-arxiv-modeling-and-performance-analysis-for-fluid-antenna-system-e.md]
confidence: medium
contested: false
contradictions: []
---

# Fluid Antenna System for UAV Communications

Fluid Antenna Systems (FASs) offer a promising solution for UAV air-to-ground (A2G) communications by enabling reconfigurable radiation characteristics. Unlike fixed antenna arrays, FAS can dynamically configure active ports to adapt to changing channel conditions.

## Key Technical Contributions

### Dynamic Port-Reconfigurable Near-Field Channel Model

Addresses limitations of traditional models by:
- Capturing dynamic port configuration of FAS
- Modeling near-field nature of UAV communications
- Decomposing LoS and NLoS components
- Integrating UAV motion dynamics with FAS port activation states

### FAS-Adaptive Subarray Partition Scheme

Uses a greedy strategy to:
- Dynamically group active ports to satisfy near-field conditions
- Reduce computational complexity significantly
- Handle subarray adjustments during port switching via dynamic update algorithm

### Channel Gain-Based Selection Strategy

Prioritizes high-gain ports to avoid:
- Low effective gain ports
- Deep-fading ports in dense FAS configurations

## Performance Factors

System performance depends on:

- FAS dimensions and port spacing
- Active port count
- UAV dynamics (altitude, velocity)
- Near-field vs. far-field conditions

## Computational Complexity

The subarray partition scheme achieves lower complexity than exhaustive search, making it suitable for real-time applications where UAV motion requires rapid adaptation.

## Related Concepts

- [[hybrid-beamforming-ntn]] — Beamforming for non-terrestrial networks
- [[datalink-communication]] — RF and wireless communication fundamentals
- [[uav-isac-cross-region]] — Integrated sensing and communication

## 📰 최근 관련 소식
- Dynamic adaptive task offloading for UAV-based road traffic monitoring (doi.org, 2027-1) — https://doi.org/10.1016/j.future.2026.108750
