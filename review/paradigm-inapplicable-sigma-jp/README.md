# Review package — theme:paradigm-inapplicable-sigma-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:paradigm-inapplicable-sigma-jp — origin CN, population #214 [GOSIGN2-LEDGER (b) row 214]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 93ec66784fb235e9f0f3ceffdf493ae87fe6afe2e16ce149a1afe703baf3b786); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 0 infos (hotlink×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 184; GOSIGN2-LEDGER (b) row 214]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 332px@320 + 387px@375 (page) and 337px@320 + 387px@375 (sample); sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-F (CN11))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN11))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 213, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 213]
- FIX5 re-judgement: item 69 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: pattern-7 fix (paradigm family) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 69]
- Computed against: canonical commit fbbe5acd44acf9c49b9b067e48946270676ae6e2; candidate file pages/theme:paradigm-inapplicable-sigma-jp.txt sha256:93ec66784fb235e9f0f3ceffdf493ae87fe6afe2e16ce149a1afe703baf3b786; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 69 [D] (pattern 7: the JP font is never loaded, and the header stack has no JP fallback at all) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 69: **FIXED** (FIX5-FONTSA, commit 8eacd6e); re-derived from this package's bytes in the per-theme record below |
| Standing items | **DISPOSITIONED** — ledger §(c3): P1 (posting-procedure convention class), P5 (class (ii) / KB-58); ledger §(c2) render row: page-overflow in the KB-33 / KB-34 families, sample credit-modal preview form (KB-32) |
| Flagged in this package | One defect flag: a translated prose link at candidate L80 still names the sibling theme's plain CN page name, which will not exist on SCP-JP (section 7). Also recorded: the review/sources.tsv supersession note is wrong (section 0), the credit block's title field carries the original-language title (section 1), and the original's code-display collapsible survives empty (section 8). The candidate is not edited |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:paradigm-inapplicable-sigma | theme:paradigm-inapplicable-sigma-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 91, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 91 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-paradigm-inapplicable-sigma.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:paradigm-inapplicable-sigma-jp.txt`, copied at worktree HEAD a0a5549 |
| Lines / bytes | 422 lines / 12,984 bytes | 435 lines / 15,453 bytes |
| SHA-256 | 5565f42368235b3ade332b55c7a4d4997042dffa7c89cf5542d1819a1815bc62 | eed8175f935cb9e3b0a98f0e5626162c327ecd255c67ead7998ce77bd7fabb2e |

Wave history: the candidate was created by the Stage 2 CN11 integration (commit b8ee399) **without** its base delivery; REWORK2-P1 (95fd1d1) restored the base include at L1; FIX-CREDIT-D (1869877) normalized the translator attribution; FIX5-FONTSA (8eacd6e) loaded the named JP font and appended it to the header stack (item 69); the usage-example population sweep (b5cb724) completed the usage example's posting name (one line, candidate L84). The sweep line is the post-verdict change the stamp's STALE line records; it does not touch item 69's closure.

One provenance record is wrong and is corrected here, not silently carried: the review/sources.tsv note for this theme claims the original was superseded upstream after the reference revision. The follow-up artifact the note cites (`gosign2-lanes/lane-oc-gs-localize-s2-E/diff-paradigm-inapplicable-sigma-from91.txt`) records rev 91 → rev 91 with no changes. Upstream latest remains revision 91, the revision this mirror freezes.

## Summary

The Sigma-9 variant of the paradigm family: a lightweight rework of theme:paradigm-inapplicable that takes its base from theme:dustframe instead of importing the Dustjacket stylesheet directly. The candidate repoints that base include to the population's own JP candidate (theme:dustframe-jp), restores it where the first integration had dropped it entirely, consolidates the theme's CSS into a single code exhibit delivered through the standard tail frame, swaps the credit furniture for the JP preview credit block, translates the body, and (the FIX5 item) loads the JP serif face and gives the header stack the JP fallback it lacked. Measured churn (diff.md, the generator's difflib count): +212/−199 in 11 change blocks (8 specific, 0 heuristic, 3 residue, all residue resolved in the appendix). The one blocking item is closed and re-derived below. One defect is flagged: a prose cross-link the translation left pointing at the sibling theme's CN page name (section 7).

## Change set

This theme's delivery involves one file beyond the two diffed here: **theme:dustframe-jp**, the base theme included at candidate L1. The relationship is a cross-theme base dependency (the original includes :scp-wiki-cn:theme:dustframe; ruling 1 repoints cross-theme imports to the JP candidate, and ruling 4 ports a needed base together with the theme). theme:dustframe-jp is itself a candidate in this repo's population (`pages/theme:dustframe-jp.txt`), so the dependency resolves inside the campaign's own deliverables; its own review package is a separate record. No other file's content is part of this theme's change set.

## Per-theme record — the FIX5 closure of ledger item 69, re-derived

- **The item.** GOSIGN2-LEDGER.md §(e) item 69 [D]: pattern 7, "JP font never loaded", in the FINDINGS (publication-affecting) set of LOCALIZE-ROWS row 213 (LOCALIZE-S2-E). The ledger's snapshot: "Current file: 0 Google Fonts imports." The FONTSA lane's evidence sharpens it: the title stack named 'Noto Serif JP' with no load behind it, and the header stack named no JP face at all, so JP glyphs on both surfaces fell back to OS defaults.
- **The re-judgement.** GOSIGN2-LEDGER-SUPPLEMENT.md row 69: FIXED, by FIX5-FONTSA, commit 8eacd6e, "pattern-7 fix (paradigm family)".
- **What the fix was supposed to change.** Add the Noto Serif JP load at the head of the theme's own code block and append 'Noto Serif JP' to the header stack, leaving the title stack and every Latin face unchanged (REPORT-GOSIGN2-FIX5-FONTSA.md §10).
- **Re-derivation from this package's bytes.** (1) The load is present: candidate L207, `@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;700&display=swap');`, the file's only Google Fonts import, preceded by the fix's provenance comment (candidate L202–206). (2) The stack half is present: candidate L324 reads `--header-font: "Anonymous Pro", 'zuijinregular', 'Poppins', 'Noto Serif JP', sans-serif;` (the JP face appended after the Latin faces), and candidate L325's title stack names 'Noto Serif JP' where the original's (original L321 region) named 'Noto Serif SC'; no 'Noto Serif SC' remains anywhere in candidate.txt (0 occurrences; the original had 2, both inside that one title-stack value). (3) The fix commit's diff for this file is exactly the comment-plus-import block and that one stack line, matching the lane report. (4) Completeness: the only JP face named in any stack is Noto Serif JP and it is loaded; the imported family is applied by both the header and title stacks, so nothing imported goes unapplied. One inherited oddity is recorded, not charged: the title stack names 'Noto Serif JP' twice, exactly as the original named 'Noto Serif SC' twice in the same value; a duplicated name inside one stack value is harmless and is the original's own form. The closure holds on the current bytes.
- **Post-verdict change.** One line, the usage-example posting name (candidate L84), landed in the population sweep (b5cb724) after the verdict. The generated stamp therefore reads STALE rather than carrying the PASS onto changed bytes; the change is outside item 69's scope and is recorded here so the reader can see exactly what moved.

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:paradigm-inapplicable-sigma-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RFIX7 — the sibling prose link (landing `fbbe5acd44acf9c49b9b067e48946270676ae6e2`, "pages: paradigm-inapplicable-sigma sibling link", 2026-11-17; record `FIX-RFIX7.md`).** +1/−1. L80's prose cross-link target `theme:paradigm-inapplicable` → `theme:paradigm-inapplicable-jp`, the sibling theme's posting name (first package of the R-fix-7 batch); the link label (` Paradigm Inapplicable Black Highlighterテーマ`) and the sentence are byte-unchanged. The self-include at L84 was already completed to `-jp` by the earlier usage sweep (`b5cb724`) and is not part of this repair. Checker 3/2/0 before and after; only the L80 `link-target-missing` warning changes address, now naming the sibling candidate's posting name, which resolves when the batch posts; class (i) 0.

## 0. Header / provenance

- What: the original opens with its base include (original L1, `:scp-wiki-cn:theme:dustframe`), then a head `[[module css]]` (original L3–7) importing its own code fragment from scp-wiki-cn.wdfiles.com. The candidate opens with the repointed base include (candidate L1), then `[[iftags +テーマ]]` (candidate L3); its provenance is carried by the credit block (candidate L5–14), whose 元記事リンク names https://scp-wiki-cn.wikidot.com/theme:paradigm-inapplicable-sigma, the host recorded for the original in review/sources.tsv. No link in the candidate substitutes a different host for the original's.
- Why: the head import module is the original's delivery channel; in the candidate that channel moves to the tail (section 3), and the head carries the base include, the tag gate and the credit furniture (P1/P2 posting conventions).
- Verify: read candidate L1–14 against original L1–11; `sha256sum original.txt` against the review/sources.tsv row.
- Disposition: provenance route is derivation from the original at revision 91 (mirror class COPY); the wrong supersession note in review/sources.tsv is corrected in the Provenance section above.

## 1. Credit and attribution

- What: the original's credit furniture is the CN credit:start/end pair (original L133–139) naming **作者：** [[*user Mercuresphere]] and a header-image credit line. The candidate carries the eight-field preview credit block (candidate L5–14): 著作権者 Mercuresphere (the author the original names; no pointer, no omission), 翻訳責任者 AI under the campaign's TASL ruling, 作成年 2022, 初訳時参照リビジョン 91, and the source link. The author line also stands in the body (candidate L21) and the header-image credit is retained (the same pixabay id-1572988 as the original). The original's bare `[[module Rate]]` (original L130, inside a `[[>]]` container) is absent from the candidate; the container pair survives empty at candidate L18–19. One observation: the block's タイトル field carries the original-language title, identical to its 原題 field. No Japanese title for this theme exists anywhere in the candidate body, so the field contradicts nothing in the file; the state is recorded here because a reviewer will notice it, and it is not flagged.
- Why: P3/T1 credit swap; the JP preview credit module is the rate-bearing form, so the separate Rate module goes (the KB-32 preview-form family). Attribution follows ruling 3 (campaign translations credited 翻訳責任者「AI」 with the TASL record in the block).
- Verify: `grep 著作権者 candidate.txt`; `grep -c "module Rate" candidate.txt` returns 0; compare candidate L5–14 with original L133–139.
- Disposition: T1 credit findings are dispositioned in ledger register (c1); no P3 item stands against this theme in §(c3).

## 2. Includes and components

- What: the base include is repointed and restored (section 3 covers the restoration): original L1 `:scp-wiki-cn:theme:dustframe` → candidate L1 `theme:dustframe-jp`. The tag gate localizes: original `[[iftags +版式]]` (L11) becomes `[[iftags +テーマ]]` (candidate L3, closing at candidate L427). The credit includes swap to `:scp-jp:credit:start-preview` / `:scp-jp:credit:end-preview`. The tail gains the `:scp-jp:component:interwiki-style` include (candidate L432–435, priority=1, theme= the candidate's own fragment 1). Neither side carries any other include; nothing is duplicated.
- Why: ruling 1 (cross-theme imports repoint to the JP candidate of the base) and ruling 4 (a theme's needed base is ported together with it); P2/T2 tag localization (KB-08).
- Verify: `grep -n "\[\[include" original.txt candidate.txt` and compare the two lists.
- Disposition: the include's history is the P1 story of section 3; KB-08 form for the gate.

## 3. Delivery and code loading

- What: two delivery facts define this theme. First, the base: the original includes theme:dustframe from the CN wiki (original L1) and layers its own CSS over it. The CN11 integration dropped that include entirely, leaving the candidate with no base delivery at all (COMPLETION-REPORT.md records this theme among the DROP pairs); REWORK2-P1 (commit 95fd1d1) restored it in the repointed form `[[include theme:dustframe-jp]]` (candidate L1), naming the base's own JP candidate in this repo's population (see the Change set section). Second, the theme's own CSS: the original spreads it over a head import module (L3–7), an inline banner module (L13–121) and a code exhibit (L309–420, 110 content lines). The candidate consolidates it into one `[[code type="css"]]` block (candidate L200–424, 223 content lines) and delivers it through a tail `[[module css]]` (candidate L429–431) importing the candidate's own fragment 1 from the draft host (sigma10-jp-test.wdfiles.com); the interwiki-style include names the same fragment at priority=1. Unlike its two siblings, this theme has no jsDelivr base import on either side: its base arrives through the dustframe include, and the candidate preserves exactly that topology. Self-delivery census: exactly one code block in the candidate, counting every form; both fragment-1 references name it, and it is the stylesheet itself. No entry in FIX-CODEADDR.md or FIX-NAVLA.md names this theme.
- Why: P4 delivery, settled by ruling 1 for the base address and by the REWORK2-P1 restoration for the dropped include. T4's P1 finding (a dustframe-jp dependency that 404'd at localize time, publication-affecting) is answered by the current bytes: the include names a candidate that exists in this population.
- Verify: `grep -n "@import" original.txt candidate.txt`; `ls pages/theme:dustframe-jp.txt` in the repo root; count code blocks in candidate.txt (1).
- Disposition: P1 DISPOSITIONED in ledger §(c3) (posting-procedure convention class); the restoration itself is campaign history (REWORK2-P1), recorded here so the reader does not have to trust the disposition.

## 4. Fonts and assets

- What: the font story is item 69, re-derived in the per-theme record: candidate L207 loads Noto Serif JP from Google Fonts, candidate L324 appends it to the header stack, and candidate L325's title stack names it where the original named 'Noto Serif SC' (original L321). The stacks also retain CN system face names from the original ('HanWang WeiBeiMedium-Gb5', 'kaiti') and the author's 'zuijinregular' face name, which the dustframe base chain defines; those are local or base-defined names, not web loads this file owes. The theme's font-description prose (candidate L184–185) describes the header and title faces generically （日本向けフォールバック / 明朝体） and makes no claim the load contradicts. Assets: the header image credit (pixabay id-1572988) is the foreign-host asset family.
- Why: pattern 7 (a JP face a stack names must be loaded, and a stack rendering JP text must carry a JP fallback; classifier signature JPFONT-LOAD); the asset hosts are the KB-58 class.
- Verify: `grep -o "Noto Serif SC" candidate.txt | wc -l` returns 0; `grep -c "fonts.googleapis" candidate.txt` returns 1; the loaded family is the one both stacks name.
- Disposition: P7 → §(e) item 69, FIXED (supplement row 69); P5 DISPOSITIONED in §(c3) (class (ii) / KB-58).

## 5. Header, sidebar, site furniture

- What: the interwiki style frame. The original embeds it hidden in the body copy: an iframe for scp-wiki-cn.wdfiles.com/local--files/nav%3Aside/styleFrame.html?bhl inside a `display:none` div and an `[[embed]]` (original L125). The candidate carries the JP environment's form as a single bare iframe after the credit block (candidate L16, `//interwiki.scp-jp.org/styleFrame.html?bhl`), and the tail's interwiki-style include (section 2) frames the theme's own fragment for other pages. One iframe per side.
- Why: P6 furniture follows the environment: the frame target is the JP interwiki host, and the bhl variant is the population's standard.
- Verify: `grep -n "styleFrame" original.txt candidate.txt` (one hit each).
- Disposition: not charged by any register; recorded as the standard environment form.

## 6. Text translation

- What: the documentation body is translated CN → JP in place: the color exhibit, the usage prose (including the passage describing this theme as the lightweight variant of the base paradigm theme), the exhibit labels and the collapsible titles. CSS comments are translated in part (classifier COMMENT-TEXT). The anchored translation span the classifier pairs is the `:root` block (B9), whose stack changes are counted in section 4; the unanchored mass is the body translation, resolved by shape in the appendix. Retained Chinese glyph forms are confined to font names ('HanWang WeiBeiMedium-Gb5', 'kaiti'), which are proper nouns, and to the credit title field recorded in section 1.
- Why: T5 translation text; R5 glyph conversion applies to prose, not to the names of fonts.
- Verify: compare the introductory prose, original L190–200 against candidate L76–86; search candidate.txt for CJK strings outside font names and the credit block.
- Disposition: T4/T5 judged jointly in LOCALIZE-ROWS row 213; the only text-adjacent blocking item was item 69 (fonts), closed in section 4. The one translation-adjacent defect in this package is a link target, counted in section 7.

## 7. Links

- What: **Flag — a prose cross-link names a page that will not exist.** Candidate L80: `[[[theme:paradigm-inapplicable| Paradigm Inapplicable Black Highlighterテーマ]]]`, in the translated sentence describing this theme as the lightweight version of the base paradigm theme. The target is the sibling theme's plain CN page name with no site prefix and no -jp completion. On SCP-JP that page will not exist; the sibling port's posting name is theme:paradigm-inapplicable-jp (its review package is the first package of this same batch). The original's identical target (original L196) was a valid same-wiki link on scp-wiki-cn, where theme:paradigm-inapplicable exists; the translation carried the label into Japanese and left the target byte-identical. The population sweep completed this file's own usage-example include to the -jp posting name (candidate L84) but this prose link is outside that sweep's include-form scope, and no register dispositions it. Flagged here with both loci; the candidate is not edited. The remaining links are regular: the source link in the credit block names the original on scp-wiki-cn.wikidot.com (section 0), and the hub link keeps its interwiki-prefix form `[[[wanderers:paradigm-shift-hub | パラダイム・シフト]]]` (candidate L78), as in the original.
- Why: P11's ground is that a reference must name the page that will exist in the target environment; a same-wiki plain name is correct only where the plain page exists. This is the cross-reference form of the defect the sweep repaired in include form across the population.
- Verify: `grep -n "theme:paradigm" candidate.txt` returns L13 (the source link, a quotation of the original's address), L80 (this flag) and L84 (the swept self-include).
- Disposition: none in any register; this package is the first record. The verdict's PASS stands on the registers as written; the flag is a candidate defect for the coordinator's repair queue, of the same one-token shape as the sweep's repairs.

## 8. Structure

- What: the classifier's EXHIBIT-RESTRUCTURE block (B8) is the relocation pairing of section 3, not a drop: every exhibit in the original (colors, fancyhr, fancyborder, the heading set, the tabview, the table, the footnote specimen) has its counterpart in the candidate, and the original's documentation body appears exactly once per side. The RATE-EXHIBIT-KEPT-CANDIDATE span fires on the original's side only (its L130 Rate, removed under section 1); the candidate keeps no bare Rate. Two structural states are recorded plainly. First, the original's code-display collapsible (original L308) survives empty at candidate L191–193, because the code exhibit moved under its own ソースコード collapsible at candidate L199; it renders as a toggle that opens onto nothing. Second, the exhibit footnote (original L292 → candidate L176) remains live while neither side carries a `[[footnoteblock]]`; that is the original's own state carried over, not a drop. CSS brace balance was checked by depth, not count: the candidate's code block scans to final depth 0 (maximum 2), the same as the original's.
- Why: R3 exhibit restructuring requires the replaced-vs-dropped ground to be stated; here the ground is relocation with a census, and the two residue states are stated rather than smoothed over.
- Verify: exhibit census by the headings and exhibit titles in both files; `grep -c "footnoteblock" original.txt candidate.txt` returns 0 and 0; a brace-depth scan over candidate L201–423.
- Disposition: no exhibit or structure item stands in any register for this theme.

## 9. Formatting only

- What: block B10 is a single blank line added at the tail (candidate L426). Whitespace-only blocks beyond it: 0. Re-indentation pairings: 0.
- Why: mechanical residue of the tail delivery module's placement.
- Verify: diff.md section 4 shows the block as blank-only.
- Disposition: none required.

## 10. Porter annotations

- What: one porter annotation rides inside the delivered code block: the FIX5 provenance comment (candidate L202–206, in English, stating that the title stack named Noto Serif JP and the header stack had no JP fallback, and that the face is now loaded and appended), under the block's banner (candidate L201). No other annotation blocks exist; the classifier's COMMENT-TEXT span is translated CSS comments, counted in section 6.
- Why: annotations inside delivered CSS are candidate content, and this one is the fix's own audit trail; diff.md's header counts review-stage comments as 0 of the +212 added lines, so the port is not credited with review-layer text.
- Verify: read candidate L200–208.
- Disposition: none required.

## 11. Dispositions and exceptions

- What: the standing dispositions, restated with their grounds so they can be re-derived from this package. P1: the dustframe dependency was charged as a 404 at localize time and dispositioned as a posting-procedure convention; the current bytes answer it directly (the base's JP candidate exists in the population and the include names it), and section 3 records the REWORK2-P1 restoration that the disposition alone does not show. P5: the foreign-host asset is the original's own header image host, KB-58. Render: the page-overflow figures are the KB-33/KB-34 cross-cutting families and the sample credit-modal item is the KB-32 preview-form property (ledger §(c2)). T1: the baseline findings (hotlink ×2, pseudo-ref ×1, with link-target warnings) are the standing classes of register (c1). This theme's `:root` blocks are unscoped on both sides (no `:lang(cn)` occurs in either file), so the scoping question its siblings raise does not arise here.
- Why: the R-fix standard is that a disposition's ground must be re-derivable from the two sources in the package, not trusted from the ledger.
- Verify: each ground names its deciding bytes in sections 3–7.
- Disposition: as listed; the one open item this package creates is the section 7 flag, which no register yet names.

## 12. Verification

- What: T1 baseline (T1-ROWS row 184): exit 1, 3 errors / 2 warns / 0 infos (hotlink ×2, pseudo-ref ×1); the FIX5 lane re-ran the checker before and after its edit and the code multisets are identical (3/2/0 → 3/2/0), so the font fix introduced no new finding. T2/T3 (RENDER-ROWS-2, lane RENDER-S2-F (CN11)): FAIL/FAIL with the §(c2) dispositions of section 11. Package-level: `python3 review/build_review.py --check` passes for this package; candidate.txt is byte-identical to the canonical file and original.txt's SHA-256 equals the review/sources.tsv value.
- Why: the checks a reviewer can re-run from this repo alone are the package checks and the greps named in each section; the campaign checkers' outcomes are cited by record, not re-claimed.
- Verify: run the --check command in the repo root; re-run any section's grep.
- Disposition: verdict as stamped (STALE only for the recorded post-verdict sweep line; see the per-theme record).

## Appendix — residue blocks and unanchored mass

- R1 — B4 (orig L7 → cand L16): the head import module's closing line pairs against the JP styleFrame iframe. Assigned to sections 3 and 5: the head delivery module is replaced by the credit block and the frame line.
- R2 — B5 (orig L9 → cand L18–19): the original's `====` separator pairs against the empty `[[>]]`/`[[/>]]` pair left when the Rate module was removed. Assigned to section 1.
- R3 — B10 (cand L426): a blank line added at the tail. Assigned to section 9.
- Unanchored translation mass (TRANS-UNANCHORED spans in B2, B3, B7): the CN → JP body translation, which the anchor matcher cannot pair line by line because the body also moved. Resolved by shape: it is the documentation body of section 6, exhibit for exhibit, with no content class of its own.

## License and attribution

- **Title:** 范式不适用 Sigma-9 版式
- **Author:** Mercuresphere
- **Source:** https://scp-wiki-cn.wikidot.com/theme:paradigm-inapplicable-sigma — revision 91
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
