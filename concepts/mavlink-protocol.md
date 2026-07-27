---
title: MAVLink Protocol
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, datalink, MAVLink, communication]
sources: [raw/articles/mastervault-mavlink-reference.md, raw/articles/mavlink-xml-schema.md, raw/articles/px4-mavlink.md]
confidence: high
contested: false
contradictions: []
---

# MAVLink Protocol

MAVLink는 드론과 지상국, 외부 구성요소 간 효율적인 데이터 교환을 위한 경량 통신 프로토콜이다. PX4, ArduPilot 등 주요 펌웨어에서 표준으로 사용된다.^[raw/articles/px4-mavlink.md]

## 패킷 구조 (v2)

```
STX | LEN | INC | CMP | SEQ | SYS | COMP | MSG_ID(3B) | PAYLOAD | CRC | SIG(opt)
0xFD  len  flags  comp  seq   sys   comp   msg_id       data      crc   signature
```

| 필드 | 설명 |
|------|------|
| **STX** | 시작 바이트 (0xFD for v2) |
| **LEN** | 페이로드 길이 |
| **INC** | 호환성 플래그 |
| **CMP** | 컴포지션 플래그 |
| **SEQ** | 시퀀스 번호 (무결성 체크) |
| **SYS** | 시스템 ID |
| **COMP** | 컴포넌트 ID |
| **MSG_ID** | 메시지 ID (3바이트, v2) |
| **PAYLOAD** | 데이터 |
| **CRC** | 체크섬 |
| **SIG** | 서명 (선택적, 보안) |

## 핵심 메시지

| MSG_ID | 이름 | 용도 |
|--------|------|------|
| 0 | **HEARTBEAT** | 연결 유지, 기체 타입/상태 |
| 1 | **SYS_STATUS** | 배터리, 센서 상태 |
| 24 | **GPS_RAW_INT** | GPS 원시 데이터 |
| 30 | **ATTITUDE** | Roll/Pitch/Yaw |
| 33 | **GLOBAL_POSITION_INT** | 위치 (lat/lng/alt) |
| 76 | **COMMAND_LONG** | 명령 전송 |
| 77 | **COMMAND_ACK** | 명령 응답 |

## Microservices (상위 프로토콜)

MAVLink 메시지 위에 구축된 고수준 프로토콜.^[raw/articles/px4-mavlink.md]

| 서비스 | 설명 |
|--------|------|
| **Command Protocol** | 확인 응답이 있는 명령 (MAV_CMD) |
| **File Transfer Protocol** | 파일 전송 |
| **Camera Protocol** | 카메라 제어 |
| **Parameter Protocol** | 파라미터 읽기/쓰기 |
| **Mission Protocol** | 웨이포인트 미션 전송 |

### 미션 프로토콜 흐름

```
GCS → MISSION_COUNT → FC
FC  → MISSION_REQUEST_INT → GCS (반복)
GCS → MISSION_ITEM_INT → FC (반복)
FC  → MISSION_ACK → GCS
```

### 파라미터 프로토콜 흐름

```
GCS → PARAM_REQUEST_LIST → FC
FC  → PARAM_VALUE → GCS (n회 반복)
```

## XML 스키마

MAVLink 정의는 계층적 XML 파일로 표준화된다.^[raw/articles/mavlink-xml-schema.md]

| 파일 | 내용 |
|------|------|
| **minimal.xml** | 최소 필요 정의 |
| **standard.xml** | 널리 구현된 정의 |
| **common.xml** | 일반적인 UAV 사용 사례 (PX4 기본값) |
| **development.xml** | 테스트 중인 제안 표준 |

### XML 구조

```xml
<?xml version="1.0"?>
<mavlink>
    <include>common.xml</include>
    <dialect>8</dialect>
    <enums>...</enums>
    <messages>...</messages>
</mavlink>
```

## pymavlink 사용

```python
from pymavlink import mavutil

# 연결
conn = mavutil.mavlink_connection('udp:127.0.0.1:14550')
conn.wait_heartbeat()

# 시동
conn.mav.command_long_send(
    conn.target_system, conn.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0, 1, 0, 0, 0, 0, 0, 0)

# 메시지 수신
msg = conn.recv_match(type='ATTITUDE', blocking=True)
print(f"Roll: {msg.roll:.2f}")
```

## 보안 고려사항

> **경고**: MAVLink 메시지는 기본적으로 인증되지 않는다.^[raw/articles/px4-mavlink.md]

- 메시지 서명 구현 필요
- 보안 강화 가이드라인 준수
- 무단 명령 실행 방지

## PX4 구현

PX4는 MAVLink 저장소를 서브모듈로 포함한다.^[raw/articles/px4-mavlink.md]

| 설정 | 설명 |
|------|------|
| `CONFIG_MAVLINK_DIALECT` | 보드별 dialect 선택 |
| 빌드 시스템 | MAVLink 2 C 헤더 파일 생성 |
| 기본 dialect | `common.xml` |

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 구성
- [[ardupilot-architecture]] — ArduPilot 아키텍처
- [[ground-control-station]] — GCS 연동
- [[ros2-drone-integration]] — ROS2 브릿지
