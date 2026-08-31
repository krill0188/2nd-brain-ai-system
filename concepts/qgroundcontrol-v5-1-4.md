---
title: QGroundControl v5.1.4 Release Notes
created: 2026-09-01
updated: 2026-09-01
type: concept
tags: [drone, drone-sw, gcs-software, qgroundcontrol, release]
sources: [inbox/fetch-2026-09-01-qgroundcontrol.md]
confidence: high
contested: false
contradictions: []
---

# QGroundControl v5.1.4

QGroundControl v5.1.4는 v5.1 안정 릴리스로, HUD 피치 표시 수정 및 다양한 버그 수정을 포함한다.

## 주요 변경사항

### HUD 피치 표시 수정 (중요)

- **nose-down 시 pitch indicator가 아래로 이동**: roll convention과 일치하도록 수정
- [HUD 문서](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/fly_view/hud.html) 참고

### 버그 수정

| 영역 | 수정 내용 |
|------|----------|
| **PlanView** | Land 도구가 Land/Alt Land를 표시했으나 rover에 대해 RTL을 삽입하는 문제 수정 |
| **Comms** | 링크 워커 스레드가 종료 시에도 실행 중이던 문제 수정 |
| **Video** | 지연된 H.265 녹화 강화, elementary streams 파싱 후 녹화 |
| **AppSettings** | 페이지 축소 시 섹션 선택 정규화, 사용 불가능한 섹션 숨김 |
| **APM** | 모터 PWM 파라미터 없을 때 ESC 컴포넌트 스킵 |
| **PX4** | UAVCAN ESC enumeration 제거 (v1.17+ PD_GRIPPER_TYPE 그리퍼 감지) |
| **Joystick** | 실제 업데이트 속도가 설정과 일치하도록 수정 |
| **MissionController** | 비행 경로 세그먼트 캐시 재사용 조건이 반전된 문제 수정 |

### PX4 특화 수정

- PX4 튜닝 및 비디오 설정 레이블 오해 수정
- 전진 비행 goto loiter 반경에 raw meters 사용
- Power 설정에서 UAVCAN ESC enumeration 제거 (v1.17+)

### APM 특화 수정

- 이미 시동된 기체에 대한 미션 시작 수정
- 모터 PWM 파라미터 없을 때 ESC 컴포넌트 스킵

## 설치

[Download and Install](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/getting_started/download_and_install.html) 페이지에서 플랫폼별 설치 지침 참고.

## 관련 개념

- [[qgroundcontrol]] — QGroundControl 개요 페이지
- [[px4-flight-stack]] — PX4 비행 스택
- [[mavlink-protocol]] — MAVLink 프로토콜
