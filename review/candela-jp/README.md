# Review package — theme:candela-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:candela-jp — origin CN, population #173 [GOSIGN2-LEDGER (b) row 173]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 155e4559259cf40efbca28a807d799a1a56d3bbc49e3bf6ad0c8d1f21873112b); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 12 errors / 0 warns / 1 info (pseudo-ref×10, hotlink×2); standing classes dispositioned in register c1 [T1-ROWS row 198; GOSIGN2-LEDGER (b) row 173]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 515–525px@320/375 on page and sample (+ 853–854px@768 on sample); page hidden-* cluster confined to webkit-320, whose only hotlink host is http.cat = transient 503 capture, not a result; sample credit-modal (preview-form) + sidebar-not-opening at webkit-768. [RENDER-ROWS-2 (RENDER-S2-E (CN3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN3))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 172, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 172]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 173]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:candela-jp.txt sha256:155e4559259cf40efbca28a807d799a1a56d3bbc49e3bf6ad0c8d1f21873112b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 173) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×10 and hotlink ×2 at the 2026-11-16 baseline (the hotlink pair was then removed by the FIX3-PC repair, section 3; the pseudo-ref lines are class (ii)); the render row's items (overflow readings, the http.cat capture artefact, credit-modal preview form, sidebar reading, section 11); T4's two counted findings, whose delivery premise the FIX3-PC repair superseded (sections 3 and 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:candela | theme:candela-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 6 (first translation; the candidate's credit block records 初訳時参照リビジョン: 6) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-candela.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:candela-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 341 lines / 10,690 bytes | 390 lines / 13,868 bytes |
| SHA-256 | 2f47ff2fc6fa00fb98b9895eaaa1192876c697096d97bce7160cd5f06f1f3d6d | 78c4772111fcea40f0b84b2a68ef81d38fbf15bfb44b8f05e79da8646e96d7bf |

Wave history: the candidate was created by the Stage 2 CN3 integration (commit 6a8eb9d, the LOCALIZE-S2-D wave's port) and has exactly one later commit, db3738b, under which two GOSIGN2 repairs landed for this file: the FIX2-INCLUDE rewrites (foreign includes to verified JP counterparts) and the FIX3-PC delivery rebuild (REPORT-GOSIGN2-FIX3-PC.md: the CN granular imports replaced by the JP bundle plus the restoration block, section 3). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

Candela is a variant theme stacked on two base themes (Parallel, then Lumina Crash), and its port is dominated by that dependency. The original imports the CN Parallel fragment's code/1 and code/3 granular deliveries and the EN Lumina local--code; the candidate imports the JP candidates' deliveries instead — and because the JP Parallel port ships as a single bundle whose final variable state differs from the CN granular sequence, the candidate carries an explicit `:root` restoration block that reproduces the CN sequence's final computed state, with a porter comment explaining the whole construction and a script-verified cascade parity claim (0 differing variables) in the FIX3-PC report. The rest is the standard port: bare Rate deleted, preview credit block installed, usage includes repointed to the JP branch and, by the usage-example population sweep, completed to the JP candidates' posting names (per-theme record), the header variables moved from `:root:lang(cn)` to `:root:lang(ja)` and translated, Noto Sans SC swapped for Noto Sans JP, prose and exhibits translated. Measured churn (diff.md, the generator's difflib count with autojunk off: +107/−58, 165 changed lines in 26 change blocks; a GNU-diff count gives 141 changed lines — the difference is alignment choice, not content). The one record-versus-bytes conflict in this package matters: T4's row charges the candidate with still importing the CN/EN deliveries live, which was true when the localize lane ran and is no longer true after FIX3-PC; the package follows the bytes and flags the stale charge (sections 3 and 11).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 26 change blocks — 18 specific (69.2%), 8 heuristic (30.8%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 12 |
| DRAFT-HOST | 7 |
| DELIVERY-MOVE | 6 |
| ESCAPED-INCLUDE | 4 |
| INCLUDE-REPOINT | 4 |
| TRANSLATION-ANCHORED | 3 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| GLYPH-FORM | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| RESTORATION | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 8 heuristic blocks are the TRANS-UNANCHORED prose translations of the usage and exhibit text (section 6), each verified line by line; the DELIVERY-MOVE primaries are the base-delivery composition of section 3, not relocations of the theme's own CSS; B22 carries four labels for one fact (the `:root:lang` header block: moved channel, glyph forms, header variables, anchored translation — sections 5 and 6); B26 (RESTORATION) is the tail module's parameter region, where the candidate's own CSS keeps the original's `{$classic}`/`{$narrow}` substitution structure (section 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:candela-jp; original theme:candela on scp-wiki-cn at reference revision 6; candidate `pages/theme:candela-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind: K5b-3 — a composition kind, because the candidate's delivery names two other population candidates' deliveries, section 3 and the change-set note; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the original opens with the gate (L1) and its delivery module (L3–7); the candidate opens with the delivery module (L1–14), the interwiki-style frame (L16–19), and the localized gate at L21.
- **Why:** Section 0 declares the provenance route and the composition, so the delivery sections are read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for candela-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery composition is recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module rate]]` under a 评分： label in a right-aligned div (original L9–13), with no credit prose. The candidate deletes it and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L23–32) carrying the eight ruling-3 fields (title 標準カンデラ テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 标准烛光 版式; 著作権者 Dr Hormress; 作成年 2024; 初訳時参照リビジョン 6; the source link, naming scp-wiki-cn.wikidot.com/theme:candela, the recorded host, which serves the original). The CREDIT-PROSE block is the translated intro paragraph that follows (candidate L34), which keeps the original's base-theme links as absolute URLs (section 7). T7 credit-module CSS: none on the page — the theme's own CSS lives in its tail module and carries no credit rules; credit styling is the base layers'. License box: none on either side, and none added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module rate' candidate.txt` returns nothing; read candidate L23–32 against the eight fields.
- **Disposition:** Applied; no credit item was charged against this theme.

### 2. Includes and components

- **What:** The usage examples are the include record (blocks ESCAPED-INCLUDE ×4, INCLUDE-REPOINT ×4): the four code blocks teach the three-line application form, and every line is repointed from `:scp-wiki-cn:` to `:scp-jp:` and kept escaped. As built, that repoint changed the branch prefix but kept the plain slugs, so the twelve lines named pages that do not exist on scp-jp: `:scp-jp:theme:parallel` with its `redstone=*` parameter, `:scp-jp:theme:lumina`, and `:scp-jp:theme:candela` with its `classic=*` / `narrow=*` parameter forms (candidate L39–65, in four triples at L39–41, L47–49, L55–57, and L63–65). The usage-example population sweep has since completed each name to its posting form — `:scp-jp:theme:parallel-jp`, `:scp-jp:theme:lumina-jp`, and `:scp-jp:theme:candela-jp` — at the same lines (per-theme record). These are the FIX2-INCLUDE rewrites (commit db3738b: foreign includes to verified JP counterparts, this theme one of its two). The credit includes (section 1) and the interwiki-style include (section 3) complete the candidate's include list; every include names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. As built, the repoint satisfied the branch half of that rule only; the sweep's completion of the three names is what brings the examples under it. parallel-jp and lumina-jp are population candidates whose existence the FIX2-INCLUDE wave verified, candela-jp is this candidate itself under its posting name, and the parameter forms survive because the JP base ports accept the same parameters (the candidate's own tail module implements `{$classic}`/`{$narrow}`, section 8). Ruling 4 is not engaged: the base themes were already ported as their own candidates, not ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the credit pair, the frame, and the twelve escaped usage lines, all `:scp-jp:`.
- **Disposition:** Applied (FIX2-INCLUDE, with the posting names completed by the population sweep); no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery is a three-layer composition, and it is the section where the prose record and the bytes disagree. The original's head module imports the CN Parallel fragment's granular deliveries (`fragment:parallel/code/1` and `code/3`, original L4–5) and the EN Lumina delivery (`scp-wiki.wdfiles.com/local--code/theme%3Alumina/1`, original L6). The candidate's head module (L1–14) imports, all from the draft host: the JP Parallel candidate's bundle `local--code/theme%3Aparallel-jp/1` (L3), the JP Lumina candidate's delivery `local--code/theme%3Alumina-jp/1` (L4), and its own `local--code/theme%3Acandela-jp/1` (L5, SELF-DELIVERY); the interwiki-style frame at priority 1 names the same own delivery (L16–19). Because the JP bundle's last bare `:root` carries the deep-diamond palette where the CN granular sequence ended in the redstone state, the candidate adds an explicit restoration block (`:root`, L7–13) resetting the five affected variables to the CN sequence's final values, and a two-part porter comment (L2, L6, section 10) explaining the construction and pointing at the FIX3-PC report. That repair is REPORT-GOSIGN2-FIX3-PC.md (2026-11-17): it replaced the two CN imports with the bundle import plus the override, verified computed-cascade parity by script (0 differing variables between the CN and JP cascades), and re-ran the checker (hotlink 2 → 0; total errors 12 → 11, the new bundle import being one expected draft-host pseudo-ref). **The record conflict:** LOCALIZE-ROWS row 172, written when the localize lane ran, charges this candidate with the CN/EN imports still live at L3–5 and calls the repair a posting prerequisite; the ledger §(c3) line dispositions the theme's P4 as "delivery class (ii): original-state CDN delivery". Both texts describe the pre-FIX3-PC state. The bytes at the FIX5 head — and already at db3738b, the commit the verdict stamp is computed against — carry the JP composition above, so this package documents the delivery as repaired and flags the two record texts as superseded, rather than repeating a charge the file no longer bears.
- **Why:** P4/T9 (delivery from JP distributions) with KB-14 (cross-theme imports name the JP port candidates): parallel-jp and lumina-jp are this theme's bases, so their JP candidate deliveries are the correct targets. The restoration block is the parity mechanism the coordinator's adjudication chose (parity inside candela, without restructuring parallel-jp). The draft-host form of all three imports is KB-41, class (iii).
- **Verify:** Read candidate L1–19; `grep -n 'scp-wiki-cn.wikidot.com/fragment\|scp-wiki.wdfiles' candidate.txt` returns nothing; the FIX3-PC report's parity table is the cascade evidence.
- **Disposition:** FIXED (FIX3-PC, landed in db3738b); the draft-host forms DISPOSITIONED (class (iii)); the T4 row's delivery charge flagged as superseded by the repair.

### 4. Fonts and assets

- **What:** Fonts (block JPFONT-LOAD): inside the theme's own CSS, the candidate swaps the original's Noto Sans SC load for Noto Sans JP at the same weights (original L88 → candidate L108, in the source-code exhibit; the same swap is in the applied module). T4 row 172's type-7 item (a dead font import, glyph risk) was recorded against the localize-time state; the page-level load now names the JP family, and the ledger §(c3) line dispositions P7 as recorded without a display-affecting mark. Assets: the candidate's `--header-logo` names its own spacelogo.png on the draft host (candidate L116 region, in the `:root` block beside the header variables); the warning-panel exhibit names a basalt-jp asset on the draft host (candidate L70). No other image is the theme's own; the base layers' assets travel with their deliveries (section 3).
- **Why:** P7/T5 with KB-16 (the font load gap): a Simplified-Chinese font load cannot serve Japanese text, so the family changes with the language. P5/KB-17 for the asset hosts: the theme's own logo is re-hosted to the JP side (draft form).
- **Verify:** `grep -n 'Noto Sans' candidate.txt` — JP only; `grep -n 'wdfiles' candidate.txt` against the lines above.
- **Disposition:** Font swap applied; the draft-host asset URLs DISPOSITIONED (class (iii) draft form; posting rewrites them to the production host).

### 5. Header, sidebar, and site furniture

- **What:** One block (B22, HEADERVAR with GLYPH-FORM): the theme's header variables move from `:root:lang(cn)` (original L89–92) to `:root:lang(ja)` (candidate L109–112) and are translated — `--header-title` 深空探索部 → 深宇宙探査部 (a wording choice, not a glyph conversion: 探索 becomes 探査）, `--header-subtitle` 控制 - 收容 - 保护 → 確保 - 収容 - 保護 (the first word also changes, to the JP motto's settled form; the rest is R5 glyph-form conversion of retained strings). The `--header-logo` beside them is section 4. No sidebar or topbar rule changes: the furniture is the base layers'.
- **Why:** P9/T6 (header variables overridden for JP) with the lang-scope switch that makes them apply on this site at all; KB-18 for the reader-visible strings; R5 names the glyph-form part separately from the translation part, which is why both are stated.
- **Verify:** Read original L89–92 against candidate L109–112.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The usage prose and the custom-element exhibits are translated throughout: the intro (CREDIT-PROSE, candidate L34), the four application instructions, the custom-element section heading and its exhibits (the warning panel and the remaining sample furniture), and the source-code exhibit's labels. The 8 heuristic blocks are this prose (TRANS-UNANCHORED primaries), each verified line by line against the mirror for this README. Chinese survives in the candidate only as quotation: the credit block's original-title field (candidate L27) and the head comment's references to the CN deliveries (candidate L2, L6, section 10). R1 in-CSS text: the theme's CSS comments (`/* CANDELA Theme */` and its companions) are English in the original and travel unchanged; the string-valued header variables are section 5.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings).
- **Verify:** The pairs are diff.md's body sections in order; a Han-character scan of candidate.txt outside the credit field and the head comments returns only translated text's shared kanji.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The intro paragraph's two base-theme links are absolute URLs (candidate L34): Parallel names scp-wiki-cn.wikidot.com/theme:parallel (the original's own page, on its recorded host) and Lumina Crash names scp-wiki.wikidot.com/theme:lumina (the EN original). Both serve; neither is a JP counterpart link, because the sentences describe the originals the theme is a variant of, while the *application* form beside them names the JP candidates (section 2). The credit block's source link (candidate L31) names scp-wiki-cn.wikidot.com/theme:candela — the recorded host, which serves the original. The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) finds no divergence and no broken link.
- **Why:** P11: prose links take the JP counterpart or the serving original; these are the serving-original form, used where the text is about the originals themselves.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the three links above, plus the delivery and asset lines of sections 3–4.
- **Disposition:** Standing; no link item was charged against this theme.

### 8. Structure

- **What:** The closing rule holds in the large: the page's section order (delivery, credit, intro, usage, custom elements, source code, applied module) matches the original's, and the theme's own CSS keeps its internal order and its `{$classic}`/`{$narrow}` substitution structure (block B26, RESTORATION-labeled for its tail span) — the parameter blocks the usage examples invoke are the same ones the original's module carried. The head restoration block (section 3) is an addition at the head, not an interleave. Exhibit census: the four application code blocks, the warning-panel exhibit, and the source-code collapsible are present on both sides in the same order; nothing was dropped or replaced, so the R3 question does not arise.
- **Why:** The closing rule exists so follow-up diffs apply cleanly; R3's census is the check that a composition change (section 3) did not absorb an exhibit change.
- **Verify:** Compare `grep -n '\[\[div class="code"\]\|\[\[code\|\[\[module' original.txt candidate.txt` — the sequences correspond, with the candidate's frame additions at the head.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotations, both CSS comments in the head module, both load-bearing. (1) Candidate L2: the dependency note — the parallel layer reads the JP candidate bundle, the restoration block after the imports reproduces the variable state the CN code/1+code/3 sequence ended in (and why: the bundle's own final `:root` is the deep-diamond palette, which would change the link and header accents), lumina is repointed to the JP candidate, and items still needing a JP port are referred to the campaign MANIFEST. (2) Candidate L6: the restoration note — the five bundle values being overridden are named with their numbers, the one variable that needs no override is named with its ground (lumina overwrites it identically), and the placement after all `@import`s is explained. There are no `[!-- ... --]` notes in the prose. The skeleton's COMMENT-TEXT count of 1 understates the pair (the two comments sit in one block); the bytes carry both, and both are recorded here.
- **Why:** R2: porter-added text is part of the change record, and these two comments are the only in-file explanation of the theme's delivery design — a reviewer who skips them cannot judge section 3.
- **Verify:** Read candidate L2 and L6.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's baseline twelve errors: pseudo-ref ×10, class (ii) — the candidate's own draft-host local--code lines (its three head imports, the frame, and the base candidates' draft deliveries named in the usage and delivery lines) — and hotlink ×2, the two CN fragment imports, which the FIX3-PC repair then removed outright (re-check: hotlink 2 → 0, total 12 → 11, the bundle import adding one expected pseudo-ref). The stamp's T1 line is the 2026-11-16 baseline and is quoted as such in section 12. (2) The render row's items, environment or capture layer, not charged to the candidate: the page-overflow readings (515–525px@320/375 on page and sample, 853–854px@768 on the sample — recorded readings on a wide base composition); the page's hidden-* cluster confined to webkit-320, whose only hotlink host is http.cat (KB-44: a transient Wikidot 503 capture, not a result); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the sample's sidebar-not-opening at webkit-768. (3) T4's two counted findings (LOCALIZE-ROWS row 172): the delivery charge, superseded by FIX3-PC as argued in section 3 (the ledger §(c3) line's "original-state CDN delivery" disposition text describes the same pre-repair state and is flagged with it); and the type-7 font item, closed by the section-4 swap and the ledger's P7 disposition. The theme's determination is PASS and this package does not re-open it; the flag is the documentation doing its job, because a reviewer who reads row 172 against the current file would otherwise conclude the repair never happened.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; and a disposition text that no longer matches the bytes is itself a finding to record.
- **Verify:** Each item names its deciding record above; the delivery item's evidence is candidate L1–14 against original L3–7.
- **Disposition:** DISPOSITIONED (items 1–2); item 3's delivery half flagged as a superseded record, its font half DISPOSITIONED.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 198): baseline exit 1, 12 errors / 0 warns / 1 info (pseudo-ref ×10, hotlink ×2), all class (ii) at the baseline; the FIX3-PC re-check (REPORT-GOSIGN2-FIX3-PC.md) records 11 errors with hotlink 0 after the delivery repair. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN3)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 172): FINDINGS jointly, display-affecting findings 2 (the delivery and font items of section 11(3)); the ledger §(c3) line records the theme's P4 and P7 outcomes as DISPOSITIONED, with the delivery text flagged in section 3 as describing the pre-repair state. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +107/−58 in 26 change blocks; the GNU-diff count of the same pair is 141 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:candela-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 173; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The twelve usage-example lines (candidate L39–41, L47–49, L55–57, and L63–65, four triples) as built read `:scp-jp:theme:parallel` (with its `redstone=*` parameter), `:scp-jp:theme:lumina`, and `:scp-jp:theme:candela` (with no parameter at L41, with `classic=*` at L49, with `narrow=*` at L57, and with `classic=* | narrow=*` at L65): the porting wave's repoint changed the branch prefix from `:scp-wiki-cn:` but left the plain names, so each line named a page that does not exist on scp-jp — the two cross-references no less than the self-reference (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed each name to its posting form — `:scp-jp:theme:parallel-jp`, `:scp-jp:theme:lumina-jp`, and `:scp-jp:theme:candela-jp` — at the same lines (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), twelve of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; this theme's record is larger, and sources.tsv marks it K5b-3 for exactly that reason. The candidate's delivery names two other population candidates — `pages/theme:parallel-jp.txt` and `pages/theme:lumina-jp.txt` — whose deliveries are part of this theme's working composition (the FIX3-PC parity computation ran over their delivered CSS as well as this file's); each has its own package in this documentation pass, and neither was edited for candela. `pages/theme-decoration-sample-candela-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). The original-side sample `pages/theme-decoration-sample-candela.txt` is the campaign's mirror-side fixture, likewise outside the port.

## License and attribution

- **Title:** 标准烛光 版式
- **Author:** Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:candela — revision 6
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
