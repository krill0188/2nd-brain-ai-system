#!/usr/bin/env python3
"""test_innovation_combine.py — Cross-Domain Scan 노드쌍 선택기 단위 테스트."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import innovation_combine as ic


def fake_graph():
    return {
        "nodes": [
            {"id": "px4", "name": "PX4", "ontologyClass": "Technology", "domain": "flight-control"},
            {"id": "ardupilot", "name": "ArduPilot", "ontologyClass": "Technology", "domain": "flight-control"},
            {"id": "yolo", "name": "YOLO", "ontologyClass": "AIModel", "domain": "ai-autonomy"},
            {"id": "swarm-coord", "name": "Swarm Coordination", "ontologyClass": "Mission", "domain": "ops-mission"},
            {"id": "no-class", "name": "온톨로지 미분류", "ontologyClass": None, "domain": ""},
        ],
        "edges": [
            {"source": "px4", "target": "ardupilot", "type": "related"},
            {"source": "px4", "target": "yolo", "type": "wikilink"},
        ],
    }


def test_pick_excludes_same_class_pairs():
    g = fake_graph()
    rng = random.Random(42)
    for _ in range(50):
        pair = ic.pick_cross_domain_pair(g, rng=rng)
        assert pair is not None
        a, b = pair
        assert a["ontologyClass"] != b["ontologyClass"], "같은 ontologyClass 쌍이 선택됨"
    print("PASS: 항상 서로 다른 ontologyClass 쌍만 선택")


def test_pick_excludes_already_connected_pairs():
    g = fake_graph()
    rng = random.Random(1)
    for _ in range(50):
        pair = ic.pick_cross_domain_pair(g, rng=rng)
        ids = tuple(sorted((pair[0]["id"], pair[1]["id"])))
        assert ids != ("px4", "yolo"), "이미 그래프에 연결된 쌍(px4-yolo)이 선택됨"
    print("PASS: 이미 연결된 쌍(px4-yolo)은 절대 선택 안 됨")


def test_pick_excludes_no_class_nodes():
    g = fake_graph()
    rng = random.Random(7)
    for _ in range(50):
        pair = ic.pick_cross_domain_pair(g, rng=rng)
        assert pair[0]["ontologyClass"] is not None and pair[1]["ontologyClass"] is not None
    print("PASS: ontologyClass 없는 노드는 후보에서 제외")


def test_avoid_pairs_respected():
    g = fake_graph()
    # 남은 유효 후보: (ardupilot,yolo) (ardupilot,swarm-coord) (px4,swarm-coord) (yolo,swarm-coord)
    avoid = {tuple(sorted(("ardupilot", "yolo"))), tuple(sorted(("ardupilot", "swarm-coord"))),
             tuple(sorted(("px4", "swarm-coord")))}
    rng = random.Random(3)
    for _ in range(30):
        pair = ic.pick_cross_domain_pair(g, avoid_pairs=avoid, rng=rng)
        ids = tuple(sorted((pair[0]["id"], pair[1]["id"])))
        assert ids not in avoid, f"avoid_pairs에 있는 쌍이 다시 선택됨: {ids}"
    print("PASS: avoid_pairs로 지정한 쌍은 재선택되지 않음")


def test_no_candidates_returns_none():
    g = {"nodes": [{"id": "a", "ontologyClass": "Technology"}], "edges": []}
    assert ic.pick_cross_domain_pair(g) is None, "후보 1개뿐인데 None을 반환하지 않음"
    print("PASS: 유효 후보가 없으면 None 반환(호출자가 처리)")


def test_format_pair_brief():
    g = fake_graph()
    pair = (g["nodes"][2], g["nodes"][3])  # yolo, swarm-coord
    brief = ic.format_pair_brief(pair)
    assert "YOLO" in brief and "Swarm Coordination" in brief
    assert "AIModel" in brief and "Mission" in brief
    print("PASS: 조합 요약 텍스트에 두 노드 정보 정상 포함")


if __name__ == "__main__":
    tests = [
        test_pick_excludes_same_class_pairs,
        test_pick_excludes_already_connected_pairs,
        test_pick_excludes_no_class_nodes,
        test_avoid_pairs_respected,
        test_no_candidates_returns_none,
        test_format_pair_brief,
    ]
    failed = 0
    for t in tests:
        try:
            t()
        except AssertionError as e:
            print(f"FAIL: {t.__name__} — {e}")
            failed += 1
    print(f"\n{len(tests) - failed}/{len(tests)} 통과")
    sys.exit(1 if failed else 0)
