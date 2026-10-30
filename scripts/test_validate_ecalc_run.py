#!/usr/bin/env python3
"""test_validate_ecalc_run.py — validate-ecalc-run.py 단위 테스트.

저장소 관례(test_lint_knowledge.py 등)대로 표준 라이브러리 + assert 기반.
실행:
  python3 scripts/test_validate_ecalc_run.py
"""
import copy
import importlib.util
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("validate_ecalc_run", HERE / "validate-ecalc-run.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

TEMPLATE_RUN = HERE.parent / "templates" / "ecalc-xcoptercalc-run.md"
TEMPLATE_CMP = HERE.parent / "templates" / "propulsion-prediction-measurement-comparison.md"


def template_data():
    return v.read_frontmatter(TEMPLATE_RUN)


def filled_run():
    """필수 입력 + 일부 결과를 채운 유효 기록. 나머지는 blocked 로 선언한다."""
    d = template_data()
    d["calculator"].update(calculation_date="2026-10-30", version="test-fixture")
    d["airframe"].update(rotor_count=4, all_up_weight_g=850, configuration="flat")
    d["battery"].update(cells_s=3, parallel_p=1, cell_capacity_mah=2200, total_capacity_mah=2200)
    d["motor"].update(kv_rpm_per_v=920)
    d["propeller"].update(diameter_in=10, pitch_in=4.7, blades=2)
    d["results"].update(hover_current_a=12.5, thrust_weight_ratio=2.1, hover_motor_rpm=5200)
    missing = [f"{s}.{k}" for s in v.TRACKED for k, val in d[s].items()
               if val is None or val == ""]
    missing = [m for m in missing if m not in v.REQUIRED_INPUTS]
    d["validation"]["blocked_fields"] = missing
    return d


def dump(d):
    """테스트 입력을 파서가 읽는 YAML 부분집합으로 직렬화."""
    def sc(x):
        if x is None:
            return "null"
        if isinstance(x, bool):
            return "true" if x else "false"
        if isinstance(x, (int, float)):
            return repr(x)
        if isinstance(x, list):
            return "[" + ", ".join(sc(i) for i in x) + "]"
        return '"' + str(x).replace('"', '\\"') + '"'

    def walk(m, ind):
        out = []
        for k, val in m.items():
            if isinstance(val, dict):
                out.append(" " * ind + f"{k}:")
                out += walk(val, ind + 2)
            else:
                out.append(" " * ind + f"{k}: {sc(val)}")
        return out
    return "---\n" + "\n".join(walk(d, 0)) + "\n---\n"


def run_errs(d, **kw):
    return v.validate_run(v.parse_yaml_subset(dump(d)[4:-5]), **kw)


def has(errs, needle):
    return any(needle in e for e in errs)


def test_template_files_parse_and_fail_as_incomplete():
    d = template_data()
    errs = v.validate_run(d)
    assert has(errs, "airframe.rotor_count: 필수 입력"), errs
    assert has(errs, "propeller.diameter_in: 필수 입력"), errs
    # 템플릿은 모르는 값을 null 로 둔 채 검증을 통과해서는 안 된다
    assert errs
    assert d["validation"]["comparison_status"] == "not_compared"


def test_valid_record_passes():
    assert run_errs(filled_run()) == []


def test_missing_required_input_fails_without_substitution():
    d = filled_run()
    d["propeller"]["pitch_in"] = None
    errs = run_errs(d)
    assert has(errs, "propeller.pitch_in: 필수 입력"), errs
    # 0 으로 메워도 통과하면 안 된다
    d["propeller"]["pitch_in"] = 0
    assert has(run_errs(d), "propeller.pitch_in: 0보다 커야 함")


def test_wrong_units_fail():
    d = filled_run()
    d["propeller"]["diameter_in"] = "10 inch"
    assert has(run_errs(d), "propeller.diameter_in: 숫자"), "문자열 단위 값"
    d = filled_run()
    d["propeller"]["diameter_mm"] = 254
    assert has(run_errs(d), "propeller.diameter_mm: 정의되지 않은 필드")
    d = filled_run()
    d["motor"]["maximum_limit"] = 60
    d["motor"]["maximum_limit_unit"] = "kW"
    d["validation"]["blocked_fields"] = [b for b in d["validation"]["blocked_fields"]
                                         if not b.startswith("motor.maximum_limit")]
    assert has(run_errs(d), "maximum_limit_unit: 'A' 또는 'W'")
    d = filled_run()
    d["battery"]["discharge_fraction"] = 80  # 퍼센트로 잘못 기입
    d["validation"]["blocked_fields"].remove("battery.discharge_fraction")
    assert has(run_errs(d), "battery.discharge_fraction: 0 초과 1 이하")


def test_nonpositive_counts_fail():
    for path, val in (("battery.cells_s", 0), ("battery.parallel_p", -1), ("airframe.rotor_count", 4.5)):
        d = filled_run()
        s, k = path.split(".")
        d[s][k] = val
        assert has(run_errs(d), f"{path}: 양의 정수"), (path, val)


def test_results_without_inputs_fail():
    d = filled_run()
    d["battery"]["cells_s"] = None
    d["validation"]["blocked_fields"] = [b for b in d["validation"]["blocked_fields"] if b != "battery.cells_s"]
    errs = run_errs(d)
    assert has(errs, "results 가 채워져 있으나 필수 입력 누락"), errs
    d = filled_run()
    d["calculator"]["calculation_date"] = ""
    d["validation"]["blocked_fields"].append("calculator.calculation_date")
    assert has(run_errs(d), "calculation_date 가 비어 있음")


def test_blocked_fields_must_match_missing():
    d = filled_run()
    d["validation"]["blocked_fields"].remove("battery.internal_resistance_ohm")
    assert has(run_errs(d), "battery.internal_resistance_ohm: 비어 있으나")
    d = filled_run()
    d["validation"]["blocked_fields"].append("results.hover_current_a")  # 값이 있는 필드
    assert has(run_errs(d), "results.hover_current_a 는 값이 있거나")
    d = filled_run()
    d["validation"]["blocked_fields"].append("battery.nonexistent")
    assert has(run_errs(d), "알 수 없는 경로")
    assert has(run_errs(filled_run(), strict=True), "--strict")


def test_confidence_and_status():
    d = filled_run()
    d["validation"]["confidence"] = "certain"
    assert has(run_errs(d), "validation.confidence")
    d = filled_run()
    d["validation"]["comparison_status"] = "compared"  # 실측 플래그 모두 false
    assert has(run_errs(d), "'compared' 인데")
    d = filled_run()
    d["validation"]["comparison_status"] = "done"
    assert has(run_errs(d), "validation.comparison_status")
    assert filled_run()["validation"]["comparison_status"] == "not_compared"


def test_cooling_enum_and_min_flight_time_field():
    d = filled_run()
    d["motor"]["cooling"] = "great"
    assert has(run_errs(d), "motor.cooling")
    d = filled_run()
    assert "min_flight_time_min" in d["results"] and "accessories_current_a" in d["airframe"]


def test_url_must_match_exactly():
    d = filled_run()
    d["calculator"]["url"] = "https://www.ecalc.ch/xcoptercalc.php?x=1"
    assert has(run_errs(d), "calculator.url")
    d = filled_run()
    d["calculator"]["url"] = "http://www.ecalc.ch/xcoptercalc.php"
    assert has(run_errs(d), "calculator.url")


def test_measured_keys_in_run_are_rejected_as_mixing():
    d = filled_run()
    d["results"]["measured_hover_current_a"] = 13.0
    errs = run_errs(d)
    assert has(errs, "예측/실측 혼합 의심"), errs


def test_consistency_checks():
    d = filled_run()
    d["battery"]["total_capacity_mah"] = 5000
    assert has(run_errs(d), "total_capacity_mah")
    d = filled_run()
    d["esc"]["continuous_current_a"] = 40
    d["esc"]["maximum_current_a"] = 30
    for p in ("esc.continuous_current_a", "esc.maximum_current_a"):
        if p in d["validation"]["blocked_fields"]:
            d["validation"]["blocked_fields"].remove(p)
    assert has(run_errs(d), "보다 큼")


def test_parser_rejects_unsupported_yaml():
    for bad in ("a:\n\tb: 1", "a: {x: 1}", "a: 1\na: 2", "a:\n   b: 1", "just text"):
        try:
            v.parse_yaml_subset(bad)
        except v.ParseError:
            continue
        raise AssertionError(f"파서가 거부해야 함: {bad!r}")


def test_file_is_never_modified():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "run.md"
        p.write_text(dump(template_data()) + "\n본문\n", encoding="utf-8")
        before = p.read_bytes()
        assert v.main([str(p)]) == 1
        assert p.read_bytes() == before


def test_cli_exit_codes():
    with tempfile.TemporaryDirectory() as td:
        ok = Path(td) / "ok.md"
        ok.write_text(dump(filled_run()), encoding="utf-8")
        assert v.main([str(ok)]) == 0
        nofm = Path(td) / "nofm.md"
        nofm.write_text("no frontmatter", encoding="utf-8")
        assert v.main([str(nofm)]) == 2
        assert v.main([str(Path(td) / "missing.md")]) == 2


# ---------------------------------------------------------------- 비교 기록
def comparison_with_run(td):
    run = filled_run()
    run_path = Path(td) / "runs" / "r1.md"
    run_path.parent.mkdir(parents=True, exist_ok=True)
    run_path.write_text(dump(run), encoding="utf-8")
    cmp_ = v.read_frontmatter(TEMPLATE_CMP)
    cmp_["run_ref"] = "runs/r1.md"
    return cmp_


def test_comparison_template_is_valid_and_not_compared():
    data = v.read_frontmatter(TEMPLATE_CMP)
    assert v.validate_comparison(data) == []
    assert all(it["measured_value"] is None and it["predicted_value"] is None
               for it in data["comparison"].values())


def test_comparison_valid_with_measurement():
    with tempfile.TemporaryDirectory() as td:
        c = comparison_with_run(td)
        it = c["comparison"]["hover_current"]
        it.update(predicted_value=12.5, measured_value=14.0, absolute_error=1.5,
                  relative_error_percent=round(1.5 / 14.0 * 100, 4),
                  measurement_source="power_module", measurement_date="2026-10-30", confidence="medium")
        assert v.validate_comparison(c, repo_root=Path(td)) == []


def test_comparison_rejects_wrong_error_and_unlisted_source():
    with tempfile.TemporaryDirectory() as td:
        c = comparison_with_run(td)
        it = c["comparison"]["hover_current"]
        it.update(predicted_value=12.5, measured_value=14.0, absolute_error=9.0,
                  relative_error_percent=1.0, measurement_source="guess", measurement_date="2026-10-30")
        errs = v.validate_comparison(c, repo_root=Path(td))
        assert has(errs, "absolute_error"), errs
        assert has(errs, "relative_error_percent"), errs
        assert has(errs, "measurement_source"), errs


def test_comparison_rejects_prediction_not_from_ecalc_run():
    with tempfile.TemporaryDirectory() as td:
        c = comparison_with_run(td)
        c["comparison"]["hover_current"]["predicted_value"] = 11.0  # run 의 12.5 와 다름
        errs = v.validate_comparison(c, repo_root=Path(td))
        assert has(errs, "eCalc 결과"), errs


def test_comparison_motor_rpm_checked_against_run():
    with tempfile.TemporaryDirectory() as td:
        c = comparison_with_run(td)
        c["comparison"]["motor_rpm_hover"]["predicted_value"] = 5200
        assert v.validate_comparison(c, repo_root=Path(td)) == []
        c["comparison"]["motor_rpm_hover"]["predicted_value"] = 6000
        assert has(v.validate_comparison(c, repo_root=Path(td)), "eCalc 결과")
        c["comparison"]["motor_rpm_hover"]["predicted_value"] = None
        c["comparison"]["motor_rpm_maximum"]["predicted_value"] = 5200  # hover 값을 maximum 항목에 넣음
        assert has(v.validate_comparison(c, repo_root=Path(td)), "run_ref 의"), "운영점 혼동"


def test_comparison_without_measurement_stays_empty():
    with tempfile.TemporaryDirectory() as td:
        c = comparison_with_run(td)
        it = c["comparison"]["hover_current"]
        it.update(predicted_value=12.5, absolute_error=0.0)
        assert has(v.validate_comparison(c, repo_root=Path(td)), "measured_value 없이 오차")
        it.update(absolute_error=None, measurement_source="ammeter")
        assert has(v.validate_comparison(c, repo_root=Path(td)), "measured_value 없이 실측 출처")
        it.update(measurement_source="", confidence="high")
        assert has(v.validate_comparison(c, repo_root=Path(td)), "실측이 없으면 'low'")


def test_comparison_wrong_unit_and_missing_run_ref():
    with tempfile.TemporaryDirectory() as td:
        c = comparison_with_run(td)
        c["comparison"]["hover_power"]["unit"] = "kW"
        assert has(v.validate_comparison(c, repo_root=Path(td)), "hover_power.unit")
        c = comparison_with_run(td)
        c["comparison"]["hover_current"]["predicted_value"] = 12.5
        c["run_ref"] = ""
        assert has(v.validate_comparison(c, repo_root=Path(td)), "run_ref 가 비어 있음")
        c["run_ref"] = "runs/none.md"
        assert has(v.validate_comparison(c, repo_root=Path(td)), "run_ref 파일 없음")
        c["run_ref"] = "../../etc/passwd"
        assert has(v.validate_comparison(c, repo_root=Path(td)), "저장소 밖")


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"PASS {name}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"FAIL {name}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    raise SystemExit(1 if failed else 0)
