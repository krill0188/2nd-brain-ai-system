---
title: "Cross-Layer Attacks on UAV C2 over 5G"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, datalink, security, 5g, research]
sources: [inbox/fetch-2026-08-19-arxiv-when-connectivity-is-not-enough-cross-layer-attacks-on-uav-c.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# 5G 기반 UAV C2 크로스 레이어 공격

## 개요

BVLOS UAV 운용에서 5G SA 네트워크를 통한 C2(Command and Control) 경로의 보안 문제 분석. 연결성만으로는 안전한 폐쇄 루프 제어가 보장되지 않음을 입증.

## 위협 모델

### 1. 사용자 평면 경합으로 인한 적시성 저하
- 공유 사용자 평면에서의 지연 증가
- 오래된 텔레메트리 및 꼬리가 두꺼운 지연 분포

### 2. 제어 평면 불안정성으로 인한 이동성 연속성 실패
- 핸드오버 중 안전 장치 작동
- 연결성 표시와 실제 제어 가능성의 괴리

### 3. gNodeB 침해 후 명령 무결성 위반
- 내비게이션 하이재킹
- 명령 재작성 공격

## 실험 설정

- Open5GS + UERANSIM 테스트베드
- MAVLink over 5G 사용자 평면
- 상용 Nokia 코어 기반 검증

## CVE 할당

- 5건의 견고성 문제 공개
- 3건 CVE 할당 완료
- 2건 추가 CVE 요청 대기 중

## 관련 개념

- [[secure-swarm-uav-communications]] — 안전한 UAV 군집 통신
- [[isac-uav-security]] — ISAC-UAV 시스템 보안
- [[mavlink-protocol]] — MAVLink 프로토콜

## 참고

Wagner Comin Sonaglio et al., arXiv:2603.04662 (2026)
