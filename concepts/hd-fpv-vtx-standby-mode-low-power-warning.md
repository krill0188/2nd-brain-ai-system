---
title: "HD FPV VTX의 Standby Mode와 저전력 경고 해결"
created: 2026-10-28
updated: 2026-10-28
type: concept
domain: hardware
tags: [fpv, drone-hw]
sources: [inbox/processed/fetch-2026-10-28-yt-fix-lowstandby-power-warning-in-your-hd-fpv-goggles-walksnai.md]
confidence: low
contested: false
contradictions: []
---

# HD FPV VTX Standby Mode (Painless360, 2026-10-27)

Walksnail 고글(Walksnail X) 기준 설명이며, 영상은 같은 현상이 DJI 등 다른 HD FPV 시스템에도 공통이라고 말한다(DJI는 확신하지 못한다는 단서 포함). 내용은 자막에만 근거한다.^[inbox/processed/fetch-2026-10-28-yt-fix-lowstandby-power-warning-in-your-hd-fpv-goggles-walksnai.md]

## 증상과 원인
- 연결 직후 화면(OSD 포함)에 low power mode 경고가 뜬다. VTX(기체 쪽 송신기)가 과열되지 않도록 초기에는 저출력으로 동작하게 한 설계다.
- 비행 컨트롤러를 OSD·텔레메트리 연결로 쓰면 FC가 **arm** 될 때 그 신호가 VTX에 전달되어 설정 출력으로 올라가고, 자동 녹화 설정도 그때 시작된다.
- FC 없이(OSD·텔레메트리 미연결) 쓰면 VTX가 armed 신호를 받지 못해 저출력에 머문다. 그 결과 도달 거리가 수백 m~km가 아니라 수 m 수준에 그친다.

## 해결
에어유닛과 연결된 상태에서 고글 메뉴 **settings → standby mode**를 끈다. 켜져 있으면 VTX가 저출력으로 시작해 arm 시 풀파워가 되고, 끄면 전원이 들어오자마자 고글에 설정한 출력 레벨로 동작한다.

## 관련 문서
[[betafpv-p1-digital-fpv-system]], [[hdzero-goggle-2-scroll-fix]], [[betaflight]]

## 📰 최근 관련 소식
- [Painless360] Fix Low/Standby Power Warning in Your HD FPV Goggles (Walksnail, DJI , HDZero etc.) (youtube.com, 2026-10-27) — https://www.youtube.com/watch?v=4nEbpeUawpk
