# Review package — theme:lampeter-warm-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:lampeter-warm-jp — origin EN, population #105 [GOSIGN2-LEDGER (b) row 105]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now e0f86df535f9af48865800c44fdc2887acd17fec74955197ab0d24f6e0302261); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 95; GOSIGN2-LEDGER (b) row 105]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page T2 no machine verdict (exit 2, networkidle, no summary); sample credit-modal (preview-form), sample overflow 576–583px@320/375, runtime-hotlink site-theme chain; T3 sample notice left-clip ≤375, broken lampeterlogo.png (deferred asset). [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 105, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 105]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 105]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:lampeter-warm-jp.txt sha256:e0f86df535f9af48865800c44fdc2887acd17fec74955197ab0d24f6e0302261; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 105) |
| Standing items | **DISPOSITIONED** — T4's P1 sigma-plus include form (posting-procedure convention class; the form itself was unified by FIX4-SIGMA, section 2) and P11 EN component links (sibling / batch-posting class, section 7); the render row's coverage caveat (the page's T2 run returned no machine verdict, section 12), its preview-form credit modal (KB-32), and the deferred logo asset (section 4) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:lampeter-warm | theme:lampeter-warm-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 41 (first translation; the candidate's credit block records 初訳時参照リビジョン: 41) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-lampeter-warm.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:lampeter-warm-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 962 lines / 27,598 bytes | 957 lines / 29,736 bytes |
| SHA-256 | fdd5bbba8d28a46b69a12b94708a46b9b47a8f5aee4b5d2d | 22a63dac9f31513718ce965556a86e80b4f421b29af958b07b04953d06a597ca |

Wave history: the candidate was created by the Stage 2 EN13 integration (commit d7c1af6, the LOCALIZE-S2-B wave's port), normalized by FIX-CREDIT-D (commit 1869877), and repaired by FIX4-SIGMA (commit 1cdad38, the stamp's canonical commit: the sigma-plus include form unified to component:sigma-plus-jp across 8 themes, 9 lines). No FIX5 commit touches this file.

## Summary

A Sigma Plus-based warm variant whose port turns on its base component: the theme is an include of Sigma Plus with its own layer over it, so the port's first line is the story (section 2). Measured churn (diff.md, Tier 1 format; the generator's difflib count with autojunk off: +149/−161, 310 changed lines in 70 change blocks, presented as 7 hunks). The semantic core: the sigma-plus include takes its unified JP form (FIX4-SIGMA), the bare Rate gives way to the credit block, the license box stands in its JP backend form with both file records translated, the retained Latin faces are re-loaded from Google Fonts with a Noto Sans JP load added and the header stack supplemented (section 4), the logo is re-hosted to the candidate's own draft-host storage (where its file is a deferred asset, section 4), and the exhibits translate (15 anchored + 40 unanchored blocks). T1's six errors are all pseudo-refs of the draft-host lines; there are no hotlinks.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 70 change blocks — 29 specific (41%), 39 heuristic (56%), 2 residue (3%), 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 40 |
| TRANSLATION-ANCHORED | 15 |
| DRAFT-HOST | 5 |
| FONT-IMPORT | 3 |
| LICENSE-BOX | 2 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| ESCAPED-INCLUDE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| SIGMA-PLUS-JP | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: the one CSS-BODY block is a P7 font-stack supplement (section 4); the two residue blocks resolve in the appendix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:lampeter-warm-jp; original theme:lampeter-warm on scp-wiki at reference revision 41; candidate `pages/theme:lampeter-warm-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart). The frame is this theme's defining feature: line 1 of both files is the Sigma Plus include (the theme is a variant layer over that component), ahead of the standard head module, interwiki frame, and the tag gate localized to `+テーマ`.
- **Why:** Section 0 declares the provenance route and puts the base include where a reviewer will look for it; the include's form is section 2's subject and P1's.
- **Verify:** The sources.tsv row for lampeter-warm-jp; `sed -n '1p' original.txt candidate.txt`.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L16), its CSS banner ("By HaydenSaintPascal", original L156), and a license box at its tail (`license-box-theme`, original L920–960) whose records name HaydenSaintPascal as the author of both image files. The candidate deletes the bare Rate and installs the JP credit block (`:scp-jp:credit:start-preview`/`end-preview`) with the eight ruling-3 fields: タイトル ランピーター テーマ（ウォーム）; 翻訳責任者 AI; 翻訳年 2026; 原題 Lampeter Theme (Warm); 著作権者 [[*user HaydenSaintPascal]]; 作成年 2025; 初訳時参照リビジョン 41; 元記事リンク the scp-wiki original, on the recorded host. The author field was checked against the original's credit: the banner and both license records name HaydenSaintPascal alone — the field (which carries him as a user link) drops nobody. The license box stands in its JP backend form (`license-box-backend |author=HaydenSaintPascal`, candidate L931–955) with both file records translated （ファイル名 lampeterlogo.png （原語版： Lampeterlogo) and lampeterlayer0.png; 作者 [[*user HaydenSaintPascal]]; ライセンス CC BY-SA 3.0, its license link localized to the deed.ja text). The theme carries no credit-module CSS of its own; credit styling arrives with the Sigma Plus base.
- **Why:** P3/T1 with KB-09 for the Rate. Ruling 3 fixes the credit fields. The license records are part of the attribution surface and translate with it (the file names keep their original forms, with the original-language name noted where it differs).
- **Verify:** Read the candidate's credit block against the eight fields; read candidate L931–955 against original L920–960.
- **Disposition:** Standing (the standard form, checker-verified in the sweep).

### 2. Includes and components

- **What:** The first line is the port's most consequential include: `:scp-wiki:component:sigma-plus` → `component:sigma-plus-jp` (original L1 → candidate L1, the classifier's SIGMA-PLUS-JP and COMPONENT-SWAP blocks). This theme is a Sigma Plus variant, so its base is a component, and the JP form is the component's own port candidate — the form FIX4-SIGMA (commit 1cdad38) unified across the 8 themes that include it, after T4 had charged the earlier form as a P1 blocker ("posting-blocking; same class as Space row 40"): an include naming a page that would not exist at posting blocks the post, and the unified form names the component candidate that will. The ledger dispositions the item as the posting-procedure convention class, the fix being the convention itself. The remaining includes are the credit pair (section 1), the license-box pair (section 1), the interwiki-style frame (section 3), and the exhibit includes repointed to `:scp-jp:` or the unprefixed component forms (the image-block at candidate L38). One escaped include inside the usage exhibit is repointed with the rest (the ESCAPED-INCLUDE block).
- **Why:** P1 (KB-15) and ruling 4 in its standing form: a theme that needs a component includes that component's JP port candidate, and the include's name must be the candidate's posting name. The FIX4-SIGMA unification is the campaign learning this once and applying it to all 8 themes at once.
- **Verify:** `sed -n '1p' candidate.txt`; `git show 1cdad38 --stat` for the 8-theme unification.
- **Disposition:** DISPOSITIONED (the P1 item, posting-procedure convention class, GOSIGN2-LEDGER §(c3)) — with the unified form itself inside the verdict's bytes at 1cdad38.

### 3. Delivery and code loading

- **What:** The candidate's own delivery is the standard form: the head module imports its own `local--code/theme%3Alampeter-warm-jp/1` from the draft host and the interwiki-style frame names the same /1 (the SELF-DELIVERY and DRAFT-HOST spans at the head; five DRAFT-HOST blocks in all, the rest being the logo lines of section 4). The Sigma Plus base's delivery arrives through the section 2 include, as the original's does.
- **Why:** P4/T9 and P6/T3. The draft-host form is KB-41, class (iii), and the draft-host set is T1's six pseudo-ref errors.
- **Verify:** `grep -n 'local--code' candidate.txt` — the head pair, both draft host.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts (three FONT-IMPORT blocks and one CSS-BODY block): the candidate loads its faces from Google Fonts at the code exhibit's head — the retained Latin faces (Special Elite; Crimson Text; Martian Mono, candidate L168–172) and an added Noto Sans JP load (candidate L175) — and supplements the header stack in place: `--header-font: "Special Elite", serif` → `"Special Elite", "Noto Serif JP", serif` (original L226–228 → candidate L237–239, the CSS-BODY block, a P7 supplement under a heuristic label). Assets: the theme's logo is re-hosted to the candidate's own draft-host storage in both its uses (the image-block exhibit at candidate L38 and the `--sp_header-logo` variable at candidate L185, both `sigma10-jp-test.wdfiles.com/local--files/theme%3Alampeter-warm-jp/lampeterlogo.png`; the original served it from the EN wiki's page-files URL). The re-host is nominal today: the file itself is not on the draft host yet, so the render lane's T3 walk saw the logo broken and recorded it as a deferred asset — the posting-time asset class, in which the URL is right and the bytes arrive with the post. The second licensed file (lampeterlayer0.png, section 1's record) is a CSS-layer image named in the license records; it carries no separate delivery line in the candidate beyond the theme's own code.
- **Why:** P7/T5 with KB-16 for the fonts (the retained faces are display faces for Latin; Japanese text needs the JP faces loaded and named). The logo is P5/T8 in its deferred form (KB-58's family): the re-host target is correct and recorded, and the asset's arrival is a posting step, which is why the ledger carries the T3 observation as a disposition rather than a defect.
- **Verify:** `grep -n 'fonts.googleapis\|lampeterlogo' candidate.txt` — the four loads and the two logo lines.
- **Disposition:** Fonts applied; the logo DISPOSITIONED (deferred asset, posting-time class).

### 5. Header, sidebar, and site furniture

- **What:** The header furniture arrives with the Sigma Plus base and the theme's own layer; the candidate's furniture-adjacent change is the `--sp_header-logo` variable of section 4. T4 recorded no P9 item for this theme. The render row's furniture observations (the sample's notice left-clip at ≤375) are the preview chrome family, recorded in section 11.
- **Why:** P9/T6 not engaged in the file.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — no masthead variable pair is set by this theme on either side.
- **Disposition:** None required.

### 6. Text translation

- **What:** The exhibit translation mass: 15 anchored blocks and 40 unanchored (the intro — including the sentence naming the theme's bases, whose links are section 7's subject — the usage prose, and the element samples). The unanchored share is the expected shape for this page's long, link-bearing prose; each block was read against the mirror for this README. The license records' labels translate in section 1.
- **Why:** P10 and KB-18 (reader-visible strings).
- **Verify:** The exhibit pairs are diff.md's hunks in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The intro's two component links are kept in their EN full-URL form, without JP routing or annotation (candidate L34): `[[[https://scp-wiki.wikidot.com/component:sigma-plus|Sigma Plus]]]` and `[[[https://scp-wiki.wikidot.com/component:toggle-sidebar|トグル式サイドバー]]]`. That is T4's P11 item for this theme, and its disposition is the sibling / batch-posting class: the links name the EN component pages as their subjects (the sentence says what the theme is built on), and the operative include was repointed in section 2 — the prose link is documentation, not delivery. The contrast with internal-affairs in this batch (whose EN prose links carry （英語版） annotations) is real and is recorded rather than harmonized: the two waves annotated differently, and the ledger's disposition covers this theme's form. The credit source link names the recorded host (scp-wiki.wikidot.com, candidate L10 of the credit block).
- **Why:** P11, with the disposition's ground as stated: subject-naming prose links to components whose JP candidates are included, not linked, in the port.
- **Verify:** `sed -n '34p' candidate.txt` — the two links on one line.
- **Disposition:** DISPOSITIONED (sibling / batch-posting class, GOSIGN2-LEDGER §(c3): P11 DISPOSITIONED).

### 8. Structure

- **What:** No structural change: the exhibit census is one-to-one in the same order, the classifier records no EXHIBIT-RESTRUCTURE block, and the only deletion at the head is a single `[[/div]]` closer the original carried in its pre-credit furniture (residue block B5, original L11, appendix) — the candidate's head area was rebuilt around the credit block, and the closer's element does not exist in the candidate's arrangement. Variable names and selectors are preserved, including the Sigma Plus `--sp_` prefixed set the base defines.
- **Why:** R3's adjudication: the census decides, and the one unmatched closer is accounted for as part of the head rebuild rather than an exhibit loss.
- **Verify:** Compare the exhibit sequences (`grep -n '^+\|^\[\[div\|^\[\[code' original.txt candidate.txt`).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a class of its own: the classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here there is none to disclose.
- **Verify:** The classification's section 9 counts (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked, absent. The candidate carries no `[!-- ... --]` notes and no port provenance comment.
- **Why:** R2: porter-added text is part of the change record; here the porter added none in-file.
- **Verify:** `grep -n 'SCP-JP port\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's six pseudo-ref errors: the candidate's own draft-host lines (the delivery pair of section 3 and the logo lines of section 4), class (ii) posting-procedure. There is no hotlink error and no class (i) error. (2) T4's two display-affecting findings: the P1 sigma-plus form (section 2, dispositioned as the convention class, with the unified form in the bytes) and the P11 component links (section 7, sibling / batch-posting class). (3) The render row's items: the page's T2 run returned no machine verdict (exit 2, networkidle — a coverage caveat, section 12); the sample's credit-modal line is the preview-form property (KB-32); its overflow readings of 576–583px at 320/375 and the runtime-hotlink chain are the cross-cutting families (KB-33/KB-34, KB-40); and the T3 walk's two sample observations are the notice left-clip at ≤375 (KB-34) and the broken lampeterlogo.png (the deferred asset of section 4).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 95): exit 1, 6 errors / 1 warn / 1 info; all six errors are pseudo-ref (the draft-host lines), class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN13)): FINDINGS — the page's T2 run returned no machine verdict (exit 2, networkidle, no summary), a coverage gap recorded as a caveat; the sample side carries the items of section 11(3), all dispositioned, including the T3 walk's notice clip and deferred-asset observations; the sample's credit-modal line is recorded and dispositioned as the preview-form property in the stamp above. (c) T4/T5 (LOCALIZE-ROWS row 105): FINDINGS jointly, display-affecting findings 2 (the P1 sigma-plus form; the P11 component links), and no unincorporated upstream updates; the ledger §(c3) line records both as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +149/−161 in 70 change blocks, presented as 7 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, including the one gap.
- **Verify:** Re-run the checker on `pages/theme:lampeter-warm-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 105; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-lampeter-warm-jp.txt` is the decoration sample the render checks ran against (its credit-modal, overflow, and T3 items are in section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. Two wave commits reach beyond this file: FIX4-SIGMA (1cdad38) unified the sigma-plus form across 8 themes, and the sigma-plus component candidate itself (`component:sigma-plus-jp`) is the port this theme's first line depends on — both are those records' own change sets, named here because this theme's posting depends on them. FIX-CREDIT-D (1869877) touched 163 files in one wave; the other 162 are those themes' own records.

## Appendix — residue and low-signal blocks

Class M treatment: the residue collapses into this table rather than per-block slots.

| Block(s) | Shape | Resolution |
|---|---|---|
| B5 (residue) | One removed line: a `[[/div]]` closer at original L11, in the head furniture ahead of the credit area | The candidate's head was rebuilt around the credit block and the closer's element has no counterpart there; section 8 |
| B57 (residue) | One empty alignment span at original L152 / candidate L160, where the body channel meets the code-css channel | No content |

## License and attribution

- **Title:** Lampeter Theme (Warm)
- **Author:** HaydenSaintPascal
- **Source:** https://scp-wiki.wikidot.com/theme:lampeter-warm — revision 41
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
