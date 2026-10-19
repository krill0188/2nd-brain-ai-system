---
title: "E-Rocket: TVC 로켓 GNC 검증용 저가 테스트베드 (PX4 + ROS 2)"
created: 2026-10-18
updated: 2026-10-18
type: concept
domain: flight-control
tags: [drone, drone-sw, drone-hw]
sources: [inbox/processed/fetch-2026-10-18-arxiv-the-e-rocket-low-cost-testbed-for-tvc-rocket-gnc-validation.md]
confidence: medium
contested: false
contradictions: []
---

# E-Rocket (TVC GNC 테스트베드)

**출처**: arXiv 2512.06535 v2 (2025-12-06), Pedro Santos 외. 초록 기준.

추력 벡터 제어(TVC) 기반 로켓 GNC 알고리즘 검증용 전기 구동 저가 프로토타입이다.^[inbox/processed/fetch-2026-10-18-arxiv-the-e-rocket-low-cost-testbed-for-tvc-rocket-gnc-validation.md]

- **하드웨어**: 시판 부품과 3D 프린트 부품, 서보로 구동되는 짐벌 위의 역회전 BLDC 모터 한 쌍으로 추력 벡터링을 구현한다.
- **소프트웨어**: 이중 컴퓨터 구성으로 PX4 오토파일럿과 ROS 2 모듈성을 활용해 맞춤 GNC 알고리즘을 수용한다.
- **검증**: 실내 모션캡처 공간에서 PID 기반 궤적 추종 기준 제어기로 정확한 추종을 보였고 테스트베드로서 적합하다고 결론 냈다(수치는 초록에 없음).

관련: [[px4-flight-stack]], [[ros2-drone-integration]], [[spinner-self-rotating-tri-rotor]].
