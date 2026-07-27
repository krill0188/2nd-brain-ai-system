---
title: MAVLink 2 & Security
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, mavlink, mavlink2, security, signing, encryption, authentication]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# MAVLink 2 & Security

MAVLink 2는 MAVLink 1의 후속 버전으로 확장된 메시지 ID, 서명, 그리고 향상된 타입 시스템을 제공한다. 보안 기능으로 메시지 서명과 암호화를 지원한다.

## MAVLink 1 vs MAVLink 2

| 특성 | MAVLink 1 | MAVLink 2 |
|------|-----------|-----------|
| **Message ID** | 0-255 (8-bit) | 0-16777215 (24-bit) |
| **Payload size** | 최대 255바이트 | 최대 255바이트 |
| **Signing** | ❌ | ✅ |
| **Compatibility** | Legacy | Backward compatible |
| **Checksum** | CRC_EXTRA | CRC_EXTRA (변경사항) |
| **Header** | 6 bytes | 10 bytes |

## MAVLink 2 Header

```
┌──────────────────────────────────────────────────┐
│  MAVLink 2 Packet                              │
├──────────────────────────────────────────────────┤
│  MAGIC (1)       │ 0xFD (253)                    │
│  LEN (1)         │ Payload length                │
│  INC_FLAGS (1)   │ Incompatibility flags         │
│  COMP_FLAGS (1)  │ Compatibility flags           │
│  SEQ (1)         │ Packet sequence               │
│  SYS_ID (1)      │ System ID                     │
│  COMP_ID (1)     │ Component ID                  │
│  MSG_ID (3)      │ Message ID (24-bit, LE)       │
│  TARGET (2)      │ Target system/comp (optional) │
│  PAYLOAD (n)     │ Message data                  │
│  CHECKSUM (2)    │ CRC (CRC_EXTRA)               │
│  SIGNATURE (13)  │ Optional signature            │
└──────────────────────────────────────────────────┘
```

## Message ID Space

### MAVLink 1 (255 messages)

```
0-149: Common messages
150-230: ArduPilot extensions
231-255: Testing
```

### MAVLink 2 (16M messages)

```
0-255: Backward compatible
256-10000: Standard extensions
10000+: Vendor specific
```

### Dialect XML

```xml
<!-- common.xml -->
<message id="3001" name="MY_VENDOR_MSG">
    <description>Vendor specific message</description>
    <field type="uint32_t" name="custom_id">Custom ID</field>
    <field type="float[4]" name="data">Data array</field>
</message>
```

## Message Signing

### Signing Overview

```
HMAC-SHA256(secret_key, message)

Provides:
- 메시지 인증 (authenticity)
- 무결성 검증 (integrity)
- 재전공 방지 (replay protection with timestamp)
```

### Signing Process

```python
import hmac
import hashlib
from struct import pack

# 1. Timestamp (6 bytes, micros since Unix epoch / 1e6)
timestamp = int(time.time())
timestamp_bytes = pack('<Q', timestamp)[:6]

# 2. Link ID (1 byte)
link_id = 0  # Primary link

# 3. Create signature
signature_data = (
    header_bytes + 
    payload_bytes + 
    checksum_bytes + 
    pack('<BQ', link_id, timestamp)
)

signature = hmac.new(secret_key, signature_data, hashlib.sha256).digest()[:13]
```

### Setup

```bash
# PX4 signing configuration
param set MAV_PROTO_VER 2

# Secret key (32 bytes)
# Stored securely on vehicle
```

### GCS Signing Setup

| GCS | 설정 위치 |
|-----|----------|
| **QGroundControl** | Settings → MAVLink → Signing |
| **MAVProxy** | --signingkey |
| **Pymavlink** | sign_key parameter |

### pymavlink Example

```python
from pymavlink import mavutil

# Signing enabled connection
master = mavutil.mavlink_connection('udp:127.0.0.1:14550', 
                                     signing_key='0123456789ABCDEF0123456789ABCDEF')

# Send signed message
master.mav.command_long_send(
    target_system, target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    confirmation, param1, param2, param3, param4, param5, param6, param7
)
```

## Key Management

### Secret Key Distribution

```
Option 1: Pre-shared key
- Setup 시 physical connection
- SD card에 key 파일

Option 2: PKI (future)
- Certificate-based
- Revocation support

Option 3: Session key
- Negotiation protocol (TBD)
```

### Key Rotation

```
Best Practice:
- Periodic rotation (30-90 days)
- Compromise 시 즉시 교체
- Key version management
```

## Encryption

### Current Status

```
MAVLink 2.0: Signing 지원, Encryption 미지원

대안:
1. External encryption (IPsec, TLS)
2. Radio-layer encryption (AES-GCM)
3. Future: MAVLink native encryption
```

### External Encryption

| Layer | 방법 |
|-------|------|
| **Network** | IPsec VPN |
| **Transport** | TLS 1.3 (UDP DTLS) |
| **Application** | Payload encryption |

### DTLS (Datagram TLS)

```
Companion Computer ←[DTLS]→ GCS

- Certificate-based auth
- Forward secrecy
- Replay protection
```

## Authentication Levels

### Level 1: Unsigned

```
Risk: 메시지 위조 가능
용도: 개발, 테스트, isolated networks
```

### Level 2: Signed

```
보장:
- 메시지 출처 확인
- 내용 변경 감지
- Timestamp 유효성

필요: Shared secret key
```

### Level 3: Signed + Encrypted

```
보장:
- Level 2 + 
- 내용 기밀성
- 트래픽 패턴 보호

필요: Shared key + Encryption channel
```

## Security Threats

### Threat Model

| 위협 | 공격 | 대응 |
|------|------|------|
| **Command injection** | 위조된 명령 | Signing |
| **Eavesdropping** | 데이터 유출 | Encryption |
| **Replay** | 메시지 재전송 | Timestamp |
| **MITM** | 중간 공격 | Signing + Encryption |
| **DoS** | 채넾 정체 | Rate limiting |

### Attack Scenarios

```
Scenario 1: Unlink command
- Attacker sends ARM_DISARM
- Unsigned: ❌ Vehicle arms
- Signed: ✓ Rejected (invalid signature)

Scenario 2: Replay RTL
- Attacker captures RTL command
- Unsigned: ❌ Replayed RTL executes
- Signed: ✓ Timestamp expired
```

## Implementation Guide

### Firmware Changes

```cpp
// PX4 signing check
bool MavlinkReceiver::verify_signature(const mavlink_message_t *msg)
{
    if (!signing_enabled()) return false;
    
    uint8_t signature[13];
    memcpy(signature, _buf + msg->len + MAVLINK_NUM_NON_PAYLOAD_BYTES, 13);
    
    return hmac_sha256_verify(msg, timestamp, secret_key, signature);
}
```

### GCS Changes

```python
# Add signing to existing code
class SigningMAVConnection(mavutil.mavlink_connection):
    def __init__(self, device, signing_key=None):
        super().__init__(device)
        if signing_key:
            self.setup_signing(signing_key, sign_outgoing=True)
```

## Compatibility

### MAVLink 1 Fallback

```
MAVLink 2 capable vehicle:
- MAVLink 1 messages → Accept
- MAVLink 2 unsigned → Reject (if signing required)
- MAVLink 2 signed → Verify, accept
```

### Proto Version

| 파라미터 | 설명 |
|----------|------|
| `MAV_PROTO_VER` | 1=MAVLink 1, 2=MAVLink 2, 0=Negotiate |

## Best Practices

### Key Security

```
✓ Hardware security module (HSM)
✓ Secure boot with key injection
✓ No hardcoded keys in firmware
✓ Key escrow for recovery
```

### Network Isolation

```
Production:
- Telemetry radio: Isolated frequency
- WiFi: WPA3-Enterprise
- Serial: Physical access control
```

## 관련 개념

- [[mavlink-protocol]] — MAVLink 1 기본
- [[datalink-communication]] — 통신 보안
- [[drone-safety-failsafe]] — 무단 명령 대응

## 수집 대상

- 드론 사이버 보안 사고 사례
- MAVLink 암호화 표준화 동향
- HSM 기반 key management
