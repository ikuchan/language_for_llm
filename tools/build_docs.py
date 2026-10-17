#!/usr/bin/env python3
"""data/*.csv から、docs の表を作り直す。

    python3 tools/build_docs.py

docs/02_requirements.md と docs/03_evaluation.md の中で、
<!-- BEGIN:名前 --> と <!-- END:名前 --> に挟まれた部分だけを置き換える。
その外側の文章には触らない。評価や重みを直したら、これを実行する。
"""
import csv
import io
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import score  # noqa: E402


def capture(fn, *a):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fn(*a)
    return buf.getvalue()


def replace_block(text, name, body):
    pat = re.compile(rf"(<!-- BEGIN:{name} -->\n).*?(\n<!-- END:{name} -->)", re.S)
    if not pat.search(text):
        sys.exit(f"マーカーが無い: {name}")
    return pat.sub(lambda m: m.group(1) + body.strip("\n") + m.group(2), text)


def requirements_table():
    with open(ROOT / "data" / "requirements.csv", encoding="utf-8", newline="") as f:
        reqs = list(csv.DictReader(f))
    lines = ["| # | 分類 | 要求 | 重み | 由来 |", "|---|---|---|---|---|"]
    for r in reqs:
        lines.append(f"| {r['id']} | {r['group']} | {r['requirement']} | {r['weight']} | {r['origin']} |")
    return "\n".join(lines)


def main():
    p = ROOT / "docs" / "02_requirements.md"
    p.write_text(replace_block(p.read_text(encoding="utf-8"), "requirements", requirements_table()), encoding="utf-8")

    rank = capture(score.ranking).split("\n\n", 1)[1]
    parts = [x for x in capture(score.md_tables).strip().split("\n\n") if x.strip()]
    p = ROOT / "docs" / "03_evaluation.md"
    t = p.read_text(encoding="utf-8")
    t = replace_block(t, "ranking", rank)
    t = replace_block(t, "detail1", parts[0])
    t = replace_block(t, "detail2", parts[1])
    p.write_text(t, encoding="utf-8")
    print("更新: docs/02_requirements.md, docs/03_evaluation.md")


if __name__ == "__main__":
    main()
