---
title: "Privacy-Preserving Federated Learning for UAV-Enabled Networks: Learning-Based Joint Scheduling and Resource Management"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, privacy, communication]
sources: [inbox/processed/hw-20261021-data-fl-uav-privacy-yang-2020.md]
confidence: medium
contested: false
contradictions: []
---

# Privacy-Preserving Federated Learning for UAV-Enabled Networks: Learning-Based Joint Scheduling and Resource Management

- 원문: arXiv:2011.14197^[inbox/processed/hw-20261021-data-fl-uav-privacy-yang-2020.md]
- 저자: Helin Yang, Jun Zhao, Zehui Xiong, Kwok-Yan Lam, Sumei Sun, Liang Xiao^[inbox/processed/hw-20261021-data-fl-uav-privacy-yang-2020.md]
- 발행: 2020-11-28^[inbox/processed/hw-20261021-data-fl-uav-privacy-yang-2020.md]

## 핵심 내용
UAV를 공중 기지국으로 쓰는 네트워크용 비동기 연합학습 프레임워크. 단말은 로컬 학습하여 원시 데이터가 UAV 서버로 가지 않는다. 저품질 단말을 걸러내는 장치 선택을 두고, A3C 알고리즘으로 장치 선택, UAV 배치, 자원 관리를 공동 최적화한다. 기존 방법보다 학습 정확도가 높고 연합학습 실행이 빠르다고 보고한다.^[inbox/processed/hw-20261021-data-fl-uav-privacy-yang-2020.md]
원문 인용: "it is impractical to send raw data of devices to UAV servers for model training"^[inbox/processed/hw-20261021-data-fl-uav-privacy-yang-2020.md]

## 설계·운용에 쓸 수 있는 지침
- 통신 제약 환경에서 원시 데이터 전송 대신 모델 갱신만 교환하는 구조의 근거로 인용 가능.^[inbox/processed/hw-20261021-data-fl-uav-privacy-yang-2020.md]

## 한계·미확인
- 초록에 수치 없음. 차등 프라이버시 등 형식적 보장 여부는 초록에서 미확인.^[inbox/processed/hw-20261021-data-fl-uav-privacy-yang-2020.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[swarm-coordination]]
