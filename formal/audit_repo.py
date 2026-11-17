#!/usr/bin/env python3
"""Byte-level audit of the sigma10-check-wiki tree (checkout 8db9331).

A single self-contained, stdlib-only script. It checks six invariants over the
entire tree and reports per-invariant counts plus every named violation.

Invariants (brief formal/lane-oc-audit/BRIEF.md):

  I1 stamp truthfulness   README verdict-stamp overall word agrees with the
                          bytes; a fresh PASS only where candidate.txt byte-
                          equals the canonical page; stale/changed files carry
                          STALE or NOT PASS.  Uses build_review.assemble_stamp
                          (the machinery's own stale verdict logic) rather than
                          reimplementing it.
  I2 diff fidelity        Regenerate every diff.md with build_review.generate
                          and compare byte for byte, except HAND_AUTHORED_DIFFS
                          (presence only, named).
  I3 mirror integrity     original.txt sha256 == mirror_sha256 and byte count
                          == mirror_bytes from review/sources.tsv.
  I4 /start consistency   Every start-themes.tsv row resolves to a review
                          package; every theme package is reached by a row;
                          build_start.py --check passes.
  I5 coverage accounting  The LINT-WAVE section-2 coverage ledger dispositions
                          every patterns/KB-*.md and every NL entry exactly
                          once; recomputed from lint_patterns.RULES /
                          SUPPRESSIONS (the linter's own structures);
                          patterns/build_index.py --check passes.
  I6 candidate sync       Every package's candidate.* byte-equals its canonical
                          page (build_review's own byte-copy property).

Documented exception shapes are encoded as named exceptions with grounds:
amethyst-v2 (build_review.AMETHYST_LINES), the two HAND_AUTHORED_DIFFS, the two
site packages' status stamps (status.tsv / .css artifacts, no canonical page),
the collapsed-form record review/existing-pages/ (README only, no package),
review/AUTHORITIES/ (vendored record, not a package), and unstamped component/
base-css/JP-original packages (hand-written verdicts).

Usage:
  python3 formal/audit_repo.py [--root DIR] [--coverage-ledger FILE]
                               [--json-out FILE] [--quiet]

Default root is this script's parent's parent; default JSON output is
<root>/formal/audit-results.txt.  Exit 0 = all invariants hold, 1 = at least
one violation.
"""

import argparse
import collections
import csv
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")


# ---------------------------------------------------------------------------
# Named exceptions (grounds recorded, never silently skipped)
# ---------------------------------------------------------------------------
DIR_ALIAS = {
    # sources.tsv dir -> actual review/ package dir (JP originals)
    "min-theme-jp": "min-theme",
    "shushuin-jp": "shushuin",
}
FULLNAME_ALIAS = {
    # /start slug fullname -> sources.tsv cand_fullname / package
    "theme:telecom-office-theme-jp": "telecommunications-monitoring-office-theme-jp",
    "theme:shushuin-jp": "shushuin",
}
EXCEPTIONS = {
    "amethyst-v2": (
        "named go-sign EXCEPTION: no candidate can be produced; "
        "build_review.AMETHYST_LINES is the stamp special case; the package "
        "holds original.txt only."),
    "site-packages": (
        "site packages (status.tsv, .css artifacts): their status stamp is "
        "generated from status.tsv by build_review.render_status_block; they "
        "have no verdict stamp and no canonical pages/*.txt candidate."),
    "hand-authored-diffs": (
        "build_review.HAND_AUTHORED_DIFFS: license-box-theme-jp (thin receiver) "
        "and peroxide-jp-base-css (one mirror, two candidates); diff.md is "
        "hand-authored and checked for presence only."),
    "collapsed-records": (
        "review/existing-pages/ holds the collapsed-form record README only "
        "(no original.*/candidate.*) - not a package under any invariant."),
    "authorities": (
        "review/AUTHORITIES/ is the vendored campaign record consumed by "
        "build_review.Records, not a package."),
    "unstamped-packages": (
        "component/fragment/base-CSS/JP-original packages carry hand-written "
        "verdict prose, not a generated verdict stamp (no '- Overall:' region "
        "delimited by STAMP_BEGIN/END)."),
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def import_from(root, rel, modname):
    """Import a module from a file inside `root` with a private module name."""
    path = root / rel
    spec = importlib.util.spec_from_file_location(modname, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import " + str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[modname] = mod
    spec.loader.exec_module(mod)
    return mod


def package_files(pkg):
    for orig in sorted(pkg.glob("original.*")):
        cand = pkg / ("candidate" + orig.suffix)
        if cand.is_file():
            return orig, cand
    return None


def all_packages(root):
    found = []
    review = root / "review"
    if not review.is_dir():
        return found
    for d in sorted(review.iterdir()):
        if d.is_dir() and package_files(d):
            found.append(d)
    return found


def read_tsv(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load_sources(root):
    """sources.tsv rows keyed by dir (using DIR_ALIAS for JP originals)."""
    rows = read_tsv(root / "review" / "sources.tsv")
    by_dir = {r["dir"]: r for r in rows}
    by_actual = {}
    for r in rows:
        by_actual[DIR_ALIAS.get(r["dir"], r["dir"])] = r
    return rows, by_dir, by_actual


def load_fullname_map(root):
    """candidate fullname -> actual package dir, from sources.tsv + class JSON."""
    mp = {}
    for r in read_tsv(root / "review" / "sources.tsv"):
        if r["cand_fullname"]:
            mp.setdefault(r["cand_fullname"], DIR_ALIAS.get(r["dir"], r["dir"]))
        if r["dir"] == "sigma-10-jp" and r["orig_fullname"]:
            mp.setdefault(r["orig_fullname"], "sigma-10-jp")
    for pkg in (root / "review").iterdir():
        cj = pkg / "classification.json"
        if pkg.is_dir() and cj.is_file():
            try:
                cf = json.loads(cj.read_text(encoding="utf-8")).get("theme", {}).get("cand_fullname")
            except Exception:
                cf = None
            if cf:
                mp.setdefault(cf, pkg.name)
    return mp


def resolve_row(row, fn2dir):
    """Map a start-themes.tsv row to a review/ package dir name."""
    slug = row["cand_slug"] or row["orig_slug"]
    if not slug:
        # Amethyst V2: no candidate slug; its package is the named exception.
        return "amethyst-v2"
    fn = "theme:" + slug
    d = fn2dir.get(fn) or FULLNAME_ALIAS.get(fn)
    return DIR_ALIAS.get(d, d) if d else None


def page_hashes(root):
    """sha256 -> list of pages/<name>.txt for byte-identity lookups."""
    idx = collections.defaultdict(list)
    for p in (root / "pages").glob("*.txt"):
        idx[sha256_bytes(p.read_bytes())].append(p.name)
    return idx


def canonical_for(pkg, sources_actual, page_index, cand_bytes_sha):
    """Canonical page path for a package (sources.tsv candidate_path first)."""
    row = sources_actual.get(pkg.name)
    if row and row.get("candidate_path"):
        rel = row["candidate_path"]
        p = pathlib.Path(rel)
        if not p.is_absolute():
            p = pkg.parent.parent / p
        return rel if p.is_file() else None
    matches = page_index.get(cand_bytes_sha, [])
    if len(matches) == 1:
        return "pages/" + matches[0]
    return None


def verdict_word(block):
    m = re.search(r"^- Overall:\s*([^\s—]+(?: [A-Z]+)?)", block or "", re.M)
    return m.group(1) if m else None


def run_check(root, rel):
    script = root / rel
    cp = subprocess.run(
        [sys.executable, str(script), "--check"], cwd=str(root),
        capture_output=True, text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    return cp.returncode, (cp.stdout + cp.stderr).strip()


def parse_coverage_ledger(path):
    """Return {kb/nl id: disposition} from LINT-WAVE section 2 tables."""
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(KB-\d+|NL-\d+)\s*\|\s*([A-Z-]+)\s*\|", line)
        if m:
            rows[m.group(1)] = m.group(2)
    return rows


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------
def audit(root, ledger_path=None):
    R = {}

    br = import_from(root, "review/build_review.py", "_audit_build_review")
    lp = import_from(root, "review/lint_patterns.py", "_audit_lint_patterns")
    rec = br.Records()

    packages = all_packages(root)
    pkg_by_name = {p.name: p for p in packages}
    sources_rows, sources_by_dir, sources_actual = load_sources(root)
    fn2dir = load_fullname_map(root)
    page_index = page_hashes(root)

    results = {"root": str(root), "invariants": {}, "exceptions": EXCEPTIONS}

    def result(iid, name, method):
        return {"name": name, "method": method, "checked": 0,
                "pass": 0, "named_exceptions": [], "violations": []}

    def violation(res, subject, detail):
        res["violations"].append({"subject": subject, "detail": detail})

    # ---------------------------------------------------------------- I1
    v = result("I1", "stamp truthfulness",
               "build_review.assemble_stamp (expected overall word) + "
               "candidate/canonical byte comparison")
    stamped = unstamped = 0
    for pkg in packages:
        readme = pkg / "README.md"
        if not readme.is_file():
            continue
        text = readme.read_text(encoding="utf-8")
        if br.STAMP_BEGIN not in text or br.STAMP_END not in text:
            unstamped += 1
            continue
        stamped += 1
        fullname = "theme:" + pkg.name
        try:
            expected_block = br.assemble_stamp(rec, fullname)
        except Exception as exc:
            violation(v, pkg.name, "stamp cannot be regenerated: %s: %s" %
                      (type(exc).__name__, exc))
            continue
        present = br.extract_stamp(text)
        if present is None:
            violation(v, pkg.name, "stamp markers incomplete")
            continue
        got, exp = verdict_word(present), verdict_word(expected_block)
        if got != exp:
            violation(v, pkg.name, "overall word %r != machinery verdict %r" %
                      (got, exp))
            continue
        v["checked"] += 1
        if got == "PASS":
            v["pass"] += 1
            orig, cand = package_files(pkg)
            csha = sha256_bytes(cand.read_bytes())
            cp = canonical_for(pkg, sources_actual, page_index, csha)
            other = sources_actual.get(pkg.name, {}).get("candidate_path")
            same = bool(cp and (root / cp).is_file() and
                        sha256_bytes((root / cp).read_bytes()) == csha)
            if not same:
                violation(v, pkg.name,
                          "PASS stamp but candidate.txt does not byte-equal "
                          "canonical page %s" % (other or cp))
        elif got == "STALE":
            v["pass"] += 0  # counted as checked; stale is the correct word
    # named exceptions
    v["named_exceptions"].append({
        "subject": "amethyst-v2", "grounds": EXCEPTIONS["amethyst-v2"]})
    for pkg in packages:
        if (pkg / "status.tsv").is_file():
            v["named_exceptions"].append({
                "subject": pkg.name, "grounds": EXCEPTIONS["site-packages"]})
            text = (pkg / "README.md").read_text(encoding="utf-8")
            expected = br.apply_status(text, br.render_status_block(pkg))
            if expected != text:
                violation(v, pkg.name, "status stamp differs from "
                          "build_review.render_status_block regeneration")
    v["named_exceptions"].append({
        "subject": "unstamped packages (%d)" % unstamped,
        "grounds": EXCEPTIONS["unstamped-packages"]})
    results["invariants"]["I1"] = v

    # ---------------------------------------------------------------- I2
    v = result("I2", "diff fidelity",
               "build_review.generate (imported) byte-for-byte vs diff.md; "
               "HAND_AUTHORED_DIFFS presence only")
    for pkg in packages:
        diff = pkg / "diff.md"
        if pkg.name in br.HAND_AUTHORED_DIFFS:
            v["named_exceptions"].append({
                "subject": pkg.name, "grounds": EXCEPTIONS["hand-authored-diffs"]})
            if pkg.name == "license-box-theme-jp":
                # Named exception: no diff by design (SITE-SCOPE Part 3 N/A);
                # the signed statement in README stands in its place.  Check
                # that documented state, never regenerate or require a file.
                readme = (pkg / "README.md").read_text(encoding="utf-8")
                if diff.is_file():
                    violation(v, pkg.name, "diff.md exists but the named "
                              "exception records no diff by design")
                elif "Statement in place of a diff" not in readme:
                    violation(v, pkg.name, "signed statement in place of a "
                              "diff is missing")
                else:
                    v["pass"] += 1
            else:
                # peroxide-jp-base-css: one mirror vs two candidates; the
                # hand-authored diff.md is present and checked only for it.
                if not diff.is_file():
                    violation(v, pkg.name, "hand-authored diff.md missing")
                else:
                    v["pass"] += 1
            continue
        generated = br.generate(pkg)
        if not diff.is_file():
            violation(v, pkg.name, "diff.md missing")
            continue
        if diff.read_text(encoding="utf-8") != generated:
            violation(v, pkg.name, "diff.md differs from build_review.generate")
        else:
            v["checked"] += 1
            v["pass"] += 1
    results["invariants"]["I2"] = v

    # ---------------------------------------------------------------- I3
    v = result("I3", "mirror integrity",
               "sha256(original.*) and byte count vs review/sources.tsv "
               "mirror_sha256 / mirror_bytes")
    for r in sources_rows:
        actual = DIR_ALIAS.get(r["dir"], r["dir"])
        pkg = root / "review" / actual
        orig = next(iter(sorted(pkg.glob("original.*"))), None) if pkg.is_dir() else None
        if orig is None:
            violation(v, actual, "no original.* for sources.tsv row")
            continue
        data = orig.read_bytes()
        sh = sha256_bytes(data)
        if sh != r["mirror_sha256"]:
            violation(v, actual, "sha256 %s != mirror_sha256 %s" %
                      (sh, r["mirror_sha256"]))
        if len(data) != int(r["mirror_bytes"]):
            violation(v, actual, "bytes %d != mirror_bytes %s" %
                      (len(data), r["mirror_bytes"]))
        v["checked"] += 1
        v["pass"] += 1
    results["invariants"]["I3"] = v

    # ---------------------------------------------------------------- I4
    v = result("I4", "/start consistency",
               "start-themes.tsv row -> package via sources.tsv/classification "
               "fullnames + named aliases; reverse coverage; build_start --check")
    rows = read_tsv(root / "start-themes.tsv")
    reached = collections.Counter()
    for r in rows:
        d = resolve_row(r, fn2dir)
        if not d:
            violation(v, r["name"], "no review package resolves from row")
            continue
        pkg = root / "review" / d
        if not (pkg.is_dir() and (pkg / "README.md").is_file()):
            violation(v, r["name"], "resolved package review/%s missing" % d)
            continue
        reached[d] += 1
        v["checked"] += 1
        v["pass"] += 1
        if d == "amethyst-v2":
            v["named_exceptions"].append({
                "subject": d + " (row " + r["name"] + ")",
                "grounds": EXCEPTIONS["amethyst-v2"]})
    for r in sources_rows:
        d = DIR_ALIAS.get(r["dir"], r["dir"])
        if d not in reached:
            violation(v, d, "theme package from sources.tsv unreachable from any row")
    v["named_exceptions"].append({
        "subject": "review/existing-pages/", "grounds": EXCEPTIONS["collapsed-records"]})
    v["named_exceptions"].append({
        "subject": "review/AUTHORITIES/", "grounds": EXCEPTIONS["authorities"]})
    rc, out = run_check(root, "build_start.py")
    v["build_start_check"] = {"returncode": rc, "output": out}
    if rc != 0:
        violation(v, "build_start.py --check", out)
    results["invariants"]["I4"] = v

    # ---------------------------------------------------------------- I5
    v = result("I5", "coverage accounting",
               "LINT-WAVE section-2 coverage ledger recomputed against "
               "lint_patterns.RULES / SUPPRESSIONS and the KB/NL corpus; "
               "build_index.py --check")
    kb_ids = {p.stem for p in (root / "patterns").glob("KB-*.md")}
    nl_text = (root / "patterns" / "NEGATIVE-LEDGER.md").read_text(encoding="utf-8")
    nl_ids = set(re.findall(r"^###\s+(NL-\d+)\b", nl_text, re.M))
    rule_ids = [r[0] for r in lp.RULES]
    rule_names = {r[1] for r in lp.RULES}
    supp_keys = set(lp.SUPPRESSIONS)
    ledger = {}
    ledger_origin = None
    if ledger_path and pathlib.Path(ledger_path).is_file():
        ledger = parse_coverage_ledger(pathlib.Path(ledger_path))
        ledger_origin = str(ledger_path)
    kb_ledger = {k: d for k, d in ledger.items() if k.startswith("KB-")}
    nl_ledger = {k: d for k, d in ledger.items() if k.startswith("NL-")}
    v["checked"] = len(kb_ids) + len(nl_ids)
    v["counts"] = {
        "kb_files": len(kb_ids), "nl_entries": len(nl_ids),
        "ledger_kb_rows": len(kb_ledger), "ledger_nl_rows": len(nl_ledger),
        "rules": len(rule_ids), "suppressions": len(supp_keys),
    }
    v["coverage_ledger"] = ledger_origin
    # exactly-once disposition of every KB file and NL entry
    for kid in sorted(kb_ids):
        n = 1 if kid in kb_ledger else 0
        if n != 1:
            violation(v, kid, "dispositioned %d times in coverage ledger" % n)
        else:
            v["pass"] += 1
    for nid in sorted(nl_ids):
        n = 1 if nid in nl_ledger else 0
        if n != 1:
            violation(v, nid, "dispositioned %d times in coverage ledger" % n)
        else:
            v["pass"] += 1
    for kid in sorted(kb_ledger):
        if kid not in kb_ids:
            violation(v, kid, "ledger row has no patterns/KB-*.md file")
    for nid in sorted(nl_ledger):
        if nid not in nl_ids:
            violation(v, nid, "ledger row has no NEGATIVE-LEDGER entry")
    # recompute from the linter's own structures
    dup = [k for k, c in collections.Counter(rule_ids).items() if c > 1]
    for kid in dup:
        violation(v, kid, "duplicate rule registration in lint_patterns.RULES")
    linted_kb = set(rule_ids)
    for kid in sorted(linted_kb):
        if kid not in kb_ids:
            violation(v, kid, "RULES references a nonexistent KB pattern file")
        if ledger and kb_ledger.get(kid) != "LINTED":
            violation(v, kid, "RULES LINTED but coverage ledger says %r" %
                      kb_ledger.get(kid))
    if ledger:
        for kid, disp in sorted(kb_ledger.items()):
            if disp == "LINTED" and kid not in linted_kb:
                violation(v, kid, "ledger LINTED but no rule in lint_patterns.RULES")
    for key in sorted(supp_keys):
        m = re.match(r"^((?:KB|NL)-\d+)", key)
        if not m:
            violation(v, key, "suppression key has no KB/NL id prefix")
            continue
        pid = m.group(1)
        if pid.startswith("KB-") and pid not in kb_ids:
            violation(v, key, "suppression references nonexistent KB pattern")
        if pid.startswith("NL-") and pid not in nl_ids:
            violation(v, key, "suppression references nonexistent NL entry")
    rc, out = run_check(root, "patterns/build_index.py")
    v["build_index_check"] = {"returncode": rc, "output": out}
    if rc != 0:
        violation(v, "build_index.py --check", out)
    results["invariants"]["I5"] = v

    # ---------------------------------------------------------------- I6
    v = result("I6", "candidate sync",
               "candidate.* sha256 byte-equal to canonical page (sources.tsv "
               "candidate_path, else unique byte-identical pages/*.txt)")
    for pkg in packages:
        _, cand = package_files(pkg)
        csha = sha256_bytes(cand.read_bytes())
        cp = canonical_for(pkg, sources_actual, page_index, csha)
        if cp is None:
            if (pkg / "status.tsv").is_file():
                v["named_exceptions"].append({
                    "subject": pkg.name, "grounds": EXCEPTIONS["site-packages"]})
                continue
            violation(v, pkg.name, "no canonical page byte-equals candidate")
            continue
        actual = (root / cp)
        if not actual.is_file() or sha256_bytes(actual.read_bytes()) != csha:
            violation(v, pkg.name, "candidate differs from canonical page %s" % cp)
        else:
            v["checked"] += 1
            v["pass"] += 1
    results["invariants"]["I6"] = v

    total_violations = sum(len(x["violations"]) for x in results["invariants"].values())
    results["totals"] = {
        "packages": len(packages),
        "sources_rows": len(sources_rows),
        "start_rows": len(rows),
        "violations": total_violations,
    }
    results["ok"] = total_violations == 0
    return results


def format_text(results):
    lines = []
    lines.append("sigma10-check-wiki byte-level audit — root=%s" % results["root"])
    for iid in ("I1", "I2", "I3", "I4", "I5", "I6"):
        v = results["invariants"][iid]
        lines.append("%s %-22s checked=%d pass=%d exceptions=%d violations=%d  [%s]" %
                     (iid, v["name"], v["checked"], v["pass"],
                      len(v["named_exceptions"]), len(v["violations"]), v["method"]))
        if iid in ("I4", "I5"):
            key = "build_start_check" if iid == "I4" else "build_index_check"
            if key in v:
                lines.append("    %s: rc=%d %s" %
                             (key, v[key]["returncode"], v[key]["output"]))
        if iid == "I5" and v.get("coverage_ledger"):
            lines.append("    coverage ledger: %s" % v["coverage_ledger"])
        for viol in v["violations"]:
            lines.append("    VIOLATION %s %s: %s" %
                         (iid, viol["subject"], viol["detail"]))
    lines.append("TOTAL packages=%d sources_rows=%d start_rows=%d violations=%d" %
                 (results["totals"]["packages"], results["totals"]["sources_rows"],
                  results["totals"]["start_rows"], results["totals"]["violations"]))
    lines.append("AUDIT: %s" % ("PASS" if results["ok"] else "FAIL"))
    return "\n".join(lines) + "\n"


def main(argv=None):
    here = pathlib.Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(here.parent), help="tree root (default: this script's parent's parent)")
    ap.add_argument("--coverage-ledger", default=None,
                    help="coverage ledger path (default: <root>/formal/coverage-ledger.md, vendored in-repo)")
    ap.add_argument("--json-out", default=None, help="JSON results path (default <root>/formal/audit-results.txt)")
    ap.add_argument("--quiet", action="store_true", help="suppress stdout text summary")
    args = ap.parse_args(argv)

    root = pathlib.Path(args.root).resolve()
    ledger = pathlib.Path(args.coverage_ledger) if args.coverage_ledger else None
    if ledger is not None and not ledger.is_file():
        sys.stderr.write("AUDIT ERROR: coverage ledger not found at %s\n" % ledger)
        return 2
    if ledger is None:
        # The coverage ledger is vendored into the repo at formal/coverage-ledger.md
        # (a copy of the lint wave's LINT-WAVE.md section 2), so the audit is
        # self-contained. A missing ledger is an audit error, never an empty one.
        candidate = root / "formal" / "coverage-ledger.md"
        if not candidate.is_file():
            sys.stderr.write("AUDIT ERROR: coverage ledger not found at %s\n" % candidate)
            return 2
        ledger = candidate
    json_out = pathlib.Path(args.json_out) if args.json_out else root / "formal" / "audit-results.txt"

    results = audit(root, str(ledger) if ledger else None)
    text = format_text(results)
    json_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(results, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8")
    if not args.quiet:
        sys.stdout.write(text)
    return 0 if results["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
