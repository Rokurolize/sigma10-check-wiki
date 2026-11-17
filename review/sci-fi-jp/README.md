# Review package — theme:sci-fi-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:sci-fi-jp — origin CN, population #222 [GOSIGN2-LEDGER (b) row 222]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 8e01f6ce53cd7e629417c9bc7da939dcf6f648d8f2fc08c5bb367f2498505471); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 6 warns / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 187; GOSIGN2-LEDGER (b) row 222]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 452–471px@320/375 + 771px@768 (both engines) + runtime-hotlink site-theme chain; sample credit-modal (preview-form) + page-overflow incl. 884px@768; T3 .open-menu toggle overlaps code text at ≤375 on both pages; full-engine (chromium+webkit) coverage. [RENDER-ROWS-G (CN13)]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN13)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 221, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 221]
- FIX5 re-judgement: item 75 (class H) FIXED — FIX5-TEXTB §4, commit 3f328d8: dead sci-fi-hub link (probe HTTP 404, no JP counterpart) converted to plain text with a translator's note; checker link-target-missing warning cleared [GOSIGN2-LEDGER-SUPPLEMENT (a) item 75]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:sci-fi-jp.txt sha256:8e01f6ce53cd7e629417c9bc7da939dcf6f648d8f2fc08c5bb367f2498505471; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); the stamp reads STALE by design, because the candidate changed after the verdict (the b5cb724 usage sweep, per-theme record). The frozen ledger remains the verdict for the bytes it judged |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 75 [H] (dead prose link to sci-fi-hub, charged under P11) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 75: **FIXED** (FIX5-TEXTB §4, commit 3f328d8); re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c3): P1 DISPOSITIONED (posting-procedure convention class), P3 credit fields FIXED by the credit waves; ledger §(c2) render row: page FINDINGS (4.15px@768, KB-33), page theme self-delivery (KB-44b), mobile logo clipped (KB-42/KB-41), page webm video frame visible (KB-54), sample credit-modal preview form (KB-32); T1 baseline 6 errors, all pseudo-ref (draft-host class (iii)) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |
| Flags from this package | Four, none charged by any ledger row: a credit pointer in two carriers (section 1), a duplicated font import (section 4), a tail port note whose factual claim the bytes refute (section 10), and a prose link to theme:bedrock that 404s on SCP-JP while theme:bedrock-jp exists (section 7). Flagged, not edited |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:sci-fi | theme:sci-fi-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 4, the first-translation reference revision, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 4 (candidate L18) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-sci-fi.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:sci-fi-jp.txt`, copied at worktree HEAD c92a320; the file's last content change is commit b5cb724 (usage-example sweep) |
| Lines / bytes | 1,825 lines / 51,843 bytes (the last line carries no trailing newline, so `wc -l` reports 1,824) | 1,850 lines / 58,045 bytes |
| SHA-256 | 89bdcf16aab3e610f298eaf12f1bbb84c613b17486683ba0dc003e1171e59cad | 8e01f6ce53cd7e629417c9bc7da939dcf6f648d8f2fc08c5bb367f2498505471 |

Wave history: Stage 2 CN13 (816deb1) created the port; FIX-CREDIT-D (1869877) normalized its translator attribution; FIX4-IWB (5559209) re-prioritized its self-delivery frame (section 3); FIX5-TEXTB (3f328d8) applied item 75's fix; the usage sweep (b5cb724) completed its own-name examples (per-theme record). The sources.tsv note for this row claims the original was superseded upstream since the reference revision; the cited follow-up artifact records rev4 → rev4 with no changes, so the note is wrong — the corrected form is in the per-theme record for the coordinator's harvest correction (sources.tsv is not edited here).

## Summary

A full single-file CN theme: one code block carries the author's compiled main.css (1,578 lines in the original), wrapped by a short exhibit body (intro, credits, usage with two include-parameter mechanisms, and two code-source exhibits) and delivered through a head module plus interwiki-style frames. The candidate keeps that architecture and the CSS body essentially verbatim — measured churn is +171/−151 changed lines (diff.md, the generator's difflib count) over 1,800+ lines, and most of it is the head frame (delivery host, JP font loads), the credit swap, and the translated body prose; the 1,600-line stylesheet is touched at five loci, all enumerated in sections 4, 5, and 10. The blocking item was one dead hub link in the translated prose. Four further defects were found by this package's checks and are flagged below; none is edited here.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 79 change blocks — 31 specific (39.2%), 45 heuristic (57.0%), 3 residue (3.8%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Label counts are signature spans across blocks (a block carries several).

| Label | Spans |
|---|---|
| COMMENT-TEXT | 57 |
| TRANS-UNANCHORED | 49 |
| TRANSLATION-ANCHORED | 21 |
| GLYPH-FORM | 7 |
| DRAFT-HOST | 4 |
| INCLUDE-REPOINT | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| SELF-DELIVERY | 3 |
| ANNOTATION | 2 |
| COMPONENT-SWAP | 2 |
| ESCAPED-INCLUDE | 2 |
| IFTAGS | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

## Standing sections

### 0. Header and provenance frame

- **What:** The original's delivery head stands inside its gate: `[[iftags +theme]]` (original L1), then a head module importing its own /1 (original L3–5), then the priority-1 interwiki-style include naming its own /1 (original L7–9). The candidate's frame stands outside its gate (candidate L1–8): the same head module with the draft-host /1, and the same include at priority 2 (the FIX4-IWB change, section 3); the gate (`+テーマ`, candidate L10) wraps credit and body. Provenance route: derived from the original at the reference revision (first translation, rev 4). Kind K5b-5: the candidate's body is the author's compiled main.css, inlined as one code block (review/sources.tsv note) — the theme has no base theme and no separate fragment; its mechanism exhibits (inc-css, inc-achi) are in-page parameter templates (sections 2 and 8).
- **Why:** The frame is where delivery is declared; P6/T3 governs its priority. Declaring the K5b-5 scope here explains why this package's stylesheet is one 1,600-line block rather than a layered delivery.
- **Verify:** Read original L1–9 against candidate L1–10.
- **Disposition:** Standing (frame form; the priority change is section 3).

### 1. Credit and attribution

- **What:** The original carries no credit block and no license box: its furniture is a bare Rate (original L39–41), and its attribution is prose — "本主题由 [[*user hoah2333]] 制作，灵感来自 [[*user EstrellaYoshte]] 的Sigma主题" (original L57: the theme was made by hoah2333, inspired by EstrellaYoshte's Sigma). The candidate carries the preview credit block (candidate L12–21) with the eight ruling-3 fields and adds a license box at the tail (candidate L1836–1841; T4 supplement, section 11 of the appendix). **FLAG — the credit author field is a pointer naming nobody, in two carriers.** The credit block's **著作権者:** reads "原語版ページの作成者に同じ（scp-wiki-cn の theme:sci-fi）" (candidate L16), and the license box's author parameter reads `author=scp-wiki-cn theme:sci-fi の作者` (candidate L1837). Neither names the author, although the original names him (hoah2333, original L57) and the candidate's own translated prose names him (candidate L54: 本テーマは [[*user hoah2333]] によって制作されました). Under the credit-field standard this is the pointer-in-place-of-a-name defect: the original names the author, the field names nobody. The EstrellaYoshte inspiration credit is carried in the same prose line (candidate L54). **翻訳責任者:** AI, **翻訳年:** 2026 (ruling 3). No T7 credit-module CSS (the preview module supplies the furniture). The original's bare Rate is removed (P3; BARE-RATE-DEL in B7): the preview credit block is rate-bearing, so no rating surface is lost.
- **Why:** P3/T1 (credit block swap), ruling 3 (the eight fields; the author field names the work's author), T4 (license box supplement), KB-09 (no bare Rate beside a rate-bearing credit block). The flag's ground is the same ruling-3 field standard the credit waves enforced: a field that defers to another page's authorship fails the check the field exists to pass.
- **Verify:** Read candidate L12–21 and L1836–1841 against original L57 and candidate L54.
- **Disposition:** Credit fields FIXED in form (credit waves; ledger §(c3)); the author-pointer is a flag from this package (per-theme record), not a disposition.

### 2. Includes and components

- **What:** Frame includes: the interwiki-style self-delivery (section 3) and the credit pair (section 1). Body includes: the two mechanism exhibits — the `{$inc-css}` template (candidate L30–40) defining the interwiki-style call with `css={$inc-css}` for a user-supplied /1, and the `{$inc-achi}` template (candidate L30–40 region) defining the `component:achi` call with `{$text}` / `{$icon}` parameters; both are carried from the original (original L29–37) with their parameter gates intact (the template still guards on `{$inc-css}` / `{$inc-achi}` being set — nothing was inlined unconditionally or dropped). The live sidebar-copy include (candidate L42–46, priority 1) is the original's own mechanism copy (original L39–43 region), not a duplicate of the frame include: the frame names the theme's own /1 at priority 2, the body copy is the documented inc-css exhibit. The achi component itself is not ported as a page: the candidate's usage text documents it as an external component (candidate L182), as the original does.
- **Why:** P1 (branch forms), T8 (component swaps), the include-parameter gate standard (a documented mechanism's definitions and gates must survive the port — here they do).
- **Verify:** `grep -n '\[\[include' candidate.txt` (7 include lines); read candidate L30–46 against original L29–46.
- **Disposition:** Standing; no include item charged, and the gate check passes.

### 3. Delivery and code loading

- **What:** One code block each side (census over all forms: original `[[code type="css"]]` at L235–1815; candidate `[[code]]` at L237–1833), and the /1 references name it: the head module @import (candidate L3) and the interwiki-style include (candidate L5–8) both point at the candidate's own draft-host local--code /1, which is that block — the stylesheet itself, not an exhibit (the navla-style check passes: there is no second stylesheet block). The delivery host changes from scp-wiki-cn.wikidot.com (original L4, L8) to the draft host sigma10-jp-test.wdfiles.com (DRAFT-HOST spans, class (iii)). One deliberate priority change: the self-delivery include stands at priority 2 in the candidate (candidate L6) where the original has priority 1 (original L7). That is FIX4-IWB (commit 5559209), which touched this file in exactly that one line: under the population's priority discipline the theme's own layer belongs at 2 (1 is the normalize/base slot), and the two priority-1 includes remaining in the candidate (the `{$inc-css}` template copy and the live sidebar copy, candidate L23–27 and L42–46) are the original's own exhibit pair, not the charged duplication — the interwiki census adjudication for this theme. The code block's type attribute is dropped (`[[code type="css"]]` → `[[code]]`): display form only; the block's role is unchanged.
- **Why:** P4 (foreign local--code → own-wiki local--code; draft host at draft stage), P6/T3 and KB-07 (priority discipline), KB-44b (theme self-delivery via the frame, the render row's disposition for the page finding of that name).
- **Verify:** `grep -n 'local--code' original.txt candidate.txt`; `git show 5559209 -- pages/theme:sci-fi-jp.txt` (one line).
- **Disposition:** Standing; priority remedy recorded (FIX4-IWB, 5559209).

### 4. Fonts and assets

- **What:** Font loads in the candidate's code block, in order: Font Awesome 4.7.0 from cdnjs (candidate L241), Font Awesome 5.15.3 (L243), Noto Sans SC and Noto Serif SC (L245), Font Awesome 4.7.0 from cdnjs again (L248), Noto Sans JP (L250), Noto Serif JP (L252). **FLAG (minor) — a duplicated font import:** the cdnjs Font Awesome 4.7.0 URL appears twice (candidate L241 and L248). The original loads it once (original L238); the duplication arose because the port's head additions (the JP-face loads and the re-asserted icon load) duplicate the original's own import — the second copy is redundant (identical URL, no parameters differ). The JP faces themselves are the port's P7 loads (JPFONT-LOAD in B22): Noto Sans JP and Noto Serif JP are added alongside the original's SC faces, which are retained. Application: the JP faces are applied in the sidebar css= channel — both copies of the URL-encoded sidebar include decode to a `--UI-font` stack naming `'Jost','Noto Sans JP'` where the original's encoding named `'Noto Sans SC'` (the P7 swap inside the encoding; residue B3/B5, appendix) — while the code block's own `:root` stacks still name the SC faces (e.g. candidate L267–268). Every named face is loaded somewhere in the file (the SC faces' loads are retained), and every loaded face is applied somewhere (the JP faces in the sidebar channel), so neither the named-but-unloaded nor the loaded-but-unapplied flag fires; the shape is recorded here because the application locus is easy to miss. Assets: no theme files are re-hosted (the theme references no local--files assets of its own; its images are the original's external URLs, carried).
- **Why:** P7/T5 and KB-16 (JP faces loaded for a CN theme whose stacks name CN faces), the duplicated-import standard (identical loads are minor defects with both loci).
- **Verify:** `grep -n '@import' candidate.txt` (six loads) against original L237–249 (five); decode either sidebar css= parameter to check the stack swap.
- **Disposition:** JP loads standing; the duplicated Font Awesome import is a minor flag (per-theme record).

### 5. Header, sidebar, and site furniture

- **What:** The theme's `:root` furniture is carried verbatim from the compiled CSS: `--title: "SCP基金会"` and `--subtitle: "控制 · 收容 · 保护"` (candidate L278–279, identical to original L274–275) keep the original's simplified-Chinese forms — 基金会 where Japanese writes 基金會/財団， and the slogan in simplified characters. These are the theme's brand strings, functioning as marks (the theme's documentation teaches users to override them per site, candidate L197–198), and header language is in any case case-by-case taste under ruling 2, recorded out of scope for migration correctness (KB-57); the glyph-form spans in the CSS body are the compiled body's retained forms, adjudicated in the appendix. The sidebar furniture is the inc-css channel of section 4. The three exhibit labels that headed the original's Rate and credit module groups ("评分模块", "信息模块", "成就模块", original L39–53) remain in the candidate as prose headings (candidate L48–52) after the P3 removal of the module groups they headed — inert headings over the carried achi exhibit, the R3 shape recorded in section 8.
- **Why:** Ruling 2 / KB-57 (header language as identity), KB-16 (the sidebar stack is a font locus, section 4), R3 (headings whose exhibits were restructured).
- **Verify:** Candidate L278–279 against original L274–275; candidate L48–52 against original L39–53.
- **Disposition:** Standing (identity strings retained; no furniture item charged — the ledger's charges for this theme were the hub link and the standing families).

### 6. Text translation

- **What:** The body prose is translated throughout (P10): the intro and credits (candidate L54–56), the usage sections (install, CSS variables, the inc-css and inc-achi documentation, candidate L58–233), the code-source exhibit headings, and the translator's note of item 75 (section 7). The CSS body's comments are carried verbatim in the original's languages (COMMENT-TEXT spans, 57 — the compiled body's banner and section comments, including the source-map-era comments; the closing rule keeps compiled CSS as delivered). Two in-CSS text changes ride with the delivery: the dropped sourceMappingURL comment and the added `/* page module css */` comments (section 10). The TRANS-UNANCHORED mass (49 spans) is the body translation pairs; the heuristic share is adjudicated in the appendix.
- **Why:** P10 (body and usage translated), the closing rule (the compiled stylesheet is the author's artifact; its comments are not porter text).
- **Verify:** Read candidate L54–233 against original L57–232 section by section.
- **Disposition:** Standing (the port itself); the one charged text item is item 75 (per-theme record).

### 7. Links

- **What:** The FIX5 item lives here (per-theme record): the dead `[[[sci-fi-hub|…]]]` link in the intro prose is de-linked with a translator's note (candidate L204). Two further prose links were checked by this package. (a) The scp-anthology-hub link on the same line (candidate L204) is kept as a link and resolves: probed 2026-11-17, https://scp-jp.wikidot.com/scp-anthology-hub returns HTTP 200 — correctly kept, not a defect. (b) **FLAG — the design-reference links in the credits prose (candidate L54):** the line names the theme's relatives as bare links, `[[[theme:ar|アンダーソン・ロボティクス・テーマ]]]` and `[[[theme:bedrock|Bedrockテーマ]]]`. Probed 2026-11-17: theme:ar exists on SCP-JP (HTTP 200 — a production page, so that link resolves and is not a defect), but theme:bedrock returns 404, while this repo carries the JP candidate `pages/theme:bedrock-jp.txt` — the bedrock link names a page that will not exist on SCP-JP in place of the port that will, the pattern-11 shape (the same family as item 75, uncharged for this locus). The credit source link (candidate L19) points at the CN original on scp-wiki-cn.wikidot.com, matching the recorded host in review/sources.tsv (scp-wiki-cn). The anthology-card CSS selectors keyed to `[href*=scp-wiki-cn]` (candidate L1600, L1604) are carried verbatim from the original and were dispositioned in the ledger (inert for JP-internal links); they are CSS, not links.
- **Why:** P11 (prose links must resolve on the JP wiki; a link to a non-existent page whose JP port exists under the -jp name is the charged family).
- **Verify:** `grep -n 'theme:bedrock\|theme:ar' candidate.txt` (one line, L54); the two probes above are one fetch each.
- **Disposition:** Item 75 FIXED; anthology link verified live; the bedrock link is a flag (per-theme record).

### 8. Structure

- **What:** The original's architecture is preserved (the localize.md closing rule): gate, frame, credit zone, intro, usage with its two parameter mechanisms, code-source exhibits, the single code block, license box at the tail. The mechanisms' definitions are all carried: the `{$inc-css}` gate and template (candidate L30–40), the `{$inc-achi}` template with its `{$text}` / `{$icon}` parameters, and the sidebar-copy include — checked against the original's definitions, nothing inlined unconditionally, nothing dropped (section 2). Structural changes: (a) the credit swap at the head (section 1); (b) the Rate and credit-module exhibit groups removed under P3, leaving their three headings as prose (section 5; EXHIBIT-RESTRUCTURE spans in B7/B9 adjudicated against the exhibit census — the exhibits themselves, Rate and the EN/CN credit module pair, are the P3 removals, and the achi exhibit that followed them is carried); (c) the license box added at the tail (appendix); (d) inside the code block, `@charset "UTF-8"` stands after the import list and banner comments (candidate L254) where the original has it first (original L236) — a displaced at-rule: CSS ignores a `@charset` not in first position, so the rule is inert in the candidate; the original's is equally inert in Wikidot's module delivery. Recorded as an observation, not a flag: no behavior differs.
- **Why:** R3 (restructure grounds stated), the closing rule (structure and rule order preserved in the compiled body).
- **Verify:** Structural census: `grep -n '\[\[module\|\[\[code\|\[\[iftags\|\[\[div' original.txt candidate.txt`.
- **Disposition:** Standing; no structural item charged.

### 9. Formatting only

- **What:** The compiled CSS body is carried byte-close: no wholesale re-indentation (the classifier reports 0 reindent blocks), and the body's line-level differences are the enumerated loci of sections 4, 5, and 10. The one visible formatting change inside the block is the final closing brace standing on its own line (candidate L1833) where the original glues it to the sourceMappingURL comment (original L1814) — adjudicated with the tail note in section 10. Body-prose line churn is the translation mass of the class summary.
- **Why:** R7 (formatting disclosed as its own class).
- **Verify:** Diff blocks B22–B77 in diff.md: the stylesheet's blocks are the font loads and the sidebar encodings, not reformatting.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three annotations. (a) The FIX5 translator's note at candidate L204 (the 訳注 appended by FIX5-TEXTB §4): a correct record of item 75's fix. (b) The delivery comment in the head frame (candidate L2 region, ANNOTATION spans in B1/B21). (c) **FLAG — the tail port note (candidate L1830–1832)** claims, in a `/* JP port note */` comment inside the code block, that the original file has one unclosed rule and that a closing brace was appended in the port. The bytes refute it: brace counts run on 2026-11-17, raw and comment/string-stripped, give both code blocks 225 `{` and 225 `}`, final depth 0, no negative excursion on either side. The candidate's final `}` is the original's final `}` (original L1814, glued to the sourceMappingURL comment) moved onto its own line; the net brace change of the port is zero, and the actual tail changes are the dropped sourceMappingURL comment and the two added `/* page module css */` comments (a string with 0 occurrences in the original). The annotation therefore misdescribes the delivered change — under the campaign's record doctrine, a note stating the opposite of the delivered files is a documentation defect in the candidate, of the same family as a prose claim contradicting delivered bytes. The note also sits inside the delivered CSS, so every page using the theme ships the false claim.
- **Why:** R2 (porter additions are listed and must be true of the files they ride in); the record-accuracy doctrine (a record that contradicts the delivered bytes is itself a defect).
- **Verify:** Count braces in both code blocks with any brace counter (raw counts suffice: 225/225 each side); read candidate L1828–1833 against original L1812–1815.
- **Disposition:** Annotations (a) and (b) standing; (c) is a flag (per-theme record), not a disposition.

### 11. Dispositions and exceptions

- **What:** (1) T1's six errors are all pseudo-ref, the draft-host class (iii): the candidate's local--code URLs on sigma10-jp-test.wdfiles.com (candidate L3, L7), sanctioned at draft stage and rewritten at posting (T1-ROWS row 217). (2) Render-row dispositions: the page's 4.15px@768 overflow is the static credit replica family (KB-33); the theme self-delivery finding is the frame form (KB-44b, section 3); the mobile logo clip is the mobile-crop family (KB-42/KB-41); the webm video frame is KB-54; the sample's credit-modal is the preview form (KB-32, ruling 5). (3) The stamp's STALE is fully explained by the b5cb724 usage sweep (per-theme record). (4) Four items are **flags, not dispositions**: the credit pointer (section 1), the duplicated font import (section 4), the tail port note (section 10), and the bedrock link (section 7). No ledger row dispositions any of them, and this package does not invent dispositions for them.
- **Why:** A disposition is a decision with grounds; items without grounds are carried as flags so the coordinator can decide them with the evidence attached.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (items 1–3); flags open (item 4).

### 12. Verification

- **What:** (a) T1 checker baseline: exit 1, 6 errors / 0 warns / 0 infos, all pseudo-ref (stamp; T1-ROWS row 217). (b) T2/T3: FINDINGS on page and sample, every finding dispositioned in ledger §(c2) (RENDER-C row 217). (c) T4 follow-up: LOCALIZE-ROWS row 222 records display-affecting findings 1 — item 75's charge — closed by FIX5. (d) FIX5 re-derivation: per-theme record below. (e) This package: `python3 review/build_review.py --check` — this package is not in the stale set (the stale set is byte-identical with and without this batch's three packages; set comparison in the batch report). (f) Brace depth: both code blocks balanced, 225/225, final depth 0, no negative excursion (section 10).
- **Why:** Verification claims name the cheapest deciding check and its result.
- **Verify:** Re-run the checker on `pages/theme:sci-fi-jp.txt`; re-run `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### Ledger item 75 [H] — the dead hub link, re-derived

The ledger charge (§(e) item 75, from LOCALIZE-S2-E): the intro prose's sci-fi-hub link is dead on SCP-JP (charged under P11; display-affecting). The supplement (row 75) re-judges it FIXED by FIX5-TEXTB §4, commit 3f328d8: "sci-fi-hub probed 404 with no JP counterpart; link converted to plain text with a translator's note". The bytes confirm it: at candidate L204 the sentence now names the event in plain text （科幻月 → SF月イベント as plain words) and carries the appended 訳注 recording that scp-jp has no sci-fi-hub page and the link was removed for that reason; the string "sci-fi-hub" survives only inside that note's explanation. The same line's second hub link (scp-anthology-hub) was correctly left as a link — it resolves (HTTP 200, probed 2026-11-17). **FIXED, confirmed from the bytes.**

### The stamp's STALE, explained

The verdict-era file is 435a6bb-era content; the file changed twice after it: 3f328d8 (the item 75 fix above) and b5cb724 (the usage-example sweep), whose whole change to this file is two lines — the install examples at candidate L58 and L219 gaining the -jp posting name (`:scp-jp:theme:sci-fi` → `:scp-jp:theme:sci-fi-jp`, in the inc-css and inc-achi examples). Both changes are recorded wave work, so the STALE stamp is the designed state, not an unjudged edit.

### The sources.tsv supersession note is wrong

This row's sources.tsv note claims the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-sci-fi-from4.txt` (campaign record, gosign2-lanes/lane-oc-gs-localize-s2-E/). The artifact's whole content records "scp-wiki-cn:theme:sci-fi rev4 → rev4 変更： なし" — no changes. The claim is therefore wrong in the ambrose shape (a supersession note whose own cited artifact refutes it). Correct form, for the coordinator's harvest correction: "Upstream latest remains rev 4; the S2 artifact records rev4 to rev4, no changes; follow-up diff artifact diff-sci-fi-from4.txt in the campaign record (K5a-i)". sources.tsv is not edited in this package.

### Flags (coordinator's queue)

1. **Credit pointer in two carriers** (section 1): credit block 著作権者 (candidate L16) and license-box author (candidate L1837) both defer to "the author of scp-wiki-cn theme:sci-fi" without naming hoah2333, whom the original names (original L57) and the candidate's own prose names (candidate L54). Repair shape, for the coordinator: name [[*user hoah2333]] in both fields, as the credit waves did elsewhere.
2. **Duplicated font import** (section 4): Font Awesome 4.7.0 from cdnjs at candidate L241 and L248; the original loads it once. Repair: delete one copy.
3. **Tail port note refuted by the bytes** (section 10): candidate L1830–1832 claims an unclosed rule in the original and an appended brace; both blocks count 225/225 balanced. Repair: correct or remove the note.
4. **Bedrock prose link** (section 7): candidate L54 links theme:bedrock (404 on SCP-JP, probed 2026-11-17) while theme:bedrock-jp exists in this repo. Repair shape: repoint to the -jp name, as the FIX5 wave did for the stellar and paradigm-sigma sibling links. The theme:ar link on the same line resolves (200) and needs nothing.

## Change set outside the two diffed files

(1) `pages/theme-decoration-sample-sci-fi-jp.txt` — the decoration sample page used by the render checks. The theme's mechanisms need no component pages: the achi component is documented, not ported (section 2), and the inc-css / inc-achi definitions are in-page templates carried in both files. No base theme exists for this port (K5b-5, standalone compiled body).

## Appendix — heuristic and residue adjudication

79 blocks: 31 specific, 45 heuristic, 3 residue. **Residue B3** (original L11–13 → candidate L21–23) and **residue B5** (original L36–38 → candidate L40–42): the tails of the two URL-encoded sidebar css= includes (the template copy and the live copy). Decoding either candidate copy shows the P7 stack swap inside the encoding: `--UI-font` names `'Jost','Noto Sans JP'` where the original's encoding names `'Noto Sans SC'`; the residue is the encoding's tail bytes, unlabeled because the signature table does not decode URL-encoded parameters. **Residue B78** (the code block's tail): adjudicated in section 10 — the brace stands on its own line, the sourceMappingURL comment is dropped, and the port note rides here. **Heuristic mass:** COMMENT-TEXT (57 spans) is the compiled body's carried comments (section 6); TRANS-UNANCHORED (49) and TRANSLATION-ANCHORED (21) are the body translation pairs; GLYPH-FORM (7 spans, in the CSS body blocks) fires on the compiled body's retained simplified-Chinese strings, adjudicated in section 5 as identity forms under ruling 2 / KB-57, not unlocalized residue — the theme's Japanese-facing prose is fully translated, and the strings the signature catches sit inside the author's compiled artifact. The one CSS-BODY heuristic block (B22) carries the font loads of section 4 (its FONT-IMPORT and JPFONT-LOAD spans are specific labels inside it). The LICENSE-BOX span (B79) is the T4 supplement of section 1: the original has no license box; the candidate's box (candidate L1836–1841) is the campaign's standard supplement, with the author-parameter flag recorded against it.
