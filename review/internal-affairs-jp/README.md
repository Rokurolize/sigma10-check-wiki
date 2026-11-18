# Review package — theme:internal-affairs-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:internal-affairs-jp — origin EN, population #102 [GOSIGN2-LEDGER (b) row 102]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 102]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 0 warns / 1 info (hotlink×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 92; GOSIGN2-LEDGER (b) row 102]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 328px@320 + sample 884px@768; 768px sidebar overprint of notice; chromium rate-pill wrap-and-clip at ≤768; WebKit CC "S". [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 102, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 102]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 102]
- Computed against: canonical commit c2a8bee9d16b617b214f78f99e32d0f4be6a1c94; candidate file pages/theme:internal-affairs-jp.txt sha256:43ef453909d7a378e214ab933c0cac0621042b183d376dbf6159f4c2df78bc58; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 102) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×2 (the EN-storage logo, class (ii) / KB-58, section 4); T4's P9 English masthead (ruling 2, section 5); the render row's cross-cutting items (KB-32/33/34/36, section 11) |
| Wave repairs inside this record | The license box was restored by FIX4-LICENSE (commit c2a8bee, KB-63) after an earlier wave's form had dropped the furniture; the jakstyle delivery repoint is FIX-P4's (commit f1138e4). Both predate the verdict, so the stamp is a plain PASS |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:internal-affairs | theme:internal-affairs-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 5 (first translation; the candidate's credit block records 初訳時参照リビジョン: 5) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-internal-affairs.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:internal-affairs-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 840 lines / 22,628 bytes | 841 lines / 23,629 bytes |
| SHA-256 | 14719f67bb476ee0fbf3a06a5b15ec37f53bfb32cc7ef6f8f62a9c94b52dfc2a | 43ef453909d7a378e214ab933c0cac0621042b183d376dbf6159f4c2df78bc58 |

Wave history: the candidate was created by the Stage 2 EN12 integration (commit 7604057), repointed by FIX-P4 (commit f1138e4, the jakstyle delivery of section 3), and repaired by FIX4-LICENSE (commit c2a8bee: license-box furniture restored in 7 themes, KB-63 — the license box of section 1). No FIX-CREDIT-D or FIX5 commit touches this file.

## Summary

A Black Highlighter derivative of JAKSTYLE, and the batch's most layered delivery: the candidate stacks four interwiki-style layers (the JP Black Highlighter fork's two sheets at priorities 1–2, the production scp-jp JAKSTYLE delivery at priority 3, and its own code at priority 4) where the original stacked the same layers as raw imports from nu-scptheme.github.io and the EN wiki's storage. Measured churn (diff.md, Tier 1 format; the generator's difflib count with autojunk off: +148/−152, 300 changed lines in 72 change blocks, presented as 11 hunks). The semantic core: the head gate rebuilt around the JP BHL theme include, the delivery hosts repointed (section 3), two bare Rates deleted (the head one for the credit block, the license-area one with its wrapper), the license box restored in its JP backend form with its file record translated (FIX4-LICENSE), the exhibits translated (27 anchored + 34 unanchored blocks), and two kept EN items dispositioned: the logo asset (section 4) and the English masthead (section 5).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 72 change blocks — 40 specific (56%), 31 heuristic (43%), 1 residue (1%), 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 34 |
| TRANSLATION-ANCHORED | 27 |
| EXHIBIT-RESTRUCTURE | 8 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 3 |
| BARE-RATE-DEL | 2 |
| DELIVERY-HOST | 2 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudications applied for this README: the eight EXHIBIT-RESTRUCTURE blocks are the head-frame rebuild, the frame's include lines, and the license block — the exhibit census (section 8) shows no exhibit restructured; the one T7-CREDIT-CSS span is the theme's general link rule, not credit CSS (section 1); the residue block is a one-word exhibit translation (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:internal-affairs-jp; original theme:internal-affairs on scp-wiki at reference revision 5; candidate `pages/theme:internal-affairs-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart). The frame differs in kind from the batch's other themes: the original gates its whole page with `[[iftags +theme]]` at L1, and its head furniture (a hidden logo image and the import module) sits inside that gate. The candidate splits the frame: a bare `[[iftags]]` gate at L1–3 wraps only the JP Black Highlighter theme include, the import module and the first three interwiki layers follow ungated (candidate L5–24), and the body gate `[[iftags +テーマ]]` opens at candidate L26 ahead of the credit block. The bare head gate is the BHL family's standing form in this candidate set (21 canonical candidates open with it); it is recorded here because a reader comparing first lines will trip on it.
- **Why:** Section 0 declares the provenance route and the frame the later sections assume; the gate tag is P2, and the layered frame is P6 (section 3).
- **Verify:** The sources.tsv row for internal-affairs-jp; `sed -n '1,26p' candidate.txt` against original L1–35.
- **Disposition:** Standing (the route itself); the frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original carries two bare Rates: one at the head (original L38) and one inside the license area's `[[=]]` wrapper (original L830), plus a license box (`license-box-theme | author=badooga`, original L832–837) whose file record names the logo's author (plaguepjp), its license (CC BY-SA 3.0), and its source (SCP-9000). The candidate deletes both Rates (the classifier's two BARE-RATE-DEL blocks, B5 and B70) and installs the JP credit block at the head (`:scp-jp:credit:start-preview`/`end-preview`, candidate L28–37) with the eight ruling-3 fields (title Internal Affairs Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Internal Affairs Theme; 著作権者 badooga; 作成年 2026; 初訳時参照リビジョン 5; 元記事リンク the scp-wiki original, on the recorded host). The author field was checked against the original's credit: the license box's author parameter and the credit prose (the intro paragraph, "the Internal Affairs Theme by badooga") name badooga alone as the theme's author — the field drops nobody; the logo's own author is credited where the original credits him, in the license record and the exhibit caption (candidate L96: "Internal Affairs ロゴ（by PlaguePJP）"). The license box itself stands at the tail in its JP form (`license-box-backend |author=badooga`, candidate L819–827) with the file record translated （ファイル名 / 著作権者 plaguepjp / ライセンス CC BY-SA 3.0 / ソース the SCP-9000 link, now annotated （英語版）) — restored by FIX4-LICENSE (KB-63) after an earlier wave's candidate had lost the furniture; the `[[=]]` wrapper and its Rate did not come back with it, by design. The theme carries no credit-module CSS of its own (no `.creditRate`/`.creditButton` selector exists in the candidate; the classifier's one T7-CREDIT-CSS span, candidate L512–513, is the theme's general link rule whose selector list happens to sit in the T7 window) — credit styling is inherited from the Black Highlighter base.
- **Why:** P3/T1 with KB-09 for the Rates (the preview credit module is the rate-bearing JP form; two bare Rates would duplicate it twice over). Ruling 3 fixes the credit fields. KB-63 records the license-box restoration class: the license furniture is part of the theme's attribution surface and its loss was a defect, repaired before the verdict.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L28–37 and L819–827 against original L830–837.
- **Disposition:** FIXED (the license box, FIX4-LICENSE at c2a8bee, inside the verdict's bytes; the credit swap is the standing P3 form).

### 2. Includes and components

- **What:** The candidate's include list: the JP Black Highlighter theme include inside the head gate (candidate L2, `:scp-jp:theme:black-highlighter-theme` — an include where the original used raw CSS imports for the same base), the four interwiki-style layer includes (section 3), the credit pair (section 1), the license-box pair (section 1), the BHL furniture includes after the body gate closes (`centered-header-bhl`, `toggle-sidebar-bhl`, `betterfootnotes`, candidate L831–833 — the original loads the same furniture through its base), and the exhibit includes repointed to `:scp-jp:` forms (the image-block at candidate L96 among them). No foreign include survives.
- **Why:** P1 (KB-15); the base-as-include form is the JP BHL port's own delivery shape (the base candidate is a theme page, included, not imported). Ruling 4 is not engaged: every component this theme needs already has its JP form.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every target is `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The batch's most layered stack, and the section this theme exists to teach. The original imports three external layers from its head module: Black Highlighter's normalize and minified sheets from `nu-scptheme.github.io` (original L6–7) and JAKSTYLE's own code from the EN wiki's storage (`scp-wiki.wdfiles.com/local--code/theme%3Ajakstyle/1`, original L8), with the interwiki frame naming the jakstyle delivery. The candidate serves the same three layers from JP hosts, as interwiki-style layers at ascending priorities: priority 1, the JP BHL fork's normalize sheet (`scp-jp.github.io/Black-Highlighter/...`, candidate L10–14); priority 2, the fork's minified sheet (candidate L16–19); priority 3, JAKSTYLE's delivery from the production scp-jp storage (`scp-jp.wdfiles.com/local--code/theme%3Ajakstyle/1`, candidate L20–24) — the production page's delivery, not the `theme:jakstyle-jp` candidate's, because this theme's base on scp-jp is the production theme:jakstyle (the dependency the localize row notes: the candidate posts correctly where production JAKSTYLE exists). The head module itself keeps the three imports in JP form alongside (candidate L5–9: the two fork sheets and the production jakstyle /1). The theme's own layer sits at the tail, after the BHL furniture includes: a module importing its own /1 from the draft host (candidate L835–836) with the interwiki frame at priority 4 (candidate L837–841). The usage exhibit's include snippet is repointed to match (candidate L44, with the `:scp-jp:` segment marked in the exhibit's own coloring).
- **Why:** P4/T9 (delivery served from JP hosts — the fork's GitHub Pages and the production wiki's storage are the JP hosts for these layers) and P6/T3 (the supplement frame, one layer per priority so the cascade order is explicit). FIX-P4 (f1138e4) made the jakstyle repoint; its target form (production delivery rather than a candidate) follows from the base's status on scp-jp, and the localize row records the dependency rather than hiding it. The draft-host form of the candidate's own lines is KB-41, class (iii).
- **Verify:** `grep -n 'interwiki-style' candidate.txt` — four includes, priorities 1–4; `grep -n 'github.io\|wdfiles' candidate.txt` — the fork and production hosts, no nu-scptheme and no scp-wiki storage in delivery lines.
- **Disposition:** DISPOSITIONED (the own-layer draft-host lines, class (iii)); the jakstyle production dependency is recorded, standing.

### 4. Fonts and assets

- **What:** Fonts: no font supplement and no stack rewrite is recorded for this theme — the classifier finds no JPFONT-LOAD, FONT-IMPORT, or JPFONT-STACK span, and the Black Highlighter base carries the JP font handling for the family (the candidate inherits it through the section 3 layers). Assets: one kept EN asset, in two lines, and they are exactly T1's hotlink×2 — the theme's logo, `scp-wiki.wdfiles.com/local--files/theme%3Ainternal-affairs/Internal%20Affairs%20Logo.png`, named by the `--lgurl` variable (candidate L345, feeding `--logo-image` at L346) and by the image-block exhibit (candidate L96). The original's third use of the file, the hidden `crom-thumbnail` image line at its L2, does not survive the head rebuild (section 0): the logo still reaches the page through the CSS variable, so the hidden preload line has no JP counterpart. The localize row's P5 wording ("EN-storage logo live + served source") matches these bytes: live in the exhibit, served in the variable.
- **Why:** The logo is P5/KB-17 territory dispositioned as class (ii) / KB-58: re-hosting is a posting-procedure step and the file serves from the original's storage today.
- **Verify:** `grep -n 'scp-wiki.wdfiles' candidate.txt` — the two lines above, both the logo.
- **Disposition:** DISPOSITIONED (class (ii) / KB-58, GOSIGN2-LEDGER §(c3): P5 DISPOSITIONED).

### 5. Header, sidebar, and site furniture

- **What:** The masthead stays English, deliberately and on the record: the candidate carries `--header-title: "INTERNAL AFFAIRS"` and `--header-subtitle: "SURVEIL - CONTROL - PERVADE"` verbatim (candidate L343–344, from original L353–354). That is T4's P9 finding for this theme, and its disposition is ruling 2: header and title language is translation taste, out of scope for migration correctness. The sidebar and topbar furniture arrives through the BHL layers and the tail furniture includes (section 2); the candidate adds no furniture rules of its own beyond the original's CSS.
- **Why:** Ruling 2 governs the masthead; P9/T6 is otherwise not engaged.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — the two lines above, identical to the original's.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3): P9 DISPOSITIONED).

### 6. Text translation

- **What:** The exhibit translation mass: 27 anchored blocks (headings, usage prose with anchors intact — the BetterFootnotes paragraph at original L108 → candidate L98 among them, crediting EstrellaYoshte in both) and 34 unanchored blocks (the intro prose with its footnote apparatus, candidate L39: the badooga attribution, the JAKSTYLE derivation, and the author's footnote musing on sub-departments, translated with its `fnnum`/`fncon` spans intact and its three EN-wiki links annotated （英語版） — the link treatment is section 7's), plus the license record's field labels (section 1) and the palette exhibit's color names (the residue block: `subcolor5-name=Black Monochrome` → 黒， appendix). The CSS comments are the base family's own English section markers, carried as porter-facing text.
- **Why:** P10 and KB-18 (reader-visible strings). The unanchored share is the expected shape for prose carrying footnote spans and links, which break the anchor majority; each block was read against the mirror for this README.
- **Verify:** The exhibit pairs are diff.md's body sections in order; read candidate L39–110 against original L100–120.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The intro prose's three EN-wiki links are kept and annotated, not repointed: SCP-9000, the Fire Suppression Department hub, and the internal-affairs hub are EN articles with no JP counterpart in this set, and the candidate marks each （英語版） so a JP reader knows where the link leads (candidate L39). The license record's source link takes the same annotated form (candidate L824). The derivation link `[[[theme:jakstyle|JAKSTYLE]]]` (candidate L39) names the production base page — the same production dependency as section 3's delivery, in prose form, and correct as written: on scp-jp that page exists. The credit source link names the recorded host (scp-wiki.wikidot.com, candidate L36).
- **Why:** P11: prose links take the JP counterpart or the serving original; where the original is the only form, the campaign's form is the annotated keep, and the annotation is the difference between a kept link and a silent one.
- **Verify:** `grep -n 'scp-wiki.wikidot.com' candidate.txt` — the credit link, the three annotated prose links, and the license source.
- **Disposition:** Standing (annotated keeps; no red link is created by this candidate — theme:jakstyle resolves on scp-jp).

### 8. Structure

- **What:** The structure changes are the frame split (section 0), the license wrapper's removal (section 1), and nothing else. The census decides the eight EXHIBIT-RESTRUCTURE blocks (B1, B2, B3, B6, B8, B11, B20, B71): every one sits in the head frame, the frame's include lines, or the license block — the regions sections 0–3 already account for — and the exhibit sequence itself (usage, palette, element samples, code exhibit) is present on both sides in the same order, nothing dropped or replaced. Variable names and selectors are preserved; `--lgurl` and `--logo-image` keep their names and their relationship (candidate L345–346).
- **Why:** R3's adjudication, decided by the census rather than the label; the label's eight firings are what a head rebuild looks like to a signature that keys on include lines inside gated regions.
- **Verify:** Compare the exhibit sequences (`grep -n '^+\*\|^\[\[div\|^\[\[code' original.txt candidate.txt`).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a class of its own: the classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered. The line-count parity of the two files (840 → 841) is consistent with that reading: this port's churn is content, not padding.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here there is none to disclose.
- **Verify:** The classification's section 9 counts (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked, absent. The candidate carries no `[!-- ... --]` notes and no port provenance comment. The port's provenance lives in the credit block and this package.
- **Why:** R2: porter-added text is part of the change record; here the porter added none in-file.
- **Verify:** `grep -n 'SCP-JP port\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two hotlink errors and one pseudo-ref: the hotlinks are the logo's two lines (section 4), class (ii) / KB-58; the pseudo-ref is the candidate's own draft-host local--code line (section 3), class (ii) posting-procedure. There is no class (i) error. (2) T4's one display-affecting finding is the P5 logo; its second item, the P9 masthead, is dispositioned under ruling 2 (section 5), and its third note is the jakstyle posting dependency (section 3) — a dependency, recorded, not a defect. (3) The render row's items, all cross-cutting, not charged to the candidate: the page-overflow readings (328px@320 on the page, 884px@768 on the sample; KB-33/KB-34), the 768px sidebar-overprint of the notice (KB-34), the chromium rate-pill wrap-and-clip at ≤768 (KB-32/KB-34: the preview rate module's label rendering), and the WebKit CC "S" glyph (KB-36).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries; ruling 2), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 92): exit 1, 3 errors / 0 warns / 1 info; two hotlink (the logo) and one pseudo-ref, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN12)): FINDINGS, the items of section 11(3), all dispositioned; engine coverage full matrix as run by the lane; no credit-modal line is recorded for this theme. (c) T4/T5 (LOCALIZE-ROWS row 102): FINDINGS jointly, display-affecting findings 1 (the P5 logo), the P9 masthead and the jakstyle dependency noted alongside, and no unincorporated upstream updates; the ledger §(c3) line records P5 and P9 as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +148/−152 in 72 change blocks, presented as 11 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:internal-affairs-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 102; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-internal-affairs-jp.txt` is the decoration sample the render checks ran against (its 884px@768 overflow reading is in section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The FIX-P4 commit (f1138e4) touched 39 files and the FIX4-LICENSE commit (c2a8bee) touched 7 license restorations plus its other items; the other files in both waves are those themes' own records, not this one's change set. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## Appendix — residue and low-signal blocks

Class M treatment: the residue collapses into this table rather than per-block slots.

| Block(s) | Shape | Resolution |
|---|---|---|
| B19 (residue) | One line in the palette exhibit: `\| subcolor5-name=Black Monochrome` → `\| subcolor5-name=黒` (original L98 → candidate L88) | A color-name label translated inside the usage exhibit; the classifier left it unlabeled because the line is a table parameter, not prose. It belongs to section 6's mass |

## License and attribution

- **Title:** Internal Affairs Theme
- **Author:** badooga
- **Source:** https://scp-wiki.wikidot.com/theme:internal-affairs — revision 5
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
