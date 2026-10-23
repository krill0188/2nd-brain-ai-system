---
title: "[Release] AI Flight Integrity Observer: Measuring PX4 Offboard degradation under controlled AI inference lag"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
ontology_class: TimingLatency
tags: [drone, latency, px4, offboard, ros2, inference-lag, sitl]
sources: [inbox/processed/hw-20261021-ai-latency-px4-offboard-afio-forum-2026.md]
confidence: medium
contested: false
contradictions: []
---

# [Release] AI Flight Integrity Observer: Measuring PX4 Offboard degradation under controlled AI inference lag

- 원문: https://discuss.px4.io/t/release-ai-flight-integrity-observer-measuring-px4-offboard-degradation-under-controlled-ai-inference-lag/49117^[inbox/processed/hw-20261021-ai-latency-px4-offboard-afio-forum-2026.md]
- 저자: zc_Liu (Dronecode Forum post)^[inbox/processed/hw-20261021-ai-latency-px4-offboard-afio-forum-2026.md]
- 발행: 2026-06-17^[inbox/processed/hw-20261021-ai-latency-px4-offboard-afio-forum-2026.md]

## 핵심 내용
커뮤니티 포럼 글(비동료심사, 신뢰도 낮음). ROS 2 수동 관측기 AFIO가 PX4 Offboard 설정점 스트림의 신선도와 시간 일관성(setpoint age, jitter, stale stream)을 감시한다. Gazebo/PX4 SITL 원형 추종 미션, ROS 2 Humble/Jazzy, PX4 v1.14/1.15에서 AI 추론 지연을 주입한 결과(관측기는 주입값을 모름):^[inbox/processed/hw-20261021-ai-latency-px4-offboard-afio-forum-2026.md]

| 주입 지연 | 결과 | 주원인 | Jitter p95 | Flight residual p95 |
|---|---|---|---|---|
| 0 ms | 100% OK | NONE | 50.9 ms | 0.214 |
| 30 ms | 100% OK | NONE | 57.2 ms | 0.237 |
| 80 ms | 100% OK | NONE | 64.4 ms | 0.264 |
| 150 ms | 100% WARN | 96.9% SETPOINT_JITTER | 119.0 ms | 0.483 |
| 300 ms | WARN+ERROR | SETPOINT_JITTER / STALE_STREAM | 277.2 ms | 1.107 |

저자 해석: 약 80 ms까지 정렬 유지, 150 ms에서 열화가 측정되고, 300 ms에서 신선도 경계를 넘음. 포럼 답글은 탐지가 AI 모델이 아닌 규칙 기반(가중합과 고정 임계값)이라고 지적.^[inbox/processed/hw-20261021-ai-latency-px4-offboard-afio-forum-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- SITL 원형 추종에서 0~80 ms 지연은 OK, 150 ms부터 WARN으로 분류된 값이 있음(저자 임계값 미공개).^[inbox/processed/hw-20261021-ai-latency-px4-offboard-afio-forum-2026.md]

## 한계·미확인
- SITL 한정, 실기체 검증 미확인, 임계값 미공개, 동료심사 없음, 코드(GitHub ZC502/ai_flight_integrity_observer)는 직접 열람하지 않음.^[inbox/processed/hw-20261021-ai-latency-px4-offboard-afio-forum-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[px4-offboard-control]]
