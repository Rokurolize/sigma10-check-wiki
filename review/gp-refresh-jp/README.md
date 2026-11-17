# Review package — theme:gp-refresh-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:gp-refresh-jp — origin CN, population #193 [GOSIGN2-LEDGER (b) row 193]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 28d622e0c5874de6d1e3810c78793a745376c5cef05c57fee145d80f5f224742); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 21 errors / 3 warns / 1 info (pseudo-ref×21); standing classes dispositioned in register c1 [T1-ROWS row 176; GOSIGN2-LEDGER (b) row 193]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 1449px@1366 (page, desktop width) + hidden-login (4 combos) + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN7))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN7))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 5 [LOCALIZE-ROWS row 192, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 192]
- FIX5 re-judgement: item 59 (class H) FIXED — FIX5-TEXTA §1, commit 6f6b349: deleted 199-line usage/specimen block restored translated at L211-411 (heading button, tab view, tables, colour demos, font credits all restored; one original technical mistake, an unclosed :root brace, fixed and recorded). One decorative image-block line was not restored, with recorded grounds (restoring it adds a hotlink error, tested; the line is not among the charged elements; asset hosts are another class) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 59]
- Computed against: canonical commit 9e0c700e350cc97ee0f0c009d6ac8a4f6c44a595; candidate file pages/theme:gp-refresh-jp.txt sha256:28d622e0c5874de6d1e3810c78793a745376c5cef05c57fee145d80f5f224742; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); the stamp above is current, not stale: the candidate file is unchanged since the FIX5 commit it was computed against |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 59 [H] (usage/specimen block deleted wholesale) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 59: **FIXED** (FIX5-TEXTA §1, commit 6f6b349); re-derived from this package's bytes in the per-theme record below — the restoration is present and complete, with one delivery consequence the supplement does not record (flag F2) |
| Standing items | **DISPOSITIONED** — ledger §(c3): P4 (delivery class (ii): original-state CDN delivery), P9 (ruling 2: header/title language out of scope); ledger §(c2) render row: page-overflow, hidden-login, runtime-hotlink site-theme chain, sample T2 no machine verdict |
| Defect flags from this review | **F1** basalt include names a page that will not exist at posting (§2); **F2** the theme's own stylesheet block is referenced by no delivery line (§3); **F3** credit 著作権者 is a pointer, not the named author (§1). None was charged in the ledger; none is edited here |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:gp-refresh | theme:gp-refresh-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 14 | — |
| Source of this copy | Mirror store `review-mirrors/orig-gp-refresh-rev14.txt` (INDEX.tsv, class COPY) | Canonical file `pages/theme:gp-refresh-jp.txt`, copied at worktree HEAD 20bb8c0; the file's last content change is commit 6f6b349 (FIX5-TEXTA) |
| Lines / bytes | 681 lines / 16,607 bytes | 1,838 lines / 48,899 bytes |
| SHA-256 | 6130a77f4c766e60ae89aa2f15bcbab610c97ea3e81bb43e51af2cef45859f35 | fe8fe39956ada3ac3b315b702dd5978fa191e2891a92497c9798347e11c1fb22 |

Provenance route: derived from the original at the reference revision. The sources.tsv row records the layering this package's diff cannot show on its own: the candidate layers over theme:basalt-jp, and the diff covers the theme's own layer plus the inlined base body (§3).

## Summary

The original is a thin page over an external base: its own CSS module (@imports of the CN Basalt code files and its own rules) plus a documentation body whose second half (original L482–680) is a usage/specimen gallery. The candidate is self-contained in form: the CN Basalt base's main body is inlined into the candidate's third code block under a porter comment explaining why (candidate L417–424), the delivered block also @imports theme:basalt-jp/1, and the documentation body is translated. The measured churn (diff.md: 16 change blocks; the bulk is the single DELIVERY-MOVE block B3 carrying the inlined base and stylesheet) is therefore mostly delivery relocation, not independent edits. The one blocking item (the deleted specimen block) was restored translated by FIX5 and is verified element by element below. Three defects no wave charged stand in the current bytes and are flagged, not fixed: the basalt include's target, the delivery numbering, and the credit author pointer.

## Standing sections

### 0. Header and provenance frame

- **What:** Candidate head (L1–9): a `[[module CSS]]` @importing the candidate's own /1 on the draft host, an interwiki-style frame at priority 1 naming the same /1, then `[[iftags +テーマ]]`. The original head has the same frame shape over the CN host, importing the CN Basalt code files and the theme's own code fragment. Classifier topology: module-css → code-css, body similarity 0.95 (one block, B3, carries the relocation).
- **Why:** The supplement frame (head module + interwiki-style) is the campaign's standard delivery frame for page-source themes; draft-host URLs are the draft-form class (iii), rewritten to the production host at posting.
- **Verify:** Read candidate L1–9 against original L1–9; the frame's target correctness is a separate question, settled in §3 (it fails there).
- **Disposition:** DISPOSITIONED (ledger §(c3) P4, delivery class (ii)); the frame's numbering defect is flag F2 (§3), not part of this disposition.

### 1. Credit and attribution

- **What:** Block B1 (CREDIT-PREVIEW, TASL-FIELDS): the candidate's credit block (L11–20) is the preview form (`credit:start-preview` / `credit:end-preview`) with the full TASL field set. Its 著作権者 field (L15) reads `原語版ページの作成者に同じ（scp-wiki-cn の theme:gp-refresh）` — a pointer naming nobody. The original names the author in its prose (original L295: 此版式由[[*user Jonuarl Reden]]基于玄武岩及…创作 — created by Jonuarl Reden, built on Basalt and the Gp Express theme, using some code from theme:shivering-night), and the candidate's own translated prose names him too (candidate L26). The license box at the tail (candidate L1831–1835, block B16) repeats the pointer as its parameter: `|author=scp-wiki-cn theme:gp-refresh の作者`.
- **Why:** A pointer in place of a named author, where the original names the author, is the standing credit defect family (the past-oriented and path-of-jinin pointers are the same shape). The license-box-backend include itself is the population form (89 canonical files use the component); the defect is the pointer text it is fed here, in both places.
- **Verify:** Read candidate L15 and L1831–1832 against original L295 and candidate L26.
- **Disposition:** **Flag F3** — not a ledger item; the ledger's credit charges for this row were not raised (its (c3) row carries no P3 charge), so the pointer stands uncharged. Recorded here and in the batch report with both sides' exact text; the candidate is not edited by this lane.

### 2. Includes and components

- **What:** Block B2 (INCLUDE-REPOINT) is the theme's base include, candidate L22–24: `[[include theme:basalt wide=a|hidetitle={$hidetitle}|centertitle={$centertitle}|acs-itemnum={$acs-itemnum}|disable-acs-anim={$disable-acs-anim}]]` inside the hidden div — the original L2 form with the `:scp-wiki-cn:` prefix dropped and nothing else changed. It names `theme:basalt`, not `theme:basalt-jp`. Probes (2026-11-17): `https://scp-jp.wikidot.com/theme:basalt` returns **404** (no such production page); the check wiki serves a page at that name (200), which is why the include appears to work in the test environment. The candidate's own delivery layer disagrees with the include: the delivered code block @imports `theme:basalt-jp/1` (candidate L427), and the porter comment at L419–424 states the base was integrated precisely because SCP-JP has no CN Basalt. Remaining includes are the credit preview pair (§1), the interwiki-style frame (§0), and the license-box pair (§1), all JP forms.
- **Why:** An include naming a page that will not exist at posting breaks the theme's header furniture the moment it is posted; the file's own comment and its own CSS import establish that the intended base is the JP port. This is the delivery-coherence rule the snippet audit applied across the population.
- **Verify:** Read candidate L22–24 against L419–427; re-run the two probes (production 404, check wiki 200).
- **Disposition:** **Flag F1** — uncharged by any wave; the FIX-CODEADDR audit covered local--code addresses, not include targets, and the usage sweep covered usage-example text, not this functional include. Remedy shape for the fixing lane: repoint the include to `theme:basalt-jp`, parameters unchanged.

### 3. Delivery and code loading

- **What:** The candidate has three code blocks, in document order: block 1 (L211–216, the restored title-customization exhibit, a bare `:root` setting `--header-title`/`--header-subtitle`), block 2 (L220–224, the restored icon exhibit, a bare `:root` setting `--logo`), and block 3 (L416–1828, the stylesheet: porter header, font loads, the basalt-jp/1 import, the inlined CN Basalt base body, and the theme's own rules). Both delivery lines name /1: the head module @import (L2) and the interwiki-style frame (L7). Served-byte probes of the draft host (2026-11-17) decide what /1 is: **/1 serves 100 bytes** (block 1, the exhibit), **/2 serves 36 bytes** (block 2), **/3 serves 36,448 bytes** (block 3, the stylesheet). No line in the file references /3. The theme's own stylesheet is therefore delivered by neither of its delivery lines; what renders on the check wiki is the base pulled in by the §2 include, without this theme's layer.
- **Why:** This is the navla-style shape the brief names: a local--code address must name the block that actually holds the CSS, not a small exhibit while the stylesheet sits unreferenced. The cause is datable: before the FIX5 restoration the stylesheet block was the file's first code block and /1 was correct; FIX5-TEXTA inserted the two exhibit blocks at L211–224 ahead of it (item 59's restoration), renumbering it to /3, and no later wave repointed the two delivery lines. The FIX-CODEADDR audit subsequently classified this theme's /1 references as matching; the served bytes contradict that classification, and the bytes govern.
- **Verify:** Count the code blocks (`grep -n '\[\[code' candidate.txt`: L211, L220, L416) and fetch the three draft-host local--code URLs; compare served sizes (100 / 36 / 36,448 bytes) against the blocks' contents.
- **Disposition:** **Flag F2** — the item 59 restoration itself is complete (§6, per-theme record); this is its unrecorded side effect, not a failure of the restoration's content. Remedy shape: repoint L2 and the L7 frame from /1 to /3 (two lines). Until then the stamp's PASS describes the ledger record, not this file's delivered state.

### 4. Fonts and assets

- **What:** Block B3 (FONT-IMPORT, JPFONT-LOAD): the delivered block's header loads Noto Sans JP and Noto Serif JP (candidate L425–426), Sofia Sans (L428), and Inter/JetBrains Mono further inside the block, matching the restored font credits (candidate L405–411: header and UI in Sofia Sans / Noto Sans JP, body in Inter / Noto Sans JP, mono in JetBrains Mono / Noto Serif JP). The original's font credits named the CN faces （思源黑体/思源宋体）; the port's equivalents are recorded in the restoration's own text. One original line was not restored: original L498, a decorative `component:image-block` include hotlinking a sandbox logo (see the per-theme record for the recorded grounds).
- **Why:** Pattern P7 (font-stack rewrites with JP loads) at patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa; every face named in the delivered stacks is loaded inside the same block, so no named-not-loaded face stands in this file. Sandbox asset hosts are the class (ii) / KB-58 family.
- **Verify:** Read candidate L425–428 and L405–411; `grep -n 'image-block' candidate.txt` returns CSS rules only, no include.
- **Disposition:** DISPOSITIONED (ledger §(c3) P4/P5 family; the unrestored image-block line is dispositioned inside supplement item 59 itself, with tested grounds).

### 5. Header, sidebar, and site furniture

- **What:** HEADERVAR fires in B3 and B12: the theme's header variables are set in the delivered block's `:root` (inside B3), and the two restored exhibits (blocks 1–2, §3) are themselves header-variable specimens (`--header-title`, `--logo`). The credit-button styles of the inlined base stand at candidate L1467–1493 (T7-CREDIT-CSS inside B3: `.creditButton` / `.rate-box-with-credit-button` rules), carried with the base body, not separately edited.
- **Why:** Header/title language choices are ruling 2 territory (ledger §(c3) P9); the furniture rules arrive with the base integration (§3) and are not independent edits.
- **Verify:** `grep -n 'header-title' candidate.txt` and read L1467–1493.
- **Disposition:** DISPOSITIONED (ruling 2, ledger §(c3) P9).

### 6. Text translation

- **What:** The translation mass is the documentation body: the specimen block restored at candidate L211–411 (per-theme record), the usage prose around it, and the tail notes. CONTENT-STRING fires once (B3): the live UI string at candidate L1180, `content: "タグ"` for the page-tags label — FIX5-TEXTA's additional same-class fix (the pre-fix file carried the Chinese 标签）. TRANS-UNANCHORED fires in B1/B3/B14/B15; B14's instance is the scp_memo exhibit region (candidate L198–209), where the classifier's LICENSE-BOX signature also false-fires on the exhibit text — the file's only license box is at the tail (B16).
- **Why:** CSS `content:` strings are reader-visible UI text (KB-18 surface class, patterns @ 9c5e907); untranslated residue there is a class H defect, which is why TEXTA fixed this one inside item 59's lane. Unanchored translation blocks are the expected heuristic mass for a full-body translation and are resolved here by shape: exhibit prose and specimen text, each verified present in both files.
- **Verify:** `grep -n 'content:' candidate.txt` for the UI strings; read the restored block at L211–411 against original L482–680.
- **Disposition:** FIXED where charged (item 59, supplement); the B14 license signature is an adjudicated classifier false-fire, recorded in the appendix.

### 7. Links

- **What:** The usage-example includes were repointed by FIX5-TEXTA as additional same-class fixes and stand in the current bytes: candidate L34 `[[include :scp-jp:theme:gp-refresh-jp]]` (escaped install form), L42 and L44 `theme:gp-refresh-jp`. The 元記事リンク in the credit block (L19) names the CN original by URL, the correct form for the original-article link. The one remaining wrong target is functional, not textual: the §2 basalt include (flag F1).
- **Why:** Copy-paste install instructions naming a page that will never exist are the class H usage-target defect (AGENTS §6 in the campaign record); TEXTA's repoints are that fix, verified present here rather than trusted from its report.
- **Verify:** `grep -n 'gp-refresh' candidate.txt` and check each occurrence's form.
- **Disposition:** FIXED (TEXTA additional fixes, inside supplement item 59's lane record); F1 stands separately (§2).

### 8. Structure

- **What:** EXHIBIT-RESTRUCTURE fires in B12/B13/B15/B16. B12 (with HEADERVAR and IFTAGS) is the tail frame region; B16 is the license box (§1). B13 and B15 are the skeleton's residue entries R1/R2: the aligner matched parts of the restored specimen block against the tail region (B13: orig 488–516 → cand at 1829; B15: orig 521–529 → cand 1834), because the restored exhibits and the tail share boilerplate. Adjudicated against the exhibit census: every charged specimen element is present at candidate L211–411 (per-theme record), so B13/B15 are alignment artifacts of the restoration, not restructurings.
- **Why:** The standing lesson that EXHIBIT-RESTRUCTURE can false-fire on restructured exhibits; adjudication is by census, not by label.
- **Verify:** The element checklist in the per-theme record, checked line by line.
- **Disposition:** No structural defect; the appendix carries the residue adjudication.

### 9. Formatting only

- **What:** None. The classifier produced no whitespace-only or formatting-only block for this pair (16 blocks, none WS-ONLY); every block carries a content signature.
- **Why:** Ground stated as required: the class summary in classification.json lists no formatting-only label for this theme.
- **Verify:** classification.json summary for gp-refresh-jp.
- **Disposition:** Nothing to disposition.

### 10. Porter annotations

- **What:** The delivered block's header comment (candidate L417–424) is the porter's own annotation: it states that the original is based on CN theme:basalt (five code files), that SCP-JP has no CN Basalt, that the base's main body (code file 1) is therefore integrated into this file, and that the darkmode/hidetitle/centertitle/acs modes were not imported. COMMENT-TEXT fires once (B3) on this header and the base's own banner comments. The annotation is accurate about the integration and is also the internal evidence that contradicts the §2 include (flag F1).
- **Why:** Porter annotations are part of the delivered record; where one contradicts the delivered bytes, the contradiction is itself a flag (here it corroborates F1).
- **Verify:** Read candidate L417–428.
- **Disposition:** Recorded; no separate ledger item covers annotations for this row.

### 11. Dispositions and exceptions

- **What:** Standing dispositions for this row: ledger §(c3) P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery) and P9 DISPOSITIONED (ruling 2); ledger §(c2) render row DISPOSITIONED in full (page-overflow 1449px@1366, hidden-login, runtime-hotlink site-theme chain; the sample's T2 produced no machine verdict, exit 2, recorded as a coverage caveat, not a pass). The one unrestored specimen line (original L498) is dispositioned inside supplement item 59 with tested grounds (restoring it adds a hotlink error; the line is not among the charged elements; asset hosts are another class).
- **Why:** These are the campaign's recorded grounds, cited by record name as the standing sections require; none is re-argued here.
- **Verify:** GOSIGN2-LEDGER.md §(c2)/(c3) rows for theme:gp-refresh-jp; GOSIGN2-LEDGER-SUPPLEMENT.md §5, item 59 row.
- **Disposition:** DISPOSITIONED as cited. Flags F1–F3 are outside these dispositions and are not covered by them.

### 12. Verification

- **What:** This package was verified from the repo alone plus the two probe sets quoted above: original.txt SHA-256 equals the sources.tsv value (6130a77f…); candidate.txt is byte-identical to the canonical file at 20bb8c0 (cmp clean, SHA-256 fe8fe399…); `python3 review/build_review.py --check` passes in the worktree. FIX5's own control: checker 20/3/1 before and after the TEXTA edit (REPORT-GOSIGN2-FIX5-TEXTA.md §1), zero new errors; the stamp's T1 baseline (21/3/1) is the ledger-time run, a different execution of the same checker.
- **Why:** The R-fix treatment requires the closure to be checkable from the package's bytes; the probes are the one external element, and each is a single fetch whose result is quoted with its URL.
- **Verify:** Re-run the three commands above; re-fetch the three local--code URLs and the two theme:basalt URLs.
- **Disposition:** Package complete; flags F1–F3 referred to the coordinator for a fix lane.

## Per-theme record — the FIX5 closure re-derived (ledger item 59)

**The charge.** Ledger §(e) item 59 [H]: the original's usage examples and specimens (heading-generation button, tab view, tables, colour demos, font credits, about 190 lines) were deleted wholesale instead of translated, conflicting with the display-test requirement that themes ship their specimens. No wave had restored the section.

**What the fix was supposed to change.** FIX5-TEXTA §1 (commit 6f6b349), re-judged FIXED in supplement §5: restore the deleted block (original L482–680, 199 lines) translated, at candidate L211–411, between the retained heading and the source-code section; fix and record one original technical mistake inside it; leave one decorative line unrestored, with grounds.

**Verification against the bytes.** Each charged element is present in the current candidate: the title-customization code exhibit (L211–216) and icon exhibit (L220–224); the horizontal-rule and heading demos (L227–244, heading specimens levels 1–6 from L229); the five-tab tabview with its footnote and long-tab specimens (L248–307); the table demo (L303–305 region); the eight colour-table specimens (L310–401); the font credits (L405–411, naming the port's JP equivalents for the CN faces). The original technical mistake is exactly where TEXTA recorded it: original L484 opens `:root {` and original L487 closes the code block with no `}` — the restored exhibit closes the brace (candidate L215). TEXTA's two additional same-class fixes are also present: the usage includes name the -jp posting form (L34/L42/L44, §7) and the page-tags UI string reads タグ (L1180, §6). The unrestored line is original L498 (the sandbox-hotlinked image-block include); the candidate carries no image-block include, consistent with the recorded grounds. Checker control 20/3/1 → 20/3/1. **Item 59 is FIXED on the bytes, as the supplement states.**

**The discrepancy the supplement does not record.** The restoration inserted its two code exhibits (L211, L220) ahead of the stylesheet block, which had been the file's first code block; the stylesheet became block 3 while both delivery lines still name /1 (§3, flag F2). The supplement's account of item 59 is accurate about the restored content and silent about the renumbering, and the later FIX-CODEADDR audit classified the /1 references as matching, which the served-byte probes (100 / 36 / 36,448 bytes) contradict. The bytes govern: the closure of item 59 stands, and F2 stands beside it as a separate, uncharged defect introduced by the fixing edit itself.

### The later repairs have landed — F2 (FIX-NAVLA2, fb43564) and F1/F3 (FIX-GP, 9e0c700)

Two repairs postdate this package's build and are now in its candidate bytes; the multi-wave note below ends at 6f6b349, so they are recorded here.

1. **F2 — the stylesheet-address repair.** FIX-NAVLA2 (report `R/review-scout/FIX-NAVLA2.md`, section 2; flagged by FIX-NAVLA.md item 2), landed in canonical commit `fb435643733dfd93d8dfa698861e4a59921d8f0f` ("pages: stylesheet-address repairs in four themes", 2026-11-17). The TEXA restoration of item 59 inserted two small code exhibits ahead of the stylesheet, renumbering it to /3 while both delivery lines still named /1. The repair changed two addresses only: the head module's `@import` (candidate L2) and the frame's `theme=` (candidate L7) now read `local--code/theme%3Agp-refresh-jp/3`. The draft-host probe served /3 at 36,448 B (the GP Refresh stylesheet) against /1's 100 B title sample; the T1 20/3/1 finding set was unchanged apart from the L2 pseudo-ref's block number, class (i) errors 0 before and after. This closes flag F2 from section 11 with the same bytes that item 59's closure rests on.

2. **F1 and F3 — the basalt-include and pointer-credit repairs.** FIX-GP (report `R/review-scout/FIX-GP.md`, items 1–2), landed in canonical commit `9e0c700e350cc97ee0f0c009d6ac8a4f6c44a595` ("pages: gp-refresh basalt include and credit, greyday exhibit link", 2026-11-17). Three lines changed: the base `[[include theme:basalt ...]]` inside the `display: none` div (candidate L23) now names `theme:basalt-jp`, keeping all five pass-through parameters byte-unchanged (the delivered CSS @import cannot carry them, so duplicate-removal did not apply; `theme:basalt` was a production 404); the credit `著作権者` field (candidate L16) changed from the pointer "原語版ページの作成者に同じ（scp-wiki-cn の theme:gp-refresh）" to the author's plain name `Jonuarl Reden`; and the tail `license-box-backend` `author=` parameter (candidate L1832) changed from the same pointer to `|author=Jonuarl Reden]]`. The checker ran 20/3/1 before and after with a byte-identical finding set, class (i) 0 both times.

The brief also names a `3f0aa78`-era state "as applicable". Commit `3f0aa788d3a56dfcfb83c698ec2c7a4a9bb44f44` ("pages: R-fix-20 flags repaired (winddew, words-of-wisdom)") touches only `pages/theme:winddew-in-hand-jp.txt` and `pages/theme:words-of-wisdom-jp.txt`; it contains no gp-refresh hunk, so there is nothing of that era to record for this theme. (The prose link to `theme:basalt` at candidate L48 was probed by FIX-GP and left on the record as a pre-existing warn outside its items; it is unchanged by both repairs.)

This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:gp-refresh-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's runtime change set is larger. (1) `pages/theme:basalt-jp.txt` — the JP Basalt port whose /1 the delivered block imports (candidate L427); the candidate's base layer is meaningless without it. (2) The check-wiki pages this file depends on at render time: `theme:basalt` exists on the check wiki (200) but not on production scp-jp (404) — that asymmetry is flag F1's whole substance. (3) The decoration sample page used by the render lane for this row (RENDER-ROWS-2, RENDER-S2-F (CN7)); its T2 run produced no machine verdict, recorded in the stamp.

## Multi-wave provenance

The candidate's current state is the product of successive waves: the S2 localization wave produced the initial port (translation, delivery frame, and, as later found, the wholesale specimen deletion); the credit waves completed the credit fields (leaving the §1 pointer, which no wave charged); FIX5-TEXTA made the restoration and the two additional same-class fixes (commit 6f6b349, the file's last content change — the usage sweep and snippet audit did not touch this file, and the stamp's computed-against hash equals the current file's). Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2)/(c3) rows and §(e) item 59; GOSIGN2-LEDGER-SUPPLEMENT.md §5 item 59; REPORT-GOSIGN2-FIX5-TEXTA.md §1. The go-sign re-run over that record is what the Status block certifies; flags F1–F3 postdate it.

## Appendix — residue and heuristic adjudication

- **R1 = B13** (EXHIBIT-RESTRUCTURE, heuristic): orig 488–516 → cand at 1829. Alignment artifact: the restored specimen exhibits share boilerplate with the tail frame; the exhibits' true counterparts are at candidate L211–411 (§8). No content is missing at either locus.
- **R2 = B15** (EXHIBIT-RESTRUCTURE + TRANS-UNANCHORED, heuristic): orig 521–529 → cand 1834. Same artifact class as R1.
- **B14's LICENSE-BOX signature** false-fires on the scp_memo exhibit (candidate L198–209); the file's only license box is B16 at the tail. Recorded so a reader does not go looking for a second license box.
- Brace balance: a depth scan of the candidate's delivered block (L416–1828) and of the original's CSS module ends at depth 0 with no negative point; the only brace defect in the pair is the original's unclosed exhibit `:root` (L484–487), fixed by the restoration (§6 record above).
