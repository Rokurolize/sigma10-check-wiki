# Review package — theme:jakstyle-jp (EN → JP port, production adoption)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:jakstyle-jp — origin EN, population #18 [GOSIGN2-LEDGER (b) row 18]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 619960f151f6f63aa550ada4b4480c3b39d4e124f00373cb6bd16d8e2feaa0c5); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 8 warns / 1 info (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 18; GOSIGN2-LEDGER (b) row 18]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 page no summary (baseline crash + webkit timeout), sample credit-modal + SP overflow 434–498px (rate widget far wider than column) + runtime-hotlink. [RENDER-ROWS-1 (RENDER-B row 18)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-B row 18)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 19, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 19]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 18]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:jakstyle-jp.txt sha256:619960f151f6f63aa550ada4b4480c3b39d4e124f00373cb6bd16d8e2feaa0c5; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 18) |
| Standing items | **DISPOSITIONED** — T4's P9 English header variables (ruling 2, section 5); the render row's coverage caveat (the page's T2 run returned no summary, section 12) and its sample items (KB-32/KB-40, section 11) |
| One text item carried, not hidden | T5 charged a display-visible typo in the usage prose （スペニット for スニペット, "snippet"). It is still in the candidate (candidate L52), because it is also in the production page this candidate mirrors: the production-drift column for this row reads 一致 (match), and correcting the production translator's text is a production-page edit, not a port change. Section 6 records it in place |
| Adoption standing | The production scp-jp page and this candidate agree (drift 一致）: the candidate is the production translation, reconciled and drift-incorporated, not a parallel re-port |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:jakstyle | theme:jakstyle-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo); the production counterpart theme:jakstyle exists on scp-jp |
| Reference revision | 327 (first-translation revision 305 / re-translation revision 327; the mirror is the later revision, and the candidate's credit block records both) | — |
| Source of this copy | Fresh fetch of the original at revision 327, 2026-11-17, via the mirror store (class FETCH-REGEN, hash-verified against review/sources.tsv) | Canonical file `pages/theme:jakstyle-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 829 lines / 22,718 bytes | 916 lines / 26,938 bytes |
| SHA-256 | 6f36265024a0ee3b02ee3b867a9a3ba4c07b8b9b46dbcfd5ff3c0d2fb22410c1 | 578d8f816d9dc9bf45316ecb8dfae13740ff80ac0b55a89e9c0db41026fa151e |

Provenance route (kind K6 in review/sources.tsv): the JP translation already existed on production scp-jp, made by a human translator (the credit block names KanekoLiku, 翻訳年 2023 — the SCP-JP staff member behind the Sigma-10 localization). The canonical candidate descends from that production page: canonical-sources import (commit d727e92), reconciliation to the live pair state (commit ffad285), exhibit escaping (commit 69c5894), the Phase 17 revision recording (commit 8dcac74, which also wrote `pages/phase17-diff-jakstyle-jp.txt`), the Phase 22 drift decision (commit d2a9dc0: the rev 305 → 327 upstream drift incorporated or decided, one of 13 such), and the gosign2 credit fixes (commits b816e10 and 5c32672, the stamp's canonical commit: FIX-CREDIT-C completed the translator/author pair in the rows 1–22 credit blocks). Most of what the diff shows is the production translation's work, adopted; the campaign's own deltas are the reconciliation chain and the credit fixes of section 1.

## Summary

The batch's largest diff by changed lines (+567/−480, 1,047 changed lines in 143 change blocks / 9 diff sections, Tier 2 format; the generator's difflib count with autojunk off), and the count needs its explanation up front: the candidate's exhibited CSS (700 lines) was assembled on the production line against an earlier original revision and only partially re-aligned when Phase 22 incorporated the rev 327 drift, so the exhibit delta is dominated by counted heuristic classes (49 CSS-BODY blocks, none of them font stacks; 13 RESTORATION blocks, candidate passages whose text matches the original's CSS at a different position) rather than by semantic changes a reviewer must judge one by one. The judged core is small and mostly at the head and tail: the BHL base repointed to the JP fork, a credit-module supplement in the head module, the credit block completed by the gosign2 credit fixes, the exhibits translated by the production translator, the English header variables kept under ruling 2, and one charged typo carried with its ground stated (Status table). T1 is nearly clean (one pseudo-ref, eight warns).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 143 change blocks — 31 specific (22%), 89 heuristic (62%), 23 residue (16%), 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| CSS-BODY | 49 |
| TRANS-UNANCHORED | 35 |
| TRANSLATION-ANCHORED | 16 |
| RESTORATION | 13 |
| T7-CREDIT-CSS | 5 |
| HEADERVAR | 2 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| IFTAGS | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudications applied for this README: the CSS-BODY mass is the code exhibit's re-emission delta between the production-line exhibit and the rev 327 mirror (verified: no font stack appears in any of the 49 blocks, so the standing P7 narration does not apply here); the RESTORATION blocks are reordered exhibit passages, per the classifier's own note that the added text matches the original's CSS elsewhere; the T7 blocks are the production line's credit-module CSS (section 1); the residue resolves by shape in the appendix. After adjudication no block is left unexplained, though the exhibit mass is explained as a class, not line by line — for an adoption, line identity with the mirror is not the standard the verdict rested on (section 12).

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:jakstyle-jp; original theme:jakstyle on scp-wiki at reference revision 327 (first-translation 305); candidate `pages/theme:jakstyle-jp.txt`. Provenance route: R4 adoption of the production translation, per the Provenance table's commit chain; drift 一致. The frame: the original opens with `[[iftags +theme]]` and a head module importing Black Highlighter from nu-scptheme.github.io. The candidate splits the gate the BHL way (a bare `[[iftags]]` wrapping the JP BHL theme include, candidate L1–3; the body gate `[[iftags +テーマ]]` at L5) and imports the base from the JP fork, adding one rule of its own to that head module (the credit-module supplement, section 1).
- **Why:** Section 0 declares the provenance route so the diff is read correctly: for this adoption the exhibit delta (Summary) is a provenance artefact first and a change list second.
- **Verify:** The sources.tsv row for jakstyle-jp (kind K6); `git log --follow -- pages/theme:jakstyle-jp.txt` for the seven-commit chain.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L16); its authorship lives in its prose and its license-area CSS. The candidate installs the JP credit block (`:scp-jp:credit:start-preview`/`end-preview`) in the production translator's form, completed by the gosign2 credit fixes: タイトル JAKSTYLE; 翻訳責任者 KanekoLiku (a human translator, kept under ruling 3's human-name rule); 翻訳年 2023; 著者 ©︎JakdragonX; 原題 JAKSTYLE; 著作権者 JakdragonX; 作成年 2021; 初訳時参照リビジョン 305; 改訳時参照リビジョン 327; 元記事リンク the scp-wiki original on the recorded host. T4 had charged two credit defects — the 元記事リンク field missing, and the 著者/著作権者 pair incomplete （著者≠著作権者） — and the ledger records them FIXED by the credit waves (FIX-CREDIT-C, commit 5c32672, is the completing commit for this row's pair); the bytes today show both fields present with the pair distinguished （著者 carrying the ©︎-marked name, 著作権者 the plain name). One residue of the adopted form remains, recorded as at isolated-terminal: the 元記事リンク's link text reads ソース rather than the title. The candidate also carries credit-module CSS the original does not have: a `.creditModule` centering rule in its head module (candidate L9–12) and further credit-area rules inside its code exhibit (the classifier's five T7-CREDIT-CSS blocks, candidate spans L344–361, L441–456, L873–879, L912–914 among them) — the production line's styling for the JP credit module, adopted with the page; the original styles only its license area.
- **Why:** P3/T1 for the form; ruling 3 for the fields, including the 著者/著作権者 distinction the FIX-CREDIT-C wave completed (the theme's author and its rights holder are recorded as separate fields where the source distinguishes them). T7: the JP credit module's geometry differs from the EN info module's, and the production page's supplement is the adopted answer.
- **Verify:** Read the candidate's credit block against the ten fields above; `grep -n 'creditModule' candidate.txt` — the head-module rule; the T1 fix commits are b816e10 and 5c32672.
- **Disposition:** FIXED (the charged P3 fields, GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** The candidate's includes are the JP BHL theme include (head gate), the interwiki-style frames, the credit pair (section 1), and the exhibit includes repointed to `:scp-jp:` forms. The internal-affairs candidate in this same batch shows what this base is worth downstream: theme:internal-affairs-jp imports this theme's production delivery at its priority 3 (recorded in that package's section 3), so this page's production standing is load-bearing beyond its own record. No foreign include survives in this candidate.
- **Why:** P1 (KB-15). Ruling 4 is not engaged.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live target is `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The base layers repoint from nu-scptheme.github.io to the JP fork (`scp-jp.github.io/Black-Highlighter/...`, candidate L7–8, with the interwiki frames following). The theme's own delivery sits at the tail, in the candidate's cluster of closing modules: a module importing its own /1 from the draft host (candidate L889) with the interwiki-style frame naming it (candidate L894) — the tail-frame arrangement this production line uses (the topology pass counts four small module-css components at the candidate's tail against the original's one). The original's own tail module framed its EN delivery the same way in miniature. The candidate's one T1 error is the pseudo-ref of these draft-host lines.
- **Why:** P4/T9 and P6/T3, in the adopted arrangement. The draft-host form is KB-41, class (iii).
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` — the fork sheets at the head, the draft-host pair at the tail.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** No asset lines and no font supplement are recorded for this theme: the candidate references no storage host at all (its only wdfiles lines are the draft-host delivery pair of section 3), so T1 records no hotlink error; and no JPFONT or FONT-IMPORT signature fires — in particular, the 49 CSS-BODY blocks contain no font stack (checked across all 49 blocks' text), so there is no hidden P7 mass in this diff. The theme's typography rides on the Black Highlighter base, as the original's does.
- **Why:** P5 satisfied vacuously (no foreign asset is referenced); P7 not engaged.
- **Verify:** `grep -n 'wdfiles\|fonts.googleapis' candidate.txt` — the delivery pair only.
- **Disposition:** None required.

### 5. Header, sidebar, and site furniture

- **What:** The header variables stay English: the candidate's `:root` carries the original's `--header-title` / `--header-subtitle` pair unchanged (HEADERVAR spans at candidate L184–185 and L201–202, inside the code exhibit; a third span at L59–61 is the same variables quoted in the usage exhibit). T4 charged the pair as display-affecting (pattern 9), and the ledger dispositions it under ruling 2: header and title language is out of scope for migration correctness. (The localize row cites the pair at L180–181; in the current candidate bytes they sit at L184–185, the row having been written against an earlier state of the file — the pair itself is unchanged.)
- **Why:** Ruling 2 governs; P9/T6 is otherwise not engaged.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — the exhibit quotation and the :root pair, both English, both identical to the original's.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3): P9 DISPOSITIONED).

### 6. Text translation

- **What:** The production translator's translation mass: 16 anchored blocks and 35 unanchored (the intro in the author's own voice, kept in register — the candidate's L46–48 preserves the original's first-person shrug about his own memory — the usage prose, and the element samples). One charged item stands unrepaired, on the record: T5 flagged スペニット (candidate L52: "このコードのスペニットをページの上に追加して") as a display-visible error for スニペット (snippet). It remains because the candidate mirrors the production page (drift 一致） and the word is the production translator's; the ledger's determination for this theme is PASS with no OPEN item, so the sweep absorbed the item into the adoption rather than charging the port with a production edit. This README records the word, its line, and its ground, so the next editor of the production page can fix it at the source.
- **Why:** P10 and KB-18, executed by the production translation and adopted under R4; the typo item is what the adoption rule costs in this instance, stated rather than smoothed over.
- **Verify:** `grep -n 'スペニット' candidate.txt` — the one line, L52.
- **Disposition:** Standing (the adopted translation); the typo item is recorded here and in the Status table.

### 7. Links

- **What:** The credit source link names the recorded host (scp-wiki.wikidot.com, with the link-text residue recorded in section 1). No prose link in the candidate was charged by the localize row, and no P11 item stands for this theme.
- **Why:** P11 satisfied by the adopted text.
- **Verify:** `grep -n 'wikidot.com' candidate.txt`.
- **Disposition:** Standing.

### 8. Structure

- **What:** The exhibit census is one-to-one at the page level (usage, samples, the code exhibit, the tail frames), and the structural story is inside the code exhibit: the candidate's exhibit runs 700 lines against the original's 658, assembled on the production line and drift-incorporated at Phase 22 (commit d2a9dc0) rather than re-derived from revision 327. The classifier's 13 RESTORATION blocks are the visible signature: candidate passages whose text matches the original's CSS at a different position — reordering and re-emission, not invented content (the classifier's own note on each such block says the supplement decides, and the supplement here is the provenance: the production exhibit's arrangement). No exhibit was dropped, and no rule family present in the original's exhibit is absent from the candidate's; what differs is arrangement and alignment, which is why the heuristic mass is counted and classed (Summary) instead of narrated line by line.
- **Why:** R3's adjudication for an adoption: the sanction question is answered by the provenance chain and the drift decision at Phase 22, which is the campaign's recorded act of bringing this exhibit to the rev 327 baseline.
- **Verify:** The topology components in classification.json (original code-css 658 lines at L160–818; candidate code-css 700 lines at L181–881); `git show d2a9dc0 --stat` for the drift incorporation.
- **Disposition:** Standing (the adopted exhibit, drift-incorporated).

### 9. Formatting only

- **What:** No whitespace-only class is recorded for this theme (the classifier's WS-ONLY count is 0); the exhibit's re-emission delta is counted under CSS-BODY and RESTORATION (sections 8 and the Class summary), not as formatting. The R7 follow-up-diff hazard is noted for the record: a future re-alignment of this exhibit would manufacture churn on the scale of this diff, and this package's counts are the baseline that makes such churn recognizable.
- **Why:** R7's disclosure, here a warning rather than a count.
- **Verify:** The classification's section 9 counts (WS-ONLY 0, re-indentation 0).
- **Disposition:** Standing (disclosed).

### 10. Porter annotations

- **What:** None in the candidate's text — checked, absent: no `[!-- ... --]` notes and no port provenance comment. The port's provenance lives in the credit block, the phase17-diff record, and this package.
- **Why:** R2: porter-added text is part of the change record; here the porter added none in-file.
- **Verify:** `grep -n 'SCP-JP port\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's one pseudo-ref error: the candidate's own draft-host local--code line (section 3), class (ii) posting-procedure; its eight warns are the checker's standing warnings for this file's shape, none charged as an error. There is no hotlink and no class (i) error. (2) T4's items: the P3 credit fields, FIXED (section 1); the P9 header pair, DISPOSITIONED under ruling 2 (section 5); the T5 typo, absorbed into the adoption (section 6). The stamp's display-affecting count for T4 is 0, consistent with those three outcomes. (3) The render row's items: the page's T2 run returned no summary (baseline crash plus a webkit timeout — a coverage caveat, section 12); the sample's credit-modal line is the preview-form property (KB-32), its SP overflow readings of 434–498px are the rate-widget shape recorded in the row (the widget rendering far wider than its column on the sample), and the runtime-hotlink is the environment layer (KB-40).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries; ruling 2), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1 and 3); item 2's parts are FIXED, DISPOSITIONED, and absorbed as stated.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 18): exit 1, 1 error / 8 warns / 1 info; the single error is the pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-B row 18): FINDINGS — the sample items of section 11(3), all dispositioned, and the page's T2 run returned no summary (baseline crash, webkit timeout), a coverage gap the ledger records as a caveat rather than a pass. (c) T4/T5 (LOCALIZE-ROWS row 19): FINDINGS jointly, display-affecting findings 0 after the outcomes in section 11(2); the row also confirms the prior Phase 22 repairs. The ledger §(c3) line records P3 FIXED and P9 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +567/−480 in 143 change blocks / 9 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, including the one gap.
- **Verify:** Re-run the checker on `pages/theme:jakstyle-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 18; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-SNIPPET — production-predecessor reference audit (landing 358955e).** `FIX-SNIPPET.md` records the self-reference at candidate L55 as DRIFT ground D1 (own code `@import`s under `theme%3Ajakstyle-jp`, the same delivery gsk imports as its base). Commit 358955e inserted `-jp` after the target, `theme:jakstyle` → `theme:jakstyle-jp`. The BHL exhibit at L54 is COHERENT ground C1 and was not touched. T1 before/after unchanged (1/0/1).

## Change set outside the two diffed files

The diff covers two files; this theme's record is three. `pages/phase17-diff-jakstyle-jp.txt` is the Phase 17 migration record for this theme (the revision recording of commit 8dcac74). `pages/theme-decoration-sample-jakstyle-jp.txt` is the decoration sample the render checks ran against (its credit-modal and overflow items are in section 11(3)). This candidate is also a change in another theme's record: theme:internal-affairs-jp's delivery imports this theme's production delivery (that package's section 3), a dependency created by this page's production standing, not by an edit to this file. The gosign2 credit commits (b816e10, 5c32672) touched the rows 1–44 and rows 1–22 files respectively in single waves; the other files are those themes' own records.

## Appendix — residue and low-signal blocks

Class M treatment: the residue and the exhibit mass collapse into this table rather than per-block slots.

| Block(s) | Shape | Resolution |
|---|---|---|
| B12, B18, B21, B53 (residue) | Single exhibit lines in the body (original L38/L64/L70/L144 → candidate L58/L84/L90/L166) whose text changed without tripping a signature | Part of section 6's translation mass, at lines the anchor test could not pair |
| B59–B62 cluster (residue) | The code exhibit's head region: original spans of 10/1/3/5 lines aligning to single candidate lines (original L171–193 → candidate L208–215) | The production exhibit compresses the original's :root preamble; part of section 8's re-emission class |
| Remaining residue (15 blocks) | Single-line and short alignment deltas inside the code exhibit and at its tail | The same re-emission class as CSS-BODY/RESTORATION; no content family is present here that is absent from the original's exhibit |
| CSS-BODY (49 blocks) | Heuristic code-body deltas across the exhibit; verified to contain no font stack | Section 8's counted class |
| RESTORATION (13 blocks) | Candidate passages matching the original's CSS at a different position | Reordering under the production arrangement; section 8 |

## License and attribution

- **Title:** JAKSTYLE
- **Author:** JakdragonX
- **Source:** https://scp-wiki.wikidot.com/theme:jakstyle — revision 327 (revision date 2026-10-27 14:13:30)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: KanekoLiku — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
