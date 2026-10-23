---
title: "ALFA: A Dataset for UAV Fault and Anomaly Detection"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: FlightLogData
tags: [drone, anomaly-detection, fault-prediction, dataset, flight-log]
sources: [inbox/processed/hw-20261021-data-anomaly-alfa-keipour-2019.md]
confidence: medium
contested: false
contradictions: []
---

# ALFA: A Dataset for UAV Fault and Anomaly Detection

- 원문: arXiv:1907.06268^[inbox/processed/hw-20261021-data-anomaly-alfa-keipour-2019.md]
- 저자: Azarakhsh Keipour, Mohammadreza Mousaei, Sebastian Scherer^[inbox/processed/hw-20261021-data-anomaly-alfa-keipour-2019.md]
- 발행: 2019-07-14 (v2 2020-10-24)^[inbox/processed/hw-20261021-data-anomaly-alfa-keipour-2019.md]

## 핵심 내용
고정익 UAV의 제어면·엔진 고장을 담은 실비행 데이터셋. 고장 검출·분리(FDI)와 이상 탐지 연구용이다. 처리된 데이터는 47회 자율비행: 23회는 갑작스러운 엔진 완전 정지, 24회는 7종의 다른 제어면 고장. 합계 정상비행 66분, 고장 후 비행 13분. 그 밖에 자율/보조/수동 비행의 원시 데이터 수 시간 분량, 고장 시각·유형 정답, 보조 도구와 평가 지표가 포함된다.^[inbox/processed/hw-20261021-data-anomaly-alfa-keipour-2019.md]
원문 인용: "Most of the current fault detection methods are evaluated in simulation"^[inbox/processed/hw-20261021-data-anomaly-alfa-keipour-2019.md]

## 설계·운용에 쓸 수 있는 지침
- 비행 로그 기반 고장 탐지의 실데이터 평가 기준으로 사용 가능(시뮬레이션 평가의 한계 보완).^[inbox/processed/hw-20261021-data-anomaly-alfa-keipour-2019.md]

## 한계·미확인
- 고정익 한정이며 멀티로터 일반화는 원문 초록에서 미확인. 센서 채널 목록·로그 형식 미확인(초록만 열람).^[inbox/processed/hw-20261021-data-anomaly-alfa-keipour-2019.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[drone-esc-failure-cases]]
