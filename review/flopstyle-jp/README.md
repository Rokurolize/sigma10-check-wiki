# Review package — theme:flopstyle-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:flopstyle-jp — origin EN, population #11 [GOSIGN2-LEDGER (b) row 11]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 11]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 2 infos (hotlink×2); standing classes dispositioned in register c1 [T1-ROWS row 11; GOSIGN2-LEDGER (b) row 11]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — 768px sidebar×preview-notice overlap (both unreadable), 768px overflow 884px, sample credit-modal; large source-code content-overflow warns. [RENDER-ROWS-1 (RENDER-A row 11)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 11)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 12, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 12]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 11]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:flopstyle-jp.txt sha256:c53b84b67d3c135ecf9b1ed0fd725b89846502b9b2cab5a2ec5b2362dea9a5f1; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 11) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×2 (class (ii), section 11); the render row's items (KB-33/KB-34 overflow family, KB-32 credit modal, KB-37 content-overflow warns, section 11); T4's items closed as P1 DISPOSITIONED (posting-procedure convention), P3 FIXED, P4 DISPOSITIONED (class (ii)), P5 DISPOSITIONED (class (ii) / KB-58) in the ledger §(c3) line |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:flopstyle | theme:flopstyle-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 510 (re-translation reference; first translation was made from rev 21, and the credit block records both: 初訳時参照リビジョン 21 / 改訳時参照リビジョン 510) | — |
| Source of this copy | Fetched at the recorded reference revision (mirror store class FETCH-REGEN, hash-verified against review/sources.tsv) | Canonical file `pages/theme:flopstyle-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 2,529 lines / 59,439 bytes | 525 lines / 13,173 bytes |
| SHA-256 | c2fbc5f644736875dab4cfc62bc9c4116a46f108fcaf1a058a2b5421565ff480 | c53b84b67d3c135ecf9b1ed0fd725b89846502b9b2cab5a2ec5b2362dea9a5f1 |

Wave history: the candidate's recent history is the campaign's own: 2ca24fb (drop the empty documentation tab set), 8dcac74 (Phase 17: reference revisions recorded, three drifts incorporated), d2a9dc0 (Phase 22: the 13 pending reference-revision drifts incorporated or decided — this theme's is the credit-only decision of the per-theme record), b816e10 (gosign2 T1 fixes: credit fields and furniture for rows 1–44, colon encoding, foreign-include rewrites), 5c32672 (FIX-CREDIT-C: the translator pair completed), 1869877 (FIX-CREDIT-D: attribution normalization). No FIX5 commit touches this file.

## Summary

This package's diff (+441/−2,445) does not measure a port; it measures a decision not to re-port. Flopstyle already lives on SCP-JP as a production theme (translated by fumeinadebaisu in 2020 from EN rev 21), and the candidate is that production page carried into the Sigma-10 candidate form: it delivers the production CSS (`style0.css` from scp-jp.github.io) unchanged, keeps the production translation's body and CSS lineage, and confines its own changes to the credit block (completed to the eight ruling-3 fields, with both reference revisions and the adaptation line), the removal of the production page's duplicate bare Rate, and the dropping of an empty documentation tab set. The EN original at the re-translation reference revision (rev 510) is a wholesale rewrite of the 2020 theme (structure, CSS variables, and font system all reorganized); the Phase 22 record (`pages/phase17-diff-flopstyle-jp.txt`) judges that a local diff cannot carry it, that a re-port would be a new project, and that this migration therefore changes nothing but the credit. Every large block in the diff is the visible shape of that non-adoption, and section 0 declares the route so the counts are read correctly.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 48 change blocks — 6 specific (12.5%), 34 heuristic (70.8%), 8 residue (16.7%), 0 skipped. The low specific share is itself a finding about this theme: the classifier's signatures describe port edits, and most of this diff is two CSS generations diverging, which no port signature should claim. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 3 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 23 |
| EXHIBIT-RESTRUCTURE | 5 |
| FONT-IMPORT | 1 |
| INFO-DEL | 2 |
| IFTAGS | 2 |
| JPFONT-LOAD | 1 |
| RESTORATION | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 10 |
| TRANSLATION-ANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the 23 CSS-BODY primaries are the candidate's production-lineage CSS exhibit aligning against scattered regions of the rev-510 CSS; they are narrated once, as a class, in section 8 and the per-theme record, not as 23 port edits. The 5 EXHIBIT-RESTRUCTURE blocks are the original's documentation body and closing furniture, which the candidate replaces with the production translation's body form (section 8). The 8 residue blocks resolve in the appendix, all to the same two shapes (unadopted rev-510 CSS regions; small seams). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:flopstyle-jp; original theme:flopstyle on scp-wiki at reference revision 510 (re-translation); candidate `pages/theme:flopstyle-jp.txt`. Provenance route: **adopted from the production JP counterpart (R4, sources.tsv kind K6)** — the candidate is the Sigma-10 form of the live production page theme:flopstyle (recorded in `pages-existing/existing:theme-flopstyle.txt`, 618 lines; difflib similarity of that page to this candidate is 0.878, and the differences are the candidate-form changes narrated in sections 1–3), not a fresh derivation from the EN original at rev 510. The migration deliverable for the production page is `pages/phase17-diff-flopstyle-jp.txt`, whose Phase 22 text states the decision: upstream was wholly rewritten after 2020, a local diff cannot carry it, a re-port would be required, so this time nothing changes but the credit. The frame: the candidate opens with its delivery module and interwiki-style frame (candidate L1–8) and places the tag gate `[[iftags +テーマ]]` at L10; the original's own frame sits at its tail (original L2517–2529).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; without the declaration, this diff misattributes upstream's rewrite to the port and the port's restraint to deletion (the R4 hazard, KB-68 family).
- **Verify:** Read `pages/phase17-diff-flopstyle-jp.txt` (the decision and its one applied diff: the credit fields); compare `pages-existing/existing:theme-flopstyle.txt` against candidate.txt.
- **Disposition:** Standing (the route itself, decided in Phase 22); its consequences are recorded in sections 3, 4, and 8.

### 1. Credit and attribution

- **What:** The original's credit furniture at rev 510 is an `:scp-wiki:info:start`/`end` pair (original L30–36). The production page's credit was a skeleton carrying a duplicate bare `[[module Rate]]` (the T4 row's item (ii)). The candidate installs the preview form at candidate L12–23: `:scp-jp:credit:start-preview`/`end-preview` with the eight ruling-3 fields completed by the credit waves (title Flopstyle CSS（SCP-JP）; 翻訳責任者 fumeinadebaisu; 翻訳年 2020; the adaptation line 翻訳について recording that the candidate builds on fumeinadebaisu's existing translation with modifications; 原題 Flopstyle: LITE; 著作権者 Lt Flops; 作成年 2020; 初訳時参照リビジョン 21; 改訳時参照リビジョン 510; the source link naming scp-wiki.wikidot.com, the original's recorded host). No `[[module Rate]]` remains anywhere in the candidate (grep returns nothing): the duplicate is deleted, and the preview module is the rate-bearing form. No T7 credit-module CSS supplement was added; the theme's credit styling travels in its delivered CSS as before.
- **Why:** P3/T1 with KB-09: the skeleton credit and the duplicate bare Rate are exactly the failure the credit waves exist to close, and the preview module replaces both. Ruling 3 fixes the eight fields; where an existing human translation is adopted, the translator field keeps the human's name and the adaptation is stated in the 翻訳について field, which is what the bytes show (the population-wide attribution normalization at 1869877 did not overwrite this field, because the translation is not the campaign's).
- **Verify:** Read candidate L12–23 against the eight fields; `grep -n 'module Rate' candidate.txt` returns nothing; the applied production diff in `pages/phase17-diff-flopstyle-jp.txt` shows the same field completion from the production side.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** The candidate's live includes are the interwiki-style frame (candidate L5–8) and the credit pair (section 1). Its body exhibits name `:scp-jp:` targets: the usage include exhibit reads `[[include theme:flopstyle-jp]]` with a translator's footnote (candidate L58) explaining that the posted form is `[[include :scp-jp:theme:flopstyle]]`, and the Flops Header exhibit names `:scp-jp:component:flops-header` (candidate L69). The original's closing furniture — `:scp-wiki:component:croqstyle`, `fade-in`, and `toggle-sidebar` includes (original L2517–2519) — is not carried: the production delivery already supplies the site's furniture, and the candidate's frame replaces the original's tail frame (block B48). T4's item (i) (an EN include kept in the usage instructions, with an unresolvable usage line) is the pre-fix state of the usage exhibit; the candidate's exhibit text is the JP form above, and the ledger closes P1 as a posting-procedure convention (below).
- **Why:** P1 (KB-15): includes name the JP counterpart that exists on scp-jp. For an adopted production page, the counterpart set is the production site's own, which is why the original's EN closing components have no candidate counterpart to repoint to. Ruling 4 is not engaged: no component port was owed.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, and the two exhibits, all JP forms.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P1, posting-procedure convention class).

### 3. Delivery and code loading

- **What:** One delivery fact, stated at candidate L1–8: a `[[module CSS]]` importing `https://scp-jp.github.io/files/theme/flopstyle/style0.css`, and the interwiki-style include at priority 1 with `theme=` naming the same file. That is the production theme's own published CSS, byte-unchanged; the candidate adds no local--code delivery of its own (grep returns no local--code line in the candidate), because the adopted page's CSS already lives on the JP distribution host. The candidate's own small module (candidate L25–28: the `.templateInfo` and collapsible-link rules) is the only live CSS the page itself adds. The original's delivery at rev 510 is the opposite shape: its CSS sits in two large `[[code]]` exhibits (original L924–2399) with a tail module importing its own local--code /1 and /2 from scp-wiki.wdfiles.com (original L2520–2524) — none of which the candidate adopts, per the route of section 0. The ledger names this "original-state CDN delivery": the candidate keeps the delivery state the production page already had.
- **Why:** T9 (base delivery from JP distributions): where a JP distribution of the theme exists and is adopted, delivery from it is the correct form, and P4's host repointing has nothing to repoint. The class (ii) disposition records that any change to this delivery is a posting-procedure matter, not a candidate edit.
- **Verify:** Read candidate L1–8; `grep -n 'local--code' candidate.txt` returns nothing.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P4, delivery class (ii): original-state CDN delivery).

### 4. Fonts and assets

- **What:** Inside the candidate's source exhibit, the font loads are two Google Fonts imports (candidate L99–100: Montserrat 700; Noto Sans JP 400;700) — the production lineage's JP form (block B17, JPFONT-LOAD). The rev-510 original loads its fonts from fonts.bunny.net (original L939: Architects Daughter; L952: the full Montserrat range) with long license comment blocks; none of that is adopted, with the rest of the rewrite. The stack that renders is `"Montserrat", "Noto Sans JP", "Arial", sans-serif` (candidate exhibit, header rules). Assets: the theme's warning-header logo exhibit and its live CSS rule keep the EN-host file `https://scp-wiki.wdfiles.com/local--files/scp-style-resource/scp_trans.png` (candidate L89, escaped exhibit; L362, live rule in the exhibit; the original has the same URL at L1764 and L2030) — T4's item (iii), a deployed-CSS hotlink inherited from the original and the production page alike.
- **Why:** P7/T5 covers the JP font load that the production lineage carries; KB-16's gap does not arise because the adopted CSS already loads a JP face. P5/KB-17 would re-host the logo; KB-58 is the deferred-asset disposition the ledger applies, because the file is a shared style resource the production site already hotlinks in its current state.
- **Verify:** `grep -n '@import' candidate.txt` — candidate L2 (the style0 delivery) and L99–100 only; `grep -n 'scp_trans' candidate.txt` — L89 and L362.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P5, class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** No furniture supplement: the candidate sets no `--header-title`/`--header-subtitle`/`--logo-image` override of its own, and its sidebar and topbar behaviour is whatever the adopted production CSS already does on the JP site (it was written for that site). The render record's furniture-shaped items (the 768px sidebar × preview-notice overlap) are recorded in section 11 as cross-cutting preview-chrome shapes, not as candidate furniture defects.
- **Why:** P8/P9 supplements exist to adapt a foreign theme to the JP furniture; an adopted production page needs no adaptation, and adding one would diverge it from the production page it must stay identical to in behaviour.
- **Verify:** `grep -n -- '--header-title\|--logo-image' candidate.txt` returns nothing outside the adopted CSS exhibit's own inherited rules.
- **Disposition:** Standing; no supplement owed.

### 6. Text translation

- **What:** The candidate's body is the production translation's body (fumeinadebaisu, 2020), carried over, not re-translated by the campaign: the usage prose, the feature collapsible, and the customization exhibits (candidate L31–96; blocks B7–B16, the TRANSLATION-ANCHORED and TRANS-UNANCHORED groups and the COMMENT-TEXT seams inside the exhibits). Against the rev-510 original's documentation body (original L596–681 and the tabview exhibits), the candidate's body is a different generation of the same documentation — which is why several of these blocks carry EXHIBIT-RESTRUCTURE as a secondary label. The one campaign-authored text is the translator's footnote at candidate L58 (a `[[footnote]]` 訳注 explaining the posted include form), the P10-sanctioned form for an original-side circumstance. In-CSS text (R1): the exhibit's comments are the production lineage's English comments, kept; nothing in the exhibit was translated by this migration.
- **Why:** P10 sanctions the 訳注 footnote form; the rest of this section is adoption, and the taxonomy's R4 warning applies: crediting the campaign with the production translator's prose (or blaming it for that prose's choices) would misattribute the work in both directions. The credit block's adaptation line (section 1) is the in-file statement of the same fact.
- **Verify:** Compare candidate L31–96 against `pages-existing/existing:theme-flopstyle.txt` (the same prose) rather than against the original; the footnote is candidate L58.
- **Disposition:** Standing (adoption); the footnote is the campaign's only added body text.

### 7. Links

- **What:** The candidate's live outbound link is the credit source link (candidate L22), naming scp-wiki.wikidot.com — the original's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed. Exhibit links inside the customization samples are escaped code text (section 2), not navigation.
- **Why:** P11 under the dead-reference evidence standard: a link that already names the serving original needs no change.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only live hit.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The structural story is section 0's route, and this section exists to keep the diff honest about it. The original at rev 510 is a self-contained theme page: documentation body, two CSS code exhibits totalling about 1,475 lines (original L924–2399), a license-box region, and a tail delivery frame. The candidate is a 525-line adoption layer: delivery frame, credit, a small live module, the production body, and a 426-line CSS source exhibit (candidate L98–523) whose content is the production lineage's CSS (the rev-21 generation, JP-adapted), not the rev-510 CSS. The 23 CSS-BODY blocks are the differ aligning that exhibit against the rev-510 regions it most resembles; block B32 alone spans original L1513–2054 against candidate L206–207, and B26 and B45 are the same shape (appendix). The candidate did not delete those regions in any sense a reviewer should act on: they were never the JP theme's content, and the Phase 22 record says why they were not adopted. The one genuine structural edit to the adopted page is 2ca24fb's: an empty documentation tab set present in the production page was dropped from the candidate, a removal of empty furniture, recorded in the commit and visible against `pages-existing/`.
- **Why:** R3/R4: a restructure, an adoption, and a deletion share a diff shape; the census here (candidate vs production page, 0.878 similar, differences enumerated in sections 1–3) is what distinguishes them, and ledger class I's silent-deletion charge does not survive it.
- **Verify:** The three-way comparison is reproducible from this repo: original.txt (rev 510), `pages-existing/existing:theme-flopstyle.txt` (production), candidate.txt.
- **Disposition:** Standing; no structural deletion charged.

### 9. Formatting only

- **What:** None as a class: the classifier finds no whitespace-only block and no re-indentation pair (0 and 0). The candidate's exhibit preserves the production CSS's own formatting; the original's formatting is a different generation's and is counted in section 8's divergence, not here.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** classification.json (`reindent_blocks: 0`); diff.md shows no whitespace-only section.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, in the P10-sanctioned body form: the `[[footnote]]` 訳注 at candidate L58, explaining that the original referred to the EN-uploaded theme and that the posted include form is `[[include :scp-jp:theme:flopstyle]]`. No comment-form annotations (`[!-- --]`, CSS banner notes) and no editor lines were added by the campaign; the exhibit's banner comment (`Flopstyle CSS Theme [2020 Wikidot Theme] Created by Lt Flops`) is the original lineage's own, carried with the adopted CSS.
- **Why:** R2: porter-added text is part of the change record; the footnote is also load-bearing, because it is the only in-file note that the usage exhibit's include form differs between the candidate page and a posted article page.
- **Verify:** Read candidate L58; `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's hotlink ×2: the deployed-CSS hotlink of section 4 (the scp_trans.png file, in its exhibit and live-rule occurrences), class (ii) — a shared style resource in the production site's current delivery state (KB-58 family); posting procedure, not a candidate edit. (2) The render row's page-overflow items (768px sidebar × preview-notice overlap, 884px overflow at 768): the recorded cross-cutting families, static credit replica fixed width (KB-33) and preview chrome (KB-34), environment/preview layer, not charged to the candidate. (3) The sample's credit-modal errors: KB-32, the preview form has no modal mechanism (ruling 5). (4) The render row's large source-code content-overflow warns: KB-37 specimen shapes — code content wider than the viewport by design. T4's three items are closed in sections 1, 2, and 4 with their ledger outcomes (P3 FIXED; P1 and P4/P5 DISPOSITIONED).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 11's, the render items are RENDER-ROWS-1 (RENDER-A row 11), the localize items are the ledger §(c3) line for this theme.
- **Disposition:** DISPOSITIONED (all four).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 11): exit 1, 2 errors / 1 warn / 2 infos; both errors are hotlink, dispositioned in section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, RENDER-A row 11): FINDINGS, the items of section 11(2–4), all dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 12): FINDINGS jointly, display-affecting findings 1; the ledger §(c3) line records the theme's T4 outcome as P1 DISPOSITIONED, P3 FIXED, P4 DISPOSITIONED, P5 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +441/−2,445 in 48 change blocks / 1 diff section (the Tier 2 grouping folds this diff's sections; the block index in diff.md is the full enumeration).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:flopstyle-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 11; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The Phase 22 decision (why this diff is mostly non-adoption)

The reference-revision machinery first recorded flopstyle at rev 21, the revision the 2020 production translation was made from. When the re-translation reference was set to rev 510, the drift was total: the EN theme had been rewritten end to end (page structure, CSS variable system, font stack — the rev-510 file in this package shows all three). Phase 22's disposition, written into `pages/phase17-diff-flopstyle-jp.txt` in Japanese, is that a local diff is not a viable vehicle for that rewrite, a re-port would be needed, and therefore this migration changes nothing but the credit (「局所差分ではなく再移植が必要なため、今回は変更なし。クレジットのみ更新。」). The applied production diff in that same file is exactly the credit-field completion of section 1. A reviewer who wants to judge the decision itself has all three texts in this repo: the rev-510 original (this package), the production page (`pages-existing/`), and the decision record. What this package adds is the insistence that the decision be read as the theme's migration outcome — not as 2,445 lines of unexplained deletion.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots. All eight residue blocks are one of two shapes, both consequences of the section 0 route.

| Block | Shape | Resolution |
|---|---|---|
| B26 (no signature) | Original L1313–1479 (license-box CSS region) against candidate L160–162 | Rev-510 CSS with no production-lineage counterpart; not adopted (sections 0, 8) |
| B32's neighbours B28, B37, B39 (no signature) | Small unmatched seams inside the CSS exhibit alignment | Alignment seams between the two CSS generations; no content family is present on one side only beyond what sections 4 and 8 enumerate |
| B45 (no signature) | Original L2101–2337 against candidate L511–514 (the reduced-motion banner region) | Rev-510 CSS region; the candidate exhibit carries the production lineage's own reduced-motion block at its tail (candidate L511–520), so the shape is divergence, not absence |
| B6, B12, B18 (no signature) | Small body/exhibit seams (original L593–594, L607–611, L682–687) | Seams of the body adoption: the production body and the rev-510 documentation body diverge at these points; the content is present in production form (section 6) |
| B5, B15, B16, B22, B48 (heuristic, EXHIBIT-RESTRUCTURE) | The original's documentation body, license exhibits, and closing furniture | Replaced by the production translation's body and the candidate's head frame; adjudicated in section 8, not deletions |

## Change set outside the two diffed files

The diff covers two files; the theme's record is three files larger. `pages/phase17-diff-flopstyle-jp.txt` is the migration deliverable for the production page and carries the Phase 22 decision (per-theme record). `pages-existing/existing:theme-flopstyle.txt` is the production counterpart the candidate adopts (section 0). `pages/theme-decoration-sample-flopstyle-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11). The sibling theme flopstyle-dark is a separate row with its own package; nothing in this theme's record depends on it.
