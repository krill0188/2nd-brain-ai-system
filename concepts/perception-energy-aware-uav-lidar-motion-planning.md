---
title: "인지·에너지 인식 UAV 모션 계획 (이분산 불확실성 학습 모델)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-21-arxiv-perception-and-energy-aware-motion-planning-for-uav-using-le.md]
confidence: medium
contested: false
contradictions: []
---

# 인지·에너지 인식 UAV 모션 계획 (이분산 불확실성 학습 모델)

Takemura·Ishigami(arXiv 2309.14272, 2023-09)의 GNSS 차단 환경 UAV 모션 계획 논문. 초록 기준 요약이다.^[inbox/processed/fetch-2026-10-21-arxiv-perception-and-energy-aware-motion-planning-for-uav-using-le.md]

- **비용 함수**: UAV 총 에너지 소비와 탑재 LiDAR의 인지 품질 두 지표를 함께 최적화한다.
- **학습**: 비행 전 고충실도 시뮬레이터로 비행 데이터를 얻어, 수평 속도의 함수로서 에너지 소비와 LiDAR 측정의 이분산(heteroscedastic) 불확실성을 학습한다.
- **온라인 계획**: 학습 모델로 에너지·인지 품질을 추정해 배터리 사용량과 위치추정 오차를 줄인다.
- **검증**: 사실적 환경 시뮬레이션에서 에너지 효율과 인지 품질의 트레이드오프를 다룰 수 있음을 확인했다. 코드는 공개(GitLab)됐다.

## 관련
[[multirotor-energy-power-models]], LiDAR 관성 오도메트리 [[flight-ready-lidar-inertial-odometry]], GNSS 차단 평가 [[visual-slam-gps-denied-evaluation]].
