---
title: "Low-latency jamming mitigation in SWaP-constrained GNSS analog CRPAs via hierarchical dithered null steering"
created: 2026-10-22
captured: 2026-10-22
type: paper
domain: hardware
source: https://doi.org/10.1038/s44459-026-00049-8 (PMC13331733)
tags: [drone, gnss, 4-재밍스푸핑, crpa, null-steering, swap, 시뮬레이션]
authors: "M. Elaraby, A. Massoud, M. Hassan, H. Elghamrawy, A. Noureldin"
published: "2026 (저널명은 Europe PMC 응답에 없음)"
---

## 핵심 내용
아날로그 빔포밍 CRPA 는 소형·저전력 재밍 방어 수단이지만 기존 격자 탐색 방식은 느리고 실패하기 쉽다고 지적하고, 이진 정제와 경량 디더링을 결합한 계층 탐색 프레임워크를 제안한다. 억제 대비(suppression contrast)를 안내 신호로 사용해 모호한 경우를 해결.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 4소자 아날로그 CRPA 시뮬레이션에서 평균 재머 억제 거의 50 dB.
- 전수 탐색 대비 측정 복잡도 평균 약 96% 감소(최대 98%).
- SWaP 제약이 있는 GNSS 수신기에서 저지연 동작이 가능하다는 주장(소형 드론 CRPA 후보 알고리즘).

## 한계·미확인
시뮬레이션 결과이며 실기체 비행·실측 억제량은 없음. 소자 배치·플랫폼 영향(기체 구조 산란)은 초록에서 확인 못함.
