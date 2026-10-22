---
title: "Septentrio mosaic-G5 P3 / P3H 공식 데이터시트 (789채널, 전력, 헤딩)"
created: 2026-10-23
captured: 2026-10-23
type: product
domain: hardware
category: gnss
manufacturer: Septentrio
source: https://raw.githubusercontent.com/sparkfun/SparkFun_GNSS_mosaic-G5_P3/main/docs/assets/component_documentation/Septentrio_mosaic-G5_P3_%26_P3H.pdf ; https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P3H ; https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P3
tags: [drone, hardware, gnss, septentrio, mosaic-g5, p3, p3h, datasheet]
---
# mosaic-G5 P3 / P3H 데이터시트

출처 유형: ① Septentrio 제조사 데이터시트 PDF(P3·P3H 합본)가 SparkFun 공식 GitHub 저장소 docs 에 동봉된 사본 ② septentrio.com 제품 페이지(Bright Data scrape_as_markdown 로 열람; 일반 curl 은 403). 확인 방법: PDF 는 curl 다운로드 후 Ghostscript 텍스트 추출, 제품 페이지는 본문 대조. 신뢰도: 높음(제조사 PDF 원본). 이전 시도에서 막힌 "P3/P3H 채널 수" 해결.

## 핵심 사양 (데이터시트에 적힌 값만)
| 항목 | 값 |
|---|---|
| 하드웨어 채널 | 789 hardware channels (P3·P3H 공통 기재) |
| 신호 | GPS L1C/A, L1C, L2C, L2PY, L5 / GLONASS L1CA, L2CA, L2P, L3 CDMA / BeiDou B1I, B1C, B2a, B2I, B2b, B3I / Galileo E1, E5a, E5b, E6 / QZSS L1C/A, L1C/B, L2C, L5, L6(L6는 소프트웨어 업데이트로 추가 예정 각주) |
| 밴드 | P3: quad-band, P3H: 단일안테나 quad-band / 이중안테나 triple-band (제품 페이지) |
| RTK 수평/수직 | 0.6 cm + 0.5 ppm / 1 cm + 1 ppm, 초기화 7 s (개활지, RMS, 기선 <40 km) |
| 기타 측위 | Standalone 1.2 m(수평)/1.9 m(수직), DGNSS 0.4 m/0.7 m |
| 속도 정확도 | 3 cm/s |
| 헤딩(P3H만) | 기선 1 m: 헤딩 0.15°, 피치/롤 0.25° / 5 m: 0.03°, 0.05° |
| 갱신율 | 위치 20 Hz, 측정치만(P3만) 20 Hz, 지연 <10 ms (99.9%) |
| 시간 | PPS 분해능 1.4 ns, 이벤트 정확도 <3 ns |
| 최초 측위 | 콜드 <35 s, 웜 <10 s, 재포착 1 s |
| 추적 임계 C/N0 | 추적 20 dB-Hz, 포착 30 dB-Hz |
| 전력 | P3 0.44 W typ / 0.57 W max, P3H(이중안테나) 0.6 W typ / 0.785 W max, 입력 3.3 VDC |
| 안테나 | 프리앰프 범위 15–50 dB(SA)/15–35 dB(DA), 바이어스 3.0–5.5 V, 전류제한 150 mA |
| 크기·무게 | 22.8 x 16.4 x 2.4 mm, 2.2 g, SMT 솔더형 LGA |
| 온도 | 동작 -40~85 C, 보관 -55~85 C, 습도 5~95% 비응축 |
| 진동 | IEC 60721-3-5 Profile 5M3, MIL-STD-810H 514.8 Cat.4, 516.8 Proc.I |
| 인터페이스 | UART 2(LVTTL, 최대 4 Mbps), USB 2.0 HS 1, GPIO 2, PPS out 2, Event marker 2 |
| 프로토콜 | SBF, NMEA 0183 v2.3/3.03/4.0, RTCM 3.x(MSM) 입력 |
| 인증 | CE, FCC, RoHS, WEEE, ISED |
| 기술 | AIM+, LOCK+, APME+, IONO+, RAIM+; Galileo HAS/OSNMA(소프트웨어 업데이트 예정 각주) |

## P3 대 P3H 차이
- P3: 전체 raw 측정치 출력(P3 only), 헤딩 없음. P3H: 헤딩 가능(이중안테나), raw 데이터 미제공(제품 페이지 문구상 "Full raw data" 는 P3 페이지에만 있음; ArduSimple 은 P3H 가 RAW 위성 데이터를 제공하지 않는다고 기재했다고 검색 요약에 나옴 = 2차, 미확인).
- 제품 페이지 펌웨어: P3H/P3 모두 Firmware v1.1.0, Hardware Manual v2.0.0 링크 존재(열람 시점 2026-10-23).

## 한계·미확인
- 데이터시트 PDF 의 발행일·개정 번호 미확인(텍스트 추출에서 날짜 못 찾음, 하단 저작권 연도는 추출 깨짐). 
- septentrio.com 의 공식 datasheet 다운로드(web.septentrio.com/l/... )는 Microsoft SharePoint 로그인으로 리다이렉트되어 열람 안 함(로그인 우회 금지). 
- 제품 페이지 "Show more specifications" 접힘 내용은 일부만 노출되어 PDF 값을 기준으로 함.
