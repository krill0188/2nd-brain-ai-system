---
calculator:
  name: "eCalc xcopterCalc"
  url: "https://www.ecalc.ch/xcoptercalc.php"
  version: ""
  calculation_date: ""
  accuracy_statement: ""

airframe:
  rotor_count: null
  configuration: ""
  frame_size_mm: null
  all_up_weight_g: null
  tilt_limit_deg: null
  accessories_current_a: null
  accessories_weight_g: null

environment:
  elevation_m: null
  temperature_c: null
  pressure_hpa: null

battery:
  cell_type: ""
  cells_s: null
  parallel_p: null
  cell_capacity_mah: null
  total_capacity_mah: null
  discharge_fraction: null
  internal_resistance_ohm: null
  voltage_per_cell: null
  continuous_c_rating: null
  maximum_c_rating: null
  weight_g: null

esc:
  model: ""
  continuous_current_a: null
  maximum_current_a: null
  resistance_ohm: null
  weight_g: null

motor:
  manufacturer: ""
  model: ""
  cooling: ""
  kv_rpm_per_v: null
  no_load_current_a: null
  no_load_voltage_v: null
  maximum_limit: null
  maximum_limit_unit: ""
  resistance_ohm: null
  case_length_mm: null
  magnetic_poles: null
  weight_g: null

propeller:
  manufacturer: ""
  model: ""
  diameter_in: null
  pitch_in: null
  blades: null
  pconst: null
  tconst: null
  gear_ratio: null

results:
  battery_load_c: null
  battery_voltage_v: null
  battery_energy_wh: null
  min_flight_time_min: null
  hover_flight_time_min: null
  mixed_flight_time_min: null
  battery_rated_voltage_v: null
  hover_current_a: null
  hover_power_w: null
  hover_motor_rpm: null
  maximum_current_a: null
  maximum_power_w: null
  maximum_motor_rpm: null
  thrust_weight_ratio: null
  specific_thrust_g_per_w: null
  estimated_motor_temperature_c: null
  maximum_rate_of_climb_mps: null
  maximum_speed_kmh: null
  estimated_range_m: null

validation:
  source_of_component_data: ""
  measured_thrust_test_available: false
  flight_log_available: false
  comparison_status: "not_compared"
  confidence: "low"
  blocked_fields: []
  notes: ""
---

<!--
eCalc xcopterCalc 계산 기록 템플릿 (canonical 페이지 아님, 복사해서 사용)

사용법
1. 이 파일을 research/ 또는 raw/ 밖의 작업 위치로 복사한다(예: research/ecalc-runs/<날짜>-<기체>.md).
2. 사람이 eCalc 화면에서 한 건 계산하고 값을 옮겨 적는다. 자동·대량 호출 금지.
3. 모르는 값은 null(문자열은 "")로 둔다. 제조사 사양을 추정해 채우지 않는다.
4. null/"" 로 남긴 필드는 validation.blocked_fields에 점 표기 경로로 모두 적는다(예: "battery.internal_resistance_ohm").
5. results는 eCalc가 계산한 예측값만 넣는다. 실측값은 propulsion-prediction-measurement-comparison.md에 기록한다.
6. 검증: python3 scripts/validate-ecalc-run.py <복사한 파일>

단위는 필드명 접미사가 정한다: _g 그램, _mm 밀리미터, _in 인치, _a 암페어, _v 볼트, _w 와트,
_wh 와트시, _mah 밀리암페어시, _ohm 옴, _c 섭씨(온도) 또는 C-rate(battery_load_c, *_c_rating),
_hpa 헥토파스칼, _m 미터, _min 분, _mps m/s, _kmh km/h, _deg 도.
필수 입력(null 불가): airframe.rotor_count, airframe.all_up_weight_g, battery.cells_s, battery.parallel_p,
motor.kv_rpm_per_v, propeller.diameter_in, propeller.pitch_in, propeller.blades
results 의미: hover_*/maximum_* 의 전류·전력은 eCalc "Total Drive" 블록(전 모터 합산; P(in))의 값이다.
Motor @ Hover/Maximum 블록(모터 1개 기준)의 값을 넣지 않는다. *_motor_rpm 은 Motor 블록의 Revolutions.
min_flight_time_min = eCalc "min. Flight Time"(도움말: 최대 스로틀 기준, 배터리 max. discharge % 적용, 중량과 무관).
motor.cooling 은 excellent|good|medium|poor|verypoor (eCalc 냉각 선택값).
motor.maximum_limit_unit 은 "A" 또는 "W" (maximum_limit 이 null 이면 "").
-->
