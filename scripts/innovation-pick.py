#!/usr/bin/env python3
"""innovation-pick.py <run-id> — innovation-run.sh의 라운드별 기계 단계.
같은 런 안에서 이미 쓴 노드쌍은 다시 고르지 않도록 상태를 유지한다.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import innovation_combine as ic

WIKI_ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: innovation-pick.py <run-id>", file=sys.stderr)
        return 1
    run_id = sys.argv[1]
    tried_path = WIKI_ROOT / "innovations" / "runs" / run_id / ".tried-pairs.json"

    tried: set[tuple[str, str]] = set()
    if tried_path.exists():
        tried = {tuple(p) for p in json.loads(tried_path.read_text(encoding="utf-8"))}

    graph = ic.load_graph()
    pair = ic.pick_cross_domain_pair(graph, avoid_pairs=tried)
    if pair is None:
        print("더 이상 새로운 cross-domain 노드쌍이 없습니다(전부 소진).", file=sys.stderr)
        return 1

    key = tuple(sorted((pair[0]["id"], pair[1]["id"])))
    tried.add(key)
    tried_path.parent.mkdir(parents=True, exist_ok=True)
    tried_path.write_text(json.dumps([list(t) for t in tried]), encoding="utf-8")

    print("# Cross-Domain 조합 후보\n")
    print(ic.format_pair_brief(pair))
    return 0


if __name__ == "__main__":
    sys.exit(main())
