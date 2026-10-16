---
title: "UK AAIB 조사 - Velos 단일 로터 UAS ESC 고장 추락 (2019)"
created: 2026-10-16
captured: 2026-10-16
type: case
domain: hardware
source: https://www.gov.uk/aaib-reports/aaib-investigation-to-velos-single-rotor-uas-registration-n-a-180919
organization: UK Air Accidents Investigation Branch (AAIB)
field: 하드웨어 고장·안전
published: "2020-04"
tags: [drone, hardware, case, failure, ESC, motor, battery-depletion, loss-of-control, AAIB]
---

# UK AAIB 조사 - Velos 단일 로터 UAS ESC 고장 추락 (2019)

## 개요

영국 항공사고조사국(AAIB)이 2019년 9월 발생한 Velos 단일 로터 UAS 추락 사고를 조사한 공식 보고서(2020년 4월 발행). **ESC 고장으로 모터가 출력을 잃고, 배터리가 급속히 방전되어 제어 불능** 상태가 된 사례.

## HW 구성 (표)

| 항목 | 내용 | 출처 신뢰도 |
|------|------|------------|
| 기체 | Velos 단일 로터 UAS | 높음(AAIB 공식) |
| 고장 부위 | ESC | 높음 |
| 고장 결과 | 모터 회전 감소 → 과부하 → 배터리 급속 방전 | 높음 |
| 최종 결과 | 제어 불능, 추락 | 높음 |
| 경고 표시 | 조종사 화면 밖에 위치 → 미인지 | 높음 |
| 기체 세부 사양 | 미확인 (보고서 본문에 있으나 초록에 미기재) | — |

## 고장 메커니즘

1. **ESC 결함** 발생 → 해당 모터 출력 감소.
2. 정상 모터가 보상 시도 → **배터리에 과부하**.
3. 배터리 급속 방전 → **전체 추력 손실** → 제어 불능.
4. 조종사가 경고 화면을 시야 밖에 배치 → **이상 징후 미인지**, 정상 절차(모터 개별 비활성화) 미수행.

## 성과·한계

- **교훈 1:** ESC 고장은 단순 단일 부품 고장이 아닌 **배터리 급속 방전 연쇄반응** 유발 가능 → 배터리 용량 여유(margin) 설계 필수.
- **교훈 2:** 텔레메트리 경고 화면은 **조종사 주 시야 내** 배치 의무화.
- **교훈 3:** 단일 로터 시스템은 모터 1개 고장 시 보상 능력 없음 → 다중 로터가 고장 허용성에서 유리.
- **한계:** 공개 보고서 초록에 기체 중량·배터리 용량·ESC 모델 등 세부 수치 미기재; 전문 확인 필요.

## 출처의 신뢰도

- UK AAIB 공식 조사 보고서 (Tier 0): **높음** — 독립 항공 사고 조사 기관
- 확인 날짜: 2026-10-16
