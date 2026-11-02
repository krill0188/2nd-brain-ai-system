---
title: "Joint Optimization"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [uav-communication, fluid-antennas, trajectory-optimization, beamforming, offline-online-framework]
sources: []
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Joint Optimization

저고도 무선 네트워크(LAWNs)에서 UAV 통신 시스템은 대규모 전파 변화와 빠른 국지적 채널 변동에 적응해야 한다. Fluid antennas(FAs)는 컴팩트 어레이 내에서 안테나 위치를 재구성하여 추가 자유도(DoF)를 제공한다. 본 개념은 UAV trajectary planning(거시적 이동성)과 FA position reconfiguration(미시적 이동성)을 결합한 ** joint optimization** 문제를 다룬다.

## 개요

UAV 통신 시스템에서 안테나 위치 재구성 및 trajectary 계획과 빔포밍을 동시에 최적화하는 **joint optimization** 문제는 고해상도 채널 상태 정보(CSI)의 불확실성과 높은 계산 복잡도 등으로 인해 주요 설계 과제로 지적된다. UAV의 거시적 이동성(large-scale air-to-ground geometry adaptation)과 FA의 미시적 이동성(fine-grained local channel adaptation)을 결합하여 통신 성능을 향상시키는 것을 목표로 한다.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| Trajectory Planning | UAV의 거시적 이동을 통한 공중-ground 기하학적 구조 적응 |
| Position Reconfiguration | FA 위치를 통한 미시적 채널 적응 |
| Beamforming | 신호 전송을 위한 빔 형성 및 방향 제어 |
| Information Uncertainty | 채널 상태 정보의 불확실성으로 인한 최적화 복잡도 증가 |
| Mobility Constraints | 에너지 및 하드웨어 제약 하에서의 이동 제약 |

## 활용처

- 저고도 무선 네트워크(LAWNs)에서의 UAV 통신 시스템 설계
- 변동성이 큰 공중 채널 환경에서의 실시간 성능 최적화
- 통신 품질과 유한한 계산 자원 간의 트레이드오프 관리

## 관련 페이지

- [[Fluid Antennas]] — fluid antennas enabled UAV communication fundamentals
- [[Trajectory Planning]] — UAV trajectory optimization for air-to-ground geometry adaptation
- [[Beamforming]] — beamforming techniques in UAV communication systems

## 출처

- (사용자 재확인 필요) Liu et al., "Fluid Antennas Enabled UAV Communication Systems: Fundamentals, Challenges, and Future Directions," *arXiv preprint arXiv:2610.35047*, 2026. [http://arxiv.org/abs/2610.35047v1](http://arxiv.org/abs/2610.35047v1)

## 참고

[[2-dof-magnetic-spherical-joint]] [[actoroptimization]]
