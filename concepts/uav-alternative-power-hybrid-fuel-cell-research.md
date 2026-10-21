---
title: "UAV 대안 동력원 연구: ICE 하이브리드와 PEM 연료전지"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: hardware
ontology_class: Engine
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-paper-hybrid-ice-generator-multirotor-krznar-2024.md, inbox/processed/fetch-2026-10-16-hw-paper-pem-fuel-cell-uav-alternative-power-shuhayeu-2024.md]
confidence: low
contested: false
contradictions: []
---

# UAV 대안 동력원 연구

## ICE+발전기 하이브리드 (Krznar 외, 2024)
15~35 kg급 멀티콥터 이론 설계 3종(MTOW 15.6/27.9/34.9 kg)에서 배터리 대비 하이브리드 체공시간을 비교했다.^[inbox/processed/fetch-2026-10-16-hw-paper-hybrid-ice-generator-multirotor-krznar-2024.md]

| 설계 | 배터리 체공 | 하이브리드 체공 | 하이브리드 유리 임계 동력장치 질량 |
|---|---|---|---|
| 1 (15.6 kg) | 26.4 min | 61.9 min | 4.94 kg |
| 2 (27.9 kg) | 27.1 min | 84.8 min | 8.41 kg |
| 3 (34.9 kg) | 29.42 min | 147.2 min | 10.88 kg |

연료 종류에 따라 배터리 대비 2~5배라는 결론이지만 실기 비행시험이 아닌 이론 설계안이며 배출물·소음은 미확인이다.

## PEM 연료전지 (Shuhayeu 외, 2024)
전기 UAV용 PEM 연료전지의 모델링·최적화·성능 분석 논문이다. 원문이 HTTP 403으로 열람되지 않아 검색 스니펫의 체공 약 2배, 에너지 밀도 약 1700 대 150~250 Wh/kg 수치는 확정값으로 쓰지 않는다.^[inbox/processed/fetch-2026-10-16-hw-paper-pem-fuel-cell-uav-alternative-power-shuhayeu-2024.md]

## 연결 사례
[[drone-firefighting-surveillance-cases]]의 대한항공 하이브리드 드론은 체공 2시간(배터리 전용 대비 4배)을 주장하는 운용 사례다. 고에너지 배터리는 [[amprius-sicore-battery]], 수소 추진은 [[heven-aerotech]]를 참고한다.

관련: [[drone-power-battery]].
