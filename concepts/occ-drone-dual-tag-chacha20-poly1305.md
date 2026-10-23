---
title: "OCC 드론 채널용 이중 태그 ChaCha20-Poly1305 AEAD 인증 프로토콜"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: comms-protocol
tags: [drone, datalink]
sources: [raw/papers/_unclassified/global-shutter-기반-occ-드론-채널을-위한-이중-태그-기반-chacha20-poly1305-aead-인증-프로토콜.md, inbox/processed/fetch-2026-10-23-kci-global-shutter-기반-occ-드론-채널을-위한-이중-태그-기반-chacha20-poly1305-a.md]
confidence: low
contested: false
contradictions: []
---

# OCC 드론 채널용 이중 태그 ChaCha20-Poly1305 AEAD 인증 프로토콜

김유강(아주대), 정보보호학회논문지 2026. 원문 공개이나 이 페이지는 **초록 기준**이다.

## 문제
- 메시지 단위 AEAD는 마지막 태그를 받기 전까지 위변조 탐지가 늦다.
- 패킷 단위 AEAD는 192-bit 패킷에 128-bit 태그가 붙어 오버헤드가 크다.^[raw/papers/_unclassified/global-shutter-기반-occ-드론-채널을-위한-이중-태그-기반-chacha20-poly1305-aead-인증-프로토콜.md]

## 제안
- 일반 패킷은 24-bit mini-tag로 1차 검증하고, K번째 패킷에 128-bit full-tag를 붙여 인증 주기 전체의 무결성을 최종 검증한다.
- mini-tag 검증만으로는 복호화·평문 전달을 하지 않으며 full-tag 검증 후에만 최종 복호화·전달한다.
- HKDF-Expand 기반 implicit nonce로 nonce 전송 오버헤드를 줄인다.
- 초록 보고: K=8에서 채널 효율 76.9%, 위조 공격 및 ASCON 비교로 성능·보안성 평가.^[raw/papers/_unclassified/global-shutter-기반-occ-드론-채널을-위한-이중-태그-기반-chacha20-poly1305-aead-인증-프로토콜.md]

## 한계
OCC(광학 카메라 통신) 채널 전용 설계이며, 초록 외 실험 조건은 확인하지 못했다.

관련: [[mavlink2-security]], [[datalink-communication]].

## 📰 최근 관련 소식
- Global Shutter 기반 OCC 드론 채널을 위한 이중 태그 기반 ChaCha20-Poly1305 AEAD 인증 프로토콜 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003395575
