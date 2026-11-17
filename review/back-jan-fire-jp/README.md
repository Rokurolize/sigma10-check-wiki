# Review package — theme:back-jan-fire-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:back-jan-fire-jp — origin KO, population #254 [GOSIGN2-LEDGER (b) row 254]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now cb516e59f3e159edd06af641329d3470451268dbb2586739103e56b531eb053f); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 0 infos (hotlink×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 237; GOSIGN2-LEDGER (b) row 254]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — runtime-hotlink site-theme chain + scpko.wdfiles.com / scpko.wikidot.com on both pages; sample credit-modal (preview-form) + 884px@768 overflow; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 253, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 253]
- FIX5 re-judgement: item 103 (class H) FIXED — FIX5-TEXTA §3, commit 6f6b349: credit title field -> the Japanese title already carried by the page body (L14); original-title fields left byte-unchanged [GOSIGN2-LEDGER-SUPPLEMENT (a) item 103]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:back-jan-fire-jp.txt sha256:cb516e59f3e159edd06af641329d3470451268dbb2586739103e56b531eb053f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 103 [H] (credit block's title field still in Korean while the page body carries the Japanese title) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 103: **FIXED** (FIX5-TEXTA §3, commit 6f6b349); re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c3): P4 (delivery, class (ii)), P5 (class (ii) / KB-58), P9 (ruling 2); ledger §(c2) render row: foreign-host delivery class (ii) (KB-41/KB-54 family), credit-modal preview form (KB-32), sample overflow (KB-33/KB-34 family) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:back-jan-fire | theme:back-jan-fire-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 9, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 9 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-back-jan-fire.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:back-jan-fire-jp.txt`, copied at worktree HEAD c63afef |
| Lines / bytes | 126 lines / 2,597 bytes (the file's last line carries no trailing newline, so `wc -l` reports 125) | 145 lines / 3,332 bytes |
| SHA-256 | d1dee2f91cbdb5a3b19300c03f33c07bfdd2ad2304032e75046660e0e5e04def | cb516e59f3e159edd06af641329d3470451268dbb2586739103e56b531eb053f |

Wave history: the candidate was created by the Stage 2 KO2 integration (commit d72b7b9, the LOCALIZE-S2-F wave's port); FIX-CREDIT-D (1869877) normalized its translator field; FIX5-TEXTA (6f6b349) corrected the credit title field (item 103); the usage-example population sweep (b5cb724) completed the usage example's posting name (one line). The sweep is the post-verdict change the stamp's STALE line records; it does not touch item 103's closure.

## Summary

This is the smallest port in the batch: a 110-line stylesheet with a three-line documentation body. The original hides its `[[module CSS]]` inside a conditionally hidden div so the source does not show on the theme page itself; the candidate converts that module into a displayed `[[code]]` exhibit inside a collapsible, delivers it through the standard draft-host frame placed after the gate, swaps the body's bare Rate for the preview credit block, and translates the body. Measured churn (diff.md, the generator's difflib count: +32/−13 in 10 change blocks / 3 hunks; a GNU-diff count of the same pair gives 55 changed lines — the difference is alignment choice, not content). The CSS itself is carried verbatim apart from a single colon-encoded URL. The one blocking item was a credit field that contradicted the page's own body; its fix is one line and is re-derived below. No defect flag arises from this package's checks.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 10 change blocks — 8 specific (80%), 1 heuristic (10%), 1 residue (10%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 4 |
| DRAFT-HOST | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| TRANSLATION-ANCHORED | 2 |
| BARE-RATE-DEL | 1 |
| COLON-ENC | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| INCLUDE-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes, and the sections below are written from classification.json's label_spans, not from the skeleton's per-section text): the residue block B5 is the added `----` separator before the new source-code section (candidate L20), porter furniture of the exhibit conversion, adjudicated in section 8. The heuristic block B7 ("script delta without the anchor majority") is the code exhibit's opening — the collapsible and `[[code]]` tags plus the porter banner comment (candidate L24–26), adjudicated in sections 8 and 10. B4's primary label COMPONENT-SWAP does not survive contact with the bytes: the block is the usage-example exhibit (an escaped include repoint plus the instruction line's translation); no component swap occurs anywhere in this theme, and section 2 records it as such. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:back-jan-fire-jp; original theme:back-jan-fire on scpko at reference revision 9; candidate `pages/theme:back-jan-fire-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame is inverted between the two files: the original puts its gated documentation body first (original L1–13) and its stylesheet after the gate, inside a div that hides it on +테마 pages (original L15–125); the candidate wraps body and code exhibit in the localized gate (candidate L1–137) and places the delivery frame after the gate (candidate L139–145).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for back-jan-fire-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 3 and 8.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare `[[module Rate]]` in a right-aligned div (original L3–5); the original carries no credit block, no info block, and no author naming anywhere in the file. The candidate installs the JP preview credit block (candidate L3–12) with the eight ruling-3 fields: title 灯火CSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 등잔불 테마; 著作権者 "KO 支部の作者（原語版に記録なし）" (the KO branch's author; none is recorded in the original); 作成年 2021; 初訳時参照リビジョン 9; the source link (section 7). The bare Rate is deleted. No license box exists on either side.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; the translator field took its final form in FIX-CREDIT-D (1869877). The title field is item 103 (per-theme record). The license box (T4) is not engaged: the original carries none and no register charges its absence; the credit block carries the TASL record. The 著作権者 field's wording is the honest form for this theme — the original names no author in its source, so the field records the absence instead of inventing a name (contrast theme:07k-jp in this batch, where the original does name its creator).
- **Verify:** Read candidate L3–12 against the eight fields; `grep -n 'module Rate\|license-box' candidate.txt` returns nothing.
- **Disposition:** FIXED (item 103, supplement row 103; the credit fields were FIXED by the credit waves per ledger §(c3)).

### 2. Includes and components

- **What:** Four includes, all furniture: the credit pair (candidate L3/L12, section 1), the interwiki-style frame (candidate L142–145, section 3), and the escaped usage-example exhibit `> @@[[include :scp-jp:theme:back-jan-fire-jp]]@@` (candidate L17), repointed from the original's `:scpko:theme:back-jan-fire` (original L10) — branch by the port, posting name completed by the sweep (per-theme record). Neither file carries a live component include; the classifier's COMPONENT-SWAP label on B4 is the usage exhibit's span and adjudicates to this repoint (see the class summary).
- **Why:** P1 (KB-15): the example must name the page that will exist on scp-jp, which is this candidate under its posting name (AGENTS.md §6).
- **Verify:** `grep -n '\[\[include' candidate.txt` — three live includes plus the escaped exhibit, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed, ruling 4 not engaged.

### 3. Delivery and code loading

- **What:** The original's stylesheet is a `[[module CSS show="true"]]` (original L16–125) wrapped in a div whose class attribute embeds `[[iftags -테마]]` with `display: none` (original L15): the module applies wherever the page is included, and the div trick only suppresses the source display on the theme page itself. The candidate carries the same 110 lines as a `[[code type="css"]]` exhibit (candidate L25–134) inside the gate, and delivers it with the standard frame after the gate (candidate L139–145): a `[[module css]]` importing the candidate's own `local--code/theme%3Aback-jan-fire-jp/1` from the draft host (L140), and an interwiki-style include at priority 1 naming the same /1 (L142–145). The exhibit is the page's only code block, so the frame's /1 names it; the population audit's census rule (code blocks in document order) is satisfied by inspection.
- **Why:** P4/T9 (own-code delivery from JP hosts) and P6/T3 (the supplement frame; priority 1 is the theme's own layer). The draft-host form of the two live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — candidate L140 and L143, both naming /1; confirm the single `[[code]]` block spans candidate L25–134.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: none — neither file contains a `font-family` declaration, an `@font-face`, or a font import; the theme inherits the site fonts on both sides, so P7 has nothing to attach to. Assets: exactly one, the header background image inside the CSS — `url(https://scpko.wikidot.com/local--files/theme:back-jan-fire/header)` (original L30) becomes `url(https://scpko.wikidot.com/local--files/theme%3Aback-jan-fire/header)` (candidate L39): the host is kept, the scheme was already https, and the page-name colon in the path is encoded. This is also the file's only CSS change (block B8).
- **Why:** KB-01 (colon encoding): an unencoded colon in a local--files path is a class (i) malformed-URL shape, so the encoding is the one substantive CSS edit. The kept scpko host is the original-state delivery the ledger dispositions (P4/P5, class (ii) / KB-58): the file is the original page's own attachment and no JP re-host exists.
- **Verify:** `grep -n 'font-family\|@font-face' candidate.txt` returns nothing; `grep -n 'local--files' candidate.txt` — one line, candidate L39.
- **Disposition:** Font section: none, on the ground stated. Asset: DISPOSITIONED (class (ii), ledger §(c3) P4/P5).

### 5. Header, sidebar, and site furniture

- **What:** None — no `--header-title`, `--header-subtitle`, or `--logo-image` variable exists on either side (the theme styles `#header h1 a span` and the container background directly, in rules carried verbatim), and no P8 layout adaptation appears. Ledger §(c3) records this theme's P9 as DISPOSITIONED under ruling 2; the in-file ground is stronger than the ruling needs: there is no header variable whose language could be charged.
- **Why:** P9/T6 attaches to header variables; with none present, the section is empty by construction, and saying so is the check.
- **Verify:** `grep -n -- '--header\|--logo' candidate.txt original.txt` returns nothing on either side.
- **Disposition:** DISPOSITIONED (P9, ruling 2, ledger §(c3)); in-file ground as stated.

### 6. Text translation

- **What:** The body is three content lines, all translated (blocks B3–B4): the heading (+ 등잔불 CSS 테마, original L7 → + 灯火CSSテーマ, candidate L14), the free-use line (original L9 → candidate L16), and the usage instruction (original L11 → candidate L18). The candidate adds a source-code section heading (+ ソースコード, candidate L22) and collapsible labels (ソースコードを表示 / ソースコードを閉じる, candidate L24) for the exhibit conversion of section 8. The CSS's own comment banner (the 2021 Wikidot theme generator header, original L27–29) is carried verbatim inside the code block. Korean survives in the candidate only as quotations: the credit block's original-title field and source-link label (candidate L7, L11).
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings). The section heading and collapsible labels are new furniture text the port itself introduced, translated by construction.
- **Verify:** Read candidate L14–24 against original L7–11; a Hangul scan of candidate.txt returns only candidate L7 and L11.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** One link: the credit block's source link (candidate L11), `[*https://scpko.wikidot.com/theme:back-jan-fire 등잔불 테마]` — the host matches the original's recorded host in review/sources.tsv (scpko.wikidot.com), and the label quotes the original's title. No prose link exists in either file's body; the usage example is an include exhibit, covered in section 2.
- **Why:** P11 under the dead-reference evidence standard: the source link's job is to reach the original, and it names the host that serves it.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Applied; no open link item in this file.

### 8. Structure

- **What:** Two structural changes, both delivery-driven. (a) The stylesheet's channel changes from a live module hidden by the iftags div trick to a displayed code exhibit in a collapsible (original L15–125 → candidate L24–134), with a `----` separator (candidate L20, residue block B5) and the + ソースコード heading added as the exhibit's furniture; the CSS text itself is preserved line for line apart from the single URL encoding of section 4 (the module's 110 lines and the code block's 110 lines correspond one to one). (b) The delivery frame moves outside the gate (candidate L139–145), where the original's module sat outside its gate as well — the gate inversion of section 0 is the exhibit's move inside, not the delivery's. The localize.md closing rule otherwise holds: no selector, variable, or rule order changes anywhere in the CSS.
- **Why:** R3 (exhibit restructuring) with the ground stated: the original's hidden-module form cannot serve as its own delivery exhibit on the JP side, because the candidate's delivery is the code block the frame imports (section 3); making the source a displayed exhibit is what lets one block be both. Nothing was dropped in the conversion — the census is the whole file, and both sides' CSS line counts match.
- **Verify:** `diff` the CSS interiors: original L17–124 against candidate L27–133 — identical apart from candidate L39 (section 4).
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** None beyond the recorded furniture. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered. The candidate's last line carries a trailing newline where the original's does not.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (reindent_blocks: 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation: the banner comment `/* ===== back-jan-fire ===== */` at the head of the code block (candidate L26), naming the theme at the top of its own source exhibit. It rides inside heuristic block B7 (see the class summary); the skeleton's per-section text did not isolate it. The inherited generator banner below it (candidate L27–29) is original content, not an annotation.
- **Why:** R2: porter-added text is part of the change record, and this one is the exhibit's title card — a reader opening the code block meets it first.
- **Verify:** Read candidate L25–29.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section: (1) T1's two errors — hotlink ×1 (the scpko header image, class (ii), section 4) and pseudo-ref ×1 (the draft-host delivery lines, class (iii), section 3); no class (i) error stands. (2) The render row's items, all environment or preview layer, not charged to the candidate: the runtime-hotlink site-theme chain plus scpko.wdfiles.com / scpko.wikidot.com on both pages (KB-40/KB-41 family, class (ii)); the sample credit-modal errors (KB-32, ruling 5); and the sample's 884px@768 overflow (the cross-cutting static-credit / preview-chrome families, KB-33/KB-34). (3) Ledger §(c3): P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery), P5 DISPOSITIONED (class (ii) / KB-58), P9 DISPOSITIONED (ruling 2; section 5 gives the in-file ground). No item for this theme is left as an unexplained exception, and no defect flag arises from this package's checks.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 237): exit 1, 2 errors / 0 warns / 0 infos (hotlink×1, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO2)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 253): FINDINGS jointly, display-affecting findings 2; of these, the untranslated credit title reached the §(e) register as item 103 and the remainder is the §(c3) pattern record. (d) The FIX5 closure re-derived for this package: the supplement (row 103) says FIX5-TEXTA set the credit title field to the Japanese title the body already carried; the commit (6f6b349) changes exactly that one line (タイトル: 등잔불 테마 → 灯火CSSテーマ) and leaves the original-title field byte-unchanged, and the current candidate reads タイトル: 灯火CSSテーマ (candidate L4) against the body's + 灯火CSSテーマ (candidate L14), with 原題: 등잔불 테마 (candidate L7) still quoting the original. The fix is present and complete in the bytes. (e) A brace-depth scan of the delivered code block (candidate L25–134) ends at depth 0 with no negative excursion. (f) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +32/−13 in 10 change blocks / 3 hunks; the GNU-diff count of the same pair is 55 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:back-jan-fire-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 254 as re-judged by supplement row 103; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 103 re-derived (ledger class H)

At ledger time the candidate's credit block contradicted its own page: the block's タイトル field still read 등잔불 테마 (the Korean title) while the body heading already read 灯火CSSテーマ. The localize lane charged it as 型 3 (title untranslated) with no severity call of its own — the ledger notes the parallel bulgunae item was marked minor by its lane and dispositioned there, while this row carried no such call, so the item stood as a blocking charge. FIX5-TEXTA §3 (commit 6f6b349) made the one-line correction, setting the field to the body's Japanese title and deliberately leaving the 原題 field quoting the Korean title unchanged; the supplement re-judged the item FIXED. The current bytes confirm the closure exactly as the commit made it (candidate L4 against L14, with L7 the untouched quotation). No other line of the credit block was touched by the fix.

### The usage example's posting name

The usage example at candidate L17 as built read `> @@[[include :scp-jp:theme:back-jan-fire]]@@`: the porting wave's repoint changed the branch prefix from `:scpko:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:back-jan-fire-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-back-jan-fire-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the Stage 2 KO2 integration (d72b7b9) produced the port (translation, exhibit conversion, credit block, delivery frame, and the untranslated credit title it left behind); FIX-CREDIT-D (1869877) normalized the translator field across all candidates; FIX5-TEXTA (6f6b349) corrected the title field (item 103); and the usage-example sweep (b5cb724) completed the example's posting name. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 103; GOSIGN2-LEDGER-SUPPLEMENT.md row 103; REPORT-GOSIGN2-FIX5-TEXTA.md §3. The go-sign re-run over that record is what the Status block certifies.
