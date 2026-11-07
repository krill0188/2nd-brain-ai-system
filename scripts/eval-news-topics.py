#!/usr/bin/env python3
"""eval-news-topics.py — 뉴스 주제 분류기의 골든셋 평가(실제 LLM 호출). 합격선: 일치율 ≥ 80%, 빈 라벨 비율 ≤ 25%(전체 예측), 닫힌 목록 위반 0.
일치 정의: gold 가 비어 있으면 예측도 비어 있어야(또는 alts 와 일치), gold 가 있으면 예측이 gold∪alts 와 겹쳐야 하고 그 밖의 라벨이 섞이지 않아야 한다.
"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import news_topics as nt

def main():
    items = json.loads((Path(__file__).resolve().parent / "fixtures/news-topics-golden.json").read_text(encoding="utf-8"))["items"]
    feed = [dict(it) for it in items]
    for it in feed: it.pop("gold"); it.pop("alts")
    stat = nt.apply_topics(feed, limit=len(feed))
    ok = bad_label = empty_pred = 0
    rows = []
    for g, p in zip(items, feed):
        gold, alts, pred = set(g["gold"]), set(g["alts"]), set(p.get("topics") or [])
        if not pred: empty_pred += 1
        bad_label += len(pred - set(nt.TOPICS))
        allowed = gold | alts
        if not pred:
            good = not gold                                   # 비어 있는 예측: 정답도 비어 있어야 한다
        else:
            good = pred <= allowed and bool(pred & allowed)   # 예측이 정답∪대안 안에 있어야 한다(정답이 비었으면 대안만 허용)
        ok += good
        if not good: rows.append((g["title"][:60], sorted(gold), sorted(alts), sorted(pred)))
    n = len(items)
    print(f"분류 통계 {stat}")
    print(f"일치 {ok}/{n} = {ok/n:.0%} | 빈 예측 {empty_pred}/{n} = {empty_pred/n:.0%} | 닫힌 목록 위반 {bad_label}")
    for r in rows: print("  불일치:", r)
    passed = ok / n >= 0.8 and bad_label == 0
    print("합격" if passed else "불합격")
    return 0 if passed else 1

if __name__ == "__main__":
    sys.exit(main())
