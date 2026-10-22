---
title: "국토지리정보원 네트워크 RTK·SSR·G-VRS — 드론 사용 문구, 신청 방식, 요금/승인 기간 재확인 (2026-10-24)"
created: 2026-10-24
updated: 2026-10-24
type: concept
domain: ops-mission
tags: [drone, gnss, ngii, network-rtk, ssr, g-vrs, 신청절차]
sources: [inbox/processed/hw-20261024-korea-ngii-network-rtk-g-vrs-drone-access-recheck-2026-10-24.md]
confidence: medium
contested: false
contradictions: []
---

# 국토지리정보원 네트워크 RTK·SSR·G-VRS — 드론 사용 문구, 신청 방식, 요금/승인 기간 재확인 (2026-10-24)

- 원문: https://map.ngii.go.kr/ms/mesrInfo/gnss/vrsUserView.do ; https://www.ngii.go.kr/other/file_down.do?sq=117807 (sq=121897, sq=118847) ; https://geodesy.ngii.go.kr/ (공개 JS) ; 보도 재전재: https://www.hellot.net/news/article.html?no=105917 , https://www.ebn.co.kr/news/articleView.html?idxno=1680654 , https://www.koreatimenews.com/news/article.html?no=951902^[inbox/processed/hw-20261024-korea-ngii-network-rtk-g-vrs-drone-access-recheck-2026-10-24.md]

## 핵심 내용
확인 방법: curl(브라우저 UA)로 NGII 공식 페이지·PDF 3종 재열람 + geodesy 포털 공개 JS 문자열 확인 + 보도 3건 열람. 계정값·비밀번호는 기록하지 않음.^[inbox/processed/hw-20261024-korea-ngii-network-rtk-g-vrs-drone-access-recheck-2026-10-24.md]
| 항목 | 확인 결과 | 근거·신뢰도 |
|---|---|---|
| 드론 사용 | 공식 페이지: SSR 서비스(RTS2, 마운트포인트 SSR-SSRG)는 "드론·차량 등 이동체 측위 및 SSR 수신가능 저가형 수신기 전용". VRS/FKP 는 측량 용도 구분이며 드론 사용 가능/불가를 명시한 문구는 찾지 못함 | map.ngii.go.kr 공식, 높음 |
| 2026-07 통합 | 같은 공식 페이지 상단: "본 서비스는 2026년 7월 1일 기준으로 [GNSS 서비스 포털 누리집] 기능으로 통합됩니다." 즉 국토정보플랫폼 위성기준점 서비스는 geodesy.ngii.go.kr 포털로 이전 | 공식, 높음 |
| 통합 후 메뉴 경로 | geodesy.ngii.go.kr 은 Next.js SPA. 공개 JS 에서 확인된 것은 "로그인", "마이페이지"(경로 /portal/main?pageType=application), "공지사항", "Q&A", 접속 현황 대시보드뿐. 계정 생성의 정확한 메뉴(2025 PDF: 마이페이지 > 통합회원연계 > 등록 > 계정생성)가 2026-07 이후에도 동일한지는 로그인 필요라 미확인 | JS 문자열 확인, 중간 |
| 신청 방식 | 공식 PDF 3종(계정 등록 방법·의무화·FAQ): NGII 회원가입 후 포털에서 계정 생성, 1인 최대 100개, 등록 즉시 RTS1·RTS2·GNSS 데이터 통합센터 계정 동시 생성으로 기술. **"승인 대기/심사" 문구는 3종 어디에도 없음**(텍스트 추출 후 '승인' 검색 결과 0건). 승인 소요 기간: 공식 문서에 없음 → 미확인 | 공식 PDF, 높음(없음의 확인) |
| 요금 | PDF 3종에서 '무료/무상/요금' 문구 없음. 요금 정책 공식 문구: 미확인(재확인 필요). 검색 요약에 "무상 제공" 서술이 있었으나 원문 페이지를 열어 확인하지 못해 채택하지 않음 | 미확인 |
| G-VRS | 국토교통부 국토지리정보원, 2025-10-01 격자형 측위보정정보 시범 서비스 시작(보도 3건 일치): 전국 20km x 20km 격자, UHD·DMB·위성 방송 단방향 전송, 정지측량·자동차·드론 비행 시험에서 기존 서비스와 유사한 정확도 확인, 민간 협의체 1개월 사용자 테스트, 시범은 약 300명 동시 접속, 신청 방법은 NGII 누리집(10월 1일부터) 안내. 위성기준점 4개 추가로 총 103개소 예정. 드론 택배·농업 방제 활용 기대 서술 | 보도(2차, 국토부 보도자료 재전재), 중. 국토부 원문·현재 정식 전환 여부 미확인 |
## 설계에 쓸 수 있는 지침
- 드론 용도는 SSR(SSR-SSRG, RTS2) 이 공식 문구상 가장 명시적. 계정은 NGII 회원가입→GNSS 서비스 포털에서 직접 생성(승인 단계 문구 없음). 단 2026-07 통합 후 화면 경로는 로그인 후 재확인.^[inbox/processed/hw-20261024-korea-ngii-network-rtk-g-vrs-drone-access-recheck-2026-10-24.md]
- G-VRS 는 2025-10 시범 단계 보도만 확인: 비행체 설계 문서에서는 "시범 서비스(2025-10), 정식 여부 미확인"으로 표기.^[inbox/processed/hw-20261024-korea-ngii-network-rtk-g-vrs-drone-access-recheck-2026-10-24.md]
## 한계·미확인
- 승인 소요 기간, 요금, 상업 드론 이용 제한: 공식 확인 못 함(재확인 필요: 위치기준과 문의처는 20261022 파일 기재). 국토교통부 보도자료 원문 URL 미확인(smartcity.go.kr 전재 URL 은 curl 시 오류 페이지 응답). 위 보도 3건의 2차 출처 한계.^[inbox/processed/hw-20261024-korea-ngii-network-rtk-g-vrs-drone-access-recheck-2026-10-24.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
