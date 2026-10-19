---
title: "자폭 드론 촬영 이미지 기반 YOLO 세그멘테이션 시야 방해 강건성 평가"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, ops-mission]
sources: [inbox/processed/fetch-2026-10-17-kci-국방-ai-신뢰성ㆍ보안성-향상을-위한-러-우-전쟁-자폭-드론-촬영-이미지-기반-yolo-세그멘테이션-모델의-.md]
confidence: medium
contested: false
contradictions: []
---

# 러-우 전쟁 자폭 드론 영상 YOLO 세그멘테이션 강건성

**출처**: KCI 학술지 논문 (2026)

드론 촬영 표적 인식 AI는 센서 잡음·강우 같은 시야 방해로 오탐·미탐과 화질 저하가 생길 수 있다. Kaggle DroneVision(전차 항공영상) 데이터셋으로 YOLO 인스턴스 세그멘테이션의 강건성을 평가했다.^[inbox/processed/fetch-2026-10-17-kci-국방-ai-신뢰성ㆍ보안성-향상을-위한-러-우-전쟁-자폭-드론-촬영-이미지-기반-yolo-세그멘테이션-모델의-.md]

## 실험
- 전차 이미지 1,296장 중 학습 1,102장, 검증 194장. 조건은 Original, Salt & Pepper Noise, Heavy Rain, Mixed.^[inbox/processed/fetch-2026-10-17-kci-국방-ai-신뢰성ㆍ보안성-향상을-위한-러-우-전쟁-자폭-드론-촬영-이미지-기반-yolo-세그멘테이션-모델의-.md]
- YOLOv12s-seg와 YOLO26s-seg의 Box/Mask mAP50-95 비교.^[inbox/processed/fetch-2026-10-17-kci-국방-ai-신뢰성ㆍ보안성-향상을-위한-러-우-전쟁-자폭-드론-촬영-이미지-기반-yolo-세그멘테이션-모델의-.md]
- Original: YOLOv12s-seg가 Box 0.9477, Mask 0.9028로 우수. Mixed의 Mask는 YOLO26s-seg 0.7932가 YOLOv12s-seg 0.7866보다 근소하게 높았다.^[inbox/processed/fetch-2026-10-17-kci-국방-ai-신뢰성ㆍ보안성-향상을-위한-러-우-전쟁-자폭-드론-촬영-이미지-기반-yolo-세그멘테이션-모델의-.md]
- 시사점: 국방 AI 신뢰성 검증은 원본 성능뿐 아니라 시야 방해 강건성, 입력 품질 저하에 따른 성능 변화, Box/Mask 성능 차이를 함께 봐야 한다.^[inbox/processed/fetch-2026-10-17-kci-국방-ai-신뢰성ㆍ보안성-향상을-위한-러-우-전쟁-자폭-드론-촬영-이미지-기반-yolo-세그멘테이션-모델의-.md]

## 관련
[[yolo]], [[computer-vision-drone]], [[kci-tank-zone-vulnerability-selective-counter-drone-protection]] 참조.
