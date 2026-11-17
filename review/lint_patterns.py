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
    # --- adjudicated amendments (ADJ1 / ADJ2, 2026-11-18) ---
    "KB-03:inherited-url-none": (
        "url(none) byte-identical to the original is the original's closed "
        "no-image idiom (relative 'none' request; the co-declared background "
        "still paints), not a malformed resource; KB-03 only nominates its "
        "literal url(null)/url()/elided/unbalanced forms."
    ),
    "KB-07:component-frame-scope": (
        "the 'original has frame, candidate has none' pair fire is scoped to "
        "theme packages; for a component/fragment/base-CSS package the wrapper "
        "frame belongs to the companion theme package, not the fragment."
    ),
    "KB-21:inherited-scheme-route": (
        "an include parameter byte-identical to the original except for the "
        "scheme (https -> http), with '= ' spacing inherited and tolerated by "
        "the module, is a KB-42 class-(ii) standing record, not a KB-21 defect."
    ),
    "KB-42:attribute-selector-match": (
        "http:// inside a CSS [href=...]/[href*=...] attribute-selector MATCH "
        "string selects the site's own link and loads nothing."
    ),
    "KB-42:doc-anchor-specimen": (
        "http:// inside an [[a href=...]] inline-anchor syntax specimen is a "
        "documentation example, not a delivered reference."
    ),
    "KB-42:escaped-wikilink-label": (
        "http:// used as a wikilink display label inside an escaped/specimen "
        "exhibit is prose, not a fetched URL."
    ),
    "KB-42:blank-evidence": (
        "a KB-42 fire with an empty evidence line is corpus drift (package "
        "refreshed after the run), not an adjudicable reference; skip it."
    ),
    "KB-42:kb21-defer": (
        "a port-introduced 'name=\\s+http://' include parameter is KB-21's "
        "shape; do not double-nominate under KB-42. The inherited-scheme-only "
        "form is routed by KB-21:inherited-scheme-route to the KB-42 record."
    ),
    "KB-70:selector-coverage": (
        "a sole [[code]] block carrying CSS declarations is the stylesheet even "
        "with a universal/pseudo-element/pseudo-class selector or a gated "
        "preset fragment; selector-shape blind spots are not port hits."
    ),
    "KB-71:aligned-block-boundaries": (
        "css_channels boundaries are computed on a newline-preserving scrub and "
        "index ctx['lines']; a multi-line @@...@@ span no longer shifts the "
        "reported range or manufactures an unclosed comment."
    ),
    "KB-71:original-side-depth": (
        "a depth_end>0 finding whose original block at the same ordinal ends at "
        "the same depth is a recorded original-state shape (standing "
        "disposition), not a port-introduced brace displacement."
    ),
    "KB-72:documented-face-match": (
        "a documented face that matches a loaded/declared face (after stripping "
        "Wikidot markup, the copula and span tails, and splitting face lists), "
        "or a face-less prose/joke specimen, is not a KB-72 nomination."
    ),
    "KB-73:carried-gate-body": (
        "a gate marker whose body is a non-blank module/wikitext slot (any case "
        "of 'module css', interleaved [[ift{$p}gs]] and '[!{$p} --]' closers) "
        "carries its content and is not an emptied slot."
    ),
    "KB-76:live-tail-only": (
        "only live [[div]] blocks outside [[code]]/[[module]] and @@/{{ escapes "
        "count as tail duplicates; exhibit/sample text is not a live div."
    ),
    "KB-76:original-region-pairing": (
        "pair the duplicated signature against the original's whole-file count "
        "(not a fixed last-60-line window) when the body was restructured."
    ),
    "KB-78:original-empty-pair": (
        "a candidate empty collapsible whose original carries the same empty "
        "pair (parameterized openers and blank lines included, compared by "
        "proximity/label) is inherited, not a port hit; stay silent."
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
        # ADJ1 §3.3(a)/§4.1: preserve newlines in every mask so scrubbed-line
        # indices stay aligned with ctx["lines"]. Replacing a newline with a
        # space here shifted every later candidate.txt:N evidence line after a
        # multi-line @@...@@ span (flopstyle-dark delta 975, KB-70/71/76 FPs).
        for k in range(a, min(b + 2, len(text))):
            if text[k] != "\n":
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


def code_block_spans(lines):
    """ADJ1 §3.3: served-byte census of [[code]] blocks.

    Channel markers are detected on escape-masked raw lines so a stray CSS
    /* ... */ span in the prose cannot swallow a real [[code]] opener
    (flopstyle-dark /1 at L1820 sits under a comment opened at L249). Gated
    blocks are included; escaped @@/{{ examples are not.
    """
    _, escaped = _scrub(lines)
    starts = []
    off = 0
    for line in lines:
        starts.append(off)
        off += len(line) + 1
    spans = []
    stack = None
    for idx, line in enumerate(lines):
        base = starts[idx]
        for m in re.finditer(r"\[\[code[^\]]*\]\]", line):
            if not escaped[base + m.start()]:
                stack = idx
        close = line.find("[[/code]]")
        if close >= 0 and stack is not None and not escaped[base + close]:
            spans.append((stack, idx))
            stack = None
    if stack is not None:
        spans.append((stack, len(lines) - 1))
    return [{"kind": "code-raw", "start": a, "end": b} for a, b in spans]


def parse_includes(lines):
    """Return include blocks: {name,start,end,params:[(line,key,value)]}."""
    blocks = []
    i = 0
    # ADJ2 KB-07 (wikifot): stop the include-name capture at a whitespace-
    # delimited key= token before | / ]] so an inline priority=1 on the opening
    # line is parsed as a parameter instead of swallowed into the name.
    open_re = re.compile(
        r"\[\[include\s+([^\]\n|]+?)(?=\s+[\w-]+\s*=|\s*\]\]|\s*\||\s*$)"
    )
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
        # ADJ1 §1: KB-03's literal recipe is url(null)/url()/elided/unbalanced;
        # url(none) is the original's closed no-image idiom (suppression
        # KB-03:inherited-url-none) and is never nominated.
        if re.search(r"url\(\s*null\s*\)", low) or re.search(r"url\(\s*\)", low):
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
        # Only nominate when the original had a frame (the port dropped it), and
        # only for theme packages. ADJ2 KB-07 (peroxide-jp-base-css): the frame
        # of a component/fragment/base-CSS package belongs to its companion
        # theme wrapper, not to the fragment's own delivery.
        o = "".join(ctx["orig_lines"])
        if "interwiki-style" in o:
            name = ctx["package"]
            component_like = ("base-css" in name or "fragment" in name
                              or "component" in name)
            if component_like and "interwiki-style" not in "\n".join(ctx["lines"]):
                return
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
    """True if two loads sit in distinct mutually exclusive conditional gates.

    ADJ2 KB-07 (foxtrot): recognise the interleaved form
    ``>[[iftags]][[/ift{$p}gs]]`` in addition to ``[!-- {$p} ...]``. Each
    preset is gated by a distinct parameter, so at most one load renders.
    """
    def gate_before(idx):
        for k in range(idx, max(-1, idx - 12), -1):
            m = re.search(r"\[!--\s*\{\$([\w-]+)", lines[k])
            if not m:
                m = re.search(r"\[\[/ift\{\$([\w-]+)\}gs\]\]", lines[k])
            if m:
                return m.group(1)
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


def _orig_scheme_include(ctx, line):
    """Original include carrying the same target and the '= ' spacing.

    The candidate's line number need not match the original's (the y2k doc
    body moved), so the inherited spacing is matched by include target, not
    by line index (ADJ1 §2).
    """
    m = re.search(r"\[\[include\s+([^\s|\]]+)", line)
    if not m:
        return ""
    name = m.group(1)
    for ol in ctx["orig_lines"]:
        if name in ol and re.search(r"=\s+https?://", ol):
            return ol
    return ""


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
        if re.search(r"\[\[image\s+http://", s):
            yield Finding(ctx["package"], "KB-21", "lint_fragile_param", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          "http scheme inside [[image ...]] asset parameter")
        elif re.search(r"=\s+http://", s):
            # ADJ1 §2 routing: when the original's corresponding include carries
            # the same '= ' spacing, the stray space is inherited and tolerated
            # by the module; the scheme delta is KB-42's class-(ii) standing
            # record (suppression KB-21:inherited-scheme-route), not a KB-21
            # defect. Only a port-introduced stray space is charged here.
            if not _orig_scheme_include(ctx, line):
                yield Finding(ctx["package"], "KB-21", "lint_fragile_param", "candidate:",
                              "candidate.txt:%d" % (i + 1), line,
                              "space inside asset parameter")


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

    ADJ2 adds four suppressions: attribute-selector MATCH strings (chaos,
    magazine, internal-affairs), [[a href=...]] syntax specimens (sci-fi,
    scplive, share-future, steam-guide), wikilink labels in escaped exhibits
    (paramycota), and empty evidence lines (magazine, flopstyle-dark). The
    inherited-scheme-only include param (y2k) stays: ADJ1 §2 routes KB-21's
    charge here as the class-(ii) standing record.
    """
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if not line.strip():
            continue  # KB-42:blank-evidence: corpus drift, not a reference
        for m in re.finditer(r"http://([^\s\"'\)\|>\]]+)", s):
            host = m.group(1).split("/")[0]
            if any(h in m.group(1) for h in NL07_HTTP_HOSTS):
                continue  # NL-07: namespace identifier, not a fetched URL
            pre = s[max(0, m.start() - 80):m.start()]
            post = s[m.end():m.end() + 12]
            # CSS attribute-selector MATCH string: selects the site's own link.
            if (re.search(r"href\*?=\s*[\"'][^\"']*$", pre)
                    and post.startswith(("\"]", "']"))):
                continue  # KB-42:attribute-selector-match
            # [[a href="..."]] inline-anchor documentation specimen.
            if (re.search(r"\[\[a[^\]]*href\*?=\s*[\"'][^\"']*$", pre)
                    and post.startswith(("]]", "\"]", "']"))):
                continue  # KB-42:doc-anchor-specimen
            # http:// as the display label of a [[[...|...]]] wikilink exhibit.
            if (re.search(r"\[\[\[[^\]]*\|$", pre) and post.startswith("]]]")):
                continue  # KB-42:escaped-wikilink-label
            if re.search(r"=\s+http://", s) and not _orig_scheme_include(ctx, line):
                continue  # KB-42:kb21-defer: a port-introduced stray space
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
    code_chans = code_block_spans(ctx["lines"])
    # A delivered code block need not carry type="css" (sci-fi-jp's /1 is a
    # plain [[code]] that holds the stylesheet); judge by CSS markers.
    # ADJ1 §3.1/§3.2: broaden selector coverage to the universal selector,
    # pseudo-classes/pseudo-elements and arbitrary simple selectors, and treat
    # a page's sole code block with CSS declarations as the stylesheet. Gated
    # preset/fragment blocks stay in the census (they are delivered ordinals).
    def looks_css(c):
        body = "\n".join(ctx["lines"][c["start"]:c["end"] + 1])
        css_re = (r"(:root\s*\{|@import\b|font-family\s*:"
                  r"|[ #.][\w-]+(?:::?[\w-]+)*\s*\{|\*\s*\{|::?[\w-]+\s*\{)")
        if re.search(css_re, body):
            return True
        return (len(code_chans) == 1
                and bool(re.search(r"[\w-]+\s*:\s*[^;{}]+;", body)))
    chans = [c for c in code_chans if looks_css(c)]  # gated blocks included
    self_refs = []
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        # ADJ1 §3.3(b): only local--code/ is a code address; a local--files/
        # asset URL is never parsed as an ordinal self-reference.
        if "local--code/" not in s:
            continue
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
            # ADJ1 §4.1/§4.2: the pattern's own deciding step re-checks the
            # delivered block against the original side before emitting. The
            # original's corresponding stylesheet may be a [[module CSS]] or
            # a [[code]] block at a different ordinal (immrama, pastel-skies,
            # wikifot), so pair by the depth PROFILE (end depth + longest
            # positive run), not by channel index. An identical profile is a
            # recorded original-state shape; ink's port-introduced unclosed
            # rule has no such counterpart and still fires.
            note = "block ends above depth 0"
            if ctx["orig_lines"]:
                for och in css_channels(ctx["orig_lines"]):
                    oblock = ctx["orig_lines"][och["start"]:och["end"] + 1]
                    odepth = 0
                    orun = 0
                    olargest = 0
                    for ol in oblock:
                        odepth += ol.count("{") - ol.count("}")
                        if odepth >= 1:
                            orun += 1
                            olargest = max(olargest, orun)
                        else:
                            orun = 0
                    if odepth == end_depth and abs(olargest - longest) <= 2:
                        note = ("DISPOSITION: original %s L%d ends depth=%d "
                                "longest=%d - inherited original shape "
                                "(KB-71:original-side-depth)"
                                % (och["kind"], och["start"] + 1, odepth, olargest))
                        break
            yield Finding(ctx["package"], "KB-71", "lint_block_structure", "candidate:",
                          "candidate.txt:%d-%d" % (ch["start"] + 1, ch["end"] + 1),
                          "brace_depth_end=%d longest_positive=%d" % (end_depth, longest),
                          note)


def _kb72_faces(raw):
    """ADJ2 KB-72: extract ASCII font-face tokens from a documented value.

    Strip Wikidot markup, wiki-link labels, the copula です/です。 and gloss
    parentheses, then split a /-separated face list into individual faces.
    A token mixing Latin letters with Japanese prose is not a face.
    """
    v = raw.strip()
    v = re.sub(r"\[\[\[[^\]]*?\|([^\]]+)\]\]\]", r" \1 ", v)
    v = re.sub(r"\[\[\*[^\]]*?\|([^\]]+)\]\]", r" \1 ", v)
    # Remaining Wikidot tags ([[footnote]], [[span]], [[div]], ...) are
    # furniture, not faces: cosmos L207's note text must not yield 'footnote'.
    v = re.sub(r"\[\[/?[^\]]*\]\]", " ", v)
    v = v.replace("**", " ").replace("//", " ").replace("@@", " ")
    v = re.sub(r"です。?\s*$", "", v.strip())
    v = re.sub(r"（[^）]*）|\([^)]*\)", " ", v)
    trim = " 　「」\"'*/-{}[]。、.:;!?＋"
    v = v.strip(trim)
    faces = []
    for part in v.split("/"):
        p = part.strip(trim)
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9 ._+-]*", p):
            faces.append(p)
    return faces


def _kb72_tokens(text):
    """Case-/punctuation-insensitive token set (adelle-sans == Adelle Sans)."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def lint_doc_default(ctx):
    """KB-72: documented default contradicts the shipped :root variable / loaded font.

    ADJ2: compare extracted faces, not the linter's greedy capture of です /
    ** / [[/span]]; a face-less prose/joke specimen is not a nomination.
    Record-ground dispositions stay for the per-package report.
    """
    text = "\n".join(ctx["lines"])
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        # Require a documentation statement: keyword followed by a colon, or
        # the '本文フォントはX' prose form. CSS selector lines (.btn-default)
        # and code lines are not documentation statements.
        m = re.search(r"(?m)^(?!.*[{};])\s*(?:\*\*)?(?:デフォルト値|デフォルト|default|本文フォントは)\s*[:：]\s*[「\"']?([^\s」\"'、。]+)", s)
        if not m:
            m = re.search(r"本文フォントは\s*([^\s、。]+)", s)
        if not m:
            continue
        raw = m.group(1)
        full = re.search(r"本文フォントは\s*(.+)$", line)
        if full:
            raw = full.group(1)
        faces = _kb72_faces(raw)
        if not faces:
            continue  # no named face: prose/joke specimen (KB-72:documented-face-match)
        others = [l for k, l in enumerate(ctx["lines"]) if k != i]
        delivered = "\n".join(re.findall(r"(?m)^[^\n]*:root[^\n]*\{[\s\S]*?\}",
                                          "\n".join(others)))
        delivered += "\n" + "\n".join(
            l for l in others
            if re.search(r"@import\b|font-family\s*:|--[\w-]*font[\w-]*\s*:", l, re.I))
        dtokens = _kb72_tokens(delivered)
        if all(_kb72_tokens(f) <= dtokens for f in faces):
            continue  # every documented face is loaded/declared
        # Record-ground dispositions (e.g. a carried translated specimen or a
        # base-theme specimen) are adjudicated per package; the byte-level
        # detector reports the nomination and does not invent that record.
        yield Finding(ctx["package"], "KB-72", "lint_doc_default", "candidate:",
                      "candidate.txt:%d" % (i + 1), line,
                      "documented faces %r not found in :root/loads" % (faces,))


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
        if (re.search(r"\[!--\s*\{\$", s)
                or re.search(r"\[\[/?ift[^\]]*\{\$", s)):
            # ADJ2 KB-73 type (b): a gate carries its body when the span up to
            # its closer holds a module (any case of 'module css') or any
            # non-blank wikitext token. Recognise interleaved [[ift{$p}gs]]
            # markers and the '[!{$p} --]' closer form as well.
            j = i + 1
            while j < len(ctx["lines"]) and not re.search(
                    r"\[!--[^\]]*--\]|\[![^\]]*--\]", ctx["lines"][j]):
                j += 1
            body = ctx["lines"][i + 1:j] if j > i + 1 else []
            window = "\n".join(body) if body else "\n".join(ctx["lines"][i + 1:i + 6])
            if re.search(r"\[\[module\s+css\s*\]\]", window, re.I):
                continue  # KB-73:carried-gate-body
            if re.search(r"\S", window):
                continue  # a non-blank wikitext slot carries its contents
            yield Finding(ctx["package"], "KB-73", "lint_param_gate", "candidate:",
                          "candidate.txt:%d" % (i + 1), line,
                          "slot marker with no module (b) - verify variant paths first")


def lint_dup_tail_block(ctx):
    """KB-76: duplicate live [[div]] block at the candidate tail.

    ADJ1 §5: build the tail census from a newline-preserving scrub (KB-71's
    aligned boundaries), excluding [[code]]/[[module]] channels and @@/{{}
    escapes, so exhibit/sample text is not counted as a live div. Pair the
    signature against the ORIGINAL'S WHOLE-FILE count, not a fixed last-60-line
    window: a restructured body moves the documentation region to the tail.
    """
    if not ctx["orig_lines"]:
        return

    def live_div_opens(lines, window=None):
        scrubbed = _scrub(lines)[0].split("\n")
        covered = set()
        for ch in css_channels(lines):
            for k in range(ch["start"], ch["end"] + 1):
                covered.add(k)
        first = 0 if window is None else max(0, len(lines) - window)
        out = []
        for k in range(first, len(lines)):
            s = scrubbed[k] if k < len(scrubbed) else ""
            if k in covered:
                continue
            if re.match(r"\s*\[\[div\b", lines[k]) and re.match(r"\s*\[\[div\b", s):
                out.append(lines[k].strip())
        return out

    c = live_div_opens(ctx["lines"], 60)
    o = live_div_opens(ctx["orig_lines"])  # whole-file pairing
    for sig in set(c):
        if c.count(sig) > 1 and c.count(sig) > o.count(sig):
            yield Finding(ctx["package"], "KB-76", "lint_dup_tail_block", "pair",
                          "candidate.txt:<tail>", sig[:200],
                          "candidate live tail count %d > original whole-file %d" %
                          (c.count(sig), o.count(sig)))


def lint_empty_collapsible(ctx):
    """KB-78: [[collapsible]] open immediately followed by its close (empty)."""
    for i, line, s in split_scrubbed(ctx["scrubbed"], ctx["lines"]):
        if re.match(r"\s*\[\[collapsible\b", s):
            j = i + 1
            while j < len(ctx["lines"]) and not ctx["lines"][j].strip():
                j += 1
            if j < len(ctx["lines"]) and re.match(r"\s*\[\[/collapsible\]\]", ctx["lines"][j]):
                # ADJ2 KB-78: the original-side test must also recognise a
                # parameterized opener followed (after blank lines) by its
                # close, and pair by proximity/label rather than the literal
                # [[collapsible]][[/collapsible]] string. An inherited empty
                # pair is original-state (KB-78:original-empty-pair) and stays
                # silent; a candidate-only empty pair is the nomination.
                oempty = False
                ol = ctx["orig_lines"]
                for k in range(len(ol)):
                    if not re.match(r"\s*\[\[collapsible\b", ol[k]):
                        continue
                    jj = k + 1
                    while jj < len(ol) and not ol[jj].strip():
                        jj += 1
                    if jj < len(ol) and re.match(r"\s*\[\[/collapsible\]\]", ol[jj]):
                        oempty = True
                        break
                if oempty:
                    continue
                yield Finding(ctx["package"], "KB-78", "lint_empty_collapsible", "pair",
                              "candidate.txt:%d-%d" % (i + 1, j + 1), line + " / " + ctx["lines"][j],
                              "candidate-only empty collapsible (relocated content)")


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
     "Static detection: url(null)/url()/url(https://…)/unbalanced url( per declaration",
     ["KB-03:inherited-url-none"]),
    ("KB-07", "lint_interwiki_style", "candidate:/pair", lint_interwiki_style,
     "Static detection: count interwiki-style includes, priorities, theme= args",
     ["KB-07:mutually-exclusive-gate", "KB-07:original-identical-stack",
      "KB-07:component-frame-scope"]),
    ("KB-13", "lint_modalbox_pin", "candidate:", lint_modalbox_pin,
     "Static detection: global .modalbox position:fixed + no .credit-static-view carve-out", []),
    ("KB-20", "lint_oversize", "candidate:", lint_oversize,
     "Static detection: character-count every candidate against 200000",
     ["KB-20:own-css-size"]),
    ("KB-21", "lint_fragile_param", "candidate:", lint_fragile_param,
     "Static detection: include param '= ' and http:// inside include/image params",
     ["KB-21:inherited-scheme-route"]),
    ("KB-32", "lint_preview_credit", "candidate:", lint_preview_credit,
     "Static detection (file-first disposition): credit:start-preview -> credit-modal is preview-form", []),
    ("KB-42", "lint_http_scheme", "candidate:", lint_http_scheme,
     "Static detection: grep http:// in live references; class (ii) on sight",
     ["NL-07:xmlns-identifier", "NL-15:css-source-comment", "KB-42:inherited-http",
      "KB-42:attribute-selector-match", "KB-42:doc-anchor-specimen",
      "KB-42:escaped-wikilink-label", "KB-42:blank-evidence", "KB-42:kb21-defer"]),
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
     ["KB-70:inherited-self-import", "KB-70:selector-coverage"]),
    ("KB-71", "lint_block_structure", "candidate:", lint_block_structure,
     "Static detection: comment termination + brace-depth profile per delivered block",
     ["NL-01/02:two-channel", "KB-71:aligned-block-boundaries", "KB-71:original-side-depth"]),
    ("KB-72", "lint_doc_default", "candidate:", lint_doc_default,
     "Static detection: documented default vs :root vars / loaded font set",
     ["KB-72:documented-face-match"]),
    ("KB-73", "lint_param_gate", "pair", lint_param_gate,
     "Static detection: original gate/slot dropped, emptied, or undocumented",
     ["KB-73:param-gated-channel", "KB-73:carried-gate-body"]),
    ("KB-76", "lint_dup_tail_block", "pair", lint_dup_tail_block,
     "Static detection: duplicate short [[div]] block at candidate tail > original",
     ["KB-76:live-tail-only", "KB-76:original-region-pairing"]),
    ("KB-78", "lint_empty_collapsible", "pair", lint_empty_collapsible,
     "Static detection: [[collapsible]] open immediately followed by close",
     ["KB-78:original-empty-pair"]),
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
