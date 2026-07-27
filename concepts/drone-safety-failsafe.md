---
title: Drone Safety & Failsafe
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone, drone-sw, safety, failsafe, RTL, geofence]
sources: [raw/articles/px4-basic-concepts.md, raw/articles/px4-flight-modes-dev.md]
confidence: high
contested: false
contradictions: []
---

# Drone Safety & Failsafe

드론 안전 시스템은 비행 중 발생할 수 있는 위험 상황을 감지하고 자동으로 대응하여 기체와 주변을 보호하는 메커니즘이다. PX4와 ArduPilot은 다층적 failsafe 시스템을 제공한다.

## Failsafe 트리거 조건

| 조건 | 설명 | 기본 동작 |
|------|------|----------|
| **RC Loss** | 조종기 신호 상실 | Hold/RTL/Land |
| **GCS Loss** | 지상국 통신 단절 | Hold/RTL |
| **Low Battery** | 배터리 부족 | Warning → RTL → Land |
| **GPS Loss** | 위성 신호 상실 | Altitude Hold → Land |
| **Geofence Breach** | 비행 구역 이탈 | RTL/Hold |
| **Data Link Loss** | 텔레메트리 단절 | Hold |
| **EKF Error** | 상태 추정 오류 | Land |

## Return to Launch (RTL)

가장 중요한 안전 기능 중 하나로, 기체를 이륙 지점으로 자동 복귀시킨다.^[raw/articles/px4-basic-concepts.md]

### RTL 동작 순서

1. 현재 고도에서 Home position으로 수평 이동
2. 도착 후 상승/하강하여 RTL_ALT 도달
3. 수직 하강 후 착륙

### RTL 파라미터

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `RTL_ALT` | 복귀 고도 | 30m |
| `RTL_ALT_MIN` | 최소 복귀 고도 | 20m |
| `RTL_LOITER_TIME` | 착륙 전 대기 시간 | 5s |
| `RTL_CONE_DIST` | 콘 모양 경로 거리 | -1 (비활성) |

## Geofence (지오펜스)

비행 가능 영역을 지리적/고도적 제한으로 설정한다.

| 유형 | 설명 |
|------|------|
| **Circular** | 원형 반경 제한 |
| **Polygon** | 다각형 영역 제한 |
| **Altitude** | 최대 고도 제한 |
| **Cylinder** | 원통형 3D 제한 |

### Geofence 동작

- **Warning**: 경계 근접 시 경고
- **RTL**: 경계 침범 시 자동 복귀
- **Hold**: 위치 유지
- **Land**: 즉시 착륙

## Arming/Disarming

시동(Arming)은 모터와 액추에이터에 전원을 공급하는 상태다.^[raw/articles/px4-basic-concepts.md]

### Arming 조건

- GPS lock (자율 모드용)
- 센서 캘리브레이션 완료
- 배터리 충분
- RC/조이스틱 중립 위치
- EKF 수렴

### Arming 방법

| 방법 | 설명 |
|------|------|
| **RC Stick** | 모드2: 우측 스틱 우하단 1초 |
| **Switch** | 사전 설정 스위치 |
| **MAVLink** | `MAV_CMD_COMPONENT_ARM_DISARM` |
| **QGC** | GUI 버튼 |

## Low Battery Failsafe

배터리 전압 기반 자동 대응 시스템.

| 레벨 | 전압 | 동작 |
|------|------|------|
| **Warning** | ~3.7V/cell | 경고음/메시지 |
| **Critical** | ~3.5V/cell | RTL |
| **Emergency** | ~3.3V/cell | 즉시 착륙 |

## Mode Requirements & Restrictions

PX4는 각 모드에 필요한 조건을 `FailsafeFlags` uORB 토픽으로 정의한다.^[raw/articles/px4-flight-modes-dev.md]

```cpp
// src/modules/commander/ModeUtil/mode_requirements.cpp
mode_req_angular_velocity
mode_req_attitude
mode_req_local_alt
mode_req_local_position
mode_req_global_position
mode_req_mission
mode_req_offboard_signal
mode_req_home_position
mode_req_manual_control
```

## 안전 체크리스트

### Pre-flight

- [ ] 프로펠러 장착 확인
- [ ] 배터리 충전 상태
- [ ] GPS 위성 수 (8+)
- [ ] Compass 캘리브레이션
- [ ] RC 바인딩 확인
- [ ] Geofence 설정
- [ ] RTL 고도 확인
- [ ] failsafe 동작 테스트

### In-flight

- [ ] 배터리 전압 모니터링
- [ ] 통신 링크 상태
- [ ] GPS 신호 품질
- [ ] 고도/속도 제한 준수

## 관련 개념

- [[px4-flight-modes]] — 비행 모드와 failsafe 연동
- [[px4-offboard-control]] — Offboard 안전 고려사항
- [[swarm-coordination]] — 멀티 기체 안전
- [[flight-controller-hardware]] — 안전 관련 하드웨어
