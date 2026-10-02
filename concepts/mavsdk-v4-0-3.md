---
title: "MAVSDK v4.0.3 Release"
created: 2026-10-02
updated: 2026-10-02
type: concept
domain: comms-protocol
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-10-02-mavsdk.md]
confidence: medium
contested: false
contradictions: []
---

# MAVSDK v4.0.3 Release

2026-10-01 릴리스된 MAVSDK v4.0.2의 후속 패치 버전으로, 예제 추가와 Python/Kotlin 바인딩의
핸들 수명(handle lifetime) 버그 수정을 포함한 유지보수 릴리스다.^[inbox/processed/fetch-2026-10-02-mavsdk.md]

## 주요 변경사항

- **MavlinkDirect 수신 예제 추가**: 커스텀/비표준 MAVLink 메시지를 직접 수신하는 예제 코드 제공.
- **system_tests 커스텀 메시지 ID 이동**: 테스트용 커스텀 메시지 ID를 공통(common) 범위 밖으로
  재배치해 표준 메시지 ID와의 충돌 가능성 제거.
- **Python 바인딩 핸들 수명 버그 수정**: 객체 핸들이 예기치 않게 해제되는 문제 수정.
- **Kotlin 바인딩 핸들 수명 버그 수정 및 첫 end-to-end 테스트 추가**: Kotlin 바인딩에도 동일한
  수명 버그를 수정하고, 회귀 방지를 위한 e2e 테스트 최초 도입.

## 영향

v4.0.0에서 도입된 신규 Python/Kotlin 바인딩의 안정성을 계속 개선하는 흐름의 연장선으로, 핸들
수명 버그는 장시간 구동되는 컴패니언 컴퓨터/GCS 통합 환경에서 메모리 접근 오류를 유발할 수
있었던 부분이다.

## 관련 개념

- [[mavsdk]] — MAVSDK 개요 페이지
- [[mavsdk-v4-0-1]] — 직전 패치 릴리스(Python destroy() 동시성, FTP 타임아웃 수정)
- [[mavlink-protocol]] — MAVLink 프로토콜
