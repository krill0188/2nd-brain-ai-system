---
title: "드론 보안·운영 SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-security-ops.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 보안·운영 SW 레지스트리

드론과 융합해 쓰는 SW의 보안·운영 분야 제품·오픈소스 22건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-software-ecosystem-registry]].

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| MAVLink 2 메시지 서명 | 오픈소스 | MAVLink 프로토콜 기능(문서 CC BY 4.0) | MAVLink 프로젝트 | https://github.com/mavlink/mavlink-devguide | devguide 'Message Signing' 문서: MAVLink 2는 서명으로 메시지의 신뢰 출처 검증 지원. C 및 pymavlink 사용법 별도 안내 | 문서 파일 en/guide/message_signing.md 확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| PlotJuggler | 오픈소스 | MPL-2.0 | PlotJuggler | https://github.com/PlotJuggler/PlotJuggler | 저장소 설명: 시계열 시각화 도구 | https://plotjuggler.io. PX4/ArduPilot 로그 직접 지원 여부는 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| PX4 Flight Review | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/flight_review | 저장소 설명: 비행 로그 분석·리뷰 웹 앱 | 공개 인스턴스 https://review.px4.io ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| pyulog | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/pyulog | 저장소 설명: ULog 파일용 파이썬 모듈·스크립트 | 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| ulog_cpp | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/ulog_cpp | 저장소 설명: ULog 읽기·쓰기 C++ 라이브러리 | 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| UAV Log Viewer | 오픈소스 | GPL-3.0 | ArduPilot | https://github.com/ArduPilot/UAVLogViewer | 저장소 설명: UAV 로그 온라인 뷰어 | 공개 인스턴스 https://plot.ardupilot.org ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| Foxglove SDK | 오픈소스 | MIT | Foxglove | https://github.com/foxglove/foxglove-sdk | 저장소 설명: 로보틱스·피지컬 AI 멀티모달 데이터 로깅·시각화 | 상용 서비스 https://foxglove.dev (가격 미기재) ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| Rerun | 오픈소스 | Apache-2.0 | Rerun | https://github.com/rerun-io/rerun | 저장소 설명: 멀티모달 로보틱스 데이터 시각화·질의·스트리밍 | 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| MAVProxy | 오픈소스 | GPL-3.0 | ArduPilot | https://github.com/ArduPilot/MAVProxy | 저장소 설명: MAVLink 프록시·커맨드라인 지상국(패킷 중계·점검 용도) | 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| mavlink2rest | 오픈소스 | MIT | patrickelectric | https://github.com/patrickelectric/mavlink2rest | 저장소 설명: MAVLink를 REST로 노출 | 관측·로깅 용도 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| Wireshark | 오픈소스 | GPL-2.0 | Wireshark Foundation(미러) | https://github.com/wireshark/wireshark | 저장소 설명: 네트워크 프로토콜 분석기 읽기전용 미러 | MAVLink 디섹터 포함 여부는 이 조사에서 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| libpcap | 오픈소스 | 미확인(LICENSE 파일 있음, 종류 미판독) | The Tcpdump Group | https://github.com/the-tcpdump-group/libpcap | 저장소 설명: 커널 패킷 캡처 인터페이스 | 드론 직접 연동 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| WireGuard (wireguard-tools) | 오픈소스 | GPL-2.0 | WireGuard | https://github.com/WireGuard/wireguard-tools | 저장소 설명: 미러(공식 저장소는 git.zx2c4.com) | 링크 암호화(VPN) 용도. 드론 연동은 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| Tailscale | 오픈소스 | BSD-3-Clause | Tailscale | https://github.com/tailscale/tailscale | 저장소 설명: WireGuard 기반 보안 접속 | 서비스는 상용 요금제 존재 가능, 가격 미기재 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| OpenVPN | 오픈소스 | 미확인(COPYING 참조) | OpenVPN Inc. | https://github.com/OpenVPN/openvpn | 저장소 설명: 오픈소스 VPN 데몬 | 세부 조항은 COPYING 확인 필요 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| ZeroTier | 오픈소스 | MPL 및 비공개 구성요소 구분(LICENSE.txt) | ZeroTier | https://github.com/zerotier/ZeroTierOne | 저장소 설명: 'Smart Ethernet Switch for Earth' | 일부 nonfree 폴더 존재(LICENSE.txt 안내) ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| libsodium | 오픈소스 | ISC (LICENSE) | libsodium 프로젝트 | https://github.com/jedisct1/libsodium | 저장소 설명: 현대적 암호 라이브러리 | 임베디드 링크 암호용 후보. 드론 연동 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| OpenSSL | 오픈소스 | Apache-2.0 | OpenSSL 프로젝트 | https://github.com/openssl/openssl | 저장소 설명: 범용 TLS·암호 라이브러리 | 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| wolfSSL | 오픈소스 | GPL-3.0 (듀얼 상용 라이선스 여부는 미확인) | wolfSSL | https://github.com/wolfSSL/wolfssl | 저장소 설명: 임베디드~클라우드용 소형 TLS 구현 | 미확인 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| DroneSploit | 오픈소스 | GPL-3.0 | dronesploit 조직 | https://github.com/DroneSploit/dronesploit | 저장소 설명: 드론 침투테스트 프레임워크 콘솔 | 보안 점검 목적. 승인된 시험에만 사용 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| Aircrack-ng | 오픈소스 | GPL-2.0 | aircrack-ng | https://github.com/aircrack-ng/aircrack-ng | 저장소 설명: WiFi 보안 감사 도구 모음 | 무선 링크 점검용. 승인된 시험에만 사용 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |
| Ettercap | 오픈소스 | GPL-2.0 | Ettercap 프로젝트 | https://github.com/Ettercap/ettercap | 미확인 | 저장소 설명 'Ettercap Project'뿐. 승인된 시험에만 사용 ^[inbox/processed/hw-registry-20261017-software-security-ops.md] |

## 한계
- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.
- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.
- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.

## 관련 문서
- [[mavlink2-security]]
- [[drone-hw-vendor-registry]]
