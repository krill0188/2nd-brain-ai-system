---
title: "국토지리정보원 실시간 측위보정정보(네트워크 RTK) 계정 등록 절차 - 공식 안내문 3종"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ops-mission
ontology_class: PrecisePositioning
tags: [drone, gnss, ngii, network-rtk, ntrip, 신청절차, 공식]
sources: [inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
confidence: medium
contested: false
contradictions: []
---

# 국토지리정보원 실시간 측위보정정보(네트워크 RTK) 계정 등록 절차 - 공식 안내문 3종

- 원문: https://www.ngii.go.kr/other/file_down.do?sq=121897^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
- 저자: 국토지리정보원(NGII) 위치기준과 (안내문 PDF 3종)^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
- 발행: 계정등록 의무화 안내 2025-03-01 게시(시행일 2025-06-02 표기), 계정등록 방법 PDF(게시일 미확인), FAQ PDF(게시일 미확인), 열람 2026-10-22^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]

## 핵심 내용
NGII 공식 파일 다운로드(www.ngii.go.kr/other/file_down.do)의 PDF 3종(sq=117807 '계정 등록 의무화 안내', sq=121897 '측위보정정보 서비스 계정등록 방법', sq=118847 '계정 등록 의무화 관련 FAQ')에서 확인한 신청 절차. 확인 방법: curl로 직접 내려받아 Ghostscript로 텍스트 추출. 신뢰도: 높음(정부 1차). 20261021의 유통사 게시글(2차) 한계를 보완.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]

## 신청 절차 (공식 안내문 기준, 계정값은 기록하지 않음)
1. 국토지리정보원 홈페이지(https://ngii.go.kr) 접속 및 회원가입.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
2. 지각변동감시시스템(GNSS 서비스 포털, https://geodesy.ngii.go.kr) 접속 후 NGII 홈페이지 ID로 로그인.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
3. 검색/다운로드 > 마이페이지 > 통합회원연계 > 등록 > 계정생성.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
4. 한 번의 등록으로 3개 서비스(RTS1, RTS2, GNSS 데이터 통합센터) 계정이 동시에 생성됨. 한 명이 최대 100개까지 실시간 측위보정정보 서비스용 계정 생성 가능.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
5. 생성한 계정으로 각 서비스에 로그인해 보정정보 수신. 서버 주소: RTS1 = rts1.ngii.go.kr, RTS2 = rts2.ngii.go.kr, GNSS 데이터 통합센터 = www.gnssdata.or.kr.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
- 문의: 위치기준과 031-210-2656 등(공식 안내문 기재).^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]

## 정책 변경 사항 (공식)
- 계정 등록 의무화 안내문: 시행일 '25.6.2 09시, 시행 전 3개월(25.3.1~5.31) 미등록자 병행 운영. 변경 전/후 표: RTS2는 변경 전 '계정 없이 이용 가능'이었으나 변경 후 '계정 등록 필수'.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
- 주의: 시행일은 안내문 PDF에는 2025-06-02로 적혀 있으나, 유통사 블로그·공지(2차)에서는 2025-08-01로 연기되었다고 서술(공식 연기 공지는 이번에 못 찾음 → 실제 시행일 미확인).^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
- FAQ: 기존 RTS1 ID는 RTS1·RTS2 계정 정보가 연동되어 계속 사용 가능하나 GNSS 데이터 통합센터까지 쓰려면 통합회원 가입 권고. 하나의 계정으로 중복 접속 불가(단, 하나의 NGII ID로 여러 통합 ID 생성은 가능). 계정 등록은 국토정보플랫폼이 아니라 지각변동감시시스템에서만 가능하도록 일원화.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]
- 비밀번호 관련: 안내문·FAQ에 서비스별 공통 초기 비밀번호 규정이 적혀 있으나 값은 기록하지 않음.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]

## 한계·미확인
(1) 현재(2026-10) 시점 화면 기준 절차는 확인하지 못함: geodesy.ngii.go.kr 은 로그인형 SPA이고 로그인은 시도하지 않음. 국토정보플랫폼 위성기준점 서비스 페이지(map.ngii.go.kr)에 '2026년 7월 1일 기준으로 GNSS 서비스 포털 기능으로 통합' 공지가 있어 위 PDF의 메뉴 경로가 바뀌었을 수 있음. (2) 승인 소요 기간, 요금(무료 여부), 법인/개인 구분, 드론 상용 이용 제한 여부는 공식 문서에서 미확인. (3) PDF 3종의 게시일 중 2종은 미확인.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-account-registration-official-guide.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
