---
title: "Construction of Network RTK Testbed Using Reference Stations of NGII"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: navigation-gnss-denied
ontology_class: PrecisePositioning
tags: [drone, gnss, kci, network-rtk]
sources: [inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]
confidence: medium
contested: false
contradictions: []
---

# Construction of Network RTK Testbed Using Reference Stations of NGII

- 원문: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003060454^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]
- 저자: Bu-Gyeom Kim, Changdon Kee^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]
- 발행: 2024 (Journal of Positioning, Navigation, and Timing, vol. 13, no. 1, p. 103; DOI 10.11003/JPNT.2024.13.1.103)^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]

## 핵심 내용
KCI 포털 수록 논문(초록 직접 확인). 국토지리정보원(NGII) 상시관측소로 실시간 네트워크 RTK 연구용 테스트베드를 구축. 서울 3개소 포함, 서로 100 km 미만인 4개 관측소 그룹을 선정하고 RTCM 실시간 자료의 잡음을 분석했다. 사용자 기준국을 테스트베드 내에 두고 MAC 방식 네트워크 RTK 성능을 GPS L1 후처리로 분석했다.^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 반송파 위상 측정 잡음: mm 수준 (초록)^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]
- 보정 적용 후 모든 사용자 잔차 오차 10 cm 이내^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]
- LAMBDA 로 정수 모호성 결정 시 고정률 100%, 모든 모호성이 참값으로 해결^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]
- 관측소 간 거리 100 km 미만 4개소 그룹^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]

## 한계·미확인
L1 단일 주파수 후처리 평가. 드론 동적 환경 아님. 신청 절차 등 서비스 이용 정보 아님.^[inbox/processed/hw-20261021-korea-kci-kim-ngii-network-rtk-testbed-jpnt-2024.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
