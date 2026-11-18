# Review package — theme:janitor-closet-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:janitor-closet-jp — origin EN, population #103 [GOSIGN2-LEDGER (b) row 103]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now cacf29771e1c117c36adf4ccca65c1ad8e26999559f983e69f3032aad49ef5f3); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 93; GOSIGN2-LEDGER (b) row 103]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow everywhere incl. 1683px@1366, 806px@768, 350–419px@≤375 both engines; runtime-hotlink incl. scp-wiki.wikidot.com; WebKit CC "S". [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 103, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 103]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 103]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:janitor-closet-jp.txt sha256:cacf29771e1c117c36adf4ccca65c1ad8e26999559f983e69f3032aad49ef5f3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 103) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 (the EN-storage asset set, class (ii) / KB-58, section 4); T4's P9 English masthead (ruling 2, section 5); the render row's cross-cutting items (KB-33/34/36/40, section 11) |
| Wave repairs inside this record | The license box was restored by FIX4-LICENSE (commit c2a8bee, KB-63, the stamp's canonical commit); the attribution normalization is FIX-CREDIT-D's (commit 1869877). Both predate the verdict, so the stamp is a plain PASS |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:janitor-closet | theme:janitor-closet-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 8 (first translation; the candidate's credit block records 初訳時参照リビジョン: 8) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-janitor-closet.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:janitor-closet-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 520 lines / 9,646 bytes | 503 lines / 10,563 bytes |
| SHA-256 | 2a69637f9b8d07c56e79e3c39ac02b6ffcc47bd4ba8f06c3a5c31d92a0b1b03 | e37274a8450bba3e18c394ffce3f0a8f0f144e69d2ff9a80aa41bd7003f192ea |

Wave history: the candidate was created by the Stage 2 EN12 integration (commit 7604057, the LOCALIZE-S2-B wave's port), normalized by FIX-CREDIT-D (commit 1869877), and repaired by FIX4-LICENSE (commit c2a8bee: license-box furniture restored in 7 themes, KB-63 — the license box of section 1). No FIX5 commit touches this file.

## Summary

A small, playful EN theme whose port is the standard shape with two wave repairs inside it. Measured churn (diff.md, Tier 1 format; the generator's difflib count with autojunk off: +140/−162, 302 changed lines in 67 change blocks, presented as 17 hunks). The semantic core: the info-module credit demo gives way to the JP credit block, the license box is restored in its JP backend form (FIX4-LICENSE), five font stacks gain a Noto Sans JP supplement in place (section 4), the exhibits translate (17 anchored + 28 unanchored blocks), and two kept EN items are dispositioned: the three asset lines on EN storage (section 4) and the English masthead (section 5). The render row's page-overflow readings are the largest in this batch (up to 1683px at 1366) and are still the recorded cross-cutting families, not a candidate defect (section 11).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 67 change blocks — 39 specific (58%), 27 heuristic (40%), 1 residue (1%), 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 28 |
| TRANSLATION-ANCHORED | 17 |
| WS-ONLY | 9 |
| JPFONT-STACK | 5 |
| SELF-DELIVERY | 3 |
| INFO-DEL | 2 |
| LICENSE-BOX | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: the one residue block is a heading translation (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:janitor-closet-jp; original theme:janitor-closet on scp-wiki at reference revision 8; candidate `pages/theme:janitor-closet-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart). The frame is the standard candidate form: a head module importing the candidate's own delivery, the interwiki-style frame, and the tag gate `[[iftags +theme]]` localized to `+テーマ`.
- **Why:** Section 0 declares the provenance route; the gate tag is P2 and the frame is P6 (section 3).
- **Verify:** The sources.tsv row for janitor-closet-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is the EN info-module demo (`:scp-wiki:info:start` at original L12, with its companion lines) and a license box at its tail (`license-box-theme`, original L496–515, parameterless in the mirror). The candidate deletes the info demo (the classifier's two INFO-DEL blocks) and installs the JP credit block (`:scp-jp:credit:start-preview`/`end-preview`) with the eight ruling-3 fields: タイトル Janitor's Closet Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Janitor's Closet Theme; 著作権者 winkwonkboi; 作成年 2025; 初訳時参照リビジョン 8; 元記事リンク the scp-wiki original, on the recorded host. The author field was checked against the original's credit: its intro prose names the maker ("the Janitor's Closet Theme made by winkwonkboi", original L20), and no second creator appears — the field drops nobody. The license box stands at the candidate's tail in its JP backend form (`license-box-backend`, candidate L486–493) — restored by FIX4-LICENSE (KB-63) after an earlier wave's candidate had lost the furniture, the same restoration internal-affairs in this batch received. The theme carries no credit-module CSS of its own; credit styling is inherited.
- **Why:** P3/T1 with KB-09 for the demo's deletion (the preview credit module is the rate-bearing JP form). Ruling 3 fixes the credit fields. KB-63 records the license-box restoration class.
- **Verify:** Read candidate L1–11 (the credit block) and L486–493 against original L496–515; `grep -n 'info:start' candidate.txt` returns nothing.
- **Disposition:** FIXED (the license box, FIX4-LICENSE at c2a8bee, inside the verdict's bytes; the credit swap is the standing P3 form).

### 2. Includes and components

- **What:** The candidate's includes are the credit pair (section 1), the interwiki-style frame (section 3), the license-box pair (section 1), and the exhibit includes repointed to `:scp-jp:` forms (the image-block at candidate L24 among them; its `name=` asset stays on EN storage, section 4). No foreign include survives.
- **Why:** P1 (KB-15). Ruling 4 is not engaged.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every target is `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The standard candidate form: the head module imports the candidate's own `local--code/theme%3Ajanitor-closet-jp/1` from the draft host, and the interwiki-style frame names the same /1 delivery (the classifier's SELF-DELIVERY and DRAFT-HOST spans at the head). The original's own delivery lines are replaced by these; nothing else in the delivery layer changes.
- **Why:** P4/T9 and P6/T3. The draft-host form is KB-41, class (iii), and it is T1's one pseudo-ref error for this theme.
- **Verify:** `grep -n 'local--code' candidate.txt` — the head pair, both draft host.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts (five JPFONT-STACK blocks, the in-stack supplement form): the candidate appends `"Noto Sans JP"` to five of the theme's font stacks, keeping the retained Latin face first — `"Patua One", serif` → `"Patua One", "Noto Sans JP", serif` (original L181 → candidate L175), `"Afacad Flux"` twice (L189 → L183; L327 → L321), and `"Source Serif 4"` twice (L312 → L306; L341 → L335). The supplement is uniform (Noto Sans JP in every stack, serif stacks included), which is the wave's standard form: the JP face is the fallback for Japanese glyphs in every stack that can meet them. No separate JP font load is added; the stacks name a face the Sigma-10 environment loads. Assets: three lines stay on EN storage, and they are exactly T1's hotlink×3 — the exhibit image `173canon.jpg` (candidate L24, in the image-block's `name=`), the page background `bg.jpg` (candidate L159), and the header logo `lightlogo.png` (candidate L164), all `scp-wiki.wdfiles.com/local--files/theme%3Ajanitor-closet/`.
- **Why:** P7/T5 with KB-16 for the stacks (the original's stacks are Latin-only, so Japanese text falls back to a default face without the supplement). The assets are P5/KB-17 territory dispositioned instead: class (ii), KB-58 — re-hosting is a posting-procedure step and the files serve from the original's storage today.
- **Verify:** `grep -n 'scp-wiki.wdfiles' candidate.txt` — the three lines above; `grep -n 'Noto Sans JP' candidate.txt` — the five stack lines.
- **Disposition:** Font supplement applied; the three asset lines DISPOSITIONED (class (ii) / KB-58, GOSIGN2-LEDGER §(c3): P5 DISPOSITIONED).

### 5. Header, sidebar, and site furniture

- **What:** The candidate sets no `--header-title` or `--header-subtitle` variable (verified by grep on both files — the theme has none to translate). T4's P9 item for this theme is its English masthead strings, display-affecting in the rendered page: the theme's masthead is its logo image and header styling rather than a variable pair, and the strings a reader sees there stay English. The disposition is ruling 2: header and title language is translation taste, out of scope for migration correctness.
- **Why:** Ruling 2 governs the masthead; P9/T6 is otherwise not engaged in the file.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt original.txt` returns nothing on either side — the absence is the point: there is no variable line to point at, and the item lives in the rendered masthead.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3): P9 DISPOSITIONED).

### 6. Text translation

- **What:** The exhibit translation mass: 17 anchored blocks and 28 unanchored (the intro — "これは winkwonkboi が、Cleanliness Guaranteed* シリーズ配下のページのために作った…" at candidate L16, keeping the series name in English as a proper noun — the usage prose, and the element samples), plus the residue block's heading (Examples → 例， appendix). The CSS comments are the author's own, carried as porter-facing text.
- **Why:** P10 and KB-18 (reader-visible strings).
- **Verify:** The exhibit pairs are diff.md's hunks in order; read candidate L14–60 against the original's corresponding exhibits.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link names the recorded host (scp-wiki.wikidot.com, candidate L11). No prose link in the candidate was charged by the localize row, and no P11 item stands for this theme; the intro's series reference is a name, not a link.
- **Why:** P11 satisfied.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit link.
- **Disposition:** Standing.

### 8. Structure

- **What:** No structural change: the exhibit census is one-to-one in the same order, the classifier records no EXHIBIT-RESTRUCTURE block, and the only deletions are the credit furniture of section 1 (the info demo out, the credit block in, the license box restored at the tail where the original keeps its own). Variable names and selectors are preserved.
- **Why:** R3 satisfied by the census; no sanction question arises.
- **Verify:** Compare the exhibit sequences (`grep -n '^+\|^\[\[div\|^\[\[code' original.txt candidate.txt`).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** 9 whitespace-only blocks, small blank-line deltas around the exhibits and the credit area. No re-indentation class is recorded. The count is disclosed so a follow-up diff's padding churn is recognizable against it (R7).
- **Why:** R7: formatting churn is disclosed as its own class.
- **Verify:** The classification's section 9 counts (WS-ONLY 9, re-indentation 0).
- **Disposition:** Standing (disclosed; no semantic content).

### 10. Porter annotations

- **What:** None — checked, absent. The candidate carries no `[!-- ... --]` notes and no port provenance comment.
- **Why:** R2: porter-added text is part of the change record; here the porter added none in-file.
- **Verify:** `grep -n 'SCP-JP port\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three hotlink errors and one pseudo-ref: the hotlinks are the asset set of section 4, class (ii) / KB-58; the pseudo-ref is the candidate's own draft-host local--code line (section 3), class (ii) posting-procedure. There is no class (i) error. (2) T4's two display-affecting findings: the P5 assets (the same three lines) and the P9 masthead (section 5), both dispositioned in the ledger. (3) The render row's items, all cross-cutting, not charged to the candidate: page-overflow at every width, including 1683px@1366, 806px@768, and 350–419px at ≤375 in both engines (KB-33/KB-34: the static credit replica's fixed width and the preview chrome — the readings are the batch's largest because the replica's fixed width is compared against this theme's narrow content column, and the lane recorded the shape, not a candidate rule, as the cause); the runtime-hotlink observation including scp-wiki.wikidot.com (KB-40: the runtime hosts arrive via the shared site theme chain); and the WebKit CC "S" glyph (KB-36).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries; ruling 2), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 93): exit 1, 4 errors / 1 warn / 1 info; three hotlink (the section 4 assets) and one pseudo-ref, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN12)): FINDINGS, the items of section 11(3), all dispositioned; engine coverage full matrix as run by the lane; no credit-modal line is recorded for this theme. (c) T4/T5 (LOCALIZE-ROWS row 103): FINDINGS jointly, display-affecting findings 2 (the P5 assets; the P9 masthead), and no unincorporated upstream updates; the ledger §(c3) line records both as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +140/−162 in 67 change blocks, presented as 17 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:janitor-closet-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 103; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-janitor-closet-jp.txt` is the decoration sample the render checks ran against (its overflow readings are in section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The FIX4-LICENSE commit (c2a8bee) touched 7 license restorations plus its other items, and FIX-CREDIT-D (1869877) touched 163 files; the other files in both waves are those themes' own records, not this one's change set. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## Appendix — residue and low-signal blocks

Class M treatment: the residue collapses into this table rather than per-block slots.

| Block(s) | Shape | Resolution |
|---|---|---|
| B8 (residue) | One heading line: `+ Examples` → `+ 例` (original L30 → candidate L26) | A section heading translated （例 is the standard short form for "Examples" in this page's heading style); it belongs to section 6's mass |

## License and attribution

- **Title:** Janitor's Closet Theme
- **Author:** winkwonkboi
- **Source:** https://scp-wiki.wikidot.com/theme:janitor-closet — revision 8
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
