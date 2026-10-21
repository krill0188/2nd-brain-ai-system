---
title: "서울특별시 네트워크 RTK 시스템 접속 정보 (서울시 공식 페이지)"
created: 2026-10-22
captured: 2026-10-22
type: paper
domain: hardware
source: https://gnss.eseoul.go.kr/service_sub1_01
tags: [drone, gnss, 8-한국, network-rtk, ntrip, vrs, seoul]
authors: "서울특별시 토지관리과 (공식 서비스 페이지)"
published: "미확인(열람일 2026-10-22)"
---

## 핵심 내용
서울특별시가 운영하는 멀티 GNSS 네트워크 RTK 서비스의 공개 접속 안내. 접속 주소 gnss.eseoul.go.kr, 접속 포트 2101, 사용자 ID·비밀번호는 별도 가입이 필요 없다고 페이지에 게시되어 있다(계정 값은 비밀정보 저장 금지 원칙에 따라 이 파일에 적지 않음 — 페이지에서 직접 확인). 가상기준점(VRS) 방식 마운트포인트와 지원 위성군 표가 있다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- VRS 마운트포인트: VRS-RTCM32(RTCM 3.2 MSM5, GPS/GLO/GAL/BDS/QZS), VRS-RTCM31(RTCM 3.1, GPS/GLO), VRS-RTCM23(RTCM 2.3), VRS-CMRx(CMRx, 5개 위성군), VRS-CMRplus(CMR+, GPS/GLO).
- 단일기준점 RTK(도봉, 송파, 금천, 강서, 용산): YONS-RTCM32 등.
- 방식 설명: VRS 는 사용자가 NMEA GGA 로 개략 위치를 서버에 보내면 인접 기준국(5개 이상)으로 해당 위치용 보정을 생성하는 양방향 방식 — 이동통신망 필요.
- 드론에서는 FC/컴패니언이 NTRIP 클라이언트로 GGA 를 주기 송신해야 함(위 방식 설명에서 도출).
- 홈페이지 회원 기능은 서울시 회원 계정으로 로그인 후 등록(FAQ), GNSS 시스템·기준국 현황 등은 로그인 없이 이용 가능.

## 한계·미확인
서울 지역 한정 서비스이며 국토지리정보원(NGII) 전국 서비스의 신청 절차·접속 정보는 아님. 정확도·이용 조건·가용 시간은 페이지에 없음. 계정 값은 의도적으로 미기재.
