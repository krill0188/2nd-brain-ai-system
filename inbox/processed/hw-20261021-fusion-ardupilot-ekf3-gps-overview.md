---
title: "ArduPilot EKF3 overview: GPS usage parameters (ArduPilot docs)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: navigation-gnss-denied
source: https://ardupilot.org/copter/docs/common-apm-navigation-extended-kalman-filter-overview.html
tags: [drone, gnss, 5-GNSS/INS융합]
authors: "ArduPilot 문서"
published: "미확인"
---

## 핵심 내용
ArduPilot EKF3 개요. IMU마다 하나의 코어를 구동(EK3_IMU_MASK)하고 한 번에 한 코어 출력만 사용(EK3_PRIMARY). 코어는 비주 GPS 인스턴스도 쓸 수 있어 성능 좋은 GPS로 레인 전환 가능. GPS/비GPS 환경 간 비행 중 센서 전환을 지원한다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- EK3_GPS_TYPE: 0=3D 속도+2D 위치, 1=2D 속도+2D 위치, 2=2D 위치만, 3=GPS 없음(광학흐름만)
- EK3_YAW_M_NSE 기본 0.5: GPS와 컴퍼스 간 헤딩 가중, 값이 낮으면 컴퍼스 신뢰 증가

## 한계·미확인
이 페이지에는 GPS 지연, 게이트, GPS 체크가 없음(개발자 EKF 위키 참조). 해당 수치 미확인.
