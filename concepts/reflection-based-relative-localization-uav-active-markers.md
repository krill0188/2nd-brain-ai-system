---
title: "반사 기반 UAV 팀 상대 위치추정 (능동 마커, CTU Prague)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, swarm]
sources: [inbox/processed/fetch-2026-10-22-yt-reflection-based-relative-localization-for-cooperative-uav-t.md]
confidence: low
contested: false
contradictions: []
---

# 반사 기반 UAV 팀 상대 위치추정 (능동 마커, CTU Prague)

프라하 공대 FEE-CTU 다중로봇 시스템 그룹의 영상(2026-10-21)이 소개한 방법이다. 능동 마커의 반사를 모호성의 원인으로 제거하는 대신, 상대 위치추정의 단서로 쓴다. 근거는 영상 자막이며 자막에 없는 내용은 적지 않았다.^[inbox/processed/fetch-2026-10-22-yt-reflection-based-relative-localization-for-cooperative-uav-t.md]

## 방법
- 입력은 카메라(대상 UAV 방향 벡터)와 지면까지의 높이다. 설명란은 단일 빔 거리계를 쓰고 로봇 크기·마커 정보가 필요 없다고 한다.
- 센서 불확실성을 반영해 방향 벡터 둘레에 타원형 원뿔을 만든다.
- 영상에서 길쭉하게 보이는 반사에 타원을 씌우고, UAV와 반사면 사이의 알려진 거리로 그 위치를 계산해 반사 패턴의 타원 원뿔을 만든다.
- 두 원뿔 안에서 무작위 점을 샘플링해 교집합에 드는 점만 남긴다.
- 등속 운동 모델의 파티클 필터로 강건성을 높인다. 가중치는 교집합 점과의 정합도로 주고 Koshi 커널(자막 표기; Cauchy 커널로 추정)을 써 이상치에 관대하다. 리샘플링 후 대상의 3D 위치를 추정한다.
- 반사면의 성질·텍스처에 의존하지 않는다. 대상 환경은 잔잔한 수면·평평한 실내 바닥 같은 경면 근평면이다.

## 실험 결과
- 대상은 자외선(UV) LED를, 관측 UAV는 UV 대역통과 필터 카메라를 사용했다.
- 실내외, 여러 표면·조명에서 대상 UAV의 3D 위치를 안정적으로 추적했고, UAV 3대 동시 비행(multi-UV) 실험도 했다.
- Raspberry Pi 5를 탑재한 마이크로 기체를 포함해 모든 플랫폼에서 온보드 실시간으로 동작했다.
- 기존 최신 기법 UVR(자막 표기) 대비 야외 전 실험에서 우수했고, 특히 30 m 이상에서 차이가 컸다. 기존 방식은 마커 간격이 알려져 있어야 하는데 거리가 멀면 간격이 몇 픽셀로 줄어 추정이 불안정해진다.

## 관련
다중 UAV 상대 위치추정의 위치는 [[uav-swarm-target-localization]], 군집 운용 개요는 [[swarm-coordination]], UWB 기반 군집 위치추정은 [[kci-uwb-degraded-uav-swarm-positioning]] 참조.
