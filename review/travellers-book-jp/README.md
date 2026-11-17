# Review package — theme:travellers-book-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:travellers-book-jp — origin CN, population #240 [GOSIGN2-LEDGER (b) row 240]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ac71b69e4dddd42fb1ba31a7be11668644a5ba7fc743a8612f1ef0f55bbbbd44); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 2 warns / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 205; GOSIGN2-LEDGER (b) row 240]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 323px@320 + 960px@768; T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN16)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN16)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 239, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 239]
- FIX5 re-judgement: item 96 (class H) FIXED — FIX5-TEXTB §2, commit 3f328d8: dead wanderers:travellers-book-hub link (probe HTTP 404) converted to plain text with a translator's note; warning cleared [GOSIGN2-LEDGER-SUPPLEMENT (a) item 96]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:travellers-book-jp.txt sha256:ac71b69e4dddd42fb1ba31a7be11668644a5ba7fc743a8612f1ef0f55bbbbd44; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 96 [H] (dead prose link to wanderers:travellers-book-hub) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 96: **FIXED** (FIX5-TEXTB §2, commit 3f328d8); re-derived from this package's bytes in the per-theme record below |
| Stamp state | The generated stamp above reads STALE by design: the candidate changed after the 435a6bb-era verdict, in exactly one line (the usage-example sweep completed the install example's name to the -jp posting name, canonical commit b5cb724). No re-judgement is fabricated; the frozen ledger remains the verdict record for the bytes it judged |
| Open flags from this package | Two, neither charged or dispositioned in any campaign record: the credit pointer in both attribution carriers (section 1), and the load-only JP font supplement (section 4). Both are argued in the per-theme record; the package is written against the candidate as it stands |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:travellers-book | theme:travellers-book-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 14 | — |
| Source of this copy | Campaign mirror store `review-mirrors/orig-travellers-book-rev14.txt`, a byte copy (class COPY in the mirror INDEX) of the S2 lane cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-travellers-book.txt`, fetched once 2026-11-16 | Canonical file `pages/theme:travellers-book-jp.txt` at worktree HEAD c6454ab; the file's last content changes are b5cb724 (usage-example sweep) over 3f328d8 (FIX5-TEXTB) |
| Lines / bytes | 358 lines / 9,334 bytes (the final line carries no trailing newline, so `wc -l` reports 357) | 396 lines / 12,165 bytes |
| SHA-256 | 4e18db3fd03791e1caa0884f8134ad709dc0c2e694028a8a0f7a7e67d90a8f65 (equals the review/sources.tsv mirror hash) | ac71b69e4dddd42fb1ba31a7be11668644a5ba7fc743a8612f1ef0f55bbbbd44 |

Provenance route: derived from the branch original at the reference revision. One element was adopted from a production counterpart (the T7 credit-module supplement, from the production Wanderers theme; section 1), which is a supplement adoption, not a body adoption (R4 does not apply to the body: the topology pass finds no relocation and the body diffs against the CN original throughout). One correction is owed to this theme's review/sources.tsv note, which claims the original was "superseded upstream since the reference revision": the cited follow-up artifact (`diff-travellers-book-from14.txt`, campaign record) records the opposite, `theme:travellers-book rev14 → rev14 変更: なし` (re-checked at the current revision, no changes, empty intervening-revision table). Revision 14 is both the reference and the current revision. The correct standard form for the note is recorded in the lane report (BATCH-RFIX17.md) for the coordinator's harvest correction; this package's original.txt is unaffected (its hash equals the sources.tsv value).

## Summary

A small, self-contained port (diff.md: +90/−57, 147 changed lines in 31 classifier blocks). The original is a Wanderers' Library Sigma-9 variant whose single code block is both its source exhibit and its delivered stylesheet, importing the CN Sigma-9 base from a jsdelivr mirror. The candidate keeps that topology exactly (no relocation: the topology pass matches both sides component for component), repoints the self-delivery to its own draft-host code block, drops the CN Sigma-9 import with the ground stated in an in-file annotation (the JP environment's site theme provides that layer), translates the body, and adds the standard apparatus: preview credit block, interwiki-style frame, JP license box, and a palette-adapted credit-module rule adopted from the production Wanderers theme. The theme's one blocking item, a dead link to the CN hub page, was converted to plain text with a translator's note by FIX5 and is re-derived below. Two defects no campaign record charges are flagged by this package: both attribution carriers carry a pointer where the author belongs (the original names W Asriel in its code banner), and the JP font loads the port added are named by no font stack in the file, whose only stacks name the original's CN system faces.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with its delivery module (original L1–3: a `[[module CSS]]` importing its own code block from the CN wiki's file host), then the exhibit gate `[[iftags +版式]]`. The candidate opens with the same module repointed to its own draft-host code block (candidate L1–3), adds the interwiki-style frame (candidate L5–9), and opens its gate `[[iftags +テーマ]]` at L10. Provenance route: this package's original is the mirror-store copy of the S2 lane cache at revision 14 (see Provenance); no live re-fetch was made for this package.
- **Why:** The header is the delivery declaration; its repoint is P4, the gate tag localization is P2.
- **Verify:** Read original L1–5 against candidate L1–10.
- **Disposition:** Recorded; part of the delivery change argued under section 3.

### 1. Credit and attribution

- **What:** The original's credit apparatus is the CN credit include pair (`:scp-wiki-cn:credit:start`/`end`, original L14–16) holding only the placeholder text 页面信息, plus the code banner naming the maker (original L69: "Made by [[*user W Asriel]] for the Traveller's Book", carried byte-identically at candidate L88). The candidate replaces the include pair with the preview credit block (`:scp-jp:credit:start-preview`, candidate L11–20) with the eight standard fields, and adds a JP license box at the tail (candidate L389–394, T4 supplement; the original has no box). Two of the added fields are defective in the same way: the credit block's 著作権者 field (candidate L16) reads "原語版ページの作成者に同じ（scp-wiki-cn の theme:travellers-book）" (same as the original page's creator), and the license box's author parameter (candidate L390) reads "scp-wiki-cn theme:travellers-book の作者" (the author of scp-wiki-cn theme:travellers-book). Both are pointers naming nobody, while the original names W Asriel. The title field correctly uses the body's own Japanese form (旅行者の書 テーマ); the 原題 field correctly quotes the CN title. The original's labelled bare Rate (original L6–9: the labels 评分 / 评分模块与著作信息模块 in `[[>]]` blocks around a `[[module Rate]]`) loses its module in the candidate; the labels stand as plain exhibit text (candidate L24–26), and the preview credit block is rate-bearing, so the widget renders once (KB-09; block B2, BARE-RATE-DEL). T7 credit CSS: the candidate carries one credit-module rule at the code block's tail (candidate L375–385: `.rate-box-with-credit-button .creditButton` background and border in the theme's forest green #228B22), under a comment stating it was carried from the production counterpart `pages-existing/existing:theme-wanderers.txt` line 153 with production's green #006c00 adapted to this theme's palette. This is the FIX4-CREDIT supplement (commit 9fbcd94): ledger §(c4) names this theme in the KB-11 confirmed hit set and records CREDIT-VERIFY rendering the supplement live with exact computed-style matches. The supplement is a single rule, not the basalt 8-selector canonical set; its comment is the record of why.
- **Why:** P3/T1 for the block swap, T4 for the license box, KB-09 for the Rate removal, KB-11/T7 for the credit rule. The pointer fields fail the campaign's TASL standard (ruling 3): the field must name the author the original names.
- **Verify:** Read candidate L11–20 and L389–394 against original L14–16 and L69; read the T7 comment and rule at candidate L375–385.
- **Disposition:** **DEFECT FLAG (open)** — the credit pointer in both carriers (candidate L16 and L390), where the original names W Asriel. No ledger item charges it (the theme's only item is 96); flagged here and in the lane report for a repair lane. The remainder of this section's classes (preview swap, license-box presence, bare-Rate removal, the T7 supplement) are in their settled forms.

### 2. Includes and components

- **What:** Original includes: the credit pair (section 1) and `component:image-block` (the header-image exhibit, original L23). Candidate includes: the interwiki-style frame (L5–9), the credit pair (L11/L20), `:scp-jp:component:image-block` (L31, repointed to the JP component with its image re-hosted to the candidate's own attachment, caption translated), the install example (L29, an exhibit line naming the candidate's own posting name), and the license-box pair (L389/L394). No include in the candidate points at a CN-wiki page, and no include is duplicated.
- **Why:** P1 repoints and the T8 component swap to the JP form of the shared component.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` (4 / 7 lines).
- **Disposition:** Standing as recorded; no foreign include stands in the candidate.

### 3. Delivery and code loading

- **What:** Both sides deliver identically in shape: one `[[code type="css"]]` block (original L61–357; candidate L71–386) that is both the displayed source exhibit and the delivered stylesheet, imported by the head module from the page's own local--code /1 (original: the CN wiki's file host; candidate: the draft host). The candidate adds the interwiki-style frame at priority=1 naming the same /1 (candidate L5–9). Self-delivery census: exactly one code block in any form on each side, so /1 names the stylesheet itself; the address was never in the population audit's mismatch set. One delivery change of substance: the original's code block opens by importing the CN Sigma-9 base (`sigma9_ch_wl.min.css` from cdn.jsdelivr.net/gh/scp-cn-tech/sigma9, original L63); the candidate does not carry that import. The ground is stated in the candidate's own header comment (candidate L75–80): in the SCP-JP environment the Sigma-9 site-theme layer is provided by the site theme, so this file does not include it. The render record corroborates the outcome (the pages render styled; the only delivery finding is the site-theme chain's own hotlink class, section 11). Draft-host URLs are the draft-form class (iii).
- **Why:** P4/T9 for the self-delivery repoint; the base-layer decision is the porter's, recorded in the file. A base the original imports may only be dropped with a stated ground and a delivery chain that still covers it; here the covering layer is the environment's site theme, which is the same layer the render checks measured.
- **Verify:** Read candidate L1–9 and L71–80 against original L1–3 and L61–65; census the code blocks (`grep -n '\[\[code'`, one hit per side).
- **Disposition:** Standing as recorded (the two draft-host delivery lines stand as the checker's pseudo-ref lines, class (iii)).

### 4. Fonts and assets

- **What:** The candidate's code block adds two JP font loads at its head (candidate L72–73: Noto Sans JP, in the file's v1 `css?family=` grammar, and Noto Serif JP). No font stack in the candidate names either face: a census of `font-family` in the delivered CSS finds exactly two declarations, `#header` naming '宋体' (SimSun; candidate L203) and the header-title pseudo-element naming '等线' (DengXian; candidate L235), both with `!important` and both inherited byte-identically from the original (original L184, L216). The loads therefore change nothing in this file's own rendering: they are a load-only supplement, the mirror image of the KB-16 gap (a named face with no load). Assets: the header image (tree.png) is re-hosted from the CN wiki's file host to the candidate's own draft-host attachment (candidate L31 and the CSS at L214; class (ii) posting form); the body's image-credit lines (Pixabay and Pixite attributions, candidate L32–38) are carried and translated, and the license box's source note defers to them.
- **Why:** P7/T5 is the class the loads belong to, and its settled form is a load **plus** stacks that name the loaded face (the population's repairs align the winning stacks to the JP faces, as in the shancheng and walk-in-the-dark fixes). A load no stack names is either inert weight in this file or a load serving another layer's stacks; the package's bytes cannot decide which, because the covering site-theme layer's stacks are outside these two files.
- **Verify:** `grep -n 'Noto' candidate.txt` (only the two import lines); `grep -n 'font-family' candidate.txt` (the two CN-face declarations).
- **Disposition:** **DEFECT FLAG (open)** — the load-only JP font supplement (candidate L72–73 against L203/L235), flagged for the coordinator's adjudication with the evidence stated: if the loads are meant for this file, its stacks must name the JP faces; if they serve the site-theme layer, that ground belongs in the file's annotation next to the Sigma-9 note. No ledger item charges or dispositions it. The asset re-hosting is DISPOSITIONED (class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The theme sets no --header-title/--header-subtitle variables in either file (census: no hits on either side); its header treatment is the `#header h1 a::before` rule whose `content:` string is the theme's CN title "旅行者之书", byte-identical on both sides (original L217, candidate L236). The credit block's title field uses the Japanese form (旅行者の書 テーマ, candidate L12) while the CSS content string keeps the CN form.
- **Why:** The content string is the theme's title treatment, an identity string under the main chat's boundary (names and marks stay; prose sentences translate), and it stands under ruling 2 (header/title language out of scope for migration correctness; KB-57), the same ground as the sibling themes' retained header strings. It is recorded here rather than passed over, because a reviewer comparing glyph forms will spot the simplified 书 against the body's 書.
- **Verify:** `grep -n '旅行者之书' original.txt candidate.txt` (the CSS string at original L217 / candidate L236, plus the credit block's quotation fields).
- **Disposition:** DISPOSITIONED (ruling 2 / KB-57).

### 6. Text translation

- **What:** The body is translated throughout (original L18–59 → candidate L21–66): the introduction, the image-credit lines, the heading samples (kept bilingual, 第2見出し / H2 and siblings), and the three tabview worlds. The heuristic classifier blocks are this mass at line granularity: B14, B16, B17 are single CJK prose lines the script-delta heuristic could not anchor, and B19 is the code block's head region (the porter annotation and the carried banner). In-CSS text (R1): the code banner ("BASED ON FLANNEL NATURE CSS THEME / BASED ON SCP SIGMA-9 CSS THEME / Made by W Asriel") is carried byte-identically, as a quotation of the original's attribution; the CSS comments are the original's own. Four TRANSLATION-ANCHORED and fourteen TRANS-UNANCHORED blocks are the translation mass, resolved by shape in the appendix.
- **Why:** P10 for the body; KB-18 for reader-visible strings. Carried attribution banners are quotations, not untranslated residue.
- **Verify:** Read candidate L21–66 against original L18–59 section by section.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The introduction's base-theme link names `theme:wanderers` in both files (original L19, candidate L26): that page exists on SCP-JP (the FIX5 lane probed it live and left it untouched), so the un-suffixed name is correct here. The neighbouring hub link is this theme's FIX5 item: the original names `wanderers:travellers-book-hub` (original L19), a CN hub page with no JP counterpart; the candidate carries the hub's name as plain text with a translator's note stating the conversion and its ground (candidate L26). The image-credit links (Pixabay, Pixite) stand unchanged as external attributions; one of them is an http:// link, standing as a prose/license link of the T12 residue class. The credit block's source link points back to the CN original.
- **Why:** P11 for the hub link: a dead target fails at click time, and where no JP counterpart exists the settled remedy is plain text with the name preserved in a note, not a repoint to a nonexistent page.
- **Verify:** Read candidate L26 against original L19; the item 96 re-derivation is in the per-theme record.
- **Disposition:** FIXED (item 96); the http:// credit link is DISPOSITIONED (class (ii), T12 prose class).

### 8. Structure

- **What:** No structural change beyond the apparatus additions. The topology pass finds no relocation (both sides: one head module, one code block), the CSS body is carried with its selectors and order intact, and brace depth measured over both whole files ends at 0 with no negative excursion on either side. The one label that suggests otherwise, EXHIBIT-RESTRUCTURE on B7, is the image-block exhibit line: the exhibit stands in place with its include repointed and its image re-hosted, a false-fire of the label on a repoint inside an exhibit line, adjudicated here against the exhibit census (the header-image exhibit, the heading samples, and the tabview all stand against their originals).
- **Why:** The localize.md closing rule (structure, variable names, selectors, and channel order preserved) is this port's stated discipline, and the bytes bear it out.
- **Verify:** Compare the structural maps: `grep -n` for `[[module`, `[[code`, `[[tabview` in both files.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** Six whitespace-only blocks inside the CSS body (B22, B24, B25, B27, B28, B29), single blank-line or trailing-space adjustments at rule boundaries; 0 re-indentation blocks. Nothing else in the diff is formatting-only.
- **Why:** Formatting-only churn is disclosed as its own class so a reviewer can skip it; at this size it carries no follow-up-diff hazard (the R7 rule is not triggered).
- **Verify:** The WS-ONLY labels in classification.json, with their ranges.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two porter annotations stand in the candidate: the translator's note in the introduction recording the hub link's conversion (candidate L26, written by the FIX5 lane as part of item 96's fix), and the header comment of the code block (candidate L75–80), which states that the original's CN Sigma-9 delivery is not carried because the JP environment's site theme provides that layer, and that the images were replaced with the candidate page's own attachments. A third comment, at the T7 rule (candidate L375–378), records that supplement's production provenance and palette adaptation; it is counted with section 1's class. The code banner naming W Asriel is the original's own, not an annotation (section 6).
- **Why:** R2 (porter annotation additions): the annotations are part of the change record, and the code block's header comment is load-bearing — it is the only in-file statement of the base-layer decision in section 3.
- **Verify:** Read candidate L26, L75–80, and L375–378.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme: (1) the render-row dispositions (ledger §(c2), RENDER-ROWS-G (CN16)): the runtime-hotlink site-theme chain (environment layer, KB-40 — the hosts arrive via the shared site theme, not this candidate), the credit-modal preview form (ruling 5; KB-32), and the page-overflow figures (323px@320, 960px@768) in the recorded cross-cutting families (KB-33/KB-34), plus the chromium-only coverage statement; (2) the T1 standing classes (register c1): 6 pseudo-ref errors, the draft-host delivery form (class (iii)); (3) the retained CN title content string under ruling 2 (section 5); (4) the http:// Pixabay credit link, T12 prose class (section 7). Not dispositions, and not hidden by this list: the two open defect flags (sections 1 and 4), which no record has decided.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above, except the flagged items, which are open).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the campaign checker baseline for this file is 6 errors / 2 warnings / 1 info (all 6 errors pseudo-ref), and the FIX5 lane's control run around item 96's edit reports 6/2/1 before and 6/1/1 after (the dead-hub warning cleared, no new error); (b) the supplement's re-judgment of item 96 is re-derived from this package's own bytes in the per-theme record below; (c) render checks T2/T3 produced dispositions only, no open finding (ledger §(c2)); the T7 supplement was separately render-verified by the campaign's CREDIT-VERIFY pass (ledger §(c4)); (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib): +90/−57 across 8 hunks. The classifier's adjudication: 22 specific blocks, 9 heuristic, 0 residue; the heuristic blocks are resolved by shape in the appendix.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:travellers-book-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement), with the two open flags recorded above.

## Per-theme record

### The FIX5 closure (ledger item 96), re-derived

At ledger time this candidate carried one blocking defect: its introduction linked to `wanderers:travellers-book-hub` (ledger §(e) item 96 [H], charged under P11 and in the LOCALIZE-S2-E lane's cross-cutting dead-target list), a hub page that does not exist on SCP-JP. FIX5-TEXTB §2 (commit 3f328d8) records the fix: the dead link was converted to plain text, the hub's name and site preserved in a translator's note, on probe evidence (the hub returns HTTP 404; no JP counterpart exists in the repo or the population), while the neighbouring `theme:wanderers` link was probed live and deliberately left untouched; the checker went from 6/2/1 to 6/1/1 as the link-target-missing warning cleared. Re-derived from this package's bytes: the original's intro carries both links on one line (original L19); the candidate's intro (candidate L26) names `theme:wanderers` as a link and 「旅行者の書」 as plain text with the 訳注 stating the conversion and its ground. The closure holds exactly as the supplement states it.

### Flag A — the credit pointer, in both carriers

Argued in section 1. The original names its author in its code banner (original L69: W Asriel), and the candidate carries that banner byte-identically (candidate L88), so the name was in the porter's hands. Both attribution carriers the port added decline to use it: the credit block's 著作権者 field (candidate L16) defers to "the original page's creator", and the license box's author parameter (candidate L390) defers to "the author of scp-wiki-cn theme:travellers-book". This is the credit-pointer defect family (ruling 3's TASL standard: the field names the author the original names), flagged, not edited, by this package.

### Flag B — the load-only JP font supplement

Argued in section 4. The port added two JP font loads (candidate L72–73) and no stack to name them; the file's only font-family declarations name the CN system faces '宋体' and '等线' with `!important` (candidate L203, L235), inherited byte-identically. In the population's settled P7 form, a JP load arrives with stacks that name the loaded face as the CJK fallback; where a candidate's winning stacks kept the source faces while its loads stood unused, the review pass has treated the misalignment as the defect (the shancheng shape). The counter-consideration, stated for the coordinator's adjudication rather than decided here: this file's own annotation says the Sigma-9 layer comes from the site theme, and a load in this file would serve that layer's stacks too if they name the JP faces; those stacks are outside this package's two files, so the package records the state and the deciding check (read the JP Sigma-10 site theme's font stacks for a Noto Sans JP / Noto Serif JP name) rather than a verdict. Flagged, not edited, by this package.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-travellers-book-jp.txt` — the decoration sample page used by the render checks. (2) The T7 supplement's source, `pages-existing/existing:theme-wanderers.txt` (the production counterpart of the base theme), is not part of the change set but is part of the record: the supplement was adopted from it, as its comment states. (3) The delivery itself: the local--code code block served from the draft host (theme /1), which is the runtime form of the candidate's code block.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave (LOCALIZE-S2-E) produced the initial port (translation, delivery repoint, the Sigma-9 base decision, the pointer credit fields and the load-only font supplement this package flags); FIX-CREDIT-D (commit 1869877) normalized translator attribution across the population; FIX4-CREDIT (commit 9fbcd94) restored the credit-module supplement (KB-11 family); FIX5-TEXTB (commit 3f328d8) resolved item 96's dead hub link; and the usage-example sweep (commit b5cb724) completed the install example's posting name. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2) (render row), §(c3) (localize row), §(c4) (KB-11 set), §(e) item 96; GOSIGN2-LEDGER-SUPPLEMENT.md item 96; REPORT-GOSIGN2-FIX5-TEXTB.md §2. The go-sign re-run over that record is what the Status block certifies.

## Appendix — classifier heuristic blocks, adjudicated by shape

There are no residue blocks in this package. The 9 heuristic blocks resolve as follows:

- **B14, B16, B17 (single lines, body):** one-line CJK prose translations the script-delta heuristic could not anchor (the heading-sample and tabview boundary lines). They are P10 translation, assigned to section 6.
- **B19 (original L62–63 → candidate L74–82, code-css):** the code block's head: the porter annotation (COMMENT-TEXT fired inside it) plus the carried attribution banner. Assigned to sections 6 and 10.
- **B4, B5, B6, B9, B12 (TRANS-UNANCHORED primaries):** unanchored body translation lines (the introduction's continuation, the credit lines, the heading samples). P10 mass, assigned to section 6.
- **EXHIBIT-RESTRUCTURE on B7:** the image-block exhibit line; adjudicated in section 8 as a false-fire on an include repoint inside an exhibit line — the exhibit stands.
- **Skeleton "none" sections:** the skeleton's per-section listing follows primary labels only; the sections above are written from classification.json's label_spans (JPFONT-LOAD fires inside B18, T7-CREDIT-CSS inside B30, LICENSE-BOX inside B31, COMMENT-TEXT inside B19), per the settled format.
