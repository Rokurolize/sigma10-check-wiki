#!/usr/bin/env python3
"""Generate the per-page status/procedure column of pages-existing/existing:index.txt.

STARTFIX lane, finding 8. Before this generator the existing-articles index
(the priority verification surface) listed each of the 153 pages with two
links and no status or procedure. This script adds a fourth column sourced
mechanically from the repository's own records:

  * reproduction state — start-themes.tsv's `exist` column for the 30 pages
    that have a theme row, and parity-existing.json for the other 123;
  * migration procedure — start-themes.tsv's `staff` column for themed pages
    (plus the linked diff page when one exists), otherwise the keep-as-is /
    legacy / source-citation disposition in review/existing-pages/README.md;
  * record kind — the cross-reference table of that same README.

The generator is idempotent and circularity-free: the hand-maintained part
of the index is the non-table text plus the first three cells of each table
row. On regeneration those first three cells and all prose are read back
verbatim; only the fourth cell (and the fourth header cell, and the one
explanatory paragraph) are owned by this script. A --check run verifies the
committed page equals a fresh regeneration.

Usage:
  python3 build_existing_index.py           regenerate the index in place
  python3 build_existing_index.py --check   verify without writing
"""
import csv
import json
import os
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent
INDEX = REPO / "pages-existing" / "existing:index.txt"
EXISTING_README = REPO / "review" / "existing-pages" / "README.md"
PARITY = REPO / "parity-existing.json"
TSV = REPO / "start-themes.tsv"

STATUS_INTRO = (
    "* 各行の「状態・手続き」は、Wikijump側の描画再現状態（再現状態）、移行時の手続き（移行手続き）、および記録の種別（記録）です。"
    "再現状態は [[[start:wikijump-parity|Wikijump描画再現の記録]]] と review/existing-pages/README.md から、"
    "移行手続きは start-themes.tsv のスタッフ適用手続きと同READMEのクロスリファレンスから機械的に生成されています（build_existing_index.py）。"
    "公開済みページは移行日に影響を受ける優先の検証面です。"
)
HEADER4 = "||~ 状態・手続き ||"
MARKER = "各行の「状態・手続き」"


def load_xrefs():
    """Fullname -> (kind, cross-reference) from the README's record table."""
    text = EXISTING_README.read_text(encoding="utf-8")
    section = text.split("## Full record table", 1)[1]
    out = {}
    for line in section.splitlines():
        m = re.match(r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|$", line)
        if m:
            out[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    return out


def load_parity():
    """Fullname-without-prefix -> reproduction state ('match'/'mismatch (...)')."""
    data = json.loads(PARITY.read_text(encoding="utf-8"))
    out = {}
    # Key by `target` (the -category-slug form used by existing: page names),
    # not `label` (the production theme:component: fullname).
    for x in data["match_theme"] + data["match_other"]:
        out[x["target"]] = "match"
    for x in data["mismatch"]:
        out[x["target"]] = f"mismatch ({x['kinds']})"
    return out


def load_staff():
    """check-wiki target slug -> (reproduction, procedure, diff page or '').

    The index links use existing:theme-x (a '-' where the production
    fullname has ':'), so key by the same replacement build_start.py uses
    for its Existing-page links: existing.replace(':', '-').
    """
    out = {}
    with open(TSV, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if not r["existing"]:
                continue
            proc = r["staff"] or "No change (keep as-is)"
            diff = ""
            if r["diff"] == "1":
                diff = f"[[[phase17-diff-{r['orig_slug']}-jp|diff page]]]"
            out[r["existing"].replace(":", "-")] = (r["exist"], proc, diff)
    return out


def short_xref(text):
    m = re.search(r"production counterpart of `([^`]+)`", text)
    if m:
        return "production counterpart of " + m.group(1)
    if text.startswith("no theme row"):
        return "no theme row; parity record only"
    if text.startswith("legacy"):
        return "legacy record; no action"
    m = re.search(r"review/[A-Za-z0-9-]+/", text)
    if m:
        return "cited in " + m.group(0)
    return text[:90]


def status_cell(fullname, xrefs, parity, staff):
    # `bare` is the check-wiki target slug (theme-x), the key shape used
    # by load_staff().
    bare = fullname.split(":", 1)[1]
    if bare in staff:
        repro, proc, diff = staff[bare]
        proc = proc + (f" ({diff})" if diff else "")
    else:
        repro = parity.get(bare, "match")
        proc = "No source change at migration; keep as-is"
    kind, xref = xrefs.get(fullname, ("unknown", "no record"))
    record = short_xref(xref)
    if kind.startswith("old"):
        proc = "Legacy record; no action (keep as-is)"
    return f"再現状態: {repro} / 移行手続き: {proc} / 記録: {record}"


def generate():
    xrefs = load_xrefs()
    parity = load_parity()
    staff = load_staff()
    lines = INDEX.read_text(encoding="utf-8").split("\n")
    intro_present = any(MARKER in l for l in lines)
    out = []
    records = 0
    for line in lines:
        if line.startswith("||~"):
            out.append(line if HEADER4 in line else line + " " + HEADER4)
        elif line.startswith("||"):
            cells = [c.strip() for c in line.split("||")[1:-1]]
            if len(cells) < 3:
                out.append(line)
                continue
            m = re.search(r"\[\[\[(existing:[^\]|]+)\|", cells[0])
            if not m:
                out.append(line)
                continue
            fullname = m.group(1)
            records += 1
            out.append("|| " + " || ".join(cells[:3]) + " || "
                       + status_cell(fullname, xrefs, parity, staff) + " ||")
        else:
            out.append(line)
            if (not intro_present and line.startswith("* 対象:")
                    and "153" in line):
                out.append(STATUS_INTRO)
    if not intro_present and not any(MARKER in l for l in out):
        raise RuntimeError("failed to insert the status-column explanation")
    if records != 153:
        raise RuntimeError(f"expected 153 record rows, found {records}")
    return "\n".join(out)


def main():
    generated = generate()
    check = "--check" in sys.argv[1:]
    current = INDEX.read_text(encoding="utf-8")
    # compare modulo the trailing newline, which Wikidot normalizes
    if generated.rstrip("\n") == current.rstrip("\n"):
        print("OK: existing:index status column is up to date (153 records)")
        return 0
    if check:
        print("PROBLEM: existing:index.txt differs from build_existing_index.py "
              "(run python3 build_existing_index.py)", file=sys.stderr)
        return 1
    INDEX.write_text(generated.rstrip("\n") + "\n", encoding="utf-8")
    print("existing:index.txt regenerated with per-page status/procedure "
          "(153 records)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
