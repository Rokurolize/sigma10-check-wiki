# Review package — theme:flowergarden-jp (KO → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:flowergarden-jp — origin KO, population #261 [GOSIGN2-LEDGER (b) row 261]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9d374deea17eb0688f90a07c3069ef0f9e17753bf855e7aa08a33a3add595022); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 0 warns / 1 info (pseudo-ref×8); standing classes dispositioned in register c1 [T1-ROWS row 265; GOSIGN2-LEDGER (b) row 261]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page sidebar-not-opening + runtime-hotlink site-theme chain; sample credit-modal (preview-form) + runtime-hotlink; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 260, source LOCALIZE-S2-F]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 260]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 261]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:flowergarden-jp.txt sha256:9d374deea17eb0688f90a07c3069ef0f9e17753bf855e7aa08a33a3add595022; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 261) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×8 (class (ii), section 11); the render row's cross-cutting items (KB-40 site-theme chain, including the page sidebar item; KB-32 preview-form credit modal, section 11). T4/T5 passed with zero display-affecting findings, so this theme carries no localize dispositions |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:flowergarden | theme:flowergarden-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 57 (first translation; the candidate's credit block records 初訳時参照リビジョン: 57) | — |
| Source of this copy | Campaign cache `review-wave2-frozen/k3/orig-flowergarden.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:flowergarden-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 621 lines / 16,245 bytes | 644 lines / 18,781 bytes |
| SHA-256 | 6721a7c5e5f1a5d44ad27d551c384d15209ffe2a8573f068045bb20a92ff1812 | 2d7cdf3a32d751f94c8981cc994d4d5c7594721bcc02a49a2810300ad4c6ed78 |

Wave history: the candidate was created by the Stage 2 KO3 integration (commit 783e87d, the LOCALIZE-S2-F wave's port) and touched last by 1869877 (FIX-CREDIT-D). No FIX-wave commit touches this file. sources.tsv carries no drift note for this theme: the rev-57 mirror is the port's whole baseline, and T4 recorded a clean pass.

## Summary

Flower Garden （꽃밭） is a soft-toned KO theme whose port is small in decision count and unusually well documented in-file. The decisions: the KO credit pair becomes the JP preview block; the original's two code blocks (a main exhibit and a hidden display:none block holding the frame CSS) are consolidated into the single code page the frame references, with a CSS comment in the exhibit explaining the consolidation; the Korean webfonts, which the original loads from a KO file host, are replaced by Noto Serif JP / Noto Sans JP with the stacks rewritten, and the license box's font entry states the substitution and its reason; and where the original is silent (it documents none of its theme-specific classes, and it states no licenses for its image files), the porter says so in the file — a supplied class documentation section, and license entries that record the gap and ask for author confirmation before posting. Sixty of the ninety blocks are whitespace-only (the exhibit's blank-line normalization), so the measured churn (diff.md: +171/−148, 319 changed lines in 90 change blocks / 14 hunks) overstates the semantic content by design of the form.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 90 change blocks — 73 specific (81.1%), 15 heuristic (16.7%), 2 residue (2.2%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 5 |
| CONTENT-STRING | 2 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 8 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 5 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 3 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 2 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 2 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 3 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 11 |
| TRANSLATION-ANCHORED | 2 |
| WS-ONLY | 60 |

Adjudication for this README (every A-tier block and every primary family was read against the bytes): the three EXHIBIT-RESTRUCTURE primaries are the tail furniture region (block B90: license box plus the delivery tail) and the code-block consolidation seams — adjudicated in sections 3 and 8, not content restructurings. The eight CSS-BODY primaries are the exhibit's stack and variable edits, of which the font ones are P7 rewrites per the standing lesson (section 4). The two residue blocks resolve in the appendix (a blank seam; a collapsible seam at the exhibit/license boundary). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:flowergarden-jp; ancestor theme:flowergarden on scpko at reference revision 57; candidate `pages/theme:flowergarden-jp.txt`. Provenance route: derived from the ancestor at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the candidate opens with a module CSS importing its own /1 from the draft host (candidate L2) and a single `:scp-jp:component:interwiki-style` include at priority 1 delivering the same /1 (candidate L5–8), then the localized gate and the credit block. The ancestor's frame sits at its tail (`:scp-wiki:component:interwiki-style` at original L618–620, delivering its /1 from scpko.wdfiles.com) and its head opens with the gate and the info pair — the candidate moves the frame to the head, the JP form's convention.
- **Why:** Section 0 declares the route so later counts are read against the right baseline; the gate's tag is P2, the frame is P6/T3 with P4 delivery (section 3).
- **Verify:** The sources.tsv row for flowergarden-jp; `sha256sum original.txt` against the Provenance table; the frame lines at candidate L1–10.
- **Disposition:** Standing (the route itself); the frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The ancestor's credit furniture is the KO `info:start`/`info:end` pair (original L2, L16) with its prose (title 꽃밭 테마, 제작: [[*user thd-glasses]]). The candidate deletes the pair (INFO-DEL ×2, blocks B1, B3) and installs the JP preview block (candidate L11–20) with the eight ruling-3 fields (title 花園テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 꽃밭 테마; 著作権者 [[*user thd-glasses]]; 作成年 2021; 初訳時参照リビジョン 57; the source link, candidate L19, naming scpko.wikidot.com, the ancestor's recorded host). The candidate also adds the closing license box (`license-box-backend` at candidate L601, `license-box-end` at L642), whose entries document the theme's image files and its fonts. The image entries carry an honesty marker this package records rather than resolves: each states ライセンス: 原語版に記載なし（投稿前に著者へ確認してください） — the original states no license for the files, and the entry asks for author confirmation before posting (one entry does record a Pixabay origin for its file). The font entry (candidate L640) is complete by contrast: Noto Serif JP / Noto Sans JP, Google Fonts, SIL Open Font License, with the substitution note of section 4.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the info pair is deleted rather than duplicated (KB-09). The license entries follow the attribution standard's other half: where the source record is silent, the entry says so and names the pre-posting action, instead of inventing a license — a documentation gap carried visibly is the correct state for a draft-stage candidate.
- **Verify:** `grep -n 'info:start\|credit:\|license-box' candidate.txt` — no info pair, one preview pair, one license-box pair; read candidate L11–20 and L601–642.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified). The license-gap entries stand as recorded in-file; they are a posting-time confirmation item, not a ledger finding (T4 passed this theme).

### 2. Includes and components

- **What:** The candidate's live includes are the frame (section 3), the credit pair, and the license-box pair. The usage exhibit's escaped include is repointed `:scpko:theme:flowergarden` → `:scp-jp:theme:flowergarden` as built (block B5, candidate L27) — a repoint that changed the branch prefix but kept the plain slug, so the exhibit named a page that does not exist on scp-jp; the usage-example population sweep has since completed the name on the same line to `:scp-jp:theme:flowergarden-jp` (SWEEP-USAGE.md; canonical commit b5cb724). No component includes needed repointing: the theme is self-contained CSS over the base it assumes, on both sides.
- **Why:** P1 (KB-15) for the exhibit repoint: it names the JP counterpart that exists. The repoint as built satisfied the branch half of that rule only — its plain slug named no JP page — and the sweep's completion to the posting name is what brings it under the rule.
- **Verify:** `grep -n '\[\[include' candidate.txt` — six includes, all `:scp-jp:` forms; no `:scpko:` include survives.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The ancestor delivers from two code blocks: a main exhibit (original L575) addressed as its /1 by the tail frame, and a second code block (original L598) wrapped in a display:none container, holding the frame-related CSS in-page. The candidate consolidates the two into a single code exhibit (candidate L39, its only code block, hence its /1 by construction) and delivers it from the head: the module import (candidate L2) and the priority-1 frame (candidate L5–8), both naming the draft host's local--code/theme%3Aflowergarden-jp/1. The consolidation is documented in-file by a CSS comment at the exhibit's frame section (candidate L580): 原語版では display:none の非表示コードブロックだったものを、interwiki-style が参照する local--code/1 に統合 — "what was a hidden display:none code block in the original is integrated into the local--code/1 that interwiki-style references." The candidate's exhibit sits at the head of the body (candidate L39 onward) where the ancestor's exhibits sit at its tail; the prose body is correspondingly short on both sides.
- **Why:** P4/T3: one code page, addressed correctly, delivered by the standard frame — the consolidation removes the hidden-block apparatus, which existed to work around the ancestor's tail-frame arrangement, and the in-file comment preserves the reasoning. The draft-host form of the delivery lines is KB-41, class (iii), rewritten at posting.
- **Verify:** `grep -n '\[\[code' candidate.txt original.txt` — one block against two; read candidate L578–582 for the consolidation comment.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the consolidation itself is part of the port as integrated and T4-passed.

### 4. Fonts and assets

- **What:** The font program is replaced, and the replacement is the section's whole content. The ancestor loads two Korean webfont stylesheets from the KO file host (original L26–27: GabiaBombaram.css, NapjakBlock.css, from scpko.wdfiles.com/local--files/korean-font/) and names a shelf of Korean faces in its stacks (EBSHunminjeongeumSBA, GenKJwajinOTF-Rg, BBTreeCB, MapoDacapo, MapoFlowerIsland, GabiaBombaram, Nanum Gothic). The candidate drops both stylesheet imports, loads Noto Serif JP and Noto Sans JP from Google Fonts in a single import (candidate L43, block B9), and rewrites the stacks to the JP faces with system fallbacks: `'Noto Serif JP', 'Hiragino Mincho ProN', serif`; `'Noto Sans JP', 'Hiragino Sans', sans-serif` (and their verdana variants); the monospace stack keeps its Latin faces and Nanum Gothic Coding, which needs no substitution. The license box's font entry (candidate L640) documents the change and its ground: 原語版が使用していたKorean Webフォントは配信元の都合により差し替えています — the Korean webfonts were replaced because of the distributor's circumstances. Image assets are the license box's inventory (section 1); their `url()` references in the exhibit are re-hosted to the draft host (DRAFT-HOST blocks B12, B13, B63).
- **Why:** P7/T5 with KB-16, in its substitution form: the ancestor's faces are served from a KO community file host whose availability the port cannot rely on (the entry's stated ground), so the port loads the standard JP faces and re-points every stack at them — a font-stack rewrite where the original faces are named and accounted for, not silently dropped. T4 passed this theme with zero display-affecting findings, the checker's confirmation that the substitution is complete (no stack left naming an unloaded face).
- **Verify:** Read candidate L43 against original L26–27; `grep -n 'font-family' candidate.txt` returns the JP stacks and the mono stack; `grep -n 'korean-font\|GabiaBombaram\|MapoFlower' candidate.txt` returns nothing outside the license entry's prose.
- **Disposition:** Standing (part of the port); no font item dispositioned.

### 5. Header, sidebar, and site furniture

- **What:** The theme sets its header through the exhibit's variables on both sides, and the port's changes there are the font stacks of section 4 and the CONTENT-STRING pair (×2: the header string defaults in the exhibit, translated). The theme sets no `--header-title` text of its own that survives as a language item: no P9 finding was recorded for this theme, and T4 passed it. The render row's sidebar item (page sidebar-not-opening) is recorded by the lane as part of the KB-40 environment-layer chain item, not as a furniture defect of the candidate (section 11).
- **Why:** The section's ground is stated plainly: the furniture changes are the font and string changes already recorded, and the one furniture-shaped render item belongs to the environment layer by its own record.
- **Verify:** The CONTENT-STRING blocks are in classification.json (candidate exhibit region); the sidebar disposition is the ledger §(c2) block for this theme.
- **Disposition:** Standing; no header item recorded or dispositioned.

### 6. Text translation

- **What:** The body prose is translated (TRANSLATION-ANCHORED ×2 primaries; TRANS-UNANCHORED 11 label occurrences — the body is short; most of the file is CSS), covering the usage text and the exhibit captions. The candidate also *adds* documentation the original lacks (section 10): the class documentation section at candidate L30–31. Korean survives reader-visible only in the credit block's 原題 field (candidate L15). In-CSS text (R1): the exhibit's comments are translated where they carry meaning (COMMENT-TEXT ×5), including the consolidation comment of section 3, which is the porter's own Japanese.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). T5 passed this theme jointly with T4.
- **Verify:** The pairs are diff.md's 14 hunks in order; a Hangul scan of candidate.txt outside the exhibit returns the credit 原題 field only.
- **Disposition:** Standing (the port itself); T4/T5 PASS with zero display-affecting findings (LOCALIZE-ROWS row 260).

### 7. Links

- **What:** One LINK-REPOINT block (inside block B3's region): the ancestor's credit-region link arrangement is replaced by the preview block's source link (candidate L19), naming scpko.wikidot.com — the ancestor's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed. The license box's one outbound link (the Pixabay source page for a background file, candidate L613) is an attribution record, kept verbatim.
- **Why:** P11 under the dead-reference evidence standard; attribution sources are provenance data (the TASL record), which the port preserves.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit source link is the only live hit.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The localize.md closing rule holds, with the one deliberate structural change recorded in section 3: the two code blocks consolidated into one, and the exhibit's position moved from the ancestor's tail to the candidate's head-of-body, following the frame's move. Variable names, selectors, and the exhibit's internal order are preserved (the 60 whitespace blocks are blank-line seams inside it, section 9). An exhibit census — usage exhibits, the code exhibit, the license region — corresponds to the ancestor's, and the classifier's three EXHIBIT-RESTRUCTURE primaries adjudicate to the tail furniture (B90) and the consolidation seams, so the R3 question does not arise.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the consolidation is documented in-file (candidate L580) and the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[code\|\[\[collapsible\|license-box' original.txt candidate.txt` — one code block against two, the license pair added, the collapsibles corresponding.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Sixty whitespace-only blocks (WS-ONLY ×60 primaries), all inside the CSS exhibit: the blank-line normalization the KO3 integration applied to code blocks (the same EN9-style normalization seen across this batch's KO/EN waves). They are two-thirds of this package's blocks and none carries a semantic line. The classifier finds no re-indentation pair in the primary census, so the R7 follow-up-diff hazard is not triggered beyond the normalization itself.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the honest statement is that the class dominates the block count and means nothing semantically.
- **Verify:** The blocks are listed in classification.json with their exhibit line ranges (original L42–491 region); spot-reading any of them in diff.md shows blank-line-only pairs.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three porter marks, all substantive. (1) The supplied documentation section (candidate L30–31): a heading + クラス（原語版に記載なし） and a paragraph stating that the original documents none of this theme's own classes, and describing the classes that are defined (all thin, pale-toned boxes) — documentation the porter wrote because the original is silent, marked as supplied in its own heading. (2) The consolidation comment in the exhibit (candidate L580, quoted in section 3). (3) The license box's gap markers and font-substitution note (candidate L607–640, section 1 and 4): attribution annotations that record what the original does not state. No `[!-- --]` translator notes exist in the candidate.
- **Why:** R2: porter-added text is part of the change record, and this theme's annotations are the port's documentation conscience — each one marks the exact place where the port had to decide something the original left unsaid, and says what was decided.
- **Verify:** Read candidate L30–31, L580, and L607–640.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Two items, both cross-cutting, each with its ground. (1) T1's eight pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host local--code lines and the frame's delivery references (section 3); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. (2) The render row's items: the page sidebar-not-opening with the runtime-hotlink site-theme chain (KB-40, environment-layer: runtime hosts arrive via the shared site theme chain, not the candidate) and the sample credit-modal item (KB-32, preview-form property: `credit:start-preview` has no modal mechanism, GOSIGN-TESTS.md T2 note), with T3 none beyond the cross-cutting items, in the lane's own words. There are no T4 items (the localize check passed with zero display-affecting findings). The license-gap entries of section 1 are not ledger items; they are recorded here so the package does not hide them: they resolve at posting time by author confirmation, as the entries themselves say.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged to the candidate's bytes.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 265's, the render items are the ledger §(c2) block for this theme (RENDER-S2-H (KO3)).
- **Disposition:** DISPOSITIONED (both).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 265): exit 1, 8 errors / 0 warns / 1 info; all eight errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO3)): FINDINGS, the cross-cutting items of section 11(2) only, all dispositioned; engine coverage is the full matrix as run by the lane, not separately caveated in the row. (c) T4/T5 (LOCALIZE-ROWS row 260): PASS jointly, display-affecting findings 0 — one of the batch's two clean localize passes. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +171/−148 in 90 change blocks / 14 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:flowergarden-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 261; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The port that writes down what the original left unsaid

Flowergarden's original is an unusually quiet source: it does not document its own classes and does not license its image files. A mechanical port would have carried that silence across, and the JP page would have inherited two invisible gaps. This candidate instead marks both gaps at the exact places a reader meets them — a supplied class section whose heading admits the original says nothing, and license entries that say "not stated in the original; confirm with the author before posting" six times over. That is the difference between a translation and a port, and it is why this theme's package, despite a block count dominated by whitespace, is one of the batch's most instructive: the semantic content of the port is largely the judgment calls, and every one of them is written down in the file itself.

### The usage example's posting name

The usage example at candidate L27 as built read `@@[[include :scp-jp:theme:flowergarden]]@@`: the porting wave's repoint changed the branch prefix from `:scpko:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:flowergarden-jp` on the same line (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots.

| Block | Shape | Resolution |
|---|---|---|
| B6 (no signature) | Original L21–22 → candidate L28: a blank-line seam between the usage exhibit and the body prose | Formatting seam where the candidate's head furniture re-flows the page (section 9's class, at body level) |
| B85 (no signature) | Original L593 → candidate L598–599: a `[[/collapsible]]` seam at the code exhibit's close, before the license box | Exhibit-boundary seam of the consolidation (section 8): the candidate's single exhibit closes where the ancestor's first exhibit closed, with its second (hidden) block absorbed |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-flowergarden-jp.txt` is the decoration sample the render checks ran against (its credit-modal item is section 11(2)). There are no companion fragments, no base-theme layering, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 꽃밭 테마
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/theme:flowergarden — revision 57
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
