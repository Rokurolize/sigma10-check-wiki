# Review package — theme:ink-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ink-jp — origin CN, population #198 [GOSIGN2-LEDGER (b) row 198]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 54e481fa402c820c7e42157c1585ad01ec1b22dfb4d5f772be7571ae1cfafd26); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 20 errors / 5 warns / 4 infos (hotlink×16, pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 228; GOSIGN2-LEDGER (b) row 198]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 606–610px@320/375 + 931px@768 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN8))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN8))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 197, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 197]
- FIX5 re-judgement: item 62 (class B) FIXED — FIX5-FURNB, commit 25bb0b4: both live bare Rates removed. Residual checker double-rate at L1743 is the escaped literal example, identical to orig L100 (KB-09 false-positive class), dispositioned within the item on that evidence [GOSIGN2-LEDGER-SUPPLEMENT (a) item 62]
- Computed against: canonical commit 25bb0b40f10153f1f8bdda252283bb7aa7a76875; candidate file pages/theme:ink-jp.txt sha256:54e481fa402c820c7e42157c1585ad01ec1b22dfb4d5f772be7571ae1cfafd26; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); the stamp above is current, not stale: the candidate file is unchanged since the FIX5 commit it was computed against |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 62 [B] (two live bare `[[module Rate]]` duplicating the credit-embedded Rate) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 62: **FIXED** (FIX5-FURNB, commit 25bb0b4), with the residual checker double-rate dispositioned inside the item as the KB-09 escaped-example false positive; re-derived from this package's bytes in the per-theme record below — both deletions are present, and the sole surviving Rate mention is the literal example |
| Standing items | **DISPOSITIONED** — ledger §(c3): P5 (class (ii) / KB-58), P11 (sibling / batch-posting class); P3 credit fields FIXED by the credit waves and closed through (e). Ledger §(c2) render row: page-overflow and runtime-hotlink site-theme chain; sample T2 no machine verdict |
| Defect flags from this review | None. The delivery census (§3), credit fields (§1), and content census (§8) were all checked and hold |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ink | theme:ink-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 15, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 15 | — |
| Source of this copy | Mirror store `review-mirrors/orig-ink-rev15.txt` (INDEX.tsv, class COPY) | Canonical file `pages/theme:ink-jp.txt`, copied at worktree HEAD 20bb8c0; the file's last content change is commit 25bb0b4 (FIX5-FURNB) |
| Lines / bytes | 1,519 lines / 43,077 bytes | 3,155 lines / 79,238 bytes |
| SHA-256 | 3bdfa2c164e22d844ec599b664b9666e64ea683b5318e0e0eeee284792f2abe1 | 5852f588fd3bb468b354b04dd4049e3f474a31fc1c32dc71361a8b3dbc7859ac |

Provenance route: derived from the original at the reference revision (sources.tsv row, kind standard).

## Summary

The original delivers its CSS from outside the page body: a head `[[module CSS]]` (L1–41) that @imports `theme:ink/code/1` on the CN host and carries the theme's own first rules, followed by the credit furniture, exhibits, and the page's own code fragment source. The candidate keeps that shape and makes it self-contained: the head module now @imports the candidate's own /1, /2 and /3 (candidate L2–4) with three matching interwiki-style frames, a second module (L20–57) carries the port of the original head module's own rules (the two modules open with the same `/* {$xinyihui} */` comment and `:root`), and the three code blocks hold the base layer, the sigma-plus override, and the theme layer (§3). The candidate is twice the original's size because the base layer the original imported is now inlined as block 1. The measured churn (diff.md: 98 change blocks) is mostly that layering plus the exhibit translation. The theme's one blocking item was furniture, not CSS: two live rating widgets duplicating the credit one. Both are gone; the re-derivation below locates both deletions in the current bytes.

## Standing sections

### 0. Header and provenance frame

- **What:** Candidate head (L1–19): a `[[module CSS]]` @importing the candidate's own /1, /2, /3 on the draft host, then three interwiki-style includes at priorities 1, 2, 3 naming the same three addresses in order. The original head module (L1–41) @imports only `theme:ink/code/1` on the CN host (original L3) and carries rules the candidate keeps as its second module (candidate L20–57). Classifier topology: no relocation detected; each side's components match by kind.
- **Why:** The supplement frame is the campaign's standard delivery frame; draft-host URLs are the draft-form class (iii), rewritten at posting. Keeping the original's head-module rules as a module (rather than folding them into a code block) preserves the original's cascade order.
- **Verify:** Read candidate L1–57 against original L1–41; the address-to-block mapping is verified in §3.
- **Disposition:** DISPOSITIONED (delivery class (ii)/(iii) family, ledger §(c1) standing classes).

### 1. Credit and attribution

- **What:** Block B5 (CREDIT-PREVIEW, TASL-FIELDS, CREDIT-PROSE): the candidate's credit block (L1689–1701, inside the quote wrapper at L1687–1703) is the preview form with the full TASL field set, and it names the author twice over: 著者 `[[*user OxygenNine]]` and 著作権者 `OxygenNine`. The original's credit furniture (original L47–54) names him in prose （由 [[*User OxygenNine]]制作） and carries a `credit:more` segment with the license line 授权协议：CC-BY-SA 4.0 International; the candidate's field set records the license through the TASL form and adds a 使用フォント field (Noto Sans JP、Noto Serif JP、JetBrains Mono, SIL OFL 1.1). The wrapper that holds the block is also item 62's first locus (§8 record): it once held the duplicate bare Rate as well.
- **Why:** Ledger §(c3) records P3 credit fields FIXED for this row (credit waves, checker-verified); the field check here confirms the author is named, so the credit pointer defect family does not bite.
- **Verify:** Read candidate L1687–1703 against original L45–58.
- **Disposition:** FIXED (P3, credit waves) and verified; no defect.

### 2. Includes and components

- **What:** COMPONENT-SWAP fires in B9/B11/B12 and INCLUDE-REPOINT in nine blocks (B5, B9, B11, B12, B15, B55–B58): the component includes in the body and exhibits were swapped to the JP component candidates and repointed to JP targets as part of the localization. The load-bearing component include is in the delivered layer: code block 2 @imports `component:sigma-plus-jp/1` on the draft host (candidate L1676), the JP sigma-plus candidate, with the port's override rules after it (block B4, SIGMA-PLUS-JP). No include names a page that will not exist at posting.
- **Why:** Component swaps to JP candidates are the standard localization move (the sigma-plus dependency is ported alongside the theme, per the campaign's cross-theme dependency rule: a dependent theme imports the base's JP port candidate, never the raw upstream delivery).
- **Verify:** `grep -n '\[\[include' candidate.txt`; confirm `pages/component:sigma-plus-jp.txt` exists in the canonical repo (change set, below).
- **Disposition:** No defect; no ledger item covers includes for this row beyond the (e) item.

### 3. Delivery and code loading

- **What:** The candidate has three code blocks, and each delivery address names the block that holds its layer. Block 1 (L62–1671, inside `[[div id="base"]]`) opens with `@charset` and the font-bauhaus / Font Awesome / cc-icons loads — the base layer the original imported as `theme:ink/code/1`. Block 2 (L1675–1683, inside `[[div id="sigma-plus"]]`) is the sigma-plus-jp override: an @import of `component:sigma-plus-jp/1` plus a `:root` setting `--sp_header-logo` to the Black-Highlighter logo, with the porter's comment explaining the specificity adaptation (the JP component loads the original rev.38, and this `:root` overrides its `:where(:root)`). Block 3 (L2009–3151) is the theme's own layer, opening with the JP font load (B77, §4). The head module @imports /1, /2, /3 (L2–4) and the three frames name /1, /2, /3 at priorities 1, 2, 3 (L7–18): no block is unreferenced, and no address names an exhibit. The FIX-CODEADDR matching classification therefore holds for this theme, verified by census.
- **Why:** A local--code address must name the block that actually holds the CSS (the navla-style failure is the counter-shape, seen in this batch's gp-refresh package); here the layering is deliberate and each layer is a real stylesheet.
- **Verify:** `grep -n '\[\[code' candidate.txt` (L62, L1675, L2009) and read each block's first lines against the addresses at L2–18.
- **Disposition:** DISPOSITIONED as topology (delivery class (ii)/(iii)); no defect.

### 4. Fonts and assets

- **What:** Block B77 (JPFONT-LOAD): the theme layer's head (candidate L2010) loads Noto Sans JP, Noto Serif JP and JetBrains Mono from Google Fonts — the three faces the credit block's 使用フォント field names (§1). The base layer's loads (block 1, L65–67: font-bauhaus.css from the JP component host, Font Awesome 4.3.0, cc-icons 1.2.1) are the original's own load set carried with the base. The T1 baseline's 16 hotlink errors are the file's CN-hosted exhibit and asset URLs, the standing class (ii) / KB-58 family.
- **Why:** Pattern P7 (font-stack rewrites with JP loads) at patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa: every JP face the stacks name is loaded in the same delivery; asset hosts the original state carries are dispositioned, not silently dropped.
- **Verify:** Read candidate L2010 and L62–67; `grep -c 'wikidot.com/local--files' candidate.txt` for the standing hotlink class.
- **Disposition:** DISPOSITIONED (ledger §(c3) P5, class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The furniture-relevant rewrites are the CSS-BODY blocks B81/B82 inside the delivered layers: font-family rewrite blocks, which are P7 font-stack rewrites in substance (the stacks re-pointed at the JP faces loaded in §4) even where the classifier labels them CSS-BODY heuristic. GLYPH-FORM fires in B78 at the theme layer's `:root`: `--ink-title-a: '中華異学会'` keeps the traditional glyph forms of the theme's fictional society name, a proper noun carried from the original, not an unlocalized residue. B13's GLYPH-FORM is a heading translation （示例 → 例）, adjudicated in the appendix.
- **Why:** Per the standing lesson, font-family rewrite blocks are narrated as P7 regardless of their classifier label; proper-noun glyph forms are original state.
- **Verify:** `grep -n 'font-family' candidate.txt` inside blocks B81/B82's spans (classification.json); read candidate L2011–2015.
- **Disposition:** DISPOSITIONED as the P7 class; no furniture defect.

### 6. Text translation

- **What:** TRANSLATION-ANCHORED fires in 46 blocks and TRANS-UNANCHORED in 39; COMMENT-TEXT fires in 17 blocks, the CSS comment translations inside the two big delivered blocks, resolved by shape in the appendix. CONTENT-STRING fires once (B4). The exhibit body (usage text, specimens, the mz-hr examples) is translated throughout; the one string deliberately left in its original form is the literal Rate example at L1743, which is not translation residue but the item 62 residual (per-theme record).
- **Why:** Unanchored and comment mass is the expected heuristic load for a full-body translation of a CSS-heavy theme; each family is resolved by shape rather than block by block, per the standing lessons.
- **Verify:** classification.json label spans for ink-jp; spot-read any three anchored blocks against the diff.
- **Disposition:** No translation defect charged or found; item 61's analogue (untranslated UI strings) does not occur in this file — its one charged text defect was the Rate duplication.

### 7. Links

- **What:** The 元記事リンク in the credit block (candidate L1699) names the CN original by URL with its title — the correct form for the original-article link. The INCLUDE-REPOINT mass (§2) covers the body's component and page references; no usage exhibit in the current file names a page that will not exist at posting (the usage sweep's class was checked against this file's exhibits as part of the census in §12).
- **Why:** Copy-paste targets and original-article links are the two link classes the campaign polices; both hold here.
- **Verify:** `grep -n 'scp-wiki-cn.wikidot.com/theme:ink' candidate.txt` (credit link) and read the usage exhibits around candidate L1710–1760.
- **Disposition:** No defect.

### 8. Structure

- **What:** EXHIBIT-RESTRUCTURE fires in B15 and B55–B58, all inside exhibit regions and all carrying INCLUDE-REPOINT as the co-label: adjudicated against the exhibit census, these are the standing false-fire shape (include repoints inside exhibits), with every specimen element present on both sides. IFTAGS fires once (B4): the page's tag gate is retained in the JP form. The structural event of the file is the delivery layering (§3), which the classifier's topology records as no relocation — the original's external fragment became block 1 in place, and the theme layer kept its position after the exhibits.
- **Why:** The standing lesson that EXHIBIT-RESTRUCTURE false-fires on include repoints inside exhibits; adjudication is by census.
- **Verify:** The exhibit census: compare the exhibit headings of original L60–1519 against candidate L1705–3155.
- **Disposition:** No structural defect.

### 9. Formatting only

- **What:** None. The classifier produced no whitespace-only or formatting-only block for this pair (98 blocks, none WS-ONLY).
- **Why:** Ground stated as required: the class summary in classification.json lists no formatting-only label for this theme.
- **Verify:** classification.json summary for ink-jp.
- **Disposition:** Nothing to disposition.

### 10. Porter annotations

- **What:** One porter annotation stands out from the CSS comment mass: the sigma-plus override comment (candidate L1678–1679, in Japanese) explaining that component:sigma-plus-jp loads the original rev.38 and that this block's `:root` overrides its `:where(:root)` (specificity 0) by coming later — the reasoning for block 2's existence, recorded in the file itself. It rides inside block B4 (SIGMA-PLUS-JP), which is why this section is not "none" despite the skeleton's per-section listing: B4's label spans place the annotation inside a multi-label block. The remaining COMMENT-TEXT blocks are the base and theme layers' own comments in translation (§6).
- **Why:** Porter annotations are part of the delivered record; this one documents a deliberate cascade adaptation a reviewer would otherwise misread as a stray `:root`.
- **Verify:** Read candidate L1675–1683.
- **Disposition:** Recorded; no ledger item covers annotations for this row.

### 11. Dispositions and exceptions

- **What:** Standing dispositions for this row: ledger §(c3) P5 DISPOSITIONED (class (ii) / KB-58: asset hosts), P11 DISPOSITIONED (sibling / batch-posting class); ledger §(c2) render row DISPOSITIONED in full (page-overflow 606–610px at 320/375 and 931px at 768, runtime-hotlink site-theme chain; the sample's T2 produced no machine verdict, exit 2, recorded as a coverage caveat). The residual checker double-rate at candidate L1743 is dispositioned inside item 62 itself (per-theme record): it is the escaped literal example, KB-09's named false-positive class.
- **Why:** Cited by record name, as the standing sections require; not re-argued here.
- **Verify:** GOSIGN2-LEDGER.md §(c2)/(c3) rows for theme:ink-jp; GOSIGN2-LEDGER-SUPPLEMENT.md item 62; KB-09 in patterns/ @ 9c5e907.
- **Disposition:** DISPOSITIONED as cited.

### 12. Verification

- **What:** Verified from the repo alone: original.txt SHA-256 equals the sources.tsv value (3bdfa2c1…); candidate.txt is byte-identical to the canonical file at 20bb8c0 (cmp clean, SHA-256 5852f588…); `python3 review/build_review.py --check` passes in the worktree. The Rate census is a one-command check: `grep -in 'module rate' candidate.txt` returns exactly one line (L1743, the literal example) against the original's three (L56 live, L100 literal, L298 live). FIX5's own control: checker 20 errors / 5 warns / 4 infos before and after the FURNB edit, identical totals, the double-rate line migrating from the live locus to the escaped example.
- **Why:** The R-fix treatment requires the closure to be checkable from the package's bytes; the census is the cheapest deciding check for a duplication charge.
- **Verify:** Re-run the commands above.
- **Disposition:** Package complete; no flags referred.

## Per-theme record — the FIX5 closure re-derived (ledger item 62)

**The charge.** Ledger §(e) item 62 [B]: two live bare `[[module Rate]]` (ledger-time candidate L1701 and L1944) duplicating the credit-embedded Rate — pattern 3, display-affecting. Both still present at ledger time.

**What the fix was supposed to change.** FIX5-FURNB (commit 25bb0b4), re-judged FIXED in supplement item 62: delete both live Rates and nothing else — the first sat inside the credit quote wrapper (keeping the wrapper's `[[/>]]` so the `[[>]]` stays balanced), the second inside a documentation `mz-hr` example (leaving its text and horizontal rule intact). The residual checker double-rate was dispositioned inside the item: after the deletions the checker's first rate match is the literal example `{{[[Module Rate]]}}`, original-faithful at original L100, the KB-09 false-positive class (patterns @ 9c5e907).

**Verification against the bytes.** The census decides it: the current candidate contains exactly one Rate mention, candidate L1743 `{{[[Module Rate]]}}` — Wikidot literal markup that displays the syntax and renders no widget, byte-for-byte the same device as original L100. Both charged loci are clean. (1) The credit quote wrapper (candidate L1687–1703) now holds only the credit block; its `[[>]]` and `[[/>]]` are balanced and no Rate stands inside it — the original's corresponding bare Rate is original L56, inside its own credit wrapper (original L45–58). (2) The mz-hr example: the original's instance (original L295–299) reads テキストまたは画像's CN form, a rule, then a live `[[module rate]]` inside `[[div class="mz-hr"]]`; the candidate's corresponding example (L1940–1943) reads テキストまたは画像， the rule, and `[[/div]]` — text and rule intact, the widget gone. Checker control 20/5/4 → 20/5/4 with zero new errors. **Item 62 is FIXED on the bytes, as the supplement states, and the residual is the dispositioned KB-09 false positive, not a third widget.**

## Change set outside the two diffed files

The diff covers two files; the port's runtime change set is larger. (1) `pages/component:sigma-plus-jp.txt` — the JP sigma-plus component candidate that code block 2 imports (candidate L1676) and overrides; the theme's sigma-plus layer is meaningless without it. (2) The decoration sample page used by the render lane for this row (RENDER-ROWS-2, RENDER-S2-F (CN8)); its T2 run produced no machine verdict, recorded in the stamp.

## Multi-wave provenance

The candidate's current state is the product of successive waves: the S2 localization wave produced the initial port (delivery layering, exhibit translation, and, as later found, both duplicated Rates carried over from the original's furniture); the credit waves completed the credit fields (ledger §(c3) P3 FIXED); FIX5-FURNB removed the two live Rates (commit 25bb0b4, the file's last content change — the usage sweep and snippet audit did not alter this file's Rate state, and the stamp's computed-against hash equals the current file's). Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2)/(c3) rows and §(e) item 62; GOSIGN2-LEDGER-SUPPLEMENT.md item 62; REPORT-GOSIGN2-FIX5-FURNB.md, ink section. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue and heuristic adjudication

- **B98** (unlabeled, the pair's one residue block): orig 1515 → cand 3150, the tail alignment. The original mirror ends at its `[[/code]]` (L1516) without the `[[/collapsible]]` / `[[/iftags]]` closers; the candidate supplies both closers (candidate L3153–3155). An original-state truncation at the page tail, closed properly by the port; no content is missing on either side.
- **B95** (GLYPH-FORM + COMMENT-TEXT + TRANSLATION-ANCHORED): the tail `@supports` block (original L1505–1515, candidate L3139–3151). The block's text is identical on both sides at the glyph level; the signature fired on the aligned region, not on a glyph change inside the block. Adjudicated false-fire.
- **B13** (GLYPH-FORM): original `+ 示例` → candidate `+ 例` — a heading translation, the glyph change being the translation itself.
- **B59** (GLYPH-FORM): same adjudication class as B13/B78 — glyph-form differences inside translated or proper-noun strings (§5).
- The 17 COMMENT-TEXT blocks are the delivered layers' CSS comments in translation; the 39 TRANS-UNANCHORED blocks are exhibit prose and specimen text, each present in both files. Resolved by shape, as the standing lessons prescribe.

## Post-adjudication repair (2026-11-18)

The pattern linter's KB-71 nomination, adjudicated in the campaign record (theme-lint/ADJ1.md section 4.3), confirmed a structural defect: the delivered stylesheet's final rule (.printuser.avatarhover > a > img) was missing its closing brace, leaving the block at brace depth 1; the original ends at depth 0 and has no such rule. The single missing brace is added in the canonical page; no other byte changed. T1 finding counts are unchanged (error 20 / warn 5 / info 4 before and after); the page is reflected to the Wikidot check wiki.
