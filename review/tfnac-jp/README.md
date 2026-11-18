# theme:tfnac-jp — The Foundation Network AssCO11 theme (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:tfnac-jp — origin CN, population #236 [GOSIGN2-LEDGER (b) row 236]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now abec21eaf0bbfd529c8824651e62e9c4a4a3675c615071328f985c1e7e5b5d3e); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 0 infos (old-bhl×2, hotlink×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 196; GOSIGN2-LEDGER (b) row 236]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 507px@320/375 + 782px@768 (page) and 519px@320/375 + 883px@768 (sample) + runtime-hotlink site-theme chain + candidate hosts nu-scptheme.github.io, s1.ax1x.com; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN15)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN15)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 235, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 235]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 236]
- Computed against: canonical commit fdec3533e70523dede654707a79aeb8e959a0905; candidate file pages/theme:tfnac-jp.txt sha256:abec21eaf0bbfd529c8824651e62e9c4a4a3675c615071328f985c1e7e5b5d3e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

This file is the explanation record for one theme's Sigma-10 port. The
diff it explains is `diff.md` in this directory, generated from
`original.txt` (the frozen mirror) and `candidate.txt` (a byte copy of
the canonical candidate). The verdict stamp at the head of this file is generated; do not
edit inside the stamp markers.

## Provenance

- Theme: `theme:tfnac` on scp-wiki-cn (CN branch), revision 3.
  Author Liurd; a Sigma+ based theme made for the "Shattering the
  Snow Globe" setting in the CN 2023 canon contest.
- Frozen mirror: `original.txt`, 624 lines, 13,491 bytes, SHA-256
  `a39356c788b719ce55c2f1951cd2fa66f4cb969424088bff064a1ce16fa8d31c`
  (matches `review/sources.tsv`; mirror-store class COPY).
- Candidate: `candidate.txt`, 632 lines, 14,701 bytes, SHA-256
  `60eb7d174db96fdde58d1fc327a6bf13c35b2c7c35c083acc00bc6d330a6b67e`,
  byte-identical to the canonical file.
- Kind (sources.tsv): standard. Route: derived from the original at
  revision 3 (LOCALIZE-S2-E wave, CN15 batch).
  `review/sources.tsv` records the original as superseded upstream
  since the reference revision, with a follow-up diff artifact in
  the campaign record (section 12).
- The candidate entered the canonical repository in the Stage 2 CN15
  integration (9f252b5) and was touched twice since: by the
  Sigma-Plus shared-receiver rework (2d69b1c, rework2-p3 — the
  commit that put the base include into its current form,
  section 2) and by the credit attribution normalization (1869877,
  FIX-CREDIT-D).

## Summary

A Sigma+ theme whose port is mostly a translation exercise over a
reconstructed stylesheet: the original page carries no CSS of its
own in code form (its style module hides behind a negative-tag div
trick at the tail), and the candidate gathers that CSS into a typed
code exhibit delivered by a tail import and a priority-1 frame. The
furniture swaps are standard (CN credit trio and labelled bare Rate
out; one preview credit block in), the base include names the JP
Sigma+ port, and T4's five pattern charges are all dispositioned in
the ledger. Three things in the bytes deserve a reviewer's
attention. The sample-code collapsible that exhibits the theme's
credits snippet in the original is empty in the candidate: the
snippet survives, untranslated, folded into the tail of the CSS
exhibit instead (flagged in the per-theme record). The CN credit
module's two label lines survive as orphan prose under the new
credit block. And the usage exhibit names the plain slug, the known
sweep family. The header slogan is the author's CN gag line, kept
verbatim under a ruling-2 disposition.

## Class summary (auto-classification)

51 change blocks: 25 specific (49.0%), 25 heuristic (49.0%),
1 residue (2.0%), 0 skipped. The generator counts +121 / −119 lines
(diff.md is Tier 1 format: 3 hunks). Label firings: TRANS-UNANCHORED
×30, TRANSLATION-ANCHORED ×17, IFTAGS ×2, DELIVERY-MOVE ×2,
DRAFT-HOST ×2, SELF-DELIVERY ×2, EXHIBIT-RESTRUCTURE ×2, and single
firings of COMPONENT-SWAP, INCLUDE-REPOINT, SIGMA-PLUS-JP,
BARE-RATE-DEL, CREDIT-PREVIEW, CREDIT-PROSE, TASL-FIELDS, GLYPH-FORM,
COMMENT-TEXT, RESTORATION. The classifier also derives an
OLD-BHL-KEPT presence: 2 references to the EN BHL project's logo
file inside the delivered CSS (candidate L209, L213), class (ii)
posting rewrite.

Adjudication notes: both EXHIBIT-RESTRUCTURE primaries were checked
against the exhibit census — B1 is the base-include swap at the
file's head (section 2), and B47 is the sample-code collapsible of
section 8, which is a genuine content displacement, not a repoint
false-fire. The RESTORATION firing (B50) marks the displaced
credits snippet at its new position inside the CSS exhibit
(section 8). The heuristic mass is the documentation body's
translation blocks, counted per the class-M convention.

## 0. Tag frame and page furniture

**What.** The candidate's frame stands at the tail, after the gate
closes: an interwiki-style include at priority 1 naming the
candidate's own `local--code/…/1` on the draft host (candidate
L629–632), preceded by the tail delivery module (section 3). The
gate converts from `[[iftags +版式]]` to `[[iftags +テーマ]]`
(candidate L3, blocks B2 and B49, IFTAGS ×2 — the second firing is
the original's negative-tag interlude, section 8). The original has
no frame include; its head is the base include (section 2).

**Why.** Pattern class P1 (frame and tag furniture; KB-03, KB-04).
Failure prevented: a gate keyed to the CN tag name never opens on
scp-jp, and a theme without the priority-1 frame does not receive
its CSS in the check environment.

**Verify.** `grep -n 'iftags\|interwiki-style' candidate.txt` —
gate at L3 with the JP tag name, frame at the tail with priority 1.

**Disposition.** T4 charged this theme's frame-adjacent item as
pattern 1 (the base include's 404 at check time); ledger part (c3)
dispositions P1 under the posting-procedure convention class, and
the include's current form is section 2. The (b) verdict is PASS.

## 1. Credit block and license (P3, P9)

**What.** The original's credit furniture is a labelled bare Rate
(`**评分：**` over `[[module Rate]]`, original L4–7) under a second
label （评分模块与著作信息模块）, plus the CN credit trio
`credit:start` / `credit:more` / `credit:end` (original L12–16) whose
clickable label texts are 页面信息 and 更多页面信息. The candidate
deletes the Rate (block B2, BARE-RATE-DEL) and the trio, and carries
one preview credit block (candidate L5–14, block B3: CREDIT-PREVIEW,
CREDIT-PROSE, TASL-FIELDS) with eight fields: title
版式：The Foundation Network AssCO11; translator of record AI;
translation year 2026; original title the same; copyright holder
Liurd; creation year 2023; reference revision 3; and a source link
to `https://scp-wiki-cn.wikidot.com/theme:tfnac` — the host
`review/sources.tsv` records, so the host check passes. The author
field agrees with the original's prose credit and with the credits
div the page exhibits (作者： → 著者： Liurd, block B46, GLYPH-FORM —
the label's glyph conversion inside the live div).

One residue of the old furniture survives: the trio's two label
lines stand as bare prose under the credit block （ページ情報 /
追加のページ情報, candidate L16–17), the module they labelled having
been deleted. They are flagged in the per-theme record (item 2).

**Why.** Pattern class P3 (credit furniture swap; KB-16, KB-17) with
P9 (attribution; KB-47). Failure prevented: CN credit components do
not exist on scp-jp, and a bare Rate beside the credit block renders
a second rating widget.

**Verify.** `sed -n '5,17p' candidate.txt` against original L4–16;
`grep -c 'module Rate' candidate.txt` returns 0.

**Disposition.** No ledger line charges this theme's credit fields;
the (c3) line for this theme covers patterns 1, 4, 5, 9, 11 only.
Neither side carries a license box, so there is no P9 license-box
conversion to record; no credit CSS supplement exists on either
side. The (b) verdict is PASS.

## 2. Includes and component references (P2, P8)

**What.** The base include converts at the file's head:
`[[include :scp-wiki-cn:component:sigma-plus]]` →
`[[include component:sigma-plus-jp]]` (candidate L1, block B1:
COMPONENT-SWAP, INCLUDE-REPOINT, SIGMA-PLUS-JP) — the bare same-site
form naming the JP Sigma+ port, which is delivered in this
repository (`pages/component:sigma-plus-jp.txt`). At T4 check time
the include named a form that returned 404 and the theme rendered
unstyled (the row's one display-affecting finding); the
shared-receiver rework (2d69b1c) put it into the current form. The
usage exhibit repoints `:scp-wiki-cn:theme:tfnac` →
`:scp-jp:theme:tfnac` (candidate L23, residue block B7). The
image-block exhibit keeps its unprefixed component name, as the
original had it; its asset is section 4. The frame and credit
includes are sections 0 and 1.

**Why.** Pattern classes P2 (include repoints; KB-05) and P8
(exhibit fidelity; KB-42, KB-43). Failure prevented: a base include
naming a page that does not exist leaves the theme unstyled — the
exact failure T4 caught — and an exhibit pointing at the origin
branch shows readers a page that is not the one this candidate
installs.

**Verify.** `sed -n '1p' candidate.txt`;
`grep -n 'scp-wiki-cn:' candidate.txt` returns nothing;
`ls pages/component:sigma-plus-jp.txt` in the repository root
confirms the include's target is delivered.

**Disposition.** The base include's charge (pattern 1) is
DISPOSITIONED in part (c3) under the posting-procedure convention
class; the bytes go further than the disposition, since the include
now names a delivered page. Two flags ride on this section, both in
the per-theme record: the usage exhibit names the plain slug
`:scp-jp:theme:tfnac` where the posting name is `theme:tfnac-jp`
(item 3, the sweep family), and the prose link beside it names
`component:sigma-plus` without the `-jp` form its own include uses
(item 4).

## 3. Delivery topology (P4)

**What.** The original's own CSS is delivered by a
`[[module CSS show="true"]]` inside a collapsible in the source
section at the page's tail (original L151 onward), placed outside
the main gate behind a negative-tag hidden-div interlude
(section 8). The candidate restructures the delivery into the
family's standard form: the CSS stands as a typed code exhibit
(candidate L143–621) whose head carries a porter comment identifying
it as the gathered original CSS (section 10); a tail module imports
the exhibit's delivery
(`https://sigma10-jp-test.wdfiles.com/local--code/theme%3Atfnac-jp/1`,
candidate L625–628, blocks B50–B51, SELF-DELIVERY ×2); and the frame
names the same URL at priority 1 (section 0). DELIVERY-MOVE fires
twice (B47, B50). Inside the delivered CSS, two references to the EN
BHL project's logo file stand (candidate L209, L213:
`mask-image: url(https://nu-scptheme.github.io/Black-Highlighter/img/logo.svg)`)
— the classifier's OLD-BHL-KEPT presence, and T4's pattern-4 charge
(the BHL logo ×2 in the exhibit).

**Why.** Pattern class P4 (delivery topology; KB-23). Failure
prevented: a delivery hidden behind a tag trick and a `show="true"`
module is one edit away from silently not applying; the exhibit +
import + frame form is the shape the check environment and the JP
site both apply deterministically.

**Verify.** `sed -n '625,632p' candidate.txt`;
`grep -n 'nu-scptheme' candidate.txt` returns the two mask-image
lines and nothing else.

**Disposition.** Ledger part (c3) dispositions pattern 4 as
"delivery class (ii): original-state CDN delivery", and register
c1's old-bhl entry (ledger part (c1), KB-17) dispositions the
nu-scptheme references as a posting-time rewrite to
scp-jp.github.io/Black-Highlighter. The two mask-image lines stand
under those dispositions. The draft-host form of the own delivery
URL is environment class (iii) (KB-41). The (b) verdict is PASS.

## 4. Fonts and assets (P5, P7)

**What.** The theme loads no fonts of its own on either side; the
Sigma+ base supplies the faces, so there is no P7 event in this
pair. The one asset is the usage exhibit's photograph: the
image-block exhibit names
`https://s1.ax1x.com/2023/04/11/ppqxqrn.jpg` (candidate L29), a CN
image host, unchanged from the original (original L29). Its caption
credits the photograph's source through an Unsplash mirror link,
carried with the exhibit. Probed once on 2026-11-17, the ax1x URL
returned no HTTP response at all (curl status 000 — the host did
not answer), against the render lane's record that the pages render
styled today; the exhibit image is exactly the kind of reference
the posting-time rewrite exists to replace.

**Why.** Pattern class P5 (assets; KB-25, KB-26). Failure prevented:
an exhibit photograph hotlinked from an unmaintained image host
breaks silently when the host goes, taking the theme's only usage
illustration with it.

**Verify.** `sed -n '29,30p' candidate.txt`; the probe above can be
re-run with one `curl -sI` against the exhibit's URL.

**Disposition.** T4 charged the image as pattern 5; part (c3)
dispositions P5 as class (ii) / KB-58, and part (c2) dispositions
the candidate's foreign hosts (nu-scptheme.github.io, s1.ax1x.com)
as the posting-time rewrite class (KB-41/KB-54 family), recording
that no error-box defect arises from them today. The probe result
is recorded in the per-theme record (item 5) as the current
evidence under that disposition.

## 5. Header, titles and rendered strings (P6)

**What.** The delivered CSS sets `--header-title: "S · C · P"` and
`--header-subtitle: "控制，收容，保护...？"` (candidate L147–148,
inside the exhibit's `:root`). The subtitle is the author's gag
line — the CN motto in its CN order with a puzzled ellipsis —
carried verbatim, simplified glyphs and all, from the original's
module (original L156–157). It is a rendered string on every page
the theme styles, and it is also the work's joke: the theme is a
parody Foundation network whose masthead doubts the motto.

**Why.** Pattern class P6 (header and rendered strings; KB-29,
KB-30, KB-31). The class's failure mode is an untranslated masthead;
here the untranslated form is the content, not an oversight, which
is why the lane's charge and the ledger's answer take the shape
they do.

**Verify.** `grep -n 'header-subtitle' candidate.txt` — one line,
the CN string; the same string in `original.txt` at L157.

**Disposition.** T4 charged the slogan as pattern 9; part (c3)
dispositions P9 under ruling 2 (header/title language is out of
scope for migration correctness). It stands by that disposition and
is not flagged. (The sibling case in this batch, sodium-pentasulfide,
differs in the one respect that matters: no ledger line dispositions
its subtitle.)

## 6. Body translation (P10)

**What.** The documentation body is translated throughout: 17
TRANSLATION-ANCHORED blocks and 30 TRANS-UNANCHORED blocks (counted
class treatment, per the class-M convention) covering the intro
prose, the usage instructions, the heading and tab exhibits, the
credits div （作者： → 著者：, block B46), and the collapsible labels.
The CSS comments inside the exhibit cross with the CSS; the
exhibit's own head comment is the porter's (section 10). One
translation exception stands inside the file: the credits snippet
in its code-exhibit copy keeps its CN text （打碎雪景球 / 作者：,
candidate L613–621) although the same snippet's live rendering is
translated — that copy's placement is the section-8 item, and its
untranslated state is recorded with it.

**Why.** Pattern class P10 (translation; KB-50, KB-51). Failure
prevented: untranslated documentation makes the candidate unusable
as a JP theme page.

**Verify.** Spot-check any anchored block against diff.md (e.g.
B44, the credits prose); `grep -n '著者' candidate.txt` shows the
live div translated.

**Disposition.** T4/T5 judged this theme FINDINGS jointly; the
translation-side charges are the pattern items of sections 2–5.
The (b) verdict is PASS.

## 7. Link targets (P11)

**What.** Two reader-facing links in the prose name targets this
repository does not deliver: the Sigma+ link
(`[[[component:sigma-plus|Sigma+]]]`, candidate L25), whose
delivered JP form is the `component:sigma-plus-jp` the file itself
includes at L1; and the contest hub link
(`[[[2023-canon-contest-hub|2023年カノンコンテスト]]]`, candidate
L19), the CN branch's 2023 canon contest page, which has no JP
counterpart in this repository. The remaining links are the credit
source link (recorded host, section 1), the author user-link, and
the exhibit caption's source link (section 4).

**Why.** Pattern class P11 (link targets; KB-54). Failure prevented:
a prose link naming a page the JP site will not have strands the
reader — and in the Sigma+ case the correct target exists and is
already named correctly elsewhere in the same file.

**Verify.** `grep -n 'component:sigma-plus\]\|component:sigma-plus|' candidate.txt`
against `sed -n '1p' candidate.txt`.

**Disposition.** T4 charged two dead reader links as pattern 11;
part (c3) dispositions P11 under the sibling / batch-posting class.
The disposition asserts the targets arrive with the batch posting;
for the Sigma+ link the batch's own delivery contradicts it (the
delivered page is the `-jp` form). The pair is flagged in the
per-theme record (item 4) with the disposition noted.

## 8. Structural fidelity and exhibit census (P8, R3)

**What.** The exhibit census is mostly preserved — usage exhibit,
image-block exhibit, heading and tab exhibits, the live credits
div, the footnoteblock, and the source section all stand in the
original's order — with one genuine displacement and one structural
simplification:

1. **The sample-code exhibit lost its body at its position.** The
   original's `+ 展开示例代码` collapsible (original L127–138)
   exhibits the theme's credits snippet as a `[[code]]` block. The
   candidate's corresponding collapsible (candidate L127–130,
   `+ サンプルコードを開く`) is empty. The snippet itself survives —
   folded, untranslated, into the tail of the CSS code exhibit
   (candidate L613–621, immediately before its `[[/code]]`), where
   it sits as non-CSS text inside a CSS block. Block B47 records
   the exchange at the original position; the classifier's
   RESTORATION firing in B50 marks the snippet at its new one.
2. **The source section's gate trick is gone.** In the original,
   the source section stands outside the main gate, its delivery
   module wrapped in a collapsible behind a
   `[[div [[iftags -版式]]style="display: none"[[/iftags]]]]`
   interlude (original L150–154, block B49). The candidate puts its
   source exhibit inside the gate in a plain collapsible and
   delivers by tail import (section 3). No content is lost in the
   simplification; the CSS text is the same.

**Why.** Pattern class P8 (structural fidelity; KB-42, KB-43) and
residue class R3 (a source element whose form or position changed).
Failure prevented: an exhibit shell left empty at its documented
position teaches the next reader that the theme has no credits
snippet to copy — the snippet is the theme's attribution mechanism,
so its exhibit is the one a user copies it from.

**Verify.** `sed -n '127,130p' candidate.txt` (empty) against
original L127–138; `sed -n '613,621p' candidate.txt` (the displaced
snippet).

**Disposition.** No ledger line charges either item — the checks do
not compare exhibit positions. The displacement is flagged in the
per-theme record (item 1). The (b) verdict is PASS.

## 9. Formatting-only changes (R4)

**What.** None. The classifier reports no whitespace-only block and
no re-indentation block for this pair. The size delta (+121 / −119)
is content: translations, the credit swap, and the delivery
restructure.

**Why.** Residue class R4 has no instance here; the ground is the
classifier's zero counts for both signatures across 51 blocks.

**Verify.** `grep -c 'WS-ONLY' classification.json` returns 0.

**Disposition.** Nothing to disposition.

## 10. Porter annotations (R2)

**What.** One annotation, in CSS-comment form at the delivered
exhibit's head (candidate L144):
`/* ===== tfnac：原語版の CSS をまとめたもの ===== */` — "tfnac: the
original-language CSS, gathered". It is the in-file record that the
exhibit is a reconstruction of CSS the original page carried only
inside its tail module (section 3), and it is accurate. The
candidate contains no `[!-- --]` comments.

**Why.** Residue class R2 (porter annotations). This one documents
the delivery reconstruction; removing it would orphan the exhibit's
provenance.

**Verify.** `sed -n '144p' candidate.txt`;
`grep -c '\[!--' candidate.txt` returns 0.

**Disposition.** No ledger line charges the annotation.

## 11. Dispositioned deviations (class (ii) / (iii) summary)

**What.** The deviations a reader of the diff might otherwise charge
against the candidate, with their dispositions:

- T1's findings (T1-ROWS row 196: exit 1, 4 errors / 2 warns) are
  old-bhl ×2 (the mask-image references of section 3, register c1's
  KB-17 posting-rewrite class), hotlink ×1 (the ax1x exhibit image,
  section 4), and pseudo-ref ×1 (the frame include). Environment
  class (ii).
- The render check's items (RENDER-ROWS-G, CN15) are all
  DISPOSITIONED in ledger part (c2): page-overflow 507px at 320/375
  and 782px at 768 on the page, 519px and 883px on the sample, in
  the recorded cross-cutting families (static credit replica fixed
  width at mobile widths, KB-33; preview chrome, KB-34); the
  runtime-hotlink site-theme chain plus the candidate's own foreign
  hosts, under the posting-time rewrite class (KB-41/KB-54 family);
  and the sample credit-modal, the preview form's known property
  (KB-32). The T3 re-run recorded no new screenshot-grounded visual
  finding. Coverage caveat, not a finding: chromium-only (no WebKit
  verdict).
- The pattern dispositions (P1, P4, P5, P9, P11) are sections 2–7.
- The draft-host form of the delivery URLs is environment class
  (iii) (KB-41).

**Why.** These classes exist so a reviewer does not re-litigate
environment properties as candidate defects; each item above names
its record so the disposition can be re-checked at its source.

**Verify.** The theme's rows in `review/AUTHORITIES/ledger-parts/`
(T1-ROWS row 196, RENDER-ROWS-G) and its blocks in
`GOSIGN2-LEDGER.md` parts (c1), (c2), and (c3).

**Disposition.** All items above are DISPOSITIONED in the cited
records. The items the records do not reach are the per-theme record
below.

## 12. Verification history

**What.** T1 (source check): FINDINGS (classified), 4 errors in the
standing classes — T1-ROWS row 196. T2/T3 (render check): FINDINGS,
all items dispositioned in (c2); chromium-only coverage —
RENDER-ROWS-G (CN15). T4/T5 (localize check): FINDINGS with 1
display-affecting item (pattern 1, the base include) and four
further pattern charges (4, 5, 9, 11), all dispositioned in (c3) —
LOCALIZE-ROWS row 235 (LOCALIZE-S2-E). Follow-up state:
`review/sources.tsv` records the original as superseded upstream
since revision 3, and the campaign record holds the follow-up diff
artifact `diff-tfnac-from3.txt` (class K5a-i); this package's
baseline remains revision 3, the revision the port was made from.
The (b) verdict is PASS, with no OPEN items at the determination
and no FIX5 re-judgement.

**Why.** The verification section exists so the reader can see which
checks ran, what they found, and what became of each finding,
without re-running the campaign.

**Verify.** The cited rows; the stamp at the head of this file is
generated from the same records by `review/build_review.py`.

**Disposition.** Verdict: PASS (go-sign ledger part (b)), with the
flags below carried for the coordinator.

## Per-theme record: tfnac-jp

**Item 1 — the sample-code collapsible is empty; its snippet is
displaced and untranslated (flag, not edited).** Candidate
L127–130: the `+ サンプルコードを開く` collapsible opens and closes
with nothing inside. The original's collapsible (original
L127–138) exhibits the credits snippet as a code block. The snippet
text survives at candidate L613–621, folded into the tail of the
CSS code exhibit as non-CSS lines, with its CN text untranslated
（打碎雪景球 / 作者：) although the same snippet's live rendering at
candidate L113–121 is translated. A reader following the
documentation finds an empty exhibit at the documented position and
the snippet only by reading the CSS block to its end. The repair
(moving the snippet back into its collapsible, translated to match
its live twin) belongs to the coordinator's repair lane.

**Item 2 — orphaned credit-module label lines (minor flag).**
Candidate L16–17 （ページ情報 / 追加のページ情報） are the deleted CN
credit trio's clickable labels, left as free-floating prose under
the new credit block with no module around them. The same shape as
the empty-label items charged on sibling themes; uncharged here.
Two lines; the repair is deletion.

**Item 3 — usage exhibit names a plain-slug page (sweep family).**
Candidate L23: `@@[[include :scp-jp:theme:tfnac]]@@`. The posting
name is `theme:tfnac-jp`; the snippet names a page that will not
exist. Flagged for the population sweep; not edited.

**Item 4 — the P11 pair, with the disposition noted (flag).** The
prose links at candidate L19 (contest hub) and L25
(`component:sigma-plus`) name pages this repository does not
deliver. Part (c3) dispositions pattern 11 under the sibling /
batch-posting class. For the contest hub that may prove right at
posting time; for the Sigma+ link it cannot — the batch delivers
the component as `component:sigma-plus-jp`, the very form the
file's own L1 include uses after the shared-receiver rework. The
prose link was not carried along by that rework. Recorded with both
loci so the posting step does not mistake the disposition for the
repair.

**Item 5 — the ax1x exhibit image did not answer (probe evidence).**
The image-block exhibit's photograph (candidate L29,
`https://s1.ax1x.com/2023/04/11/ppqxqrn.jpg`) returned curl status
000 on 2026-11-17 — no HTTP response — where the render lane's
record has the pages rendering styled. The reference stands under
the (c2)/(c3) posting-time dispositions (section 4); the probe is
recorded so the reflection step knows the origin copy may already
be unreachable, which makes the re-hosting half of the rewrite
load-bearing rather than cosmetic.

### Post-package repairs (REFRESH3-F)

**FIX-STELLAR, landing `2dbb83d` (report `R/review-scout/FIX-STELLAR.md`, item 3,
"theme:tfnac-jp").** This landing postdates the package build
(`7170328`) and repairs items 1, 2 and the Sigma+ half of item 4. Three
candidate changes: (a) the credits snippet restored into the empty
sample-code collapsible (as-built L127–130), translated to match its live
twin byte for byte (雪景球を打ち破る / 著者： [[*user Liurd]]), and the
displaced, untranslated copy at the CSS exhibit's tail (8 lines) removed;
(b) the two orphaned credit labels ページ情報 / 追加のページ情報 and one
surrounding blank line removed (as-built L16–17) — the JP preview credit
block has no "more" boundary for them to head; (c) the prose link
`[[[component:sigma-plus|Sigma+]]]` → `[[[component:sigma-plus-jp|Sigma+]]]`,
the form the candidate's own L1 include uses. Item 3's usage-example flag
belongs to an earlier sweep, not to this landing. Checker per the report:
error 4 / warn 2 / info 0 before and after; the only delta is the L25
warn's target changing to `component:sigma-plus-jp` (the standing
posting-time class), with no new class (i) error. This package documents
the corrected candidate; its stamp reads STALE against the pre-repair
verdict, by design.

## Change set

Delivered with this candidate in the canonical repository: the
candidate page itself (`pages/theme:tfnac-jp.txt`), its decoration
sample (`pages/theme-decoration-sample-tfnac-jp.txt`), and the base
component it includes (`pages/component:sigma-plus-jp.txt`, a
campaign-shared port with its own record). The candidate's own
history is three commits: the Stage 2 CN15 integration, the
shared-receiver rework, and FIX-CREDIT-D.

## Appendix: residue resolution

The classifier left 1 block unlabeled (2.0%). Per the class-M
convention it is resolved here by shape.

| Block | Lines (orig → cand) | Resolution |
|---|---|---|
| B7 | 22 → 23 | The usage exhibit line itself: the repoint `:scp-wiki-cn:theme:tfnac` → `:scp-jp:theme:tfnac` (section 2; the plain-slug flag is item 3). The classifier's repoint signature did not fire on the @@-escaped form here. |

## Post-adjudication repair (2026-11-18)

The pattern linter's KB-70 nomination, adjudicated in the campaign record (theme-lint/ADJ1.md section 3.4), confirmed a code-address defect: the candidate delivers its stylesheet as code block /2, but both self-addresses (the [[module CSS]] @import and the interwiki-style include's theme= parameter) pointed at /1, which holds the credits exhibit. Both addresses are repointed to /2 in the canonical page; no other byte changed. T1 finding counts are unchanged (error 4 / warn 2 before and after); the page is reflected to the Wikidot check wiki.

## License and attribution

- **Title:** 版式：The Foundation Network AssCO11
- **Author:** Liurd
- **Source:** https://scp-wiki-cn.wikidot.com/theme:tfnac — revision 3
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
