---
source_url: "file://MasterVault/Drone/Protocol/MAVLink-Reference.md"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "Master (personal dev notes)"
sha256: "6d9f3e7a2c5b8d4e1f6a9b3c7d2e5f8a1b4c7d9e2f5a8b1c4d7e9f2a5b8c1d4"
tags: [datalink, drone-sw]
---

# MAVLink 프로토콜 레퍼런스

## 패킷 구조 (v2)

```
STX | LEN | INC | CMP | SEQ | SYS | COMP | MSG_ID(3B) | PAYLOAD | CRC | SIG(opt)
0xFD  len  flags  comp  seq   sys   comp   msg_id       data      crc   signature
```

## 핵심 메시지

| MSG_ID | 이름 | 용도 |
|--------|------|------|
|| 0 | HEARTBEAT | 연결 유지, 기체 타입/상태 |
|| 1 | SYS_STATUS | 배터리, 센서 상태 |
|| 24 | GPS_RAW_INT | GPS 원시 데이터 |
|| 30 | ATTITUDE | Roll/Pitch/Yaw |
|| 33 | GLOBAL_POSITION_INT | 위치 (lat/lng/alt) |
|| 76 | COMMAND_LONG | 명령 전송 |
|| 77 | COMMAND_ACK | 명령 응답 |

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
