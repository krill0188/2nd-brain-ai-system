---
title: "Innovation: Flying safe — GNSS robustness for unmanned aircraft systems (기체 전원 ON/OFF 시 GPS C/N0 저하 실측)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: hardware
ontology_class: GNSSSignalsEnvironment
tags: [drone, hardware, gnss, rfi, onboard-interference, cn0, antenna-placement]
sources: [inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]
confidence: medium
contested: false
contradictions: []
---

# Innovation: Flying safe — GNSS robustness for unmanned aircraft systems (기체 전원 ON/OFF 시 GPS C/N0 저하 실측)

- 원문: https://www.gpsworld.com/innovation-flying-safe/ (원 논문: Stubbs & Akos, "GNSS/GPS Robustness for UAS", ION ITM 2016, pp. 485-493)^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]
- 저자: Joshua Stubbs, Dennis M. Akos (GPS World 칼럼 편집: Richard B. Langley)^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]
- 발행: 2016-04-04 (GPS World)^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]

## 핵심 내용
출처 유형: GPS World 공개 기사(Bright Data scrape_as_markdown 로 전문 열람; curl 은 403). 원 ITM 논문 본문은 ION 유료라 미열람. 신뢰도: 중상(동료심사 학회 논문 기반 해설기사, 수치는 그림·표 이미지라 본문 텍스트에 일부만 있음).^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]
- 실험: 소형 UAS(비행제어기, 915 MHz·2.4 GHz 통신 링크 탑재)에서 GPS L1 단일주파수 평가키트 수신기+스펙트럼 분석기, 40 dB 인라인 증폭. 3조건: (1) 안테나 기체 외부·전원 OFF 기준 (2) 안테나 기체 내부·전원 OFF (3) 안테나 기체 내부·전원 ON(전 장비 가동).^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]
- 결과(본문 텍스트 그대로): 추적 위성 수는 조건 간 변화 없음. C/N0 는 "up to 10-dB difference" (안테나 같은 위치, UAS ON 대 OFF). 스펙트럼 분석기에서 UAS ON 시 노이즈 플로어가 크게 상승하고 L1 중심의 GPS 융기(bump)가 사라짐. 위치해 출력은 유지되나 정확도 저하 가능, 사용자가 RFI를 모르고 지나칠 수 있다고 지적.^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]
- 모터·ESC 개별 기여는 분리 측정하지 않음(전체 기체 장비 ON/OFF 비교). 로터 블레이드 변조도 아님.^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]
## 설계에 쓸 수 있는 지침
- 안테나를 기체 내부에 두면 외부 대비 감쇠가 있고(Fig.4, 값은 그림), 장비 ON 시 최대 10 dB C/N0 저하가 실측됨. 설계 시 "위성 수가 같아도 C/N0 를 따로 감시" 근거로 사용.^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]
## 한계·미확인
- 정확한 표 수치(Table 1)·그림 값은 이미지라 미확인. 모터/ESC 단독 정량, 안테나-소스 거리별 C/N0 곡선: 미확인.^[inbox/processed/hw-20261023-env-uas-onboard-rfi-cn0-stubbs-akos-2016.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
