# theme:stargazer-jp — Stargazer theme (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:stargazer-jp — origin EN, population #140 [GOSIGN2-LEDGER (b) row 140]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now cf26715f871d45a1d950a269814d0d300410108f61655e26318137ce0c6546be); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 12 errors / 1 warn / 1 info (hotlink×10, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 160; GOSIGN2-LEDGER (b) row 140]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 457–522px@320/375 on page and sample; runtime-hotlink site-theme chain; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-D (EN20))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN20))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 140, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 140]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 140]
- Computed against: canonical commit 2dbb83da26b94a9c4a2e7de3a1562025f3552358; candidate file pages/theme:stargazer-jp.txt sha256:cf26715f871d45a1d950a269814d0d300410108f61655e26318137ce0c6546be; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

This file is the explanation record for one theme's Sigma-10 port. The
diff it explains is `diff.md` in this directory, generated from
`original.txt` (the frozen mirror) and `candidate.txt` (a byte copy of
the canonical candidate). The verdict stamp at the head of this file is generated; do not
edit inside the stamp markers.

## Provenance

- Theme: `theme:stargazer` on scp-wiki (EN branch), revision 11.
  Author AstralNavigator; an aesthetic dark-mode theme extending the
  Basalt theme.
- Frozen mirror: `original.txt`, 674 lines, 22,382 bytes, SHA-256
  `714f35025ae4dfc883ac8b26733e55325ea53eb352ffefcdcbc18dce3e794e1a`
  (matches `review/sources.tsv`; mirror-store class COPY).
- Candidate: `candidate.txt`, 1,004 lines, 36,185 bytes, SHA-256
  `275b9c10b490fd0541d224135ead2c0342fdd9a1932297baa298d61e59189fb3`,
  byte-identical to the canonical file.
- Kind (sources.tsv): K5b-3 — the candidate layers over
  `theme:basalt-jp`; this diff covers the theme's own layer only.
- The candidate entered the canonical repository in the Stage 2 EN20
  integration (3faf2e1, LOCALIZE-S2-C wave) and was touched twice
  since: by the pattern-4 repoint wave (f1138e4, FIX-P4) and by the
  duplicate-import removal (a497307, FIX4-MECH). The first of those
  matters to section 3: the delivery this package describes is the
  post-repoint one, and the ledger's disposition wording predates it.

## Summary

Stargazer is a thin variable layer over Basalt: its own stylesheet
re-skins the base's palette for a dark sky look, and everything else
(frame, header text, most mechanics) comes from the base. The
original delivered that layer awkwardly — the Basalt import's URL is
malformed (a space inside the path), the layer's CSS sits in a code
exhibit imported at the tail from the EN files host, and a stray
frame at the very tail points at the author's sandbox experiment.
The port inlines the layer into a head module whose first line
imports the JP Basalt candidate, frames the base at priorities 1
and 2 (the two slots the EN Basalt CDN bundle's two files occupied),
and deletes the tail module and the sandbox frame. The Basalt base
dependency was T4's principal charge against this theme (pattern 4:
the whole base arrived from EN hosts, header text included); the
charge is answered in the current bytes by the FIX-P4 repoint,
although the ledger's disposition line still describes the older
class-(ii) framing — the per-theme record states both. What remains
open is small: the layer's `--header-logo` override still names the
EN-hosted Basalt logo although the JP base hosts its own copy, the
delivered module carries its banner comment twice, and one prose
link still points at the EN Basalt page.

## Class summary (auto-classification)

65 change blocks (diff.md is Tier 2 format for this package):
44 specific (67.7%), 19 heuristic (29.2%), 2 residue (3.1%),
0 skipped. The generator counts +452 / −122 lines (574 changed lines
by a plain diff count); the classifier detects one relocation (the
code exhibit's CSS → the head module, similarity 0.992). Label
firings: TRANSLATION-ANCHORED ×29, TRANS-UNANCHORED ×20,
EXHIBIT-RESTRUCTURE ×9, INCLUDE-REPOINT ×8, LINK-REPOINT ×2,
RESTORATION ×2, WS-ONLY ×2, and single firings of CONTENT-STRING,
CREDIT-PREVIEW, DELIVERY-MOVE, DRAFT-HOST, HEADERVAR, IFTAGS,
TASL-FIELDS, DELIVERY-HOST, FONT-IMPORT, JPFONT-STACK, BARE-RATE-DEL,
COMPONENT-SWAP, LICENSE-BOX, SELF-DELIVERY.

Adjudication notes: the nine EXHIBIT-RESTRUCTURE primaries were
checked against the exhibit census — eight are image-block include
repoints (their INCLUDE-REPOINT spans are the whole change) and one
is the license-box conversion (section 1); no exhibit was
restructured. The RESTORATION firing in block B63 is the source
exhibit's duplicated banner (per-theme record, item 2); the one in
the head mega-block B1 rides on the delivery reconstruction of
section 3. The CONTENT-STRING firing is an empty `content: ""` value
(candidate L233) — no reader-visible string is involved.

## 0. Tag frame and page furniture

**What.** The candidate's head stands outside the tag gate: the
delivery module (candidate L1–322), then two interwiki-style frame
includes naming the base delivery at priorities 1 and 2
(candidate L324–332, section 3), then the gate
`[[iftags +テーマ]]` (candidate L333, block B1, IFTAGS) opening over
the credit block and body. The original opens its gate first
(`[[iftags +theme]]`, original L1) and keeps its modules inside it;
its only frame is the stray tail frame deleted with the tail
(section 3).

**Why.** Pattern class P1 (frame and tag furniture; KB-03, KB-04).
Failure prevented: a gate keyed to the EN tag name never opens on
scp-jp, and a layered theme whose frames name the origin branch's
bundle applies the wrong base in the check environment.

**Verify.** `grep -n 'iftags\|interwiki-style' candidate.txt` — gate
at L333 with the JP tag name; two frames above it, both
`:scp-jp:component:interwiki-style`.

**Disposition.** No ledger line charges the frame placement. The (b)
verdict for this theme is PASS.

## 1. Credit block and license (P3, P9)

**What.** The original's only credit furniture is a labelled bare
Rate (original L37–38), deleted (block B6, BARE-RATE-DEL). The
candidate carries a preview credit block (candidate L335–344, block
B1: CREDIT-PREVIEW, TASL-FIELDS) with eight fields: title
Stargazerテーマ; translator of record AI; translation year 2026;
original title Stargazer Theme; copyright holder AstralNavigator;
creation year 2026; reference revision 11; and a source link to
`https://scp-wiki.wikidot.com/theme:stargazer` — the host
`review/sources.tsv` records, so the host check passes. The author
field agrees with the original's prose credit and with the license
box below.

The license record converts form: the original carries the
stargazer logo's license as blockquote text inside a collapsible
(original L645–663); the candidate carries it as a license-box
component pair, `:scp-jp:component:license-box-backend` with
`author=AstralNavigator` and `license-box-end` (candidate L998–1003,
block B64, LICENSE-BOX), its fields translated (ファイル名 / 作者 /
ライセンス / 出典）. The source field keeps the file's EN files-host
URL, which is the file's origin record, not a navigation link.

**Why.** Pattern classes P3 (credit furniture swap; KB-16, KB-17)
and P9 (license box; KB-47, KB-48). Failure prevented: a bare Rate
beside the credit block renders a second rating widget, and a
license statement left as free prose drifts from the component form
the JP site renders.

**Verify.** `sed -n '335,344p' candidate.txt`;
`sed -n '998,1003p' candidate.txt` against original L645–663;
`grep -c 'module Rate' candidate.txt` returns 0.

**Disposition.** No ledger line charges the credit or license for
this theme; no credit CSS supplement exists on either side. The (b)
verdict is PASS.

## 2. Includes and component references (P2, P8)

**What.** INCLUDE-REPOINT fires 8 times. The usage exhibits convert
to bare same-site forms naming the posting names:
`@@[[include theme:stargazer-jp]]@@` (candidate L380, block B7,
COMPONENT-SWAP) with the Basalt companion exhibit beside it. The
seven image-block exhibits repoint `:scp-wiki:component:image-block`
→ `:scp-jp:component:image-block` (candidate L494 and L588–643,
blocks B14, B47–B57), keeping their table captions. The license-box
include is section 1; the frame includes are section 0. The
image-block exhibits' asset (the Basalt logo) is section 4.

**Why.** Pattern classes P2 (include repoints; KB-05) and P8
(exhibit fidelity; KB-42, KB-43). Failure prevented: an exhibit
pointing at the origin branch shows readers a page that is not the
one this candidate installs. Note the usage exhibit names the
correct `-jp` posting name — this theme is not in the plain-slug
sweep family.

**Verify.** `grep -n 'scp-wiki:' candidate.txt` returns nothing;
`grep -c 'image-block' candidate.txt` returns 7 exhibit lines plus
none live.

**Disposition.** No ledger line charges the repoints. The (b)
verdict is PASS.

## 3. Delivery topology (P4)

**What.** The original's delivery has four pieces. (1) A head module
importing Basalt from `https://scp-wiki.wikidot.com/local--code/ theme%3Abasalt/1`
(original L3–5) — the URL contains a literal space; as written it
cannot have been the working path, and the theme in practice rode on
the CDN bundle its code exhibit imported. (2) A head module with the
Bungee Hairline font and the title rules (original L7–30).
(3) The theme's own CSS as a code exhibit (original L337–642), whose
head imported the EN Basalt CDN bundle. (4) A tail module importing
the exhibit's delivery from the EN files host with an unencoded
colon (`https://scp-wiki.wdfiles.com/local--code/theme:stargazer/1`,
original L666–668), followed by a frame at priority 3 naming a
sandbox page (`scp-sandbox-3.wdfiles.com/local--code/astral:blue-basalt-in-space/1`,
original L670–673) — the author's own experiment, unrelated to this
theme's delivery.

The candidate rebuilds the topology. The own layer is inlined into a
head module (candidate L1–322; the classifier's one relocation,
similarity 0.992, block B1, DELIVERY-MOVE) whose first line imports
`theme:basalt-jp/1` from the draft host (candidate L2). The two
frames (section 0) name the same basalt-jp delivery at priorities 1
and 2: in the Stage-2 candidate they named the Basalt CDN bundle's
two files (`normalize-min.css`, `basalt-bedrock-min.css` — the T4
charge's L326/L331), and the FIX-P4 wave (f1138e4) repointed both to
the JP base candidate, whose single delivery now fills both slots.
The Bungee module survives inside the gate (candidate L346–369,
section 4). The tail module and the sandbox frame are deleted
(block B65): the tail import is subsumed by the inlined module, and
the sandbox frame framed somebody else's experiment.

**Why.** Pattern class P4 (delivery topology; KB-23). Failure
prevented: a port whose base arrives from the origin branch's CDN is
not self-contained — it inherits the EN base's behaviour wholesale
(including, here, EN header text; section 5) and breaks if the bundle
moves. Layering over the JP base candidate makes the port a member
of the JP theme family it will be posted beside.

**Verify.** `sed -n '1,2p' candidate.txt` and
`sed -n '324,332p' candidate.txt`;
`grep -n 'cdn.scpwiki\|scp-sandbox' candidate.txt` returns nothing;
`git log --oneline -- pages/theme:stargazer-jp.txt` shows the FIX-P4
commit in the file's history.

**Disposition.** T4 charged this topology as pattern 4, one of the
theme's two display-affecting findings (LOCALIZE-ROWS row 140).
Ledger part (c3) records "P4 DISPOSITIONED (delivery class (ii):
original-state CDN delivery)". The current bytes go further than
that wording: the imports and frames were actually repointed to
basalt-jp by FIX-P4. The per-theme record (item 4) states the
discrepancy between the disposition's wording and the bytes; this
package follows the bytes. The draft-host form of the base delivery
URL is environment class (iii) (KB-41).

## 4. Fonts and assets (P5, P7)

**What.** The Bungee Hairline load moves from fonts.bunny.net to
Google Fonts (candidate L347, block B2, DELIVERY-HOST and
FONT-IMPORT), and the `.theme-title` stack gains the JP face:
`'Bungee Hairline', sans-serif` → `'Bungee Hairline', 'Noto Sans JP', sans-serif`
(candidate L350, block B3, JPFONT-STACK). The theme's own CSS names
no other display font; the base delivers the body faces.

Assets. Three references to EN-hosted files stand in the candidate:
the layer's `--header-logo` variable names the Basalt dark-mode logo
on the EN files host
(`https://scp-wiki.wdfiles.com/local--files/theme%3Abasalt/basalt_scp_logo-for_darkmode.svg`,
candidate L34, mirrored in the source exhibit at L708); the seven
image-block exhibits name the same file (section 2); and the title
image names the theme's own logo on the EN host
(`https://scp-wiki.wdfiles.com/local--files/theme%3Astargazer/stargazer_logo.svg`,
candidate L374, unchanged from original L34).

**Why.** Pattern classes P7 (font stacks; KB-35, KB-36) and P5
(assets; KB-25, KB-26). Failure prevented: a title stack without a JP
face renders the theme's Japanese title text in a fallback font, and
assets left on the origin host are outside the port's control.

**Verify.** `sed -n '346,352p' candidate.txt`;
`grep -n 'scp-wiki.wdfiles' candidate.txt` lists the logo references
(plus the license source field, section 1).

**Disposition.** The font charge (pattern 7) is DISPOSITIONED in the
ledger's class summary: where the base delivers the face — basalt-jp
loads Noto Sans JP (its L113) — the charge is answered by the
FIX-P4 migration, and this candidate additionally names the face in
its title stack. The asset references are T1's hotlink class
(section 11). Two of them have JP-side equivalents today and are
recorded in the per-theme record: the `--header-logo` override
(item 1), and the theme's own logo, whose draft-host form
(`…/local--files/theme%3Astargazer-jp/stargazer_logo.svg`) probed
404 on 2026-11-17 against the EN form's 200 — the deferred-hosting
end-state (KB-58).

## 5. Header, titles and rendered strings (P6)

**What.** The theme's own CSS sets no header text: its only
HEADERVAR firing is the header colour pair
(`--header-title-color`, `--header-subtitle-color`, candidate
L105–106, inside block B1). The header title and subtitle text are
inherited from the base. Under the original's CDN delivery that
inheritance was EN text ("SCP Foundation" / "SECURE - CONTAIN -
PROTECT") on a JP page — the second of T4's display-affecting
findings, recorded in the LOCALIZE-S2-C disposition report (item 12)
as tied to the Basalt-base migration. Under the current delivery the
base is basalt-jp, whose header variables resolve to its JP title
settings, so the inheritance is JP. The candidate's CONTENT-STRING
firing is an empty `content: ""` (candidate L233): no reader-visible
string.

**Why.** Pattern class P6 (header and rendered strings; KB-29,
KB-30, KB-31). Failure prevented: a JP page rendering an EN masthead
because its base bundle came from the EN CDN.

**Verify.** `grep -n 'header-title' candidate.txt` returns only the
colour variables; the base's settings are in
`pages/theme:basalt-jp.txt` (`--header-title: var(--title)` with the
JP title defined in the same file).

**Disposition.** The finding is answered by the FIX-P4 repoint
(section 3), under the same (c3) P4 disposition. Nothing else in this
section is charged.

## 6. Body translation (P10)

**What.** The documentation body is translated throughout: 29
TRANSLATION-ANCHORED blocks and 20 TRANS-UNANCHORED blocks (counted
class treatment, per the class-M convention) covering the intro
prose, the Basalt settings documentation with its tab headings, the
colour-system exhibits with their `{{.table1}}`–`{{.table6}}`
captions, and the credits prose for the component authors. The two
residue blocks are single-word tab headings in the settings section:
`+* Info` → `+* 情報` (B8) and `+* Coloring` → `+* 配色` (B45),
resolved in the appendix. The source exhibit's CSS comments cross
untranslated with the CSS, as comments do in this family (they are
the author's own banner and section markers, carried identically in
the delivered module and the exhibit).

**Why.** Pattern class P10 (translation; KB-50, KB-51). Failure
prevented: untranslated documentation makes the candidate unusable
as a JP theme page.

**Verify.** Spot-check any anchored block against diff.md (e.g.
B44, the credits prose); `grep -n '^+ ' candidate.txt` shows the JP
heading sequence.

**Disposition.** T4/T5 judged this theme FINDINGS jointly; the
translation-side charges are the delivery and header items of
sections 3 and 5. The (b) verdict is PASS.

## 7. Link targets (P11)

**What.** LINK-REPOINT fires twice: the colour-system prose now
links `[[[anomaly-classification-system-guide|…]]]` as a bare JP
page name where the original used the absolute EN URL (candidate
L581, block B46), and the component credits link
`component:betterfootnotes` and `component:acs-animation` as bare
names (candidate L660–661, block B60). One absolute EN link stands:
the intro prose links the word Basalt to
`https://scp-wiki.wikidot.com/theme:basalt` and sends readers to
"Basalt's wiki page" for the settings documentation (candidate
L385), although the candidate's own base is basalt-jp and the same
page's other links were repointed.

**Why.** Pattern class P11 (link targets; KB-54). Failure prevented:
a functional link left pointing at the origin branch sends JP
readers to the wrong wiki — here, to the EN Basalt page whose
settings documentation describes the EN delivery, not the JP port
the reader has actually loaded.

**Verify.** `grep -n 'scp-wiki.wikidot.com' candidate.txt` — the
hits are the credit source link (correct, section 1), the icon
credit's page link (candidate L459, an author-page reference carried
from the original), and the Basalt link above.

**Disposition.** No ledger line charges the Basalt link; it is
recorded as a minor item in the per-theme record (item 3). The
repoints themselves are uncharged.

## 8. Structural fidelity and exhibit census (P8, R3)

**What.** The exhibit census is preserved: the title block, the
usage exhibits, the seven image-block exhibits with their table
captions, the Basalt settings tabs, the colour-system exhibits, the
source-code collapsible, and the license collapsible all stand in
the original's order. The source exhibit's content changed form,
not census: it now mirrors the delivered module (banner, variables,
rules) instead of the original exhibit's text, and in doing so it
carries the banner comment twice (candidate L677–691 and L692–706),
because the delivered module itself carries it twice — once as the
module's preamble after the Basalt import (candidate L3–17) and once
at the head of the theme CSS proper (candidate L19–33). The
original exhibit carries it once (original L339–353). The
duplication is inside CSS comments; nothing renders differently.
The classifier's RESTORATION firing in block B63 marks exactly these
added banner lines in the exhibit.

**Why.** Pattern class P8 (structural fidelity; KB-42, KB-43) and
residue class R3 (an element whose form changed, ground stated
here). Failure prevented: an exhibit that silently diverges from the
delivered text misleads the next reviewer about what the theme
actually loads; the divergence here is named and bounded to a
comment.

**Verify.** `grep -n 'Version 1.0.0' candidate.txt` returns four
lines (module ×2, exhibit ×2) against the original's one;
`sed -n '675,712p' candidate.txt`.

**Disposition.** No ledger line charges the structure. The banner
duplication is recorded as a minor item in the per-theme record
(item 2). The (b) verdict is PASS.

## 9. Formatting-only changes (R4)

**What.** Two WS-ONLY blocks (B4, B5), both in the Bungee module:
trailing spaces after two declarations (original L16 and L26,
`width: 150px; ` and `width: 50px; `) are dropped in the candidate
(candidate L355, L365). The classifier reports 0 reindent blocks.
Nothing else in the pair is formatting-only; the size delta is the
delivery reconstruction.

**Why.** Residue class R4 (formatting-only). Trailing-space removal
inside a carried module is the class's textbook instance.

**Verify.** Blocks B4 and B5 in classification.json;
`grep -n ' $' candidate.txt` in the module region returns nothing.

**Disposition.** Nothing to disposition.

## 10. Porter annotations (R2)

**What.** None. The candidate contains no `[!-- --]` porter comments
and no translator's notes. The CSS banner comments are the author's
own, carried from the original (section 8).

**Why.** Residue class R2 has no instance here; the ground is the
grep below, run before writing this section.

**Verify.** `grep -c '\[!--' candidate.txt` returns 0.

**Disposition.** Nothing to disposition.

## 11. Dispositioned deviations (class (ii) / (iii) summary)

**What.** The deviations a reader of the diff might otherwise charge
against the candidate, with their dispositions:

- T1's findings (T1-ROWS row 160: exit 1, 12 errors / 1 warn / 1
  info) are hotlink ×10 — the EN-hosted logo references of section 4,
  in the standing class register c1 records for the population — and
  pseudo-ref ×2 (the frame and license-box includes). Environment
  class (ii).
- The render check's items (RENDER-ROWS-2, EN20) are all
  DISPOSITIONED in ledger part (c2): page-overflow 457–522px at
  320/375 widths on page and sample, in the recorded cross-cutting
  families (static credit replica fixed width at mobile widths,
  KB-33; preview chrome, KB-34); the runtime-hotlink site-theme
  chain (KB-40, environment layer); and the sample credit-modal, the
  preview form's known property (KB-32). Engine coverage is the full
  matrix as run by the lane, not separately caveated in the row.
- The pattern-4 and pattern-7 dispositions are sections 3–5.
- The draft-host form of the delivery URLs is environment class
  (iii) (KB-41).

**Why.** These classes exist so a reviewer does not re-litigate
environment properties as candidate defects; each item above names
its record so the disposition can be re-checked at its source.

**Verify.** The theme's rows in `review/AUTHORITIES/ledger-parts/`
(T1-ROWS row 160, RENDER-ROWS-2) and its blocks in
`GOSIGN2-LEDGER.md` parts (c2) and (c3).

**Disposition.** All items above are DISPOSITIONED in the cited
records. The minor items the records do not reach are the per-theme
record below.

## 12. Verification history

**What.** T1 (source check): FINDINGS (classified), 12 errors in the
standing classes — T1-ROWS row 160. T2/T3 (render check): FINDINGS,
all items dispositioned in (c2) — RENDER-ROWS-2 (EN20). T4/T5
(localize check): FINDINGS with 2 display-affecting items — pattern
4 (the EN-CDN base dependency) and the EN header-text inheritance
recorded with it (LOCALIZE-S2-C item 12) — LOCALIZE-ROWS row 140.
Both trace to the base delivery, and both are answered in the
current bytes by the FIX-P4 repoint (f1138e4); the candidate's later
FIX4-MECH touch (a497307) removed duplicate imports under KB-65.
Ledger part (c3) records P4 DISPOSITIONED. The (b) verdict is PASS,
with no OPEN items at the determination and no FIX5 re-judgement.

**Why.** The verification section exists so the reader can see which
checks ran, what they found, and what became of each finding,
without re-running the campaign.

**Verify.** The cited rows and commits; the stamp at the head of
this file is generated from the same records by
`review/build_review.py`.

**Disposition.** Verdict: PASS (go-sign ledger part (b)), with the
minor items below carried for the coordinator.

## Per-theme record: stargazer-jp

**Item 1 — the `--header-logo` override names the EN-hosted Basalt
logo (minor flag, not edited).** Candidate L34 (and the exhibit copy
at L708) sets `--header-logo` to
`https://scp-wiki.wdfiles.com/local--files/theme%3Abasalt/basalt_scp_logo-for_darkmode.svg`.
The candidate imports basalt-jp at L2, and basalt-jp hosts the same
dark-mode logo on the JP side (its own `--logo` at
`pages/theme:basalt-jp.txt` L1156 names the draft-host
`theme%3Abasalt-jp` copy). Because the override sits after the
import in the same module, the EN file is what renders. A mechanical
posting-time host swap would not fix it: the JP copy lives under
`theme%3Abasalt-jp`, not `theme%3Abasalt`. The seven image-block
exhibits name the same EN file (candidate L494, L588–643). Recorded
for the reflection step with both loci; the candidate is not edited
here.

**Item 2 — duplicated banner comment in the delivered module
(minor).** The module's CSS carries the author's banner comment
twice (candidate L3–17 and L19–33), and the source exhibit mirrors
both copies (L677–691, L692–706); the original exhibit carries it
once (original L339–353). Comment-only, no rendering effect; recorded
so a future editor does not mistake the second copy for a section
boundary.

**Item 3 — intro prose link still points at the EN Basalt page
(minor).** Candidate L385 links to
`https://scp-wiki.wikidot.com/theme:basalt` for the settings
documentation, while the candidate layers over basalt-jp and its
other prose links were repointed to JP page names (section 7).
Recorded; not edited.

**Item 4 — the (c3) disposition wording understates the repair
(record note).** Part (c3) dispositions pattern 4 as "delivery class
(ii): original-state CDN delivery", which describes leaving the CDN
dependency in place. The bytes show the FIX-P4 wave actually
repointed the head import and both frame slots to `theme:basalt-jp/1`
(f1138e4; the pre-fix frame values are visible in that commit's
parent). The practical difference matters for section 5: the header
text inheritance is JP now because the base changed, not because the
charge was waived. This package follows the bytes.

### Post-package repairs (REFRESH3-F)

**FIX-STELLAR, landing `2dbb83d` (report `R/review-scout/FIX-STELLAR.md`, item 1,
"theme:stargazer-jp").** This landing postdates the package build
(`7170328`) and repairs items 1–3. Three candidate changes: (a) the logo
repoint at 9 loci — the EN
`https://scp-wiki.wdfiles.com/local--files/theme%3Abasalt/basalt_scp_logo-for_darkmode.svg`
→ basalt-jp's own darkmode logo on the draft host,
`https://sigma10-jp-test.wdfiles.com/local--files/theme%3Abasalt-jp/basalt_scp_logo-for_darkmode.svg`
(the delivered `--header-logo` L34, its source-exhibit mirror, and the
seven image-block exhibits; probed HTTP 200, `image/svg+xml`, 2,405 bytes
— a folder change, not a host swap of the EN path); (b) the 14-line
author banner comment removed at its second copy in both the delivered
module and the source-exhibit mirror, keeping the first (head) copy —
banner occurrences 4 → 2 (comment-only); (c) the intro prose link
`[[[https://scp-wiki.wikidot.com/theme:basalt|Basalt]]]` →
`[[[theme:basalt-jp|Basalt]]]`. Checker per the report: error 11 / warn 1 /
info 1 → 11/2/1 — the 9 EN-host hotlinks became 9 draft-host pseudo-refs
(both class (ii)), plus the standing `link-target-missing` warn for the
not-yet-posted `theme:basalt-jp`; no new class (i) error. This package
documents the corrected candidate; its stamp reads STALE against the
pre-repair verdict, by design.

## Change set

Delivered with this candidate in the canonical repository: the
candidate page itself (`pages/theme:stargazer-jp.txt`), its
decoration sample (`pages/theme-decoration-sample-stargazer-jp.txt`),
and the base candidate it layers over (`pages/theme:basalt-jp.txt`,
with its own package). The candidate's own history is three commits:
the Stage 2 EN20 integration, FIX-P4, and FIX4-MECH.

## Appendix: residue resolution

The classifier left 2 blocks unlabeled (3.1%). Per the class-M
convention they are resolved here by shape, one row per block.

| Block | Lines (orig → cand) | Resolution |
|---|---|---|
| B8 | 47 → 383 | Settings tab heading translated: `+* Info` → `+* 情報` (section 6, P10). |
| B45 | 240 → 578 | Settings tab heading translated: `+* Coloring` → `+* 配色` (section 6, P10). |
