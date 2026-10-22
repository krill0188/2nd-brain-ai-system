---
title: "국토지리정보원 네트워크 RTK 서버·마운트포인트·서비스 구분 - 공식 페이지와 변경 안내문"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ops-mission
tags: [drone, gnss, ngii, network-rtk, ntrip, ssr, 공식, 드론]
sources: [inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]
confidence: medium
contested: false
contradictions: []
---

# 국토지리정보원 네트워크 RTK 서버·마운트포인트·서비스 구분 - 공식 페이지와 변경 안내문

- 원문: https://map.ngii.go.kr/ms/mesrInfo/gnss/vrsUserView.do^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]
- 저자: 국토지리정보원(NGII) 국토정보플랫폼 위성기준점 서비스 페이지 + 변경 안내문 PDF(sq=92032)^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]
- 발행: 페이지 열람 2026-10-22, 변경 안내문 시행일 2022-05-02^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]

## 핵심 내용
국토정보플랫폼(map.ngii.go.kr)의 '위성기준점 서비스 > 네트워크RTK서비스' 공식 페이지와 '네트워크RTK 서비스 변경 안내'(sq=92032) PDF에서 확인한 서버 구성. 확인 방법: curl 직접 열람 + PDF 텍스트 추출. 신뢰도: 높음(정부 1차). 20261021의 유통사 글(fkp.ngii.go.kr:2201, 2021년경)은 이 변경 안내문으로 폐기됨을 확인.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]

## 설계·운용에 쓸 수 있는 지침 (공식 문구)

| 서비스 | 접속 주소 | 포트 | 마운트포인트 | 비고(공식) |
|---|---|---|---|---|
| VRS | RTS1.ngii.go.kr | 2101 | VRS-CMRx, VRS-RTCM23, VRS-RTCM31, VRS-RTCM34, RTK-RTCM32 | 공공측량 성과심사 사용 가능(2018.3.30 작업규정 개정), 시스템 동시접속 1200명 제한, Single RTK(RTK-RTCM32)는 공공측량 작업용으로 부적합(관련 규정 검토 중) |
| VRS / FKP | RTS2.ngii.go.kr | 2101 | VRS-RTCM31, VRS-RTCM32, FKP-RTCM31 | Multi-GNSS 지원, 사용자 수 무제한 서술 |
| SSR | RTS2.ngii.go.kr | 2101 | SSR-SSRG | '드론·차량 등 이동체 측위 및 SSR 수신 가능 저가형 수신기 전용' |

- 변경 안내문(시행 2022-05-02): FKP 접속 주소·포트가 fkp.ngii.go.kr:2201 에서 RTS2.ngii.go.kr:2101 로 변경, VRS는 vrs3.ngii.go.kr 에서 RTS1.ngii.go.kr 로 변경. 마운트포인트 개명표 포함(예: VRS_V32 -> VRS-RTCM32, SSRG -> SSR-SSRG).^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]
- 마운트포인트 설명(공식): VRS- = 이동국 인근 가상기준점 관측치, SB_AutoSelection-(구) = 가장 가까운 위성기준점 실제 관측치(Single RTK), VRS-RTCM32/34 = Multi-GNSS 가능, FKP-RTCM31 = 면보정 파라미터 기반 Multi-GNSS 가능.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]
- 페이지 서술: RTK는 기준국과 거리가 멀어질수록 정밀도가 저하되는 단점이 있고, SSR은 오차 요인별 보정정보를 제공해 드론·자율차 등 이동체와 저가형 수신기에서 고정밀 위치 서비스 가능.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]
- 이용 구분(공식): VRS·FKP는 공공측량·일반측량·지적측량용, SSR은 드론·차량 등 이동체 측위용.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]
- 페이지에는 공용 비밀번호 값이 적혀 있으나 기록하지 않음. 사용자 ID는 '개인별 아이디'(계정 생성 절차는 별도 파일 참조).^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]

## 한계·미확인
(1) 페이지에 2026-07-01 이후 GNSS 서비스 포털로 기능이 통합된다는 공지가 떠 있어 위 표가 현재 포털의 값과 같은지는 미확인(geodesy.ngii.go.kr 은 로그인형 SPA, 로그인 시도 안 함). (2) 동일 포트 2101에서 RTS1/RTS2를 구분하는 방식은 주소로만 구분(공식 표 기준). (3) SSR 정확도·수렴 시간·지원 수신기 목록·좌표계는 문서에 없음 → 미확인. (4) '서울시 네트워크 RTK(gnss.eseoul.go.kr:2101)'는 검색 결과 스니펫으로만 확인, 이번에 본문 미열람. (5) 국토교통부 G-VRS(인터넷 없이 위치 보정, 2025-09-29 보도자료) 존재는 검색 결과 제목으로만 확인했고 본문은 리다이렉트 오류로 열람 실패.^[inbox/processed/hw-20261022-korea-ngii-network-rtk-server-mountpoints-official.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
