---
title: "UAV 다중분광 캐노피 분석 기반 제초제 선발·들잔디 F1 우선선발"
created: 2026-11-05
updated: 2026-11-05
type: concept
domain: ops-mission
tags: [drone, drone-ai, drone-hw]
sources:
  - inbox/fetch-2026-11-05-kci-겨울철-uav-다중분광-캐노피-표현형-분석을-이용한-제초제-선발-종간교잡-들잔디-f1-개체의-순차적-우선선발.md
confidence: low
contested: false
contradictions: []
---

# UAV 다중분광 캐노피 분석 기반 제초제 선발·들잔디 F1 우선선발

아열대농업생명과학지(2026) 게재 논문 초록 기준 요약이다. 원문은 비공개(페이월)다.^[inbox/fetch-2026-11-05-kci-겨울철-uav-다중분광-캐노피-표현형-분석을-이용한-제초제-선발-종간교잡-들잔디-f1-개체의-순차적-우선선발.md]

## 배경
종간교잡은 잔디 육종에서 양친 종의 서로 다른 형질을 결합하기 위한 방법이나, 특정 형질 선발이 다른 형질의 우수성을 반드시 의미하지는 않는다. 선행연구에서 제초제(glufosinate-ammonium) 처리 후 생존 개체를 선발했으나, 겨울철 캐노피 표현형은 평가되지 않았다.

## 방법
- **플랫폼**: UAV 기반 다중분광 영상 촬영
- **대상**: 종간교잡 Zoysia F1 집단(35개체) 및 양친(P1, P2)
- **지수**: NDVI, NDRE, CIgreen
- **관측**: 제초제 처리 전 1회 + 겨울철 12회 반복 관측

## 결과
### 제초제 처리 전(35개체)
- NDVI 범위: −0.017 ~ 0.225 (연속적 변이)

### 제초제 선발 후 유지된 12개체(H1~H12) + 양친
- **P1**: 겨울철 관측기간 동안 상대적으로 높은 NDVI 유지
- **P2**: 뚜렷한 NDVI 감소
- **H1~H12**: 개체 간 전체적 NDVI·CIgreen 수준 차이 있으나 개체별 시간적 반응은 유의하지 않음
- **NDRE**: 유의한 Plant × Time 상호작용 → 개별 F1 개체 간 선형적 시간적 반응 차이 확인

### 다중지수 합의점수(NDVI, NDRE, CIgreen 정규화 순위 통합)
- 상위 3개체: **H12, H9, H6** (H1~H12 중 가장 높은 점수)

## 의의
제초제 선발 후 유지된 F1 개체들에서도 겨울철 캐노피 표현형의 변이가 존재하며, 다중분광 지수 통합 평가를 통해 우수 개체를 선별 가능함을 보임. UAV 다중분광 영상이 육종 선발 파이프라인에 활용될 수 있음을 실증.

## 관련
농업용 드론 멀티스펙트럴은 [[uav-multispectral-glint-correction]], [[kci-barley-wet-stress-hyperspectral-detection]], 정밀착륙·비전 기반 내비게이션은 [[rtk-gps-precise-landing]], [[visual-positioning-odometry]] 참조.