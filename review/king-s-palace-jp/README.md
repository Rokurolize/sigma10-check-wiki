# Review package — theme:king-s-palace-jp (KO → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:king-s-palace-jp — origin KO, population #271 [GOSIGN2-LEDGER (b) row 271]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 31f6780c467e1b7f9609b8fcc090291ddae73b8b17d46cbfe5c48278a4d9a5ce); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 3 warns / 2 infos (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 275; GOSIGN2-LEDGER (b) row 271]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 270, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 270]
- FIX5 re-judgement: item 105 (class C) FIXED — FIX5-INFO, commit 9a1c86a: info-module / duplicate credit residue removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 105]
- Computed against: canonical commit f5acc90cbb800f3c0752713589322929dac75821; candidate file pages/theme:king-s-palace-jp.txt sha256:31f6780c467e1b7f9609b8fcc090291ddae73b8b17d46cbfe5c48278a4d9a5ce; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); the stamp reads STALE by design, because the candidate changed after the verdict (the 2a8a125 host repair and two later record-level changes, all itemized in the per-theme record). The frozen ledger remains the verdict for the bytes it judged |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 105 [C] (型 3 double credit: two live credit blocks on one page) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 105: **FIXED** (FIX5-INFO, commit 9a1c86a); re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c3): P3 credit fields FIXED by the credit waves (the FIXED outcome is what item 105 then charged as over-applied), P6 FIXED by the frame waves; ledger §(c2) render row: runtime-hotlink site-theme chain (KB-40, environment layer), sample credit-modal preview form (KB-32), sample 884px@768 overflow (KB-33/KB-34 families); T1 pseudo-ref ×4, the draft-host class (iii) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:king-s-palace | theme:king-s-palace-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 12, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 12 (candidate L22) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-king-s-palace.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:king-s-palace-jp.txt`, copied at worktree HEAD 118306b |
| Lines / bytes | 622 lines / 12,401 bytes (the file's last line carries no trailing newline, so `wc -l` reports 621) | 641 lines / 13,481 bytes |
| SHA-256 | 26f56d08efca117cb889267fc3dc7ed9db0850300c3942eb2e37fe117b1b8965 | ffb47dbdce758da2329eb1f68c4b67ce611458d40eeaedae7a903aa67f93282f |

Wave history: the candidate was created by the Stage 2 KO5 integration (commit 3c781b1); FIX-CREDIT-D (1869877) normalized its translator attribution; FIX4-IWA (8c62b7b) added the interwiki frame whose absence T4 had charged （型 6); FIX5-INFO (9a1c86a) removed the duplicate credit block. Three later commits changed the file again (2a8a125, b5cb724, 722ceb5); they are the reason the stamp reads STALE, and each is itemized in the per-theme record.

## Summary

This is a small, conservative port. The original is a single live CSS module wrapped in a tag gate, preceded by a Rate exhibit, an info-module exhibit, and a short usage body; the candidate keeps that exact architecture, translates the body, swaps the KO info pair for the JP preview credit block, repoints the theme's own asset URLs to the draft host under its JP page name, and appends one small credit-module CSS correction at the end. Measured churn is 80 changed lines (diff.md, the generator's difflib count: +47/−33 in 22 change blocks / 5 hunks) against a 641-line file, and the ~540-line stylesheet body is carried byte-identical except for three asset URLs. The one blocking item was furniture, not CSS: the credit waves had left two live credit blocks on the page, and FIX5 removed the unlabelled duplicate. One minor observation stands open from this package's checks (a style exhibit whose self-link kept the original's slug, section 7); it is flagged, not edited.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 22 change blocks — 15 specific (68.2%), 6 heuristic (27.3%), 1 residue (4.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 3 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| LINK-REPOINT | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 9 |
| TRANSLATION-ANCHORED | 7 |

Labels are sets, so the column sums past 22: B5 alone carries CREDIT-PREVIEW, TASL-FIELDS, INFO-DEL, CREDIT-PROSE, and TRANS-UNANCHORED spans. The sections below are written from the label spans, not from the primary labels.

## Standing sections

### 0. Header and provenance frame

- **What:** The original has no delivery header: it opens with the tag gate `[[iftags +테마]]` (original L1). The candidate opens with the interwiki-style frame (candidate L1–3, `priority=1`, no further parameters) and then the localized gate (candidate L5). Provenance route: derived from the original at the reference revision (scpko, revision 12; mirror class COPY, hash-verified); no production JP counterpart exists for this theme, and the candidate's credit block records the revision it was made from (candidate L22).
- **Why:** P6/T3: the frame supplies the JP environment's interwiki layer the original never needed (T4 charged its absence as 型 6). The frame as first added by FIX4-IWA also carried a `theme=` parameter naming this page's own local--code /1; that address was dead on arrival, because the theme delivers by live module and has no code block (sub-shape (B) of the code-address audit), and the parameter was dropped by the remedy landing 722ceb5, leaving the frame itself intact.
- **Verify:** Read candidate L1–5 against original L1–3; `grep -n 'local--code' candidate.txt` returns nothing on either side.
- **Disposition:** P6 FIXED (ledger §(c3); FIX4-IWA, commit 8c62b7b); the `theme=` parameter's removal is recorded with its citation (722ceb5) in the per-theme record, not re-litigated here.

### 1. Credit and attribution

- **What:** The original's credit furniture is the KO info-module pair (original L13–14, `:scpko:info:start` / `info:end`) under the label "rating module with info module", plus the CSS banner credit (original L63–76: Created by c_bonefish; Base Code by Denevola; Logo by SunnyClockwork; CC BY-SA 3.0). The candidate replaces the info pair, in its position and under the translated label, with one preview credit block (candidate L15–24) carrying the eight standard fields; the block is the specimen form (its title and holder fields carry the 【サンプル】 marker, matching the labelled-exhibit presentation of the furniture pair it sits in). The holder field names c_bonefish, the author the original names in its prose (original L18) and banner (original L67); the banner itself is carried verbatim (candidate L74–87), so the Denevola and SunnyClockwork attributions survive in place. Neither side carries a license-box include; the license statement is the banner's CC BY-SA 3.0 line on both sides. The bare `[[module Rate]]` at candidate L9 stands under its own label (評価モジュール:) and is the labelled exhibit half of the Rate/credit pair, not a second rating widget beside an unlabelled credit block; the duplicate that did stand here is the per-theme record's subject.
- **Why:** P3/T1 (the branch info module does not render in the JP environment; the preview credit module is the rate-bearing JP form), ruling 3 (2026-11-16) for the field set and the translator credit form （翻訳責任者: AI, candidate L17); KB-09's duplicate-Rate rule, with the ledger's paired-exhibit exception for labelled pairs.
- **Verify:** `grep -n 'credit:' candidate.txt` (one include pair, L15/L24); read candidate L15–24 against original L13–14 and L63–76.
- **Disposition:** P3 FIXED (credit waves; ledger §(c3)); the over-application of that fix is ledger item 105, FIXED by FIX5-INFO (per-theme record).

### 2. Includes and components

- **What:** Original includes: the info pair (original L13–14, section 1), `component:image-block` (original L29), and the hidden self-include that sets the default `custom=1` (original L617, `:scpko:theme:king-s-palace`). Candidate includes: the frame (candidate L1), the credit pair (L15/L24), `:scp-jp:component:image-block` (candidate L39), and the self-include repointed to `theme:king-s-palace-jp` (candidate L628, INCLUDE-REPOINT and COMPONENT-SWAP spans of B21). Tag gates are localized at all three sites (B1, B2, B17: gate at candidate L5, the hidden-module gate at candidate L71 matching original L61). The escaped usage example (B8, candidate L30–33) names `:scp-jp:theme:king-s-palace-jp` (its posting name was completed by the usage sweep; per-theme record). No include is duplicated on either side.
- **Why:** P1 (include targets take the JP branch forms), P2/T2 (tag names localize, KB-08), T8 (the self-include is the theme's own page on the JP wiki).
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; no include in the candidate points at a KO-wiki page.

### 3. Delivery and code loading

- **What:** Delivery topology is unchanged: both sides deliver the theme's CSS from a single live `[[module CSS show="true"]]` (original L62, candidate L72). There are no `[[code]]` blocks in either file, in any form, and no `local--code` reference anywhere, so there is no self-delivery address to audit beyond the frame parameter already recorded in section 0. What changes is the asset addressing inside the CSS: the three own-asset URLs move from the original's scpko `local--files` paths to the draft host's `local--files` under the candidate's own page name, colon-encoded (B19: header backgrounds, candidate L90–91; B20: logo, candidate L124), and the exhibit image-block's `name=` makes the same move (candidate L39, the DRAFT-HOST span inside B11). The include-parameter mechanism is carried intact: the hidden self-include still passes `custom=1` as the default (candidate L628–630), so the stylesheet's `var(--color-*-{$custom})` bindings resolve exactly as the original's do.
- **Why:** P4/T9 (own-wiki delivery under the candidate's name; the draft host is the draft-stage form of the JP files host, KB-41). Preserving the `{$custom}` gate matters because the palette is parameterized by it (two color schemes selected by the including page); inlining or dropping the gate would silently fix every consumer to one scheme.
- **Verify:** `grep -n 'local--files' original.txt candidate.txt` (3 original lines, 4 candidate lines including the exhibit); `grep -n 'custom' candidate.txt` for the gate and its bindings.
- **Disposition:** DISPOSITIONED — draft-host form, class (iii) for the candidate's own attachments at draft stage, rewritten to the production host at posting (section 11).

### 4. Fonts and assets

- **What:** none — no `font-family` declaration, `@import`, or `@font-face` exists on either side (grep count 0 on both files); the theme sets sizes and weights only and inherits its stacks, so there is no JP font supplement and no font named but unloaded. The one font name in the record, "Special Elite by Astigmatic" (original L73, candidate L84), sits inside the carried banner comment and credits the typeface of the logo artwork; it is not a webfont on either side. Assets are the four own-host image URLs of section 3; the two Pixabay background-image credits remain banner comments on both sides (original L71–72, candidate L82–83).
- **Why:** P7/T5 apply only where a stack exists to supplement; P5's re-hosting is what section 3 records.
- **Verify:** `grep -c 'font-family' original.txt candidate.txt` (0 / 0).
- **Disposition:** None required; the absence is checked, not assumed (the skeleton's "none" for this section is correct, and this is its ground).

### 5. Header, sidebar, and site furniture

- **What:** none as a change class — no HEADERVAR signature fired and no header, sidebar, or topbar variable is overridden: the theme's `--header-background-1/2` declarations are carried with only their URLs repointed (section 3). The `#interwiki` rule set (candidate L354–397) is the original's own furniture CSS, carried in place; the frame of section 0 is what connects it to the JP environment's interwiki layer.
- **Why:** P8/P9/T6 have no instance here; recording the absence keeps "checked, absent" distinct from "not considered".
- **Verify:** `grep -n 'header-title\|header-subtitle\|logo-image' candidate.txt` returns no variable overrides; the interwiki rules pair one-to-one with the original's.
- **Disposition:** None required.

### 6. Text translation

- **What:** The exhibit body (original L3–58 → candidate L5–68) is translated from Korean to Japanese throughout: the two furniture labels (B3, B4), the homage line (B6, section 7), the authorship sentence (B7: the c_bonefish credit sentence), the usage instructions (B8, B9, including the dark-version `custom=2` note), the section and heading samples (B10, B12: 제목1–6 → 見出し1–6), and the tabview samples (B13: the keyboard-mash placeholder ㅁㄴㅇㄹ → サンプル本文; B14: link-state labels; B15: the footnote text 똑똑 → ノック、ノック). Seven blocks are anchored translations, nine are unanchored; every unanchored block is resolved line by line in the appendix, and all nine are one-to-one translations of their originals. One deletion rides inside B2: the original's `+` title heading (original L3) has no counterpart line; its text survives as the credit block's title field (candidate L16) and in the translated intro sentence (candidate L28), so no content is lost, but a reviewer comparing headings should know the heading line itself was dropped rather than translated. In-CSS text: the banner comment is carried in English verbatim; no Korean CSS comments exist to translate (COMMENT-TEXT did not fire).
- **Why:** P10/KB-18 (reader-visible text localizes); the title-heading deletion is recorded under the exhibit ground of section 8.
- **Verify:** Read candidate L5–68 against original L3–58; the heading samples align one-to-one (candidate L41–46 against original L31–36).
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** One prose link is repointed (B6): the homage line's target, from the original's absolute KO URL `[*http://scpko.wikidot.com/theme:the-foundation-theme|재단 테마]` to the bare JP name `[[[theme:the-foundation-theme|財団テーマ]]]` (candidate L26). Probed for this package (2026-11-17): `theme:the-foundation-theme` exists on scp-jp as the JP production page ("The Foundationテーマ"), so the bare name lands on the JP counterpart, which carries the un-suffixed name as a production page rather than as a campaign candidate; the KO original also still serves. The credit block's source link (candidate L23) names scpko.wikidot.com, the host recorded in sources.tsv for the original — after the repair recorded in the per-theme record; at ledger time it named the branch's dead old host, which is the dead-domain link T4's row 270 charged. One observation stands open: the tabview's link-state exhibit (candidate L55) still points its "visited link" sample at `theme:king-s-palace`, the original's own slug carried over unchanged, where the original was pointing at itself on its own wiki; on scp-jp that name does not exist (the candidate is `theme:king-s-palace-jp`), so the exhibit's visited-state demonstration names a page a JP reader cannot have visited. It is flagged in this package's lane report with this line reference; the candidate is not edited here.
- **Why:** P11 (prose links take the JP counterpart or the serving original, under the dead-reference evidence standard: the homage repoint is grounded in the probe above, not in the name's shape).
- **Verify:** Fetch `https://scp-jp.wikidot.com/theme:the-foundation-theme` (the JP counterpart page) and read candidate L26 and L55 against original L16 and L45.
- **Disposition:** Homage repoint standing; source-link host FIXED by the 2a8a125 repair (per-theme record); the L55 exhibit self-link is an open observation, flagged for the coordinator.

### 8. Structure

- **What:** The localize closing rule is kept: gate, exhibits, tabview, hidden footnoteblock div, the live module, and the hidden self-include block stand in the original's order, and the stylesheet's selectors and variable names are unchanged. Three structural facts a reviewer should have explicitly. (a) The `+` title heading deletion (section 6): an exhibit-line removal, with the text preserved in the credit field and intro. (b) The one append: the credit-module CSS correction module sits after the self-include block at the very end (candidate L635–641, the T7 supplement of the per-theme record), the append-at-end position the closing rule prescribes for JP corrections. (c) B11's EXHIBIT-RESTRUCTURE label is adjudicated as a false fire of the known shape: the image-block exhibit is neither dropped nor replaced — same include, same image file (logo2.png), with its host repointed and its caption translated; the label fired on the include repoint inside the exhibit region. CSS integrity: a brace-depth scan of both files ends at depth 0 with maximum depth 2 and no negative excursion, so no displaced closing brace hides in the carried stylesheet.
- **Why:** The closing rule (structure, variable names, selectors, and channel order preserved; JP corrections appended) is what keeps a follow-up diff applicable; R3 requires the ground for exhibit changes to be stated, which (a) and (c) do.
- **Verify:** Compare the structural maps: `grep -n` for `[[module`, `[[iftags`, `[[include` in both files; the depth scan is a five-line brace counter over either file.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** none — WS-ONLY blocks: 0; re-indentation: 0 blocks pair up after leading-whitespace normalization. The diff contains no formatting-only churn to skip.
- **Why:** Formatting-only change is disclosed as its own class so it is never mistaken for semantic change (negative-ledger rule R7 is not triggered).
- **Verify:** The class summary's counts and diff.md's five hunks.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two porter annotations stand in the candidate, both riding inside other labeled blocks (the skeleton's "none" for this section does not survive an explicit check, which is why they are listed here). (1) The port banner comment at candidate L73 (the classifier's residue block B18): "SCP-JP port of the Korean branch theme "왕의 어전 CSS 테마". Original: https://scpko.wikidot.com/theme:king-s-palace (rev 12)." — added by the porter ahead of the carried original banner, and one of the two lines the 2a8a125 repair later touched (its host). (2) The explanatory comment inside the appended T7 module (candidate L636), which states in English why the credit anchor rule is restated for the JP credit module's DOM.
- **Why:** R2 (porter annotation additions): annotations are part of the change record and are never original content or translation; the first is also the package's in-file provenance pointer.
- **Verify:** Read candidate L73 and L635–641.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section: (1) the four draft-host `local--files` URLs (candidate L39, L90–91, L124) — draft form, class (iii) at draft stage, rewritten to the production host at posting (section 3); (2) the labelled bare Rate beside the specimen credit block — the ledger's paired-exhibit exception, not a KB-09 duplication (section 1 and the per-theme record); (3) the invisible-footnote placement T4 noted （型 3 bundle): the exhibit's `[[footnoteblock]]` sits inside a `display: none` div (original L52–54, candidate L62–64) — that is the original's own placement, carried byte-identical, so no port change arises from it; (4) the render-row dispositions: runtime-hotlink site-theme chain (KB-40, environment layer, not charged to the theme), sample credit-modal preview form (KB-32; ruling 5, 2026-11-16), sample page-overflow 884px@768 (KB-33/KB-34 families). No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** The evidence behind the stamp. (a) T1 baseline (2026-11-16): exit 1, 4 errors / 3 warnings / 2 infos, all four errors pseudo-ref — the draft-host class of section 3 [T1-ROWS row 275; GOSIGN2-LEDGER (b) row 271]. (b) T2/T3 (RENDER-S2-H (KO5)): dispositions only, no open finding [ledger §(c2) row]. (c) T4/T5 (LOCALIZE-S2-F): FINDINGS with the 型 3 bundle and 型 6 charged; every element of that bundle is mapped to its resolution in the per-theme record [LOCALIZE-ROWS row 270]. (d) T4's follow-up half: sources.tsv records no upstream supersession note for this theme and no follow-up diff artifact (contrast kitchen and magazine, section 12 of their packages), so the mirror stays at revision 12, the revision the port was made from. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib, autojunk off): +47/−33, 80 changed lines in 5 hunks. A GNU-diff count of the same pair gives 77 changed lines; the difference is alignment choice, not content.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:king-s-palace-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### Ledger item 105 [C] — the double credit, re-derived

At ledger time the candidate carried two live `credit:start-preview` blocks: a 【サンプル】-titled specimen at old L16 and an unlabelled block with the plain title at old L27, beside the labelled bare Rate at old L10. Ledger item 105 charged the second block: the paired-exhibit exception covers labelled pairs only (the Rate exhibit and its specimen), and two credit furniture sets rendering on one page is a display defect. The supplement re-judged the item FIXED by FIX5-INFO, commit 9a1c86a, and the commit's diff for this file is exactly the claimed change and nothing else: eleven lines deleted (the whole unlabelled block, fields and both includes), no other hunk in the file. The current bytes confirm the end state directly: one credit include pair (candidate L15/L24), the labelled bare Rate standing (candidate L9), and the specimen's fields intact. The fix is present and complete; a reader can check it with the grep in section 1 and the commit diff, without trusting the supplement.

The rest of T4 row 270's 型 3 bundle maps as follows. The bare Rate: excepted by the ledger itself as a labelled exhibit （評価モジュール:), and FIX5's commit message records the same reading ("the labelled Rate/credit pair stays, as the ledger excepts"). The invisible footnote: the original's own placement, carried unchanged (section 11, item 3). The dead-domain link: the credit source link named the KO branch's old host, scp-wiki-ko.wikidot.com, which no longer serves the branch; that is the subject of the repair below. 型 6 (interwiki missing) was closed by the frame addition (section 0).

### Post-verdict changes — why this stamp reads STALE

The verdict was computed against the candidate as FIX5 left it. Three later commits changed the file, so the generator emits a STALE stamp rather than carrying the PASS onto changed bytes; the frozen ledger remains the verdict for the bytes it judged, and the changes are recorded here so the reader can judge them.

1. **Commit 2a8a125 (the host repair).** The candidate's credit source link (candidate L23) and its porter banner comment (candidate L73) named scp-wiki-ko.wikidot.com, the KO branch's dead old host. The repair replaced the host with scpko.wikidot.com in exactly those two lines and nothing else (host replacement only, two occurrences; the same repair touched five KO candidates). Probes at repair time (2026-11-17): all five theme pages, this theme's page among them, returned 404 on the old host and 200 on scpko.wikidot.com. The current bytes confirm both lines now name scpko.wikidot.com, which is also the host sources.tsv records for the original.
2. **Commit b5cb724 (the usage-example sweep).** The escaped usage example's include name was completed from `:scp-jp:theme:king-s-palace` to `:scp-jp:theme:king-s-palace-jp` (candidate L31), the population sweep's single-insertion repair form.
3. **Commit 722ceb5 (the frame remedy).** The frame's `theme=` parameter, which named this page's own local--code /1 although the theme has no code block, was dropped (sub-shape (B)); the frame include itself stands (section 0).

### The T7 credit correction (B22)

The appended module at candidate L635–641 restates one rule. The original styles the credit anchor as `.creditButton p a` (original L519–522), because the KO credit module wraps the anchor in a `<p>`; the JP credit module emits the anchor as a direct child of `.creditButton`, so that selector can never match in the JP environment. The candidate carries the original rule in place (candidate L530–533, where it is inert) and the appended module ships the same two declarations (`border-left: none !important; color: #000 !important`) under the corrected selector `#page-content .rate-box-with-credit-button .creditButton a`, with its reason stated in its own comment (candidate L636; section 10). This is the T7 class in its correction form (R6): the theme's own credit CSS is not supplemented from the basalt selector set, it is repaired at the point where the module DOM changed.


### Post-package repairs (REFRESH3-D)

FIX-FRAMEADDR (`722ceb5`, sub-shape (B)) lands *before* this package's candidate build (`ae7b058`), so the frame at L1 was already remedied; recopy confirms no byte change from it. The earlier repairs this file carries (source-link, info residue, credit fields, usage sweep) also predate the build and are recorded in the package record. The one post-package repair is the exhibit slug below.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Aking-s-palace-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- **FIX-RFIX6 — visited-link exhibit slug** (report `R/review-scout/FIX-RFIX6.md`; landing `f5acc90cbb800f3c0752713589322929dac75821`, 2026-11-17): candidate L54 `[[[theme:king-s-palace|訪問済みリンク]]]` → `[[[theme:king-s-palace-jp|訪問済みリンク]]]`, the -jp posting name. Recopy changed this line only (13,481 → 13,484 bytes).

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

(1) `pages/theme-decoration-sample-king-s-palace-jp.txt` — the decoration sample page the render checks ran against. The port's deliveries are the draft-host attachments named in section 3 (header1.png, header2.png, logo.png, logo2.png under the candidate's own page name); no shared fragment or base page belongs to this theme's change set (the start-themes.tsv row records no dependencies).

## Appendix — heuristic and residue adjudication

The classifier left 6 heuristic blocks and 1 residue block open. All resolve as ordinary classes; none needs a new signature.

- **R1 — B18 (residue; inserted at candidate L73):** the porter banner comment. Assigned to section 10 (porter annotations, R2).
- **R2 — B6 (heuristic; original L16 → candidate L26):** the homage line; translation plus the P11 link repoint. Assigned to sections 6 and 7. The classifier's LINK-REPOINT primary already had it; the heuristic copy in this appendix is the same block.
- **R3 — B7 (heuristic; original L18 → candidate L28):** the authorship sentence; a one-to-one translation whose script delta lacks anchors. Assigned to section 6.
- **R4 — B9 (heuristic; original L24 → candidate L34):** the dark-version instruction sentence; one-to-one translation. Assigned to section 6.
- **R5 — B13 (heuristic; original L42 → candidate L52):** the tabview placeholder text; the original's keyboard-mash filler (ㅁㄴㅇㄹ) is replaced by the standard Japanese sample filler サンプル本文 — a sample-content substitution inside a translation, not a content drop. Assigned to section 6.
- **R6 — B14 (heuristic; original L45 → candidate L55):** the link-state exhibit labels; one-to-one translation. Assigned to section 6; its unchanged link target is the open observation of section 7.
- **R7 — B15 (heuristic; original L47 → candidate L57):** the footnote sample text; the Korean knock-knock filler 똑똑 is rendered ノック、ノック. One-to-one translation. Assigned to section 6.

Multi-label spans the primary-label listing under-reports, for the record: B5 carries the TASL-FIELDS, INFO-DEL, and CREDIT-PROSE spans inside the CREDIT-PREVIEW block (all section 1); B11 carries a DRAFT-HOST span inside the exhibit (section 3); B21 carries an INCLUDE-REPOINT span beside COMPONENT-SWAP (section 2); B1 and B2 split the frame insertion and the tag localization of the opening lines between them (sections 0 and 2).

## License and attribution

- **Title:** 【サンプル】왕의 어전 CSS 테마
- **Author:** 【サンプル】c_bonefish
- **Source:** https://scpko.wikidot.com/theme:king-s-palace — revision 12
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
