#!/usr/bin/env python3
"""승인된 위키 문서→온톨로지 클래스 연결(ontology/class-approvals-*.json)을 해당 문서 frontmatter에 한 줄(ontology_class)로 반영한다.
규칙: 이미 ontology_class가 있으면 건드리지 않는다. 본문·다른 필드는 불변. 삽입 위치는 domain: 다음 줄(없으면 type: 다음 줄). 기본은 미리보기(--apply로 적용).
"""
import json, re, sys, glob, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
apply = "--apply" in sys.argv
files = sorted(glob.glob(os.path.join(root, "ontology", "class-approvals-*.json")))
changed = skipped = 0
for f in files:
    for it in json.load(open(f, encoding="utf-8"))["approved"]:
        p = os.path.join(root, it["path"])
        text = open(p, encoding="utf-8").read()
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m: print("프런트매터 없음", it["path"]); continue
        fm = m.group(1)
        if re.search(r"^ontology_class:", fm, re.M): skipped += 1; continue
        line = f"ontology_class: {it['ontology_class']}"
        if re.search(r"^domain:.*$", fm, re.M): fm2 = re.sub(r"^(domain:.*)$", lambda x: x.group(1) + "\n" + line, fm, count=1, flags=re.M)
        elif re.search(r"^type:.*$", fm, re.M): fm2 = re.sub(r"^(type:.*)$", lambda x: x.group(1) + "\n" + line, fm, count=1, flags=re.M)
        else: fm2 = fm + "\n" + line
        new = text[: m.start(1)] + fm2 + text[m.end(1):]
        changed += 1
        if apply: open(p, "w", encoding="utf-8").write(new)
print(("적용" if apply else "미리보기") + f": 변경 {changed}건, 이미 있어 건너뜀 {skipped}건")
