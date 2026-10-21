---
title: "Champion-level drone racing using deep reinforcement learning"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
tags: [drone, swift, reinforcement-learning, sim2real, onboard-latency, jetson-tx2]
sources: [inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Champion-level drone racing using deep reinforcement learning

- 원문: https://pmc.ncbi.nlm.nih.gov/articles/PMC10468397/ (Nature 620:982-987, DOI 10.1038/s41586-023-06419-4; PMC 오픈액세스 CC BY 4.0)^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 저자: Elia Kaufmann, Leonard Bauersfeld, Antonio Loquercio, Matthias Müller, Vladlen Koltun, Davide Scaramuzza^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 발행: 2023-08-30^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]

## 핵심 내용
Swift는 온보드 센싱·연산만으로 비행하는 자율 레이싱 드론으로, 시뮬레이션 강화학습과 실비행 데이터를 결합한다. 세 명의 인간 챔피언과 맞대결해 각 상대에게 여러 레이스를 이기고 최단 레이스 기록을 냈다. nature.com 접근 실패의 대체 경로(PMC 전문).^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
원문 수치(PMC 본문 추출):^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 하드웨어: Jetson TX2(6코어 CPU 2 GHz, GPU 256 CUDA 코어 1.3 GHz), RealSense T265(VIO 100 Hz, 카메라 30 Hz), STM32 216 MHz에서 Betaflight, 기체 870 g, 최대 정적 추력 약 35 N, 추력중량비 4.1.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 게이트 검출기 1회 순전파 40 ms(Jetson TX2, FP16, 384x384), 레이싱 정책 CPU 추론 8 ms.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 감각운동 지연: Swift 40 ms, 전문 인간 조종사 평균 220 ms.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 트랙: 7게이트, 30x30x8 m, 75 m 랩. 승패: Vanover 5/9, Bitmatta 4/7, Schaepper 6/9. 최고 인간 기록 대비 0.5 s 우위, 단일 랩 차이 0.16 s 언급.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 정책/가치망: 2층 MLP 128 노드, 관측 31차원, 행동 4차원(추력+몸체 각속도), PPO, 1x10^8 상호작용(워크스테이션 약 50분), 미세조정 2x10^7.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 데이터: 모캡 레이스 기록과 의사코드는 Zenodo(10.5281/zenodo.7955278), 전체 코드는 오용 방지를 위해 비공개.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- 온보드 지각(40 ms)+정책(8 ms) 구조로 40 ms 감각운동 지연을 달성한 사례.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]
- 잔차 동역학 모델(k-NN, k=5)로 시뮬-실제 격차를 줄임.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]

## 한계·미확인
- 추출 요약 기반, 절대 랩타임은 본문에 없다고 보고됨. 제어 루프 주파수(정책 출력 주기)는 미확인.^[inbox/processed/hw-20261021-ai-sim2real-swift-champion-drone-racing-kaufmann-2023.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-simulation]]
