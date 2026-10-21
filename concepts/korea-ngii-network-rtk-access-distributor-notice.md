---
title: "국토지리정보원 네트워크 RTK(FKP) 이용안내 - 측량장비 유통사 게시글 (2차 출처)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ops-mission
tags: [drone, gnss, ntrip, 신뢰도-낮음]
sources: [inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]
confidence: medium
contested: false
contradictions: []
---

# 국토지리정보원 네트워크 RTK(FKP) 이용안내 - 측량장비 유통사 게시글 (2차 출처)

- 원문: http://geosolution.co.kr/mall/m_view.php?ps_db=notice&ps_boid=6&ps_mode=^[inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]
- 저자: 측량장비 유통사 지오솔루션 (공지글, 국토지리정보원 서비스 안내 전재 형태)^[inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]
- 발행: 미확인 (게시글 내 장애 안내는 2021년 날짜, 열람일 2026-10-22)^[inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]

## 핵심 내용
국토지리정보원 공식 신청·접속 안내 페이지는 이번에 열람하지 못했고(geodesy.ngii.go.kr 은 로그인형 SPA 포털, 신청 절차 정적 페이지 미발견), 대신 유통사 공지글만 확인했다. 글은 "국토지리정보원에서 접속자수 제한이 없는 멀티GNSS서비스를 운영"한다며 FKP 접속 방법을 안내한다. 같은 포털의 공개 첫 화면에는 RTS1 / RTS2 / RTS3 네트워크 RTK 현황, VRS·FKP·SSR 항목이 있음(직접 확인).^[inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- FKP 접속 주소 fkp.ngii.go.kr, 포트 2201, ID/비밀번호는 VRS 서비스와 동일 (유통사 글 기재, 시점 2021년 전후)^[inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]
- 접속자 수 제한 없음이라고 서술(같은 글)^[inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]
- 별도 검색 결과(블로그형 2차 자료): 사전 회원가입·네트워크 RTK 서비스 신청 필요, 마운트포인트 예 VRS-RTCM31/32/34. 공식 확인은 못 함.^[inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]

## 한계·미확인
공식 출처 아님 → 신뢰도 낮음. 현재 유효한 주소·포트, 신청 승인 기간, 요금 여부는 미확인. 위 KCI 논문(korea-kci-lee-network-rtk-mountpoint-comparison-2026)의 서비스 구분(RTS1/RTS2, RTCM 조합 10종)으로 보완 가능.^[inbox/processed/hw-20261021-korea-ngii-network-rtk-access-distributor-notice.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
