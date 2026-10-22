---
title: "모터·ESC·프로펠러 근접 GNSS 안테나 C/N0 저하 정량 — 4차 재조사 결과 (2026-10-24)"
created: 2026-10-24
updated: 2026-10-24
type: concept
domain: hardware
tags: [drone, hardware, gnss, cn0, esc, motor, antenna-placement, negative-result]
sources: [inbox/processed/hw-20261024-conv-motor-esc-antenna-cn0-quant-search-round4-2026-10-24.md]
confidence: medium
contested: false
contradictions: []
---

# 모터·ESC·프로펠러 근접 GNSS 안테나 C/N0 저하 정량 — 4차 재조사 결과 (2026-10-24)

- 원문: 본 폴더 gnss/research/env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi ; 20261023 gnss/research/env-uas-onboard-rfi-cn0-stubbs-akos-2016 ; OpenAlex API ; WebSearch 4회^[inbox/processed/hw-20261024-conv-motor-esc-antenna-cn0-quant-search-round4-2026-10-24.md]

## 핵심 내용
판정: **"모터/ESC/프로펠러로부터 거리 X 에서 C/N0 Y dB 저하"를 거리·dB 로 적은 OA 논문·학위논문·기술노트는 이번에도 확인하지 못함(미확인).** 새로 시도한 수단: OpenAlex 3개 질의, WebSearch 4회(영문), PMC 전문 열람, ArduPilot 문서/포럼 검색 결과 확인.^[inbox/processed/hw-20261024-conv-motor-esc-antenna-cn0-quant-search-round4-2026-10-24.md]
| 후보 | 확인 내용 | 정량 근거 여부 |
|---|---|---|
| Stubbs & Akos 2016 (GPS World 해설, 20261023 파일) | 기체 장비 전체 ON/OFF 시 C/N0 최대 10 dB 차이 | 있음(장비 전체, 거리 아님) |
| Hehenberger 2022 (본 폴더) | 설치 높이 50~130 mm 패턴 시뮬, 로터 없는 측정 | 모터 EMI 아님 |
| ArduPilot 공식 문서(검색 결과 요약) | 외장 GPS/컴퍼스를 마스트에 올려 PDB 등에서 떼라는 권고; 모터 부하 영향은 컴퍼스(CompassMot) 중심 | C/N0 수치 없음(문서 본문 미열람) |
| 제3자 블로그(LogHat) | 검색 요약에 "50 mm 마스트로 온보드 RFI 대부분 해결" 서술. 페이지 본문 재확인 시 해당 문구 추출 실패 | 미확인, 일화 수준 |
| UST 매거진 / 안테나 가이드 | 멀티로터 안테나를 프로펠러 가까이 두지 말 것(소음·가림) 정성 서술 | 수치 없음 |
| u-blox UBX-15030289 안테나 앱노트 | 부록에 C/N0 계산 예. 거리별 모터 노이즈 표는 확인 못 함 | 미확인(전문 미열람) |
## 설계에 쓸 수 있는 지침
- 쓸 수 있는 정량 문장은 Stubbs 2016 의 "기체 ON 시 최대 10 dB" 하나뿐. 거리 의존성은 "미확인"으로 두고, 설계 요구는 "C/N0 를 모터 구동 전/후 로그로 직접 측정" 으로 처리.^[inbox/processed/hw-20261024-conv-motor-esc-antenna-cn0-quant-search-round4-2026-10-24.md]
## 한계·미확인
- ArduPilot/PX4 포럼의 실측 로그 링크, Septentrio 기술노트 PDF(로그인 리다이렉트로 20261023 실패)는 이번에도 확보 못 함.^[inbox/processed/hw-20261024-conv-motor-esc-antenna-cn0-quant-search-round4-2026-10-24.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
