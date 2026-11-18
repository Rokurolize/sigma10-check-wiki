#!/usr/bin/env python3
"""Build the /start theme-table subpages from start-themes.tsv.

The theme table of the Sigma-10 display-check index used to live inside
pages/start.txt as one ~168,000-character page. It now lives as structured
data in start-themes.tsv (one row per theme), and this script renders the
subpages under pages/ (start:themes-*), grouped by the branch the theme
was created in (the TSV `page` column holds the origin code: jp/en/cn/
ko/fr). pages/start.txt itself is a hand-maintained hub that links to
the subpages; it is not generated.

Reader-facing fields (STARTFIX lane):
  * Status = "Prep: <plain prep> / Verdict: <verdict> / Staff: <staff>".
    Plain prep is a mechanical, total translation of the TSV `seibi`
    field that drops internal wave codes (EN1/CN9/KO1, "settled in CN1")
    and renders the Check 5 outcome as plain words, while preserving every
    real condition or caveat verbatim (see prep_parts()). The TSV itself
    is never edited.
    Verdict is sourced mechanically from review/sources.tsv's `verdict`
    column AND the package's generated verdict stamp: build_review.py's
    own Records()/assemble_stamp() supply the stamp word (PASS / STALE /
    NOT PASS / EXCEPTION) and its one-line ground. Both sources are shown,
    so a porter can see at a glance whether the candidate passed review.
  * The Theme cell carries the candidate slug alongside the title, so a
    CN/KO row is findable by slug. The slug comes from review/sources.tsv
    (cand_fullname, else orig_fullname), the same data the verdict uses.
  * Rows-per-page was lowered from 54 to 40 because the added reader
    fields push a 54-row page past the 40,000-character cap; plan_pages()
    still chunks by origin and keeps every table contiguous.

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
import importlib.util
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(REPO, "start-themes.tsv")
SOURCES_DATA = os.path.join(REPO, "review", "sources.tsv")
PARITY_DATA = os.path.join(REPO, "parity-existing.json")
PAGES_DIR = os.path.join(REPO, "pages")
MAX_PAGE_CHARS = 40000
PARITY_PAGE = "start:wikijump-parity"

WD = "https://sigma10-jp-test.wikidot.com/"
REVIEW_URL = "https://github.com/Rokurolize/sigma10-check-wiki/tree/main/review/"
WJ = "https://codex-wsl-maintenance.tail3a09a5.ts.net/"

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
# 54 rows/page overflowed the 40,000-char cap once the verdict phrase and
# the candidate slug were added to each row (measured: en-2 at 39,999
# bytes before the change). 40 leaves headroom and keeps tables contiguous.
MAX_ROWS_PER_PAGE = 40

# Live page titles on both check wikis. The numbered subpage titles are
# derived from the same page plan that generates the tables (live_title_map
# below) and written to start-titles.json, so the campaign reflect path has a
# single authoritative title set and a future re-split cannot silently leave
# the live page metadata on an old "EN 1/3" / "CN 1/2" shape.
ORIGIN_TITLE_JP = {
    "jp": "JP原典テーマ", "en": "EN原典テーマ", "cn": "CN原典テーマ",
    "ko": "KO原典テーマ", "fr": "FR原典テーマ",
}
STATIC_TITLES = {
    "start": "表示確認トップ",
    "start:themes-jp": "テーマ表（JP原典テーマ）",
    "start:themes-ko": "テーマ表（KO原典テーマ）",
    "start:themes-fr": "テーマ表（FR原典テーマ）",
    "start:wikijump-parity": "Wikijump描画再現の記録",
}
TITLES_FILE = "start-titles.json"

# Sample-page gaps recorded in review packages. When a candidate's own
# documentation includes a component that has no JP port anywhere in the
# repository, its sample shows a missing-include notice; the row's Details
# explains the notice instead of leaving a porter to guess at it.
SAMPLE_GAPS = {
    "dynamikron-jp": (
        "Sample note: this candidate's colour exhibit includes "
        "component:theme-squares from the EN SCP Wiki; no JP port of that component "
        "exists in this repository, so the sample shows a missing-include notice. "
        "Recorded gap, not a candidate defect — ground in the dynamikron review package"
    ),
}

# --- mechanical sources for the reader-facing verdict / slug -------------

_BR = None


def build_review():
    """Import review/build_review.py once, from its canonical repo path.

    Reusing the generator's own Records()/assemble_stamp() is what makes
    the verdict word and its ground "in build_review.py's terms" rather
    than a re-implementation that could drift from the record.
    """
    global _BR
    if _BR is None:
        path = os.path.join(REPO, "review", "build_review.py")
        spec = importlib.util.spec_from_file_location(
            "_startfix_build_review", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _BR = mod
    return _BR


def load_sources():
    with open(SOURCES_DATA, encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    by_cand = {r["cand_fullname"]: r for r in rows if r["cand_fullname"]}
    by_orig = {r["orig_fullname"]: r for r in rows if r["orig_fullname"]}
    return by_cand, by_orig


def source_row(r, by_cand, by_orig):
    """Join one TSV row to its review/sources.tsv row by identity.

    Ordinary rows join on `theme:<cand_slug>` (else `theme:<orig_slug>`).
    The telecom row's slugs are the short form and build_review.py's own
    FILE_ALIASES maps them to the long canonical fullname. Amethyst has
    neither slug, so its origin fullname is lifted from detail_override.
    """
    br = build_review()
    key = ("theme:" + r["cand_slug"] if r["cand_slug"] else
           "theme:" + r["orig_slug"] if r["orig_slug"] else None)
    if key:
        key = br.FILE_ALIASES.get(key, key)
        if key in by_cand:
            return by_cand[key]
        if key in by_orig:
            return by_orig[key]
    m = re.search(r"theme:([a-z0-9-]+)", r["detail_override"] or "")
    if m:
        k = "theme:" + m.group(1)
        if k in by_orig:
            return by_orig[k]
        if k in by_cand:
            return by_cand[k]
    return None


_MERGED = re.compile(r"^Complete \(merged in (?:EN|CN|KO)\d+, (.*)\)$")
_SETTLED = re.compile(r" \(settled in (?:EN|CN|KO)\d+\)$")
_WAVE_CODE = re.compile(r"(?:EN|CN|KO)\d+")


def prep_parts(seibi):
    """Return (category, reader-facing phrase) for a TSV `seibi` value.

    The mapping is total: every distinct seibi value in start-themes.tsv
    falls into one of the categories below. Wave codes and "merged in"
    bookkeeping are dropped; the Check 5 outcome is put in plain words;
    every real condition or caveat is preserved verbatim.
    """
    m = _MERGED.match(seibi)
    if m:
        outcome = m.group(1)
        if outcome == "Check 5 not measured: retired 2026-11-16":
            return "wave-retired", "Complete (Check 5 retired 2026-11-16; not measured)"
        if outcome == "Check 5 passed":
            return "wave-passed", "Complete (Check 5 passed)"
        return "wave-other", f"Complete ({outcome})"
    if seibi.startswith("No candidate could be produced"):
        return "no-candidate", _SETTLED.sub("", seibi)
    fixed = {
        "Complete": "complete",
        "Complete (reference rev recorded)": "reference-rev",
        "Complete (diff applied)": "diff-applied",
        "Complete (no reference rev: JP original)": "jp-original",
    }
    if seibi in fixed:
        return fixed[seibi], seibi
    if seibi.startswith("Complete (") and seibi.endswith(")"):
        return "condition", seibi
    return "unclassified", seibi


def verdict_parts(fullname, rec, sources_verdict):
    """Return (stamp word, one-line verdict phrase) for a theme.

    The stamp word and ground come from build_review.py's assemble_stamp;
    the sources.tsv verdict is appended when it differs from the stamp
    word (normally PASS vs STALE after the candidate changed). Citations
    and the 64-hex sha256 are trimmed from the ground for readability; the
    substantive ground is kept verbatim.

    STALE rows follow the coordinator's ruling (recorded on pages/start.txt
    under "Overall state (at a glance)"): every post-verdict change landed
    through the campaign's recorded, verified repair waves and is noted in
    the package, so the record verdict stands and a STALE row is posted like
    a PASS row. The row therefore renders the record verdict with the
    ruling's plain ground, matching the harmonized STALE wording the stamp
    now carries itself. The factual stamp word is kept in a trailing bracket
    so the audit instrument's reading stays available; the stamp region is
    generated only by build_review.py, never hand-edited.
    """
    br = build_review()
    block = br.assemble_stamp(rec, fullname)
    m = re.search(r"^- Overall:\s*(.*)$", block, re.M)
    if not m:
        raise ValueError("no Overall line in stamp for " + fullname)
    overall = m.group(1).strip()
    word, dash, ground = overall.partition(" \u2014 ")
    ground = re.sub(r"\s*\[[^\]]*\]", "", ground).strip()
    ground = re.sub(r"\s*\(verdict against [^)]*\)", "", ground).strip()
    if not dash:
        ground = ""
    word = word.strip()
    if word == "STALE":
        record_word = sources_verdict or "PASS"
        phrase = (f"{record_word} (record verdict) \u2014 candidate revised after the "
                  f"verdict through recorded repairs; see package [package stamp: STALE]")
        return word, phrase
    phrase = f"{word} \u2014 {ground}" if ground else word
    if sources_verdict and sources_verdict != word:
        phrase += f" (record verdict: {sources_verdict})"
    return word, phrase


def enrich_rows(rows, by_cand, by_orig, rec):
    """Attach _slug, _prep, _prep_cat and _verdict to every TSV row."""
    problems = []
    br = build_review()
    for r in rows:
        s = source_row(r, by_cand, by_orig)
        if s is None:
            problems.append(f"no review/sources.tsv row for {r['name']}")
            continue
        full = br._norm(s["cand_fullname"] or s["orig_fullname"])
        try:
            word, phrase = verdict_parts(full, rec, s["verdict"])
        except Exception as e:
            problems.append(f"verdict for {full}: {type(e).__name__}: {e}")
            continue
        r["_slug"] = (s["cand_fullname"] or s["orig_fullname"]).split(":")[-1]
        r["_prep_cat"], r["_prep"] = prep_parts(r["seibi"])
        r["_verdict"] = phrase
    return problems


# -------------------------------------------------------------- rendering

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


def live_title_map(plan):
    """Return {fullname: live Japanese title} for every /start page.

    Numbered subpage titles are derived from plan_pages() (the same plan that
    generates the tables), so a future re-split updates N/M in the title set
    together with the pages. Unnumbered origin subpages and the hub/ledger
    use their fixed live titles.
    """
    titles = dict(STATIC_TITLES)
    counts = {}
    for fn, _, _ in plan:
        m = re.match(r"^start:themes-([a-z]+)-(\d+)$", fn)
        code = m.group(1) if m else fn[len("start:themes-"):]
        counts[code] = counts.get(code, 0) + 1
    for fn, _, _ in plan:
        if fn in STATIC_TITLES:
            continue
        m = re.match(r"^start:themes-([a-z]+)-(\d+)$", fn)
        label = ORIGIN_TITLE_JP[m.group(1) if m else fn[len("start:themes-"):]]
        if m:
            titles[fn] = f"テーマ表（{label} {int(m.group(2))}/{counts[m.group(1)]}）"
        else:
            titles[fn] = f"テーマ表（{label}）"
    return titles


def sample_links(slug):
    """The [Wikidot] / [Wikijump] link pair for a sample page slug.
    An empty slug means the bare theme-decoration-sample page."""
    name = "theme-decoration-sample" + ("-" + slug if slug else "")
    return f"[{WD}{name} Wikidot] / [{WJ}{name} Wikijump]"


def render_row(r):
    # The row status carries porting/migration state plus the mechanical
    # review verdict. The existing article's Wikijump reproduction state
    # (the TSV `exist` column) is rendered on the parity ledger page
    # instead (render_parity below): the tables are the primary porting
    # record, the ledger is the secondary Wikijump verification record.
    status = f"Prep: {r['_prep']} / Verdict: {r['_verdict']} / Staff: {r['staff']}"
    label = r["name"] + (f" ({r['_slug']})" if r.get("_slug") else "")
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
    if key in SAMPLE_GAPS:
        detail += " / " + SAMPLE_GAPS[key]
    return f"|| {label} || {status} || {detail} ||"


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
        "The Status column shows Prep (plain-language work state), Verdict (the review verdict from review/sources.tsv and the generated package stamp), and Staff (the staff procedure). "
        f"This subpage has {len(rows)} rows. {navline}",
        "[[/div]]",
        "[[/div]]",
        "",
        "||~ Theme (candidate slug) ||~ Status ||~ Details ||",
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
        "**Measured build eaefd8bf27 (partly re-measured on f7e6cd103).** In the reproduction-state column, \"match\" means what the reader sees is identical between Wikidot and Wikijump, and \"mismatch\" means there is a difference, of the kind named in parentheses.",
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
    br = build_review()
    by_cand, by_orig = load_sources()
    rec = br.Records()
    problems = enrich_rows(rows, by_cand, by_orig, rec)
    # The prep mapping must be total and must not leak internal codes.
    seen = {}
    for r in rows:
        cat, phrase = prep_parts(r["seibi"])
        seen.setdefault(cat, 0)
        seen[cat] += 1
        if cat == "unclassified":
            problems.append(f"unclassified seibi pattern: {r['seibi']!r}")
        if r.get("_prep") and (_WAVE_CODE.search(r["_prep"]) or "merged in" in r["_prep"]):
            problems.append(f"wave code survived prep translation: {r['_prep']!r}")
    if os.environ.get("STARTFIX_PREP_CATEGORIES"):
        for cat, n in sorted(seen.items()):
            print(f"PREP-CATEGORY {cat}: {n}")
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
    # Authoritative live-title set for the reflect path (Item 3, FIX3).
    titles = live_title_map(plan)
    titles_path = os.path.join(REPO, TITLES_FILE)
    if mode == "--check":
        try:
            with open(titles_path, encoding="utf-8") as f:
                current_titles = json.load(f)
        except FileNotFoundError:
            problems.append(f"{TITLES_FILE}: file missing (run build_start.py)")
        else:
            if current_titles != titles:
                problems.append(f"{TITLES_FILE}: differs from the generated title set (run build_start.py)")
    else:
        with open(titles_path, "w", encoding="utf-8") as f:
            json.dump(titles, f, ensure_ascii=False, indent=2, sort_keys=True)
            f.write("\n")
    outputs = []
    for i, (fn, title, chunk) in enumerate(plan):
        nav = []
        if i > 0:
            nav.append(f"Previous subpage: [[[{plan[i - 1][0]}|{plan[i - 1][1]}]]]")
        if i < len(plan) - 1:
            nav.append(f"Next subpage: [[[{plan[i + 1][0]}|{plan[i + 1][1]}]]]")
        outputs.append((fn, render_page(title, chunk, " / ".join(nav))))
    outputs.append((PARITY_PAGE, render_parity(rows, parity)))
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
    print(f"OK: {total} rows on {len(plan)} subpages + parity ledger; "
          f"prep categories: {dict(sorted(seen.items()))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
