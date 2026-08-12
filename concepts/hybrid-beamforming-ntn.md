---
title: "Hybrid Beamforming in Non-Terrestrial Networks"
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [drone, datalink, comms-protocol, beamforming, uav, satellite]
domain: comms-protocol
sources: [inbox/fetch-2026-08-12-arxiv-hybrid-beamforming-in-non-terrestrial-networks-architectures.md]
confidence: medium
contested: false
contradictions: []
---

# Hybrid Beamforming in Non-Terrestrial Networks

Hybrid analog-digital beamforming (HBF) is a key enabling technology for non-terrestrial networks (NTNs) where large antenna arrays compensate for severe propagation loss. Fully digital beamforming is often impractical due to RF chain cost, power consumption, and payload limitations on aerial platforms.

## Key Challenges for NTN Platforms

NTN platforms like LEO satellites and UAVs impose distinctive HBF design challenges:

- **High mobility** and Doppler effects
- **Sparse line-of-sight-dominant channels**
- **Stringent on-board energy budgets**
- **Coupling between beamforming and platform placement/trajectory** (UAV-specific)

## Technical Categories

HBF techniques for NTN systems cover five categories:

1. **System architecture and precoding design** — shared analog/digital precoder structures
2. **Time-varying beam management** — traffic-driven beam hopping (LEO) vs. mobility-aware beam tracking (UAV)
3. **Network-level cooperation and scheduling** — multi-platform coordination
4. **Sensing capability and reconfigurable surfaces** — integrated sensing and communication
5. **Security and multiple access** — protected transmission schemes

## Platform-Specific Differences

| Aspect | LEO Satellite | UAV |
|--------|--------------|-----|
| Dominant time-varying mechanism | Traffic-driven beam hopping | Mobility-aware beam tracking |
| Channel characteristics | Predictable orbital dynamics | Highly dynamic, trajectory-dependent |
| Energy constraints | Solar-powered, stable | Battery-limited, mission-dependent |

## Research Directions

Open challenges include scalable, robust, and hardware-efficient HBF for next-generation NTNs, particularly addressing real-time adaptation to platform motion and dynamic channel conditions.

## Related Concepts

- [[datalink-communication]] — RF and wireless communication for drones
- [[uav-isac-cross-region]] — Integrated sensing and communication for UAVs
- [[swarm-coordination]] — Multi-platform coordination
