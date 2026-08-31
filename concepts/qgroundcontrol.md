---
title: QGroundControl
created: 2026-07-29
updated: 2026-09-01
type: concept
tags: [drone, drone-sw, gcs-software]
sources: [inbox/fetch-2026-07-29-qgroundcontrol.md, inbox/fetch-2026-09-01-qgroundcontrol.md]
confidence: high
contested: false
contradictions: []
---

# QGroundControl

QGroundControl(QGC)는 MAVLink 프로토콜을 사용하는 드론을 위한 오픈소스 지상 통제 소프트웨어(GCS)이다. PX4와 ArduPilot을 모두 지원하며, 크로스 플랫폼(Windows, macOS, Linux, Android, iOS)에서 실행된다.

## 핵심 기능

- **미션 계획**: 직관적인 웨이포인트 편집, 설문(Survey) 패턴 생성
- **비행 모니터링**: 실시간 비행 데이터, 지도상 기체 위치 표시
- **설정/캘리브레이션**: 센서 캘리브레이션, 펌웨어 업데이트
- **비행 모드 전환**: 수동/자동 모드 간 실시간 전환

## 릴리스 이력

### v5.1.4 (2026-08-30)

- **HUD 피치 표시 수정**: nose-down 시 pitch indicator가 아래로 이동 (roll convention 일치) ^[inbox/fetch-2026-09-01-qgroundcontrol.md]
- **PlanView**: Land/Alt Land 도구가 rover에 대해 RTL을 삽입하는 문제 수정
- **Comms**: 링크 워커 스레드 종료 시 정리 개선
- **Video**: H.265 녹화 안정성 강화
- **PX4**: UAVCAN ESC enumeration 제거 (v1.17+ PD_GRIPPER_TYPE 그리퍼 감지)
- **APM**: 모터 PWM 파라미터 없을 때 ESC 컴포넌트 스킵

### v5.0.8 (2025-10-09)

- **macOS 서명**: 앱 번들 서명, 공증(Notarization), 스테이플링 지원
- **Android SD 카드**: Android 11+(API 30+) SD 카드 권한 수정
- **버그 수정**: 
  - allLinksRemoved 이중 시그널로 인한 크래시 수정
  - Linux 마우스 휠 맵 줌 수정
  - 거리 센서 최소값 FactGroup 수정
  - Remote ID 도구바 드롭다운 닫기 수정
  - Vehicle 종료 시 CameraManager null 포인터 크래시 수정

## 관련 개념

- [[px4-flight-stack]] — QGC가 기본 지원하는 비행 스택
- [[mavlink-protocol]] — QGC가 사용하는 통신 프로토콜
- [[mission-planner]] — ArduPilot 중심의 대안 GCS
- [[ground-control-station]] — GCS 개념 개요
