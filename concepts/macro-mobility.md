---
title: "Macro-Mobility"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [uav-communication, fluid-antennas, low-altitude-wireless-networks, trajectory-planning, mobility-classification]
sources: []
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Macro-Mobility

Low-altitude wireless networks (LAWNs) require UAV communication systems to adapt to large-scale propagation changes and fast local channel fluctuations. Macro-mobility refers to the UAV trajectory planning providing large-scale air-to-ground geometry adaptation, enabling the system to cope with broad environmental and propagative changes over wide areas. It operates on a longer time scale and larger spatial scope compared to micro-mobility, serving as the macroscopic movement layer within the dual-mobility framework.

## 개요

Fluid antennas (FAs) introduce an additional degree of freedom (DoF) by reconfiguring antenna positions within a compact aperture. This architecture enables a dual-mobility perspective for UAV communication systems: macro-mobility governs the UAV's overall trajectory to adapt large-scale air-to-ground geometry, while micro-mobility, provided by FA position reconfiguration, handles fine-grained local channel adaptation. Macro-mobility is essential for addressing the fundamental challenge of large-scale propagation changes in low-altitude wireless networks, where the UAV must reposition itself to maintain viable connectivity across varying terrain and user distributions.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| **공간 스케일** | 광역 air-to-ground geometry adaptation (대규모) |
| **시간 스케일** | 장기적/비행 경로 계획 주기 |
| **목적** | 큰 규모의 채널 환경 변화 적응 |
| **수단** | UAV 궤적 계획(Trajectory Planning) |

## 활용처

- 저고도 무선 네트워크(LAWN)에서의 광역 커버리지 최적화
- 변화하는 지형 및 사용자 분포에 대한 공중 기지국 재구성
- 전체적인 air-to-ground 기하학적 구조 최적화

## 관련 페이지

- [[Fluid-Antenna]] — fluid antennas enabled UAV communication fundamentals
- [[Dual-Mobility-Perspective]] — dual-mobility framework encompassing macro- and micro-mobility

## 출처

- (사용자 재확인 필요) original paper: Liu et al., "Fluid Antennas Enabled UAV Communication Systems: Fundamentals, Challenges, and Future Directions," arXiv preprint arXiv:2610.35047, 2026.

## 참고

[[dual-mobility-perspective]] [[eve-air-mobility-transition]]
