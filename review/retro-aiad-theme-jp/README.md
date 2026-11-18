# Review package — theme:retro-aiad-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:retro-aiad-theme-jp — origin EN, population #130 [GOSIGN2-LEDGER (b) row 130]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 0 warns / 0 infos (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 125; GOSIGN2-LEDGER (b) row 130]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page T2 no machine verdict (exit 2); sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-C (EN18))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN18))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 130, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 130]
- FIX5 re-judgement: item 25 (class H) FIXED — FIX5-TEXTA §6, commit 6f6b349: usage-example includes repointed to theme:y2k-jp and theme:retro-aiad-theme-jp [GOSIGN2-LEDGER-SUPPLEMENT (a) item 25]
- Computed against: canonical commit 6f6b34974c400a68e01363f5423d1cf817492522; candidate file pages/theme:retro-aiad-theme-jp.txt sha256:7961eae93bc1dcf6026232bfb189c5ca3cb0b70b089ca2d6c29ecdb979939ad2; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes). This package's stamp also reads PASS, not STALE: the candidate is byte-identical to the file the FIX5 wave judged (its last content change is the FIX5 commit itself) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 25 [H] (usage-example includes naming non-port page names) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 25: **FIXED** (FIX5-TEXTA §6, commit 6f6b349); re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c3): P1 DISPOSITIONED (posting-procedure convention class), P3 credit fields FIXED by the credit waves; ledger §(c2) render row: page T2 no machine verdict (exit 2, coverage caveat), sample credit-modal preview form (KB-32), sample 884px@768 overflow (KB-33), runtime-hotlink site-theme chain (KB-40); T1 baseline 5 errors, all pseudo-ref (draft-host class (iii)) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:retro-aiad-theme | theme:retro-aiad-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 15, the first-translation reference revision, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 15 (candidate L25) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-retro-aiad-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:retro-aiad-theme-jp.txt`, copied at worktree HEAD c92a320; the file's last content change is commit 6f6b349 (FIX5-TEXTA) |
| Lines / bytes | 153 lines / 3,546 bytes (the last line carries no trailing newline, so `wc -l` reports 152) | 160 lines / 5,001 bytes |
| SHA-256 | 32e389b894e2d3d28865ee1cbc25c10ca50c477e591a9055fddd9c50fa58c164 | 7961eae93bc1dcf6026232bfb189c5ca3cb0b70b089ca2d6c29ecdb979939ad2 |

Wave history: Stage 2 EN18 integration (3c1bcdf) created the port; FIX2-CREDIT (666f543) completed its credit fields; FIX5-TEXTA (6f6b349) applied item 25's fix and is the file's last change — which is why this stamp, alone among this batch's three, reads PASS against the current bytes.

## Summary

A thin layer over the Y2K theme: the theme's own CSS is five rules (two asset backgrounds, a transparent header span, and two `::before` title strings), and everything else is the base theme's. The candidate keeps that architecture exactly — it layers over theme:y2k-jp through a head @import plus the interwiki-style priority pair, translates the exhibit body, and swaps the original's Rate/info exhibits for the preview credit block. Measured churn is +73/−71 changed lines (diff.md, the generator's difflib count) across 49 classifier change blocks, most of it the exhibit translation. The one blocking item was a copy-paste hazard: the page's own install instructions named the EN page names, which will not exist on SCP-JP; FIX5 repointed them, and the per-theme record re-derives the fix from the bytes.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 49 change blocks — 25 specific (51.0%), 23 heuristic (46.9%), 1 residue (2.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Label counts are signature spans across blocks (a block carries several).

| Label | Spans |
|---|---|
| TRANS-UNANCHORED | 24 |
| TRANSLATION-ANCHORED | 12 |
| DRAFT-HOST | 6 |
| SELF-DELIVERY | 3 |
| IFTAGS | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| TASL-FIELDS | 1 |
| WS-ONLY | 1 |

## Standing sections

### 0. Header and provenance frame

- **What:** The original's delivery head stands inside its gate: `[[iftags +theme]]` (original L1) then a head module importing the Y2K base's code block from scp-wiki.wdfiles.com (original L3–5). The candidate's frame stands outside its gate (candidate L1–14): one head module importing both layers (base and own) from the draft host, then two interwiki-style includes at priorities 1 (base) and 2 (own); the gate (`+テーマ`, candidate L16) wraps credit and body only. Provenance route: derived from the original at the reference revision (first translation, rev 15). Kind K5b-3: the candidate layers over theme:y2k-jp, and this package's diff covers the theme's own layer only (review/sources.tsv note); the base is a separate candidate (change set).
- **Why:** The frame is where delivery is declared; P6/T3 layering (priority 1 base, 2 own) is the campaign's standard form for a layered theme. Declaring the K5b scope here keeps the base theme's diff out of this package's claims.
- **Verify:** Read original L1–5 against candidate L1–16; `pages/theme:y2k-jp.txt` exists in the canonical repo.
- **Disposition:** Standing (frame form); no header item charged.

### 1. Credit and attribution

- **What:** The original has no credit block: it carries an info-module exhibit (`:scp-wiki:info:start` / `more` / `end` with placeholder text, original L16–20) and its attribution in prose (original L22–24). The candidate carries the preview credit block (candidate L18–27) with the eight ruling-3 fields. **著作権者:** [[*user Placeholder McD]] — the theme's developer, per original L22 ("developed by [[*user Placeholder McD]]"). The base theme's author (etoisle) and the logo's author (EstrellaYoshte) are not in the field, and were not in any original credit field either: the original credits them in prose, and the candidate keeps those credits in the translated prose at the same loci (candidate L29 for etoisle's base authorship, candidate L31 for the logo and background credits) and in the code banner (candidate L125–130). Checked against the credit-field standard, the field names the theme's own author and no attribution the original makes is dropped. No license box on either side (T4: none — original has none, candidate adds none). No T7 credit-module CSS (the preview module supplies the furniture). The original's bare Rate exhibit (original L7–10), its "Rating:" label, and the empty "Rating w/ Credit Module:" label (original L12–14) are removed together with the info pair (BARE-RATE-DEL and INFO-DEL spans, B3/B5): the preview credit block is rate-bearing, so no rating surface is lost, and the labels headed the exhibit set that P3 replaces.
- **Why:** P3/T1 (credit block swap; the EN info module does not render here), ruling 3 (the eight fields; campaign translations credited to AI — **翻訳責任者:** AI, **翻訳年:** 2026), KB-09 (no bare Rate beside a rate-bearing credit block).
- **Verify:** Read candidate L18–27 against original L16–24; `grep -c 'module Rate' candidate.txt` (0).
- **Disposition:** FIXED (P3 credit fields, credit waves; ledger §(c3)); standing.

### 2. Includes and components

- **What:** Original includes: the info trio (removed, section 1) and `component:image-block` (original L37, kept at candidate L44 with its caption translated and its file reference made absolute, section 4). Candidate adds: the `:scp-jp:credit:start-preview` / `end-preview` pair and the frame's two `component:interwiki-style` includes (candidate L6–14; the bare `component:` form, as in the population's frame form). The usage-example includes inside the body are exhibits, covered in section 7.
- **Why:** P1 (branch forms of shared components), T8 (component swaps to JP forms), P6 (the frame includes).
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare.
- **Disposition:** Standing; no include in the candidate points at an EN-wiki page.

### 3. Delivery and code loading

- **What:** Two delivery channels, mirroring the original's topology. (a) Module @import: the original imports the base's /1 in its head module (scp-wiki.wdfiles.com, original L4) and its own /1 in a tail module after the gate (scp-wiki.wikidot.com/local--code, original L151–153); the candidate imports both from the draft host sigma10-jp-test.wdfiles.com in its single head module (candidate L2–3; DRAFT-HOST spans, class (iii) draft form). (b) The interwiki-style supplement frame (candidate L6–14) names the same two URLs at priorities 1 and 2 — an addition of the port (the original has no interwiki-style include), in the T3/T9 form. Self-delivery census, all code forms counted: the candidate has exactly one code block, `[[code type="css"]]` at candidate L123–158, and its /1 references (candidate L3, L13) name that block; the block holds the theme's complete own CSS and doubles as the displayed source exhibit, the same dual role as the original's single code block (original L114–146, delivered by its tail module). The named block is the stylesheet, not a sample (the navla-style check: there is no second, larger stylesheet block). The base's /1 references (candidate L2, L8) name theme:y2k-jp's code block, in the base candidate's own package's keeping.
- **Why:** P4 (foreign local--code → own-wiki local--code; draft host at draft stage, class (iii)), T3/T9 (own-code delivery via interwiki-style with layered priorities), KB-07 (priority discipline: 1 normalize/base, 2 own).
- **Verify:** `grep -n 'local--code' original.txt candidate.txt`; count code blocks in each file over all forms (`[[code`, `[[code type=`).
- **Disposition:** Standing; the draft-host URLs are class (iii), rewritten at posting.

### 4. Fonts and assets

- **What:** The theme's one font stack names "Microsoft Sans Serif" — a system face with no loadable source, kept first as the theme's identity face. P7: `"Noto Sans JP"` is appended to both `::before` stacks (candidate L148, L155; JPFONT-STACK span in B47, and B48 adjudicated in the appendix), and the face is loaded by one Google Fonts @import placed at the head of the delivered code block (candidate L132; JPFONT-LOAD in B44). Assets: the two CSS backgrounds are repointed from `scp-wiki.wdfiles.com/local--files/theme:retro-aiad-theme/` to the draft host under the JP page name (candidate L135, L139; P5/DRAFT-HOST), and the exhibit logo, a bare file name in the original (original L37), becomes an absolute draft-host URL under the JP page name (candidate L44). No font import is duplicated (one font load; the head module's two @imports are the two delivery layers, distinct targets), and no named face is left unloaded (Microsoft Sans Serif is a system font; Noto Sans JP is loaded).
- **Why:** P7/T5 and KB-16 (JP face loaded and suffixed into the stacks it serves), P5 (theme files re-hosted under the candidate's own page).
- **Verify:** `grep -n '@import' candidate.txt` (three: two delivery, one font); read candidate L147–157.
- **Disposition:** Standing (P7 applied by the port; no font item was charged against this theme).

### 5. Header, sidebar, and site furniture

- **What:** The theme sets no `--header-title` / `--header-subtitle` variables (those come from the Y2K base). Its furniture is the two `::before` content strings in its own CSS: `"Infotech Department"` → `"情報技術部門"` (candidate L149) and `"Artificial Intelligence Applications Division"` → `"人工知能適用課"` (candidate L156). Both are reader-visible strings rendered on every page using the theme, and both are translated (KB-18); 人工知能適用課 is SCP-JP's established name for the AIAD. The sidebar and topbar are the base theme's (P8: no adaptation in this layer).
- **Why:** KB-18 (visible text, including CSS `content:`, is translated); these are content strings, not identity marks — the identity mark (the theme's name and its face) is section 4.
- **Verify:** Original L136–145 against candidate L147–157.
- **Disposition:** Standing (translated by the port; no furniture item charged).

### 6. Text translation

- **What:** The exhibit body is translated throughout (P10): the introduction and credits prose (candidate L29–33), the install instruction (candidate L33), section heading (+ 例）, the image caption, the horizontal-rule and heading explanations, collapsible labels (+ 見出し / - 見出し）, the heading samples （第一 through 第六見出し）, tab names, the blockquote, the table, and the closing font note (candidate L116). Two flattenings are recorded rather than hidden: the original's joke tab names "Tabulator" / "Tabulation" both become タブ (candidate L67, L70), and "How quaint." becomes 趣がありますね (candidate L73). The code block's banner comment is carried verbatim in English (original L116–121 → candidate L125–130), as a quotation of the original's authorship banner. The TRANS-UNANCHORED (24 spans) and TRANSLATION-ANCHORED (12 spans) mass is these exhibit pairs; the heuristic share is adjudicated in the appendix.
- **Why:** P10 (body, usage, and sample text translated; terminology matched to the JP wiki's established forms).
- **Verify:** Read candidate L29–116 against original L22–109 section by section; the exhibits align one-to-one.
- **Disposition:** Standing (the port itself); T5's joint verdict word for this theme carried the one display-affecting charge of item 25, closed in the per-theme record.

### 7. Links

- **What:** The FIX5 item lives here (per-theme record): the install example's two escaped includes (candidate L36–37) now name `:scp-jp:theme:y2k-jp` and `:scp-jp:theme:retro-aiad-theme-jp`. Beyond it: the user links ([[*user …]] ×4 across prose and credit) are carried; the credit source link (candidate L26) points at the EN original on scp-wiki.wikidot.com, matching the recorded host in review/sources.tsv (scp-wiki) — probed as part of the campaign record; no host defect. No other prose link in the candidate names an un-suffixed theme page.
- **Why:** P11 and ledger class H (usage examples are copy-paste surfaces: an example naming a page that will not exist fails for every reader who follows it).
- **Verify:** `grep -n 'theme:' candidate.txt` — every occurrence is a -jp name or the EN source URL.
- **Disposition:** FIXED (item 25); no other link item.

### 8. Structure

- **What:** The original's architecture is preserved (the localize.md closing rule): gate, credit/info zone, install example, exhibits in the original's order, source code in its collapsible at the body's tail. Three structural changes: (a) the frame moved out of the gate and merged (head + tail modules → one head module plus the interwiki pair, section 3); (b) the Rate/info exhibits were replaced by the credit block at the body's head (section 1); (c) the code collapsible gains a `+ ソースコード` heading (candidate L120) where the original has the bare text "Source code" (original L112) — the EXHIBIT-RESTRUCTURE span (in B42): the exhibit itself is carried in place, only its heading is promoted and translated. The achi-style parameter mechanisms do not exist in this theme; its one mechanism is the two-layer delivery, whose definitions are all carried (section 3).
- **Why:** R3 (exhibit restructuring stated with its ground), the closing rule (structure, selectors, and channel order preserved; corrections appended, not interleaved).
- **Verify:** Structural census: `grep -n '\[\[module\|\[\[code\|\[\[iftags\|\[\[collapsible' original.txt candidate.txt`.
- **Disposition:** Standing; no structural item charged (this theme's (e) item was textual, class H).

### 9. Formatting only

- **What:** One WS-ONLY block (B43): the banner line "Based on Y2K Theme created by Etoisle " loses its trailing space (original L120 → candidate L129). No re-indentation: the code block keeps the original's four-space indent, and the classifier reports 0 reindent blocks. The remaining line churn is the translation and delivery mass counted in the class summary.
- **Why:** R7 (formatting disclosed as its own class so it is never mistaken for semantic change).
- **Verify:** Diff block B43 in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked explicitly. The candidate contains no `[!-- … --]` porter notes and no 訳注； the classifier's ANNOTATION label does not fire for this theme. The only non-original text is the credit block (section 1) and the delivery frame (section 3), both standing supplements rather than annotations, and the FIX5 lines of section 7 are edits to the example, not notes.
- **Why:** R2 (annotations are listed when present; here the ground for "none" is the explicit check).
- **Verify:** `grep -n '!--' candidate.txt` (no matches); `grep -n '訳注' candidate.txt` (no matches).
- **Disposition:** None (absent, checked).

### 11. Dispositions and exceptions

- **What:** (1) T1's five errors are all pseudo-ref, the draft-host class (iii): the candidate's local--code and local--files URLs on sigma10-jp-test.wdfiles.com (candidate L2, L3, L8, L13, L44), sanctioned at draft stage and rewritten at posting (T1-ROWS row 125). (2) Render-row dispositions: the page's T2 exit 2 is a coverage caveat, not a finding; the sample's credit-modal is the preview form (KB-32, ruling 5); its 884px@768 overflow is the static credit replica family (KB-33); the runtime-hotlink chain is the environment layer (KB-40). (3) P1's c3 disposition (posting-procedure convention) covers the branch-form conventions of the file as a whole. No item for this theme is left as an unexplained exception, and this package raises no new flag.
- **Why:** Each disposition cites its class or KB entry; environment-layer lines are recorded as not-charged (AGENTS.md §3).
- **Verify:** T1-ROWS row 125; ledger §(c2) row for this theme (RENDER-S2-C (EN18)).
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** (a) T1 checker baseline: exit 1, 5 errors / 0 warns / 0 infos, all pseudo-ref (stamp; T1-ROWS row 125). (b) T2/T3: page no machine verdict (exit 2, coverage caveat); sample FINDINGS, all dispositioned (ledger §(c2)). (c) T4 follow-up: LOCALIZE-ROWS row 130 records display-affecting findings 1 — item 25's charge — closed by FIX5. (d) FIX5 re-derivation: per-theme record below. (e) This package: `python3 review/build_review.py --check` — this package is not in the stale set (the stale set is byte-identical with and without this batch's three packages; set comparison in the batch report). (f) Brace depth: both files' CSS balanced (comment/string-stripped counts 5 opens / 5 closes each, final depth 0).
- **Why:** Verification claims name the cheapest deciding check and its result.
- **Verify:** Re-run the checker on `pages/theme:retro-aiad-theme-jp.txt`; re-run `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### Ledger item 25 [H] — the usage-example names, re-derived

The ledger charge (§(e) item 25, from LOCALIZE-S2-C): the install example's includes point at non-port page names on scp-jp — at charge time, candidate L36 named `theme:y2k` and L37 named `theme:retro-aiad-theme`, while the candidates are theme:y2k-jp and theme:retro-aiad-theme-jp; display-affecting for copy-paste, as charged. The supplement (row 25) re-judges it FIXED by FIX5-TEXTA §6, commit 6f6b349: "usage-example includes repointed to theme:y2k-jp and theme:retro-aiad-theme-jp". The bytes confirm it exactly, and show the fix covered the branch as well as the suffix: candidate L36 reads `@@[[include :scp-jp:theme:y2k-jp]]@@` and L37 `@@[[include :scp-jp:theme:retro-aiad-theme-jp]]@@` — both the `:scp-jp:` branch form and the -jp posting names. Corroboration from the file's history: 6f6b349 is the candidate's last content change, and the candidate's SHA-256 (7961eae9…) equals the verdict stamp's computed-against hash, which is why this package's stamp reads PASS rather than STALE. **FIXED, confirmed from the bytes.**

## Change set outside the two diffed files

(1) `pages/theme:y2k-jp.txt` — the base theme's JP candidate, this theme's layer 1 (its own package covers the base port; the original side's base is theme:y2k on scp-wiki). (2) `pages/theme-decoration-sample-retro-aiad-theme-jp.txt` — the decoration sample page used by the render checks. No fragment or component file belongs to this theme's change set: its delivery is the two local--code channels of section 3, whose runtime form is the posted pages' own code blocks.

## Appendix — heuristic and residue adjudication

49 blocks: 25 specific, 23 heuristic, 1 residue; all adjudicated here or in the sections. **Residue B10** (original L35–36 → candidate L42–43, unlabeled): the rule line plus "+ Examples" → "+ 例" — a heading translation pair (P10), unlabeled because the block pairs a horizontal-rule line with a one-word heading. **Heuristic TRANS-UNANCHORED blocks B39, B41, B42** (blockquote continuation, the font-note prose, the source-code heading zone): P10 translation by shape; B42 also carries the EXHIBIT-RESTRUCTURE heading promotion adjudicated in section 8. **Heuristic CSS-BODY block B48** (original L144–145 → candidate L155–157, the `h2 span::before` rule): its font-family line is a P7 stack suffix and its content line a KB-18 string translation — narrated as P7/KB-18 in sections 4–5 under the standing rule that font-stack rewrites are P7 even when the classifier labels the block CSS-BODY heuristic. The remaining TRANS-UNANCHORED / TRANSLATION-ANCHORED heuristic mass (B7–B38 passim) is the exhibit translation pairs of section 6, resolved by shape: every pair is a CN-free EN→JP line mapping inside the exhibit body, with no delivery, credit, or structural content.

## License and attribution

- **Title:** Retro AIAD Theme
- **Author:** Placeholder McD
- **Source:** https://scp-wiki.wikidot.com/theme:retro-aiad-theme — revision 15
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
