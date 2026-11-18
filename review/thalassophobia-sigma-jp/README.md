# theme:thalassophobia-sigma-jp — Thalassophobia theme, Sigma-9 variant (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:thalassophobia-sigma-jp — origin EN, population #146 [GOSIGN2-LEDGER (b) row 146]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4c00c5e4b41b1219d532b8950d9ffc8bd2bce880b3285c3f4d0f90e378a11f6c); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 3 warns / 1 info (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 131; GOSIGN2-LEDGER (b) row 146]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-* cluster + sidebar-unreachable confined to chromium-375, whose only hotlink host is http.cat = transient 503 capture, not a result; page runtime-hotlink site-theme chain otherwise; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 146, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 146]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 146]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:thalassophobia-sigma-jp.txt sha256:4c00c5e4b41b1219d532b8950d9ffc8bd2bce880b3285c3f4d0f90e378a11f6c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

This file is the explanation record for one theme's Sigma-10 port. The
diff it explains is `diff.md` in this directory, generated from
`original.txt` (the frozen mirror) and `candidate.txt` (a byte copy of
the canonical candidate). The verdict stamp at the head of this file is generated; do not
edit inside the stamp markers.

## Provenance

- Theme: `theme:thalassophobia-sigma` on scp-wiki (EN branch),
  revision 56. Author TheDarkArtist. This is the Sigma-9 based
  variant of the Thalassophobia theme — a different theme from
  `theme:thalassophobia` (Fish^12's BHL layer, the sibling package
  in this batch), sharing the name and the deep-sea subject but not
  the author, the base, or the CSS.
- Frozen mirror: `original.txt`, 767 lines, 17,465 bytes, SHA-256
  `0eae64dffdda6fb31596e95b48fcd80cdf98eec2b7b49ad91be990a5bed72d30`
  (matches `review/sources.tsv`; mirror-store class COPY).
- Candidate: `candidate.txt`, 803 lines, 21,607 bytes, SHA-256
  `64d73032e83eea9bfa280ff3e45631fc153b44efc237e3630730bdd5efd583e5`,
  byte-identical to the canonical file.
- Kind (sources.tsv): standard. Route: derived from the original at
  revision 56 (LOCALIZE-S2-C wave, EN21 batch).
- The candidate entered the canonical repository in the Stage 2 EN21
  integration (dda4fd3) and was touched once since, by the pattern-4
  repoint wave (f1138e4, FIX-P4).

## Summary

The heaviest documentation port in this batch's tail: a Sigma-9
theme with a long settings manual, a large CSS exhibit, and three
selectable variant modules (the copper and gradient variants ship as
extra `[[module CSS]]` blocks a user enables). The port translates
the manual in full, converts the credit furniture (a centred bare
rate and an author-label pair) into a preview credit block, adds
Noto Sans JP to every font stack with the import that loads it,
extends the sidebar rules to the interwiki sidebar throughout the
CSS (the JP environment's frame element), repoints the theme's six
image files and the variant gradients to the draft host, frames its
own second code delivery at priority 3, and appends a credit-module
correction whose comment explains, in unusual and welcome detail,
exactly which JP DOM difference it retargets. T4's only charge was a
minor link item. The open items are the family's usual ones: the six
repointed files still answer 404 on the draft host (uncharged by
T4, recorded here with fresh probes), and the usage exhibit names
the plain slug.

## Class summary (auto-classification)

86 change blocks: 27 specific (31.4%), 56 heuristic (65.1%),
3 residue (3.5%), 0 skipped. The generator counts +200 / −165 lines
(diff.md is Tier 1 format: 18 hunks). Label firings: TRANS-UNANCHORED
×38, TRANSLATION-ANCHORED ×19, CSS-BODY ×19, DRAFT-HOST ×8,
HEADERVAR ×3, EXHIBIT-RESTRUCTURE ×2, INCLUDE-REPOINT ×2,
DELIVERY-MOVE ×2, SELF-DELIVERY ×2, and single firings of
CREDIT-PREVIEW, TASL-FIELDS, IFTAGS, ESCAPED-INCLUDE, COMMENT-TEXT,
JPFONT-LOAD, DELIVERY-HOST, T7-CREDIT-CSS.

Adjudication notes: the heuristic share is this batch's highest,
and it is honest mass — the settings manual's translation blocks
plus the CSS-BODY lines. The 19 CSS-BODY blocks were sampled across
the exhibit and all three variant modules and resolve into three
shapes, narrated where they belong: font-stack rewrites gaining
Noto Sans JP (section 4, P7 — e.g. block B59's four stacks at
candidate L266–270), `#interwiki` selector extensions (section 8 —
e.g. candidate L327, L338, L534, where sidebar rules gain the
interwiki counterparts), and asset repoints inside variant modules
(section 4 — e.g. the gradient at candidate L649). Both
EXHIBIT-RESTRUCTURE primaries are include repoints against the
census (B1's head furniture and B69's delivery include region); no
exhibit was restructured. The two classifier "moves" (similarity
0.667) are the header-variable snippet exhibit and the delivery
module trading places in its alignment; the files' actual layout is
unchanged in that respect (sections 3, 8).

## 0. Tag frame and page furniture

**What.** The candidate opens with the gate
(`[[iftags +テーマ]]`, candidate L1, block B1, IFTAGS) over the
credit block and body, and frames its own delivery at the tail: an
interwiki-style include at priority 3 naming
`local--code/theme%3Athalassophobia-sigma-jp/2` on the draft host
(candidate L790–793, block B86) — the page's second code delivery,
which carries the variant set. The original opens with the same
gate form (`+theme`) and frames its own delivery at the tail
likewise; the Sigma family's priority for the theme's own frame is
3 in both.

**Why.** Pattern class P1 (frame and tag furniture; KB-03, KB-04).
Failure prevented: a gate keyed to the EN tag name never opens on
scp-jp, and a multi-code-block theme whose frame names the wrong
delivery applies the base layer without its variants.

**Verify.** `grep -n 'iftags\|interwiki-style' candidate.txt` —
gate at L1 with the JP tag name; one frame at the tail, priority 3,
naming the `/2` delivery.

**Disposition.** No ledger line charges the frame. The (b) verdict
for this theme is PASS.

## 1. Credit block and license (P3, P9)

**What.** The original's credit furniture is a bare rate centred in
a `[[=]]` block (original L2–4) and an author-label component pair
(`:scp-wiki:component:author-label-source`, `name=TheDarkArtist`,
original L5–9) wrapping a "Lorem ipsum" line. Both are deleted
(block B1's region). The candidate carries one preview credit block
(candidate L2–11, block B1: CREDIT-PREVIEW, TASL-FIELDS) with eight
fields: title Thalassophobiaテーマ（Sigma-9）; translator of record
AI; translation year 2026; original title Thalassophobia Theme
(Sigma-9); copyright holder `[[*user TheDarkArtist]]`; creation
year 2022; reference revision 56; and a source link to
`https://scp-wiki.wikidot.com/theme:thalassophobia-sigma` — the
host `review/sources.tsv` records, so the host check passes. The
author field agrees with the original's author-label component.

At the tail the candidate appends the credit-module correction
(candidate L796–802, block B86, T7-CREDIT-CSS): a module retargeting
the theme's credit-button anchor rule from the EN credit module's
`<p>`-wrapped structure to the JP module's direct-child structure,
with the EN declarations unchanged. Its comment (candidate L797)
states the DOM difference and the reasoning in full — the model
form of a T7 supplement, since a reader can verify the claim
against both modules.

**Why.** Pattern classes P3 (credit furniture swap; KB-16, KB-17)
and P9 (attribution; KB-47), with the tail module under T7 (credit
CSS supplements). Failure prevented: EN credit components do not
exist on scp-jp, a bare rate beside the credit block renders a
second rating widget, and a credit-button rule written against the
EN module's DOM silently never matches on JP — the supplement
exists because the theme's gold credit anchor would otherwise lose
its styling.

**Verify.** `sed -n '2,11p' candidate.txt` against original L1–9;
`sed -n '796,802p' candidate.txt` for the supplement and its
comment; `grep -ci 'module rate' candidate.txt` returns 0.

**Disposition.** T4 verified this theme's credit at 8/8 fields with
no live duplicate rate, and ledger part (c3) records no credit line
for the theme (its only line is P11). Neither side carries a
license box, so there is no P9 license-box conversion to record.
The (b) verdict is PASS.

## 2. Includes and component references (P2, P8)

**What.** INCLUDE-REPOINT fires twice: the usage exhibit
(`@@[[include :scp-jp:theme:thalassophobia-sigma]]@@`, candidate
L57, block B10, ESCAPED-INCLUDE) and a documentation include in the
delivery region (block B69). The frame and credit includes are
sections 0 and 1. No live include names a foreign prefix.

**Why.** Pattern classes P2 (include repoints; KB-05) and P8
(exhibit fidelity; KB-42, KB-43). Failure prevented: an exhibit
pointing at the origin branch shows readers a page that is not the
one this candidate installs.

**Verify.** `grep -n 'scp-wiki:' candidate.txt` returns nothing;
`grep -n 'include' candidate.txt` lists the census.

**Disposition.** One flag rides on this section, of the sweep
family: the usage exhibit names the plain slug
`:scp-jp:theme:thalassophobia-sigma`, where the posting name is
`theme:thalassophobia-sigma-jp` (candidate L57; per-theme record,
item 1). T4 did not charge it for this theme; the sweep owns the
family's repair and the candidate is not edited here.

## 3. Delivery topology (P4)

**What.** The original's layout: a CSS exhibit (original L234–553)
as the base layer's source, a self-delivery module (original
L562–565), and three variant modules (original L569–617, L624–676,
L681–765) carrying the selectable variants inline. The candidate
preserves the topology one-for-one: exhibit (candidate L247–575),
self-delivery module repointed to the draft host (candidate
L584–587, block B70: DELIVERY-HOST, DELIVERY-MOVE, SELF-DELIVERY),
three variant modules (candidate L592–639, L647–698, L704–787), the
priority-3 frame naming the `/2` delivery (section 0), and the T7
module (section 1). DRAFT-HOST fires 8 times across the delivery
and asset references. The FIX-P4 wave's touch on this file was in
this surface (the base-delivery repoint family); the current import
and frame values are the JP forms shown above.

**Why.** Pattern class P4 (delivery topology; KB-23). Failure
prevented: a variant theme whose modules are reordered or merged
changes which cascade a user gets when they enable a variant; the
port's job is to keep the selection mechanism identical and change
only where the files live.

**Verify.** `grep -n 'module CSS' candidate.txt` lists the exhibit
snippet module and the five tail modules in order;
`sed -n '584,587p' candidate.txt` shows the self-delivery import.

**Disposition.** No ledger line charges the topology. The draft-host
form of the delivery URLs is environment class (iii) (KB-41). The
(b) verdict is PASS.

## 4. Fonts and assets (P5, P7)

**What.** Fonts. The exhibit's head import is widened to load Noto
Sans JP with the theme's faces (block B57, JPFONT-LOAD), and the
stacks follow in a block the classifier labels CSS-BODY (B59,
candidate L266–270): `--body-font: 'Roboto', 'Noto Sans JP', sans-serif`,
`--header-font` and `--title-font: 'Josefin Sans', 'Noto Sans JP', sans-serif`,
`--mono-font: 'Fira Code', 'Noto Sans JP', monospace`. Per the
standing adjudication rule these are P7 font-stack rewrites,
narrated as such. Every named family is loaded by the import or the
base.

Assets. Six image files are repointed to the draft host under the
candidate's own folder: `image.png`, `logo.svg`, `gradient.png`,
`gradient-red.png`, `copperlinks.png`, `coppermode.png` (references
at candidate L39–40, L78–79, L87–88 in the body exhibits, L261 and
L293 in the CSS, and L649 in a variant module — DRAFT-HOST ×8).
The variant gradient's original reference names the author's own
sandbox (`waltz-sandbox.wdfiles.com/local--files/thasalophobia-sigma/gradient-red`,
original L627 — the folder name is the author's misspelling, sic),
so the repoint also retires a personal-sandbox dependency. Probed
once each on 2026-11-17, all six files answer 404 on the draft
host.

**Why.** Pattern classes P7 (font stacks; KB-35, KB-36) and P5
(assets; KB-25, KB-26). Failure prevented: stacks naming no JP face
render JP text in fallback fonts; assets left on a personal sandbox
are outside the port's control, and assets repointed but not
uploaded are broken images until the upload half lands.

**Verify.** `sed -n '257,270p' candidate.txt`;
`grep -o 'local--files/theme%3Athalassophobia-sigma-jp/[A-Za-z0-9_.-]*' candidate.txt | sort -u`
lists the six files; the probes above can be re-run with one
`curl -sI` per file.

**Disposition.** The font changes are uncharged. The assets were
not charged by T4 either (its row records the page dependencies as
existing on scp-jp and charges only the link item); they stand
under the deferred-hosting class (KB-58) as a family, and the fresh
probe state is recorded in the per-theme record (item 2). The (b)
verdict is PASS.

## 5. Header, titles and rendered strings (P6)

**What.** HEADERVAR fires 3 times. The header-variable snippet
exhibit in the manual (original L68–71 → candidate L70–73, block
B13) is translated with the manual. In the variant modules, the
fictional masthead titles are translated as content: the red
variant's `--header-title: "ABYSSAL AREA-7"` →
`"深淵エリア-7"` (candidate L706, block B85). These are the theme's
in-fiction area names, carried as rendered strings; the base
Sigma-9 masthead text itself comes from the base delivery, not from
this layer.

**Why.** Pattern class P6 (header and rendered strings; KB-29,
KB-30, KB-31). Failure prevented: a variant that switches the
masthead to an EN fictional name on a JP page breaks the fiction's
consistency the variant exists to create.

**Verify.** `grep -n 'header-title' candidate.txt` — the JP forms
in the variant modules and the snippet exhibit.

**Disposition.** No ledger line charges the header for this theme.
The (b) verdict is PASS.

## 6. Body translation (P10)

**What.** The settings manual is translated in full: 19
TRANSLATION-ANCHORED blocks and 38 TRANS-UNANCHORED blocks (counted
class treatment, per the class-M convention) covering the intro,
the formatting and layout exhibits, the colour and component
documentation, and the variant instructions. The three residue
blocks are manual lines of the same surface — a section heading
(`+ Formatting Examples` → `+ 書式例`, B16) and two exhibit
sentences whose code tokens dominate the line (the `darkbox` and
`lightbox` div explanations, B49 and B50, their prose translated
and their punctuation converted) — resolved in the appendix. The
CSS comments inside the exhibit cross with the CSS (COMMENT-TEXT
×1 rides on an exhibit-head translation block).

**Why.** Pattern class P10 (translation; KB-50, KB-51). Failure
prevented: an untranslated settings manual makes a
variant-heavy theme unusable — the variants are enabled by
following the manual, so the manual is the mechanism.

**Verify.** Spot-check any anchored block against diff.md (e.g.
B36–B41, the component documentation); T4's row records no
untranslated or garbled prose for this theme.

**Disposition.** T4/T5 judged this theme FINDINGS jointly, on the
link item of section 7 only. The (b) verdict is PASS.

## 7. Link targets (P11)

**What.** T4's only charge against this theme: the link-syntax
sample in the manual keeps its EN target —
`[https://scp-wiki.wikidot.com A link you have probably visited]`
(candidate L104, its caption translated to
おそらく訪問済みのリンク). The line is a syntax exhibit: it
demonstrates how a visited link renders, and its target is the EN
front page as sample content. The remaining links name JP targets
or the recorded source (section 1).

**Why.** Pattern class P11 (link targets; KB-54). The lane charged
it because a reader copying the sample copies an EN target; the
counterweight is that the sample's subject is link rendering, not
navigation.

**Verify.** `sed -n '104p' candidate.txt` against original L102.

**Disposition.** Part (c3) dispositions P11 for this theme under
the sibling / batch-posting class. The line stands under that
disposition; it is recorded here because it is the theme's only T4
charge and a reader of the diff will meet it.

## 8. Structural fidelity and exhibit census (P8, R3)

**What.** The census is preserved: manual sections in order, the
CSS exhibit, the self-delivery module, and the three variant
modules in their original order (section 3's map). One systematic
CSS adaptation runs through the exhibit and variants: the sidebar
selector lists gain their `#interwiki` counterparts
(`#side-bar a` → `#side-bar a, #interwiki a`, candidate L327;
the hover list at L338; `div#side-bar` → `div#side-bar, #interwiki`,
L534; the same in the variant modules, e.g. L595). The JP
environment renders the interwiki sidebar as a sibling element the
EN theme never had to style; without the extension the theme's
sidebar styling silently skips it. These are the plurality of the
CSS-BODY blocks (section: class summary), and they are additions,
not rewrites: every original selector survives, extended.

**Why.** Pattern class P8 (structural fidelity; KB-42, KB-43). The
fidelity question for an adaptation is whether the original's
behaviour survives intact; here it does, with the JP frame element
brought inside the same rules rather than restyled separately.

**Verify.** `grep -n '#interwiki' candidate.txt` lists the extended
rules; `grep -c '#interwiki' original.txt` returns 0.

**Disposition.** No ledger line charges the structure or the
adaptation. The (b) verdict is PASS.

## 9. Formatting-only changes (R4)

**What.** None. The classifier reports no whitespace-only block and
no re-indentation block for this pair. The size delta (+200 / −165)
is content: translations, the JP stack and selector additions, and
the tail supplement.

**Why.** Residue class R4 has no instance here; the ground is the
classifier's zero counts for both signatures across 86 blocks.

**Verify.** `grep -c 'WS-ONLY' classification.json` returns 0.

**Disposition.** Nothing to disposition.

## 10. Porter annotations (R2)

**What.** One annotation, and it is the batch's most thorough: the
T7 module's comment (candidate L797), a three-sentence explanation
of the EN and JP credit modules' DOM difference and why the rule
was retargeted with its declarations unchanged (section 1). The
candidate contains no `[!-- --]` comments.

**Why.** Residue class R2 (porter annotations). This one is the
supplement's audit trail: without it, the retargeted selector reads
as a gratuitous change to a working rule.

**Verify.** `sed -n '797p' candidate.txt`;
`grep -c '\[!--' candidate.txt` returns 0.

**Disposition.** No ledger line charges the annotation.

## 11. Dispositioned deviations (class (ii) / (iii) summary)

**What.** The deviations a reader of the diff might otherwise charge
against the candidate, with their dispositions:

- T1's findings (T1-ROWS row 131: exit 1, 7 errors / 3 warns / 1
  info) are pseudo-ref ×7 only — the credit, frame, and component
  includes whose targets exist when the theme is installed.
  Environment class (ii); no hotlink or old-bhl findings.
- The render check's items (RENDER-ROWS-2, EN21) are DISPOSITIONED
  in ledger part (c2): the page's hidden-* cluster and
  sidebar-unreachable state confined to chromium-375, whose only
  hotlink host was http.cat — a transient Wikidot 503 capture, not
  a result (KB-44); the runtime-hotlink site-theme chain otherwise
  (KB-40, environment layer). One coverage caveat, carried from the
  row: the sample's T2 run produced no machine verdict (exit 2, no
  summary), so the sample rests on the page-side run and the T3
  walk.
- The link item is dispositioned in (c3) (section 7); the asset
  references stand under the deferred-hosting class (section 4).
- The draft-host form of the delivery URLs is environment class
  (iii) (KB-41).

**Why.** These classes exist so a reviewer does not re-litigate
environment properties as candidate defects; each item above names
its record so the disposition can be re-checked at its source.

**Verify.** The theme's rows in `review/AUTHORITIES/ledger-parts/`
(T1-ROWS row 131, RENDER-ROWS-2) and its blocks in
`GOSIGN2-LEDGER.md` parts (c2) and (c3).

**Disposition.** All items above are DISPOSITIONED in the cited
records. The two items carried forward are the per-theme record
below.

## 12. Verification history

**What.** T1 (source check): FINDINGS (classified), 7 errors all
pseudo-ref — T1-ROWS row 131. T2/T3 (render check): FINDINGS as
dispositioned in section 11, with the sample-verdict caveat noted
there — RENDER-ROWS-2 (EN21). T4/T5 (localize check): FINDINGS with
1 display-affecting item counted in LOCALIZE-ROWS row 146; the
row's own text records the single charge as pattern 11, minor and
not display-affecting (the EN-site example link), with credit at
8/8, no live duplicate rate, no untranslated or garbled prose, and
all dependencies existing on scp-jp — the count-versus-text shape
seen elsewhere in the vendored rows, resolved here in favour of
the text, which the (c3) P11 disposition matches. Ledger part (c3)
records P11 DISPOSITIONED only. The (b) verdict is PASS, with no
OPEN items at the determination and no FIX5 re-judgement.

**Why.** The verification section exists so the reader can see which
checks ran, what they found, and what became of each finding,
without re-running the campaign.

**Verify.** The cited rows; the stamp at the head of this file is
generated from the same records by `review/build_review.py`.

**Disposition.** Verdict: PASS (go-sign ledger part (b)), with the
two items below carried for the coordinator.

## Per-theme record: thalassophobia-sigma-jp

**Item 1 — usage exhibit names a plain-slug page (sweep family).**
Candidate L57: `@@[[include :scp-jp:theme:thalassophobia-sigma]]@@`.
The posting name is `theme:thalassophobia-sigma-jp`; the snippet
names a page that will not exist. Uncharged by T4 for this theme.
Flagged for the population sweep; not edited.

**Item 2 — the six asset files are still unhosted (probe
evidence).** The repoints are done (section 4's census, all under
`local--files/theme%3Athalassophobia-sigma-jp/` on the draft host);
the uploads are not. Probes run once each on 2026-11-17:
`image.png` 404, `logo.svg` 404, `gradient.png` 404,
`gradient-red.png` 404, `copperlinks.png` 404, `coppermode.png`
404. Unlike its sibling theme, this one drew no pattern-5 charge —
T4's row does not mention the files — so no ledger line records
their state at all; this package records it so the reflection step
treats the uploads as outstanding. The class governing them is the
deferred-hosting class (KB-58).

## Change set

Delivered with this candidate in the canonical repository: the
candidate page itself (`pages/theme:thalassophobia-sigma-jp.txt`)
and its decoration sample
(`pages/theme-decoration-sample-thalassophobia-sigma-jp.txt`). The
candidate's own history is two commits: the Stage 2 EN21 integration
and FIX-P4.

## Appendix: residue resolution

The classifier left 3 blocks unlabeled (3.5%). Per the class-M
convention they are resolved here by shape, one row per block.

| Block | Lines (orig → cand) | Resolution |
|---|---|---|
| B16 | 95 → 97 | Manual section heading translated: `+ Formatting Examples` → `+ 書式例` (section 6, P10). |
| B49 | 202 → 204 | Exhibit sentence translated around its code tokens: the `darkbox` div explanation, prose JP, punctuation converted (section 6, P10). |
| B50 | 207 → 209 | The matching `lightbox` exhibit sentence, same shape (section 6, P10). |

## License and attribution

- **Title:** Thalassophobia Theme (Sigma-9)
- **Author:** TheDarkArtist
- **Source:** https://scp-wiki.wikidot.com/theme:thalassophobia-sigma — revision 56
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
