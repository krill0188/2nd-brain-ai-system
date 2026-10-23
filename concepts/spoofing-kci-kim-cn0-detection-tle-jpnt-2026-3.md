---
title: "A Study on C/N0 Based GNSS Spoofing Detection Considering GNSS Environmental Characteristics and TLE-Based Satellite Orbit Information Over the Korean Peninsula"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
ontology_class: GNSSInterferenceSecurity
tags: [drone, gnss, kci]
sources: [inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-tle-jpnt-2026-3.md]
confidence: medium
contested: false
contradictions: []
---

# A Study on C/N0 Based GNSS Spoofing Detection Considering GNSS Environmental Characteristics and TLE-Based Satellite Orbit Information Over the Korean Peninsula

- 원문: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003381247^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-tle-jpnt-2026-3.md]
- 저자: Yoo Hak Kim, Jae Min Ahn^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-tle-jpnt-2026-3.md]
- 발행: 2026 (Journal of Positioning, Navigation, and Timing, vol. 15, no. 3, p. 391; DOI 10.11003/JPNT.2026.15.3.391)^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-tle-jpnt-2026-3.md]

## 핵심 내용
KCI 포털 수록 논문(초록 직접 확인). 앞선 연구(위 1호 논문)를 확장해 다중 Off-Prompt 상관기 구조와 TLE 기반 위성 궤도 정보로 시변 C/N0 추세를 생성한다. 정상 조건(H0)에 신틸레이션·멀티패스를 포함하고, 스푸핑(H1)은 코드 지연 0.1 chip, 전력 우위 +1/+2/+3 dB 로 모델링한다. 위상 정렬(0도) 스푸핑을 정교한 공격으로 보고 추가 위상 오프셋에서 민감도를 평가한다.^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-tle-jpnt-2026-3.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 스푸핑 모델: 코드 지연 0.1 chip, 전력 우위 +1, +2, +3 dB^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-tle-jpnt-2026-3.md]
- 상관 왜곡 기반 탐지는 준동기(near-synchronous) 스푸핑에서 성능이 제한된다고 서술(초록)^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-tle-jpnt-2026-3.md]

## 한계·미확인
초록 후반(탐지 성능 수치)은 열람한 분량에서 잘려 미확인. 시뮬레이션 연구.^[inbox/processed/hw-20261021-spoofing-kci-kim-cn0-detection-tle-jpnt-2026-3.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
