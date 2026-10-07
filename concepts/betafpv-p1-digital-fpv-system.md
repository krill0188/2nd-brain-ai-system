---
title: "BETAFPV P1 디지털 FPV 시스템 (베타 하드웨어)"
created: 2026-10-05
updated: 2026-10-07
type: concept
domain: hardware
tags: [drone, drone-hw, fpv, hardware]
sources: [inbox/processed/fetch-2026-10-05-yt-100-for-a-digital-hd-vrx-whats-the-catch-betafpv-p1-vrx-revi.md, inbox/processed/fetch-2026-10-07-yt-building-a-p1-whoop-to-find-out-how-much-slower-it-really-is.md]
confidence: low
contested: false
contradictions: []
---

# BETAFPV P1 디지털 FPV 시스템

Joshua Bardwell의 P1 vRX 리뷰(2026-10-04, 자막 앞부분 8000자 기준) 요약. 자막이 비행 테스트 도중에서 끊겨
최종 결론은 반영하지 않았다. 리뷰어는 제조사가 이 제품을 "베타 하드웨어·베타 펌웨어"로 명시했다고 강조한다.
^[inbox/processed/fetch-2026-10-05-yt-100-for-a-digital-hd-vrx-whats-the-catch-betafpv-p1-vrx-revi.md]

## 구성

- **고글용 모듈**: SkyOne용과 Fat Shark용 외형. 핀은 고정용일 뿐 전원·신호 경로가 아니다. 전원은 외부 케이블(내부 전원
  개조 절차는 있으나 개조 필요, 제조사는 최종판에서 내장 전원을 약속), 영상은 mini HDMI로 고글 HDMI 입력에 연결.
- **독립형 vRX**: 삼각대용 1/4-20, 2~6S DC/Type-C 입력, mini HDMI 출력. 화면 달린 독립 수신기도 있으며 2~6S(XT30/DC).
- **Matrix AIO 휘프 FC**: 2.4 GHz ExpressLRS 수신기와 P1 영상 송신기 내장. 이를 이용한 휘프는 17 g 미만.
- 가격(리뷰어 언급): 고글 약 $200 미만, vRX Pro $100, Nano $75(베타 가격, 정식 출시 시 상승 가능), 카메라+송신기 약 $40. FC는
  상품 페이지를 찾지 못함.

## 성능 관찰 (초기)

- 화질은 DJI만큼은 아니지만 가격 대비 양호하다는 평. 카메라 상하반전 설정은 기체가 아니라 지상국에 저장됨.
- 전방위 안테나로 장애물 뒤 비행에서도 신호가 유지됐고, 비트레이트가 떨어지면 끊김 대신 블록 노이즈가 생기는
  동작을 리뷰어가 선호했다. ELRS RSSI 표시 이상(10 mW)은 원인 미확인.
- 리뷰어는 HDZero 고글의 HDMI 입력 녹화 기능으로 메뉴를 촬영했다(P1 DVR은 메뉴·OSD 미기록).

## 추가 근거: P1 휘프 조립(2026-10-06)

Joshua Bardwell이 Matrix P1 AIO FC로 65 mm 휘프를 직접 조립한 영상(자막 앞부분 8000자 기준, 비행 결과 전에서 끊겨 속도 비교
결론은 없음).^[inbox/processed/fetch-2026-10-07-yt-building-a-p1-whoop-to-find-out-how-much-slower-it-really-is.md]

- **중량**: FC+카메라 8 g, 프레임 9 g, 캐노피 10 g, 모터 16 g(모터 4개 합계, 발언 기준) 등으로 배터리 제외 약 16~18 g 수준을 추정했다.
  디지털 영상 송신기 내장 기체로는 인상적이며, 가장 가벼운 아날로그 휘프(BetaFPV Air65류 16~17 g)와 비슷하다고 평했다.
- **모터**: WeBleed Gore 0702 28,500 KV 사용. 23,000~40,000 KV 보유분 중 "강력하되 극단적이지 않은" 값으로 골랐다.
- **커넥터 vs 직접 납땜**: 모터 플러그는 저항이 커 전압 손실이 있고 직접 납땜이 성능상 유리하다. 이번에는 영상 송신기·FC 시험이 목적이라
  플러그를 쓰고, 모터 교체를 쉽게 하려는 이유도 있다. 전류가 클수록 플러그 저항 영향이 커지므로 최고 KV를 피한 것이 유리하다고 설명했다.
- **조립 팁**: FC 화살표가 기수 방향(다르면 Betaflight에서 재매핑 가능). 모터 회전 방향을 미리 확인하지 않아 Betaflight에서 반전했다.
  카메라 고정 나사가 업틸트 각도를 정하며 중간 단계 구멍을 선택했다. 안테나는 영상용과 ELRS 제어용이 분리돼 있다.

## 관련 개념

- [[fpv-hardware]] — FPV 하드웨어 일반
- [[hdzero-goggle-2-scroll-fix]] — 비교 대상 디지털 FPV(HDZero) 고글
- [[betafpv-meteor65-pro-ii]] — 같은 제조사의 1S 휘프(Matrix FC 계열)
- [[elrs-41-release]] — 내장 수신기가 쓰는 ExpressLRS

## 📰 최근 관련 소식
- [Joshua Bardwell] $100 for a digital HD vRX. What's the catch? // BETAFPV P1 VRX REVIEW (youtube.com, 2026-10-04) — https://www.youtube.com/watch?v=5zjWdQfQGmE
- [Joshua Bardwell] Building a P1 whoop to find out how much slower it really is (youtube.com, 2026-10-06) — https://www.youtube.com/watch?v=ZrNlxbI4rlQ
