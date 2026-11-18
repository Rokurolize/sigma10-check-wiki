# theme:thalassophobia-jp — Thalassophobia theme (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:thalassophobia-jp — origin EN, population #145 [GOSIGN2-LEDGER (b) row 145]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 8ca33abcbe76bfd5bf9b5406027897cddbeccdfb9022a33c6c5d42669a207190); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 3 warns / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 130; GOSIGN2-LEDGER (b) row 145]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 322px@320 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 145, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 145]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 145]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:thalassophobia-jp.txt sha256:8ca33abcbe76bfd5bf9b5406027897cddbeccdfb9022a33c6c5d42669a207190; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

This file is the explanation record for one theme's Sigma-10 port. The
diff it explains is `diff.md` in this directory, generated from
`original.txt` (the frozen mirror) and `candidate.txt` (a byte copy of
the canonical candidate). The verdict stamp at the head of this file is generated; do not
edit inside the stamp markers.

## Provenance

- Theme: `theme:thalassophobia` on scp-wiki (EN branch), revision 19.
  Author Fish^12 — their first theme, as the page itself announces.
  A Black Highlighter layer with a deep-sea palette.
- Frozen mirror: `original.txt`, 393 lines, 10,841 bytes, SHA-256
  `f5c44eb35000433e50ef7525c934290f0e8bf261ee7a5a1832a12293f7fde86d`
  (matches `review/sources.tsv`; mirror-store class COPY).
- Candidate: `candidate.txt`, 420 lines, 12,858 bytes, SHA-256
  `a059f18be28245da700ba4877954eba928fff5c4f8b0668d62c63d1db6548a33`,
  byte-identical to the canonical file.
- Kind (sources.tsv): standard. Route: derived from the original at
  revision 19 (LOCALIZE-S2-C wave, EN21 batch). This theme is the
  plain Thalassophobia; its sibling `theme:thalassophobia-sigma-jp`
  is a separate Sigma-9 based theme with its own package.
- The candidate entered the canonical repository in the Stage 2 EN21
  integration (dda4fd3) and was touched once since, by the credit
  attribution normalization (1869877, FIX-CREDIT-D).

## Summary

A small BHL port with an unusually complete tail. The base arrives
the JP way (the BHL page include at the head, the JP project's CSS
files in the module and both frame slots), the EN credit furniture
(a bare rate and an author-label component pair) becomes one preview
credit block, the body and settings documentation are translated,
the font stacks gain Noto Sans JP and the import that loads it, and
the tail keeps the original's BHL component includes and priority-3
self frame, then adds three small SCP-JP correction modules, each
with its rationale in a comment. Two repairs hide in the CSS: a
missing semicolon that invalidated two of the original's variable
declarations is restored. The open items are the known ones: the
theme's three image files are repointed to the draft host but still
not uploaded (all three probed 404 today), and the usage exhibit
names the plain slug — the one finding in this batch's set that the
T4 lane counted display-affecting for this theme.

## Class summary (auto-classification)

66 change blocks: 39 specific (59.1%), 24 heuristic (36.4%),
3 residue (4.5%), 0 skipped. The generator counts +126 / −105 lines
(diff.md is Tier 1 format: 7 hunks). Label firings: TRANS-UNANCHORED
×22, TRANSLATION-ANCHORED ×19, INCLUDE-REPOINT ×6, WS-ONLY ×6,
DELIVERY-HOST ×5, DRAFT-HOST ×5, EXHIBIT-RESTRUCTURE ×6, COMMENT-TEXT
×3, CSS-BODY ×3, and single firings of IFTAGS, CREDIT-PREVIEW,
TASL-FIELDS, ESCAPED-INCLUDE, LINK-REPOINT, JPFONT-LOAD,
CONTENT-STRING, HEADERVAR, SELF-DELIVERY ×2, T7-CREDIT-CSS.

Adjudication notes: the six EXHIBIT-RESTRUCTURE primaries were
checked against the exhibit census — all six are include repoints
(the image-block and BHL component lines; their INCLUDE-REPOINT
spans are the whole change), and no exhibit was restructured. The
three CSS-BODY blocks are adjudicated individually in sections 4
and 8: two are font-stack rewrites (P7, whatever the label says)
and one is a semicolon repair. The T7-CREDIT-CSS firing (B66) marks
the tail correction modules of section 1.

## 0. Tag frame and page furniture

**What.** The candidate's head carries, before the gate, an
unconditional `[[iftags]]` block including the JP BHL theme page
(candidate L1–3, residue block B1 — an addition with no original
counterpart), the carried `.hl-*` highlight-colour module
(candidate L5–15), and then the gate `[[iftags +テーマ]]`
(candidate L16, block B2, IFTAGS) opening over the base module, the
two BHL frame slots (candidate L22–33), and the body. Its own frame
stands at the tail at priority 3 (candidate L402–405, section 3),
as the original's did. The original opens with the `.hl-*` module
and its gate, frames only itself at priority 3, and includes no BHL
page.

**Why.** Pattern class P1 (frame and tag furniture; KB-03, KB-04).
Failure prevented: a gate keyed to the EN tag name never opens on
scp-jp, and a BHL theme posted to JP without the base page include
misses the furniture the JP BHL page carries.

**Verify.** `grep -n 'iftags\|interwiki-style' candidate.txt` —
unconditional include block at L1–3, gate at L16 with the JP tag
name, own frame at the tail with priority 3.

**Disposition.** No ledger line charges the frame or the added
include block. The (b) verdict for this theme is PASS.

## 1. Credit block and license (P3, P9)

**What.** The original's credit furniture is a bare rate in a
right-aligned div (original L28–30, lowercase `[[module rate]]`)
and an author-label component pair
(`:scp-wiki:component:author-label-source`, original L31–34)
wrapping the author's intro line. Both are deleted (block B8's
region). The candidate carries one preview credit block (candidate
L32–41, block B8: CREDIT-PREVIEW, TASL-FIELDS) with eight fields:
title Thalassophobiaテーマ; translator of record AI; translation
year 2026; original title Thalassophobia Theme; copyright holder
`[[*user Fish^12]]`; creation year 2021; reference revision 19; and
a source link to `https://scp-wiki.wikidot.com/theme:thalassophobia`
— the host `review/sources.tsv` records, so the host check passes.
The author field agrees with the original's author-label component
(`name=Fish^12`) and its prose.

At the tail, after the frame, the candidate adds three small
correction modules (candidate L407–420, block B66, T7-CREDIT-CSS):
a page-history module keeping the history option row inside the
mobile viewport; a credit-dialogue module keeping the BHL credit
back-link on one line (the T7 credit CSS proper); and a top-bar
module keeping navigation labels whole at narrow widths. Each
carries an English comment stating its purpose and its SCP-JP
scope. They are platform corrections for the JP environment, of the
family the JP BHL candidates carry; none of them translates or
replaces original content.

**Why.** Pattern classes P3 (credit furniture swap; KB-16, KB-17)
and P9 (attribution; KB-47), with the tail modules under the T7
credit-CSS and platform-correction classes. Failure prevented: EN
credit components do not exist on scp-jp, a bare rate beside the
credit block renders a second rating widget, and the JP platform's
known BHL friction points (a credit dialogue whose back-link wraps,
a history row that overflows) recur on every page the theme styles
if the corrections are not carried with it.

**Verify.** `sed -n '32,41p' candidate.txt` against original
L28–34; `sed -n '407,420p' candidate.txt` for the three modules and
their comments; `grep -ci 'module rate' candidate.txt` returns 0.

**Disposition.** Ledger part (c3) records P3 credit fields FIXED for
this theme (credit waves, checker-verified), and T4's pattern-3 item
was a minor notation point on the source link. Neither side carries
a license box, so there is no P9 license-box conversion to record.
The (b) verdict is PASS.

## 2. Includes and component references (P2, P8)

**What.** INCLUDE-REPOINT fires 6 times. The BHL component includes
at the tail repoint `:scp-wiki:component:toggle-sidebar-bhl` and
`:scp-wiki:component:centered-header-bhl` → their `:scp-jp:` forms
(candidate L396–397, blocks B62 and B64). The image-block exhibits
repoint to `:scp-jp:component:image-block`. The usage exhibit
repoints `:scp-wiki:theme:thalassophobia` →
`:scp-jp:theme:thalassophobia` (candidate L125, block B27,
ESCAPED-INCLUDE) — see the flag below. The BHL page include
(section 0), the credit pair (section 1), and the frames
(section 3) complete the include census.

**Why.** Pattern classes P2 (include repoints; KB-05) and P8
(exhibit fidelity; KB-42, KB-43). Failure prevented: an exhibit or
live include pointing at the origin branch shows readers a page
that is not the one this candidate installs.

**Verify.** `grep -n 'scp-wiki:' candidate.txt` returns nothing;
`grep -n 'include' candidate.txt` lists the full census.

**Disposition.** One flag rides on this section: the usage exhibit
names the plain slug `:scp-jp:theme:thalassophobia`, where the
posting name is `theme:thalassophobia-jp`. T4 charged it for this
theme as a display-affecting slug error (LOCALIZE-ROWS row 145);
it belongs to the population sweep family and is flagged in the
per-theme record (item 1), not edited here.

## 3. Delivery topology (P4)

**What.** The original delivers the BHL base by module imports from
the EN project's GitHub Pages (original L13–16) and its own layer by
a tail module importing its code from the EN files host
(`https://scp-wiki.wdfiles.com/local--code/theme%3Athalassophobia/1`,
original L387–389), framed at priority 3. The candidate repoints
the base to the JP project's files (`scp-jp.github.io/Black-Highlighter/css/min/…`)
in the module inside the gate (candidate L17–20, block B3,
DELIVERY-HOST) and in the priority-1/2 frame slots (candidate
L22–33), adds the BHL page include at the head (section 0), and
repoints its own delivery to the draft host: tail module importing
`local--code/theme%3Athalassophobia-jp/1` (candidate L398–401,
block B63) with the priority-3 frame naming the same URL (candidate
L402–405, block B65). DELIVERY-HOST fires 5 times, DRAFT-HOST 5,
SELF-DELIVERY 2. The code exhibit (original L181–380 → candidate
L193–392) remains the delivery's source on both sides.

**Why.** Pattern class P4 (delivery topology; KB-23). Failure
prevented: a base imported from the EN project's Pages is the EN
BHL build, not the JP port the JP site runs beside; and an own
delivery left on the origin files host is outside the port's
control.

**Verify.** `sed -n '17,20p' candidate.txt` and
`sed -n '398,405p' candidate.txt`;
`grep -n 'nu-scptheme\|scp-wiki.wdfiles' candidate.txt` returns
nothing.

**Disposition.** No ledger line charges the topology. The draft-host
form of the delivery URLs is environment class (iii) (KB-41). The
(b) verdict is PASS.

## 4. Fonts and assets (P5, P7)

**What.** Fonts. The exhibit's import is widened to load the JP
face with the theme's own: candidate L202 imports Anonymous Pro,
Miriam Libre, and Noto Sans JP from Google Fonts in one URL (block
B48, JPFONT-LOAD). The stacks follow (blocks B58, B59 — labeled
CSS-BODY, adjudicated here as the P7 rewrites they are):
`--body-font: 'Miriam Libre', sans-serif` →
`'Miriam Libre', 'Noto Sans JP', sans-serif` (candidate L261), and
`--mono-font: 'Anonymous Pro', monospace` →
`'Anonymous Pro', 'Noto Sans JP', monospace` (candidate L264).
Every family the stacks name is loaded by that import or by the
base.

Assets. The theme's three image files are repointed from the EN
files host to the draft host under the candidate's own folder: the
body image `thalassophobiaimage.png` (candidate L108, block B24),
the background gradient `thalassophobiagradient.png` (candidate
L249, block B55), and the header logo `thalassophobiaheader.svg`
(candidate L257, block B57, HEADERVAR). All three were T4's
pattern-5 charge: at check time they answered 404 on the draft
host, so the body image, the background gradient, and the header
logo did not render. Probed again once each on 2026-11-17, all
three still answer 404.

**Why.** Pattern classes P7 (font stacks; KB-35, KB-36) and P5
(assets; KB-25, KB-26). Failure prevented: a stack naming the branch
serif renders JP text in an unloaded font; and an asset repoint
without the upload is a broken image — the repoint and the upload
are two halves of one step, and only the first half is in the
candidate's gift.

**Verify.** `sed -n '201,202p' candidate.txt`;
`grep -n 'sigma10-jp-test.wdfiles' candidate.txt` lists the three
asset references (plus the delivery, section 3); the probes above
can be re-run with one `curl -sI` per file.

**Disposition.** The font changes are uncharged. The assets are
DISPOSITIONED in part (c3) as class (ii) / KB-58 (deferred hosting),
with T4's rider that resolution by upload at go-sign needs staff
confirmation. The fresh probes are recorded in the per-theme record
(item 2): the upload half is still outstanding. The (b) verdict is
PASS.

## 5. Header, titles and rendered strings (P6)

**What.** The theme's rendered strings live in its variable block:
`--theme-name: "Thalassophobiaテーマ"` (candidate L255, block B56,
CONTENT-STRING; the companion `--theme-id` keeps its machine value
`thalassophobia`), and the header logo variable of section 4
(block B57, HEADERVAR). The theme sets no `--header-title` text of
its own; the masthead text comes from the BHL base, whose JP form
the candidate now loads (section 3).

**Why.** Pattern class P6 (header and rendered strings; KB-29,
KB-30, KB-31). Failure prevented: a theme-name string left in EN is
the name the JP site's theme machinery displays.

**Verify.** `grep -n 'theme-name\|theme-id' candidate.txt`.

**Disposition.** No ledger line charges the header for this theme.
The (b) verdict is PASS.

## 6. Body translation (P10)

**What.** The documentation body is translated throughout: 19
TRANSLATION-ANCHORED blocks and 22 TRANS-UNANCHORED blocks (counted
class treatment, per the class-M convention) covering the intro
prose, the word-list and settings documentation, and the exhibit
captions. The three residue blocks are single translation lines of
the same surface: a word-list entry (`//noun//` → `//名詞//`, B11)
and a settings-table value (`| subcolor4-name=Black` → `黒`, B21),
resolved in the appendix. The CSS comments inside the exhibit
cross with the CSS (COMMENT-TEXT ×3, riding on translation blocks
in the exhibit's head region).

**Why.** Pattern class P10 (translation; KB-50, KB-51). Failure
prevented: untranslated documentation makes the candidate unusable
as a JP theme page.

**Verify.** Spot-check any anchored block against diff.md (e.g.
B38–B39, the settings tables); `sed -n '43p' candidate.txt` shows
the intro prose translated, with the author's page link carried.

**Disposition.** T4/T5 judged this theme FINDINGS jointly; the
translation-side charges are the asset and slug items of sections 2
and 4. The (b) verdict is PASS.

## 7. Link targets (P11)

**What.** LINK-REPOINT fires once (block B28): a documentation link
repointed to its JP form. The author's page link in the intro prose
(`[https://scp-wiki.wikidot.com/hotfish|著者ページ]`, candidate L43)
is carried from the original: it is the author's own hub page on
the EN wiki, an attribution reference with no JP counterpart, and
it was not charged. The credit source link names the recorded host
(section 1).

**Why.** Pattern class P11 (link targets; KB-54). Failure prevented:
a functional link left pointing at the origin branch sends JP
readers to the wrong wiki; attribution links to an author's own
page are the class's standing exception.

**Verify.** `grep -n 'hotfish' candidate.txt` — one hit, the intro
prose.

**Disposition.** No ledger line charges a link target for this
theme.

## 8. Structural fidelity and exhibit census (P8, R3)

**What.** The exhibit census is preserved: intro, usage exhibit,
body image exhibit, word lists, settings tables, source exhibit,
and the tail furniture all stand in the original's order. One
repair hides in the source exhibit (block B61, labeled CSS-BODY):
the original's line 300 runs two variable declarations together
without the separating semicolon
(`--search-textbox-text-color: var(--sky-blue) --login-line-divider-color: var(--light-bronze);`),
which makes the whole declaration invalid — a CSS parser drops it,
so neither variable is set by that line in the original. The
candidate inserts the missing semicolon (candidate L312), and both
variables now take effect. No other rule changes.

**Why.** Pattern class P8 (structural fidelity; KB-42, KB-43). A
port is expected to carry the original's behaviour, and where the
original's text is invalid as written, the faithful act is the
minimal repair that makes the author's evident intent parse —
recorded here so it is not mistaken for drift. (The same batch's
telecom package records the mirror-image case: an unclosed block
repaired by an added brace.)

**Verify.** `sed -n '300p' original.txt` against
`sed -n '312p' candidate.txt`.

**Disposition.** No ledger line charges the structure or the
repair. The (b) verdict is PASS.

## 9. Formatting-only changes (R4)

**What.** Six WS-ONLY blocks (B49–B54), all single lines inside the
source exhibit: whitespace-only adjustments on variable lines in
the exhibit's first half (original L210–232 → candidate L222–244).
The classifier reports 0 reindent blocks. Nothing else in the pair
is formatting-only.

**Why.** Residue class R4 (formatting-only). The ground is the
classifier's count plus the blocks' positions inside carried CSS,
where no declaration changes.

**Verify.** Blocks B49–B54 in classification.json.

**Disposition.** Nothing to disposition.

## 10. Porter annotations (R2)

**What.** Three annotations, all in CSS comments at the head of the
tail correction modules (candidate L408, L413, L418 region): the
history-row, credit-dialogue, and top-bar rationales of section 1.
They are written in English, addressed to maintainers, and each
names its SCP-JP scope and the behaviour it keeps. The candidate
contains no `[!-- --]` comments.

**Why.** Residue class R2 (porter annotations). These three are
load-bearing: the correction modules are meaningless without the
statement of what they correct.

**Verify.** `sed -n '407,420p' candidate.txt`;
`grep -c '\[!--' candidate.txt` returns 0.

**Disposition.** No ledger line charges the annotations.

## 11. Dispositioned deviations (class (ii) / (iii) summary)

**What.** The deviations a reader of the diff might otherwise charge
against the candidate, with their dispositions:

- T1's findings (T1-ROWS row 130: exit 1, 4 errors / 3 warns / 1
  info) are pseudo-ref ×4 only — the frame, credit, and BHL
  component includes whose targets exist when the theme is
  installed. Environment class (ii), shared with the whole
  population; notably, this candidate has no hotlink or old-bhl
  findings at all.
- The render check's items (RENDER-ROWS-2, EN21) are DISPOSITIONED
  in ledger part (c2): page-overflow 322px at 320 width, in the
  recorded cross-cutting families (static credit replica fixed
  width at mobile widths, KB-33; preview chrome, KB-34), and the
  runtime-hotlink site-theme chain (KB-40, environment layer). One
  coverage caveat, carried from the row: the sample's T2 run
  produced no machine verdict (exit 2, no summary), so the sample
  rests on the page-side run and the T3 walk.
- The asset references are class (ii) / KB-58 (section 4).
- The draft-host form of the delivery URLs is environment class
  (iii) (KB-41).

**Why.** These classes exist so a reviewer does not re-litigate
environment properties as candidate defects; each item above names
its record so the disposition can be re-checked at its source.

**Verify.** The theme's rows in `review/AUTHORITIES/ledger-parts/`
(T1-ROWS row 130, RENDER-ROWS-2) and its blocks in
`GOSIGN2-LEDGER.md` parts (c2) and (c3).

**Disposition.** All items above are DISPOSITIONED in the cited
records. The two items carried forward are the per-theme record
below.

## 12. Verification history

**What.** T1 (source check): FINDINGS (classified), 4 errors all
pseudo-ref — T1-ROWS row 130. T2/T3 (render check): FINDINGS as
dispositioned in section 11, with the sample-verdict caveat noted
there — RENDER-ROWS-2 (EN21). T4/T5 (localize check): FINDINGS with
2 display-affecting items — pattern 5 (the three draft-host assets
answering 404) and the usage sample's slug error — plus a minor
pattern-3 notation point — LOCALIZE-ROWS row 145 (LOCALIZE-S2-C).
Ledger part (c3) records P3 FIXED and P5 DISPOSITIONED. The
campaign's interwiki-priority appendix records this theme at
priority 3 (BHL order), matching the frame the candidate carries.
The (b) verdict is PASS, with no OPEN items at the determination
and no FIX5 re-judgement.

**Why.** The verification section exists so the reader can see which
checks ran, what they found, and what became of each finding,
without re-running the campaign.

**Verify.** The cited rows; the stamp at the head of this file is
generated from the same records by `review/build_review.py`.

**Disposition.** Verdict: PASS (go-sign ledger part (b)), with the
two items below carried for the coordinator.

## Per-theme record: thalassophobia-jp

**Item 1 — usage exhibit names a plain-slug page (sweep family;
charged display-affecting for this theme).** Candidate L125:
`@@[[include :scp-jp:theme:thalassophobia]]@@`. The posting name is
`theme:thalassophobia-jp`; the snippet names a page that will not
exist. T4 charged this instance as display-affecting (LOCALIZE-ROWS
row 145), one step stronger than the family's usual notation,
because the snippet is the theme's only install instruction.
Flagged for the population sweep; not edited.

**Item 2 — the three asset files are still unhosted (probe
evidence under the KB-58 disposition).** The repoints are done
(candidate L108, L249, L257, all under
`local--files/theme%3Athalassophobia-jp/` on the draft host); the
uploads are not. Probes run once each on 2026-11-17:
`thalassophobiaimage.png` 404, `thalassophobiagradient.png` 404,
`thalassophobiaheader.svg` 404 — the same state T4 recorded, so the
body image, background gradient, and header logo still do not
render from the JP side. T4's rider stands: resolution by upload
needs staff confirmation. Recorded so the reflection step treats
the uploads as outstanding work, not as a completed half of the
disposition.

## Change set

Delivered with this candidate in the canonical repository: the
candidate page itself (`pages/theme:thalassophobia-jp.txt`) and its
decoration sample
(`pages/theme-decoration-sample-thalassophobia-jp.txt`). The
candidate's own history is two commits: the Stage 2 EN21 integration
and the FIX-CREDIT-D normalization.

## Appendix: residue resolution

The classifier left 3 blocks unlabeled (4.5%). Per the class-M
convention they are resolved here by shape, one row per block.

| Block | Lines (orig → cand) | Resolution |
|---|---|---|
| B1 | (added) → 1–4 | The added head furniture: the unconditional BHL page-include block (candidate L1–3) and the carried `.hl-*` module's opening (section 0, P1). |
| B11 | 45 → 54 | Word-list exhibit entry translated: `//noun//` → `//名詞//` (section 6, P10). |
| B21 | 81 → 90 | Settings-table value translated: `\| subcolor4-name=Black` → `黒` (section 6, P10). |

## License and attribution

- **Title:** Thalassophobia Theme
- **Author:** Fish^12
- **Source:** https://scp-wiki.wikidot.com/theme:thalassophobia — revision 19
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
