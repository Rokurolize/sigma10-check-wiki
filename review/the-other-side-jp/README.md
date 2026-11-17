# Review package — theme:the-other-side-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:the-other-side-jp — origin CN, population #237 [GOSIGN2-LEDGER (b) row 237]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now c4016a128f7316c42fa9d80ac4b3d0ec9effbac887467f2924b4a3d9e5a88b14); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 0 warns / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 202; GOSIGN2-LEDGER (b) row 237]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 325px@320 on page and sample (+ 884px@768 on sample) + runtime-hotlink site-theme chain; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN16)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN16)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 236, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 236]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 237]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:the-other-side-jp.txt sha256:c4016a128f7316c42fa9d80ac4b3d0ec9effbac887467f2924b4a3d9e5a88b14; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/the-other-side-jp/candidate.txt (sha256 c4016a128f7316c42fa9d80ac4b3d0ec9effbac887467f2924b4a3d9e5a88b14)
Original: theme:the-other-side — scp-wiki-cn, revision 59 (sha256 821b32af177666a56eb127b84aa9d2885b629bfcdeb7634ed83426d7232a6f05)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 237); one of the 286 of 286 pass-eligible themes. The generated stamp above reads STALE: the candidate changed after the verdict-era bytes (the usage-example sweep, commit b5cb724, repointed one usage line to the -jp form), so the stamp's verdict lines describe the pre-sweep file |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no the-other-side entries |
| Wave edits after the port | Translator normalized to AI (FIX-CREDIT-D, 1869877); the credit-module CSS supplement and the footnote-component restoration, both inside the FIX4-CREDIT commit (9fbcd94); one usage line repointed (population sweep, b5cb724) |
| Open items recorded by this package | Two charges the T4 lane raised and the ledger closed by disposition, stated here at full strength so the reader can judge them: the pattern-9 header defaults (the CN subtitle delivered untranslated, section 5) and the pattern-7 font state (JP faces loaded but never stacked; Fira Code and Jost named but never loaded, section 4). Also a record conflict: sources.tsv's note claims the original was superseded upstream; the campaign's own follow-up artifact records rev 59 → rev 59, no changes (Per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:the-other-side | theme:the-other-side-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 59 (per sources.tsv and the candidate's credit block: **初訳時参照リビジョン:** 59; the TSV's rev_created_at cell is blank for this row) | — |
| Source of this copy | The T4 lane's fetch of 2026-11-16 (mirror store class COPY, from the localize lane's working copy `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-the-other-side.txt`), via the campaign mirror store | Canonical file `pages/theme:the-other-side-jp.txt`, created in commit ddf2c89 ("Stage 2 CN16 integration"); its last content change is commit b5cb724 (the usage-example sweep) |
| Lines / bytes | 605 lines / 67,300 bytes | 562 lines / 66,541 bytes |
| SHA-256 | 821b32af177666a56eb127b84aa9d2885b629bfcdeb7634ed83426d7232a6f05 | c4016a128f7316c42fa9d80ac4b3d0ec9effbac887467f2924b4a3d9e5a88b14 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart exists on SCP-JP for this theme, and none was adopted. The T4 lane's follow-up artifact (`diff-the-other-side-from59.txt`, in the lane's directory) records the upstream state after the reference revision as **rev 59 → rev 59, no changes**, with an empty intervening-revision list: there is no post-reference upstream delta for this package to classify, and the sources.tsv note claiming otherwise is corrected in the Per-theme record.

## Summary

The Other Side （彼岸） is Mr 09_doctor's CN theme: a Penumbra-derived design whose stylesheet lives in a 292-line code exhibit, whose documentation body carries CN literary specimens (a Middlemarch quotation, an Asimov passage) as float/column layout exhibits, and whose tail hides its base include (theme:penumbra) and a footnote component in a display:none div. The candidate moves delivery to the head (a module importing its own /1 on the draft host, a priority-1 frame), translates the documentation prose while deliberately leaving the literary specimens in Chinese as layout exhibits, compresses the sidebox documentation set into one simplified demo, drops the table and nested-blockquote specimens, swaps the footnote component to its JP port, and appends a license box and a T7 credit supplement. Two of the T4 lane's charges survive as dispositions a reviewer should weigh: the header subtitle default is delivered in Chinese (the ledger closes it under ruling 2), and the JP font faces the port loads are never named in any delivered stack. The theme passed with no open items; both charges are stated at full strength in sections 4 and 5.

## Classification

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 2 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 4 |
| DUPIMPORT-DEL | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 3 |
| FONT-IMPORT | 2 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 3 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 13 |
| TRANS-UNANCHORED | 51 |
| WS-ONLY | 11 |

Counts: 88 blocks — 35 specific (39.8%), 48 heuristic (54.5%), 5 residue (5.7%), 0 skipped. The generator's own auto-classification of the same pair (diff.md, Tier 2) reads: mechanical 12 blocks / 24 lines, translation 24 / 61, supplement 3 / 60, residual 49 / 224 — the two instruments count different units; this README follows the classifier's blocks and resolves its residual 49-block tail (the generator's coarser class) block by block in the Appendix through the classifier's finer split. Topology: the original's code-css (orig L303–595, 292 lines) plus a tail module-css (orig L602–605); the candidate's head module-css (cand L1–3) plus code-css (cand L222–542, 320 lines); external own delivery true (the head module imports the candidate's own /1). Labels are sets per block; this README's sections were written from classification.json's label spans, not from the skeleton's per-section lists.

## Standing sections

### 0. Header and provenance frame

- **What:** The original's head (L1–28) is exhibit furniture: a bare `[[module Rate]]`, the CN credit-module template exhibits (`credit:start` / `more` / `end` and `credit:start-standalone`), and the star-toggle collapsible — all before the intro. The candidate's head (L1–21) is delivery and credit: the head module importing its own /1 (cand L1–3), the JP interwiki frame at priority=1 (cand L5–8), the localized gate (cand L10), and the preview credit block (cand L12–21). Provenance route: derived from the original at reference revision 59 (see Provenance).
- **Why:** P1/P2/P3/P6 rework exactly this frame for the JP environment; each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–28 against candidate L1–21; blocks B1–B6 in classification.json.
- **Disposition:** Recorded; the credit reading is section 1, the delivery reading section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is the bare Rate (orig L3) and the CN credit-module template exhibits (orig L5–17), all deleted (block B2, label BARE-RATE-DEL plus the exhibit deletions). The candidate carries the preview credit block (cand L12–21): `:scp-jp:credit:start-preview` / `end-preview` with all eight ruling-3 fields — title 彼岸 The Other Sideテーマ, translator AI, translation year 2026, original title 彼岸 The Other Side, copyright holder **[[*user Mr 09_doctor]]** (the only named-form holder in its T4 set; the lane verified it against the original's CSS header, "[2026 Wikidot Theme] 彼岸 The Other Side, by Mr 09_doctor"), creation year 2026, reference revision 59, and the source link to scp-wiki-cn.wikidot.com/theme:the-other-side — the recorded host, matching sources.tsv; no host flag. The theme's credit-module CSS is the T7 supplement inside the code exhibit (cand L523–541, labels T7-CREDIT-CSS): palette-adapted rules for the JP credit module's markup, added by FIX4-CREDIT (9fbcd94) — before that commit the candidate carried **zero** credit-module rules (the KB-11 register's finding for this theme, one of exactly five FIX4-CREDIT themes), and the supplement's own comment states its source: the production penumbra counterpart's block (`pages-existing/existing:theme-penumbra.txt` L758–772). The license box (cand L544–557, label LICENSE-BOX) is section 4's supplement: author=Mr 09_doctor, the three image entries with their license-unknown caution, and the font entry.
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing credit form, so a separate bare Rate beside it would duplicate the rating widget (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 fixes the eight fields and credits campaign translations to AI. The T7 supplement exists because the frozen JP credit component's markup differs from what the theme's inherited rules expected (KB-11's family).
- **Verify:** Read candidate L12–21 against the eight-field list; `grep -n 'module Rate' candidate.txt` (absent) against original L3; `git show 9fbcd94 -- pages/theme:the-other-side-jp.txt` for the supplement's arrival.
- **Disposition:** Standing. Ledger (c3): credit fields FIXED by the credit waves; KB-11 register: FIXED in 9fbcd94, with CREDIT-VERIFY rendering this theme's supplement live with exact computed-style matches.

### 2. Includes and components

- **What:** The candidate's include list (grep): the credit pair (L12/L21), the JP interwiki frame (L5–8), `component:image-block` in the examples (cand L72, repointed `:scp-jp:` with its file re-hosted), and — after the closing gate — `component:betterbetterfootnote-jp` in a display:none div (cand L558–561, label COMPONENT-SWAP). The original's tail hid two includes in the same device (orig L599–601): its base `theme:penumbra` (CN) and `component:betterbetterfootnote` (the fendsfox form). The candidate drops the penumbra include entirely — its penumbra-derived CSS is carried inline in its own code exhibit, and the intro states the derivation — and swaps the footnote component to the JP port the campaign produced. The footnote include's history matters: the port as created (ddf2c89) dropped it along with the tail; FIX4-CREDIT (9fbcd94) restored it in the JP form — a component restoration riding inside a credit-named commit (Per-theme record). No foreign include is kept, so KB-15/KB-54 do not engage.
- **Why:** P1: foreign-site includes are repointed to the JP site, and ruling 4 (port a needed component with the theme) is what the footnote swap executes — the component exists as a JP port and the theme's footnote rendering depends on it. The base include's removal is the opposite shape: the base's contribution is inlined, so no include is owed (section 3).
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists, including the tail divs (orig L598–601, cand L558–561).
- **Disposition:** Standing; no include in the candidate points at a CN-wiki page.

### 3. Delivery and code loading

- **What:** The original delivers from its tail: a `[[module CSS]]` (orig L602–605) importing its own CN local--code /1, with the stylesheet in the code exhibit (orig L303–595). The candidate delivers from its head: a module (cand L1–3) importing its own /1 on the draft host (sigma10-jp-test.wdfiles.com) and the JP frame at priority=1 naming the same address (cand L5–8, labels SELF-DELIVERY + DRAFT-HOST). The address census is sound: the candidate has exactly one `[[code]]` block and it holds the CSS (cand L222–542), so /1 names the right block — this theme is not in the FIX-CODEADDR no-target class. The code exhibit grew from 292 to 320 lines: the T7 supplement (cand L523–541) and the font-import relocation (section 4) account for the growth. The original's three font imports sat after its CSS header comment (orig L311–313); in the candidate the imports lead the exhibit (cand L224–228, the two JP imports prepended) and the header comment follows them (cand L230–238) — the generator's block 72 reads as a deletion of the original's imports, but the bytes show a relocation; the classifier's DUPIMPORT-DEL span records that one of the original's duplicated import forms did not survive the move. The T4 lane recorded the frame configuration as a note: a non-BHL self-delivery frame (priority=1, own /1), acceptable because the theme is not BHL-family — its penumbra derivation is inlined, not layered.
- **Why:** P4/T9: deliveries are served from JP hosts in this environment, and a candidate's own local--code on the draft host is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. P6: the frame carries the priority the layering requires.
- **Verify:** Read orig L598–605 against cand L1–8; `grep -c '\[\[code' candidate.txt` = 1; read cand L222–238 for the import relocation.
- **Disposition:** The draft-host addresses are class (iii), recorded as not-charged in section 11; the frame configuration is the T4 lane's recorded note (P6 APPLIED with notes).

### 4. Fonts and assets

- **What:** The candidate prepends two JP font imports to the code exhibit (cand L224–225: Noto Sans JP and Noto Serif JP from Google Fonts, label JPFONT-LOAD) and relocates the original's three imports below them (cand L226–228: Kaisei HarunoUmi, Noto Sans SC, Noto Serif SC). **No delivered stack names the JP faces.** The delivered variables (cand L381–383) are the original's: `--header-font: "Kaisei HarunoUmi", cursive` (Kaisei is loaded and is the one working JP face), `--body-font: "Noto Serif SC", serif`, `--mono-font: 'Fira Code', "Noto Sans SC", ...`. Two further gaps: **Fira Code** is named in --mono-font but loaded nowhere in the candidate (its only occurrence is cand L383), and **--font1: 'Jost'** (cand L250) is loaded nowhere and referenced by no other rule. The T4 lane marked pattern 7 MISSED for exactly this state; it did not tag the item display-affecting, and the ledger's pattern-7 preamble records non-display-affecting pattern-7 notes as recorded, not blocking — so the item stands as a recorded note, stated here at full factual strength. Assets: the three specimen images were re-hosted from the CN sandbox host to the candidate's own draft-host attachments (castle-of-remorse.png cand L256, logo.png cand L72, vector.png cand L197), and the license box (cand L544–557) records that the images' licenses are unstated in the original and need author confirmation before posting — the sanctioned draft state (posting requires re-upload to SCP-JP storage, an owner-ordered deferral).
- **Why:** P7/T5 exists because a stack naming an unloaded face, or a loaded face no stack names, leaves the JP rendering to fallback in ways the record should not call fixed. KB-16 (font load gap) is the standing pattern for the Fira Code shape. The license box is KB-63's supplement form: what the original left unstated is stated, with the caution, rather than silently dropped.
- **Verify:** `grep -n 'Noto Sans JP\|Noto Serif JP' candidate.txt` (only the import lines L224–225); `grep -n 'Fira Code' candidate.txt` (only L383); read cand L381–383 against orig L453–455.
- **Disposition:** DISPOSITIONED as a recorded pattern-7 note (ledger pattern-7 preamble; the lane's P7 verdict was MISSED without a display-affecting tag). The asset re-hosting is the class (ii)/(iii) draft state, recorded in section 11.

### 5. Header, sidebar, site furniture

- **What:** The HEADERVAR block (B37) is the pattern-9 item. The candidate's delivered defaults are `--header-title: "悔恨城堡"` (cand L254) and `--header-subtitle: "願我們能到達希望的彼岸"` (cand L255) — byte-identical to the original's (orig L326–327), traditional-Chinese text shown in every themed page's header. The T4 lane's distinction, preserved here because it is the crux: the title is the work's proper name (a judgment call), but the subtitle is a plain prose sentence ("may we reach the far shore of hope") that should have been translated; and the candidate's own usage specimen (cand L45–46) demonstrates both variables with Japanese example values, so the candidate shows the localized form while delivering the CN defaults. The lane marked P9 MISSED and display-affecting. The ledger (c3) closes the theme's charges "under the class outcomes above (header language = ruling 2; …)". Sidebar and furniture: the original carries no sidebar/topbar layout CSS beyond a #top-bar offset, carried identically (lane P8: N-A with notes).
- **Why:** P9 covers reader-visible header variables; ruling 2 (RULINGS-20261116) takes header and title language out of migration-correctness scope. Both positions are recorded because they genuinely conflict on the subtitle: the ruling governs the campaign's verdict, and the lane's charge is the fact a reviewer needs to judge whether the ruling's scope is the right one for a prose subtitle.
- **Verify:** Read orig L326–327 against cand L254–255 (byte-identical); read the usage specimen at cand L45–48; the lane's P9 text is in the LOCALIZE-S2-E report (part-CN16.md, CN16-1).
- **Disposition:** DISPOSITIONED under ruling 2 (ledger (c3)). The lane's charge (display-affecting; the subtitle at minimum should have been translated) is recorded alongside the disposition, not replaced by it.

### 6. Text translation

- **What:** The documentation prose is translated (TRANS-UNANCHORED ×51, TRANSLATION-ANCHORED ×13): the intro (with its derivation statement), the usage specimens (which demonstrate the header variables in Japanese, section 5), the component specimens, and the collapsible furniture (the star-toggle's show/hide rendered as 再生を停止する/再開する — the lane judged the rendering acceptable against the original's pause/continue wording). Two deliberate non-translations: (a) the literary specimens stay in Chinese — the translator note at cand L181 declares them specimens of the theme's float/column layout, intentionally untranslated (lane P10: APPLIED with notes); their truncation is a structural item (section 8), separate from the language choice. (b) The intro's links to CN theme and work pages were made explicit scp-wiki-cn URLs (cand L29, label LINK-REPOINT) because no JP counterparts exist — the lane judged same-site-ifying them would have been wrong, and they are not tag/hub links, so no P11 violation arises. In-CSS text (residue class R1): the code body's comments stay in Chinese (porter-visible only), except the header comment block, which gained the porter's own annotation lines (cand L230–238, section 10).
- **Why:** P10: body and usage text are translated; a specimen whose content is the exhibit's subject (a CN literary layout) is the standing exception shape, declared in the file itself rather than left for a reviewer to discover. KB-18 covers reader-visible strings; the header defaults are reader-visible and are section 5's item, not this section's.
- **Verify:** Read orig L29–48 against cand L24–48; read the translator note at cand L181; `grep -n 'scp-wiki-cn' candidate.txt` (the credit source link and the intro's explicit links).
- **Disposition:** Standing (lane P10 APPLIED with notes; P11 APPLIED with notes).

### 7. Links

- **What:** The candidate's links: the credit block's source link (cand L20, to the CN original — the required ruling-3 back-reference, on the recorded host), the intro's explicit scp-wiki-cn links (cand L29, section 6), and the specimen-internal links carried with the exhibits. No JP tag-page or hub counterpart exists for the intro's targets, which is the ground of the explicit-URL form.
- **Why:** P11 repoints links to their JP counterparts where counterparts exist; where none exist, an explicit original-site URL is the honest form (the lane's judgment, recorded in its report).
- **Verify:** `grep -n 'http' candidate.txt` and compare against the original's list.
- **Disposition:** Standing (lane P11 APPLIED with notes).

### 8. Structure

- **What:** The stylesheet body honors the localize.md closing rule in shape: the code exhibit carries the original's rules in order (its brace-depth scan ends at 0 with minimum 0, matching the original's), with the JP corrections at the head imports, the T7 supplement and the license-adjacent tail, not interleaved. Four structural losses sit in the documentation body, all from the creation (ddf2c89) and all recorded by the T4 lane. (a) The table specimen (orig L166–168) and the nested-blockquote specimen (orig L162) are dropped: the candidate's blockquote demo (cand L160–164) has no `>>` nesting and the JP body has no table example at all (the lane's T5 item (c)). (b) The sidebox documentation set (orig L224–292: the limit/anchor/sidebox nesting explanation, the usage-tricks example, the multiple-sidebox example, the ≤1290px minimization note, the limit div explanation) is replaced by one simplified demo (cand L202–214) that puts sample text in a darkbox; the nesting-requirement explanation and the minimization note are lost (blocks B68, B71). (c) The literary specimens are heavily truncated: the Middlemarch quotation (orig L185–200) survives as single lines (cand L183, L189), one CN dialogue line is deleted outright (orig L195, residue B59), and the Asimov passage (orig L206–220) survives as fragments (cand L195, L199; residue B62, B67). The lane records the information loss alongside the translator's declaration (section 6). (d) The font-specimen block (orig L296–302) is deleted, replaced by the license box's font entry (cand L544–557) — the lane judged the replacement valid. Two separator lines (`@@ @@`, cand L171, L176; residue B54, B55) were added in the blockquote region where the original ran its specimens together.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so the ground for each is stated. The specimen compressions are the port's documentation choices, visible to the T4 lane, which charged none of them as defects beyond its T5 note on (a); they are recorded here because a reviewer comparing bodies will find the JP documentation materially thinner than the CN one, and should find that fact stated rather than discover it.
- **Verify:** `grep -n 'sidebox\|1290' candidate.txt` against original L224–292; read orig L185–220 against cand L181–200.
- **Disposition:** Standing (restructuring recorded; the lane's T5 item (c) is the (a) loss, recorded in its report).

### 9. Formatting only

- **What:** 11 WS-ONLY blocks — the batch's highest count, and their shape is specific: the original's code exhibit and body carry heavy blank-line padding, and the candidate's compression of it accounts for most of the count (the generator's Tier 2 header likewise separates 24 mechanical lines). 0 re-indentation blocks. None of the whitespace churn touches a rule's text.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; this is not R7 wholesale re-indentation (content lines keep their indentation, so follow-up diffs still apply).
- **Verify:** classification.json (11 WS-ONLY blocks, reindent_blocks 0); diff.md's mechanical class (12 blocks / 24 lines by the generator's counting).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two porter texts ride inside other blocks, found by direct inspection (the standing lesson: annotations hide inside labeled blocks). (a) The code exhibit's header comment (cand L230–238) combines the porter's annotation with the original's own header comment, below the relocated imports. (b) The T7 supplement's comment (cand L523–529) states the supplement's provenance (adapted from the production penumbra counterpart's block) — an annotation that is also the supplement's audit trail. The translator note at cand L181 (section 6) is a third, reader-visible by design. No `[!-- ... --]` notes exist (`grep -c '\[!--' candidate.txt` = 0).
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation.
- **Verify:** Read cand L230–238 and L523–529.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The pattern-9 header defaults (cand L254–255): DISPOSITIONED under ruling 2 (header language out of scope), with the T4 lane's display-affecting charge recorded at full strength in section 5. (2) The pattern-7 font state (section 4): DISPOSITIONED as a recorded pattern-7 note under the ledger's pattern-7 preamble (the lane's MISSED verdict carried no display-affecting tag). (3) The render findings: page-overflow 325px@320 on page and sample (+884px@768 on sample) and the runtime-hotlink site-theme chain — DISPOSITIONED in (c2) under KB-40 (environment layer); the sample's credit-modal item DISPOSITIONED as the preview form's property (KB-32; ruling 5's family). (4) The draft-host delivery and attachment addresses (cand L2, L7, L72, L197, L256): class (ii)/(iii) draft state, rewritten or re-uploaded at posting. (5) The T3 re-run's chromium-only coverage (no WebKit verdict): a coverage statement, not a finding. (6) The structural losses of section 8: recorded restructuring, charged by no register beyond the lane's T5 note. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–6).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 4 errors / 0 warn / 1 info (pseudo-ref×4; T1-ROWS row 202 — the register's row numbering for this theme is 202, while the ledger's (b) row is 237; both name theme:the-other-side). The pseudo-refs are the self-delivery forms, class (ii) per register (c1). (b) T2/T3 render: RENDER-S2-G (CN16): FINDINGS, dispositioned in (c2) (section 11, item 3); the T3 re-run recorded no new screenshot-grounded visual finding. (c) T4 localize plus follow-up: FINDINGS with 1 display-affecting item (the P9 header item, section 5) plus the P7 item without the tag (section 4); the lane's per-pattern verdicts are P1–P6, P8, P10, P11 APPLIED (several with notes), P7 and P9 MISSED; outcomes in ledger (c3) as quoted in sections 4 and 5. The follow-up artifact records rev 59 → rev 59, no changes (Provenance). (d) T5: judged by the same lane; its items are the specimen losses of section 8 and the collapsible wording of section 6. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp (which reads STALE for the sweep reason in the Status block). Counts in this README are the classifier's (88 change blocks) and the generator's (diff.md: +163/−206 in 14 sections).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:the-other-side-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 237), with sections 4 and 5 recording the two charges the determination closed by disposition.

## Per-theme record

### The sources.tsv supersession note is wrong for this row (record conflict)

sources.tsv's note for this row states that the original "was superseded upstream since the reference revision" and cites the follow-up artifact `diff-the-other-side-from59.txt`. The artifact itself (138 bytes, in the T4 lane's directory) records the opposite: `rev59 -> rev59`, an empty intervening-revision list, and "no changes". The note's claim is therefore false for this row, and this package follows the artifact: the mirror at rev 59 is the current upstream state, and there is no post-reference delta to classify. The same wrong-note shape occurred on the ambrose-chapter-two row (corrected in commit b3ce875) and on the alcur and inland-empire rows (corrected in f1e25db and 9dbeaaf); the correction for this row is the coordinator's to land, and it is flagged in the batch report. The package itself is unaffected: original.txt is the rev-59 fetch either way.

### FIX4-CREDIT's diff exceeds its subject (wave attribution)

Commit 9fbcd94's subject covers credit supplements. Its diff for this file does three things: it adds the T7 credit-module CSS inside the code exhibit (cand L523–541), it restores the footnote component include in its JP form in the tail div (cand L558–561), and it adjusts the surrounding lines. The second item is a component restoration (ruling 4's family), not a credit supplement: the port as created had dropped the original's footnote component along with its tail, and this commit is where the theme's footnote rendering was made whole. A reader reconciling the commit against the file needs the fuller account; the registers' KB-11 entry records only the credit half.

### The ledger's (c3) closure is a class reference, not an itemization

For most themes the (c3) register itemizes outcomes pattern by pattern. For this theme it closes in one line — "row charges DISPOSITIONED under the class outcomes above (header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves)" — which compresses three different outcome kinds (a ruling-based disposition, a class disposition, and a fix) and does not mention the pattern-7 item at all. The itemized record exists, but it lives in the T4 lane's own report (part-CN16.md, CN16-1), which this package cites pattern by pattern in sections 3–6. A reviewer who reads only the ledger will under-count this theme's charges by two (P7, and the P9 charge's display-affecting tag); this package's sections 4 and 5 exist to close exactly that gap.

### The penumbra counterpart's role

The T7 supplement's source is the production penumbra page (`pages-existing/existing:theme-penumbra.txt` L758–772), not the CN penumbra original: the port's credit rules were adapted from the JP production lineage's form of the base theme, palette-adjusted to this theme. That is why the supplement's comment names the production file. The relationship is a companion source for one block, not a production adoption of this theme (which has no JP production page); residue class R4 does not apply to the package as a whole.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-the-other-side-jp.txt` — the render sample page (an include of the candidate and of the shared `theme-decoration-sample`); it is the "sample" the T2/T3 checks rendered. (2) `pages-existing/existing:theme-penumbra.txt` — the production penumbra page, the T7 supplement's source (Per-theme record). (3) `component:betterbetterfootnote-jp` — the JP footnote component the tail include names; it is a campaign port in its own right (ruling 4), living outside this repo's pages/ set as a component page. (4) The delivery itself: the candidate's own local--code /1 on the draft host, the runtime form of the code exhibit (cand L222–542), named by the head module and the frame.

## Multi-wave provenance

The candidate's current state is the product of one creation and three wave touches: ddf2c89 created it in the Stage 2 CN16 integration (translation, head delivery, credit block, specimen compressions, the footnote component dropped with the tail, the CN header defaults and font stacks carried); FIX-CREDIT-D (1869877) normalized the translator field to AI; FIX4-CREDIT (9fbcd94) added the T7 credit supplement and restored the footnote component in JP form; the usage-example sweep (b5cb724) repointed the usage include to the -jp form, which is why the stamp reads STALE; and the ledger determination passed the theme with no OPEN items, its charges closed by the dispositions itemized in section 11, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 237, (c1) pseudo-ref entry, (c2) the-other-side entry, (c3) the-other-side entry and the pattern-7 preamble, (d) item 6 (the labelled paired Rate exhibits — this theme's quoted Rate example is the pattern-3 exception the ledger names); T1-ROWS row 202; LOCALIZE-ROWS row 236 and the lane report part-CN16.md (CN16-1); RENDER-ROWS (RENDER-S2-G) the-other-side row; KB-11 and KB-32/KB-40 preambles. The go-sign re-run over that record is what the Status block certifies, subject to sections 4 and 5.

## Appendix — residue blocks

The classifier emitted five residue blocks and forty-eight heuristic blocks; all are resolved, none required a new signature.

- **R1 — B54 and B55 (residue; insertions at cand L171 and L176).** The two `@@ @@` separator lines added in the blockquote specimen region. Resolved in section 8: exhibit separators where the original ran its specimens together.
- **R2 — B59 (residue; orig L194–195 → cand L193).** The deleted CN dialogue line inside the Middlemarch specimen. Resolved in section 8, item (c): part of the specimen truncation, recorded with the translator's declaration in section 6.
- **R3 — B62 (residue; orig L207–208 → cand L198–199).** The Asimov passage's repositioned line, carrying the specimen's footnote. Resolved in section 8, item (c).
- **R4 — B67 (residue; orig L217–220 → cand L215–216).** The specimen tail: the Asimov quotation's closing lines trimmed, with `[[footnoteblock]]` repositioned to cand L216 (the candidate does carry its footnoteblock — unlike its batch-mate skipos). Resolved in section 8, item (c).
- **R5 — B68 (heuristic; orig L224–231 → cand L220).** The sidebox explanation's compression into the source-code transition. Resolved in section 8, item (b).
- **R6 — B70 (heuristic; orig L235–236 → cand L230–234).** The code exhibit's header region: the porter annotation added inside the exhibit's comment header. Resolved in section 10.
- **R7 — B71 (heuristic; orig L238–304, deleted).** The 67-line sidebox example collapsible. Resolved in section 8, item (b).
- **R8 — the remaining heuristic mass (TRANS-UNANCHORED and TRANSLATION-ANCHORED blocks across the body, and the WS-ONLY padding blocks).** The translated documentation prose and the padding compression, interleaved line by line; the classifier's "script delta without the anchor majority" note is the honest label for them. Each region is accounted in sections 6, 8 and 9, and the generator's Tier 2 auto-classification (translation 24 blocks / 61 lines, mechanical 12 / 24) corroborates the split at its coarser grain.
