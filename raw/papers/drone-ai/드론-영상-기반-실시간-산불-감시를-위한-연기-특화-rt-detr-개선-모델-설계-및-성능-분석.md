---
title: "\ub4dc\ub860 \uc601\uc0c1 \uae30\ubc18 \uc2e4\uc2dc\uac04 \uc0b0\ubd88 \uac10\uc2dc\ub97c \uc704\ud55c \uc5f0\uae30 \ud2b9\ud654 RT-DETR \uac1c\uc120 \ubaa8\ub378 \uc124\uacc4 \ubc0f \uc131\ub2a5 \ubd84\uc11d"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: journalArticle
authors: "\uc870\uc601\ubcf5(\uad6d\ub9bd\uacbd\uad6d\ub300\ud559\uad50), "
year: "2026"
doi: ""
url: "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003370768"
zotero_key: EGV5XKTT
tags: ["auto:2nd-brain", "open-access"]
sha256: b7579a8ba0359b0a
---

# 드론 영상 기반 실시간 산불 감시를 위한 연기 특화 RT-DETR 개선 모델 설계 및 성능 분석

**Authors**: 조영복(국립경국대학교),   
**Year**: 2026  
**URL**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003370768

## Abstract

드론 영상을 활용한 산불 연기의 조기 감지는 광범위한 산림 지역을 실시간으로 감시하는 데 필수적이나, 드론 특유의 고도 변화, 시점 다양성, 소형 연기 객체 등의 문제로 일반 객체 검출기 적용에 한계가있다. 본 논문에서는 드론 영상 기반 실시간 산불 감시를 위해 RT-DETR을 기반으로 연기 특화 백본을개선한 모델을 제안하고 그 성능을 면밀히 분석한다. 제안 모델은 채널 중요도 기반 선택적 합성곱모듈(SCPConv)과 효율적 다중 스케일 어텐션(EMA)을 결합한 SCPConvBlock을 백본으로 구성하고, 전경집중 다중 스케일 피라미드 네트워크(MSFFPN)를 적용하여 드론 영상에서 빈번히 발생하는 소형·희박연기의 배경 혼동 문제를 해소하였다. 드론 촬영 산불 연기 데이터셋에서의 비교 및 절제 실험 결과, 제안 모델은 RT-DETR 대비 정밀도(Precision) 0.883(+0.7%p), 재현율(Recall) 0.800(+2.4%p), mAP50 0.862(+3.8%p), mAP95 0.539(+2.2%p)의 향상된 성능을 달성하였으며, 학습 수렴 에포크를 기존 125 에포크에서 25 에포크로 약 80% 단축하였다. 본 결과는 고정된 하이퍼파라미터와 난수 시드 하에서 수행된단일 실행 결과이며, 반복 실행에 따른 통계적 변동성은 평가하지 않았음을 한계점으로 명시한다.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
