---
source_url: "file://MasterVault/Drone/ArduPilot/ArduPilot-DevNotes.md"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "Master (personal dev notes)"
sha256: "5c8d3e7f9a2b6c4d8e1f5a9b3c7d2e6f1a5b9c3d7e2f6a1b5c9d3e7f2a6b1c5"
tags: [drone-sw]
---

# ArduPilot 개발 노트

## 핵심 아키텍처

```
┌─────────────────────────────────────────┐
│            Vehicle Code                 │
│  Copter │ Plane │ Rover │ Sub           │
├─────────────────────────────────────────┤
│            Libraries                    │
│  AP_AHRS │ AP_GPS │ AP_Motors │ AC_PID  │
├─────────────────────────────────────────┤
│            AP_HAL (하드웨어 추상화)      │
├─────────────────────────────────────────┤
│  ChibiOS │ Linux │ SITL                 │
└─────────────────────────────────────────┘
```

## SITL 빠른 시작

```bash
# Copter
sim_vehicle.py -v ArduCopter --map --console

# 특정 위치
sim_vehicle.py -v ArduCopter -L Seoul

# 멀티 기체
sim_vehicle.py -v ArduCopter -n 3

# 프레임 지정
sim_vehicle.py -v ArduCopter -f hexa
```

## Lua 스크립트 (임무 자동화)

```lua
-- scripts/my_script.lua
function update()
    local pos = ahrs:get_position()
    if pos then
        gcs:send_text(6, string.format("Lat: %.6f", pos:lat()))
    end
    return update, 1000 -- 1초마다 실행
end
return update, 1000
```

## 자주 쓰는 파라미터

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| FRAME_CLASS | 프레임 타입 | 1 (쿼드) |
| ARMING_CHECK | 시동 체크 | 1 (전체) |
| FS_THR_ENABLE | 스로틀 페일세이프 | 1 |
| WPNAV_SPEED | 웨이포인트 속도 | 500 cm/s |
| ATC_RAT_PIT_P | 피치 PID P | 0.135 |

## 비행로그 분석

- `.bin` → DataFlash 로그
- `.tlog` → 텔레메트리 로그
- 분석 도구: ardupilot-log-analyzer (자체 개발)
- MAVExplorer, UAV Log Viewer
