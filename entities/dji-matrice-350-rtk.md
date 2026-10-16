---
title: "DJI Matrice 350 RTK와 Zenmuse H30T 운용 사양·사례"
created: 2026-10-16
updated: 2026-10-16
type: entity
domain: hardware
tags: [drone, drone-hw, hardware, ops-mission]
sources: [inbox/processed/fetch-2026-10-16-hw-product-frame-dji-matrice-350-rtk.md, inbox/processed/fetch-2026-10-16-hw-product-payload-dji-zenmuse-h30t.md, inbox/processed/fetch-2026-10-16-hw-case-recon-devon-cornwall-m350-boardmasters-2024.md]
confidence: medium
contested: false
contradictions: []
---

# DJI Matrice 350 RTK + Zenmuse H30T

DJI 산업용 중형 플랫폼(9.2 kg급)과 멀티센서 페이로드 조합이다. 사양은 DJI 공식 spec 페이지, 운용 사례는 DJI 고객 사례(제조사 게재)에 근거하므로 성과는 홍보 성격임을 감안한다.

## 기체 (공식 spec 페이지)
- 최대 이륙중량 9.2 kg, 배터리 제외 약 3.77 kg / TB65 2개 포함 약 6.47 kg. 대각 휠베이스 895 mm.^[inbox/processed/fetch-2026-10-16-hw-product-frame-dji-matrice-350-rtk.md]
- 최대 비행시간 55분(무풍·무페이로드·약 8 m/s, 참고용), 최대 수평속도 23 m/s, 풍속 저항 12 m/s, IP55, -20~50 °C.
- 배터리 TB65: 5880 mAh, 44.76 V, 263.2 Wh, 약 1.35 kg. 최대 페이로드 960 g은 단일 짐벌 댐퍼 기준이며 구성에 따라 달라진다(검색 요약의 2.7 kg과 상이).

## 페이로드 Zenmuse H30T
- 줌 40 MP(최대 400x), 와이드 48 MP, 열화상 VOx 1280x1024, 레이저 거리계 905 nm 3~3000 m. 무게 920 g은 H30 시리즈 공통 표기로 H30T 단독 값은 미확인.^[inbox/processed/fetch-2026-10-16-hw-product-payload-dji-zenmuse-h30t.md]
- 호환 기체: Matrice 400 / 350 RTK / 300 RTK. 인터페이스 DJI SKYPORT, DJI Pilot 2.

## 운용 사례: Devon and Cornwall 경찰 (Boardmasters 2024)
- 최대 6만 명 규모 페스티벌에서 실시간 영상 송출, 교통·군중·사고 감시, 지상 부대 유도, 야간 열화상 감시에 사용했다.^[inbox/processed/fetch-2026-10-16-hw-case-recon-devon-cornwall-m350-boardmasters-2024.md]
- 정량 성과(사건 건수, 대응 시간)는 공개되지 않았고 비행 시간·횟수도 미확인이다.

관련: [[dji-enterprise]], [[drone-payload-systems]], [[drone-first-responder-dfr]], [[drone-payload-datalink-product-specs-catalog]].
