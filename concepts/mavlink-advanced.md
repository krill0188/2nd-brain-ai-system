---
title: MAVLink Advanced Features
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, datalink, mavlink, mavlink2, security, signing, advanced]
sources: []
confidence: medium
domain: comms-protocol
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# MAVLink Advanced Features

MAVLink 2는 MAVLink 1의 확장으로 더 큰 메시지, 더 많은 필드, 그리고 보안 기능을 제공한다. 현대 드론 시스템에서 필수적인 프로토콜이다.

## MAVLink 1 vs MAVLink 2

| Feature | MAVLink 1 | MAVLink 2 |
|---------|-----------|-----------|
| **Packet size** | 263 bytes max | 65507 bytes max |
| **Fields** | 64 max | 128 max |
| **Field types** | Limited | Extended (uint64, etc.) |
| **Signing** | ❌ | ✅ |
| **Compatibility** | Legacy | Modern |
| **Wire format** | v1.0 | v2.0 (different) |

## MAVLink 2 Packet Format

```
┌─────────────────────────────────────────┐
│ 0 │ Magic (0xFD for v2)               │
│ 1 │ Length (payload)                    │
│ 2 │ Incompatibility flags              │
│ 3 │ Compatibility flags                │
│ 4 │ Sequence                           │
│ 5 │ System ID                          │
│ 6 │ Component ID                       │
│ 7-9 │ Message ID (3 bytes)             │
│ 10 │ Target System (optional)          │
│ 11 │ Target Component (optional)       │
│ 12+ │ Payload                          │
│ ... │ Checksum (2 bytes)               │
└─────────────────────────────────────────┘
```

## Incompatibility Flags

| Flag | Value | Description |
|------|-------|-------------|
| **MAVLINK_IFLAG_SIGNED** | 0x01 | Packet is signed |
| **Reserved** | 0xFE | Future use |

## Message Extensions

### Extended Fields

```xml
<!-- common.xml -->
<message id="33" name="GLOBAL_POSITION_INT">
    <description>The filtered global position</description>
    <field type="int32_t" name="lat">Latitude</field>
    <field type="int32_t" name="lon">Longitude</field>
    <field type="int32_t" name="alt">Altitude</field>
    <!-- MAVLink 2 extensions -->
    <field type="uint16_t" name="eph">GPS HDOP</field>
    <field type="uint16_t" name="epv">GPS VDOP</field>
</message>
```

### Array Support

```xml
<field type="float[16]" name="q">Attitude quaternion</field>
<field type="int16_t[6]" name="torque">Joint torques</field>
```

## Message Signing

### Security Model

```
Authentication: ✅ (HMAC-SHA256)
Encryption: ❌ (not provided)
Replay protection: ✅ (timestamp)
```

### Signing Process

```
1. Generate timestamp (boot time)
2. Compute HMAC-SHA256:
   HMAC(key, packet_without_signature + timestamp)
3. Append 6-byte signature:
   - 4 bytes: HMAC digest (truncated)
   - 2 bytes: timestamp (LSB)
```

### Setup

```python
from pymavlink import mavutil

# Enable signing
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
master.setup_signing(
    secret_key=b'my_secret_key_32_bytes_long!!!!!',
    initial_timestamp=0,
    link_id=0
)
```

### Key Management

| Aspect | Recommendation |
|--------|---------------|
| **Key generation** | Random 32 bytes |
| **Key distribution** | Secure channel (pre-shared) |
| **Key rotation** | Per-session or periodic |
| **Storage** | Hardware security module |

## Routing

### Component IDs

| ID | Component |
|----|-----------|
| 1 | Autopilot |
| 190 | GCS |
| 191 | Onboard computer |
| 195 | Camera |
| 196 | Gimbal |
| 240-254 | OEM components |

### Target Routing

```python
# Send to specific target
master.mav.command_long_send(
    target_system=1,      # Drone 1
    target_component=1,   # Autopilot
    command=mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    confirmation=0,
    param1=0, param2=0, param3=0,
    param4=0, param5=0, param6=0,
    param7=10  # Altitude
)
```

## Stream Multiplexing

### Multiple Links

```
┌─────────────────────────────────────────┐
│           MAVLink Router              │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │ Serial  │ │  UDP    │ │  TCP    │   │
│  │ /dev/tty│ │ 14550   │ │ 5760    │   │
│  └────┬────┘ └────┬────┘ └────┬────┘   │
│       └───────────┼───────────┘        │
│                   │                     │
│              ┌────┴────┐                │
│              │  Core   │                │
│              │ Routing │                │
│              └────┬────┘                │
└───────────────────┼─────────────────────┘
                    │
            ┌───────┴───────┐
            ▼               ▼
        ┌──────┐       ┌──────┐
        │ FC   │       │ GCS  │
        └──────┘       └──────┘
```

### MAVLink Router

```bash
# Install
sudo apt install mavlink-router

# Config (/etc/mavlink-router/main.conf)
[General]
TcpServerPort=5760

[UartEndpoint fc]
Device = /dev/ttyACM0
Baud = 921600

[UdpEndpoint gcs]
Mode = Normal
Address = 192.168.1.100
Port = 14550
```

## Message Coalescing

### Batch Transmission

```python
# Multiple messages in single packet
messages = [
    heartbeat_msg,
    attitude_msg,
    position_msg
]

# Send as batch
master.mav.send(messages)
```

### Timing Optimization

| Message | Rate | Priority |
|---------|------|----------|
| HEARTBEAT | 1 Hz | Critical |
| ATTITUDE | 50 Hz | High |
| POSITION | 10 Hz | High |
| BATTERY | 1 Hz | Medium |
| GPS_RAW_INT | 5 Hz | Medium |

## Custom Dialects

### Creating Dialect

```xml
<!-- mycompany.xml -->
<?xml version="1.0"?>
<mavlink>
    <include>common.xml</include>
    <messages>
        <message id="5000" name="MY_COMPANY_STATUS">
            <description>Custom status message</description>
            <field type="uint32_t" name="custom_field1">Custom data</field>
            <field type="float" name="custom_field2">More data</field>
        </message>
    </messages>
</mavlink>
```

### Generation

```bash
# Generate headers
mavgen.py --lang=C --wire-protocol=2.0 mycompany.xml

# Python
mavgen.py --lang=Python --wire-protocol=2.0 mycompany.xml
```

## Advanced Commands

### Command Long vs Command Int

| Command | Use Case |
|---------|----------|
| **COMMAND_LONG** | float params, simple commands |
| **COMMAND_INT** | lat/lon/alt, geospatial commands |

### Command Int Example

```python
# Navigate to GPS coordinate
master.mav.command_int_send(
    target_system=1,
    target_component=1,
    frame=mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
    command=mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
    current=0,
    autocontinue=1,
    param1=0,  # Hold time
    param2=0,  # Acceptance radius
    param3=0,  # Pass through
    param4=0,  # Yaw
    x=int(37.5665 * 1e7),  # Lat
    y=int(126.9780 * 1e7),  # Lon
    z=30.0  # Alt
)
```

## Parameter Protocol

### Transaction

```
GCS → FC: PARAM_REQUEST_LIST
FC → GCS: PARAM_VALUE (for each param)
...
GCS → FC: PARAM_SET
FC → GCS: PARAM_VALUE (ack)
```

### Parameter Types

| Type | Size | Range |
|------|------|-------|
| PARAM_TYPE_UINT8 | 1 byte | 0-255 |
| PARAM_TYPE_INT32 | 4 bytes | ±2e9 |
| PARAM_TYPE_REAL32 | 4 bytes | IEEE 754 float |

## Mission Protocol

### Upload Sequence

```
1. MISSION_COUNT (GCS → FC)
2. MISSION_REQUEST_INT (FC → GCS)
3. MISSION_ITEM_INT (GCS → FC)
4. ... (repeat for each item)
5. MISSION_ACK (FC → GCS)
```

### Download Sequence

```
1. MISSION_REQUEST_LIST (GCS → FC)
2. MISSION_COUNT (FC → GCS)
3. MISSION_REQUEST_INT (GCS → FC)
4. MISSION_ITEM_INT (FC → GCS)
5. ...
6. MISSION_ACK (GCS → FC)
```

## FTP Protocol

### File Transfer

```
Op codes:
- Create (Open for reading)
- Open (Open for writing)
- Read
- Write
- Remove
- Rename
```

### Usage

```python
# Download parameter file
master.mav.ftp_request(
    session=0,
    opcode=mavutil.mavlink.FTP_OP_READFILE,
    size=0,
    offset=0,
    name='/fs/microsd/parameters'
)
```

## Debugging

### Packet Inspection

```bash
# Wireshark filter
mavlink_proto

# MAVProxy
mavproxy.py --master=/dev/ttyACM0 --baudrate=921600

# pymavlink dump
python -m pymavlink.tools.mavlogdump flight.bin
```

### Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| **CRC error** | Version mismatch | Use same MAVLink version |
| **Dropped packets** | Buffer overflow | Reduce stream rate |
| **Timeout** | No heartbeat | Check connection |
| **Invalid message** | Bad dialect | Regenerate headers |

## Performance

| Metric | Target |
|--------|--------|
| **Latency** | < 50ms (local) |
| **Throughput** | 1000+ msg/sec |
| **CPU usage** | < 5% (embedded) |
| **RAM usage** | < 10KB (stack) |

## 관련 개념

- [[mavlink-protocol]] — MAVLink basics
- [[datalink-communication]] — Physical layer
- [[px4-offboard-control]] — Command usage
- [[mavsdk]] — High-level API

## 수집 대상

- MAVLink 3 draft specification
- Micro air vehicle swarm coordination
- Secure MAVLink implementations
