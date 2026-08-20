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
- [MATLAB] What Is Polyspace Bug Finder? (youtube.com, 2026-08-10) — https://www.youtube.com/watch?v=sYCQltmHn_g
- [밀덕텔링] 10억 짜리 자폭드론 ‘K-루카스’가 풀어야 할 진짜 숙제 (비즈한국, Fri, 07 Au) — https://news.google.com/rss/articles/CBMif0FVX3lxTFBISzhzcWVleV91NmlvVXJsUWp4Ylh5VFpwczhuYkZ4WVFublM5b3Bib1ZZNUo0ZUxUMTRZbnRadlhteXFsUno5ZTFBY3BLNl9Rb0lONWU0X1pIY0Y3N01CNzN6QzRwN2VsMWRnMFh2Mm9lVmtBSW56UlIxX3NWYzg?oc=5
- 니어스랩, 풍력 자율비행 기술 앞세워 글로벌 방산 드론시장 공략 (드론매거진 뉴스, Mon, 10 Au) — https://news.google.com/rss/articles/CBMiZEFVX3lxTE4yUUJOb2pHMDl3YVhWWnd0eWFHbURRSjJPb185Y2k1aWRGY2lPcnVIbktNVFZib2prM2NMemNNZ1NwX3l0aWxiSzItN1Q1WEpDQjBfX1Uzd2pEOFVvaEh0V3BtaUc?oc=5
- 치킨값 나오나?…'니어스랩' 청약, 오늘부터 (위키트리, Wed, 12 Au) — https://news.google.com/rss/articles/CBMiVkFVX3lxTFBsOWF3OXhGMUxZMkV1Ri1yOGlNdi1sSm5BUHk1UVpRY1FuNU1lLWFyZ3JjQVJnLXVlREdadkRrR205dC1iMkZGZG1VR0FUVWVUcTh5Tll3?oc=5
- 美 방산 드론 스타트업 네로스, 2억5천만 달러 투자 유치…기업가치 25억 달러로 급등 (드론매거진 뉴스, Thu, 13 Au) — https://news.google.com/rss/articles/CBMiZEFVX3lxTE9saWNpWW1BeHpxMTRPNEN3blZNcDM2UW9fM2I1NWp1ZG9iQkVCNlJfbnFEc3YyUzJQZ25PczhRRFhCUGRvN3hJdWc1VnBqUW5ncThob1JkdndxVFRoMlFsTkVMR1E?oc=5
- 이동 중에도 발사, 獨 라인메탈 자폭드론 FV-014 (데일리방산, Thu, 13 Au) — https://news.google.com/rss/articles/CBMicEFVX3lxTE9MMlpPY2dBSUZzWXZ2d0dTSTVQV3lDSXdqbHFpQU9SZllMRjUtdExORHhQV3AyZFhmZ1NRc1ZobjJTblEzd1VUNHpibUR2UGtHc1FXM2RMdExnUjQyNGZScmVUakRsRTNrT1M3akRlTTI?oc=5
- "AI·드론부터 핵심 부품까지"… 부산은행, 1125억 펀드로 동남권 방산 벤처 실탄 장전 (청년투데이, Thu, 13 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTFBqY0t2dWx1NXNBRERzdVNRaU0zMVJySFFnRXpMTlg5Y1puTVBPWl9faTk3NHVkZXh0T1pja3ZZRVhoX0MyQlljQzhoMzVkNDQzRkFBQnN3eS16SmhSWkhlckFDSVdYVDNwcUE?oc=5
- 美, 中 드론·배터리 밀어낸다…LG엔솔, 왜 방산 진출 얘기 나오나 (임팩트온, Wed, 19 Au) — https://news.google.com/rss/articles/CBMiaEFVX3lxTFBEVkxZUEtJZ0NBRWgwN2RUaXIzcGRueUViRFZ5R0JDMTNZZkhqdHZvTlhUaWx3MG9jVDJOeUNWTUpMUVJzZ1A5ZHJXZ1ZteHRWdzEwN1RiamtqX0hDcEoxLVNNZlFKZzZU0gFsQVVfeXFMTTh6X3pULTFlN2w2WE5IbmcySG5LdWc1cFhqUC0wMmpnb2lRLWxyZUdJbVBxUHZfbWRIY1poaGFqZWM3WHoxTFB5bWV0UG84N2p2dFZTUnVUOVpFbzFuNnRjSlV5NzV5ZE5hYzZV?oc=5
- 젤렌스키 체제에 첫 공개 도전…‘드론전 영웅’ 페도로우 “전시에도 대선” (문화일보, Wed, 19 Au) — https://news.google.com/rss/articles/CBMiUEFVX3lxTE5TcnFiZk9sXzFkcTQ3X1gwQXQwajFTc2VnWWRkM1ZLeXZIYjFGUTNDOUxFV2w3d0s5ZWNleVpTZjNsRTVTT3ZHb2JWaTd1djR6?oc=5
