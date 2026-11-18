# Review package — theme:legend-of-blue-jp (KO → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:legend-of-blue-jp — origin KO, population #272 [GOSIGN2-LEDGER (b) row 272]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 231f8a00c34bf8c6d6c4ebf76d66bcd286a3cb42385b9552902079ef3badc3fd); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 0 warns / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 276; GOSIGN2-LEDGER (b) row 272]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 361–362px@320 on page and sample; sample credit-modal (preview-form); T3 theme-color swatch table wider than the content column, right-hand cells cut at 375/320 (both pages). [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 271, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 271]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 272]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:legend-of-blue-jp.txt sha256:231f8a00c34bf8c6d6c4ebf76d66bcd286a3cb42385b9552902079ef3badc3fd; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS at the ledger determination; the stamp above reads STALE by design** — the candidate changed after the verdict was computed (two post-verdict repairs, detailed in the per-theme record), so the generator preserves the pre-change verdict lines under a STALE header instead of carrying the verdict over. This package is built against the current candidate and does not try to make the stamp read PASS |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×6 (sections 3 and 4); the render row's items (section 11). T4's one finding was a real defect (the broken source link), repaired after the verdict by canonical commit 2a8a125 — the repair, not a disposition, is what closed it (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:legend-of-blue | theme:legend-of-blue-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 78 (first translation; the candidate's credit block records 初訳時参照リビジョン: 78) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-legend-of-blue.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:legend-of-blue-jp.txt`, byte-identical to the canonical file in its post-sweep state (repairs 2a8a125 and b5cb724; see the per-theme record) |
| Lines / bytes | 905 lines / 24,136 bytes | 902 lines / 22,549 bytes |
| SHA-256 | b36018755ee86e89a908ced197250f39fe55bc940b66e33080c24def08810d36 | 231f8a00c34bf8c6d6c4ebf76d66bcd286a3cb42385b9552902079ef3badc3fd |

Wave history: the candidate was created by the Stage 2 KO5 integration (commit 3c781b1), then touched by 1869877 (FIX-CREDIT-D, translator-attribution normalization), and after the go-sign verdict by two repairs: 2a8a125 (the KO source-link host correction, which is what makes the stamp read STALE) and b5cb724 (the usage-example sweep). The stamp's "computed against" line names 2a8a125 and the file hash of that moment; the current file differs from it by the sweep's single line, as the per-theme record details.

## Summary

A KO theme port (the Legend of Blue theme, by salamander724 and thd-glasses, made for the Chonghaejin group) whose package is defined by one post-verdict repair. The original delivers its CSS through the exhibit itself (a live CSS module), carries a labeled Rate and a placeholder info pair for credit, decorates its exhibits with Korean display faces loaded from three hosts, and documents its images in its own copyright section. The candidate adds a head delivery frame in the population's form, swaps the credit furniture for the JP preview block, converts the exhibit to a code listing, substitutes the Korean display faces with a documented JP serif stack, re-hosts the theme's five images to the JP side keeping their file names, translates the body including the copyright section (even localizing the Creative Commons deed links), and appends a small credit-module CSS correction with its reasoning stated in a comment. Its one T4 finding was a genuine defect: the credit block's source link named the KO branch's old host, which does not serve the page. That defect was repaired after the go-sign verdict (commit 2a8a125), and the generated stamp therefore reads STALE over the preserved verdict lines — the designed behavior for a post-verdict change, documented in full in the per-theme record. Measured churn (diff.md, the generator's difflib count with autojunk off: +183/−199, 382 changed lines in 86 change blocks / 14 hunks; a GNU-diff count of the same pair gives 307 changed lines — the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 86 change blocks — 30 specific (34.9%), 45 heuristic (52.3%), 11 residue (12.8%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 48 |
| TRANSLATION-ANCHORED | 16 |
| DRAFT-HOST | 9 |
| COMMENT-TEXT | 3 |
| CSS-BODY | 3 |
| IFTAGS | 3 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 3 CSS-BODY blocks are the font-stack substitution (B69, section 4), a single-rule font restatement (B72, section 4), and the exhibit container's closing-tag change (B79, section 8); the 1 EXHIBIT-RESTRUCTURE block is the image-block exhibit's repoint and caption change (B17, sections 2 and 8), not a restructuring — the exhibit census is complete; the 11 residue blocks are seven theme-color swatch name lines in the color table (B10–B16, section 6), a heading translation (B6), two single exhibit lines (B62, B73), and a formatting-artifact line with its heading (B80, section 8), all resolved by shape. The classifier's ANNOTATION count is 0, but the candidate carries three porter annotations riding inside other labeled blocks (B67, B69, B86) — section 10 records them, per the standing lesson that annotations hide inside other blocks. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:legend-of-blue-jp; original theme:legend-of-blue on scpko at reference revision 78; candidate `pages/theme:legend-of-blue-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 KO5 wave (sources.tsv kind: standard; no production JP counterpart is recorded). The original opens with its tag gate (`[[iftags +테마]]`, original L1); the candidate places its delivery frame ahead of the localized gate (`+テーマ`, candidate L1–10), the frame order the self-delivering candidates in this population use.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate is P2, the frame is P4/P6 (section 3).
- **Verify:** The sources.tsv row for legend-of-blue-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a labeled bare Rate (two labels, 평가 모듈 and 정보형 평가 모듈, original L3–6, block B2) and an info pair (`:scp-wiki:info:start`/`more`/`end`) whose body is the placeholder text "Info about your page." (original L7–13, block B3, INFO-DEL). The candidate deletes both and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–21) carrying the eight ruling-3 fields (title 青の伝説テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 🌊 바다의 전설 테마 🐳, the original's title kept whole, emoji included; 著作権者 salamander724 / thd-glasses; 作成年 2021; 初訳時参照リビジョン 78; the source link, section 7). The author field names both creators, matching the original's prose attribution (its intro names [[*user salamander724]] and [[*user thd-glasses]] as the makers, and the candidate's intro keeps both, candidate L23) — no named creator is dropped. The translator field took its ruling-3 form in 1869877. No license box is appended; instead the original carries its own image-copyright section, and the candidate translates it in place (sections 4 and 8) — the attribution record for this theme is the original's own, carried over, not a supplement. The source link in the credit block is the site of this package's post-verdict repair; its full account is the per-theme record, and its current form is verified in section 7.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become), and the placeholder info pair goes with it — its body was never real content. Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L12–21 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER line 1653: P3 credit fields FIXED, credit waves, checker-verified); the source link's defect and repair are the per-theme record.

### 2. Includes and components

- **What:** The include repoints: the image-block exhibit's include, `component:image-block` → `:scp-jp:component:image-block` (block B17; its asset host is section 4 and its caption is section 8); the toggle-sidebar include, `:scpko:component:toggle-sidebar` → `:scp-jp:component:toggle-sidebar`, which also moves — the original places it at the head of its code-exhibit zone (original L214), and the candidate places it at the page's tail as a live page-level include (candidate L896's zone, block B86); and the credit includes (section 1). The head's interwiki-style include is a delivery line (section 3). The usage example's include carries the COMPONENT-SWAP label (block B8) because its wiki prefix changes branch (`:scpko:` → `:scp-jp:`); its name form is section 7.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; all repointed targets have verified JP counterparts. The toggle-sidebar relocation follows from the exhibit conversion of section 8: in the original the include sits inside a live module zone, and once the exhibit is a code listing the component has to live at page level to keep functioning — the tail is where this candidate's other post-gate furniture sits.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live include names a `:scp-jp:` target; the toggle-sidebar stands at the tail.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original has no head delivery frame at all: its CSS lives in the page's code-exhibit zone as a live `[[module CSS show="true"]]` (original L218's zone, block B67), so the page delivers through the exhibit itself, and there is no separate own-code address. The candidate delivers in the population's frame form: a head `[[module CSS]]` importing its own `local--code/theme%3Alegend-of-blue-jp/1` from the draft host (candidate L1–3), an interwiki-style include at priority 1 naming the same (candidate L5–8), and the exhibit converted to a `[[code type="CSS"]]` listing whose content is what the /1 serves. The draft-host form reaches further into this candidate than the frame: the served exhibit's own asset addresses are re-hosted to the same draft host (the background images of section 4, blocks B70, B71, B77, B78), as are the source URLs in the copyright section's entries for the theme's own files (blocks B81, B82). Nine blocks carry the DRAFT-HOST label in all; T1's checker counts six pseudo-ref errors among them by its own rule for live references.
- **Why:** P4/T9 (delivery served from JP hosts) and P6/T3 (the interwiki-style frame): the candidate gives the theme the same explicit delivery the rest of the population carries, instead of the exhibit-module delivery the KO page used. The draft-host form is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting — for the frame lines and the re-hosted asset addresses alike.
- **Verify:** Read candidate L1–10 against original L1 and L214–218; `grep -n 'sigma10-jp-test' candidate.txt` — the frame lines, the exhibit's asset addresses, and the copyright entries' source lines.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts — a documented substitution, not a kept-name drop. The original loads Korean display typography from three hosts: Google Fonts (Basic and IBM Plex Mono), an UnYetgul stylesheet from scpko.wdfiles.com, and two @font-face faces from cdn.jsdelivr.net (noonfonts: 완도청정바다체 "Wando Clean Sea" and 완도희망체 "Wando Hope") (original L220–232, block B67). Its stacks name those faces first (`--body-font: '완도청정바다체', sans-serif`; `--header-font`/`--title-font: '완도희망체', 'UnYetgul', sans-serif`). The candidate loads one import, IBM Plex Mono plus Noto Serif JP from Google Fonts (candidate L219), and rewrites the stacks wholesale to `'Noto Serif JP', 'Yu Mincho', 'Hiragino Mincho ProN', serif` for all three variables (block B69), restates the one other rule that named UnYetgul (block B72), and sets the image caption's font to 'Noto Serif JP' (block B17). The substitution is documented in the file: the :root block's comment reads "Typefaces (SCP-JP: substituted with exception-host fonts; see page notes)" (section 10). Checked explicitly: no Korean face name survives anywhere in the candidate (`grep -n 'UnYetgul\|Wando\|완도\|Basic' candidate.txt` returns nothing), so there is no named-but-unloaded case of the kind flagged in this batch's laruetheme and laughter-and-knives packages — the names were replaced, not orphaned. Assets: the theme's five own images are re-hosted from scpko.wdfiles.com to the draft host with their file names kept — legend_of_blue.png (the image-block exhibit, block B17), underwater.jpg, Makara.png, PAPER.jpeg, and helm_wheel.png (the CSS backgrounds, blocks B70, B71, B77, B78). The copyright section's entries for third-party images (the Wikimedia Commons files at the tail) keep their original source URLs, as they should: only the theme's own files move.
- **Why:** P7/T5: the theme's display faces are Korean faces for Hangul text; the JP text needs a JP face, and the population's treatment is substitution with the change documented — the failure shape P7 guards against is the silent orphan (a name kept with no load), which the grep above excludes. P5 with KB-17 (asset hosts): the theme's own images are re-hosted to the JP side; the draft-host form is class (iii) at this stage.
- **Verify:** `grep -n '@import\|@font-face' candidate.txt` — the one font import, no @font-face; `grep -n 'wdfiles' candidate.txt` — the draft-host lines only, no scpko storage remains.
- **Disposition:** Substitution applied and documented in-file; asset re-hosts DISPOSITIONED (class (iii)).

### 5. Header and sidebar furniture

- **What:** No header-variable change fires in this package (no HEADERVAR label): the theme's header rendering rides on the font variables of section 4 and its background images, all treated there. The sidebar furniture is the toggle-sidebar component, repointed and relocated to the page tail (section 2) — in the candidate it stands after the closing gate alongside the credit-CSS module (block B86's zone), live at page level rather than embedded in the exhibit zone as the original had it.
- **Why:** Stated so the section's near-emptiness is a checked fact: this theme's furniture changes are the font substitution and the sidebar component's move, both recorded in their own sections rather than duplicated here.
- **Verify:** The label counts in the class summary (no HEADERVAR); `grep -n 'toggle-sidebar' candidate.txt` — the tail placement.
- **Disposition:** Standing (nothing to disposition).

### 6. Text translation

- **What:** The body translates throughout: the intro (including the Chonghaejin attribution, candidate L23), the usage prose, the theme-color table — whose swatch name lines are the seven unlabeled residue blocks B10–B16 (for example 해수대 → 海水， candidate L35's zone), resolved here by shape — the component exhibits, and the image-copyright section, whose field labels translate （파일명 → ファイル名, 제작자 → 制作者, 라이선스 → ライセンス, 출처 → 出典） while the authors and licenses they record stay exact (blocks B81–B85). The translation even reaches the license links: the Creative Commons deed links are localized from deed.ko to deed.ja and their labels normalized to "CC BY-SA 3.0" (candidate L882, L887). The COMMENT-TEXT blocks (3) are the CSS comments following the prose into Japanese. One completion rides in the intro: the original's group link has an empty label (`[[[chonghaejin|]]]`, original L16), and the candidate supplies the group's name as the label (`[[[chonghaejin|清海鎮]]]`) — the link target is unchanged.
- **Why:** P9/P10 (body, exhibits, and documentation into Japanese). The copyright section is the sensitive case: its labels are prose and translate, while its contents (file names, author names, license names, source URLs) are records and stay byte-exact apart from the re-hosted own-file sources of section 4 — which is what the blocks show.
- **Verify:** Read candidate L875–902 against original L883–905 for the copyright section; `grep -n 'deed' candidate.txt` — deed.ja twice, no deed.ko.
- **Disposition:** Applied (T5's verdict for this theme is PASS in the ledger aggregate — the only T5 PASS among this batch's FINDINGS rows, recorded in section 12).

### 7. Links and references

- **What:** The credit block's source link now reads `https://scpko.wikidot.com/theme:legend-of-blue` (candidate L19) — the host recorded for the original in sources.tsv, and the form that serves the page. At the ledger determination it read `https://scp-wiki-ko.wikidot.com/theme:legend-of-blue`, the KO branch's old host, which does not serve it: that was T4's one finding against this theme and the subject of the post-verdict repair detailed in the per-theme record (probe pair: 404 on the old host, 200 on scpko.wikidot.com). The usage example (candidate L29) reads `:scp-jp:theme:legend-of-blue-jp` in its post-sweep form (per-theme record). The intro's links: the two author links and the Chonghaejin group link (section 6), all relative and resolving on the hosting wiki as the original's did. No other outbound prose links ride in the candidate.
- **Why:** P9 link hygiene with the dead-reference evidence standard: a credit source link must name the serving original, and the repair history is exactly that standard applied — probe both hosts, follow the one that serves.
- **Verify:** `grep -n 'scpko.wikidot\|scp-wiki-ko' candidate.txt` — the serving host in the credit link and the porter comment; the old host appears nowhere.
- **Disposition:** Applied, with the source link's defect and repair recorded in the per-theme record.

### 8. Structure and exhibits

- **What:** Four structural acts beyond the credit swap (section 1) and the delivery frame (section 3). (1) The exhibit container conversion: the original presents its CSS as a live `[[module CSS show="true"]]` inside a collapsible (original L214–218's zone); the candidate presents it as a `[[code type="CSS"]]` listing inside the same collapsible form, with the closing tags restated to match (blocks B67, B79) — the exhibit's content is the same CSS, its presentation changes from executed module to listing, which is what makes the head frame of section 3 the delivery instead. (2) The credit-CSS supplement at the tail (block B86, T7-CREDIT-CSS): after the closing gate, the candidate appends the relocated toggle-sidebar include and a `[[module CSS]]` restating one credit rule for the JP credit module's structure, with its reasoning in an English comment (section 10): the KO theme styles the credit anchor through a `<p>` wrapper (`.creditButton p a`), the JP credit module emits the anchor as a direct child of `.creditButton`, and the rule is restated as `#page-content .rate-box-with-credit-button .creditButton a { border-left: solid 1px transparent; }`. (3) The image-block caption's form (block B17): the original's caption is an inscription with ruby glosses — Hanja characters each carrying a Hangul reading in a ruby span, set vertically in UnYetgul. The candidate keeps the full Hanja inscription as plain vertical text in 'Noto Serif JP' and drops the ruby gloss markup; the readings were Korean pronunciations, and a JP gloss would be a new translation act rather than a carry-over. Recorded here and in the per-theme record as an observation, not silently. (4) A formatting-artifact line (`@@@@`, original L905's zone, block B80) is deleted at the copyright section's head; it renders nothing. The EXHIBIT-RESTRUCTURE primary (1) is block B17's repoint-and-caption zone, adjudicated in the class summary; the exhibit census is otherwise complete (color table, usage, image exhibit, component exhibits, the full code exhibit, and the copyright section).
- **Why:** P8 (exhibit structure follows the original) governs the census; each act above is argued on its own ground — the container conversion is the delivery change's other half, the credit-CSS restatement is T7 (a rule restated because the JP module's DOM differs, with the reason written in the file), and the caption's glosses are the one place the port simplifies rather than carries over, which is why it is named.
- **Verify:** Read candidate L213–220 against original L214–232 for the container; candidate L892–902 for the tail supplement; candidate L72 against original L65–70 for the caption.
- **Disposition:** Applied and recorded; the caption observation is carried in the per-theme record.

### 9. Formatting only

- **What:** No whitespace-only or reindent blocks fire in this package (WS-ONLY and REINDENT both absent from the label counts). The nearest item is the deleted `@@@@` artifact line (block B80, section 8), which is a content-line deletion of a non-rendering artifact, counted there rather than here.
- **Why:** Stated so the section's emptiness is a checked fact: the classifier separates formatting mass from content mass, and here there is no formatting mass to excuse.
- **Verify:** The label counts in the class summary; block B80 in classification.json.
- **Disposition:** Standing (nothing to disposition).

### 10. Porter annotations

- **What:** Three porter annotations stand in the candidate, all in English, all riding inside other labeled blocks (the classifier's ANNOTATION count is 0 — this is the standing case of annotations hiding inside other blocks, checked explicitly). (1) The code exhibit's banner comment (candidate L218, inside block B67): "SCP-JP port of the Korean branch theme "바다의 전설 테마". Original: https://scpko.wikidot.com/theme:legend-of-blue (rev 78)." — the port's provenance note at the head of its served CSS; this is the second of the two lines the 2a8a125 repair touched (its host read scp-wiki-ko.wikidot.com before the repair). (2) The :root typeface comment (candidate L238's zone, inside block B69): "Typefaces (SCP-JP: substituted with exception-host fonts; see page notes)" — the font substitution's in-file marker (section 4). (3) The tail credit-CSS comment (candidate L899's zone, inside block B86): the explanation of the .creditButton restatement quoted in section 8. No other porter prose stands in the file.
- **Why:** T11: annotations are how judgment calls stay auditable. This candidate is the batch's model case — its three judgment calls (provenance, font substitution, credit-structure restatement) each carry their note at the site of the change.
- **Verify:** `grep -n 'SCP-JP' candidate.txt` — the three annotation sites.
- **Disposition:** Standing (the annotations are part of the port as delivered).

### 11. Dispositions and exceptions

- **What:** Three standing items, all closed. (1) T1's pseudo-ref ×6 (sections 3 and 4): class (iii), sanctioned draft-host form. (2) The render row's items: page-overflow of 361–362px at the 320px viewport on both the theme page and the sample; the sample's credit-modal reading, dispositioned preview-form (the standing GOSIGN-TESTS T2 amendment); and the T3 reading that the theme-color swatch table is wider than the content column, its right-hand cells cut at the 375px and 320px viewports on both pages — the table is the original's own design (a full-width table with fixed cell heights), kept as the original made it, so the reading records the original's geometry reproducing faithfully at small viewports rather than a port-introduced break. (3) T4's one finding, the broken source link （型3): not dispositioned but repaired — after the verdict, by 2a8a125, with the probe evidence in the per-theme record. The ledger's disposition list also records this theme's P3 credit fields as FIXED by the credit waves (GOSIGN2-LEDGER line 1653).
- **Why:** A disposition names its ground: class (iii) for the draft host, the preview-form amendment for the modal reading, and the repair commit for the link. The swatch-table reading names its ground too — the original's own table geometry, present on both pages because the port keeps the table.
- **Verify:** The theme's rows in RENDER-ROWS-2 and LOCALIZE-ROWS; the disposition line in GOSIGN2-LEDGER.
- **Disposition:** DISPOSITIONED (items 1 and 2); item 3 closed by repair (2a8a125).

### 12. Verification record

- **What:** T1 (source check, T1-ROWS row 276): pseudo-ref ×6 (exit 1, 6 errors / 0 warns / 1 info), no hotlink and no http errors — the candidate's own file is clean of the error classes that attach to source text, its draft-host lines being the class-(iii) population. T4 (localize check, LOCALIZE-ROWS row 271, wave LOCALIZE-S2-F): FINDINGS, 1 finding — 型3, the broken source link, with the row's own note that everything else was in order and nothing was display-breaking （それ以外は整っており表示崩壊級なし). T2/T3 (render check, RENDER-ROWS-2, wave RENDER-S2-H (KO5)): the readings of section 11. The go-sign ledger row (§(b) row 272) aggregates T1 FINDINGS (classified), T2 FINDINGS, T3 FINDINGS, T4 FINDINGS, T5 PASS — every finding classified, none OPEN. Those are the verdict lines the stamp preserves; the stamp's STALE header records that the file changed after they were computed (per-theme record).
- **Why:** The counts are the acceptance evidence for the sections above: each checker's scope is stated so a clean result is not read past what the checker can see (T1 reads this file; T4 is what caught the link, because the link is in this file; the render check is what saw the table geometry).
- **Verify:** The three ledger-part files named above, rows 276 and 271 and the theme's render row; GOSIGN2-LEDGER §(b) row 272 for the aggregate.
- **Disposition:** PASS at the ledger determination, with the items of section 11 dispositioned or repaired as recorded.

## Per-theme record

**The post-verdict repairs, and why the stamp reads STALE.** This theme's candidate is one of five KO candidates whose credit source link and porter banner comment named the KO branch's old host, scp-wiki-ko.wikidot.com, which no longer serves those pages. T4 had charged the broken link as this theme's one finding （型3, section 12), but no wave repaired it before the go-sign determination, so the verdict was computed against the file with the broken host. After the verdict, canonical commit 2a8a125 ("pages: KO source-link host correction") repaired all five files — this theme, theme:jiha-jp, theme:kcia10-jp, theme:minimal-scp-foundation-by-cocoonist-jp, and theme:king-s-palace-jp — by host replacement only, two occurrences per file (here: the credit link at candidate L19 and the banner comment at candidate L218). The repair commit records its probe evidence: on 2026-11-17 all five theme pages returned 404 on the old host and 200 on scpko.wikidot.com. Because the file changed after the verdict, the generated stamp reads STALE and preserves the pre-change verdict lines below it rather than carrying the PASS over — that is the designed behavior, and this package follows the jiha package's treatment of the same repair family: build against the current candidate, let the stamp say STALE, and put the explanation here. A second, smaller post-verdict change landed after the stamp's computed-against state: the usage-example sweep (b5cb724) inserted -jp into the example's self-reference (candidate L29), so the current file's SHA-256 (231f8a00…, Provenance table) differs from the stamp's recorded 0dbe18cb…; a harvest-time regeneration will keep the STALE marking with the updated hash. Neither repair changes any verdict line's substance: the link repair removes the one defect T4 had found, and the sweep line is the population-wide example correction.

**The image caption's ruby glosses do not survive (observation).** The original's image-block caption is the theme's inscription text in Hanja, each character glossed with its Hangul reading in ruby markup (original L65–70). The candidate prints the inscription complete and in order as plain vertical text (candidate L72) and drops the gloss markup. The glosses are Korean pronunciations; supplying Japanese readings would be a new translation decision, and printing Korean readings in a JP exhibit would serve no JP reader. The simplification is recorded here and in section 8 for the coordinator's judgment, alongside the batch's other exhibit-form observations.

**The font substitution is documented in the file itself.** Unlike the batch's two font defects (laruetheme, laughter-and-knives: names kept, loads dropped), this theme's Korean display faces were replaced outright by a JP serif stack, with the substitution marked at the site (the :root comment, section 10) and no orphaned face name left in any stack (section 4's grep). It is recorded here as the third shape of the batch's font story: substitution with documentation, against repair (lumina) and defect (the two BHL themes).

## Change set outside the two diffed files

| File | Change |
|---|---|
| `pages/theme-decoration-sample-legend-of-blue-jp.txt` | The theme's decoration sample: a JP page applying the candidate, the surface the T2/T3 render checks measured (section 11's sample readings) |

## License and attribution

- **Title:** 🌊 바다의 전설 테마 🐳
- **Author:** salamander724 / thd-glasses
- **Source:** https://scpko.wikidot.com/theme:legend-of-blue — revision 78
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
