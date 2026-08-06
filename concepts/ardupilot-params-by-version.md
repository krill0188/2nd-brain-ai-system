---
title: "ArduPilot 버전별 주요 파라미터 변경점 (4.4~4.7)"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, flight-control, ardupilot, parameter, version]
sources: [ArduPilot 공식 릴리즈노트 기반 정리]
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# ArduPilot 버전별 주요 파라미터 변경점 (4.4~4.7)

ArduPilot(Copter/Plane/Rover)은 점 버전마다 파라미터 신설·기본값 변경이 잦다. Mission Planner의 **Compare Params** 기능으로 업그레이드 전후를 반드시 비교할 것. 보드별 설정은 [[fc-vendor-param-guide]] 참조. 아키텍처 배경은 [[ardupilot-architecture]] 참조.

## Copter/Plane 4.4 (2023)

- EKF3 단독 기본화 — `AHRS_EKF_TYPE=3`, EKF2 계열 파라미터 정리
- `BATT_*` 모니터 옵션 확장 (INA2xx I2C 전원센서 정식 지원)
- Harmonic Notch 표준화: `INS_HNTCH_*` — 김벌·프롭 진동 대응 필수 튜닝 항목화

## 4.5 (2024)

- `CAN_Dn_PROTOCOL` DroneCAN 명칭 정리 (UAVCAN→DroneCAN)
- `RC_PROTOCOLS` 비트마스크로 수신기 프로토콜 제한 가능
- Copter: `PILOT_THR_BHV` 등 스로틀 거동 세분화, AutoTune 개선

## 4.6 (2025)

- `FENCE_*` 지오펜스 다형 확장(복합 폴리곤), `AVOID_*` 통합 정리
- Scripting 확장: `SCR_ENABLE` 기본 메모리 상향, Lua 바인딩 추가
- `SERVOn_FUNCTION` 신규 기능 번호 다수 추가 (페이로드·짐발)

## Plane 4.7 (2026-07 릴리즈)

- QuadPlane VTOL 전환 로직 개선 관련 `Q_*` 파라미터 확장
- TECS 세부 게인 노출 확대 (`TECS_*`)
- 신규 보드 지원 추가에 따른 `BRD_*` 옵션 증가
- 일부 기본값 변경 — 업그레이드 후 **Full Parameter List에서 노란색(비기본값) 항목 검토** 권장

## 업그레이드 체크리스트

1. Mission Planner → Full Parameter List → **Save to file** (기체별 백업)
2. 펌웨어 업그레이드 (같은 기체 유형 내 점 버전은 파라미터 유지됨)
3. 메시지 탭의 "param XXX deprecated/renamed" 경고 해소
4. Compare Params로 백업 대비 변경 항목 검토 → 시험 비행

## 공식 참조

- 릴리즈노트: https://github.com/ArduPilot/ardupilot/releases
- 전체 파라미터(버전별): https://ardupilot.org/copter/docs/parameters.html
