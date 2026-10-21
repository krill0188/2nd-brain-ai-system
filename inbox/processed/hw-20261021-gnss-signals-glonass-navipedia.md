---
title: "GLONASS Signal Plan (Navipedia, ESA)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: navigation-gnss-denied
source: https://gssc.esa.int/navipedia/index.php/GLONASS_Signal_Plan
tags: [drone, gnss, 1-신호]
authors: "ESA Navipedia"
published: "미확인"
---

## 핵심 내용
GLONASS의 FDMA 신호(L1, L2)와 CDMA 신호(L1OC, L2OC, L3OC) 주파수 체계를 정리한 문서. FDMA는 채널 번호 k에 따라 주파수가 달라지며, 현재 14개 주 채널(2개는 시험용)이 사용된다고 기술한다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- FDMA 기준: L1 f0=1602 MHz, 간격 562.5 kHz / L2 f0=1246 MHz, 간격 437.5 kHz / L3 f0=1201 MHz, 간격 437.5 kHz
- L1 범위(k=-7~+6): 1592.9525~1610.485 MHz
- CDMA 반송파: L1OC 1600.995 MHz, L2OC 1248.06 MHz, L3OC 1202.025 MHz (GLONASS-K1, fb=5.115 MHz)
- FDMA 구조라 수신기가 위성별 채널 보정을 해야 하므로 RTK 호환성은 수신기 사양 확인 필요(이 문서에는 언급 없음)

## 한계·미확인
RTK에서의 FDMA 처리 방법, 위성 수는 미확인.
