---
title: "pymavlink v2.4.50 Release"
created: 2026-09-25
updated: 2026-09-25
type: concept
domain: comms-protocol
tags: [drone, drone-sw, datalink]
sources: [inbox/processed/fetch-2026-09-25-pymavlink.md]
confidence: medium
contested: false
contradictions: []
---

# pymavlink v2.4.50 Release

2026-09-24 릴리스. 이전 v2.4.49(2025-08) 이후 누적된 기능 추가·버그 수정·의존성 갱신을
포함한다.^[inbox/processed/fetch-2026-09-25-pymavlink.md]

## 주요 변경사항

- **비행 모드/단위**: RATE_ACRO, TURTLE 모드 추가, 소비 단위 L/h 추가.
- **mavutil**: ws/wss가 최초 실패 후에도 재연결을 시도, port 필드 예약어 처리, 변수명 `type` → `t`.
- **서명**: MAVLink 서명 타임스탬프 한도를 설정 가능하게 변경.
- **도구**: Wireshark MAVLink Telemetry Log(TLOG) 리더 추가, mavlogdump `follow` 인자 수정, mavfft_pid 샘플레이트 보정, mavftp `Set()` 사용 수정.
- **생성기**: mavgen_lua의 MAV_BOOL/int8 비트마스크 지원, WIP 메시지 사용 시 C 코드 경고 생성.
- **품질/빌드**: ruff·pylint·mypy 린트 도입, Python dev 패키지 감지, CI 브랜치 규칙 및 의존성 bump.

## 한계

수집 원문이 변경 목록 도중 잘려 있다.

## 관련 개념

- [[pymavlink]] — pymavlink 개요 및 릴리스 이력
- [[mavlink]] — MAVLink 프로토콜 엔티티
- [[mavsdk]] — MAVLink 기반 고수준 SDK
