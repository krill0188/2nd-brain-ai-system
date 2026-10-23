---
title: "AIM+ Anti-Spoofing Protection (Septentrio 기술 해설)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
ontology_class: GNSSInterferenceSecurity
tags: [drone, gnss, aim-plus, osnma, septentrio]
sources: [inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]
confidence: medium
contested: false
contradictions: []
---

# AIM+ Anti-Spoofing Protection (Septentrio 기술 해설)

- 원문: https://www.septentrio.com/en/learn-more/advanced-positioning-technology/aim-spoofing-protection^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]
- 저자: Septentrio (제조사 기술 해설, 개별 저자 없음)^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]
- 발행: 미확인(보관본 2026 스냅샷)^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]

## 핵심 내용
출처 유형: 제조사 기술 해설 페이지(Septentrio). septentrio.com 직접 접속은 403이라 web.archive.org 보관본(2026 스냅샷)으로 열람. 제조사 주장이며 독립 검증 아님.^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]

스푸핑 종류(비동기·meaconing 재방송·동기/은폐형)를 구분하고, Septentrio 수신기의 대응을 (1) 실데이터로 조정한 무결성·이상 탐지 알고리즘, (2) 3대역 다성좌 기반 성좌 간 일관성 검사와 대체 신호, (3) 일부 신호의 암호 기반 인증(Galileo OSNMA 등), (4) 재밍 대응과의 결합으로 나열한다. 스푸핑은 보통 재밍과 함께 사용되어 대체 신호를 제거한다는 점을 강조한다.^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 스푸핑 방어는 GNSS 코어(수신기)에서 처리하는 것이 외부 센서보다 효과적이라는 제조사 주장.^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]
- 다중 주파수·다성좌 수신이 스푸핑 완화의 전제(신호 다양성).^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]
- OSNMA 는 meaconing 에는 속을 수 있어 이상탐지와 병행해야 한다는 JammerTest 글의 설명과 일치.^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]
- 드론에서는 스푸핑 플래그/인증 상태를 로그·failsafe 로 연계 설계할 필요(이 페이지는 연계 방법 미언급).^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]

## 한계·미확인
정량 탐지율·오탐률 수치는 이 페이지에 없음. 'ASP+' 라는 표기가 본문에 등장하나 AIM+ 와의 관계는 페이지에 명확히 정의되지 않음. 독립 검증 없음.^[inbox/processed/hw-20261021-spoofing-septentrio-aim-plus-spoofing-protection-page.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
