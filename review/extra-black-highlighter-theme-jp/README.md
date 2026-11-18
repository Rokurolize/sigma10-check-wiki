# Review package — theme:extra-black-highlighter-theme-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:extra-black-highlighter-theme-jp — origin EN, population #10 [GOSIGN2-LEDGER (b) row 10]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 36edd54937643f2626a9c9b986812351f6d819912739fa42ec26b7d7e6a6a611); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 2 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 10; GOSIGN2-LEDGER (b) row 10]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — preview-notice rating widget「価:0」missing, mobile overflow 337–419px, sidebar x=0, sample credit-modal. [RENDER-ROWS-1 (RENDER-A row 10)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 10)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 11, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 11]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 10]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:extra-black-highlighter-theme-jp.txt sha256:36edd54937643f2626a9c9b986812351f6d819912739fa42ec26b7d7e6a6a611; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 10) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (ii), section 11); the render row's items (KB-33/KB-34 overflow family; KB-32 preview-form credit modal, section 11); T4's P5 item dispositioned class (ii)/KB-58 and its P7 item dispositioned under the T4 bar, while its P3 item was FIXED by the credit waves and FIX3-A1 (sections 1, 4, 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:extra-black-highlighter-theme | theme:extra-black-highlighter-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 21 (first translation; the candidate's credit block records 初訳時参照リビジョン: 21) | — |
| Source of this copy | Campaign cache `review-wave2-frozen/k1/orig-extra-black-highlighter-theme.txt`, via the mirror store (class FETCH-REGEN, hash-verified against review/sources.tsv) | Canonical file `pages/theme:extra-black-highlighter-theme-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 426 lines / 12,718 bytes | 467 lines / 15,144 bytes |
| SHA-256 | a8542f7b3f9d486085ef9fbe9cc46c5d3295bb8df7df5b85a428c8f10128a13a | 246973dd9589113f2c63e64d591443ca6719da2e20913a3a483b8549555d99f0 |

Wave history: the candidate entered the repo with the display-check composition import (commit d727e92), was recorded by Phase 17 (8dcac74: reference revision recorded, drift incorporated), then touched by b816e10 (gosign2 T1 fixes: credit fields and furniture), 5c32672 (FIX-CREDIT-C), and last by 19ae059 (FIX3-A1: the LOCALIZE-A rows 1–11 fixes; the verdict stamp is computed against this commit). Kind note (sources.tsv K6): a production JP page, theme:extra-black-highlighter-theme, already exists, and the migration was delivered as a diff against it (`pages/phase17-diff-extra-black-highlighter-theme-jp.txt`); the recorded production drift is 一致 (match). Recorded drift on the other side: the original has been superseded upstream since rev 21; the campaign record carries the follow-up diff artifact `diff-extra-black-highlighter-theme-from21.txt` (sources.tsv K5a-i note).

## Summary

This is the batch's second production-adoption port (kind K6, the flopstyle shape): SCP-JP already had this theme, translated in 2024 by Salty_149, and the candidate is that production page brought into Sigma-10 form — measured here at 0.9557 difflib similarity to the production copy in `pages-existing/` (2026-11-17), with the migration itself delivered as the Phase 17 diff file. Read against the EN original, the diff therefore measures the production page's four years of independent life as much as the migration: BHL delivery re-based to the JP distribution, the credit completed to the eight fields (an early candidate state had a duplicate bare Rate and a two-field skeleton, T4's P3 item, fixed by the credit waves and FIX3-A1), the exhibit's whitespace normalized wholesale (40 whitespace-only blocks, the adoption's formatting signature), and three small JP production CSS corrections riding at the tail that have no original counterpart at all. Measured churn against the original (diff.md, Tier 2 format: +211/−170, 381 changed lines in 99 change blocks / 4 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 99 change blocks — 76 specific (76.8%), 21 heuristic (21.2%), 2 residue (2.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 6 |
| DRAFT-HOST | 3 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 6 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 6 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 22 |
| TRANSLATION-ANCHORED | 21 |
| WS-ONLY | 40 |

Adjudication for this README (every A-tier block and every primary family was read against the bytes): the six EXHIBIT-RESTRUCTURE primaries are include repoints inside exhibit regions (their INCLUDE-REPOINT secondaries say so: blocks B5, B7, B16, B95, B97) plus the image-block exhibit (B18) — adjudicated in sections 2 and 8 against the exhibit census, not restructurings. The 40 WS-ONLY primaries are the production adoption's whitespace signature inside the exhibit (section 9). The two residue blocks resolve in the appendix (a blank seam; the examples-heading translation). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:extra-black-highlighter-theme-jp; original theme:extra-black-highlighter-theme on scp-wiki at reference revision 21; candidate `pages/theme:extra-black-highlighter-theme-jp.txt`. Provenance route (declared, per the standing rule for this kind): **R4 production adoption** (sources.tsv kind K6) — the candidate is the Sigma-10 form of the live production page theme:extra-black-highlighter-theme, not a fresh derivation from the original; the migration deliverable is `pages/phase17-diff-extra-black-highlighter-theme-jp.txt`, a diff written to be applied to the production page, and the recorded production drift is 一致 (the production page still matches its recorded state). The frame: the candidate opens with its credit block (candidate L3–12), then a head module importing BHL from scp-jp.github.io and Noto Sans JP (candidate L14–16), the head frame at priorities 1–2 (candidate L63–68), and a tail frame at priority 3 delivering its own /1 (candidate L449–451) — the original's frame is the same shape on EN hosts (`:scp-wiki:component:` includes, nu-scptheme.github.io imports, scp-wiki.wdfiles.com code page; original L35–42, L423–425).
- **Why:** Section 0 declares the route so later counts are read against the right baseline: for a K6 theme, a diff line can be the production page's own history rather than a porting decision, and sections below say which is which where it matters. The gate's tag is P2; the frame is P6/T3 with T9 delivery (section 3).
- **Verify:** The sources.tsv row for extra-black-highlighter-theme-jp (kind K6, drift 一致）; `sha256sum original.txt` against the Provenance table; the phase17-diff file's header, which names the production page and rev 21.
- **Disposition:** Standing (the route itself); the frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The candidate's credit block stands at the head (candidate L3–12) with the eight ruling-3 fields: title and 原題 both "Extra Black Highlighter Theme"; **翻訳責任者 Salty_149, 翻訳年 2024** — the production page's human translator and year, kept, because the adoption rule keeps the live JP creator's credit where the candidate derives from their page; 著作権者 Woedenaz; 作成年 2021; 初訳時参照リビジョン 21; the source link (candidate L11) naming scp-wiki.wikidot.com, the original's recorded host. The path here was not direct: T4 (LOCALIZE-ROWS row 11, item (i)) found an early candidate state with a duplicate bare Rate (the credit's embedded Rate plus a bare one at L60, two widgets) and a two-field skeleton credit; the bytes now show the completed eight fields and no bare Rate anywhere (`grep -n 'module Rate' candidate.txt` returns nothing; BARE-RATE-DEL ×1 records the deletion against the original's arrangement). The tail's second supplement module (candidate L459–462) is a credit-dialog correction in CSS form (section 4's tail note).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so a second bare Rate is a duplicate widget, deleted rather than kept (KB-09). The translator field follows the attribution standard for adopted production pages: the human translator of the underlying JP page is credited as 翻訳責任者， and the AI attribution rule applies to translations Muse made, which this one is not.
- **Verify:** Read candidate L3–12 against the eight fields; the FIX3-A1 report (REPORT-GOSIGN2-FIX3-A1.md) records the rows 1–11 repairs this file received.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified; the duplicate Rate removed in the same waves, final touch FIX3-A1 commit 19ae059).

### 2. Includes and components

- **What:** The frame includes take the `:scp-jp:component:` form (candidate L63, L68, L449). The usage exhibit's escaped includes are repointed (candidate L86–87: `:scp-jp:theme:black-highlighter-theme`, `:scp-jp:theme:extra-black-highlighter-theme`). The theme-squares exhibit include is repointed `:scp-wiki:component:` → `:scp-jp:component:` (candidate L96). The logo image-block's `name=` moves from nu-scptheme.github.io to scp-jp.github.io (candidate L130, block B18) — the same JP BHL distribution as the frame, which is T4's P5 item's current state (section 11). The tail's `:scp-jp:component:bhl-dark-sidebar` (candidate L445) is the repoint of the original's `:scp-wiki:component:bhl-dark-sidebar` (original L419).
- **Why:** P1 (KB-15) for every repoint: each names the JP counterpart that exists. The logo's host is P5/T9: the artwork is BHL's own logo file, served from the JP distribution of BHL rather than the EN upstream.
- **Verify:** `grep -n '\[\[include' candidate.txt` — eleven includes, all `:scp-jp:` or bare JP forms; no `:scp-wiki:` survives.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** BHL delivery moves from nu-scptheme.github.io to scp-jp.github.io in both the head module imports (candidate L14–15, block B2) and the frame's `theme=` arguments (candidate L63–68 region). Own-code delivery keeps the original's two-path shape: a tail module importing the candidate's own /1 (candidate L447) and the tail frame at priority 3 naming the same /1 (candidate L449–451), both on the draft host where the original used scp-wiki.wdfiles.com (original L421, L425). The candidate's exhibit is its first code block (candidate L220), so the /1 address is correct against its own count. Three DRAFT-HOST label occurrences are the tail lines themselves.
- **Why:** T9 (base delivery from JP distributions) for BHL; P4 for the own-code lines, whose draft-host form is KB-41, class (iii) — sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` against the lines above; no nu-scptheme.github.io line survives.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** This layer declares no font stacks of its own: every `font-family` value on both sides is a BHL variable (`var(--body-font)`, `var(--header-font)`, `var(--mono-font)`), so the type program arrives with the base. The head module does carry one font import the original lacks: Noto Sans JP from Google Fonts (candidate L16, JPFONT-LOAD in block B2), inherited from the production page's form. T4's P7 item ("no JP font") was recorded against the stack state and dispositioned under the T4 bar; the bytes' position is that a JP face is loaded at the head while no stack in this layer names it — the naming happens in the base's stacks. Assets: the one artwork reference is the BHL logo (section 2). The tail's three supplement modules (candidate L454–467) are production-born JP corrections with English porter comments: the page-history option row kept within the mobile viewport, the credit dialog's back-link kept on one line (the T7-CREDIT-CSS block — the credit module supplement in this theme takes this small CSS form), and the top-bar labels kept whole at narrow widths.
- **Why:** P7/T5 with KB-16: the load gap the class guards against is a theme whose text has no JP face anywhere in its stack; here the face is loaded in this layer and named in the base's, and the ledger judged the item under the T4 bar. The tail supplements are T7-family production corrections (the credit one directly), recorded here because a reader of the diff meets them as unexplained additions.
- **Verify:** Read candidate L14–16 and L454–467; `grep -n 'font-family' candidate.txt` returns variables only.
- **Disposition:** DISPOSITIONED — P7 (GOSIGN2-LEDGER §(c3): recorded without a display-affecting mark; T4 bar).

### 5. Header, sidebar, and site furniture

- **What:** The theme sets no `--header-title`, `--header-subtitle`, or `--logo-image` of its own in either version: it is a pure BHL variant (a darker Black Highlighter), and its furniture is the base's, with the variant's work done in the exhibit's variable overrides. The sidebar furniture is the tail's bhl-dark-sidebar include (section 2). The render row's sidebar item (sidebar x=0) is a measurement of the preview environment, dispositioned with the overflow family (section 11).
- **Why:** The section's ground is stated plainly: there is no header-variable change to narrate, because the theme's design leaves furniture to the base on both sides. No P9 item was recorded for this theme.
- **Verify:** `grep -n -- '--header-title\|--logo-image' candidate.txt original.txt` — no hits on either side.
- **Disposition:** Standing; no header item recorded or dispositioned.

### 6. Text translation

- **What:** The body prose is translated (20 TRANSLATION-ANCHORED primaries; TRANS-UNANCHORED 22 label occurrences), covering the usage text, the theme-colors exhibit headings, and the specimen captions (the logo caption at candidate L130: SCP財団ロゴ）. The theme's own name and the credit title stay in English as names (section 1). The exhibit's CSS comments are the original's English comments, carried (R1), apart from the production supplements' comments at the tail (section 4), which are the production page's own English.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). For a K6 adoption, part of the translated state is the production page's own translation, which the migration kept — that is the adoption working as intended, not unexamined carry-over: T5 judged the result jointly with T4.
- **Verify:** The pairs are diff.md's four sections in order; an English-prose scan of candidate.txt outside the exhibit returns the theme name and the tail comments.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the items named.

### 7. Links

- **What:** No LINK-REPOINT block fired. The candidate's one attribution link is the credit source link (candidate L11), naming scp-wiki.wikidot.com — the original's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed.
- **Why:** P11 under the dead-reference evidence standard: a link that already names the serving original needs no change.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit source link is the only live hit.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and exhibit order are preserved; the candidate's additions are the credit block at the head (section 1) and the three tail supplement modules (section 4), both adoption/migration furniture, and its one deletion is the duplicate bare Rate (section 1). An exhibit census (theme-colors exhibit, usage exhibits, logo exhibit, the code exhibit) corresponds one to one with the original's. The classifier's six EXHIBIT-RESTRUCTURE primaries adjudicate to include repoints inside exhibits (section 2), so the R3 question does not arise.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[include\|\[\[code\|\[\[module' original.txt candidate.txt` — the sequences correspond apart from the recorded furniture.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Forty whitespace-only blocks (WS-ONLY ×40 primaries), all inside the CSS exhibit (original L196–412 → candidate L222–438): the production page's exhibit whitespace differs from the original's throughout (blank-line placement between rules), and the adoption carried the production whitespace into the candidate wholesale. This is the largest formatting class in the batch and it is adoption-shaped, not edit-shaped: no semantic line is involved in any of the forty. The classifier finds no re-indentation pair (0).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; on a K6 theme the honest attribution is to the production page's own formatting, which the migration had no reason to normalize against the EN original.
- **Verify:** The forty blocks are listed in classification.json with their exhibit line ranges; spot-reading any of them in diff.md shows blank-line-only pairs.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** No translator notes and no `[!-- --]` comments exist in the candidate (the annotation scan returns no hits). The porter marks that do exist are the three English CSS comments heading the tail supplement modules (candidate L455, L460, L465: "SCP-JP Wikidot page history: …", "SCP-JP Wikidot BHL credit otherwise correction: …", "SCP-JP Wikidot extra-black-highlighter-theme top bar labels: …") — production-born comments that name their own purpose and wiki, carried by the adoption. They are recorded here because they are the only in-file explanation of the tail modules (section 4).
- **Why:** R2: porter-added text is part of the change record; on an adopted page, the production page's own annotations are part of what was adopted.
- **Verify:** Read candidate L454–467.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's two pseudo-ref errors: class (ii), posting-procedure — the candidate's own draft-host local--code lines (section 3); the posting procedure rewrites or re-hosts them. (2) The render row's items: the preview-notice rating widget 「価:0」 missing, mobile overflow 337–419px, and sidebar x=0 — the recorded cross-cutting families, static credit replica fixed width (KB-33) and preview chrome (KB-34), with the register noting the per-theme figures match the campaign-wide shapes; and the sample credit-modal item, preview-form property (KB-32). (3) T4's P5 item (the logo served from a test bucket at T4 time): dispositioned class (ii)/KB-58; the current bytes serve the logo from the JP BHL distribution (candidate L130), which is the distribution the frame itself uses. (4) T4's P7 item: argued in section 4. T4's third display-affecting item, P3, is not here because it was fixed (section 1).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; preview-environment shapes are recorded as not-charged to the candidate.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 10's, the render items are the ledger §(c2) block for this theme (RENDER-A (row 10)), the T4 outcomes are the §(c3) line (LOCALIZE-A).
- **Disposition:** DISPOSITIONED (items 1, 2, 4 and the P5 item); FIXED (the P3 item, section 1).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 10): exit 1, 2 errors / 0 warns / 2 infos; both errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-A row 10): FINDINGS, the items of section 11(2), all dispositioned; engine coverage is the full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 11): FINDINGS jointly, display-affecting findings 3 (P3 fixed; P5 and P7 dispositioned, sections 1, 4, 11); the ledger §(c3) line records exactly those three outcomes. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +211/−170 in 99 change blocks / 4 diff sections (Tier 2 format).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:extra-black-highlighter-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 10; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### What adoption means for this diff

A reviewer comparing the two files in this package cold would over-credit and over-blame the migration in equal measure: the whitespace mass is not the migration reformatting anything, the tail corrections are not the migration inventing fixes, and the translator credit is not an attribution error. All three are the production page's own four-year history, which the candidate adopts wholesale because that is what K6 means: the live JP page is the port's real source, the EN original at rev 21 is its reference, and the Phase 17 diff file is the migration's actual deliverable. The go-sign question for such a theme is narrower than for a fresh port — does the candidate faithfully carry the production page into Sigma-10 form, with the credit completed and the delivery re-based — and on the records (drift 一致, T4's three items closed as one FIXED and two DISPOSITIONED) it does.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots.

| Block | Shape | Resolution |
|---|---|---|
| B14 (no signature) | Original L62–63 → candidate L89: a blank-line seam between the usage exhibits | Formatting seam where the candidate's head furniture (credit block, longer frame) re-flows the page (section 9's class, at body level) |
| B17 (no signature) | Original L101–102 → candidate L127–128: the exhibit heading `+ 例` against the original's heading line | A one-line heading translation the differ left unlabeled; counted in section 6 |

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-SNIPPET — production-predecessor reference audit (landing 358955e).** `FIX-SNIPPET.md` records the self-reference at candidate L87 as DRIFT ground D1 (own code delivered from `theme%3Aextra-black-highlighter-theme-jp/1`). Commit 358955e inserted `-jp` after the target, `theme:extra-black-highlighter-theme` → `theme:extra-black-highlighter-theme-jp`. The adjacent BHL exhibit (L86) is COHERENT ground C2 and was not touched. Before/after T1 counts are unchanged (2/0/1).

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/phase17-diff-extra-black-highlighter-theme-jp.txt` is the migration deliverable itself (the diff to apply to the production page), and `pages-existing/existing:theme-extra-black-highlighter-theme.txt` is the production copy the adoption was measured against (similarity 0.9557, section 0). `pages/theme-decoration-sample-extra-black-highlighter-theme-jp.txt` is the decoration sample the render checks ran against (its items are section 11(2)). The follow-up diff artifact for the upstream drift since rev 21 (`diff-extra-black-highlighter-theme-from21.txt`) sits in the campaign record, outside this repo. There are no companion fragments for this theme.

## License and attribution

- **Title:** Extra Black Highlighter Theme
- **Author:** Woedenaz
- **Source:** https://scp-wiki.wikidot.com/theme:extra-black-highlighter-theme — revision 21 (revision date 2022-09-28 18:16:56)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: Salty_149 — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
