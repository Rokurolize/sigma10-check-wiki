# Review package — theme:ambrose-chapter-two-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ambrose-chapter-two-jp — origin EN, population #55 [GOSIGN2-LEDGER (b) row 55]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9375d8f246703545263d99e8ef59bf543610d4a04a46e86e3346cbe7cfe060ac); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 1 info (hotlink×2); standing classes dispositioned in register c1 [T1-ROWS row 55; GOSIGN2-LEDGER (b) row 55]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate-inherent 328px@320 page overflow (8px) + 320 header clip (wordmark/account links clipped, 検索 overlaps); 503/http.cat transient capture, not a defect. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 55, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 55]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 55]
- Computed against: canonical commit 5d951775998e4a1eeccf8e8695a6518b328962ee; candidate file pages/theme:ambrose-chapter-two-jp.txt sha256:9375d8f246703545263d99e8ef59bf543610d4a04a46e86e3346cbe7cfe060ac; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/ambrose-chapter-two-jp/candidate.txt (sha256 2de80325edb68114d2d947572c2ae48f697057e7c921788c92e1f50739dcd855)
Original: theme:ambrose-chapter-two — scp-wiki, revision 19 (sha256 216d3928ca5cdd1133a3be84c0561746026d955d6220748fc6859b96384b7276)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 55); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme, the supplement carries no ambrose entries, and no FIX5 re-judgement was needed |
| Fixed after the localize check | P6 (interwiki-style frame) and P7 (Japanese font supplement), both landed in commit 1869877 (FIX-CREDIT-D) together with the translator-attribution normalization |
| Standing items | **DISPOSITIONED** — T1 hotlink×2, class (ii) (ledger (c1)); render findings: 328px@320 page overflow (8px) and the 320 header clip, narrow-width family (ledger (c2)); the 503/http.cat transient capture (KB-44); localize P5 class (ii) / KB-58 and P9 ruling 2 (ledger (c3)) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ambrose-chapter-two | theme:ambrose-chapter-two-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 19 (created 2026-04-25 12:53:23 UTC per the fetching lane's record), as recorded in the candidate's credit block: **初訳時参照リビジョン:** 19 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-ambrose-chapter-two.txt` (fetched once by the LOCALIZE-S2-A lane), via the campaign mirror store (class COPY, byte-identical) | Canonical file `pages/theme:ambrose-chapter-two-jp.txt`, created in commit 3205f27 (Stage 2 EN batch 1); its last content change is commit 1869877 (FIX-CREDIT-D) |
| Lines / bytes | 546 lines / 10,519 bytes (the last line carries no trailing newline, so `wc -l` reports 545) | 508 lines / 9,408 bytes |
| SHA-256 | 216d3928ca5cdd1133a3be84c0561746026d955d6220748fc6859b96384b7276 | 2de80325edb68114d2d947572c2ae48f697057e7c921788c92e1f50739dcd855 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart was adopted: the candidate's CSS body measures 0.984-similar to the original's own stylesheet (classifier topology pass), not to any pages-existing file. Reference-revision currency: revision 19 is still the upstream latest (the lane's follow-up check; the artifact `diff-ambrose-chapter-two-from19.txt` in the campaign record records rev19 → rev19, no changes). One wrinkle in the copy route, the blank-line padding the candidate's CSS body carries, is byte-traced in section 9.

## Summary

The original is a self-delivering shell around a code exhibit: its whole stylesheet sits in a `[[code type="css"]]` block, served as the page's own local--code /1 and loaded twice (a module-CSS @import and the interwiki-style theme= URL), next to a bare Rate module and a full sample body, with no credit block anywhere. The candidate inlines the same stylesheet into `[[module CSS]]`, drops the sample body and the bare Rate, and adds the preview credit block with the eight attribution fields; its one later commit adds the JP interwiki frame and the Japanese font supplement. The measured churn is smaller than it looks (diff.md: +103/−140 in 16 hunks; the classifier counts 74 change blocks, of which 60 are blank-line whitespace inside the moved CSS and only 14 carry content). The two EN asset URLs survive byte-identical and are the standing T1 hotlink pair, dispositioned class (ii). The theme passed at the ledger determination with no open items; the one genuine oddity a reviewer will spot, the subtitle-removal snippet stranded without its explanation at the tail of the CSS, is recorded in the Per-theme record rather than hidden.

## Classification

| Label | Blocks |
|---|---|
| WS-ONLY | 60 |
| DELIVERY-MOVE | 7 |
| TRANS-UNANCHORED | 4 |
| JPFONT-STACK | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| HEADERVAR | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| RESTORATION | 1 |
| TASL-FIELDS | 1 |

Counts: 74 blocks — 71 specific (95.9%), 2 heuristic (2.7%), 1 residue (1.4%), 0 skipped. Topology: the original's code-css body (orig L71–544) moved to the candidate's module-css (cand L25–506) at 0.984 similarity; the candidate-side own-delivery companion body was unavailable to the classifier (its recorded caveat). Labels are sets per block; the per-section lists in the classifier's skeleton show each block once, under its primary label, so this README's sections were written from classification.json's label spans, not from the skeleton's section lists (the skeleton's sections 4, 5 and 7 print "none" although font, header-variable and link-bearing labels fired inside blocks whose primaries sit elsewhere).

## Standing sections

### 0. Header and provenance frame

- **What:** The original's header (L1–13) declares its delivery and gating: a `[[module CSS]]` @import of the page's own local--code /1 (L1–3), the `[[iftags +theme]]` gate wrapping a bare `[[module Rate]]` (L5–8), and the EN interwiki-style include (L10–13, theme= the same /1, its URL carrying a stray trailing semicolon). The candidate's header (L1–17) is the JP frame: the `:scp-jp:` interwiki-style include first (L1–4), the localized gate (L6), then the credit block (L8–17). The differ groups the original header's removal into block B1 (orig L1–10 → cand L1) with the include repoint, the gate and the Rate deletion as labeled spans inside it; the candidate's gate and credit block are insertions B3 and B4. Provenance route: derived from the original at reference revision 19 (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery; P1/P2/P3/P6 rework exactly this frame for the JP environment, and each piece of it is accounted for in sections 1–3.
- **Verify:** Read original L1–13 against candidate L1–17; blocks B1–B4 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original has no credit block, no info module and no license box anywhere (grep finds none); its attribution lives in the CSS comment header (orig L73–87) and its only rating device is the bare `[[module Rate]]` (orig L7). The candidate adds the preview credit block (cand L8–17, block B4): `:scp-jp:credit:start-preview` / `end-preview` carrying all eight ruling-3 fields (cand L9–16) — title アンブローズ第二章テーマ, translator AI, translation year 2026, original title "Ambrose Chapter Two", copyright holder Proasek, creation year 2026, reference revision 19, and the source link to the EN page. The bare Rate is deleted in the same header rework (B1, span orig L7; label BARE-RATE-DEL). The comment-header credits (Proasek; Golden Feast by c_bonefish; header code from thd-glasses; info-bar/rating code from EstrellaYoshte; the two pixabay ornament credits; CC BY-SA 3.0) are carried verbatim inside the moved CSS (cand L28–42). The theme's own credit-module CSS (`.creditRate`, `.rate-box-with-credit-button` and the `.fa-info` rules, orig L382–399) is likewise carried verbatim (cand L337–354): supplement type T7 by inheritance from the original, not by addition, in the theme's own gold (#8A7500) that its rate-widget rules already use. No license box exists on either side, and none was charged (KB-63 covers dropped boxes; this original never had one to drop).
- **Why:** P3/T1: the preview credit module is the JP environment's credit form and it is rate-bearing, so a separate bare Rate beside it would duplicate the rating widget (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 (RULINGS-20261116, in review/AUTHORITIES/) fixes the eight fields and credits campaign translations to AI. The localize check verified all eight fields present (LOCALIZE-S2-A pattern table, item 3: APPLIED).
- **Verify:** Read candidate L8–17 against the eight-field list; `grep -n 'module Rate' candidate.txt` (absent) against original L7; `grep -n 'license-box' original.txt candidate.txt` (absent in both).
- **Disposition:** Standing (the port's credit form). One record note: the localize lane examined the candidate with the translator field reading `SCP-JP`; the current bytes read `AI`, normalized by FIX-CREDIT-D (commit 1869877) under ruling 3. The lane report describes the earlier state; the git diff decides (see Multi-wave provenance).

### 2. Includes and components

- **What:** The candidate's complete include list (grep): the JP interwiki-style (L1–4), the credit pair (L8/L17), and the escaped usage include in the prose (L21). The original's includes are the EN interwiki-style (L10–13), the escaped usage include `:scp-wiki:theme:ambrose-chapter-two` (L23), and `component:image-block` (L44, displaying the EN top-image.png inside the sample body). Changes: (a) the interwiki-style include is repointed `:scp-wiki:` → `:scp-jp:` and moved to the head of the page (B1/B2); (b) the usage include is rewritten to the same-site JP fullname `theme:ambrose-chapter-two-jp` with no site prefix (cand L21); (c) the image-block include is dropped with the sample body (section 8). No `:scp-wiki:` include remains in the candidate (grep: none). No component swap (T8) was needed and no foreign include is kept, so KB-15/KB-54 do not engage. The base is standalone (**基盤:** 単体, cand L23; the start-themes.tsv base column reads "standalone"), so neither side carries a base-theme include and the bare sigma-plus shape (KB-64) does not occur.
- **Why:** P1: foreign-site includes are repointed to the JP site, and a same-site include takes the bare fullname form (the include forms by context, AGENTS.md §5 as inventoried in the taxonomy). Ruling 4 (port a needed component with the theme) does not engage: the theme's only component dependency was image-block, an exhibit device rather than a delivery dependency, and it left with the exhibit.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; no include in the candidate points at an EN-wiki page.

### 3. Delivery and code loading

- **What:** The original delivers its stylesheet out of its own code exhibit: the page's only `[[code type="css"]]` block (orig L71–544) is served as the page's local--code /1, and the page loads that /1 twice, by the module-CSS @import (orig L2) and by the interwiki-style theme= URL (orig L12). The candidate inlines the same CSS body into `[[module CSS]]` (cand L25–506); the classifier's topology pass measures the move code-css → module-css at 0.984 similarity, and inside the moved body the line offset is a constant −45 (orig L73 ↔ cand L28 through orig L543 ↔ cand L498), which is what the move looks like when nothing inside was restructured. The frame keeps the self-delivery form (labels DELIVERY-HOST + DRAFT-HOST + SELF-DELIVERY on B2): cand L3 names the candidate's own /1 on the draft host (sigma10-jp-test.wdfiles.com), dropping the original URL's stray trailing semicolon. Single lines inside the moved body that the topology pass matched individually (B8, B12, B16, B33, B36) carry the internal edits classified in sections 4 and 9. No cross-theme @import exists on either side (KB-14 does not engage; the Golden Feast lineage is code ancestry recorded in the comment header, not a runtime import). The priority value is unchanged (1 on both sides); with a standalone base there is no BHL layering stack for it to order.
- **Why:** P4/T9: deliveries are served from JP hosts in this environment, and the draft-host form of a candidate's own local--code is the sanctioned draft-stage form (class (iii)), rewritten to scp-jp.wdfiles.com at posting. Inlining removes the candidate's runtime dependence on the EN wiki's code page altogether: the candidate never reads scp-wiki.wdfiles.com/local--code, and the localize lane confirmed no `[[html]]`, `<link>` or `<script>` self-loads exist either (pattern table, item 4).
- **Verify:** Read orig L1–3 and L10–13 against cand L1–4 and L25; the topology entry in classification.json (similarity 0.984, with its caveat that the candidate-side /1 companion body was unavailable to the classifier).
- **Disposition:** The draft-host URL at cand L3 is class (iii) draft form, recorded as not-charged in section 11 (the classifier's own note on B2).

### 4. Fonts and assets

- **What:** Three font changes inside the moved body, all of them the P7 fix: (a) a new @import of Noto Sans JP from Google Fonts (weights 400;700) at cand L27 (label JPFONT-LOAD, inside B9); (b) `"Noto Sans JP"` inserted into the three 'Poiret One' stacks — cand L71 (#header h1 a), L211 (#page-title), L221 (h1–h6) (label JPFONT-STACK, blocks B16/B33/B36; `grep -c 'Noto Sans JP' candidate.txt` = 3, the import carrying the +-encoded family name in its URL); (c) the Poiret One import itself repointed from fonts.bunny.net (orig L89) to fonts.googleapis.com (cand L44) (label FONT-IMPORT, inside B12). Assets: the two decorative image URLs are byte-identical to the original — background.png on scp-wiki.wdfiles.com (orig L101 → cand L56) and top-image.png on scp-wiki.wikidot.com (orig L172 → cand L127), both `local--files` paths of the EN theme page. They are the T1 checker's two hotlink errors (section 12) and the localize P5 finding. The pixabay URLs in the comment header (cand L38–39) are credit text naming the ornament sources, not loaded assets.
- **Why:** P7/T5: Poiret One has no Japanese glyphs, so without a JP font in the stack, Japanese heading text falls back to an OS-dependent generic cursive (the localize lane's pattern 7 finding, display-affecting). P5/KB-17 (patterns 9c5e907): only SCP-JP storage, Google Fonts, BootstrapCDN and cdnjs may be hotlinked; fonts.bunny.net is a mirror outside that list, so the import went to the canonical host (the campaign's FIX4-REPOINT wave made the same repoint across its charged bunny set; this file's repoint was already present in the S2 draft the localize lane examined). The two image URLs are the opposite case: re-hosting them is a posting-procedure act, class (ii), so the candidate keeps the original-state hosts (KB-58 deferred hosting; the campaign's owner order bars re-upload).
- **Verify:** `grep -n 'fonts.bunny.net\|fonts.googleapis.com\|Noto' candidate.txt` (bunny absent; two googleapis imports; three stack insertions); `grep -n 'local--files' candidate.txt` (exactly L56 and L127).
- **Disposition:** Fonts FIXED (ledger (c3): P7 FIXED, font wave; the change itself sits in commit 1869877, see Multi-wave provenance). Assets DISPOSITIONED (ledger (c3): P5, class (ii) / KB-58; ledger (c1): the hotlink class is (ii)).

### 5. Header, sidebar, site furniture

- **What:** The theme's header variables are carried verbatim: the `:root` block (orig L91–96 → cand L46–51) keeps `--title: "Ambrose Restaurants"`, `--short_title: "Ambrose"` and `--header-subtitle: "Chapter 2"`, and the rules consuming them are unchanged (`content: var(--title)` at cand L79; `content: var(--header-subtitle)` at cand L94; the ≤499px short-title swap at cand L403–409). The classification's HEADERVAR labels fire only on the subtitle exhibit's copies of `--header-subtitle` (B8/B74, section 8); the :root block itself matched equal. Sidebar, top-bar, login-status and search-box rules are byte-preserved inside the moved body (orig L181–250 → cand L136–205), and `div.open-menu a` keeps its color rule (cand L253–256). No JP-specific layout adaptation was made.
- **Why:** P9/T6 variables exist to be overridden where the JP environment requires it; here the values are the work's own names (the restaurant's name and its chapter subtitle), and ruling 2 (2026-11-16) places header and title language outside migration correctness (KB-57, patterns 9c5e907). P8 layout adaptation is owed only where the JP furniture's structure differs: the localize lane judged P8 APPLIED on the ground that the JP Sigma-10 layout has the same left-sidebar structure and the copied offsets do not contradict it, while recording that it did not itself verify the mobile menu-button position on a device; the T2/T3 render rows are the coverage that exists at narrow widths (section 11).
- **Verify:** Read orig L91–96 against cand L46–51; `grep -n 'header-subtitle' candidate.txt` (L49 the definition, L94 the consumer, L503 the exhibit copy).
- **Disposition:** DISPOSITIONED (ledger (c3): P9, ruling 2). The untranslated subtitle is a recorded judgment, not residue: the localize T5 pass considered the same strings and recorded the proper-noun reading for --title/--short_title and an author-judgment flag for "Chapter 2", which ruling 2 then settled as out of scope.

### 6. Text translation

- **What:** The candidate's reader-visible prose is three lines (cand L19, L21, L23) against the original's prose block (orig L17–34). B5 (orig L17 → cand L19, heuristic tier) compresses the 60-word attribution sentence (author, Golden Feast derivation, restaurant hub) into one sentence, "Ambrose第二章のためのテーマです。"; the attribution content is not lost, it moved to the credit block (section 1) and survives verbatim in the CSS comment header. B6 (orig L19 → cand L21, heuristic tier) replaces the "intended for use in works relating to the Ambrose Chapter two project…" sentence with the usage line itself; the sentence's second half (the permission to use the theme elsewhere) has no counterpart in the candidate. B7 (the residue block, orig L21–26 → cand L23) is the import-instruction block, resolved in section 8. The localize T5 pass found no untranslated body paragraph and no mistranslation in what remains, and recorded the surviving prose as consistent with the original's summary (part-EN3, T5 finding 4). In-CSS text (residue class R1): the CSS comment header stays in English verbatim (cand L28–42), porter-visible only; the string-valued variables are dealt with in section 5. No glyph-form conversions (R5) occur; this port has no CN text.
- **Why:** P10: body and usage text are translated, with the work's name in its JP form (第二章). The classifier's TRANS-UNANCHORED label on B5/B6 is the honest one: translation by compression has no line anchors, and that is exactly the shape where silent deletions hide, so both blocks are accounted for here rather than waved through.
- **Verify:** Read orig L17–26 against cand L19–23, and the credit block (cand L8–17) for the relocated attribution.
- **Disposition:** Standing (the port itself). The dropped permission half-sentence is recorded above so the compression is fully visible; the T5 pass raised no finding on the body text.

### 7. Links

- **What:** The candidate's only prose links are the credit block's source link (cand L16, to the EN original — the required ruling-3 back-reference) and the usage include (cand L21, a page reference, section 2). The original intro's links (the Golden Feast theme link and the Ambrose Restaurants hub link, orig L17) and the exhibit body's link samples (orig L56, L61) have no counterparts: the intro was compressed (section 6) and the sample body dropped (section 8). No prose link in the candidate targets the EN page except that required source link; the un-suffixed fullname otherwise appears only inside the two asset URLs' encoded paths (section 4).
- **Why:** P11 repoints links to original-site tag pages and hubs to their JP counterparts where the link survives; here the carrying prose was compressed away, so there was nothing to repoint, and the dead-target failure P11 exists to prevent does not arise: the one surviving link's target is this package's own original.
- **Verify:** `grep -n 'ambrose' candidate.txt` and read each hit's role (frame URL, credit link, prose, the two asset paths).
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** Inside the CSS body, the localize.md closing rule is honored: every rule of the original's stylesheet survives in the same order (the 0.984-similarity move at a constant −45 line offset, sections 3 and 9), and the JP corrections sit at the frame and at the body's head (the cand L27 font import), not interleaved. Three structural changes sit outside the CSS body. (a) The sample body is dropped (B9, orig L36–72 → cand L27): the "Page Elements" exhibits (toc, the image-block, heading samples Title1–Title6, body/footnote/link samples, the four-tab tabview) and the collapsible frame that wrapped the code exhibit (orig L70–71) have no candidate counterpart. (b) The import-instruction exhibit is restructured (B7): the `[[div class="code"]]` wrapper, the `@@@@` separator and the instruction prose (orig L21–26) are replaced by the one-line usage form (cand L21) and the base-declaration line `**基盤:** 単体` (cand L23). (c) The subtitle-removal exhibit is relocated, not dropped (B8 + B74): the original presents it in the body as a code exhibit (orig L28–34); the candidate carries the same snippet, still @@-escaped, at the tail of its module CSS (cand L501–505). The differ pairs its original position with the module's opening line (B8) and its re-emergence with the original's closing lines (B74, labeled RESTORATION because the added lines match the original's own earlier region — a diff-only signal, not a fix-wave restoration; nothing for this theme was ever deleted and then restored by a later wave).
- **Why:** Residue class R3: a sanctioned exhibit replacement and a silent deletion have the same diff shape, so the ground for each is stated. Exhibit decisions: (a) dropped — the drop happened in the S2 port and was visible to every later check; the localize pass itemized this theme's defects and did not charge the sample body (ledger class I, which charges exhibit restructuring when it reaches live structure, was not raised — the live structure, the CSS body, is intact), and the theme's element rendering is exercised through the decoration sample page (Change set, item 1). (b) replaced — the instruction's payload, the include line, survives in direct form at cand L21; the wrapper was exhibit furniture. (c) relocated — the snippet survives verbatim; its explanation prose (orig L26) did not, which is the T5 orphan carried to the Per-theme record. The bare Rate deletion inside B1 is decided in section 1 (removed, because the preview credit module is rate-bearing, KB-09).
- **Verify:** `grep -n '\[\[toc\]\]\|image-block\|tabview' candidate.txt` (absent) against original L42–69; read cand L499–506 against orig L28–34.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it), with the T5 orphan carried to the Per-theme record.

### 9. Formatting only

- **What:** 60 of the 74 change blocks are whitespace-only, and every one is the same shape: a blank line in the original's code exhibit that carries whitespace in the candidate's module CSS — 59 become a single space, 1 becomes four spaces (orig L474 → cand L429, inside the #toc rule). Two further padded blank lines ride inside B12 (orig L88/L90, flanking the font import). Content lines are untouched: the classifier counts 0 re-indentation blocks, and no rule's text differs by indentation. The padding's source is identifiable byte-for-byte: the repo's own EN-side copy of the original page (`pages/theme:ambrose-chapter-two.txt`, the EN sample's base) differs from the raw rev-19 fetch on exactly these 62 lines, every one blank→padded, and the two files are identical after stripping trailing whitespace; the candidate's CSS body descends from that padded copy route, not from the raw fetch this package mirrors.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change. This is not R7 wholesale re-indentation (content lines keep their indentation, so follow-up diffs still apply); it is blank-line padding acquired in the copy route.
- **Verify:** classification.json (60 WS-ONLY blocks, reindent_blocks 0); `diff pages/theme:ambrose-chapter-two.txt review/ambrose-chapter-two-jp/original.txt` shows 62 changed lines, all trailing whitespace.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none — no signature fired, and direct inspection agrees: the candidate contains no `[!-- ... --]` translator notes and no editor line (`grep -c '\[!--' candidate.txt` = 0). The only added text with no original counterpart is the frame, the credit block, the base line and the font supplement, each accounted for in its own section. The CSS comment header is the original's own, carried verbatim, not an annotation.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; here the ground for "none" is the grep above plus the section-by-section accounting.
- **Verify:** The grep in What.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The two EN asset URLs (cand L56, L127): T1 hotlink×2, DISPOSITIONED class (ii) — posting-time rewrites and original-state asset hosts; re-upload is barred by owner order and deferred hosting is the recorded state (GOSIGN2-LEDGER (c1) hotlink entry; (c3) P5, KB-58). (2) The draft-host self-delivery URL (cand L3): class (iii) draft form (the classifier's own note on B2), rewritten at posting (P4); not charged. (3) The render findings: candidate-inherent 328px@320 page overflow (8px) and the 320 header clip (wordmark/account links clipped, search overlaps), DISPOSITIONED as the narrow-width header clip/collision family, a render-side difference class (GOSIGN2-LEDGER (c2), citing FIX3-S2EN §6.5 observations X1–X9 and the KB-35 family). (4) The 503/http.cat capture in the same render row: DISPOSITIONED, a transient Wikidot capture, not a defect (KB-44). (5) Header and title language kept in English: DISPOSITIONED under ruling 2 (ledger (c3) P9; KB-57). (6) The orphaned subtitle snippet (cand L501–505): recorded by the localize T5 pass as an unexplained fragment; no register raises it to an OPEN item and the theme passed with none, so it stands as a known oddity, argued in the Per-theme record. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–5); item 6 recorded.

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 2 errors / 1 warn / 1 info; the errors are hotlink×2 (the section 4 asset URLs); the warn and info codes are not itemized in the extracted row (T1-ROWS row 55; REPORT-GOSIGN2-T1-BASELINE row 55 agrees). Register (c1) dispositions the hotlink class as (ii), and the P6/P7 fixes are recorded as checker-verified in (c3). (b) T2/T3 render: FINDINGS, both items dispositioned in (c2) (section 11, items 3–4); the row records no credit-modal error for this theme, and engine coverage is the lane's full matrix as run (RENDER-ROWS-1). (c) T4 localize plus follow-up: FINDINGS with 4 display-affecting items (LOCALIZE-ROWS row 55); outcomes P5 DISPOSITIONED / P6 FIXED / P7 FIXED / P9 DISPOSITIONED (ledger (c3)). The follow-up currency check found nothing to follow: the upstream original's latest revision is still 19, so the rev19 → rev19 diff artifact records no changes (lane record, part-EN3 follow-up section). (d) T5: the localize lane's findings (the subtitle string, the proper-noun titles, the orphaned snippet, no mistranslation found) are recorded in part-EN3 and carried in sections 5–6 and the Per-theme record. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (74 change blocks) and the generator's (diff.md: +103/−140 in 16 hunks); the two count different units (change blocks vs context hunks) over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ambrose-chapter-two-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 55).

## Per-theme record

### The orphaned subtitle snippet (localize T5 finding 3)

The original explains its subtitle-removal snippet before exhibiting it: "If you wish to use this theme without the "chapter 2" subheading, you may append the following within your work:" (orig L26), then the snippet itself in a code exhibit (orig L28–34). The candidate keeps the snippet — `@@`, `:root { --header-subtitle: ""; }`, `@@` at cand L501–505, at the tail of the delivered module CSS — and drops the explanation. The localize lane's T5 finding 3 states the consequence plainly: a reader meets a fragment whose effect they cannot know, and recommends deleting it or adding a one-line explanation. No later wave acted on the recommendation, and no register dispositions the item by name; the ledger determination passed the theme with no OPEN items, so it stands as a recorded oddity rather than a charged defect. This package does not edit the candidate (review packages never do); the observation is preserved here, with the lane's recommendation, so a future editor decides with the evidence in hand. One placement note: in the original the snippet is a body exhibit (documentation), while in the candidate the same lines sit inside the delivered `[[module CSS]]` block; the render rows record no finding arising from that placement.

### Record conflict — the sources.tsv note for this row

sources.tsv's notes column for this theme states that the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-ambrose-chapter-two-from19.txt` (kind K5a-i). The artifact records the opposite: `rev19 → rev19 変更: なし` (no changes), with an empty intervening-revision list, and the fetching lane's follow-up section confirms the upstream latest revision is still 19 (2026-04-25), identical to the reference revision. There is no post-reference delta to classify and no supersession. The note is a population-level convention in sources.tsv (its own report describes the K5a-i note as recorded across many rows from the existence of a follow-up artifact); for this row it does not survive contact with its own citation, and this package follows the artifact.

### One commit, three fixes (wave attribution)

The ledger's (c3) register attributes this theme's P6 fix to the "frame waves" and its P7 fix to "the font wave", campaign-level wave names. The file's own history is narrower: only two commits have ever touched `pages/theme:ambrose-chapter-two-jp.txt` (3205f27, its creation; 1869877, FIX-CREDIT-D), and the git diff of 1869877 shows the frame include, the translator-field normalization (SCP-JP → AI), the Noto Sans JP @import and all three stack insertions landing in that single commit. The register's outcomes are correct — both items are FIXED in the current bytes — and only the commit-level attribution differs; this package follows the git record. The same diff reconciles the localize lane's line numbers: it examined the 502-line 3205f27 state, so its references (hotlinks at L50/L121, the snippet at L495–499, the credit block at L3–12) sit 5–6 lines above the current file's (L56/L127, L501–505, L8–17) — the frame's five lines and the font import's one.

### Post-package repairs (REFRESH3-E)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:ambrose-chapter-two-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-FRAMED — frame sub-shape (D) treated as (B), own-address pointer dropped (landing 5d95177).** `FIX-FRAMED.md` records this theme's frame as sub-shape (D): the frame's `theme=` named the theme's own code block (/1) on the draft host, but the candidate carries no `[[code]]` block in any form (its CSS is live `[[module CSS]]`), so the named block does not exist — a dead pointer, verified in the report. The original's once-live form: its @import (L2) and frame (L12) name its own /1; block 1, `[[code type="css"]]` L71–544, is the CSS source. The coordinator's ruling treats (D) as (B) and applies the minimal remedy: drop the single `| theme=https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aambrose-chapter-two-jp/1` line, keep the `[[include :scp-jp:component:interwiki-style]]` frame, its priority, and every other byte unchanged. Commit 5d95177 deleted exactly that one line at candidate L3. The checker finding set is unchanged (2 errors / 0 warn / 1 info before and after; the dropped line was not a class (i) finding), as tabulated in FIX-FRAMED.md.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-ambrose-chapter-two-jp.txt` — the render sample page (two lines: an include of the candidate and an include of the shared `theme-decoration-sample`), created in the same S2 commit 3205f27; it is the "sample" the T2/T3 checks rendered, and it is where this theme's sample content lives after the candidate page dropped its own sample body (section 8). (2) `pages/theme:ambrose-chapter-two.txt` — the repo's EN-side copy of the original page, the EN sample's base: content-identical to this package's mirror after stripping trailing whitespace, its 62 blank lines space-padded (the shape the candidate's CSS body inherited, section 9). (3) The delivery itself: the candidate's own local--code /1 on the draft host, named by the frame (cand L3), which is the runtime form of the self-delivery; the classifier records its companion body as unavailable (classification.json topology caveat). The original side's /1 was the code exhibit itself (section 3).

## Multi-wave provenance

The candidate's current state is the product of two commits and three check waves, not a single porting pass: the S2 EN batch 1 created it (commit 3205f27: translation, credit block, CSS inlining, sample-body drop, bare-Rate removal, and the bunny→Google font-import repoint already present); LOCALIZE-S2-A then examined that state and charged P5/P6/P7/P9 plus the T5 notes (its report is part-EN3 in the campaign record, `gosign2-lanes/lane-oc-gs-localize-s2-A/`); the FIX3-S2EN adjudication dispositioned the render findings as the narrow-width family; FIX-CREDIT-D (commit 1869877, the file's last content change) landed the frame, the font supplement and the attribution normalization in one commit; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 55, (c1) hotlink entry, (c2) ambrose entry, (c3) ambrose entry; GOSIGN2-LEDGER-SUPPLEMENT.md (no ambrose entries); T1-ROWS row 55; LOCALIZE-ROWS row 55; RENDER-ROWS-1 (RENDER-S2-A) ambrose row. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue blocks

The classifier emitted three open blocks; all three are resolved, none required a new signature.

- **R1 — B7 (residue; orig L21–26 → cand L23, body → body).** The import-instruction block. Resolved in sections 6 and 8: the block was restructured — its payload (the include line) survives as the usage line (cand L21, the added side of B6), its wrapper and separator were dropped as exhibit furniture, and its slot in the page is taken by the base-declaration line (cand L23). The subtitle explanation sentence inside it (orig L26) is the prose half of the T5 orphan (Per-theme record).
- **R2 — B5 (heuristic; orig L17 → cand L19, body → body).** The introduction sentence. Resolved in section 6 as P10 translation by compression (the classifier's TRANS-UNANCHORED label stands); the attribution content's relocation is traced to the credit block and the comment header.
- **R3 — B6 (heuristic; orig L19 → cand L21, body → body).** The usage sentence. Resolved in sections 6–7: the prose sentence was replaced by the usage line itself, in the P1 same-site include form; the permission half-sentence's absence is recorded in section 6.

## License and attribution

- **Title:** Ambrose Chapter Two
- **Author:** Proasek
- **Source:** https://scp-wiki.wikidot.com/theme:ambrose-chapter-two — revision 19
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
