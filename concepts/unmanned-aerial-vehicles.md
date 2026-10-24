---
title: "Unmanned Aerial Vehicles"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [hardware, uav, aerial-platform, communications, swarm]
sources: []
confidence: medium
contested: false
contradictions: []
domain: hardware
---

# Unmanned Aerial Vehicles

무인 항공기(UAV)라 불리는 무인 항공기는, 조종사 없이 원격 제어나 자율 비행 방식으로 운용되는 항공기를 의미한다. 탐사, 점검, 감시, 군사 등 다양한 분야에서 활용되며, 특히 통신이 제한된 환경이나 위험 지역에서 그 활용도가 높다.

## 개요

본문에서는 '무인 항공기'를 로봇 함대의 주요 구성 요소로 다루며, 지상 차량과 결합된 연계 탐사 및 점검 상황에서 중앙 집중식 통신 없이'ad-hoc 무선 네트워크'를 통해 상호 통신하고, 최종적으로는 '모바일 지상 관제소'에 결과를 보고한다고 명시하고 있다. 다양한 센서(장거리 라이다, 근거리 카메라)를 장착하고 있으며, GPS가 사용 불가능한 환경이나 열화된 환경 등에서 운영되는 것을 전제로 한다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| 플랫폼 형태 | 고정익, 회전익, VTOL 등 mission에 따라 다양함 |
| 센서 장착 | long-range lidar, close-range camera 등 task에 따라 차등 장착 |
| 통신 방식 | ad-hoc wireless networks (proximity-dependent, obstruction-sensitive) |
| 운영 환경 | GPS-free navigation, degraded environments |
| 협업 체계 | Heterogeneous Fleets ( heterogeneous robots with different sensors ) |

## 활용처

- 알 수 없는 환경의 simultaneous exploration과 inspection 수행
- 실시간 통신을 통해 mobile ground control station에 findings 보고
- 통신 인프라가 부족한 재난 지역, 야외 야적장, 실내 구조 등

## 관련 페이지

- [[SLEI3D]] — Coordinates heterogeneous fleets under limited communication
- [[Lidar]] — Equipped on Unmanned Aerial Vehicles for fast exploration
- [[Camera]] — Equipped on Unmanned Aerial Vehicles for detailed inspection
- [[Ad-Hoc Wireless Networks]] — Communication medium for UAVs in proximity
- [[Mobile Ground Control Station]] — Receives real-time reports from UAVs

## 출처

- (사용자 재확인 필요)原文 참조: http://arxiv.org/abs/2601.00163v1

## 분류

- [[auto-hub-hardware]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
