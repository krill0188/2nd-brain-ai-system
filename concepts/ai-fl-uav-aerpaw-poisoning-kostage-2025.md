---
title: "Federated Learning-enabled Network Incident Anomaly Detection Optimization for Drone Swarms (NSF AERPAW)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, data-poisoning, label-flipping, adversarial-training, differential-privacy, aerpaw, emulation]
sources: [inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]
confidence: medium
contested: false
contradictions: []
---

# Federated Learning-enabled Network Incident Anomaly Detection Optimization for Drone Swarms (NSF AERPAW)

- 원문: https://doi.org/10.1145/3700838.3700857 ; PDF https://par.nsf.gov/servlets/purl/10621115^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]
- 저자: Kevin Kostage, Rohan Adepu, Jenaya Monroe, Trevontae Haughton, Juan Mogollon, Saketh Poduvu, Kannappan Palaniappan, Chengyi Qu, Prasad Calyam, Reshmi Mitra^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]
- 발행: 2025-01 (ICDCN 2025, 2025-01-04~07, Hyderabad)^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]

## 핵심 내용 (NSF PAR PDF 본문 확인)
- 설정: NSF AERPAW 테스트베드의 고정 노드(집계 서버)와 이동 노드(클라이언트)로 Flower+TensorFlow FL, 드론 네트워크 이상(공격) 탐지 MLP, IoT 공격 데이터셋 2종. 오염 공격 2종(label flipping, feature noise)을 데이터에 주입, 방어는 TensorFlow 내장 강건 집계·차분 프라이버시와 적대적 학습.^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]
- 초록 수치: 오염량 33%에서 적대적 학습으로 정확도 최대 91.1%, 능동 드론 시나리오에서 CPU 사용량 최대 233% 증가.^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]
- 실기체 여부(본문 문구가 서로 다름): 서론 "real-world drone testbed", "flight durations ranging from 25 to 60 minutes" 라고 쓰는 한편, 같은 서론에서 "demonstrate the effectiveness ... in emulated scenarios using the AERPAW infrastructure", "simulated flight paths" 로 서술, 한계 절에 "absence of battery life monitoring during simulations", 결과 절에 "constant due to the emulation setup on the AERPAW". AERPAW 는 "virtual real-time emulations and approved real portable node missions" 둘 다 제공한다고 소개하나, 어느 결과가 실비행인지 본문에서 구분되지 않음.^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]
- 오염은 클라이언트 데이터에 소프트웨어로 라벨 뒤집기/잡음 주입(데이터 오염 시뮬레이션), 실제 기체 탈취·무선 공격 아님.^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 방어(적대적 학습)는 정확도를 지키지만 CPU 부하 최대 233% 증가라는 비용이 있어 온보드 연산 예산과 상충.^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]

## 한계·미확인
- 실비행 구간이 어느 것인지 불명확(에뮬레이션과 혼재 서술)이므로 "실기체 실증"으로 분류하지 않음. 공격은 데이터 오염 주입 모델이고 기체 대상 공격 시험 아님. 신뢰도 중(ACM 학회 논문, 본문 직접 확인했으나 서술 모순).^[inbox/processed/hw-20261022-ai-fl-uav-aerpaw-poisoning-kostage-2025.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[swarm-coordination]]
