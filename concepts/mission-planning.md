---
title: Mission Planning
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone, drone-sw, mission, waypoint, survey, QGC, planning]
sources: []
confidence: medium
domain: ops-mission
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# Mission Planning

미션 계획은 드론이 자율적으로 수행할 비행 경로와 작업을 사전에 정의하는 과정이다. QGroundControl(QGC) 등 GCS 소프트웨어를 통해 시각적으로 계획한다.

## 미션 요소

```
┌─────────────────────────────────────────┐
│           Mission Plan                │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │ Takeoff │ │ Waypt   │ │ Action  │   │
│  └────┬────┘ └────┬────┘ └────┬────┘   │
│       │           │           │        │
│       └───────────┼───────────┘        │
│                   │                     │
│              ┌────┴────┐                │
│              │  Land   │                │
│              └─────────┘                │
└─────────────────────────────────────────┘
```

## 미션 아이템 유형

| 유형 | 설명 | MAVLink |
|------|------|---------|
| **Takeoff** | 이륙 | `MAV_CMD_NAV_TAKEOFF` |
| **Land** | 착륙 | `MAV_CMD_NAV_LAND` |
| **RTL** | 복귀 | `MAV_CMD_NAV_RETURN_TO_LAUNCH` |
| **Waypoint** | 경유지 | `MAV_CMD_NAV_WAYPOINT` |
| **Loiter** | 선회 | `MAV_CMD_NAV_LOITER_TIME` |
| **Delay** | 대기 | `MAV_CMD_NAV_DELAY` |
| **Jump** | 반복 | `MAV_CMD_DO_JUMP` |

## Waypoint 미션

### 기본 구조

```
TAKEOFF (altitude: 30m)
   ↓
WAYPOINT_1 (lat, lon, alt, delay)
   ↓
WAYPOINT_2 (lat, lon, alt)
   ↓
...
   ↓
LAND (lat, lon)
```

### Waypoint 파라미터

| 파라미터 | 설명 | 단위 |
|----------|------|------|
| **Lat** | 위도 | deg |
| **Lon** | 경도 | deg |
| **Alt** | 고도 | m (MSL or Relative) |
| **Delay** | 대기 시간 | s |
| **Acceptance Radius** | 도착 판정 반경 | m |
| **Yaw** | 요 각도 | deg |

## Survey 미션

정지영상 영을 위한 자동 영 경로 생성.

### 그리드 설정

| 파라미터 | 설명 |
|----------|------|
| **Area** | 다각형 영역 |
| **Altitude** | 영 고도 |
| **Overlap** | 중복률 (전방/측방) |
| **GSD** | Ground Sample Distance |
| **Speed** | 비행 속도 |

### 카메라 설정

```
Camera: Sony A7R IV
Focal Length: 35mm
Sensor: Full Frame
Resolution: 61MP

Calculated:
- GSD @ 100m: 1.2cm/pixel
- Overlap: 80% forward, 70% side
- Flight lines: 12
- Images: 240
```

## QGroundControl 미션 계획

### 인터페이스

| 패널 | 기능 |
|------|------|
| **Plan View** | 미션 편집 |
| **Fly View** | 실시간 비행 |
| **Survey Tool** | 자동 경로 생성 |
| **Pattern Tool** | 구조물 영 패턴 |

### 미션 파일

| 형식 | 확장자 | 설명 |
|------|--------|------|
| **QGC Plan** | .plan | JSON 기반 |
| **MAVLink Mission** | .txt | waypoint 리스트 |
| **KML** | .kml | Google Earth |

### 미션 파일 예시

```json
{
  "fileType": "Plan",
  "geoFence": {
    "circles": [],
    "polygons": []
  },
  "items": [
    {
      "AMSLAltAboveTerrain": null,
      "Altitude": 30,
      "AltitudeMode": 1,
      "autoContinue": true,
      "command": 22,
      "doJumpId": 1,
      "frame": 3,
      "params": [0, 0, 0, null, 0, 0, 30],
      "type": "SimpleItem"
    }
  ],
  "plannedHomePosition": [37.5665, 126.9780, 30],
  "vehicleType": 2,
  "version": 2
}
```

## 고급 미션 기능

### 조건부 미션

| 조건 | 설명 |
|------|------|
| **DO_JUMP** | 특정 아이템으로 점프 |
| **DO_SET_ROI** | 관심 지점 설정 |
| **DO_CHANGE_SPEED** | 속도 변경 |
| **DO_SET_CAM_TRIGG_DIST** | 거리 기반 영 |

### VTOL 미션

| 명령 | 설명 |
|------|------|
| **NAV_VTOL_TAKEOFF** | VTOL 이륙 |
| **NAV_VTOL_LAND** | VTOL 착륙 |
| **DO_VTOL_TRANSITION** | 모드 전환 |

## 미션 검증

### Pre-flight 체크

- [ ] Waypoint 좌표 확인
- [ ] 고도 설정 확인
- [ ] Geofence 설정
- [ ] RTL 고도 확인
- [ ] 배터리 충분
- [ ] 통신 테스트

### 시뮬레이션

```bash
# SITL에서 미션 테스트
make px4_sitl gazebo-classic

# QGC에서 미션 업로드
# 미션 실행 및 검증
```

## MAVSDK 미션 API

```python
from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan

drone = System()
await drone.connect()

# 미션 아이템 생성
mission_items = [
    MissionItem(37.5665, 126.9780, 30, 0, True, float('nan'), float('nan'),
                MissionItem.CameraAction.NONE, float('nan'), float('nan')),
    MissionItem(37.5670, 126.9785, 30, 0, True, float('nan'), float('nan'),
                MissionItem.CameraAction.TAKE_PHOTO, float('nan'), float('nan')),
]

# 미션 계획 생성
mission_plan = MissionPlan(mission_items)

# 미션 업로드
await drone.mission.upload_mission(mission_plan)

# 미션 시작
await drone.mission.start_mission()
```

## 관련 개념

- [[ground-control-station]] — QGC 상세
- [[px4-flight-modes]] — 미션 모드
- [[drone-payload-systems]] — 페이로드 트리거
- [[drone-simulation]] — 미션 시뮬레이션

## 수집 대상

- 실제 촬영 미션 사례 연구
- 자동 경로 최적화 알고리즘
- 실시간 미션 재계획 방법론
