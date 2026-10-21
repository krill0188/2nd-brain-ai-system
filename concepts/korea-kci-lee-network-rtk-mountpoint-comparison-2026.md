---
title: "Comparative Analysis of GNSS Positioning Performance According to Network-RTK Service-Mountpoint Combinations"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: navigation-gnss-denied
tags: [drone, gnss, kci, network-rtk]
sources: [inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]
confidence: medium
contested: false
contradictions: []
---

# Comparative Analysis of GNSS Positioning Performance According to Network-RTK Service-Mountpoint Combinations

- 원문: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003377692^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]
- 저자: Lee Jeong Woo, Lee Jisun, Kwon Jay Hyoun^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]
- 발행: 2026 (한국측량학회지 JKSGPC, vol. 44, no. 4, p. 421)^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]

## 핵심 내용
KCI 포털 수록 논문(초록 직접 확인). 국내 네트워크-RTK 서비스가 서비스 방식과 RTCM 메시지 타입 조합 10개로 운영되는데 가용률·정확도가 검토되지 않았다는 문제의식으로, 전국 183개 통합기준점 관측 자료로 서비스별 자료 가용률과 고시 성과 대비 정확도, 공공측량 작업규정 허용오차 만족 여부를 평가했다.^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 자료 가용률 최고: RTS1 의 VRS-RTCM34, RTS2 의 VRS-RTCM32 — 183점 중 174점(95.1%)^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]
- 수평 정확도: RTS2 VRS-RTCM32 최대 0.168 m, 평균 0.028 m 차이로 가장 우수^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]
- 공공측량 허용오차(5 cm) 만족률: RTS2 VRS-RTCM32 91.4%, RTS1 VRS-RTCM34 90.8%^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]
- 타원체고 목표(10 cm) 만족률: RTS1 VRS-RTCM34 92.5%(오차 평균 -0.004 m)^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]
- RTS2 계열은 RTS1 대비 평균 7~10%p 낮은 만족률^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]
- 저자 권고: RTS1 은 VRS-RTCM34, RTS2 는 VRS-RTCM32 사용이 바람직^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]

## 한계·미확인
지상 통합기준점 정지 측정 기준이며 드론 동적 비행 성능은 아님. 마운트포인트 명칭 매핑 등 세부는 본문 미열람.^[inbox/processed/hw-20261021-korea-kci-lee-network-rtk-mountpoint-comparison-2026.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
