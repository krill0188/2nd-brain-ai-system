---
title: "OpenFly: A comprehensive platform for aerial vision-language navigation"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, vln, benchmark, aerial-navigation, 3d-gaussian-splatting]
sources: [inbox/processed/hw-20261021-ai-vlm-nav-openfly-gao-2025.md]
confidence: medium
contested: false
contradictions: []
---

# OpenFly: A comprehensive platform for aerial vision-language navigation

- 원문: https://arxiv.org/abs/2502.18041^[inbox/processed/hw-20261021-ai-vlm-nav-openfly-gao-2025.md]
- 저자: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, et al. (23명), Bin Zhao^[inbox/processed/hw-20261021-ai-vlm-nav-openfly-gao-2025.md]
- 발행: 2025-02-25 (v1), v7 2026-03-01, ICLR 2026 채택^[inbox/processed/hw-20261021-ai-vlm-nav-openfly-gao-2025.md]

## 핵심 내용
실외 항공 VLN은 시야가 넓어 데이터 수집이 어렵고 벤치마크가 적다. OpenFly는 (1) Unreal Engine, GTA V, Google Earth, 3D Gaussian Splatting을 통합한 시뮬레이션, (2) 포인트클라우드 획득, 장면 의미분할, 비행 궤적 생성, 지시문 생성을 자동화한 툴체인, (3) 18개 장면, 비행 고도와 길이가 다양한 100k 궤적 벤치마크로 구성된다. 키프레임 인식형 VLN 모델 OpenFly-Agent를 제안하고 최근 VLN 방법들과 비교한다. 툴체인, 데이터셋, 코드를 오픈소스로 공개 예정.^[inbox/processed/hw-20261021-ai-vlm-nav-openfly-gao-2025.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- 항공 VLN 학습/평가용 대규모 데이터: 100k 궤적, 18 장면.^[inbox/processed/hw-20261021-ai-vlm-nav-openfly-gao-2025.md]

## 한계·미확인
- 초록만 확인. 성공률 등 성능 수치와 실기 평가 여부는 미확인. 논문 제목이 버전별로 다름(v1 "A Versatile Toolchain and Large-scale Benchmark ...").^[inbox/processed/hw-20261021-ai-vlm-nav-openfly-gao-2025.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
