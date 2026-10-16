---
title: "다중 스펙트럼 헬리패드 기반 야간 UAV 정밀 착륙 (IR 정렬 + 거리센서 하강)"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: flight-control
tags: [drone, drone-sw, drone-ai]
sources: [inbox/processed/fetch-2026-10-16-kci-다중-스펙트럼-헬리패드를-이용한-야간-uav-정밀-착륙-ir적외선-영상-기반-정렬-및-거리-센서-기반-하강-.md]
confidence: low
contested: false
contradictions: []
---

# 다중 스펙트럼 헬리패드 기반 야간 UAV 정밀 착륙

김동현(국립금오공과대학교), 한국통신학회논문지 2026. 원문 비공개로 초록만 근거라 confidence는 low이다.

- RGB·IR·열화상 카메라 모두에서 검출되도록 헬리패드를 설계해, 센서 모달리티가 바뀌어도 하나의 인지–제어 파이프라인으로 운용한다.
- 착륙은 탐색–정렬–하강 3단계다. 정렬 단계는 IR 마커 중심 오차로 수평 오차를 줄이고, 최종 하강 단계는 거리 측정값으로 수직 속도를 제한한다.
- 구현은 PX4 오프보드 제어와 ROS 2 기반이다.
- 주·야간 실험(착륙 오프셋, 성공률, 착륙시간, 실시간 성능)에서 RGB·IR·열화상 모두 평균 30fps, 평균 착륙오차 16.1 cm 이내, 성공률 100%를 보고했다.^[inbox/processed/fetch-2026-10-16-kci-다중-스펙트럼-헬리패드를-이용한-야간-uav-정밀-착륙-ir적외선-영상-기반-정렬-및-거리-센서-기반-하강-.md]

시행 횟수와 조건은 초록에 없다. 관련: [[rtk-gps-precise-landing]], [[px4-offboard-control]], [[ros2-drone-integration]], [[kci-vtol-swarm-takeoff-landing-operation]].
