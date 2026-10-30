---
title: "aerial-autonomy-stack: a Faster-than-real-time, Autopilot-agnostic, ROS2 Framework to Simulate and Deploy Perception-based Drones"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
tags: [drone, edge, deployment, ros2, px4, ardupilot, simulator]
sources: [inbox/processed/hw-20261021-data-edge-aerial-autonomy-stack-panerati-2026.md]
confidence: medium
contested: false
contradictions: []
---

# aerial-autonomy-stack: a Faster-than-real-time, Autopilot-agnostic, ROS2 Framework to Simulate and Deploy Perception-based Drones

- 원문: arXiv:2602.07264^[inbox/processed/hw-20261021-data-edge-aerial-autonomy-stack-panerati-2026.md]
- 저자: Jacopo Panerati, Sina Sajjadi, Sina Soleymanpour, Varunkumar Mehta, Iraj Mantegh^[inbox/processed/hw-20261021-data-edge-aerial-autonomy-stack-panerati-2026.md]
- 발행: 2026-02-06 (v2 2026-05-02)^[inbox/processed/hw-20261021-data-edge-aerial-autonomy-stack-panerati-2026.md]

## 핵심 내용
GPU 가속 인식부터 비행 컨트롤러 동작까지 드론 자율성을 구성하는 오픈소스 ROS 2 프레임워크. PX4와 ArduPilot 두 오토파일럿을 공통 인터페이스로 지원한다. 엣지 컴퓨트와 네트워킹을 포함한 개발·배포 파이프라인 전체를 실시간보다 20배 넘게 빠르게 시뮬레이션한다고 보고한다.^[inbox/processed/hw-20261021-data-edge-aerial-autonomy-stack-panerati-2026.md]
원문 인용: "over 20x faster-than-real-time, end-to-end simulation"^[inbox/processed/hw-20261021-data-edge-aerial-autonomy-stack-panerati-2026.md]

## 설계·운용에 쓸 수 있는 지침
- 인식 모델 배포 전 end-to-end 시뮬레이션으로 빌드-테스트-릴리스 주기를 단축하는 구성 사례.^[inbox/processed/hw-20261021-data-edge-aerial-autonomy-stack-panerati-2026.md]

## 한계·미확인
- 초록 외 하드웨어(Jetson 등) 지원 목록과 20배 달성 조건은 미확인.^[inbox/processed/hw-20261021-data-edge-aerial-autonomy-stack-panerati-2026.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]

## 📰 최근 관련 소식
- Estonian Drone Autonomy Startup Advances to Anduril AI Grand Prix Finals (dronelife.com, Mon, 26 Oc) — https://dronelife.com/2026/10/26/anduril-ai-grand-prix-autonomous-drone-racing/
