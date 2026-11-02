---
title: "Micro-Mobility"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [uav-communication, fluid-antennas, low-altitude-wireless-networks, channel-adaptation]
sources: []
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Micro-Mobility

Micro-Mobility는 UAV 통신 시스템에서, 플루이드 안테나(FAs)의 위치 재구성을 통해 빠른 시간 척도에서 국소 채널 변동에 적응하는 미세한 이동성을 의미한다. 이는 UAV의 전체 비행 경로 계획이 제공하는 거시적 공기-지상 기하학적 적응과는 구별되며, 안테나 어레이 내부의 컴팩트한 어페르처 내에서 안테나 위치를 실시간으로 변환하여 급변하는 통신 환경을 보완한다.

## 개요

Low-altitude wireless networks (LAWNs)를 지원하는 UAV 통신 시스템은 대규모 진행률 변화와 빠른 국소 채널 변동에 대처해야 한다. 기존 고정 안테나와 달리 플루이드 안테나는 어레이 내 안테나 위치를 재구성하여 추가적인 자유도(DoF)를 제공한다. 본 개념은 UAV 트랙토리 플래닝이 매크로 무빙(macro-mobility)을 담당하여 넓은 규모의 공기-지상 기하학을 적응시키는 데 반해, 플루이드 안테나의 위성 재구성이 마이크로 무빙(micro-mobility)을 통해 국소 채널을 세밀하게 적응시킨다는 **이중 이동성(Double Mobility) 관점**에서 논의된다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| 자유도(DoF) | 플루이드 안테나(FAs)를 통한 추가적인 자유도 제공 |
| 적용 규모 | 국소 채널 변동을 위한 미시적 수준 |
| 수식어와 연계 | Dual-Mobility Perspective (매크로 + 미시적 이동성 조합) |

## 활용처

- 저고도 무선 네트워크(LAWN) 환경에서의 UAV 통신
- 빠른 채널 변동이 발생하는 시나리오에서 실시간 빔포밍 및 어답터 조정
- 고성능 공기-지상 통신이 요구되는 스마트 시티, 재난 구조, 물류 배송 등

## 관련 페이지

- [[Fluid Antennas]] — 플루이드 안테나 개념 및 동작 원리
- [[Dual-Mobility Perspective]] — 매크로와 마이크로 이동성의 결합 개념

## 출처

- (사용자 재확인 필요) — 원문: Liu et al., "Fluid Antennas Enabled UAV Communication Systems: Fundamentals, Challenges, and Future Directions," *arXiv preprint arXiv:2610.35047*, 2026.
