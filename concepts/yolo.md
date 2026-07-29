---
title: YOLO
created: 2026-07-29
updated: 2026-07-29
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

## 최신 릴리스: Ultralytics v8.4.110 (2026-07-29)

### 주요 변경사항

- **RKNN 내보기 확장**: Rockchip NPU 하드웨어에서 모든 YOLO 태스크 지원
  - 객체 검출, 인스턴스 분할, 분류, 포즈 추정
  - 방향 경계 상자(OBB), 시맨틱 분할, 깊이 추정
- **텐서 기반 플로팅 개선**: GPU 메모리 상에서 마스크 합성 수행, CPU 전송 최소화

## 드론 응용

- **임무 중 객체 검출**: [[computer-vision-drone]]에서 실시간 타겟 인식
- **장애물 회피**: [[drone-ai-agents]]의 자율 비행 시스템
- **페이로드 통합**: [[drone-payload-systems]]의 카메라와 연동

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
- [[opencv]] — YOLO 모델 배포에 사용되는 컴퓨터 비전 라이브러리
- [[drone-ai-agents]] — AI 기반 자율 드론 시스템
