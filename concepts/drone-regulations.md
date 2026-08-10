---
title: Drone Regulations
created: 2026-07-27
updated: 2026-08-09
type: concept
tags: [drone, regulations, UAS, FAA, EASA, BVLOS, compliance]
sources: []
confidence: medium
domain: regulations
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# Drone Regulations

드론 규제는 안전한 공역 운용을 위해 국가/지역별로 시행되는 법적 프레임워크다. FAA(미국), EASA(유럽), 국토교통부(한국) 등 각국 기관이 관리한다.

## 규제 프레임워크

### 국제 기구

| 기구 | 지역 | 역할 |
|------|------|------|
| **ICAO** | 국제 | 국제민간항공기구, 표준 권고 |
| **FAA** | 미국 | Federal Aviation Administration |
| **EASA** | 유럽 | European Union Aviation Safety Agency |
| **CAA** | 영국 | Civil Aviation Authority |
| **국토교통부** | 한국 | 한국교통안전공단 |

## FAA Part 107 (미국)

상업용 드론 운용을 위한 규정.

### 요구사항

| 항목 | 요구사항 |
|------|----------|
| **Remote Pilot Certificate** | FAA 인증 시험 통과 |
| **Age** | 16세 이상 |
| **English** | 영어 능통 |
| **TSA Check** | 보안 심사 |

### 운용 제한

| 제한 | 규정 |
|------|------|
| **고도** | 400ft AGL 이하 |
| **속도** | 100mph 이하 |
| **시야** | VLOS (Visual Line of Sight) |
| **시간** | 일출~일몰 |
| **인원** | 조종자 1명 |

### Part 107 vs Part 91

| 규정 | 용도 |
|------|------|
| **Part 107** | 상업용 드론 (<55lbs) |
| **Part 91** | 일반 항공 |
| **Part 135** | 공중 택시/화물 |

## EASA (유럽)

### 드론 분류

| 클래스 | 무게 | 요구사항 |
|--------|------|----------|
| **C0** | <250g | 등록 불필요 |
| **C1** | <900g | A1 개방 카테고리 |
| **C2** | <4kg | A2 개방 카테고리 |
| **C3/C4** | <25kg | A3 특정 카테고리 |

### 운용 카테고리

| 카테고리 | 설명 |
|----------|------|
| **Open** | 저위험, 간소화 규정 |
| **Specific** | 중위험, 위험 평가 필요 |
| **Certified** | 고위험, 항공기급 인증 |

## 한국 규제

### 드론법 주요 내용

| 항목 | 규정 |
|------|------|
| **등록** | 250g 이상 의무 등록 |
| **조종자격** | 1종/2종/3종 구분 |
| **금지구역** | 군사시설, 공항 주변 |
| **비행허가** | 150m 이상 또는 특수비행 |

### 조종 자격

| 종류 | 운용 범위 | 시험 |
|------|-----------|------|
| **1종** | 25kg 이하 | 필기 + 실기 |
| **2종** | 7kg 이하 | 필기 + 실기 |
| **3종** | 2kg 이하 | 온라인 교육 |

## BVLOS (Beyond Visual Line of Sight)

시야 밖 비행을 위한 특별 인증.

### 요구사항

| 항목 | 설명 |
|------|------|
| **DAA** | Detect and Avoid (충돌 회피) |
| **C2 Link** | 신뢰성 있는 조종 링크 |
| **Geo-awareness** | 공역 인식 시스템 |
| **Contingency** | 비상 대응 계획 |

### 인증 유형

| 유형 | 설명 |
|------|------|
| **SAIL I/II** | 저위험 BVLOS |
| **SAIL III/IV** | 중위험 BVLOS |
| **SAIL V/VI** | 고위험 BVLOS |

## Remote ID

드론 식별을 위한 원격 신원 확인 시스템.

### FAA Remote ID

| 유형 | 설명 |
|------|------|
| **Standard** | 내장 Remote ID |
| **Broadcast Module** | 외장 모듈 |
| **FRIA** | FAA 인식 식별 영역 |

### 전송 정보

- 드론 ID
- 위치 (위도/경도/고도)
- 속도
- 조종자 위치
- 타임스탬프

## 항공 교통 관리

### UTM (UAS Traffic Management)

| 시스템 | 설명 |
|--------|------|
| **LAANC** | Low Altitude Authorization |
| **USSP** | UAS Service Provider |
| **FIMS** | FAA UTM System |

### 공역 분류

| 공역 | 설명 |
|------|------|
| **Class G** | 비관제 공역 (<1200ft) |
| **Class E** | 비관제 (IFR 분리) |
| **Class B/C/D** | 관제 공역 |
| **Restricted** | 금지/제한 공역 |

## 규제 준수 체크리스트

### 운용 전

- [ ] 드론 등록 확인
- [ ] 조종 자격 확인
- [ ] 보험 가입
- [ ] 공역 확인
- [ ] NOTAM 확인

### 운용 중

- [ ] VLOS 유지
- [ ] 고도 제한 준수
- [ ] 인원/재산 안전
- [ ] 프라이버시 보호

## 관련 개념

- [[drone-safety-failsafe]] — 안전 시스템
- [[datalink-communication]] — C2 링크 규제
- [[swarm-coordination]] — 군집 비행 규제

## 세부 규제 사례

- [[faa-deter-program]] — FAA DETER 프로그램(공항 대응 드론 탐지)
- [[faa-uas-environmental-assessment]] — FAA UAS 환경영향평가
- [[uk-caa-bvlos-scale]] — 영국 CAA BVLOS 대규모 운용 규정
- [[us-dod-cuas-marketplace]] — 미국 국방부 C-UAS 마켓플레이스
- [[china-drone-export-controls]] — 중국 대미 드론·부품 수출 통제
- [[faa-249-gram-registration-rule]] — FAA 249그램 드론 등록 규정

## 수집 대상

- 각국 최신 규제 업데이트
- BVLOS 인증 사례 연구
- UTM 시스템 기술 표준

## 📰 최근 관련 소식
- 폭발물 싣고 독일 공항 날아든 드론···경찰 “기폭 장치 제거” (경향신문, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiWkFVX3lxTE1WS0FOM3RRX2JDNEZWTXpCc2lMMDFCaVJ1NmlVOFQ0NXBSZ1M2Q3B1TVlPYy1SMUxPMC0wTThVX01rd2dnQlA5N2o5TTlyNlY1bFF2OEoyTE13UdIBX0FVX3lxTE12bng0UngtcWxZNTRDLWlMWGlVRzFhblk5cDNtcnVzUGg5QmdCNGgxYzFHRm05V0RCRmcxV3JtbDE5bmRBOHN1elp1TEtJRkdvaUxaMF81aHZZYnBTbXJ3?oc=5
- '물류 난타전' 우크라 방공망 구멍...독 공항, 폭발물 드론에 비상 (YTN 사이언스, Thu, 06 Au) — https://news.google.com/rss/articles/CBMijAFBVV95cUxNLTVDRWI5UWoyVDA2ZzBPTjNxZUxaNHZLWnVWOHdjd0VtSDU2YlU0SS1Sd182cFpIMllmeXdZWWRLRFJqalE4dU4zYjJ5UnFlNUIyb0VYdEJkVnR1WHppSy1udkEwZUV0dk1ZUkxTSmhuMlg3Ui11UVN5RnotQ29TRExJVFNJd0pCcXkxSA?oc=5
- "美 정보기관, 독일 공항 폭발드론 러시아 소유 가능성 제기" (연합뉴스, Sat, 08 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE1rUGYybHdOX1ZOWXE0czNrQkdGQ2RXc0ZJek9KSVpQaWV5MXdyYl92ZS1jaEY1M3VYNk1xMEQzazBPcXlqaEtPb0lyYnVJWHBlMW9hdHVvRmtOMGfSAWBBVV95cUxQNzJBcEcybmpXRnVqT2NXeGhHdFVlWXBkdnM3cjk0UXlWbEx2YWE2Zm9IdllSbEdoNDdXd0ctQUFadGVkYVdySmJZSmVTLTJDU2x5a3I3ZEJUS1liYXZhUWc?oc=5
- '폭발물 드론' 공항 출몰에 비상 걸린 독일, 드론 연구 확대 (연합뉴스, Sun, 09 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE83cmdnQ2dUSjdJMWZoX09OSnB5RXNqck1yOTc1NDUxTDluUXhqMUFtalRGdmdfLTV3Ukd0VUZRWG9lY1ROR2gwdWJtMFF5THFiYmFkeDJEOFdUSG_SAWBBVV95cUxPU05qa1JkSjBQcnlzWGg1SlpuaHQ4bEdkenp2UzYtalktdF9FWFg2LWk3N3h6VC1CdUJkeG1ocU5waURXYnZPa1plSXZOT0NndXpNMnB2OWR1X1IyMXN0R1Y?oc=5
