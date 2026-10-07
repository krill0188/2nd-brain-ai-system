---
title: "다수 VTOL 무인기 군집비행 이착륙 운용방안 (KCI)"
created: 2026-10-07
updated: 2026-10-07
type: concept
domain: flight-control
tags: [drone, swarm, research]
sources: [raw/papers/swarm/다수-vtol-무인기의-군집비행을-위한-이착륙-운용방안-및-실비행-적용.md]
confidence: low
contested: false
contradictions: []
---

# 다수 VTOL 무인기 군집비행 이착륙 운용방안

이호진(LIG디펜스&에어로스페이스)의 한국항공운항학회지(2026) 논문. 다수 VTOL 고정익 UAV가 군집비행에
진입·이탈할 때의 이착륙 절차를 제안하고 옥외 비행시험으로 적용성을 확인했다. 초록이 중간에서 잘려
결론 문장은 확인하지 못했다(confidence low).^[raw/papers/swarm/다수-vtol-무인기의-군집비행을-위한-이착륙-운용방안-및-실비행-적용.md]

## 제안 절차

- **이륙**: 전 기체 동시 수직이륙 → 그룹별 지정 고도로 고도 분리 → 그룹 단위 순차 출발. 출발하는
  그룹 내 기체들은 병렬로 천이(transition)한 뒤 군집비행에 진입한다.
- **착륙**: 공간 분리 → 군집 순차 이탈 → 역천이(reverse transition) → 착륙.

## 비행시험 결과

- 20대를 2개 그룹으로 나눠 시험. 지정 고도 도달 후 선두 그룹이 천이를 시작한 시점부터 **전 기체가 20.5초 이내**에
  천이를 완료했다.

## 관련 개념

- [[swarm-coordination]] — 군집 구조와 편대 비행 일반
- [[swarm-modes]] — Formation/Follow-Leader 등 군집 운용 모드
- [[kci-uav-swarm-mission-reliability-abort]] — 군집 임무 신뢰도 모델링
- [[indi-stability-tilt-rotor-vtol]] — 틸트로터 VTOL 제어기 안정성(천이 구간 제어 맥락, 기체 형상은 다름)
