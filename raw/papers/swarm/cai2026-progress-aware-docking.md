---
title: "A Progress-Aware Leader-Follower Midair Docking System for Dual-Drone Aerial Manipulation"
authors:
  - Yifan Cai
  - Jan Ming Kevin Tan
  - Xiangqi Li
  - Chenzhe Jin
  - Narsimlu Kemsaram
  - Valerio Modugno
venue: "IEEE CASE 2026"
year: 2026
doi: "10.48550/arXiv.2605.29410"
url: "https://arxiv.org/abs/2605.29410"
pdf: "https://arxiv.org/pdf/2605.29410"
topics: [swarm, drone-hw, ros2, px4]
abstract: |
  Reliable midair docking between small unmanned aerial vehicles (UAVs) is essential 
  for modular aerial cooperation and manipulation, but it requires precise 
  relative-pose control and repeatable platform under tight thrust and payload 
  constraints. We present a dual-drone docking platform where two quadrotors 
  operate in a leader-follower formation and dock using a lightweight modular 
  frame with passive magnetic latching. A progress-aware mission supervisor 
  manages phase transitions: approach, alignment, capture, and settle. This 
  platform integrates a complete hardware-software stack (ROS 2 with Crazyflie/PX4 
  interfaces) and synchronized logging for benchmark evaluation. We evaluate 
  the platform in simulation and real-world experiments using quantitative metrics 
  such as formation error, baseline and yaw consistency, docking success rate, 
  time-to-dock, and failure-mode statistics.
ingested: 2026-07-27
---

# A Progress-Aware Leader-Follower Midair Docking System for Dual-Drone Aerial Manipulation

## Metadata

| 항목 | 내용 |
|------|------|
| **저자** | Yifan Cai, Jan Ming Kevin Tan, Xiangqi Li, Chenzhe Jin, Narsimlu Kemsaram, Valerio Modugno |
| **발행처** | IEEE CASE 2026 (arXiv:2605.29410) |
| **연도** | 2026 |
| **DOI** | 10.48550/arXiv.2605.29410 |
| **PDF** | https://arxiv.org/pdf/2605.29410 |

## 주요 내용

### 연구 목표
- 듀얼 드론 공중 도킹 시스템 개발
- Leader-Follower 편대 비행 및 정밀 도킹

### 핵심 기술
- **Progress-aware mission supervisor**: approach → alignment → capture → settle 단계 관리
- **Passive magnetic latching**: 경량 모듈 프레임 자석 잠금
- **ROS 2 + Crazyflie/PX4**: 완전한 하드웨어-소프트웨어 스택

### 평가 지표
- Formation error (편대 오차)
- Baseline and yaw consistency
- Docking success rate
- Time-to-dock
- Failure-mode statistics

## 관련 위키 페이지

- [[swarm-coordination]] — 스웜 편대 비행
- [[px4-system-architecture]] — PX4 시스템
- [[ros2-drone-integration]] — ROS2 드론 연동
- [[drone-payload-systems]] — 페이로드 시스템

## 인용

```bibtex
@inproceedings{cai2026progress,
  title={A Progress-Aware Leader-Follower Midair Docking System for Dual-Drone Aerial Manipulation},
  author={Cai, Yifan and Tan, Jan Ming Kevin and Li, Xiangqi and Jin, Chenzhe and Kemsaram, Narsimlu and Modugno, Valerio},
  booktitle={IEEE International Conference on Automation Science and Engineering (CASE)},
  year={2026}
}
```
