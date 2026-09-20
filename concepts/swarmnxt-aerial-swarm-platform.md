---
title: "SwarmNxt: 고속 애자일 공중 스웜을 위한 오픈소스 SW-HW 플랫폼"
created: 2026-09-12
updated: 2026-09-12
type: concept
domain: ai-autonomy
tags: [drone, swarm, ai-autonomy]
sources: [raw/papers/swarm/swarmnxt-open-source-software-hardware-platform-for-fast-and-agile-aerial-swarms.md]
confidence: medium
contested: false
contradictions: []
---

# SwarmNxt: 고속 애자일 공중 스웜을 위한 오픈소스 SW-HW 플랫폼

오픈소스 OmniNxt 드론 하드웨어 위에 구축된 엔드투엔드 스웜 툴킷. 상용 드론이 대부분 폐쇄형이거나
민첩한 비전 기반 협업 비행에 필요한 온보드 연산 자원이 부족하다는 문제, 그리고 다수 드론에 걸친
소프트웨어 개발·배포·유지보수의 공학적 부담을 동시에 해결하는 것을 목표로 한다.

## 구성

- **하드웨어 조립 가이드**: 비디오 튜토리얼을 포함한 상세 조립 절차 제공.
- **자동화 도구**: 병렬 소프트웨어 배포와 스웜 전체 업데이트를 지원.
- **ROS 2 기반 자율 내비게이션 프레임워크**: 제어·계획·깊이 추정을 단일 ROS 2 멀티에이전트
  시스템으로 통합해 물리적 스웜 실험을 위한 오픈 리서치 인프라를 제공.

## 검증 실험

- **6드론 스웜**: 분산형(decentralized) 계획 수립과 고속 드론 간 충돌 회피를 수행.
- **4드론 스웜**: 장애물이 가득한 환경에서 온보드 깊이 추정 기반 협업 비행을 수행.
- 두 실험 모두 실내에서 외부 모션 캡처로 글로벌 위치를 제공받았으나, 인지·계획·제어는 온보드에서
  자체 수행됨.

## 영향

시간 critical한 안전·보안·수색구조(SAR) 임무에서 다수 드론이 재난 현장을 신속히 조사하고
GPS 차단·붕괴 환경을 매핑할 수 있는 실전 실험용 오픈 인프라를 제공한다. 비행 제어 알고리즘과
군집 자율성 연구자 다수가 동일 하드웨어·소프트웨어 기반 위에서 재현 가능한 실험을 할 수 있게 한다.

## 관련 개념

- [[game-theoretic-drone-swarm-defense]] — 게임이론 기반 드론 스웜 방어 전술
- [[swarm-modes]] — 군집 드론 운용 모드 개요
- [[decentralized-swarm-gps-denied]] — GPS/통신 차단 환경 분산형 UAV 군집
