# theme:spidersfalling-jp — review package

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:spidersfalling-jp — origin EN, population #139 [GOSIGN2-LEDGER (b) row 139]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 13910bedfabfe39d36cfb3e400d90b2f7ec278c9edc74979abcdf9647d6b1a49); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 11 errors / 1 warn / 1 info (pseudo-ref×11); standing classes dispositioned in register c1 [T1-ROWS row 124; GOSIGN2-LEDGER (b) row 139]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow. [RENDER-ROWS-2 (RENDER-S2-D (EN19))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN19))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 139, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 139]
- FIX5 re-judgement: item 30 (class B) FIXED — FIX5-FURNA, commit 9e8931f: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 30]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:spidersfalling-jp.txt sha256:13910bedfabfe39d36cfb3e400d90b2f7ec278c9edc74979abcdf9647d6b1a49; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| Item | State |
|---|---|
| Ledger verdict (this theme) | FINDINGS, one blocking item (class B), population #139, EN origin [GOSIGN2-LEDGER (b) row 139] |
| FIX5 re-judgement | Item 30 FIXED [GOSIGN2-LEDGER-SUPPLEMENT (a) item 30; FIX5-FURNA, commit 9e8931f] |
| Blocking items open | 0 — the item-30 closure is re-derived from this package's bytes in the Per-theme record below |
| Generated verdict stamp | STALE (see §11): the candidate changed after the verdict head 435a6bb in two recorded landings (b5cb724, 722ceb5), neither of which re-opens item 30 |
| Review class | R-fix (ROLLOUT class R, sub-class R-fix: a FIX5-fixed blocking item re-derived from the package bytes) |

## Provenance

| Field | Value |
|---|---|
| Original page | theme:spidersfalling, branch scp-wiki (EN), reference revision 5 |
| Mirror file | review-mirrors/theme_spidersfalling.txt (campaign record), 448 lines / 9,275 B |
| Mirror SHA-256 | 9854ec649b85d3bda09d3f6d1c5a7f8ef9f1d7c5b47b7c8a11f9cfaab9b0d2b9aa (== review/sources.tsv row) |
| Candidate file | pages/theme:spidersfalling-jp.txt, 459 lines / 9,921 B |
| Candidate SHA-256 | 13910bedfabfe39d36cfb3e400d90b2f7ec278c9edc74979abcdf9647d6b1a49 (== candidate.txt in this package) |
| Population audits touching this theme | FIX5-FURNA (item 30); FIX-CODEADDR census: no local--code self-delivery exists on either side (§3) |
| Patterns cited at | patterns/ @ 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa |

Provenance route: sources.tsv row → mirror store (frozen) → this package's
original.txt; canonical pages/ file → this package's candidate.txt.

## Summary

Spidersfalling is an EN Halloween variant of theme:xmas: a snowfall layer
re-skinned as falling spiders over one background image. The port is
structurally conservative. It keeps all five in-page CSS modules and all
four include-parameter variation gates in their original positions, adds
the standard JP head (interwiki frame plus preview credit block),
translates the prose and the CSS comments, and re-hosts the eleven
Spider.webp asset lines from the EN wiki's file area to the JP draft host
under the candidate's own page name. The theme's one blocking item, a
duplicate bare Rate module carried over from the original beside the
preview credit module, was deleted by FIX5-FURNA; the deletion is visible
in the first diff hunk and is re-derived in the Per-theme record. Churn is
small: +45/−34 lines by build_review.py's count (Tier 1 diff, 14 hunks);
the classifier (classify_hunks.py) splits the change into 23 blocks, 17
specific and 6 heuristic, 0 residue.

## Standing sections

### 0. Header and provenance

- What: The candidate opens with the interwiki-style frame at L1–3
  (priority=1 only; the theme= parameter it once carried was dropped by
  the codeaddr remedy, §3/§11) and the tag gate at L5,
  `[[iftags +テーマ]]` for the original's `[[iftags +theme]]` at original
  L1 (classifier block B1: IFTAGS). The original has no frame and no
  credit block; its head is the tag gate, its own bare Rate (L2–4), and
  prose.
- Why: P1 (frame supplement) and P2 (tag-name localization). The frame is
  the JP site's standard theme wrapper; the tag gate keeps the theme
  body from rendering on untagged pages, in the JP tag namespace.
- Verify: `sed -n '1,5p' candidate.txt` against `sed -n '1,5p' original.txt`.
- Disposition: T1 FINDINGS (classified): the 11 errors are the pseudo-ref
  class (draft-host delivery addresses), dispositioned in register c1
  [stamp; GOSIGN2-LEDGER (c1)].

### 1. Credit and attribution

- What: The candidate adds the preview credit block at L6–15 with all
  eight TASL fields: タイトル Spidersfalling; 翻訳責任者 AI; 翻訳年 2026;
  原題 Spidersfalling; 著作権者 [[*user Mooagain]]; 作成年 2022; 初訳時
  参照リビジョン 5; 元記事リンク
  https://scp-wiki.wikidot.com/theme:spidersfalling, which names the
  recorded original host (scp-wiki.wikidot.com) exactly. The original
  carries no credit block; its attribution is prose. Original L6 names
  Dc_Yerko (creator of the base xmas theme for the Spanish site),
  stormbreath (who adapted it), and EstrellaYoshte (snowflake code);
  original L8 names Mooagain, who modified the theme for Halloween and
  drew the spider image. The candidate's prose translates both lines
  with all four names and roles intact (candidate L17 and L19). The
  credit field names Mooagain alone, and that is the correct scope: the
  field records the author of this theme (the Halloween variant), and
  the other three names belong to the base theme's lineage, which the
  prose directly under the block carries. This is not the
  dropped-author shape: no name the original attaches to this theme is
  missing from the field, and no name is missing from the page.
- Why: P3 (credit supplement) with the TASL record per ruling 3 of
  RULINGS-20261116 (campaign translations credited to AI with the
  reference revision recorded). The failure prevented is an unattributed
  or misattributed port: a reader can trace the variant's author, the
  base theme's lineage, and the exact source revision from the page head.
- Verify: `sed -n '6,19p' candidate.txt`; `grep -n "Mooagain\|Dc_Yerko\|stormbreath\|EstrellaYoshte" original.txt candidate.txt` (each name once per file, in the prose).
- Disposition: Ledger (c3) row 139: P3 credit fields FIXED (credit waves,
  checker-verified) [GOSIGN2-LEDGER (c3) row 139]. No attribution defect
  is recorded by this package.

### 2. Includes and components

- What: The candidate's live includes are the frame (L1) and the credit
  pair (L6, L15); the body has no component includes on either side. The
  usage exhibits name JP addresses in escaped form: candidate L24 and
  L33 `[[include:scp-jp:theme:spidersfalling-jp]]`, and L32 the
  black-highlighter variant instruction naming
  `:scp-jp:theme:black-highlighter-theme` (classifier blocks B3, B5:
  ESCAPED-INCLUDE, INCLUDE-REPOINT). The original's exhibits name the
  EN addresses (:scp-wiki:theme:spidersfalling,
  :scp-wiki:theme:black-highlighter-theme).
- Why: P1 (include repointing to the pages that will exist on scp-jp).
  The failure prevented is a usage instruction that points a reader at a
  page name that will never exist on the JP wiki.
- Verify: `grep -n "include" candidate.txt` — every live or exhibited
  include names a :scp-jp: address or the credit/frame components.
- Disposition: T4 FINDINGS with 3 display-affecting findings
  [LOCALIZE-ROWS row 139]; the (c3) register closes this theme's P3 and
  P6 items as FIXED and no include finding stands against row 139.

### 3. Delivery mechanism

- What: No relocation and no self-delivery. Both files deliver CSS
  in-page through five [[module CSS]] blocks: the main module (original
  L30–151 with show="true"; candidate L41–162) and four
  parameter-gated variation modules whose gates are comment-wrapped
  include parameters — {$spidersfalling-header} (original L155 /
  candidate L166), {$spidersfalling-spiders} (L168 / L179),
  {$spidersfalling-header-bhl} (L278 / L289), {$spidersfalling-spiders-bhl}
  (L336 / L347). The gated contents are carried in place, neither inlined
  unconditionally nor dropped. A code-block census over all forms
  ([[code]], [[code type="CSS"]], other typed forms) finds zero code
  blocks on either side, so no local--code self-delivery address exists
  to audit; consistently, the frame carries no theme= parameter on
  current bytes (dropped by canonical 722ceb5, sub-shape (B) of the
  codeaddr audit: a frame delivery address for a theme that delivers
  in-page is dead weight; recorded here with its citation, not
  re-litigated).
- Why: Delivery parity (P10 family): the original's mechanism is
  in-page modules with include-parameter gates, and the port keeps the
  mechanism rather than substituting a code-block delivery. The failure
  prevented is a gate silently becoming unconditional (a variation
  applying to every page) or vanishing (a documented variation doing
  nothing).
- Verify: `grep -n "module CSS" original.txt candidate.txt` (five
  openers each); `grep -n "spidersfalling-" candidate.txt` (the four
  gates present); `grep -c "\[\[code" original.txt candidate.txt` (0/0).
- Disposition: No delivery finding in any register for row 139; the
  frame's present form is the codeaddr remedy's recorded outcome
  [FIX-CODEADDR.md; canonical 722ceb5].

### 4. Fonts and assets

- What: Fonts: none on either side — neither file contains @import,
  @font-face, or a font-family declaration (grep-verified); the section's
  font half is empty with that ground. Assets: the theme's single image,
  Spider.webp, appears on 11 lines on each side (original L56, L69, L82
  and the gated-module copies; candidate L67, L80, L93 and copies),
  re-hosted from scp-wiki.wikidot.com/local--files/theme:spidersfalling/
  to sigma10-jp-test.wdfiles.com/local--files/theme%3Aspidersfalling-jp/
  (classifier: DRAFT-HOST on 11 blocks).
- Why: KB-41 (patterns/ @ 9c5e907): a candidate's delivery assets are
  re-hosted under the candidate's own page name on the JP draft host
  (posting-rewrite class (iii)), so the theme does not hotlink the EN
  wiki's file area at runtime. The failure prevented is a port that
  renders only while the foreign wiki serves its files.
- Verify: `grep -c "Spider.webp" original.txt candidate.txt` (11/11);
  `grep -n "wdfiles" candidate.txt` (all asset lines name the draft host).
- Disposition: The render row's runtime-hotlink site-theme chain is
  DISPOSITIONED (KB-40) [GOSIGN2-LEDGER (c2) row 139]; the two remaining
  scp-wiki.wikidot.com strings in the candidate are content links (the
  credit source link, §1, and the xmas prose link, §7), not delivery.

### 5. Header, sidebar, and furniture

- What: The theme defines no --header-title or --header-subtitle
  variables on either side. Its furniture is the snowfall layer markup
  (#header-extra-div-1/2 and the .snowfall rules) and the spider
  background layers, all inside the main module and its BHL gated
  variant, carried without structural change (§3). The candidate adds
  and removes nothing in this layer.
- Why: Parity carry; no class fires. The failure this section exists to
  catch (a furniture rule or variable dropped in the move) does not
  occur: the modules moved as whole blocks (§3).
- Verify: `grep -n "header-extra-div" original.txt candidate.txt`
  (present in both, in the main and BHL modules).
- Disposition: No furniture finding in any register for row 139.

### 6. Text translation

- What: Prose translation at candidate L17 (the lineage line), L19 (the
  Mooagain line), L21 (the usage lead-in), and L28–35 (the BHL variant
  instructions). CSS comments are translated in place: the banner
  comment heading the main module (original L31–37 → candidate L42–48)
  and the SNOWFALL comment (candidate L60 and its gated-module copies).
  The classifier's TRANS-UNANCHORED blocks (7) and COMMENT-TEXT blocks
  (3) are this mass. No prose is left untranslated; "Spidersfalling" is
  the theme's name, an identity string.
- Why: T5 translation completeness; CSS comment translation is expected
  heuristic mass (residue class R1 in the TAXONOMY memo), resolved by
  shape in the appendix. The failure prevented is reader-facing English
  residue in a JP deliverable.
- Verify: diff hunks 1–4 in diff.md carry the whole prose change;
  `grep -n "SNOWFALL\|蜘蛛落下" candidate.txt` shows the comment
  translation in each module copy.
- Disposition: T5 FINDINGS under the joint T4/T5 verdict
  [LOCALIZE-ROWS row 139]; no untranslated-prose item stands against
  row 139 in the (c3) register.

### 7. Links

- What: The credit source link names the recorded host (§1). The prose
  links are the original's own content references, kept: the xmas theme
  link (scp-wiki.wikidot.com/theme:xmas, candidate L17) and the Spanish
  site link (lafundacionscp.wikidot.com, candidate L17) — both point at
  the works the lineage sentence names, in the wikis where they live.
  No prose link was repointed, and none needed to be: neither names a
  theme this campaign ports as a dependency of this page.
- Why: P11 applies to references the port itself must re-target (its
  own usage exhibits, §2; its dependency links); content references to
  the original works stay on their home wikis. The failure prevented is
  the item-88 shape (a prose link to a name that resolves nowhere),
  which does not arise here.
- Verify: `grep -n "wikidot.com" candidate.txt` — three occurrences:
  the credit link and the two lineage links, all accounted above.
- Disposition: No link finding for row 139 in any register.

### 8. Structure and exhibits

- What: Body order is preserved exactly: lineage prose, modifier line,
  usage exhibit, BHL-variant exhibit, then the five CSS modules (§3).
  Neither file uses + headings; the sections are prose-led on both
  sides, so the heading census is trivially equal. The BHL exhibit
  (original L20–24 → candidate L28–35) keeps its two-snippet structure
  (plain and black-highlighter forms) with JP addresses substituted.
- Why: Structure parity: an exhibit restructured or a body section
  dropped would misstate how the theme is used. Nothing of the kind
  occurs; the DELIVERY-MOVE label does not fire for this pair at all.
- Verify: `grep -n "module CSS" candidate.txt` (§3) plus a read of
  candidate L17–40 against original L6–29.
- Disposition: No structure finding for row 139.

### 9. Formatting only

- What: Two WS-ONLY blocks (blank-line placement around the head
  blocks). No other formatting-only change.
- Why: Class I-adjacent formatting; recorded so the churn count is
  fully accounted.
- Verify: classification.json, label_counts WS-ONLY = 2.
- Disposition: None required.

### 10. Porter annotations

- What: None. The candidate carries no bracketed porter note; the
  classifier fires no PORTER-NOTE label for this pair, and the only
  comments in the file are the original's own CSS comments, translated
  (§6). Ground: `grep -n "移植" candidate.txt` returns only the
  translated banner/comment text, no annotation.
- Why: Porter annotations are campaign-internal speech; their absence
  here means nothing internal ships in the deliverable.
- Verify: the grep above.
- Disposition: None required.

### 11. Dispositions and exceptions

- What: (a) The stamp's STALE verdict has exactly two causes, both
  recorded landings after the verdict head 435a6bb: b5cb724 (the
  snippet sweep completing the two usage-example lines to the -jp
  form, §2) and 722ceb5 (the frame theme= parameter dropped under
  codeaddr sub-shape (B), §3). Neither touches the item-30 locus beyond
  the frame line. (b) The render row's remaining findings are
  dispositioned, not open: runtime-hotlink site-theme chain (KB-40);
  sample credit-modal errors are the preview form's property
  (credit:start-preview has no modal mechanism; ruling 5 of
  RULINGS-20261116 and the GOSIGN-TESTS T2 amendment); the 884px@768
  overflow belongs to the cross-cutting overflow families (KB-33/KB-34).
  (c) T1's 11 pseudo-ref errors are the draft-host delivery addresses
  in the frame's history and the asset lines, classes (ii)/(iii),
  register c1.
- Why: A STALE stamp means the verdicts describe the pre-change file;
  this package exists so the reader can see exactly what changed and
  re-judge. The changes are enumerated above and in the Change set
  section; nothing else about the theme moved.
- Verify: `git log --oneline 435a6bb..HEAD -- pages/theme:spidersfalling-jp.txt` in the canonical repo returns exactly b5cb724 and 722ceb5.
- Disposition: As recorded; the go-sign's scope note applies (the
  verdict is Wikidot-side; the Wikijump phase is frozen and excluded).

### 12. Verification

- What: T1 baseline 11 errors / 1 warn / 1 info (stamp). The FIX5-FURNA
  checker run for the item-30 edit moved the candidate from 11/0/1 to
  11/0/0, clearing the double-rate info; the 11 standing errors are the
  pseudo-ref class. This package's own checks: original.txt SHA-256
  equals the sources.tsv value; candidate.txt is byte-identical to the
  canonical pages/ file; a brace-depth scan over both files ends at
  depth 0 and never goes negative; `grep -c "module Rate" candidate.txt`
  returns 0 (Per-theme record).
- Why: The cheapest deciding checks for this theme are the hash
  equalities and the Rate grep; a render re-check cannot decide a
  source-level duplication.
- Verify: the commands above, all runnable from this repo plus the
  canonical checkout.
- Disposition: T1 FINDINGS (classified) [stamp].

## Per-theme record — the FIX5 closures, re-derived

### Item 30 [B] — duplicate bare Rate beside the preview credit module

- Ledger: GOSIGN2-LEDGER (a) item 30 charges population #139 with class
  B (KB-09, duplicate rate modules): a bare [[module Rate]] sitting
  beside the preview credit module, which renders its own rate widget.
- Supplement: item 30 FIXED by FIX5-FURNA, commit 9e8931f
  [GOSIGN2-LEDGER-SUPPLEMENT (a) item 30].
- What the fix was supposed to change: FURNA's report records that the
  ported candidate had carried the original's bare Rate block over
  verbatim ([[>]] / [[module Rate]] / [[/>]] at pre-edit candidate
  L17–19, immediately after credit:end-preview at L16), duplicating the
  preview credit module's widget. The fix deleted those three lines and
  nothing else; the lane's checker run moved 11/0/1 → 11/0/0, the
  cleared info being the double-rate notice.
- Re-derivation from this package's bytes: the deletion is visible in
  the diff itself. Original L2–4 carry the bare Rate block (the
  original has no credit module, so on its home wiki the block is the
  page's only rate widget and is not a defect there). The candidate has
  no counterpart lines: `grep -c "module Rate" candidate.txt` returns
  0 — no Rate module in any case remains anywhere in the candidate,
  while the preview credit block stands at L6–15. Commit 9e8931f is an
  ancestor of the verdict head 435a6bb, and neither post-verdict
  landing (b5cb724, 722ceb5) touches the credit flow. The closure is
  confirmed from the bytes, not from the ledger.

### Register (c3) closures for row 139

- P3 (credit fields) FIXED: re-verified in §1 (eight fields present,
  author field correctly scoped, source link on the recorded host).
- P6 (frame) FIXED: the frame stands in its interwiki form at L1–3;
  its current parameter set is the codeaddr remedy's outcome (§3).

## Per-theme record


### Post-package repairs (REFRESH3-D)

Recopy was a verified no-op: `candidate.txt` is byte-identical to the current canonical `pages/theme:spidersfalling-jp.txt`. No repair lands after this package's candidate build, so the record below is the slice's sub-shape and remedy, confirmed present in the built bytes.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Aspidersfalling-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- The two post-FIX5 landings (b5cb724 usage sweep and 722ceb5 frame remedy) are already recorded in sections 3 and 11 and the multi-wave provenance; both predate the package build `cb269a7`.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

None belonging to this theme beyond the two stamp-cause landings
(b5cb724, 722ceb5), both of which touch only this candidate file and are
inside its history below. The item-30 fix (9e8931f) predates the verdict
head; its effect is visible in the diff (Per-theme record).

## Multi-wave provenance

765e2f8 (Stage 2 EN19 port) → 666f543 (FIX2-CREDIT) → 8c62b7b
(FIX4-IWA, frame) → 9e8931f (FIX5-FURNA, item 30) → b5cb724 (snippet
sweep, usage examples) → 722ceb5 (codeaddr sub-shape (B), frame). The
mirror is revision 5 throughout; no wave re-based the port on a later
original revision.

## Appendix — heuristic and residue adjudication

Residue blocks: none (0 of 23). The classifier's 6 heuristic blocks are
adjudicated by shape: B2 (head region, mixed labels — the frame, credit,
and prose changes of §§0–2); B9 and B14 (CSS-BODY with COMMENT-TEXT —
the snowfall CSS whose comments are translated, §6); B13 and B18
(TRANS-UNANCHORED heuristic — gated-module CSS and comment mass, §6);
B22 (INCLUDE-REPOINT heuristic — the BHL exhibit's address, §2). No
block is left unexplained, and no heuristic block conceals a content
drop: the module census (§3) and the asset census (§4) are equal on
both sides.

## License and attribution

- **Title:** Spidersfalling
- **Author:** Mooagain
- **Source:** https://scp-wiki.wikidot.com/theme:spidersfalling — revision 5
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
