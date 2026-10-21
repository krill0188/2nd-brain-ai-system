---
title: "드론 GNSS 수신기·모듈·안테나 제품 레지스트리"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: vendor-registry
tags: [drone, drone-hw, gnss, vendor-registry]
sources: [inbox/processed/hw-20261021-gnss-vendors.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 GNSS 수신기·모듈·안테나 제품 레지스트리

GNSS 제조사 공식 페이지에서 확인한 제품 74건의 요약표(수집 2026-10-21). 페이지에 없는 값은 '—'(미확인)이며 추정하지 않는다. 제조사 개요는 [[vendor-registry-gnss-imu]], GNSS 공학 자료는 [[gnss-engineering-hub]]를 본다.^[inbox/processed/hw-20261021-gnss-vendors.md]

| 제조사 | 제품 | 지원 위성군 | 주파수 대역 | 인터페이스 | RTK/PPK/PPP |
|---|---|---|---|---|---|
| Antcom (Hexagon) | Antcom 4NC-3.5CG1215P-XX-X-7.5EM GPS L1/L2 CRPA (FRPA footprint) | — | — | — | — |
| Antcom (Hexagon) | Antcom 4NF-5.5CGXX15P-XX-X Lightweight 4-element CRPA | — | — | — | — |
| Antcom (Hexagon) | Antcom 7NF-6.29CG1215P-6S-X 7-element CRPA with cable outputs | — | — | — | — |
| ArduSimple | ArduSimple simpleRTK2B Budget (u-blox ZED-F9P) | — | Multiband: L1, L2, E5b | JST-GH 6핀: 5V_IN / ZED-F9P UART1 RX / TX / 4,5 미연결 | — |
| ArduSimple | ArduSimple simpleRTK3B Compass (Unicore UM982, dual antenna heading) | — | Tripleband: L1, L2, L5 | JST-GH 6핀: 5V_IN / COM3 RX / COM3 TX / Timepulse / | — |
| ArduSimple | ArduSimple simpleRTK3B Pro (Septentrio mosaic-X5) | — | Tripleband: L1, L2, L5 | JST-GH 6핀: 5V_IN / COM3 RX / COM3 TX / Timepulse 출 | — |
| ArduSimple | ArduSimple simpleRTK 4 Optimum (u-blox ZED-X20P) | — | Allband: L1, L2, L5, L6 (Galileo HAS 지원 표기) | JST-GH 6핀: 5V_IN / UART1 RX / TX / Timepulse / Eve | — |
| ARK Electronics | ARK DAN GPS (u-blox DAN-F10N) | — | L1/L5/E5a/B2a | Pixhawk Standard UART/I2C Connector (6 Pin JST GH) | 미기재 |
| ARK Electronics | ARK G5 RTK Heading GPS (mosaic-G5 P3H) | multi-constellation, quad-band GNSS(단독), triple-band 듀얼안테나 헤 | quad-band / triple band(구체 미기재) | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | RTK 지원 |
| ARK Electronics | ARK G5 P6 RTK GPS (mosaic-G5 P6) | multi-constellation, multi-frequency tracking of all availab | multi-frequency(구체 미기재) | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | RTK, Galileo HAS corrections |
| ARK Electronics | ARK G5 P8 RTK GPS (mosaic-G5 P8) | multi-constellation, multi-frequency(구체 목록 미기재) | multi-frequency(구체 미기재) | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | RTK(페이지 'RTK Status' LED 표기) |
| ARK Electronics | ARK G5 RTK GPS (mosaic-G5 P3) | multi-constellation, quad-band GNSS 모듈(구체 위성군 목록 미기재; 'GPS/G | quad-band(구체 대역 미기재) | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | RTK 지원; Galileo HAS positioning service compatibility |
| ARK Electronics | ARK GPS (u-blox M9N) | 4 GNSS 동시 수신 (구체 위성군 미기재) | 미기재 | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH | 미지원/미기재 |
| ARK Electronics | ARK MOSAIC-X5 RTK GPS | — | L1 / L2 / L5 | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | RTK 지원(RTK Status LED) |
| ARK Electronics | ARK RTK Base (u-blox F9P) | GPS, GLONASS, Galileo, BeiDou 동시 수신 | 미기재 | USB-C; Pixhawk Standard UART (6 Pin JST GH); F9P U | RTK Fixed Base / Moving Base / Rover 가능 |
| ARK Electronics | ARK RTK GPS L1/L5 (ZED-F9P-15B) | GPS, GLONASS, Galileo, BeiDou 동시 수신 | L1/L5 | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | RTK; Moving Base 미지원 ('Does not Support Moving Base for Head |
| ARK Electronics | ARK RTK GPS (u-blox ZED-F9P, L1/L2) | GPS, GLONASS, Galileo, BeiDou 동시 수신 | L1/L2 (구체 신호명 미기재) | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | RTK; Moving Base for Heading 지원 |
| ARK Electronics | ARK SAM GPS Mini (u-blox SAM-M10Q) | 미기재 | 미기재 | Pixhawk Standard UART/I2C (6 Pin JST GH) | 미지원 |
| ARK Electronics | ARK SAM GPS (u-blox SAM-M10Q) | 미기재(SAM-M10Q: BeiDou, Galileo, GLONASS, GPS 는 u-blox 페이지 참조) | 미기재 | Pixhawk Standard UART/I2C (6 Pin JST GH) | 미지원 |
| ARK Electronics | ARK TESEO GPS (ST TESEO LIV4F) | GPS/Galileo/Glonass/BeiDou/QZSS 동시, IRNSS ready | L1/L5 | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | 미기재 |
| ARK Electronics | ARK X20 RTK GPS (u-blox ZED-X20P) | all-band all constellation(구체 목록 미기재) | all-band(구체 미기재) | Pixhawk Standard CAN x2 (DroneCAN), 4 Pin JST GH;  | RTK, PPP-RTK, PPP 알고리즘 |
| Beitian | Beitian BN-220 GPS / BN-880 GPS & Compass | GPS, GLONASS, Galileo, BeiDou, QZSS, SBAS | GPS L1, GLONASS L1, BeiDou B1, SBAS L1, Galileo E1 | — | — |
| CUAV | CUAV C-RTK 2 (PPK/RTK module) | GPS, GLONASS, Galileo, BeiDou (4 concurrent), QZSS, SBAS | GPS L1C/A, L2C; GLONASS L1OF, L2OF; Galileo E1B/C, E5b; BeiDou B1I, B2 | DroneCAN; USB Type-C (HS), F9P USB 1, F9P UART 1,  | RTK 및 PPK 지원(RAW 저장); PPK base로는 비권장 |
| CUAV | CUAV C-RTK 9Ps | 북두(BeiDou), 갈릴레오(Galileo), 글로나스(GLONASS), GPS (페이지 중국어 원문) | GPS L1C/A, L2C; GLONASS L1OF, L2OF; Galileo E1 B/C, E5b; BeiDou B1I, B | UART x 2, USB x 1, 안테나 MMCX x 1 | RTK 지원; PPK 불지원 (페이지 '不支持') |
| DJI | DJI D-RTK 2 High Precision GNSS Mobile Station | GPS, BeiDou, GLONASS, Galileo (11개 신호) | GPS L1 C/A, L2, L5; BeiDou B1, B2, B3; GLONASS F1, F2; Galileo E1, E5A | 데이터링크: OcuSync, Wi-Fi, LAN, 4G; 메모리 16 GB | RTK 지원(RTCM 2.X/3.X 차분 데이터); PPK/PPP 미확인 |
| Emlid | Emlid Reach M2 RTK GNSS Module for UAV & Drone Mapping | GPS/QZSS L1C/A, L2C; GLONASS L1OF, L2OF; BeiDou B1I, B2I; Ga | — | USB, UART, Event(카메라 핫슈 동기, 소개문에 microsecond 미만 해상 | RTK, PPK (페이지 소개문), 보정 입력 NTRIP·VRS·RTCM3 |
| Emlid | Emlid Reach RS4 multi-band RTK GNSS receiver | GPS L1C/A, L2C, L5; GLONASS L1OF, L2OF; Galileo E1-B/C, E5a, | — | RS-232, USB Type-C, LoRa 868/915 MHz(최대 1 W, 최대 8  | — |
| Harxon | Harxon HX-CUX012A Full-band low-profile embedded helix | — | — | — | — |
| Harxon | Harxon HX-HE202A L1/L5 embedded helix | — | — | — | — |
| Harxon | Harxon HX-HE205A L1/L2 dual-band embedded helix (D-QHA) | — | — | — | — |
| Harxon | Harxon HX-HE401A Full-band embedded helix (multi-point feed) | — | — | — | — |
| Harxon | Harxon HX-HE402A Full-band embedded helix (D-QHA) | — | — | — | — |
| Holybro | Holybro DroneCAN H-RTK F9P (Rover / Helical) | BeiDou, Galileo, GLONASS, GPS / QZSS | B1I, B2I, E1B/C, E5b, L1C/A, L1OF, L2C, L2OF | DroneCAN 1 Mbit/s (CAN 종단저항 소프트웨어 전환 지원); Helical은 | RTK 지원(PPK 미확인) |
| Holybro | Holybro H-RTK F9P Series (Rover / Helical / Base, IST8310) | GPS, GLONASS, BeiDou, Galileo | GPS L1C/A, L2C; GLONASS L1OF, L2OF; BeiDou B1, B2; Galileo E1-B/C, E5b | Rover: GH1.25 10pin 또는 6pin 케이블; Helical/Base: Por | RTK 지원; Moving Base RTK 5 Hz max(Helical/Base) |
| Holybro | Holybro H-RTK ZED-F9P Ultralight | GPS / QZSS, GLONASS, Galileo, BeiDou | L1C/A, L2C, L1OF, L2OF, E1B/C, E5b, B1I, B2I | UART (TX1/RX1, TX2/RX2), I2C; 38400-230400 bps (기본 | RTK 지원 |
| Holybro | Holybro H-RTK mosaic-G5 (Dual Antenna Heading) | GPS, GLONASS, Beidou, Galileo, QZSS | GPS: L1C/A, L1C, L2C, L2P(Y), L5; GLONASS: L1CA, L2CA, L2P, L3 CDMA; B | Port 1 USB Type-C; UART1 (GH1.25 10pin); UART2 (GH | RTK 지원(PPK/PPP 미확인) |
| Holybro | Holybro H-RTK Unicore UM982 (Dual Antenna Heading) | GPS, GLONASS, Beidou, Galileo, QZSS | BDS B1I/B2I/B3I; GPS L1C/A/L2P(Y)/L2C/L5; GLONASS L1/L2; Galileo E1/E5 | Port 1 GH1.25 10-pin; Port 2 USB Type-C; Port 3 UA | RTK 지원(PPK/PPP 미확인) |
| Holybro | Holybro M10 GPS / M9N GPS (V2, IP67 계열) | BeiDou, Galileo, GLONASS, GPS, QZSS (M10, M9N 공통) | GPS L1, Galileo E1, GLONASS L1, BeiDou B1, SBAS L1, QZSS L1 | UBX/NMEA 출력; 커넥터 JST-GH-10pin / JST-GH-6pin / Mole | 미지원 |
| Matek Systems | Matek GNSS & Compass M10Q-5883 (EOL 표기) | GPS, GLONASS, Galileo, BeiDou (u-blox M10 시리즈) | L1 GNSS 신호 | UART(TX, RX), I2C(DA, CL) 컴퍼스, JST-GH-6P, UART 기본  | 미지원 |
| Matek Systems | Matek GNSS & Compass M9N-5883 | GPS, GLONASS, Galileo, BeiDou (NEO-M9N) | — | UART(TX, RX) GNSS, I2C(DA, CL) 컴퍼스, JST-GH-6P, UAR | 미지원 |
| Maxtena | Maxtena M1227HCT-A2-SMA Rugged L1/L2 GPS GLONASS Active Antenna | — | — | — | — |
| NovAtel (Hexagon) | NovAtel (Hexagon) GAJT-310 anti-jam antenna | — | — | — | — |
| NovAtel (Hexagon) | NovAtel (Hexagon) GAJT-710ML anti-jam antenna | — | — | — | — |
| NovAtel (Hexagon) | NovAtel (Hexagon) GAJT-AE3 anti-jam antenna system | — | — | — | — |
| Quectel | Quectel LC29H series | GPS/QZSS, GLONASS, BDS, NavIC, Galileo | L1 및 L5 동시 수신 (dual-band) | — | Optional RTK; Optional integrated dead reckoning (DR) |
| Quectel | Quectel LG290P | GPS, GLONASS, Galileo, BDS, QZSS, NavIC (+SBAS: WAAS, EGNOS, | L1, L2, L5, E6 quad-band 동시 수신 | UART, I2C* | Quad-band RTK; RTK HOLD(RTK 보정 중단 시 최대 10분 고정밀 유지); PP-HAS E |
| Quectel | Quectel LG580P (03) | GPS, GLONASS, Galileo, BDS, QZSS, NavIC, SBAS | L1, L2, L5, L6 | UART, SPI*, I2C*, CAN* | 고정밀 RTK 계열 모듈(RTK 알고리즘 상세 미확인) |
| Septentrio | Septentrio mosaic-G5 P1 | GPS, GLONASS, BeiDou, Galileo, QZSS, SDCM(NavIC 미기재) | GPS L1C/A, L1PY, L2C, L2P(Y), L5; GLONASS L1CA, L2CA, L2P, L3 CDMA; Be | USB device (2.0 HS) 1, Event markers 2, PPS out 2 | — |
| Septentrio | Septentrio mosaic-G5 P8 | GPS, GLONASS, BeiDou, Galileo, QZSS, NavIC, SBAS(EGNOS, WAAS | GPS L1C/A, L1C, L1PY, L2C, L2P(Y), L5; GLONASS L1CA, L2CA, L2P, L3 CDM | USB device (2.0 HS) 1, Event markers 2, PPS out 1 | RTK 지원, Galileo HAS 지원 |
| Septentrio | Septentrio mosaic GNSS Module Hardware Manual v1.11.0 (mosaic-X5/T/H 공통 사양 보강) | — | — | — | — |
| Septentrio | Septentrio mosaic-X5 | GPS, GLONASS, BeiDou, Galileo, QZSS, NavIC, SBAS(Egnos, WAAS | GPS L1C/A, L1PY, L2C, L2P(Y), L5; GLONASS L1CA, L2CA, L2P, L3 CDMA; Be | USB device (2.0 HS) 1, Event markers 2, 설정 가능 PPS  | RTK 지원('RTK positioning at the lowest power consumption' 문구) |
| STMicroelectronics | STMicroelectronics Teseo-LIV4F tiny dual-band GNSS module | GPS/QZSS, Galileo, GLONASS, BeiDou (동시 멀티컨스텔레이션·멀티밴드), IRNSS | GPS/QZSS L1C/A·L5C, GLONASS L1OF, BeiDou B1i·B2a, Galileo E1·E5a | UART, I2C (NMEA 는 UART 와 I2C 모두 지원) | RTK 기준국 메시지(RTCM 1005/1006) 언급, 자체 RTK 솔루션 여부 미확인 |
| Swift Navigation | Swift Navigation Piksi Multi | GPS L1/L2, GLONASS G1/G2, BeiDou B1/B2, Galileo E1/E5b, SBAS | — | UART-LVTTL 2 (1 Mbps), CAN 2 (1 Mbps), Ethernet 10 | 초기화 시간 < 10 s, 신뢰도 > 99%, 솔루션 지연 < 30 ms |
| Tallysman (Calian) | Tallysman TW3972 Triple-Band GNSS Antenna + L-band | — | — | — | — |
| Taoglas | Taoglas MagmaX2 AA.205.151111 GNSS L1/L2/L5 External Magnetic Mount Antenna | — | — | — | — |
| Tersus GNSS | Tersus BX50L-TAP | GPS, GLONASS, Galileo, BeiDou, QZSS, SBAS, IRNSS | 'almost all frequencies' (구체 미기재) | COM, USB, CAN, PPS, event mark | RTK; TAP(위성 기반 PPP) 서비스 |
| Tersus GNSS | Tersus BX50M-TAP | GPS, GLONASS, Galileo, BeiDou, QZSS, SBAS, IRNSS | 'almost all frequencies' (구체 미기재) | COM, USB, CAN, PPS, event mark | RTK; TAP PPP |
| Tersus GNSS | Tersus MX206 Module | 모든 현행 GNSS 위성군(구체 미기재) | 'almost all frequencies' | 3 x UART, 2 x CAN, SPI Master/Slave, I2C, 2 x PPS, | PPP/RTK 듀얼모드 자동 전환; TAP PPP |
| u-blox | u-blox ANN-MB series (ANN-MB-00/01/02) L1/L2 multi-band GNSS antenna | — | — | — | — |
| u-blox | u-blox ANN-MB1 L1/L5 multi-band GNSS antenna | — | — | — | — |
| u-blox | u-blox ANN-MB5 L1/L5 multi-band standard precision GNSS antenna | — | — | — | — |
| u-blox | u-blox MAX-F10S | BeiDou, Galileo, GPS / QZSS, NavIC | — | UART, I2C | 미표기 |
| u-blox | u-blox MAX-M10S (MAX-M10 series 페이지) | BeiDou, Galileo, GLONASS, GPS / QZSS (변형에 따라 SBAS 포함) | L1 대역 위주(페이지 대역 항목 없음, 미확인) | UART, I2C | 미표기 |
| u-blox | u-blox NEO-F10N | BeiDou, Galileo, GPS / QZSS | B1C, B2a, E1B/C, E5a, L1C/A, L5 | UART | 미지원/미표기(Carrier phase output 항목 '-') |
| u-blox | u-blox NEO-F9P | GPS / QZSS, GLONASS, Galileo, BeiDou | L1C/A, L5, L1OF, E1B/C, E5a, B1I, B2a | UART x 2, USB, SPI, I2C | RTK rover, base station with survey-in |
| u-blox | u-blox SAM-M10Q | BeiDou, Galileo, GLONASS, GPS / QZSS | — | UART, I2C | 미표기 |
| u-blox | u-blox ZED-F20P | GPS, Galileo, BeiDou, GLONASS, NavIC, QZSS | L1C/A, L1C/B, L2C, L5, E1B/C, E5a, B1I, B1C, B2a, L1OF, L2OF | UART x 2, SPI, I2C | RTK rover, base station with survey-in; 'RTK and PPP-RTK sup |
| u-blox | u-blox ZED-X20D | GPS, Galileo, BeiDou, GLONASS, NavIC, QZSS | L1C/A, L1C/B, L2C, L5, L6, E1B/C, E5a, E6, B1I, B1C, B2a, B3I, L1OF, L | UART x 2, USB, SPI, I2C | RTK rover; RTK, PPP-RTK, PPP 언급 |
| u-blox | u-blox ZED-X20P | GPS, Galileo, BeiDou, GLONASS, NavIC, QZSS, SBAS | L1C/A, L1C/B, L2C, L5, L6, E1B/C, E5a, E6, B1I, B1C, B2a, B3I, L1OF, L | UART x 2, SPI, I2C | RTK rover, base station with survey-in; 페이지에 RTK/PPP-RTK/PPP |
| Unicore | Unicore UM960 | GPS, BDS, GLONASS, Galileo, QZSS, SBAS | GPS L1C/A, L2C, L2P, L5; BDS B1I, B3I, B1C, B2a, B2b; GLONASS G1, G2;  | 3 x UART (LVTTL), 1 x I2C* | RTK (RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm |
| Unicore | Unicore UM980 | GPS, BDS, GLONASS, Galileo, QZSS, NavIC, SBAS | GPS L1C/A, L1C, L2C, L2P(Y), L5; BDS B1I, B3I, B1C, B2a, B2b; GLONASS  | 3 x UART (LVTTL), 1 x SPI*, 1 x I2C*, 1 x CAN* (*특 | RTK (RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm; PPP(B2b-PPP,  |
| Unicore | Unicore UM980C | GPS, BDS, GLONASS, Galileo, QZSS, NavIC, SBAS, L-Band | GPS L1C/A, L1C, L2C, L2P(Y), L5; BDS B1I, B3I, B1C, B2a, B2b; GLONASS  | 3 x UART (LVTTL), 1 x SPI*, 1 x I2C*, 1 x CAN* | RTK (RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm |
| Unicore | Unicore UM981 (RTK/INS) | GPS, BDS, GLONASS, Galileo, QZSS, NavIC, SBAS | GPS L1C/A, L1C, L2C, L2P(Y), L5; BDS B1I, B3I, B1C, B2a, B2b; GLONASS  | 3 x UART (LVTTL), 1 x I2C*, 1 x SPI*, 1 x CAN* | RTK (RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm |
| Unicore | Unicore UM982 (듀얼안테나 포지셔닝·헤딩) | GPS, BDS, GLONASS, Galileo, QZSS, SBAS(주안테나) | 주안테나: GPS L1C/A, L2C, L2P(Y), L5; BDS B1I, B3I, B1C, B2a, B2b*; GLONAS | 3 x UART (LVTTL), 1 x SPI*, 1 x I2C*, 1 x CAN* | RTK (RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm |

제품별 원본 사양 기록은 inbox/processed/hw-20261021-product-gnss-*.md 에 있다.^[inbox/processed/hw-20261021-gnss-vendors.md]
