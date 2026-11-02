---
title: "Dual-Mobility Perspective"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [uav-communication, fluid-antennas, trajectory-planning, channel-adaptation, dual-mobility]
sources:
  - http://arxiv.org/abs/2610.35047v1
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Dual-Mobility Perspective

Dual-Mobility Perspective는 저고도 무선 네트워크에서 UAV 통신 시스템이 거대 규모 공중-지상 기하학적 변화와 빠른 지역적 채널 변동에 적응할 수 있도록 설계된 개념으로, UAV 궤적 계획에 의해 제공되는 거시적 이동성과 유동 안테나 위치 재구성에 의해 제공되는 미시적 이동성을 통합한 프레임워크이다.

이 관점은 UAV의 전체적인 경로 계획이 공중-지상 링크 기하학을 적응시키는 매크로 무브먼트(macro-mobility)를 담당하는 반면, 유동 안테나의 위치를 실시간으로 재구성하여 지역 채널 상태를 미세하게 보정하는 미시적 적응(micro-mobility)을 가능하게 한다고 정의한다. 두 관점의 조합은 고도화된 환경 조건 하에서 통신 성능을 최적화하는 것을 목표로 한다.

## 개요

Fluid Antennas Enabled UAV Communication Systems 연구에서 중심 논점으로 부상한 개념이다. UAV가 공중에서 이동하며 발생하는 대규모 채널 변동은 궤적 계획만으로 해결하기 어려우며, 안테나 자체의 물리적 재구성이 필요한 지역적 변동까지 대응해야 한다. Dual-Mobility Perspective는 이러한 이분법을 해결하기 위해 공간적 이동과 안테나 위치 재구성을 분리하여 체계적으로 다룬다.

이 프레임워크에서 **macro-mobility**는 UAV의 비행 경로 및 위치를 통해 대-scale 기하학적 변화를 다루고, **micro-mobility**는 안테나 어레이 내부의 위치 변경을 통해 small-scale 파라미터 변동을 보완한다. 이는 통신 신뢰성과 용량을 극대화하기 위한 이중 단계 적응 전략을 제공한다.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| **Macro-Mobility** | UAV trajectory planning에 의해 제공되며, 공중-지상 기하학의 대-scale 적응을 담당 |
| **Micro-Mobility** | Fluid Antenna position reconfiguration에 의해 제공되며, 미세한 지역 채널 적응을 담당 |
| **Joint Optimization** | UAV trajectory, FA positions, 및 beamforming을 동시에 최적화하는 문제 (높은 계산 복잡도) |

## 관련 페이지

- [[Fluid Antennas Enabled UAV Communication Systems — Fundamentals, Challenges, and Future Directions]] — 본 개념이 포함된 원본 문헌
- [[Macro-Mobility]] — Dual-Mobility Perspective 내의 매크로 이동성 구성 요소
- [[Micro-Mobility]] — Dual-Mobility Perspective 내의 미시적 이동성 구성 요소

## 출처

- http://arxiv.org/abs/2610.35047v1 (Liu et al., 2026)

재확인 필요: 본 문서는 원문 발췌 내용에 기반하여 구조화했으나, Dual-Mobility Perspective 개념의 구체적인 수학적 모델이나 최적화 알고리즘 세부 사항은 원문에 명시되지 않았으며, 추가적인 검증이 필요합니다.

## 참고

[[a2z-longtail-dual]] [[bayesian-residual]]
