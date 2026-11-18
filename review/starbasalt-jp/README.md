# theme:starbasalt-jp — review package
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:starbasalt-jp — origin CN, population #231 [GOSIGN2-LEDGER (b) row 231]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 7f29e9d4dce9515ae13a60d2626249c9c4e655e0b0ae3dcb78ceb3efc6a5ae75); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 1 warn / 1 info (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 262; GOSIGN2-LEDGER (b) row 231]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-rate on all combos on both pages (T3: script false positive, rate widget visible) + page-overflow at every viewport (437–506px mobile; sample 1489px@1366) + runtime-hotlink site-theme chain + candidate cdn.jsdelivr.net (one sample hotlink line also lists http.cat among other hosts, no hidden-* cluster); sample carries NO credit-modal machine line (T3: modal N/A, preview form); T3 sample §15 content panels unstyled plain text on black; full-engine coverage. [RENDER-ROWS-G (CN14)]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-G row, findings cell]
- Credit modal: no credit-modal line recorded — the row states the sample carries NO credit-modal machine line (T3: modal N/A, preview form) [RENDER-ROWS-G (CN14)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 230, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 230]
- FIX5 re-judgement: items 86 (class I) FIXED, 87 (class I) FIXED — FIX5-STRUCTA, commit 8c0cd35: same root cause as item 87; terminating the comment restores the full stylesheet, including the section-15 panel styling; header comment terminated at L352 (one-line edit); spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) items 86–87; (c) check 1]
- Computed against: canonical commit fb435643733dfd93d8dfa698861e4a59921d8f0f; candidate file pages/theme:starbasalt-jp.txt sha256:7f29e9d4dce9515ae13a60d2626249c9c4e655e0b0ae3dcb78ceb3efc6a5ae75; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| Item | State |
|---|---|
| Ledger verdict (this theme) | FINDINGS, two blocking items (both class I, one root cause), population #231, CN origin [GOSIGN2-LEDGER (b) row 231] |
| FIX5 re-judgement | Items 86 and 87 FIXED [GOSIGN2-LEDGER-SUPPLEMENT (a) items 86–87; FIX5-STRUCTA, commit 8c0cd35; spot-check (c) 1 PASS] |
| Blocking items open | 0 — both closures are re-derived from this package's bytes in the Per-theme record below |
| Generated verdict stamp | STALE (see §11): the only post-verdict change is the navla2 delivery-address repair (fb43564), which does not touch the stylesheet |
| Review class | R-fix (ROLLOUT class R, sub-class R-fix) |

## Provenance

| Field | Value |
|---|---|
| Original page | theme:starbasalt, branch scp-wiki-cn (CN), reference revision 7 |
| Mirror file | review-mirrors/theme_starbasalt.txt (campaign record), 1,007 lines / 30,511 B |
| Mirror SHA-256 | 0f2cb73dca42df7d69622b2c0f79f354d7538de119a2d264d813c2f8a73bb897 (== review/sources.tsv row) |
| Candidate file | pages/theme:starbasalt-jp.txt, 1,036 lines / 33,061 B (last line unterminated) |
| Candidate SHA-256 | 7f29e9d4dce9515ae13a60d2626249c9c4e655e0b0ae3dcb78ceb3efc6a5ae75 (== candidate.txt in this package) |
| Population audits touching this theme | FIX5-STRUCTA (items 86/87); FIX-NAVLA2 (delivery addresses, canonical fb43564) |
| Patterns cited at | patterns/ @ 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa |

Provenance route: sources.tsv row → mirror store (frozen) → this package's
original.txt; canonical pages/ file → this package's candidate.txt.

**Provenance discrepancy (recorded for the coordinator's harvest
correction; sources.tsv is not edited by this lane).** The sources.tsv
row for this theme claims the original was superseded upstream since the
reference revision. The artifact the row cites,
gosign2-lanes/lane-oc-gs-localize-s2-E/diff-starbasalt-from7.txt in the
campaign record, records "theme:starbasalt rev7 → rev7, no changes". The
note is wrong. Correct form: "Upstream latest remains rev 7; the S2
artifact records rev7 to rev7, no changes; follow-up diff artifact
diff-starbasalt-from7.txt in the campaign record (K5a-i)".

## Summary

Star Basalt is a CN Basalt derivative: Basalt's layout re-skinned with
space imagery inherited from theme:space. The port repoints the base
include to the JP Basalt candidate (ruling 1), moves the theme's own
stylesheet out of an in-page CSS module into a delivered code block,
re-hosts the space imagery to the JP storage host, translates the body,
and adds the Google Fonts loads its rewritten stacks need. The theme's
two blocking items share one root cause: a porter banner comment at the
head of the delivered stylesheet was never terminated, so the first 102
lines of the stylesheet, including every font import and the panel
rules, were delivered as a comment. FIX5-STRUCTA terminated the comment
with a one-line edit; both closures are re-derived below from the
current bytes. Churn is large only because the stylesheet changed
channel: +364/−335 lines by build_review.py's count (Tier 2 diff, 11
classifier blocks, 9 specific and 2 heuristic, 0 residue).

## Standing sections

### 0. Header and provenance

- What: The candidate's head is the delivery layer: the hidden base
  include (L1–3), the interwiki frame (L5–9), and the head module
  (L10–12), then the tag gate at L17 and the credit block (§1). The
  original opens with a ThemePreviewer module (original L1, pointing at
  a cloudfront base-CSS URL) before its hidden include; the previewer
  is branch furniture for in-wiki theme preview, not theme content, and
  the candidate replaces that function with the frame/head-module pair
  (§3). The provenance discrepancy in the sources.tsv note is recorded
  in the Provenance section above.
- Why: P1 (frame supplement) and P2 (tag gate). The failure prevented
  is a deliverable whose head still depends on the origin branch's
  preview furniture.
- Verify: `sed -n '1,17p' candidate.txt` against `sed -n '1,6p' original.txt`.
- Disposition: T1 FINDINGS (classified): 1 pseudo-ref error, 1 warn, 1
  info [stamp; register c1].

### 1. Credit and attribution

- What: The candidate adds the preview credit block at L19–28 (inside a
  [[>]] div): タイトル 星空玄武岩 テーマ（Star Basalt）; 翻訳責任者 AI;
  翻訳年 2026; 原題 星空玄武岩 版式; 著作権者 [[*user L-none-Lam]]
  （メンテナンス: [[*user gudagudaorder123]]）; 作成年 2024; 初訳時参照
  リビジョン 7; 元記事リンク
  https://scp-wiki-cn.wikidot.com/theme:starbasalt, naming the recorded
  original host (scp-wiki-cn.wikidot.com) exactly. Provenance note: the
  original carries no credit apparatus at all — no credit block, no
  license box, no banner naming an author — and neither name in the
  field occurs anywhere in original.txt (grep-verified). The two names
  come from the branch record the credit waves worked from; they are
  not derivable from the two diffed files, and no name in the original
  contradicts them. This is recorded as a provenance note, not a
  defect: there is no attribution in the bytes to drop or contradict.
- Why: P3 with the TASL record per ruling 3 of RULINGS-20261116. The
  failure prevented is an unattributed port; the residual risk here is
  the opposite kind (a field whose authority is the campaign record
  rather than the page), which is why the ground is stated openly.
- Verify: `sed -n '19,28p' candidate.txt`; `grep -n "L-none-Lam\|gudagudaorder123" original.txt` (no matches).
- Disposition: The (c3) register records row 231's charges under its
  disposition (e) only; no credit charge stands against this theme
  [GOSIGN2-LEDGER (c3) row 231].

### 2. Includes and components

- What: Live includes: the hidden base include at L2,
  `[[include theme:basalt-jp darkmode=a]]`, repointed from the
  original's `:scp-wiki-cn:theme:basalt` (classifier block B1:
  COMPONENT-SWAP / INCLUDE-REPOINT); the frame (L5); the credit pair
  (L19, L28); and an image-block include at L181 carrying the re-hosted
  logo (§4). The usage exhibits are escaped: L35 names
  theme:starbasalt-jp, and L45–49 name theme:basalt-jp with Basalt's
  documented parameter sets. Each live include occurs once; the
  [[include]] mentions at L41–42 are the original's own prose
  instructions, translated, not includes.
- Why: Ruling 1 of RULINGS-20261116: a cross-theme import repoints to
  the JP fixed base candidate, never to the raw upstream delivery. The
  failure prevented is a JP theme silently layering over the CN wiki's
  live Basalt.
- Verify: `grep -n "\[\[include" candidate.txt` — the live set is
  L2, L5, L19, L28, L181; everything else is escaped or prose.
- Disposition: T4 FINDINGS with 1 display-affecting finding
  [LOCALIZE-ROWS row 230, LOCALIZE-S2-E] — that finding is item 86/87's
  root cause, closed in the Per-theme record.

### 3. Delivery mechanism

- What: The delivery topology changes channel. The original delivers
  its own CSS as an in-page [[module CSS]] (original L4–681, content
  from L6). The candidate delivers the same stylesheet as code block 3
  (candidate L351–1034), referenced by the frame's theme= parameter
  (L7) and the head module's @import (L11). Those two addresses are
  the navla2 repair (canonical fb43564, record FIX-NAVLA2.md in the
  campaign record): before it, both named code block 1, the 98-byte
  title-customization sample, while the stylesheet sat unreferenced at
  block 3 — the navla shape. The repair is recorded here with its
  citation and is not re-litigated. The candidate's code-block census
  is exactly 3: block 1 (L166–170, the title sample), block 2
  (L174–178, the icon sample), block 3 (L351–1034, the stylesheet);
  the served-byte census in FIX-NAVLA2 confirms /3 serves the 24,066 B
  stylesheet and /1 the 98 B sample on the draft host. The original's
  two code exhibits (original L823, L831, both [[code type="css"]])
  are the same two samples, carried at candidate L165–170 and
  L173–178. The Basalt base is included, not inlined (§2).
- Why: Delivery parity (P10 family) with the JP code-block delivery
  form. The failure the navla2 repair prevented is a frame that loads
  a 98-byte exhibit as the theme's stylesheet: the page renders
  unstyled while every address looks plausible.
- Verify: `grep -n "\[\[code" candidate.txt` (three openers);
  `sed -n '5,12p' candidate.txt` (both delivery addresses name /3).
- Disposition: The mis-addressed state was a post-verdict defect found
  by the population re-sweep and remedied at fb43564 [FIX-NAVLA2.md];
  no delivery finding stands open.

### 4. Fonts and assets

- What: Fonts. The original loads nothing: it has no @import anywhere,
  and its stacks (original L87–89) name Urbanist, DM Sans, and Martian
  Mono with "Noto Sans SC" and 'LXGW-WenKai' as fallbacks. The
  candidate adds five Google Fonts @imports at the head of its
  stylesheet (candidate L353–357: Urbanist, DM Sans, Martian Mono,
  Noto Sans JP, Noto Serif JP; classifier JPFONT-LOAD / FONT-IMPORT)
  and rewrites the stacks (candidate L440–442): "Noto Sans SC" becomes
  "Noto Sans JP" in the header and body stacks, and the mono fallback
  'LXGW-WenKai' becomes 'Noto Serif JP' (P7 font-stack rewrite). Every
  face the candidate's stacks name is loaded by its own imports except
  Nanum Gothic, kept as a header-stack fallback (candidate L440): it
  is loaded neither in this file nor in theme:basalt-jp's file (grep:
  0 occurrences there). The original also loaded it nowhere — it is an
  inherited named-unloaded system fallback, identical in kind on both
  sides, recorded here as a note rather than a port-introduced gap.
  Assets. The space imagery is re-hosted from scptestwiki.wdfiles.com
  and scp-wiki.wdfiles.com (theme:space file paths) to
  scp-jp-storage.wdfiles.com file:8260379-* paths: --logo (candidate
  L360), --sp_header-logo (L392), and the body/header layer images
  (L425–427); classifier ASSET-REHOST on 3 blocks. The classifier's
  HTTP-KEPT presence lines (candidate L436–438) are the W3C namespace
  strings inside the --space-*-mask data URIs, byte-identical to the
  original's — the documented false positive for that signature, not
  kept http delivery.
- Why: P7 (font-stack localization) with KB-16's load discipline: a
  stack may not name a face nothing loads, which is why the candidate
  self-loads its faces instead of inheriting the original's unloaded
  stacks; and KB-17/P5 for the asset hosts (JP storage host for
  re-hosted files). The failure prevented is a theme that falls back
  to system fonts because its named faces were never fetched.
- Verify: `grep -n "@import" candidate.txt` (five, all Google Fonts);
  `sed -n '440,442p' candidate.txt` against `sed -n '87,89p' original.txt`.
- Disposition: No font or asset finding stands against row 231; the
  render row's candidate-host findings are dispositioned class (ii)
  (KB-41/KB-54) [GOSIGN2-LEDGER (c2) row 231].

### 5. Header, sidebar, and furniture

- What: The header variables are localized in the moved stylesheet:
  --header-title "SCP 基金会" → "SCP財団" (glyph-form conversion,
  classifier GLYPH-FORM) and --header-subtitle "明星，彗星，行星" →
  "星、彗星、惑星" (a translated noun list with localized punctuation),
  at candidate L388–389. The sidebar, fnColor, and furniture rules are
  inside the restored stylesheet span (§12 and the Per-theme record);
  before the FIX5 edit they were part of what the unterminated comment
  swallowed.
- Why: Header text is reader-facing furniture; the values here are in
  fact localized, so no ruling-2 question arises (header language as
  such is out of scope for migration correctness under ruling 2 of
  RULINGS-20261116).
- Verify: `sed -n '387,389p' candidate.txt`.
- Disposition: No furniture finding stands against row 231.

### 6. Text translation

- What: The body prose is translated throughout (candidate L31–349):
  the theme introduction (L31, naming theme:basalt-jp and the CN
  theme:space page it draws on), the usage instructions, the parameter
  exhibits, and the section bodies. The exhibit headings map one to
  one: original 版式设置 (L696) → テーマ設定 (candidate L39); 页面元素
  (L711) → ページ要素 (L54); the heading samples (original L846–856 →
  candidate L189–199); 着色 (L932) → 色付け (L275). One prose change is
  a correction, not a translation choice: the original's font prose
  (original L1000) names the header font "Sofia Sans / 思源黑体",
  stale against its own CSS, whose header stack is Urbanist; the
  candidate's prose (candidate L342–346) states the fonts its stacks
  actually deliver (Urbanist / Noto Sans JP; DM Sans / Noto Sans JP;
  Martian Mono / Noto Serif JP). The port corrects the prose to the
  bytes; the difference is recorded here so it is not misread as a
  translation error.
- Why: T5 translation completeness, with prose/bytes consistency: a
  documentation sentence that contradicts the delivered CSS is a
  defect in the documentation. The failure prevented is a reader
  following font instructions for faces the theme does not use.
- Verify: `sed -n '1000p' original.txt` against `sed -n '342,346p' candidate.txt`.
- Disposition: T5 FINDINGS under the joint T4/T5 verdict
  [LOCALIZE-ROWS row 230]; no translation item stands open.

### 7. Links

- What: The credit source link names the recorded host (§1). The
  introduction's links (candidate L31) name theme:basalt-jp (the JP
  base candidate, §2) and keep the theme:space reference on its home
  wiki (scp-wiki-cn.wikidot.com/theme:space), since the sentence
  credits the CN original the imagery came from. The parameter
  exhibits link the ACS guide and the ACS animation component in
  JP-relative form (candidate L48–49), as the original's exhibits did
  in CN-relative form.
- Why: P11 for the dependency link (repointed to the JP candidate);
  content references to origin works stay on their home wikis. The
  failure prevented is the item-88 shape, which does not arise here.
- Verify: `grep -n "wikidot.com" candidate.txt` — the credit link and
  the theme:space credit line, both accounted above.
- Disposition: No link finding for row 231.

### 8. Structure and exhibits

- What: The candidate's body sits before its code block (candidate
  L14–349, then the stylesheet at L351); the original's body sits
  after its module CSS (original L682–1007). The classifier therefore
  shows the original's body range as deletions at the candidate's tail
  (blocks B9–B11); those are differ alignment artefacts of the move,
  adjudicated by the heading census in §6: every original body section
  is present in the candidate, in the same order, and the two code
  exhibits map one to one (§3). No body section, exhibit, or CSS
  module is dropped: the original has exactly one stylesheet (its
  module CSS) and the candidate has exactly one (code block 3), plus
  the two samples on both sides.
- Why: Structure parity; the DELIVERY-MOVE label can hide a dropped
  module in multi-module originals, so the census is stated
  explicitly: 1 stylesheet + 2 samples on both sides.
- Verify: the censuses in §3 and the heading map in §6.
- Disposition: No structure finding for row 231.

### 9. Formatting only

- What: None as a standalone class: classify_hunks.py fires no
  WS-ONLY label for this pair. The whitespace differences are inside
  the moved blocks and are accounted there.
- Why: Recorded so the section's emptiness has its ground (the
  classifier's label census), not an omission.
- Verify: classification.json, label_counts (no WS-ONLY key).
- Disposition: None required.

### 10. Porter annotations

- What: One porter annotation exists, and it matters: the banner
  comment at candidate L352, "Star Basalt (星空玄武岩) — CNオリジナルの
  JP移植（starbasalt rev 7 準拠）", heading the delivered stylesheet.
  It is not a translation of an original comment — the original has no
  header comment at all (its module CSS opens directly with :root at
  original L6). This annotation is also the item-87 locus: as ported,
  it was missing its terminator (Per-theme record).
- Why: Porter annotations normally ride inside other labeled blocks;
  here the annotation is called out explicitly because it is both the
  theme's provenance statement inside the delivered CSS and the site
  of its blocking defect.
- Verify: `sed -n '352p' candidate.txt`.
- Disposition: The annotation's content is accurate (the port is based
  on rev 7; §0's discrepancy concerns the sources.tsv note, not this
  comment). Its form is the FIXED item 87.

### 11. Dispositions and exceptions

- What: (a) The stamp's STALE verdict has exactly one cause: canonical
  fb43564 (the navla2 repair, two lines: frame theme= /1→/3 at L7 and
  head-module @import /1→/3 at L11). It does not touch the stylesheet,
  so the item 86/87 closures below are unaffected. (b) The sources.tsv
  supersession note is wrong; the correct form is recorded in the
  Provenance section for the coordinator's harvest correction. (c) The
  render row's remaining findings are dispositioned: the hidden-rate
  lines are a script false positive (the rate widget is visible); the
  page-overflow figures belong to the cross-cutting overflow families
  (KB-33/KB-34); the candidate's foreign/sandbox delivery hosts are
  class (ii) (KB-41/KB-54); the sample carries no credit-modal line
  (preview form; KB-32 family).
- Why: A STALE stamp means the verdicts describe the pre-change file;
  the change is two address lines, enumerated above, and the reader
  can re-judge from §3.
- Verify: `git show fb43564 -- pages/theme:starbasalt-jp.txt` in the
  canonical repo (two changed lines).
- Disposition: As recorded; go-sign scope note applies (Wikidot-side
  only).

### 12. Verification

- What: T1 baseline 1 error / 1 warn / 1 info (stamp): the error is the
  pseudo-ref class; the warn is the link-target class for the base
  include. FIX5-STRUCTA's checker runs were identical before and after
  the fix (1/1/1), as expected for a CSS-comment terminator. This
  package's own checks: original.txt SHA-256 equals the sources.tsv
  value; candidate.txt is byte-identical to the canonical file; a
  whole-file brace-depth scan ends at the same depth on both files
  (1, an artefact of braces inside wikitext spans) and never goes
  negative; the stylesheet's own integrity is proven by the item-87
  re-derivation below (first */ in the file at L352, imports live at
  L353–357, body rule byte-identical to the original's).
- Why: The deciding checks for a comment-terminator fix are textual:
  where the first */ falls, and whether the formerly commented span is
  now live CSS identical in substance to the original's.
- Verify: `grep -n -m1 '\*/' candidate.txt` returns L352;
  `sed -n '353,357p' candidate.txt` shows the five live imports.
- Disposition: T1 FINDINGS (classified) [stamp].

## Per-theme record — the FIX5 closures, re-derived

### Items 87 and 86 [I] — the unterminated comment and the unstyled panels

- Ledger: GOSIGN2-LEDGER (a) item 87 charges population #231 with an
  unterminated CSS comment in the delivered code block: opened at
  candidate L352, closing only at L454, commenting out 102 lines (all
  five font @imports, the :root groups, and the body rules). Item 86
  charges the visible consequence on the sample page: the §15 content
  panels rendered as unstyled plain text on black; LOCALIZE-S2-E
  graded it display-fatal.
- Supplement: both items FIXED by FIX5-STRUCTA, commit 8c0cd35, a
  one-line edit terminating the comment at L352; supplement (c)
  spot-check 1 PASS (L352 now closes on the same line; the first */ in
  the file is at L352) [GOSIGN2-LEDGER-SUPPLEMENT (a) items 86–87;
  (c) check 1].
- What the fix was supposed to change: STRUCTA's report records the
  mechanism from the pre-fix bytes. The port had added a banner
  comment at the head of the stylesheet (candidate L352) and never
  closed it; the stylesheet's first */ was the self-contained
  `/*--------- CODE ----------*/` comment at L454. Everything between
  — the five @imports (L353–357), the first :root groups (L359–385),
  the main :root (L387–443), and the body rule (L445–453) — was inside
  the comment and never applied. The comment is a port-only addition:
  the original has no header comment, which is why the original
  renders styled and the port did not. The fix appended */ to L352
  and changed nothing else.
- Re-derivation from this package's bytes: on the current candidate,
  L352 reads `/* Star Basalt (星空玄武岩) — CNオリジナルのJP移植
  （starbasalt rev 7 準拠）。*/` and is the first */ in the file
  (grep-verified). The five Google Fonts @imports sit live at
  L353–357, outside any comment. The body rule at candidate L445–453
  is byte-identical to the original's body rule (original L92–100) —
  STRUCTA's class-E parity check, re-run for this package — which
  confirms the restored span is the original's stylesheet in
  substance, not a reconstruction. Item 86's closure follows from the
  same bytes: the §15 panel styling lives in the restored span, so no
  separate edit was needed or made. Commit 8c0cd35 is an ancestor of
  the verdict head 435a6bb, and the only post-verdict change
  (fb43564) touches L7 and L11, not the stylesheet. Both closures are
  confirmed from the bytes, not from the ledger.

### The post-verdict repair, recorded — FIX-NAVLA2, canonical commit fb43564

The "only post-verdict change" just described is the navla2 stylesheet-address repair: FIX-NAVLA2 (report `R/review-scout/FIX-NAVLA2.md`, section 3; flagged by FIX-NAVLA.md item 2), landed in canonical commit `fb435643733dfd93d8dfa698861e4a59921d8f0f` ("pages: stylesheet-address repairs in four themes", 2026-11-17). The candidate has three code blocks — a 98 B title sample at /1, a 39 B icon sample at /2, and the 24,066 B stylesheet at /3 — while both delivery lines named /1; the stylesheet was the only copy and nothing delivered it. The repair changed two addresses only: the interwiki-style frame's `theme=` (candidate L7) and the head module's `@import` (candidate L11) now read `local--code/theme%3Astarbasalt-jp/3`. The draft-host probe served /3 at 24,066 B (the Star Basalt stylesheet) against /1's 98 B; the T1 checker's 1/1/1 finding set was unchanged apart from the L11 pseudo-ref's block number, class (i) errors 0 before and after. This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:starbasalt-jp.txt` (its hash already matched the canonical file), `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record; the items 86/87 closures above stand on the bytes independently of that word.

## Change set outside the two diffed files

The navla2 repair (fb43564) is inside the candidate file and visible in
the diff as the /3 addresses (§3); its record is FIX-NAVLA2.md in the
campaign record. The sources.tsv note correction (Provenance section)
is owed by the coordinator at harvest; this lane does not edit
sources.tsv.

## Multi-wave provenance

d727e92 → ffad285 → ab71620 → 12d839e (Stage 2 CN14 port) → f1138e4
(FIX-P4, Basalt repoint) → 8c0cd35 (FIX5-STRUCTA, items 86/87) →
fb43564 (navla2, delivery addresses). The mirror is revision 7
throughout, and upstream has not moved past rev 7 (Provenance
section).

## Appendix — heuristic and residue adjudication

Residue blocks: none (0 of 11). The classifier's 2 heuristic blocks are
adjudicated by shape: B8 (DELIVERY-MOVE with EXHIBIT-RESTRUCTURE — the
stylesheet's channel move and the exhibit region it crosses, §§3/8)
and B10 (TRANS-UNANCHORED heuristic — the body translation mass, §6).
diff.md's own auto-class table (translation 1 block, supplement 3,
residual 7, by build_review.py's token-level heuristic) is a different
instrument from classify_hunks.py; the adjudicated classification is
the classifier's, and every one of its blocks is accounted in the
sections above.

## License and attribution

- **Title:** 星空玄武岩 版式
- **Author:** L-none-Lam（メンテナンス: gudagudaorder123）
- **Source:** https://scp-wiki-cn.wikidot.com/theme:starbasalt — revision 7
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
