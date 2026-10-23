---
title: "A Study on C/N0 Based GNSS Spoofing Detection Considering the GNSS-Environmental Characteristics of the Korean Peninsula"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
ontology_class: GNSSInterferenceSecurity
tags: [drone, gnss, kci]
sources: [inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]
confidence: medium
contested: false
contradictions: []
---

# A Study on C/N0 Based GNSS Spoofing Detection Considering the GNSS-Environmental Characteristics of the Korean Peninsula

- 원문: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003314286^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]
- 저자: Yoo Hak Kim, Jae Min Ahn^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]
- 발행: 2026 (Journal of Positioning, Navigation, and Timing, vol. 15, no. 1, p. 25; DOI 10.11003/JPNT.2026.15.1.25)^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]

## 핵심 내용
KCI 포털 수록 논문(초록 직접 확인). 고정 GNSS 수신기(기준국)에서 속도 정보를 쓸 수 없을 때 C/N0 로 스푸핑을 탐지하는 방법. 한반도 전리층 신틸레이션으로 인한 C/N0 감쇠를 정상 상태(H0)로 모델링하고, 스푸핑(H1)은 전력 우위 +3/+6/+9 dB 와 0.25 chip 코드 지연으로 표현한다. 1 ms 마다 C/N0 를 추정하고 슬라이딩 윈도우 χ² 지표와 적응 임계값을 사용한다.^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 모든 PRN 에서 ROC AUC 0.9 초과 (시뮬레이션, 초록)^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]
- 스푸핑 모델: 전력 우위 +3, +6, +9 dB / 코드 지연 0.25 chip^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]
- 전리층 신틸레이션이 C/N0 기반 탐지의 오경보 요인이며 이를 모델에 포함해야 한다는 점^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]

## 한계·미확인
시뮬레이션. 드론 탑재 수신기(이동체) 적용은 대상이 아님(고정국 대상). 실측 검증 미확인.^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-korea-jpnt-2026-1.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
