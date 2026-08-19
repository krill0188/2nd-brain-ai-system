---
title: "ISAC-UAV System Physical-Layer Security"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, datalink, isac, security, beamforming]
sources: [inbox/fetch-2026-08-19-arxiv-improving-physical-layer-security-in-isac-uav-system-beamfor.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# ISAC-UAV 시스템 물리 계층 보안

## 개요

통합 감지 및 통신(ISAC)을 활용한 UAV 보안 통신 시스템. UAV 궤적 및 빔포밍 벡터 최적화를 통한 평균 통신 비밀률 극대화.

## 시스템 구성

- 다중 안테나 UAV
- ISAC 파형 전송
- 다중 지상 IoT 장치와의 통신
- 주변 환경 감지

## 최적화 접근법

### Successive Convex Approximation (SCA)
- 비볼록 문제 해결을 위한 효율적 알고리즘
- 다변수 결합으로 인한 비볼록성 극복

### 목표
- 평균 통신 비밀률 최대화
- 감지 표적 정확도 보장

## 관련 개념

- [[cross-layer-attacks-uav-5g]] — UAV C2 보안 공격
- [[secure-swarm-uav-communications]] — 안전한 UAV 군집 통신
- [[uav-isac-cross-region]] — 교차 지역 ISAC

## 참고

Yue Xiu et al., arXiv:2409.14431 (2024)
