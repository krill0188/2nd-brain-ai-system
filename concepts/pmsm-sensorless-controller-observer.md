---
title: "PMSM 센서리스 제어기-관측기 (UAV 프로펠러 적용)"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: hardware
tags: [drone, drone-hw]
sources: [inbox/processed/fetch-2026-10-17-arxiv-a-robust-sensorless-controller-observer-strategy-for-pmsms-w.md]
confidence: medium
contested: false
contradictions: []
---

# PMSM 센서리스 제어기-관측기

**출처**: arXiv 2002.01823 (2020-02-05)

영구자석 동기 전동기(PMSM)의 토크/전류 제어기와 위치·속도·자속·고정자 저항 관측기를 결합한 혼합 센서리스 전략이다. 완전 가관측성을 위해 신호 주입 기법을 함께 설계한다.^[inbox/processed/fetch-2026-10-17-arxiv-a-robust-sensorless-controller-observer-strategy-for-pmsms-w.md]

## 핵심
- 속도 일정/완만 변화 가정이나 기계 모델 정보 없이, 회전자 속도를 부호가 일정하고 크기가 0이 아닌 미지 입력 외란으로 모델링한다.^[inbox/processed/fetch-2026-10-17-arxiv-a-robust-sensorless-controller-observer-strategy-for-pmsms-w.md]
- 경사하강 저항/역기전력 추정과 단위원(unit circle) 표현을 결합하고, 영역 실용 점근 안정성을 증명했다. 인력 영역은 임의로 크게 만들 수 있다(저차원 다양체 제외).^[inbox/processed/fetch-2026-10-17-arxiv-a-robust-sensorless-controller-observer-strategy-for-pmsms-w.md]
- 검증은 UAV 프로펠러 제어를 가정한 수치 시뮬레이션이다(하드웨어 실험 없음).^[inbox/processed/fetch-2026-10-17-arxiv-a-robust-sensorless-controller-observer-strategy-for-pmsms-w.md]

## 관련
BLDC/ESC 특성 연구는 [[bldc-motor-esc-characterization-research]], ESC 고장 사례는 [[drone-esc-failure-cases]] 참조.
