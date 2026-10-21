---
title: "Downloading and Analyzing Data Logs in Mission Planner (ArduPilot Copter docs)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: simulation-test
source: https://ardupilot.org/copter/docs/common-downloading-and-analyzing-data-logs-in-mission-planner.html
authors: "ArduPilot Dev Team"
published: "미확인"
tags: [drone, flight-log, dataflash, ardupilot]
---
## 핵심 내용
ArduPilot의 DataFlash 로그는 오토파일럿 내 SD 카드나 온보드 플래시에 저장되거나 MAVLink로 스트리밍되며 비행 후 내려받는다. 기본은 첫 arm 시 기록 시작이고 LOG_DISARMED로 전원 인가 시 시작하게 바꿀 수 있다. 온보드 플래시(보통 16MB)는 순환 버퍼처럼 가장 오래된 로그를 덮어쓴다. Mission Planner의 Flight Data 화면 DataFlash Logs 탭에서 내려받고 "Review a Log"로 .bin/.log를 열어 필드를 그래프로 본다. MAVExplorer(MAVProxy 일부), 웹 로그 도구도 쓸 수 있다. 다운로드 시 Google Earth용 KMZ가 생성된다.
원문 인용: "Dataflash logs are stored on the autopilot and can be downloaded after a flight."

## 설계·운용에 쓸 수 있는 지침
- LOG_BACKEND_TYPE: 1=SD, 2=MAVLink, 4=온보드 플래시.
- LOG_MAX_FILES 최대 500, LOG_FILE_MB_FREE 기본 500MB.
- MAVLink 스트리밍은 보통 921600 baud 고속 링크 필요.
- Copter 고속 자세 로깅은 SCHED_LOOP_RATE(약 400Hz), 느린 루프는 약 15% 미만 유지(PM 메시지).
- SD 쓰기 문제 시 BRD_SD_SLOWDOWN 최대 32(기본 0).
- 이벤트 10=Armed, 11=Disarmed.

## 한계·미확인
- 바이너리 메시지 포맷(FMT 메시지 구조) 상세는 이 페이지에 없음: 미확인.
- 게시일 미확인.
