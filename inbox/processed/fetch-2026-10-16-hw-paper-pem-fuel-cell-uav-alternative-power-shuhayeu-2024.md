---
title: "Investigating PEM Fuel Cells as an Alternative Power Source for Electric UAVs: Modeling, Optimization, and Performance Analysis"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://doi.org/10.3390/en17174427
tags: [drone, hardware, fuel-cell, hybrid-power, endurance]
authors: Shuhayeu, Martsinchyk, Martsinchyk, Milewski
published: 2024-09-04, Energies
---

# 요약

전기 UAV의 대안 동력원으로 PEM 연료전지를 배터리와 비교하는 모델링·최적화·성능 분석 논문이다. 서지 정보(제목·저자·게재지·발행일)는 Crossref 메타데이터로 확인했다.

# 핵심 내용

- 제목이 나타내듯 PEM 연료전지 모델링, 최적화, 성능 분석을 한 편에서 다룬다.
- 검색 스니펫에는 연료전지 체공시간이 배터리 대비 약 2배이고 에너지 밀도가 약 1700 Wh/kg 대 150~250 Wh/kg이라는 문구가 보였으나, **원문(MDPI)이 HTTP 403으로 열람되지 않아 본문에서 확인하지 못했다.** 이 수치는 확정값으로 쓰지 않는다.

# 설계에 쓸 수 있는 지침

- 연료전지 대안을 검토할 때는 시스템 질량(연료전지+수소저장+BoP)을 함께 넣어 체공시간을 계산해야 공정한 비교가 된다는 점을 체크리스트에 넣을 수 있다.
- 배터리와 같은 조건에서 체공시간·질량을 비교하는 구조는 Krznar 2024(하이브리드 ICE) 사례와 함께 보면 동력원 선정 비교표로 묶기 좋다.

# 한계·미확인

- 원문 본문 미열람: 모델 구성, 최적화 목적함수, 수치 결과 **모두 미확인**.
- 스니펫의 Wh/kg 및 체공 배수 수치는 원문 대조 전이므로 **미확인** 처리.
- 열람 가능한 원문 확보 시 재수집 필요.
