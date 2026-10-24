#!/usr/bin/env python3
"""지정한 승인 파일(ontology/class-approvals-*.json)이 추가한 frontmatter ontology_class 한 줄을 되돌린다(apply-class-approvals.py의 역방향).
사용: revert-class-approvals.py <승인파일> [--apply]. 승인 파일의 클래스와 값이 같은 줄만 지우고, 다른 값이면 건드리지 않는다. 기본은 미리보기.
"""
import json, re, sys, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
if not args: sys.exit("사용법: revert-class-approvals.py ontology/class-approvals-XXXX.json [--apply]")
apply = "--apply" in sys.argv
changed = skipped = 0
for it in json.load(open(args[0], encoding="utf-8"))["approved"]:
    p = os.path.join(root, it["path"])
    text = open(p, encoding="utf-8").read()
    pat = re.compile(r"^ontology_class: " + re.escape(it["ontology_class"]) + r"[ \t]*\n", re.M)
    m = re.match(r"---\n(.*?\n)---\n", text, re.S)
    if not m or not pat.search(m.group(1)): skipped += 1; continue
    fm2 = pat.sub("", m.group(1), count=1)
    changed += 1
    if apply: open(p, "w", encoding="utf-8").write("---\n" + fm2 + "---\n" + text[m.end():])
print(("되돌림" if apply else "미리보기") + f": 변경 {changed}건, 해당 없음 {skipped}건")
