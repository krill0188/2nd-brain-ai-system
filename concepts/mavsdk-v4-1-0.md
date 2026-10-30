---
title: "MAVSDK v4.1.0 Release"
created: 2026-10-28
updated: 2026-10-28
type: concept
domain: comms-protocol
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-10-28-mavsdk.md]
confidence: low
contested: false
contradictions: []
---

# MAVSDK v4.1.0 Release

2026-10-27 릴리스. 이번 노트는 ArduPilot 호환성 보강과 MAVLink 프로토콜 처리 개선이 중심이다(수집본은 목록 끝이 잘려 있어 일부 항목이 누락됐을 수 있다).^[inbox/processed/fetch-2026-10-28-mavsdk.md]

## ArduPilot 호환
- ArduCopter에서 RTL 고도 지원(action), hold 비행 모드에 Brake 사용, 위치 health를 EKF 상태에서 가져오도록 변경(telemetry).
- 미션: ArduPilot용 `MAV_CMD_MISSION_START` 전송, 다운로드 시 `MAV_FRAME_GLOBAL_RELATIVE_ALT` 허용, Mission Planner 가져오기 때 terrain frame의 lat/lon 스케일 수정(mission_raw).
- 미션·지오펜스·`DO_REPOSITION`에서 non-`_INT` `MAV_FRAME` 표기 전송.

## 프로토콜·코어
- **MAVLink 32비트 sysid 지원**(PR #3041).
- `mavlink_direct`에 명령 송수신 추가, wrapper에 mavlink direct server 추가.
- IN_PROGRESS 응답 이후 명령 재전송 중단; FTP burst 다운로드 gap을 제한해 무한 할당 방지; 누락 이미지 추적 수 상한(camera); 로그 파일 다운로드 취소(log_files).

## 빌드·도구
Ubuntu 26.04(GCC 15, clang 21)로 이전, 전체 재생성 스크립트 추가, aarch64 wheel을 manylinux_2_28로 빌드, MSVC 의존성 병렬 빌드, Python 래퍼의 콜백 trampoline 유지·C++ 기본값 사용, 보안 정책 추가.

## 관련 문서
- [[mavsdk-v4-0-6]] — 직전 패치
- [[mavsdk]] — MAVSDK 개요
- [[mavlink-protocol]] — MAVLink 프로토콜
- [[ardupilot]] — ArduPilot
