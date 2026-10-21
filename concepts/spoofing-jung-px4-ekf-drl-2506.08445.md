---
title: "GPS Spoofing Attacks on AI-based Navigation Systems with Obstacle Avoidance in UAV"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-spoofing-jung-px4-ekf-drl-2506.08445.md]
confidence: medium
contested: false
contradictions: []
---

# GPS Spoofing Attacks on AI-based Navigation Systems with Obstacle Avoidance in UAV

- 원문: https://arxiv.org/abs/2506.08445^[inbox/processed/hw-20261021-spoofing-jung-px4-ekf-drl-2506.08445.md]
- 저자: Ji Hyuk Jung, Mi Yeon Hong, Ji Won Yoon^[inbox/processed/hw-20261021-spoofing-jung-px4-ekf-drl-2506.08445.md]
- 발행: 2025-06-10 (arXiv, cs.CR; IEEE Access 2025)^[inbox/processed/hw-20261021-spoofing-jung-px4-ekf-drl-2506.08445.md]

## 핵심 내용
DRL 기반 드론 항법에 대한 GPS 스푸핑 공격을 연구한다. PX4 EKF 센서융합을 겨냥한 공격 모델을 만들고 DRL 항법과 결합하여 현실적 시나리오를 구성했다. 기본 DRL 시스템과 DRL+PX4 구성 모두에서 공격이 성공함을 실험으로 보인다. (시뮬레이션 기반으로 보이나 초록만으로 확정 불가)^[inbox/processed/hw-20261021-spoofing-jung-px4-ekf-drl-2506.08445.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- PX4 EKF 센서융합이 스푸핑 표적이 됨을 시사^[inbox/processed/hw-20261021-spoofing-jung-px4-ekf-drl-2506.08445.md]
- 정량 지침 없음^[inbox/processed/hw-20261021-spoofing-jung-px4-ekf-drl-2506.08445.md]

## 한계·미확인
초록에 정량 수치 없음. 실비행 여부 미확인.^[inbox/processed/hw-20261021-spoofing-jung-px4-ekf-drl-2506.08445.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
