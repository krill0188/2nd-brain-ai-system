---
title: "AirSim Image APIs"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
tags: [drone, synthetic-data, airsim, simulator]
sources: [inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]
confidence: medium
contested: false
contradictions: []
---

# AirSim Image APIs

- 원문: https://microsoft.github.io/AirSim/image_apis/^[inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]
- 저자: Microsoft AirSim team^[inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]

## 핵심 내용
AirSim 이미지 API는 ImageType 10종(Scene, DepthPlanar, DepthPerspective, DepthVis, DisparityNormalized, Segmentation, SurfaceNormals, Infrared, OpticalFlow, OpticalFlowVis)을 제공한다. simGetImage는 단일 PNG 바이트, simGetImages는 ImageRequest 목록으로 여러 카메라·유형을 한 번에 받으며 PNG, 비압축 RGB, float 배열을 반환한다. 세그멘테이션은 시작 시 메시별 ID(0-255)와 팔레트 색을 할당하며 simSetSegmentationObjectID로 변경하고 -1이면 숨긴다. 깊이는 float로 받는 것이 일반적이다.^[inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]
원문 인용: "pure white means depth of 100m or more while pure black means depth of 0 meters" (DepthVis)^[inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]

## 설계·운용에 쓸 수 있는 지침
- 정확한 세그멘테이션 RGB가 필요하면 비압축 이미지를 요청한다.^[inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]
- 합성 데이터의 라벨(깊이, 세그, 광학 흐름)을 한 호출로 동기 수집 가능.^[inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]

## 한계·미확인
- ImageRequest 플래그 완전 정의는 페이지에 없음. AirSim 유지보수 상태는 미확인.^[inbox/processed/hw-20261021-data-synthetic-airsim-image-apis.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[drone-simulation]]
