# Review package — theme:it-pillar-of-industry-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:it-pillar-of-industry-jp — origin KO, population #268 [GOSIGN2-LEDGER (b) row 268]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9960df257c0a45c0c29f26d2ca26074a5003a946677521cf18251e561834e8d1); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 287; GOSIGN2-LEDGER (b) row 268]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 267, source LOCALIZE-S2-F]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 267]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 268]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:it-pillar-of-industry-jp.txt sha256:9960df257c0a45c0c29f26d2ca26074a5003a946677521cf18251e561834e8d1; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 268) |
| Standing items | **DISPOSITIONED** — the render row's cross-cutting items only (KB-40 environment layer; the sample's preview-form credit modal, KB-32; its 884px@768 overflow, KB-33/KB-34, section 11) |
| Notable record | This is one of the 19 themes whose localize row is a clean PASS: T4 and T5 both PASS with zero display-affecting findings (LOCALIZE-ROWS row 267). No repair wave after the port touched this file except the campaign-wide attribution normalization |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:it-pillar-of-industry | theme:it-pillar-of-industry-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 21 (first translation; the candidate's credit block records 初訳時参照リビジョン: 21) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-it-pillar-of-industry.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:it-pillar-of-industry-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 594 lines / 11,131 bytes | 597 lines / 11,750 bytes |
| SHA-256 | c84514ae6d1ff51e99e83d9ff27f7f5b9b4f3c37dfa4f3d5bdf5d6ee26c18b2 | a27735e830ae75199b3da79e7efaf2087e001c6e39e2a435930c1883aefe9410 |

Wave history: the candidate was created by the Stage 2 KO4 integration (commit 56b9d1a, the LOCALIZE-S2-F wave's port; the file also appears in the earlier canonical-sources and Phase 6 imports and the EN21 integration's tree, which carried the composition, not this port) and has exactly one later commit, 1869877 (FIX-CREDIT-D: the campaign-wide translator-attribution normalization, 163 files). No FIX5 commit touches this file.

## Summary

The smallest diff in this batch (+40/−42, 82 changed lines in 20 change blocks, presented as 3 hunks, Tier 1 format; the generator's difflib count with autojunk off). The original is a compact KO theme that already delivers by local--code and already exhibits its code, so the port is mostly a change of hosts and language: the delivery repoints from scpko to the candidate's own draft-host storage, the theme's four images are re-hosted onto that same storage, the bare Rate and the info-module demo give way to the credit block, and the KO prose translates. Nothing else needed doing, and the record agrees: T4/T5 PASS outright, and T1's only errors are the six pseudo-refs of the draft-host lines themselves.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 20 change blocks — 16 specific (80%), 4 heuristic (20%), 0 residue, 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DRAFT-HOST | 7 |
| TRANS-UNANCHORED | 8 |
| TRANSLATION-ANCHORED | 5 |
| DELIVERY-HOST | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| COMMENT-TEXT | 1 |
| ESCAPED-INCLUDE | 1 |
| IFTAGS | 1 |
| INFO-DEL | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

(The DRAFT-HOST count exceeds the block rows it shares because the label fires per line group inside the delivery and asset blocks; the per-section text gives the line-level truth.) After adjudication no block is left unexplained, and there is no residue to append.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:it-pillar-of-industry-jp; original theme:it-pillar-of-industry on scpko at reference revision 21; candidate `pages/theme:it-pillar-of-industry-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart). The frame is the simple KO form on both sides: a head module importing the theme's own local--code delivery (original L1–3), the interwiki-style frame at priority 1, and the tag gate (`[[iftags +테마]]`, original L10) localized to `+テーマ` in the candidate.
- **Why:** Section 0 declares the provenance route; the gate tag is P2 and the delivery repoint is P4 (section 3).
- **Verify:** The sources.tsv row for it-pillar-of-industry-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L16) followed by the KO info-module demo (`[[include info:start]]` with its placeholder prose, original L21–23). The candidate deletes both (the INFO-DEL block covers the demo lines) and installs the JP credit block (`:scp-jp:credit:start-preview`/`end-preview`, at the same head position) with the eight ruling-3 fields: タイトル IT産業の担い手 CSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 IT 산업역군 CSS 테마; 著作権者 c_bonefish, Denevola; 作成年 2022; 初訳時参照リビジョン 21; 元記事リンク the scpko original, on the recorded host. The author field names both of the theme's authors; the original carries its attribution through its info module (external content, not in the mirror) and no in-file text in the mirror contradicts the pair — the check basis is stated because the info module's own text is not part of this package's evidence. There is no license box on either side, and the theme carries no credit-module CSS (its credit styling is inherited).
- **Why:** P3/T1 with KB-09 (the preview credit module is the rate-bearing JP form; the bare Rate and the EN-style info demo would duplicate and foreign-frame it). Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read the credit block against the eight fields.
- **Disposition:** Standing (the standard form, checker-verified in the sweep; T4's row for this theme is a clean PASS).

### 2. Includes and components

- **What:** The candidate's includes are the credit pair (section 1), the interwiki-style frame (section 3), and the exhibit includes: the image-block exhibit (unprefixed `component:image-block` in both files; its asset is re-hosted, section 4) and one escaped include inside the usage exhibit (block B8, original/candidate L27–28: the include snippet a user copies, repointed to the candidate's own page in its escaped display form). The original's unprefixed `info:start` include is deleted with its demo (section 1). No foreign include survives.
- **Why:** P1 (KB-15). Ruling 4 is not engaged.
- **Verify:** `grep -n '\[\[include' candidate.txt`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** No channel conversion: the original already delivers its own CSS by local--code (original L2 imports `scpko.wikidot.com/local--code/theme%3Ait-pillar-of-industry/1`) with the interwiki-style frame naming the same /1 at priority 1 (original L5–8). The candidate repoints both lines to its own delivery on the draft host (candidate L2 and L7, `sigma10-jp-test.wdfiles.com/local--code/theme%3Ait-pillar-of-industry-jp/1`). These two lines, with the four asset lines of section 4, are the candidate's draft-host set, and they are T1's six pseudo-ref errors.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the supplement frame, kept at the original's priority). The draft-host form is KB-41, class (iii).
- **Verify:** `grep -n 'local--code' candidate.txt` — the two lines above, both draft host.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: there is nothing to do, and the bytes prove it — `font-family` occurs zero times in both files. The theme declares no font stacks of its own; its typography is inherited from the Sigma base, so no JP load and no stack rewrite exists, and T4's clean PASS covers the point. Assets: the theme's four images are re-hosted onto the candidate's own draft-host storage (the kwangheung set: logo1 in the image-block exhibit at candidate L33 and again in the CSS at L583, the background at L78, logo3 at L84, logo2 at L588 — all `sigma10-jp-test.wdfiles.com/local--files/theme%3Ait-pillar-of-industry-jp/`). The original served the same images from its KO storage. No EN or KO storage URL survives in the candidate, which is why T1 records no hotlink error for this theme.
- **Why:** P5/T8 (assets served from JP-side storage) executed as a draft-host re-host, the candidate-set's standing form before posting; P7 not engaged (no stacks exist to rewrite).
- **Verify:** `grep -n 'wdfiles' candidate.txt` — every hit is the draft host; `grep -c 'font-family' original.txt candidate.txt` — 0 and 0.
- **Disposition:** Applied (re-hosted to the draft host; the posting step moves them with the page, class (iii) form).

### 5. Header, sidebar, and site furniture

- **What:** None: the candidate sets no `--header-title`, `--header-subtitle`, or `--logo-image` (verified by grep on both files), its header imagery is the re-hosted kwangheung set (section 4), and T4 recorded no P9 item for this theme.
- **Why:** P9/T6 not engaged.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle\|--logo-image' candidate.txt original.txt` returns nothing.
- **Disposition:** None required.

### 6. Text translation

- **What:** The KO→JP translation mass: 5 anchored blocks and 8 unanchored (the intro and usage prose, the element samples — the footnote sound-effect sample among them, 똑똑 → コンコン, block B14 — and the link exhibit's heading, block B13: `+ Link` → `+ リンク`, which the classifier labels LINK-REPOINT for its line shape; it is a heading translation, and the exhibit's link targets were localized with it). One comment-text block (B16) sits at the code exhibit's head. The mass is small because the theme's page is mostly its code exhibit, which is not prose.
- **Why:** P10 and KB-18 (reader-visible strings).
- **Verify:** The exhibit pairs are diff.md's three hunks in order.
- **Disposition:** Standing (the port itself; T5 PASS).

### 7. Links

- **What:** The credit source link names the recorded host (scpko.wikidot.com). The usage exhibit's links were localized inside section 6's blocks; no prose link in the candidate targets a foreign page, and the localize row records no P11 item for this theme.
- **Why:** P11 satisfied; nothing kept, nothing red.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit link only, outside the code exhibit's comments.
- **Disposition:** Standing.

### 8. Structure

- **What:** No structural change: the exhibit census is one-to-one (usage, element samples, the code exhibit in the same order), the classifier records no EXHIBIT-RESTRUCTURE block, and the code body is carried with its selectors and variables intact (533 lines in the original's exhibit, 536 in the candidate's, the delta being the head lines of sections 3–4). The only deletions are the credit furniture of section 1.
- **Why:** R3 satisfied by the census; nothing was dropped or replaced, so no sanction question arises.
- **Verify:** Compare the exhibit sequences (`grep -n '^+\|^\[\[div\|^\[\[code' original.txt candidate.txt`).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None: the classifier finds no whitespace-only block and no re-indentation (0 and 0). The two files' near-equal lengths (594 → 597 lines) match that reading.
- **Why:** R7's disclosure, here a null result.
- **Verify:** The classification's section 9 counts (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked, absent. The candidate carries no `[!-- ... --]` notes and no port provenance comment; its one comment-text block is the code exhibit's own head comment, carried from the original.
- **Why:** R2: porter-added text is part of the change record; here the porter added none in-file.
- **Verify:** `grep -n 'SCP-JP port\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Two items, each with its ground. (1) T1's six pseudo-ref errors: the candidate's own draft-host lines (the two delivery lines of section 3 and the four asset lines of section 4), class (ii) posting-procedure. There is no hotlink error and no class (i) error. (2) The render row's items, all cross-cutting, not charged to the candidate: the page side records only the runtime-hotlink site-theme chain (KB-40, environment layer); the sample side records the preview-form credit modal (KB-32: credit:start-preview has no modal mechanism, the 2026-11-16 ruling's preview-form property) and an 884px@768 page-overflow reading (KB-33/KB-34); the lane's T3 walk found nothing beyond the cross-cutting items.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–2).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 287): exit 1, 6 errors / 1 warn / 1 info; all six errors are pseudo-ref (the draft-host lines), class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO4)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane; the sample's credit-modal line is recorded and dispositioned as the preview-form property in the stamp above. (c) T4/T5 (LOCALIZE-ROWS row 267): PASS and PASS, display-affecting findings 0 — one of the sweep's 19 clean localize rows. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +40/−42 in 20 change blocks, presented as 3 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:it-pillar-of-industry-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 268; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-it-pillar-of-industry-jp.txt` is the decoration sample the render checks ran against (its credit-modal and overflow items are in section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The FIX-CREDIT-D commit (1869877) that normalized this candidate's attribution touched 163 files in one wave; the other 162 are those themes' own records, not this one's change set. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** IT 산업역군 CSS 테마
- **Author:** c_bonefish, Denevola
- **Source:** https://scpko.wikidot.com/theme:it-pillar-of-industry — revision 21
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
