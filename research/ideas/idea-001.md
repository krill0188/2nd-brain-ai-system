---
id: idea-001
title: "센서·상태추정·데이터 기반 3중 융합 드론 이상탐지: 융합 조합별 오탐률/누락률 비교 검증"
status: draft
created: 2026-09-30
updated: 2026-10-01
gaps: [GAP-003]
sources: [raw/papers/_unclassified/드론-이상-징후-탐지-방법-연구-동향-및-개선-방안-연구.md]
novelty_confidence: 0.55
---

> ⚠ 미검증 연구 아이디어 — canonical 아님

## Hypothesis

동일 비행 로그·센서 데이터셋에서 (1) 센서 기반, (2) 상태추정 기반, (3) 데이터 기반 이상탐지
방법을 2개씩 조합한 세 가지 융합 모델(센서+상태추정 / 센서+데이터 / 상태추정+데이터)과 3방법 전체
융합 모델을 각각 구현·비교하면, 단일 방법 대비 오탐률(false positive rate)과 미탐률(miss rate)이
통계적으로 유의하게 낮아질 것이다. 특히 "센서+데이터" 조합이 "상태추정+데이터" 조합보다 계산 비용
대비 개선폭이 클 것으로 예상한다(상태추정 기반 방법은 모델 정확도 의존성이 커서 융합 이득이 제한적).

## Why now (근거 요약)

[[drone-anomaly-detection-survey]]는 센서 기반·상태추정 기반·데이터 기반 세 방법의 원리·장단점을
정리하고 "센서+상태추정", "센서+데이터", "상태추정+데이터", "세 방법의 통합적 융합"을 발전 방향으로
제시했지만, 실제 구현·성능평가 결과는 제시하지 않았다 ^[raw/papers/_unclassified/드론-이상-징후-탐지-방법-연구-동향-및-개선-방안-연구.md].
즉 융합 방향은 방법론적으로 제안되었으나 "어느 조합이 얼마나 개선되는가"는 미검증 상태다. 이는
GAP-003(드론 이상 징후 탐지: 센서·상태추정·데이터 기반 융합 미구현)로 원장에 등재되어 있다.

## Novelty Ledger

### Known Similar Work
- [[drone-anomaly-detection-survey]] — 3방법 분류·장단점·융합 발전 방향을 제시한 동향 연구(대진대 김남용, 한국융합과학회지 2026). 구현·정량 비교는 없음.
- [[flight-logging-analysis]] — ULog 기반 비행 데이터 분석(데이터 기반 방법의 기초 재료가 될 수 있는 위키 내 인접 개념).
- [[sensor-calibration]], [[drone-safety-failsafe]] — 센서 기반/안전 시스템 관련 인접 개념. 융합 구현 사례로 확인된 것은 아님.

### What already exists
- 3방법 각각의 원리·장단점에 대한 문헌 리뷰 수준 정리.
- 융합이 "바람직하다"는 방향성 제안.

### What appears missing
- 두 개 이상 방법을 실제로 결합한 구현체와, 단일 방법 대비 정량적 성능 개선(오탐률/미탐률/지연시간)을
  같은 데이터셋·같은 임무 조건에서 비교한 결과.
- 융합 조합 간(센서+상태추정 vs 센서+데이터 vs 상태추정+데이터) 상대적 우열 비교.

### Potential novelty
- 동일 비행 로그(예: PX4 ULog 또는 ArduPilot dataflash)에 대해 4가지 융합 조합(3개 2-way + 1개
  3-way)을 통제된 조건에서 나란히 비교한 최초의 정량 벤치마크가 될 수 있음. 서베이가 제시한
  "발전 방향"을 실제로 검증하는 후속 연구로서 자리매김 가능.

### Threat to novelty
- 원 논문(대진대 김남용, 2026)의 저자 그룹이 후속 구현 논문을 이미 준비 중일 수 있음 — 국내
  이상탐지 융합 구현 논문이 KCI/arXiv에 새로 게재되면 재평가 필요.
- 서베이 자체가 1차 문헌이라 본 위키에 등재된 것 외 해외 융합 이상탐지 선행연구(예: UAV FDI/FDD
  분야)가 존재할 가능성이 높음 — 위키 내에는 비교 대상이 확인되지 않으므로 novelty_confidence를
  중간 이하로 유지.

### Novelty confidence
0.55 — 위키 내 비교 대상 부재는 확인되나, 위키 밖(해외 UAV fault detection/FDI 문헌) 선행연구
존재 가능성을 배제할 근거가 없어 중간 수준으로 제한.

## Evidence Status

2026-09 근거 1편([[drone-anomaly-detection-survey]]) → 신규 생성. 재평가 대상 없음(첫 등재).

2026-10 재평가: idea 생성 이후(2026-09-30 daily ingest, 730e1a8) raw/inbox/concepts/gaps 어디에도
GAP-003 관련 신규 근거 없음(`git log --since=2026-09-30 -- raw inbox concepts entities comparisons
queries` 결과 해당 배치 커밋 이후 변경 0건). 국내외 융합 이상탐지 구현 논문 게재 여부(Threat to
novelty)도 미확인 상태 유지 → novelty_confidence 0.55 유지.

## Minimal validation plan

1. 공개 PX4 ULog 또는 ArduPilot dataflash 이상 이벤트 데이터셋(예: 모터 고장·GPS 손실·배터리
   이상 라벨 포함)을 확보하거나, SITL에서 고장 주입(fault injection) 시뮬레이션으로 라벨링된
   데이터셋을 자체 구축.
2. 단일 방법 베이스라인 3종(센서 임계값 기반, EKF 잔차 기반 상태추정, LSTM/오토인코더 기반
   데이터 방법) 구현.
3. 2-way 융합 3종 + 3-way 융합 1종을 앙상블 또는 게이팅 방식으로 구현.
4. 동일 테스트셋에서 오탐률·미탐률·탐지 지연시간(ms)을 7개 모델(단일 3 + 융합 4) 간 비교.
