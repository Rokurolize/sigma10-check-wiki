#!/usr/bin/env python3
"""Regenerate the generated files of every review package under review/.

Ownership model follows build_start.py and patterns/build_index.py: a
package's diff.md is a generated file. The hand-maintained sources of a
package are original.<ext> (the frozen mirror of the original source)
and candidate.<ext> (the ported source); diff.md is derived from those
two and must never be hand-edited. A package is any immediate
subdirectory of review/ that holds both original.<ext> and
candidate.<ext> for one shared extension (.css for site packages,
.txt for page packages).

Output shape follows the tiered format of the DIFF-PRESENTATION scout
memo: Tier 1 (at most 400 changed lines and at most 20 hunks) is a
summary table plus the full unified diff in one fenced block. Tier 2
(larger) adds a summary header with per-class line counts, a
change-block index, and the full diff split into <details> sections,
with purely mechanical sections grouped into one collapsed section at
the end. Auto-class labels in Tier 2 are heuristic (see classify());
they are printed as heuristic wherever they appear and never upgrade
or replace the hand-written explanation in the package README.md.
Both tiers' summary tables count review-stage comment lines in the
candidate separately (see count_review_added()).

The same generator also owns two generated regions inside package
READMEs, delimited by BEGIN/END GENERATED markers and never hand-edited:

- the verdict stamp of a theme package (assembled mechanically from the
  vendored campaign record in review/AUTHORITIES/: the go-sign ledger,
  its FIX5 supplement, and the ledger parts in AUTHORITIES/ledger-parts/;
  the part list is an explicit allowlist, see RENDER_PART_FILES), and
- the Status table of a site package (rendered from the package's
  hand-maintained status.tsv plus the canonical commit).

--check verifies all of it: every diff.md matches its sources, every
stamp region matches regeneration, every citation inside a stamp
resolves against the vendored record, the vendored files' SHA-256
hashes match AUTHORITIES/INDEX.md, and the population-check seed table
still carries the aliases the generator's seed data rests on.

Usage:
  python3 review/build_review.py           regenerate every generated file
  python3 review/build_review.py --check   verify everything (no writes);
                                           exits non-zero on any problem
"""


import difflib
import hashlib
import pathlib
import re
import subprocess
import sys


HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
AUTH = HERE / "AUTHORITIES"
PARTS = AUTH / "ledger-parts"

FIX5_HEAD = "435a6bb7193bf09bc02fa5bf529280c2a2389ec2"
RECORD_SUFFIX = ("record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md "
                 "as of the FIX5 head 435a6bb")
STAMP_BEGIN = ("<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; "
               "regenerate with review/build_review.py -->")
STAMP_END = "<!-- END GENERATED VERDICT STAMP -->"
STATUS_BEGIN = ("<!-- BEGIN GENERATED STATUS STAMP — do not hand-edit; "
                "regenerate with review/build_review.py -->")
STATUS_END = "<!-- END GENERATED STATUS STAMP -->"


TIER2_CHANGED_LINES = 400
TIER2_HUNKS = 20

# Tokens whose substitution does not change what a line does: branch
# names, the old-BHL host's named rewrite target, and the -jp suffix
# of a ported slug. Used only by the mechanical auto-class heuristic.
_MECH_SUBS = [
    (re.compile(r"scp-wiki-cn|backrooms-wiki-cn"), "scp-jp"),
    (re.compile(r"nu-scptheme\.github\.io"), "scp-jp.github.io"),
    (re.compile(r"((?:theme|fragment|component):[a-z0-9][a-z0-9-]*?)-jp\b"),
     r"\1"),
]
_CJK = re.compile(r"[⺀-鿿가-힯＀-￯]")
_SUPPLEMENT = re.compile(
    r"credit:(start|end)(-preview)?|interwiki-style|license-box"
    r"|local--code|@import|start-preview")


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git(*args):
    r = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def git_blob_sha(rel, ref):
    out = _git("show", f"{ref}:{rel}")
    return hashlib.sha256(out).hexdigest() if out is not None else None


def git_last_change(*rels):
    out = _git("log", "-1", "--format=%H", "--", *rels)
    return out.decode().strip() if out else ""


def git_head():
    out = _git("rev-parse", "HEAD")
    return out.decode().strip() if out else ""


def package_files(pkg):
    """Return (original_path, candidate_path) for a package dir."""
    for orig in sorted(pkg.glob("original.*")):
        cand = pkg / ("candidate" + orig.suffix)
        if cand.is_file():
            return orig, cand
    return None


def packages():
    found = []
    for d in sorted(HERE.iterdir()):
        if d.is_dir() and package_files(d):
            found.append(d)
    return found


def _norm_mech(line):
    s = " ".join(line.split())
    for rx, rep in _MECH_SUBS:
        s = rx.sub(rep, s)
    return s


def _skeleton(line):
    """A line with every CJK/kana/hangul char and all punctuation and
    whitespace removed: what remains is the language-neutral skeleton."""
    return re.sub(r"[^A-Za-z0-9]", "", _CJK.sub("", line))


def classify(removed, added):
    """Heuristic auto-class for one change block. Order matters:
    mechanical (same lines after token substitution), translation
    (same skeleton after CJK removal), supplement (JP-frame signature
    lines added), else residual."""
    if all(not l.strip() for l in removed + added):
        return "mechanical"
    if sorted(map(_norm_mech, removed)) == sorted(map(_norm_mech, added)):
        return "mechanical"
    if any(_CJK.search(l) for l in removed + added):
        sk_r = sorted(filter(None, map(_skeleton, removed)))
        sk_a = sorted(filter(None, map(_skeleton, added)))
        if sk_r == sk_a:
            return "translation"
    if any(_SUPPLEMENT.search(l) for l in added):
        return "supplement"
    return "residual"


def _gist(removed, added):
    for line in added + removed:
        g = " ".join(line.split())
        if g:
            return (g[:77] + "…") if len(g) > 78 else g
    return "(blank lines only)"


def _header(pkg, oname, cname):
    out = []
    out.append(f"# Diff — {pkg.name}: {oname} → {cname}")
    out.append("")
    out.append(f"This file is GENERATED by build_review.py from {oname} and")
    out.append(f"{cname} in this directory; do not hand-edit it. Regenerate")
    out.append("with `python3 review/build_review.py`; verify with")
    out.append("`python3 review/build_review.py --check`.")
    out.append("")
    return out


def generate_tier1(pkg, oname, cname, o_lines, c_lines, diff, review_added):
    added = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
    removed = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
    hunks = sum(1 for l in diff if l.startswith("@@"))
    out = _header(pkg, oname, cname)
    out.append("| | Lines |")
    out.append("|---|---|")
    out.append(f"| {oname} | {len(o_lines)} |")
    out.append(f"| {cname} | {len(c_lines)} |")
    out.append(f"| Added | +{added} |")
    out.append(f"| Review-stage comments | {review_added} of the +{added} added lines |")
    out.append(f"| Removed | -{removed} |")
    out.append(f"| Hunks | {hunks} |")
    out.append("")
    out.append("```diff")
    out.extend(diff)
    out.append("```")
    out.append("")
    return "\n".join(out)


def _format_range(start, stop):
    beginning = start + 1
    length = stop - start
    if length == 1:
        return str(beginning)
    if not length:
        beginning -= 1
    return f"{beginning},{length}"


def _section_text(group, o_lines, c_lines):
    """Unified-diff text for one grouped-opcode section, built from the
    same autojunk=False alignment as the index so header, index, and
    diff text always describe one identical alignment."""
    a0, a1 = group[0][1], group[-1][2]
    b0, b1 = group[0][3], group[-1][4]
    lines = [f"@@ -{_format_range(a0, a1)} +{_format_range(b0, b1)} @@"]
    for tag, i1, i2, j1, j2 in group:
        if tag == "equal":
            lines.extend(" " + l for l in o_lines[i1:i2])
        if tag in ("replace", "delete"):
            lines.extend("-" + l for l in o_lines[i1:i2])
        if tag in ("replace", "insert"):
            lines.extend("+" + l for l in c_lines[j1:j2])
    return lines


def generate_tier2(pkg, oname, cname, o_lines, c_lines, diff, review_added):
    sm = difflib.SequenceMatcher(a=o_lines, b=c_lines, autojunk=False)
    groups = list(sm.get_grouped_opcodes(3))
    sections = [_section_text(g, o_lines, c_lines) for g in groups]
    # Change blocks with their section number and auto-class.
    blocks = []  # (index, section, tag, i1, i2, j1, j2, cls)
    sec_of = {}
    for si, group in enumerate(groups, 1):
        for op in group:
            if op[0] != "equal":
                sec_of[(op[1], op[3])] = si
    for op in sm.get_opcodes():
        if op[0] == "equal":
            continue
        tag, i1, i2, j1, j2 = op
        cls = classify(o_lines[i1:i2], c_lines[j1:j2])
        blocks.append((len(blocks) + 1, sec_of[(i1, j1)], tag,
                       i1, i2, j1, j2, cls))
    added = sum(b[6] - b[5] for b in blocks)
    removed = sum(b[4] - b[3] for b in blocks)
    class_lines = {}
    class_blocks = {}
    for b in blocks:
        cls = b[7]
        class_blocks[cls] = class_blocks.get(cls, 0) + 1
        class_lines[cls] = class_lines.get(cls, 0) + (b[4] - b[3]) + (b[6] - b[5])
    sec_classes = {}
    for b in blocks:
        sec_classes.setdefault(b[1], set()).add(b[7])
    mech_sections = [si for si in range(1, len(groups) + 1)
                     if sec_classes.get(si) == {"mechanical"}]

    out = _header(pkg, oname, cname)
    out.append("Tier 2 format (large diff): summary header, change-block")
    out.append("index, then the full diff in collapsed sections. Purely")
    out.append("mechanical sections are grouped into one collapsed section")
    out.append("at the end. Auto-class labels are heuristic (token-level")
    out.append("normalization only); the package README.md carries the")
    out.append("adjudicated explanation.")
    out.append("")
    out.append("| | Lines |")
    out.append("|---|---|")
    out.append(f"| {oname} | {len(o_lines)} |")
    out.append(f"| {cname} | {len(c_lines)} |")
    out.append(f"| Added | +{added} |")
    out.append(f"| Review-stage comments | {review_added} of the +{added} added lines |")
    out.append(f"| Removed | -{removed} |")
    out.append(f"| Changed | {added + removed} |")
    out.append(f"| Change blocks | {len(blocks)} |")
    out.append(f"| Diff sections (context 3) | {len(groups)} |")
    out.append("")
    out.append("## Changed lines by auto-class (heuristic)")
    out.append("")
    out.append("| Auto-class | Blocks | Changed lines |")
    out.append("|---|---|---|")
    for cls in ("mechanical", "translation", "supplement", "residual"):
        if cls in class_blocks:
            out.append(f"| {cls} | {class_blocks[cls]} | {class_lines[cls]} |")
    out.append("")
    out.append("## Change-block index")
    out.append("")
    out.append("| # | Section | Original | Candidate | +/− | Auto-class | Gist |")
    out.append("|---|---|---|---|---|---|---|")
    for (n, si, tag, i1, i2, j1, j2, cls) in blocks:
        o_rng = f"{i1 + 1}–{i2}" if i2 > i1 else "—"
        c_rng = f"{j1 + 1}–{j2}" if j2 > j1 else "—"
        gist = _gist(o_lines[i1:i2], c_lines[j1:j2]).replace("|", "\\|")
        out.append(f"| {n} | {si} | {o_rng} | {c_rng} | "
                   f"+{j2 - j1}/−{i2 - i1} | {cls} | {gist} |")
    out.append("")
    out.append("## Full diff")
    out.append("")
    for si, group in enumerate(groups, 1):
        if si in mech_sections:
            continue
        ga = sum(op[4] - op[3] for op in group if op[0] != "equal")
        gr = sum(op[2] - op[1] for op in group if op[0] != "equal")
        a_rng = f"{group[0][1] + 1}–{group[-1][2]}"
        b_rng = f"{group[0][3] + 1}–{group[-1][4]}"
        classes = ", ".join(sorted(sec_classes.get(si, set())))
        out.append("<details>")
        out.append(f"<summary>Section {si} — original {a_rng} · "
                   f"candidate {b_rng} · +{ga}/−{gr} · {classes}</summary>")
        out.append("")
        out.append("```diff")
        out.extend(sections[si - 1])
        out.append("```")
        out.append("")
        out.append("</details>")
        out.append("")
    if mech_sections:
        out.append("<details>")
        out.append(f"<summary>Purely mechanical sections "
                   f"({', '.join(str(s) for s in mech_sections)}) — "
                   f"whitespace, host, and branch-token changes only "
                   f"(heuristic)</summary>")
        out.append("")
        for si in mech_sections:
            out.append("```diff")
            out.extend(sections[si - 1])
            out.append("```")
            out.append("")
        out.append("</details>")
        out.append("")
    return "\n".join(out)


_COMMENT_PAIRS = (("/*", "*/"), ("<!--", "-->"), ("[!--", "--]"))


def review_stage_lines(lines):
    """0-based indexes of candidate lines that are review-stage comments.

    A review-stage comment is a comment block (CSS /* */, HTML <!-- -->,
    or Wikidot [!-- --]) that carries the REVIEW: marker, or a lone line
    carrying the marker outside any block. Every line of such a block
    counts: the marker heads the block, the rest is its body.
    """
    closers = dict(_COMMENT_PAIRS)
    marked = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        opener = next((op for op, _ in _COMMENT_PAIRS if op in line), None)
        if opener is None:
            if "REVIEW:" in line:
                marked.add(i)
            i += 1
            continue
        closer = closers[opener]
        j = i
        block = []
        while j < len(lines):
            block.append(lines[j])
            if closer in lines[j] and (
                    j > i or lines[j].index(closer) > lines[j].index(opener)):
                break
            j += 1
        if any("REVIEW:" in b for b in block):
            marked.update(range(i, min(j, len(lines) - 1) + 1))
        i = j + 1
    return marked


def count_review_added(o_lines, c_lines):
    """Added diff lines that are review-stage comments in the candidate."""
    marked = review_stage_lines(c_lines)
    if not marked:
        return 0
    matcher = difflib.SequenceMatcher(a=o_lines, b=c_lines, autojunk=False)
    n = 0
    for tag, _i1, _i2, j1, j2 in matcher.get_opcodes():
        if tag in ("insert", "replace"):
            n += sum(1 for j in range(j1, j2) if j in marked)
    return n


def generate(pkg):
    orig, cand = package_files(pkg)
    original = orig.read_text(encoding="utf-8")
    candidate = cand.read_text(encoding="utf-8")
    o_lines = original.splitlines()
    c_lines = candidate.splitlines()
    diff = list(difflib.unified_diff(
        o_lines, c_lines,
        fromfile=orig.name, tofile=cand.name, lineterm=""))
    added = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
    removed = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
    hunks = sum(1 for l in diff if l.startswith("@@"))
    review_added = count_review_added(o_lines, c_lines)
    if added + removed <= TIER2_CHANGED_LINES and hunks <= TIER2_HUNKS:
        return generate_tier1(pkg, orig.name, cand.name, o_lines, c_lines,
                              diff, review_added)
    return generate_tier2(pkg, orig.name, cand.name, o_lines, c_lines,
                          diff, review_added)


# ------------------------------------------------------- vendored record
#
# The stamp data model (campaign memo VERDICT-STAMP) assembles each
# theme's verdicts from the vendored record in review/AUTHORITIES/.
# The render part list is an explicit allowlist: RENDER-ROWS-RERUN16-
# PARTIAL.md is excluded BY NAME, never globbed (rule S2 — it holds
# mid-run rows plus static predictions the final RERUN16 supersedes).

# Seed alias table, from LEDGER-POPULATION-CHECK section 2 (items E3/E4
# and its normalisation rule). The population and ledger (b) key the
# telecom theme by its short form; every ledger part and the canonical
# candidate file use the long form. Amethyst's render row is spelled
# theme:amethyst-v2-jp in RENDER-ROWS-2. Part rows are stored under the
# population fullname; the candidate file is looked up under the long
# form where one exists. --check verifies these names still appear in
# the vendored population check (check_seed_table).
PART_ALIASES = {
    "theme:telecommunications-monitoring-office-theme-jp":
        "theme:telecom-office-theme-jp",
    "theme:amethyst-v2-jp": "theme:amethyst-v2",
}
FILE_ALIASES = {
    "theme:telecom-office-theme-jp":
        "theme:telecommunications-monitoring-office-theme-jp",
}


def _norm(name):
    return PART_ALIASES.get(name, name)


RENDER_PART_FILES = (
    "RENDER-ROWS-1.md",
    "RENDER-ROWS-2.md",
    "RENDER-ROWS-G.md",
    "RENDER-ROWS-RERUN16.md",
)


def _section(text, start_marker, end_marker):
    a = text.index(start_marker)
    b = text.index(end_marker, a) if end_marker else len(text)
    return text[a:b]


def _rows(text):
    for line in text.splitlines():
        if line.startswith("|"):
            yield [c.strip() for c in line.split("|")]


def _load_ledger_b():
    text = (AUTH / "GOSIGN2-LEDGER.md").read_text(encoding="utf-8")
    by_name, by_n = {}, {}
    for p in _rows(_section(text, "## (b)", "## (c)")):
        if len(p) >= 10 and p[1].isdigit() and p[2].startswith("theme:"):
            row = {"n": int(p[1]), "fullname": p[2], "origin": p[3],
                   "t1": p[4], "t23": p[5], "t4": p[6], "t5": p[7],
                   "overall": p[8]}
            by_name[row["fullname"]] = row
            by_n[row["n"]] = row
    return by_name, by_n


def _load_t1():
    text = (PARTS / "T1-ROWS.md").read_text(encoding="utf-8")
    by_name, by_row = {}, {}
    for p in _rows(text):
        if len(p) >= 9 and p[1].isdigit():
            name = p[2].strip("`")
            row = {"row": int(p[1]),
                   "fullname": name if name.startswith("theme:") else None,
                   "exit": p[3], "errors": int(p[4]) if p[4].isdigit() else None,
                   "warns": int(p[5]) if p[5].isdigit() else None,
                   "infos": int(p[6]) if p[6].isdigit() else None,
                   "multiset": p[7]}
            by_row[row["row"]] = row
            if row["fullname"]:
                by_name[_norm(row["fullname"])] = row
    return by_name, by_row


def _load_localize():
    text = (PARTS / "LOCALIZE-ROWS.md").read_text(encoding="utf-8")
    by_name, by_row = {}, {}
    for p in _rows(text):
        if len(p) >= 8 and p[1].isdigit():
            name = p[2]
            row = {"row": int(p[1]),
                   "fullname": name if name.startswith("theme:") else None,
                   "source": p[3], "t4": p[4], "t5": p[5], "disp": p[6]}
            by_row[row["row"]] = row
            if row["fullname"]:
                by_name[_norm(row["fullname"])] = row
    return by_name, by_row


def _load_render(filename):
    text = (PARTS / filename).read_text(encoding="utf-8")
    rows = {}
    for p in _rows(text):
        if len(p) >= 6 and p[1].startswith("theme:"):
            rows[_norm(p[1])] = {"fullname": p[1], "t2": p[2], "t3": p[3],
                                 "cell": "|".join(p[4:-2]).strip(),
                                 "source": p[-2]}
    return rows


def _load_supplement():
    text = (AUTH / "GOSIGN2-LEDGER-SUPPLEMENT.md").read_text(encoding="utf-8")
    items, by_id = {}, {}
    for p in _rows(_section(text, "## (a)", "## (b)")):
        if len(p) >= 7 and p[1].isdigit():
            row = {"id": int(p[1]), "cls": p[2], "fullname": p[3],
                   "outcome": p[4], "text": "|".join(p[5:-1]).strip()}
            items.setdefault(row["fullname"], []).append(row)
            by_id[row["id"]] = row
    checks = {}
    ctext = _section(text, "## (c)", "## (d)")
    blocks = re.split(r"(?m)^(?=\d+\.\s)", ctext)
    for block in blocks:
        m = re.match(r"(\d+)\.\s", block)
        if not m:
            continue
        for im in re.finditer(r"\(items?\s+([\d,\s]+)\)", block):
            for tok in im.group(1).split(","):
                tok = tok.strip()
                if tok.isdigit():
                    checks[int(tok)] = int(m.group(1))
    return items, by_id, checks


class Records:
    """The vendored campaign record, loaded once per generator run."""

    def __init__(self):
        self.ledger_b, self.ledger_b_by_n = _load_ledger_b()
        self.t1, self.t1_by_row = _load_t1()
        self.localize, self.localize_by_row = _load_localize()
        self.render = {name: _load_render(name) for name in RENDER_PART_FILES}
        self.supp_items, self.supp_by_id, self.supp_checks = _load_supplement()


# Hardcoded exception record for theme:amethyst-v2, the named exception.
# Its rows cannot be joined by fullname at all (blank fullname cells in
# T1-ROWS row 144 and LOCALIZE-ROWS row 287, spelled theme:amethyst-v2-jp
# in RENDER-ROWS-2, theme:amethyst-v2 in ledger (b)); the record below is
# sourced from LEDGER-POPULATION-CHECK section 2 item E3 and the ledger
# rows it names. If this record is absent the generator must fail, not
# emit a stamp with blank lines.
AMETHYST_LINES = (
    "- Theme: theme:amethyst-v2 — origin CN, population #162 [GOSIGN2-LEDGER (b) row 162]",
    "- Overall: EXCEPTION — named exception, outside the pass-eligible set: no candidate could be produced; the go-sign (COMPLETION-REPORT §10) covers the 286 pass-eligible themes with this exception standing [GOSIGN2-LEDGER (b) row 162; GOSIGN2-LEDGER-SUPPLEMENT (d)]",
    "- T1 (source check): EXCEPTION — no candidate exists; the part carries the theme as an unnamed exception row with all cells blank [T1-ROWS row 144]",
    "- T2/T3 (render, combined verdict): NOT-RUN — [combined T2/T3] report `EXCEPTION` — standing named exception: component-family theme, no standalone candidate or sample could be produced (CN1 lane MANIFEST.md evidence; canonical file pages/theme:amethyst-v2-jp.txt absent); no T2/T3 runs were made. [RENDER-ROWS-2, where the row is spelled theme:amethyst-v2-jp]",
    "- Engine coverage: not run [RENDER-ROWS-2 row]",
    "- Credit modal: not applicable — no sample run exists [RENDER-ROWS-2 row]",
    "- T4 (localize patterns + follow-up): N/A (named exception — no candidate) — display-affecting findings: 0 [LOCALIZE-ROWS row 287, where the fullname cell is blank]",
    "- T5 (translation text): N/A (named exception — no candidate) — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 287]",
    "- FIX5 re-judgement: none — the theme is the named exception and stands outside the 107-item register [GOSIGN2-LEDGER-SUPPLEMENT (d)]",
)


# -------------------------------------------------------- verdict stamp

def _plural(n, word):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def _render_row(rec, fullname):
    # Rule S1: RERUN16 supersedes ROWS-2 wholesale for its 17 themes.
    for name in ("RENDER-ROWS-RERUN16.md", "RENDER-ROWS-1.md",
                 "RENDER-ROWS-G.md", "RENDER-ROWS-2.md"):
        if fullname in rec.render[name]:
            return name[:-3], rec.render[name][fullname]
    raise KeyError(f"no render row for {fullname}")


def _rows1_core(source):
    m = re.match(r"^(.+?) \((row \d+)\)$", source)
    if m:
        return f"{m.group(1)} {m.group(2)}"
    m = re.match(r"^(.+?) \((?:EN|CN|KO)\d+\)$", source)
    if m:
        return m.group(1)
    return source


def _batch(source):
    m = re.search(r"\(([A-Z]+\d+)\)$", source)
    return m.group(1) if m else source


def _t23_citation(part, row):
    if part == "RENDER-ROWS-1":
        return f"[RENDER-ROWS-1 ({_rows1_core(row['source'])})]"
    if part == "RENDER-ROWS-G":
        return f"[RENDER-ROWS-G ({_batch(row['source'])})]"
    if part == "RENDER-ROWS-RERUN16":
        return (f"[RENDER-ROWS-RERUN16 ({_batch(row['source'])}) — supersedes "
                f"the RENDER-ROWS-2 row for this theme, rule S1]")
    return f"[RENDER-ROWS-2 ({row['source']})]"


def _credit_citation(part, row):
    if part == "RENDER-ROWS-1":
        return f"[RENDER-ROWS-1 ({_rows1_core(row['source'])})]"
    if part == "RENDER-ROWS-G":
        return f"[RENDER-ROWS-G ({_batch(row['source'])})]"
    if part == "RENDER-ROWS-RERUN16":
        return "[RENDER-ROWS-RERUN16 row]"
    return f"[RENDER-ROWS-2 ({row['source']})]"


def _overall_line(rec, fullname, brow):
    if brow["overall"] == "PASS":
        return (f"- Overall: PASS — passed at the ledger determination; "
                f"no OPEN items [GOSIGN2-LEDGER (b) row {brow['n']}]")
    if brow["overall"].startswith("EXCEPTION"):
        return (f"- Overall: EXCEPTION — named exception, outside the "
                f"pass-eligible set [GOSIGN2-LEDGER (b) row {brow['n']}]")
    items = rec.supp_items.get(fullname, [])
    still = [i for i in items if i["outcome"] == "STILL OPEN"]
    if still:
        return (f"- Overall: NOT PASS — NOT PASS at the ledger determination "
                f"(section (e) register); {len(still)} OPEN item(s) remain "
                f"STILL OPEN after the FIX5 re-judgement "
                f"[GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (a)]")
    outcomes = {i["outcome"] for i in items}
    if outcomes == {"FIXED"}:
        oc = "FIXED"
    elif outcomes == {"DISPOSITIONED"}:
        oc = "DISPOSITIONED with grounds"
    else:
        oc = "FIXED / DISPOSITIONED"
    k = len(items)
    cnt = ("its one OPEN item" if k == 1 else
           "both OPEN items" if k == 2 else f"all {k} OPEN items")
    return (f"- Overall: PASS — NOT PASS at the ledger determination "
            f"(section (e) register); {cnt} re-judged {oc} by the FIX5 wave; "
            f"go-sign issued 2026-11-17 (COMPLETION-REPORT §10) "
            f"[GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]")


def _t1_line(rec, fullname, brow):
    t1 = rec.t1[fullname]
    word = brow["t1"]
    nums = (f"exit {t1['exit']}, {_plural(t1['errors'], 'error')} / "
            f"{_plural(t1['warns'], 'warn')} / {_plural(t1['infos'], 'info')}")
    if t1["multiset"] == "—":
        mult, codes = "(no error codes)", set()
    else:
        mult = f"({t1['multiset']})"
        codes = {seg.rsplit("×", 1)[0].strip()
                 for seg in t1["multiset"].split(",")}
    if word == "PASS":
        suffix = ""
        cite = f"[T1-ROWS row {t1['row']}; GOSIGN2-LEDGER (b) row {brow['n']}]"
    elif codes and codes <= {"no-credit", "no-rate"}:
        # The environment-form named exception (ledger (d) item 2, KB-53):
        # sigma-10's standing codes are dispositioned in register c1.
        suffix = ("; both codes dispositioned in register c1 as the "
                  "environment-form named exception (KB-53)")
        cite = f"[T1-ROWS row {t1['row']}; GOSIGN2-LEDGER (c1)]"
    else:
        suffix = "; standing classes dispositioned in register c1"
        cite = f"[T1-ROWS row {t1['row']}; GOSIGN2-LEDGER (b) row {brow['n']}]"
    return (f"- T1 (source check): {word} — baseline 2026-11-16: {nums} "
            f"{mult}{suffix} {cite}")


def _engine_line(part, row):
    cell = row["cell"]
    if part == "RENDER-ROWS-G":
        # Rule S4: coverage comes from the row's findings cell, never the
        # part header.
        if "mixed coverage" in cell:
            txt = "mixed: page full-engine, sample chromium-only"
        elif "chromium-only coverage" in cell:
            txt = "chromium-only, both pages (no WebKit verdict)"
        else:
            txt = "full (chromium+webkit, both pages)"
        return f"- Engine coverage: {txt} [RENDER-ROWS-G row, findings cell]"
    if part == "RENDER-ROWS-RERUN16":
        # The rerun ran the full matrix for all 17 themes (part header);
        # its findings cells state no coverage phrase.
        return (f"- Engine coverage: full (chromium+webkit, both pages) "
                f"[RENDER-ROWS-RERUN16 ({_batch(row['source'])})]")
    base = ("full matrix as run by the lane; coverage not separately "
            "caveated in the row")
    if "Wikidot 503" in cell and "unjudgeable" in cell:
        m = re.search(r"(sample chromium-\d+)", cell)
        width = m.group(1) if m else "sample chromium-1366"
        return (f"- Engine coverage: full matrix as run by the lane, with "
                f"one width unjudgeable ({width}, transient Wikidot 503; "
                f"ledger (a) caveat 3) [{part} row; GOSIGN2-LEDGER (a)]")
    if "does not exist (404" in cell:
        return (f"- Engine coverage: {base} (the sample page itself 404s — "
                f"there is no sample render to caveat) [{part} row]")
    if "inconclusive" in cell or "exit 2" in cell:
        return (f"- Engine coverage: {base} (the row records inconclusive "
                f"runs, carried verbatim above) [{part} row]")
    return f"- Engine coverage: {base} [{part} row]"


_DISPO = ("sample credit-modal errors dispositioned preview-form "
          "(credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 "
          "amendment, 2026-11-16)")


def _credit_line(part, row):
    cell = row["cell"]
    cite = _credit_citation(part, row)
    if "NO credit-modal machine line" in cell:
        # Hazard H4 state (ii): the row itself records the absence; quote
        # its own clause rather than stamping the disposition.
        seg = next(s for s in cell.split("; ")
                   if "NO credit-modal machine line" in s)
        return (f"- Credit modal: no credit-modal line recorded — the row "
                f"states the {seg} {cite}")
    if part == "RENDER-ROWS-1":
        # Hazard H4: ROWS-1 phrases the line bare (`sample credit-modal`)
        # and takes the preview-form disposition from the part header.
        if "sample credit-modal" in cell or "(shared showcase)" in cell:
            dispo = (_DISPO[:-1] + "; ROWS-1 phrases the line bare and "
                     "takes the disposition from the part header)")
            return f"- Credit modal: {dispo} {cite}"
        if "does not exist (404" in cell:
            return (f"- Credit modal: no credit-modal line in this theme's "
                    f"row; the sample page does not exist, so no sample "
                    f"credit-modal error could arise {cite}")
        if "preview-static-credit" in cell:
            return (f"- Credit modal: no sample credit-modal line in this "
                    f"theme's row; the row's only credit item is the shared "
                    f"preview-static-credit panel, recorded as cross-cutting, "
                    f"not a per-theme fault {cite}")
        return (f"- Credit modal: no credit-modal line in this theme's row; "
                f"no sample credit-modal error recorded {cite}")
    if "credit-modal (preview-form)" in cell:
        return f"- Credit modal: {_DISPO} {cite}"
    return f"- Credit modal: no credit-modal line recorded {cite}"


_PREFIX_RE = re.compile(
    r"^FIX\d-[A-Z0-9-]+( §\d+)?(, commit [0-9a-f]+)?"
    r"( \(no edit(, no commit)?\))?$")


def _fix5_line(rec, fullname, brow):
    items = rec.supp_items.get(fullname, [])
    if not items:
        return (f"- FIX5 re-judgement: none — no OPEN items at the ledger "
                f"determination [GOSIGN2-LEDGER (b) row {brow['n']}]")
    if len(items) == 1:
        head = (f"item {items[0]['id']} (class {items[0]['cls']}) "
                f"{items[0]['outcome']}")
    else:
        head = "items " + ", ".join(
            f"{i['id']} (class {i['cls']}) {i['outcome']}" for i in items)
    groups = []
    for i in items:
        text = i["text"]
        if ": " in text:
            pre, body = text.split(": ", 1)
            pre = re.sub(r"(?<=\s)s(\d+)\b", r"§\1", pre)
            if not _PREFIX_RE.match(pre):
                pre, body = "", text
        else:
            pre, body = "", text
        body = re.sub(r"\s*Spot-verified\b[^.]*\.\s*$", "", body).rstrip()
        if body.endswith("."):
            body = body[:-1]
        if groups and groups[-1][0] == pre:
            groups[-1][1].append(body)
        else:
            groups.append((pre, [body]))
    rendered = ["; ".join(bodies) if not pre else f"{pre}: {'; '.join(bodies)}"
                for pre, bodies in groups]
    text = " ".join(rendered)
    checks = {rec.supp_checks[i["id"]] for i in items
              if i["id"] in rec.supp_checks}
    if checks:
        text += "; spot-verified for this supplement"
    ids = [i["id"] for i in items]
    if len(ids) == 1:
        ref = f"item {ids[0]}"
    elif max(ids) - min(ids) == len(ids) - 1:
        ref = f"items {min(ids)}–{max(ids)}"
    else:
        ref = "items " + ", ".join(str(x) for x in ids)
    bracket = f"[GOSIGN2-LEDGER-SUPPLEMENT (a) {ref}"
    if len(checks) == 1:
        bracket += f"; (c) check {next(iter(checks))}"
    bracket += "]"
    return f"- FIX5 re-judgement: {head} — {text} {bracket}"


def assemble_stamp(rec, fullname):
    """The full generated stamp block for a theme, markers included."""
    if fullname == "theme:amethyst-v2":
        lines = [STAMP_BEGIN, "## Verdict stamp", *AMETHYST_LINES,
                 f"- Computed against: canonical commit {FIX5_HEAD}; "
                 f"candidate file: absent (pages/theme:amethyst-v2-jp.txt "
                 f"does not exist); {RECORD_SUFFIX}", STAMP_END]
        return "\n".join(lines) + "\n"
    brow = rec.ledger_b[fullname]
    rel = f"pages/{FILE_ALIASES.get(fullname, fullname)}.txt"
    cand = REPO / rel
    cur_sha = sha256_file(cand) if cand.is_file() else ""
    verdict_sha = git_blob_sha(rel, FIX5_HEAD)
    stale = not cand.is_file() or verdict_sha is None or cur_sha != verdict_sha
    commit = git_last_change(rel) or git_head()
    lines = [STAMP_BEGIN, "## Verdict stamp"]
    lines.append(f"- Theme: {fullname} — origin {brow['origin']}, "
                 f"population #{brow['n']} [GOSIGN2-LEDGER (b) row {brow['n']}]")
    if stale:
        # A changed file must never carry a fresh PASS: the verdict words
        # stay below, explicitly bannered as describing the pre-change file.
        lines.append(
            f"- Overall: STALE — candidate file changed since the verdict "
            f"was computed (verdict against 435a6bb-era content, file "
            f"sha256 now {cur_sha}); verdict not carried over, "
            f"re-judgement required")
        lines.append("> verdicts below describe the pre-change file")
    else:
        lines.append(_overall_line(rec, fullname, brow))
    lines.append(_t1_line(rec, fullname, brow))
    part, row = _render_row(rec, fullname)
    lines.append(f"- T2/T3 (render, combined verdict): {brow['t23']} — "
                 f"{row['cell']} {_t23_citation(part, row)}")
    lines.append(_engine_line(part, row))
    lines.append(_credit_line(part, row))
    loc = rec.localize[fullname]
    src = loc["source"].split(" ")[0]
    lines.append(f"- T4 (localize patterns + follow-up): {loc['t4']} — "
                 f"display-affecting findings: {loc['disp']} "
                 f"[LOCALIZE-ROWS row {loc['row']}, source {src}]")
    lines.append(f"- T5 (translation text): {loc['t5']} — the source reports "
                 f"judge T4/T5 jointly; one verdict word covers both "
                 f"[LOCALIZE-ROWS row {loc['row']}]")
    lines.append(_fix5_line(rec, fullname, brow))
    note = "" if fullname.endswith("-jp") else " (shared original+port page; no -jp file)"
    lines.append(f"- Computed against: canonical commit {commit}; "
                 f"candidate file {rel}{note} sha256:{cur_sha}; "
                 f"{RECORD_SUFFIX}")
    lines.append(STAMP_END)
    return "\n".join(lines) + "\n"


# ------------------------------------------- generated README regions

def apply_stamp(readme_text, block):
    """Insert or refresh the verdict stamp block in a theme README."""
    block = block.rstrip("\n")
    if STAMP_BEGIN in readme_text:
        a = readme_text.index(STAMP_BEGIN)
        b = readme_text.index(STAMP_END) + len(STAMP_END)
        return readme_text[:a] + block + readme_text[b:]
    lines = readme_text.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("# "):
            lines[i + 1:i + 1] = ["", *block.split("\n")]
            return "\n".join(lines)
    return block + "\n\n" + readme_text


def extract_stamp(readme_text):
    if STAMP_BEGIN not in readme_text:
        return None
    a = readme_text.index(STAMP_BEGIN)
    b = readme_text.index(STAMP_END) + len(STAMP_END)
    return readme_text[a:b]


# --------------------------------------------------------- site Status

_STATUS_FIELDS = (
    ("Package status", "package_status"),
    ("Candidate status", "candidate_status"),
    ("Verification status", "verification_status"),
    ("Governing requirement", "governing_requirement"),
)


def render_status_block(pkg):
    """The generated Status stamp of a site package, from status.tsv."""
    src = {}
    for line in (pkg / "status.tsv").read_text(encoding="utf-8").splitlines():
        if "\t" in line:
            k, v = line.split("\t", 1)
            src[k.strip()] = v.strip()
    # The named commit is the last commit touching the material the
    # stamp vouches for (the original and candidate files). status.tsv
    # is the stamp's own configuration and the README is generated, so
    # neither may move it; HEAD would make the field self-referential.
    inputs = sorted(p.name for p in pkg.glob("original.*")) \
        + sorted(p.name for p in pkg.glob("candidate.*"))
    commit = (git_last_change(*[f"review/{pkg.name}/{n}" for n in inputs])
              or git_head())
    out = [STATUS_BEGIN, "| Field | Value |", "|---|---|"]
    for label, key in _STATUS_FIELDS:
        out.append(f"| {label} | {src.get(key, '')} |")
    out.append(f"| Canonical commit | {commit} |")
    out.append(STATUS_END)
    return "\n".join(out)


def apply_status(readme_text, block):
    """Insert or refresh the generated Status table in the ## Status
    section of a site package README. Only the table is generated; the
    prose and quotations around it stay hand-written."""
    m = re.search(r"^## Status\s*$", readme_text, re.M)
    if not m:
        return readme_text
    nxt = re.search(r"^## ", readme_text[m.end():], re.M)
    sec_end = m.end() + nxt.start() if nxt else len(readme_text)
    section = readme_text[m.start():sec_end]
    if STATUS_BEGIN in section:
        a = section.index(STATUS_BEGIN)
        b = section.index(STATUS_END) + len(STATUS_END)
        section = section[:a] + block + section[b:]
    else:
        lines = section.split("\n")
        start = next(i for i, l in enumerate(lines) if l.startswith("|"))
        end = start
        while end < len(lines) and lines[end].startswith("|"):
            end += 1
        lines[start:end] = block.split("\n")
        section = "\n".join(lines)
    return readme_text[:m.start()] + section + readme_text[sec_end:]


# ------------------------------------------------------------- --check

def check_stamp_citations(block, fullname, rec):
    """Every citation locator inside a stamp must resolve against the
    vendored record for this theme."""
    problems = []
    for m in re.finditer(r"GOSIGN2-LEDGER \(b\) row (\d+)", block):
        row = rec.ledger_b_by_n.get(int(m.group(1)))
        if not row or row["fullname"] != fullname:
            problems.append(
                f"citation does not resolve: GOSIGN2-LEDGER (b) row "
                f"{m.group(1)} is not {fullname}")
    for m in re.finditer(r"T1-ROWS row (\d+)", block):
        row = rec.t1_by_row.get(int(m.group(1)))
        ok = row and (_norm(row["fullname"] or "") == fullname or
                      (fullname == "theme:amethyst-v2" and row["row"] == 144))
        if not ok:
            problems.append(
                f"citation does not resolve: T1-ROWS row {m.group(1)} "
                f"is not {fullname}")
    for m in re.finditer(r"LOCALIZE-ROWS row (\d+)", block):
        row = rec.localize_by_row.get(int(m.group(1)))
        ok = row and (_norm(row["fullname"] or "") == fullname or
                      (fullname == "theme:amethyst-v2" and row["row"] == 287))
        if not ok:
            problems.append(
                f"citation does not resolve: LOCALIZE-ROWS row "
                f"{m.group(1)} is not {fullname}")
    for m in re.finditer(r"RENDER-ROWS-(1|2|G|RERUN16)", block):
        rows = rec.render[f"RENDER-ROWS-{m.group(1)}.md"]
        ok = (fullname in rows or
              (fullname == "theme:amethyst-v2" and m.group(1) == "2"
               and "theme:amethyst-v2-jp" in rows))
        if not ok:
            problems.append(
                f"citation does not resolve: RENDER-ROWS-{m.group(1)} "
                f"has no row for {fullname}")
    for m in re.finditer(r"SUPPLEMENT \(a\) items? ([\d, –-]+)", block):
        ids = [int(t) for t in re.findall(r"\d+", m.group(1))]
        for i in ids:
            row = rec.supp_by_id.get(i)
            if not row or row["fullname"] != fullname:
                problems.append(
                    f"citation does not resolve: SUPPLEMENT (a) item {i} "
                    f"is not {fullname}")
    return problems


def check_vendored_hashes():
    problems = []
    idx = (AUTH / "INDEX.md").read_text(encoding="utf-8")
    name = None
    for line in idx.splitlines():
        hm = re.match(r"^###\s+`([^`]+)`", line) or \
            re.match(r"^###\s+(\S+\.md)\b", line)
        if hm:
            name = hm.group(1)
        sm = re.search(r"SHA-256:\s+`([0-9a-f]{64})`", line)
        if sm and name:
            f = AUTH / name
            if not f.is_file():
                problems.append(f"vendored file missing: AUTHORITIES/{name}")
            elif sha256_file(f) != sm.group(1):
                problems.append(f"vendored hash drift: AUTHORITIES/{name}")
            name = None
    return problems


def check_seed_table():
    text = (PARTS / "LEDGER-POPULATION-CHECK.md").read_text(encoding="utf-8")
    problems = []
    for token in ("theme:amethyst-v2", "theme:sigma-10-jp",
                  "theme:telecommunications-monitoring-office-theme-jp"):
        if token not in text:
            problems.append(
                f"seed table drift: {token} missing from "
                f"LEDGER-POPULATION-CHECK")
    return problems


def all_packages():
    return sorted(d for d in HERE.iterdir()
                  if d.is_dir() and d.name != "AUTHORITIES")


def main():
    check = "--check" in sys.argv[1:]
    stale = []
    problems = []
    for pkg in packages():
        generated = generate(pkg)
        target = pkg / "diff.md"
        if check:
            if not target.is_file() or target.read_text(encoding="utf-8") != generated:
                stale.append(pkg.name)
        else:
            target.write_text(generated, encoding="utf-8")
            print(f"diff.md regenerated (review/{pkg.name})")
    if check and stale:
        print("diff.md stale for: " + ", ".join(stale)
              + "; run review/build_review.py", file=sys.stderr)
    try:
        rec = Records()
    except (OSError, ValueError, KeyError) as e:
        rec = None
        problems.append(f"vendored record could not be loaded: {e}")
    if rec is not None:
        for pkg in all_packages():
            readme = pkg / "README.md"
            if not readme.is_file():
                continue
            cur = readme.read_text(encoding="utf-8")
            new = cur
            fullname = f"theme:{pkg.name}"
            if (pkg / "candidate.txt").is_file() and fullname in rec.ledger_b:
                block = assemble_stamp(rec, fullname)
                new = apply_stamp(new, block)
                if check:
                    present = extract_stamp(cur)
                    if present is not None:
                        problems += [
                            f"review/{pkg.name}/README.md: {p}"
                            for p in check_stamp_citations(
                                present, fullname, rec)]
            if (pkg / "status.tsv").is_file():
                new = apply_status(new, render_status_block(pkg))
            if new != cur:
                if check:
                    stale.append(f"{pkg.name} (README generated region)")
                else:
                    readme.write_text(new, encoding="utf-8")
                    print(f"README stamp regenerated (review/{pkg.name})")
        if check:
            problems += check_vendored_hashes()
            problems += check_seed_table()
    for p in problems:
        print(f"PROBLEM: {p}", file=sys.stderr)
    if check:
        if stale or problems:
            if stale:
                print("stale generated files for: " + ", ".join(stale),
                      file=sys.stderr)
            return 1
        print("all diff.md files are up to date")
        print("all stamps are up to date; citations resolve; "
              "vendored hashes match")
    return 0


if __name__ == "__main__":
    sys.exit(main())
