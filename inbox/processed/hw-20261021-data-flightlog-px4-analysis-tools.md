---
title: "Flight Log Analysis (PX4 User Guide)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: simulation-test
source: https://docs.px4.io/main/en/log/flight_log_analysis.html
authors: "PX4 project"
published: "미확인"
tags: [drone, flight-log, analysis, pyulog]
---
## 핵심 내용
PX4 로그 분석 도구: Flight Review(웹, 업로드/공유/대화형 플롯), pyulog(ulog_info, ulog_messages, ulog_params, ulog2csv, ulog2kml 스크립트), FlightPlot(Java 기반 GUI, .ulg/.px4log/.bin 읽기), PlotJuggler(시계열 GUI, 모든 uORB 토픽 그래프). 외부 플랫폼 Roboto는 고진동, GPS 열화, 추정기 실패, 로그 오류를 자동 감지한다고 소개된다.

## 설계·운용에 쓸 수 있는 지침
- 자동화 파이프라인에서는 pyulog로 ULog를 CSV로 변환해 후처리(ulog2csv).
- 수동 점검 기준(문서): 충돌 포착 여부, roll/pitch rate의 setpoint 추종, 센서 데이터 유효성, 진동 peak-to-peak가 약 2-3 m/s2를 넘는지 확인.
- 로그가 갑자기 끊기면 SD 카드의 fault_date.log를 확인.

## 한계·미확인
- 도구별 자동 점검 항목 목록은 페이지에 없음(미확인). 도구 성능 수치 미확인.
