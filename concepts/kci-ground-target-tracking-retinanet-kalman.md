---
title: "감시 드론을 위한 심층 신경망 기반 지상 표적 추적 기법 (KCI)"
created: 2026-10-01
updated: 2026-10-01
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-01-kci-감시-드론을-위한-심층-신경망-기반-지상-표적-추적-기법.md]
confidence: medium
contested: false
contradictions: []
---

# 감시 드론을 위한 심층 신경망 기반 지상 표적 추적 기법

청주대학교 김상현(항공우주시스템공학회지, 2026)의 연구. 공중에서 지상을 감시하는 드론이 다수의
이동 표적을 탐지·추적하는 기법을 다룬다. 객체 탐지용 심층 신경망 RetinaNet으로 지상 표적을
탐지하고, 탐지 정보를 바탕으로 칼만 필터(Kalman Filter)를 이용해 다수 표적을 추적하는 방식을
구현했다.^[inbox/processed/fetch-2026-10-01-kci-감시-드론을-위한-심층-신경망-기반-지상-표적-추적-기법.md]

## 방법

- **탐지**: RetinaNet 기반 지상 표적 객체 탐지.
- **추적**: 탐지 결과에 칼만 필터를 결합해 다수 표적을 동시 추적.
- **데이터셋/검증**: 데이터셋 수집 및 성능 실험을 위해 3차원 가상 환경을 별도 구현.

## 결과

- 심층 신경망만 단독 사용한 경우보다 칼만 필터를 함께 사용한 경우 표적 인식 정확도가 향상됨을
  실험으로 확인.

## Related

- [[computer-vision-drone]] — 드론 컴퓨터 비전: YOLO, SLAM, 객체 추적 전반
- [[pt-detr-small-target-detection]] — RT-DETR 기반 UAV 소형 객체 탐지
- [[drone-anomaly-detection-survey]] — 드론 이상 징후/표적 탐지 방법 연구 동향
