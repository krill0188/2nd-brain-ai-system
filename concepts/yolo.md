---
title: YOLO
created: 2026-07-29
updated: 2026-08-11
type: concept
tags: [drone, drone-ai, ai-agent]
sources: [inbox/fetch-2026-07-29-yolo.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# YOLO (You Only Look Once)

YOLO는 실시간 객체 검출을 위한 딥러닝 아키텍처이다. 단일 신경망으로 이미지를 한 번만 보고 객체의 위치와 클래스를 동시에 예측하여 빠른 처리 속도를 제공한다.

## 핵심 특징

- **실시간 성능**: 고성능 GPU에서 30~140 FPS 이상 처리
- **단일 단계 검출**: 영역 제안과 분류를 동시에 수행
- **높은 정확도**: COCO 데이터셋에서 우수한 mAP 성능

## 릴리스 이력

버전별 상세 변경사항은 개별 페이지 참고(최신순): [[yolo-v8-4-117]] · [[yolo-v8-4-116]] · [[yolo-v8-4-115]] · [[yolo-v8-4-112]]

## 드론 응용

- **임무 중 객체 검출**: [[computer-vision-drone]]에서 실시간 타겟 인식
- **장애물 회피**: [[drone-ai-agents]]의 자율 비행 시스템
- **페이로드 통합**: [[drone-payload-systems]]의 카메라와 연동

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
- [[opencv]] — YOLO 모델 배포에 사용되는 컴퓨터 비전 라이브러리
- [[drone-ai-agents]] — AI 기반 자율 드론 시스템
