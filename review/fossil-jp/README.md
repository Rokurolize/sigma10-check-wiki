# Review package — theme:fossil-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:fossil-jp — origin EN, population #90 [GOSIGN2-LEDGER (b) row 90]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 90]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 0 infos (hotlink×5, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 80; GOSIGN2-LEDGER (b) row 90]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 533–536px@≤375 and 847–856px@768 both engines; sample 545–548px@≤375 + 898px@768; credit-modal heading pale tan on gray (contrast 1.03). [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 90, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 90]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 90]
- Computed against: canonical commit f1138e4f4c7bcce523971efdee87d55f90302d3c; candidate file pages/theme:fossil-jp.txt sha256:aa5d3159242eff556a692b5524652331fe3aaf1d55e99d97f84bb8db611d8ba3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 90) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×5 + pseudo-ref ×1 (classes (ii)/(iii), section 11); the render row's items (KB-40 / KB-32, section 11); the T4 items P1 and P5 (section 11). One T4 sub-item (the `content: "TAGS"` string) has no separate ledger disposition; it is recorded standing in section 5 and flagged in section 11 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:fossil | theme:fossil-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 16 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-fossil.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:fossil-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 1,239 lines / 34,464 bytes | 1,248 lines / 35,753 bytes |
| SHA-256 | a9351c72805e23d04d411795b5859af9929f0b7110389a94434471e053800bb3 | aa5d3159242eff556a692b5524652331fe3aaf1d55e99d97f84bb8db611d8ba3 |

Wave history: the candidate was created by the Stage 2 EN10 integration (commit c210f75, the LOCALIZE-S2-A wave's port); commit f1138e4 (FIX-P4, the pattern-4 repoint of base-theme delivery to JP port candidates across 39 files) carries this file's sigma-plus form and its translator-attribution normalization, both visible in that commit's diff for this file. No production JP counterpart exists, so the R4 adoption question does not arise.

## Summary

A sigma-plus-based EN port with the standard head (base include, own-code import, interwiki frame, gate, bare Rate) and a long specimen body (tabs, blockquotes, tables, the font specimen) ahead of its `[[code]]` CSS. The port swaps the base to the JP sigma-plus candidate, repoints its own delivery to the draft host, installs the JP preview credit block in place of the bare Rate, adds the JP font supplement (a Noto Sans JP load and its stack entries) and moves the display face's load from a third-party mirror to Google Fonts proper, and translates the specimen body in full. Two recorded items stand by disposition: the five asset references that remain on EN storage (KB-58) and the sigma-plus include's final form (posting-procedure convention). Measured churn (diff.md, the generator's difflib count with autojunk off: +115/−113, 228 changed lines in 64 change blocks / 8 diff hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 64 change blocks — 29 specific (45.3%), 34 heuristic (53.1%), 1 residue (1.6%), 0 skipped. The heuristic mass is the specimen body's sentence-by-sentence translation (TRANS-UNANCHORED ×34 label occurrences), resolved by shape in the appendix. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 3 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 2 |
| SIGMA-PLUS-JP | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 14 |
| TRANS-UNANCHORED | 34 |
| WS-ONLY | 7 |

Adjudication for this README (every specific block was read against the bytes): the three EXHIBIT-RESTRUCTURE primaries (B1, B3, B10) are include repoints, not restructures (section 8). B57 (heuristic, CSS-BODY) is a P7 font-stack insertion (section 4). One classifier miss is recorded: the original's bare Rate is spelled `[[module rate]]` in lowercase (original L14), which the BARE-RATE-DEL signature does not match; its deletion rides inside B5 and is narrated in section 1 from the bytes. The single residue block (B64) is a trailing blank line (section 9).

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:fossil-jp; original theme:fossil on scp-wiki at reference revision 16; candidate `pages/theme:fossil-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard). The candidate's head keeps the original's shape: the sigma-plus include (candidate L1), the own-code import module (L3–5), the interwiki frame inside its `[[div_]]` wrapper (L6–11, the wrapper is the original's own), then the localized gate `[[iftags +テーマ]]` (L13).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3, the base form is T8 (section 2).
- **Verify:** The sources.tsv row for fossil-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare Rate (`[[>]]` / `[[module rate]]` / `[[/>]]`, original L13–15, inside B5's range) plus its authorship prose ("This is an aesthetic theme gifted to [[*user Pedagon]]…", original L17). The candidate deletes the bare Rate and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L15–24) carrying the eight ruling-3 fields (タイトル Fossil Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Fossil Theme; 著作権者 EstrellaYoshte; 作成年 2024; 初訳時参照リビジョン 16; the source link to scp-wiki.wikidot.com/theme:fossil). The theme's name stands in English in both title fields, as a proper name; no record charges it. The gift prose is translated in place after the block (candidate L26). T7 credit-module CSS: 3 matching lines on each side — the theme's own credit rules are inherited from the original unchanged, and no supplement was needed. No license box is added: the original carried none, and this theme's license record rides in the credit block.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; the translator form (AI) arrives with f1138e4 for this file.
- **Verify:** `grep -n 'module rate' candidate.txt` returns nothing; read candidate L15–24 against the eight fields.
- **Disposition:** Applied.

### 2. Includes and components

- **What:** Two include changes. (1) The base: `:scp-wiki:component:sigma-plus` (original L1) becomes `[[include component:sigma-plus-jp]]` (candidate L1, B1) — the JP port candidate of the sigma-plus component in its bare include form; the same swap is this file's FIX-P4 hunk (pattern-4 repoint of base-theme delivery to JP port candidates). The usage prose's component link follows in text form (candidate L32: `Fossil Theme は [[[component:sigma-plus|sigma-plus]]] を土台にしたテーマです。`, B9). (2) The image exhibit's include is repointed `:scp-jp:component:image-block` (candidate L36, B10) while its `name=` asset stays on EN storage (section 4). The candidate's remaining includes are the frame (section 3) and the credit pair (section 1); its usage line names the candidate itself (candidate L30: `[[include :scp-jp:theme:fossil]]`, the recorded convention of section 11).
- **Why:** P1 (KB-15) for the exhibit repoint; T8/KB-64 for the sigma-plus base form — the port's base is the JP sigma-plus candidate, and the include's final posted form is the posting-procedure convention the ledger dispositions.
- **Verify:** `grep -n '\[\[include' candidate.txt` — five live includes plus the escaped usage line, as listed.
- **Disposition:** DISPOSITIONED (the sigma-plus item, P1, posting-procedure convention class; section 11); the exhibit repoint is applied.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS from EN storage: an `@import` of `https://scp-wiki.wdfiles.com/local--code/theme:fossil/1` (original L3) and an interwiki frame naming the same URL (original L6–10). The candidate repoints both to its own code on the draft host: `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Afossil-jp/1` (candidate L4, B2; frame parameter at candidate L9, B4), keeping the frame's priority=1 and its `[[div_]]` wrapper. No other delivery lines change; the CSS body itself is delivered from the candidate's own `[[code]]` block (the /1 index), as in the original.
- **Why:** P6/T3: the own layer must name the candidate's own code, and on the draft wiki that is the draft-host form (KB-41, class (iii)); the frame repoint is what makes the delivered bytes the candidate's rather than the EN original's.
- **Verify:** `grep -n 'local--code' candidate.txt` — the two lines above, both draft-host.
- **Disposition:** DISPOSITIONED (class (iii) draft-wiki form).

### 4. Fonts and assets

- **What:** Fonts, three changes (P7). (1) A JP supplement load is added at the head of the delivered CSS: `@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap')` (candidate L155, B54, JPFONT-LOAD). (2) The display face's load is repointed: Półtawski Nowy was loaded from a third-party mirror, api.fonts.coollabs.io (original L159–161); the candidate loads the same family and weights from fonts.googleapis.com (candidate L167–169, B56, FONT-IMPORT). (3) The stacks gain the JP face: `--header-font` inserts `"Noto Sans JP"` after Półtawski Nowy and `--body-font` inserts it after Public Sans (candidate L210–212, B57 — a CSS-BODY heuristic block whose substance is the P7 stack insertion). The Sometype Mono load (candidate L169 area) and the Public Sans stack entries are otherwise the original's. Assets: five references stay on EN storage (scp-wiki.wdfiles.com) — the header image named by the image-block exhibit (candidate L36) and the theme's texture artwork in the CSS body; these are the T1 row's five hotlink errors and the T4 row's P5 item (live + served EN-storage assets).
- **Why:** P7/T5 for the supplement and the stack entries; the load repoint is KB-17's shape (a font load moved to its canonical host with family and weights unchanged). P5/KB-58 for the assets: EN-storage hosting is the deferred state — re-upload is barred by owner order, and posting is where the hosting question is settled.
- **Verify:** `grep -n '@import' candidate.txt` — the delivery import of section 3 plus the three font loads above. `grep -cn 'scp-wiki.wdfiles.com' candidate.txt` — 5.
- **Disposition:** DISPOSITIONED (assets, class (ii) / KB-58; section 11); the font changes are applied.

### 5. Header, sidebar, and site furniture

- **What:** This theme sets no `--header-title`/`--header-subtitle`/`--logo-image` variables on either side (grep returns 0/0); its header is the sigma-plus base's. One CSS-rendered string is recorded here because the T4 row flags it: `content: "TAGS"` (candidate L1103; original L1095), the tag-list heading the theme's CSS renders, kept byte-unchanged in English. The ledger's §(c3) line for this theme carries no separate disposition for it (section 11 records the gap); it stands as part of the delivered CSS, and a JP styling pass at posting can localize it without touching the port's structure. Sidebar and topbar rules are inherited from the base and the theme body unchanged.
- **Why:** P9/T6 is the furniture class; a CSS content string is reader-visible text, so it is recorded rather than passed over (KB-18's concern), with its record state stated exactly.
- **Verify:** `grep -n '"TAGS"' candidate.txt` — one hit, candidate L1103.
- **Disposition:** Standing as recorded; see section 11 for the disposition gap.

### 6. Text translation

- **What:** The specimen body is translated in full: the usage prose (candidate L26–32), the horizontal-rule and heading instructions (L38, L40), the collapsible labels (L43–44), the heading specimens （見出し2–6, L46–54), the tab specimens (L60–122, including the repeated long-tab filler sentences, each translated in place), the blockquote specimens (L128–134), the table specimen (L138–140), and the font specimen lines (L143–153: 見出しの書体は Półtawski Nowy / 本文の書体は Public Sans / 等幅の書体は Sometype Mono — the font names stand as proper names inside translated sentences). The 34 TRANS-UNANCHORED blocks are this mass; they resolve by shape in the appendix (sentence-level specimen translation, anchored where a markup token survives: TRANSLATION-ANCHORED ×14). No English prose survives outside proper names, the font specimen's subject names, and the section 5 string.
- **Why:** P10 and KB-18: reader-visible strings are translated; specimen filler is translated with the same care as instructions because the specimen is what a user copies.
- **Verify:** diff.md's body sections in order; `grep -n 'This is\|How quaint' candidate.txt` returns nothing.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The candidate's live outbound links are the credit block's source link (candidate L23) and the translated `[[*user Pedagon]]` gift line's counterpart (candidate L26 names Pedagon without the user-link markup — the prose translation carries the name as text; the original's `[[*user …]]` form is not reproduced). The source link names scp-wiki.wikidot.com/theme:fossil, the original's recorded host in sources.tsv — the serving form, not a defect. No other prose links exist in this theme; the asset URLs are CSS references (section 4), and the usage line's include is sample text (section 2).
- **Why:** P11 under the dead-reference evidence standard: a link is charged when its target does not serve or a JP counterpart exists; neither holds for the source link.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only prose hit.
- **Disposition:** Standing.

### 8. Structure

- **What:** No structural change. The classifier's three EXHIBIT-RESTRUCTURE primaries do not survive contact with the bytes: B1 is the sigma-plus include swap at the page head, B3 is the interwiki frame's include repoint, and B10 is the image-block include repoint — three include repoints the signature matched because they sit in exhibit-adjacent lines, with no exhibit added, removed, or reordered. The exhibit census confirms it: heading specimens, tabs, blockquotes, table, font specimen, and the source-code exhibit stand in the original's order on both sides. The R3 question (a silent structural deletion) does not arise.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a repoint share a diff shape; here the census, not the label, decides.
- **Verify:** Compare the exhibit sequence via `grep -n '\[\[tab\|見出し\|++++' original.txt candidate.txt` and the three blocks in diff.md.
- **Disposition:** Standing; no class I item.

### 9. Formatting only

- **What:** Seven WS-ONLY blocks (B55, B58–B63), each the deletion of a whitespace-only line inside the CSS body (trailing-space lines the candidate normalizes away), and one residue block (B64): a trailing blank line added at the candidate's end (candidate L1247). No re-indentation and no line-ending conversion (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class (R7) so it is never mistaken for a semantic change.
- **Verify:** The eight blocks are diff.md's whitespace-only entries; `grep -n ' $' candidate.txt` shows the surviving trailing-space state.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. This candidate carries no `Ported for SCP-JP` banner, no `[JP]` markers, and no translator-note comments; its provenance record is the credit block and this package.
- **Why:** R2: the absence is recorded so a reviewer does not have to wonder whether annotations were overlooked.
- **Verify:** `grep -n 'Ported for\|\[JP\]\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, plus one record gap. (1) T1's five hotlink errors: class (ii) — the EN-storage asset lines of section 4, posting-time hosting state (KB-58); the ledger's §(c1) hotlink line dispositions the class. (2) T1's one pseudo-ref error: class (iii), draft-wiki form — the candidate's own draft-host delivery lines (section 3). (3) The render row's two items: the credit-modal heading contrast of 1.03 (the preview form's known state, KB-32) and the sample's Chromium/WebKit page-level runtime-hotlink site-theme chain (KB-40, environment-layer, not charged). (4) T4's P1 and P5 items: P1 (the sigma-plus include) DISPOSITIONED under the posting-procedure convention class, and P5 (the EN-storage assets) DISPOSITIONED, class (ii) / KB-58, both per the ledger's §(c3) line. Record gap, flagged not smoothed: the T4 row's third item, the T5 `content: "TAGS"` string (section 5), has no corresponding line in the ledger's §(c3) dispositions for this theme. The string stands byte-unchanged in the candidate; the theme's PASS rests on the recorded P1/P5 dispositions, and this package records the TAGS item as standing without a named disposition so the next reader of either record sees the gap.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–4); the TAGS item stands as recorded in section 5.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 80): exit 1, 6 errors / 1 warn / 0 infos (hotlink×5, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN10)): FINDINGS, the two items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 90): FINDINGS jointly, display-affecting count 1 as the row records it (the EN-storage assets); the ledger's §(c3) line dispositions P1 and P5 for this theme; the T5 TAGS item is recorded in section 5. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +115/−113 in 64 change blocks / 8 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:fossil-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 90; go-sign, COMPLETION-REPORT §10).

## Appendix — heuristic and residue mass, resolved by shape

Class M treatment: the 34 heuristic blocks are not listed one by one; they fall into the shapes below, each verified against the bytes at the cited ranges. The 1 residue block is listed in full.

| Shape | Blocks | Where | Resolution |
|---|---|---|---|
| Specimen sentence translation (unanchored) | B7, B8, B9 (usage prose), B11, B12 (instructions), B21 (tab aside), B23–B29, B31–B43 (long-tab filler, translated in place, repetition preserved), B45–B49 (blockquote and table specimens), B51 (font specimen line) | candidate L26–153 | P10 translation; the repeated filler sentences are the specimen's own repetition, kept |
| Font-stack insertion in a CSS body block | B57 | candidate L210–212 | P7 stack supplement (section 4) |
| BHL import repoint inside a CSS body block | — (none in this package; the delivery import is B2, specific) | — | — |
| Residue: trailing blank line added | B64 | candidate L1247 | Formatting tail (section 9) |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-fossil-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The base include `component:sigma-plus-jp` is another candidate in the population with its own package; this theme's record names it as a dependency, not a change. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
