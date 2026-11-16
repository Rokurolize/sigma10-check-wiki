#!/usr/bin/env python3
"""Build the /start theme-table subpages from start-themes.tsv.

The theme table of the Sigma-10 display-check index used to live inside
pages/start.txt as one ~168,000-character page. It now lives as structured
data in start-themes.tsv (one row per theme), and this script renders the
subpages under pages/ (start:themes-*), grouped by the branch the theme
was created in (the TSV `page` column holds the origin code: jp/en/cn/
ko/fr). pages/start.txt itself is a hand-maintained hub that links to
the subpages; it is not generated.

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
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(REPO, "start-themes.tsv")
PARITY_DATA = os.path.join(REPO, "parity-existing.json")
PAGES_DIR = os.path.join(REPO, "pages")
MAX_PAGE_CHARS = 40000
PARITY_PAGE = "start:wikijump-parity"

WD = "https://sigma10-jp-test.wikidot.com/"
WJ = "https://codex-wsl-maintenance.tail3a09a5.ts.net:8443/"

# The subpages are grouped by the branch the theme was created in
# (its origin), which is the categorization a reader expects: a theme
# posted on SCP-JP as a translation belongs to its origin branch's
# table, not to a "posted themes" bucket. The TSV `page` column holds
# the origin code. For themes posted on SCP-JP the origin is the branch
# tag on the production page (the JP census in the campaign scope
# record); for unposted themes it is the campaign's originality
# classification. Within an origin, rows are in sample-slug order and
# are chunked only for page size.
ORIGINS = [
    ("jp", "JP原典テーマ"),
    ("en", "EN原典テーマ"),
    ("cn", "CN原典テーマ"),
    ("ko", "KO原典テーマ"),
    ("fr", "FR原典テーマ"),
]
MAX_ROWS_PER_PAGE = 54


def plan_pages(by_origin):
    """Return [(fullname, title, rows)] in reading order."""
    plan = []
    for code, label in ORIGINS:
        rows = sorted(by_origin.get(code, []),
                      key=lambda r: (r["orig_slug"] or r["cand_slug"] or r["name"]))
        if not rows:
            continue
        nchunks = (len(rows) + MAX_ROWS_PER_PAGE - 1) // MAX_ROWS_PER_PAGE
        base, extra = divmod(len(rows), nchunks)
        pos = 0
        for i in range(nchunks):
            size = base + (1 if i < extra else 0)
            chunk = rows[pos:pos + size]
            pos += size
            if nchunks == 1:
                plan.append((f"start:themes-{code}", f"テーマ表（{label}）", chunk))
            else:
                plan.append((f"start:themes-{code}-{i + 1}",
                             f"テーマ表（{label} {i + 1}/{nchunks}）", chunk))
    return plan


def sample_links(slug):
    """The [Wikidot] / [Wikijump] link pair for a sample page slug.
    An empty slug means the bare theme-decoration-sample page."""
    name = "theme-decoration-sample" + ("-" + slug if slug else "")
    return f"[{WD}{name} Wikidot] / [{WJ}{name} Wikijump]"


def render_row(r):
    # The row status carries porting/migration state only. The existing
    # article's Wikijump reproduction state (the TSV `exist` column) is
    # rendered on the parity ledger page instead (render_parity below):
    # the tables are the primary porting record, the ledger is the
    # secondary Wikijump verification record, and the two stay separate.
    status = f"整備: {r['seibi']} ／ スタッフ: {r['staff']}"
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


def render_page(title, rows, navline):
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


def render_parity(rows, parity):
    """The Wikijump reproduction ledger for the 153 existing articles.

    Kept apart from the theme tables on purpose: the tables document
    porting and migration state (the primary purpose of this wiki set);
    whether the still-in-development Wikijump reproduces a page is a
    secondary verification record and lives only here. Theme-row states
    come from the TSV `exist` column; the articles without a theme row
    come from parity-existing.json."""
    lines = [
        "[[=]]",
        "+ Wikijump描画再現の記録",
        "[[/=]]",
        "",
        '[[div class="content-panel standalone centered"]]',
        '[[div class="panel-body"]]',
        "[[[start|Sigma-10 表示確認トップ]]] のテーマ表とは目的の異なる、副次的な検証の記録です。"
        "このWiki群の本来の目的はテーマ移植とSigma-10への移行であり、このページはその作業記録ではありません。"
        "Wikijumpは開発途中のソフトウェアであり、Wikidotの表示を再現できないページがあるのは想定内です。"
        "ここでは、SCP-JP本番の既存記事153件について、Wikijump側で読者に見える表示がWikidot側と一致するかどうかを記録します。"
        "不一致はWikijump側の課題としてここに集約し、テーマ移植や移行の残作業には数えません。",
        "[[/div]]",
        "[[/div]]",
        "",
        "**測定ビルド eaefd8bf27（一部は f7e6cd103 で再測定）。** 「一致」はWikidotとWikijumpで読者に見えるものが同じであること、「不一致」は括弧内に書いた差があることです。",
        "",
        "+ 不一致の分類",
        "",
        "色の差（本文・見出しの色）、リテラルの差（マークアップのようなテキストの漏れ）、画像の差（壊れた画像・読み込みの差）、折りたたみの差、タブの差、includeエラーの差です。",
        "",
    ]
    themed = [r for r in rows if r["existing"]]
    lines += [f"+ テーマ行に対応する既存記事（{len(themed)}件）", "",
              "||~ テーマ ||~ 既存ページ ||~ 再現状態 ||"]
    for r in themed:
        target = r["existing"].replace(":", "-")
        lines.append(f"|| {r['name']} || [[[existing:{target}|{r['existing']}]]] || {r['exist']} ||")
    rest = len(parity["match_theme"]) + len(parity["match_other"]) + len(parity["mismatch"])
    lines += ["", f"+ テーマ行のない既存記事（{rest}件）", ""]
    nmatch = len(parity["match_theme"]) + len(parity["match_other"])
    lines += [f"**一致（{nmatch}件）**", ""]
    lines.append(f"テーマページ（{len(parity['match_theme'])}件）: "
                 + "、".join(f"[[[existing:{x['target']}|{x['label']}]]]" for x in parity["match_theme"]))
    lines += [""]
    lines.append(f"コンポーネント・その他（{len(parity['match_other'])}件）: "
                 + "、".join(f"[[[existing:{x['target']}|{x['label']}]]]" for x in parity["match_other"]))
    lines += ["", f"**不一致（{len(parity['mismatch'])}件）**", ""]
    for x in parity["mismatch"]:
        lines.append(f"* [[[existing:{x['target']}|{x['label']}]]] — {x['kinds']}")
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
    rows, by_origin = load_rows()
    if set(by_origin) != {code for code, _ in ORIGINS}:
        print(f"origin set mismatch: {sorted(by_origin)}", file=sys.stderr)
        return 1
    plan = plan_pages(by_origin)
    if mode == "--toc":
        for fn, title, chunk in plan:
            first = chunk[0]["orig_slug"] or chunk[0]["name"]
            last = chunk[-1]["orig_slug"] or chunk[-1]["name"]
            posted = sum(1 for r in chunk if r["existing"])
            note = f"、うちSCP-JP投稿済み{posted}行" if posted else ""
            print(f"* [[[{fn}|{title}]]]（{len(chunk)}行{note}、{first} から {last} まで）")
        return 0
    with open(PARITY_DATA, encoding="utf-8") as f:
        parity = json.load(f)
    outputs = []
    for i, (fn, title, chunk) in enumerate(plan):
        nav = []
        if i > 0:
            nav.append(f"前の分冊: [[[{plan[i - 1][0]}|{plan[i - 1][1]}]]]")
        if i < len(plan) - 1:
            nav.append(f"次の分冊: [[[{plan[i + 1][0]}|{plan[i + 1][1]}]]]")
        outputs.append((fn, render_page(title, chunk, " ／ ".join(nav))))
    outputs.append((PARITY_PAGE, render_parity(rows, parity)))
    problems = []
    expected = {label + ".txt" for label, _ in outputs}
    for name in os.listdir(PAGES_DIR):
        if name.startswith("start:themes-") and name not in expected:
            problems.append(f"stale generated file pages/{name} (remove it; its category is retired)")
    for label, text in outputs:
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
                problems.append(f"{label}: differs from its data source (run build_start.py)")
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
    if problems:
        for p in problems:
            print("PROBLEM:", p)
        return 1
    total = sum(len(chunk) for _, _, chunk in plan)
    print(f"OK: {total} rows on {len(plan)} subpages + parity ledger")
    return 0


if __name__ == "__main__":
    sys.exit(main())
