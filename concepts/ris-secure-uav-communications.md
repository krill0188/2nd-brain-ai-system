---
title: "RIS-Aided Robust Secure UAV Communications"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [datalink, comms-protocol, ris, security]
sources: [raw/papers/comms-protocol/ris-secure-uav-communications.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# RIS-Aided Robust Secure UAV Communications

재구성 가능한 지능형 표면(RIS)을 활용한 UAV 보안 통신 시스템. TDMA 프로토콜 기반 다운링크/업링크 통신의 평균 최악 경우 비밀률 최대화.

## 시스템 구성

- UAV와 지상 사용자 간 양방향 통신
- 도청자 존재 상황에서의 보안 통신
- RIS를 통한 채널 품질 향상
- TDMA 기반 DL/UL 통신

## 최적화 문제

### 목표
평균 최악 경우 비밀률 최대화

### 설계 변수
- UAV 궤적
- RIS 수동 빔포밍
- 합법적 송신기의 전송 전력

### 제약
- 도청 채널 CSI 불완전성
- 비볼록(non-convex) 최적화 문제

## 알고리즘

### AO (Alternating Optimization)
1. UAV 궤적 최적화 (SCA 적용)
2. RIS 빔포밍 최적화 (S-Procedure, SDR 적용)
3. 전력 할당 최적화

### 기법
- Successive Convex Approximation (SCA)
- S-Procedure
- Semidefinite Relaxation (SDR)

## 성능

- 기준 알고리즘 대비 평균 비밀률 상당한 개선
- 제안 알고리즘의 강건성 확인

## 관련 개념

- [[datalink-communication]] — 드론 데이터링크 통신 기술
- [[fluid-antenna-system]] — FAS 기반 UAV 통신
- [[hybrid-beamforming-ntn]] — 비지상 네트워크 하이브리드 빔포밍
- [[chaotic-map-uav-secure-comms]] — 카오스 맵 기반 UAV 보안 통신

## 출처

- Li et al., "Robust Secure UAV Communications with the Aid of Reconfigurable Intelligent Surfaces", arXiv:2008.09404, 2020.
