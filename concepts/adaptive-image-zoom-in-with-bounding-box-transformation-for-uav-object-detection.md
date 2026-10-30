---
title: "Adaptive Image Zoom-In With Bounding Box Transformation For UAV Object Detection"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [object-detection, uav-imaging, bounding-box, zoom, adaptive, corner-aligned]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Adaptive Image Zoom-In With Bounding Box Transformation For UAV Object Detection

핵심 요약
: UAV 영상에서 작은 객체 탐지를 위해, 전경 객체가 일반 장면 이미지에 비해 작고 드물다는 문제를 해결하고 최적화를 돕기 위해 입력 영상에 적응형으로 영역을 확대(zooming)하는 프레임워크다. 비일률적 확대와 객체 탐지 훈련·추론을 연결하는 경량 오프셋 예측 방식과 바운드 박스 변환 방법을 도입했다.

## 개요
UAV가 촬영한 영상에서는 객체가 작고 sparse하여 객체 탐지 모델 최적화가 어렵다. 본 논문은 입력 이미지에 **비일률적(Non-uniform) zooming**을 적용해 객체 특징을 더 잘 캡처하도록 하는 Adaptive Image Zoom-in framework를 제안한다. 주요 설계 포인트는 다음과 같다.

1. **비일률적 확대 방식**: 이미지 전체를 uniform하게 확대하는 것이 아니라, 객체의 위치와 크기에 따라 유연하게 zooming을 조절하는 경량 offset prediction scheme을 도입했다.
2. **바운드 박스 기반 확대 objectives**: 오프셋 예측과 연계해, ground-truth bounding box를 zoomed space로 warping하여 탐지 모델을 훈련하고, inference 시 예측된 box를 original space로 warping해 복귀시키는 Corner-aligned bounding box transformation 방법을 제안한다.

## 핵심 파라미터
| 파라미터 / 개념 | 내용 |
|----------------|------|
| 비일률적 확대 | 객체 위치·크기에 따라 이미지를 유연하게 확대하는 방식 |
| 오프셋 예측 | zooming 변환을 학습하기 위한 경량 scheme |
| 코너 정렬 바운드 박스 변환 | ground-truth box를 zoomed space로, 예측 box를 original space로 warping |

## 활용처
- UAV 플랫폼에서의 소형 객체 탐지 (예: 건물 검사, 피해 상황 모니터링, 표적 식별)
- 고해상도 확대 없이도 탐지 정확도 향상이 필요한 GCS 기반 실시간 영상 처리 시스템

## 관련 페이지
- [[object-detection]] — UAV 환경에서의 객체 탐지 개념
- [[bounding-box]] — 객체 탐지에서 사용되는 바운드 박스 개념

## 출처
- (사용자 재확인 필요) Wang et al., "Adaptive Image Zoom-in with Bounding Box Transformation for UAV Object Detection," arXiv:2602.07512, 2026. DOI: 10.48550/arXiv.2602.07512.

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형

## 📰 최근 관련 소식
- GA-ASI Partnering With Spirit Defense For FQ-42 CCA Production (www.suasnews.com, Sun, 25 Oc) — https://www.suasnews.com/2026/10/ga-asi-partnering-with-spirit-defense-for-fq-42-cca-production/
