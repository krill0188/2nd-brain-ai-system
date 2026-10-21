---
title: "aerial-autonomy-stack: a Faster-than-real-time, Autopilot-agnostic, ROS2 Framework to Simulate and Deploy Perception-based Drones"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: edge-ai-compute
source: arXiv:2602.07264
authors: "Jacopo Panerati, Sina Sajjadi, Sina Soleymanpour, Varunkumar Mehta, Iraj Mantegh"
published: "2026-02-06 (v2 2026-05-02)"
tags: [drone, edge, deployment, ros2, px4, ardupilot, simulator]
---
## 핵심 내용
GPU 가속 인식부터 비행 컨트롤러 동작까지 드론 자율성을 구성하는 오픈소스 ROS 2 프레임워크. PX4와 ArduPilot 두 오토파일럿을 공통 인터페이스로 지원한다. 엣지 컴퓨트와 네트워킹을 포함한 개발·배포 파이프라인 전체를 실시간보다 20배 넘게 빠르게 시뮬레이션한다고 보고한다.
원문 인용: "over 20x faster-than-real-time, end-to-end simulation"

## 설계·운용에 쓸 수 있는 지침
- 인식 모델 배포 전 end-to-end 시뮬레이션으로 빌드-테스트-릴리스 주기를 단축하는 구성 사례.

## 한계·미확인
- 초록 외 하드웨어(Jetson 등) 지원 목록과 20배 달성 조건은 미확인.
