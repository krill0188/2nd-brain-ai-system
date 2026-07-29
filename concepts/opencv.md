---
title: OpenCV
created: 2026-07-29
updated: 2026-07-29
type: concept
tags: [drone, drone-ai, ai-agent]
sources: [inbox/fetch-2026-07-29-opencv.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# OpenCV

OpenCV(Open Source Computer Vision Library)은 실시간 컴퓨터 비전을 위한 오픈소스 라이브러리이다. 드론 분야에서는 객체 인식, 추적, SLAM, 이미지 처리 등 다양한 AI 응용에 활용된다.

## 핵심 기능

- **이미지/비디오 처리**: 필터링, 변환, 형태학적 연산
- **객체 검출**: Haar Cascade, HOG, 딥러닝 기반 검출
- **특징점 추출**: SIFT, SURF, ORB 등
- **카메라 캘리브레이션**: 렌즈 왜곡 보정, 스테레오 비전

## 최신 릴리스: OpenCV 5.0.0 (2026-06-06)

2026년 6월 6일 출시된 OpenCV 5.0.0은 메이저 버전 업그레이드이다:

- 4.x에서 5.x로의 마이그레이션 가이드 제공
- Android SDK 16KB 페이지 크기 대응 패키지 제공

## 드론 응용

- **객체 추적**: [[computer-vision-drone]]과 연계하여 실시간 타겟 추적
- **비전 기반 내비게이션**: [[drone-ai-agents]]에서 SLAM 및 장애물 회피
- **페이로드 통합**: [[drone-payload-systems]]의 카메라 시스템과 연동

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
- [[yolo]] — OpenCV와 함께 사용되는 객체 검출 모델
- [[ros2-drone-integration]] — OpenCV가 통합되는 ROS2 환경
