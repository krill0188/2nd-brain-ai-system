---
title: "국토지리정보원 GNSS 서비스포털 접근 시도 기록 (신청 절차 미확인)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ops-mission
tags: [drone, gnss, ngii, network-rtk, 미확인]
sources: [inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]
confidence: medium
contested: false
contradictions: []
---

# 국토지리정보원 GNSS 서비스포털 접근 시도 기록 (신청 절차 미확인)

- 원문: https://geodesy.ngii.go.kr/^[inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]
- 저자: 국토지리정보원(NGII) 포털 (열람 기록)^[inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]
- 발행: 열람일 2026-10-22^[inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]

## 핵심 내용
geodesy.ngii.go.kr 첫 화면(Next.js 기반)은 열리며 메뉴는 검색, 다운로드, 공지사항, Q&A, 로그인뿐이고 화면에는 상시관측소 상태, Single RTK, RTS1/RTS-VRS/RTS2-VRS/FKP 접속자 현황, SSR 상태 항목이 표시된다. 공지사항 데이터를 부르는 공개 경로(/backend/portal/openapi/bbs/notice/list)는 접근 시 '국토지리정보원 서비스 이용안내 — 현재 일시적인 접속 지연이 발생' 안내 화면을 돌려주었다.^[inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 이번 시도로 확인되는 것은 서비스 구분(VRS/FKP/SSR)이 포털에 표시된다는 사실뿐.^[inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]
- 신청 절차·접속 서버 주소·포트·마운트포인트·요금은 이번에도 공식 페이지에서 확인하지 못함.^[inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]
- 로그인이 필요한 영역은 시도하지 않음.^[inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]

## 한계·미확인
신청 절차 미확인. 포털 점검/지연 상태였을 가능성이 있어 재시도 필요. 3자 블로그가 보여주는 마운트포인트(VRS-RTCM31 등)는 공식 확인이 아니므로 기록하지 않음.^[inbox/processed/hw-20261021-korea-ngii-geodesy-portal-access-attempt-2026-10-22.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
