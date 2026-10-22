---
title: "\uad6d\ubc29 AI \uc2e0\ub8b0\uc131\u318d\ubcf4\uc548\uc131 \ud5a5\uc0c1\uc744 \uc704\ud55c \ub7ec-\uc6b0 \uc804\uc7c1 \uc790\ud3ed \ub4dc\ub860 \ucd2c\uc601 \uc774\ubbf8\uc9c0 \uae30\ubc18 YOLO \uc138\uadf8\uba58\ud14c\uc774\uc158 \ubaa8\ub378\uc758 \uc2dc\uc57c \ubc29\ud574 \uac15\uac74\uc131 \ud3c9\uac00"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: journalArticle
authors: "\uc624\uc900\ud658(\uc721\uad703\uc0ac\uad00\ud559\uad50), "
year: "2026"
doi: ""
url: "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003394304"
zotero_key: 87KCZXJB
tags: ["auto:2nd-brain"]
sha256: bcf20244ddfd6057
---

# 국방 AI 신뢰성ㆍ보안성 향상을 위한 러-우 전쟁 자폭 드론 촬영 이미지 기반 YOLO 세그멘테이션 모델의 시야 방해 강건성 평가

**Authors**: 오준환(육군3사관학교),   
**Year**: 2026  
**URL**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003394304

## Abstract

러–우 전쟁은 자폭 드론이 전차 등 고가치 표적을 탐지ㆍ타격하는 수단으로 활용될 수 있음을 보여주었다. 드론 촬영 이미지 기반 표적 인식 AI는 국방 보안, 감시정찰, 표적 식별, 유무인복합전투체계 운용과 직결되지만, 실제 전장 영상은 센서잡음, 강우 등 시야 방해 요인으로 인해 오탐ㆍ미탐과 시각 정보 품질 저하가 발생할 수 있다. 본 연구는 Kaggle에서 제공하는 DroneVision: Tank Detection from Aerial Videos(https://www.kaggle.com/competitions/image-innovators) 데이터셋을 활용하여 러- 우 전쟁 자폭 드론 촬영 이미지 기반 YOLO 인스턴스 세그멘테이션 모델의 강건성을 평가하였다. 전차 이미지1,296장 중 1,102장을 학습용, 194장을 검증용으로 분할하고, Original, Salt & Pepper Noise, Heavy Rain, Mixed 조건에서YOLOv12s-seg와 YOLO26s-seg의 Box mAP50-95와 Mask mAP50-95를 비교하였다. 실험 결과 Original 조건에서는YOLOv12s-seg가 0.9477과 0.9028로 우수했으나, Mixed 조건의 Mask 성능은 YOLO26s-seg가 0.7932로 YOLOv12s-seg의0.7866보다 근소하게 높았다. 이는 국방 AI 신뢰성ㆍ보안성 검증 분야에서 원본 성능뿐 아니라 시야 방해 강건성, 입력 품질저하에 따른 성능 변화, Box / Mask 성능 차이를 함께 평가해야 함을 시사한다.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
