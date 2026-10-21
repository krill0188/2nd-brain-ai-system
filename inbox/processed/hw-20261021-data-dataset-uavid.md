---
title: "UAVid: A Semantic Segmentation Dataset for UAV Imagery"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: ai-autonomy
source: arXiv:1810.10438
authors: "Ye Lyu, George Vosselman, Guisong Xia, Alper Yilmaz, Michael Ying Yang"
published: "2018-10-24 (v2 2020-05-18; ISPRS J. Photogramm. Remote Sens. 게재)"
tags: [drone, dataset, uavid, segmentation]
---
## 핵심 내용
도시 장면을 경사(oblique) 시점으로 찍은 고해상도 UAV 시맨틱 분할 데이터셋. 4K 경사 영상 30개 시퀀스에서 300장을 8개 클래스로 조밀 라벨링했다. 큰 스케일 변화, 이동 객체 인식, 시간적 일관성이 과제이며 여러 딥러닝 기준선과 Multi-Scale-Dilation 네트워크가 최고 성능이라고 보고한다.
원문 인용: "In total, 300 images have been densely labeled with 8 classes for the semantic labeling task." (Abstract)

## 설계·운용에 쓸 수 있는 지침
- 정사영(nadir) 위주 데이터와 달리 측면이 보이는 경사 촬영 분할 학습·평가에 사용.

## 한계·미확인
- arXiv 초록만 열람. 클래스 이름, 해상도 세부, 정확도 수치는 미확인.
