---
title: "Hybrid Electrical-Internal Combustion Engine Power Supply for Multirotors: Feasibility Analysis and Case Study"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://doi.org/10.13044/j.sdewes.d12.0505
tags: [drone, hardware, hybrid-power, battery, endurance]
authors: Matija Krznar, Danijel Pavković, Juraj Benić, Danko Brezak, Mihael Cipek
published: 2024-06 (vol. 12, issue 2), Journal of Sustainable Development of Energy, Water and Environment Systems (JSDEWES), article 1120505
---

# 요약

15~35 kg급 대형 멀티콥터에 내연기관(ICE)+발전기 세트를 쓰는 하이브리드 동력이 실현 가능한지 판단하는 방법을 제시하고, 이론상의 헤비리프트 설계 3종에서 순수 배터리와 하이브리드를 비교한 사례 연구다.

# 핵심 내용

- 설계 3종 최대이륙중량: 15.6 kg / 27.9 kg / 34.9 kg (Table 5).
- 배터리 대비 하이브리드 체공시간 (Table 8, 페이지 기재값):

| 설계 | 동력장치 질량 | 배터리 에너지 | 하이브리드 에너지 | 배터리 체공 | 하이브리드 체공 |
|---|---|---|---|---|---|
| 1 (15.6 kg) | 6.06 kg | 792 Wh | 1857 Wh | 26.4 min | 61.9 min |
| 2 (27.9 kg) | 12.12 kg | 1584 Wh | 4954 Wh | 27.1 min | 84.8 min |
| 3 (34.9 kg) | 18.17 kg | 2376 Wh | 9742 Wh | 29.42 min | 147.2 min |

- 하이브리드가 배터리보다 유리해지는 동력장치 임계 질량: 4.94 kg / 8.41 kg / 10.88 kg.
- 결론: 연료 종류에 따라 체공시간이 배터리 대비 2배에서 5배 수준으로 늘어난다고 기술.

# 설계에 쓸 수 있는 지침

- 체공시간 목표가 30분을 넘는 대형기라면, 동력장치 질량 임계값을 먼저 계산해 배터리-only와 하이브리드 중 무엇이 유리한지 판단하는 절차를 그대로 쓸 수 있다.
- 배터리 에너지와 하이브리드 에너지를 나란히 두는 표 형식은 자사 설계 비교표 양식으로 재사용 가능하다.

# 한계·미확인

- 세 설계는 **이론 설계안**이며 실기 비행시험 결과가 아니다.
- 배출물·소음 결과는 페이지에 없고 향후 과제로만 언급되어 **미확인**.
- 표 7의 탱크 구성별 세부 체공시간은 본 요약에서 전부 옮기지 않았다.
