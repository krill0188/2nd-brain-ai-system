---
id: idea-005
title: "DAME-Net 복원 + 에지 제약 경량 탐지 직렬 파이프라인: 정확도 개선 대 엣지 예산 초과 트레이드오프"
status: draft
created: 2026-10-01
updated: 2026-10-01
gaps: [GAP-007]
sources: [inbox/fetch-2026-08-19-arxiv-compositional-degradation-uav-image-restoration-conditional-.md, inbox/processed/fetch-2026-08-19-arxiv-edge-constrained-uav-small-object-detection-with-p2-enhancem.md]
novelty_confidence: 0.4
---

> ⚠ 미검증 연구 아이디어 — canonical 아님

## Hypothesis

MDUR 벤치마크의 복합 열화(비·안개·노이즈 등) 조건에서 "DAME-Net 복원 → YOLOX-Nano+P2 탐지" 직렬
파이프라인은 "복원 없이 YOLOX-Nano+P2 직접 탐지"보다 AP_small을 유의하게 개선시키지만, DAME-Net
복원 단계 추가로 인한 종단 지연시간·총 FLOPs 증가가 에지 제약 탐지기(QIEA가 원래 최적화하려는
지연/메모리 예산)의 한도를 초과할 것이다 — 즉 복원-탐지 결합은 정확도는 높이지만 "에지 제약"이라는
원래 설계 목표와 정면으로 상충한다.

## Why now (근거 요약)

[[dame-net-uav-image-restoration]]은 MDUR 벤치마크(43가지 열화 구성)에서 복원 성능 개선과 "UAV
객체 탐지 다운스트림 작업에서 유효성 검증"을 주장하지만 구체적 파이프라인 구성이나 비용 데이터는
제시하지 않는다 ^[inbox/fetch-2026-08-19-arxiv-compositional-degradation-uav-image-restoration-conditional-.md].
[[edge-constrained-uav-small-object-detection]]은 VisDrone 데이터셋에서 P2 분기+QIEA로 AP_small을
크게 개선했지만 열화(비/안개/노이즈) 조건은 다루지 않는다
^[inbox/processed/fetch-2026-08-19-arxiv-edge-constrained-uav-small-object-detection-with-p2-enhancem.md].
두 페이지는 위키에서 "관련 개념"으로 상호 링크되어 있으나 직렬 결합 비교는 없다(GAP-007).

## Novelty Ledger

### Known Similar Work
- [[dame-net-uav-image-restoration]] — FDPM+CDMM 기반 복원, MDUR 벤치마크, 다운스트림 탐지
  "유효성 검증"만 언급(구체 수치·비교 대상 모델 불명).
- [[edge-constrained-uav-small-object-detection]] — YOLOX-Nano+P2+QIEA, VisDrone AP_small 31~
  44.9% 향상. 열화 이미지 조건 미고려.

### What already exists
- 복원 단독 벤치마크(MDUR)와 경량 탐지 단독 벤치마크(VisDrone)가 각각 독립적으로 존재.
- 두 페이지 간 "관련 개념" 링크로 개념적 인접성만 표시됨.

### What appears missing
- 두 파이프라인을 직렬 연결했을 때의 AP_small 개선분 대 종단 지연시간/FLOPs 증가분의 정량적
  트레이드오프.
- DAME-Net이 주장하는 "다운스트림 유효성 검증"이 구체적으로 어떤 탐지기·어떤 비용 조건에서
  이뤄졌는지 확인 가능한 근거.

### Potential novelty
- 두 논문 모두 2026-08 최근 등재로, 결합 파이프라인 비교는 두 원 논문 어디에도 명시되지 않음.
  "정확도 개선 vs 엣지 예산 초과"라는 구체적 트레이드오프 가설은 실무(엣지 디바이스 탑재) 의사결정에
  직접 기여 가능.

### Threat to novelty
- DAME-Net 원 논문 실험 섹션(arXiv:2604.09313)을 아직 원문 대조하지 않았음 — "다운스트림 유효성
  검증"이 이미 edge-constrained류 경량 탐지기와의 결합을 부분적으로 수행했을 가능성을 배제 못함.
  이 경우 novelty가 크게 줄어듦.
- 두 논문 모두 최근 게재라 후속 결합 연구가 다음 daily ingest에서 새로 발견될 가능성이 있음.

### Novelty confidence
0.4 — 위키 페이지 요약만으로는 DAME-Net의 다운스트림 검증 실험 범위를 판단할 수 없어 원문 확인
전까지 중간 이하로 제한. 원문에서 결합 미수행이 확인되면 상향 재평가 가능.

## Evidence Status

2026-10 근거 2편([[dame-net-uav-image-restoration]], [[edge-constrained-uav-small-object-detection]],
GAP-007) → 신규 생성. 재평가 대상 없음(첫 등재).

## Minimal validation plan

1. 선행조건: DAME-Net 원 논문(arXiv:2604.09313)의 "다운스트림 탐지 유효성 검증" 실험 섹션을
   원문 대조해 이미 edge-constrained류 경량 탐지기와 결합 실험을 했는지 확인(중복이면 각도 조정
   필요).
2. MDUR 벤치마크의 43개 열화 구성 중 대표 서브셋(단일 요인/2요인/4요인 복합)에 대해 "복원 없음",
   "DAME-Net 복원 후 탐지" 두 파이프라인을 YOLOX-Nano+P2로 실행.
3. AP_small, 종단 지연시간(ms), 총 FLOPs를 두 파이프라인 간 비교.
4. 엣지 디바이스(예: Jetson Nano급) 기준 지연시간 예산선을 긋고, 예산 내 최대 AP_small 조합을
   파레토 분석으로 식별.
