#!/usr/bin/env python3
"""validate-ecalc-run.py — eCalc xcopterCalc 계산 기록·예측/실측 비교 기록 검증기.

대상 템플릿:
  templates/ecalc-xcoptercalc-run.md                        (기본 모드)
  templates/propulsion-prediction-measurement-comparison.md (--comparison)

원칙: 입력이 불완전하면 보정하지 않고 실패한다. 누락값을 0·최근값·평균으로
채우지 않고, 파일을 수정하지도 않는다(읽기 전용). 표준 라이브러리만 사용한다.

실행:
  python3 scripts/validate-ecalc-run.py <run.md> [<run2.md> ...]
  python3 scripts/validate-ecalc-run.py --comparison <comparison.md>
  python3 scripts/validate-ecalc-run.py --strict <run.md>   # blocked_fields 도 허용하지 않음

종료 코드: 0 전부 통과 / 1 검증 실패 / 2 사용법·읽기·파싱 오류
"""
from __future__ import annotations

import argparse
import math
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

ECALC_NAME = "eCalc xcopterCalc"
ECALC_URL = "https://www.ecalc.ch/xcoptercalc.php"
CONFIDENCE = {"low", "medium", "high"}
COMPARISON_STATUS = {"not_compared", "compared"}
CONFIGURATIONS = {"", "flat", "coax"}
LIMIT_UNITS = {"", "A", "W"}
COOLING = {"", "excellent", "good", "medium", "poor", "verypoor"}
MEASUREMENT_SOURCES = {
    "static_thrust_stand", "ammeter", "power_module", "px4_ulog",
    "ardupilot_bin", "fc_telemetry", "battery_log", "motor_temperature_sensor",
}

# 섹션별 필드 정의. 키 집합은 정확히 일치해야 하며, 접미사 단위가 다른 키(예: diameter_mm)는 미지 키로 실패한다.
SCHEMA: dict[str, dict[str, str]] = {
    "calculator": {"name": "str", "url": "str", "version": "str",
                   "calculation_date": "str", "accuracy_statement": "str"},
    "airframe": {"rotor_count": "int+", "configuration": "str", "frame_size_mm": "num+",
                 "all_up_weight_g": "num+", "tilt_limit_deg": "tilt",
                 "accessories_current_a": "num0", "accessories_weight_g": "num0"},
    "environment": {"elevation_m": "elev", "temperature_c": "temp", "pressure_hpa": "pres"},
    "battery": {"cell_type": "str", "cells_s": "int+", "parallel_p": "int+",
                "cell_capacity_mah": "num+", "total_capacity_mah": "num+",
                "discharge_fraction": "frac", "internal_resistance_ohm": "num+",
                "voltage_per_cell": "num+", "continuous_c_rating": "num+",
                "maximum_c_rating": "num+", "weight_g": "num+"},
    "esc": {"model": "str", "continuous_current_a": "num+", "maximum_current_a": "num+",
            "resistance_ohm": "num+", "weight_g": "num+"},
    "motor": {"manufacturer": "str", "model": "str", "cooling": "str", "kv_rpm_per_v": "num+",
              "no_load_current_a": "num+", "no_load_voltage_v": "num+",
              "maximum_limit": "num+", "maximum_limit_unit": "str",
              "resistance_ohm": "num+", "case_length_mm": "num+",
              "magnetic_poles": "int+", "weight_g": "num+"},
    "propeller": {"manufacturer": "str", "model": "str", "diameter_in": "num+",
                  "pitch_in": "num+", "blades": "int+", "pconst": "num+",
                  "tconst": "num+", "gear_ratio": "num+"},
    "results": {"battery_load_c": "num0", "battery_voltage_v": "num0",
                "battery_rated_voltage_v": "num0",
                "battery_energy_wh": "num0", "min_flight_time_min": "num+",
                "hover_flight_time_min": "num+",
                "mixed_flight_time_min": "num+", "hover_current_a": "num0",
                "hover_power_w": "num0", "hover_motor_rpm": "num0",
                "maximum_current_a": "num0", "maximum_power_w": "num0",
                "maximum_motor_rpm": "num0", "thrust_weight_ratio": "num+",
                "specific_thrust_g_per_w": "num0", "estimated_motor_temperature_c": "temp_est",
                "maximum_rate_of_climb_mps": "num0", "maximum_speed_kmh": "num0",
                "estimated_range_m": "num0"},
    "validation": {"source_of_component_data": "str", "measured_thrust_test_available": "bool",
                   "flight_log_available": "bool", "comparison_status": "str",
                   "confidence": "str", "blocked_fields": "list", "notes": "str"},
}
# blocked_fields 대상 섹션(validation 은 메타라서 제외)
TRACKED = [s for s in SCHEMA if s != "validation"]
# 계산에 반드시 필요한 입력 — null 이면 blocked 로도 허용하지 않고 실패.
REQUIRED_INPUTS = [
    "airframe.rotor_count", "airframe.all_up_weight_g", "battery.cells_s",
    "battery.parallel_p", "motor.kv_rpm_per_v", "propeller.diameter_in",
    "propeller.pitch_in", "propeller.blades",
]
# 의심스러운 예측/실측 혼합 키 접두사
MEASURED_PREFIXES = ("measured", "actual", "logged", "observed", "test_")

COMPARISON_UNITS = {
    "hover_current": "A", "hover_power": "W", "maximum_current": "A",
    "maximum_power": "W", "motor_rpm_hover": "rpm", "motor_rpm_maximum": "rpm", "thrust": "g",
    "thrust_weight_ratio": "ratio", "flight_time": "min",
    "motor_temperature": "C", "battery_voltage_drop": "V",
}
COMPARISON_ITEM_KEYS = {
    "predicted_value", "measured_value", "unit", "absolute_error",
    "relative_error_percent", "measurement_source", "measurement_date", "confidence",
}
# 비교 항목 → run 기록 results 필드(예측값 출처). 목록에 없는 항목은 출처 교차검증 불가.
RUN_RESULT_FOR = {
    "hover_current": ["hover_current_a"], "hover_power": ["hover_power_w"],
    "maximum_current": ["maximum_current_a"], "maximum_power": ["maximum_power_w"],
    "motor_rpm_hover": ["hover_motor_rpm"], "motor_rpm_maximum": ["maximum_motor_rpm"],
    "thrust_weight_ratio": ["thrust_weight_ratio"],
    "flight_time": ["hover_flight_time_min", "mixed_flight_time_min"],
    "motor_temperature": ["estimated_motor_temperature_c"],
}


class ParseError(Exception):
    pass


# ---------------------------------------------------------------- YAML 부분집합
def _scalar(tok: str, lineno: int):
    tok = tok.strip()
    if tok in ("null", "~", ""):
        return None
    if tok == "true":
        return True
    if tok == "false":
        return False
    if len(tok) >= 2 and tok[0] == tok[-1] and tok[0] in "\"'":
        return tok[1:-1].replace('\\"', '"') if tok[0] == '"' else tok[1:-1]
    if re.fullmatch(r"[+-]?\d+", tok):
        return int(tok)
    if re.fullmatch(r"[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?", tok):
        return float(tok)
    if tok.startswith("[") and tok.endswith("]"):
        inner = tok[1:-1].strip()
        if not inner:
            return []
        parts, buf, quote = [], "", ""
        for ch in inner:
            if quote:
                buf += ch
                if ch == quote:
                    quote = ""
            elif ch in "\"'":
                quote = ch
                buf += ch
            elif ch == ",":
                parts.append(buf)
                buf = ""
            else:
                buf += ch
        parts.append(buf)
        return [_scalar(p, lineno) for p in parts]
    if tok[0] in "{|>&*!%@`":
        raise ParseError(f"line {lineno}: 지원하지 않는 YAML 구문 {tok[:20]!r}")
    return tok  # 따옴표 없는 문자열(예: 날짜)


def _strip_comment(line: str) -> str:
    quote = ""
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = ""
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            return line[:i]
    return line


def parse_yaml_subset(text: str) -> dict:
    """들여쓰기 2칸 매핑 + 스칼라 + 인라인 리스트만 지원하는 엄격 파서."""
    rows = []
    for n, raw in enumerate(text.split("\n"), 1):
        line = _strip_comment(raw).rstrip()
        if not line.strip():
            continue
        if "\t" in line[: len(line) - len(line.lstrip())]:
            raise ParseError(f"line {n}: 탭 들여쓰기 불가")
        indent = len(line) - len(line.lstrip(" "))
        if indent % 2:
            raise ParseError(f"line {n}: 들여쓰기는 2칸 단위")
        m = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_]*):(?:\s+(.*))?", line.strip())
        if not m:
            raise ParseError(f"line {n}: 'key: value' 형식이 아님: {line.strip()[:40]!r}")
        rows.append((n, indent, m.group(1), m.group(2)))

    root: dict = {}
    stack = [(-2, root)]  # (indent, mapping)
    for idx, (n, indent, key, val) in enumerate(rows):
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if not stack:
            raise ParseError(f"line {n}: 들여쓰기 오류")
        parent = stack[-1][1]
        if key in parent:
            raise ParseError(f"line {n}: 중복 키 {key!r}")
        if val is None or val == "":
            nxt = rows[idx + 1] if idx + 1 < len(rows) else None
            if nxt and nxt[1] > indent:
                child: dict = {}
                parent[key] = child
                stack.append((indent, child))
            else:
                parent[key] = None
        else:
            parent[key] = _scalar(val, n)
    return root


def read_frontmatter(path: Path) -> dict:
    try:
        raw = path.read_bytes().decode("utf-8")
    except OSError as e:
        raise ParseError(f"읽기 실패: {e}")
    except UnicodeDecodeError as e:
        raise ParseError(f"UTF-8 아님: {e}")
    if not raw.startswith("---\n"):
        raise ParseError("파일이 frontmatter('---')로 시작하지 않음")
    end = raw.find("\n---\n", 4)
    if end < 0:
        raise ParseError("frontmatter 종료 '---' 없음")
    return parse_yaml_subset(raw[4:end])


# ---------------------------------------------------------------- 공통 판정
def is_num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def is_date(v) -> bool:
    if not isinstance(v, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        return False
    try:
        date.fromisoformat(v)
        return True
    except ValueError:
        return False


def _check_value(path: str, kind: str, v, errs: list[str]) -> None:
    """None/"" 은 호출 전에 걸러진다. 여기서는 값이 있을 때의 형식·범위만 본다."""
    if kind == "str":
        if not isinstance(v, str):
            errs.append(f"{path}: 문자열이어야 함 (값 {v!r})")
        return
    if kind == "bool":
        if not isinstance(v, bool):
            errs.append(f"{path}: true/false 이어야 함 (값 {v!r})")
        return
    if not is_num(v):
        errs.append(f"{path}: 숫자(단위 없는 값)여야 함 (값 {v!r}) — 단위는 필드명 접미사가 정한다")
        return
    if kind == "int+":
        if not (isinstance(v, int) and v > 0):
            errs.append(f"{path}: 양의 정수여야 함 (값 {v!r})")
    elif kind == "num+":
        if not v > 0:
            errs.append(f"{path}: 0보다 커야 함 (값 {v!r})")
    elif kind == "num0":
        if v < 0:
            errs.append(f"{path}: 음수 불가 (값 {v!r})")
    elif kind == "tilt":
        if not 0 < v <= 90:
            errs.append(f"{path}: 0 초과 90 이하 도(deg) (값 {v!r})")
    elif kind == "elev":
        if not -500 <= v <= 9000:
            errs.append(f"{path}: -500~9000 m 범위 밖 (값 {v!r})")
    elif kind == "temp":
        if not -60 <= v <= 70:
            errs.append(f"{path}: -60~70 °C 범위 밖 (값 {v!r})")
    elif kind == "temp_est":
        if not -60 <= v <= 300:
            errs.append(f"{path}: -60~300 °C 범위 밖 (값 {v!r})")
    elif kind == "pres":
        if not 300 <= v <= 1100:
            errs.append(f"{path}: 300~1100 hPa 범위 밖 (값 {v!r})")
    elif kind == "frac":
        if not 0 < v <= 1:
            errs.append(f"{path}: 0 초과 1 이하 비율이어야 함 — 퍼센트가 아님 (값 {v!r})")


def _is_missing(v) -> bool:
    return v is None or v == ""


# ---------------------------------------------------------------- 실행 기록 검증
def validate_run(data: dict, strict: bool = False) -> list[str]:
    errs: list[str] = []
    top_extra = set(data) - set(SCHEMA)
    top_missing = set(SCHEMA) - set(data)
    if top_missing:
        errs.append(f"필수 섹션 누락: {sorted(top_missing)}")
    if top_extra:
        errs.append(f"알 수 없는 최상위 키: {sorted(top_extra)}")

    values: dict[str, object] = {}  # 점 표기 경로 → 값
    for sec, fields in SCHEMA.items():
        body = data.get(sec)
        if not isinstance(body, dict):
            if sec in data:
                errs.append(f"{sec}: 매핑이어야 함")
            continue
        missing_keys = set(fields) - set(body)
        extra_keys = set(body) - set(fields)
        if missing_keys:
            errs.append(f"{sec}: 필수 필드 누락 {sorted(missing_keys)}")
        for k in sorted(extra_keys):
            hint = " (예측/실측 혼합 의심)" if k.startswith(MEASURED_PREFIXES) else " (단위 접미사 불일치 또는 오타 가능)"
            errs.append(f"{sec}.{k}: 정의되지 않은 필드{hint}")
        for k, kind in fields.items():
            if k not in body:
                continue
            p = f"{sec}.{k}"
            v = body[k]
            values[p] = v
            if kind == "list":
                if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                    errs.append(f"{p}: 문자열 리스트여야 함")
            elif not _is_missing(v):
                _check_value(p, kind, v, errs)

    if errs and any(e.startswith(("필수 섹션", "알 수 없는")) for e in errs):
        return errs  # 구조가 깨졌으면 이후 교차검증은 의미 없음

    g = values.get
    # --- 출처 고정값
    if g("calculator.name") != ECALC_NAME:
        errs.append(f"calculator.name: {ECALC_NAME!r} 이어야 함 (값 {g('calculator.name')!r})")
    if g("calculator.url") != ECALC_URL:
        errs.append(f"calculator.url: 정확히 {ECALC_URL!r} 이어야 함 (값 {g('calculator.url')!r})")
    d = g("calculator.calculation_date")
    if not _is_missing(d) and not is_date(d):
        errs.append(f"calculator.calculation_date: YYYY-MM-DD 형식이어야 함 (값 {d!r})")

    # --- 열거형
    if (g("airframe.configuration") or "") not in CONFIGURATIONS:
        errs.append(f"airframe.configuration: {sorted(CONFIGURATIONS - {''})} 중 하나 (값 {g('airframe.configuration')!r})")
    if (g("motor.cooling") or "") not in COOLING:
        errs.append(f"motor.cooling: {sorted(COOLING - {''})} 중 하나 (값 {g('motor.cooling')!r})")
    if (g("motor.maximum_limit_unit") or "") not in LIMIT_UNITS:
        errs.append(f"motor.maximum_limit_unit: 'A' 또는 'W' 만 허용 (값 {g('motor.maximum_limit_unit')!r})")
    if not _is_missing(g("motor.maximum_limit")) and _is_missing(g("motor.maximum_limit_unit")):
        errs.append("motor.maximum_limit 이 있으면 maximum_limit_unit('A'|'W')이 필요함")
    if _is_missing(g("motor.maximum_limit")) and not _is_missing(g("motor.maximum_limit_unit")):
        errs.append("motor.maximum_limit 이 없는데 maximum_limit_unit 만 채워져 있음")
    if g("validation.confidence") not in CONFIDENCE:
        errs.append(f"validation.confidence: {sorted(CONFIDENCE)} 중 하나 (값 {g('validation.confidence')!r})")
    status = g("validation.comparison_status")
    if status not in COMPARISON_STATUS:
        errs.append(f"validation.comparison_status: {sorted(COMPARISON_STATUS)} 중 하나 (값 {status!r})")

    # --- 비교 상태 일관성: 실측 수단이 없으면 not_compared 유지
    has_meas = g("validation.measured_thrust_test_available") is True or g("validation.flight_log_available") is True
    if status == "compared" and not has_meas:
        errs.append("comparison_status 'compared' 인데 실측 가용 플래그가 모두 false")

    # --- 필수 입력
    for p in REQUIRED_INPUTS:
        if _is_missing(values.get(p)):
            errs.append(f"{p}: 필수 입력이 비어 있음 (0·추정값으로 채우지 않는다)")

    # --- 결과는 입력 없이 채워질 수 없다
    results_filled = [p for p in values if p.startswith("results.") and not _is_missing(values[p])]
    if results_filled:
        missing_req = [p for p in REQUIRED_INPUTS if _is_missing(values.get(p))]
        if missing_req:
            errs.append(f"results 가 채워져 있으나 필수 입력 누락({missing_req}) — 입력 없는 결과는 인정 불가")
        if _is_missing(g("calculator.calculation_date")):
            errs.append("results 가 채워져 있으나 calculator.calculation_date 가 비어 있음")

    # --- 일관성(수정하지 않고 불일치만 보고)
    cap, par, tot = g("battery.cell_capacity_mah"), g("battery.parallel_p"), g("battery.total_capacity_mah")
    if is_num(cap) and is_num(par) and is_num(tot) and not math.isclose(cap * par, tot, rel_tol=0.01):
        errs.append(f"battery.total_capacity_mah({tot}) != cell_capacity_mah*parallel_p({cap * par})")
    for lo, hi in (("esc.continuous_current_a", "esc.maximum_current_a"),
                   ("battery.continuous_c_rating", "battery.maximum_c_rating")):
        a, b = g(lo), g(hi)
        if is_num(a) and is_num(b) and a > b:
            errs.append(f"{lo}({a}) 가 {hi}({b}) 보다 큼")

    # --- blocked_fields == 실제 누락 필드(필수 입력 제외)
    blocked = g("validation.blocked_fields")
    if isinstance(blocked, list):
        known = {f"{s}.{k}" for s in TRACKED for k in SCHEMA[s]}
        for b in blocked:
            if b not in known:
                errs.append(f"validation.blocked_fields: 알 수 없는 경로 {b!r}")
        if len(set(blocked)) != len(blocked):
            errs.append("validation.blocked_fields: 중복 항목")
        actual_missing = {p for p in values if p.split(".")[0] in TRACKED and _is_missing(values[p])
                          and p not in REQUIRED_INPUTS}
        declared = set(blocked) & known
        for p in sorted(declared - actual_missing):
            errs.append(f"validation.blocked_fields: {p} 는 값이 있거나 필수 입력이라 blocked 불가")
        for p in sorted(actual_missing - declared):
            errs.append(f"{p}: 비어 있으나 validation.blocked_fields 에 선언되지 않음")
        if strict and actual_missing:
            errs.append(f"--strict: 누락 필드 {len(actual_missing)}개 존재")
    return errs


# ---------------------------------------------------------------- 비교 기록 검증
def validate_comparison(data: dict, repo_root: Path = REPO_ROOT) -> list[str]:
    errs: list[str] = []
    if set(data) != {"run_ref", "comparison"}:
        return [f"최상위 키는 run_ref, comparison 만 허용 (현재 {sorted(data)})"]
    run_ref = data["run_ref"]
    comp = data["comparison"]
    if not isinstance(comp, dict):
        return ["comparison: 매핑이어야 함"]
    if set(comp) != set(COMPARISON_UNITS):
        errs.append(f"comparison 항목 불일치: 누락 {sorted(set(COMPARISON_UNITS) - set(comp))}, 초과 {sorted(set(comp) - set(COMPARISON_UNITS))}")

    run_results: dict = {}
    any_pred = any(isinstance(it, dict) and it.get("predicted_value") is not None for it in comp.values())
    if any_pred:
        if _is_missing(run_ref):
            errs.append("predicted_value 가 있으나 run_ref 가 비어 있음")
        else:
            rp = (repo_root / str(run_ref)).resolve()
            try:
                rp.relative_to(repo_root.resolve())
            except ValueError:
                errs.append(f"run_ref 가 저장소 밖을 가리킴: {run_ref!r}")
                rp = None
            if rp is not None:
                if not rp.is_file():
                    errs.append(f"run_ref 파일 없음: {run_ref!r}")
                else:
                    try:
                        run_data = read_frontmatter(rp)
                        run_errs = validate_run(run_data)
                        if run_errs:
                            errs.append(f"run_ref 기록이 검증에 실패함 ({len(run_errs)}건) — 먼저 run 기록을 고칠 것")
                        run_results = run_data.get("results", {}) if isinstance(run_data.get("results"), dict) else {}
                    except ParseError as e:
                        errs.append(f"run_ref 파싱 실패: {e}")

    for name, unit in COMPARISON_UNITS.items():
        it = comp.get(name)
        if it is None:
            continue
        if not isinstance(it, dict):
            errs.append(f"{name}: 매핑이어야 함")
            continue
        if set(it) != COMPARISON_ITEM_KEYS:
            errs.append(f"{name}: 키 불일치 누락 {sorted(COMPARISON_ITEM_KEYS - set(it))} 초과 {sorted(set(it) - COMPARISON_ITEM_KEYS)}")
            continue
        pred, meas = it["predicted_value"], it["measured_value"]
        if it["unit"] != unit:
            errs.append(f"{name}.unit: {unit!r} 이어야 함 (값 {it['unit']!r})")
        if it["confidence"] not in CONFIDENCE:
            errs.append(f"{name}.confidence: {sorted(CONFIDENCE)} 중 하나 (값 {it['confidence']!r})")
        for fld, v in (("predicted_value", pred), ("measured_value", meas)):
            if v is not None and (not is_num(v) or (name != "motor_temperature" and v < 0)):
                errs.append(f"{name}.{fld}: 숫자(음수 불가)여야 함 (값 {v!r})")
        pred_ok, meas_ok = is_num(pred), is_num(meas)

        # 실측 메타데이터는 measured_value 가 있을 때만 존재해야 한다
        if meas is None:
            for fld in ("absolute_error", "relative_error_percent"):
                if it[fld] is not None:
                    errs.append(f"{name}.{fld}: measured_value 없이 오차를 적을 수 없음")
            for fld in ("measurement_source", "measurement_date"):
                if not _is_missing(it[fld]):
                    errs.append(f"{name}.{fld}: measured_value 없이 실측 출처·일자를 적을 수 없음")
            if it["confidence"] != "low":
                errs.append(f"{name}.confidence: 실측이 없으면 'low' 이어야 함")
        else:
            if it["measurement_source"] not in MEASUREMENT_SOURCES:
                errs.append(f"{name}.measurement_source: 허용 목록 {sorted(MEASUREMENT_SOURCES)} 중 하나 (값 {it['measurement_source']!r})")
            if not is_date(it["measurement_date"]):
                errs.append(f"{name}.measurement_date: YYYY-MM-DD (값 {it['measurement_date']!r})")
        if pred is None and meas is not None:
            for fld in ("absolute_error", "relative_error_percent"):
                if it[fld] is not None:
                    errs.append(f"{name}.{fld}: predicted_value 없이 오차를 적을 수 없음")

        # 오차 재계산 — 틀리면 실패, 고쳐 쓰지 않는다
        if pred_ok and meas_ok:
            abs_err = abs(pred - meas)
            if not is_num(it["absolute_error"]):
                errs.append(f"{name}.absolute_error: 예측·실측이 모두 있으면 필수")
            elif not math.isclose(it["absolute_error"], abs_err, rel_tol=0.01, abs_tol=0.01):
                errs.append(f"{name}.absolute_error: |pred-meas|={abs_err:.4g} 와 불일치 (값 {it['absolute_error']!r})")
            if meas == 0:
                if it["relative_error_percent"] is not None:
                    errs.append(f"{name}.relative_error_percent: 실측 0 에서는 null 이어야 함")
            elif not is_num(it["relative_error_percent"]):
                errs.append(f"{name}.relative_error_percent: 예측·실측이 모두 있으면 필수")
            elif not math.isclose(it["relative_error_percent"], abs_err / abs(meas) * 100, rel_tol=0.01, abs_tol=0.01):
                errs.append(f"{name}.relative_error_percent: {abs_err / abs(meas) * 100:.4g} 와 불일치 (값 {it['relative_error_percent']!r})")

        # 예측값 출처 교차검증: eCalc 결과 외의 값을 predicted 에 넣으면 혼합
        if pred_ok and name in RUN_RESULT_FOR and run_results:
            cands = [run_results.get(f) for f in RUN_RESULT_FOR[name] if is_num(run_results.get(f))]
            if not cands:
                errs.append(f"{name}.predicted_value: run_ref 의 {RUN_RESULT_FOR[name]} 가 비어 있어 출처 확인 불가")
            elif not any(math.isclose(pred, c, rel_tol=1e-6, abs_tol=1e-9) for c in cands):
                errs.append(f"{name}.predicted_value({pred}) 가 run_ref 의 eCalc 결과 {cands} 와 다름 — 예측값은 eCalc 결과만 허용")
    return errs


# ---------------------------------------------------------------- CLI
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="eCalc 계산 기록·비교 기록 검증기 (읽기 전용, 보정 없음)")
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--comparison", action="store_true", help="예측/실측 비교 기록 검증")
    ap.add_argument("--strict", action="store_true", help="누락 필드가 하나라도 있으면 실패(run 모드)")
    args = ap.parse_args(argv)

    worst = 0
    for path in args.paths:
        try:
            data = read_frontmatter(path)
        except ParseError as e:
            print(f"ERROR {path}: {e}")
            worst = 2
            continue
        errs = validate_comparison(data) if args.comparison else validate_run(data, strict=args.strict)
        if errs:
            print(f"FAIL {path} ({len(errs)}건)")
            for e in errs:
                print(f"  - {e}")
            worst = max(worst, 1)
        else:
            print(f"OK   {path}")
    return worst


if __name__ == "__main__":
    sys.exit(main())
