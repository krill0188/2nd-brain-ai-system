---
title: "GPS Signal Plan (Navipedia, ESA)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: rf-datalink-engineering
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]
confidence: medium
contested: false
contradictions: []
---

# GPS Signal Plan (Navipedia, ESA)

- 원문: https://gssc.esa.int/navipedia/index.php/GPS_Signal_Plan^[inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]
- 저자: ESA Navipedia^[inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]
- 발행: 미확인^[inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]

## 핵심 내용
Navipedia의 GPS 신호 계획 문서. GPS L1(1575.42 MHz), L2(1227.60 MHz), L5(1176.45 MHz) 대역과 각 대역의 신호(C/A, P(Y), M, L1C, L2C, L5)를 설명한다. L1C는 파일럿 성분이 BOC(1,1)과 BOC(6,1)의 시분할 다중, 데이터 성분은 BOC(1,1)로 기술된다. L2C는 CM/CL이 시분할 다중(각 511.5 kbps, 합성 1.023 MHz), L5는 두 직교 반송파 위의 BPSK이며 코드율 10.23 Mchips/s이다. 문서 구성: GPS L1/L2/L5 Band, GPS Modernization.^[inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- L1 1575.42 MHz / L2 1227.60 MHz / L5 1176.45 MHz (문서 본문)^[inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]
- C/A 코드 1.023 Mchips/s, P(Y) 10.23 Mchips/s, L5 코드 10.23 Mchips/s^[inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]
- 드론 수신기 선정 시 L1+L5(또는 L1+L2) 다중대역 지원 여부를 확인하는 기준 주파수 표로 사용 가능^[inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]

## 한계·미확인
신호 표(Tables 1-3)가 이미지라 텍스트로 확인 못 함. 신호 전력 수준·위성 수·발효 일정은 미확인. 문서 게재일 미확인.^[inbox/processed/hw-20261021-gnss-signals-gps-navipedia.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
