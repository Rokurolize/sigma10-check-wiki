# Review package — theme:paradigm-inapplicable-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:paradigm-inapplicable-jp — origin CN, population #213 [GOSIGN2-LEDGER (b) row 213]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9604baa9b97a04b9e6b859cdd7d711a1d3b0a4d29fea575567be55965c57fdbc); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (hotlink×5, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 183; GOSIGN2-LEDGER (b) row 213]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 996–999px@320/375 + 1018px@768 (page) and 581–584px@320/375 + 996–1018px (sample); sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-F (CN11))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN11))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 212, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 212]
- FIX5 re-judgement: item 68 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: pattern-7 fix (paradigm family) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 68]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:paradigm-inapplicable-jp.txt sha256:9604baa9b97a04b9e6b859cdd7d711a1d3b0a4d29fea575567be55965c57fdbc; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 68 [D] (pattern 7: the JP font is named in the stacks but never loaded) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 68: **FIXED** (FIX5-FONTSA, commit 8eacd6e); re-derived from this package's bytes in the per-theme record below |
| Standing items | **DISPOSITIONED** — ledger §(c3): P4 (delivery class (ii): original-state CDN delivery), P5 (class (ii) / KB-58), P11 (sibling / batch-posting class); ledger §(c2) render row: page-overflow in the KB-33 / KB-34 families, sample credit-modal preview form (KB-32) |
| Flagged in this package | No defect flags. Three observations are recorded rather than passed over: the review/sources.tsv supersession note is wrong (section 0), the credit block's title field carries the original-language title (section 1), and the original's code-display collapsible survives empty (section 8) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:paradigm-inapplicable | theme:paradigm-inapplicable-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 132, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 132 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-paradigm-inapplicable.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:paradigm-inapplicable-jp.txt`, copied at worktree HEAD a0a5549 |
| Lines / bytes | 773 lines / 22,690 bytes (the file's last line carries no trailing newline, so `wc -l` reports 772) | 785 lines / 24,732 bytes |
| SHA-256 | 333745dc397502cc400384b91a6bfba2b702ae05e281735da5abe0f7b440dc49 | 9604baa9b97a04b9e6b859cdd7d711a1d3b0a4d29fea575567be55965c57fdbc |

Wave history: the candidate was created by the Stage 2 CN11 integration (commit b8ee399); REWORK2-P4 (7d9877c) separated the inlined Dustjacket base back to the pinned jsDelivr @import form; FIX-CREDIT-D (1869877) normalized the translator attribution; FIX5-FONTSA (8eacd6e) loaded the named JP font (item 68); the usage-example population sweep (b5cb724) completed the usage example's posting name (one line, candidate L82). The sweep line is the post-verdict change the stamp's STALE line records; it does not touch item 68's closure.

One provenance record is wrong and is corrected here, not silently carried: the review/sources.tsv note for this theme claims the original was superseded upstream after the reference revision. The follow-up artifact the note cites (`gosign2-lanes/lane-oc-gs-localize-s2-E/diff-paradigm-inapplicable-from132.txt`) records rev 132 → rev 132 with no changes. Upstream latest remains revision 132, the revision this mirror freezes.

## Summary

A Dustjacket-family theme by Mercuresphere, written for the Wanderers' Library "Paradigm Shift" hub. The original delivers its CSS two ways at once: a head module importing its own code fragment from the CN wiki's file host, and a `[[code]]` exhibit whose first line @imports the pinned Dustjacket base (Crimone's crimson-anemone, version 2.4.4) from jsDelivr. The candidate consolidates the CSS into a single code exhibit (the original's inline banner module folds into it; classifier body similarity 0.98), delivers that exhibit through the standard tail frame on the draft host with the pinned base import ahead of it, swaps the credit furniture for the JP preview credit block, translates the documentation body, and (the FIX5 item) loads the JP serif face the stacks already named. Measured churn (diff.md, the generator's difflib count): +226/−214 in 13 change blocks (9 specific, 0 heuristic, 4 residue, all residue resolved in the appendix). The one blocking item is closed and re-derived below; no defect is flagged.

## Per-theme record — the FIX5 closure of ledger item 68, re-derived

- **The item.** GOSIGN2-LEDGER.md §(e) item 68 [D]: pattern 7, "JP font named but never loaded", in the FINDINGS (display/delivery-affecting) set of LOCALIZE-ROWS row 212 (LOCALIZE-S2-E). The ledger's snapshot of the defect: "Current file: 0 Google Fonts imports." The stacks naming the unloaded face are the header/title/UI/mono variables, and the theme's own font-description prose claims the face for those surfaces, so JP glyphs on them fell back to an OS default.
- **The re-judgement.** GOSIGN2-LEDGER-SUPPLEMENT.md row 68: FIXED, by FIX5-FONTSA, commit 8eacd6e, "pattern-7 fix (paradigm family)".
- **What the fix was supposed to change.** Load the named JP face (Noto Serif JP) without touching the stacks that already name it and without altering any Latin face (REPORT-GOSIGN2-FIX5-FONTSA.md §9).
- **Re-derivation from this package's bytes.** (1) The pre-fix state is visible against the mirror: the original's stacks name 'Noto Serif SC' (original L363–366 and L749–750; 7 occurrences of the SC name in original.txt), and the candidate's corresponding stacks name 'Noto Serif JP' (candidate L366–369 and L752–753; 11 occurrences of the JP name in candidate.txt, 0 of the SC name). (2) The load is present: candidate L214, `@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;700&display=swap');`, the file's only Google Fonts import, at the head of the delivered code block where a CSS @import is valid, preceded by the fix's own provenance comment (candidate L209–213). (3) The fix commit's diff for this file is exactly +6 lines (the comment and the import), matching the lane report's account line for line. (4) Completeness: every stack that names a JP face names Noto Serif JP, and that face is loaded; no imported face goes unapplied (the import's single family is the one the stacks and the font-description prose name). The closure holds on the current bytes.
- **Post-verdict change.** One line, the usage-example posting name (candidate L82), landed in the population sweep (b5cb724) after the verdict. The generated stamp therefore reads STALE rather than carrying the PASS onto changed bytes; the change is outside item 68's scope and is recorded here so the reader can see exactly what moved.

## 0. Header / provenance

- What: the original opens with a head `[[module CSS]]` (original L1–5) importing its own code fragment from scp-wiki-cn.wdfiles.com. The candidate opens with `[[iftags +テーマ]]` (candidate L1); its provenance is carried by the credit block (candidate L3–12), whose 元記事リンク names https://scp-wiki-cn.wikidot.com/theme:paradigm-inapplicable, the host recorded for the original in review/sources.tsv. No link in the candidate substitutes a different host for the original's.
- Why: the head import module is the original's delivery channel; in the candidate that channel moves to the tail (section 3), and the head carries the JP environment's tag gate and credit furniture instead (P1/P2 posting conventions).
- Verify: read candidate L1–12 against original L1–9; `sha256sum original.txt` against the review/sources.tsv row.
- Disposition: provenance route is derivation from the original at revision 132 (mirror class COPY); the wrong supersession note in review/sources.tsv is corrected in the Provenance section above.

## 1. Credit and attribution

- What: the original's credit furniture is the CN credit:start/end pair (original L131–137) naming **作者：** [[*user Mercuresphere]] and a header-image credit line. The candidate carries the eight-field preview credit block (candidate L3–12): 著作権者 Mercuresphere (the author the original names; no pointer, no omission), 翻訳責任者 AI under the campaign's TASL ruling, 作成年 2022, 初訳時参照リビジョン 132, and the source link. The author line also stands in the body (candidate L19) and the header-image credit is retained (candidate L21, the same pixabay id-1572988 as original L135). The original's bare `[[module Rate]]` (original L128, inside a `[[>]]` container) is absent from the candidate; the container pair survives empty at candidate L16–17. One observation: the block's タイトル field carries the original-language title, identical to its 原題 field. No Japanese title for this theme exists anywhere in the candidate body, so the field contradicts nothing in the file; the state is recorded here because a reviewer will notice it, and it is not flagged.
- Why: P3/T1 credit swap; the JP preview credit module is the rate-bearing form, so the separate Rate module goes (the KB-32 preview-form family). Attribution follows ruling 3 (campaign translations credited 翻訳責任者「AI」 with the TASL record in the block).
- Verify: `grep 著作権者 candidate.txt`; `grep -c "module Rate" candidate.txt` returns 0; compare candidate L3–12 with original L131–137.
- Disposition: T1 credit findings are dispositioned in ledger register (c1); no P3 item stands against this theme in §(c3).

## 2. Includes and components

- What: three include-level changes. The tag gate localizes: original `[[iftags +版式]]` (L9) becomes `[[iftags +テーマ]]` (candidate L1, closing at candidate L776), wrapping the whole page. The credit includes swap to `:scp-jp:credit:start-preview` / `:scp-jp:credit:end-preview`. The tail gains the `:scp-jp:component:interwiki-style` include (candidate L782–785, priority=1, theme= the candidate's own fragment 1). Neither side carries any other include.
- Why: P2/T2 tag localization (KB-08: iftags conditions name JP tags); the interwiki frame is the environment's standard furniture for externally framed themes.
- Verify: `grep -n "\[\[include" original.txt candidate.txt` and compare the two lists.
- Disposition: KB-08 form; no include item stands in §(c3) for this theme.

## 3. Delivery and code loading

- What: topology consolidation, module-css → code-css (classifier body similarity 0.98). The original spreads its CSS over a head import module (L1–5), an inline banner module (L11–119), and the code exhibit (L316–771) whose head @imports the pinned Dustjacket base. The candidate carries one `[[code type="css"]]` block (candidate L207–773, 565 content lines) into which the banner module's CSS folds, and a tail `[[module css]]` (candidate L778–781) that imports first the pinned base, `https://fastly.jsdelivr.net/gh/Crimone/crimson-anemone@2.4.4/dustjacket.css` (the version the original pins at its L324), then the candidate's own fragment 1 from the draft host (sigma10-jp-test.wdfiles.com). The exhibit's own copy of the base @import (original L324) is deleted (classifier label DUPIMPORT-DEL): the live import sits in the tail module ahead of the theme's fragment, so the base loads exactly once and before the theme's CSS, the same cascade order as the original. The wave that produced this shape is REWORK2-P4 (commit 7d9877c), which separated the CN11 candidate's inlined Dustjacket copy (about 2,195 lines removed) back to the pinned-import form. Self-delivery census: exactly one code block in the candidate, counting every form (`[[code]]`, `[[code type="css"]]`, other typed forms); both fragment-1 references (the tail import and the interwiki frame's theme=) name it, and it is the stylesheet itself, not a small exhibit beside an unreferenced larger block. No entry in FIX-CODEADDR.md or FIX-NAVLA.md names this theme.
- Why: P4 delivery; pattern 4 for this theme is dispositioned as KB-14 verbatim import (the pinned third-party base is imported, never inlined or re-hosted), and the tail frame is the population's standard delivery for code-exhibit themes (patterns/ at commit 9c5e907).
- Verify: `grep -n "@import" original.txt candidate.txt` (original 2, candidate 3 including the font load of section 4); count code blocks in candidate.txt (1).
- Disposition: P4 DISPOSITIONED in ledger §(c3) (delivery class (ii): original-state CDN delivery).

## 4. Fonts and assets

- What: the font story is item 68, re-derived in the per-theme record: the stacks (candidate L366–369, L752–753) name 'Noto Serif JP' where the original named 'Noto Serif SC', and candidate L214 loads that face from Google Fonts. The stacks also retain CN system face names from the original ('HanWang WeiBeiMedium-Gb5', '仿宋', 'kaiti'); those are local font names, not web loads, on both sides, and the FIX5 lane recorded leaving them because altering them would be an uncharged redesign. The theme's font-description prose (in the exhibit body) claims Noto Serif JP for the header, title and mono surfaces; after the load that claim is true. Assets: the border images on wanderers-library.wdfiles.com and evernight-aquarium.wdfiles.com (candidate L416, L426, L758) and the pixabay header image are the foreign-host asset family.
- Why: pattern 7 (the JP face a stack names must be loaded; classifier signature JPFONT-LOAD); the asset hosts are the KB-58 class (original-state assets retained pending re-hosting decisions, not port-introduced).
- Verify: `grep -c "Noto Serif SC" candidate.txt` returns 0; `grep -c "fonts.googleapis" candidate.txt` returns 1; the loaded family is the one the stacks name.
- Disposition: P7 → §(e) item 68, FIXED (supplement row 68); P5 DISPOSITIONED in §(c3) (class (ii) / KB-58).

## 5. Header, sidebar, site furniture

- What: the interwiki style frame. The original embeds it hidden in the body copy: an iframe for scp-wiki-cn.wdfiles.com/local--files/nav%3Aside/styleFrame.html?bhl inside a `display:none` div and an `[[embed]]` (original L120–126). The candidate carries the JP environment's form as a single bare iframe after the credit block (candidate L14, `//interwiki.scp-jp.org/styleFrame.html?bhl`), and the tail's interwiki-style include (section 2) frames the theme's own fragment for other pages. One iframe per side.
- Why: P6 furniture follows the environment: the frame target is the JP interwiki host, and the bhl variant is the population's standard.
- Verify: `grep -n "styleFrame" original.txt candidate.txt` (one hit each).
- Disposition: not charged by any register; recorded as the standard environment form.

## 6. Text translation

- What: the documentation body is translated CN → JP in place: the color exhibit （深海， 燐光， 空色， 巻層雲， 深淵， ターコイズ， キュラソー for the original's Deep Sea, Phosphorescence, Azure, Cirrostratus, Abyss, Turquoise, Curacao), the usage prose, the exhibit labels and the collapsible titles. CSS comments are translated in part (classifier COMMENT-TEXT). The anchored translation spans the classifier pairs are the two `:root` blocks (B9, B10), whose face-name substitution is counted in section 4; the unanchored mass is the body translation, resolved by shape in the appendix. Retained Chinese glyph forms are confined to font names ('仿宋', the HanWang face name), which are proper nouns, and to the credit title field recorded in section 1. The classifier's GLYPH-FORM span fires inside B10 on exactly that retained font name.
- Why: T5 translation text; R5 glyph conversion applies to prose, not to the names of fonts.
- Verify: compare the color exhibit, original L139–185 against candidate L23–70; search candidate.txt for CJK strings outside font names and the credit block.
- Disposition: T4/T5 judged jointly in LOCALIZE-ROWS row 212; the only text-adjacent blocking item was item 68 (fonts), closed in section 4.

## 7. Links

- What: three link forms. The source link in the credit block names the original on scp-wiki-cn.wikidot.com (section 0). The usage example names the posting name `:scp-jp:theme:paradigm-inapplicable-jp` (candidate L82, completed by the sweep). The hub link keeps its interwiki-prefix form `[[[wanderers:paradigm-shift-hub | パラダイム・シフト]]]` (candidate L76), as in the original. A full census of `theme:paradigm` references in candidate.txt returns only L11 (the source link, a quotation of the original's address) and L82: no plain-form reference naming a page that will not exist remains.
- Why: P1 posting names for the candidate's own references; the hub is a sibling-wiki page, so its interwiki form is the correct permanent form (P11's sibling class).
- Verify: `grep -n "theme:paradigm" candidate.txt`.
- Disposition: P11 DISPOSITIONED in §(c3) (sibling / batch-posting class).

## 8. Structure

- What: the classifier's EXHIBIT-RESTRUCTURE block (B7) is the relocation pairing of section 3, not a drop: every exhibit in the original (colors, fancyhr, fancyborder, the heading set, the tabview, the table, the footnote specimen) has its counterpart in the candidate, and the original's documentation body appears exactly once per side. The RATE-EXHIBIT-KEPT-CANDIDATE span fires on the original's side only (its L128 Rate, removed under section 1); the candidate keeps no bare Rate. Two structural states are recorded plainly. First, the original's code-display collapsible (original L315) survives empty at candidate L198–200, because the code exhibit moved under its own ソースコード collapsible at candidate L206; it renders as a toggle that opens onto nothing. Second, the exhibit footnote (original L299 → candidate L183) remains live while neither side carries a `[[footnoteblock]]`; that is the original's own state carried over, not a drop. CSS brace balance was checked by depth, not count: the candidate's code block scans to final depth 0 (maximum 3), the same as the original's.
- Why: R3 exhibit restructuring requires the replaced-vs-dropped ground to be stated; here the ground is relocation with a census, and the two residue states are stated rather than smoothed over.
- Verify: exhibit census by the headings and exhibit titles in both files; `grep -c "footnoteblock" original.txt candidate.txt` returns 0 and 0; a brace-depth scan over candidate L208–772.
- Disposition: no exhibit or structure item stands in any register for this theme.

## 9. Formatting only

- What: blocks B11 and B12 are blank-line moves at the code block's tail (one blank deleted at original L770, one added at candidate L775). Whitespace-only blocks: 0. Re-indentation pairings: 0.
- Why: mechanical residue of the relocation; no rule text changes.
- Verify: diff.md sections 5 shows both blocks as blank-only.
- Disposition: none required.

## 10. Porter annotations

- What: one porter annotation rides inside the delivered code block: the FIX5 provenance comment (candidate L209–213, in English, stating that the stacks named Noto Serif JP with no load present and that the face is now loaded), under the block's banner (candidate L208) which states the Dustjacket base loads by @import. No other annotation blocks exist; the classifier's COMMENT-TEXT span is translated CSS comments, counted in section 6.
- Why: annotations inside delivered CSS are candidate content, and this one is the fix's own audit trail; diff.md's header counts review-stage comments as 0 of the +226 added lines, so the port is not credited with review-layer text.
- Verify: read candidate L207–215.
- Disposition: none required.

## 11. Dispositions and exceptions

- What: the standing dispositions, restated with their grounds so they can be re-derived from this package. P4: the jsDelivr-pinned Dustjacket import is original-state CDN delivery (the original imports the identical URL), class (ii). P5: the foreign-host assets are the original's own asset hosts, KB-58. P11: the hub link's interwiki form is the sibling class. Render: the page-overflow figures are the KB-33/KB-34 cross-cutting families and the sample credit-modal item is the KB-32 preview-form property (ledger §(c2)). T1: the baseline findings (hotlink ×5, pseudo-ref ×1) are the standing classes of register (c1). One further state a reviewer might mistake for an oversight: the `:root:lang(cn)` selector scoping of the font variables is byte-preserved from the original (2 occurrences per side). The FIX5 lane recorded the decision to leave it: re-scoping to `:lang(ja)` would be an uncharged redesign, and the class-D fix was the load, not the scope.
- Why: the R-fix standard is that a disposition's ground must be re-derivable from the two sources in the package, not trusted from the ledger.
- Verify: each ground names its deciding bytes in sections 3–7; `grep -c "lang(cn)" original.txt candidate.txt` returns 2 and 2.
- Disposition: as listed; nothing in this section is an open item.

## 12. Verification

- What: T1 baseline (T1-ROWS row 183): exit 1, 6 errors / 1 warn / 1 info (hotlink ×5, pseudo-ref ×1); the FIX5 lane re-ran the checker before and after its edit and the code multisets are identical (6/1/1 → 6/1/1), so the font fix introduced no new finding. T2/T3 (RENDER-ROWS-2, lane RENDER-S2-F (CN11)): FAIL/FAIL with the §(c2) dispositions of section 11. Package-level: `python3 review/build_review.py --check` passes for this package; candidate.txt is byte-identical to the canonical file and original.txt's SHA-256 equals the review/sources.tsv value.
- Why: the checks a reviewer can re-run from this repo alone are the package checks and the greps named in each section; the campaign checkers' outcomes are cited by record, not re-claimed.
- Verify: run the --check command in the repo root; re-run any section's grep.
- Disposition: verdict as stamped (STALE only for the recorded post-verdict sweep line; see the per-theme record).

## Appendix — residue blocks and unanchored mass

- R1 — B3 (orig L5 → cand L14): the head module's closing line pairs against the JP styleFrame iframe. Assigned to sections 3 and 5: the head delivery module is replaced by the credit block and the frame line.
- R2 — B4 (orig L7 → cand L16–17): the original's `====` separator pairs against the empty `[[>]]`/`[[/>]]` pair left when the Rate module was removed. Assigned to section 1.
- R3 — B11 (orig L770 → cand L772) and R4 — B12 (cand L775): blank-line moves at the code tail. Assigned to section 9.
- Unanchored translation mass (TRANS-UNANCHORED spans in B1, B2, B5, B6): the CN → JP body translation, which the anchor matcher cannot pair line by line because the body also moved. Resolved by shape: it is the documentation body of section 6, exhibit for exhibit, with no content class of its own.

## License and attribution

- **Title:** 范式不适用 主题版式
- **Author:** Mercuresphere
- **Source:** https://scp-wiki-cn.wikidot.com/theme:paradigm-inapplicable — revision 132
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
