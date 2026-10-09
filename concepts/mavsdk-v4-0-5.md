---
title: "MAVSDK v4.0.5 Release"
created: 2026-10-08
updated: 2026-10-09
type: concept
domain: comms-protocol
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-10-08-mavsdk.md, inbox/processed/fetch-2026-10-09-mavsdk.md]
confidence: medium
contested: false
contradictions: []
---

# MAVSDK v4.0.5 Release

2026-10-07 릴리스. 변경 사항은 두 건이다.^[inbox/processed/fetch-2026-10-08-mavsdk.md]

- **examples**: 커스텀 GAS_SENSOR 메시지의 송수신 예제 추가(PR #3152, @julianoes).
- **system_tests**: System을 DestroyWithResultQueued 상태로 유지하지 않도록 수정(PR #3153, @bansiesta).

릴리스 노트에 그 이상의 설명은 없다.

## 관련 개념

- [[mavsdk-v4-0-4]] — 직전 패치(discovery 수정)
- [[mavsdk]] — MAVSDK 개요
- [[mavlink-protocol]] — MAVLink 프로토콜
- [[mavsdk-v4-0-6]] — 다음 패치(JNI `-Xcheck:jni` 테스트)^[inbox/processed/fetch-2026-10-09-mavsdk.md]
