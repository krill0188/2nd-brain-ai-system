---
title: "NC2S: Secure Command, Control and Communications for UxVs"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-sw, gcs-software, security, mavlink, military]
sources: [raw/papers/drone-sw/nc2s-secure-c3-uxv.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# NC2S: Secure Command, Control and Communications for UxVs

무인차량(UxV)용 새로운 안전한 C3(Command, Control, Communications) 아키텍처. MAVLink의 인증/암호화 부재 문제를 해결하는 zero-trust 기반 계층적 자격 증명 시스템.

## 보안 메커니즘

- **mTLS + ECDSA**: 상호 TLS, 타원 곡선 디지털 서명 알고리즘
- **ECDH**: 타원 곡선 디피-헬만 키 교환
- **HMAC**: 해시 기반 메시지 인증 코드로 무결성 보장

## 프로토콜

- 자격 증명 관리
- 키 갱신
- 제어 이양(control handover)
- 전술 지휘관(TC) ↔ GCS ↔ UxV 간 계층적 권한

## 검증 결과

- Wi-Fi 및 Rohde&Schwarz HR-5000H 전술 라디오로 실험 검증
- HR-5000H: Wi-Fi 대비 약 **2배수 높은 지연** but 안정적 통신
- 최소 메시지 손실로 C3 링크 적합성 확인

## 관련 개념

- [[mavlink-protocol]] — MAVLink 프로토콜 구조
- [[mavlink2-security]] — MAVLink 2 보안 기능
- [[secure-swarm-uav-communications]] — 안전한 UAV 군집 통신

## 출처

T. Rebolo et al., "Secure Command, Control and Communications Systems (C3) for Army UxVs", arXiv:2511.21936, 2025. ^[raw/papers/drone-sw/nc2s-secure-c3-uxv.md]
