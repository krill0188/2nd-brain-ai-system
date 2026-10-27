#!/usr/bin/env python3
"""paper-fulltext-pilot.py — Phase A 파일럿(수동 실행). 설계: drone-wiki-web/docs/paper-fulltext-pipeline-design.md §8.
원문(PDF)이 있는 논문 N편에 대해: 텍스트 추출 → 수치 문장 청킹 → 후보 생성(ai_router 저가치) → 코드 판정(paper_claims_lib)
→ (통과분만) 별도 판정 호출 → 수율·시간·탈락 사유를 보고서로 남긴다. raw·canonical·웹 레포는 건드리지 않고 ~/2nd/.ua/papers-pilot/ 에만 쓴다.

실행(반드시 venv): ~/2nd/.venv/bin/python scripts/paper-fulltext-pilot.py --candidates <json> --n 10 [--dry]
"""
import argparse, collections, hashlib, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.expanduser("~/projectm/scripts"))
import paper_claims_lib as L
import paper_fulltext_lib as F

OUT = os.path.expanduser("~/2nd/.ua/papers-pilot")


def pick(cands, n):
    """도메인별로 번갈아 결정론적으로 n편을 고른다(같은 입력 → 같은 선택)."""
    by = collections.defaultdict(list)
    for c in sorted(cands, key=lambda x: x["arxiv"]):
        by[c["domain"]].append(c)
    doms = [d for d, _ in sorted(by.items(), key=lambda kv: (-len(kv[1]), kv[0]))]
    out, i = [], 0
    while len(out) < n and any(by.values()):
        d = doms[i % len(doms)]
        if by[d]:
            out.append(by[d].pop(0))
        i += 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--max-chunks", type=int, default=4)
    ap.add_argument("--dry", action="store_true", help="모델 호출 없이 추출·청킹까지만")
    ap.add_argument("--reuse", action="store_true", help="비어 있지 않은 candidates.json이 있으면 후보 생성 호출을 건너뛰고 재판정만")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    cands = pick(json.load(open(a.candidates)), a.n)

    call = None
    if not a.dry:
        import ai_router
        call = ai_router.call

    jpath = os.path.join(OUT, "judge-cache.json")
    jcache = json.load(open(jpath)) if os.path.exists(jpath) else {}
    report, providers = [], collections.Counter()
    why_all = collections.Counter()
    for c in cands:
        aid, t0 = c["arxiv"], time.time()
        rec = {"arxiv": aid, "domain": c["domain"], "title": c["title"][:80], "calls": 0}
        try:
            pages = F.strip_references(F.extract_pages(c["path"]))
        except Exception as e:
            rec["error"] = f"추출 실패: {type(e).__name__}"; report.append(rec); print("추출실패", aid, type(e).__name__); continue
        text = "\n".join(pages)
        open(os.path.join(OUT, aid + ".txt"), "w", encoding="utf-8").write(text)
        sents = F.numeric_sentences(pages)
        chunks = F.make_chunks(sents, max_chunks=a.max_chunks)
        rec.update(pages=len(pages), chars=len(text), numeric_sentences=len(sents), chunks=len(chunks))
        if a.dry:
            report.append(rec); print(aid, rec); continue

        cand_path = os.path.join(OUT, aid + ".candidates.json")
        cand_list, parse_fail, truncated = [], 0, 0
        if a.reuse and os.path.exists(cand_path) and json.load(open(cand_path)):
            cand_list = json.load(open(cand_path)); chunks = []; rec["reused_candidates"] = True
        for ch in chunks:
            try:
                raw, meta = call(F.chunk_prompt(ch), tier="low", project="2nd-paper-fulltext-pilot", timeout=150)
                providers[meta.get("provider")] += 1; rec["calls"] += 1
                items, was_cut = F.parse_candidates_ex(raw)
                truncated += was_cut
                for x in items:
                    x["locator"] = F.locate(ch, str(x.get("quote", "")))
                    cand_list.append(x)
            except ValueError:
                parse_fail += 1
            except Exception as e:  # RouterError 등 — 이 논문은 중단하고 다음으로
                rec["error"] = f"호출 실패: {type(e).__name__}"; break
        json.dump(cand_list, open(cand_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        good, bad = L.judge([F.clean_candidate(x) for x in cand_list], text)
        for b in bad:
            why_all[b["_why"].split("[")[0].strip()] += 1
        rec.update(candidates=len(cand_list), parse_fail=parse_fail, truncated=truncated, code_pass=len(good), code_reject=len(bad))

        final = []
        for g in good:                                           # 통과분만 별도 판정 호출(같은 입력은 캐시)
            jk = hashlib.sha256(F.judge_prompt(g).encode()).hexdigest()[:16]
            if jk in jcache:
                ok = jcache[jk]
            else:
                try:
                    v, meta = call(F.judge_prompt(g), tier="low", system=F.JUDGE, project="2nd-paper-fulltext-pilot", timeout=60)
                    providers[meta.get("provider")] += 1; rec["calls"] += 1
                    ok = v.strip().upper().startswith("OK")
                    jcache[jk] = ok
                except Exception:
                    ok = False
            if ok:
                final.append({**g, "evidenceKind": L.evidence_kind(g), "reviewStatus": "pending"})
            else:
                why_all["JUDGE 거절"] += 1
        rec["judge_pass"] = len(final)
        json.dump(final, open(os.path.join(OUT, aid + ".verified.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        json.dump(bad, open(os.path.join(OUT, aid + ".rejected.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        rec["seconds"] = round(time.time() - t0, 1)
        report.append(rec)
        print(f"{aid} p={rec['pages']} chunks={rec['chunks']} 후보={rec['candidates']} 코드통과={rec['code_pass']} 최종={rec['judge_pass']} calls={rec['calls']} {rec['seconds']}s")

    summ = {"papers": len(report), "calls": sum(r.get("calls", 0) for r in report), "providers": dict(providers), "reject_reasons": dict(why_all),
            "candidates": sum(r.get("candidates", 0) for r in report), "code_pass": sum(r.get("code_pass", 0) for r in report), "judge_pass": sum(r.get("judge_pass", 0) for r in report),
            "errors": [r["arxiv"] for r in report if "error" in r]}
    json.dump(jcache, open(jpath, "w", encoding="utf-8"))
    json.dump({"summary": summ, "papers": report}, open(os.path.join(OUT, "pilot-report.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n요약", json.dumps(summ, ensure_ascii=False))


if __name__ == "__main__":
    main()
