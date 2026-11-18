# theme:stellar-jp — Stellar theme (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:stellar-jp — origin EN, population #141 [GOSIGN2-LEDGER (b) row 141]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now e150c7f32c1490c6d54e77b6707c867474eb0b5119c0d508faa10c498170d79b); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 0 infos (hotlink×6, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 161; GOSIGN2-LEDGER (b) row 141]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 498–503px@320/375 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN20))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN20))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 141, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 141]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 141]
- Computed against: canonical commit 2dbb83da26b94a9c4a2e7de3a1562025f3552358; candidate file pages/theme:stellar-jp.txt sha256:e150c7f32c1490c6d54e77b6707c867474eb0b5119c0d508faa10c498170d79b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

This file is the explanation record for one theme's Sigma-10 port. The
diff it explains is `diff.md` in this directory, generated from
`original.txt` (the frozen mirror) and `candidate.txt` (a byte copy of
the canonical candidate). The verdict stamp at the head of this file is generated; do not
edit inside the stamp markers.

## Provenance

- Theme: `theme:stellar` on scp-wiki (EN branch), revision 19.
  Author GeminidStrix; an aesthetic theme built on Basalt.
- Frozen mirror: `original.txt`, 1,016 lines, 41,402 bytes, SHA-256
  `75a505a24417079cebb0a44214947897b5e2dfd24b722f9935bea90297c70d17`
  (matches `review/sources.tsv`; mirror-store class COPY).
- Candidate: `candidate.txt`, 1,603 lines, 72,071 bytes, SHA-256
  `24643dbb5a91bf0b578090e972fc66b77c64336dada08d3421be7b4b9adb8c7b`,
  byte-identical to the canonical file.
- Kind (sources.tsv): K5b-3 — the candidate layers over
  `theme:basalt-jp`; this diff covers the theme's own layer only.
- The candidate entered the canonical repository in the Stage 2 EN20
  integration (3faf2e1, LOCALIZE-S2-C wave) and was touched twice
  since: by f931619 (FIX2-COLON — the commit whose diff also carries
  this file's Basalt repoint, section 3) and by a497307 (FIX4-MECH,
  duplicate-import removal).
- Upstream state: the T4 lane's follow-up diff from revision 19
  found no changes; the original is still at revision 19, so this
  package's baseline is current as well as frozen.

## Summary

Stellar is the largest of the Basalt-layer ports in this batch: a
full variable and component layer over the base, with a long
documentation body. The port inlines the layer's CSS into a head
module over a basalt-jp import, frames the base at priorities 1 and
2, translates the body one-for-one, and converts the license tail to
the JP license-box form. T4 charged the theme on four patterns; two
of them (the EN-CDN base dependency and the credit's translator
field) are answered in the current bytes, one (the EN-article link
with a JP counterpart) still stands and is flagged below, and one
(the three EN file hotlinks) is dispositioned through the T1
standing class with its JP-hosted forms not yet uploaded. One
methodological warning belongs in this summary: the classifier
aligned this pair into only 13 blocks, because the candidate
interleaves the moved CSS with the body and defeats line alignment.
The shares in the class summary are therefore block shares over a
collapsed alignment; every section below was adjudicated against
diff.md and the two files directly, not against the block labels.

## Class summary (auto-classification)

13 change blocks: 13 specific (100%), 0 heuristic, 0 residue,
0 skipped — over the collapsed alignment described in the summary.
The generator counts +1,032 / −445 lines (1,477 changed lines). The
classifier detects one relocation (the code exhibit's CSS → the head
module, similarity 0.961) plus a candidate-side external-delivery
note. Label firings: DELIVERY-MOVE ×12, IFTAGS ×2, EXHIBIT-RESTRUCTURE
×2, DRAFT-HOST ×2, TRANS-UNANCHORED ×2, and single firings of
ASSET-REHOST, DELIVERY-HOST, SELF-DELIVERY, FONT-IMPORT, JPFONT-STACK,
COLON-ENC, CONTENT-STRING, CREDIT-PREVIEW, HEADERVAR, RESTORATION,
TASL-FIELDS, INCLUDE-REPOINT, LICENSE-BOX, and
RATE-EXHIBIT-KEPT-CANDIDATE.

Adjudication notes: the RATE-EXHIBIT-KEPT-CANDIDATE firing (block B1,
original span L8–9) is a false-fire — it marks the original's bare
Rate lines, and the candidate contains no Rate module anywhere
(`grep 'module Rate' candidate.txt` is empty; the T4 lane verified
the same). Both EXHIBIT-RESTRUCTURE primaries resolve to the head
mega-block (B1) and the license conversion (B13); the exhibit census
is unchanged (section 8). The RESTORATION primary on B12 is an
artifact of the collapsed alignment: the block spans the moved CSS,
the frame and credit zone, and the source exhibit, and checked
against the files it contains no restoration of dropped content —
its parts are the standard swaps of sections 0–3. The
CONTENT-STRING firing is empty `content: ""` values (candidate
L1183, L1235): no reader-visible string.

## 0. Tag frame and page furniture

**What.** The candidate's head stands outside the tag gate: the
delivery module (candidate L1–581), then two interwiki-style frame
includes naming the base delivery at priorities 1 and 2 (candidate
L583–591, section 3), then the gate `[[iftags +テーマ]]` (candidate
L592, block B12, IFTAGS) opening over the credit block and body. The
original opens its gate at L6 (`[[iftags +theme]]`) after its head
module and has no frame includes at all — its base arrived by plain
@import.

**Why.** Pattern class P1 (frame and tag furniture; KB-03, KB-04).
Failure prevented: a gate keyed to the EN tag name never opens on
scp-jp, and a layered theme whose frames name the origin branch's
bundle applies the wrong base in the check environment.

**Verify.** `grep -n 'iftags\|interwiki-style' candidate.txt` — gate
at L592 with the JP tag name; two frames above it, both
`:scp-jp:component:interwiki-style`.

**Disposition.** No ledger line charges the frame placement. The (b)
verdict for this theme is PASS.

## 1. Credit block and license (P3, P9)

**What.** The original's credit furniture is a bare Rate in a
right-aligned div with no label (original L8–10), deleted — the
candidate has no Rate module (section: class summary). The candidate
carries a preview credit block (candidate L594–603, block B12:
CREDIT-PREVIEW, TASL-FIELDS) with eight fields: title Stellarテーマ;
translator of record AI; translation year 2026; original title
Stellar Theme; copyright holder GeminidStrix; creation year 2026;
reference revision 19; and a source link to
`https://scp-wiki.wikidot.com/theme:stellar` — the host
`review/sources.tsv` records, so the host check passes. The author
field agrees with the original's prose credit and license box.

The license record converts form: the original carries the
background image's license between a `license-box-theme` /
`license-box-end` include pair with `=====` separators and English
fields (original L1006–1015); the candidate carries
`:scp-jp:component:license-box-backend` with `author=GeminidStrix`
and `license-box-end` (candidate L1597–1602, block B13, LICENSE-BOX),
its fields translated （ファイル名 / 作者 / ライセンス / 出典）. The
source field keeps the file's EN wiki-host URL, the original's own
form, as the file's origin record.

**Why.** Pattern classes P3 (credit furniture swap; KB-16, KB-17)
and P9 (license box; KB-47, KB-48). Failure prevented: a bare Rate
beside the credit block renders a second rating widget, and a
license statement in the EN component form does not render on
scp-jp.

**Verify.** `sed -n '594,603p' candidate.txt`;
`sed -n '1597,1602p' candidate.txt` against original L1006–1015.

**Disposition.** T4 charged the credit on pattern 3: at check time
the translator field read `SCP-JP`, an organisation name that
identifies no translator. The current bytes name AI, the campaign's
translator of record, so the charge no longer stands; all eight
fields were present even then. Ledger part (c3) records no credit
line for this theme (its only line is P4), so the repair is visible
only in the bytes — noted here so the record is complete. No credit
CSS supplement exists on either side.

## 2. Includes and component references (P2, P8)

**What.** Every live include in the candidate is `:scp-jp:`-prefixed
or a JP delivery import: the credit pair (section 1), the two frames
(section 0), twelve image-block exhibits repointed to
`:scp-jp:component:image-block`, and the license-box pair
(section 1). The usage exhibit names the correct posting name in
`:scp-jp:` form: `{{@@[[include :scp-jp:theme:stellar-jp]]@@}}`
(candidate L614, block B1's region; INCLUDE-REPOINT fires once, on
the license include). This theme is not in the plain-slug sweep
family. The head module's second import, the Wide Image Sizer
component's CSS, is a delivery import and is covered in section 3.

**Why.** Pattern classes P2 (include repoints; KB-05) and P8
(exhibit fidelity; KB-42, KB-43). Failure prevented: an exhibit or
live include pointing at the origin branch shows readers a page that
is not the one this candidate installs.

**Verify.** `grep -n 'scp-wiki:' candidate.txt` returns nothing;
`grep -n 'include' candidate.txt` lists the frame, credit,
image-block, and license includes.

**Disposition.** No ledger line charges the repoints; the T4 lane's
pattern-1 verdict for this theme was APPLIED. The (b) verdict is
PASS.

## 3. Delivery topology (P4)

**What.** The original's head module (original L1–5) imports three
stylesheets: the Wide Image Sizer component's CSS from the JP files
host (`https://scp-jp.wdfiles.com/local--code/component:wide-image-sizer/1`
— a JP-hosted component the EN theme already depended on), Basalt
from the EN files host (`local--code/theme:basalt/1`, unencoded
colon), and its own layer from the page's code URL
(`https://scp-wiki.wikidot.com/theme:stellar/code/1`). The layer's
source is the code exhibit (original L419–999).

The candidate's head module (candidate L1–581) imports basalt-jp's
delivery (candidate L2) and the Wide Image Sizer import kept on its
JP host with the colon now encoded (candidate L3, COLON-ENC in block
B11's family), then carries the layer's CSS inline — the
classifier's relocation, similarity 0.961 (blocks B1–B12,
DELIVERY-MOVE ×12). The source exhibit is retained below the body
(candidate L1013–1590) mirroring the delivered CSS. The frames
(section 0) name basalt-jp at priorities 1 and 2.

The path here matters. The Stage-2 candidate first imported the
Basalt CDN bundle's two files (normalize, bedrock) in the module and
framed the same two URLs — T4's pattern-4 charge, display-affecting:
the entire base was a live EN-CDN dependency. The current bytes
import and frame `theme:basalt-jp/1` instead. The change landed in
commit f931619, whose title records only unencoded-colon URL fixes;
its diff for this file shows the two CDN imports and both frame
values replaced by the basalt-jp delivery (and a second basalt-jp
import the FIX4-MECH wave later removed as a duplicate, KB-65).

**Why.** Pattern class P4 (delivery topology; KB-23). Failure
prevented: a port whose base arrives from the origin branch's CDN
inherits the EN base wholesale and breaks if the bundle moves;
layering over the JP base candidate makes the port a member of the
JP theme family. Keeping the Wide Image Sizer import is the same
class in the other direction: the component is JP-hosted, and the
candidate's host is the one the JP site serves.

**Verify.** `sed -n '1,3p' candidate.txt`;
`grep -n 'cdn.scpwiki' candidate.txt` returns nothing;
`git show f931619 -- pages/theme:stellar-jp.txt` shows the repoint.

**Disposition.** Ledger part (c3) records "P4 DISPOSITIONED
(delivery class (ii): original-state CDN delivery)". As with the
sibling Basalt ports, the wording understates the bytes: the
dependency was not left in place under a class-(ii) waiver, it was
repointed to the JP base candidate. The per-theme record (item 4)
states the discrepancy; this package follows the bytes. The
draft-host form of the delivery URLs is environment class (iii)
(KB-41).

## 4. Fonts and assets (P5, P7)

**What.** Fonts. The original's CSS imports its display faces from a
CoolLabs Fonts mirror (Orbitron + Roboto; Quantico) and the author's
personal `fonts.css` hosted on the EN wiki
(`https://scp-wiki.wikidot.com/local--files/geminid/fonts.css`,
original L441–443). The candidate imports both families from Google
Fonts (candidate L24–25, block B3, FONT-IMPORT) and drops the
personal file. The stacks are JP-covered: the UI and body stacks
read `'Quantico', 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Yu Gothic', sans-serif`
(candidate L37, L112, block B7, JPFONT-STACK), and Noto Sans JP is
actually loaded by the base (basalt-jp loads it). One gap stands:
the mono stack names `'JetBrains Mono', 'Noto Sans Mono CJK JP'`
(candidate L102 and exhibit L1111), and neither face is loaded by
the candidate or its base. Two wording corrections recorded per
`FIX-STELLAR.md` item 2(b): the original's bytes name only
`'Jetbrains Mono'` (original L520, `--body-font-primary`), so the
two-face stack with the CJK fallback is the port's own P7 rewrite,
not a feature of the original; and the author's personal `fonts.css`
(original L443), probed once on 2026-11-17, serves (302 → 200,
`text/css`, 49,654 bytes) but declares only three data-URI faces
('CIRCLE-STARGAZE', 'PROJECT SPACE', 'SQUARE-STARGAZE'), has no
`@import`, and contains no "JetBrains" in any case — it cannot carry
a mono load as served today (whether an earlier revision did could
not be verified). The port dropped the personal-file hotlink and did
not replace the load; the documentation's font sample still tells
readers the monospace font is JetBrains Mono (candidate L991).

Assets. Three EN-hosted files are referenced, each twice (delivered
module and source exhibit): the object-warning component's logo
(`--logo`, candidate L30 / L1039, scp-wiki.wdfiles.com), the theme's
background image (`--stellar-background`, candidate L101 / L1110,
scp-wiki.wikidot.com — the very file the license box documents), and
the header icon (`Cream-SCP-icon.svg`, candidate L276 / L1285).
These six references are exactly T1's hotlink×6 for this theme.

**Why.** Pattern classes P7 (font stacks; KB-35, KB-36) and P5
(assets; KB-25, KB-26). Failure prevented: a stack naming an unloaded
font silently falls back, and assets left on the origin host are
outside the port's control.

**Verify.** `sed -n '23,26p' candidate.txt`;
`grep -n 'JetBrains' candidate.txt` (two stacks, one sample claim,
no load); `grep -n 'scp-wiki.wdfiles\|scp-wiki.wikidot.com/local--files'
candidate.txt` lists the six asset references.

**Disposition.** The font-stack charge (pattern 7) is DISPOSITIONED
in the ledger's class summary where the base delivers the face —
basalt-jp loads Noto Sans JP — and the stacks themselves carry JP
faces throughout. The mono faces are not covered by that
disposition; T4 noted the same gap without a display-affecting mark.
It is recorded as a minor flag in the per-theme record (item 2). The
asset references are dispositioned as T1's hotlink standing class,
environment class (ii) (register c1); their end-state is recorded
with probe evidence in the per-theme record (item 3).

## 5. Header, titles and rendered strings (P6)

**What.** The layer sets its own header text, in JP:
`--title: "SCP財団"` and `--subtitle: "確保 - 収容 - 保護"`
(candidate L35–36), bound through `--header-title: var(--title)` /
`--header-subtitle: var(--subtitle)` (candidate L32–33; HEADERVAR
firing in block B12 at the exhibit copy, L1041–1042). The original's
values were "SCP Foundation" / "SECURE - CONTAIN - PROTECT". The
subtitle's spaced-hyphen form faithfully follows the EN dash style;
it differs from the comma form some JP themes use, a variant rather
than an error (the T4 lane's pattern-9 note). Unlike its sibling
Stargazer, this theme does not inherit header text from the base, so
the Basalt migration raised no header question here. The
CONTENT-STRING firing is empty `content: ""` values: no
reader-visible string.

**Why.** Pattern class P6 (header and rendered strings; KB-29,
KB-30, KB-31). Failure prevented: a JP page rendering an EN masthead
from its own variables.

**Verify.** `grep -n -- '--title:\|--subtitle:' candidate.txt`;
`grep -n 'SCP Foundation' candidate.txt` returns nothing.

**Disposition.** No ledger line charges the header for this theme.
The (b) verdict is PASS.

## 6. Body translation (P10)

**What.** The documentation body is translated in full, structure
one-for-one — the T4 lane's section list runs 情報 / セクション /
テキスト要素 / タブと表 / テキストブロック書式 / 画像とフロートボックス /
文書スタイル / メモ / 配色 / フォントスタイル / 脚注， each standing
where the original's section stood (candidate L605–1012). The
classifier's collapsed alignment labels only 2 TRANS-UNANCHORED
blocks for this whole surface; the translation mass is in diff.md
itself, and this section rests on the files and the T4 lane's
full-body check, not on the labels. Lorem ipsum sample text is kept
verbatim: it is the original's own filler.

**Why.** Pattern class P10 (translation; KB-50, KB-51). Failure
prevented: untranslated documentation makes the candidate unusable
as a JP theme page.

**Verify.** `sed -n '605,650p' candidate.txt` against original
L20–60; the heading sequence `grep -n '^++' candidate.txt` is JP
throughout.

**Disposition.** T4/T5 judged this theme FINDINGS jointly; the
translation-side findings are the credit field (section 1, since
repaired) and the link item (section 7). No mistranslation finding
stands. The (b) verdict is PASS.

## 7. Link targets (P11)

**What.** The body's functional links mostly name JP targets: the
anomaly-classification guide as a bare JP page name, the component
credits as bare same-site names, and the Wide Image Sizer /
BetterFootnotes / ACS links the T4 lane verified exist on scp-jp.
Two EN links stand. The intro prose links Basalt's wiki page and its
GitHub home (candidate L616): the GitHub home is the Basalt
project's own required reference, and no JP Basalt page is posted
yet for the wiki link to name (the T4 lane recorded this as an
observation, not a finding). The icon credit's link is different:
`[[[https://scp-wiki.wikidot.com/desk-of-junior-designer-s-yvonne|こちらを参照]]]`
(candidate L868) points at the EN article although a JP counterpart
of that page exists on scp-jp.

**Why.** Pattern class P11 (link targets; KB-54). Failure prevented:
a functional link left pointing at the origin branch sends JP
readers to the wrong wiki when a JP page exists to receive them.

**Verify.** `grep -n 'desk-of-junior-designer' candidate.txt`;
the T4 lane's pattern-11 evidence (LOCALIZE-S2-C section for this
theme) records the JP counterpart's existence (rev 0).

**Disposition.** The desk-of link is T4's pattern-11 FINDING for this
theme; no ledger line dispositions it. It is flagged in the
per-theme record (item 1). The Basalt links are as dispositioned
above.

## 8. Structural fidelity and exhibit census (P8, R3)

**What.** The exhibit census is preserved one-for-one (the T4 lane
verified the section sequence against the original): documentation
sections, twelve image-block exhibits, the font and colour samples,
the source-code collapsible, and the license tail all stand in the
original's order. The source exhibit's content now mirrors the
delivered module (section 3) — a form change forced by the delivery
reconstruction, not a census change. The two EXHIBIT-RESTRUCTURE
primaries resolve to the head mega-block (B1, the delivery
reconstruction) and the license conversion (B13).

**Why.** Pattern class P8 (structural fidelity; KB-42, KB-43).
Failure prevented: a silently dropped or reordered exhibit breaks
the theme's documentation contract with its readers.

**Verify.** Compare the section sequence:
`grep -n '^++' original.txt candidate.txt`.

**Disposition.** No ledger line charges the structure. The (b)
verdict is PASS.

## 9. Formatting-only changes (R4)

**What.** None. The classifier reports no whitespace-only block and
no re-indentation block for this pair (0 WS-ONLY firings across the
13 blocks). The size delta (+1,032 / −445) is content: the delivered
module copy of the CSS on the added side, and the original's head
imports and furniture on the removed side.

**Why.** Residue class R4 has no instance here; the ground is the
classifier's zero counts.

**Verify.** `grep -c 'WS-ONLY' classification.json` returns 0.

**Disposition.** Nothing to disposition.

## 10. Porter annotations (R2)

**What.** None. The candidate contains no `[!-- --]` porter comments
and no translator's notes (the T4 lane noted the same: no 訳注 used,
none needed). The box-drawing banner comments in the CSS are the
author's own, carried from the original.

**Why.** Residue class R2 has no instance here; the ground is the
grep below, run before writing this section.

**Verify.** `grep -c '\[!--' candidate.txt` returns 0.

**Disposition.** Nothing to disposition.

## 11. Dispositioned deviations (class (ii) / (iii) summary)

**What.** The deviations a reader of the diff might otherwise charge
against the candidate, with their dispositions:

- T1's findings (T1-ROWS row 161: exit 1, 8 errors / 1 warn) are
  hotlink ×6 — the three EN-hosted files of section 4 in their live
  and exhibit copies, in the standing class register c1 records —
  and pseudo-ref ×2 (the frame and license includes). Environment
  class (ii).
- The render check's items (RENDER-ROWS-2, EN20) are DISPOSITIONED
  in ledger part (c2): page-overflow 498–503px at 320/375 widths, in
  the recorded cross-cutting families (static credit replica fixed
  width at mobile widths, KB-33; preview chrome, KB-34), and the
  runtime-hotlink site-theme chain (KB-40, environment layer). One
  coverage caveat, carried verbatim from the row: the sample's T2
  run produced no machine verdict (exit 2, no summary), so the
  sample page's render state rests on the page-side run and the T3
  walk rather than a sample verdict.
- The pattern-4 and pattern-7 dispositions are sections 3–4.
- The draft-host form of the delivery URLs is environment class
  (iii) (KB-41).

**Why.** These classes exist so a reviewer does not re-litigate
environment properties as candidate defects; each item above names
its record so the disposition can be re-checked at its source.

**Verify.** The theme's rows in `review/AUTHORITIES/ledger-parts/`
(T1-ROWS row 161, RENDER-ROWS-2) and its blocks in
`GOSIGN2-LEDGER.md` parts (c2) and (c3).

**Disposition.** All items above are DISPOSITIONED in the cited
records. The items the records do not reach are the per-theme record
below.

## 12. Verification history

**What.** T1 (source check): FINDINGS (classified), 8 errors in the
standing classes — T1-ROWS row 161. T2/T3 (render check): FINDINGS
as dispositioned in section 11, with the sample-verdict caveat
noted there — RENDER-ROWS-2 (EN20). T4/T5 (localize check):
FINDINGS with 3 display-affecting items counted in LOCALIZE-ROWS
row 141; the lane's own verdict names patterns 4 and 5 as the
display-affecting pair (pattern 5 covering three files), with
pattern 3 (credit attribution) and pattern 11 (the EN-article link)
as further findings. Of those: pattern 4 is answered by the
f931619 repoint, pattern 3 by the credit field's current value,
pattern 5 stands under the T1 class, and pattern 11 stands open
(item 1). Ledger part (c3) records P4 DISPOSITIONED only. The T4
follow-up diff from revision 19 found no upstream changes. The (b)
verdict is PASS, with no OPEN items at the determination and no
FIX5 re-judgement.

**Why.** The verification section exists so the reader can see which
checks ran, what they found, and what became of each finding,
without re-running the campaign.

**Verify.** The cited rows and the LOCALIZE-S2-C section for this
theme in the campaign record; the stamp at the head of this file is
generated from the same records by `review/build_review.py`.

**Disposition.** Verdict: PASS (go-sign ledger part (b)), with the
flags below carried for the coordinator.

## Per-theme record: stellar-jp

**Item 1 — body link to the EN article although the JP page exists
(flag, not edited).** Candidate L868 links
`https://scp-wiki.wikidot.com/desk-of-junior-designer-s-yvonne` in
the icon credit. The T4 lane verified the JP counterpart exists on
scp-jp (rev 0) and charged the link as this theme's pattern-11
finding. No ledger line dispositions it, and the link stands in the
current bytes. The repair is a one-line repoint to the bare JP page
name, of the same shape as this candidate's other links; it belongs
to the coordinator's repair lane.

**Item 2 — the mono faces are named but loaded nowhere (minor
flag; wording corrected at REFRESH3-F).** The mono stack (candidate
L102, exhibit L1111) names JetBrains Mono and Noto Sans Mono CJK JP;
no `@import` or `@font-face` in the candidate or in basalt-jp loads
either. Two wording points corrected per `FIX-STELLAR.md` item 2(b):
the original's bytes name only `'Jetbrains Mono'` (original L520), so
the two-face stack with the CJK fallback is the port's own P7 rewrite,
not something the original had; and the author's `fonts.css`
(original L443), though it serves (probe 2026-11-17: 302 → 200,
`text/css`, 49,654 bytes), declares only three data-URI faces and no
mono face at all — it cannot be the source of a JetBrains load as
served today (whether an earlier revision was could not be verified).
The port dropped the personal-file hotlink and did not replace the
load; the documentation's font sample (candidate L991) still presents
JetBrains Mono as the theme's monospace font. T4 noted the gap without
a display-affecting mark, and the ledger's pattern-7 disposition covers
only the base-delivered Noto Sans JP. The landing `2dbb83d` restored the
load through the candidate's own Google Fonts route (see the
post-package repairs subsection below).

**Item 3 — pattern 5's files: disposition path and probe evidence
(record note).** T4 charged the three EN-hosted files as
display-affecting (pattern 5); ledger part (c3) names no P5 line
for this theme (unlike its sibling rows), but the same six
references are T1's hotlink×6, dispositioned in register c1 as
environment class (ii). Probes run once each on 2026-11-17: the
draft-host forms of the theme's own two files
(`…/local--files/theme%3Astellar-jp/stellar-theme-background.jpg`
and `…/Cream-SCP-icon.svg`) answer 404, while the original background
URL answers 302 to the files host — the pages render today, and the
end-state still requires the posting-time upload. The third file is
a component's logo (object-warning-box-source), whose JP hosting is
that component's own record, not this theme's.

**Item 4 — the (c3) disposition wording understates the repair
(record note).** Part (c3) dispositions pattern 4 as "delivery class
(ii): original-state CDN delivery". The bytes show the CDN imports
and frame values replaced by the basalt-jp delivery in commit
f931619 (a commit titled for colon-URL fixes; its diff for this file
is the repoint). As with Stargazer, this package follows the bytes:
the base dependency is a JP candidate now, not a waived EN one.

**Item 5 — classification collapse (method note).** The classifier
produced 13 blocks for a 1,477-line diff because the candidate's
interleaving defeats its alignment (the head mega-block B1 spans
original L2–420; B12 spans candidate L449–1458). The shares in the
class summary are exact for those blocks and unrepresentative of
the change mass; every line-level claim in this package was verified
against diff.md and the two files, and the two classifier labels
that would have misled a label-driven reading (the Rate false-fire
and the Restoration primary) are adjudicated in the class summary.

### Post-package repairs (REFRESH3-F)

**FIX-STELLAR, landing `2dbb83d` (report `R/review-scout/FIX-STELLAR.md`, item 2,
"theme:stellar-jp").** This landing postdates the package build
(`7170328`) and repairs items 1 and 2. Two candidate changes: (a) the
memo's icon-source link (candidate L868, now L869) repointed from
`https://scp-wiki.wikidot.com/desk-of-junior-designer-s-yvonne` to the
bare JP page form `[[[desk-of-junior-designer-s-yvonne|こちらを参照]]]` — the
`[[*user EstrellaYoshte]]` attribution beside it is untouched; the JP
target was verified by one probe (HTTP 200) and by the checker raising
no `link-target-missing`; (b) the mono load restored at candidate L26,
in the position the `fonts.css` line occupied in the original's import
order (third, after Orbitron/Roboto and Quantico) and in the candidate's
own Google Fonts form:
`@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap');`
— the load goes through the candidate's own route because the served
`fonts.css` declares no mono face (see item 2, wording corrected above);
'Noto Sans Mono CJK JP' is left as the stack's second entry, the JP
system-font name, with no load needed. Checker per the report: error 7 /
warn 1 / info 0 before and after, finding sets identical after
line-number normalization. This package documents the corrected
candidate; its stamp reads STALE against the pre-repair verdict, by
design.

## Change set

Delivered with this candidate in the canonical repository: the
candidate page itself (`pages/theme:stellar-jp.txt`), its decoration
sample (`pages/theme-decoration-sample-stellar-jp.txt`), and the
base candidate it layers over (`pages/theme:basalt-jp.txt`, with its
own package). The candidate's own history is three commits: the
Stage 2 EN20 integration, f931619, and FIX4-MECH.

## Appendix: residue resolution

The classifier left no blocks unlabeled for this pair (0 residue).
The appendix exists in this package to state that ground explicitly:
the adjudication burden for this theme sat not in residue but in the
collapsed alignment, handled in the class summary and item 5 above.

## License and attribution

- **Title:** Stellar Theme
- **Author:** GeminidStrix
- **Source:** https://scp-wiki.wikidot.com/theme:stellar — revision 19
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
