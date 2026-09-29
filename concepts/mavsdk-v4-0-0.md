---
title: "MAVSDK v4.0.0 Release"
created: 2026-09-23
updated: 2026-09-23
type: concept
domain: comms-protocol
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-09-23-mavsdk.md]
confidence: medium
contested: false
contradictions: []
---

# MAVSDK v4.0.0 Release

2026-09-22 릴리스된 MAVSDK 메이저 버전. C++ API에 호환성 깨짐 변경(breaking change)이
포함되며, MavlinkDirect/MavlinkDirectServer 플러그인이 정식화(stabilize)되고 Python
바인딩이 새로 도입(기존 MAVSDK-Python에서 마이그레이션 필요)되며 C·Kotlin 바인딩이
신규 추가됐다.^[inbox/processed/fetch-2026-09-23-mavsdk.md]

## 주요 변경사항

- **C++ API 변경**: 기존 v3 대비 호환성이 깨지는 API 변경 포함(공식 마이그레이션 가이드 참고).
- **MavlinkDirect / MavlinkDirectServer 플러그인 정식화**: 저수준 MAVLink 메시지 직접
  송수신 플러그인이 experimental 단계를 벗어났다.
- **신규 언어 바인딩**: Python 바인딩 전면 재작성(기존 MAVSDK-Python과 별도 마이그레이션
  가이드 제공), C 바인딩, Kotlin 바인딩이 새로 추가됐다.
- **코어 개선**: `set_callback_executor` API로 콜백 디스패치 커스터마이징 지원, 빈 미션
  조회 시 빈 결과 반환 수정, 현재 미션 아이템 설정 버그 수정, 미션 전송 WorkItem 소멸자
  데이터 레이스 수정 등.

## 영향

기존 v3 기반 C++ 통합은 마이그레이션 가이드 검토가 필요하며(해석), Python 사용자는
기존 MAVSDK-Python에서 신규 바인딩으로 이전 작업이 요구된다. GCS/컴패니언 컴퓨터
소프트웨어가 MAVSDK에 의존하는 경우 업그레이드 전 breaking change 목록 확인이 필요하다.

## 한계

수집 원문이 "What's Changed" PR 목록 도중 잘려 있어 전체 변경 항목·구체적 breaking
change 목록은 원문 링크(mavsdk.mavlink.io)에서 추가 확인이 필요하다.

## 관련 개념

- [[mavsdk]] — MAVSDK 개요 페이지
- [[mavlink-protocol]] — MAVLink 프로토콜
- [[px4-offboard-control]] — PX4 Offboard 제어
