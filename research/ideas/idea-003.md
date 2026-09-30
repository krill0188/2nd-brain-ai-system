---
id: idea-003
title: "SkyJEPA와 DroneWAM 직접 비교: 제어용 JEPA 세계모델을 내비게이션 과제로 전이했을 때의 성능"
status: draft
created: 2026-09-30
updated: 2026-09-30
gaps: [GAP-008]
sources: [inbox/processed/fetch-2026-09-30-arxiv-dronewam-efficient-world-action-model-for-drone-visual-navig.md, inbox/processed/fetch-2026-07-30-arxiv-skyjepa-learning-long-horizon-world-models-for-zero-shot-sim.md]
novelty_confidence: 0.35
---

> ⚠ 미검증 연구 아이디어 — canonical 아님

## Hypothesis

SkyJEPA(쿼드로터 저수준 제어용 JEPA 세계모델)의 물리 기반 프로버(physics-inspired prober)와
장기 예측 구조를, DroneWAM의 시각 내비게이션 과제(DroneNav-6D)에 어댑터 방식으로 이식하면,
DroneWAM 고유의 Adaptive Rollout 게이트만 사용하는 것보다 궤적 정확도는 비슷하거나 낮지만
sim-to-real 전이 강건성(도메인 시프트 조건에서의 성능 저하폭)은 더 우수할 것이다 — 즉 "제어 특화
JEPA 구조"와 "내비게이션 특화 JEPA 구조"는 각기 다른 축(정확도 vs 전이 강건성)에서 우위를 가질
것이다.

## Why now (근거 요약)

[[skyjepa-world-models]]와 [[dronewam-efficient-world-action-model]]은 둘 다 드론 응용 JEPA
계열 세계모델이면서도 대상 과제가 다르다(전자는 쿼드로터 저수준 제어, 후자는 시각 내비게이션)
^[inbox/processed/fetch-2026-07-30-arxiv-skyjepa-learning-long-horizon-world-models-for-zero-shot-sim.md]
^[inbox/processed/fetch-2026-09-30-arxiv-dronewam-efficient-world-action-model-for-drone-visual-navig.md].
두 연구는 위키에서 "관련 개념"으로 상호 링크되어 있지만, 동일 과제·동일 벤치마크에서 직접 비교된
적은 없다(GAP-008).

## Novelty Ledger

### Known Similar Work
- [[skyjepa-world-models]] — 잠재 공간 역학 모델 + 물리 기반 프로버 + 샘플링 기반 최적 제어로
  쿼드로터 실시간 제어, 제로샷 sim-to-real 전송을 주장(Rao et al., arXiv:2606.23444).
- [[dronewam-efficient-world-action-model]] — JEPA 기반 world model + Adaptive Rollout 게이트로
  DroneNav-6D 벤치마크 최고 궤적 정확도 달성(arXiv:2609.33148).
- [[computer-vision-drone]] — 두 연구가 공통으로 속하는 상위 개념(드론 AI 자율 의사결정).

### What already exists
- 두 세계모델 각각의 단독 벤치마크 성과(SkyJEPA: open-loop 예측 정확도 + sim-to-real 전송,
  DroneWAM: DroneNav-6D 궤적 정확도).
- 두 연구 간 아키텍처적 유사성(JEPA 기반, latent space 예측)이 위키 위키링크로 이미 표시됨.

### What appears missing
- 두 모델을 동일 과제(제어 또는 내비게이션 둘 중 하나)와 동일 데이터셋에서 나란히 평가한 결과.
- SkyJEPA의 물리 기반 프로버 구조를 내비게이션 과제에, 또는 DroneWAM의 Adaptive Rollout을
  저수준 제어 과제에 이식했을 때의 교차 적용성.

### Threat to novelty
- **[[skyjepa-world-models]]의 출처(sources)가 canonical 페이지에서 빈 배열([])로 기록되어 있고,
  "raw source not preserved in repo — needs recapture" 노트가 있어 confidence: medium 상태다.**
  다만 2026-09-30 확인 결과 `inbox/processed/fetch-2026-07-30-arxiv-skyjepa-learning-long-horizon-world-models-for-zero-shot-sim.md`
  파일 자체는 존재한다 — canonical 페이지의 sources 필드 누락은 메타데이터 정합성 문제로 보이며,
  이 아이디어의 근거로 인용은 가능하나 원 논문 본문(arXiv:2606.23444) 재확인 전까지는 SkyJEPA
  관련 세부 주장(제로샷 sim-to-real 강건성 등)을 낮은 확신으로 취급해야 함.
- DroneWAM 코드·데이터가 "공개 예정"이며 아직 실제로 재현 가능한지 미확인 — 공개 지연 시 실증
  검증 자체가 지연될 수 있음.
- JEPA 계열 세계모델 교차비교 연구가 로보틱스/자율주행 분야에는 이미 존재할 가능성이 높음(드론
  특화 사례만 위키 내 부재 확인) — novelty_confidence를 낮게 유지하는 주된 이유.

### Potential novelty
- 드론 도메인 한정으로는 제어-특화 JEPA와 내비게이션-특화 JEPA를 교차 평가한 사례가 위키/원 논문
  어디에도 없음. "정확도 vs 전이 강건성" 트레이드오프 가설은 두 원 논문 모두 명시적으로 다루지
  않은 축.

### Novelty confidence
0.35 — SkyJEPA 근거의 출처 정합성 문제(원문 재확인 필요)와 DroneWAM 코드 미공개 상태로 인해
현시점 실행 가능성이 낮고, 위키 밖 JEPA 교차비교 선행연구 존재 가능성도 배제 못해 낮은 확신으로
설정. SkyJEPA 원문 재확인 또는 DroneWAM 코드 공개 중 하나라도 이뤄지면 상향 재평가 가능.

## Evidence Status

2026-09 근거 2편([[skyjepa-world-models]], [[dronewam-efficient-world-action-model]]) → 신규
생성. SkyJEPA 근거의 출처 정합성 문제로 낮은 확신 등급 부여. 재평가 대상 없음(첫 등재).

## Minimal validation plan

1. 선행 작업: `inbox/processed/fetch-2026-07-30-arxiv-skyjepa-learning-long-horizon-world-models-for-zero-shot-sim.md`
   원문과 arXiv:2606.23444 본문을 대조해 SkyJEPA canonical 페이지의 sources 필드 정합성부터
   확인(연구 착수 전 필수 선행 조건).
2. DroneWAM 코드/데이터 공개(https://github.com/1e12Leon/DroneWAM) 여부 확인.
3. 두 조건이 충족되면, DroneNav-6D 벤치마크에서 SkyJEPA의 프로버 구조를 어댑터로 이식한 변형
   모델을 구현하고 DroneWAM 원본과 궤적 정확도·연산량을 비교.
4. 도메인 시프트 조건(예: DroneNav-6D의 랜덤 바람 교란 강도를 학습 시보다 높여 평가)에서 두
   모델의 성능 저하폭을 비교해 "정확도 vs 전이 강건성" 가설을 검증.
