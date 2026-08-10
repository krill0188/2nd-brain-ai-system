---
title: "6G ISAC: MATLAB/USRP 기반 구현"
created: 2026-08-04
updated: 2026-08-04
type: concept
tags: [datalink, 6g, isac, simulation]
domain: comms-protocol
sources: [inbox/fetch-2026-08-04-yt-6g-isac-implementation-with-matlab-and-usrp.md]
confidence: high
contested: false
contradictions: []
---

# 6G ISAC: MATLAB/USRP 기반 구현

통합 감지 및 통신(Integrated Sensing and Communication, ISAC)은 6G의 핵심 기술로, 단일 파형으로 데이터 전송과 레이더 감지를 동시에 수행한다.

## 구현 환경

- **도구**: MATLAB, Simulink, Wireless Testbench
- **하드웨어**: NI USRP FPGA
- **파형**: 6G 후보 OFDM 파형 (100MHz 대역폭)

## 핵심 기술

### 타겟 에뮬레이터
- 설정 가능한 지연, 도플러 시프트, 이득 적용
- 이동하는 표적을 나타내는 현실적인 레이더 반사 생성
- 하드웨어 인더 루프(HIL) 환경에서 반복 가능한 테스트 제공

### 채널 추정
- 통신 및 감지를 위한 채널 추정
- 100MHz 대역폭에서의 성능 검증

## 관련 개념

- [[datalink-communication]] — 드론 데이터링크 통신
- [[uav-isac-cross-region]] — UAV ISAC 교차 지역 협력

## 📰 최근 관련 소식
- [MATLAB] 6G ISAC Implementation with MATLAB and USRP (youtube.com, 2026-08-03) — https://www.youtube.com/watch?v=20bb37XtbIk
- [화보] 이제 ‘드론’으로 배송을 (kyeongin.com, Tue, 04 Au) — https://news.google.com/rss/articles/CBMiUkFVX3lxTE9ZZlZYUHF4WEZLSFZUQUtjVGs2dWp5cmh5WVR6LVdrNlctYm5oOVlEU2YxOUtnVXFGZUFaRnY4TlFLS3BxN3daTmZZUFRELXJlVWc?oc=5
- 수원 광교호수공원·광교저수지 일대선 ‘드론’으로 간식 배달받는다 (프레시안, Wed, 05 Au) — https://news.google.com/rss/articles/CBMia0FVX3lxTE00LVhCQkZ2UFNCWUl5cEVHbndNTVV6bWsyckozM25wMy1IM2NhVUFzaGN1QVY0dVF3VkVJVHNMa2UwM25VM3h5ZUpTWmFVSmtKbVBET0NUT1NjcFBqVHJCWm1jclZOeF84MnM0?oc=5
- 2.5㎞ 날아 목표물 명중…美 해병대, 한반도 첫 자폭드론 실사격 공개 (newsis.com, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiYEFVX3lxTE9wcjNDZzBqZ1JWa1d1UmNWQkVCNUo4YTRCaHh0Z2ZvT2NIQ1hxYWh6bTZPYlRScDJyUXF2UDgtY2t4Tm41U1d0SWVDdmZrSEQwRnNIeVlMTGxSMGpxWjlpatIBeEFVX3lxTE9Qb1NHdEVnaWQwZC1PMjNoOFc5N1BUN3c5V0RoZGlBbzRfRGhPb3NnYThvUnhEU0NsV3A5UFlJNWMyb2dRNXlzbTBjQUk0MUVWTW9Qa0FwRDdnUnpWV00xOGdjU3Jsd3BIRldKY19fVEJpdG5NSlNJTA?oc=5
- 美 해병대, 한국서 첫 자폭드론 실사격훈련…2.5㎞ 날아 목표물 명중[이현호의 밀리터리!톡] (sedaily.com, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiUkFVX3lxTE16dFloM1ZKa0lzQW1PTUZXUG5Fam1UWFhEN2V3eGZ1dWFnNWRJMWg0Sld4T1N5RVJaeGhxLW0yZjluMzVIVFAtNGRXYU4weVB3akHSAVNBVV95cUxON1pudENjWVNXMXhRZmo0TDhmMjdrV3IwdHBIeHQtS3BRaFlEcFhCdzdNSU0xaS1ERi1xZUkwd3JlSHdsQ0tFT2xPYkhhUjF4S0J0VQ?oc=5
- 미, 한반도서 자폭드론 첫 훈련...한국 배치 가능성도? (YTN 사이언스, Fri, 07 Au) — https://news.google.com/rss/articles/CBMijAFBVV95cUxPbmpqM3hNZTZIbjM3VE9pWGl4T1FhbXRoRlF5QXdnSlRrYkhTemJ0MXFzZTRfTHpjaXp6UnpXMENYcEhlSS1pNDQycGZiMTJnZlkwNDVGRWpkR2NDVElQaXM2cjgwU3pKQldpT25Qb0E5ejg5cXZDcWVnTlZsX2tqVzJSV2xwRV9DTDF2Uw?oc=5
