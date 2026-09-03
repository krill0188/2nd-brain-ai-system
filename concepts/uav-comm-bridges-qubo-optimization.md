---
title: "재난 대응 UAV 통신 브릿지 조합 최적화 (QUBO/양자 컴퓨팅)"
created: 2026-09-04
updated: 2026-09-04
type: concept
domain: comms-protocol
tags: [drone, datalink, swarm, comms-protocol]
sources: []
confidence: medium
contested: false
contradictions: []
---

# 재난 대응 UAV 통신 브릿지 조합 최적화 (QUBO/양자 컴퓨팅)

**저자**: Matteo Vandelli, Daniele Dragoni  
**발행일**: 2026-09-02  
**arXiv**: http://arxiv.org/abs/2609.02562v1

## 연구 개요

자연 재해 피해 지역에서 구조 작전을 지원하기 위해 5G 안테나를 탑재한 UAV를 전략적으로 배치하는 조합 최적화 문제를 다룬다. 플라잉 애드혹 네트워크(FANET) 상에서 신호 커버리지 극대화·간섭 최소화·네트워크 연결성 보장을 동시에 달성하는 것이 목표다.

## 수리적 정식화

- **정수 이차 계획법(IQP)**: 기본 문제 정식화; 다중 주파수 사용으로 간섭 완화
- **CPLEX 솔버**: 수치 해법 및 확장성 분석
- **QUBO 변환**: 양자 알고리즘 적용을 위해 이진 최적화 문제로 재정식화

## 주요 발견

- 후보 사이트 수 증가에 따라 TTS(Time-to-Solution)가 지수적으로 증가 → 긴급 실시간 시나리오에서 고전 솔버의 한계
- **시간 제한 근사 해**: 최적해는 아니지만 대부분의 경우 연결성 보존; 실용적 트레이드오프 제공
- **양자 단열 알고리즘(QAA)**: HPC 에뮬레이션에서 소규모 인스턴스 정확 해결 → 대규모 재난 대응에 양자 컴퓨팅 적용 가능성 제시

## 의의

UAV 긴급 배치 최적화에 양자 컴퓨팅을 접목한 선도적 연구다. FANET 네트워크 최적화 문제에 QUBO 정식화를 적용하는 새로운 패러다임을 제시하며, 재난 드론 운용 인프라 설계에 참고 가치가 있다.

## 관련 페이지

드론 데이터링크·무선 통신 기술은 [[datalink-communication]]을, 다중 UAV 네트워킹 아키텍처는 [[unet-multi-uav-networking]]을 참조한다.
