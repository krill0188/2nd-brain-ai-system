---
title: "A Digital Twin Empowered Lightweight Model Sharing Scheme for Multi-Robot Systems"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
tags: [drone, digital-twin, knowledge-distillation, multi-uav, edge]
sources: [inbox/processed/hw-20261021-conv-dt-model-sharing-xiong-2023.md]
confidence: medium
contested: false
contradictions: []
---

# A Digital Twin Empowered Lightweight Model Sharing Scheme for Multi-Robot Systems

- 원문: arXiv:2305.02214^[inbox/processed/hw-20261021-conv-dt-model-sharing-xiong-2023.md]
- 저자: Kai Xiong, Zhihong Wang, Supeng Leng, Jianhua He^[inbox/processed/hw-20261021-conv-dt-model-sharing-xiong-2023.md]
- 발행: 2023-05-03^[inbox/processed/hw-20261021-conv-dt-model-sharing-xiong-2023.md]

## 핵심 내용
제조 환경 UAV 팀의 3차원 장면 인식 문제. 온보드 센싱·연산이 제한적이라, 엣지 서버에 둔 각 UAV의 디지털 트윈이 지식 증류를 안내해 여러 경량 모델을 만들고 최적 모델을 배포한다. 디지털 트윈은 모델 공유 네트워크 토폴로지와 모델 구조도 조정하며, 네트워크 캘큘러스로 자원 소모 최소화와 수렴을 보장한다. 공개 포인트클라우드 데이터셋 시뮬레이션에서 개별 모델 대비 연산 자원 활용과 인식 정확도가 개선된다고 보고.^[inbox/processed/hw-20261021-conv-dt-model-sharing-xiong-2023.md]
원문 인용: "Digital Twin (DT) empowered Knowledge Distillation (KD) method"^[inbox/processed/hw-20261021-conv-dt-model-sharing-xiong-2023.md]

## 설계·운용에 쓸 수 있는 지침
- 장치 트윈(UAV별) + 엣지 트윈(집합) 2계층에서 경량 모델 배포 결정을 내리는 구조 참고.^[inbox/processed/hw-20261021-conv-dt-model-sharing-xiong-2023.md]

## 한계·미확인
- 초록에 수치 없음. 실기 검증 미확인.^[inbox/processed/hw-20261021-conv-dt-model-sharing-xiong-2023.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[drone-simulation]]
