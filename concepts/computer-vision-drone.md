---
title: Computer Vision for Drones
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-ai, computer-vision, SLAM, detection, tracking, YOLO]
sources: []
confidence: medium
domain: ai-autonomy
contested: false
contradictions: []
---

# Computer Vision for Drones

드론 컴퓨터 비전은 탑재된 카메라와 AI 알고리즘을 활용하여 환경을 인식, 분석, 이해하는 기술이다. 객체 감지, SLAM, 추적 등 다양한 응용이 있다.

## 핵심 기술 영역

### 1. Object Detection (객체 감지)

| 모델 | 특성 | FPS (Jetson) |
|------|------|-------------|
| **YOLOv5/v8/v10** | 범용, 빠름 | 30-60+ |
| **YOLO-NAS** | AutoNAC 최적화 | 40-80 |
| **RT-DETR** | Transformer 기반 | 20-40 |

**드론 특화:**
- 작은 객체 감지 최적화
- 동적 배경 대응
- 실시간 요구사항

### 2. SLAM (Simultaneous Localization And Mapping)

SLAM은 실시간으로 지도를 생성하고 동시에 위치를 추정하는 기술이다.

| 알고리즘 | 타입 | 특성 |
|---------|------|------|
| **ORB-SLAM3** | Visual | 가볍고, 정확 |
| **VINS-Fusion** | Visual-Inertial | IMU 융합 |
| **RTAB-Map** | LIDAR+Visual | 메모리 효율 |
| **LIO-SAM** | LIDAR-Inertial | 실외 강력 |

**입력 모달리티:**
- **Visual SLAM**: 카메라만
- **VIO (Visual-Inertial)**: 카메라 + IMU
- **LIDAR SLAM**: LiDAR
- **Multi-modal**: 융합

### 3. Visual Odometry (VO)

| 방법 | 설명 |
|------|------|
| **Feature-based** | 특징점 매칭 (ORB, SIFT) |
| **Direct** | 픽셀 강도 직접 사용 (LSD, DSO) |
| **Semi-Direct** | 하이브리드 (SVO) |

### 4. Object Tracking (객체 추적)

| 알고리즘 | 특성 |
|----------|------|
| **SORT** | 단순, 실시간 |
| **DeepSORT** | 딥러닝 융합 |
| **ByteTrack** | 고성능 |

## 시스템 아키텍처

```
┌─────────────────────────────────────────┐
│         Camera (RGB/Depth)            │
│         CSI / USB / GMSL             │
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│         ISP / Preprocessing           │
│         Debayer / Undistort           │
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│         Neural Network (GPU)          │
│     YOLO / SLAM / Segmentation        │
│         TensorRT / ONNX Runtime      │
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│         Post-processing               │
│     NMS / Filtering / Fusion          │
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│         Output / Control                │
│     MAVSDK / ROS2 / FC Command       │
└─────────────────────────────────────────┘
```

## 하드웨어 플랫폼

| 플랫폼 | GPU | TOPS | 용도 |
|--------|-----|------|------|
| **Raspberry Pi 5** | VideoCore VII | 0.1 | 경량 |
| **Jetson Orin Nano** | 1024 CUDA | 40 | 표준 |
| **Jetson Orin NX** | 2048 CUDA | 100 | 고성능 |
| **Intel NUC** | Iris Xe | 2-4 | x86 |
| **Coral TPU** | Edge TPU | 4 | 전용 |

## 통합 예시

### YOLO + Tracking + Control

```python
import cv2
from ultralytics import YOLO

# Load model
model = YOLO('yolov8n.pt')

# Inference
results = model(frame)

# Tracking
for box in results[0].boxes:
    x1, y1, x2, y2 = box.xyxy[0]
    cls = int(box.cls)
    conf = float(box.conf)
    
    # Calculate center offset
    center_x = (x1 + x2) / 2
    offset_x = center_x - frame_width / 2
    
    # Send velocity command to drone
    send_velocity_command(offset_x * k_p, 0, 0)
```

### SLAM + Navigation

```python
# ORB-SLAM3 output
pose = slam.get_current_pose()  # [x, y, z, qx, qy, qz, qw]

# Path planning with current pose
path = planner.plan(start=pose, goal=target)

# Follow path with PX4
for waypoint in path:
    mavsdk.offboard.set_position_ned(waypoint)
```

## 도전 과제

| 과제 | 설명 | 해법 |
|------|------|------|
| **동적 배경** | 드론 움직임 | Stabilization, IMU 융합 |
| **조명 변화** | 그림자, 일몰 | HDR, 오토-조리개 |
| **작은 객체** | 먼 거리 | Super-resolution |
| **실시간성** | 지연 제한 | TensorRT, Pruning |
| **안전성** | 오탐 대응 | Redundancy, 다중 인지 |

## 응용 분야

| 분야 | 기술 | 설명 |
|------|------|------|
| **검색/구조** | Detection + Thermal | 실종자 탐색 |
| **농업** | NDVI + Segmentation | 작물 분석 |
| **건설** | Photogrammetry | 3D 매핑 |
| **보안** | Tracking + Recognition | 경계 감시 |
| **배달** | Navigation + VO | GPS-denied 내비 |

## 관련 개념

- [[drone-ai-agents]] — AI 에이전트 통합
- [[swarm-coordination]] — 멀티 드론 비전
- [[px4-offboard-control]] — 비전 데이터 기반 제어
- [[flight-controller-hardware]] — 컴패니언 컴퓨터 선택
- [[ros2-drone-integration]] — ROS2 비전 파이프라인

## 📰 최근 관련 소식
- Army seeks next-gen missile that could shoot down small drones for less than $150K a pop (DefenseScoop, Tue, 04 Au) — https://news.google.com/rss/articles/CBMie0FVX3lxTE5GbzRtdW9TS3Y4b3JkaW9oazVGWW9nUWRxa0hGY25RV2h1UEg1MVVfQnhSUE1xS1VFMzVSUGRyckRva0VEZFV5aWhqeHZsbngwV2FpTDBLMVEwdllFOWVXYVZyU3g2VDNESS1WekhBLXNYOEdhMWZrenRESQ?oc=5
- Drones Bring Whole Blood Directly to Trauma Scenes (dronelife.com, Mon, 10 Au) — https://dronelife.com/2026/08/10/drones-bring-whole-blood-directly-to-trauma-scenes/
- Powerful Public Safety Technology Needs Powerful Guardrails: What Flock’s Camera Controversy Means for Drones (dronelife.com, Fri, 14 Au) — https://dronelife.com/2026/08/14/public-safety-technology-drones-flock-guardrails/
- White House Imposes New Tariffs on Imported Drones and Components (dronelife.com, Fri, 14 Au) — https://dronelife.com/2026/08/14/drone-import-tariffs-us-supply-chain/
- DJI Puts Drones to the Test on the World's Highest Peak, Advancing Critical High-Altitude Delivery, Mapping, and Climate Research Applications - PR Newswire (news.google.com, Thu, 09 Ju) — https://news.google.com/rss/articles/CBMinwJBVV95cUxNVFN0OGNPbWYwX0I5TEMzMGlxV0pmQ1R0ZGZyUzFFOWp1ZUhOT0UzMm1NRElrOVF3cGFzU09hUTN0NnBVZUllVDdtZ1RCTWQyNV95SEpMaDJhb3JvQXk1OWo0YWY3bTFKMXB6YzdPNEUzUTJQX3BQa2pqWTREbzhuRHJhSkt6RkxnQ3l5Y0JkTG0tYWpfcklQMFVWS1NqV0FqWHdCMS02UXIxckU2WkItMkViZnhaV2NOamhpU3dBbHBmYmhaQVZheHZMdDZFUXQ2UXRvUFI2UERFWXBTWWpfeEt1VWxva3c2RGJXNHROcVM3MDJvRlZHSjlTaUVQVFhSSlVwRnNPaVVJeERLTjJsM2FTUFVKOVhhWGZlck5fMA?oc=5
- From Border Security to Biosecurity: Drones Join the Fight Against New World Screwworm - Dronelife (news.google.com, Tue, 11 Au) — https://news.google.com/rss/articles/CBMid0FVX3lxTE15WUZwa1BYNlNJR1M5NHVwT20yMGpSZmhPcEdMM3pmeVotUmRWeE5faEJrVFR1NnVfS0RVamViWmt6UEJTYUtKWVRxZUQtemcwRkRPYXdKWjFMZVJtZWRzeFk1MHJ5VW5CcjJZRkFZbTRMRExzYVpZ?oc=5
- [멈춤보단 천천히라도] 윈도우에 NVIDIA GPU( CUDA ) 사용하도록 파이토치 설치하는 방법 (youtube.com, 2026-08-12) — https://www.youtube.com/watch?v=TU_RGWEQBaM
- SimActive Correlator3D Supports Large-Scale Green Hydrogen Mapping in Chile (dronelife.com, Thu, 13 Au) — https://dronelife.com/2026/08/13/simactive-green-hydrogen-mapping-chile/
