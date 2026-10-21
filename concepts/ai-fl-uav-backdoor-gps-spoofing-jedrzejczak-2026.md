---
title: "Receiver-Domain Behavioral Probing for Backdoor-Resilient Federated GPS Spoofing Detection in UAV Networks"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, poisoning, backdoor, gps-spoofing, byzantine]
sources: [inbox/processed/hw-20261021-ai-fl-uav-backdoor-gps-spoofing-jedrzejczak-2026.md]
confidence: medium
contested: false
contradictions: []
---

# Receiver-Domain Behavioral Probing for Backdoor-Resilient Federated GPS Spoofing Detection in UAV Networks

- 원문: https://arxiv.org/abs/2610.10360^[inbox/processed/hw-20261021-ai-fl-uav-backdoor-gps-spoofing-jedrzejczak-2026.md]
- 저자: Will Jedrzejczak, Cole Walther, Dilpreet Gill, Moh Khalid Hasan^[inbox/processed/hw-20261021-ai-fl-uav-backdoor-gps-spoofing-jedrzejczak-2026.md]
- 발행: 2026-10-07^[inbox/processed/hw-20261021-ai-fl-uav-backdoor-gps-spoofing-jedrzejczak-2026.md]

## 핵심 내용 (arXiv 초록)
UAV 함대가 원시 수신기 데이터를 공유하지 않고 GPS 스푸핑 탐지기를 연합학습하는 설정. 클라이언트가 보고한 자체 검증 정확도로 가중치를 주는 설계는 공격 수단이 됨: 10대 중 2대가 데이터 일부를 오염시키고 업데이트를 키우고 정확도를 부풀리면 backdoor lift +0.3036(부풀리지 않은 같은 공격보다 높음). 제안: coordinator가 판별력 있는 GPS 특징을 정상값으로 바꾼 반사실(counterfactual) 스푸핑 샘플로 모든 제출 모델을 평가해 클라이언트가 "주장하는 것이 아니라 모델이 하는 것"으로 가중. IID에서 공격 lift를 -0.0265로 감소(정직한 함대와 통계적으로 구분 안 됨). 공격자 수가 설정값을 넘으면 Multi-Krum은 +0.0061에서 +0.2837로 악화, 제안법은 기준선 근처 유지. 단일 공개 수신기 데이터셋을 가상 클라이언트로 분할해 평가; 클라이언트 이질성이 강하면 실패한다고 보고.^[inbox/processed/hw-20261021-ai-fl-uav-backdoor-gps-spoofing-jedrzejczak-2026.md]

## 설계에 쓸 수 있는 지침
- 클라이언트 자기 보고 지표를 집계 가중치로 쓰지 말 것. 서버 측 독립 검증(반사실 샘플) 필요.^[inbox/processed/hw-20261021-ai-fl-uav-backdoor-gps-spoofing-jedrzejczak-2026.md]
- 포이즈닝 방어는 정직한 다수만 가정하는 방식이 정확한 공격자 수 가정(Multi-Krum)보다 강건하다고 보고.^[inbox/processed/hw-20261021-ai-fl-uav-backdoor-gps-spoofing-jedrzejczak-2026.md]

## 한계·미확인
- 초록만 열람. 실제 기체 시험 아님(시뮬레이션 분할). 강한 이질성에서 실패. 방어 대상은 모델 포이즈닝이며 모델 반전·차등 프라이버시는 다루지 않음(초록상 미언급).^[inbox/processed/hw-20261021-ai-fl-uav-backdoor-gps-spoofing-jedrzejczak-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[swarm-coordination]]
