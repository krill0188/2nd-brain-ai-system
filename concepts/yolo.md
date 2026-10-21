---
title: YOLO
created: 2026-07-29
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, ai-agent]
sources: [inbox/fetch-2026-07-29-yolo.md, inbox/fetch-2026-09-01-yolo.md, inbox/fetch-2026-09-15-yolo.md, inbox/fetch-2026-09-16-yolo.md, inbox/fetch-2026-09-17-yolo.md, inbox/fetch-2026-09-18-yolo.md, inbox/processed/fetch-2026-10-02-yolo.md, inbox/processed/fetch-2026-10-17-kci-국방-ai-신뢰성ㆍ보안성-향상을-위한-러-우-전쟁-자폭-드론-촬영-이미지-기반-yolo-세그멘테이션-모델의-.md, inbox/processed/fetch-2026-10-17-yolo.md, inbox/processed/fetch-2026-10-18-yolo.md, inbox/processed/fetch-2026-10-21-yolo.md]
confidence: high
contested: false
contradictions: []
---

# YOLO (You Only Look Once)

YOLO는 실시간 객체 검출을 위한 딥러닝 아키텍처이다. 단일 신경망으로 이미지를 한 번만 보고 객체의 위치와 클래스를 동시에 예측하여 빠른 처리 속도를 제공한다.

## 핵심 특징

- **실시간 성능**: 고성능 GPU에서 30~140 FPS 이상 처리
- **단일 단계 검출**: 영역 제안과 분류를 동시에 수행
- **높은 정확도**: COCO 데이터셋에서 우수한 mAP 성능

## 릴리스 이력

버전별 상세 변경사항은 개별 페이지 참고(최신순): [[yolo-v8-4-155]] · [[yolo-v8-4-154]] · [[yolo-v8-4-153]] · [[yolo-v8-4-152]] · [[yolo-v8-4-150]] · [[yolo-v8-4-148]] · [[yolo-v8-4-146]] · [[yolo-v8-4-144]] · [[yolo-v8-4-143]] · [[yolo-v8-4-142]] · [[yolo-v8-4-141]] · [[yolo-v8-4-139]] · [[yolo-v8-4-138]] · [[yolo-v8-4-137]] · [[yolo-v8-4-117]] · [[yolo-v8-4-116]] · [[yolo-v8-4-115]] · [[yolo-v8-4-112]]

### v8.4.171 (2026-10-01)

- **AMD ROCm/MIGraphX 엔드투엔드 지원 추가**: AMD GPU에서 네이티브 PyTorch 학습·실행 및
  MIGraphX 실행 공급자로 export된 ONNX 모델 구동 가능. NVIDIA/CUDA 일변도이던 드론 컴패니언
  컴퓨터의 추론 하드웨어 선택지를 넓힌다. 상세는 [[yolo-v8-4-171]] 참고.^[inbox/processed/fetch-2026-10-02-yolo.md]

### v8.4.137 (2026-08-31)

- **channels-last 자동 활성화**: PyTorch 1.11+ CUDA 훈련 시 NHWC 메모리 레이아웃 자동 적용 ^[inbox/fetch-2026-09-01-yolo.md]
- **성능 개선**: Tensor Core 하드웨어에서 컨볼루션 성능 향상
- **호환성**: PyTorch 1.10 이하, CPU, MPS 훈련은 NCHW 유지

## 드론 응용

- **임무 중 객체 검출**: [[computer-vision-drone]]에서 실시간 타겟 인식
- **장애물 회피**: [[drone-ai-agents]]의 자율 비행 시스템
- **페이로드 통합**: [[drone-payload-systems]]의 카메라와 연동

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
- [[opencv]] — YOLO 모델 배포에 사용되는 컴퓨터 비전 라이브러리
- [[drone-ai-agents]] — AI 기반 자율 드론 시스템

## 최신 근거 연결 (2026-10-17)

- 직전 릴리스 [[yolo-v8-4-178]](2026-10-16)는 Platform 링크·트래킹·내보내기 호환성 수정 중심이며 신규 아키텍처는 없다.^[inbox/processed/fetch-2026-10-17-yolo.md]
- 시야 방해(노이즈·폭우) 강건성 평가에서 모델 순위가 조건별로 바뀔 수 있다는 근거: [[kci-yolo-seg-visibility-robustness-suicide-drone]]^[inbox/processed/fetch-2026-10-17-kci-국방-ai-신뢰성ㆍ보안성-향상을-위한-러-우-전쟁-자폭-드론-촬영-이미지-기반-yolo-세그멘테이션-모델의-.md]

## 최신 근거 연결 (2026-10-18)

- 최신 릴리스는 [[yolo-v8-4-181]](2026-10-17)로, 데이터셋 로딩·자동 주석·회전 박스 트래킹·세그멘테이션 메모리·JetPack 7.2 감지 중심의 수정이며 아키텍처 변경은 없다.^[inbox/processed/fetch-2026-10-18-yolo.md]

## 최신 근거 연결 (2026-10-21)

- 최신 릴리스는 [[yolo-v8-4-183]](2026-10-20)다. 직전 [[yolo-v8-4-182]](2026-10-18)는 라벨 검증 강화 중심이었고, 이번 릴리스는 Axelera Metis(Voyager SDK 1.9.0)·Intel LiteRT 배포 확대와 학습·예측 안정성 수정이 핵심이며 모델 아키텍처 변경은 릴리스 노트에 없다.^[inbox/processed/fetch-2026-10-21-yolo.md]
- 분류기 라벨 정렬 수정으로 ImageNette 검증 정확도가 9.45% → 70.37%로 보고됐다. 릴리스 노트의 자체 수치이며 드론 데이터셋 결과는 아니다.^[inbox/processed/fetch-2026-10-21-yolo.md]
