---
title: "FPGA Chaotic Map for UAV Secure Communication"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [datalink, comms-protocol, security, fpga]
sources: [raw/papers/datalink/fpga-chaotic-map-uav-secure-communication.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# FPGA Chaotic Map for UAV Secure Communication

FPGA 기반 혼돈 맵(chaotic map)을 활용한 UAV 안전 통신 시스템. 공중 기지국(ABS)과 지상 기지국(GBS) 간 RF 채널 보안을 위한 물리 계층 암호화 기법.

## 핵심 원리

- **로지스틱 맵(Logistic Map)**: 혼돈적 파라미터 공간에서 비주기적·광대역·잡음 특성 상태 생성
- **가변 피드백 컨트롤러**: 오차 역학의 점근적 안정화 및 정보 신호 동기화
- **스크램블링/디스크램블링**: 설계자 선택의 가역 함수 기반

## 보안 요소

- 맵 기밀성
- 가변 피드백 컨트롤러 및 스케일 팩터
- 경계 피드백 게인
- 스크램블링 함수 선택

## 장점

- **재밍 공격 저항성**: 광대역 스펙트럼으로 무작위 RF 채널 선택
- **다중경로 효과 감소**
- **에너지 효율성**: FPGA 기반 하드웨어 자원 최소화

## 관련 개념

- [[secure-swarm-uav-communications]] — 협력적 프렌들리 재밍 기반 안전한 UAV 군집 통신
- [[isac-uav-security]] — ISAC-UAV 시스템 물리 계층 보안
- [[datalink-communication]] — 드론 데이터링크 통신 기술 개요

## 출처

Christian Nwachioma et al., "FPGA prototyping of synchronized chaotic map for UAV secure communication", arXiv:2101.03880, 2020. ^[raw/papers/datalink/fpga-chaotic-map-uav-secure-communication.md]
