# Review package — theme:galactic-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:galactic-theme-jp — origin EN, population #93 [GOSIGN2-LEDGER (b) row 93]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now bde4ca75c34dd4c166a0f319768db2249d4e83389836e6df110901483f7d42d3); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 7 infos (hotlink×4, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 83; GOSIGN2-LEDGER (b) row 93]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — WebKit CC "S" (cross-cutting), notice clip ≤375, 1366 sidebar-collapsed with theme's own ☰; runtime-hotlink; assets 404 deferred. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 93, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 93]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 93]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:galactic-theme-jp.txt sha256:bde4ca75c34dd4c166a0f319768db2249d4e83389836e6df110901483f7d42d3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 93) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×4 + pseudo-ref ×1 (classes (ii)/(iii), section 11); the render row's items (KB-40 / KB-36 / KB-58, section 11); the T4 items P5 and P9 (section 11). One undocumented one-line deletion (the inert `[[footnoteblock]]`) is recorded in section 8 and flagged for the coordinator |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:galactic-theme | theme:galactic-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 102 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-galactic-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:galactic-theme-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 1,042 lines / 25,520 bytes | 1,058 lines / 26,696 bytes |
| SHA-256 | a94747ad2652af4950471701feb51fcb29471295aadd7bd2ff41a945ad308c2a | 46089c4ac1214d55af01d6a53dd201c3d02443fb502b426db34808a3e42d0293 |

Wave history: the candidate was created by the Stage 2 EN10 integration (commit c210f75, the LOCALIZE-S2-A wave's port) and touched once since, by 1869877 (FIX-CREDIT-D, translator-attribution normalization). No production JP counterpart exists, so the R4 adoption question does not arise.

## Summary

A Galactic Federation BHL port in the wave's standard form: the triple base delivery rebuilt on the JP BHL distribution, the bare Rate replaced by the JP preview credit block, the JP font supplement added and the display face's load moved from a third-party mirror to Google Fonts, the tail own-layer delivery repointed to the draft host at priority 3, and the specimen body translated in full. Two recorded items stand by disposition: the asset references that remain on EN storage, some of which return 404 and are deferred under KB-58, and the English header tagline, which ruling 2 places out of scope. One byte-level deletion has no record behind it — the original's tail `[[footnoteblock]]` — and section 8 adjudicates it inert on this page (the page contains no footnote elements for it to render) while flagging it as undocumented. Measured churn (diff.md, the generator's difflib count with autojunk off: +115/−105, 220 changed lines in 71 change blocks / 4 diff hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 71 change blocks — 37 specific (52.1%), 30 heuristic (42.3%), 4 residue (5.6%), 0 skipped. The heuristic mass is the specimen body's translation and CSS comment mass, resolved by shape in the appendix. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COLON-ENC | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 2 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 5 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 6 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 21 |
| TRANS-UNANCHORED | 31 |
| WS-ONLY | 1 |

Adjudication for this README (every specific block was read against the bytes): the five EXHIBIT-RESTRUCTURE primaries are include repoints (B3, B5, B9, B68, B70) — no exhibit was restructured (section 8). The four residue blocks resolve as the image exhibit's source completion (B18), a heading translation (B24), a blank-line deletion (B66), and the footnoteblock deletion (B67, section 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:galactic-theme-jp; original theme:galactic-theme on scp-wiki at reference revision 102; candidate `pages/theme:galactic-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard). The candidate's head restructures the original's single gate into the wave's two-part form: an unconditional `[[iftags]]` wrapper carrying the JP BHL base include (candidate L1–3, B1), then the localized gate `[[iftags +テーマ]]` (candidate L5) over the body.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate split is the T9 delivery form, and the gate's tag is P2.
- **Verify:** The sources.tsv row for galactic-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare Rate (original L15–17, inside B7) and nothing else — no info pair, no license box. The candidate deletes the bare Rate and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L21–31) carrying the eight ruling-3 fields (タイトル Galactic Federation Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Galactic Federation Theme; 著作権者 Woedenaz; 作成年 2019; 初訳時参照リビジョン 102; the source link to scp-wiki.wikidot.com/theme:galactic-theme). The theme's name stands in English in both title fields, as a proper name; no record charges it. T7 credit-module CSS: none on either side (grep returns 0/0); nothing was added and no correction was needed. No license box is added: the original carried none.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; FIX-CREDIT-D (1869877) is the translator form arriving.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L21–31 against the eight fields.
- **Disposition:** Applied.

### 2. Includes and components

- **What:** Every live foreign include is repointed: the two head frames and the tail frame to `:scp-jp:component:interwiki-style` (B3, B5, B70), the colors exhibit's `:scp-jp:component:theme-squares` (candidate L37–38, B9), the tail furniture pair `:scp-jp:component:toggle-sidebar-bhl` and `:scp-jp:component:centered-header-bhl` (candidate L1048–1049, B68), the credit pair (section 1), and the base include `:scp-jp:theme:black-highlighter-theme` (candidate L2). The usage exhibit's escaped includes follow (candidate L89–90, B23): the BHL line `@@[[include :scp-jp:theme:black-highlighter-theme]]@@` at candidate L89, and the theme's own line at candidate L90. As built the own line read `@@[[include :scp-jp:theme:galactic-theme]]@@`: the repoint changed the branch prefix but kept the plain slug, naming a page that does not exist on scp-jp; the usage-example population sweep has since completed it to `@@[[include :scp-jp:theme:galactic-theme-jp]]@@` (see the per-theme record). No live include in the candidate names a `:scp-wiki:` target.
- **Why:** P1 (KB-15) for the component repoints; T9 for the base include — a dependent theme imports the base's JP port candidate, never the raw upstream delivery. For the usage exhibit's own line, the as-built repoint satisfied the branch half of P1 only; the sweep's completion to the posting name is what brings it under the rule.
- **Verify:** `grep -n '\[\[include' candidate.txt` against the list above.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** Base (T9), the triple form: the original imports BHL from the upstream distribution host nu-scptheme.github.io (module imports and both frame parameters, original L3–13); the candidate repoints all of them to the JP distribution scp-jp.github.io/Black-Highlighter (candidate L8–9 imports, B2; frame parameters at candidate L14 and L19, B4/B6), adds the JP BHL candidate include (candidate L2), and keeps the frames at priority=1 (normalize) and priority=2 (BHL). Own layer (T3): the original's tail module and priority=3 frame name its own code on EN storage (original L1037–1041); the candidate repoints both to its own code on the draft host (candidate L1053–1057, B69/B71). The delivered body is the candidate's own `[[code]]` block (the /1 index), as in the original.
- **Why:** P4/T9 (base delivery from the JP distribution) and P6/T3 (the layered frame stack: 1 normalize / 2 base / 3 own). The draft-host form of the own-layer lines is KB-41, class (iii).
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` against the list above.
- **Disposition:** DISPOSITIONED (draft-host own-layer lines, class (iii)); the base repoint and frame stack are applied.

### 4. Fonts and assets

- **What:** Fonts (P7), at the head of the delivered CSS: the candidate adds the JP supplement load (Google Fonts Noto Sans JP, weights 400;700, candidate L184, B61) and repoints the display face's load — Sirin Stencil was loaded from the third-party mirror fonts.bunny.net (original L172); the candidate loads it from fonts.googleapis.com (candidate L187, B62). Assets: four references stay on EN storage (scp-wiki.wdfiles.com): the logo artwork named by the `--logo-image` variable (candidate L202, its URL colon-encoded by B63, section 5) and by the image exhibit (candidate L73, B18 — where the original's bare filename `galfedlogo.png` with a link parameter is completed to the full EN-storage URL), and the theme's remaining artwork in the CSS body. The render record notes that some of these EN assets return 404; that state is the ledger's KB-58 deferral (section 11), recorded here so the 404s are not mistaken for a port error.
- **Why:** P7/T5 for the supplement; the load repoint is KB-17's shape (a font load moved to its canonical host, family unchanged). P5/KB-58 for the assets: EN-storage hosting is the deferred state — re-upload is barred by owner order, and posting is where the hosting question is settled.
- **Verify:** `grep -n '@import' candidate.txt` — the delivery imports of section 3 plus the two font loads above. `grep -cn 'scp-wiki.wdfiles.com' candidate.txt` — 4.
- **Disposition:** DISPOSITIONED (assets, class (ii) / KB-58; section 11); the font changes are applied.

### 5. Header, sidebar, and site furniture

- **What:** The header variables stand in both files: `--logo-image` (candidate L202; its URL's colon is percent-encoded, `theme%3Agalactic-theme`, where the original's was literal — B63's COLON-ENC, the wave's URL-grammar normalization inside CSS url() values), `--header-title: "GALACTIC FEDERATION"` (candidate L203), and `--header-subtitle: "cleansing the defiled minds"` (candidate L204) — the tagline kept in English, byte-unchanged. The T4 row records the untranslated tagline as its P9 item (display-affecting count 2 for this theme, the assets and the tagline); the ledger dispositions P9 under ruling 2 — header and title language is out of scope for migration correctness — so the string stands by decision, not by oversight. The centered-header and toggle-sidebar components are repointed (section 2); sidebar and topbar rules are otherwise inherited.
- **Why:** P9/T6 is the variable class; ruling 2 is the disposition that governs its language. Recording the decision here is what separates a kept string from an untranslated one (KB-18 does not charge text a ruling has placed out of scope).
- **Verify:** `grep -n -- '--header-\|--logo-image' candidate.txt` — the three lines above.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3) P9 line for this theme).

### 6. Text translation

- **What:** The specimen body is translated in full: the colors section heading (candidate L34), the usage prose and its note (L78–84), the heading specimens （見出し2–6, L104–112), the tab specimens (L118–162, including the six repeated empty-tab labels), the table specimen (L174–176), and the collapsible labels (L101–102, L182). The 31 TRANS-UNANCHORED and 21 TRANSLATION-ANCHORED blocks are this mass, resolved by shape in the appendix. English survives as live text only in the section 5 tagline (dispositioned) and in proper names (the theme's name, Black Highlighter, Sirin Stencil).
- **Why:** P10 and KB-18: reader-visible strings are translated; specimen filler is translated with the same care as instructions because the specimen is what a user copies.
- **Verify:** diff.md's body sections in order; `grep -n 'Second Title\|Tabulator' candidate.txt` returns nothing.
- **Disposition:** Standing (the port itself); the retained tagline is dispositioned in section 5.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L30), naming scp-wiki.wikidot.com/theme:galactic-theme, the original's recorded host in sources.tsv — the serving form, not a defect. The usage note's theme link is repointed with its sentence (candidate L84 names the JP BHL theme page form). The asset URLs are CSS and exhibit references, not prose links (section 4). No prose link in the candidate targets a page that does not serve.
- **Why:** P11 under the dead-reference evidence standard: a link is charged when its target does not serve or a JP counterpart exists; neither holds here.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only prose hit; the remaining hits are the asset lines of section 4.
- **Disposition:** Standing.

### 8. Structure

- **What:** No exhibit restructuring: the classifier's five EXHIBIT-RESTRUCTURE primaries are include repoints in exhibit-adjacent lines (B3, B5, B9, B68, B70); the exhibit census (colors, headings, tabs, table, source code) stands in the original's order on both sides. One genuine deletion stands outside the exhibits, recorded here because no campaign record mentions it: the original's `[[footnoteblock]]` (original L1032, between the source-code collapsible and the gate's close) has no counterpart in the candidate (B67). The adjudication is a census, not a guess: neither file contains a single `[[footnote]]` element (grep returns 0 on both sides), so the block had nothing to render on this page and its removal changes nothing this page displays. It is nonetheless an undocumented deletion — the T1, T4, and render records are all silent on it — and it is flagged in this package's batch report for the coordinator, because a theme page's furniture should not disappear without a record even when the disappearance is inert.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a repoint share a diff shape and ledger class I charges the silent form; here the census decides both questions (no restructure; one inert, undocumented deletion).
- **Verify:** `grep -c '\[\[footnote\]\]' original.txt candidate.txt` — 0 and 0; `grep -n 'footnoteblock' candidate.txt` returns nothing.
- **Disposition:** Standing, flagged as undocumented (this section and the batch report are its record now).

### 9. Formatting only

- **What:** One WS-ONLY block: B66, a blank line deleted at the original's tail (original L1029) — the same block the appendix lists as this package's formatting residue. No re-indentation and no line-ending conversion (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Original L1026–1033 against candidate L1042–1047 in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. This candidate carries no `Ported for SCP-JP` banner, no `[JP]` markers, and no translator-note comments; its provenance record is the credit block and this package.
- **Why:** R2: the absence is recorded so a reviewer does not have to wonder whether annotations were overlooked.
- **Verify:** `grep -n 'Ported for\|\[JP\]\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items. (1) T1's four hotlink errors: class (ii) — the EN-storage asset lines of section 4, posting-time hosting state (KB-58); the ledger's §(c1) hotlink line dispositions the class. (2) T1's one pseudo-ref error: class (iii), draft-wiki form — the candidate's own draft-host delivery lines (section 3). (3) The render row's three items: the page's runtime-hotlink site-theme chain (KB-40, environment-layer, not charged), the WebKit-only CC-license "S" glyph-coverage artifact (KB-36, engine font coverage, not a theme defect), and the EN assets returning 404 (KB-58, deferred hosting). (4) T4's P5 and P9 items: P5 (the live and served EN-storage assets) DISPOSITIONED, class (ii) / KB-58, and P9 (the untranslated tagline) DISPOSITIONED under ruling 2, both per the ledger's §(c3) line. The footnoteblock deletion (section 8) is not a disposition — it has no deciding record — and is listed here so its absence from the disposition set is explicit.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); ruling 2; the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–4); the footnoteblock item stands as flagged in section 8.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 83): exit 1, 5 errors / 1 warn / 7 infos (hotlink×4, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN10)): FINDINGS, the three items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 93): FINDINGS jointly, display-affecting count 2 (the EN-storage assets, live and served; the untranslated tagline); the ledger's §(c3) line dispositions P5 and P9 for this theme. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +115/−105 in 71 change blocks / 4 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:galactic-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 93; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The usage example at candidate L90 as built read `@@[[include :scp-jp:theme:galactic-theme]]@@`: the porting wave's repoint changed the branch prefix but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to this candidate's posting name, `:scp-jp:theme:galactic-theme-jp` — candidate L90 now reads `@@[[include :scp-jp:theme:galactic-theme-jp]]@@` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — heuristic and residue mass, resolved by shape

Class M treatment: the 30 heuristic blocks are not listed one by one; they fall into the shapes below, each verified against the bytes at the cited ranges. The 4 residue blocks are listed in full.

| Shape | Blocks | Where | Resolution |
|---|---|---|---|
| Specimen sentence translation (unanchored) | The TRANS-UNANCHORED body mass (31 label occurrences across heuristic and mixed blocks) | candidate L34–182 | P10 translation (section 6) |
| CSS comment translation | Inside the CSS-BODY heuristic blocks | the delivered CSS body | Expected heuristic mass; comments carry no behaviour |
| Residue: image exhibit source completion | B18 | candidate L73 | The bare filename completed to the full EN-storage URL (section 4) |
| Residue: heading translation | B24 | candidate L93 (`+ 例`) | P10 translation of the `+ Examples` heading |
| Residue: blank line deleted at the tail | B66 | original L1029 | Formatting (section 9) |
| Residue: `[[footnoteblock]]` deleted | B67 | original L1032 | Inert on this page (no footnote elements); undocumented, flagged (section 8) |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-galactic-theme-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The base include `:scp-jp:theme:black-highlighter-theme` is another candidate in the population with its own package; this theme's record names it as a dependency, not a change. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Galactic Federation Theme
- **Author:** Woedenaz
- **Source:** https://scp-wiki.wikidot.com/theme:galactic-theme — revision 102
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
