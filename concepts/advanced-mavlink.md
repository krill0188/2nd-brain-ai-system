---
title: Advanced MAVLink
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, mavlink, mavlink2, security, signing, routing, dialect]
sources: []
confidence: medium
domain: comms-protocol
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# Advanced MAVLink

MAVLink 2는 MAVLink 1의 확장으로 더 큰 메시지, 더 많은 필드, 보안 기능을 제공한다. 대규모 드론 운용과 보안이 중요한 상황에서 필수적이다.

## MAVLink 1 vs MAVLink 2

| 특성 | MAVLink 1 | MAVLink 2 |
|------|-----------|-----------|
| **Protocol** | v1.0 | v2.0 |
| **Packet size** | 최대 263 bytes | 최대 280 bytes |
| **Fields** | 255 max | 65535 max |
| **Array size** | 255 max | 65535 max |
| **Signing** | ❌ | ✅ |
| **Extensions** | 제한적 | 풍부 |
| **Compatibility** | MAVLink 1 only | MAVLink 1+2 |

## MAVLink 2 Packet Structure

```
┌─────────────────────────────────────────────────────────┐
│                     MAVLink 2 Frame                     │
├────────┬────────┬────────┬────────┬────────┬────────┤
│ Start  │ Len    │ Incomp │ Comp   │ Seq    │ Sys ID │
│ 0xFD   │        │ Flags  │ Flags  │        │        │
├────────┼────────┼────────┼────────┼────────┼────────┤
│ Comp ID│ Msg ID │ Target │ Target │ Payload│ CRC    │
│        │ (3B)   │ Sys    │ Comp   │        │        │
├────────┴────────┴────────┴────────┴────────┴────────┤
│ Signature (optional, 13 bytes)                        │
└─────────────────────────────────────────────────────────┘
```

### New Fields

| 필드 | 설명 |
|------|------|
| **Incompatibility flags** | MAVLink 2 전용 기능 |
| **Compatibility flags** | MAVLink 1 호환 기능 |
| **Target system** | 메시지 대상 시스템 |
| **Target component** | 메시지 대상 컴포넌트 |

## Message Extensions

### Extension Fields

```xml
<message id="33" name="GLOBAL_POSITION_INT">
    <description>Global position</description>
    <field type="int32_t" name="lat">Latitude</field>
    <field type="int32_t" name="lon">Longitude</field>
    <!-- ... standard fields ... -->
    
    <!-- MAVLink 2 extensions -->
    <extensions/>
    <field type="uint16_t" name="hdg">Heading</field>
</message>
```

### Zero Truncation

```
MAVLink 2는 trailing zeros를 생략하여 대역폭 절약.
수신측은 누락된 필드를 zero로 채움.
```

## Message Signing

메시지 인증을 통한 보안 강화.

### Signing Process

```
1. Secret key (48 bytes) 설정
2. Timestamp 생성 (microseconds)
3. Link ID 설정 (0-3)
4. HMAC-SHA256 계산
5. Signature (6 bytes) 첨부
```

### Signing Setup

```python
from pymavlink import mavutil

# MAVLink 2 + signing
master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14550',
    source_system=255,
    dialect='common',
    mavlink_version=2
)

# Secret key 설정 (48 bytes)
secret_key = b'0123456789abcdef' * 3  # 48 bytes
master.setup_signing(secret_key, allow_unsigned=False)
```

### PX4 Signing 설정

```bash
# MAVLink signing 활성화
param set MAV_PROTO_VER 2  # MAVLink 2 강제

# Secret key (hex string)
param set MAV_X_SIGNING_KEY "0123456789abcdef..."
```

### Allow Unsigned

```
allow_unsigned=True:  서명 없는 메시지 허용 (gradual migration)
allow_unsigned=False: 서명 필수 (strict security)
```

## Routing & Forwarding

### Message Routing

```
MAVLink Router:
├── Serial → UDP
├── UDP → Serial  
├── UDP → UDP
└── Filtering & Logging
```

### MAVLink Router 설정

```ini
# /etc/mavlink-router/main.conf
[General]
TcpServerPort=5760

[UartEndpoint fc]
Device = /dev/ttyACM0
Baud = 921600

[UdpEndpoint gcs]
Mode = normal
Address = 192.168.1.100
Port = 14550

[UdpEndpoint onboard]
Mode = normal  
Address = 192.168.1.10
Port = 14540
```

### Message Filtering

```
Route rules:
- Blacklist: 특정 메시지 차단
- Whitelist: 특정 메시지만 허용
- Rate limiting: 메시지 속도 제한
```

## Dialects & Custom Messages

### Custom Dialect

```xml
<!-- my_dialect.xml -->
<?xml version="1.0"?>
<mavlink>
    <include>common.xml</include>
    
    <messages>
        <message id="12000" name="MY_CUSTOM_MSG">
            <description>Custom message</description>
            <field type="uint32_t" name="custom_id">ID</field>
            <field type="float" name="value">Value</field>
        </message>
    </messages>
</mavlink>
```

### Dialect Generation

```bash
# MAVLink generator
python -m pymavlink.tools.mavgen \
    --lang=C \
    --wire-protocol=2.0 \
    --output=generated \
    my_dialect.xml
```

## High Latency Links

### High Latency Protocol

```
지연 시간이 긴 링크 (satellite, long-range radio)용:
- 메시지 압축
- 중요 메시지 우선순위
- ACK 최소화
```

### MAVLink FTP

```
파일 전송 over MAVLink:
- Open, Read, Write, Close operations
- CRC-32 checksum
- Resume 지원
```

## Command Protocol

### COMMAND_INT vs COMMAND_LONG

| 타입 | 설명 | 사용 |
|------|------|------|
| **COMMAND_LONG** | float 파라미터 | 일반 명령 |
| **COMMAND_INT** | int32 좌표 | 위치 기반 명령 |

### Command Acknowledgment

```
COMMAND_ACK:
- MAV_RESULT_ACCEPTED
- MAV_RESULT_TEMPORARILY_REJECTED
- MAV_RESULT_DENIED
- MAV_RESULT_UNSUPPORTED
- MAV_RESULT_FAILED
- MAV_RESULT_IN_PROGRESS
```

### Long Running Commands

```
1. COMMAND_INT/LONG 전송
2. COMMAND_ACK (IN_PROGRESS) 수신
3. COMMAND_ACK (ACCEPTED/FAILED) 대기
4. Timeout: 10s (default), 재시도
```

## Parameter Protocol

### Parameter Transaction

```
PARAM_VALUE (stream)
  ↓
PARAM_REQUEST_READ (single)
PARAM_REQUEST_LIST (all)
  ↓
PARAM_SET
  ↓
PARAM_VALUE (ack)
```

### Parameter Cache

```python
# Parameter 캐싱
param_cache = {}

@master.on_message('PARAM_VALUE')
def on_param(msg):
    param_cache[msg.param_id] = msg.param_value
```

## Mission Protocol

### Mission Transaction

```
MISSION_COUNT
  ↓
MISSION_REQUEST_INT (for each item)
  ↓
MISSION_ITEM_INT
  ↓
MISSION_ACK
```

### Mission Types

| 타입 | 설명 |
|------|------|
| **MAV_MISSION_TYPE_MISSION** | Flight plan |
| **MAV_MISSION_TYPE_FENCE** | Geofence |
| **MAV_MISSION_TYPE_RALLY** | Rally points |

## RTPS/ROS2 Bridge

### uXRCE-DDS

```
MAVLink ↔ DDS 변환:
- PX4 uORB → MAVLink → ROS2
- 직접: PX4 uORB → uXRCE-DDS → ROS2
```

### Performance Comparison

| 방식 | 지연 | 대역폭 |
|------|------|--------|
| MAVLink bridge | ~10ms | 중간 |
| uXRCE-DDS | ~1ms | 높음 |

## Debugging Tools

### MAVLink Inspector

```
QGC → Analyze → MAVLink Inspector
├── Message rates
├── Field values
├── Graphing
└── Logging
```

### MAVProxy

```bash
# MAVProxy 시작
mavproxy.py --master=/dev/ttyACM0 --baudrate=921600

# 명령
> messages  # 메시지 목록
> message GLOBAL_POSITION_INT  # 특정 메시지
> param show  # 파라미터
> arm throttle  # 시동
```

## 관련 개념

- [[mavlink-protocol]] — MAVLink 기본
- [[mavsdk]] — 고수준 SDK
- [[datalink-communication]] — 링크 계층
- [[ros2-drone-integration]] — ROS2 연동

## 수집 대상

- MAVLink 3 로드맵
- DDS-MAVLink interop
- Quantum-safe signing

## 📰 최근 관련 소식
- 중국, 美 대상 드론·핵심부품 수출통제 강화 (뉴시스, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiYEFVX3lxTE9KZUtyQ2tOWWpIWW1DM0ZpdXBsUTFodVp0ai12YmU3QmN1Tmd2YXFPOEtINFliTU1SdElZNGpOclBvNGVhVXBXdHl4QUZRX0JKVWxwMThXWnpVX2pOTzJYV9IBeEFVX3lxTE9KRTZneHpFODBaODlfQmx2OTZ5M1IwZzg4dHBvS3FTdjFJY1RKZUd6R0hLQTFCME04dS0tenllelVNSWhnb3lJd0ZNd29Bb0EzQjVuUWNTbkJTY05nX084SkxkWGE3SWlFeEVBRjh3enpYcG1aRkFHXw?oc=5
- 고령층 많은 농업 현장이 폭염에 가장 취약…드론 띄워서 살핀다 (연합뉴스, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTFBLdElwUE03UmVsRlpCcEpNSHRBQmtBTGw3ZnFDbEduWTZTbTRZMXk4ZlBwcHYwMi1uQlA3eDR6QjRPT0xOa3l2QVF0NmVUbm5lWG1iQnRNa21lNTDSAWBBVV95cUxQZXFtT1l1WHRQRUFoR1J4amtHeFV6eEJxVjFTSkhzTFYwT1c3dEg0NkZ1RTROZkt1U1FoNHBHZUlJSnBZMmt2bkRxUWc4R1hVWmF2Smo2bzllcDI5RUhsRF8?oc=5
- 美 해병대, 한국서 첫 자폭드론 실사격훈련…2.5㎞ 날아 목표물 명중[이현호의 밀리터리!톡] (sedaily.com, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiUkFVX3lxTE16dFloM1ZKa0lzQW1PTUZXUG5Fam1UWFhEN2V3eGZ1dWFnNWRJMWg0Sld4T1N5RVJaeGhxLW0yZjluMzVIVFAtNGRXYU4weVB3akHSAVNBVV95cUxON1pudENjWVNXMXhRZmo0TDhmMjdrV3IwdHBIeHQtS3BRaFlEcFhCdzdNSU0xaS1ERi1xZUkwd3JlSHdsQ0tFT2xPYkhhUjF4S0J0VQ?oc=5
- 미, 한반도서 자폭드론 첫 훈련...한국 배치 가능성도? (YTN 사이언스, Fri, 07 Au) — https://news.google.com/rss/articles/CBMijAFBVV95cUxPbmpqM3hNZTZIbjM3VE9pWGl4T1FhbXRoRlF5QXdnSlRrYkhTemJ0MXFzZTRfTHpjaXp6UnpXMENYcEhlSS1pNDQycGZiMTJnZlkwNDVGRWpkR2NDVElQaXM2cjgwU3pKQldpT25Qb0E5ejg5cXZDcWVnTlZsX2tqVzJSV2xwRV9DTDF2Uw?oc=5
- '중국 독점 겨냥' 드론·부품 최대 100% 관세...한국 15% (YTN 사이언스, Fri, 14 Au) — https://news.google.com/rss/articles/CBMif0FVX3lxTFB4WklaLTZ1UXphSDRfVTRub3ltdTUtZDVLS3RweEttN0FidzZEcS1LV3kwUHN0TWoxMXlfOTFiSk82a0NkM21wcVNfWXNvTktkcEtlY3BySDNQOWJ5UDMwU3E1ZGhXenlKOXdDSkNIcVo1ejJHYnRkNElQQ0k3aGM?oc=5
- 美, 중동 다국적 공격드론TF 띄운다…'무기재고 부족' 우려 덜까 (연합뉴스, Fri, 14 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE1RS0x1cDdIT3NBTU9KTi1TeHpLN1dxOU1tTXpTQi16Y0ZZOW9IS0FxT1VOOFl2OF82Q050X2VWOHNMSGdyQ1Y0ZTRHeFluMGg5T1dHLU11MTRnSGfSAWBBVV95cUxQUW41cFlVT3FhX2pqdTZWVTBEYWtLS2szOU5ocld1STdoWncyVG44QW5wSEdwOXNUUm9OT3JnLUs3Zk8wVVVQU2h6M2ZhMDMyTjJIbjlKOHJiSGstb0xTY1A?oc=5
- 트럼프, 중국 겨냥 드론·드론 부품에 최대 100% 관세‥한국은 15% (imnews.imbc.com, Thu, 13 Au) — https://news.google.com/rss/articles/CBMidEFVX3lxTE1XbERsS1R0RExSNHV0a2xXUU15OExVT2puQzJkaDdSVTZpV1NPX0thcGo2d0RvVmlVanl4V1lybWFtVTJQdG9GUWcwOHVlZ2NCbUdSYlE1WnQxWmFsUVI3VnRieXE4eDZlSXVGQXpmcGM2QTU20gF0QVVfeXFMUDVURVJ2QlhVNGgyc2Y1OHE1dG1tSzNyWW1SZlRuODRCS0VqMXBBNWNHVkRDSm1xSTZyTHc2YW1nNkY4UzdGV3ZSVkk4cndxM2N0ejNqdUl5ZUR0cHVBN1g1RngyZnJpOU85aDQwdktSTWpvdTY?oc=5
- 트럼프, 中겨냥 드론·드론부품에 최대 100% 관세…한국은 15% (연합뉴스, Thu, 13 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE1jTzBaVW5RQlpiMEZVcWpIbWxnakFyQ28yQWpzSzVQR2Yyc0tNTlNpTHR5Mm1GbXItZUdSX2NNdmRETzA0OVQ3MXh0XzVzRTJlTXlQd0w5NGliMmvSAWBBVV95cUxNM2M1SHRJdG91SVQ5YnQ4MmVVOEFQdHFFOE9GYkUtWjZQdndxNFozTlVOM1NLMzg5ZzZKWVZvd3FBLTFkQlZ1QVhkc1RjdmRVaDZ5NWdESm9PRXBlMUNGS3c?oc=5
