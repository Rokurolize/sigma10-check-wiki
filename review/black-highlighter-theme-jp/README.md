# Review package — theme:black-highlighter-theme-jp (EN → JP, kind K6: production-matched migration)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:black-highlighter-theme-jp — origin EN, population #5 [GOSIGN2-LEDGER (b) row 5]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 5]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 3 warns / 1 info (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 5; GOSIGN2-LEDGER (b) row 5]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — preview-notice rating widget「価:0」missing, mobile overflow 337–419px, sidebar x=0, sample credit-modal; two network-caused first runs recovered. [RENDER-ROWS-1 (RENDER-A row 5)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 5)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 6, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 6]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 5]
- Computed against: canonical commit 19ae059fb6dc405206a7c26de53dd4264f50dc97; candidate file pages/theme:black-highlighter-theme-jp.txt sha256:90a09217f2a75130bd4db4d2866ff213288606afd6c21153adb9f68876890bd7; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 5). The sources.tsv row's own verdict column also reads PASS |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×1; the render row's rating-widget, overflow, sidebar, and credit-modal items (ledger (c2), section 11); T4's findings per the ledger (c3) line (P3 FIXED; P10, lane-recorded severity / specimen class) |
| Recorded tension | The candidate's credit block records 初訳時参照リビジョン: 135 and 改訳時参照リビジョン: 135 — the same number twice, in a block that also dates the first translation to 2019, while rev 135 is the 2026 re-translation reference. The phase17-diff file that will actually be applied to the production page adds only the 改訳 line. Per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:black-highlighter-theme | theme:black-highlighter-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 135 (re-translation reference; rev_created_at 2026-11-06). Two reference revisions are recorded for this theme: the first-translation reference and this re-translation reference (review/sources.tsv) | — |
| Source of this copy | Campaign mirror store, FETCH-REGEN 2026-11-17 (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:black-highlighter-theme-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 240 lines / 6,181 bytes | 315 lines / 10,001 bytes |
| SHA-256 | 4c9aed07acb14f40db2b698d5a17afd89792beac36b5460bfb171fbe72116a47 | 90a09217f2a75130bd4db4d2866ff213288606afd6c21153adb9f68876890bd7 |

**Kind K6 provenance (read this before the diff).** This theme breaks the batch's pattern. SCP-JP production already has a theme:black-highlighter-theme page — Black Highlighter was translated to JP in 2019 and has lived there since — and the TSV records the production page as matching (exist: 一致）. The candidate in this package is therefore not a fresh port: it is the Sigma-10 migration candidate for an existing JP page, descending from the JP production lineage (its translator credit is the human translator's, section 1), and the migration's actual deliverable is a separate small file, `pages/phase17-diff-black-highlighter-theme-jp.txt`, which applies the migration to the production page (section 12 and the change-set section). The original.txt in this package is the EN page at rev 135, the re-translation reference the migration was checked against (the Phase 22 wave, commit d2a9dc0, incorporated or decided the pending reference-revision drifts, rev 130 → 135 for this theme). Every count below must be read against that baseline: much of the diff is the JP lineage's own seven-year history, not migration change.

Wave history: Phase 17 (8dcac74, reference revisions recorded), Phase 22 (d2a9dc0, the rev 130 → 135 drift decided), the gosign2 T1 fix wave (b816e10, credit fields/furniture), FIX-CREDIT-C (5c32672, the translator pair completed in rows 1–22 credit blocks), and FIX3-A1 (19ae059, LOCALIZE-A rows 1–11 fixes; the stamp's computed-against commit).

## Summary

Black Highlighter is the base theme half the modern SCP ecosystem layers over, and on JP it is a production page, not a port candidate. The migration candidate's real changes against the EN rev-135 reference are few and identifiable: the delivery re-homes from the EN CDN (`cdn.scpwiki.com/theme/en/…`) to the JP distribution (`scp-jp.github.io/Black-Highlighter/…`); the credit block is completed to the ruling-3 form while keeping the production page's own 著者 line and its human translator's name; and the JP page's three deliberate CSS corrections (history-table, credit-dialog, top-bar) are carried and marked as JP corrections in their comments. The production deliverable is smaller still: the phase17-diff adds exactly one credit line （改訳時参照リビジョン: 135) to the live page, the base CSS being CDN-followed and the JP corrections being kept by decision. Measured churn against the EN reference (diff.md, the generator's difflib count with autojunk off: +228/−162, 390 changed lines in 57 change blocks; a GNU-diff count of the same pair gives 297 changed lines) mostly measures lineage distance, not migration work — this package says so wherever the counts appear.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 57 change blocks — 19 specific (33.3%), 33 heuristic (57.9%), 5 residue (8.8%), 0 skipped. The heuristic share is high for the K6 reason: the classifier's translation anchors assume a fresh port, and a production-lineage page pairs loosely with the EN reference. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 32 |
| TRANSLATION-ANCHORED | 11 |
| EXHIBIT-RESTRUCTURE | 5 |
| INCLUDE-REPOINT | 4 |
| CSS-BODY | 3 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| IFTAGS | 1 |
| TASL-FIELDS | 1 |
| T7-CREDIT-CSS | 1 |

Adjudication for this README: the five residue blocks resolve as the frame-wrapper difference (B4: the original wraps its frames in a hidden div, the candidate does not; section 3), three alignment artefacts in the interleaved documentation/CSS regions where the JP lineage and the EN text do not pair line-for-line (B8, B20, B28), and one block (B7) where the candidate's CSS module carries JP-lineage rules with no counterpart at the EN position. The EXHIBIT-RESTRUCTURE primaries sit in the same lineage zones and adjudicate the same way (section 8). After adjudication no block is left unexplained, but the honest summary of this classification is that block-level pairing is weak evidence for this package; the deciding records are the phase17-diff and the ledger, and the sections below lean on them.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:black-highlighter-theme-jp; original theme:black-highlighter-theme on scp-wiki at re-translation reference revision 135; candidate `pages/theme:black-highlighter-theme-jp.txt`. Provenance route: **K6** (sources.tsv kind: branch-original, exist: 一致） — the R4 question is live here and is answered by adoption: the JP production page is the candidate's base, the EN rev-135 text is the reference it was re-checked against, and the migration deliverable is the phase17-diff file. The candidate opens with its delivery module (candidate L1–4), its two frames (candidate L6–14, unwrapped — the original wraps its pair in a hidden div, original L10–21), and the gate `[[iftags +テーマ -nobhl]]` (candidate L16; the `-nobhl` exclusion carried from the original's gate).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; for K6 the baseline declaration IS the section's content, because a reader who assumes a fresh port will misread every number in this package.
- **Verify:** The sources.tsv row for black-highlighter-theme-jp (kind K6, the production note, the two recorded reference revisions); `sha256sum original.txt` against the Provenance table; read `pages/phase17-diff-black-highlighter-theme-jp.txt` (1,161 bytes) for the deliverable's own account of itself.
- **Disposition:** Standing (the route itself, decided at Phase 17/22 and recorded in the TSV).

### 1. Credit and attribution

- **What:** The candidate carries a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L95–106) whose fields mix the production lineage and the normalized form: タイトル Black Highlighterテーマ; **翻訳責任者： YS_GPCR** — the live JP page's human translator, preserved (the standing attribution rule: human translator names stay where they match the live JP creator; the "AI" attribution used by fresh ports would be false here); 翻訳年 2019; **著者：** ©︎Woedenaz & Croquembouche (the production page's own field, carried); 原題 Black Highlighter Theme; **著作権者：** Woedenaz、Croquembouche (the normalized field, added — so the block carries both 著者 and 著作権者 lines naming the same pair, the terminology wobble LOCALIZE-A row 6 charged, visible in the bytes as a doubled field rather than a contradiction); 作成年 2019; 初訳時参照リビジョン: 135; 改訳時参照リビジョン: 135; and the source link (candidate L105) naming `scp-wiki.wikidot.com/theme:black-highlighter-theme` — the original's recorded host. LOCALIZE-A row 6's pattern-3 charges （元記事リンク absent; 翻訳責任者/翻訳年/初訳時参照リビジョン missing) describe the block BEFORE the credit waves: FIX-CREDIT-C (5c32672) and FIX3-A1 (19ae059) completed it, and the current bytes have every field — the ledger (c3) line's "P3 FIXED (checker-verified)" is accurate for the documented candidate. The revision pair is the exception, recorded in the per-theme record: both revision fields read 135, which cannot both be right against the block's own 2019 first-translation date and the phase17-diff's rev 130 → 135 account. License box (T4): neither side carries one; BHL's license substance is its font/OFL prose (candidate L296: all fonts under SIL Open Font License 1.1), carried in the body.
- **Why:** P3/T1 with the K6 rider: on a production-lineage page the credit record is the page's own history first and the campaign's form second; the waves that completed the form were right to keep YS_GPCR's name and the 著者 line, and this package records the one place the completion overshot (the duplicated revision number).
- **Verify:** Read candidate L95–106 against the phase17-diff's before-text (which shows the production block carrying 著者/原題/作成年 and no revision line).
- **Disposition:** FIXED (credit fields, by the credit waves; the ledger (c3) outcomes); the revision-pair duplication is recorded in the per-theme record as a surviving inconsistency under that disposition.

### 2. Includes and components

- **What:** Four INCLUDE-REPOINT blocks, all in the delivery frame set: the candidate's two interwiki frames name the JP distribution's stylesheets (section 3) where the original's name the EN CDN's. The documentation's component references are repointed to `:scp-jp:` forms or carried as bare `component:` names, and one ESCAPED-INCLUDE block is a usage specimen kept escaped. No live include names a foreign-wiki target; BHL is a base, not a component consumer, and its page carries no component includes beyond the frames.
- **Why:** P1 (KB-15): includes and frames name the JP supply.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every target is `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** BHL delivers as hosted CSS, not page code: the candidate's head module imports normalize.min.css and black-highlighter.min.css from `scp-jp.github.io/Black-Highlighter/css/min/` (candidate L2–3), and its two interwiki frames (priority 1 and 2, candidate L6–14) name the same addresses. The original's identical structure names `cdn.scpwiki.com/theme/en/black-highlighter/css/min/` (original L2–3) and wraps its frames in a hidden div (original L10–21) where the candidate leaves them bare (residue block B4). The rest of the candidate is inline module CSS (topology: module-css [16,93] and the tail corrections) — the JP page's own supplement layer, where the EN page carries its own. T1's single pseudo-ref error is the frame/import address form; there are no draft-host lines in this candidate at all (its one DRAFT-HOST-labeled block sits in the frame region and names the production github.io host — the label is the classifier's, the host is production, and no class (iii) rewrite is owed for it at posting).
- **Why:** P4 and P6/T3: the delivery host must be the JP distribution (the scp-jp.github.io BHL mirror is how JP's BHL is served, and dependent themes in this batch — theme:black-rain-jp — frame the same host). The phase17-diff states the production consequence: the base is CDN-followed, so upstream CSS drift needs no page edit.
- **Verify:** Read candidate L1–14 against original L1–21.
- **Disposition:** Applied; the frame-unwrap is standing (the frames function identically unwrapped on the JP form).

### 4. Fonts and assets

- **What:** BHL's fonts ship inside its hosted CSS (both distributions), so this page declares no font loads of its own in either file; the font license prose is carried in the body (candidate L296, SIL OFL 1.1). The theme's logo is served from the JP files host in both lineages (the phase17-diff's context line shows the production page's `scp-jp.wdfiles.com` logo address, unchanged by the migration). No asset address in the candidate names a foreign sandbox or a CN host.
- **Why:** P7/T5 and P5 are satisfied by the base's own supply here; there is no per-theme font or asset change to narrate beyond the delivery host of section 3.
- **Verify:** `grep -n '@import\|@font-face' candidate.txt` returns the two delivery imports only.
- **Disposition:** Standing.

### 5. Header, sidebar, and site furniture

- **What:** BHL IS the header/sidebar furniture layer; its JP corrections include the top-bar label rule (candidate L311–315, section 10). The render row's sidebar item (x=0) is section 11's. No `--header-title`-class override exists on either side.
- **Why:** P9/T6 names no override change here.
- **Verify:** The tail modules (candidate L301–315) against the original's tail in diff.md.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The documentation body exists in the candidate as the JP lineage's own translation, revised against rev 135: eleven TRANSLATION-ANCHORED and thirty-two TRANS-UNANCHORED blocks pair the EN reference's docs with the JP text. Unlike a fresh port, sameness here is not evidence of quality and difference is not evidence of drift: the JP text predates the reference revision by years and was re-checked at Phase 22, which decided the rev 130 → 135 drift (docs and delivery-source changes; the body CSS already followed). The stale-link charge from LOCALIZE-A row 6 (a `scptestwiki.wikidot.com` link at the row's L150, pattern 10) does not occur in the documented candidate: `grep -c 'scptestwiki' candidate.txt` returns 0 — whether removed by FIX3-A1 or absent from this lineage, the bytes are clean, and the item is dispositioned in the ledger as P10 (lane-recorded severity / specimen class).
- **Why:** P10 for the documentation; the K6 rider of section 0 for its reading.
- **Verify:** The grep above; the body sections of diff.md, read as lineage comparison rather than port diff.
- **Disposition:** Standing; the stale link is absent from the documented bytes.

### 7. Links

- **What:** The credit source link (candidate L105) names the original's recorded host (section 1). The body's reference links name the BHL project's own homes (the github.io distribution, the SIL license page at candidate L296). No `scptestwiki` address occurs (section 6), and no prose link targets a test or sandbox wiki.
- **Why:** P11: links name the serving original or the record's home; a stale test-wiki link is exactly what P11 exists to catch, and it is not here.
- **Verify:** `grep -n 'scptestwiki\|http://' candidate.txt` — the first returns nothing; the second returns only the SIL license URL carried from the original's own prose.
- **Disposition:** Standing; no dead link carried.

### 8. Structure

- **What:** The closing rule holds in its K6 form: the candidate preserves the production page's architecture (delivery module, frames, gate with `-nobhl`, supplement modules, documentation, credit, font-license prose, tail corrections, closing gate) and the EN reference's architecture corresponds section for section. The five EXHIBIT-RESTRUCTURE primaries and the residue blocks sit in the zones where the two lineages' texts interleave and adjudicate as alignment artefacts (class summary), with one substantive exception already charged (the frame unwrap, section 3). Nothing in the EN reference's documentation is missing from the JP page's structure; the migration adds no section and drops none.
- **Why:** R3 exists to force this adjudication; for K6 the census compares architectures, not lines, and they match.
- **Verify:** Compare the module/section sequences of the two files (topology in classification.json).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** No whitespace-only block pair and no re-indentation signature fires (0 and 0). This section is empty by measurement, stated with its ground.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the measurement is zero.
- **Verify:** classification.json's counts for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The candidate's annotations are the JP lineage's own correction comments, in English, inside its three tail CSS modules (candidate L302, L307, L312): "SCP-JP Wikidot page history: keep the history option row within the mobile viewport", "SCP-JP Wikidot BHL credit otherwise correction: keep the back link on one line in the otherwise credit dialog" (the T7-CREDIT-CSS block, B57 — credit-module CSS the JP page carries for the credit dialog), and "SCP-JP Wikidot black-highlighter-theme top bar labels: keep top navigation labels whole at narrow widths". Each names itself an SCP-JP correction and states the failure it prevents — the annotation discipline R2 asks for, kept by the production lineage itself. No `[!-- … --]` note exists (`grep -n '\[!--' candidate.txt` returns nothing).
- **Why:** R2: porter-added text is part of the change record; on a K6 page the "porters" are the JP page's maintainers across its history, and their comments are the record that these three rules are deliberate JP corrections — which is why the phase17-diff keeps them by decision.
- **Verify:** Read candidate L301–315.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's one pseudo-ref error: the frame address form of section 3; there is no class (i) error and no draft-host line in the file. (2) The render row's items, DISPOSITIONED in the ledger (c2) register: the preview-notice rating widget 「価:0」 missing, mobile overflow 337–419px, sidebar x=0, and the sample credit-modal — page-overflow in the recorded cross-cutting families (static credit replica fixed width, KB-33; preview chrome, KB-34), the per-theme figures matching the campaign-wide shapes; the register also records that two network-caused first runs were recovered, a measurement property, not a theme property. (3) T4's findings (LOCALIZE-A row 6): the credit item FIXED (section 1, with the revision-pair record); the stale-link item DISPOSITIONED (P10, lane-recorded severity / specimen class) and absent from the documented bytes (section 6).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 3 and 6.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 5): exit 1, 1 error / 3 warns / 1 info; the error is pseudo-ref ×1, section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS, lane RENDER-A): FAIL/FAIL with FINDINGS, the items of section 11(2), all dispositioned. (c) T4/T5 (LOCALIZE-A row 6): FINDINGS jointly, display-affecting findings 1, dispositioned as in section 11(3) and the ledger §(c3) line (P3 FIXED; P10 DISPOSITIONED, lane-recorded severity / specimen class). (d) The migration's own verification is the phase17-diff's premise, checkable in-repo: the production page matches its recorded state (TSV exist: 一致）, the upstream drift was decided at Phase 22, and the deliverable's diff is one credit line. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +228/−162 in 57 change blocks; the GNU-diff count of the same pair is 297 changed lines — for this package both numbers measure lineage distance more than change, as section 0 states.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:black-highlighter-theme-jp.txt`, read the phase17-diff file, and run `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 5; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### One revision number too many (the credit block's duplicated 135)

The candidate's credit block records both 初訳時参照リビジョン: 135 and 改訳時参照リビジョン: 135. The two fields mean different things — the revision the first translation was made from, and the revision the re-translation was checked against — and the block's own dates say they cannot both be 135: the first translation is dated 2019 in the same block （翻訳年： 2019), and rev 135 of the EN page was created on 2026-11-06 (review/sources.tsv). The campaign's other artifact for this theme agrees with the dates: the phase17-diff, which is the file that will actually be applied to the production page, adds only the 改訳時参照リビジョン: 135 line, to a production block that records no first-translation revision at all. The duplicated 135 in the candidate is the visible residue of FIX-CREDIT-C's completion pass, which filled missing revision fields across rows 1–22 from the current reference revision — correct for the 改訳 field, and for the many fresh ports whose only translation is the current one, but wrong for a production-lineage page whose first translation has its own, earlier reference (the TSV records two reference revisions for this theme precisely because they differ). The practical stakes are small — the deliverable that touches production does not contain the error — but the candidate is the documentation of record, and its credit block currently certifies a 2019 translation of a 2026 revision. Recorded for the coordinator: the candidate's 初訳時参照リビジョン line should either carry the first-translation reference the TSV records or be removed to match the phase17-diff; this package makes neither edit.

## Change set outside the two diffed files

The diff covers two files; this port's record is defined by a third. `pages/phase17-diff-black-highlighter-theme-jp.txt` (1,161 bytes) is the migration deliverable for the production page: it states the drift account (rev 130 → 135; base CDN-followed; the JP corrections kept by decision; credit only) and contains the one-line diff that adds 改訳時参照リビジョン: 135 to the live page's credit block. `pages/theme-decoration-sample-black-highlighter-theme-jp.txt` is the decoration sample the render checks ran against (its credit-modal state is section 11(2)). The candidate is also the base of record for dependent themes in this batch: theme:black-rain-jp layers over the production page this migration maintains. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
