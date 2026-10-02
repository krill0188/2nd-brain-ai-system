---
title: "MAVSDK v4.0.1 Release"
created: 2026-09-29
updated: 2026-10-02
type: concept
domain: comms-protocol
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-09-29-mavsdk.md]
confidence: medium
contested: false
contradictions: []
---

# MAVSDK v4.0.1 Release

2026-09-28 릴리스된 [[mavsdk-v4-0-0]] 이후 첫 패치 버전. Python 바인딩 안정성과 FTP 플러그인
버그를 수정한 유지보수 릴리스다.^[inbox/processed/fetch-2026-09-29-mavsdk.md]

## 주요 변경사항

- **Python `destroy()` 동시성 안전성**: 동시 호출에도 안전하도록 `destroy()` 구현 수정.
- **Configuration 재사용 가능**: `Mavsdk` 생성 이후에도 `Configuration` 객체를 계속 사용할 수
  있도록 수정.
- **FTP 타임아웃 시퀀스 번호 보존**: `ftp` 플러그인에서 요청이 타임아웃되어도 요청 시퀀스
  번호를 보존하도록 수정(버그 픽스).
- **MavlinkDirect 커스텀 메시지 예제 추가**: Python 예제로 커스텀 메시지 송수신 사용법 문서화.
- **문서/CI 개선**: README에 바인딩 설명 추가, Python wheel 빌드를 최적화 모드로 전환.

## 영향

v4.0.0에서 도입된 신규 Python 바인딩을 실제 서비스에 적용할 때 문제였던 동시 `destroy()`
호출과 `Configuration` 재사용 제약이 해소돼, 컴패니언 컴퓨터/GCS 소프트웨어의 MAVSDK-Python
통합 안정성이 개선된다. FTP 타임아웃 시퀀스 버그 수정은 파일 전송 재시도 로직의 신뢰성에
직접 영향을 준다.

## 관련 개념

- [[mavsdk]] — MAVSDK 개요 페이지
- [[mavsdk-v4-0-0]] — 직전 메이저 릴리스(breaking change, 신규 바인딩)
- [[mavsdk-v4-0-3]] — 후속 패치 릴리스(Python/Kotlin 바인딩 핸들 수명 버그 수정)
- [[mavlink-protocol]] — MAVLink 프로토콜
