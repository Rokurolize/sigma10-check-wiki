# Review package — theme:07k-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:07k-jp — origin KO, population #249 [GOSIGN2-LEDGER (b) row 249]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now b486662b51d9fe8a1e8e29244cd84c0809b6fed6c73bd1e36c95d63e4272a91d); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 0 warns / 1 info (pseudo-ref×2, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 232; GOSIGN2-LEDGER (b) row 249]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + scpko.wdfiles.com; sample credit-modal (preview-form) + runtime-hotlink; T3 none beyond cross-cutting items. All 78 H targets produced a summary.md (no exit-2 incompleteness in this lane). [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 248, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 248]
- FIX5 re-judgement: item 99 (class C) FIXED — FIX5-INFO, commit 9a1c86a: info-module / duplicate credit residue removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 99]
- Computed against: canonical commit 84e8201ca3418907cf4fcb86c19a78d31d20617c; candidate file pages/theme:07k-jp.txt sha256:b486662b51d9fe8a1e8e29244cd84c0809b6fed6c73bd1e36c95d63e4272a91d; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 99 [C] (EN-style info module left beside the JP credit module; two rating areas) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 99: **FIXED** (FIX5-INFO, commit 9a1c86a); re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c3): P5 (class (ii) / KB-58), P7 (recorded without a display-affecting mark; T4 bar), P9 (ruling 2); ledger §(c2) render row: foreign-host delivery class (ii) (KB-41/KB-54 family), credit-modal preview form (KB-32) |
| Flagged in this package | Three items no register names: the GongGothic font stacks left without a load (section 4), the author name absent from the credit furniture after the info block's removal (section 1), and the raisa-ribbon `side` divergence between the candidate's two include copies (section 2). Flagged with evidence; the candidate is not edited |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:07k | theme:07k-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 3, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 3 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-07k.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:07k-jp.txt`, copied at worktree HEAD c63afef |
| Lines / bytes | 369 lines / 6,808 bytes (the file's last line carries no trailing newline, so `wc -l` reports 368) | 397 lines / 8,738 bytes |
| SHA-256 | 0ab68ddf3946c2ef2b3027e8143117ae51d31d81d9ad8006b6d93042ccc9c802 | 742f7a142a89df69905fc2c8c7863654cd79d8fe23d217c655522bc8dda5ebdc |

Wave history: the candidate was created by the Stage 2 KO1 integration (commit 18280b3, the LOCALIZE-S2-F wave's port); FIX-CREDIT-D (1869877) normalized its translator field; FIX5-INFO (9a1c86a) removed the leftover info module (item 99); the usage-example population sweep (b5cb724) completed the usage example's posting name (one line). The sweep is the post-verdict change the stamp's STALE line records; it does not touch item 99's closure.

## Summary

The original is a component-driven KO theme: three live component includes at the head, one 268-line `[[module CSS]]` carrying the whole stylesheet (including the Korean webfont loads), and a gated documentation body whose credit furniture is a bare Rate plus an EN-style info block. The candidate keeps the components (repointed), moves the stylesheet bodily into a `[[code]]` exhibit that doubles as the delivery (topology similarity 0.932), delivers it through the standard draft-host frame, swaps the credit furniture for the preview credit block plus a license box, and translates the body. Measured churn (diff.md, the generator's difflib count: +137/−113 in 8 change blocks; a GNU-diff count of the same pair gives 250 changed lines — the difference is alignment choice, not content). The one blocking item (the doubled rating furniture) is closed and re-derived below. Three smaller items survive every register and are flagged in this package rather than passed over: the delivered CSS still names two Korean font faces that nothing loads, the credit furniture nowhere names the theme's author, and the candidate's two copies of one component include disagree on a parameter.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 8 change blocks — 8 specific (100%), 0 heuristic, 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 4 |
| TRANS-UNANCHORED | 4 |
| DRAFT-HOST | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes, and the sections below are written from classification.json's label_spans, not from the skeleton's per-section text): the skeleton printed "none" for sections 2, 4, and 6 although INCLUDE-REPOINT (B1), FONT-IMPORT and JPFONT-LOAD (B3), and TRANS-UNANCHORED (B2, B3, B6, B7) fired inside multi-label blocks; those sections are written here from the spans. The two EXHIBIT-RESTRUCTURE primaries adjudicate as follows: B1 is the head include repoint plus the new delivery frame, not an exhibit change; B8 is the tail furniture swap (info pair out, license box in) whose INFO-DEL span is item 99's fix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:07k-jp; original theme:07k on scpko at reference revision 3; candidate `pages/theme:07k-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; the candidate's body is a fresh translation of the KO body, as the diff shows line by line, so the R4 production-adoption question does not arise). The frame itself changed shape: the original opens with its three component includes ungated (original L1–3) and its stylesheet module (L5–272); the candidate keeps the includes at the head (candidate L1–3), shrinks the module to a one-line import (L4–6), adds the interwiki-style frame (L8–11), and only then opens the localized gate `[[iftags +テーマ]]` (L12).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for 07k-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a centered bare `[[module Rate]]` (original L276–278) plus an `:scpko:info:start`/`end` pair (original L280–284) whose body names the title and the creator (**제작:** [[*user thd-glasses]], original L283). The candidate carries the JP preview credit block (candidate L14–23) with the eight ruling-3 fields (title 建設者 テーマ（Site-07K）; 翻訳責任者 AI; 翻訳年 2026; 原題 건설자 테마; 著作権者 "原語版ページの作成者に同じ（scpko の theme:07k）"; 作成年 2024; 初訳時参照リビジョン 3; the source link, section 7). The bare Rate is gone (the empty `[[=]]`/`[[/=]]` pair at candidate L29–31 is where it stood) and, after FIX5, the info pair is gone too (per-theme record). The candidate also gains a license box the original never had: `:scp-jp:component:license-box-backend` with author parameter "scpko theme:07k の作者" (candidate L390–391), a blockquote note on image and font sources (L393), and `license-box-end` (L395).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). The info pair is ledger class C residue: an EN-style info module beside the JP credit module renders a second rating area, which is item 99. T4 (KB-63/KB-60): the license box is a supplement where the original had none. Ruling 3 fixes the eight fields and the translator form (FIX-CREDIT-D, commit 1869877).
- **Verify:** `grep -n 'info:start\|info:end\|module Rate' candidate.txt` returns nothing; read candidate L14–23 against the eight fields and L390–395 for the license box.
- **Disposition:** FIXED (item 99, supplement row 99; the credit fields themselves were FIXED by the credit waves per ledger §(c3)). One attribution gap is flagged, not dispositioned: the creator's name. The original names thd-glasses (original L283); after FIX5-INFO removed the info pair, that line is gone, and neither the credit block's 著作権者 field ("the same as the original page's creator") nor the license box's author parameter names him — the string `thd-glasses` survives in the candidate only inside an image URL path (candidate L74). No register names this loss; it is the same family as ledger item 91 (a credit field that drops a named creator) and is recorded here with both sides' text for the coordinator.

### 2. Includes and components

- **What:** The component include set (original L1–3: centered-header-sigma-9, toggle-sidebar, raisa-ribbon) is repointed to `:scp-jp:` (candidate L1–3) and then repeated a second time inside the gated body (candidate L25–27), where the original has no second copy. The two candidate copies disagree on the raisa-ribbon parameter: the head copy reads `alt=1|side=right` (candidate L3), the body copy `alt=1|side=1` (candidate L27), and the original's single copy reads `side=1` (original L3). The remaining includes: the credit pair (section 1), the interwiki-style frame (section 3), the image-block exhibit repointed `:scpko:` → `:scp-jp:` (original L326 → candidate L73), and the usage example's blockquoted include (original L295 → candidate L42, section 7's census covers its form). The body's component list (candidate L55–57) names the three components in plain `[[[component:…]]]` link form, as the original's list did.
- **Why:** P1 (KB-15): every live include names the JP counterpart that exists on scp-jp; all three components have JP ports, so none is kept foreign and ruling 4 is not engaged (nothing had to be ported alongside). The duplicated set inside the gate is the port's own structure: on the candidate page itself (which carries the テーマ tag) both copies render; for pages that include the theme, only the ungated head copy applies.
- **Verify:** `grep -n '\[\[include' candidate.txt` — nine includes, all `:scp-jp:` targets; compare candidate L3 against L27 for the parameter divergence.
- **Disposition:** Repoints applied. The `side` divergence is flagged: the head copy's `side=right` is the lone instance of that form in the repo (the original and the body copy both read `side=1`), no record names the change, and the repo alone cannot prove which value the JP component expects; recorded with both loci, not edited.

### 3. Delivery and code loading

- **What:** The original delivers everything from one live `[[module CSS]]` (original L5–272, 268 lines: the two `@font-face` blocks, the `:root` variables, and the full rule body). The candidate's head module (candidate L4–6) only imports the candidate's own `local--code/theme%3A07k-jp/1` from the draft host, and the interwiki-style include at priority 1 names the same /1 delivery (candidate L8–11). The stylesheet body itself moved, near-verbatim, into a `[[code type="css"]]` exhibit inside a collapsible in the gated body (candidate L119–387; topology pass: module-css → code-css, similarity 0.932), so the exhibit block is the delivery: it is the page's only code block, and the frame's /1 names it. The four DELIVERY-MOVE spans (B2, B3's tail, B4, B5) are this single relocation seen by the differ.
- **Why:** P4/T9 (own-code delivery from JP hosts) and P6/T3 (the supplement frame; priority 1 is the theme's own layer). The draft-host form of the two live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — candidate L5 and L10, both naming /1; confirm the page's single `[[code]]` block spans candidate L119–387.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Load: the original's two `@font-face` blocks (original L6–17: GongGothicMedium and GongGothicBold, served from cdn.jsdelivr.net noonfonts) are deleted, and the candidate's code block opens with three Google Fonts imports (candidate L120–122: Noto Sans JP, Noto Serif JP, Gothic A1, each 400;700). Stacks: the candidate's delivered CSS contains exactly two `font-family` lines, and both are the original's, unchanged — `'GongGothicBold', "Montserrat", "Arial", sans-serif` for the header wordmark (candidate L144) and `'GongGothicMedium', "Montserrat", "Arial", sans-serif` for headings and the page title (candidate L148). No stack anywhere in the file names Noto Sans JP, Noto Serif JP, or Gothic A1; the string "Gothic A1" occurs in the candidate only inside the porter comment (candidate L128). Assets: the logo variable `--lgurl` is re-hosted from `http://scpko.wdfiles.com/local--files/thd-glasses-art-works-page/Site-07k.png` (original L25) to the candidate's own draft-host attachment `theme%3A07k-jp/site-07k.png` (candidate L140), and the image-block exhibit's `name=` keeps the scpko.wdfiles host with the scheme upgraded to https (candidate L74).
- **Why:** P7/T5 with KB-16 (the font load gap) is the class this section exists to check, and the bytes fail it in mirror form: the port removed the load for the faces the stacks name and added loads for faces no stack names, so the header and headings fall back to the generic tail of their stacks. The porter comment (section 10) states the substitution was made ("フォントは Google の Gothic A1 で代替し"), which the stacks contradict. P5/KB-17 covers the asset hosts; the jsdelivr loads disappear with the faces they served.
- **Verify:** `grep -n 'font-family' candidate.txt` — two lines, both GongGothic; `grep -n 'GongGothic' candidate.txt` — the comment (L126) and the two stacks, no `@font-face`; `grep -n '@import' candidate.txt` — the three Google Fonts lines at the code head.
- **Disposition:** FLAGGED (font load gap, KB-16 shape): the stacks at candidate L144/L148 name faces loaded nowhere in the file or its base delivery, and the imported JP families are referenced by no stack. Recorded with exact lines; the candidate is not edited. The asset lines are DISPOSITIONED (class (ii)/(iii) host forms, ledger §(c2)).

### 5. Header, sidebar, and site furniture

- **What:** The `:root` header variables are carried over with their Korean values byte-identical: `--header-title: "초도격리개발기지"` and `--header-subtitle: "회수 · 격리 · 배송"` (original L21–22 → candidate L136–137). No other header variable is overridden (`--lgurl` is section 4's asset), and no P8 layout adaptation appears: the sidebar and topbar behaviour comes from the three JP components of section 2, and the theme's own furniture rules are inside the moved CSS body, unmodified apart from the delivery relocation.
- **Why:** P9/T6 is the variable class; the values are header and title language, which ruling 2 (2026-11-16) places outside migration correctness as translation taste, and ledger §(c3) dispositions this theme's P9 on exactly that ground.
- **Verify:** `grep -n -- '--header-' candidate.txt` — two lines, values identical to original L21–22.
- **Disposition:** DISPOSITIONED (P9, ruling 2).

### 6. Text translation

- **What:** The documentation body is translated throughout (the TRANS-UNANCHORED spans inside B3 and B8, each verified line by line against the mirror for this README): the introduction (candidate L36–42), the component information section (L46–57), the design information tabview with its heading-level and table samples (L62–111), and the ribbon usage instructions (L84–107). The collapsible labels are translated (コードを表示 / コードを閉じる, candidate L118). No CONTENT-STRING signature fired: the theme's CSS contains no `content:` strings (the only `content:` matches are `justify-content`). Korean survives in the candidate in exactly three roles, all recorded: the credit block's original-title field (candidate L18, a quotation), the header variables (section 5, ruling 2), and the porter comment's Korean theme-name line (candidate L125, section 10). R5 glyph-form conversion: none — the source is Korean and no retained string changes glyph form.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored group is where a silent deletion would hide, which is why each block was read individually rather than waved through as a class.
- **Verify:** The pairs are diff.md's body sections in order; a Hangul scan of candidate.txt returns only candidate L18, L125–126, and L136–137.
- **Disposition:** Standing (the port itself); the survivals are dispositioned or quoted as recorded above.

### 7. Links

- **What:** The credit block's source link (candidate L22) reads `https://scpko.wikidot.com/theme:07k` — the host matches the original's recorded host in review/sources.tsv (scpko.wikidot.com), and no defect arises. The usage example (candidate L42) is a blockquoted live-form include `> [[include :scp-jp:theme:07k-jp]]`: the port repointed the branch but left the plain name, and the population sweep completed it to the posting name (per-theme record). The component list's plain page links (candidate L55–57) name component pages without a branch prefix, the same form as the original's list; they resolve on the local wiki. No prose link in the candidate targets a KO-wiki page.
- **Why:** P11 under the dead-reference evidence standard: a link takes the JP counterpart or the serving original; the source link's job is to reach the original, and it names the host that serves it.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit; `grep -n 'theme:07k' candidate.txt` shows the -jp self-reference and the scpko source URL only.
- **Disposition:** Applied; no open link item in this file.

### 8. Structure

- **What:** The localize.md closing rule holds for the stylesheet: the CSS body moved as one block (similarity 0.932) with its internal order, variable names, and selectors preserved, and the JP additions sit outside it (the head frame before, the license box after the gate's body). Three structural deviations, each with its ground stated. (a) The component include set is duplicated inside the gate (section 2) — the original carries it once. (b) The tail furniture swap (B8): the info pair and the bare Rate are out, the license box is in (section 1). (c) The documentation exhibits proper — the tabview, its two tabs, the heading/table samples, the ribbon exhibit — are present on both sides in the same order, translated; an exhibit census finds nothing else dropped or replaced, so the R3 question (sanctioned replacement vs silent deletion) arises only for the credit exhibits, whose replacement is the credit block itself (P3).
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond, with the section 1/2 differences named above.
- **Disposition:** Standing; no structural deletion beyond the recorded furniture swap, no class I item for this theme.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered. The only byte-level formatting delta is at the tail: the original's last line carries no trailing newline and the candidate's does.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (reindent_blocks: 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation group, at the head of the code block (candidate L124–133): a bilingual provenance comment naming the theme and revision ("건설자 / Site-07K Theme — Ported for SCP-JP (theme:07k rev 3 on scpko)"), stating that the KO components have no SCP-JP counterparts and were replaced by JP equivalents or translator's notes, and that the fonts were replaced by Google's Gothic A1; followed by two one-line comments ("日本語フォント (JP localization)" and the substitution note), the substitution note then repeated verbatim a second time (candidate L131 and L133). The skeleton's "none" for this section does not survive contact with the bytes and is corrected here: the COMMENT-TEXT span rides inside B3.
- **Why:** R2: porter-added text is part of the change record. This comment is also evidence in section 4's flag: its substitution claim is the statement the delivered stacks contradict, and its component claim needs one qualification — the components were in fact repointed to existing JP ports (section 2), not replaced by notes.
- **Verify:** Read candidate L124–133.
- **Disposition:** Standing (the duplicated one-line comment is recorded as a minor blemish, not edited).

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section: (1) T1's three errors — pseudo-ref ×2 (the draft-host delivery lines, class (iii), section 3) and hotlink ×1 (the scpko.wdfiles asset form, class (ii), section 4) — no class (i) error stands. (2) The render row's items, all environment or preview layer, not charged to the candidate: the runtime-hotlink site-theme chain plus scpko.wdfiles.com (KB-40/KB-41 family, class (ii)) and the sample credit-modal errors (KB-32, ruling 5). (3) Ledger §(c3): P5 DISPOSITIONED (class (ii) / KB-58), P7 DISPOSITIONED (recorded without a display-affecting mark; T4 bar), P9 DISPOSITIONED (ruling 2, section 5). Carried openly as flags, not dispositions: the GongGothic stacks (section 4), the unnamed creator (section 1), and the raisa-ribbon parameter divergence (section 2).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3); three flags recorded with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 232): exit 1, 3 errors / 0 warns / 1 info (pseudo-ref×2, hotlink×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO1)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 248): FINDINGS jointly, display-affecting findings 3; of these, the info-module residue reached the §(e) register as item 99 and the rest are the §(c3) pattern dispositions. (d) The FIX5 closure re-derived for this package: the supplement (row 99) says FIX5-INFO removed the info-module residue; the commit (9a1c86a) removes exactly the six info-pair lines (the pair had already been repointed to `:scp-jp:` forms by then), and the current candidate contains no `info:start`, `info:end`, or `module Rate` (grep, section 1) — one rating area remains, the rate-bearing preview credit block. The fix is present and complete in the bytes. (e) A brace-depth scan of the delivered code block (candidate L119–387) ends at depth 0 with no negative excursion. (f) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +137/−113 in 8 change blocks; the GNU-diff count of the same pair is 250 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:07k-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 249 as re-judged by supplement row 99; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 99 re-derived (ledger class C)

At ledger time the candidate rendered two rating areas: the JP preview credit block (rate-bearing) at its head and the EN-style info module the port had carried over from the original (by then repointed to `:scp-jp:info:start`/`end`), because the original's credit furniture was exactly that info pair (original L280–284) beside a bare Rate. The port removed the bare Rate but left the info pair; the ledger charged the pair (item 99 [C]: "Two credit/info furniture sets render on one page"), noting the pattern-3 exception covers labelled pairs only, which this was not. FIX5-INFO (commit 9a1c86a) deleted the pair's six lines and nothing else in this file; the supplement re-judged the item FIXED. The current bytes confirm the closure and its completeness: no info include, no bare Rate, one credit block. One side effect of the deletion is recorded in section 1: the info body was the candidate's last in-text naming of the creator, thd-glasses, and the credit furniture that replaced it does not carry the name.

### The usage example's posting name

The usage example at candidate L42 as built read `> [[include :scp-jp:theme:07k]]`: the porting wave's repoint changed the branch prefix from `:scpko:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:07k-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-07K items 1–3 — font loads, creator name, raisa parameter (landing 05dd295, 2026-11-17).** `FIX-07K.md` records three repairs, all in commit 05dd295 (review+pages: U-7 and R-fix-3 packages; foundom, navla, 07k repairs). (1) The original's two jsDelivr `@font-face` blocks (GongGothicMedium/Bold) were restored byte-identically at the head of the delivered code block (candidate L120–132), the three Google Fonts `@import`s removed, and the porter comment reworded to say what the bytes do; the two duplicate substitution notes and the orphaned JP-font header went with the imports. (2) The 著作権者 field (L19) and license-box `author=` (L397–398) were set to `[[*user thd-glasses]]` / `thd-glasses`, the established form for this author. (3) The raisa-ribbon head copy's `side=right` became `side=1`, matching the in-gate copy and the original. 1 file, 19 insertions / 12 deletions.

**This refresh's candidate edit — the L400 license-box source note (flagged in FIX-07K.md's Adjacent observation).** FIX-07K recorded that the note at candidate L400 still said the KO-side webfonts were "re-hosted on the candidate page or replaced with Google Fonts equivalents", which item 1's repair made false: the GongGothic load is the original's jsDelivr URL carried over unchanged. This refresh applies that one-line correction to `review/07k-jp/candidate.txt`: the font clause now reads `KO 側のウェブフォント（GongGothic）は原語版の jsDelivr 読み込みをそのまま引き継いでいます`, with the image-licence sentence and the rest of the line untouched. **This is a candidate edit made by this lane**: after recopy, `candidate.txt` differs from the canonical `pages/theme:07k-jp.txt` by this single note line and nothing else; it is flagged prominently in the REFRESH3-C report. The verdict stamp is computed from the canonical file by the generator and is unaffected by this candidate-only edit.
**Coordinator landing note (refresh-3 slice C).** The one-line correction above was applied to the canonical `pages/theme:07k-jp.txt` itself in the slice-C landing commit, so `candidate.txt` is again byte-identical to the candidate page and the stamp regenerated at landing is computed from the corrected bytes. The lane's candidate-only framing above is the pre-landing state it reported.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-07k-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The three JP components the theme includes (component:centered-header-sigma-9, component:toggle-sidebar, component:raisa-ribbon) are shared campaign ports, not files of this theme's change set. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the Stage 2 KO1 integration (18280b3) produced the port (translation, delivery relocation, credit block, license box, and, as later found, the leftover info pair and the unconverted font stacks); FIX-CREDIT-D (1869877) normalized the translator field across all candidates; FIX5-INFO (9a1c86a) removed the info pair (item 99); and the usage-example sweep (b5cb724) completed the example's posting name. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 99; GOSIGN2-LEDGER-SUPPLEMENT.md row 99; REPORT-GOSIGN2-FIX5-INFO.md (07k section). The go-sign re-run over that record is what the Status block certifies.

## License and attribution

- **Title:** 건설자 테마
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/theme:07k — revision 3
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
