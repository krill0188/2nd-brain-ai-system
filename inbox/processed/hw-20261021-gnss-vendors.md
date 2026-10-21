---
title: "GNSS 제조사 조사 (2026-10-21)"
created: 2026-10-21
captured: 2026-10-21
type: vendor-list
domain: hardware
tags: [drone, hardware, gnss, vendors]
---

# GNSS 제조사 조사표

국가·본사는 이번에 연 공식 페이지에서 확인되지 않아 전부 "일반지식·미확인"으로 둔다(추정 표기 아님, 사실 확인 안 됨). 접근 구분: 성공=사양 확보, 부분=페이지는 열렸으나 사양 일부/전부 미확보, 실패=403·타임아웃 등.

| 제조사 | 국가·본사 | 공식 URL | 제품군 | 접근 | 드론용 | 제품 파일 수 |
|---|---|---|---|---|---|---|
| u-blox | 일반지식·미확인 | https://www.u-blox.com | ZED-X20P/X20D/F20P, NEO-F10N/F9P, MAX-M10S/F10S, SAM-M10Q | 성공(WebFetch는 Header overflow 오류, curl로 성공) | 일부(모듈 칩; 드론 FC 장착은 ARK/Holybro 등 완제품) | 8 |
| Septentrio | 일반지식·미확인 | https://www.septentrio.com | mosaic-X5, mosaic-G5 P1/P8 | 부분(직접 접속 403, web.archive.org 보관본으로 열람; datasheet PDF 미열람) | 일부(완제품 통해 드론 사용) | 3 |
| Unicore | 일반지식·미확인 | https://en.unicore.com | UM980, UM980C, UM982, UM960, UM981 | 성공 | 일부(UAV 용도 분류 존재) | 5 |
| Quectel | 일반지식·미확인 | https://www.quectel.com | LG290P, LC29H, LG580P | 성공(spec 탭 일부 미확보) | 미확인 | 3 |
| ARK Electronics | 일반지식·미확인 | https://arkelectron.com | ARK RTK GPS 계열, G5/X5/X20, SAM, TESEO, DAN | 성공 | 예(PX4/DroneCAN) | 14 |
| Holybro | 일반지식·미확인 | https://holybro.com | H-RTK F9P/mosaic-G5/UM982, DroneCAN, M10/M9N | 성공(상품 JSON 본문 사용) | 예 | 6 |
| CUAV | 일반지식·미확인 | https://www.cuav.net | C-RTK 2, C-RTK 9Ps | 부분(C-RTK 2는 ArduPilot 문서로 대체) | 예 | 2 |
| Matek Systems | 일반지식·미확인 | https://www.mateksys.com | M9N-5883, M10Q-5883 | 성공 | 예 | 2 |
| DJI | 일반지식·미확인 | https://www.dji.com/d-rtk-2 | D-RTK 2 (D-RTK 3는 URL 404) | 성공 | 예(지상 기준국) | 1 |
| Tersus GNSS | 일반지식·미확인 | https://www.tersus-gnss.com | BX50L-TAP, BX50M-TAP, MX206 | 부분(제품 소개만, datasheet 미열람) | UAV 측량 용도 일부 명시 | 3 |
| SIYI | 일반지식·미확인 | https://www.siyi.biz | UniGNSS M10, F9P RTK, M9N (메뉴 확인) | 부분(SPA 페이지라 사양 미확보) | 예 | 0 |
| Calian (Tallysman) | 일반지식·미확인 | https://www.tallysman.com | TW3972 등 GNSS 안테나 | 부분(페이지 열림, 사양은 JS 렌더링으로 미확보, Bright Data도 동일) | 일부 | 0 |
| Maxtena | 일반지식·미확인 | https://www.maxtena.com | 안테나 | 부분(홈 200, GNSS 제품 URL 미발견) | 미확인 | 0 |
| Swift Navigation | 일반지식·미확인 | https://www.swiftnav.com | Piksi Multi(URL은 홈으로 리다이렉트된 듯), Skylark 서비스 | 부분(제품 사양 없음) | 미확인 | 0 |
| Furuno | 일반지식·미확인 | https://www.furuno.com/en/products/gnss-module/ | GNSS 타이밍/차량용 모듈(백서: 재밍·스푸핑 대응) | 부분(목록만, 모델 사양 미확보) | 미확인 | 0 |
| Broadcom | 일반지식·미확인 | https://www.broadcom.com/products/wireless/gnss-gps-socs | GNSS SoC | 부분(내용 없음) | 미확인 | 0 |
| CHCNAV | 일반지식·미확인 | https://www.chcnav.com | 추정 URL 404 | 부분(홈만) | 미확인 | 0 |
| Allystar | 일반지식·미확인 | https://www.allystar.com | 미확인 | 부분(홈 200, 제품 페이지 502) | 미확인 | 0 |
| Emlid | 일반지식·미확인 | https://emlid.com | Reach M2/RS4 | 실패(emlid.com 403; docs.emlid.com은 열리나 사양 미확보) | 미확인 | 0 |
| ArduSimple | 일반지식·미확인 | https://www.ardusimple.com | simpleRTK 계열 | 실패(403) | 미확인 | 0 |
| NovAtel (Hexagon) | 일반지식·미확인 | https://novatel.com | OEM7 | 실패(403) | 미확인 | 0 |
| Hemisphere GNSS | 일반지식·미확인 | https://www.hemispheregnss.com | 미확인 | 실패(403) | 미확인 | 0 |
| Taoglas | 일반지식·미확인 | https://www.taoglas.com | 안테나 | 실패(403) | 미확인 | 0 |
| Antcom | 일반지식·미확인 | https://www.antcom.com | 안테나 | 실패(403) | 미확인 | 0 |
| STMicroelectronics (Teseo) | 일반지식·미확인 | https://www.st.com | Teseo | 실패(연결 불가) | 미확인(ARK TESEO GPS 제품이 LIV4F 사용 기재) | 0 |
| MediaTek | 일반지식·미확인 | https://www.mediatek.com | GNSS | 실패(404) | 미확인 | 0 |

미시도: Trimble, mRo, Maxtena 상세, 안티재밍 CRPA 전용 제조사.
