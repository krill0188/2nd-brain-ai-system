---
title: "ESC 고장 사례: AAIB Velos 추락과 BetaFPV Beta85X 화재"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: hardware
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-case-failure-aaib-velos-uas-esc-2019.md, inbox/processed/fetch-2026-10-16-hw-case-failure-betafpv-beta85x-esc-fire-2019.md]
confidence: medium
contested: false
contradictions: []
---

# ESC 고장 사례

두 사례 모두 2019년 발생했고 서로 다른 신뢰 수준의 출처다. AAIB는 독립 조사기관 보고서이고, BetaFPV는 제조사 자체 발표라 근본 원인 구분이 불완전하다.

## UK AAIB — Velos 단일 로터 UAS (2019-09 사고, 2020-04 보고서)
- ESC 결함 → 모터 출력 감소 → 배터리 과부하·급속 방전 → 추력 상실과 제어 불능 → 추락.^[inbox/processed/fetch-2026-10-16-hw-case-failure-aaib-velos-uas-esc-2019.md]
- 경고 표시가 조종사 시야 밖에 있어 이상을 인지하지 못했고 모터 개별 비활성화 절차도 수행되지 않았다.
- 시사점: 배터리 용량 여유 설계, 경고 화면의 주 시야 배치, 단일 로터의 고장 허용성 한계. 보고서 초록에 기체 중량·ESC 모델 등 수치는 없다.

## BetaFPV Beta85X 화재 (2019-02 발표)
- 초도 2,000대 중 약 100건(~5%) 화재, 제조사는 ESC 보드 불량률을 약 1%로 추정했다. BLHeli_32 ESC, 1105 모터, 4S 조건.^[inbox/processed/fetch-2026-10-16-hw-case-failure-betafpv-beta85x-esc-fire-2019.md]
- 원인으로 불량 납땜과 과전류를 제시했고, 벤치에서 4S 풀 스로틀 15~20초 후 화재를 재현했다. 프로토타입 50대로는 내구 시험이 부족했다고 인정했다.
- 제조사 조치: 4S 사용 중단 권고, 보증 교체, 시험 기준 개선. 독립 조사는 없다.

## 공통 교훈
실부하(풀 스로틀 지속) 열 시험, 납땜 품질 100% 검사, 전압·전류 정격 여유 확인이 반복된다. ESC 자체의 효율·열 거동 연구는 [[bldc-motor-esc-characterization-research]]를 참고한다.

관련: [[drone-safety-failsafe]], [[drone-power-battery]], [[fpv-hardware]].
