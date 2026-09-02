---
title: "\ub4dc\ub860 \uc2dc\uacc4\uc5f4 RGB \uc601\uc0c1\uacfc \ub525\ub7ec\ub2dd \uae30\ubc18 \ubd84\ub958 \ubaa8\ub378\uc744 \uc774\uc6a9\ud55c \ubcbc \ud488\uc885\uad70\uc758 \ucd9c\uc218 \ud310\ubcc4"
created: 2026-09-02
updated: 2026-09-02
type: paper
item_type: journalArticle
authors: "\uc815\uc724\uc815(\uad6d\ub9bd\uc2dd\ub7c9\uacfc\ud559\uc6d0), "
year: "2026"
doi: ""
url: "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003375652"
zotero_key: 3XP3QZ7H
tags: ["auto:2nd-brain"]
sha256: 9d333a937020fb12
---

# 드론 시계열 RGB 영상과 딥러닝 기반 분류 모델을 이용한 벼 품종군의 출수 판별

**Authors**: 정윤정(국립식량과학원),   
**Year**: 2026  
**URL**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003375652

## Abstract

1. 벼의 출수 여부를 자동으로 판별하고 출수기를 추정하기위해 드론의 시계열 RGB 영상을 활용한 YOLOv11 기반 분류 모델을 구축하였다.
2. 벼 144품종을 대상으로 오전, 정오, 오후의 3개 시간대에 영상을 수집하였으며, 정사영상 정합 및 분할 과정을통해 총 79,331장의 데이터셋을 구축하였다.
3. 모델 학습 결과 정확도는 초기 0.941에서 최종 0.953으로 향상되었고, 손실값은 초기 0.281에서 최종 0.142로감소하여 안정적으로 수렴하는 경향을 보였다.
4. Confusion matrix 분석 결과 출수 전과 출수 후 단계를높은 정확도로 구분하였으며, 오분류는 주로 출수 초기단계에서 발생하였다. 이는 출수 초기에는 이삭의 노출정도가 낮고 영상에서 식별 가능한 형태적 특징이 제한적이기 때문으로 판단되었다.
5. 전체 144품종에서 예측 출수일과 실측 출수일 간의 평균 편향은 1.89일이었으며, MAE와 RMSE는 각각 2.14 일과 2.66일이었다. 전체 품종의 60.42%가 실측 출수일기준 ±2일 이내에 예측되었으며, 모델은 전반적으로 실측 출수일보다 늦게 예측하는 경향을 보였다.
6. Grad-CAM 분석 결과, 출수 이후 이삭 부위에 높은 가중치가 나타나 모델이 출수 판별에 유효한 시각적 특징을 반영하고 있음을 확인하였다. 또한 일부 잎과 배경영역에서도 가중치가 나타나, 모델이 이삭 자체뿐 아니라 군락 내 공간적 맥락을 함께 활용했을 가능성이 확인되었다.
7. 이상의 결과는 드론 영상과 YOLO 기반 분류 모델이 다수 품종의 출수 시기를 일관된 기준으로 평가하고 현장조사 부담을 줄이기

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
