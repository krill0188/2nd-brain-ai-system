---
title: "MAVLink Protocol Deep Dive — 메시지 구조와 마이크로서비스"
created: 2026-07-28
updated: 2026-07-28
type: concept
tags: [datalink, drone-sw]
sources:
  - inbox/processed/mastervault-mavlink-reference.md
  - inbox/processed/mavlink-xml-schema.md
  - inbox/processed/px4-mavlink.md
confidence: high
contested: false
contradictions: []
---

# MAVLink Protocol Deep Dive

MAVLink v2 패킷 구조, XML 스키마, 마이크로서비스 패턴의 심층 분석.

## 패킷 구조 (v2)

```
STX | LEN | INC | CMP | SEQ | SYS | COMP | MSG_ID(3B) | PAYLOAD | CRC | SIG(opt)
0xFD  len  flags  comp  seq   sys   comp   msg_id       data      crc   signature
```

## 핵심 메시지

| MSG_ID | 이름 | 용도 |
|--------|------|------|
| 0 | HEARTBEAT | 연결 유지, 기체 타입/상태 |
| 1 | SYS_STATUS | 배터리, 센서 상태 |
| 24 | GPS_RAW_INT | GPS 원시 데이터 |
| 30 | ATTITUDE | Roll/Pitch/Yaw |
| 33 | GLOBAL_POSITION_INT | 위치 (lat/lng/alt) |
| 76 | COMMAND_LONG | 명령 전송 |
| 77 | COMMAND_ACK | 명령 응답 |

## 프로토콜 패턴

### 미션 프로토콜
```
GCS → MISSION_COUNT → FC
FC  → MISSION_REQUEST_INT → GCS (반복)
GCS → MISSION_ITEM_INT → FC (반복)
FC  → MISSION_ACK → GCS
```

### 파라미터 프로토콜
```
GCS → PARAM_REQUEST_LIST → FC
FC  → PARAM_VALUE → GCS (n회 반복)
```

## XML 스키마 구조

### Core File Structure
```xml
<?xml version="1.0"?>
<mavlink>
    <include>common.xml</include>
    <dialect>8</dialect>
    <enums>...</enums>
    <messages>...</messages>
</mavlink>
```

### Enum 정의
```xml
<enum name="LANDING_TARGET_TYPE">
    <description>Type of landing target</description>
    <entry value="0" name="LANDING_TARGET_TYPE_LIGHT_BEACON">
        <description>Landing target signaled by light beacon</description>
    </entry>
</enum>
```

### 메시지 정의
- **id**: 0-255 (MAVLink 1); 0-16777215 (MAVLink 2)
- **name**: 식별자
- **extensions**: MAVLink 2 전용 필드 표시

## pymavlink 사용 예시

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

## 마이크로서비스

MAVLink 위에 구축된 고수준 프로토콜:
- **Command Protocol** — 확인 응답 기반 명령
- **File Transfer Protocol**
- **Camera Protocol**
- **Parameter Protocol**
- **Mission Protocol**

## 보안 고려사항

MAVLink 메시지는 기본적으로 인증되지 않음. 프로덕션 시스템은 메시지 서명과 보안 강화 가이드라인을 구현해야 함.

## 관련 페이지

- [[mavlink-protocol]] — MAVLink 개요
- [[mavsdk]] — 고수준 SDK
- [[ground-control-station]] — GCS 통합
