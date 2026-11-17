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
  * A row's detail cell gains a "Review:" segment linking to the theme's
    review package on GitHub when review/<dir-key>/README.md exists in
    the repo at generation time (dir-key: cand_slug, else orig_slug).
    With no package the segment is omitted entirely, so --check's byte
    comparison also guards the link state.
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
REVIEW_URL = "https://github.com/Rokurolize/sigma10-check-wiki/tree/main/review/"
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
    ("jp", "JP-origin themes"),
    ("en", "EN-origin themes"),
    ("cn", "CN-origin themes"),
    ("ko", "KO-origin themes"),
    ("fr", "FR-origin themes"),
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
                plan.append((f"start:themes-{code}", f"Theme table ({label})", chunk))
            else:
                plan.append((f"start:themes-{code}-{i + 1}",
                             f"Theme table ({label} {i + 1}/{nchunks})", chunk))
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
    status = f"Prep: {r['seibi']} / Staff: {r['staff']}"
    if r["detail_override"]:
        detail = r["detail_override"]
    else:
        detail = f"Base: {r['base']} / Reference rev: {r['rev']}"
        if r["existing"]:
            target = r["existing"].replace(":", "-")
            detail += f" / Existing page: [[[existing:{target}|{r['existing']}]]]"
        detail += f" / Original: {sample_links(r['orig_slug'])}"
        detail += f" / Port candidate: {sample_links(r['cand_slug'])}"
        if r["diff"] == "1":
            detail += f" / Diff: [[[phase17-diff-{r['orig_slug']}-jp|diff page]]]"
    key = r["cand_slug"] or r["orig_slug"]
    if key and os.path.exists(os.path.join(REPO, "review", key, "README.md")):
        detail += f" / Review: [{REVIEW_URL}{key} review package]"
    return f"|| {r['name']} || {status} || {detail} ||"


def render_page(title, rows, navline):
    lines = [
        "[[=]]",
        f"+ {title}",
        "[[/=]]",
        "",
        '[[div class="content-panel standalone centered"]]',
        '[[div class="panel-body"]]',
        "A subpage of the theme table of the [[[start|Sigma-10 display-check top page]]]. "
        "How to read the table is in \"How to read this table (theme, status, details)\" on the top page. "
        "The canonical source of this subpage is start-themes.tsv in the Git repository (sigma10-check-wiki), generated by build_start.py. "
        f"This subpage has {len(rows)} rows. {navline}",
        "[[/div]]",
        "[[/div]]",
        "",
        "||~ Theme ||~ Status ||~ Details ||",
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
        "+ Record of Wikijump rendering reproduction",
        "[[/=]]",
        "",
        '[[div class="content-panel standalone centered"]]',
        '[[div class="panel-body"]]',
        "A secondary verification record, with a different purpose from the theme table of the [[[start|Sigma-10 display-check top page]]]. "
        "The purpose of this wiki set is theme porting and the Sigma-10 migration, and this page is not a record of that work. "
        "Wikijump is software still under development, so some pages cannot reproduce the Wikidot rendering; that is expected. "
        "For the 153 existing articles on production SCP-JP, this page records whether what a reader sees on the Wikijump side matches the Wikidot side. "
        "Mismatches are collected here as Wikijump-side issues and are not counted as remaining porting or migration work.",
        "[[/div]]",
        "[[/div]]",
        "",
        "**Measured build eaefd8bf27 (partly re-measured on f7e6cd103).** In the reproduction-state column, 一致 means what the reader sees is identical between Wikidot and Wikijump, and 不一致 means there is a difference, of the kind named in parentheses.",
        "",
        "+ Categories of mismatch",
        "",
        "Color differences (body and heading colors), literal differences (leaked markup-like text), image differences (broken images and loading differences), collapsible differences, tab differences, and include-error differences.",
        "",
    ]
    themed = [r for r in rows if r["existing"]]
    lines += [f"+ Existing articles with a theme row ({len(themed)})", "",
              "||~ Theme ||~ Existing page ||~ Reproduction state ||"]
    for r in themed:
        target = r["existing"].replace(":", "-")
        lines.append(f"|| {r['name']} || [[[existing:{target}|{r['existing']}]]] || {r['exist']} ||")
    rest = len(parity["match_theme"]) + len(parity["match_other"]) + len(parity["mismatch"])
    lines += ["", f"+ Existing articles without a theme row ({rest})", ""]
    nmatch = len(parity["match_theme"]) + len(parity["match_other"])
    lines += [f"**Matches ({nmatch})**", ""]
    lines.append(f"Theme pages ({len(parity['match_theme'])}): "
                 + ", ".join(f"[[[existing:{x['target']}|{x['label']}]]]" for x in parity["match_theme"]))
    lines += [""]
    lines.append(f"Components and others ({len(parity['match_other'])}): "
                 + ", ".join(f"[[[existing:{x['target']}|{x['label']}]]]" for x in parity["match_other"]))
    lines += ["", f"**Mismatches ({len(parity['mismatch'])})**", ""]
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
            note = f", of which {posted} posted on SCP-JP" if posted else ""
            print(f"* [[[{fn}|{title}]]] ({len(chunk)} rows{note}, {first} to {last})")
        return 0
    with open(PARITY_DATA, encoding="utf-8") as f:
        parity = json.load(f)
    outputs = []
    for i, (fn, title, chunk) in enumerate(plan):
        nav = []
        if i > 0:
            nav.append(f"Previous subpage: [[[{plan[i - 1][0]}|{plan[i - 1][1]}]]]")
        if i < len(plan) - 1:
            nav.append(f"Next subpage: [[[{plan[i + 1][0]}|{plan[i + 1][1]}]]]")
        outputs.append((fn, render_page(title, chunk, " / ".join(nav))))
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
