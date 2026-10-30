---
run_ref: ""
comparison:
  hover_current:
    predicted_value: null
    measured_value: null
    unit: "A"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  hover_power:
    predicted_value: null
    measured_value: null
    unit: "W"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  maximum_current:
    predicted_value: null
    measured_value: null
    unit: "A"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  maximum_power:
    predicted_value: null
    measured_value: null
    unit: "W"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  motor_rpm_hover:
    predicted_value: null
    measured_value: null
    unit: "rpm"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  motor_rpm_maximum:
    predicted_value: null
    measured_value: null
    unit: "rpm"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  thrust:
    predicted_value: null
    measured_value: null
    unit: "g"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  thrust_weight_ratio:
    predicted_value: null
    measured_value: null
    unit: "ratio"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  flight_time:
    predicted_value: null
    measured_value: null
    unit: "min"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  motor_temperature:
    predicted_value: null
    measured_value: null
    unit: "C"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
  battery_voltage_drop:
    predicted_value: null
    measured_value: null
    unit: "V"
    absolute_error: null
    relative_error_percent: null
    measurement_source: ""
    measurement_date: ""
    confidence: "low"
---

<!--
예측값-실측값 비교 템플릿 (canonical 페이지 아님, 복사해서 사용)

규칙
- run_ref: 예측값을 가져온 eCalc 계산 기록 파일의 저장소 상대경로.
- predicted_value 는 eCalc 결과(run 기록의 results)에서만, measured_value 는 계측에서만 가져온다. 서로 대입하지 않는다.
- 실측이 없으면 measured_value / absolute_error / relative_error_percent / measurement_source / measurement_date 모두 null 또는 "".
- absolute_error = |predicted - measured|, relative_error_percent = absolute_error / |measured| * 100. 둘 다 값이 있을 때만 적는다.
- measurement_source 허용값:
    static_thrust_stand       정적 추력시험대
    ammeter                   전류계
    power_module              전력 모듈
    px4_ulog                  PX4 ULog
    ardupilot_bin             ArduPilot BIN
    fc_telemetry              비행 컨트롤러 텔레메트리
    battery_log               배터리 로그
    motor_temperature_sensor  모터 온도 센서
- measurement_date 는 YYYY-MM-DD. confidence 는 low / medium / high.
- predicted_value 출처 교차검증: hover_*, maximum_*, motor_rpm_hover/motor_rpm_maximum(운영점 구분), thrust_weight_ratio, flight_time, motor_temperature 는 run 기록 results 값과 일치해야 한다.
  thrust(= TWR x 총중량으로 유도) 와 battery_voltage_drop(= 정격전압 - 부하전압으로 유도) 은 eCalc 직접 출력이 아니므로 수기 입력이며 교차검증하지 않는다.
- unit 은 항목별로 고정: A, W, A, W, rpm, rpm, g, ratio, min, C, V (위 항목 순서와 같음).
- 검증: python3 scripts/validate-ecalc-run.py --comparison <복사한 파일>
-->
