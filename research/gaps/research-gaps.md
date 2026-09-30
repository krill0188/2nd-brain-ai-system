---
status: draft
title: "연구 공백 원장 (Research Gaps Ledger)"
created: 2026-09-30
updated: 2026-09-30
type: gap-ledger
tags: [research, gaps, meta]
---

> ⚠ 스테이징 산출물 — canonical 아님

이 문서는 `concepts/`, `entities/`, `comparisons/`, `queries/` 전체를 스캔하여 발견한 연구 공백을
기록하는 원장이다. `research-gap-miner` 스킬(Weekly)이 갱신하며, 승인된 공백은
`research-idea-generator`가 연구 아이디어로 승격할 수 있다. 이 파일 자체는 canonical 지식이 아니다.

첫 실행(2026-09-30)이므로 모든 항목이 신규(GAP-001~GAP-014)다.

---

### GAP-001 · FPV FC 펌웨어(Betaflight/INAV/ArduPilot) 정량 비교 부재
- status: open
- type: 3
- evidence: [[fc-firmware-comparison]]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 동일 기체·동일 임무(레이싱/장거리/정밀자율) 조건에서 세 펌웨어의 지연시간·자세제어 정확도·배터리 소모를 정량 비교한 벤치마크 데이터가 위키에 편입되면 종료.

### GAP-002 · 한국 드론 규제(BVLOS·공역) 3자 비교(미국 FAA·EU U-space·한국) 부재
- status: open
- type: 3
- evidence: [[kci-bvlos-faa-nprm-korea]], [[kci-korea-airspace-eu-uspace]]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 동일 저자(윤민철) 계열의 FAA-한국 비교와 EU-한국 비교를 통합한 3자(FAA·EU·한국) 단일 비교표 또는 후속 연구가 canonical화되면 종료.

### GAP-003 · 드론 이상 징후 탐지: 센서·상태추정·데이터 기반 융합 미구현
- status: open
- type: 4
- evidence: [[drone-anomaly-detection-survey]] ^[inbox/processed/fetch-2026-08-19-kci-드론-이상-징후-탐지-방법-연구-동향-및-개선-방안-연구.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 세 가지 탐지 방법(센서/상태추정/데이터) 중 둘 이상을 결합한 실제 구현·성능평가 결과가 위키에 편입되면 종료.

### GAP-004 · MUM-T(유무인복합 편대) 검증이 시뮬레이션(M&S)에만 국한됨
- status: open
- type: 6
- evidence: [[kci-light-attack-helicopter-mum-t-verification]] ^[raw/papers/_unclassified/소형무장헬기-유무인복합-운용-통합검증환경-구축-및-비행제어시스템-통합-검증.md], [[kci-manned-unmanned-teaming-defensive-air-ops]] ^[raw/papers/_unclassified/방어적-대공-작전-및-엄호-시나리오에서의-협업-전투용-무인기-통합-유무인-복합-편대-임무-효과도-분석.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 실제 비행 시험(HIL이 아닌 실기체) 기반 MUM-T 효과도 검증 결과가 두 연구 중 하나라도 공개되면 종료. 시뮬레이션 결과만 반복되면 open 유지.

### GAP-005 · 한라산 구상나무 NDVI 활력도 임계값(0.5)이 예비 단일 조사에 그침
- status: open
- type: 5
- evidence: [[kci-hallasan-fir-ndvi-vitality-assessment]] ^[raw/papers/_unclassified/드론-다중분광센서-기반-ndvi를-활용한-한라산-구상나무-개체의-고도사면향별-활력도-예비평가.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 다른 계절·연도 또는 타 산지 구상나무 군락에서 동일 NDVI<0.5 임계값의 재현성이 검증되면 종료. 저자 스스로 "예비평가"로 명명한 만큼 후속 정량 검증이 나오기 전까지 open.

### GAP-006 · UAV 식생 이상 탐지(병해·활력도) 3계열 방법 간 교차 비교 부재
- status: open
- type: 3
- evidence: [[pine-wilt-disease-uav-detection]] ^[raw/papers/drone-ai/comparison-of-uav-image-based-detection-accuracy-of-pine-wilt-disease-affected-t.md], [[kci-hallasan-fir-ndvi-vitality-assessment]], [[kci-barley-wet-stress-hyperspectral-detection]]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: RGB+텍스처 채널(소나무재선충병), NDVI(구상나무), 초분광(보리)의 세 접근법을 동일 데이터셋 또는 통합 벤치마크로 비교한 연구가 편입되면 종료.

### GAP-007 · DAME-Net 복원 벤치마크(MDUR)가 위키 내 타 UAV 영상 복원/탐지 방법과 미비교
- status: open
- type: 3
- evidence: [[dame-net-uav-image-restoration]] ^[inbox/processed/fetch-2026-08-19-arxiv-compositional-degradation-uav-image-restoration-conditional-.md], [[edge-constrained-uav-small-object-detection]]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: DAME-Net과 위키에 이미 등재된 다른 열화 대응/소형 객체 탐지 파이프라인(예: edge-constrained 계열)을 동일 조건에서 비교한 결과가 나오면 종료.

### GAP-008 · 드론용 JEPA 계열 세계모델(SkyJEPA vs DroneWAM) 직접 비교 부재
- status: open
- type: 3
- evidence: [[skyjepa-world-models]], [[dronewam-efficient-world-action-model]] ^[inbox/processed/fetch-2026-09-30-arxiv-dronewam-efficient-world-action-model-for-drone-visual-navig.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 쿼드로터 제어용 SkyJEPA와 시각 내비게이션용 DroneWAM을 동일 과제(제어 또는 내비게이션) 및 동일 벤치마크에서 직접 비교한 결과가 나오면 종료.

### GAP-009 · DroneWAM이 자체 구축 합성 데이터셋(DroneNav-6D)에서만 검증됨
- status: open
- type: 6
- evidence: [[dronewam-efficient-world-action-model]] ^[inbox/processed/fetch-2026-09-30-arxiv-dronewam-efficient-world-action-model-for-drone-visual-navig.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 실제 비행 데이터 또는 제3자 데이터셋(비-DroneNav-6D)에서 DroneWAM의 궤적 정확도가 재현되면 종료.

### GAP-010 · Flytrex 옥상 도킹+AI 함대배치 효과(비용 60%↓·시간 절반)가 자사 발표에만 근거
- status: open
- type: 5
- evidence: [[flytrex-rooftop-docks-ai-fleet-positioning]] ^[inbox/processed/fetch-2026-09-17-rss-dronelife.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 제3자(규제기관·학술·독립 언론) 검증 데이터 또는 Flytrex가 공개한 원자료 기반 수치가 확인되면 종료.

### GAP-011 · Lowe's-DoorDash-Wing 드론 배송이 단일 지역·소수 품목에서만 검증됨
- status: open
- type: 6
- evidence: [[lowes-wing-doordash-drone-delivery-pilot]] ^[inbox/processed/fetch-2026-09-25-rss-dronedj.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 매튜스(NC) 외 지역 확장 또는 품목 확대 후 배송 성공률·품목 파손율 데이터가 공개되면 종료.

### GAP-012 · 미 국방부 C-UAS 마켓플레이스와 DIU 저비용 ISR 챌린지의 중복/보완성 미분석
- status: open
- type: 3
- evidence: [[us-dod-cuas-marketplace]] ^[inbox/processed/fetch-2026-08-05-rss-dronelife.md], [[diu-low-cost-isr-challenge]] ^[inbox/processed/fetch-2026-09-30-rss-dronelife.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: 두 조달 프로그램의 대상 기술 범위·예산·심사기준을 비교해 중복/보완 관계를 규명한 분석이 편입되면 종료.

### GAP-013 · Matternet M3의 "무인력 개입 수천 건 규모 확장" 목표가 2027년 상용화 이전 미검증
- status: open
- type: 5
- evidence: [[matternet]] ^[inbox/processed/fetch-2026-09-29-rss-dronedj.md]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: M3가 2027년 하반기 상용 서비스 개시 후 실제 무인 운영 배송 건수·개입률 데이터가 공개되면 종료.

### GAP-014 · AI 지식관리 도구 비교가 원본 미보존 상태(confidence: low)로 근거 재현 불가
- status: open
- type: 5
- evidence: [[knowledge-tool-roles]]
- first_found: 2026-09-30
- last_checked: 2026-09-30
- resolution_condition: Zotero·NotebookLM·LLM Wiki·Obsidian·Understand Anything 비교의 원본 출처(raw source)가 재수집되어 confidence가 medium 이상으로 갱신되면 종료.

---

## 요약

- 신규: GAP-001 ~ GAP-014 (14건)
- 갱신: 0건 (첫 실행)
- 해소: 0건 (첫 실행)
- 현재 open: 14건
