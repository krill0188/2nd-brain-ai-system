---
title: "Galileo Signal Plan (Navipedia, ESA)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: rf-datalink-engineering
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]
confidence: medium
contested: false
contradictions: []
---

# Galileo Signal Plan (Navipedia, ESA)

- 원문: https://gssc.esa.int/navipedia/index.php/Galileo_Signal_Plan^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]
- 저자: ESA Navipedia^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]
- 발행: 미확인^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]

## 핵심 내용
Galileo의 E1, E6, E5(E5a/E5b) 대역과 변조 방식을 정리한 문서. E1은 CBOC(MBOC 구현), E6는 BPSK(5), E5는 AltBOC(15,10) 광대역 신호이며 E5a와 E5b는 E5의 구성 성분으로 다뤄진다. 문서에 C-band 절도 있다.^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- E1 1575.420 MHz (CBOC)^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]
- E6 1278.750 MHz (BPSK(5))^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]
- E5 1191.795 MHz (AltBOC(15,10)), E5a 1176.450 MHz, E5b 1207.140 MHz^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]
- E1/E5a는 GPS L1/L5와 같은 중심주파수라 단일 안테나·RF 체인 공용 설계가 가능한 대역 배치(주파수 표에서 확인되는 사실)^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]

## 한계·미확인
E5a/E5b 개별 변조는 문서에서 별도 기재되지 않음. 인증 신호(OSNMA) 등 서비스 정보는 이 페이지에서 미확인.^[inbox/processed/hw-20261021-gnss-signals-galileo-navipedia.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
