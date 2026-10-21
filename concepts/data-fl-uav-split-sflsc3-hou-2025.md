---
title: "Split Federated Learning for Low-Altitude Wireless Networks: Joint Sensing, Communication, Computation, and Control Co-design"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, split-learning, isac, co-design]
sources: [inbox/processed/hw-20261021-data-fl-uav-split-sflsc3-hou-2025.md]
confidence: medium
contested: false
contradictions: []
---

# Split Federated Learning for Low-Altitude Wireless Networks: Joint Sensing, Communication, Computation, and Control Co-design

- 원문: arXiv:2504.01443^[inbox/processed/hw-20261021-data-fl-uav-split-sflsc3-hou-2025.md]
- 저자: Xiangwang Hou, Xianghe Wang, Jiacheng Wang, Zekai Zhang, Jun Du, Jingjing Wang, Yong Ren^[inbox/processed/hw-20261021-data-fl-uav-split-sflsc3-hou-2025.md]
- 발행: 2025-04-02 (v2 2026-01-29)^[inbox/processed/hw-20261021-data-fl-uav-split-sflsc3-hou-2025.md]

## 핵심 내용
UAV 지원 연합 엣지 학습에 분할 연합학습을 도입한 SFLSC3 프레임워크. 자원 제약 UAV가 전체 모델을 학습해야 하는 기존 방식의 계산·프라이버시·통신 비용 문제를 UAV와 엣지 서버가 학습을 나눠 맡아 줄인다. UAV 배치, 분할 지점, 센싱량, 클라이언트 측 집계 빈도에 대한 수렴 격차의 닫힌형 상한을 유도하고, 목표 정확도까지의 지연을 최소화하는 비볼록 공동 최적화를 저복잡도 알고리즘으로 푼다. 표적 동작 인식 과제 시뮬레이션에서 기준선보다 수렴과 지연이 좋다고 보고.^[inbox/processed/hw-20261021-data-fl-uav-split-sflsc3-hou-2025.md]
원문 인용: "SFLSC3 optimally partitions model training between UAVs and edge servers"^[inbox/processed/hw-20261021-data-fl-uav-split-sflsc3-hou-2025.md]

## 설계·운용에 쓸 수 있는 지침
- 모델 분할 지점과 센싱·통신·연산·제어를 함께 설계하는 공동 최적화 변수 목록으로 참고.^[inbox/processed/hw-20261021-data-fl-uav-split-sflsc3-hou-2025.md]

## 한계·미확인
- 초록에 수치 없음. 실기 검증 여부 미확인.^[inbox/processed/hw-20261021-data-fl-uav-split-sflsc3-hou-2025.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[swarm-coordination]]
