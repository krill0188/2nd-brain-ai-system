---
title: "\ub3c4\uc2ec \uc720\uc218\uc9c0\uc5d0\uc11c \ucde8\ub4dd\ud55c \ub2e8\uc77c UAV \ucd08\ubd84\uad11\uc601\uc0c1\uc744 \uc774\uc6a9\ud55c \ud76c\uc18c \uc4f0\ub808\uae30 \ud6c4\ubcf4\uc601\uc5ed \uc120\ubcc4\uc744 \uc704\ud55c \ubc30\uacbd\uc720\ud615 \ubcf4\uc870 U-Net++\uc758 \uc801\uc6a9\uc131 \ud3c9\uac00"
created: 2026-09-06
updated: 2026-09-06
type: paper
item_type: journalArticle
authors: "\ucd5c\ubcd1\uae38(\uc778\ucc9c\ub300\ud559\uad50), "
year: "2026"
doi: ""
url: "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003377693"
zotero_key: BTG5JCM6
tags: ["auto:2nd-brain"]
sha256: fdb115ebcbb0c775
---

# 도심 유수지에서 취득한 단일 UAV 초분광영상을 이용한 희소 쓰레기 후보영역 선별을 위한 배경유형 보조 U-Net++의 적용성 평가

**Authors**: 최병길(인천대학교),   
**Year**: 2026  
**URL**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003377693

## Abstract

본 연구는 단일 도심 유수지에서 취득한 150개 밴드 UAV(Unmanned Aerial Vehicle) VNIR 초분광영상을 이용하여 희소 쓰레기 후보영역을 선별하고, 수면, 식생, 도로, 건물 및 차량을 보조과제로 학습하는 배경유형 보조 U-Net++의 적용성을 평가하였다. 6개 쓰레기 재질을 하나의 표적 클래스로 통합하고 동일한 객체 단위 공간분할과 검증전용 후보 설정 절차를 두 모델에 적용하였다. 모델별 검증 최적 운영점에서 배경유형 보조 모델은 시험객체 14개 중 8개를 탐지하여 객체 탐지율 57.14%, 후보 정밀도 53.33%, 후보 F1 55.17%를 나타냈고, 기준모델은 6개를 탐지하여 후보 F1 44.44%를 기록하였다. 공통 최소 후보면적 12 px와 검증 오탐 후보 밀도 FCPM (False Candidates per Million Valid Pixels)를 3 이하로 적용한 고정 체크포인트 기반 통제분석에서도 배경유형 보조 모델은 8개, 기준모델은 6개를 탐지하였다. 이 조건에서 후보 F1은 각각 55.17%와 48.00%였고, 객체 탐지율 차이는 14.29%p였다. 다만 배경유형 보조학습의 이점은 모든 후보부담과 최소면적 조건에서 일관되지 않았으며, 시험객체 수도 14개로 제한적이었다. 따라서 본 결과는 배경유형 보조학습의 일반적 우수성이 아니라 특정 운영조건에서 확인된 제한적 적용 가능성으로 해석하였다. 향후에는 독립된 지역과 촬영일 자료를 이용한 외부검증과 다중 시드 반복학습이 필요하다. 아울러 보조손실 가중치, 완충거리, 후보부담 및 배경유형별 성능에 대한 민감도 분석이 요구된다

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
