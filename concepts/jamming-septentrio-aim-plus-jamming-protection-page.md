---
title: "AIM+ GNSS jamming protection (Septentrio 기술 해설: 노치·광대역 완화)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
tags: [drone, gnss, aim-plus, septentrio]
sources: [inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]
confidence: medium
contested: false
contradictions: []
---

# AIM+ GNSS jamming protection (Septentrio 기술 해설: 노치·광대역 완화)

- 원문: https://www.septentrio.com/en/learn-more/advanced-positioning-technology/aim-gnss-jamming-protection^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]
- 저자: Septentrio (제조사 기술 해설, 개별 저자 없음)^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]
- 발행: 미확인(보관본 2026 스냅샷)^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]

## 핵심 내용
출처 유형: 제조사 기술 해설 페이지(Septentrio). septentrio.com 직접 접속은 403이라 web.archive.org 보관본(2026 스냅샷)으로 열람. 제조사 주장이며 독립 검증 아님.^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]

AIM+(Advanced Interference Monitoring and Mitigation)는 모든 Septentrio 수신기에 내장된 간섭 감시·완화 기능이라고 소개한다. 협대역 간섭은 최대 3개의 노치 필터(자동/수동)로 제거하고, 광대역 간섭(chirp 재머 포함)은 WBI(Wideband Interference) 완화로 줄인다고 설명한다. 웹 UI 스펙트럼 창에서 RF 스펙트럼을 보며 간섭 유형·원인을 분석할 수 있다. L2 대역은 아마추어 무선 때문에 협대역 간섭에 취약하다는 설명이 있다.^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 노치 필터 3개: 자동 모드는 간섭 구간을 자동 완화, 수동 모드는 중심 주파수와 대역폭을 지정(예: Notch1 을 1235 MHz 로 설정한 화면).^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]
- WBI 완화는 설정에서 'on' 으로 활성화(pulse blanking 보다 효과적이라는 제조사 주장).^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]
- 불법 chirp 재머는 약 400 m 반경에서 GNSS를 교란한다는 사진 설명(AIM+ 켠 경우/끈 경우 비교 이미지).^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]
- 스푸핑: Spirent GSS9000 신호생성기로 현실적 전력·실제 항법 데이터를 넣은 스푸핑도 'non-authentic' 로 식별했다고 주장.^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]
- 드론 설계 시사점: 위 기능은 수신기 설정이므로 FC 쪽에서 GNSS 품질 지표/스푸핑 플래그를 읽어 failsafe 에 쓸 수 있는지는 별도 확인 필요(이 페이지에 없음).^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]

## 한계·미확인
재밍 전력(dBm)별 억제 dB·정량 성능 수치 없음(웹 페이지 수준 해설). 공식 백서/기술문서 PDF 는 이번에 찾지 못함 — 검색 결과에 'free 20-page GNSS interference brochure' 가 있다는 언급만 있었고 열람하지 못함(가입 필요로 추정, 시도하지 않음).^[inbox/processed/hw-20261021-jamming-septentrio-aim-plus-jamming-protection-page.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
