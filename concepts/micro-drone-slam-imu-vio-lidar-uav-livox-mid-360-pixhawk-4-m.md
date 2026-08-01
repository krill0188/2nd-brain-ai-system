---
title: "검색 결과에서 \"micro drone\"으로 명시된 SLAM 사례는 카메라+IMU(VIO) 조합을 사용한 반면, LiDAR-관성 오도메트리 사례는 더 큰 임베디드 UAV 플랫폼(Livox Mid-360/Pixhawk 4 Mini)이나 다중 센서 정찰 드론 프로젝트에서 등장해, 마이크로 스케일에서는 카메라+IMU 조합이 상대적으로 더 구체적인 근거를 갖는다."
created: 2026-08-01
updated: 2026-08-01
type: concept
tags: []
sources:
  - raw/papers/drone-hw/danial2025-microdrone-slam.md
confidence: medium
domain: ai-agent
contested: false
contradictions: []
---
# 검색 결과에서 "micro drone"으로 명시된 SLAM 사례는 카메라+IMU(VIO) 조합을 사용한 반면, LiDAR-관성 오도메트리 사례는 더 큰 임베디드 UAV 플랫폼(Livox Mid-360/Pixhawk 4 Mini)이나 다중 센서 정찰 드론 프로젝트에서 등장해, 마이크로 스케일에서는 카메라+IMU 조합이 상대적으로 더 구체적인 근거를 갖는다.

> 이 페이지는 인간 승인형 AI 연구 세션 `research/runs/20260801-research-1785543589`에서 마스터 승인을 거쳐 승격된 inference 클레임(`C3`)이다. 세션 원본 산출물은 `research/hypotheses/20260801-research-1785543589.md`, `research/reviews/20260801-research-1785543589.md`에 그대로 보존되어 있다.

## 주장

검색 결과에서 "micro drone"으로 명시된 SLAM 사례는 카메라+IMU(VIO) 조합을 사용한 반면, LiDAR-관성 오도메트리 사례는 더 큰 임베디드 UAV 플랫폼(Livox Mid-360/Pixhawk 4 Mini)이나 다중 센서 정찰 드론 프로젝트에서 등장해, 마이크로 스케일에서는 카메라+IMU 조합이 상대적으로 더 구체적인 근거를 갖는다.

## 근거

- [[flight-ready-lidar-inertial-odometry]]
- [[recon-swarm-project]]
- ^[raw/papers/drone-hw/danial2025-microdrone-slam.md]

## 검토 노트 (Critic)

- 반론/모순: 없음
- 한계: recon-swarm-project.md는 학술 문헌이 아니라 마스터 개인 프로젝트 로드맵이며, LiDAR+카메라+Radar+Optical Flow를 모두 탑재하는 계획으로 "마이크로드론"이 아닌 표준 UAV급 플랫폼을 전제로 한다. flight-ready-lidar-inertial-odometry의 Livox Mid-360(약 265g)도 진정한 마이크로드론(보통 250g 미만)에 탑재하기엔 무겁다는 점에서 이 추론은 성립하지만, "구체성의 차이"는 실제로는 검색 카테고리(마이크로드론 vs. 일반 UAV)의 차이에서 기인한 것일 수 있어 인과관계 해석에 유의해야 한다.

## 관련

[[flight-ready-lidar-inertial-odometry]] [[recon-swarm-project]]
