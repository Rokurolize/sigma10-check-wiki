#!/usr/bin/env python3
"""Classify the change blocks of a review package by mechanism signature.

Companion to build_review.py. Where build_review owns candidate.txt,
diff.md and the index, this tool owns classification.json and the
skeleton README.md of a package: it diffs the package's frozen original
against the canonical candidate, labels every change block (one maximal
run of non-equal lines from a SequenceMatcher opcode pass) with the
mechanism signatures of the campaign taxonomy, and emits a skeleton
explanation page whose only open parts are the judgment slots.

Pipeline (design: campaign record review-scout/CLASSIFIER.md):
  1. topology pre-pass  -- inventory each side's delivery components,
     match bodies across sides, label relocations DELIVERY-MOVE;
  2. channel tagging    -- module-css / code-css / code-other / html /
     body per line, self-delivery resolved before any code block is
     called inert;
  3. signature pass     -- line-group granularity inside CSS channels,
     labels are a set, one primary by precedence for narration;
  4. residue pass       -- unlabeled and heuristic-only blocks are
     emitted as open slots with their partial-match notes.

Determinism follows build_review.py: no wall-clock values anywhere;
every output derives from the two inputs, sources.tsv, or the recorded
patterns/ commit. The signature-table version is recorded in every
output, so a classification made by an older table is detectable.

Usage:
  python3 review/classify_hunks.py PACKAGE_DIR [options]
  python3 review/classify_hunks.py --original F --candidate F --out DIR
  python3 review/classify_hunks.py --check PACKAGE_DIR

The tool never edits build_review.py's files and never overwrites a
human-edited README.md: a skeleton is written only when README.md is
absent, or byte-identical to a skeleton this tool generated (its hash
is recorded in classification.json).
"""
import argparse
import collections
import difflib
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import unicodedata
import urllib.parse

CLASSIFIER_VERSION = "0.1.0"
SIGNATURE_TABLE_VERSION = "2026-11-17.1"

# ---------------------------------------------------------------------------
# Signature metadata: precision grade, skeleton section, standing Why and
# Verify lines (English; citations by class/KB id, bodies never copied).

SIG_META = {
    "CREDIT-PREVIEW": ("A", 1,
        "Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.",
        "Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp."),
    "TASL-FIELDS": ("A", 1,
        "Credit fields (ruling 3, KB-10): the eight attribution fields are required for the TASL record; campaign translations are credited to AI.",
        "Compare the credit block against the mirror's; every added field needs an evidenced value."),
    "CREDIT-PROSE": ("C", 1,
        "Translated credit prose (P3/P10): attribution text is reader-visible and localizes with the page.",
        "Read the pair in the mirror and the candidate side by side."),
    "T7-CREDIT-CSS": ("B", 1,
        "Credit-module CSS supplement (T7, KB-11/KB-12/KB-62): the JP credit module's DOM needs rules the branch original never shipped, or its inherited rules corrected in place.",
        "KB-11/KB-12 recipes: confirm the selectors in the candidate and whether the production counterpart carries them (supplement vs inherited)."),
    "BARE-RATE-DEL": ("B", 1,
        "Duplicate bare Rate removed (KB-09, ledger class B): the preview credit module is already rate-bearing, so a second bare Rate module double-renders the widget.",
        "Grep both sources for [[module Rate]]; the candidate must hold none outside labelled exhibits."),
    "RATE-EXHIBIT-KEPT-CANDIDATE": ("B", 1,
        "Bare Rate removed beside an exhibit label (KB-09 exception side): labelled paired exhibits are the standing exception, so this needs the writer's kept-vs-removed reasoning, not an automatic fix label.",
        "The exhibit-decision slot for this block, argued from the mirror."),
    "INFO-DEL": ("A", 1,
        "Info-module residue removed (P3, ledger class C): the old info module pair is not part of the JP environment's furniture.",
        "Grep the candidate for info:start / info:end includes; none may remain."),
    "LICENSE-BOX": ("A", 1,
        "License box (T4, KB-63/KB-60): the license box must be present in its settled JP form, restored where the port dropped it.",
        "KB-63 recipe: license-box includes present in the candidate; form judgment per KB-60."),
    "INCLUDE-REPOINT": ("A", 2,
        "Foreign include repointed (P1, KB-15): includes must name the JP counterpart that actually exists on scp-jp.",
        "DEPS record: the repointed target's JP counterpart is verified to exist."),
    "ESCAPED-INCLUDE": ("B", 2,
        "Escaped usage-example include repointed (P1, AGENTS.md section 3): escaped examples are judged too, because readers copy them.",
        "Read the example as a reader would paste it; the include must resolve on scp-jp."),
    "SIGMA-PLUS-JP": ("A", 2,
        "Sigma-plus JP form (T8, KB-64): only component:sigma-plus-jp exists in the JP environment; the bare form does not resolve.",
        "Grep the candidate for component:sigma-plus without the -jp suffix; none may remain."),
    "SIGMA-PLUS-NONJP": ("A", 2,
        "Wrong sigma-plus form: :scp-jp:component:sigma-plus (no -jp) names a page that does not exist and 404s (AGENTS.md section 5).",
        "Grep the candidate for the non-jp form; this is a defect, not a disposition."),
    "COMPONENT-SWAP": ("B", 2,
        "Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.",
        "The swapped target is in the campaign component inventory and exists on the check wiki."),
    "IFTAGS": ("A", 2,
        "Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.",
        "KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly."),
    "DELIVERY-MOVE": ("B", 3,
        "Body relocated between deliveries (topology): where the CSS lives changed (code page to inline module CSS, exhibit to own fragment); the move itself is the change, and internal edits classify separately.",
        "Compare the moved body against its counterpart in the mirror or its companion delivery."),
    "DELIVERY-HOST": ("A", 3,
        "Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.",
        "Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11."),
    "SELF-DELIVERY": ("A", 3,
        "Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel.",
        "The named delivery resolves on the draft host and serves the current candidate body."),
    "BASE-DELIVERY": ("B", 3,
        "Base-theme delivery swap/removal (ruling 1, KB-14, T9/T10): cross-theme imports repoint to the JP fixed base candidate.",
        "Include graph: the named fullname is the base; its JP candidate delivery is the target."),
    "CROSS-IMPORT": ("B", 3,
        "Cross-theme import repoint (KB-14): imports of another theme page take that theme's JP candidate delivery.",
        "Include graph plus the target theme's own package."),
    "DRAFT-HOST": ("A", 3,
        "Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.",
        "Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii))."),
    "DUPIMPORT-DEL": ("A", 4,
        "Duplicated @import removed (KB-65): the same import twice in one channel is a sweep finding; copies inside parameter-gated preset blocks are deliberate and kept.",
        "Grep the candidate for the import string; exactly the intended copies survive."),
    "JPFONT-LOAD": ("A", 4,
        "JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.",
        "KB-16 recipe with base subtraction: the resolved base does not already load the family."),
    "JPFONT-STACK": ("B", 4,
        "JP family appended to a stack (P7/T5): the Latin faces have no kana glyphs; the appended JP family is the fallback that renders Japanese.",
        "Read the paired font-family lines; Latin families unchanged, JP family appended."),
    "FONTLOAD-CJK-STACK": ("B", 4,
        "Stack naming an unloaded CJK face corrected (FIX5 class D tail): a stack that names a face loaded nowhere falls back unpredictably.",
        "The removed face is loaded nowhere in the candidate; the added face is the JP form."),
    "FONT-IMPORT": ("B", 4,
        "Other font-load change (P5, KB-04): malformed family parameters (a hyphen for a +) make the load fail.",
        "KB-04: the family parameter form; the deciding evidence is the load probe (400 vs 200)."),
    "ASSET-REHOST": ("A", 4,
        "Asset re-hosted to JP storage (P5, KB-17): assets are served from the allowlisted JP hosts in this environment.",
        "KB-17 host list; the re-hosted URL serves."),
    "COLON-ENC": ("A", 4,
        "Unencoded colon encoded (KB-01): a raw colon in a URL path segment breaks the local--code / local--files address.",
        "KB-01 recipe: the pair differs only by the %3A encoding."),
    "HEADERVAR": ("A", 5,
        "Header/title variables (P9/T6, KB-57): the header text variables are the theme's visible title surface.",
        "KB-57: where the value stays in the original's language, the disposition is ruling 2 (section 11)."),
    "TRANSLATION-ANCHORED": ("B", 6,
        "Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.",
        "Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing."),
    "TRANS-UNANCHORED": ("C", 6,
        "Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.",
        "Writer confirmation against the mirror, line by line."),
    "GLYPH-FORM": ("B", 6,
        "Shinjitai conversion (R5): retained source-language strings converted to Japanese glyph forms; neither translated nor left untouched, and the reviewer must see it separately.",
        "Fold-compare the pair; only glyph forms differ."),
    "CONTENT-STRING": ("B", 6,
        "Visible string in CSS (KB-18, R1 reader-visible half): content: strings and string-valued variables render for readers.",
        "The string renders in the sample page's DOM text."),
    "COMMENT-TEXT": ("C", 6,
        "CSS comment translation (R1 porter-visible half): comments are porter-visible only; counted and skipped, never argued as reader-facing change.",
        "None; known non-finding class (NEGATIVE-LEDGER candidate)."),
    "LINK-REPOINT": ("C", 7,
        "Link target repointed (P11): prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.",
        "Probe the target; a repoint needs sameness evidence."),
    "RESTORATION": ("C", 8,
        "Deleted/emptied structure restored (ledger class I, FIX5): content the port had lost is restored from the original or a named sibling source.",
        "The ledger/supplement item for this theme, plus the restored region read against the mirror."),
    "EXHIBIT-RESTRUCTURE": ("C", 8,
        "Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.",
        "The exhibit-decision slot for this block, argued from the mirror."),
    "SELECTOR-CORRECTION": ("B", 8,
        "In-place JP-DOM selector correction (R6): an inherited rule's selector is corrected to the frozen JP markup form; nothing was added.",
        "The corrected selector matches the JP module's DOM; declarations are unchanged."),
    "KB06-DEFAULT": ("B", 8,
        "Unsubstituted variable given a default (KB-06): a {$param} no caller supplies renders literally; an evidenced literal default is the fix.",
        "KB-06: the include's parameter list never supplies the variable."),
    "WS-ONLY": ("A", 9,
        "Whitespace-only change (R7 component): no content moved.",
        "Stripped line multisets are equal; counted here so a reviewer can skip the block."),
    "CSS-BODY": ("C", 8,
        "Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.",
        "Writer review; a recurring shape is a new-signature candidate for the patterns loop."),
    "ANNOTATION": ("B", 10,
        "Porter annotation added (R2): translator notes and editor lines are the porter's voice, listed so they are never mistaken for original content.",
        "Each annotation is the porter's addition, absent from the mirror."),
}

# Primary-label precedence for narration (design section 3).
PRECEDENCE = [
    "RESTORATION", "EXHIBIT-RESTRUCTURE",
    "CREDIT-PREVIEW", "TASL-FIELDS", "T7-CREDIT-CSS", "BARE-RATE-DEL",
    "RATE-EXHIBIT-KEPT-CANDIDATE", "INFO-DEL", "LICENSE-BOX",
    "SELECTOR-CORRECTION", "CREDIT-PROSE",
    "COMPONENT-SWAP",
    "DELIVERY-MOVE", "DELIVERY-HOST", "BASE-DELIVERY", "CROSS-IMPORT",
    "SELF-DELIVERY", "DRAFT-HOST",
    "INCLUDE-REPOINT", "ESCAPED-INCLUDE", "SIGMA-PLUS-JP",
    "SIGMA-PLUS-NONJP", "IFTAGS",
    "JPFONT-LOAD", "FONTLOAD-CJK-STACK", "JPFONT-STACK", "FONT-IMPORT",
    "ASSET-REHOST", "COLON-ENC",
    "HEADERVAR", "CONTENT-STRING", "TRANSLATION-ANCHORED", "GLYPH-FORM",
    "LINK-REPOINT", "TRANS-UNANCHORED", "COMMENT-TEXT",
    "ANNOTATION", "WS-ONLY", "CSS-BODY",
]

SECTIONS = [
    (0, "Header / provenance"),
    (1, "Credit and attribution"),
    (2, "Includes and components"),
    (3, "Delivery and code loading"),
    (4, "Fonts and assets"),
    (5, "Header, sidebar, site furniture"),
    (6, "Text translation"),
    (7, "Links"),
    (8, "Structure"),
    (9, "Formatting only"),
    (10, "Porter annotations"),
    (11, "Dispositions and exceptions"),
    (12, "Verification"),
]

# Known JP component ports for COMPONENT-SWAP (campaign inventory seed).
JP_PORTS = {
    "component:sigma-plus-jp", "component:rok-gov-base-jp",
    "component:excerpts-tool-jp", "component:license-box-theme-jp",
    "component:betterbetterfootnote",
}

JP_FAMILIES = ["Noto Sans JP", "Noto Serif JP", "Hiragino Kaku Gothic",
               "Hiragino Sans", "Yu Gothic", "YuGothic", "Meiryo",
               "BIZ UDPGothic", "M PLUS"]
CJK_OS_FACES = ["等线", "邓线", "Microsoft YaHei", "SimSun", "SimHei",
                "NotoSansSC", "Noto Sans SC", "PingFang SC", "NSimSun",
                "FangSong", "KaiTi"]
TASL_TOKENS = ["翻訳責任者", "翻訳年", "原題", "著作権者", "作成年",
               "参照リビジョン", "元記事リンク", "タイトル"]
CREDIT_SELECTOR_RE = re.compile(
    r"\.creditRate|\.creditButton|rate-box-with-credit-button|"
    r"close-credits|\.credit-back|\.fa-info|\.creditModule")

# Simplified / traditional variants -> shinjitai canonical, for
# GLYPH-FORM fold-comparison.
_FOLD_MAP = {
    "國": "国", "语": "語", "龍": "竜", "龙": "竜", "廣": "広", "广": "広",
    "應": "応", "应": "応", "變": "変", "变": "変", "學": "学", "體": "体",
    "點": "点", "线": "線", "开": "開", "關": "関", "关": "関", "页": "頁",
    "员": "員", "现": "現", "时": "時", "间": "間", "圖": "図", "图": "図",
    "书": "書", "畫": "画", "號": "号", "樂": "楽", "乐": "楽", "氣": "気",
    "气": "気", "萬": "万", "與": "与", "这": "這", "个": "個", "们": "們",
    "么": "麼", "讓": "譲", "让": "譲", "實": "実", "实": "実", "长": "長",
    "东": "東", "车": "車", "马": "馬", "门": "門", "见": "見", "贝": "貝",
    "头": "頭", "飞": "飛", "鱼": "魚", "鸟": "鳥", "黃": "黄", "黑": "黒",
    "黨": "党", "舊": "旧", "澤": "沢", "齊": "斉", "櫻": "桜", "樱": "桜",
    "單": "単", "单": "単", "戰": "戦", "战": "戦", "傳": "伝", "传": "伝",
    "达": "達", "远": "遠", "运": "運", "过": "過", "还": "還", "进": "進",
    "连": "連", "邊": "辺", "边": "辺", "选": "選", "钱": "銭", "鐵": "鉄",
    "铁": "鉄", "银": "銀", "场": "場", "歷": "歴", "壓": "圧",
}
GLYPH_FOLD = dict(_FOLD_MAP)

# ---------------------------------------------------------------------------
# Text helpers

def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def kana_count(s):
    return sum(1 for ch in s if "぀" <= ch <= "ヿ")


def cjk_count(s):
    return sum(1 for ch in s if "一" <= ch <= "鿿")


def fold_glyphs(s):
    return "".join(GLYPH_FOLD.get(ch, ch) for ch in s)


def char_overlap(a, b):
    ca, cb = collections.Counter(a), collections.Counter(b)
    inter = sum((ca & cb).values())
    return inter / max(1, max(len(a), len(b)))


def script_delta(removed, added):
    """True when the added side gains kana, or CJK text changed."""
    if kana_count(added) > kana_count(removed):
        return True
    return cjk_count(added) > 0 and cjk_count(removed) > 0 and added != removed


# ---------------------------------------------------------------------------
# Pass 2 (run first in code): channel tagging and components.

_MODULE_CSS_OPEN = re.compile(r"\[\[module\s+css\]\]", re.I)
_MODULE_CLOSE = re.compile(r"\[\[/module\]\]", re.I)
_CODE_OPEN = re.compile(r'\[\[code(?:\s+type="([^"]*)")?\]\]', re.I)
_CODE_CLOSE = re.compile(r"\[\[/code\]\]", re.I)
_HTML_OPEN = re.compile(r"\[\[html\]\]", re.I)
_HTML_CLOSE = re.compile(r"\[\[/html\]\]", re.I)


def tag_channels(lines):
    channels = []
    state = "body"
    for line in lines:
        low = line.strip().lower()
        if state == "body":
            if _MODULE_CSS_OPEN.match(low):
                state = "module-css"
                channels.append(state)
            elif _CODE_OPEN.match(low):
                m = _CODE_OPEN.match(low)
                t = (m.group(1) or "").lower()
                state = "code-css" if t == "css" else (
                    "html" if t == "html" else "code-other")
                channels.append(state)
            elif _HTML_OPEN.match(low):
                state = "html"
                channels.append(state)
            else:
                channels.append("body")
        else:
            channels.append(state)
            if state == "module-css" and _MODULE_CLOSE.match(low):
                state = "body"
            elif state in ("code-css", "code-other") and _CODE_CLOSE.match(low):
                state = "body"
            elif state == "html" and _HTML_CLOSE.match(low):
                state = "body"
    return channels


def components(lines, channels):
    """Maximal runs of one non-body channel, as delivery components."""
    comps = []
    i = 0
    while i < len(lines):
        if channels[i] == "body":
            i += 1
            continue
        j = i
        while j + 1 < len(lines) and channels[j + 1] == channels[i]:
            j += 1
        comps.append({"kind": channels[i], "start": i, "end": j,
                      "lines": lines[i:j + 1]})
        i = j + 1
    return comps


def comment_mask(lines):
    """Per line: True when the line sits inside a /* ... */ span."""
    mask = []
    inside = False
    for line in lines:
        starts_inside = inside
        pos = 0
        touched = starts_inside
        while True:
            if inside:
                end = line.find("*/", pos)
                if end == -1:
                    touched = True
                    break
                inside = False
                pos = end + 2
            else:
                start = line.find("/*", pos)
                if start == -1:
                    break
                touched = True
                inside = True
                pos = start + 2
        mask.append(touched)
    return mask


_CODE_URL_RE = re.compile(
    r"local--code/([^/'\")\s]+)/(\d+)|"
    r"wikidot\.com/([^/'\")\s]+)/code/(\d+)|"
    r"local--code/([^/'\")\s]+)")
_INCLUDE_RE = re.compile(r"\[\[include\s+([^\]\s|]+)")
_FOREIGN_INCLUDE_RE = re.compile(r"\[\[include\s+:([a-z0-9-]+):([^\]\s|]+)", re.I)


def decode_fullname(raw):
    name = urllib.parse.unquote(raw)
    return name


def code_refs(lines):
    """All code-delivery references: (line_index, fullname, number)."""
    refs = []
    for i, line in enumerate(lines):
        for m in _CODE_URL_RE.finditer(line):
            raw = m.group(1) or m.group(3) or m.group(5)
            num = m.group(2) or m.group(4) or ""
            refs.append((i, decode_fullname(raw), num))
    return refs


def include_target(line):
    m = _INCLUDE_RE.search(line)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Pass 1: topology pre-pass.

def body_similarity(a_lines, b_lines):
    sa = collections.Counter(l.strip() for l in a_lines if l.strip())
    sb = collections.Counter(l.strip() for l in b_lines if l.strip())
    if not sa or not sb:
        return 0.0
    inter = sum((sa & sb).values())
    return inter / min(sum(sa.values()), sum(sb.values()))


def topology(orig_lines, orig_ch, cand_lines, cand_ch, own_orig, companions):
    """Return (topology_dict, move_targets_cand, move_sources_orig).

    move_targets_cand: set of candidate component ids (index into the
    candidate component list) that are the receiving side of a move;
    likewise move_sources_orig for the original side.
    """
    o_comps = components(orig_lines, orig_ch)
    c_comps = components(cand_lines, cand_ch)
    moves = []
    tgt, src = set(), set()
    # Content matching across different component kinds.
    for oi, oc in enumerate(o_comps):
        if oc["kind"] not in ("code-css", "code-other", "module-css"):
            continue
        for ci, cc in enumerate(c_comps):
            if cc["kind"] == oc["kind"]:
                continue
            sim = body_similarity(oc["lines"], cc["lines"])
            if sim >= 0.6:
                moves.append({"from_kind": oc["kind"], "to_kind": cc["kind"],
                              "orig_range": [oc["start"], oc["end"] + 1],
                              "cand_range": [cc["start"], cc["end"] + 1],
                              "similarity": round(sim, 3),
                              "basis": "content"})
                src.add(oi)
                tgt.add(ci)
    # Companion deliveries supplied with the package: match by content
    # against candidate components of a different kind.
    for comp in companions:
        cl = comp["lines"]
        for ci, cc in enumerate(c_comps):
            sim = body_similarity(cl, cc["lines"])
            if sim >= 0.6:
                moves.append({"from_kind": "companion:" + comp["name"],
                              "to_kind": cc["kind"],
                              "orig_range": None,
                              "cand_range": [cc["start"], cc["end"] + 1],
                              "similarity": round(sim, 3),
                              "basis": "companion"})
                tgt.add(ci)
    # Candidate-side-only move: the original references its own code
    # delivery whose body is not in the original file, and the
    # candidate carries a large inline module-css body.
    own_refs = [r for r in code_refs(orig_lines) if r[1] == own_orig]
    orig_inline_css = sum(
        1 for c in o_comps if c["kind"] == "module-css"
        for l in c["lines"] if l.strip())
    external_own = bool(own_refs) and orig_inline_css <= 20
    if external_own:
        for ci, cc in enumerate(c_comps):
            if cc["kind"] != "module-css":
                continue
            body = [l for l in cc["lines"] if l.strip()]
            if len(body) >= 20:
                moves.append({"from_kind": "external-own-delivery",
                              "to_kind": "module-css",
                              "orig_range": None,
                              "cand_range": [cc["start"], cc["end"] + 1],
                              "similarity": None, "basis": "candidate-side",
                              "caveat": "companion body unavailable; "
                                        "candidate-side only"})
                tgt.add(ci)
    topo = {
        "original_components": [
            {"kind": c["kind"], "range": [c["start"], c["end"] + 1],
             "lines": len(c["lines"])} for c in o_comps],
        "candidate_components": [
            {"kind": c["kind"], "range": [c["start"], c["end"] + 1],
             "lines": len(c["lines"])} for c in c_comps],
        "moves": moves,
        "external_own_delivery": external_own,
    }
    return topo, o_comps, c_comps, tgt, src


# ---------------------------------------------------------------------------
# Pass 3: signature detectors.
#
# A detector receives a Ctx and returns None or
# (label, {"orig": [[s, e), ...], "cand": [[s, e), ...]}, [notes]).
# Ranges are 0-based half-open line ranges inside the block's own sides,
# expressed as absolute file line ranges for the JSON record.

class Ctx:
    def __init__(self, **kw):
        self.__dict__.update(kw)


def _lines_with(lines, start, pred):
    return [start + i for i, l in enumerate(lines) if pred(l)]


def _span(lines_idx):
    if not lines_idx:
        return []
    out = [[lines_idx[0], lines_idx[0] + 1]]
    for i in lines_idx[1:]:
        if i == out[-1][1]:
            out[-1][1] = i + 1
        else:
            out.append([i, i + 1])
    return out


def _rule_spans(lines, start, idxs):
    """Extend selector-line indices to their full rule (to closing })."""
    out = []
    for i in idxs:
        j = i
        while j + 1 < len(lines) and "}" not in lines[j] and j - i < 14:
            j += 1
        out.append([start + i, start + j + 1])
    return out


def det_credit_preview(ctx):
    hits = _lines_with(ctx.added, ctx.c1,
                       lambda l: re.search(
                           r"\[\[include\s+(:scp-jp:)?credit:(start|end)-preview", l))
    if hits:
        return ("CREDIT-PREVIEW", {"cand": _span(hits)}, [])
    return None


def det_tasl(ctx):
    hits = [ctx.c1 + i for i, l in enumerate(ctx.added)
            if any(t in l for t in TASL_TOKENS)]
    distinct = {t for l in ctx.added for t in TASL_TOKENS if t in l}
    if hits and (ctx.labels_so_far & {"CREDIT-PREVIEW"} or len(distinct) >= 2):
        return ("TASL-FIELDS", {"cand": _span(hits)}, [])
    return None


def det_credit_prose(ctx):
    if ctx.block_cand_range is None:
        return None
    s, e = ctx.block_cand_range
    if ctx.credit_region and ctx.credit_region[0] <= s and e <= ctx.credit_region[1]:
        if script_delta("\n".join(ctx.removed), "\n".join(ctx.added)):
            return ("CREDIT-PROSE", {}, ["position: inside the credit include pair"])
    return None


def det_t7(ctx):
    if not (set(ctx.added_channels) & {"module-css", "code-css"}):
        return None
    idxs = [i for i, l in enumerate(ctx.added) if CREDIT_SELECTOR_RE.search(l)]
    if idxs:
        return ("T7-CREDIT-CSS",
                {"cand": _rule_spans(ctx.added, ctx.c1, idxs)},
                ["supplement-vs-inherited needs the production counterpart"])
    return None


def det_bare_rate(ctx):
    hits = _lines_with(ctx.removed, ctx.o1, lambda l: "[[module Rate]]" in l)
    if not hits:
        return None
    readded = any("[[module Rate]]" in l for l in ctx.added)
    if readded:
        return None
    near = ctx.orig_lines[max(0, ctx.o1 - 6):ctx.o2 + 6]
    exhibit = any(re.search(r"exhibit|sample|見本|サンプル|\[\[tab", l, re.I)
                  for l in near)
    if exhibit:
        return ("RATE-EXHIBIT-KEPT-CANDIDATE", {"orig": _span(hits)},
                ["removed Rate sits beside an exhibit label; routed to "
                 "residue for the writer's kept-vs-removed reasoning"])
    if "credit:start-preview" in ctx.cand_text:
        return ("BARE-RATE-DEL", {"orig": _span(hits)}, [])
    return None


def det_info_del(ctx):
    hits = _lines_with(ctx.removed, ctx.o1,
                       lambda l: re.search(r"\[\[include\s+\S*info:(start|end)", l))
    if hits:
        return ("INFO-DEL", {"orig": _span(hits)}, [])
    return None


def det_license_box(ctx):
    hits = _lines_with(ctx.added, ctx.c1,
                       lambda l: "license-box-" in l and "[[include" in l)
    if not hits:
        return None
    notes = ["restoration (KB-63): the original carried a license box"
             if "license-box" in ctx.orig_text else
             "supplement (T4): the original carried no license box"]
    return ("LICENSE-BOX", {"cand": _span(hits)}, notes)


def _include_pair(ctx):
    """Paired removed/added include lines inside the block."""
    pairs = []
    rems = [(i, l) for i, l in enumerate(ctx.removed) if "[[include" in l]
    adds = [(i, l) for i, l in enumerate(ctx.added) if "[[include" in l]
    for ri, rl in rems:
        for ai, al in adds:
            pairs.append((ri, rl, ai, al))
    return pairs


def det_include_repoint(ctx):
    notes = []
    hit_o, hit_c = [], []
    for ri, rl, ai, al in _include_pair(ctx):
        fm = _FOREIGN_INCLUDE_RE.search(rl)
        if not fm:
            continue
        target = fm.group(2)
        if (":scp-jp:" in al or "[[include " + target in al
                or "[[include :" not in al) and target in al:
            hit_o.append(ctx.o1 + ri)
            hit_c.append(ctx.c1 + ai)
    if hit_o:
        return ("INCLUDE-REPOINT",
                {"orig": _span(hit_o), "cand": _span(hit_c)}, notes)
    return None


def det_escaped_include(ctx):
    def inner(line):
        m = re.search(r"@@(.*)@@", line)
        return m.group(1) if m else None
    hit_o, hit_c = [], []
    for ri, rl in enumerate(ctx.removed):
        ri_in = inner(rl)
        if not ri_in or "[[include" not in ri_in:
            continue
        fm = _FOREIGN_INCLUDE_RE.search(ri_in)
        if not fm:
            continue
        for ai, al in enumerate(ctx.added):
            al_in = inner(al)
            if al_in and fm.group(2) in al_in and ":scp-jp:" in al_in:
                hit_o.append(ctx.o1 + ri)
                hit_c.append(ctx.c1 + ai)
    if hit_o:
        return ("ESCAPED-INCLUDE",
                {"orig": _span(hit_o), "cand": _span(hit_c)}, [])
    return None


def det_sigma_plus(ctx):
    out = []
    bad = _lines_with(ctx.added, ctx.c1,
                      lambda l: ":scp-jp:component:sigma-plus" in l
                      and "sigma-plus-jp" not in l)
    if bad:
        out.append(("SIGMA-PLUS-NONJP", {"cand": _span(bad)},
                    ["names a page that does not exist; defect"]))
    good = _lines_with(ctx.added, ctx.c1,
                       lambda l: "component:sigma-plus-jp" in l)
    bare = _lines_with(ctx.removed, ctx.o1,
                       lambda l: re.search(
                           r"\[\[include\s+(:[a-z0-9-]+:)?component:sigma-plus[\]\s|]", l)
                       and "sigma-plus-jp" not in l)
    if good or bare:
        spans = {}
        if good:
            spans["cand"] = _span(good)
        if bare:
            spans["orig"] = _span(bare)
        out.append(("SIGMA-PLUS-JP", spans,
                    ["bare form removed"] if bare else []))
    return out or None


def det_component_swap(ctx):
    hit_o, hit_c = [], []
    for ri, rl, ai, al in _include_pair(ctx):
        ta, tb = include_target(rl), include_target(al)
        if not ta or not tb or ta == tb:
            continue
        base = tb.split(":")[-1]
        if tb in JP_PORTS or base in JP_PORTS or tb.endswith("-jp"):
            if ta != tb:
                hit_o.append(ctx.o1 + ri)
                hit_c.append(ctx.c1 + ai)
    if hit_o:
        return ("COMPONENT-SWAP",
                {"orig": _span(hit_o), "cand": _span(hit_c)}, [])
    return None


def det_iftags(ctx):
    hit_o, hit_c, notes = [], [], []
    for i, l in enumerate(ctx.removed):
        if "[[iftags" in l:
            hit_o.append(ctx.o1 + i)
    for i, l in enumerate(ctx.added):
        if "[[iftags" in l:
            hit_c.append(ctx.c1 + i)
            if l.strip() == "[[iftags]]":
                notes.append("bare [[iftags]] line: KB-08 anomaly flag")
    if hit_o or hit_c:
        jp = any(("テーマ" in l or "コンポーネント" in l) for l in ctx.added)
        if jp or hit_o:
            return ("IFTAGS",
                    {"orig": _span(hit_o), "cand": _span(hit_c)}, notes)
    return None

def _hosts(line):
    return re.findall(r"https?://([^/'\")\s]+)", line)


def det_delivery_host(ctx):
    hit_o, hit_c = [], []
    for ri, rl in enumerate(ctx.removed):
        for ai, al in enumerate(ctx.added):
            ho, ha = _hosts(rl), _hosts(al)
            if ho and ha and ho != ha:
                if "nu-scptheme.github.io" in ho and "scp-jp.github.io" in ha:
                    hit_o.append(ctx.o1 + ri)
                    hit_c.append(ctx.c1 + ai)
                elif any("local--code" in x for x in (rl, al)) and ho[0] != ha[0]:
                    hit_o.append(ctx.o1 + ri)
                    hit_c.append(ctx.c1 + ai)
    if hit_o:
        return ("DELIVERY-HOST",
                {"orig": _span(sorted(set(hit_o))),
                 "cand": _span(sorted(set(hit_c)))}, [])
    return None


def det_self_delivery(ctx):
    hit_o, hit_c = [], []
    for i, name, _n in code_refs(ctx.removed):
        if name in (ctx.own_orig, ctx.own_cand):
            hit_o.append(ctx.o1 + i)
    for i, name, _n in code_refs(ctx.added):
        if name in (ctx.own_orig, ctx.own_cand):
            hit_c.append(ctx.c1 + i)
    if hit_o or hit_c:
        return ("SELF-DELIVERY",
                {"orig": _span(hit_o), "cand": _span(hit_c)}, [])
    return None


def det_base_cross(ctx):
    """BASE-DELIVERY / CROSS-IMPORT; graph decides, else partial note."""
    hit_o, hit_c, partial = [], [], []
    refs_o = [(i, n) for i, n, _ in code_refs(ctx.removed)
              if n not in (ctx.own_orig, ctx.own_cand)]
    refs_c = [(i, n) for i, n, _ in code_refs(ctx.added)
              if n not in (ctx.own_orig, ctx.own_cand)]
    names = {n for _i, n in refs_o} | {n for _i, n in refs_c}
    for name in names:
        role = ctx.graph.get((ctx.own_cand, name)) if ctx.graph else None
        if role == "base":
            hit_o += [ctx.o1 + i for i, n in refs_o if n == name]
            hit_c += [ctx.c1 + i for i, n in refs_c if n == name]
            return ("BASE-DELIVERY",
                    {"orig": _span(hit_o), "cand": _span(hit_c)},
                    ["base per include graph: " + name])
        if role:
            hit_o += [ctx.o1 + i for i, n in refs_o if n == name]
            hit_c += [ctx.c1 + i for i, n in refs_c if n == name]
            return ("CROSS-IMPORT",
                    {"orig": _span(hit_o), "cand": _span(hit_c)},
                    ["cross-theme per include graph: " + name])
        partial.append("BASE-DELIVERY/CROSS-IMPORT? " + name +
                       " (include graph needed to decide base vs cross)")
    if partial:
        ctx.partial_notes.extend(partial)
    return None


def det_draft_host(ctx):
    hits = _lines_with(ctx.added, ctx.c1,
                       lambda l: "sigma10-jp-test.wdfiles.com" in l)
    if hits:
        return ("DRAFT-HOST", {"cand": _span(hits)},
                ["class (iii) draft-stage form"])
    return None


def det_dupimport(ctx):
    hit_o = []
    gated_all = True
    for i, l in enumerate(ctx.removed):
        if "@import" not in l:
            continue
        key = l.strip()
        occ = [j for j, cl in enumerate(ctx.cand_lines) if cl.strip() == key]
        if occ:
            hit_o.append(ctx.o1 + i)
            for j in occ:
                if not ctx.cand_in_iftags[j]:
                    gated_all = False
    if hit_o:
        notes = []
        prec = "A"
        if gated_all:
            notes.append("every surviving copy sits inside an iftags "
                         "gate; downgraded to heuristic for writer "
                         "confirmation (parameter-gated preset shape)")
            prec = "C"
        return ("DUPIMPORT-DEL", {"orig": _span(hit_o)}, notes, prec)
    return None


def det_jpfont_load(ctx):
    hits = _lines_with(ctx.added, ctx.c1,
                       lambda l: ("@import" in l or "fonts.googleapis" in l
                                  or "<link" in l)
                       and ("Noto+Sans+JP" in l or "Noto+Serif+JP" in l
                            or "Noto Sans JP" in l or "Noto Serif JP" in l
                            or "family=Noto" in l))
    if hits:
        return ("JPFONT-LOAD", {"cand": _span(hits)},
                ["absence claim needs base subtraction (resolved base)"])
    return None


def _font_families(line):
    m = re.search(r"font-family\s*:\s*([^;]+)", line)
    if not m:
        return None
    return [f.strip().strip("'\"") for f in m.group(1).split(",")]


def det_font_stacks(ctx):
    """FONTLOAD-CJK-STACK (precedence) and JPFONT-STACK on paired lines."""
    if len(ctx.removed) != len(ctx.added):
        return None
    cjk_hits, jp_hits = [], []
    for k, (rl, al) in enumerate(zip(ctx.removed, ctx.added)):
        fo, fa = _font_families(rl), _font_families(al)
        if not fo or not fa:
            continue
        removed_cjk = [f for f in fo if any(x in f for x in CJK_OS_FACES)]
        gained_jp = [f for f in fa if any(x in f for x in JP_FAMILIES)
                     and f not in fo]
        if removed_cjk and gained_jp:
            cjk_hits.append(k)
        elif gained_jp:
            latin_o = {f for f in fo if all(x not in f for x in JP_FAMILIES)}
            latin_a = {f for f in fa if all(x not in f for x in JP_FAMILIES)}
            if latin_o <= latin_a:
                jp_hits.append(k)
    out = []
    if cjk_hits:
        out.append(("FONTLOAD-CJK-STACK",
                    {"orig": _span([ctx.o1 + k for k in cjk_hits]),
                     "cand": _span([ctx.c1 + k for k in cjk_hits])}, []))
    elif jp_hits:
        out.append(("JPFONT-STACK",
                    {"orig": _span([ctx.o1 + k for k in jp_hits]),
                     "cand": _span([ctx.c1 + k for k in jp_hits])}, []))
    return out or None


def det_font_import(ctx):
    hit_o, hit_c = [], []
    for i, l in enumerate(ctx.removed):
        if "@import" in l and "fonts.googleapis" in l and "Noto" not in l:
            hit_o.append(ctx.o1 + i)
    for i, l in enumerate(ctx.added):
        if "@import" in l and "fonts.googleapis" in l and "Noto" not in l:
            hit_c.append(ctx.c1 + i)
    if hit_o or hit_c:
        return ("FONT-IMPORT",
                {"orig": _span(hit_o), "cand": _span(hit_c)},
                ["the deciding evidence is the load probe (KB-04)"])
    return None


def det_asset_rehost(ctx):
    hit_o, hit_c = [], []
    for ri, rl in enumerate(ctx.removed):
        for ai, al in enumerate(ctx.added):
            if ("scp-jp-storage.wdfiles.com" in al
                    or "scp-jp.wdfiles.com" in al) and _hosts(rl) != _hosts(al):
                hit_o.append(ctx.o1 + ri)
                hit_c.append(ctx.c1 + ai)
    if hit_o:
        return ("ASSET-REHOST",
                {"orig": _span(sorted(set(hit_o))),
                 "cand": _span(sorted(set(hit_c)))}, [])
    return None


def det_colon_enc(ctx):
    if len(ctx.removed) != len(ctx.added) or not ctx.removed:
        return None
    hits = []
    for k, (rl, al) in enumerate(zip(ctx.removed, ctx.added)):
        if "%3A" in al and al.replace("%3A", ":") == rl and "@@" not in rl:
            hits.append(k)
    if hits and len(hits) == len(ctx.removed):
        return ("COLON-ENC",
                {"orig": _span([ctx.o1 + k for k in hits]),
                 "cand": _span([ctx.c1 + k for k in hits])}, [])
    return None


def det_headervar(ctx):
    pred = lambda l: re.search(r"--(header-title|header-subtitle|logo-image)", l)
    hit_o = _lines_with(ctx.removed, ctx.o1, pred)
    hit_c = _lines_with(ctx.added, ctx.c1, pred)
    if hit_o or hit_c:
        return ("HEADERVAR",
                {"orig": _span(hit_o), "cand": _span(hit_c)}, [])
    return None


_LEAD_TOKEN = re.compile(
    r"^(\[\[[a-zA-Z][^\s\|\]]*|\{\{|\+{1,6}|\*\*?|##|--|\|\||\[\[tab\b)")


def _anchor(a, b):
    sa, sb = a.strip(), b.strip()
    if not sa or not sb:
        return False
    ma, mb = _LEAD_TOKEN.match(sa), _LEAD_TOKEN.match(sb)
    if ma and mb and ma.group(1) == mb.group(1):
        return True
    pa = re.match(r"([a-zA-Z-]+)\s*:", sa)
    pb = re.match(r"([a-zA-Z-]+)\s*:", sb)
    if pa and pb and pa.group(1) == pb.group(1):
        return True
    if sa.endswith("{") and sb.endswith("{") \
            and sa[:-1].strip() == sb[:-1].strip():
        return True
    ha, hb = re.match(r"(\++)", sa), re.match(r"(\++)", sb)
    if ha and hb and ha.group(1) == hb.group(1):
        return True
    return False


def det_translation(ctx):
    rem, add = "\n".join(ctx.removed), "\n".join(ctx.added)
    if not script_delta(rem, add):
        return None
    if len(ctx.removed) == len(ctx.added) and ctx.removed:
        pairs = list(zip(ctx.removed, ctx.added))
        anchored = sum(1 for a, b in pairs if _anchor(a, b))
        if anchored >= (len(pairs) + 1) // 2:
            return ("TRANSLATION-ANCHORED", {},
                    [f"anchored pairs {anchored}/{len(pairs)}"])
    return ("TRANS-UNANCHORED", {},
            ["script delta without the anchor majority"])


def det_glyph(ctx):
    if len(ctx.removed) != len(ctx.added) or not ctx.removed:
        return None
    if kana_count("\n".join(ctx.added)) != kana_count("\n".join(ctx.removed)):
        return None
    good = 0
    for rl, al in zip(ctx.removed, ctx.added):
        if rl == al:
            good += 1
            continue
        if cjk_count(rl) == 0:
            continue
        if char_overlap(fold_glyphs(rl), fold_glyphs(al)) >= 0.75:
            good += 1
    if good >= (len(ctx.removed) + 1) // 2 and good > 0:
        return ("GLYPH-FORM", {}, ["fold-compare: glyph forms only"])
    return None


def det_content_string(ctx):
    pred = lambda l: (re.search(r"content\s*:\s*[\"']", l)
                      or re.search(r"--[a-zA-Z0-9-]*(text|lock-info|theme-name)\s*:", l)
                      or "--RATE_text" in l)
    hit_o = _lines_with(ctx.removed, ctx.o1, pred)
    hit_c = _lines_with(ctx.added, ctx.c1, pred)
    if (hit_o or hit_c) and script_delta("\n".join(ctx.removed),
                                         "\n".join(ctx.added)):
        return ("CONTENT-STRING",
                {"orig": _span(hit_o), "cand": _span(hit_c)}, [])
    return None


def det_comment_text(ctx):
    rem_c = [l for i, l in enumerate(ctx.removed) if ctx.orig_comment[ctx.o1 + i]]
    add_c = [l for i, l in enumerate(ctx.added) if ctx.cand_comment[ctx.c1 + i]]
    if (rem_c or add_c) and script_delta("\n".join(rem_c), "\n".join(add_c)):
        return ("COMMENT-TEXT", {},
                ["porter-visible only; labeled and skipped by design"])
    return None


def det_annotation(ctx):
    hits = _lines_with(ctx.added, ctx.c1,
                       lambda l: "[!--" in l or "**訳注" in l
                       or "Edited for SCP-JP" in l
                       or l.strip().startswith("訳注"))
    if hits:
        return ("ANNOTATION", {"cand": _span(hits)}, [])
    return None


def det_link_repoint(ctx):
    hit_o, hit_c = [], []
    for ri, rl in enumerate(ctx.removed):
        if "[[[" not in rl and "http" not in rl:
            continue
        for ai, al in enumerate(ctx.added):
            if ("[[[" in al or "http" in al) and rl != al:
                to = re.findall(r"\[\[\[([^\]|]+)", rl)
                ta = re.findall(r"\[\[\[([^\]|]+)", al)
                if to and ta and to[0] != ta[0]:
                    hit_o.append(ctx.o1 + ri)
                    hit_c.append(ctx.c1 + ai)
    if hit_o:
        return ("LINK-REPOINT",
                {"orig": _span(sorted(set(hit_o))),
                 "cand": _span(sorted(set(hit_c)))}, [])
    return None


def det_exhibit(ctx):
    rem_text = "\n".join(ctx.removed)
    if not ctx.removed:
        return None
    exhibit = ("[[tab" in rem_text or "[[code" in rem_text
               or ("[[include" in rem_text and "component:" in rem_text))
    if not exhibit:
        return None
    add_text = "\n".join(ctx.added)
    counterpart = any(tok in add_text for tok in ("[[tab", "[[code"))
    if not counterpart:
        return ("EXHIBIT-RESTRUCTURE", {},
                ["no translated counterpart on the added side; the "
                 "writer's replaced-vs-dropped call is forced"])
    return None


def det_restoration(ctx):
    if len(ctx.added) < 8 or ctx.removed and len(ctx.added) < 2 * len(ctx.removed):
        return None
    elsewhere = collections.Counter(
        l.strip() for i, l in enumerate(ctx.orig_lines)
        if not (ctx.o1 <= i < ctx.o2) and l.strip())
    hits = sum(1 for l in ctx.added
               if l.strip() and elsewhere.get(l.strip(), 0) > 0)
    nonblank = sum(1 for l in ctx.added if l.strip())
    if nonblank and hits / nonblank >= 0.6:
        return ("RESTORATION", {},
                ["added content matches the original's own earlier "
                 "region; diff-only signal, supplement decides"])
    return None


def _selector_tokens(line):
    if "{" not in line:
        return None, None
    sel, decl = line.split("{", 1)
    toks = [t for t in re.split(r"[\s>+~]+", sel.strip()) if t]
    return toks, decl


def det_selector_correction(ctx):
    if len(ctx.removed) != len(ctx.added):
        return None
    hits = []
    for k, (rl, al) in enumerate(zip(ctx.removed, ctx.added)):
        to, do = _selector_tokens(rl)
        ta, da = _selector_tokens(al)
        if to is None or ta is None:
            continue
        if do.strip() != da.strip():
            continue
        if to != ta and set(ta) <= set(to) and (">" in al or len(ta) < len(to)):
            hits.append(k)
    if hits:
        sec = 1 if any(CREDIT_SELECTOR_RE.search(ctx.added[k])
                       or CREDIT_SELECTOR_RE.search(ctx.removed[k])
                       for k in hits) else 8
        return ("SELECTOR-CORRECTION",
                {"orig": _span([ctx.o1 + k for k in hits]),
                 "cand": _span([ctx.c1 + k for k in hits])},
                [], {"section": sec})
    return None


def det_kb06(ctx):
    if len(ctx.removed) != len(ctx.added):
        return None
    hits = []
    for k, (rl, al) in enumerate(zip(ctx.removed, ctx.added)):
        if "{$" in rl and "{$" not in al:
            pre = rl.split("{$")[0]
            if pre and al.startswith(pre[:max(4, len(pre) // 2)]):
                hits.append(k)
    if hits:
        return ("KB06-DEFAULT",
                {"orig": _span([ctx.o1 + k for k in hits]),
                 "cand": _span([ctx.c1 + k for k in hits])},
                ["the include's parameter list decides whether the "
                 "variable was ever supplied"])
    return None


def det_ws_only(ctx):
    if not ctx.removed or not ctx.added:
        return None
    if collections.Counter(l.strip() for l in ctx.removed) == \
            collections.Counter(l.strip() for l in ctx.added):
        return ("WS-ONLY", {}, [])
    return None


def det_css_body(ctx):
    chans = set(ctx.added_channels) | set(ctx.removed_channels)
    if not (chans & {"module-css", "code-css"}):
        return None
    nonblank = [l for l in ctx.added if l.strip()]
    if not nonblank:
        nonblank = [l for l in ctx.removed if l.strip()]
    cssish = sum(1 for l in nonblank
                 if re.search(r"[{};]\s*$|:\s*[^;]+;|^\s*[a-z-]+\s*:|"
                              r"^[.#:@*a-zA-Z\[][^=]*\{?\s*$", l))
    if nonblank and cssish / len(nonblank) >= 0.6:
        return ("CSS-BODY", {}, ["no other signature matched"])
    return None


DETECTORS = [
    det_credit_preview, det_tasl, det_t7, det_bare_rate, det_info_del,
    det_license_box, det_include_repoint, det_escaped_include,
    det_sigma_plus, det_component_swap, det_iftags, det_delivery_host,
    det_self_delivery, det_base_cross, det_draft_host, det_dupimport,
    det_jpfont_load, det_font_stacks, det_font_import, det_asset_rehost,
    det_colon_enc, det_headervar, det_glyph, det_content_string,
    det_comment_text, det_annotation, det_link_repoint, det_exhibit,
    det_restoration, det_selector_correction, det_kb06, det_ws_only,
    det_translation, det_credit_prose,
]

# ---------------------------------------------------------------------------
# Block classification driver.

def _norm_result(res):
    """Detectors return None, (label, spans, notes), or
    (label, spans, notes, extra-dict)."""
    if res is None:
        return None
    if len(res) == 3:
        label, spans, notes = res
        return (label, spans, notes, {})
    if len(res) == 4:
        label, spans, notes, extra = res
        if isinstance(extra, str):  # precision grade passed bare
            return (label, spans, notes, {"prec": extra})
        return (label, spans, notes, extra or {})
    raise ValueError("bad detector result: %r" % (res,))


def _in_iftags(lines):
    flags, inside = [], False
    for line in lines:
        low = line.strip().lower()
        if low.startswith("[[iftags"):
            inside = True
        flags.append(inside)
        if low == "[[/iftags]]":
            inside = False
    return flags


def classify_blocks(orig_lines, cand_lines, ctx_extra):
    o_ch = tag_channels(orig_lines)
    c_ch = tag_channels(cand_lines)
    o_comment = comment_mask(orig_lines)
    c_comment = comment_mask(cand_lines)
    topo, o_comps, c_comps, tgt, src = topology(
        orig_lines, o_ch, cand_lines, c_ch,
        ctx_extra["own_orig"], ctx_extra.get("companions", []))
    sm = difflib.SequenceMatcher(None, orig_lines, cand_lines, autojunk=False)
    opcodes = [op for op in sm.get_opcodes() if op[0] != "equal"]
    # Candidate credit region (between the preview includes).
    credit_region = None
    cand_text = "\n".join(cand_lines)
    orig_text = "\n".join(orig_lines)
    start = next((i for i, l in enumerate(cand_lines)
                  if "credit:start-preview" in l), None)
    if start is not None:
        end = next((i for i in range(start, min(len(cand_lines), start + 80))
                    if "credit:end" in cand_lines[i]), None)
        credit_region = (start, (end + 1) if end is not None else start + 1)
    cand_in_iftags = _in_iftags(cand_lines)
    blocks = []
    for bi, (tag, o1, o2, c1, c2) in enumerate(opcodes, 1):
        removed = orig_lines[o1:o2]
        added = cand_lines[c1:c2]
        r_ch = o_ch[o1:o2]
        a_ch = c_ch[c1:c2]
        ctx = Ctx(
            orig_lines=orig_lines, cand_lines=cand_lines,
            removed=removed, added=added,
            o1=o1, o2=o2, c1=c1, c2=c2,
            removed_channels=r_ch, added_channels=a_ch,
            orig_comment=o_comment, cand_comment=c_comment,
            orig_text=orig_text, cand_text=cand_text,
            credit_region=credit_region,
            block_cand_range=(c1, c2),
            cand_in_iftags=cand_in_iftags,
            own_orig=ctx_extra["own_orig"],
            own_cand=ctx_extra["own_cand"],
            graph=ctx_extra.get("graph"),
            labels_so_far=set(), partial_notes=[])
        labels = {}
        notes = []
        extra = {}
        for det in DETECTORS:
            try:
                res = det(ctx)
            except Exception as exc:  # a detector must never abort a run
                notes.append("detector %s raised %s" % (det.__name__, exc))
                continue
            items = res if isinstance(res, list) else [res]
            for item in items:
                norm = _norm_result(item)
                if norm is None:
                    continue
                label, spans, n, x = norm
                if label not in labels:
                    labels[label] = spans
                if label == "SIGMA-PLUS-JP":
                    pass
                notes.extend(n)
                extra[label] = x
                ctx.labels_so_far.add(label)
        # Delivery-move labeling from the topology pre-pass.
        for ci, cc in enumerate(c_comps):
            if ci not in tgt:
                continue
            cand_cover = sum(1 for l in added if l.strip())
            in_span = sum(1 for i, l in enumerate(added)
                          if l.strip() and cc["start"] <= c1 + i <= cc["end"])
            if cand_cover and in_span / cand_cover >= 0.5:
                labels.setdefault("DELIVERY-MOVE", {"cand": [[c1, c2]]})
                move = next((m for m in topo["moves"]
                             if m.get("cand_range") == [cc["start"], cc["end"] + 1]),
                            None)
                if move and move.get("caveat"):
                    notes.append(move["caveat"])
        for oi, oc in enumerate(o_comps):
            if oi not in src:
                continue
            orig_cover = sum(1 for l in removed if l.strip())
            in_span = sum(1 for i, l in enumerate(removed)
                          if l.strip() and oc["start"] <= o1 + i <= oc["end"])
            if orig_cover and in_span / orig_cover >= 0.5:
                labels.setdefault("DELIVERY-MOVE", {"orig": [[o1, o2]]})
        # CSS-BODY catch-all: only when nothing else fired.
        if not labels:
            res = _norm_result(det_css_body(ctx))
            if res:
                label, spans, n, x = res
                labels[label] = spans
                notes.extend(n)
                extra[label] = x
        # Wrapper absorption: a block of only channel markers / blanks
        # inherits the label of the labelled neighbour it wraps.
        marker = re.compile(r"\[\[/?(module|code|html)[^\]]*\]\]", re.I)
        if not labels and removed + added and any(
                marker.match(l.strip()) for l in removed + added) and all(
                l.strip() == "" or marker.match(l.strip())
                for l in removed + added):
            notes.append("wrapper-only block; absorbs the wrapped "
                         "body's label at skeleton build")
            labels = {"__WRAPPER__": {}}
        primary = None
        tier = None
        label_prec = {l: extra.get(l, {}).get(
            "prec", SIG_META[l][0] if l in SIG_META else "C") for l in labels}
        primary_section = None
        if labels and "__WRAPPER__" not in labels:
            primary = next((l for l in PRECEDENCE if l in labels), None)
            precs = list(label_prec.values())
            if "A" in precs:
                tier = "A"
            elif "B" in precs:
                tier = "B"
            else:
                tier = "C"
            if primary:
                primary_section = extra.get(primary, {}).get(
                    "section", SIG_META[primary][1])
        elif "__WRAPPER__" in labels:
            tier = "wrapper"
        blocks.append({
            "id": "B%d" % bi,
            "orig_range": [o1, o2],
            "cand_range": [c1, c2],
            "orig_lines": _range_str(o1, o2),
            "cand_lines": _range_str(c1, c2),
            "channel_pair": [r_ch[0] if r_ch else "body",
                             a_ch[0] if a_ch else "body"],
            "labels": sorted(labels),
            "primary": primary,
            "primary_section": primary_section,
            "label_prec": label_prec,
            "tier": tier,
            "label_spans": labels,
            "notes": notes,
            "partial_notes": ctx.partial_notes,
            "first_removed": removed[0] if removed else "",
            "first_added": added[0] if added else "",
        })
    # Wrapper absorption: resolve __WRAPPER__ against neighbours.
    for i, b in enumerate(blocks):
        if "__WRAPPER__" not in b["labels"]:
            continue
        neighbour = None
        for j in (i - 1, i + 1):
            if 0 <= j < len(blocks) and blocks[j]["primary"]:
                neighbour = blocks[j]
                break
        if neighbour:
            b["labels"] = [neighbour["primary"]]
            b["primary"] = neighbour["primary"]
            b["tier"] = neighbour["tier"]
            b["label_spans"] = {neighbour["primary"]: {}}
            b["notes"].append("absorbed wrapper label from " + neighbour["id"])
        else:
            b["labels"] = []
            b["primary"] = None
            b["tier"] = None
    # Reindent theme-level measure.
    reindent_blocks = 0
    for b in blocks:
        rem = orig_lines[b["orig_range"][0]:b["orig_range"][1]]
        add = cand_lines[b["cand_range"][0]:b["cand_range"][1]]
        if rem and add and len(rem) == len(add):
            if (collections.Counter(l.lstrip() for l in rem)
                    == collections.Counter(l.lstrip() for l in add)
                    and collections.Counter(l.strip() for l in rem)
                    != collections.Counter(l.strip() for l in add)):
                reindent_blocks += 1
    return blocks, topo, reindent_blocks


def _range_str(a, b):
    if a == b:
        return "at %d" % (a + 1)
    return "%d-%d" % (a + 1, b)


def _tier_of(block):
    if not block["labels"]:
        return "residue"
    if block["tier"] == "wrapper":
        return "wrapper"
    prec = block.get("label_prec") or {}
    if any(prec.get(l, SIG_META.get(l, ("C",))[0]) in ("A", "B")
           for l in block["labels"]):
        return "specific"
    if block["labels"] == ["COMMENT-TEXT"]:
        return "skipped"
    return "heuristic"


# ---------------------------------------------------------------------------
# Derived presence labels (whole-candidate, never diff labels).

def derived_presence(orig_lines, cand_lines, blocks):
    cand_ranges = [(b["cand_range"][0], b["cand_range"][1])
                   for b in blocks if b["cand_range"][0] != b["cand_range"][1]]

    def unchanged(line_no):
        return not any(s <= line_no < e for s, e in cand_ranges)

    out = {}
    foreign = [i for i, l in enumerate(cand_lines)
               if _FOREIGN_INCLUDE_RE.search(l) and unchanged(i)]
    if foreign:
        out["FOREIGN-KEPT"] = {
            "class": "named exception candidate (KB-54 / KB-15)",
            "count": len(foreign),
            "lines": [_range_str(i, i + 1) for i in foreign[:5]],
            "example": cand_lines[foreign[0]].strip()}
    http = [i for i, l in enumerate(cand_lines)
            if "http://" in l and unchanged(i)]
    if http:
        out["HTTP-KEPT"] = {
            "class": "(ii) posting rewrite",
            "count": len(http),
            "lines": [_range_str(i, i + 1) for i in http[:5]],
            "example": cand_lines[http[0]].strip()}
    bhl = [i for i, l in enumerate(cand_lines)
           if "nu-scptheme.github.io" in l and unchanged(i)]
    if bhl:
        out["OLD-BHL-KEPT"] = {
            "class": "(ii) posting rewrite",
            "count": len(bhl),
            "lines": [_range_str(i, i + 1) for i in bhl[:5]],
            "example": cand_lines[bhl[0]].strip()}
    return out


# ---------------------------------------------------------------------------
# Skeleton README generation.

def _slot(name, instruction):
    return "<!-- SLOT: %s -->\n%s\n" % (name, instruction)


def build_skeleton(classification, patterns_commit, supplement_items=None):
    theme = classification["theme"]
    blocks = classification["blocks"]
    by_section = collections.defaultdict(list)
    for b in blocks:
        if not b["primary"]:
            continue
        label = b["primary"]
        sec = b.get("primary_section") or SIG_META.get(label, ("C", 8))[1]
        by_section[sec].append((label, b))
    derived = classification["derived_presence"]
    out = []
    out.append("# Review package — %s" % theme["cand_fullname"])
    out.append("")
    out.append("Status: draft (skeleton generated by classify_hunks.py %s; "
               "SLOT markers remain)" % CLASSIFIER_VERSION)
    out.append("Candidate: %s (sha256 %s)"
               % (theme["candidate_file"], theme["candidate_sha256"]))
    out.append("Original: %s — %s, revision %s (sha256 %s)"
               % (theme["orig_fullname"], theme.get("wiki", "?"),
                  theme.get("revision", "?"), theme["original_sha256"]))
    out.append("Classifier: classify_hunks.py %s; signature table %s; "
               "patterns commit %s"
               % (CLASSIFIER_VERSION, SIGNATURE_TABLE_VERSION,
                  patterns_commit or "unrecorded"))
    out.append("")
    out.append("## 0. Header / provenance")
    out.append("")
    topo = classification["topology"]
    moves = topo["moves"]
    if moves:
        for m in moves:
            line = "- Delivery: %s -> %s" % (m["from_kind"], m["to_kind"])
            if m.get("similarity") is not None:
                line += " (body similarity %.2f)" % m["similarity"]
            if m.get("caveat"):
                line += " — " + m["caveat"]
            out.append(line)
    else:
        out.append("- Delivery: no relocation detected between the sides; "
                   "each side's components match by kind.")
    if classification.get("r4_signal"):
        s = classification["r4_signal"]
        out.append("- Production-adoption signal: candidate resembles the "
                   "production JP counterpart at %.2f similarity vs %.2f "
                   "for the original (R4); declaration is a slot below."
                   % (s["cand_prod"], s["cand_orig"]))
    out.append("")
    out.append(_slot("provenance-route",
        "State the provenance route: derived from the original at the "
        "reference revision, adopted from the production JP counterpart "
        "(R4), or JP original with no reference revision, with the "
        "evidence for it."))
    out.append("")
    out.append("## Class summary")
    out.append("")
    counts = collections.Counter()
    for b in blocks:
        for l in b["labels"]:
            counts[l] += 1
    if counts:
        out.append("| Label | Blocks |")
        out.append("|---|---|")
        for label, n in sorted(counts.items()):
            out.append("| %s | %d |" % (label, n))
    else:
        out.append("No labels: every block is residue.")
    out.append("")
    out.append("Counts: %d blocks, %d specific, %d heuristic, %d residue, "
               "%d skipped (comment text)."
               % (len(blocks), classification["summary"]["specific"],
                  classification["summary"]["heuristic"],
                  classification["summary"]["residue"],
                  classification["summary"]["skipped"]))
    out.append("")
    for sec_no, sec_name in SECTIONS[1:]:
        out.append("## %d. %s" % (sec_no, sec_name))
        out.append("")
        items = by_section.get(sec_no, [])
        if sec_no == 9:
            out.append("- WS-ONLY blocks: %d"
                       % sum(1 for b in blocks if "WS-ONLY" in b["labels"]))
            out.append("- Re-indentation: %d blocks pair up after "
                       "leading-whitespace normalization"
                       % classification["summary"]["reindent_blocks"])
            if classification["summary"]["reindent_blocks"] >= 10:
                out.append("- Theme-level verdict: wholesale re-indentation "
                           "suspected (R7); follow-up-diff applicability "
                           "is on record here, not hidden.")
            out.append("")
            continue
        if sec_no == 11:
            if derived:
                for label, d in derived.items():
                    out.append("- %s: %d occurrence(s), e.g. %s "
                               "(lines %s). Class: %s."
                               % (label, d["count"], d["example"],
                                  ", ".join(d["lines"]), d["class"]))
            else:
                out.append("- No derived presence label fired.")
            if supplement_items:
                for item in supplement_items:
                    out.append("- FIX5 item %s: %s."
                               % (item.get("item", "?"),
                                  item.get("outcome", "?")))
            out.append("")
            out.append(_slot("disposition-argument",
                "For every disposition stub above, restate the grounds so "
                "a reviewer can re-derive them from the two sources in "
                "this package (the R-disp standard)."))
            out.append("")
            continue
        if sec_no == 12:
            out.append(_slot("verification-results",
                "Record the T1 checker outcome, T2/T3 status, and T4 "
                "follow-up diff outcome as actually run, or why a test "
                "does not apply, each phrased as a check the reviewer "
                "can re-run."))
            out.append("")
            continue
        if not items:
            out.append("none — no signature for this section fired over "
                       "%d change blocks." % len(blocks))
            out.append("")
            continue
        seen_labels = []
        for label, b in items:
            if label not in seen_labels:
                seen_labels.append(label)
        for label in seen_labels:
            prec, _sec = SIG_META[label][0], SIG_META[label][1]
            out.append("- %s (%s): %s" % (label, prec, SIG_META[label][2]))
            out.append("  Verify: %s" % SIG_META[label][3])
            for _l, b in items:
                if _l == label:
                    out.append("  - %s: orig %s -> cand %s (%s -> %s)"
                               % (b["id"], b["orig_lines"], b["cand_lines"],
                                  b["channel_pair"][0], b["channel_pair"][1]))
            out.append("")
        out.append(_slot("judgment",
            "For each class above, state why this theme's instance is "
            "right (the palette adaptation of a T7 supplement, the "
            "priority value chosen for a frame, the slogan default under "
            "KB-06, or equivalent)."))
        out.append("")
        if any(l in ("EXHIBIT-RESTRUCTURE", "RATE-EXHIBIT-KEPT-CANDIDATE")
               for l, _b in items):
            out.append(_slot("exhibit-decision",
                "For every EXHIBIT-RESTRUCTURE block, state replaced vs "
                "dropped and the ground; for every bare-Rate block beside "
                "an exhibit label, state the kept-vs-removed reasoning."))
            out.append("")
    out.append("## Appendix — residue blocks")
    out.append("")
    residue = [b for b in blocks if _tier_of(b) == "residue"]
    heuristic = [b for b in blocks if _tier_of(b) == "heuristic"]
    if not residue and not heuristic:
        out.append("No residue: every block carries a specific label.")
    else:
        for i, b in enumerate(residue + heuristic, 1):
            out.append("### Residue R%d — %s (%s; orig %s -> cand %s, "
                       "%s -> %s)"
                       % (i, b["id"], _tier_of(b), b["orig_lines"],
                          b["cand_lines"], b["channel_pair"][0],
                          b["channel_pair"][1]))
            if b["first_removed"]:
                out.append("- Removed first line: %s" % b["first_removed"])
            if b["first_added"]:
                out.append("- Added first line: %s" % b["first_added"])
            for n in b["partial_notes"]:
                out.append("- Partial match that failed a guard: %s" % n)
            for n in b["notes"]:
                out.append("- Note: %s" % n)
            out.append("")
            out.append(_slot("residue-resolution",
                "Assign this block to a section (and write it there) or "
                "propose it as a new signature / pattern in the lane "
                "report."))
            out.append("")
    return "\n".join(out) + "\n"

# ---------------------------------------------------------------------------
# Assembly and CLI.

def read_sources_tsv(path):
    rows = {}
    if not path or not path.is_file():
        return rows
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return rows
    header = lines[0].split("\t")
    for line in lines[1:]:
        cells = line.split("\t")
        row = dict(zip(header, cells + [""] * (len(header) - len(cells))))
        if row.get("dir"):
            rows[row["dir"]] = row
    return rows


def load_graph(path):
    graph = {}
    if not path:
        return graph
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        cells = line.split("\t")
        if len(cells) >= 3 and not line.startswith("#"):
            graph[(cells[0], cells[1])] = cells[2]
    return graph


def load_supplement(path, cand_fullname):
    if not path:
        return []
    items = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        cells = line.split("\t")
        if len(cells) >= 3 and cells[0] == cand_fullname:
            items.append({"item": cells[1], "outcome": cells[2]})
    return items


def patterns_commit(repo_root):
    try:
        r = subprocess.run(
            ["git", "-C", str(repo_root), "log", "-1", "--format=%H",
             "--", "patterns/"],
            capture_output=True, text=True, timeout=10)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except Exception:
        pass
    return None


def classify(original_path, candidate_path, theme, companions=None,
             graph=None, production_path=None):
    o_bytes = pathlib.Path(original_path).read_bytes()
    c_bytes = pathlib.Path(candidate_path).read_bytes()
    o_lines = o_bytes.decode("utf-8").splitlines()
    c_lines = c_bytes.decode("utf-8").splitlines()
    comp = []
    for cp in companions or []:
        p = pathlib.Path(cp)
        comp.append({"name": p.name,
                     "lines": p.read_bytes().decode("utf-8").splitlines()})
    blocks, topo, reindent_blocks = classify_blocks(
        o_lines, c_lines,
        {"own_orig": theme["orig_fullname"], "own_cand": theme["cand_fullname"],
         "companions": comp, "graph": graph})
    derived = derived_presence(o_lines, c_lines, blocks)
    summary = {
        "blocks": len(blocks),
        "specific": sum(1 for b in blocks if _tier_of(b) == "specific"),
        "heuristic": sum(1 for b in blocks if _tier_of(b) == "heuristic"),
        "residue": sum(1 for b in blocks if _tier_of(b) == "residue"),
        "skipped": sum(1 for b in blocks if _tier_of(b) == "skipped"),
        "reindent_blocks": reindent_blocks,
        "label_counts": dict(collections.Counter(
            l for b in blocks for l in b["labels"])),
    }
    result = {
        "tool": "classify_hunks.py",
        "classifier_version": CLASSIFIER_VERSION,
        "signature_table_version": SIGNATURE_TABLE_VERSION,
        "theme": dict(theme,
                      original_file=str(original_path),
                      candidate_file=str(candidate_path),
                      original_sha256=sha256_bytes(o_bytes),
                      candidate_sha256=sha256_bytes(c_bytes),
                      original_lines=len(o_lines),
                      candidate_lines=len(c_lines)),
        "topology": topo,
        "blocks": blocks,
        "derived_presence": derived,
        "summary": summary,
        "residue": [b["id"] for b in blocks if _tier_of(b) == "residue"],
    }
    if production_path:
        p_lines = pathlib.Path(production_path).read_bytes() \
            .decode("utf-8").splitlines()
        result["r4_signal"] = {
            "cand_prod": round(body_similarity(p_lines, c_lines), 3),
            "cand_orig": round(body_similarity(o_lines, c_lines), 3),
        }
    return result


def report_lines(result):
    s = result["summary"]
    yield "blocks=%d specific=%d heuristic=%d residue=%d skipped=%d" % (
        s["blocks"], s["specific"], s["heuristic"], s["residue"],
        s["skipped"])
    for b in result["blocks"]:
        tier = _tier_of(b)
        if tier in ("residue", "heuristic"):
            yield "RESIDUE: %s %s orig %s -> cand %s (%s -> %s): %s" % (
                tier.upper(), b["id"], b["orig_lines"], b["cand_lines"],
                b["channel_pair"][0], b["channel_pair"][1],
                "; ".join(b["partial_notes"] + b["notes"]) or "no signature")


def write_outputs(result, out_dir, theme_name, patterns_hash,
                  supplement_items=None, write_skeleton=True):
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    skeleton_hash = None
    skeleton_status = "not-written"
    if write_skeleton:
        readme = out_dir / "README.md"
        skeleton = build_skeleton(result, patterns_hash, supplement_items)
        if not readme.is_file():
            readme.write_text(skeleton, encoding="utf-8")
            skeleton_hash = sha256_bytes(skeleton.encode("utf-8"))
            skeleton_status = "written (new)"
        else:
            existing = readme.read_bytes()
            prior = None
            cj = out_dir / "classification.json"
            if cj.is_file():
                try:
                    prior = json.loads(cj.read_text(encoding="utf-8")) \
                        .get("skeleton", {}).get("sha256")
                except Exception:
                    prior = None
            if prior and sha256_bytes(existing) == prior:
                readme.write_text(skeleton, encoding="utf-8")
                skeleton_hash = sha256_bytes(skeleton.encode("utf-8"))
                skeleton_status = "regenerated (was byte-identical skeleton)"
            else:
                skeleton_status = ("REFUSED: README.md is human-edited "
                                   "(or of unknown provenance); untouched")
    result["skeleton"] = {"sha256": skeleton_hash, "status": skeleton_status}
    cj = pathlib.Path(out_dir) / "classification.json"
    cj.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n",
                  encoding="utf-8")
    return skeleton_status


def check_package(pkg_dir, theme, original_path, candidate_path):
    pkg = pathlib.Path(pkg_dir)
    cj_path = pkg / "classification.json"
    if not cj_path.is_file():
        print("PROBLEM: %s has no classification.json" % pkg)
        return 1
    try:
        recorded = json.loads(cj_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print("PROBLEM: %s classification.json unreadable: %s" % (pkg, exc))
        return 1
    problems = 0
    if recorded.get("classifier_version") != CLASSIFIER_VERSION \
            or recorded.get("signature_table_version") != SIGNATURE_TABLE_VERSION:
        print("PROBLEM: %s classification made by classifier %s / table %s, "
              "current is %s / %s — STALE"
              % (pkg, recorded.get("classifier_version"),
                 recorded.get("signature_table_version"),
                 CLASSIFIER_VERSION, SIGNATURE_TABLE_VERSION))
        problems += 1
    th = recorded.get("theme", {})
    for key, path in (("original_sha256", original_path),
                      ("candidate_sha256", candidate_path)):
        now = sha256_bytes(pathlib.Path(path).read_bytes())
        if th.get(key) != now:
            print("PROBLEM: %s %s changed since classification — STALE"
                  % (pkg, key))
            problems += 1
    sk = recorded.get("skeleton", {})
    if sk.get("sha256") and not (pkg / "README.md").is_file():
        print("PROBLEM: %s skeleton README.md was generated but is missing"
              % pkg)
        problems += 1
    if not problems:
        print("OK: %s classification is fresh" % pkg)
    return 1 if problems else 0


def derive_theme(name, candidate_path, original_path, row):
    cand_fullname = row.get("cand_fullname") or ""
    orig_fullname = row.get("orig_fullname") or ""
    if not cand_fullname and candidate_path:
        stem = pathlib.Path(candidate_path).stem
        cand_fullname = stem if ":" in stem else "theme:" + stem
    if not orig_fullname and cand_fullname:
        orig_fullname = cand_fullname[:-3] if cand_fullname.endswith("-jp") \
            else cand_fullname
    return {
        "dir": name,
        "cand_fullname": cand_fullname,
        "orig_fullname": orig_fullname,
        "wiki": row.get("wiki", ""),
        "revision": row.get("revision", ""),
        "kind": row.get("kind", "normal"),
        "verdict": row.get("verdict", ""),
    }


def find_in_package(pkg, *names):
    for n in names:
        p = pkg / n
        if p.is_file():
            return p
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("package", nargs="?", help="package directory")
    ap.add_argument("--check", action="store_true",
                    help="verify classification freshness only (no writes)")
    ap.add_argument("--original", help="original source file (ad-hoc mode)")
    ap.add_argument("--candidate", help="candidate source file")
    ap.add_argument("--out", help="output directory (ad-hoc mode)")
    ap.add_argument("--name", help="package name (ad-hoc mode)")
    ap.add_argument("--repo", help="repo root (for pages/ lookup and the "
                                   "patterns commit)")
    ap.add_argument("--sources", help="sources.tsv path")
    ap.add_argument("--graph", help="include-graph TSV (theme, referenced, "
                                    "role)")
    ap.add_argument("--supplement", help="FIX5 items TSV (theme, item, "
                                         "outcome)")
    ap.add_argument("--production", help="production counterpart file "
                                         "(R4 signal)")
    ap.add_argument("--companions", nargs="*", default=[],
                    help="companion delivery files for the topology "
                         "pre-pass")
    ap.add_argument("--no-skeleton", action="store_true",
                    help="write classification.json only")
    args = ap.parse_args(argv)

    graph = load_graph(args.graph)
    repo_root = pathlib.Path(args.repo) if args.repo else None

    # Ad-hoc mode.
    if args.original and args.candidate:
        name = args.name or pathlib.Path(args.candidate).stem
        theme = derive_theme(name, args.candidate, args.original, {})
        result = classify(args.original, args.candidate, theme,
                          companions=args.companions, graph=graph,
                          production_path=args.production)
        out_dir = pathlib.Path(args.out) if args.out else pathlib.Path(".")
        status = write_outputs(result, out_dir, name,
                               patterns_commit(repo_root) if repo_root else None,
                               write_skeleton=not args.no_skeleton)
        for line in report_lines(result):
            print(line)
        print("skeleton: %s" % status)
        print("classification.json: %s" % (out_dir / "classification.json"))
        return 0

    if not args.package:
        ap.error("a package directory (or --original/--candidate) is required")
    pkg = pathlib.Path(args.package)
    here = pathlib.Path(__file__).resolve().parent
    sources_path = pathlib.Path(args.sources) if args.sources \
        else here / "sources.tsv"
    rows = read_sources_tsv(sources_path)
    row = rows.get(pkg.name, {})
    if not row and re.fullmatch(r"[a-z0-9][a-z0-9-]*", pkg.name):
        # Dir-key fallback: the directory name is the candidate slug
        # (TOOLING section 1); sources.tsv takes precedence when a row
        # exists.
        row = {"cand_fullname": "theme:" + pkg.name}
    original = find_in_package(pkg, "original.txt", "original.css")
    candidate = None
    if args.candidate:
        candidate = pathlib.Path(args.candidate)
    else:
        candidate = find_in_package(pkg, "candidate.txt", "candidate.css")
    if candidate is None and row.get("cand_fullname") and repo_root:
        guess = repo_root / "pages" / (row["cand_fullname"] + ".txt")
        if guess.is_file():
            candidate = guess
    if original is None or candidate is None:
        print("PROBLEM: %s lacks an original or a resolvable candidate"
              % pkg)
        return 1
    theme = derive_theme(pkg.name, str(candidate), str(original), row)
    if args.check:
        return check_package(pkg, theme, original, candidate)
    result = classify(original, candidate, theme,
                      companions=args.companions, graph=graph,
                      production_path=args.production)
    items = load_supplement(args.supplement, theme["cand_fullname"])
    status = write_outputs(
        result, pkg, pkg.name,
        patterns_commit(repo_root or (here.parent)),
        supplement_items=items, write_skeleton=not args.no_skeleton)
    for line in report_lines(result):
        print(line)
    print("skeleton: %s" % status)
    return 0


if __name__ == "__main__":
    sys.exit(main())
