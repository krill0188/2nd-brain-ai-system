---
title: "Galilean State Estimation for Inertial Navigation Systems with Unknown Time Delay"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: navigation-gnss-denied
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]
confidence: medium
contested: false
contradictions: []
---

# Galilean State Estimation for Inertial Navigation Systems with Unknown Time Delay

- 원문: https://arxiv.org/abs/2605.13266^[inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]
- 저자: Giulio Delama, Martin Scheiber, Yixiao Ge, Tarek Hamel, Stephan Weiss, Robert Mahony^[inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]
- 발행: 2026-05-13 (arXiv)^[inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]

## 핵심 내용
상용 GNSS 수신기는 50~300 ms 미지의 지연을 갖고, 보상하지 않으면 INS 성능이 저하된다. 최신 온라인 방식은 지연을 EKF 상태로 추정하는 것인데, 본 논문은 Galilean 대칭을 이용해 항법 상태와 지연을 함께 추정하는 Equivariant Filter(EqF)를 제안한다. 고정익 UAV 2대(GNSS 지연 90 ms, 120 ms)로 2~3분 비행 검증, 시뮬레이션은 최대 500 ms. EKF는 지연이 커지면 비일관·성능 저하, EqF는 정확도·일관성 유지.^[inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 상용 GNSS 지연 50~300 ms (초록)^[inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]
- 실비행 지연 90 ms, 120 ms; 시뮬레이션 최대 500 ms^[inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]
- FC에서 GPS 지연 파라미터(EKF2_GPS_DELAY 등)를 실측해야 하는 근거^[inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]

## 한계·미확인
초록 기준. 정량 오차 개선율 미확인. PPS 하드웨어 동기와의 비교는 다루지 않음(확인 범위).^[inbox/processed/hw-20261021-fusion-delama-galilean-gnss-delay-2605.13266.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
