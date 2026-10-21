#!/usr/bin/env python3
"""마스터 지시(2026-10-21 '도메인이 없는 문서에 도메인 연결')로 승인된 domain 값을 frontmatter에 한 줄 추가한다(ontology/domain-approvals-*.json).
규칙: 이미 domain:이 있으면 건드리지 않는다(기존 값 재라벨 금지). 값은 공식 19개 어휘(add-domain-tags.py DRONE_DOMAINS)에서만 허용. 본문·다른 필드 불변. 삽입 위치는 type: 다음 줄. 기본은 미리보기(--apply로 적용).
"""
import json, re, sys, glob, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(root, "scripts"))
src = open(os.path.join(root, "scripts", "add-domain-tags.py"), encoding="utf-8").read()
m = re.search(r"DRONE_DOMAINS = \{(.*?)\n\}", src, re.S)
OFFICIAL = set(re.findall(r'"([a-z-]+)"', m.group(1)))
apply = "--apply" in sys.argv
changed = skipped = 0
for f in sorted(glob.glob(os.path.join(root, "ontology", "domain-approvals-*.json"))):
    for it in json.load(open(f, encoding="utf-8"))["approved"]:
        if it["domain"] not in OFFICIAL: print("공식 어휘 아님, 건너뜀", it); continue
        p = os.path.join(root, it["path"]); text = open(p, encoding="utf-8").read()
        mm = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not mm: print("프런트매터 없음", it["path"]); continue
        fm = mm.group(1)
        if re.search(r"^domain:", fm, re.M): skipped += 1; continue
        if re.search(r"^type:.*$", fm, re.M): fm2 = re.sub(r"^(type:.*)$", lambda x: x.group(1) + "\ndomain: " + it["domain"], fm, count=1, flags=re.M)
        else: fm2 = fm + "\ndomain: " + it["domain"]
        changed += 1
        if apply: open(p, "w", encoding="utf-8").write(text[: mm.start(1)] + fm2 + text[mm.end(1):])
print(("적용" if apply else "미리보기") + f": 변경 {changed}건, 이미 있어 건너뜀 {skipped}건 (공식 어휘 {len(OFFICIAL)}개)")
