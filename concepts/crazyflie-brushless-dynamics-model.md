---
title: "How to Model Your Crazyflie Brushless: 나노 쿼드콥터 동역학 모델"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: hardware
ontology_class: Multirotor
tags: [drone, drone-hw, drone-ai]
sources: [inbox/processed/fetch-2026-10-17-arxiv-how-to-model-your-crazyflie-brushless.md]
confidence: medium
contested: false
contradictions: []
---

# How to Model Your Crazyflie Brushless

**저자**: Gräfe, Scherer, Hönig, Trimpe (arXiv 2603.05944, 2026-03-06)

2025년 초 출시된 Crazyflie Brushless는 브러시드 모터를 쓰는 Crazyflie 2.1보다 추력이 약 50% 크다.^[inbox/processed/fetch-2026-10-17-arxiv-how-to-model-your-crazyflie-brushless.md] 이 논문은 해당 기체의 동역학 모델과 핵심 파라미터를 식별하고, 시뮬레이션·하드웨어 분석으로 모델 정확도를 평가한다. 제작사 개요는 [[bitcraze]] 참조.

## 주요 결과
- 모델 기반으로 end-to-end 신경망 위치 제어기를 학습했다.^[inbox/processed/fetch-2026-10-17-arxiv-how-to-model-your-crazyflie-brushless.md]
- 수직 이동 1.8 m만으로 2회전 백플립을 수행하는 제어기를 학습했고 시뮬레이션에서 하드웨어로 전이에 성공했다.^[inbox/processed/fetch-2026-10-17-arxiv-how-to-model-your-crazyflie-brushless.md]
- 도메인 랜덤화가 제어 성능에 미치는 영향을 조사해 sim-to-real 격차 해소에 관한 시사점을 제시했다.^[inbox/processed/fetch-2026-10-17-arxiv-how-to-model-your-crazyflie-brushless.md]
- 프로젝트 전체를 오픈소스로 공개했다.^[inbox/processed/fetch-2026-10-17-arxiv-how-to-model-your-crazyflie-brushless.md]

## 관련
RL 기반 쿼드로터 제어는 [[rl-quadrotor-tunable-control]], [[agile-quadrotor-learning]] 참조. 초록 기준 요약이며 파라미터 수치는 원문에 없다.

## 📰 최근 관련 소식
- Your Own Personal eVTOL? Skyfly Raises $10 Million to Bring the Axe to Market (dronelife.com, Tue, 20 Oc) — https://dronelife.com/2026/10/20/skyfly-personal-evtol-aircraft-funding/
