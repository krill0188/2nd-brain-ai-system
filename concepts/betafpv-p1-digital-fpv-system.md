---
title: "BETAFPV P1 디지털 FPV 시스템 (베타 하드웨어)"
created: 2026-10-05
updated: 2026-10-24
type: concept
domain: hardware
tags: [drone, drone-hw, fpv, hardware]
sources: [inbox/processed/fetch-2026-10-05-yt-100-for-a-digital-hd-vrx-whats-the-catch-betafpv-p1-vrx-revi.md, inbox/processed/fetch-2026-10-07-yt-building-a-p1-whoop-to-find-out-how-much-slower-it-really-is.md, inbox/processed/fetch-2026-10-24-yt-betafpv-gets-serious-about-artlynk-with-new-hd-fpv-hardware.md]
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

## 추가 근거: ArtLynk 신제품 라인업(2026-10-23)

Painless360의 신제품 소개 영상(자막 기준). 리뷰어는 "빅3(DJI·Walksnail·HDZero)가 아닌 시스템은 꾸준한 신제품이 사용자 신뢰의 조건"이라며,
BetaFPV가 이 시스템에 크게 투자하고 있다고 평가했다. BetaFPV는 약 10~11개월간 HD 제품을 내왔고 아날로그 → ArtLynk 기반 HD 순으로 확장했다.
^[inbox/processed/fetch-2026-10-24-yt-betafpv-gets-serious-about-artlynk-with-new-hd-fpv-hardware.md]

- **P1 HD VTX 올인원 휘프 FC(1S)**: FC+ESC+VTX 일체형. ESC 12 A 연속, DShot 300/600, ExpressLRS 수신기 내장, VTX P1A 최대 200 mW,
  지연 약 60 ms(리뷰어가 ArtLynk의 약점으로 지적), 1080p 60fps, 카메라 FOV 153°(16:9). 모터 커넥터 JST 1.25 3핀, 전원 BT2.0, 무게 약 4.6 g.
  같은 JST 모터 커넥터를 쓰는 기존 휘프의 메인보드를 교체하는 용도.
- **HD FPV 모니터**: 밝기 1,000 nit, 안테나 2개, 하단 1/4인치 마운트, 외부 배터리 전원. 고글 없이 쓰거나 시선 비행 보조용.
- **P1 VTX Nano 수신기(고글 모듈)**: Fat Shark용·Skyzone용 두 버전. 고글 HDMI 입력으로 1080p 60fps, 다중 주파수·밴드, SD 카드 녹화, 범위는 약 400 m 이상.
  리뷰어는 고글 내부 개조가 필요해 본인은 쓰지 못하며, 외부 전원 독립형이 더 나았을 것이라 평했다.

## 관련 개념

- [[fpv-hardware]] — FPV 하드웨어 일반
- [[hdzero-goggle-2-scroll-fix]] — 비교 대상 디지털 FPV(HDZero) 고글
- [[betafpv-meteor65-pro-ii]] — 같은 제조사의 1S 휘프(Matrix FC 계열)
- [[elrs-41-release]] — 내장 수신기가 쓰는 ExpressLRS

## 📰 최근 관련 소식
- [Joshua Bardwell] $100 for a digital HD vRX. What's the catch? // BETAFPV P1 VRX REVIEW (youtube.com, 2026-10-04) — https://www.youtube.com/watch?v=5zjWdQfQGmE
- [Joshua Bardwell] Building a P1 whoop to find out how much slower it really is (youtube.com, 2026-10-06) — https://www.youtube.com/watch?v=ZrNlxbI4rlQ
- [Painless360] BetaFPV gets serious about ArtLynk with new HD FPV hardware (youtube.com, 2026-10-23) — https://www.youtube.com/watch?v=Xs2nlZzw-yQ
- [Painless360] CaddxFPV Ratel Ultra Analogue FPV Camera: What is it like to fly? (youtube.com, 2026-10-24) — https://www.youtube.com/watch?v=q7u32D_vS0U
