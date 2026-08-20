---
title: "Chaotic Map Based UAV Secure Communication"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [datalink, comms-protocol, security, fpga]
sources: [raw/papers/comms-protocol/fpga-chaotic-map-uav-secure-communication.md]
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Chaotic Map Based UAV Secure Communication

FPGA 기반 카오스 맵 동기화를 활용한 UAV 보안 통신 시스템. Aerial Base Station(ABS)과 Ground Base Station(GBS) 간 RF 채널 보안 통신.

## 핵심 원리

### 카오스 기반 확산
- Logistic map 기반 동역학
- 비주기적, 광대역, 노이즈 유사 주파수 특성
- 정보 확산을 통한 도청 방지

### 가변 피드백 컨트롤러
- 오류 동역학 점근적 안정화
- 전송 중 동기화 유지
- 정보 신호 특성 포함 오류 검출

## 보안 요소

| 요소 | 설명 |
|------|------|
| Map 기밀성 | Logistic map 파라미터 |
| 컨트롤러 | 가변 피드백 컨트롤러 및 게인 |
| 스크램블링 | 설계자 선택의 가역 함수 |

## 장점

- 재밍 공격 및 다중경로 효과에 강건
- 광대역 스펙트럼으로 랜덤 RF 채널 선택
- 단순 알고리즘 (상관 합산 + 검출 메커니즘)
- 낮은 하드웨어 자원 활용
- 에너지 효율적

## 관련 개념

- [[datalink-communication]] — 드론 데이터링크 통신 기술
- [[mavlink2-security]] — MAVLink 2 보안 서명 및 암호화
- [[secure-swarm-uav-communications]] — 협력적 프렌들리 재밍을 통한 안전한 UAV 군집 통신

## 출처

- Nwachioma et al., "FPGA prototyping of synchronized chaotic map for UAV secure communication", arXiv:2101.03880, 2020.
