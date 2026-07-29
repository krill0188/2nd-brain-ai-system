---
title: MAVLink Advanced Features
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, mavlink, mavlink2, security, signing, ras, rtps, advanced]
sources: []
confidence: medium
domain: comms-protocol
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# MAVLink Advanced Features

MAVLink 2.0, 보안 서명, Reliable ACK, RTPS 등 MAVLink 고급 기능. 상업용/군용 드론 배포를 위한 필수 기술.

## MAVLink 1 vs MAVLink 2

### Packet Structure

```
MAVLink 1: 8 bytes header + payload + 2 bytes checksum
MAVLink 2: 10 bytes header + payload + 2 bytes checksum + signature (optional)

Header differences:
- MAVLink 1: 0xFE
- MAVLink 2: 0xFD
- MAVLink 2: Incompatibility/Compatibility flags
```

### Key Differences

| Feature | MAVLink 1 | MAVLink 2 |
|---------|-----------|-----------|
| **ID space** | 0-255 | 0-16777215 (24-bit) |
| **Signed messages** | No | Yes |
| **Extensions** | Limited | Flexible |
| **Empty byte truncation** | No | Optional |
| **Compatibility** | Legacy | Modern standard |

### Migration

```c
// PX4 auto-negotiates
// GCS sends MAVLink 1 capability → Use v1
// GCS sends MAVLink 2 capability → Use v2 with signing if available

// Force MAVLink 2
MAVLINK_STX = 253;  // 0xFD
```

## Message Signing

### Signing Process

```
Message + Secret Key → HMAC-SHA256 → Signature (6-13 bytes)

┌─────────────────────────────────────────────────────┐
│ Header │ Payload │ CRC │ Flags │ Timestamp │ LinkID │ Sig │
└─────────────────────────────────────────────────────┘
                                      └── HMAC ──┘
```

### Key Management

| Aspect | 방법 |
|--------|------|
| **Key distribution** | Pre-shared key (PSK) |
| **Key rotation** | Manual re-pairing |
| **Storage** | Secure element recommended |
| **Lifetime** | Session or permanent |

### PX4 Signing Setup

```bash
# Key configuration
param set MAV_SIK_KEY "hex_key_here"

# Require signing
param set MAV_SIK_ENFORCE 1

# Timestamp tolerance (ms)
param set MAV_SIK_TIMEOUT 100
```

### Security Benefits

| Attack | Protection |
|--------|------------|
| **Replay** | Timestamp + incrementing seq |
| **Injection** | Signature verification |
| **Spoofing** | Key-based auth |
| **MITM** | Requires key possession |

## Reliable ACK (RAS)

### Need for Reliability

```
Standard MAVLink: Unreliable, no ordering guarantee
Problem: Command execution, mission upload

RAS: MAVLink over reliable transport
```

### RAS Transport Options

| Layer | Protocol | Use Case |
|-------|----------|----------|
| **Serial** | None (no RAS) | Local, trusted |
| **TCP** | Built-in reliable | Ethernet, WiFi |
| **UDP** | Custom retry | Low latency |
| **RTPS** | DDS reliability | ROS2 integration |

### Custom Ack Pattern

```python
# Command with explicit ack
command_long = CommandLong(
    target_system=1,
    target_component=1,
    command=MAV_CMD_NAV_TAKEOFF,
    confirmation=0
)

# Wait for COMMAND_ACK
ack = await asyncio.wait_for(
    ack_future, timeout=5.0
)

if ack.result == MAV_RESULT_ACCEPTED:
    print("Command executed")
```

## Micro-RTPS Agent

### uXRCE-DDS Bridge

PX4 ↔ DDS ↔ ROS2 통합에서 사용.

```
PX4 (uORB) <-> uXRCE-DDS Client <-> Agent <-> ROS2 (DDS)
```

### Setup

```bash
# Agent build
git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
cd Micro-XRCE-DDS-Agent
mkdir build && cd build
cmake .. && make

# Run agent
MicroXRCEAgent udp4 -p 8888
```

### DDS Topics

| Direction | Topic | Description |
|-----------|-------|-------------|
| PX4 → ROS2 | SensorCombined | Raw sensors |
| ROS2 → PX4 | VehicleCommand | Command input |
| PX2 → ROS2 | VehicleAttitude | Estimated attitude |
| ROS2 → PX4 | OffboardControlMode | External control |

## MAVLink Router

### Multi-endpoint Routing

```
MAVLink Router: 1 input → N outputs

Example:
FC (UART) → Router ─┬─→ QGC (UDP)
                    ├─→ Companion (TCP)
                    └─→ Logger (file)
```

### Configuration

```ini
# mavlink-router.conf
[General]
TcpServerPort=5760
ReportStats=false

[UartEndpoint fc]
Device=/dev/ttyS1
Baud=921600

[UdpEndpoint qgc]
Mode=Server
Address=0.0.0.0
Port=14550

[UdpEndpoint companion]
Mode=Normal
Address=192.168.1.100
Port=14540
```

## MAVLink Tunneling

### Encapsulated Protocols

| Protocol | ID | Use |
|----------|-----|-----|
| **GPS_RTCM_DATA** | 233 | RTK corrections |
| **SERIAL_CONTROL** | 126 | Serial passthrough |
| **PLAY_TUNNEL** | 141 | Custom tunnel |
| **TUNNEL** | 385 | Generic tunnel |

### Serial Passthrough

```
MAV_CMD_SERIAL_CONTROL:
- device = SERIAL_CONTROL_DEV_GPS1
- flags = SERIAL_CONTROL_FLAG_REPLYWAIT
- timeout = 1000ms
- baudrate = 0 (don't change)
- count = N bytes
- data[N] = payload
```

## High-latency Links

### Challenges

| Link Type | Latency | Issues |
|-----------|---------|--------|
| **Satellite** | 500-2000ms | RTT, jitter |
| **Long-range RF** | 50-500ms | Packet loss |
| **Cellular** | 100-1000ms | Variable |

### Mitigation Strategies

```
1. Command buffering
2. State prediction
3. Adaptive timeouts
4. Reduced frequency
5. Critical command prioritization
```

### MAVLink High Latency Mode

```
HIGH_LATENCY2 message:
- Reduced update rate (1Hz)
- Critical data only
- Heartbeat extension
```

## Message Packing Optimization

### Efficient Packing

```python
# MAVLink 2: Truncate zero-bytes at end
# Pack fields in order of size (largest first)

# Bad: uint8_t, uint64_t (5 bytes padding)
# Good: uint64_t, uint8_t (no padding)

msg = custom_message_encode(
    uint64_field,  # 8 bytes
    uint32_field,  # 4 bytes
    uint16_field,  # 2 bytes
    uint8_field    # 1 byte
)
```

### Array Handling

```
Fixed arrays: Compile-time known
Variable arrays: Length prefix

MAVLink 2: Empty trailing bytes truncated
```

## Time Synchronization

### Synchronizing Multiple Systems

```
TIMESYNC message:
tc1: Time sync request timestamp (local)
ts1: Time sync response timestamp (local)

RTT = ts1 - tc1
Offset = (remote_time - local_time)

Algorithm:
1. Send TIMESYNC
2. Record local tx time
3. Peer records rx, tx response
4. Calculate offset
```

### Distributed Systems

| Component | Time Source |
|-----------|-------------|
| **FC** | RTC, GPS |
| **GCS** | System clock |
| **Camera** | Trigger timestamp |
| **Lidar** | Scan timestamp |

## MAVLink FTP

### File Transfer Over MAVLink

```
FILE_TRANSFER_PROTOCOL message:
- Target network: MAV_COMP_ID_MISSIONPLANNER
- Payload: FTP request/response

Operations:
- Open file
- Read bytes
- Write bytes  
- Remove file
- List directory
Truncate file
```

### Use Cases

1. **Mission upload/download** — .plan files
2. **Log retrieval** — ULog files
3. **Parameter files** — .params
4. **Firmware update** — Binary upload

## Protocol Version Negotiation

### Auto-detection

```
1. GCS sends HEARTBEAT with version
2. Drone responds with capability
3. Both downgrade if needed

Priority:
- If both support v2 → Use v2
- Else → Use v1
```

### Capability Flags

```c
MAV_PROTOCOL_CAPABILITY_MAVLINK2 = 1 << 8;
MAV_PROTOCOL_CAPABILITY_FTP = 1 << 7;
MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET = 1 << 5;
```

## Security Best Practices

1. **Use MAVLink 2 with signing**
2. **Rotate keys periodically**
3. **Validate timestamps**
4. **Rate limiting on commands**
5. **Secure key storage**
6. **Audit logging**

## 관련 개념

- [[mavlink-protocol]] — MAVLink 기초
- [[mavsdk]] — MAVSDK 고급 기능
- [[px4-offboard-control]] — Signed offboard
- [[ros2-drone-integration]] — RTPS bridge

## 수집 대상

- MAVLink 암호화 확장 (ChaCha20 등)
- 실제 보안 배포 사례
- Quantum-resistant signing
