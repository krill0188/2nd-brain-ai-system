---
title: "An Analytical Design Optimization Method for Electric Propulsion Systems of Multicopter UAVs with Desired Hovering Endurance"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/1809.02472
authors: "Xunhua Dai, Quan Quan, Jinrui Ren, Kai-Yuan Cai"
published: "2018-09-01"
tags: [drone, hardware, paper, propulsion, motor, ESC, battery, design-optimization, hovering]
---

# An Analytical Design Optimization Method for Electric Propulsion Systems of Multicopter UAVs with Desired Hovering Endurance

## 핵심 내용 (방법·결과)

멀티콥터 추진계(프로펠러·모터·ESC·배터리) 설계를 **경험과 시행착오에 의존하는 방식에서 벗어나** 해석적 최적화 방법으로 전환하는 실용적 방법론을 제안했다. IEEE/ASME Transactions on Mechatronics 2019, vol. 24, pp. 228–239 게재.

**핵심 방법:**
- 전체 설계 문제를 **프로펠러 → 모터 → ESC → 배터리** 순서의 하위 문제로 분리(decouple).
- 각 하위 문제를 해석적으로 풀어 최적 파라미터 도출.
- 실제 제품 데이터베이스에서 최근접 제품 선택 → 빠른 프로토타이핑 지원.
- 실험 및 통계 분석으로 방법론 유효성 검증.

## 설계에 쓸 수 있는 지침

- **설계 순서 원칙:** 프로펠러 먼저 선정(추력·직경·피치) → 모터(KV·최대 전류) → ESC(전류 용량) → 배터리(셀 수·용량) 순서로 최적화.
- 호버링 지속시간을 목표로 역산할 때 이 방법론의 공식을 직접 적용 가능.
- 기성 부품 데이터베이스 기반 접근이므로 신규 설계 시 개발 비용 및 시간 절감.
- 동일 저자(Quan 등)의 멀티콥터 제어 교재와 함께 사용하면 설계-제어 일관성 확보.

## 한계·미확인 항목

- 전진 비행 최적화는 포함되지 않음 (호버링 체공시간 중심).
- 데이터베이스의 최신성(2018년 기준): 현재 기성 부품과 갭 발생 가능.
- ESC 열 손실 모델 포함 여부: 미확인.
