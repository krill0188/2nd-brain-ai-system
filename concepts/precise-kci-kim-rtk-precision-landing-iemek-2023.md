---
title: "Experiments of RTK based Precision Landing for Rotary Wing Drone"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, gnss, kci, rtk]
sources: [inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Experiments of RTK based Precision Landing for Rotary Wing Drone

- 원문: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002952659^[inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]
- 저자: Young-Kyu Kim, Jin-Woung Jang, Jong-Hee Lee, Jong-Ho Yoo, Seungh Hyun Paik, Dae-Nyeon Kim^[inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]
- 발행: 2023 (IEMEK J. Embedded Systems and Applications, vol. 18, no. 2, p. 75; DOI 10.14372/IEMEK.2023.18.2.75)^[inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]

## 핵심 내용
KCI 포털 수록 논문(초록 직접 확인). 드론 스테이션 자동 충전용으로 영상처리 대신 RTK 기반 정밀 착륙 정확도를 실험했다. 이륙점 1, 경유점 2, 착륙점 1 로 구성한 미션을 RTK 측량 정확도 설정 0.3 / 0.2 / 0.1 m 로 각각 10회 반복했다.^[inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 착륙 오차 거리 평균: 0.3 m 설정 약 0.258 m / 0.2 m 설정 약 0.12 m / 0.1 m 설정 약 0.057 m^[inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]
- 각 설정 10회 반복 시험^[inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]
- 영상처리 대비 임무중량·비용·개발복잡도 부담이 적다는 저자 주장(초록)^[inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]

## 한계·미확인
기체·RTK 모듈·기선 길이·보정 방식 미확인. 반복 10회 소표본.^[inbox/processed/hw-20261021-precise-kci-kim-rtk-precision-landing-iemek-2023.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
