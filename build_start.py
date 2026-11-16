#!/usr/bin/env python3
"""Build the /start theme-table subpages from start-themes.tsv.

The theme table of the Sigma-10 display-check index used to live inside
pages/start.txt as one ~168,000-character page. It now lives as structured
data in start-themes.tsv (one row per theme), and this script renders the
seven subpages under pages/ (start:themes-*). pages/start.txt itself is a
hand-maintained hub that links to the subpages; it is not generated.

Usage:
  python3 build_start.py           regenerate the subpages in pages/
  python3 build_start.py --check   verify pages/ matches the TSV (no writes);
                                   also checks table contiguity and page size
  python3 build_start.py --toc     print the hub table-of-contents lines

Row template (proven against the pre-split start.txt: 286 of 287 rows are
pure template; the exceptions are data, not code):
  * cand_slug defaults to orig_slug + "-jp". Two rows differ and carry the
    value explicitly in the TSV: "Quand le soleil se couche" reuses the
    original sample as its candidate sample (cand_slug == orig_slug), and
    the Sigma-10 environment row points at the bare theme-decoration-sample
    page (cand_slug empty).
  * Amethyst V2 is the only row whose detail cell is free text; it is
    stored verbatim in detail_override.
  * The existing-page label is the real SCP-JP fullname (theme:basalt);
    the check-wiki target replaces ":" with "-" (existing:theme-basalt),
    with old:theme:basalt the one multi-category case, which the same
    replacement produces.

Wikidot tables split at blank lines, so a generated table is one
contiguous block of || lines with no blank line inside. --check enforces
this for every generated page.
"""
import csv
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(REPO, "start-themes.tsv")
PAGES_DIR = os.path.join(REPO, "pages")
MAX_PAGE_CHARS = 40000

WD = "https://sigma10-jp-test.wikidot.com/"
WJ = "https://codex-wsl-maintenance.tail3a09a5.ts.net:8443/"

PAGE_ORDER = ["stage1", "en-1", "en-2", "en-3", "cn-1", "cn-2", "ko"]
PAGE_TITLES = {
    "stage1": "テーマ表（既存JPテーマ）",
    "en-1": "テーマ表（EN原典テーマ 1/3）",
    "en-2": "テーマ表（EN原典テーマ 2/3）",
    "en-3": "テーマ表（EN原典テーマ 3/3）",
    "cn-1": "テーマ表（CN原典テーマ 1/2）",
    "cn-2": "テーマ表（CN原典テーマ 2/2）",
    "ko": "テーマ表（KO原典テーマ）",
}


def fullname(page):
    return "start:themes-" + page


def sample_links(slug):
    """The [Wikidot] / [Wikijump] link pair for a sample page slug.
    An empty slug means the bare theme-decoration-sample page."""
    name = "theme-decoration-sample" + ("-" + slug if slug else "")
    return f"[{WD}{name} Wikidot] / [{WJ}{name} Wikijump]"


def render_row(r):
    status = f"既存: {r['exist']} ／ 整備: {r['seibi']} ／ スタッフ: {r['staff']}"
    if r["detail_override"]:
        detail = r["detail_override"]
    else:
        detail = f"基盤: {r['base']} ／ 参照rev: {r['rev']}"
        if r["existing"]:
            target = r["existing"].replace(":", "-")
            detail += f" ／ 既存ページ: [[[existing:{target}|{r['existing']}]]]"
        detail += f" ／ 原典: {sample_links(r['orig_slug'])}"
        detail += f" ／ テーマ移植候補: {sample_links(r['cand_slug'])}"
        if r["diff"] == "1":
            detail += f" ／ 差分: [[[phase17-diff-{r['orig_slug']}-jp|差分ページ]]]"
    return f"|| {r['name']} || {status} || {detail} ||"


def render_page(page, rows):
    title = PAGE_TITLES[page]
    idx = PAGE_ORDER.index(page)
    nav = []
    if idx > 0:
        prev = PAGE_ORDER[idx - 1]
        nav.append(f"前の分冊: [[[{fullname(prev)}|{PAGE_TITLES[prev]}]]]")
    if idx < len(PAGE_ORDER) - 1:
        nxt = PAGE_ORDER[idx + 1]
        nav.append(f"次の分冊: [[[{fullname(nxt)}|{PAGE_TITLES[nxt]}]]]")
    navline = " ／ ".join(nav)
    lines = [
        "[[=]]",
        f"+ {title}",
        "[[/=]]",
        "",
        '[[div class="content-panel standalone centered"]]',
        '[[div class="panel-body"]]',
        "[[[start|Sigma-10 表示確認トップ]]] のテーマ表の分冊です。"
        "表の読み方はトップページの「この表の読み方（テーマ・状態・詳細）」にあります。"
        "この分冊の正本はGitリポジトリ（sigma10-check-wiki）の start-themes.tsv です（build_start.py で生成します）。"
        f"この分冊は {len(rows)} 行です。{navline}",
        "[[/div]]",
        "[[/div]]",
        "",
        "||~ テーマ ||~ 状態 ||~ 詳細 ||",
    ]
    lines += [render_row(r) for r in rows]
    return "\n".join(lines) + "\n"


def load_rows():
    with open(DATA, encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    by_page = {}
    for r in rows:
        by_page.setdefault(r["page"], []).append(r)
    return rows, by_page


def check_table_contiguity(text, label, problems):
    lines = text.split("\n")
    table_idx = [i for i, l in enumerate(lines) if l.startswith("||")]
    if not table_idx:
        problems.append(f"{label}: no table lines")
        return
    for i in range(table_idx[0], table_idx[-1] + 1):
        if not lines[i].startswith("||"):
            problems.append(f"{label}: line {i + 1} breaks the table: {lines[i][:40]!r}")
            return


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    rows, by_page = load_rows()
    if set(by_page) != set(PAGE_ORDER):
        print(f"page set mismatch: {sorted(by_page)}", file=sys.stderr)
        return 1
    if mode == "--toc":
        for page in PAGE_ORDER:
            sub = by_page[page]
            first = sub[0]["orig_slug"] or "amethyst-v2"
            last = sub[-1]["orig_slug"] or "amethyst-v2"
            print(f"* [[[{fullname(page)}|{PAGE_TITLES[page]}]]]（{len(sub)}行、{first} から {last} まで）")
        return 0
    problems = []
    for page in PAGE_ORDER:
        text = render_page(page, by_page[page])
        label = fullname(page)
        if len(text) > MAX_PAGE_CHARS:
            problems.append(f"{label}: {len(text)} chars exceeds {MAX_PAGE_CHARS}")
        check_table_contiguity(text, label, problems)
        path = os.path.join(PAGES_DIR, label + ".txt")
        if mode == "--check":
            try:
                current = open(path, encoding="utf-8").read()
            except FileNotFoundError:
                problems.append(f"{label}: file missing")
                continue
            if current != text:
                problems.append(f"{label}: differs from start-themes.tsv (run build_start.py)")
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
    if problems:
        for p in problems:
            print("PROBLEM:", p)
        return 1
    total = sum(len(by_page[p]) for p in PAGE_ORDER)
    print(f"OK: {total} rows on {len(PAGE_ORDER)} subpages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
