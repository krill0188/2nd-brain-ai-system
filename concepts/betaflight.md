---
title: Betaflight
created: 2026-07-29
updated: 2026-08-03
type: concept
tags: [drone, drone-sw, flight-control]
sources: [inbox/fetch-2026-07-29-betaflight.md, inbox/fetch-2026-08-03-betaflight.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# Betaflight

Betaflight는 FPV(First Person View) 드론과 소형 레이싱 드론을 위한 오픈소스 비행 제어 소프트웨어이다. 주로 멀티콥터에 사용되며, 직관적인 설정 인터페이스와 높은 커스터마이징 가능성으로 인해 FPV 커뮤니티에서 널리 사용된다.

## 핵심 특징

- **실시간 설정**: Betaflight Configurator를 통해 GUI 기반 설정 가능
- **PID 튜닝**: 고급 PID 제어기 설정으로 비행 특성 미세 조정
- **안전 기능**: Arming 조건, failsafe, 모터 정지 등 다양한 안전 메커니즘
- **하드웨어 호환성**: 다양한 FC(Flight Controller) 보드 지원

## 최신 릴리스 (2026.6.1)

2026년 8월 2일 릴리스된 2026.6.1 버전의 주요 변경사항:

### 신규 기능
- **LED 기능 확장**: GPS 바, 배터리 바, 고도 바 표시
- **S-term (Wing)**: 고정익용 S-term 제어
- **Altitude Hold**: 고도 유지 모드 (4.6 버전용)
- **Position Hold**: 위치 유지 모드
- **Auto-disarm**: 착륙 충격 감지 시 자동 시동 해제
- **Collision Detection**: 충돌 감지 기능
- **Virtual Blackbox**: SITL용 가상 블랙박스
- **Servo Logging**: 블랙박스에 서보 데이터 기록

### 개선사항
- **MSP 개선**: gyro_cal_on_first_arm, RSSI dBm 알람, CLI 패스스루 지원
- **Wing 지원**: TPA 공속 추정, 요 타입 러더/차분추력, PDS+Wing 설정점 감쇠
- **OSD**: Blackbox 저장 모드 액션 추가
- **디버깅**: DEBUG_TASK 모드, PRBS FLASH 테스트
- **카메라**: CADDX GM3 짐벌 드라이버

## 관련 개념

- [[flight-controller-hardware]] — Betaflight가 실행되는 FC 하드웨어
- [[drone-safety-failsafe]] — Arming 및 failsafe 메커니즘
- [[px4-flight-stack]] — Betaflight와 비교되는 다른 오픈소스 비행 스택
- [[edgetx-custom-audio]] — EdgeTX 라디오 설정
