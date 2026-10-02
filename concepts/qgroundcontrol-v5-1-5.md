---
title: "QGroundControl v5.1.5 Release Notes"
created: 2026-10-02
updated: 2026-10-02
type: concept
domain: gcs-software
tags: [drone, drone-sw, gcs-software, qgroundcontrol]
sources: [inbox/processed/fetch-2026-10-02-qgroundcontrol.md]
confidence: high
contested: false
contradictions: []
---

# QGroundControl v5.1.5

QGroundControl v5.1.5는 v5.1 안정 릴리스 계열의 패치 버전으로, 번역·MAVLink enum 노출·미션
관리·FTP·카메라 등 다수 영역의 버그 수정을 포함한다.^[inbox/processed/fetch-2026-10-02-qgroundcontrol.md]

## 주요 변경사항

| 영역 | 수정 내용 |
|------|----------|
| **번역** | ko_KR, pt_PT, zh_CN에서 누락된 `%1` 플레이스홀더 복원 |
| **MAVLink** | enum 값을 QML에 노출(`MAVLinkEnums`) |
| **MissionManager** | 깨진 enum 번역으로 유실됐던 미션 명령 복원 |
| **Scripting** | 선택한 스크립트의 다운로드/삭제 아이콘 중앙 정렬 |
| **APM** | ArduPilot lua 스크립트 목록 디렉터리 미동작 수정, 이미 시동된 기체에서도 이륙 시작 |
| **MainWindow** | 치명적 차량 메시지 팝업이 키보드 포커스를 가로채던 문제 수정 |
| **FTP** | MAVFTP URI 스킴 제거 시 경로 보존 |
| **Comms** | 링크 연결 상태를 스레드 종속 소켓이 아닌 원자적 플래그에서 읽도록 수정 |
| **Camera** | 셔터 버튼으로 타임랩스 캡처 중지, 줌 슬라이더가 카메라 보고 줌 값을 명령으로 되돌려보내던 문제 수정 |
| **Vehicle** | 느린 링크에서 실패를 유발하던 초기 연결 외부 타임아웃 제거 |
| **AnalyzeView** | 0바이트 온보드 로그 다운로드 시 멈추던 문제 수정, 정상 완료되도록 처리 |

## 설치

[Download and Install](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/getting_started/download_and_install.html)
페이지에서 플랫폼별 설치 지침 참고.

## 관련 개념

- [[qgroundcontrol]] — QGroundControl 개요 페이지
- [[qgroundcontrol-v5-1-4]] — 직전 안정 릴리스(HUD 피치 표시 수정 등)
- [[mavlink-protocol]] — MAVLink 프로토콜
