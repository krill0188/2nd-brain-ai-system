---
id: idea-002
title: "UAV 식생 이상탐지 3계열(RGB+텍스처 / NDVI / 초분광) 통합 벤치마크 교차 비교"
status: draft
created: 2026-09-30
updated: 2026-09-30
gaps: [GAP-006]
sources: [raw/papers/drone-ai/comparison-of-uav-image-based-detection-accuracy-of-pine-wilt-disease-affected-t.md, raw/papers/_unclassified/드론-다중분광센서-기반-ndvi를-활용한-한라산-구상나무-개체의-고도사면향별-활력도-예비평가.md, raw/papers/_unclassified/무인기-기반-초분광-영상을-이용한-보리-습해-조기-탐지.md]
novelty_confidence: 0.5
---

> ⚠ 미검증 연구 아이디어 — canonical 아님

## Hypothesis

동일 대상(예: 병해·활력도 저하가 진행 중인 침엽수 또는 작물 군락)에 대해 (1) RGB+GLCM 텍스처
채널(소나무재선충병 탐지 방식), (2) NDVI 단일 지수(구상나무 활력도 평가 방식), (3) 축소된 대표
파장 기반 소수 식생지수(보리 습해 탐지 방식)를 동일 비행·동일 센서 조건에서 나란히 적용하면,
탐지/분류 정확도는 초분광 기반 방법이 가장 높지만 "정확도 대비 데이터 취득·처리 비용"은 RGB+텍스처
방법이 가장 우수할 것이다 — 즉 최고 정확도 방법과 최고 비용효율 방법이 일치하지 않을 것이다.

## Why now (근거 요약)

세 연구는 서로 다른 식생 이상(병해·활력도·습해)과 서로 다른 센서 모달리티(RGB, 다중분광 NDVI,
초분광)를 각각 독립적으로 다뤘고, 이미 위키 내에서 상호 링크되어 있다 —
[[pine-wilt-disease-uav-detection]]은 RGB+텍스처 채널 구성별 YOLO26-Large 탐지 정확도를 비교했고
^[raw/papers/drone-ai/comparison-of-uav-image-based-detection-accuracy-of-pine-wilt-disease-affected-t.md],
[[kci-hallasan-fir-ndvi-vitality-assessment]]는 NDVI<0.5 임계값으로 한라산 구상나무 활력도를
예비평가했으며 ^[raw/papers/_unclassified/드론-다중분광센서-기반-ndvi를-활용한-한라산-구상나무-개체의-고도사면향별-활력도-예비평가.md],
[[kci-barley-wet-stress-hyperspectral-detection]]은 초분광 밴드를 축소한 식생지수로 보리 습해를
조기 탐지했다 ^[raw/papers/_unclassified/무인기-기반-초분광-영상을-이용한-보리-습해-조기-탐지.md]. 그러나
세 방법이 같은 데이터셋 또는 같은 대상에 적용되어 정확도·비용을 직접 비교한 사례는 없다(GAP-006).

## Novelty Ledger

### Known Similar Work
- [[pine-wilt-disease-uav-detection]] — RGB 3채널 vs RGB+텍스처(6채널) vs RGB+텍스처+지형(8채널)
  구성별 YOLO26-Large 탐지 정확도 비교(소나무재선충병).
- [[kci-hallasan-fir-ndvi-vitality-assessment]] — MicaSense RedEdge-P 다중분광 NDVI로 구상나무
  개체 활력도를 고도·사면향별로 평가(예비 단일 조사).
- [[kci-barley-wet-stress-hyperspectral-detection]] — UAV 초분광 영상에서 5개→1개 식생지수로
  단계적 축소하며 KNN 분류 성능을 비교(보리 습해).
- [[computer-vision-drone]] — 세 연구가 공통으로 걸치는 상위 개념(드론 컴퓨터 비전 응용, 농업/임업
  섹션에 NDVI+Segmentation 언급).

### What already exists
- 각 방법론 내부(채널 구성 간, 식생지수 개수 간) 비교는 있음.
- 세 방법 모두 "식생 이상 신호를 드론 영상에서 정량화한다"는 공통 목표를 가짐이 위키에서 확인됨.

### What appears missing
- 세 방법을 동일 대상·동일 비행 조건에서 직접 비교한 교차 벤치마크.
- 센서 비용(RGB 카메라 vs 다중분광 센서 vs 초분광 센서)과 처리 비용(GLCM 텍스처 연산 vs NDVI
  단순 연산 vs 초분광 차원축소) 대비 정확도의 트레이드오프 정량화.

### Potential novelty
- "정확도 최고" 방법과 "비용효율 최고" 방법이 다를 수 있다는 가설 자체가, 현장 적용(임업/농업
  드론 서비스) 의사결정에 직접 기여할 수 있는 실용적 기여점. 세 원 연구 중 어느 것도 비용축을
  명시적으로 다루지 않았음(서베이/개별 연구는 정확도 중심).

### Threat to novelty
- 세 원 연구가 서로 다른 작물/수종(소나무, 구상나무, 보리)을 대상으로 해 "동일 대상" 조건을
  충족하는 통합 데이터셋 구축 자체가 실현 가능성의 병목 — 만약 통합 데이터셋 구축이 불가능하다고
  판명되면 아이디어를 "동일 대상"에서 "동일 카테고리(침엽수 병해/활력도)"로 축소해야 함.
- GLCM 텍스처, NDVI, 초분광 식생지수 통합 비교 문헌이 국내외에 이미 존재할 가능성 — 위키 밖 문헌은
  미확인이므로 novelty_confidence를 중간으로 제한.

### Novelty confidence
0.5 — 위키 내 3연구의 상호 미비교는 확실하나, 통합 데이터셋 실현 가능성 미검증 및 위키 밖 선행
문헌 존재 가능성으로 중간 수준.

## Evidence Status

2026-09 근거 3편([[pine-wilt-disease-uav-detection]], [[kci-hallasan-fir-ndvi-vitality-assessment]],
[[kci-barley-wet-stress-hyperspectral-detection]]) → 신규 생성. 재평가 대상 없음(첫 등재).

## Minimal validation plan

1. 실현 가능성 우선 검증: 침엽수 병해(소나무재선충병) 발생지 인근에서 RGB, 다중분광(NDVI),
   초분광 3종 센서를 동일 조사구·동일 비행일에 동시 취득 가능한지 확인(가능하면 "동일 대상"
   유지, 불가하면 인접 조사구로 축소).
2. 3종 센서 데이터에 각 원 연구의 방법(RGB+GLCM+YOLO26 / NDVI 임계값 / 초분광 식생지수+KNN)을
   동일 라벨(의심목/정상목)에 대해 각각 적용.
3. 정확도(F1)와 처리 비용(센서 단가 + 전처리 시간)을 축으로 산점도를 그려 파레토 프론티어 분석.
4. 파레토 최적 방법이 대상(수종/작물)에 따라 달라지는지 확인.
