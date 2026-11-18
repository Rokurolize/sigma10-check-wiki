# theme:sodium-pentasulfide-jp — Sodium Pentasulfide theme (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:sodium-pentasulfide-jp — origin CN, population #229 [GOSIGN2-LEDGER (b) row 229]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 108abafeb88c08aee4eca8ff64e28c16a84f599d9d1c366ee6c5186e5d7bd187); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 11 errors / 4 warns / 1 info (pseudo-ref×11); standing classes dispositioned in register c1 [T1-ROWS row 260; GOSIGN2-LEDGER (b) row 229]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 331px@320 + 909px@768; T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN14)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN14)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 228, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 228]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 229]
- Computed against: canonical commit 1e3da43416851307b491da1cf4cadf7bc1f61850; candidate file pages/theme:sodium-pentasulfide-jp.txt sha256:108abafeb88c08aee4eca8ff64e28c16a84f599d9d1c366ee6c5186e5d7bd187; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

This file is the explanation record for one theme's Sigma-10 port. The
diff it explains is `diff.md` in this directory, generated from
`original.txt` (the frozen mirror) and `candidate.txt` (a byte copy of
the canonical candidate). The verdict stamp at the head of this file is generated; do not
edit inside the stamp markers.

## Provenance

- Theme: `theme:sodium-pentasulfide` on scp-wiki-cn (CN branch),
  revision 65. Author OneWildMaggot; a red variant layered over the
  Sodium theme (Ankv), its design referencing Woedenaz's Ouroborous
  theme (both credits carried in the candidate, section 1).
- Frozen mirror: `original.txt`, 454 lines (453 by `wc`), 12,484 bytes,
  SHA-256 `0a66fc559a9c94b20a1f64ceffca54a9f3d8e5a14f9ee4d56faabfaea4b0d2`
  (matches `review/sources.tsv`; mirror-store class COPY).
- Candidate: `candidate.txt`, 1,355 lines, 40,184 bytes, SHA-256
  `64b96da50c1e0f6be8b9a5bfae8cf6ca5e09e8c0f9b8a3cbd47f5aec8df6d0e36`,
  byte-identical to the canonical file.
- Kind (sources.tsv): K5b-3 — the candidate layers over
  `theme:sodium-jp`; this diff covers the theme's own layer only (the
  base layer is `theme:sodium-jp`'s own record; the per-theme record
  below states what that means for reading this diff).
- The candidate entered the canonical repository in the Stage 2 CN14
  integration (12d839e, LOCALIZE-S2-E wave) and was touched once since,
  by the credit completion wave (666f543, FIX2-CREDIT).
- `review/sources.tsv` records that the original has been superseded
  upstream since revision 65; the campaign holds a follow-up diff
  artifact for the upstream delta (section 12). The port's baseline
  remains revision 65.

## Summary

The original page is a thin shell over external CSS: it imports the
base Sodium stylesheet from a GitHub Pages host and its own stylesheet
from a file hosted on a CN sandbox wiki, followed by a small module of
override rules. The port rebuilds that delivery inside the repository:
the base layer becomes an import of the JP Sodium candidate's own
delivery, the theme's own layer is reconstructed as an in-page code
exhibit (candidate L390–1305) served as the page's `local--code/…/1`
and framed at priority 1, and the override module is carried over in
its original form with only its import repointed. Around that
reconstruction sit the standard furniture changes: the CN credit
furniture (a labelled bare Rate and two credit-module trios) is
replaced by one JP preview credit block whose fields carry the
original's full attribution, the documentation body and showcase are
translated, the anomaly-class-bar exhibits are repointed to the JP
component with their parameter values converted to the component's
English token vocabulary, and one CN tracking component that the
original embeds as a joke is left behind with a translator's note in
the file saying so. One display-affecting finding stands open against
the bytes: the header subtitle keeps the CN motto form instead of the
JP standard tagline (per-theme record, item 1).

## Class summary (auto-classification)

112 change blocks (diff.md is Tier 2 format for this package: summary
header, block index, collapsed diff): 60 specific (53.6%), 42
heuristic (37.5%), 10 residue (8.9%), 0 skipped. The generator counts
+1,088 / −187 lines (1,275 changed lines by a plain diff count). The
heuristic mass is the documentation body's translation blocks and the
reconstructed CSS exhibit; the residue is ten single lines inside the
class-bar exhibits and one font-sample line, all resolved in the
appendix. Label firings include COMMENT-TEXT ×73 (they ride on the
documentation translation blocks, whose showcase tokens match the
comment signature, and on the reconstructed CSS's own comments),
TRANSLATION-ANCHORED ×41, TRANS-UNANCHORED ×47, INCLUDE-REPOINT ×11,
EXHIBIT-RESTRUCTURE ×11, DELIVERY-MOVE ×3, DRAFT-HOST ×5,
ASSET-REHOST ×3, and single firings of IFTAGS, BARE-RATE-DEL,
CREDIT-PREVIEW, CREDIT-PROSE, TASL-FIELDS, COMPONENT-SWAP, GLYPH-FORM
×2, FONT-IMPORT, JPFONT-LOAD, CONTENT-STRING, HEADERVAR, DELIVERY-HOST
×2, SELF-DELIVERY ×2.

Adjudication note: the eleven EXHIBIT-RESTRUCTURE primaries were
checked against the exhibit census — nine are the class-bar include
repoints (their INCLUDE-REPOINT spans are the whole change), one is
the usage-exhibit pair, and one is the scpper collapsible (section 8);
no exhibit was restructured. The DELIVERY-MOVE primaries are the
delivery reconstruction of section 3, checked block by block: nothing
the original delivers is missing from the candidate.

## 0. Tag frame and page furniture

**What.** The candidate opens with the interwiki-style frame include
at priority 1 naming its own code delivery (candidate L1–4, block B1,
SELF-DELIVERY), placed before the tag gate, and converts the gate
itself from `[[iftags +版式]]` to `[[iftags +テーマ]]` (B1, IFTAGS).
The original has no frame: its furniture head is the credit block and
the two CSS modules at the tail. The candidate's own-delivery module
also sits outside the gate at the tail (candidate L1323–1355), as the
original's did (original L422–454).

**Why.** Pattern class P1 (frame and tag furniture; KB-03, KB-04).
Failure prevented: a Sigma-10 page without the priority-1 frame does
not receive its theme CSS in the check environment, and a gate keyed
to the CN tag name never opens on the JP site, whose theme tag is
テーマ.

**Verify.** `grep -n 'iftags\|interwiki-style' candidate.txt` — one
gate, JP tag name, frame before it; `sed -n '1,6p' candidate.txt`.

**Disposition.** No ledger line charges the frame. The (b) verdict for
this theme is PASS.

## 1. Credit block and license (P3, P9)

**What.** The original's credit furniture is three pieces: a labelled
bare Rate (`**评分：**` over `[[module Rate]]`, original L3–5), the CN
credit trio `credit:start` / `credit:more` / `credit:end`
(original L12–16), and the standalone trio
`credit:start-standalone` / `more-standalone` / `end-standalone`
(original L22–26). All three are deleted (block B2 carries
BARE-RATE-DEL and CREDIT-PREVIEW; the standalone trio's deletion
rides in block B3). The candidate carries one preview credit block
(candidate L9–18, CREDIT-PROSE and TASL-FIELDS in B2) with eight
fields: title 五硫化ナトリウム テーマ（Sodium Pentasulfide);
translator of record AI; translation year 2026; original title
五硫化钠 版式 (the CN work's name, quoted with its own glyphs);
copyright holder `[[*user OneWildMaggot]]` with the base-work
attribution carried in full — base: Ankv's Sodium theme, linked to
`theme:sodium-jp` (the JP port of the base), and design reference:
Woedenaz's Ouroborous theme; creation year 2026; reference revision
65; and a source link to
`https://scp-wiki-cn.wikidot.com/theme:sodium-pentasulfide`.

**Why.** Pattern class P3 (credit furniture swap; KB-16, KB-17) with
P9 (attribution; KB-47). Failure prevented: CN credit components do
not exist on scp-jp, a bare Rate beside the credit block renders a
second rating widget, and dropping the base-work and design-reference
lines would strip attribution the original itself carries. The source
link names the host `review/sources.tsv` records for the original
(scp-wiki-cn); the host check passes.

**Verify.** `sed -n '9,18p' candidate.txt` against original L3–26;
`grep -c 'module Rate' candidate.txt` returns 0;
`grep -n 'scp-wiki-cn' candidate.txt` shows the credit source link
only (the remaining hits are exhibit sample text, section 7).

**Disposition.** Ledger part (c3) records P3 credit fields FIXED for
this theme (credit waves, checker-verified); the fixing commit is in
the file's history (666f543). No credit CSS supplement was needed:
the theme's rate-widget styling is its own override rules, carried
with the delivery (section 3), not a T7 credit supplement. Neither
side carries a license box, so there is no P9 license-box conversion
to record.

## 2. Includes and component references (P2, P8)

**What.** INCLUDE-REPOINT fires 11 times and COMPONENT-SWAP once.
The usage exhibits (original L46–47) repoint from
`:scp-wiki-cn:theme:sodium` and `:scp-wiki-cn:theme:sodium-pentasulfide`
to the bare same-site forms `@@[[include theme:sodium-jp]]@@` and
`@@[[include theme:sodium-pentasulfide-jp]]@@` (block B7, candidate
L39–40) — the posting names of the JP candidates. The image-block
exhibit repoints to `:scp-jp:component:image-block` with its asset
moved to the draft host (block B9, section 4). The nine
anomaly-class-bar exhibits repoint
`:scp-wiki-cn:component:anomaly-class-bar-source` →
`:scp-jp:component:anomaly-class-bar-source` (blocks B83–B102,
candidate L294–368). The frame and credit includes are sections 0
and 1. One include is deliberately absent: the original's
`component:scpper-tracking-module` (original L412) — section 8.

**Why.** Pattern classes P2 (include repoints; KB-05) and P8 (exhibit
fidelity; KB-42, KB-43). Failure prevented: an exhibit pointing at the
CN branch shows readers a page that is not the one this candidate
installs, and a live include naming a CN component resolves nowhere
on scp-jp.

**Verify.** `grep -n 'scp-wiki-cn:' candidate.txt` returns nothing;
`grep -c 'anomaly-class-bar-source' candidate.txt` returns 9 (the
component page itself is not part of this repository's candidate
set).

**Disposition.** No ledger line charges the repoints. The (b) verdict
is PASS.

## 3. Delivery topology (P4)

**What.** The original delivers in three pieces, all outside the
page's own text: a tail module importing the base Sodium CSS from
`https://3nkv.github.io/Sodium/sodium.min.css` (original L417–419);
a second tail module importing the theme's own CSS from a file on a
CN sandbox wiki,
`https://scpsandboxcn.wikidot.com/local--files/onewildmaggot5/sodium-pentasulfide%20%281%29.css`
(original L422–424); and, inline in that second module, the theme's
override rules (original L426–454: four `:root` variables, the
rate-widget hover colour, the header background position, the
hovertip blur, and an `@supports` open-menu rule). The candidate
rebuilds each piece in-repo:

- Base layer: the first tail module now imports
  `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Asodium-jp/1`
  (candidate L1318–1320, block B111, DELIVERY-HOST) — the JP Sodium
  candidate's own delivery, not the upstream minified file.
- Own layer: the second tail module imports the candidate's own
  `local--code/theme%3Asodium-pentasulfide-jp/1` (candidate L1323–1325,
  block B112, SELF-DELIVERY), and the override rules follow it
  unchanged in substance (candidate L1327–1355: the same variables,
  the same hover colour, the same positions and blur, the same
  `@supports` rule).
- The own layer's substance — the content of the externally hosted
  file, which has no counterpart lines in the original page — is
  carried as a code exhibit inside a `+ ソースコード` collapsible
  (candidate L390–1305, blocks B108–B109, DELIVERY-MOVE): the full
  stylesheet with its font imports (section 4), its `:root` header
  variables (section 5), its content strings translated, and its
  comments translated with it. The head frame (section 0) names the
  same `/1` delivery at priority 1.

DELIVERY-MOVE fires 3 times (B108, B109, B112), DELIVERY-HOST twice
(B111, B112), DRAFT-HOST 5 times (the two tail imports and the
exhibit-internal file URLs).

**Why.** Pattern class P4 (delivery topology; KB-23). Failure
prevented: a port that keeps importing the author's sandbox file and
a GitHub Pages build is not a self-contained Sigma-10 candidate — the
files can vanish or change under it, and the check environment cannot
render it. The layered form (base delivery + own delivery + in-page
overrides) preserves the original's cascade order: base first, own
layer second, overrides last, exactly as the original's two modules
ordered them.

**Verify.** `sed -n '1317,1355p' candidate.txt` against original
L417–454; `grep -n 'local--code' candidate.txt` shows the frame, the
exhibit delivery, and the two tail imports naming `theme:sodium-jp/1`
and `theme:sodium-pentasulfide-jp/1` only;
`grep -n '3nkv.github.io\|scpsandboxcn' candidate.txt` returns
nothing.

**Disposition.** The ledger's T2/T3 items for this theme are
dispositioned in section 11; none charges the topology. The (b)
verdict is PASS. The draft-host form of the delivery URLs is
environment class (iii) (KB-41): the posting form is decided at
reflection time, not a candidate defect.

## 4. Fonts and assets (P5, P7)

**What.** Fonts enter with the reconstructed layer: the code exhibit
opens with three Google Fonts imports (candidate L391–393:
JetBrains Mono; Noto Serif JP; Jost) and a body rule setting
`'Noto Serif JP', 'Noto Serif CJK JP', serif` (block B108,
FONT-IMPORT and JPFONT-LOAD). The documentation's font samples
convert with it: the sample spans name Noto Serif JP where the
original names Noto Serif SC (candidate L385–388 and the exhibit
span at candidate L179, residue block B64), and the exhibit's stacks
name only families the imports load. Assets: the theme's logo,
`scplogo`, is referenced twice — the image-block exhibit's `name=`
(block B9: original's `http://scpsandboxcn.wikidot.com/local--files/onewildmaggot5/scplogo`
→ candidate's draft-host `…/local--files/theme%3Asodium-pentasulfide-jp/scplogo.png`)
and the exhibit's `--header-logo` variable (block B109, ASSET-REHOST
span candidate L1168–1169 plus the DRAFT-HOST spans). The class-bar
exhibits' icon URLs repoint from the EN files host to the JP
production files host (`scp-wiki.wdfiles.com` →
`scp-jp.wdfiles.com`, blocks B86 and B96, ASSET-REHOST).

**Why.** Pattern classes P7 (font stacks; KB-35, KB-36) and P5
(assets; KB-25, KB-26). Failure prevented: a stack naming the CN
branch's serif renders the JP page in a font that is not loaded, and
an asset left on the author's sandbox host is outside the port's
control.

**Verify.** `sed -n '390,395p' candidate.txt`;
`grep -n 'Noto Serif SC' candidate.txt` returns nothing;
`grep -n 'scplogo' candidate.txt` shows the two draft-host
references.

**Disposition.** The logo file is not yet hosted on the draft host:
probed once on 2026-11-17,
`https://sigma10-jp-test.wdfiles.com/local--files/theme%3Asodium-pentasulfide-jp/scplogo.png`
returned 404 while the original serves from the CN sandbox. That is
the deferred-hosting class (KB-58), environment class (ii) — the
repoint is the port's job; the upload is a later campaign step. No
ledger line names the asset for this theme; the (c3) line records
only the P3 fix.

## 5. Header, titles and rendered strings (P6)

**What.** The reconstructed layer's `:root` sets
`--header-title: "SCP財団"` (candidate L409, block B109, HEADERVAR) —
the JP form. The same block sets
`--header-subtitle: "収容 制御 保護"` (candidate L410). Two further
HEADERVAR spans (candidate L847–848, L851–852) are the subtitle's
animation bindings, mechanics unchanged. CONTENT-STRING fires once
as a label (5 spans in B109: candidate L521–522, L783–784, L791–792,
L1179–1180, L1199–1200) — the reconstructed CSS's own `content:`
strings, translated where reader-visible as part of the layer's
reconstruction.

**Why.** Pattern class P6 (header and rendered strings; KB-29, KB-30,
KB-31). Failure prevented: a header variable carrying CN text renders
Chinese on every JP page using the theme.

**Verify.** `grep -n 'header-title\|header-subtitle' candidate.txt`.

**Disposition.** The title is in order. The subtitle is not: the JP
standard tagline is 確保 - 収容 - 保護 (the form sibling candidates
carry, e.g. `theme:stellar-jp`), while the candidate's value is the
CN motto carried over — it lacks 確保 and names 制御, which is no part
of the tagline in either branch's standard form. The T4 lane charged
exactly this as this theme's one display-affecting finding
(LOCALIZE-ROWS row 228); no ledger line dispositions it. It was flagged in the per-theme record (item 1) for the coordinator; the candidate was not edited by this package. **Closed after the build by landing `1e3da43` (FIX-GUIDER item 2, Post-package repairs):** the subtitle now reads 確保 - 収容 - 保護, matching the branch tagline; the flag no longer stands against the current bytes.

## 6. Body translation (P10)

**What.** The documentation body is translated throughout: 41
TRANSLATION-ANCHORED blocks and 47 TRANS-UNANCHORED blocks (counted
class treatment, per the class-M convention — the blocks are the
usage prose, the syntax showcase with its heading / table / link
samples, the font and colour samples, and the reconstructed CSS's
comments). The showcase's sample content is translated as content
(the heading samples read 1 級見出し and so on). The warning line
under the credit block is translated in place (original L27 →
candidate L20). Two translation sub-shapes deserve names:

- The class-bar exhibits' parameter values are translated to the
  component's English token vocabulary (residue blocks B84–B103 and
  the GLYPH-FORM block B95): `risk-class` 待观察 → `notice`,
  需谨慎 → `caution`, 警告 → `warning`, 危险 → `danger`,
  危急 → `critical`; `container-class` 等待分级 → `pending`,
  已解明 → `explained`, 无效化 → `neutralized`, 机密 → `keter`.
  These are machine-read values, not prose: the CN tokens are not
  values the component defines.
- GLYPH-FORM fires twice (B8, B95): B95 is the `keter` value above,
  adjudicated here rather than as a glyph conversion; B8 is a
  retained-string line in the head documentation. The credit block's
  原題 field keeps the CN title's simplified glyphs as a quotation of
  the work's name (section 1), which is not a conversion failure.

**Why.** Pattern class P10 (translation; KB-50, KB-51), with the
value-vocabulary conversion under P2's rule that exhibits must name
what the JP site defines. Failure prevented: untranslated
documentation makes the candidate unusable as a JP theme page, and
CN class tokens in the exhibits would silently render the wrong (or
no) class bar when a reader copies them.

**Verify.** `grep -n 'risk-class\|container-class' candidate.txt`
shows only English tokens; spot-check any anchored block against
diff.md (e.g. B104–B107 at the font samples).

**Disposition.** T4's translation-side charges for this theme were
the subtitle (section 5) and the P3 gaps since fixed; the (c3) line
records the P3 fix. The (b) verdict is PASS.

## 7. Link targets (P11)

**What.** No prose link in the candidate targets a CN page. The
documentation's link samples are exhibit content and keep their
sample targets by design: a Baidu sample link, an intentionally dead
`[[[4o4-n0t-f0und]]]` sample, and two `<a href>` samples pointing at
the CN front page inside the syntax showcase (original L61 region,
translated as samples in block B16). They demonstrate link syntax;
they are not navigation. The one functional link, the credit source
link, names the recorded host (section 1). The credit block's
theme links name `theme:sodium-jp` and `theme:ouroborous-theme`
(attribution, section 1).

**Why.** Pattern class P11 (link targets; KB-54). Failure prevented:
a functional link left pointing at the origin branch sends JP
readers to the wrong wiki; exhibit samples are exempt because their
targets are the lesson.

**Verify.** `grep -n 'scp-wiki-cn' candidate.txt` — every hit is the
credit source link or a showcase sample line.

**Disposition.** No ledger line charges a link target for this theme.

## 8. Structural fidelity and exhibit census (P8, R3)

**What.** The exhibit census is preserved: usage exhibits, the
image-block exhibit, the syntax showcase, the nine class-bar
exhibits, the font samples, and the closing collapsible all stand in
the original's order. Two deviations, both forced by the delivery
reconstruction and both visible in the file:

1. The `+ ソースコード` collapsible holding the reconstructed CSS
   (candidate L389–1306) is an addition. In the original there was
   nothing to exhibit: the CSS lived in the external file. The
   collapsible is where the port puts the layer it rebuilt
   (section 3).
2. The closing collapsible (candidate L1308–1316) keeps the
   original's joke text, translated (original L405–415), but the
   `component:scpper-tracking-module` include inside it
   (original L412–414) is not carried. In its place the porter left a
   translator's note (candidate L1315) stating that the original
   embeds the CN tracking component there as a joke and that the JP
   port does not bring it over. Block B110 records the exchange:
   the include's lines have no translated counterpart, and the note
   is the counterpart. The component is a CN-branch tracking widget
   with no JP counterpart; the mechanism it performs (visit
   tracking) is not part of the theme.

**Why.** Pattern class P8 (structural fidelity; KB-42, KB-43) and
residue class R3 (a source element replaced, with the ground stated
in the file itself). Failure prevented: silently dropping a source
element — even a joke — leaves the next reviewer unable to tell an
accident from a decision; the in-file note makes the decision
auditable, and this section records it.

**Verify.** `sed -n '1308,1316p' candidate.txt` against original
L405–415; `grep -c 'scpper-tracking-module' candidate.txt` returns 1
(the mention inside the note) against the original's live include.

**Disposition.** No ledger line charges either deviation. The (b)
verdict is PASS.

## 9. Formatting-only changes (R4)

**What.** None. The classifier reports no whitespace-only block and
no re-indentation block for this pair. The size delta (+1,088 / −187)
is content: the reconstructed own layer on the added side, and the
deleted CN credit furniture on the removed side.

**Why.** Residue class R4 has no instance here; the ground is the
classifier's zero count for both signatures across 112 blocks.

**Verify.** `grep -c 'WS-ONLY' classification.json` returns 0.

**Disposition.** Nothing to disposition.

## 10. Porter annotations (R2)

**What.** One annotation, and it is load-bearing: the translator's
note at candidate L1315 inside the closing collapsible, recording the
scpper decision (section 8). The candidate contains no `[!-- --]`
porter comments. The parenthetical design-reference in the credit
block is attribution (section 1), not annotation.

**Why.** Residue class R2 (porter annotations). The note is the
in-file half of the R3 record in section 8; removing it would orphan
the decision.

**Verify.** `sed -n '1315p' candidate.txt`;
`grep -c '\[!--' candidate.txt` returns 0.

**Disposition.** No ledger line charges the annotation.

## 11. Dispositioned deviations (class (ii) / (iii) summary)

**What.** The deviations a reader of the diff might otherwise charge
against the candidate, with their dispositions:

- T1's 11 errors are all pseudo-references (T1-ROWS row 260: 11
  errors of 4 include-class and 1 credit-class flags whose targets
  exist only when the theme is installed) — environment class (ii),
  shared with the whole population.
- The render check's items (RENDER-ROWS-G, CN14) are all
  DISPOSITIONED in ledger part (c2): the page runtime-hotlink
  site-theme chain (KB-40, environment layer — the runtime hosts
  arrive via the shared site theme chain, not the candidate); the
  sample credit-modal, which is the preview form's known property
  (KB-32); and page-overflow 331px at 320 width and 909px at 768
  width, in the recorded cross-cutting families (static credit
  replica fixed width at mobile widths, KB-33; preview chrome,
  KB-34), the per-theme figures matching the campaign-wide shapes.
  The T3 re-run recorded no new screenshot-grounded visual finding.
- The draft-host delivery and asset URLs are environment class (iii)
  (KB-41); the unhosted logo file is the deferred-hosting class
  (KB-58), section 4.
- Coverage caveat, not a finding: this theme's render coverage is
  chromium-only (no WebKit verdict), as the (c2) block records.

**Why.** These classes exist so a reviewer does not re-litigate
environment properties as candidate defects; each item above names
its record so the disposition can be re-checked at its source.

**Verify.** The theme's blocks in `review/AUTHORITIES/T1-ROWS.md`
(row 260), `RENDER-ROWS-G.md`, and `GOSIGN2-LEDGER.md` part (c2).

**Disposition.** All items above are DISPOSITIONED in the cited
records. The one finding that was not dispositioned was the header subtitle (section 5, per-theme record item 1); it is closed by the post-build FIX-GUIDER landing `1e3da43` recorded in Post-package repairs.

## 12. Verification history

**What.** T1 (structural / link check): exit 1, 11 errors, all
pseudo-ref, class (ii) — T1-ROWS row 260. T2/T3 (render check):
FINDINGS as dispositioned in section 11; chromium-only coverage —
RENDER-ROWS-G (CN14). T4/T5 (localize check): FINDINGS with 1
display-affecting item (the header subtitle) plus the P3 credit gaps
the credit waves later fixed — LOCALIZE-ROWS row 228 (LOCALIZE-S2-E).
Ledger part (c3) records the P3 fix as FIXED for this theme. The (b)
verdict is PASS. Follow-up state: `review/sources.tsv` records the
original as superseded upstream since revision 65, and the campaign
record holds the follow-up diff artifact
`diff-sodium-pentasulfide-from65.txt` (class K5a-i) measuring the
upstream delta; this package's baseline remains revision 65, the
revision the port was made from, and no re-port is recorded.

**Why.** The verification section exists so the reader can see which
checks ran, what they found, and what became of each finding,
without re-running the campaign.

**Verify.** The cited rows; the stamp at the head of this file is
generated from the same records by `review/build_review.py`.

**Disposition.** Verdict: PASS (go-sign ledger part (b)), with the
subtitle flag carried in the per-theme record below.

## Per-theme record: sodium-pentasulfide-jp

**Item 1 — header subtitle keeps the CN motto form (flag, not
edited).** Candidate L410 sets `--header-subtitle: "収容 制御 保護"`.
The JP standard tagline is 確保 - 収容 - 保護. The candidate's value
carries over the CN motto's wording: 確保 is absent and 制御 appears,
which belongs to neither branch's standard tagline. T4 charged this
as the theme's display-affecting finding (LOCALIZE-ROWS row 228);
ledger part (c3) dispositions only the P3 credit fix for this theme,
so the charge stands open against the bytes. Whether the remedy is
the standard tagline or a documented theme variant is the
coordinator's call; this package records the evidence and does not
edit the candidate.

**Item 2 — how to read this diff (K5b-3 anatomy).** The original
page is 454 lines because its substance lived in two external files;
the candidate is 1,355 lines because the port rebuilt the theme's own
layer in-page. The +1,088 added lines are therefore mostly
reconstruction, not expansion, and the base Sodium layer appears in
this diff only as the tail import (section 3) — it is
`theme:sodium-jp`'s own package that explains it. For the record:
the base theme's own ledger state is separate from this theme's
PASS (its (b) row is NOT PASS at determination with an (e) item of
its own); layering over it is the K5b-3 premise the campaign
accepted for this family, and nothing in this package re-judges the
base.

### Post-package repairs (REFRESH3-F)

**FIX-GUIDER, landing `1e3da43` (report `R/review-scout/FIX-GUIDER.md`, item 2,
"theme:sodium-pentasulfide-jp header subtitle").** This landing postdates
the package build (`7170328`) and repairs item 1's flag. One candidate
change: `--header-subtitle: "収容 制御 保護"` →
`--header-subtitle: "確保 - 収容 - 保護"` at candidate L410. The old value
was the CN motto carried over unlocalized; the JP standard form was
verified against the population before writing — the exact declaration
stands in theme:candela-jp, theme:minimalist-bhl-jp, theme:magicity-jp
and theme:sunside-jp. Checker per the report: error 11 / warn 4 / info 1
before and after, class (i) errors 0. This package documents the
corrected candidate; its stamp reads STALE against the pre-repair
verdict, by design.

## Change set

Delivered with this candidate in the canonical repository: the
candidate page itself (`pages/theme:sodium-pentasulfide-jp.txt`), its
decoration sample (`pages/theme-decoration-sample-sodium-pentasulfide-jp.txt`),
and the family companions it layers over —
`pages/theme:sodium-jp.txt` with its base CSS fragment
(`pages/fragment:sodium-jp-base-css.txt`) and the base's decoration
sample. The candidate's own history is two commits: the Stage 2 CN14
integration and the FIX2-CREDIT completion (section 1).

## Appendix: residue resolution

The classifier left 10 blocks unlabeled (8.9%). Per the class-M
convention they are resolved here by shape, one row per block;
sections above cite the rows that carry a section's argument.

| Block | Lines (orig → cand) | Resolution |
|---|---|---|
| B64 | 186 → 179 | Font-sample span: the stack in the sample converts Noto Serif SC → Noto Serif JP (section 4/6, P7). |
| B84 | 308 → 300 | Class-bar exhibit value: `risk-class` 待观察 → `notice` (section 6). |
| B87 | 319 → 310 | Class-bar exhibit value: `risk-class` 需谨慎 → `caution` (section 6). |
| B89 | 329 → 319 | Class-bar exhibit value: `risk-class` 警告 → `warning` (section 6). |
| B91 | 339 → 328 | Class-bar exhibit value: `risk-class` 危险 → `danger` (section 6). |
| B93 | 349 → 337 | Class-bar exhibit value: `risk-class` 危急 → `critical` (section 6). |
| B97 | 360 → 347 | Class-bar exhibit value: `risk-class` 待观察 → `notice`, second exhibit (section 6). |
| B99 | 367 → 353 | Class-bar exhibit value: `container-class` 等待分级 → `pending` (section 6). |
| B101 | 377 → 362 | Class-bar exhibit value: `container-class` 已解明 → `explained` (section 6). |
| B103 | 387 → 371 | Class-bar exhibit value: `container-class` 无效化 → `neutralized` (section 6). |

## License and attribution

- **Title:** 五硫化钠 版式
- **Author:** OneWildMaggot（ベース: AnkvのSodiumテーマ／デザインはWoedenazのOuroborousテーマを参考）
- **Source:** https://scp-wiki-cn.wikidot.com/theme:sodium-pentasulfide — revision 65
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
