# Review package — theme:i57-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:i57-theme-jp — origin EN, population #100 [GOSIGN2-LEDGER (b) row 100]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 84273331fde99d48b134b4c8f401eb2ecece9fe823f0cbcd2d2ac1108ed28459); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 0 warns / 1 info (hotlink×7, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 90; GOSIGN2-LEDGER (b) row 100]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — credit-modal title white-on-light-gray (contrast 1.61); chromium/webkit disagree on 翻訳責任者 = possible stale-cache/page-state (noted); theme header wordmark overprints logo + search at ≤375, `.open-menu` overlaps body. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 100, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 100]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 100]
- Computed against: canonical commit 1e34c0b668faf170da8af14c127251af3e35fa26; candidate file pages/theme:i57-theme-jp.txt sha256:84273331fde99d48b134b4c8f401eb2ecece9fe823f0cbcd2d2ac1108ed28459; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/i57-theme-jp/candidate.txt (sha256 d400dac38d6d650a01b7659b7fb2c33c4903c1e7233b1a087e1aca18e3e7dcd5)
Original: theme:i57-theme — scp-wiki, revision 40 (sha256 38e76ac03336a335294e8700378c6c858a8482d52e554947c05d88124692451c)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Check | Verdict |
|---|---|
| Population row | PASS [GOSIGN2-LEDGER (b) row 100] |
| T1 source check | FINDINGS (classified) — 8 errors / 0 warns / 1 info (hotlink ×7, pseudo-ref ×1) [T1-ROWS row 90] |
| T2/T3 render | FINDINGS — credit-modal title white-on-light-gray (contrast 1.61); engines disagree on 翻訳責任者 (possible stale-cache, noted); header wordmark overprints logo + search at ≤375 with .open-menu overlap [RENDER-ROWS-1 (RENDER-S2-B)] |
| T4 localize patterns | FINDINGS — display-affecting 2 (P5 EN-storage imagery; P9 masthead sentences in English) [LOCALIZE-ROWS row 100] |
| Generated stamp | STALE — the candidate changed after the ledger determination (one usage line, in the post-determination sweep); the pre-change verdict lines are preserved in the stamp and the change is recorded under Per-theme record below |

## Provenance

| Item | Value |
|---|---|
| Original page | theme:i57-theme (scp-wiki) |
| Reference revision | 40 — first-translation revision |
| Mirror class | COPY (stored mirror file used as-is) |
| Mirror file | R/review-mirrors/orig-i57-theme-rev40.txt |
| Original SHA-256 | 38e76ac03336a335294e8700378c6c858a8482d52e554947c05d88124692451c |
| Candidate file | pages/theme:i57-theme-jp.txt |
| Candidate SHA-256 (this package) | d400dac38d6d650a01b7659b7fb2c33c4903c1e7233b1a087e1aca18e3e7dcd5 |

Provenance route: standard derivation from the EN branch original at the reference revision (sources.tsv kind `standard`, verdict PASS, notes empty). The candidate entered the canonical repository in the Stage 2 EN12 creation commit 7604057, then received the FIX-CREDIT-D attribution normalization in 1869877 (one line in this file) and one usage-line repair in the post-determination sweep commit b5cb724; the acts are verified under Per-theme record.

## Summary

Dc_Yerko and ROUNDERHOUSE's Facility-57 theme: a single self-delivered CSS exhibit behind a head module and a priority-1 frame, a short documentation body (Use, Examples), and a preload-gimmick asset set (the 1px pig loader images). The port is close to the original in shape and size (697 lines on both sides): the body is translated in place, the exhibit's bunny.net font imports were written against Google Fonts from the start, the masthead stack gained Noto Sans JP, and the EN-storage imagery and the English masthead strings stand exactly where the ledger's dispositions left them. This review flags one silent drop: the original's `[[footnoteblock]]` (orig L149) has no counterpart in the candidate, which demonstrates footnotes in its body but gives them no rendering block. The delivery lines' form deviations (an unterminated @import, a spaced frame parameter) are recorded as observations, matching the same porter signature seen elsewhere in this batch.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COLON-ENC | 5 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| FONT-IMPORT | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 26 |
| TRANSLATION-ANCHORED | 19 |
| WS-ONLY | 34 |

Counts: 94 blocks, 67 specific, 22 heuristic, 5 residue, 0 skipped (comment text). Diff size: +111/−111 lines by both the generator's difflib count and GNU diff (original 697 lines, candidate 697).

Adjudication of the classifier's labels against the bytes, where they diverge: WS-ONLY ×34 is this theme's disclosure mass — the exhibit was whitespace-normalized across many hunks (indentation and blank-line rhythm), which inflates the block count without content change; it is treated in section 9 and not mistaken for edits. Both EXHIBIT-RESTRUCTURE primaries are false-fires on repoints (B2 is the frame include zone, B10 the image-block line) under the standing adjudication rule; the exhibit census is equal (one code block each side, collapsibles and samples corresponding). FONT-IMPORT (the exhibit's import zone) is the bunny→Google host form, but for this theme it is a creation form, not a wave fix (section 4). The footnoteblock's absence carries no label at all — a pure deletion of a one-line module leaves no hunk signature the table names — and is handled as this review's flag in section 8.

## Standing sections

### 0. Header / provenance

**What.** The candidate's head is the original's head shape exactly: a head `[[module css]]` importing the exhibit (cand L1–3), the priority-1 interwiki frame (cand L4–7), then the body gate `[[iftags +テーマ]]` (cand L9) holding the credit block (L11–20) and the documentation body. The original: module (orig L1–3), frame (orig L5–8), gate `[[iftags +theme]]` (orig L11) holding the info module and the bare Rate before the body. Provenance data is the table above.

**Why.** The head is the delivery surface (P4/T9) and the gate is P2/T2 (KB-08; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). No frame include wraps the body on either side; the theme's furniture is its masthead CSS, treated in section 5.

**Verify.** `head -20` both files; `grep -n "iftags" candidate.txt` returns the single gate (L9, closed at L697).

**Disposition.** No header item is charged against this theme in any row.

### 1. Credit and attribution

**What.** The candidate's credit block (cand L11–20, `:scp-jp:credit:start-preview`/`end-preview`) carries all eight TASL fields: タイトル "I57 Theme", 翻訳責任者 "AI", 翻訳年 2026, 原題 "I57 Theme", 著作権者 "Dc_Yerko, ROUNDERHOUSE", 作成年 2019, 初訳時参照リビジョン 40, and 元記事リンク to https://scp-wiki.wikidot.com/theme:i57-theme — the host recorded in sources.tsv for this theme, so no cross-host probe arises. The author field matches the original's exhibit banner (orig L163–165: "Designed by Dc_Yerko with help from Uncle Nicolini / Ported to EN, edited and shinied by ROUNDERHOUSE / Updated in 2023 by Dc_Yerko"); the banner itself is carried in the candidate's exhibit (cand L161–163), so the third name in it (Uncle Nicolini, credited with help) survives in the file even though the field names the two principals, which is the campaign's field convention. The original's bare info module (orig L13–15, `[[include info:start]]` with placeholder text) is removed with the swap (INFO-DEL); its content is placeholder furniture, nothing of substance rides with it.

**Why.** The credit swap is P3/T1 (KB-21, KB-22): the JP preview credit module is the rate-bearing form and the branch-original info module does not render here; the TASL fields trace the port to its source, authors, and reference revision.

**Verify.** Read cand L11–20 against orig L13–15 and L163–165; `grep -n "Designed by" candidate.txt` returns the carried banner at L161.

**Disposition.** No credit item is charged against this theme (the ledger's (c3) line carries P5 and P9 only); population-wide, the ledger's assembly note records credit-missing-fields = 0 after the credit waves. The field set was complete from creation; only the attribution value changed later (1869877).

### 2. Includes and components

**What.** Includes, candidate side: the priority-1 interwiki frame (L4–7), the credit pair (L11, L20), and the one-line image-block include in the body (L32, repointed to `:scp-jp:component:image-block` with its parameters inline). INCLUDE-REPOINT fires ×1 (the frame zone, B2, shared with the exhibit false-fire). The usage exhibit shows the self-include in @@-escape form (cand L26). The original's bare Rate module (orig L17–19) is absent (BARE-RATE-DEL ×1): the preview credit module is already rate-bearing, so the bare module would double-render the widget (KB-09). No include is duplicated.

**Why.** Repoints are P1/T3 (an include naming the EN site resolves there or nowhere here); the Rate removal is KB-09's class, riding the credit swap's definition rather than a separate charge.

**Verify.** `grep -n "\[\[include" candidate.txt` returns L4, L11, L20, L32; `grep -n "module Rate" candidate.txt` returns nothing.

**Disposition.** Uncharged per-theme; the Rate removal is definitional to the P3 swap (section 1).

### 3. Delivery and code loading

**What.** Self-delivery on two lines (DELIVERY-HOST ×2, SELF-DELIVERY ×2, DRAFT-HOST ×2): the head module's @import (cand L2) and the frame's theme= (cand L6), both naming the candidate's own draft-host address local--code/theme%3Ai57-theme-jp/1. The page holds exactly one `[[code]]` block (the exhibit at cand L152), so /1 names the exhibit: the FIX-CODEADDR population audit lists no mismatch for this theme. The original's two delivery lines disagree with each other — its module imports `https://scp-wiki.wikidot.com/theme:i57-theme/code/1` (orig L2) while its frame names `https://scp-wiki.wdfiles.com/local--code/theme:i-57/1` (orig L7), a different page name (theme:i-57) from the theme's own (theme:i57-theme); the candidate normalizes both lines to its own page's exhibit, which is the only self-consistent JP form. Two form deviations ride on the candidate's lines: the @import at L2 lacks the trailing semicolon the original's line carries (orig L2), and the frame parameter at L6 reads `theme= https://…` with a space the original's frame does not have (orig L7; the original does use the spaced form on its image-block line, orig L31).

**Why.** Host repoints are P4/T9: a self-delivery must name the candidate's own page or it serves another page's code. The draft host is the class (iii) draft-form (KB-41). The form deviations have no class; the render record shows the theme styled (its findings are contrast and wordmark items, not an unstyled page), so they are recorded as observations, not breaks — the same porter signature appears on this batch's magpie-swoops tail lines.

**Verify.** `grep -n "local--code" candidate.txt` returns exactly L2 and L6; `grep -c "\[\[code" candidate.txt` returns 1; the FIX-CODEADDR audit (R/review-scout/FIX-CODEADDR.md) is the population cross-check.

**Disposition.** Class (iii) draft-form under T1 disposition class (iii), population-wide (KB-41); no delivery item is charged against this theme individually.

### 4. Fonts and assets

**What.** The exhibit's imports (cand L153–155): Noto Sans JP first (added, JPFONT-LOAD ×1), then Play and Open Sans from fonts.googleapis.com. The original imports Play and Open Sans from fonts.bunny.net (orig L156–157, in the older css v1 parameter form); the candidate's googleapis forms stand from creation (commit 7604057 already contains them — no committed version ever carried the bunny lines), so this is a creation form, not a wave fix, and correspondingly the ledger's (c1) pattern-2 preamble does not name this theme in its fixed list. The theme's single font stack (the masthead stack, cand L243: 'Play', 'Open Sans', "Noto Sans JP", sans-serif) carries the JP face (JPFONT-STACK ×1, B64); it is the exhibit's only font-family line, so the supplement is complete for this theme's design. Assets: seven lines name EN storage (scp-wiki.wikidot.com local--files/theme%3Ai57-theme/…) — the logo image-block (cand L32), the two 1px preload images (L110 pig_loader.gif, L114 pig_loaded.webp), two exhibit backgrounds (L194 opera.webp, L200 SCP-LOGO-RENDER-HD.webp), and the preload pair's CSS rules (L646, L655) — all with the page-name colon %3A-encoded (COLON-ENC ×5 across the file's URL lines).

**Why.** The import host form is the pattern-2 shape (P5, KB-03/KB-04) adopted at creation. The Noto load and stack insertion are P7 (KB-05). The EN-storage assets are P5's charged item: the T1 baseline's hotlink ×7 is exactly these seven lines, counted.

**Verify.** `grep -n "@import" candidate.txt` returns L2 (delivery) and L153–155; `grep -cn "scp-wiki.wikidot.com/local--files" candidate.txt` returns 7; `git show 7604057:pages/theme:i57-theme-jp.txt | grep googleapis` proves the creation form.

**Disposition.** P5 DISPOSITIONED under T1 class (ii) (posting-procedure) / KB-58 [ledger (c3), i57-theme line] — the EN-storage imagery is display-affecting finding (a) of LOCALIZE-ROWS row 100, left for the posting step. The font acts are uncharged (creation form).

### 5. Header, sidebar, site furniture

**What.** The theme has no header variables on either side (grep for --header-title/--header-subtitle returns nothing in both files); its masthead is CSS content strings in the exhibit: `content: "Facility-57"` (cand L241, L248) and the taglines `content: 'Security and Containment For Latinamerica'` (cand L273) and `'Security and Containment For LatAm'` (cand L281), all kept in English, exactly the P9 charge's "masthead sentences". The render row's furniture items are the credit-modal title contrast (1.61, white on light gray) and the header wordmark overprinting the logo and search at ≤375 with the .open-menu overlap.

**Why.** Masthead strings are P9/T6 (KB-57), the theme's visible title surface; ruling 2 takes header and title language choice out of migration-correctness scope, so retention is a disposition, not a defect. The contrast item is the KB-32 preview-form family (the preview credit module's title styling), and the wordmark item the KB-35 responsive family.

**Verify.** `grep -n "content:" candidate.txt` returns the four masthead lines among the justify-content hits; `grep -c "header-title" candidate.txt original.txt` returns 0 and 0.

**Disposition.** P9 DISPOSITIONED (ruling 2: header/title language out of scope) [ledger (c3), i57-theme line]; the render items are DISPOSITIONED in the render register (KB-32, KB-35 families; the engines' disagreement on 翻訳責任者 carries the KB-49 stale-cache caution).

### 6. Text translation

**What.** The documentation body is translated in place: Use (cand L22–28, including the two footnote demonstrations), Examples (L34–…: headings collapsible, tab samples, the prose asides), and the exhibit's translatable strings where the porter chose to translate them; the exhibit's banner and signature comments stay in their original languages (cand L161–163, L690–692 — attribution-bearing text, carried verbatim, which is correct for a credit surface). TRANSLATION-ANCHORED ×19 and TRANS-UNANCHORED ×26 are the body's pairs; the appendix's heuristic entries are their single-line members. One body element is missing rather than translated: the footnoteblock, flagged in section 8.

**Why.** Body translation is P10 (KB-18). Attribution text is the exception that proves the rule: a banner naming the authors is a credit surface (section 1), and translating or "localizing" its names would falsify it.

**Verify.** Spot-read cand L22–50 against orig L21–50; `grep -n "ROUNDERHOUSE. wuz here" candidate.txt` returns the carried signature comment at L690.

**Disposition.** T5 FINDINGS under the joint T4/T5 verdict [LOCALIZE-ROWS row 100]; the translation is the port's purpose and is not an open item.

### 7. Links

**What.** The credit block's source link is treated in section 1 (recorded host, exact). The usage exhibit's self-include reached its -jp form in the post-determination sweep (cand L26; Per-theme record). The body contains no other external links; the asset URLs are section 4's P5 lines, not links.

**Why.** P11 governs link targets; a usage sample naming a nonexistent plain-form page teaches a broken include, which is the sweep's target class.

**Verify.** `grep -n "theme:i57-theme\]" candidate.txt` and the L26 line read directly.

**Disposition.** No link item is charged against this theme.

### 8. Structure

**What.** The structure is the original's, with two exceptions. (i) The gate's contents changed by the credit swap (info module and bare Rate out, credit block in — sections 1–2). (ii) **The original's `[[footnoteblock]]` (orig L149, closing the documentation body before the exhibit) has no counterpart in the candidate** (grep count 0; absent since creation, commit 7604057). The candidate's body demonstrates footnotes twice on one line (cand L28) but provides no block for them to render into on the theme page. Nothing else is dropped: the exhibit census corresponds (one code block, the collapsible set, the tab samples), and CSS brace depth scans clean on both files (final 0, min 0, max 2). The tail blank lines the candidate adds before [[/collapsible]] and [[/iftags]] (cand L694, L696; residue R4/R5) are formatting, section 9.

**Why.** Content presence is a standing check because one-line modules leave no signature in the classifier's table: a deletion this small is exactly what per-theme review exists to catch. The footnoteblock is a functional module (it is where Wikidot renders the footnote list), not furniture, so its absence is a defect of the documentation page, minor in scope — the theme's CSS delivery is unaffected.

**Verify.** `grep -n "footnoteblock" original.txt candidate.txt` returns orig L149 only; `grep -n "footnote\]\]" candidate.txt` returns the L28 demonstrations that need it.

**Disposition.** **Flag (this review): the footnoteblock drop is unrecorded in every ledger row for this theme (the (c3) line carries P5 and P9 only) and dates from creation. Recorded here and in the lane report; the candidate is not edited.** The remedy form is one line: restore `[[footnoteblock]]` at the body's end, the position the original gives it.

### 9. Formatting only

**What.** WS-ONLY ×34 — the batch's largest formatting mass relative to size: the exhibit's hunks are predominantly whitespace normalization (indentation unified, blank lines regularized), which is why a 697-line file pair produces 94 diff blocks while changing far less content than the count suggests. Residue R4/R5 (the candidate's added blank lines at L694 and L696) belong here too.

**Why.** No class: formatting-only hunks change no rendering, and naming their share keeps the diff's block count from being read as churn (KB-18's census discipline). The disclosure matters for this theme precisely because the specific-to-heuristic ratio (67 specific of 94) is otherwise the batch's highest.

**Verify.** classification.json's WS-ONLY spans (34 blocks); a whitespace-insensitive diff (`diff -w`) on the packaged pair collapses to the content changes narrated in sections 1–8.

**Disposition.** None required; not a ledger item.

### 10. Porter annotations

**What.** None. Neither file contains a `[!--` comment (grep count 0 on both sides), and no annotation rides inside any labeled block; the exhibit's comments are the original's own (banner, section heads, signatures), carried as section 6 records.

**Why.** Porter annotations (T12) are the class that would need adjudication here; their absence is stated with its ground so the empty section is a checked fact, not an oversight.

**Verify.** `grep -c "\[!--" candidate.txt original.txt` returns 0 and 0.

**Disposition.** None; no annotation item exists for this theme.

### 11. Dispositions and exceptions

**What.** The theme's disposition set: P5 (the seven EN-storage asset lines) DISPOSITIONED under T1 class (ii) / KB-58 [ledger (c3)]; P9 (the English masthead strings) DISPOSITIONED under ruling 2 [ledger (c3)]; the T1 baseline classes dispositioned in register (c1) (hotlink ×7 = the P5 lines; pseudo-ref ×1 = the @@-exhibit class); the render items DISPOSITIONED in the render register (KB-32 contrast, KB-35 wordmark, KB-49 caution on the engine disagreement); the head draft-host lines are class (iii) draft-form (KB-41). This review's footnoteblock flag is NOT in the disposition set: it is an open finding recorded by this package.

**Why.** Dispositions separate "wrong here" from "wrong at posting" and "decided out of scope"; restating them per theme keeps settled items settled while keeping the genuinely open item visible as open.

**Verify.** The theme's lines in ledger registers (c1), (c2), (c3) under review/AUTHORITIES/ledger-parts/, against sections 3–5 above.

**Disposition.** As stated per item; the population verdict is PASS [GOSIGN2-LEDGER (b) row 100] with FIX5: none.

### 12. Verification

**What.** The stamp's evidence chain: T1 baseline 2026-11-16, exit 1, 8 errors / 0 warns / 1 info [T1-ROWS row 90]; T2/T3 combined FINDINGS [RENDER-ROWS-1 (RENDER-S2-B)] as tabled above; T4 FINDINGS with display-affecting 2 [LOCALIZE-ROWS row 100]; FIX5: none. The generated stamp reads STALE because the candidate changed after the determination (the sweep line, below); its pre-change verdict lines stand as the ledger's judgement of the file.

**Why.** The four test layers are independent instruments (source, render, localize patterns, translation); the package's job is to let a third party re-derive each verdict from the cited record without trusting this README's prose.

**Verify.** Re-run the T1 checker on candidate.txt (8 classified findings expected at baseline classes); read the RENDER-ROWS-1 and LOCALIZE-ROWS rows named above; `python3 review/build_review.py --check` confirms this package's generated files match the canonical candidate.

**Disposition.** Population PASS at the ledger determination; the STALE stamp is a freshness marker, not a re-judgement.

## Per-theme record

Wave narration, each act verified against the diff and the file's git history (canonical repository):

1. **Stage 2 EN12 creation, commit 7604057** — the whole port in one act: credit block with all eight fields (attribution value "SCP-JP" at this point), info module and bare Rate removed, body translated in place, exhibit imports written against Google Fonts (Play, Open Sans) with the Noto Sans JP import and stack insertion already present, delivery lines written against the candidate's own draft-host /1, colon encodings applied, EN-storage assets and English masthead strings carried as the ledger later dispositioned them. The footnoteblock was already absent in this act — the drop is a creation defect, not a wave's. The commit subject ("Stage 2 EN12: theme port candidates") claims exactly this scope; the bytes match it except for the unrecorded footnoteblock loss, which no subject could claim.
2. **FIX-CREDIT-D, commit 1869877** — one line in this file: 翻訳責任者 "SCP-JP" → "AI". For this theme the subject matches the bytes exactly (contrast inkblot in this batch, where the same commit carried seven acts).
3. **Post-determination usage sweep, commit b5cb724** — one line: the usage exhibit's self-include `[[include :scp-jp:theme:i57-theme]]` → `theme:i57-theme-jp` (cand L26). This act postdates the ledger determination and is the whole cause of the stamp's STALE reading: the verdict lines judge the pre-sweep file, and the sweep line is a repair in the campaign's own direction, recorded here rather than treated as a defect.

Defect flag recorded by this review (not edited): the missing `[[footnoteblock]]` (orig L149; candidate: none; absent since creation). The theme page's own footnote demonstrations (cand L28) have no rendering block. Minor in scope, one line in remedy, unrecorded in every row.

Observations recorded without a flag: the head delivery lines' form deviations (unterminated @import at cand L2, spaced theme= parameter at cand L6) match the porter signature on magpie-swoops' tail lines in this batch; the render record shows both themes styled, so the deviations are noted for the coordinator's population-level judgement rather than flagged per theme.

Discrepancies between record and bytes: (i) the ledger's (c3) line charges P5 and P9 and nothing else, yet the file also contains a P7 supplement (Noto import + stack) and the pattern-2 host form, both from creation and both benign — the silence is the record's, not the file's (the same shape as magpie-swoops in this batch). (ii) The (c1) pattern-2 preamble's fixed list does not name this theme although its candidate never carried the bunny lines; read with the creation evidence, the preamble's "otherwise DISPOSITIONED" clause never had a bunny line to attach to here — the T1 hotlink ×7 is fully accounted for by the P5 asset lines. (iii) The classifier's two EXHIBIT-RESTRUCTURE primaries are repoint false-fires, adjudicated in the Class summary.

### Post-package repairs (REFRESH3-G)

- **FIX-U7, landing `1e34c0b668faf170da8af14c127251af3e35fa26`** ("pages: U-7 repairs …", 2026-11-17, R/review-scout/FIX-U7.md item 3): `[[footnoteblock]]` restored at the position corresponding to the original's (orig L149) — refreshed candidate L148, between the "solid" div example's `[[/div]]` and the `----` at L150, +2 lines. The original closes its documentation body with the block, and the candidate's body demonstrates two footnotes on one line (cand L30), so the drop was a creation defect. The "Defect flag recorded by this review (not edited)" paragraph above is the as-built record; the block is now present in the recopied candidate. Checker: error 8 / warn 0 / info 1 before and after, class (i) 0.

The regenerated stamp reads `Overall: STALE` against the pre-repair verdict, by design; no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

None for this package: the theme's port, wave, and sweep act are all inside pages/theme:i57-theme-jp.txt (1869877 and b5cb724 are population commits; their other files belong to other themes' packages).

## Appendix — residue blocks

The five residue blocks resolve by shape; the 22 heuristic entries that follow them in the skeleton are single-hunk translation pairs of the documentation body, each read against the diff — section 6 by shape.

- R1 (B8, orig L21 → cand L26): an alignment artefact — the block pairs the "+ Use" heading with the usage line across the boundary; the heading's own translation stands at cand L22 (「+ 使い方」) and the usage line is the sweep-repaired self-include — sections 6 and 7.
- R2 (B11, orig L33 → cand L34): the "+ Examples" heading translated to 「+ 例」 — section 6, P10.
- R3 (B51, orig L149–150): the footnoteblock deletion — section 8's flag; the residue class exists because a one-line module deletion matches no signature in the table. A signature proposal is carried in the lane report (a FOOTNOTEBLOCK-DEL class for a deleted [[footnoteblock]] whose page demonstrates footnotes).
- R4 (B93) and R5 (B94): the candidate's added blank lines before [[/collapsible]] and [[/iftags]] at the file's tail (cand L694, L696) — section 9.
- R6–R27 (B9, B12, B19, B22, B24, B25 and companions): prose translation pairs of the Use/Examples body (e.g. B19 "I had never seen so many titles together. It was an impressive show." → 「これだけ見出しが並ぶと壮観ですね。」; B22 "How intriguing." → 「興味深いですね。」) — section 6, P10 by shape; no new signature is proposed for any of them.

## License and attribution

- **Title:** I57 Theme
- **Author:** Dc_Yerko, ROUNDERHOUSE
- **Source:** https://scp-wiki.wikidot.com/theme:i57-theme — revision 40
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
