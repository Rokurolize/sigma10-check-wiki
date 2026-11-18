# theme:some-guider-jp — Some Guider theme (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:some-guider-jp — origin KO, population #285 [GOSIGN2-LEDGER (b) row 285]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now fb3838f4754e86bae11390b7c9408856029cdb4eb47b3069b27366468ec08e71); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 12 errors / 1 warn / 1 info (hotlink×11, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 255; GOSIGN2-LEDGER (b) row 285]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — runtime-hotlink site-theme chain + scpko.wdfiles.com / scpko.wikidot.com on both pages; sample credit-modal (preview-form), no sample overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO8))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO8))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 284, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 284]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 285]
- Computed against: canonical commit 1e3da43416851307b491da1cf4cadf7bc1f61850; candidate file pages/theme:some-guider-jp.txt sha256:fb3838f4754e86bae11390b7c9408856029cdb4eb47b3069b27366468ec08e71; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

This file is the explanation record for one theme's Sigma-10 port. The
diff it explains is `diff.md` in this directory, generated from
`original.txt` (the frozen mirror) and `candidate.txt` (a byte copy of
the canonical candidate). The verdict stamp at the head of this file is generated; do not
edit inside the stamp markers.

## Provenance

- Theme: `theme:some-guider` on scpko (KO branch), revision 17.
  Author c_bonefish, who made it for the Guiding Light (조요의 인도자)
  GoI format and similar works — stated in the original's prose
  (original L25) and carried in the candidate's (candidate L25).
- Frozen mirror: `original.txt`, 783 lines, 16,607 bytes, SHA-256
  `dc43986560317f8774951a0bd51585ac0ce21cfc08b059d440259c424b7fbc5a`
  (matches `review/sources.tsv`; mirror-store class COPY).
- Candidate: `candidate.txt`, 801 lines, 17,457 bytes, SHA-256
  `c7a6745887cb9f39e3c3bd5f863a951a08d30e4049a96dacd14005c4266e23fd`,
  byte-identical to the canonical file.
- Kind (sources.tsv): standard. Route: derived from the original at
  revision 17 (LOCALIZE-S2-F wave, KO8 batch).
- The candidate entered the canonical repository in the Stage 2 KO8
  integration (28aaab2) and was touched once since, by the credit
  attribution normalization (1869877, FIX-CREDIT-D). That later touch
  matters for section 1: the ledger records this theme's credit
  fields as fixed, and the bytes do not support the record.

## Summary

A compact, mostly mechanical port: the gate is renamed, the KO credit
furniture (a labelled bare Rate and an info-module pair) is replaced
by a preview credit block plus a static rendering of the info box,
the usage exhibit and frame are repointed, the code exhibit is
wrapped in a collapsible, and the CSS body crosses with only its
colon encodings changed. Three findings dominate the record, all of
them cases where the ledger's dispositions and the candidate's bytes
tell different stories. First, the credit block's author field names
no author and the wrong branch — `CN 支部の作者` for a KO theme by
c_bonefish — although ledger part (c3) records this theme's P3 credit
fields as FIXED. Second, the theme's font import (YoonDokrip) was
deleted while its stacks still name the family, so the display text
the font carried falls back. Third, the theme's image assets still
load from the KO wiki's file host; the registers disposition them as
a posting-time rewrite, which the per-theme record examines with
probe evidence. The four Korean `content:` strings in the CSS stand
by disposition (ruling 2), and the usage exhibit names a plain-slug
page that will not exist (the sweep family).

## Class summary (auto-classification)

26 change blocks: 19 specific (73.1%), 5 heuristic (19.2%), 2 residue
(7.7%), 0 skipped. The generator counts +55 / −42 lines. Label
firings: COLON-ENC ×6, TRANS-UNANCHORED ×9, TRANSLATION-ANCHORED ×5,
SELF-DELIVERY ×3, IFTAGS ×2, EXHIBIT-RESTRUCTURE ×2, and single
firings of CREDIT-PREVIEW, CREDIT-PROSE, TASL-FIELDS, BARE-RATE-DEL,
INFO-DEL, ESCAPED-INCLUDE, INCLUDE-REPOINT, JPFONT-LOAD, CSS-BODY,
DRAFT-HOST.

Adjudication notes: both EXHIBIT-RESTRUCTURE primaries were checked
against the exhibit census — B2 is the credit-zone furniture exchange
(section 1) and B10 is the image-block line, whose only change is its
caption's translation (the restructure signature false-fires on it;
the host question is section 4). The single CSS-BODY block (B17) is
adjudicated in section 4: it is the deleted font import, a P7 event
whatever its label says.

## 0. Tag frame and page furniture

**What.** The candidate's frame include stands at the tail, after the
gate closes (candidate L797–801): `:scp-jp:component:interwiki-style`
at priority 1 naming the candidate's own `local--code/…/1` on the
draft host. The original's frame stood at the head (original L5–8)
and named `:scp-wiki:component:interwiki-style` — the EN component
prefix, the original's own choice on the KO site — with the theme URL
on scpko. The gate converts from `[[iftags +테마]]` to
`[[iftags +テーマ]]` and moves to the file's first line (blocks B1,
B3; IFTAGS ×2).

**Why.** Pattern class P1 (frame and tag furniture; KB-03, KB-04).
Failure prevented: a gate keyed to the KO tag name never opens on
scp-jp, and a frame naming the origin wiki's component and code URL
applies the wrong delivery in the check environment.

**Verify.** `grep -n 'interwiki-style\|iftags' candidate.txt` — gate
at L1 with the JP tag name, frame at the tail with priority 1.

**Disposition.** No ledger line charges the frame or its placement.
The (b) verdict for this theme is PASS.

## 1. Credit block and license (P3, P9)

**What.** The original's furniture is a labelled bare Rate
(`**평가 모듈:**` over `[[module Rate]]`, original L14–17) and an
info-module pair (`[[include info:start]]` / `[[include info:end]]`,
original L21–23) under a second label. The candidate deletes the Rate
(block B4, BARE-RATE-DEL) and the info pair (block B6, INFO-DEL), and
carries a preview credit block (candidate L3–11, blocks B2:
CREDIT-PREVIEW, CREDIT-PROSE, TASL-FIELDS) with eight fields:
translator of record AI; translation year 2026; creation year 2023;
reference revision 17; a source link to
`https://scpko.wikidot.com/theme:some-guider` (the host
`review/sources.tsv` records — the host check passes); title and
original title both given as 어떤 길잡이 CSS 테마; and the author
field given as `**著作権者:** CN 支部の作者` (candidate L8).

Below the preview block, the candidate renders the info box's content
as static prose (candidate L21–25): title とある導き手CSSテーマ,
translator `[[*user kkaacc]]`, author c_bonefish (with a joke line),
followed by the prose crediting c_bonefish that the original also
carries. The two furniture labels survive above these blocks:
`**評価：**` over an otherwise empty right-aligned div
(candidate L14–16) and `**評価モジュールとクレジットモジュール：**`
over the static prose (candidate L18–20).

**Why.** Pattern class P3 (credit furniture swap; KB-16, KB-17) with
P9 (attribution; KB-47). Failure prevented, in the design: KO credit
components do not exist on scp-jp, and a bare Rate beside the credit
block renders a second rating widget.

**Verify.** `sed -n '3,25p' candidate.txt` against original L12–25.
The author question decides itself from the file: `grep -n 'c_bonefish'
candidate.txt` returns the prose credit (L23, L25) naming the author
the credit field does not.

**Disposition.** Ledger part (c3) records "P3 credit fields FIXED
(credit waves; checker-verified)" for this theme. The bytes do not
support the record, and this package flags the disagreement rather
than repeating the disposition (per-theme record, item 1): T4's
charges against this furniture (LOCALIZE-ROWS row 284: the "CN branch
author" factual error, the second credit-style block, the two empty
labels, and the Korean title field) all still stand in the candidate.
Neither side carries a license box, so there is no P9 license-box
conversion to record; no credit CSS supplement exists on either side.

## 2. Includes and component references (P2, P8)

**What.** The usage exhibit repoints `:scpko:theme:some-guider` →
`:scp-jp:theme:some-guider` (block B8, INCLUDE-REPOINT and
ESCAPED-INCLUDE, candidate L28). The frame and credit includes are
sections 0 and 1. The image-block exhibit (candidate L35) keeps its
component name unprefixed, as the original had it; its asset is
section 4. No other live include exists in the file.

**Why.** Pattern classes P2 (include repoints; KB-05) and P8
(exhibit fidelity; KB-42, KB-43). Failure prevented: an exhibit
pointing at the origin branch shows readers a page that is not the
one this candidate installs.

**Verify.** `grep -n 'scpko:' candidate.txt` returns nothing;
`grep -n 'include' candidate.txt` lists the frame, the credit pair,
the usage exhibit, and the image-block exhibit.

**Disposition.** One flag rides on this section, of the known sweep
family: the usage exhibit names `:scp-jp:theme:some-guider`, the
plain slug, where the candidate's posting name is
`theme:some-guider-jp` — the pasted snippet names a page that will
not exist on scp-jp (candidate L28; per-theme record, item 3). A
population sweep owns this family's repair; the candidate is not
edited here.

## 3. Delivery topology (P4)

**What.** The original delivers from the head: a module importing its
own code from `https://scpko.wikidot.com/local--code/theme%3Asome-guider/1`
(original L1–3, block B1, SELF-DELIVERY on the origin side), with the
code exhibit (original L60–781) as the delivery's source. The
candidate deletes the head module and delivers from the tail: a
module importing its own
`https://sigma10-jp-test.wdfiles.com/local--code/theme%3Asome-guider-jp/1`
(candidate L795–797, block B26), followed by the frame include naming
the same URL (section 0). The code exhibit stands on both sides as
the delivered content; the candidate wraps it in a collapsible
(section 8). Topology otherwise matches: no base theme on either
side, no relocation of the stylesheet body (the classifier reports
no moves).

**Why.** Pattern class P4 (delivery topology; KB-23). Failure
prevented: a candidate still importing its CSS from the origin wiki
is not a self-contained Sigma-10 candidate; the tail placement keeps
the delivery outside the tag gate, as the frame requires.

**Verify.** `sed -n '794,801p' candidate.txt` against original
L1–8; `grep -n 'local--code' candidate.txt` shows only the
candidate's own draft-host delivery.

**Disposition.** The draft-host form is environment class (iii)
(KB-41). No ledger line charges the topology. The (b) verdict is
PASS.

## 4. Fonts and assets (P5, P7)

**What.** Fonts first, because they carry a defect. The original's
code exhibit opens with an import of the YoonDokrip display font
from the KO files host (original L72:
`@import url('https://scpko.wdfiles.com/local--files/yoonfont/YoonDokrip.css')`)
and uses `'YoonDokrip', sans-serif` in two stacks (original L159,
L180) — the stacks that set the theme's motto text (section 5). The
candidate deletes the import (block B17, labeled CSS-BODY; the
candidate's corresponding lines are blank) and adds one Google Fonts
import of Noto Sans JP at the exhibit's head (candidate L69, block
B16, JPFONT-LOAD) — but the two stacks still name `'YoonDokrip'`
(candidate L169, L190), a family no import or `@font-face` in the
file loads. The port is internally inconsistent: either the font
load or the stack names had to change, and only the load did.

Assets: the candidate's CSS still references the theme's images on
the origin host — `background.png` (candidate L102), `logo1.png`
(L124), `logo2.png` (L142), five sidebar images on one line (L404),
`sidebar-menu-1.png` (L689) and `sidebar-menu-2.png` (L699), all
under `https://scpko.wikidot.com/local--files/theme:some-guider/…`
with the colon now percent-encoded (blocks B18–B23, COLON-ENC ×6) —
and the image-block exhibit's `name=` names the same host's
`logo1.png` (candidate L35). The only asset-side change the port made
to these references is the colon encoding.

**Why.** Pattern classes P7 (font stacks; KB-35, KB-36) and P5
(assets; KB-25, KB-26). Failure prevented: a stack naming an unloaded
font silently falls back (here, for the theme's display motto), and
assets left on the origin host are outside the port's control.

**Verify.** `grep -n -i 'yoon' candidate.txt` returns the two stacks
and no load; `grep -n 'scpko.wikidot.com' candidate.txt` lists the
eight asset references (plus the credit source link, which is
correct).

**Disposition.** The font import's deletion is dispositioned nowhere;
it is flagged in the per-theme record (item 2). The assets are
dispositioned as environment class (ii): ledger part (c2) records
"candidate-own foreign/sandbox delivery hosts: posting-time rewrite
or original-state delivery class (T1 class (ii); KB-41/KB-54 family)"
and part (c3) records P5 as "DISPOSITIONED (class (ii) / KB-58)".
The two citations do not describe the same end-state — KB-58 is the
deferred-hosting class for references already repointed to the draft
host — and the probe evidence is in the per-theme record (item 4).
The (b) verdict is PASS.

## 5. Header, titles and rendered strings (P6)

**What.** The theme sets no `--header-title` variables; its rendered
strings are the CSS `content:` lines. Four Korean strings stand in
the candidate: the GoI name 조요의 인도자 (candidate L168) and three
forms of its motto (L191, L715, L726). They are the strings the
YoonDokrip stacks set (section 4). The page title converts
어떤 길잡이 CSS 테마 → とある導き手テーマ (candidate L13); the credit
block's title field keeps the Korean form (section 1).

**Why.** Pattern class P6 (header and rendered strings; KB-29,
KB-30, KB-31). The motto strings are the work's own slogans, set as
design content in the origin language.

**Verify.** `grep -n 'content:' candidate.txt` — four Korean strings
amid `content: none` rules.

**Disposition.** T4 charged the four strings (pattern 9); ledger part
(c3) dispositions P9 under ruling 2 (header/title language is out of
scope for migration correctness). They stand by that disposition and
are not flagged. The credit title field is a different charge (a §3
field question, not a language-taste question) and rides with item 1
of the per-theme record.

## 6. Body translation (P10)

**What.** The prose body is translated throughout: 5
TRANSLATION-ANCHORED blocks and 9 TRANS-UNANCHORED blocks cover the
intro prose, the usage instructions, the heading samples
(제목1–6 → レベル1–6見出し), the tabview sample's text, and the
exhibit captions (the image-block caption 헤더 이미지 → 画像ブロック,
block B10). The tabview sample keeps its nonsense filler ㅁㄴㅇㄹ
untranslated, as a sample. The static info-box rendering
(candidate L21–25) is part of this translation surface and is
adjudicated in section 1.

**Why.** Pattern class P10 (translation; KB-50, KB-51). Failure
prevented: untranslated documentation makes the candidate unusable
as a JP theme page.

**Verify.** Spot-check any anchored block against diff.md (e.g. B11,
the heading samples); `grep -n '제목' candidate.txt` returns nothing
outside the credit block's quoted title fields.

**Disposition.** T4/T5 judged this theme FINDINGS jointly; the
translation charges are the furniture and string items recorded in
sections 1 and 5. The (b) verdict is PASS.

## 7. Link targets (P11)

**What.** The candidate's functional links name JP or recorded
targets: the credit source link names scpko (the recorded origin —
correct for a source link), the usage exhibit names `:scp-jp:`
(section 2), and the tabview sample's visited-link example names
`theme:some-guider` unprefixed (candidate L47), a sample of link
syntax carried from the original. No prose link targets the origin
branch as navigation.

**Why.** Pattern class P11 (link targets; KB-54). Failure prevented:
a functional link left pointing at the origin branch sends JP
readers to the wrong wiki.

**Verify.** `grep -n 'scpko' candidate.txt` — the hits are the
source link and the asset references of section 4.

**Disposition.** No ledger line charges a link target for this theme.
The usage exhibit's plain-slug form is flagged under section 2's
sweep family, not here.

## 8. Structural fidelity and exhibit census (P8, R3)

**What.** The exhibit census is preserved in order: usage exhibit,
image-block exhibit, heading samples, tabview sample, and the code
exhibit. Two presentation changes: the code exhibit is wrapped in a
collapsible (`show="ソースコードを表示"`, candidate L67–792, block
B15) under an added `+ ソースコード` heading, while the original's
own heading (`+ CSS 테마 코드` → `+ CSSテーマコード`) is retained
above it — the exhibit now sits under two headings where the
original had one; and the credit zone's furniture exchange
(section 1) restructured the head. Nothing the original exhibits is
missing: the census count is unchanged, and the two
EXHIBIT-RESTRUCTURE primaries resolve to these items (B2) and to the
image-block caption line (B10, a false-fire).

**Why.** Pattern class P8 (structural fidelity; KB-42, KB-43).
Failure prevented: a silently dropped or reordered exhibit breaks
the theme's documentation contract with its readers.

**Verify.** Compare the heading sequence:
`grep -n '^+' original.txt candidate.txt`.

**Disposition.** No ledger line charges the structure. The (b)
verdict is PASS.

## 9. Formatting-only changes (R4)

**What.** The residue is two blocks, both exhibit-tail mechanics of
the collapsible wrap: B24 (original L780, a blank line at the code
exhibit's end, dropped in the wrap) and B25 (original L782 →
candidate L791, the exhibit's closing line repositioned by the wrap
and the gate's closing line). The classifier reports 0 reindent
blocks; no whitespace-only change carries content weight.

**Why.** Residue class R4 (formatting-only). The ground is the
classifier's counts plus the two blocks' shapes above.

**Verify.** The appendix table; `sed -n '788,794p' candidate.txt`.

**Disposition.** Nothing to disposition.

## 10. Porter annotations (R2)

**What.** None. The candidate contains no `[!-- --]` porter comments
and no translator's notes; the joke line inside the static info-box
rendering (candidate L23) is carried content from the original's
info box, not an annotation.

**Why.** Residue class R2 has no instance here; the ground is the
grep below, run before writing this section.

**Verify.** `grep -c '\[!--' candidate.txt` returns 0.

**Disposition.** Nothing to disposition.

## 11. Dispositioned deviations (class (ii) / (iii) summary)

**What.** The deviations a reader of the diff might otherwise charge
against the candidate, with their dispositions:

- T1's findings (T1-ROWS row 255: exit 1, 12 errors / 1 warn / 1
  info) are hotlink ×11 — the origin-host references of section 4,
  dispositioned in (c2) as the posting-time-rewrite class — and
  pseudo-ref ×1, the frame/credit include class shared with the
  whole population. Both are environment class (ii) per register c1.
- The render check's items (RENDER-ROWS-2, KO8) are all
  DISPOSITIONED in ledger part (c2): the runtime-hotlink site-theme
  chain plus the scpko hosts on both pages (the class above); the
  sample credit-modal, the preview form's known property (KB-32);
  no sample overflow (a positive record); T3 recorded nothing beyond
  the cross-cutting items. Engine coverage is the full matrix as run
  by the lane, not separately caveated in the row.
- The four Korean content strings stand under ruling 2 (section 5).
- The draft-host delivery URL is environment class (iii) (KB-41).

**Why.** These classes exist so a reviewer does not re-litigate
environment properties as candidate defects; each item names its
record so the disposition can be re-checked at its source.

**Verify.** The theme's rows in `review/AUTHORITIES/ledger-parts/`
(T1-ROWS row 255, RENDER-ROWS-2) and its blocks in
`GOSIGN2-LEDGER.md` parts (c2) and (c3).

**Disposition.** All items above are DISPOSITIONED in the cited
records. The items that are not dispositioned — or whose disposition
the bytes contradict — are the per-theme record below.

## 12. Verification history

**What.** T1 (source check): FINDINGS (classified), 12 errors all in
the standing classes — T1-ROWS row 255. T2/T3 (render check):
FINDINGS, all items dispositioned in (c2) — RENDER-ROWS-2 (KO8).
T4/T5 (localize check): FINDINGS with 1 display-affecting item (the
logo embed, pattern 5) plus the pattern-3 credit charges, the
pattern-9 strings, and the §3 title charge — LOCALIZE-ROWS row 284
(LOCALIZE-S2-F). Ledger part (c3) records P3 FIXED, P5 DISPOSITIONED,
P9 DISPOSITIONED; sections 1 and 4 record where the bytes agree and
where they do not. The (b) verdict is PASS, with no OPEN items at
the determination and no FIX5 re-judgement.

**Why.** The verification section exists so the reader can see which
checks ran, what they found, and what became of each finding,
without re-running the campaign.

**Verify.** The cited rows; the stamp at the head of this file is
generated from the same records by `review/build_review.py`.

**Disposition.** Verdict: PASS (go-sign ledger part (b)), with the
flags below carried for the coordinator.

## Per-theme record: some-guider-jp

**Item 1 — the credit record and the bytes disagree (flag, not
edited).** Ledger part (c3) records this theme's P3 credit fields as
FIXED (credit waves, checker-verified), and the candidate's last
commit is the credit attribution normalization (1869877). Against
that record, the current bytes still carry every element of T4's
pattern-3 charge (LOCALIZE-ROWS row 284): (a) the author field reads
`**著作権者:** CN 支部の作者` (candidate L8) — no author named, and
the wrong branch for a KO theme whose author, c_bonefish, is named
in the candidate's own prose (L23, L25) and the original's (L25);
(b) the second credit-style block stands (candidate L21–25), and it
names a translator, `[[*user kkaacc]]`, where the preview block
names AI as translator of record — two attributions for one port in
one file; (c) the two furniture labels stand over an empty div and
the static block (candidate L14–20), the modules they headed having
been deleted; (d) the credit title field is the Korean title
(candidate L4), where the page's own JP title is とある導き手テーマ
(L13). What the credit waves verifiably did here is field presence:
all eight fields exist. Field content and the legacy furniture were
not in fact repaired. The coordinator's repair lane owns the fix;
this package records the evidence and does not edit the candidate.

**Item 2 — YoonDokrip: the load was deleted, the stacks remain
(flag, not edited).** Original L72 imports YoonDokrip.css from the
KO files host; the candidate deletes the import (block B17) and
loads only Noto Sans JP (candidate L69), while the stacks at
candidate L169 and L190 still name `'YoonDokrip'`. The affected text
is the theme's motto block (section 5's strings), which now falls
back to the generic sans-serif. No ledger line names the font.
Either restoring the load from a JP-hosted copy or renaming the
stacks resolves it; leaving both halves is the defect.

**Item 3 — usage exhibit names a plain-slug page (sweep family).**
Candidate L28: `@@[[include :scp-jp:theme:some-guider]]@@`. The
posting name is `theme:some-guider-jp`; the snippet names a page
that will not exist. Flagged for the population sweep; not edited.

**Item 4 — asset hosts: dispositioned, with a citation mismatch and
probe evidence.** The theme's images remain on the origin host
(section 4's census). Part (c2) dispositions them as a posting-time
rewrite (KB-41/KB-54 family); part (c3) cites KB-58, which describes
references already repointed to the draft host. Probes run once each
on 2026-11-17: the origin form of the logo,
`https://scpko.wikidot.com/local--files/theme:some-guider/logo1.png`,
answers 302 to the files host, which serves it (200) — the pages
render styled today, as (c2) says; the draft-host form,
`https://sigma10-jp-test.wdfiles.com/local--files/theme%3Asome-guider-jp/logo1.png`,
answers 404. So whichever citation governs, the end-state still
requires the posting-time step (repoint plus upload); nothing in the
candidate blocks it. Recorded so the reflection step does not mistake
the disposition for the completed rewrite.

### Post-package repairs (REFRESH3-F)

**FIX-GUIDER, landing `1e3da43` (report `R/review-scout/FIX-GUIDER.md`, item 1,
"theme:some-guider-jp credit furniture").** This landing postdates the
package build (`7170328`, the M-pure-11 batch commit) and is the repair
the two flags above waited for. Four candidate changes, all present in
the recopied `candidate.txt`: (a) the 著作権者 field (candidate L8)
`**著作権者:** CN 支部の作者` → `**著作権者:** [[*user c_bonefish]]` — item 1(a)'s
wrong-branch, unnamed-author field now names the author the original's
prose and the CSS banner name; (b) the credit タイトル field (candidate L4)
`어떤 길잡이 CSS 테마` → `とある導き手テーマ`, the page's own JP heading, while
原題 (L7) keeps the KO title; (c) the second credit-style block and the two
empty label divs (as-built L16–25, ten lines) removed — every field they
carried already stands in the preview block, and their translator
`[[*user kkaacc]]` contradicted the ruling-3 翻訳責任者 AI in the same file;
(d) the original's YoonDokrip load restored as
`@import url('https://scpko.wdfiles.com/local--files/yoonfont/YoonDokrip.css');`
at candidate L59, immediately after the Noto Sans JP import at the head of
the delivered code block (item 2's stacks now resolve the face in
delivery; the URL was probed 2026-11-17, HTTP 200, `text/css`, 1,348,788
bytes). Checker per the report: error 12 / warn 1 / info 1 → 13/1/1; the
one added finding is the restored import's hotlink, class (ii)
posting-time re-host, with class (i) errors 0 before and after. This
package documents the corrected candidate; its stamp reads STALE against
the pre-repair verdict, by design.

## Change set

Delivered with this candidate in the canonical repository: the
candidate page itself (`pages/theme:some-guider-jp.txt`) and its
decoration sample (`pages/theme-decoration-sample-some-guider-jp.txt`).
The candidate's own history is two commits: the Stage 2 KO8
integration and the FIX-CREDIT-D normalization (see item 1 for what
that normalization did and did not change).

## Appendix: residue resolution

The classifier left 2 blocks unlabeled (7.7%). Per the class-M
convention they are resolved here by shape, one row per block.

| Block | Lines (orig → cand) | Resolution |
|---|---|---|
| B24 | 780 → (deleted) | Blank line at the code exhibit's tail, dropped when the exhibit was wrapped in its collapsible (section 9, R4). |
| B25 | 782 → 791 | The exhibit's closing line, repositioned by the same wrap (section 9, R4). |

## License and attribution

- **Title:** 어떤 길잡이 CSS 테마
- **Author:** c_bonefish
- **Source:** https://scpko.wikidot.com/theme:some-guider — revision 17
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
