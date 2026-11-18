# Review package — theme:isolated-terminal-jp (EN → JP port, production adoption)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:isolated-terminal-jp — origin EN, population #17 [GOSIGN2-LEDGER (b) row 17]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 667482550a6e0789984acfaf7cdb973234d63d70e60705452a4d503f54395ac2); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 2 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 17; GOSIGN2-LEDGER (b) row 17]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample lower half blank white (possible stale-cache, not a defect), T2 sample incomplete (exit 2, no summary), runtime-hotlink; page credit modal opens. [RENDER-ROWS-1 (RENDER-B row 17)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-B row 17)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 18, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 18]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 17]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:isolated-terminal-jp.txt sha256:667482550a6e0789984acfaf7cdb973234d63d70e60705452a4d503f54395ac2; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 17) |
| Standing items | **DISPOSITIONED** — T4's P9 Latin masthead (ruling 2, section 5); the render row's coverage caveat (the sample's T2 run returned no machine verdict, section 12) and its stale-cache observation, recorded as not a defect |
| Adoption standing | The production scp-jp page and this candidate agree (the /start production-drift column for this row reads 一致, match): the candidate is the production translation, reconciled into the canonical repo, not a parallel re-port |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:isolated-terminal | theme:isolated-terminal-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo); the production counterpart theme:isolated-terminal exists on scp-jp |
| Reference revision | 122 (first-edition revision 121 / re-translation revision 122; the mirror is the later revision, and the candidate's credit block records both) | — |
| Source of this copy | Fresh fetch of the original at revision 122, 2026-11-17, via the mirror store (class FETCH-REGEN, hash-verified against review/sources.tsv) | Canonical file `pages/theme:isolated-terminal-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 716 lines / 21,808 bytes | 852 lines / 29,348 bytes |
| SHA-256 | b92ff4338aa6891a51b47f6ca70ba3d8e70ce5baeb1f2a6b9b47a8f5aee4b5d2d | 298eeb9faa06f59869c4a91939f973d9a55fb4cf1ada6b6752ae2ce272ef8e58 |

Provenance route (this theme is kind K5b-5+K6 in review/sources.tsv, and its history differs from a wave port): the JP translation already existed on production scp-jp, made by a human translator (the credit block names oplax-counterpoint, 翻訳年 2024, revised against original revision 122). The canonical candidate descends from that production page: the repo history is the canonical-sources import (commit d727e92), the reconciliation to the live pair state (commit ffad285), the Phase 17 revision recording (commit 8dcac74, which also wrote the small migration record `pages/phase17-diff-isolated-terminal-jp.txt`), and the gosign2 T1 credit fixes (commit b816e10, the stamp's canonical commit). Most of what the diff shows is therefore the human translation's work, adopted; the campaign's own deltas are the reconciliation and the credit-field fixes of section 1. The migration is delivered in two files: this candidate and the phase17-diff record named above.

## Summary

A Black Highlighter terminal theme whose original delivers part of its CSS as attached files on its own wiki storage, and whose JP form re-hosts those files onto JP storage with JP dot fonts substituted. Measured churn (diff.md, Tier 2 format; the generator's difflib count with autojunk off: +264/−128, 392 changed lines in 100 change blocks / 10 diff sections). The semantic core: the BHL base repointed to the JP fork (section 3); the credit demonstration pair collapsed to the JP credit form, with the campaign's T1 wave fixing the charged credit-field defects (section 1); the attached-file fonts re-hosted to scp-jp-storage and the stacks rewritten around them (section 4); one feature integration (S-CSS-P) removed with its reason recorded in a porter comment inside the CSS (sections 8 and 10); the exhibits translated by the human translator (section 6); and the Latin masthead kept under ruling 2 (section 5). T1 is the cleanest in this batch: two pseudo-ref errors and nothing else, because this candidate's assets were actually re-hosted.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 100 change blocks — 51 specific (51%), 45 heuristic (45%), 4 residue (4%), 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 42 |
| TRANSLATION-ANCHORED | 19 |
| WS-ONLY | 12 |
| EXHIBIT-RESTRUCTURE | 6 |
| CSS-BODY | 6 |
| INCLUDE-REPOINT | 6 |
| DELIVERY-HOST | 5 |
| ASSET-REHOST | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| INFO-DEL | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudications applied for this README: the six CSS-BODY blocks are P7 font-stack rewrites and one measured value change (section 4 and the appendix); the six EXHIBIT-RESTRUCTURE blocks are include repoints and the credit-area rebuild (section 8's census); one residue block is the S-CSS-P removal with its porter comment, promoted to sections 8 and 10 because it is a real change, not noise. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:isolated-terminal-jp; original theme:isolated-terminal on scp-wiki at reference revision 122 (first-edition 121); candidate `pages/theme:isolated-terminal-jp.txt`. Provenance route: R4 adoption — a production JP translation existed (human translator, 2024, revised against rev 122) and was adopted and reconciled, per the Provenance table's commit chain; the production-drift check reads 一致 (match), so candidate and production page are the same text. The frame: the original opens with `[[iftags +theme]]` and a head module importing Black Highlighter from nu-scptheme.github.io. The candidate splits the gate the BHL way (a bare `[[iftags]]` wrapping the JP BHL theme include, candidate L1–3, then the body gate `[[iftags +テーマ]]` at L5) and imports the base from the JP fork (candidate L6–9).
- **Why:** Section 0 declares the provenance route so the diff is read correctly: for an adoption, the baseline question is not "what did the wave change" but "what does the adopted translation do, and what did the campaign itself change on top" — the campaign's own commits are named in the Provenance table, and section 1 separates its credit fixes from the translator's text.
- **Verify:** The sources.tsv row for isolated-terminal-jp (kind K5b-5+K6); `git log --follow -- pages/theme:isolated-terminal-jp.txt` for the four-commit chain.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a demonstration pair: a right-aligned block with the labels **Rating:** over a bare `[[module Rate]]` and **Rating w/ Credit Module:** over the EN info module demo (`:scp-wiki:info:start` / `info:more` with placeholder prose, original L18–27). The candidate collapses the pair to the JP form alone: the translated label **クレジット付き評価モジュール** (candidate L21–23) heads the credit block (`:scp-jp:credit:start-preview`/`end-preview`, candidate L24–35), the plain-Rate demo and the info demo lines are deleted (the classifier's INFO-DEL block, original spans L22–23 and L26–27), and no bare Rate remains. The credit block is the human translator's, kept in his form: タイトル Isolated Terminal Theme; 翻訳責任者 oplax-counterpoint (a human name, kept under ruling 3's rule for human translators); 翻訳年 2024; 原題； 著作権者 EstrellaYoshte, Woedenaz; 作成年 2021; 初訳時参照リビジョン 121; 改訳時参照リビジョン 122; 元記事リンク the scp-wiki original on the recorded host. The author field names both of the theme's authors; the original carries its own attribution through the external info module (its content is not in the mirror), and nothing in the mirror contradicts the pair. The campaign's own credit work on this file is the gosign2 T1 fix (commit b816e10): T4 had charged two field defects — the タイトル field missing, and the source link malformed (a `ソース` field in place of a well-formed 元記事リンク） — and the ledger records both FIXED by the credit waves, checker-verified. The bytes today show the fix and its residue honestly: the タイトル field is present and the 元記事リンク field exists with the correct URL, but the block also retains the translator's redundant **ソース：** field line duplicating that URL, and the 元記事リンク's link text reads ソース rather than the title. The charged defects (missing title, missing well-formed source field) are fixed; the redundancy is cosmetic residue of the adopted human form, recorded here rather than silently normalized away, because this block is a human translator's credit and the campaign's adoption rule preserves it.
- **Why:** P3/T1 for the form (the JP credit module replaces both demo forms; KB-09's duplicate rule is satisfied by collapsing the pair). Ruling 3 for the fields, including its human-translator clause: campaign translations credit AI, human translations keep their names — oplax-counterpoint's credit is data about the production page's history, not a campaign claim.
- **Verify:** Read candidate L21–35 against original L18–27; the T1 fix commit is b816e10 (`git show b816e10 -- pages/theme:isolated-terminal-jp.txt` shows the field repairs).
- **Disposition:** FIXED (the charged P3 fields, GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Six INCLUDE-REPOINT blocks: the BHL theme include and interwiki-style frames repointed to `:scp-jp:` (head, section 3), the credit pair (section 1), the image-block exhibit (its include unprefixed in both files, its asset re-hosted, section 4), and one escaped include exhibit repointed inside the usage text (block B16, original L57–59 → candidate L65–67). The EN info module includes are deleted, not repointed (section 1). No foreign include survives.
- **Why:** P1 (KB-15). Ruling 4 is not engaged.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live target is `:scp-jp:` or the unprefixed component form the original itself used.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** Two delivery stories. The base: the original imports Black Highlighter's two sheets from nu-scptheme.github.io (original L4–5) and frames them with interwiki-style layers; the candidate imports the same sheets from the JP fork (`scp-jp.github.io/Black-Highlighter/...`, candidate L7–8) under the same frame shape (five DELIVERY-HOST blocks cover the head and tail frame lines). The theme's own layer: the original's page tail frames its own EN local--code /1 (original L711–715); the candidate's tail frames its own /1 on the draft host (candidate L825–831). The theme's attached-file CSS (the font attachments) is section 4's story: those imports live inside the code body, not the head.
- **Why:** P4/T9 and P6/T3, in the adopted translation's own arrangement (the translator rebuilt the base delivery on the JP fork; the campaign's reconciliation kept it). The draft-host form of the candidate's own lines is KB-41, class (iii) — and these two lines are T1's two pseudo-ref errors, the candidate's only T1 errors.
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` — the fork sheets and the one draft-host pair.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** This theme's fonts ARE its assets: the original's code body imports three attached font stylesheets from its own EN storage (original L228–230: terminus.css, profontwindows.css, vga8.css, all `scp-wiki.wdfiles.com/local--files/theme:isolated-terminal/`). The candidate re-hosts the set onto JP storage (block B74, candidate L301–304): four imports from `scp-jp-storage.wdfiles.com/local--files/file:9042763-*/` — JFDotShinonomeMing16.css, profontwindows.css, terminus.css, and jiskan24.css — so two of the original's attachments survive by name, vga8.css is replaced by two JP dot-font sheets (Shinonome and Jiskan, the JP counterparts for the terminal aesthetic), and a Noto Sans JP load is added from Google Fonts (candidate L308, JPFONT-LOAD). The stacks follow (the CSS-BODY blocks B77–B78, P7 rewrites under a heuristic label): `--body-font: 'terminus_ttfmedium', sans-serif` → `'Terminus', 'Noto Sans JP', sans-serif`, and `--UI-font` gains `'jiskan24h'`. The one image asset is also re-hosted (block B17): the pxlogo.png exhibit moves from the EN storage to `scp-jp-storage.wdfiles.com/local--files/file:9042763-10-4g1r/pxlogo.png` (candidate L71), and the BHL logo image at the head moves to the draft host (candidate L38). Nothing in this candidate hotlinks the EN wiki — which is why T1 records no hotlink error here, the only such candidate in this batch.
- **Why:** P5/T8 done in full (KB-17's re-hosting actually performed, because this adoption came through the production line where the files were posted to JP storage), and P7/T5 for the stacks: the terminal faces are the theme's identity, and the JP dot fonts are their functional counterparts, not a generic substitution.
- **Verify:** `grep -n 'wdfiles' candidate.txt` — every hit is scp-jp-storage or the draft host; `grep -n 'scp-wiki.wdfiles' candidate.txt` returns nothing.
- **Disposition:** Applied (re-hosted); no asset disposition needed.

### 5. Header, sidebar, and site furniture

- **What:** The masthead stays Latin: the candidate carries `--header-title: "SCP FOUNDATION"` verbatim (candidate L330, from original L260). T4 charged it as display-affecting (a Latin site name rendered on every JP page using the theme), and the ledger dispositions it under ruling 2: header and title language is out of scope for migration correctness. The theme's remaining furniture (its terminal chrome) is the original's CSS carried in the code body.
- **Why:** Ruling 2 governs; P9/T6 is otherwise not engaged.
- **Verify:** `grep -n -- '--header-title' candidate.txt` — the one line above, identical to the original's.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3): P9 DISPOSITIONED).

### 6. Text translation

- **What:** The human translator's translation mass, adopted: 19 anchored blocks and 42 unanchored (the usage prose, the element samples — "How quaint." → なんとも奇妙な。 among them — and the customization guidance, including the highlighted recommendation whose `{{...}}` markup becomes a `hilighter` span in the JP form, block B65). The unanchored share is high because this prose was translated as prose, not line-aligned; each block was read against the mirror for this README. One exhibit separator was added (residue block B19: a `-----` rule line at candidate L75 with no original counterpart — a translator's layout choice inside the exhibits, recorded in the appendix).
- **Why:** P10 and KB-18 (reader-visible strings), executed by the production translation and adopted under R4.
- **Verify:** The exhibit pairs are diff.md's body sections in order.
- **Disposition:** Standing (the adopted translation itself).

### 7. Links

- **What:** The credit source link names the recorded host (scp-wiki.wikidot.com, candidate L35, with the link-text residue recorded in section 1). No prose link in the candidate was flagged by the localize row, and the exhibit links were carried by the translation; the theme's own page links are the delivery and credit lines already covered.
- **Why:** P11 satisfied by the adopted text; nothing to repoint remained after the credit fix.
- **Verify:** `grep -n 'wikidot.com' candidate.txt`.
- **Disposition:** Standing.

### 8. Structure

- **What:** One real structural change, and it is the porter's own recorded decision: the original's CSS carries an "S-CSS-P Integration" section (original L234–241, styling for an external component integration); the candidate deletes the section's rules and leaves a comment in their place (candidate L311): `/* S-CSS-P integrations are removed because it's unavailable in scp-jp. */` — the integration's target does not exist on scp-jp, so the rules are dead weight with a misleading promise, and the porter recorded the removal and its ground in-file (this block is the classifier's residue B76, promoted here because it is a change with a reason, not noise). The candidate also appends a small porter patch section to the code body (`/*---- CODE BLOCK PATCH ----*/`, candidate L816–819, block B95). Everything else structural is the credit-pair collapse (section 1) and the frame split (section 0). The census decides the six EXHIBIT-RESTRUCTURE blocks: they sit on include lines and the credit area; the exhibit sequence itself is intact on both sides.
- **Why:** R3's question (sanctioned replacement vs silent deletion) is answered by the porter's own comment: the deletion is sanctioned by unavailability and is not silent. Ruling 4's converse also shows here: a component that cannot be ported (an external integration with no JP existence) is removed with its reason recorded, rather than carried as dead rules.
- **Verify:** `grep -n 'S-CSS-P' original.txt candidate.txt` — the section head in the original, the removal comment in the candidate.
- **Disposition:** Standing (a recorded, grounded removal).

### 9. Formatting only

- **What:** 12 whitespace-only blocks, all small blank-line deltas around the exhibits and the code body (the adopted translation's padding against the mirror's). No re-indentation class is recorded. The count is disclosed so a follow-up diff's padding churn is recognizable against it (R7).
- **Why:** R7: formatting churn is disclosed as its own class.
- **Verify:** The classification's section 9 counts (WS-ONLY 12, re-indentation 0).
- **Disposition:** Standing (disclosed; no semantic content).

### 10. Porter annotations

- **What:** Present — this theme is the batch's exception to the usual "none". The candidate carries the S-CSS-P removal comment inside its CSS (candidate L311, quoted in section 8): an English porter note explaining a deletion, addressed to whoever maintains the file next. It is the only porter annotation; there are no `[!-- ... --]` notes. The annotation is the adopted translation's own, kept by the reconciliation.
- **Why:** R2: porter-added text is part of the change record. This one earns its place: without it, the missing integration section reads as an accident; with it, the removal is a decision a reviewer can judge (and section 8 judges it: correct, because the integration target does not exist on scp-jp).
- **Verify:** `grep -n 'unavailable in scp-jp' candidate.txt` — the one line.
- **Disposition:** Standing (recorded, and doing its job).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two pseudo-ref errors: the candidate's own draft-host local--code lines (section 3), class (ii) posting-procedure. There are no hotlink errors and no class (i) error — the only T1 profile this clean in the batch, earned by section 4's re-hosting. (2) T4's two display-affecting findings: the P3 credit fields, FIXED (section 1), and the P9 masthead, DISPOSITIONED under ruling 2 (section 5). (3) The render row's items: the sample's lower half rendered blank white in one run (the lane's own note: possible stale cache, not a defect), the sample's T2 run returned no machine verdict (exit 2, no summary — a coverage caveat, carried in section 12), a runtime-hotlink observation (environment layer, KB-40), and a positive confirmation that the page's credit modal opens.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); KB-40; ruling 2), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1 and 3); item 2's halves are FIXED and DISPOSITIONED as stated.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 17): exit 1, 2 errors / 1 warn / 2 infos; both errors are pseudo-ref (the draft-host lines), class (ii); there is no class (i) error and no hotlink. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-B row 17): FINDINGS — the sample items of section 11(3), including the exit-2 coverage gap on the sample's T2 run; the page side carries the positive credit-modal confirmation. (c) T4/T5 (LOCALIZE-ROWS row 18): FINDINGS jointly, display-affecting findings 2 (the P3 credit fields; the P9 masthead); the ledger §(c3) line records P3 FIXED and P9 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +264/−128 in 100 change blocks / 10 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, including the one gap.
- **Verify:** Re-run the checker on `pages/theme:isolated-terminal-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 17; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-SNIPPET — production-predecessor reference audit (landing 358955e).** `FIX-SNIPPET.md` records two self-references (candidate L67 and L230) as DRIFT ground D1 (own code addresses under `theme%3Aisolated-terminal-jp`). Commit 358955e inserted `-jp` after the target on both lines, `theme:isolated-terminal` → `theme:isolated-terminal-jp`. The BHL exhibits at L66/L229 are COHERENT ground C1 and were not edited. T1 before/after unchanged (2/0/2).

## Change set outside the two diffed files

The diff covers two files; this theme's record is three. `pages/phase17-diff-isolated-terminal-jp.txt` is the Phase 17 migration record for this theme (the revision recording and drift incorporation of commit 8dcac74) — part of this theme's provenance, cited in the Provenance table. `pages/theme-decoration-sample-isolated-terminal-jp.txt` is the decoration sample the render checks ran against (its blank-white run and exit-2 gap are in section 11(3)). The gosign2 T1 fix commit (b816e10) touched the T1 rows 1–44 files in one wave; the other files are those themes' own records, not this one's change set. There are no companion fragments.

## Appendix — residue and low-signal blocks

Class M treatment: the residue collapses into this table rather than per-block slots (block B76 is additionally promoted to sections 8 and 10, as noted there).

| Block(s) | Shape | Resolution |
|---|---|---|
| B76 (residue) | The S-CSS-P section (original L234–241) replaced by one comment line (candidate L311) | A grounded removal with a porter annotation; sections 8 and 10 |
| B19 (residue) | One added `-----` rule line at candidate L75, inside the exhibits | A translator's separator with no original counterpart; section 6 |
| B62 (residue) | One empty alignment line at candidate L201 | No content |
| B81 (residue) | An empty alignment span at candidate L454–457 where the body channel meets the code-css channel | No content |
| B82 (CSS-BODY) | One measured value change inside the code body: `flex-basis: 6rem` → `8.3rem` (original L577 → candidate L688) | A real delta with no ground stated in the campaign record; shown here so a reviewer sees it rather than discovers it. It sits in the rate/credit width area of the layout, but the record does not say that, and this README does not invent a reason |

## License and attribution

- **Title:** Isolated Terminal Theme
- **Author:** EstrellaYoshte, Woedenaz
- **Source:** https://scp-wiki.wikidot.com/theme:isolated-terminal — revision 122 (revision date 2026-02-01 03:34:54)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: oplax-counterpoint — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
