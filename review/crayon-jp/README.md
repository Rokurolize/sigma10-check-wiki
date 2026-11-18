# Review package — theme:crayon-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:crayon-jp — origin EN, population #74 [GOSIGN2-LEDGER (b) row 74]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 1ec09486f8d7a9e624e9cdb393184759c08d109b40776c7a9057ef71e31e145f); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 64; GOSIGN2-LEDGER (b) row 74]
- T2/T3 (render, combined verdict): PASS-WITH-NOTES — [combined T2/T3] report `NO candidate-specific defect established` — error cluster is a transient 503 capture; other lines cross-cutting/draft-form/by-design. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 74, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 74]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 74]
- Computed against: canonical commit 1c96ee4f6dbe58243d8c4ba0136a4a4dde806972; candidate file pages/theme:crayon-jp.txt sha256:1ec09486f8d7a9e624e9cdb393184759c08d109b40776c7a9057ef71e31e145f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 74) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (draft-host asset lines, section 11); P7 no JP-capable header font (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:crayon | theme:crayon-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 16 (first translation; the candidate's credit block records 初訳時参照リビジョン: 16) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-crayon.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:crayon-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 49 lines / 1,250 bytes | 66 lines / 1905 bytes |
| SHA-256 | bbcd1e2c9ee9731e325110bc2e6061aa380df160ac2c1116a21748fcc427f143 | ade98a0a571eabb542a2e13d7e14786314333d39c2033551c02091c00eb244f3 |

Wave history: the candidate was created by the Stage 2 EN6 integration (commit 240c3d2) and has exactly one later commit, 666f543 (FIX2-CREDIT, credit-missing-fields completions over 36 themes), which is the commit that completed this file's credit fields (section 1). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. The original has been superseded upstream since revision 16; the follow-up diff artifact `diff-crayon-from16.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

The smallest package in this batch: a 49-line variant theme (the 2021 April Fool's "Subpar Creative Products" theme) whose entire CSS is one inline `[[module CSS]]` block with two background images and one font stack. The port translates the page's prose, repoints the usage include and the font load, moves the two asset URLs to the candidate's own folder on the draft host, and rebuilds the tail furniture: the original's EN license-box include is replaced by the JP credit block with all eight ruling-3 fields, the JP license box in backend form with its two entries translated, and the interwiki-style frame the frame waves added. Measured churn (diff.md, the generator's count: +37/−20 in 11 change blocks / 2 hunks). Nothing in the original was dropped: the license entries survive translated, and the theme's only exhibit (the usage syntax line) survives repointed.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 11 change blocks — 7 specific (63.6%), 3 heuristic (27.3%), 1 residue (9.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| IFTAGS | 3 |
| TRANS-UNANCHORED | 4 |
| DRAFT-HOST | 3 |
| INCLUDE-REPOINT | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the 1 residue block is a one-word label translation (section 6); the 3 heuristic blocks are one-line prose translations (section 6); the 2 EXHIBIT-RESTRUCTURE primaries are the tail furniture swap (frame + credit + license box, sections 1 and 3), not dropped or replaced exhibits — the exhibit census is one usage syntax line, present on both sides (section 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:crayon-jp; original theme:crayon on scp-wiki at reference revision 16; candidate `pages/theme:crayon-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN6 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame placement differs from the head-frame form: the original opens with its hidden rating div gated by `[[iftags -theme]]` (original L1), and the candidate keeps that order (candidate L1, tag localized) and places the added frame include at the tail, ahead of the credit gate (candidate L37–40; section 3).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for crayon-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture is the tail block inside `[[iftags +theme]]` (original L37–48): an EN `:scp-wiki:component:license-box-theme` include carrying `author=stormbreath and UncertaintyCrossing`, and two license entries (scribblebody_bg.png by stormbreath; scribble-logo.png by UncertaintyCrossing; both CC BY-SA 3.0). The candidate replaces that block (blocks B10–B11) with the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L44–53) carrying all eight ruling-3 fields (title Crayon Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Crayon Theme; 著作権者 [[*user stormbreath]]・[[*user UncertaintyCrossing]]; 作成年 2021; 初訳時参照リビジョン 16; the source link, section 7), followed by the JP license box (candidate L55–65: `:scp-jp:component:license-box-backend` with the same author parameter, the two entries translated, `:scp-jp:component:license-box-end`). At the T4 measurement the credit block was missing six of the eight required fields (LOCALIZE-ROWS row 74); the fields were completed by FIX2-CREDIT (commit 666f543), which is this file's last commit and the stamp's computed-against commit. The page's own rating block at the head (`[[>]]` **評価:** `[[module Rate]]` `[[/>]]`, candidate L2–5) is carried over unchanged from the original; no Rate-class finding stands against this theme in any record (the T1 baseline codes are pseudo-ref×2 only).
- **Why:** P3/T1 for the preview credit block (the rate-bearing JP form) and T4 for the license box in its JP backend form — the original had a license box, so this is a form swap, not the KB-63 dropped-box shape. Ruling 3 fixes the eight fields; the missing-fields state the T4 lane measured is exactly the credit-missing-fields class the credit waves were charged with.
- **Verify:** Read candidate L44–65 against the eight fields and the original's two entries; `git log -- pages/theme:crayon-jp.txt` shows 666f543 as the completing commit.
- **Disposition:** FIXED (credit fields, FIX2-CREDIT; frame, section 3). The source-link field is verified in section 7.

### 2. Includes and components

- **What:** One repoint in the body and the tail swap of section 1. B5: the usage example's escaped include, `:scp-wiki:theme:crayon` → `:scp-jp:theme:crayon` as built (candidate L11, inside `@@...@@`); as built the repoint kept the original's slug, naming a page that does not exist on scp-jp, and the population sweep has since completed the name to `:scp-jp:theme:crayon-jp` (per-theme record). The tail includes are the frame (section 3), the credit pair, and the license-box pair (section 1). Every include in the candidate names a `:scp-jp:` target; there are no other includes.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp, and the escaped usage example is repointed on the same rule, because the snippet a user pastes must name the JP theme page — as built it named the original's slug on the JP branch, a page that does not exist, and the population sweep's completion of the name is what brings the snippet under this rule. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — six includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The theme's CSS is self-contained: one inline `[[module CSS show="true"]]` block (original L15–34 → candidate L15–34, position and form unchanged). The candidate adds the frame the original lacked (LOCALIZE-ROWS row 74: interwiki-style absent (P6)): an interwiki-style include at candidate L37–40 with `priority=1` and `theme=` naming the candidate's own `local--code/theme%3Acrayon-jp/1` on the draft host (sigma10-jp-test.wdfiles.com). **Frame paragraph (the M-frame addition):** the frame is the single-layer own-code form — priority 1 is the theme's own layer, and there are no priority 2/3 layers because the theme imports no base distribution; its one CSS module is the /1 delivery the frame names. The include sits at the tail, ahead of the credit gate, rather than at the head; the ledger records the outcome as P6 FIXED (frame waves; checker-verified).
- **Why:** P6/T3 (the interwiki-style supplement frame): every candidate carries the frame so its own code delivery is named in the JP layering convention, even when, as here, the CSS also sits inline. The draft-host form of the theme= URL is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** Read candidate L37–40; `grep -n 'interwiki-style' original.txt` returns nothing.
- **Disposition:** FIXED (P6, frame waves); the draft-host URL is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Font load (block B7): the `@import` inside the CSS module moves from `fonts.bunny.net` to `fonts.googleapis.com`, family and parameters unchanged (`family=Permanent+Marker&display=swap`, candidate L16). Assets (blocks B8–B9, DRAFT-HOST): the two background images move from `scp-wiki.wdfiles.com/local--files/theme%3Acrayon/` to `sigma10-jp-test.wdfiles.com/local--files/theme%3Acrayon-jp/`, file names unchanged (scribblebody_bg.png, candidate L19; scribble-logo.png, candidate L23). The font stack that consumes the load (`'Permanent Marker', cursive`, candidate L28) is unchanged, and no JP font is added anywhere (no JPFONT-LOAD fired; see section 11 for the P7 disposition).
- **Why:** P5 with KB-17 (asset and font hosts): bunny.net is outside the sanctioned hotlink set (storage, Google Fonts, BootstrapCDN, cdnjs), so the load is repointed to Google Fonts with its parameter form intact — a host repoint, not a KB-04 malformation repair (the family parameter is well-formed on both sides). The two images are the theme's own files, re-hosted to the candidate's own folder; at draft stage that folder sits on the draft host (KB-41).
- **Verify:** `grep -n 'fonts\.\|wdfiles' candidate.txt` — three lines, matching the list above.
- **Disposition:** Font repoint applied; the draft-host asset URLs are DISPOSITIONED (class (iii) draft form; posting rewrites them to the production host).

### 5. Header, sidebar, and site furniture

- **What:** None. The candidate overrides no header variable (no `--header-title`, `--header-subtitle`, or `--logo-image`); the header keeps the original's background-image form with the repointed logo asset (section 4) and the original's two header rules. The theme has no sidebar or topbar rules of its own.
- **Why:** P9/T6 is a per-theme judgment, not a universal supplement; this variant theme's identity is its background and logotype, both carried, and no JP furniture adaptation was needed.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 6. Text translation

- **What:** All of the page's prose is translated, in four counted groups. The residue block B2: the rating label `**Rating:**` → `**評価:**` (candidate L3). The three heuristic TRANS-UNANCHORED blocks, each a one-line translation verified against the mirror: B3, the variant-theme sentence (candidate L7; the incident name "Subpar Creative Products" is kept as a quoted proper name); B4, the usage instruction (candidate L9); B6, the header credit line (candidate L13; the two author names are kept, the labels are translated). The tail's two license entries are translated inside B11 (candidate L57–63: ファイル名/作者/ライセンス), with the authors named in plain text there and in linked `[[*user]]` form in the credit block (section 1). English survives only as proper names: the theme title in the credit fields, the incident name, and the author names. There are no CSS `content:` strings and no CSS comments in this theme.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored and residue groups are where a silent deletion would hide, which is why each was read individually rather than waved through as a class.
- **Verify:** The pairs are diff.md's two hunks in order; an English-prose scan of candidate.txt returns only the proper names listed above.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the named proper names.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L52): `https://scp-wiki.wikidot.com/theme:crayon`. That is the original's recorded host — review/sources.tsv records the original at scp-wiki.wikidot.com, the same host the mirror was taken from — so the link names the serving original and no host defect arises. The usage include is exhibit text (section 2). No other prose links exist in the candidate.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; here the recorded host and the link agree, which is the check the jiha package's finding taught this batch to run on every theme.
- **Verify:** Compare candidate L52's host against the sources.tsv row's original_url host (scp-wiki.wikidot.com) — identical.
- **Disposition:** Standing; no defect flag.

### 8. Structure

- **What:** The localize.md closing rule holds. The page's two regions keep their order and form: the hidden rating div with its inline CSS module, then the iftags-gated tail furniture; the JP additions are the frame include placed ahead of the gate and the credit/license swap inside it (sections 1 and 3). The classifier's two EXHIBIT-RESTRUCTURE primaries (B10, B11) adjudicate to that tail swap: an exhibit census finds exactly one exhibit on each side, the usage syntax line (original L11 → candidate L11, repointed), present in the same position — nothing was dropped or replaced, so the R3 question (sanctioned replacement vs silent deletion) does not arise for this theme.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[module\|\[\[include\|\[\[iftags' original.txt candidate.txt` — the sequences correspond one to one, with the frame include the only addition.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no `[!-- --]` translator notes and no CSS comments at all (the theme's CSS module contains no comment lines on either side).
- **Why:** R2: porter-added text is part of the change record; here the check was run explicitly and the answer is none, not an oversight.
- **Verify:** `grep -n '\[!--\|/\*' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Two items, each with its ground. (1) T1's two pseudo-ref errors: the candidate's two draft-host asset lines (candidate L19, L23; section 4) — class (iii) draft-wiki form, DISPOSITIONED in register c1 (pseudo-ref standing class: references in draft form are rewritten to scp-jp at posting, never "fixed" in the candidate). (2) P7, no JP-capable header font: the header stack names only the Latin display face 'Permanent Marker' (candidate L28), and the T4 lane recorded the gap as minor; the ledger's outcome is DISPOSITIONED (GOSIGN2-LEDGER §(c3): recorded without a display-affecting mark; T4 bar). The theme's logotype face is a Latin display face by design, and no wave added a JP face to this stack. The T2/T3 row's error cluster is a transient 503 capture (KB-44 family), recorded as not-charged. The K5a-i note of the Provenance section (original superseded upstream since rev 16) is a follow-up-diff matter (KB-19), not a defect in this port.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–2).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 64): exit 1, 2 errors / 1 warn / 1 info; both errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A (EN6)): PASS-WITH-NOTES on both pages — no candidate-specific defect established; the error cluster is a transient 503 capture. (c) T4/T5 (LOCALIZE-ROWS row 74): FINDINGS jointly, display-affecting findings 2 — at measurement, the credit block's missing fields and the absent frame; both are since FIXED (fields by FIX2-CREDIT 666f543; frame per §(c3) P6 FIXED, frame waves), and P7 is dispositioned (section 11). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +37/−20 in 11 change blocks / 2 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:crayon-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 74; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The theme's only exhibit, the usage syntax line at candidate L11, as built named this theme by its original's slug on the JP branch, `:scp-jp:theme:crayon` — a page that does not exist on scp-jp, under the campaign's settled rule for usage examples (AGENTS.md §6). The usage-example population sweep has since completed the name to this candidate's posting name, `:scp-jp:theme:crayon-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724). This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.


### Post-package repairs (REFRESH3-D)

Two post-package landings are in the recopy (built at `5c04bbe`, before both); the candidate went 66 → 60 lines.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Acrayon-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L32.
- **FIX-RATES — head-zone bare Rate removed** (report `R/review-scout/FIX-RATES.md`; landing `1c96ee4f6dbe58243d8c4ba0136a4a4dde806972`, 2026-11-17): the five-line head-zone exhibit (`[[>]]`, `**評価:**`, `[[module Rate]]`, `[[/>]]` and its blank line) directly under the opening `[[div]]` was deleted, leaving the rate-bearing preview credit module as the sole rating widget (AGENTS.md §5). The original has no frame, no `theme=` and no local--code reference at all (FIX-FRAMEADDR §2 worked example, verified).

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Appendix — residue blocks

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B2 | 3-3 → 3-3 (body → body) | residue, no signature | One-word label translation, `**Rating:**` → `**評価:**`; section 6 |
| B3 | 7-7 → 7-7 (body → body) | heuristic TRANS-UNANCHORED | One-line prose translation (variant-theme sentence); section 6 |
| B4 | 9-9 → 9-9 (body → body) | heuristic TRANS-UNANCHORED | One-line prose translation (usage instruction); section 6 |
| B6 | 13-13 → 13-13 (body → body) | heuristic TRANS-UNANCHORED | One-line credit-line translation, author names kept; section 6 |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-crayon-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Crayon Theme
- **Author:** stormbreath・UncertaintyCrossing
- **Source:** https://scp-wiki.wikidot.com/theme:crayon — revision 16
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
