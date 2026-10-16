---
title: "제조사 레지스트리 INDEX"
created: 2026-10-17
captured: 2026-10-17
type: vendor-registry
domain: vendor-registry
tags: [drone, hardware, vendor, index]
---
# 제조사 레지스트리 INDEX (2026-10-17)

| 카테고리 | 파일 | 행 수 | 미확인/접근실패 행 수(근사) |
|---|---|---|---|
| battery | vendors-battery.md | 16 | 4 |
| camera | vendors-camera.md | 17 | 3 |
| compute | vendors-compute.md | 17 | 3 |
| datalink | vendors-datalink.md | 16 | 2 |
| esc | vendors-esc.md | 16 | 1 |
| fc | vendors-fc.md | 16 | 4 |
| frame | vendors-frame.md | 20 | 4 |
| gcs-hw | vendors-gcs-hw.md | 17 | 4 |
| gnss-imu | vendors-gnss-imu.md | 20 | 4 |
| lidar | vendors-lidar.md | 17 | 1 |
| motor | vendors-motor.md | 15 | 2 |
| payload-mech | vendors-payload-mech.md | 15 | 2 |
| power-charger | vendors-power-charger.md | 18 | 3 |
| propeller | vendors-propeller.md | 15 | 2 |
| radar | vendors-radar.md | 19 | 3 |
| 합계 | 15개 | 254 | 42 |

## 방법
- WebFetch로 각 제조사 공식 홈/제품 페이지를 열람해 페이지에 적힌 제품명만 기재. 국가/본사는 '(일반지식)' 표기 시 페이지 확인이 아님.
- 일부 행(MAD Components, Flyber, Lighter Propeller 등)은 제3자 디렉토리(WebSearch 결과) 기반으로 표시.

## 접근 실패/불가 사이트 (대표)
403: Autel, Quantum-Systems, Tarot(ECONNREFUSED), Gemfan, Sky-Drones, Flywoo, Foxtech, Embention, Septentrio, NovAtel, ArduSimple, Lightware, Iridium, Taoglas, HobbyKing, Basler, Skydroid(본문 없음)
DNS/인증서/404: Herelink.com(도메인 매각), Arbe.com(매각), Kokam(리다이렉트), Saft(인증서), Herewin, Revolectrix, Indemnis(404), Qualcomm drones(404), NXP radar(404), Orange Pi, xenics, InfiRay(인증서 만료), Dalprop(매각), MRC Systems, Drone Rescue Systems 등

## 신뢰도 낮은 항목
- 국가/본사 열 대부분은 일반 지식(페이지 미확인).
- payload-mech 카테고리는 공식 확인 제조사가 적음(검색 결과 기반 행 포함).
- 제품 라인이 칩/범용(LG ES, Samsung SDI, TI, Infineon, Getac 등)인 행은 드론 전용 여부 미확인.
- 수출통제/NDAA 비고는 페이지에 명시된 경우만 기재(Doodle Labs, ModalAI, ARK, Vantage Robotics, Freefly, Hylio, Mobilicom, Ouster, Teledyne FLIR Boson SX8). 그 외는 '미확인'.
