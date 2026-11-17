# Review package — theme:borealis-constant-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:borealis-constant-theme-jp — origin EN, population #66 [GOSIGN2-LEDGER (b) row 66]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 577722d3863622196852fcd286ebdd135afadc22f3a708f21d439723321a35df); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 10 errors / 1 warn / 1 info (hotlink×8, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 71; GOSIGN2-LEDGER (b) row 66]
- T2/T3 (render, combined verdict): PASS-WITH-NOTES — [combined T2/T3] report `NO candidate-specific blocking defect` — machine lines cross-cutting/draft-form/by-design; cornflower caption contrast 2.56 noted as observation only; interwiki priority=3 correct. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 66, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 66]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 66]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:borealis-constant-theme-jp.txt sha256:577722d3863622196852fcd286ebdd135afadc22f3a708f21d439723321a35df; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 66) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×8 and pseudo-ref ×2 (class (ii), section 11); the render row is PASS-WITH-NOTES with no candidate-specific blocking defect (one contrast observation, section 11); T4's three display-affecting items (header text in English in both variants, the EN-hosted assets, the BHL-page link item), each with its ledger disposition in section 11 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:borealis-constant-theme | theme:borealis-constant-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 40 (first translation; the candidate's credit block records 初訳時参照リビジョン: 40) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs2-en5/CACHE/orig/borealis-constant-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:borealis-constant-theme-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 638 lines / 20,033 bytes | 637 lines / 20,531 bytes |
| SHA-256 | fc0771a2d1ed4b5b4ee50a0ae7f5e3b0c1a7f8cbc2a0eefcebeeb8ff74d9f74f | 953b722eb9e3a905b58d43c72e9c2f7299cf2de40d5c562a133cebf2bdb58125 |

Wave history: the candidate was created by the Stage 2 EN5 integration (commit 7e07438, the LOCALIZE-S2-A wave's port), normalized by 1869877 (FIX-CREDIT-D), and mechanically fixed by a497307 (FIX4-MECH: duplicate @import removal across 29 themes, KB-65 — for this file the commit removes exactly one line, a duplicated Noto Sans JP @import in the exhibit head; the verdict stamp is computed against a497307 for that reason). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Black Highlighter theme for the author's "Borealis Constant" series, with a generic SPC (Shark Punching Centre) variant built in: two applied layers (code/1 and code/2), two header variants, and a tail frame in which the second layer rides inside the original's comment-marker device. The port follows the BHL frame (JP base include in a head wrapper, base module dropped, own layers repointed to the candidate's own local--code /1 and /2 on the draft host, one interwiki-style layer at priority 3), translates the prose including the SPC-variant usage section, replaces the bare Rate with the preview credit block, and re-sources the theme's display fonts from Bunny Fonts to Google Fonts with the Noto Sans JP supplement added. One mechanical fix wave also touched this file (the duplicate font import, above). What stands is recorded: both header variants stay in English (ruling 2), and eight asset references stay on EN file hosts — including two backgrounds borrowed from other EN pages (spc-001-ex, the-great-hippo) that are part of the theme's SPC joke (deferred-asset class). The render row is the batch's cleanest: PASS-WITH-NOTES, no candidate-specific blocking defect. Measured churn is the batch's smallest relative to size (diff.md: +80/−83 in 46 change blocks; a GNU-diff count of the same pair gives 131 changed lines, and the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 46 change blocks — 27 specific (58.7%), 14 heuristic (30.4%), 5 residue (10.9%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 14 |
| TRANS-UNANCHORED | 13 |
| INCLUDE-REPOINT | 5 |
| CSS-BODY | 3 |
| DRAFT-HOST | 3 |
| EXHIBIT-RESTRUCTURE | 3 |
| SELF-DELIVERY | 3 |
| DELIVERY-HOST | 2 |
| IFTAGS | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 14 heuristic blocks are prose translations and the CSS-BODY font-stack deltas (sections 4 and 6), verified line by line. The 3 EXHIBIT-RESTRUCTURE primaries adjudicate in section 8: one is the street image-block's include repoint inside an example (the recorded false-fire shape), and two are the tail component includes changing namespace. The 5 residue blocks collapse into the appendix table below, per the class M treatment; after adjudication no block is left unexplained.

Residue appendix (all five blocks, adjudicated):

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B13 | L36–37 | L40–41 | The "+ Examples" section heading and its blank line, translated (+ 例） — prose translation (section 6) |
| B30 | L109–110 | L113–114 | Two example-prose lines, translated (section 6) |
| B39 | L584–585 | L583 | Exhibit-1 tail alignment: the blank line before `[[/code]]` is absorbed as the body's last rule re-anchors; no content change |
| B40 | L608–609 | L606 | Exhibit-2 tail alignment, the same shape as B39; no content change |
| B41 | L610–612 | L607 | The original's malformed closer `[[/<]]` after the second exhibit is dropped; the section continues without it (section 8) |

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:borealis-constant-theme-jp; original theme:borealis-constant-theme on scp-wiki at reference revision 40; candidate `pages/theme:borealis-constant-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the original wraps the page in a single `[[iftags +theme]]` gate (L1–620), with a head module importing the base (L3–6), and delivers its two own layers from two tail modules outside the gate (L630–637), the second inside the comment-marker device `[!-- {$spc}` … `[!-- --]`. The candidate splits the head as its BHL siblings do (an added wrapper `[[iftags]]` holding the JP BHL theme include alone, candidate L1–3; the main gate localized to `+テーマ`, candidate L5–615) and keeps the two tail modules and the comment device in place (candidate L625–637).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for borealis-constant-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare `[[module rate]]` (original L9). The candidate deletes it and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L7–16) carrying the eight ruling-3 fields (title Borealis Constant Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Borealis Constant Theme; 著作権者 MisterFrown; 作成年 2024; 初訳時参照リビジョン 40; the source link, naming scp-wiki.wikidot.com/theme:borealis-constant-theme, the recorded host, which serves the original). The title is the theme's proper name in English on both fields, which no record flags. T7 credit-module CSS: none added; the theme's CSS carries no credit rules. License box: none on either side, and none added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module rate' candidate.txt` returns nothing; read candidate L7–16 against the eight fields.
- **Disposition:** Applied (the swap is in the bytes; the ledger's credit outcome for this theme rides on the same credit-wave record as its siblings).

### 2. Includes and components

- **What:** The candidate's includes: the added `:scp-jp:theme:black-highlighter-theme` include inside the head wrapper (candidate L2); the credit pair (section 1); one interwiki-style include (candidate L628–631, section 3); the image-block for the street photograph (candidate L47, repointed to `:scp-jp:` with its asset argument unchanged, section 4); and the two tail components after the exhibits — `:scp-jp:component:toggle-sidebar-bhl` (candidate L617) and `:scp-jp:component:customizable-acs` (candidate L619) — both repointed from their EN-namespace forms. The escaped usage examples (candidate L28–29, L35–36) as built taught the JP branch form with the plain slug, `:scp-jp:theme:borealis-constant-theme` — including the SPC variant's parameter form at candidate L36 (`:scp-jp:theme:borealis-constant-theme |spc=--`) — so each self-reference named a page that does not exist on scp-jp, not the posting form. The usage-example population sweep has since completed both self-references to the posting name, `:scp-jp:theme:borealis-constant-theme-jp` (candidate L29 and L36, the second keeping its `|spc=--` parameter; SWEEP-USAGE.md; canonical commit b5cb724). The Black Highlighter lines in the same examples (candidate L28, L35) name the production JP page and were not sweep lines. The 5 INCLUDE-REPOINT blocks are these repoints; every live include names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. The usage examples' self-repoints as built satisfied the branch half of that rule only; the sweep's completions are what bring them under it. Ruling 4 is not engaged: the components named already exist on the JP side.
- **Verify:** `grep -n '\[\[include' candidate.txt` — all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The base's channel and the own layers' hosts change; the tail structure does not. (1) The original's head module imports the base from the upstream distribution (`nu-scptheme.github.io/Black-Highlighter/stable/styles/…`, original L4–5); the candidate drops the head module — the base arrives through the JP BHL theme include (section 2). (2) The theme's own two layers: the original's tail modules import them from its EN page (`scp-wiki.wikidot.com/theme:borealis-constant-theme/code/1` and `/code/2`, original L631, L636); the candidate's tail modules import its own `local--code/theme%3Aborealis-constant-theme-jp/1` and `/2` from the draft host (candidate L625–627, L634–636, SELF-DELIVERY), and an interwiki-style include at priority 3 names the /1 delivery (candidate L628–631). The second module keeps the original's comment-marker device (`[!-- {$spc}` at candidate L633, `[!-- --]` at L637) — the theme's own SPC-variant frame, carried over unchanged in form. The layers' bodies are the two code exhibits (candidate L172–583, L588–606).
- **Why:** P4/T9: delivery is served from JP hosts — the JP base page for the base, the theme's own code for its layers — never from the original's page or the upstream distribution. P6/T3 supplies the interwiki-style supplement frame (priority 3 for the own layer riding on the base page's 1–2). The draft-host form of the own delivery is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n '@import' candidate.txt` — the exhibits' font imports (section 4) and L626/L635 (own draft-host deliveries); no nu-scptheme or scp-wiki code URL remains.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: the theme's display faces (Anta, Electrolize, Exo 2, Kanit, Lato, PT Mono, Poppins) are re-sourced — the original loads them from Bunny Fonts (`fonts.bunny.net`, original L180–181); the candidate loads the same families from Google Fonts (`fonts.googleapis.com`, candidate L179–180, the FONT-IMPORT block) — and the JP supplement is added (Noto Sans JP, candidate L173, the JPFONT-LOAD block). A later mechanical wave removed a duplicate of that supplement line (commit a497307, KB-65; Provenance), so the file today loads it exactly once. The 3 CSS-BODY heuristic blocks are the stack-side deltas of the same font work. Assets: eight references stay on EN file hosts, untouched apart from their frames — the BHL logo image (candidate L18), the street photograph's image-block (candidate L47), the SPC header logo borrowed from theme:shark-punching-centre-bhl's files (candidate L197), the aurora banner (candidate L254), two SPC backgrounds borrowed from the spc-001-ex page (candidate L540, L568), a background borrowed from the-great-hippo (candidate L574), and the shark banner (candidate L598). These are T1's eight hotlink errors and T4's Pattern 5 items; the ledger dispositions them in the deferred-asset class (section 11). Several are the SPC variant's joke furniture, borrowed from other EN pages by the original's own design.
- **Why:** P7 (JP font supplement; the Bunny→Google re-source keeps the same faces on the campaign's standard font host) and P5 (assets served from JP hosts), whose disposition is KB-58's standing treatment for original-wiki file hosts (deferred re-host, class (ii)): the assets serve today from the EN hosts, and no JP-hosted copies exist to point at.
- **Verify:** `grep -n '@import' candidate.txt` for the fonts; `grep -n 'local--files' candidate.txt` — the eight asset lines listed above.
- **Disposition:** DISPOSITIONED (assets, P5, class (ii) / KB-58); the font work stands as applied, with the duplicate-import fix recorded in Provenance.

### 5. Header, sidebar, and site furniture

- **What:** Both header variants stand in English, exactly as in the original (the HEADERVAR block): the main variant `--header-title: 'BOREALIS CONSTANT'` / `--header-subtitle: 'SHARK PUNCHING CENTRE DATABASE'` (candidate L198–199) and the SPC variant `--header-title: 'SPC DATABASE'` / `--header-subtitle: 'SEARCH, PUNCH, CONQUER'` (candidate L596–597). T4's row 66 marks the pair Pattern 9 display-affecting, explicitly including the SPC variant; the ledger dispositions it under ruling 2 (section 11). The sidebar furniture is the repointed toggle-sidebar-bhl component (section 2); no topbar rule was adapted beyond what the moved CSS bodies already carried. The render row confirms the frame: "interwiki priority=3 correct".
- **Why:** P9's JP-header expectation is what T4 measured; ruling 2 (header text language is translation taste, and these mastheads are the series' and the SPC's own names and mottoes) is the ground the ledger dispositioned it on — recorded here because both variants are always displayed when active.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — L198–199 and L596–597, English.
- **Disposition:** DISPOSITIONED (P9, ruling 2, GOSIGN2-LEDGER §(c3) line for this theme).

### 6. Text translation

- **What:** The prose is translated throughout (the 13 TRANS-UNANCHORED heuristic primaries and 14 TRANSLATION-ANCHORED blocks, verified line by line): the intro, both usage sections (default and SPC variant), the examples — including residue B13's heading and B30's example lines (appendix) — the collapsible labels, and the exhibit prose. English survives only as quotation: the credit fields (candidate L8, L11, L15), the header strings (section 5), and the CSS bodies' own comments, which are code.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings).
- **Verify:** The pairs are diff.md's body sections in order; the residue pairs are the appendix lines.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** T4's row 66 records a Pattern 11 item for this theme: at localize time the prose at its L38 named the EN BHL theme page. In the current bytes that item does not stand as a live link: the corresponding prose (candidate L38) names Black Highlighter without any link, and a sweep of the candidate finds exactly one scp-wiki theme URL — the credit source link (candidate L15, recorded host, serves). The remaining links are the license-free prose links of the examples and the asset/delivery lines already accounted for in sections 3 and 4. The LINK-REPOINT block is a prose link inside the examples whose target was repointed to its JP form. The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) finds no unintended divergence; the recorded-host form is the only one present, so there was nothing to probe.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard. The ledger dispositions this theme's P11 in the same standing class; the bytes today are stronger than the disposition (no foreign prose link remains), and the package follows the bytes.
- **Verify:** `grep -n 'scp-wiki.wikidot.com' candidate.txt` — the source link only.
- **Disposition:** DISPOSITIONED (P11, GOSIGN2-LEDGER §(c3) line for this theme); the current bytes carry no live instance.

### 8. Structure

- **What:** The skeleton corresponds: gate, credit, prose, two code exhibits, tail components, two delivery modules. The 3 EXHIBIT-RESTRUCTURE primaries adjudicate as: (1) the street image-block (original L43–45 → candidate L47 onward) — the classifier's recorded false-fire shape, an include repoint inside an example block, its caption translated in the following lines; the include changed namespace, the block did not change structure. (2)–(3) The tail component includes (original L621–624 → candidate L616–619) changing namespace at the exhibits' exit — repoints, not restructures. Exhibit census: two exhibits on each side (the two own layers), no exhibit added, dropped, split, or merged. One genuine byte-level repair rides in residue B41: the original's malformed closer `[[/<]]` after the second exhibit (original L611) does not survive into the candidate.
- **Why:** R3 requires the census before a restructure is narrated; here the census shows correspondence plus one dropped malformation.
- **Verify:** `grep -n '\[\[code' original.txt candidate.txt` — two exhibits each; read original L610–612 against candidate L607 for the malformed closer.
- **Disposition:** Standing (correspondence established).

### 9. Formatting only

- **What:** None as its own class: the classifier finds no whitespace-only block and no re-indentation (0 and 0). The two exhibit-tail residue pairs (B39, B40 in the appendix) are alignment absorptions at the `[[/code]]` boundaries, counted there rather than here.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None by the porter. The candidate contains no 訳注 footnotes and no porter comment banner; the only `[!--` markers in the file are the theme's own SPC comment device at the tail (candidate L633, L637), carried over from the original (L634, L638) as part of its frame (section 3), not annotations. The port's judgments (the English headers, the kept EN assets) are not announced in the page — their record is the T4 row, the ledger line, and this package.
- **Why:** R2: porter-added text is part of the change record; its absence is stated, not assumed — and the theme's own comment device is not misread as one.
- **Verify:** `grep -n '\[!--' candidate.txt` — L633 and L637 only, the SPC device.
- **Disposition:** Standing (as an absence, stated).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's ten errors: hotlink ×8 — the EN-hosted assets of section 4, class (ii) (KB-58); pseudo-ref ×2 — the candidate's own draft-host local--code lines (section 3), class (ii). There is no class (i) error; the 1 warn / 1 info are recorded verbatim in T1-ROWS row 71 and are not classified. (2) The render row is this batch's cleanest: PASS-WITH-NOTES, "no candidate-specific blocking defect" — the machine lines are cross-cutting / draft-form / by-design, the interwiki priority=3 is confirmed correct, and the one theme-specific note is an observation, not a defect: the cornflower caption's contrast ratio of 2.56. No credit-modal line exists in this theme's row. (3) T4's three display-affecting items and their ledger dispositions (§(c3) line for this theme): the English headers in both variants — P9 DISPOSITIONED (ruling 2); the EN-hosted assets — P5 DISPOSITIONED (class (ii) / KB-58); the BHL-page link item — P11 DISPOSITIONED (and, per section 7, no live instance remains in the bytes). The theme's determination is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1 and 3); item 2 is a PASS-WITH-NOTES with an observation.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 71): exit 1, 10 errors / 1 warn / 1 info; the errors are hotlink ×8 and pseudo-ref ×2, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): PASS-WITH-NOTES — no candidate-specific blocking defect (section 11(2)); engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 66): FINDINGS jointly, display-affecting findings 3; the ledger §(c3) line records the theme's P5/P9/P11 outcomes as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +80/−83 in 46 change blocks; the GNU-diff count of the same pair is 131 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:borealis-constant-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 66; go-sign, COMPLETION-REPORT §10).

## Per-theme record

One wave-mechanical entry beyond the standing sections: commit a497307 (FIX4-MECH) removed a duplicated Noto Sans JP @import from this candidate (KB-65, duplicate-import removal across 29 themes). The stamp is computed against that commit, and the file today loads the supplement exactly once (section 4). Apart from the usage-example record below, the theme has no §(e) entry, and no FIX5 wave touched it.

### The usage example's posting name

The usage examples at candidate L29 and L36 as built named this theme by its plain slug on the JP branch, `:scp-jp:theme:borealis-constant-theme` — the second in its `|spc=--` parameter form — a page that does not exist on scp-jp, under the campaign's settled rule for usage examples (AGENTS.md §6). The usage-example population sweep has since completed both names to this candidate's posting name, `:scp-jp:theme:borealis-constant-theme-jp` (candidate L29 and L36, the second keeping its `|spc=--` parameter) (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), two of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-borealis-constant-theme-jp.txt` is the decoration sample the render checks ran against; it belongs to this theme's record but carries no port change of its own to explain here. The original-side sample `pages/theme-decoration-sample-borealis-constant-theme.txt` is the campaign's mirror-side fixture, likewise outside the port. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
