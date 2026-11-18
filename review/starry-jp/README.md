# theme:starry-jp — review package

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:starry-jp — origin CN, population #232 [GOSIGN2-LEDGER (b) row 232]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 1676e19afc7a0cc4666352526691a0c6ec0f0ec7d5ab1e0f8519c3c3078bdcb0); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 57 errors / 3 warns / 2 infos (hotlink×54, pseudo-ref×2, http×1); standing classes dispositioned in register c1 [T1-ROWS row 192; GOSIGN2-LEDGER (b) row 232]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page sidebar-unreachable at 375/320 (both engines) + runtime-hotlink site-theme chain + candidate hosts oxygennine.wdfiles.com, scpsandboxcn.wdfiles.com, stsandbox.wdfiles.com; sample credit-modal (preview-form) + sidebar-unreachable (chromium 375/320); T3 page not separately walked, no additional visual finding; mixed coverage: page full-engine, sample chromium-only (no WebKit verdict). [RENDER-ROWS-G (CN15)]
- Engine coverage: mixed: page full-engine, sample chromium-only [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN15)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 231, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 231]
- FIX5 re-judgement: item 88 (class H) FIXED — FIX5-TEXTB §6, commit 3f328d8: prose links repointed to theme:mox-jp and theme:shivering-night-jp (probes: unsuffixed names 404) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 88]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:starry-jp.txt sha256:1676e19afc7a0cc4666352526691a0c6ec0f0ec7d5ab1e0f8519c3c3078bdcb0; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| Item | State |
|---|---|
| Ledger verdict (this theme) | FINDINGS, one blocking item (class H), population #232, CN origin, kind K5b-3 (layered over a base candidate) [GOSIGN2-LEDGER (b) row 232] |
| FIX5 re-judgement | Item 88 FIXED [GOSIGN2-LEDGER-SUPPLEMENT (a) item 88; FIX5-TEXTB §6, commit 3f328d8] |
| Blocking items open | 0 — the item-88 closure is re-derived from this package's bytes in the Per-theme record below |
| Generated verdict stamp | STALE (see §11): the only post-verdict change is the snippet sweep's usage-example completion (b5cb724), which does not touch the item-88 locus |
| Review class | R-fix (ROLLOUT class R, sub-class R-fix) |

## Provenance

| Field | Value |
|---|---|
| Original page | theme:starry, branch scp-wiki-cn (CN), reference revision 10 |
| Mirror file | review-mirrors/theme_starry.txt (campaign record), 1,078 lines / 32,349 B |
| Mirror SHA-256 | f8f9b8a61acbca5716fc9b5d4d78028beb272f5f13594acb211f4833a80e35aa (== review/sources.tsv row) |
| Candidate file | pages/theme:starry-jp.txt, 1,065 lines / 35,526 B |
| Candidate SHA-256 | 1676e19afc7a0cc4666352526691a0c6ec0f0ec7d5ab1e0f8519c3c3078bdcb0 (== candidate.txt in this package) |
| Layering note (sources.tsv) | "candidate layers over theme:mox-jp (this package's diff covers the theme's own layer only)" — correct, and load-bearing for §§3–4 |
| Population audits touching this theme | FIX5-TEXTB §6 (item 88); FIX-CODEADDR census: the candidate's self-delivery address is correct on current bytes (§3) |
| Patterns cited at | patterns/ @ 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa |

Provenance route: sources.tsv row → mirror store (frozen) → this package's
original.txt; canonical pages/ file → this package's candidate.txt.

**Provenance discrepancy (recorded for the coordinator's harvest
correction; sources.tsv is not edited by this lane).** The sources.tsv
row also claims the original was superseded upstream since the reference
revision, citing follow-up diff artifact diff-starry-from10.txt. That
artifact (campaign record, gosign2-lanes/lane-oc-gs-localize-s2-E/)
records "theme:starry rev10 → rev10, no changes". The claim is wrong.
Correct form: "Upstream latest remains rev 10; the S2 artifact records
rev10 to rev10, no changes; follow-up diff artifact
diff-starry-from10.txt in the campaign record (K5a-i)".

## Summary

Starry is a CN aesthetic theme layered over the MoX base: a 90vh
animated header, a hidden page title, and a differential stylesheet that
re-skins MoX variables. The port keeps the layering honest: its single
delivered code block holds only starry's own layer and imports
theme:mox-jp/8 for the base, exactly as the sources note states. The
original's two-part delivery (in-page preset modules plus a separate
full-CSS source exhibit) is consolidated into that one delivered block,
the prose is translated, and the theme's one blocking item — two prose
links naming theme pages that do not exist on scp-jp — was repointed by
FIX5-TEXTB and is verified on current bytes below. Churn is +396/−410
lines by build_review.py's count (Tier 2 diff); the classifier
(classify_hunks.py) splits it into 57 blocks, 53 specific, 0 heuristic,
and 4 residue, all adjudicated in the appendix. Most of the churn is the
delivery consolidation (§3) and the byte-identical CSS lines it carried
across channels (§4).

## Standing sections

### 0. Header and provenance

- What: The candidate opens with the tag gate (L1, `[[iftags +テーマ]]`)
  and the credit block (L3–12, §1); its delivery layer sits at the tail
  (§3). The original opens with a ThemePreviewer module (original L1,
  a cloudfront base-CSS URL) and its delivery module (original L3–8).
  The previewer is branch furniture, replaced by the standard JP head
  and tail forms. The provenance discrepancy in the sources.tsv note
  is recorded in the Provenance section above.
- Why: P1/P2 head forms. The failure prevented is a deliverable whose
  head still depends on the origin branch's preview furniture.
- Verify: `sed -n '1,12p' candidate.txt` against `sed -n '1,8p' original.txt`.
- Disposition: T1 FINDINGS (classified): 57 errors dominated by the
  hotlink class (the author's own asset hosts, §4), dispositioned in
  register c1 [stamp].

### 1. Credit and attribution

- What: The candidate adds the preview credit block at L3–12: タイトル
  流繁星 特种版式; 翻訳責任者 AI; 翻訳年 2026; 原題 流繁星 特种版式;
  著作権者 OxygenNine; 作成年 2025; 初訳時参照リビジョン 10; 元記事
  リンク https://scp-wiki-cn.wikidot.com/theme:starry, naming the
  recorded original host (scp-wiki-cn.wikidot.com) exactly. Two facts
  are recorded plainly. First, the original names its author nowhere
  in text (grep: "OxygenNine" does not occur in original.txt); the
  author's identity is carried by the asset host oxygennine.wdfiles.com
  used throughout the original's CSS, and the field records that handle
  in plain form. There is no name in the original to drop or contradict,
  so no attribution defect arises. Second, the タイトル field repeats
  the original title verbatim, including the CN subtitle 特种版式,
  while the theme's own JP title block (candidate L17–19) displays
  流繁星 / 特殊テーマ; the field is the work's recorded title, the
  title block is the display form, and the difference is stated here
  rather than silently harmonized.
- Why: P3 with the TASL record per ruling 3 of RULINGS-20261116. The
  failure prevented is an unattributed port; the ground for the author
  field is stated openly because it rests on the asset host, not on a
  byline.
- Verify: `sed -n '3,12p' candidate.txt`; `grep -c "OxygenNine" original.txt` (0).
- Disposition: Ledger (c3) row 232: P3 FIXED [GOSIGN2-LEDGER (c3)
  row 232].

### 2. Includes and components

- What: Live includes: the credit pair (L3, L12) and the interwiki
  frame at the tail (L1062–1065). The usage exhibits are escaped and
  name JP addresses: the install snippet at L38
  (`= {{[[include :scp-jp:theme:starry-jp]]}}`) and the customization
  exhibit at L50 (`@@[[include :scp-jp:theme:starry-jp@@` followed by
  the parameter table). No foreign include remains live: the original's
  head module imported its CSS from scp-wiki-cn.wdfiles.com local--code
  addresses (theme:mox/8, theme:starry/1); the candidate's tail module
  imports the JP counterparts from the draft host (§3).
- Why: P1 (include repointing). The failure prevented is a usage
  instruction or a delivery import that resolves to the origin branch
  or to a page that will never exist on scp-jp.
- Verify: `grep -n "include" candidate.txt` — every live or exhibited
  include names a :scp-jp: address, theme:mox-jp/theme:starry-jp, or
  the credit/frame components.
- Disposition: T4 FINDINGS with 1 display-affecting finding
  [LOCALIZE-ROWS row 231, LOCALIZE-S2-E]; the (c3) register's P4/P5
  dispositions for this row are recorded in §11.

### 3. Delivery mechanism

- What: Layered delivery, kind K5b-3. The candidate's own layer is a
  single code block ([[code type="css"]] at L342, content L343–1052),
  delivered by the tail [[module css]] (L1058–1061), which imports
  theme:mox-jp/8 first and theme:starry-jp/1 second, both from the
  draft host in colon-encoded form, and by the interwiki frame
  (L1062–1065, priority=1, theme= naming the candidate's own /1). The
  /1 address is correct: a census over all code forms finds exactly
  one code block in the candidate, and it is the stylesheet (the
  FIX-CODEADDR census did not list this theme, and the address checks
  out on current bytes). Consolidation: the original delivers its
  parameter presets as in-page module CSS (original L10–269, the
  {$normal-header} / {$no-sticky-header} / {$no-bg} comment gates) and
  separately exhibits its full CSS as a code block (original L621,
  content to L1075). The candidate merges both into the single
  delivered block; the parameter gates survive inside it in the
  original's comment-gate form (from candidate L345), neither inlined
  unconditionally nor dropped. The classifier records this as
  DELIVERY-MOVE on 48 blocks, the main move (original module CSS
  L9–269 → candidate code block) at similarity 0.871. The base is
  imported, not inlined: the candidate's block holds starry's
  differential layer only, as its banner states (§10).
- Why: Delivery parity (P10 family) under the layering the sources
  note declares. The failures prevented are the two this section
  exists to catch: a base silently inlined (the port would drift from
  theme:mox-jp's fixes) and a documented parameter gate emptied or
  made unconditional.
- Verify: `grep -n "\[\[code" candidate.txt original.txt` (one opener
  each); `sed -n '1058,1065p' candidate.txt` (import order: base
  first, own layer second).
- Disposition: The (c3) register dispositions this row's P4 as
  DISPOSITIONED (delivery class (ii), original-state CDN) and P5 as
  DISPOSITIONED (class (ii)/KB-58) [GOSIGN2-LEDGER (c3) row 232]; no
  delivery defect is recorded by this package.

### 4. Fonts and assets

- What: Fonts. Starry's own layer declares no font stacks; it consumes
  the base's variables (font-family: var(--mox-ui-font) and
  var(--mox-mono-font)), whose definitions live in theme:mox-jp's
  layer, outside this package per the layering note. The exhibit prose
  (candidate L325–329) names the effective fonts — UI: Noto Sans JP /
  Raleway; body: Noto Sans JP; mono: Oxygen Mono / Noto Sans JP —
  translated from the original's prose (original L611–615, where
  思源黑体 becomes Noto Sans JP and Oxygen Mono is kept). Raleway
  appears in an inline span style in both files, byte-identical. No
  load gap is chargeable to this layer: it names no stack of its own,
  so there is nothing it should have loaded. Assets. The own layer's
  background and icon URLs point at the author's hosts
  (oxygennine.wdfiles.com, stsandbox.wdfiles.com), byte-identical to
  the original — original-state delivery. The classifier's COLON-ENC
  mass (47 blocks) is the repeated icon URL lines containing the
  author's `system:files` path segment, carried byte-identical inside
  the moved CSS: the colon is part of a file path inside CSS url(),
  where it is legal and the file serves. T1's 54 hotlink errors are
  these same lines.
- Why: The load discipline (KB-16) applies to stacks a file declares;
  this file declares none. The asset lines are dispositioned
  original-state (class (ii)): re-hosting another author's sandbox
  files was not part of this port's delivery change, and the render
  row records the hosts as a disposition, not a defect.
- Verify: `grep -n "font-family" candidate.txt` (only var() references
  and the one span style); `grep -c "oxygennine.wdfiles.com" original.txt candidate.txt` (equal counts).
- Disposition: Render row: candidate hosts oxygennine.wdfiles.com,
  scpsandboxcn.wdfiles.com, stsandbox.wdfiles.com DISPOSITIONED class
  (ii) [GOSIGN2-LEDGER (c2) row 232]; T1 hotlink class dispositioned
  in register c1.

### 5. Header, sidebar, and furniture

- What: The MoX header variables are carried byte-identical in both of
  the candidate's copies: --mox-header-subtitle "控制 - 收容 - 保护"
  at candidate L614 (and the {$header-subtitle} parameter form at
  L593), exactly as at original L636 and L260. These are the base
  theme's identity strings (the SCP slogan in its CN form) consumed
  through MoX variables, not this theme's prose. The theme's own title
  block (candidate L17–25) is translated: 流繁星 / 特殊テーマ for the
  original's 流繁星 / 特种版式 (original L299–310). The
  sidebar-unreachability at 375/320 viewports is a render-row
  disposition (§11), an inherited layout behavior of the layered
  design, not a dropped rule: the sidebar rules are inside the moved
  stylesheet.
- Why: Header language as such is out of scope for migration
  correctness (ruling 2 of RULINGS-20261116), and the (c3) register
  dispositions this row's P9 under ruling 2. The failure this section
  exists to catch (a furniture variable silently revalued) does not
  occur: the values are byte-identical.
- Verify: `grep -n "mox-header-subtitle" original.txt candidate.txt`
  (two occurrences each, identical strings).
- Disposition: P9 DISPOSITIONED (ruling 2) [GOSIGN2-LEDGER (c3)
  row 232].

### 6. Text translation

- What: Prose translation throughout the body: the overview (candidate
  L30–40), the customization instructions and the parameter table's
  comments (L42–330 passim), the font exhibits (§4), and the section
  headings (简介 → 概要, L30; 自定义 → カスタマイズ, L42; 源代码 →
  ソースコード, L331). The classifier's TRANS-UNANCHORED blocks (3)
  and COMMENT-TEXT block (1) are this mass plus the code banner (§10).
  The one sentence that is more than translation is the overview's
  first sentence, whose link addresses changed under item 88
  (Per-theme record).
- Why: T5 translation completeness. The failure prevented is
  reader-facing CN residue in a JP deliverable, outside the identity
  strings recorded in §5.
- Verify: diff sections in diff.md; `sed -n '30,40p' candidate.txt`.
- Disposition: T5 FINDINGS under the joint T4/T5 verdict
  [LOCALIZE-ROWS row 231]; no untranslated-prose item stands open.

### 7. Links

- What: The credit source link names the recorded host (§1). The
  overview sentence (candidate L32) is item 88's locus, re-derived in
  the Per-theme record: it now names theme:mox-jp and
  theme:shivering-night-jp. A census of every `[[[theme:` link in the
  candidate returns only L32 — no other prose theme link exists, and
  none names an unsuffixed page. The remaining links in the body are
  the usage exhibits (§2) and the credit link.
- Why: P11 (dead prose links): a link to a page that will not exist on
  scp-jp is a reader-facing dead end, and this theme's ledger item was
  exactly that.
- Verify: `grep -n "\[\[\[theme:" candidate.txt` (one line, both
  addresses suffixed -jp).
- Disposition: Item 88 FIXED [supplement (a) item 88]; no other link
  finding for row 232.

### 8. Structure and exhibits

- What: Body order is preserved: title block, overview, customization
  (with its modal parameter exhibits at candidate L48, L104, L120,
  L138), font exhibits, and the source exhibit. One structural change
  is intrinsic to §3: the source exhibit and the delivered stylesheet
  are now the same block — the original exhibited a copy of its CSS
  (original L621–1075) while delivering through separate modules; the
  candidate's collapsible source view (candidate L331–1052) shows the
  delivered block itself, so the exhibit can no longer drift from the
  delivery. No body section is dropped: the heading census matches
  (概要 / カスタマイズ / ソースコード plus the exhibit subsections).
  The Rate module inside the title block (candidate L22) is the
  original's own design element at original L304, carried unchanged:
  it sits inside the theme's demonstration title div in both files,
  and each file's second occurrence is an escaped exhibit (candidate
  L169, original L453). It is not the KB-09 shape — that defect is a
  bare Rate in the credit flow duplicating the credit module's widget;
  this one is part of the title specimen the theme exists to display,
  and the render rows walked this page without a double-rate finding.
- Why: Structure parity, with the exhibit/delivery unification
  recorded as a deliberate consequence of the consolidation, not a
  silent restructure.
- Verify: `grep -n "^+ " candidate.txt` against `grep -n "^+ " original.txt` (heading sets correspond); `grep -n -i "module rate" original.txt candidate.txt` (two occurrences each, same positions in kind).
- Disposition: No structure finding for row 232.

### 9. Formatting only

- What: None as a standalone class: classify_hunks.py fires no
  WS-ONLY label for this pair.
- Why: Recorded so the section's emptiness has its ground (the
  classifier's label census).
- Verify: classification.json, label_counts (no WS-ONLY key).
- Disposition: None required.

### 10. Porter annotations

- What: One porter annotation, riding at the head of the delivered
  code block (candidate L343): "starry-jp 固有の差分 CSS — MoX 基盤は
  theme:mox-jp/8 を @import で読み込みます。このファイルはその差分の
  みです。" (starry-jp's own differential CSS; the MoX base is read via
  @import of theme:mox-jp/8; this file is that differential only). It
  is checked against the delivered bytes and is accurate: the tail
  module does import theme:mox-jp/8 (§3), and the block contains no
  MoX base rules of its own beyond starry's variable overrides. A
  prose base declaration that contradicted the bytes would itself be
  a flag; this one does not.
- Why: Porter annotations ride inside other labeled blocks; this one
  is called out because it is the layering contract a future editor
  will rely on.
- Verify: `sed -n '343p' candidate.txt` against `sed -n '1058,1061p' candidate.txt`.
- Disposition: None required.

### 11. Dispositions and exceptions

- What: (a) The stamp's STALE verdict has exactly one cause: canonical
  b5cb724 (the snippet sweep completing the two usage-example lines,
  candidate L38 and L50, to the -jp form). It does not touch L32, so
  the item-88 closure below is unaffected. (b) The sources.tsv
  supersession note is wrong; the correct form is recorded in the
  Provenance section for the coordinator's harvest correction. (c) The
  render row's remaining findings are dispositioned: sidebar
  unreachable at 375/320 on both engines (page) and on chromium
  (sample); the runtime-hotlink site-theme chain; the candidate hosts
  as class (ii) (§4); the sample credit-modal errors are the preview
  form's property (credit:start-preview has no modal mechanism;
  ruling 5 of RULINGS-20261116 and the GOSIGN-TESTS T2 amendment).
  Coverage is mixed (page full-engine, sample chromium-only), as the
  stamp records.
- Why: A STALE stamp means the verdicts describe the pre-change file;
  the change is two exhibit lines, enumerated above.
- Verify: `git show b5cb724 -- pages/theme:starry-jp.txt` in the
  canonical repo (two changed lines).
- Disposition: As recorded; go-sign scope note applies (Wikidot-side
  only).

### 12. Verification

- What: T1 baseline 57 errors / 3 warns / 2 infos (hotlink×54,
  pseudo-ref×2, http×1; stamp, register c1). This package's own
  checks: original.txt SHA-256 equals the sources.tsv value;
  candidate.txt is byte-identical to the canonical file; a whole-file
  brace-depth scan ends at the same depth on both files (2, an
  artefact of braces inside wikitext {{ }} spans) and never goes
  negative; the code-block census is 1/1 (§3); the item-88 grep (§7).
- Why: The deciding checks for this theme are textual (link census,
  hash equalities); the render dispositions rest on the sweep's own
  rows, cited in §11.
- Verify: the commands in §§3, 7 and this section, all runnable from
  this repo plus the canonical checkout.
- Disposition: T1 FINDINGS (classified) [stamp].

## Per-theme record — the FIX5 closure, re-derived

### Item 88 [H] — dead prose links to unsuffixed theme names

- Ledger: GOSIGN2-LEDGER (a) item 88 charges population #232 with
  class H (dead links): the overview prose linked theme:mox and
  theme:shivering-night, neither of which exists on scp-jp; the
  candidates are theme:mox-jp and theme:shivering-night-jp. The charge
  notes the internal inconsistency as well: the candidate's own base
  import already used theme:mox-jp/8, so the prose disagreed with the
  page's own delivery.
- Supplement: item 88 FIXED by FIX5-TEXTB §6, commit 3f328d8, with
  probes recording that the unsuffixed names return 404
  [GOSIGN2-LEDGER-SUPPLEMENT (a) item 88].
- What the fix was supposed to change: repoint the two prose links in
  the overview sentence to the -jp candidates, leaving the link texts
  (the themes' names) translated as part of the sentence.
- Re-derivation from this package's bytes: the original's sentence
  (original L316) reads "…基于[[[theme:mox |一氧化物]]]版式…
  灵感来源于[[[theme:shivering-night |夜琉璃 版式]]]". The current
  candidate's sentence (candidate L32) reads
  "[[[theme:mox-jp |一酸化物]]]テーマを基盤にした…
  [[[theme:shivering-night-jp |夜琉璃 テーマ]]]から着想を得ています" —
  both addresses carry the -jp suffix, and a census of every
  `[[[theme:` link in the candidate returns L32 alone, so no other
  prose link retains the dead form. Commit 3f328d8 is an ancestor of
  the verdict head 435a6bb, and the only post-verdict change
  (b5cb724) touched the two usage-example lines, not L32. The closure
  is confirmed from the bytes, not from the ledger.

## Change set outside the two diffed files

The snippet-sweep landing (b5cb724) is inside the candidate file and
visible in the diff as the two completed usage-example lines (§11).
The sources.tsv note correction (Provenance section) is owed by the
coordinator at harvest; this lane does not edit sources.tsv.

## Multi-wave provenance

9f252b5 (Stage 2 CN15 port) → 7d9877c (rework2-p4) → 1869877
(FIX-CREDIT-D) → 3f328d8 (FIX5-TEXTB, item 88) → b5cb724 (snippet
sweep, usage examples). The mirror is revision 10 throughout, and
upstream has not moved past rev 10 (Provenance section).

## Appendix — heuristic and residue adjudication

Heuristic blocks: none (0 of 57). The classifier's 4 residue blocks
are adjudicated as differ alignment artefacts at channel boundaries:
B4 (original L8 → candidate L17: the original head module's closing
line; the candidate has no head module, its delivery having moved to
the tail, so the line has no counterpart — §3) and B54–B56 (the file
tail: the original's closing lines against the candidate's, which
close one extra [[/div]] for the customization modal wrapper; both
files end with [[/iftags]], verified by reading both tails). The 47
COLON-ENC blocks are adjudicated in §4 (byte-identical carries inside
the moved CSS, not changes in substance). diff.md's auto-class table
(mechanical 2, supplement 3, residual 52, by build_review.py's
token-level heuristic) is a different instrument from
classify_hunks.py; the adjudicated classification is the classifier's,
and every one of its blocks is accounted in the sections above.

## License and attribution

- **Title:** 流繁星 特种版式
- **Author:** OxygenNine
- **Source:** https://scp-wiki-cn.wikidot.com/theme:starry — revision 10
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
