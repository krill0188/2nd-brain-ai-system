---
title: "NC2S - Secure Command, Control and Communications System for UxVs"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-sw, gcs-software, security, mavlink]
sources: [raw/papers/gcs-software/nc2s-secure-c3-system.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# NC2S - Secure Command, Control and Communications System for UxVs

군용 무인차량(UxV)을 위한 새로운 보안 명령-제어 아키텍처. MAVLink의 보안 취약점(인증/암호화 부재)을 해결하는 Zero-Trust 모델.

## 보안 요구사항

- **기밀성(Confidentiality)** — 데이터 노출 방지
- **무결성(Integrity)** — 메시지 변조 방지
- **인증(Authentication)** — 주체 신원 확인

## 핵심 기술

### 암호화
- mTLS (mutual Transport Layer Security)
- ECDSA (Elliptic Curve Digital Signature Algorithm) 인증서
- ECDH (Elliptic Curve Diffie-Hellman) 키 교환
- HMAC (Hash-based Message Authentication Code) 무결성 검증

### 접근 제어
- 계층적 자격 기반 권한
- Tactical Commander (TC) ↔ GCS ↔ UxV 간 접근 규제
- 실시간 제어 위임 지원

### 경량 프로토콜
- 자격 관리
- 키 갱신
- 제어 인수(handover)

## 검증 결과

| 링크 유형 | 특징 |
|-----------|------|
| Wi-Fi | 저지연, 안정적 |
| HR-5000H (전술 라디오) | Wi-Fi 대비 ~100배 높은 지연, 그러나 안정적 통신 유지 |

- TC 터미널과 GCS 간 NC2S 링크에 적합

## 관련 개념

- [[mavlink-protocol]] — MAVLink 프로토콜 개요
- [[mavlink2-security]] — MAVLink 2 보안 기능
- [[datalink-communication]] — 드론 데이터링크 통신

## 출처

- Rebolo et al., "Secure Command, Control and Communications Systems (C3) for Army UxVs", arXiv:2511.21936, 2025.
