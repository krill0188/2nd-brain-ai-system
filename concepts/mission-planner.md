---
title: Mission Planner
created: 2026-07-29
updated: 2026-07-29
type: concept
tags: [drone, drone-sw, gcs-software]
sources: [inbox/fetch-2026-07-29-missionplanner.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# Mission Planner

Mission Planner은 ArduPilot 기반 드론을 위한 Windows용 지상 통제 소프트웨어(GCS)이다. Michael Oborne이 개발했으며, ArduPilot 프로젝트의 공식 GCS로 널리 사용된다.

## 핵심 기능

- **미션 계획**: 웨이포인트 기반 자동 비행 경로 설정
- **비행 모니터링**: 실시간 텔레메트리, HUD 디스플레이
- **설정/캘리브레이션**: 센서 캘리브레이션, 파라미터 조정
- **로그 분석**: 비행 로그 다운로드 및 분석

## 최신 릴리스: v1.3.83 (2025-09-10)

### 주요 개선사항

- **DroneCAN 지원**: 멀티캐스트 DroneCAN 기능 추가
- **지형 데이터**: 플러그인을 통한 지형 DAT 파일 생성
- **RTK/GPS 설정**: Septentrio 설정 오류 수정
- **UI 개선**: 배터리 셀 아이콘 표시 수정, 고도 프레임 지원
- **지역화**: 영국(UK) 지역화 개선

## 관련 개념

- [[ardupilot]] — Mission Planner가 지원하는 비행 스택
- [[ground-control-station]] — GCS 개념 개요
- [[qgroundcontrol]] — 대안적인 오픈소스 GCS
- [[dronecan-protocol]] — Mission Planner에서 지원하는 CAN 프로토콜
