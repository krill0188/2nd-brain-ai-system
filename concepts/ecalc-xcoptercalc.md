---
title: "eCalc xcopterCalc 멀티콥터 추진계 계산기"
created: 2026-10-30
updated: 2026-10-30
type: concept
domain: hardware
tags: [drone, drone-hw, research, provenance]
sources: [raw/articles/ecalc-xcoptercalc.md, raw/articles/ecalc-xcoptercalc-help.md]
confidence: medium
contested: false
contradictions: []
---

# eCalc xcopterCalc 멀티콥터 추진계 계산기

## 개요
eCalc xcopterCalc는 배터리·ESC·모터·프로펠러 조합을 입력하면 호버 전류·전력, 최대 전류·전력, 추력-중량비, 예상 비행시간 등을 보여 주는 외부 웹 계산기다.^[raw/articles/ecalc-xcoptercalc.md] 제작자 표기는 "Solution for All Markus Müller"이다.^[raw/articles/ecalc-xcoptercalc-help.md]

DroneWiki에서는 **초기 사이징·후보 비교용 외부 도구**로만 다룬다. 계산엔진·부품 DB를 복제하지 않고, 입력 조건과 결과를 기록해 실측과 비교하는 것이 목적이다.

## 계산 대상
- 멀티콥터 추진계 한 세트(배터리 + ESC + 모터 + 프로펠러)의 정상상태 성능. 로터 수·구성(flat / coax)과 기체 중량을 입력한다.^[raw/articles/ecalc-xcoptercalc.md]
- 결과는 계산된 총중량(All-up Weight)을 기준으로 산출된다.^[raw/articles/ecalc-xcoptercalc-help.md]
- 제어 루프·기체 공력 항력은 다루지 않는다. 최대 상승률은 "기체 항력 무시" 추정이라고 도움말에 적혀 있다.^[raw/articles/ecalc-xcoptercalc-help.md]

## 입력값
캡처한 페이지의 폼 필드 기준이다(필드명은 화면 표기).^[raw/articles/ecalc-xcoptercalc.md]

| 구분 | 입력 항목 (단위) |
|---|---|
| 기체 | Model Weight (g/oz, 기준: incl. Drive / less Battery / without Drive), Frame Size (mm/inch), FCU Tilt limit (no limit, 10°~80°) |
| 로터 수와 배치 | # of Rotors, 구성 flat / coax |
| 배터리 | 셀 타입(Custom 또는 목록), 충전 상태(full / normal / low), 직렬 S·병렬 P, 셀 용량(mAh), max. discharge(10~100%), 내부저항(Ohm), 전압(V), 연속·최대 C-rate, 중량 |
| ESC | 타입(Custom 또는 목록), 연속·최대 전류(A), 저항(Ohm), 중량 |
| 부속품 | Accessories 전류 소모(A), 중량 |
| 모터 | 제조사·타입, 냉각 상태(excellent~very poor), Kv(rpm/V), 무부하 전류(A)와 측정 전압(V), 한계(Limit up to 15s: A 또는 W), 저항(Ohm), 케이스 길이, 자극 수, 중량 |
| 프로펠러 | 타입·요크 트위스트, 직경, 피치, 블레이드 수, PConst/TConst, 기어비 |
| 환경조건 | Field Elevation (m/ft ASL), Air Temperature (°C/°F), Pressure QNH (hPa/inHg) |

Custom 부품은 도움말이 정한 규칙을 따른다. 배터리 값은 **셀 1개 기준**이고, 제조사 데이터나 직접 측정값만 쓰며 유사 모터 값으로 추정해 채우지 말라고 명시한다. 모터 저항은 오옴미터가 아니라 Kelvin 4선식, Kv와 무부하 전류는 프로펠러 없이 짧게(<10 s) 돌려 측정하라고 안내한다.^[raw/articles/ecalc-xcoptercalc-help.md]

## 출력값
화면에 있는 결과 항목이다. 계산 전에는 "-"로 표시된다.^[raw/articles/ecalc-xcoptercalc.md]

| 구분 | 결과 항목 (단위) |
|---|---|
| 호버 전류·전력 | (기록 시 Total Drive 값을 쓴다) Motor @ Hover의 Current(A)·electric Power(W), Total Drive의 Current @ hover(A)·P(in) @ Hover(W) |
| 최대 전류·전력 | Motor @ Maximum의 Current(A)·electric Power(W), Total Drive의 Current @ max(A)·P(in) @ max(W) |
| RPM | Motor @ Optimum Efficiency / Maximum / Hover 각각 Revolutions(rpm) |
| 추력-중량비 | Thrust-Weight (:1) |
| 효율 | Motor 구간별·Total Drive의 Efficiency(%) |
| specific thrust | specific Thrust (g/W, oz/W) |
| 예상 비행시간 | min. / mixed / hover Flight Time (min), 배터리 Load(C), Energy(Wh), Capacity used(mAh) |
| 상승률·최대속도·거리 | max. rate of climb (m/s), max. Speed (km/h), est. Range (m), max. Tilt (°), add. Payload (g) |
| 기타 | est. Temperatur(모터 케이스, °C), Total Disc Area, Remarks(안내: 파랑 / 위험: 빨강), Wattmeter & Logger readings(전류·전압·전력) |

## DroneWiki에서의 사용 목적
1. 부품 후보를 좁히는 **사전 비교**(예: [[drone-motor-product-specs-catalog]]의 모터와 [[drone-battery-cell-pack-specs-catalog]]의 배터리 조합).
2. 계산 시점의 입력과 결과를 템플릿으로 보존해 **재현 가능한 예측값**으로 남긴다.
3. 예측값을 정적 추력시험·비행로그 실측과 나란히 놓고 오차를 기록한다([[multirotor-propeller-test-research]], [[flight-logging-analysis]]).

## 정확도와 한계
- 화면에는 "Accuracy: +/-15%"가 표시된다. 이 수치의 산정 근거와 적용 범위(어느 출력값에 해당하는지)는 캡처 본문에서 **확인되지 않았다(미확인)**.^[raw/articles/ecalc-xcoptercalc.md]
- 도움말은 피치/직경 비(P/D)가 0.667을 넘는 프로펠러(실속)에서는 호버 계산이 부정확해질 수 있고, 극단 비율은 호버 값이 "불가"로 나온다고 적는다. 직경 6.5" 미만의 레이스용 고피치 프로펠러는 허용하되 호버 정확도가 떨어진다고 한다.^[raw/articles/ecalc-xcoptercalc-help.md]
- 최대 물리 RPM과 ESC의 분당 펄스 한계(epm)는 감시하지 않는다.^[raw/articles/ecalc-xcoptercalc-help.md]
- 모터 온도는 냉각 입력에 의존하는 추정치이며, Quick Check 게이지는 모터 온도 0~70 °C를 녹색, 70~90 °C를 "critical" 노랑으로 표시하고, 모터 특성 그래프의 케이스 온도는 80 °C 초과 시 적색으로 바뀐다고 도움말에 적혀 있다(80 °C 초과 손상 가능, 100 °C 초과 매우 위험).^[raw/articles/ecalc-xcoptercalc-help.md]
- 정상상태 모델이므로 기동·돌풍·배터리 노화·저온 내부저항 증가 같은 조건은 입력으로 직접 반영되지 않는다. 이 문장은 도움말 직접 인용이 아니라 입력 항목 목록에서 본 해석이다.

## eCalc 결과와 실측값의 구분
- eCalc 결과는 **예측값(predicted)**, 시험대·전력모듈·ULog/BIN·텔레메트리 값은 **실측값(measured)**이다. 같은 필드에 섞지 않는다.
- 도움말도 로거·와트미터 값을 쓰기 전에 멀티미터로 기준 측정을 하라고 권하며, 일부 로거는 25% 이상 벗어난 경험이 있다고 한다.^[raw/articles/ecalc-xcoptercalc-help.md] 실측이라도 계측기 보정 상태를 기록해야 한다.
- 비교 기록은 `templates/propulsion-prediction-measurement-comparison.md`를 쓴다. 실측이 없으면 `comparison_status: not_compared`로 둔다.
- eCalc의 "Wattmeter & Logger readings" 블록은 **eCalc가 계산한 예상 계기값**이지 실측이 아니다.

## 라이선스·저작권·자동화 주의사항
- 페이지 하단 표기: "copyright by Solution for All Markus Müller". 재사용·재배포 조건을 밝힌 라이선스 문서는 캡처에서 **확인되지 않았다(미확인)**.^[raw/articles/ecalc-xcoptercalc-help.md]
- 무료 접속은 "Restricted Demo Version"으로 표시되고 전체 버전은 회원가입(표시가 $0.99)이 필요하다. CSV 내보내기와 설정 공유 링크는 도움말상 "for members only when logged in"이다.^[raw/articles/ecalc-xcoptercalc-help.md]
- 공식 API나 기계 판독용 결과 인터페이스는 캡처한 HTML과 도움말에서 **발견되지 않았다**. 존재하지 않는다고 단정할 근거는 없으므로 "미확인"으로 둔다.
- `robots.txt`는 요청 시 404(페이지 없음)를 반환했다. 크롤 정책이 선언되지 않았다는 뜻일 뿐 자동 수집 허용이 아니다.
- 따라서 DroneWiki는 ① 자동·대량 호출을 하지 않고, ② 계산 JS와 부품 DB를 복사하지 않으며, ③ 로그인·접근제한을 우회하지 않고, ④ eCalc 명칭·결과를 자체 계산엔진처럼 표시하지 않는다. 사람이 한 건씩 계산하고 템플릿에 옮겨 적는 방식만 허용한다.

## 로그인 없이 쓰는 절차
무료 데모에서 계산은 로그인 없이 된다(2026-10-30 확인). 로그인이 필요한 기능은 CSV 내보내기와 설정 공유 링크뿐이며, 이 둘이 하는 일(입력·결과 보존)은 아래 템플릿이 대신한다.
1. 화면에서 한 건 계산하고 입력값과 결과를 `templates/ecalc-xcoptercalc-run.md` 사본에 옮겨 적는다(스크린샷·자동 수집 불필요).
2. 부품값은 제조사 데이터시트나 직접 측정값만 쓴다. 모르면 `null`.
3. `python3 scripts/validate-ecalc-run.py <기록>`로 검증한다. 호버·최대 전류·전력은 Total Drive 값을 적는다.
4. 실측이 생기면 비교 템플릿에 따로 적는다. 시험 절차는 [[multirotor-propeller-test-research]]의 "예측값 검증 절차"를 따른다.

## DroneWiki 적용 권장 구조
1. `templates/ecalc-xcoptercalc-run.md`: 입력·결과·검증 상태를 YAML로 기록(모르는 값은 `null`, 임의 보정 금지).
2. `templates/propulsion-prediction-measurement-comparison.md`: 항목별 예측값/실측값/오차/출처 분리.
3. `scripts/validate-ecalc-run.py`: 필수 필드·단위·양수 조건·예측/실측 혼합을 검사하고, 불완전하면 보정 없이 실패.
4. 장기: 독립 추진계 계산 모듈은 공개 논문과 자체 추력시험 데이터에서 출발한다([[multirotor-propulsion-sizing-methods]], [[multirotor-energy-power-models]]). eCalc 내부식을 역공학해 재구현하지 않는다. 이 항목은 아직 설계 단계가 아니다.

## 관련 페이지
[[multirotor-propulsion-sizing-methods]] · [[multirotor-energy-power-models]] · [[multirotor-propeller-test-research]] · [[bldc-motor-esc-characterization-research]] · [[drone-power-battery]] · [[drone-motor-product-specs-catalog]] · [[drone-battery-cell-pack-specs-catalog]] · [[flight-logging-analysis]]

## 출처와 검증 상태
| 항목 | 상태 |
|---|---|
| 공식 페이지·도움말 캡처 | 2026-10-30, 각 HTTP GET 1회. 원문 HTML SHA-256과 본문 SHA-256은 각 raw 파일 frontmatter에 기록 |
| 필드·결과 목록 | 정적 HTML 분석으로 확인(실제 계산 실행은 하지 않음) |
| REA | 2026-10-30 재점검: 등록이 6.4.0 고정이고 스킬 신원이 어긋나 있던 것을 `rea setup --client claude_code`로 정비(6.5.0, 범위 지정 doctor `healthy: true`). 필드·결과 목록은 curl과 HTML 파서의 정적 분석 결과이고, REA 관찰은 아래 한 건뿐이다 |
| REA 수동적 관찰 | 격리된 임시 프로필의 headless Chrome에서 페이지를 1회 로드하고 `rea discover-webmcp-tools`를 실행: 페이지가 선언한 WebMCP 도구 **0개**(관찰 창 1.5초 내 완전). 계산 실행·입력·네트워크 캡처는 하지 않음 |
| URL 공유 파라미터 형식 | 확인 불필요로 종결: 공유 링크는 회원 전용이며 입력 전체를 템플릿에 기록하므로 필요하지 않다. 계산 후 주소창 URL은 변하지 않음 |
| 계산 위치 | **서버 측**: 임의 관찰 입력으로 `Calculate`를 1회 눌렀을 때 입력 전체가 쿼리 파라미터로 `/calcinclude/xcoptercalcres.php`에 GET 전송됨을 REA(CDP)로 관찰. 이 엔드포인트는 문서화된 공개 API가 아니므로 직접 호출·자동화하지 않는다. 관찰 입력과 결과는 위키에 저장하지 않음 |
| 계산엔진 버전 | 페이지 자산 쿼리에 `7.41.019`가 보이나 계산엔진 버전과 같은지는 미확인. 화면의 "Version: X / Data:" 칸은 비어 있음 |
| 신뢰도 | 도구의 존재·입출력 구조는 공식 출처로 확인, 정확도 수치는 자기 표기이므로 `medium` |
