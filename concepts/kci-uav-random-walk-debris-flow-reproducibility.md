---
title: "UAV 관측자료 기반 Random Walk 토석류 이동범위 공간적 재현성 평가: 2023 예천 벌방리 (KCI)"
created: 2026-10-09
updated: 2026-10-09
type: concept
domain: ops-mission
tags: [drone, ops-mission, research]
sources: [inbox/processed/fetch-2026-10-09-kci-uav-관측자료를-이용한-random-walk-기반-토석류-이동범위의-공간적-재현성-평가-2023년-예천-벌.md]
confidence: low
contested: false
contradictions: []
---

# UAV 관측 기반 Random Walk 토석류 이동범위 재현성 (KCI)

남경훈(한국화재보험협회), 『지질공학』 2026. 원문 비공개, 초록도 중간에서 절단되어 있어 결론부는 확인하지 못했다(confidence low).^[inbox/processed/fetch-2026-10-09-kci-uav-관측자료를-이용한-random-walk-기반-토석류-이동범위의-공간적-재현성-평가-2023년-예천-벌.md]

## 설계

- 2023년 경북 예천 벌방리 토석류가 대상이다. UAV와 현장조사로 확인한 실제 발생지점 5곳을 Random Walk Model(RWM)의 방출 위치로 써서 발생위치 불확실성을 줄였다.
- 10 m 격자에서 Random Walk 10³회와 10⁴회를 비교해 계산 안정성을 보고, 이동성 매개변수와 정규화 영향빈도(NIF) 임계값을 민감도 분석했다.
- UAV 관측범위와 모의범위의 일치도는 Precision, Recall, F1, IoU로, 종방향 도달특성은 축방향 도달범위로 평가했다.

## 결과(초록 기준)

- 10³ → 10⁴회로 늘려도 IoU·F1 변화는 매우 작았지만 계산시간은 약 8.5배 늘었다.
- 시험 범위 중 이동성 매개변수 9°, NIF 0.125에서 일치도가 가장 높았다. 이때 관측면적 0.0931 km², 모의면적 0.1321 km², Precision 0.440, Recall 0.624, F1 0.516, IoU 0.348.
- 모의면적이 관측면적보다 약 41.9% 커 과대모의 경향이 있었다.

UAV는 여기서 모델 검증용 '관측 정답(ground truth)'을 제공하는 역할이다. 유사한 UAV 지형 변화 관측 연구는 [[kci-uav-rainfall-induced-terrain-change-analysis]], UAV-LiDAR 정확도 요인은 [[kci-uav-lidar-ground-point-density-dem-accuracy]], 재난 대응 관점은 [[kci-disaster-response-drone-tech-direction]] 참조.
