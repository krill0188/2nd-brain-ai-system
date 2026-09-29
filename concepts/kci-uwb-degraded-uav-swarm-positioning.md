---
title: "UWB 품질 저하 환경에서 UAV 군집측위 최소운용조건 분석 (KCI)"
created: 2026-09-17
updated: 2026-09-17
type: concept
domain: comms-protocol
tags: [drone, datalink, swarm]
sources: [raw/papers/_unclassified/uwb-품질-저하-환경에서-uav-군집측위의최소운용조건분석.md]
confidence: medium
contested: false
contradictions: []
---

# UWB 품질 저하 환경에서 UAV 군집측위 최소운용조건 분석 (KCI)

김요셉(숭실대)이 《한국통신학회논문지》(2026)에 발표한 논문으로, GPS 신호가
제한된 환경에서 UAV 군집 운용 시 발생하는 위치 오차 누적 문제를 완화하기
위해 기존 Drift-Correction LSTM 모델 및 UWB/EKF 기반 UAV 군집 측위 기법의
실제 운용 관점 성능 한계와 최소 운용조건을 정량 분석한다.^[raw/papers/_unclassified/uwb-품질-저하-환경에서-uav-군집측위의최소운용조건분석.md]

## 핵심 결과

- AirSim 시뮬레이터 기반 실험으로 UWB 품질 저하 환경에서 목표 정확도를
  유지 가능한 UWB 품질 범위를 도출.
- 군집 규모가 증가하더라도 최소 링크 구성만으로 목표 정확도를 만족하며
  측정 부하(measurement load)를 절감할 수 있음을 검증.

## 관련 개념

- [[decentralized-swarm-gps-denied]] — GPS/통신 차단 환경 분산형 UAV 군집 표적 보호
- [[uav-swarm-target-localization]] — 다중경로 환경에서 UAV 스웜 표적 위치 추정
