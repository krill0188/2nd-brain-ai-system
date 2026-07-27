---
title: Visual Positioning & Odometry
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-ai, computer-vision, vio, slam, odometry, positioning]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# Visual Positioning & Odometry

Visual Odometry(VO)와 Visual-Inertial Odometry(VIO)는 카메라와 IMU를 사용하여 드론의 위치와 자세를 추정하는 기술이다. GPS가 없거나 신뢰할 수 없은 환경에서 필수적이다.

## VIO 시스템 아키텍처

```
┌─────────────────────────────────────────┐
│         Camera + IMU Sensors          │
│      (Raw images + IMU readings)      │
└───────────────────┬───────────────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
┌────────┐   ┌──────────┐   ┌──────────┐
│ Feature│   │ Optical  │   │ Direct   │
│ Matcher│   │ Flow     │   │ Method   │
└────┬───┘   └────┬─────┘   └────┬─────┘
     │            │              │
     └────────────┼──────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  Fusion Core   │
         │ (MSCKF/OKVIS)│
         └───────┬────────┘
                 │
                 ▼
    ┌────────────────────────────┐
    │   Pose (position +       │
    │   orientation) + Velocity  │
    └────────────────────────────┘
```

## Feature-Based VO

### 특징점 기반 방법

| 특징점 검출 | 설명 |
|------------|------|
| **FAST** | 속도 중심 코너 검출 |
| **ORB** | Oriented FAST + Rotated BRIEF |
| **SIFT** | Scale-Invariant Feature Transform |
| **SURF** | Speeded-Up Robust Features |

### ORB 특징점

```
1. FAST 코너 검출
2. Harris 응답으로 순위 매기기
3. 방향 할당 (intensity centroid)
4. rBRIEF 기술자 계산 (256-bit)
```

## Optical Flow

픽셀 단위 움직임 벡터를 기반으로 상대 이동 추정.

### Lucas-Kanade

```python
# OpenCV optical flow
import cv2

calc = cv2.calcOpticalFlowPyrLK(
    prev_gray, curr_gray, 
    prev_pts, None,
    winSize=(21, 21),
    maxLevel=3
)
```

### Downward Optical Flow

| 센서 | 특징 |
|------|------|
| **PX4Flow** | 아래 보면 카메라 + 소나 |
| **TeraRanger** | TOF 거리 기반 |
| **OpenMV** | OpenMV Cam 통합 |

### Flow → Velocity

```
Vx_flow = X_flow_pixels × flow_to_velocity_scale
Vy_flow = Y_flow_pixels × flow_to_velocity_scale

// 고도 보정
V_body = V_pixel × distance_to_ground
```

## Visual-Inertial Odometry

IMU와 비전 융합으로 견고한 추정.

### MSCKF (Multi-State Constraint Kalman Filter)

| 특성 | 설명 |
|------|------|
| **State** | IMU 스테이트 + 특징점 clone |
| **Update** | 특징점 reprojection error |
| **Complexity** | O(n) where n = pose clones |

### VINS-Mono/VINS-Fusion

홍콩과기대의 오픈소스 VIO.

| 버전 | 특징 |
|------|------|
| **VINS-Mono** | 단안 카메라 + IMU |
| **VINS-Fusion** | 스테레오, GPS 융합 |

### ROVIO (Robust Visual Inertial Odometry)

ETH Zurich의 필터 기반 VIO.

```
장점:
- 빠른 수렴
- 견고한 특징 추적
- 자동 초기화

단점:
- 카메라-IMU extrinsic 민감
```

### ORB-SLAM

PTAM 기반 SLAM 시스템.

| 버전 | 특징 |
|------|------|
| **ORB-SLAM1** | 단안, 루프 클로저 |
| **ORB-SLAM2** | 스테레오, RGB-D |
| **ORB-SLAM3** | Visual-Inertial, Multi-map |

## PX4 VIO 통합

### 필요 사항

| 메시지 | 설명 |
|--------|------|
| `vehicle_mocap_odometry` | 외부 추정 토픽 |
| `vehicle_visual_odometry` | 비전 추정 토픽 |
| `vehicle_odometry` | 내부 EKF 추정 |

### EKF2 설정

```bash
# 외부 비전 활성화
param set EKF2_AID_MASK 24  # EV pos + EV yaw

# 비전 포즈 순서 설정
param set EKF2_EV_POS_X 0.06  # 카메라 offset
param set EKF2_EV_POS_Y 0
param set EKF2_EV_POS_Z -0.03

# 비전 지연 보정
param set EKF2_EV_DELAY 10  # ms
```

### 외부 추정 퍼블리시

```python
from px4_msgs.msg import VehicleOdometry
import tf_transformations

odom = VehicleOdometry()
odom.timestamp = int(time.time() * 1e6)
odom.pose_frame = VehicleOdometry.POSE_FRAME_FRD
odom.position = [x, y, z]

# Quaternion (w, x, y, z)
q = tf_transformations.quaternion_from_euler(roll, pitch, yaw)
odom.q = [q[3], q[0], q[1], q[2]]

odom.velocity_frame = VehicleOdometry.VELOCITY_FRAME_FRD
odom.velocity = [vx, vy, vz]

publisher.publish(odom)
```

## Realsense T265

Intel의 Tracking Camera (VIO 내장).

### 특징

| 특성 | 값 |
|------|-----|
| **Cameras** | 스테레오 fisheye |
| **IMU** | Bosch BMI055 |
| **Processor** | Intel Myriad 2 VPU |
| **Rate** | 200Hz IMU, 30Hz stereo |
| **Latency** | ~15ms |
| **Drift** | ~1% (visual), ~5% (pure inertial) |

### PX4 연결

```bash
# Serial 연결
T265 → USB → Companion
Companion → UART → FC

# MAVLink 전송 (librealsense)
realsense2_camera_node
  └─ /camera/odom/sample
      └─ MAVLink VISUAL_POSITION_ESTIMATE
```

## Stereo Vision

### Stereo Matching

| 알고리즘 | 특징 |
|----------|------|
| **BM** | Block Matching, 빠름 |
| **SGBM** | Semi-Global, 균형 |
| **SGM** | FPGA 최적화 |

### Depth 계산

```python
# OpenCV stereo
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(left, right)

depth = (focal_length * baseline) / disparity
```

## Marker-Based Positioning

### ArUco

```python
# ArUco marker detection
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

markers, ids, _ = cv2.aruco.detectMarkers(
    frame, dictionary, parameters=parameters
)

# Pose estimation
cv2.aruco.estimatePoseSingleMarkers(
    markers, marker_length, camera_matrix, dist_coeffs
)
```

### AprilTag

| 특징 | 설명 |
|------|------|
| **Encoding** | 2D 바코드 |
| **Detection** | Edge-based |
| **ID** | 0-587 (36H11) |
| **Accuracy** | Sub-pixel |

## Indoor Navigation

### Pipeline

```
1. VIO / SLAM 초기화
2. Local map 생성
3. Path planning
4. Obstacle avoidance
5. Landing detection
```

### UWB + VIO Fusion

```
UWB: Global anchor 기반 절대 위치
VIO: 상대 이동, 높은 주파수
Fusion: EKF로 견고한 추정
```

## 실시간 제한

| 요소 | 제한 | 해결 |
|------|------|------|
| **Latency** | <50ms | GPU 가속 |
| **Jitter** | 짧은 버퍼 | Sync 스레드 |
| **Drift** | 루프 클로저 | Map 재사용 |
| **Lighting** | Robust | HDR, IR |

## 관련 개념

- [[computer-vision-drone]] — CV 기본
- [[px4-offboard-control]] — 외부 추정 통합
- [[drone-ai-agents]] — 자율 탐색
- [[swarm-coordination]] — 멀티 드론 VIO

## 수집 대상

- 실제 실내 드론 배포 사례
- 대규모 환경 SLAM
- Event camera 기반 VIO
