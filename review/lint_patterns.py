#!/usr/bin/env python3
"""Mechanical lint for the theme-porting knowledge base (patterns/KB-01..KB-81).

Ownership / provenance
----------------------
This tool turns the *Static detection* sections of the patterns knowledge base
into executable rules. It is stdlib-only and lives beside classify_hunks.py
and build_review.py, in the same style (plain functions, no third-party deps).

It deliberately does NOT re-implement checks that classify_hunks.py or
build_review.py already perform (those patterns are dispositioned
ALREADY-AUTOMATED in LINT-WAVE.md, naming the detector). It also does not
invent rules: every rule below is derived from the pattern's own Static
detection text, and the source section is quoted in the rule's registration.

Two scopes
----------
* ``candidate`` rules run on candidate.txt alone (a pure grep or a file-local
  structural check). Their registration says ``scope=candidate:.``
* ``pair`` rules run on original.txt + candidate.txt (a cross-file diff or a
  count that must be compared side by side). Their registration says
  ``scope=pair.``
* ``disposition`` rules (still scope=candidate:) do not report a defect: they
  fire an INFO/EXCEPTION record that settles a cross-cutting or named-exception
  pattern from the candidate bytes (KB-32, KB-50, KB-55, KB-56, KB-59, KB-80).

NEGATIVE-LEDGER suppressions
----------------------------
False-positive contexts recorded in patterns/NEGATIVE-LEDGER.md are named
suppressions below (SUPPRESSIONS registry); the model example is NL-07's XML
namespace identifier case, implemented in _scrub() and lint_http_scheme().
Every fired finding names the suppressions that were applied.

Usage
-----
  python3 review/lint_patterns.py --list
  python3 review/lint_patterns.py <package_dir> [<package_dir> ...]
  python3 review/lint_patterns.py --corpus [review_dir]
  python3 review/lint_patterns.py --corpus --rule KB-42 [--json]
  python3 review/lint_patterns.py --corpus --strict     # exit 1 if any finding

Exit status is 0 for a completed reporting run (findings are data, not a tool
failure); --strict makes findings exit 1. A rule that cannot complete on a
package is reported as an ERROR finding, never silently skipped.
"""

import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Suppression registry (NEGATIVE-LEDGER false-positive contexts)
# ---------------------------------------------------------------------------
SUPPRESSIONS = {
    "NL-07:xmlns-identifier": (
        "http://www.w3.org/... etc. are XML namespace identifiers, not fetched "
        "URLs; excluded from KB-42 by _scrub(NL07_HTTP_HOSTS)."
    ),
    "NL-15:css-source-comment": (
        "http:// inside a CSS source-citation comment (andesite L677 model) is "
        "neither a fetched URL nor a link; excluded by CSS-comment scrubbing."
    ),
    "NL-01/02:two-channel": (
        "single-channel audits fabricated two retracted inconsistency sets; "
        "every structural rule parses BOTH [[module CSS]] and [[code]] CSS."
    ),
    "NL-11:font-host-repoint": (
        "well-formed font host repoints (bunny -> Google) and import-only "
        "families are NOT malformed-font or dropped-font findings."
    ),
    "KB-07:mutually-exclusive-gate": (
        "repeated priority across mutually exclusive parameter-gated loads "
        "cannot co-fire and is not a collision."
    ),
    "KB-07:original-identical-stack": (
        "a priority stack identical to the original's is the original's design "
        "(dia-de-muertos 1/2/4), not a port-introduced violation."
    ),
    "KB-42:inherited-http": (
        "http URL byte-identical to the original is a class (ii) posting "
        "scheme rewrite, not a candidate-inherent defect."
    ),
    "KB-55:candela-granular": (
        "candela's granular fragment:parallel imports are a named exception; "
        "never nominated under cross-theme-import rules."
    ),
    "KB-56:peroxide-escaped": (
        ":oxygennine:peroxide:* inside @@...@@ is inert documentation; the "
        "component family ports with the theme at posting. The corpus's "
        "peroxide exhibits use the equivalent Wikidot {{...}} inline-code form; "
        "_scrub() masks both (observed-vs-recipe form discrepancy, see report)."
    ),
    "KB-70:inherited-self-import": (
        "a self-import identical to the original's with zero code blocks on "
        "both sides is the inherited sub-shape (A) (FIX-CODEADDR), not a port hit."
    ),
    "KB-20:own-css-size": (
        "a large candidate within 1.2x of its original is large because the "
        "original is large; the mechanism is inlined base, not size alone."
    ),
    "KB-73:param-gated-channel": (
        "a conditional-comment module serving a different delivery path is not "
        "a duplicate-import or a dropped gate (xmas shape)."
    ),
}

# Hosts that are namespace identifiers, not resources (NL-07, model suppression).
NL07_HTTP_HOSTS = (
    "www.w3.org", "purl.org", "schemas.xmlsoap.org", "xmlsoap.org",
    "www.w3.org/1999", "www.w3.org/2000", "www.w3.org/TR",
)

# Environment-layer hosts (KB-40) subtracted from any candidate-own host set.
ENV_HOSTS = {
    "rokurolize.github.io", "rsms.me", "scp-wiki.wdfiles.com",
    "indestructibletype-fonthosting.github.io",
}

# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

def read_lines(path):
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return ["<<READ ERROR: %s>>" % exc]


def _scrub(lines):
    """Return (scrubbed_text, escaped_positions).

    Scrubbed text keeps line structure and byte offsets but replaces every
    character inside an @@...@@ escape (NL-01/02 awareness) and every character
    inside a CSS /*...*/ comment with a space. Regexes run on scrubbed text
    cannot fire inside a false-positive context; evidence is taken from the
    original line. This is the mechanical form of the NL-07 / NL-15 rules.
    """
    text = "\n".join(lines)
    out = list(text)
    escaped = bytearray(len(text))

    # @@...@@ escapes (documentation examples) -> space, mark escaped.
    i = 0
    while True:
        a = text.find("@@", i)
        if a < 0:
            break
        b = text.find("@@", a + 2)
        if b < 0:
            b = len(text)
        for k in range(a, min(b + 2, len(text))):
            out[k] = " "
            escaped[k] = 1
        i = b + 2

    # Wikidot inline-code escapes {{...}} that contain wiki markup. The KB
    # recipe says @@...@@, but the corpus's peroxide documentation exhibits use
    # {{[[include ...]]}}; both are inert porter-visible examples. Only mask
    # spans that actually contain wikitext, so CSS braces are never touched.
    i = 0
    while True:
        a = text.find("{{", i)
        if a < 0:
            break
        b = text.find("}}", a + 2)
        if b < 0:
            break
        inner = text[a + 2:b]
        if "[[" in inner or "@@" in inner or "http://" in inner:
            for k in range(a, b + 2):
                if out[k] != "\n":
                    out[k] = " "
                    escaped[k] = 1
        i = b + 2

    # CSS /*...*/ comments -> space (keep newlines for line numbering).
    # Scan the ALREADY-MASKED text so a comment marker inside an @@ or {{}}
    # example is never treated as live, and skip the '/*' that occurs in the
    # wikitext bold separator '**word**/**word**' (madoka line 256 model).
    # An unclosed comment is left visible: KB-71, not the scrubber, judges it.
    cur = "".join(out)
    j = 0
    while True:
        a = cur.find("/*", j)
        if a < 0:
            break
        # Skip wiki-formatting '/*' tokens: '**word**/**word**' (preceded by
        # '*') and '__**//--{{x}}--//**__' (followed by '*', from '//**').
        if (a > 0 and cur[a - 1] == "*") or cur[a + 2:a + 3] == "*":
            j = a + 2
            continue
        b = cur.find("*/", a + 2)
        if b < 0:
            break
        for k in range(a, b + 2):
            if cur[k] != "\n":
                out[k] = " "
        j = b + 2

    return "".join(out), escaped


def split_scrubbed(scrubbed, lines):
    """Yield (line_index, original_line, scrubbed_line) in lockstep."""
    parts = scrubbed.split("\n")
    for i, line in enumerate(lines):
        s = parts[i] if i < len(parts) else ""
        yield i, line, s


def css_channels(lines):
    """Return list of {kind,start,end} for both CSS channels (NL-01/02).

    'module-css' is a [[module CSS]] ... [[/module]] span; 'code-css' is a
    [[code type=\"css\"]] ... [[/code]] span. A [[code]] block without a css
    type is still returned as 'code-other' so code-block ordinals (KB-70) and
    documentation-exhibit checks (KB-79) can see it.
    """
    channels = []
    stack = []  # (kind, start)
    module_re = re.compile(r"\[\[module\s+CSS\s*\]\]", re.I)
    code_re = re.compile(r"\[\[code([^\]]*)\]\]")
    code_close = "[[/code]]"
    module_close = "[[/module]]"
    # Detect markers on scrubbed text: an escaped @@[[code]]@@ documentation
    # example is not a channel and must not steal the next [[/code]] closer.
    # Indices stay aligned with the original lines.
    lines = _scrub(lines)[0].split("\n")
    for i, line in enumerate(lines):
        for m in module_re.finditer(line):
            stack.append(("module-css", i))
        for m in code_re.finditer(line):
            typ = "css" if re.search(r"type\s*=\s*['\"]?css", m.group(1), re.I) else "other"
            stack.append(("code-" + typ, i))
        if module_close in line:
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][0] == "module-css":
                    kind, start = stack.pop(k)
                    channels.append({"kind": kind, "start": start, "end": i})
                    break
        if code_close in line:
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][0].startswith("code-"):
                    kind, start = stack.pop(k)
                    channels.append({"kind": kind, "start": start, "end": i})
                    break
    for kind, start in stack:  # unclosed at EOF: still a channel to EOF
        channels.append({"kind": kind, "start": start, "end": len(lines) - 1})
    channels.sort(key=lambda c: c["start"])
    return channels


def parse_includes(lines):
    """Return include blocks: {name,start,end,params:[(line,key,value)]}."""
    blocks = []
    i = 0
    open_re = re.compile(r"\[\[include\s+([^\]\n|]+)")
    param_re = re.compile(r"^\s*\|\s*([^=]+?)\s*=\s*(.*?)\s*$")
    while i < len(lines):
        m = open_re.search(lines[i])
        if not m:
            i += 1
            continue
        name = m.group(1).strip()
        start = i
        j = i
        joined = lines[i]
        while "]]" not in joined and j + 1 < len(lines):
            j += 1
            joined += "\n" + lines[j]
        params = []
        for k in range(i, j + 1):
            pm = param_re.match(lines[k])
            if pm:
                params.append((k, pm.group(1).strip(), pm.group(2).strip()))
            else:
                # inline params on the same line as [[include name ...|k=v]]
                if k == i:
                    tail = lines[i][m.end():]
                    for part in tail.split("|"):
                        im = re.match(r"\s*([^=]+?)\s*=\s*(.*?)\s*$", part)
                        if im and "] ]" not in part and "]]" not in part:
                            params.append((i, im.group(1).strip(),
                                           im.group(2).strip().rstrip("] ")))
        blocks.append({"name": name, "start": start, "end": j, "params": params})
        i = j + 1
    return blocks


def own_slug(package, lines):
    """candidate fullname from classification.json, else package dir name."""
    cj = package / "classification.json"
    try:
        data = json.loads(cj.read_text(encoding="utf-8"))
        return data["theme"]["cand_fullname"]
    except Exception:
        return package.name


def find_package_files(package):
    orig = next(iter(sorted(package.glob("original.*"))), None)
    if orig is None:
        return None, None
    cand = package / ("candidate" + orig.suffix)
    return (orig, cand) if cand.is_file() else (None, None)


def delivered_code_ordinals(ctx):
    """Ordinals of the page's OWN [[code]] blocks that are actually delivered
    (named by a self-addressed local--code/<own>/N, e.g. the interwiki-style
    theme= frame or an @import). Documentation exhibits are not delivered.
    """
    own = ctx["fullname"].replace(":", "%3A")
    ords = set()
    for _i, _line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        for m in re.finditer(r"local--code/([^\s/\)'\"]+?)/(\d+)", s):
            if m.group(1) in (own, ctx["fullname"]):
                ords.add(int(m.group(2)))
    return ords


# ---------------------------------------------------------------------------
# Finding container
# ---------------------------------------------------------------------------

class Finding:
    __slots__ = ("package", "kb", "rule", "scope", "location", "evidence", "note")

    def __init__(self, package, kb, rule, scope, location, evidence, note=""):
        self.package = package
        self.kb = kb
        self.rule = rule
        self.scope = scope
        self.location = location
        self.evidence = evidence.strip()[:300]
        self.note = note

    def as_dict(self):
        return {"package": self.package, "kb": self.kb, "rule": self.rule,
                "scope": self.scope, "location": self.location,
                "evidence": self.evidence, "note": self.note}

    def __str__(self):
        return "\t".join([self.package, self.kb, self.rule, self.scope,
                          self.location, self.evidence,
                          self.note]).rstrip("\t")


# ---------------------------------------------------------------------------
# Rule implementations. Each detector yields Finding objects.
# ctx = {package, lines, scrubbed, channels, includes, orig_lines, fullname}
# ---------------------------------------------------------------------------

def lint_malformed_url(ctx):
    """KB-03: url(null), url(), url(https://…), unbalanced url( per declaration.

    Static detection: 'grep for url(null), url(), url(https://…), and url(
    occurrences whose line lacks a closing ) before the ;. Count url( vs )
    balance per declaration block.' Escapes/comments are not live; only a CSS
    declaration counts (prose that says 'CSSのurl()形式' is not a resource).
    """
    css_lines = set()
    for ch in css_channels(ctx["lines"]):
        for k in range(ch["start"], ch["end"] + 1):
            css_lines.add(k)
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if i not in css_lines or "[[" in line:
            continue  # a wikitext inline-code example is not a CSS declaration
        low = s.lower()
        if re.search(r"url\(\s*(null|none)\s*\)", low) or re.search(r"url\(\s*\)", low):
            yield Finding(ctx["package"], "KB-03", "lint_malformed_url", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          "empty/null resource; escapes+comments scrubbed")
        elif re.search(r"url\(\s*https://[^)]*\.\.\.\s*\)", s):
            yield Finding(ctx["package"], "KB-03", "lint_malformed_url", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          "elided placeholder (marchen ORIGINAL-DEFECT under KB-02)")
        # balance: each url( must close with a ')' on the same line. Scan from
        # each match end instead of splitting on ';' (a URL may contain ';',
        # e.g. Google Fonts css2 ?wght@400;700, which is not a declaration end).
        for m in re.finditer(r"url\(", low):
            if ")" not in low[m.end():]:
                yield Finding(ctx["package"], "KB-03", "lint_malformed_url", "candidate:",
                              "candidate.txt:%d" % (i + 1), line,
                              "unterminated url( in declaration")
                break


def lint_interwiki_style(ctx):
    """KB-07: duplicate priority / missing priority / (zero include) on the
    interwiki-style include family. Static detection: 'count of includes, each
    priority= value, each theme= argument. Charge: zero includes; any duplicate
    priority value ...; any include without priority=; BHL-family themes whose
    split is not 1/2/3.' Suppressions: mutually-exclusive gates, original-identical
    stacks (both from the pattern's own False-positive section).
    """
    incs = [b for b in ctx["includes"] if "interwiki-style" in b["name"].lower()]
    if not incs:
        # Only nominate when the original had a frame (the port dropped it).
        o = "".join(ctx["orig_lines"])
        if "interwiki-style" in o:
            yield Finding(ctx["package"], "KB-07", "lint_interwiki_style", "pair",
                          "candidate.txt:0", "<<no interwiki-style include>>",
                          "original has frame, candidate has none")
        return
    seen = {}
    suppressed = []
    for b in incs:
        prios = [(ln, k, v) for ln, k, v in b["params"] if k == "priority"]
        if not prios:
            yield Finding(ctx["package"], "KB-07", "lint_interwiki_style", "candidate:",
                          "candidate.txt:%d" % (b["start"] + 1),
                          ctx["lines"][b["start"]], "include without priority= (KB-06 default)")
            continue
        for _pl, _pk, v in prios:
            v = v.strip()
            if v in seen:
                # mutually-exclusive parameter gate around either load?
                if _gate_exclusive(ctx["lines"], seen[v], b["start"]):
                    suppressed.append("KB-07:mutually-exclusive-gate")
                    continue
                # original-identical full stack?
                if _original_identical_stack(ctx, incs):
                    suppressed.append("KB-07:original-identical-stack")
                    continue
                yield Finding(ctx["package"], "KB-07", "lint_interwiki_style", "candidate:",
                              "candidate.txt:%d" % (b["start"] + 1),
                              ctx["lines"][b["start"]],
                              "duplicate priority=%s" % v)
            else:
                seen[v] = b["start"]


def _gate_exclusive(lines, a, b):
    """True if two loads sit in distinct [!-- {$p} --] conditional gates."""
    def gate_before(idx):
        for k in range(idx, max(-1, idx - 12), -1):
            if re.search(r"\[!--\s*\{\$", lines[k]):
                return lines[k].strip()
        return None
    ga, gb = gate_before(a), gate_before(b)
    return bool(ga and gb and ga != gb)


def _original_identical_stack(ctx, incs):
    oincs = [b for b in parse_includes(ctx["orig_lines"]) if "interwiki-style" in b["name"].lower()]
    def stack(bs):
        return sorted([v for b in bs for ln, k, v in b["params"] if k == "priority"])
    return bool(oincs) and stack(incs) == stack(oincs)


def lint_modalbox_pin(ctx):
    """KB-13: global .modalbox fixed centering with no .credit-static-view carve-out."""
    text = "\n".join(ctx["lines"])
    has_carveout = bool(re.search(r"\.credit-static-view\s+\.modalbox", text))
    for ch in css_channels(ctx["lines"]):
        if ch["kind"] not in ("module-css", "code-css"):
            continue
        block_lines = ctx["lines"][ch["start"]:ch["end"] + 1]
        block = "\n".join(block_lines)
        # A GLOBAL .modalbox rule: the selector is exactly .modalbox at the
        # start of a line (optionally indented), not '#x .modalbox' (scoped).
        for m in re.finditer(r"(?m)^[ \t]*\.modalbox\s*\{([\s\S]*?)\}", block):
            body = m.group(1)
            if not re.search(r"position\s*:\s*fixed", body):
                continue
            if not (re.search(r"left\s*:\s*50%", body) or re.search(r"top\s*:\s*50%", body)
                    or re.search(r"translate\(-50%\s*,\s*-50%\)", body)):
                continue
            line_no = ch["start"] + 1 + block[:m.start()].count("\n")
            yield Finding(ctx["package"], "KB-13", "lint_modalbox_pin", "candidate:",
                          "candidate.txt:%d" % line_no,
                          block_lines[block[:m.start()].count("\n")],
                          "carve-out present -> fixed form, not a finding" if has_carveout
                          else "no .credit-static-view .modalbox carve-out")


def lint_oversize(ctx):
    """KB-20: char-count near 200,000 caused by INLINED BASE material.

    The pattern's own False-positive section: 'A large candidate whose size is
    its own CSS (not inlined base) is not this pattern; the mechanism is the
    inlining, not the size alone.' A candidate within 1.2x of its original's
    size is large because the original is large, not because base was inlined.
    """
    n = len("\n".join(ctx["lines"]))
    if n < 180000:
        return
    ratio = 0.0
    if ctx["orig_lines"]:
        o = len("\n".join(ctx["orig_lines"]))
        ratio = n / max(o, 1)
        if ratio < 1.2:
            return  # own-CSS size, not inlined base (KB-20 false positive)
    yield Finding(ctx["package"], "KB-20", "lint_oversize", "candidate:",
                  "candidate.txt:1-<EOF>", "candidate_chars=%d ratio=%.2f" % (n, ratio),
                  "approaching 200000 save limit with size growth consistent with inlined base")


def lint_fragile_param(ctx):
    """KB-21: include parameter '= ' (space before value) and http:// inside
    include params / [[image]] sources.
    """
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if "[[include" not in s and "[[image" not in s:
            continue
        # The signature is the fragile FORM: '=' followed by a space before an
        # http:// value, or an http:// scheme (not https) inside [[image ...]].
        # A plain https draft-host [[image ...]] is a normal draft-bucket asset
        # reference (KB-58), not this pattern.
        if re.search(r"=\s+http://", s) or re.search(r"\[\[image\s+http://", s):
            yield Finding(ctx["package"], "KB-21", "lint_fragile_param", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          "space and/or http scheme inside asset parameter")


def lint_preview_credit(ctx):
    """KB-32: file-first disposition. If credit:start-preview/end-preview is
    present, every credit-modal line for the page is preview-form.
    """
    text = "\n".join(ctx["lines"])
    if re.search(r"credit:(start|end)-preview", text):
        yield Finding(ctx["package"], "KB-32", "lint_preview_credit", "candidate:",
                      "candidate.txt:<credit-block>", "credit:start-preview present",
                      "DISPOSITION: credit-modal lines are preview-form; never a theme defect")


def lint_http_scheme(ctx):
    """KB-42: http:// in live references. NL-07 namespace identifiers and
    NL-15 CSS source-citation comments are scrubbed; byte-identical-to-original
    http lines are flagged as inherited (class (ii)), not candidate-inherent.
    """
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        for m in re.finditer(r"http://([^\s\"'\)\|>\]]+)", s):
            host = m.group(1).split("/")[0]
            if any(h in m.group(1) for h in NL07_HTTP_HOSTS):
                continue  # NL-07: namespace identifier, not a fetched URL
            inherited = bool(ctx["orig_lines"]) and i < len(ctx["orig_lines"]) and line.strip() == ctx["orig_lines"][i].strip()
            yield Finding(ctx["package"], "KB-42", "lint_http_scheme", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          ("class (ii) scheme-rewrite; " if inherited else "class (ii) scheme-rewrite; ") +
                          "suppressed NL-07 xmlns + NL-15 css-comment")


def lint_hidden_rate(ctx):
    """KB-50 shape (a): no bare [[module Rate]] and no real credit module ->
    hidden-rate is correct machine behaviour (preview module is NOT rate-bearing).
    """
    text = "\n".join(ctx["lines"])
    if not re.search(r"\[\[module\s+rate\]\]", text, re.I) and not re.search(r"credit:(start|end)\b(?!-preview)", text):
        yield Finding(ctx["package"], "KB-50", "lint_hidden_rate_shape_a", "candidate:",
                      "candidate.txt:<rate-furniture>", "no Rate and no real credit module",
                      "DISPOSITION: hidden-rate is correct machine behaviour (shape a)")


def lint_candela_parallel(ctx):
    """KB-55: candela's granular fragment:parallel imports -> named exception,
    never nominated under cross-theme-import rules.
    """
    if ctx["package"] != "candela-jp":
        return
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if "fragment:parallel" in s or "parallel/" in s:
            yield Finding(ctx["package"], "KB-55", "lint_candela_parallel", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          "EXCEPTION: granular CN parallel import (suppresses KB-14/KB-15)")


def lint_peroxide_escaped(ctx):
    """KB-56: :oxygennine:peroxide:* escaped = exception; live = KB-15 route."""
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if "oxygennine:peroxide" in line:
            escaped = "oxygennine:peroxide" not in s
            if escaped:
                yield Finding(ctx["package"], "KB-56", "lint_peroxide_escaped", "candidate:",
                              "candidate.txt:%d" % (i + 1), line,
                              "EXCEPTION: escaped documentation (NL-anchor suppress)")
            else:
                yield Finding(ctx["package"], "KB-56", "lint_peroxide_escaped", "candidate:",
                              "candidate.txt:%d" % (i + 1), line,
                              "LIVE peroxide include -> route to KB-15, not this exception")


def lint_escaped_footnoteblock(ctx):
    """KB-59: exact escaped @@[[footnoteblock]]@@ exhibit -> staff-call disposition."""
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if "@@[[footnoteblock]]@@" in line:
            yield Finding(ctx["package"], "KB-59", "lint_escaped_footnoteblock", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          "DISPOSITION: staff-call exhibit (rows 1/3/4), not a lane fix")


def lint_codeaddr(ctx):
    """KB-70: self-addressed local--code/<own>/N vs [[code]] block ordinals.

    Static detection: 'count [[code]] blocks ... identify which one holds the
    delivered CSS. For every self-addressed local--code/<own>/N reference,
    compare N ... Flag (a) N naming a non-CSS/exhibit block, (b) any self-address
    on a page with zero [[code]] blocks or live-module-only delivery, and (c) a
    frame target naming a different page name than the candidate's own.'
    """
    fullname = ctx["fullname"]
    slug_encoded = fullname.replace(":", "%3A")
    slug_plain = fullname
    code_chans = [c for c in css_channels(ctx["lines"]) if c["kind"].startswith("code-")]
    # A delivered code block need not carry type="css" (sci-fi-jp's /1 is a
    # plain [[code]] that holds the stylesheet); judge by CSS markers.
    def looks_css(c):
        body = "\n".join(ctx["lines"][c["start"]:c["end"] + 1])
        return bool(re.search(r"(:root\s*\{|@import\b|font-family\s*:|[ #.][\w-]+\s*\{)", body))
    chans = [c for c in code_chans if looks_css(c)]
    self_refs = []
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        for m in re.finditer(r"local--code/([^\s/\)'\"]+?)/(?:(\d+))?", s):
            seg = m.group(1)
            if seg in (slug_encoded, slug_plain, fullname.replace(":", "%3A")):
                self_refs.append((i, m.group(2)))
    if not self_refs:
        return
    if not code_chans:
        # KB-70 false-positive line: a self-import identical to the original's
        # (sub-shape (A), FIX-CODEADDR) is the inherited form, not a port hit.
        otext = "\n".join(ctx["orig_lines"])
        orig_own = bool(otext) and ("local--code/" in otext) and not any(
            re.search(r"\[\[code[^\]]*\]\]", l) for l in ctx["orig_lines"])
        for i, n in self_refs:
            if orig_own:
                continue  # inherited self-import (the-foundation-sigma disposition)
            yield Finding(ctx["package"], "KB-70", "lint_codeaddr", "candidate:",
                          "candidate.txt:%d" % (i + 1), ctx["lines"][i],
                          "(b) self-address on page with zero [[code]] blocks (live-module-only)")
        return
    css_ordinals = [code_chans.index(c) + 1 for c in chans]
    for i, n in self_refs:
        if n is None:
            continue
        n = int(n)
        if n > len(code_chans):
            yield Finding(ctx["package"], "KB-70", "lint_codeaddr", "candidate:",
                          "candidate.txt:%d" % (i + 1), ctx["lines"][i],
                          "(a) self-address /%d beyond %d code blocks" % (n, len(code_chans)))
        elif n not in css_ordinals:
            yield Finding(ctx["package"], "KB-70", "lint_codeaddr", "candidate:",
                          "candidate.txt:%d" % (i + 1), ctx["lines"][i],
                          "(a) self-address /%d names non-CSS/exhibit block (CSS=%s)" %
                          (n, css_ordinals))


def lint_block_structure(ctx):
    """KB-71: delivered CSS block that voids its own rules (unterminated banner
    comment; brace depth ending above 0). Both channels, tolerant parsing.
    """
    delivered = delivered_code_ordinals(ctx)
    all_code = [c for c in css_channels(ctx["lines"]) if c["kind"].startswith("code-")]
    for ch in css_channels(ctx["lines"]):
        if ch["kind"] == "module-css":
            pass  # inline module CSS is always delivered
        elif ch["kind"].startswith("code-"):
            if (all_code.index(ch) + 1) not in delivered:
                continue  # documentation exhibit, not the delivered block
        else:
            continue
        block = ctx["lines"][ch["start"]:ch["end"] + 1]
        depth = 0
        end_depth = 0
        longest = 0
        run = 0
        in_comment = False
        first_rule_seen = False
        first_comment_before_rule = None  # (line_idx, closed_before_rule)
        for k, line in enumerate(block):
            pos = 0
            while pos < len(line):
                if in_comment:
                    c = line.find("*/", pos)
                    if c < 0:
                        break
                    in_comment = False
                    if first_comment_before_rule is not None and not first_comment_before_rule[1]:
                        first_comment_before_rule = (first_comment_before_rule[0], True)
                    pos = c + 2
                    continue
                o = line.find("/*", pos)
                b = line.find("{", pos)
                imp = re.search(r"@import\b", line[pos:])
                imp_pos = pos + imp.start() if imp else None
                nxt = [x for x in (o, b, imp_pos) if x is not None and x >= 0]
                if not nxt:
                    break
                n = min(nxt)
                if n == o:
                    if not first_rule_seen and first_comment_before_rule is None:
                        first_comment_before_rule = (k, False)
                    in_comment = True
                    pos = o + 2
                    continue
                if n in (b, imp_pos):
                    first_rule_seen = True
                    if first_comment_before_rule is not None and not first_comment_before_rule[1]:
                        yield Finding(ctx["package"], "KB-71", "lint_block_structure", "candidate:",
                                      "candidate.txt:%d" % (ch["start"] + k + 1), line,
                                      "banner comment not closed before first rule/@import")
                        first_comment_before_rule = (first_comment_before_rule[0], True)
                    break
            # brace depth from non-comment characters (approximate: count all)
            depth += line.count("{") - line.count("}")
            if depth >= 1:
                run += 1
                longest = max(longest, run)
            else:
                run = 0
            end_depth = depth
        if in_comment:
            yield Finding(ctx["package"], "KB-71", "lint_block_structure", "candidate:",
                          "candidate.txt:%d" % (ch["start"] + 1), "<<unclosed /* comment>>",
                          "comment open at end of delivered block")
        if end_depth > 0:
            yield Finding(ctx["package"], "KB-71", "lint_block_structure", "candidate:",
                          "candidate.txt:%d-%d" % (ch["start"] + 1, ch["end"] + 1),
                          "brace_depth_end=%d longest_positive=%d" % (end_depth, longest),
                          "block ends above depth 0")


def lint_doc_default(ctx):
    """KB-72: documented default contradicts the shipped :root variable / loaded font."""
    text = "\n".join(ctx["lines"])
    vars_text = "\n".join(re.findall(r"(?m)^[^\n]*:root[^\n]*\{[\s\S]*?\}", text))
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        # Require a documentation statement: keyword followed by a colon, or
        # the '本文フォントはX' prose form. CSS selector lines (.btn-default)
        # and code lines are not documentation statements.
        m = re.search(r"(?m)^(?!.*[{};])\s*(?:\*\*)?(?:デフォルト値|デフォルト|default|本文フォントは)\s*[:：]\s*[「\"']?([^\s」\"'、。]+)", s)
        if not m:
            m = re.search(r"本文フォントは\s*([^\s、。]+)", s)
        if not m:
            continue
        named = m.group(1)
        if named and named not in vars_text and named not in text.replace(line, ""):
            yield Finding(ctx["package"], "KB-72", "lint_doc_default", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          "documented value %r not found in :root/loads" % named)


def lint_param_gate(ctx):
    """KB-73: original parameter gate/slot dropped or emptied in candidate."""
    if not ctx["orig_lines"]:
        return
    otext = "\n".join(ctx["orig_lines"])
    ctext = "\n".join(ctx["lines"])
    ogates = set(re.findall(r"\{\$[a-z-]+\}", otext))
    cgates = set(re.findall(r"\{\$[a-z-]+\}", ctext))
    for g in sorted(ogates - cgates):
        yield Finding(ctx["package"], "KB-73", "lint_param_gate", "pair",
                      "original.txt:<gates> -> candidate.txt:<gates>", g,
                      "original gate token absent from candidate (a)")
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if re.search(r"\[!--\s*\{\$", s):
            window = "\n".join(ctx["lines"][i:i + 6])
            if "[[" not in window or "module CSS" not in window:
                yield Finding(ctx["package"], "KB-73", "lint_param_gate", "candidate:",
                              "candidate.txt:%d" % (i + 1), line,
                              "slot marker with no module (b) - verify variant paths first")


def lint_dup_tail_block(ctx):
    """KB-76: exact-duplicate short [[div]] block at the candidate tail where
    the original carried one. Pair check on tail windows.
    """
    if not ctx["orig_lines"]:
        return
    def tail_blocks(lines, n=60):
        window = lines[-n:]
        opens = [l.strip() for l in window if re.match(r"\s*\[\[div\b", l)]
        return opens
    c = tail_blocks(ctx["lines"])
    o = tail_blocks(ctx["orig_lines"])
    for sig in set(c):
        if c.count(sig) > max(o.count(sig), 1):
            yield Finding(ctx["package"], "KB-76", "lint_dup_tail_block", "pair",
                          "candidate.txt:<tail>", sig[:200],
                          "candidate tail count %d > original %d" %
                          (c.count(sig), o.count(sig)))


def lint_empty_collapsible(ctx):
    """KB-78: [[collapsible]] open immediately followed by its close (empty)."""
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if re.match(r"\s*\[\[collapsible\b", s):
            j = i + 1
            while j < len(ctx["lines"]) and not ctx["lines"][j].strip():
                j += 1
            if j < len(ctx["lines"]) and re.match(r"\s*\[\[/collapsible\]\]", ctx["lines"][j]):
                oempty = False
                if ctx["orig_lines"]:
                    otext = "\n".join(ctx["orig_lines"])
                    oempty = bool(re.search(r"\[\[collapsible\]\]\s*\[\[/collapsible\]\]", otext))
                yield Finding(ctx["package"], "KB-78", "lint_empty_collapsible", "pair",
                              "candidate.txt:%d-%d" % (i + 1, j + 1), line + " / " + ctx["lines"][j],
                              "original also empty -> not a port hit" if oempty else "empty collapsible")


def lint_exhibit_leak(ctx):
    """KB-79: exhibit-shaped :root block at delivered block tail + depth > 0.
    Narrow mechanical form of the pattern's three-condition test.
    """
    delivered = delivered_code_ordinals(ctx)
    all_code = [c for c in css_channels(ctx["lines"]) if c["kind"].startswith("code-")]
    for ch in css_channels(ctx["lines"]):
        if not ch["kind"].startswith("code-"):
            continue
        if (all_code.index(ch) + 1) not in delivered:
            continue  # documentation exhibit, not the delivered block
        block = ctx["lines"][ch["start"]:ch["end"] + 1]
        depth = sum(l.count("{") - l.count("}") for l in block)
        tail = "\n".join(block[-30:])
        if depth > 0 and re.search(r"^\s*:root\s*\{", tail, re.M):
            yield Finding(ctx["package"], "KB-79", "lint_exhibit_leak", "pair",
                          "candidate.txt:%d-%d" % (ch["start"] + 1, ch["end"] + 1),
                          "depth_end=%d; :root at tail" % depth,
                          "confirm tail :root is a doc exhibit in the original")


def lint_footnoteblock_added(ctx):
    """KB-80: candidate live [[footnoteblock]] where original had inline
    [[footnote]] elements and no block -> benign supplement (not a defect).
    """
    if not ctx["orig_lines"]:
        return
    otext = "\n".join(ctx["orig_lines"])
    ctext = "\n".join(ctx["lines"])
    if re.search(r"\[\[footnote\]\]", otext) and not re.search(r"\[\[footnoteblock\]\]", otext):
        for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
            if "[[footnoteblock]]" in s:
                yield Finding(ctx["package"], "KB-80", "lint_footnoteblock_added", "pair",
                              "candidate.txt:%d" % (i + 1), line,
                              "DISPOSITION: benign footnote-visibility supplement")


# ---------------------------------------------------------------------------
# Rule registry
# ---------------------------------------------------------------------------
# (kb, rule_name, scope, detector, source-section-short, suppressions)
RULES = [
    ("KB-03", "lint_malformed_url", "candidate:", lint_malformed_url,
     "Static detection: url(null)/url()/url(https://…)/unbalanced url( per declaration", []),
    ("KB-07", "lint_interwiki_style", "candidate:/pair", lint_interwiki_style,
     "Static detection: count interwiki-style includes, priorities, theme= args",
     ["KB-07:mutually-exclusive-gate", "KB-07:original-identical-stack"]),
    ("KB-13", "lint_modalbox_pin", "candidate:", lint_modalbox_pin,
     "Static detection: global .modalbox position:fixed + no .credit-static-view carve-out", []),
    ("KB-20", "lint_oversize", "candidate:", lint_oversize,
     "Static detection: character-count every candidate against 200000",
     ["KB-20:own-css-size"]),
    ("KB-21", "lint_fragile_param", "candidate:", lint_fragile_param,
     "Static detection: include param '= ' and http:// inside include/image params", []),
    ("KB-32", "lint_preview_credit", "candidate:", lint_preview_credit,
     "Static detection (file-first disposition): credit:start-preview -> credit-modal is preview-form", []),
    ("KB-42", "lint_http_scheme", "candidate:", lint_http_scheme,
     "Static detection: grep http:// in live references; class (ii) on sight",
     ["NL-07:xmlns-identifier", "NL-15:css-source-comment", "KB-42:inherited-http"]),
    ("KB-50", "lint_hidden_rate_shape_a", "candidate:", lint_hidden_rate,
     "Static detection (shape a): no Rate and no real credit module settles hidden-rate",
     []),
    ("KB-55", "lint_candela_parallel", "candidate:", lint_candela_parallel,
     "Static detection: detect candela granular fragment:parallel imports",
     ["KB-55:candela-granular"]),
    ("KB-56", "lint_peroxide_escaped", "candidate:", lint_peroxide_escaped,
     "Static detection: :oxygennine:peroxide hits, verify @@ escaping context",
     ["KB-56:peroxide-escaped"]),
    ("KB-59", "lint_escaped_footnoteblock", "candidate:", lint_escaped_footnoteblock,
     "Static detection: detect exact @@[[footnoteblock]]@@ exhibit form", []),
    ("KB-70", "lint_codeaddr", "candidate:/pair", lint_codeaddr,
     "Static detection: self-addressed local--code/<own>/N vs [[code]] ordinals",
     ["KB-70:inherited-self-import"]),
    ("KB-71", "lint_block_structure", "candidate:", lint_block_structure,
     "Static detection: comment termination + brace-depth profile per delivered block",
     ["NL-01/02:two-channel"]),
    ("KB-72", "lint_doc_default", "candidate:", lint_doc_default,
     "Static detection: documented default vs :root vars / loaded font set", []),
    ("KB-73", "lint_param_gate", "pair", lint_param_gate,
     "Static detection: original gate/slot dropped, emptied, or undocumented",
     ["KB-73:param-gated-channel"]),
    ("KB-76", "lint_dup_tail_block", "pair", lint_dup_tail_block,
     "Static detection: duplicate short [[div]] block at candidate tail > original", []),
    ("KB-78", "lint_empty_collapsible", "pair", lint_empty_collapsible,
     "Static detection: [[collapsible]] open immediately followed by close", []),
    ("KB-79", "lint_exhibit_leak", "pair", lint_exhibit_leak,
     "Static detection: body headings with no exhibit + :root at delivered tail + depth>0", []),
    ("KB-80", "lint_footnoteblock_added", "pair", lint_footnoteblock_added,
     "Static detection: inline footnotes in original + live block in candidate", []),
]


def build_ctx(package):
    orig, cand = find_package_files(package)
    if cand is None:
        return None
    lines = read_lines(cand)
    scrubbed, _ = _scrub(lines)
    return {
        "package": package.name,
        "lines": lines,
        "orig_lines": read_lines(orig) if orig and orig.is_file() else [],
        "scrubbed": scrubbed,
        "channels": css_channels(lines),
        "includes": parse_includes(lines),
        "fullname": own_slug(package, lines),
    }


def lint_package(package, rule_filter=None):
    ctx = build_ctx(package)
    if ctx is None:
        return []
    out = []
    for kb, name, scope, detector, _src, _supp in RULES:
        if rule_filter and kb != rule_filter:
            continue
        try:
            out.extend(detector(ctx))
        except Exception as exc:  # a broken rule never silently disappears
            out.append(Finding(package.name, kb, name, scope,
                               "candidate.txt:<RULE ERROR>", "%s: %s" %
                               (type(exc).__name__, exc), "RULE-ERROR"))
    return out


def iter_packages(root):
    return sorted(p for p in root.iterdir()
                  if p.is_dir() and find_package_files(p)[1] is not None)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("packages", nargs="*", help="package directories")
    ap.add_argument("--corpus", nargs="?", const=str(HERE), default=None,
                    help="run over every review/ package (dir optional)")
    ap.add_argument("--rule", help="only this KB id (e.g. KB-42)")
    ap.add_argument("--list", action="store_true", help="list rules and exit")
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any finding")
    args = ap.parse_args(argv)

    if args.list:
        for kb, name, scope, _d, src, supp in RULES:
            print("%s\t%s\tscope=%s" % (kb, name, scope))
            print("    source: %s" % src)
            if supp:
                print("    suppressions: %s" % ", ".join(supp))
        print("SUPPRESSIONS (NEGATIVE-LEDGER):")
        for key, val in SUPPRESSIONS.items():
            print("  %s: %s" % (key, val))
        return 0

    if args.corpus:
        packages = iter_packages(pathlib.Path(args.corpus))
    elif args.packages:
        packages = [pathlib.Path(p) for p in args.packages]
    else:
        ap.print_usage(sys.stderr)
        return 2

    findings = []
    for pkg in packages:
        findings.extend(lint_package(pkg, args.rule))

    if args.json:
        print(json.dumps([f.as_dict() for f in findings], ensure_ascii=False, indent=1))
    else:
        for f in findings:
            print(f)
        print("# lint_patterns: %d packages, %d findings" % (len(packages), len(findings)))
    return 1 if (args.strict and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
