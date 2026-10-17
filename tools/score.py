#!/usr/bin/env python3
"""言語評価の集計。

data/requirements.csv（要求と重み）と data/evaluation.csv（言語ごとの評価）から、
単純合計と重み付き合計を出す。

    python3 tools/score.py            # 順位表
    python3 tools/score.py --md       # 詳細表を Markdown で出す
    python3 tools/score.py --lang Lean   # 1言語の、点を落としている項目

点数: ◎=3 ○=2 △=1 ×=0
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POINTS = {"◎": 3, "○": 2, "△": 1, "×": 0}


def load():
    with open(ROOT / "data" / "requirements.csv", encoding="utf-8", newline="") as f:
        reqs = list(csv.DictReader(f))
    with open(ROOT / "data" / "evaluation.csv", encoding="utf-8", newline="") as f:
        ev = list(csv.DictReader(f))
    assert [r["id"] for r in reqs] == [e["id"] for e in ev], "requirements と evaluation の項目が一致しない"
    langs = [k for k in ev[0] if k != "id"]
    for e in ev:
        for l in langs:
            assert e[l] in POINTS, f"不正な評価 {e['id']} {l}: {e[l]!r}"
    return reqs, ev, langs


def totals(reqs, ev, langs):
    raw_max = 3 * len(reqs)
    w_max = 3 * sum(int(r["weight"]) for r in reqs)
    out = {}
    for l in langs:
        raw = sum(POINTS[e[l]] for e in ev)
        wt = sum(POINTS[e[l]] * int(r["weight"]) for r, e in zip(reqs, ev))
        out[l] = (raw, wt)
    return out, raw_max, w_max


def ranking():
    reqs, ev, langs = load()
    t, raw_max, w_max = totals(reqs, ev, langs)
    print(f"満点: 単純 {raw_max} / 重み付き {w_max}\n")
    print("| 順位 | 言語 | 単純合計 | 割合 | 重み付き | 割合 |")
    print("|---|---|---|---|---|---|")
    for i, (l, (raw, wt)) in enumerate(sorted(t.items(), key=lambda x: -x[1][1]), 1):
        print(f"| {i} | {l} | {raw} | {raw / raw_max:.0%} | {wt} | {wt / w_max:.0%} |")


def md_tables(chunks=((0, 7), (7, 15))):
    reqs, ev, langs = load()
    for a, b in chunks:
        ls = langs[a:b]
        print("| # | 要求 | 重み | " + " | ".join(ls) + " |")
        print("|" + "---|" * (3 + len(ls)))
        for r, e in zip(reqs, ev):
            print(f"| {r['id']} | {r['short_name']} | {r['weight']} | " + " | ".join(e[l] for l in ls) + " |")
        print()


def lang_gaps(lang):
    reqs, ev, langs = load()
    if lang not in langs:
        sys.exit(f"言語が無い: {lang}（候補: {', '.join(langs)}）")
    rows = []
    for r, e in zip(reqs, ev):
        lost = (3 - POINTS[e[lang]]) * int(r["weight"])
        rows.append((lost, r["id"], r["short_name"], e[lang], r["weight"]))
    print(f"{lang}: 点を落としている項目（失点の大きい順）")
    for lost, i, n, s, w in sorted(rows, reverse=True):
        if lost:
            print(f"  失点 {lost:>2}  #{i:<5} {n}（評価 {s}、重み {w}）")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        ranking()
    elif a[0] == "--md":
        md_tables()
    elif a[0] == "--lang" and len(a) == 2:
        lang_gaps(a[1])
    else:
        sys.exit(__doc__)
