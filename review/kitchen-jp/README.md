# Review package — theme:kitchen-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:kitchen-jp — origin CN, population #200 [GOSIGN2-LEDGER (b) row 200]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); both OPEN items re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 126 errors / 1 warn / 2 infos (hotlink×125, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 230; GOSIGN2-LEDGER (b) row 200]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink incl. candidate-own ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com, bhl.scpwikicn.com, hormress.github.io, nu-scptheme.github.io, scpsandboxcn.wdfiles.com (judgment-required), no page-overflow; sample credit-modal (preview-form), runtime-hotlink incl. the same candidate-own hosts + sample font host; T3 REAL FINDING on both pages: body text (headings, paragraphs, lists, table cells, labels) renders near-white rgb(254,254,254) on the pale pink --BG (244,240,240) background and is effectively unreadable (chromium 1366/375/320, webkit 1366/375; machine contrast warn min 1.06 corroborates; canonical source has no white body-text rule, not an intended aesthetic); sidebar/credit/footer otherwise intact. [RENDER-ROWS-RERUN16 (CN8) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN8)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 199, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 199]
- FIX5 re-judgement: items 63 (class B) FIXED, 64 (class E) FIXED — FIX5-FURNB, commit 25bb0b4: duplicate bare Rate block removed; candidate palette byte-identical to original; cause isolated to the JP base swap (theme:parallel-jp unconditional dark :root at L416-420 vs original's preset-gated schemes); kitchen-local override added; contrast recomputed 1.121 -> 16.29 [GOSIGN2-LEDGER-SUPPLEMENT (a) items 63–64]
- Computed against: canonical commit 25bb0b40f10153f1f8bdda252283bb7aa7a76875; candidate file pages/theme:kitchen-jp.txt sha256:2939136b55fce97e86abc88961d64622332996d3c872f16dd66bb0bf47490857; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); this theme's stamp is not stale, because the FIX5 commit is the candidate's last change |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 63 [B] (duplicate bare Rate beside the rate-bearing preview credit block) and item 64 [E] (KB-28 contrast: body text near-white on the pale-pink background, effectively unreadable) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md rows 63 and 64: both **FIXED** (FIX5-FURNB, commit 25bb0b4); both re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c3): P1 (posting-procedure convention), P5 (class (ii) / KB-58), P9 (ruling 2: header/title language out of scope); ledger §(c2) render row: candidate-own foreign/sandbox delivery hosts (class (ii), KB-41/KB-54 family), credit-modal preview form (KB-32), the machine contrast warn as corroboration (KB-39) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:kitchen | theme:kitchen-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 9, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 9 (candidate L46) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-kitchen.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:kitchen-jp.txt`, copied at worktree HEAD 118306b |
| Lines / bytes | 1,152 lines / 37,983 bytes (the file's last line carries no trailing newline, so `wc -l` reports 1,151) | 1,163 lines / 41,432 bytes |
| SHA-256 | d30a8135d483c8bf64654b0b79b06a3ef388b187a8abfc6fec1f30f0f82e0df7 | 2939136b55fce97e86abc88961d64622332996d3c872f16dd66bb0bf47490857 |

Follow-up note (sources.tsv, K5a-i): the original has been superseded upstream since revision 9; the campaign record holds a follow-up diff artifact (`diff-kitchen-from9.txt`) for that later movement. This package's mirror stays at revision 9, the revision the port was actually made from; the supersession is recorded here rather than absorbed silently (section 12).

Wave history: the candidate was created by the Stage 2 CN8 integration (commit e469417); the Stage 2 rework (eb1e7ae) externalized the Parallel base it had initially inlined, which is the delivery form section 3 describes; FIX-CREDIT-D (1869877) normalized its translator attribution; FIX5-FURNB (25bb0b4) closed items 63 and 64 in two hunks and is the file's last content change.

## Summary

Kitchen is a Basalt-family theme built on the CN Parallel base: the original page carries its documentation inside a tag gate and its stylesheet in a live module after the gate, and a consumer applies it by including the CN Parallel page and the kitchen page together. The candidate re-bases every leg of that composition onto the JP candidates: the base arrives through an include of theme:parallel-jp at the candidate's head, the theme's own CSS moves into its own code block and is delivered from it by a local--code import and the standard frame, and the usage example shrinks to the single include that now suffices. Measured churn (diff.md, the generator's difflib count: +179/−173, 352 changed lines in 77 change blocks / 9 hunks; a GNU-diff count gives 259) is mostly that delivery relocation plus the documentation translation; the stylesheet body pairs line for line. The two blocking items were both composition defects, not translation defects: a bare Rate module the credit swap left standing beside the rate-bearing preview block, and a contrast failure caused not by anything in this file's palette (which is the original's, byte for byte) but by the JP base's default color scheme binding underneath it. Both fixes are small, late, and re-derived below from the bytes.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 77 change blocks — 42 specific (54.5%), 35 heuristic (45.5%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| COLON-ENC | 3 |
| COMMENT-TEXT | 2 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-MOVE | 8 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 3 |
| GLYPH-FORM | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 40 |
| TRANSLATION-ANCHORED | 28 |

Labels are sets, so the column sums past 77: the delivery head (B1) alone carries SELF-DELIVERY, IFTAGS, DRAFT-HOST, and TRANS-UNANCHORED spans, and the FIX5 contrast override rides inside a DELIVERY-MOVE block (B73). The sections below are written from the label spans, not from the primary labels.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with its tag gate (original L1) and has no delivery header at all; its delivery sits after the gate (section 3). The candidate opens with a three-part delivery head before the gate (candidate L1–10): the base include, the self-delivery module, and the interwiki-style frame at priority=1 naming its own code block. Provenance route: derived from the original at the reference revision (scp-wiki-cn, revision 9; mirror class COPY, hash-verified); the candidate's credit block records the revision (candidate L46). The original has since been superseded upstream; the follow-up artifact is named in Provenance and the mirror is not silently refreshed.
- **Why:** The head is the candidate's delivery contract (P4/P6); stating the provenance route here is what lets a reviewer judge every later section against the right original.
- **Verify:** Read candidate L1–12 against original L1; the credit block's revision field is candidate L46.
- **Disposition:** Recorded; the delivery head itself is argued in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is the CN credit trio (`:scp-wiki-cn:credit:start` / `credit:more` / `credit:end`, original L31–35) with prose placeholders and no fields. The candidate carries the JP preview credit block (candidate L38–49) with the eight standard fields plus a font field: author breaddddd, holder "breaddddd & Dr Hormress", revision 9, and the source link to the CN original. Both names are evidenced inside the original itself: breaddddd is named as the maker in the original's intro and as the burger artwork's author (original L172), and Dr Hormress is the author of the Parallel base this theme builds on, corroborated in-file by the base-derived variable `--dr-hormress` (original L414) and stated outright in the acknowledgment prose the porter added (candidate L380, section 10). Neither side carries a license-box include. The furniture defect of this section is the bare Rate: the original's bare `[[module rate]]` (original L28–30) stood beside a credit form that carries no rating widget of its own in the CN environment, but the JP preview block is rate-bearing, so the carried-over module duplicated the widget — that is ledger item 63, re-derived in the per-theme record. In the current bytes no bare Rate stands anywhere in the file.
- **Why:** P3/T1 (credit swap to the rate-bearing JP form), ruling 3 (2026-11-16) for the field set and translator form （翻訳責任者: AI, candidate L44); KB-09 (duplicate bare Rate beside a rate-bearing credit block renders two widgets).
- **Verify:** `grep -n 'module rate\|module Rate' candidate.txt` returns nothing; read candidate L38–49 against original L28–35.
- **Disposition:** P3 FIXED (credit waves; ledger §(c3)); the duplication is item 63, FIXED by FIX5-FURNB (per-theme record).

### 2. Includes and components

- **What:** Candidate includes: `theme:parallel-jp` (candidate L1, the base), the credit pair (L38/L49), `component:theme-squares` in the color exhibit (candidate L76; the original's `:scp-wiki:`-prefixed form at original L61 takes the bare JP component name), two `component:image-block` exhibits, and the frame (section 0). The usage example (B8) changes shape with the delivery: the original shows the consumer two includes (`:scp-wiki-cn:theme:parallel` and `:scp-wiki-cn:theme:kitchen`, original L55–56), the candidate shows one (`[[include theme:kitchen-jp]]`, candidate L71), because the base include now rides inside the candidate's own head; the intro prose states exactly that (candidate L51). The theme-squares include was the one T4 left unverified (row 199, pattern 1); it now takes the bare component form that resolves on scp-jp, and the ledger dispositions the pattern-1 class as the posting-procedure convention. No include is duplicated.
- **Why:** P1 (include targets take JP forms), T8/ruling 4 (the base the theme needs is the JP port candidate, included with the theme).
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare; read candidate L68–72 against original L52–57.
- **Disposition:** Standing; pattern 1 DISPOSITIONED (ledger §(c3) P1).

### 3. Delivery and code loading

- **What:** The original's own CSS is a live `[[module CSS]]` after the gate (original L377–1151), and the theme page applies its base to itself through an in-gate module importing the CN fragment's code (original L363–373); a consumer including the page receives the tail module as the delivery. The candidate relocates the same stylesheet into its own `[[code type="css"]]` block (candidate L383–1161, inside a collapsible in the gated body) and delivers it from the ungated head: an `@import` of its own local--code /1 (candidate L4) and the frame's `theme=` naming the same /1 (candidate L9), over the base include of `theme:parallel-jp` (candidate L1). The address audit's question answers cleanly here: the candidate contains exactly one code block in any form, that block is the stylesheet itself (some 780 lines, not an exhibit), and both delivery references name it — the exhibit-misdirection shape does not occur. The DELIVERY-MOVE blocks (B70–B77) are this relocation plus the changes that ride inside it: the JP font import (B71, section 4), the `:root:lang` gate rename (B72, section 5), the FIX5 contrast override (B73, per-theme record), and one colon-encoded asset URL (B76, section 4). The stylesheet body otherwise pairs line for line with the original's module (the burger-image series, the content rules, the palette), which the diff's long equal runs show. What did not survive the relocation is the in-gate fragment module's pair of page-title rules (original L366–372: the page-title suppression and h1 offset the original page applied to itself); their import leg is superseded by the base include, and the candidate page's title presentation is its carried meta-title block (candidate L14–16) under the base's own furniture — recorded here and in section 8 rather than passed over.
- **Why:** P4/T9 (base delivery from the JP distribution), P6/T3 (own-code delivery via the frame), KB-41 (the candidate's own local--code on the draft host is the draft-stage form, class (iii)).
- **Verify:** Count code blocks: `grep -cn '\[\[code' candidate.txt` (1); read candidate L1–10 and L382–386 against original L363–380.
- **Disposition:** DISPOSITIONED as draft form (class (iii)) for the /1 URLs; the relocation itself is the port's delivery change, standing.

### 4. Fonts and assets

- **What:** Fonts: the original imports Kaushan Script, EB Garamond, and Noto Serif SC from Google Fonts (original L378–380). The candidate imports the same three with the CJK face swapped to Noto Serif JP (candidate L384–386, JPFONT-LOAD), and the two stacks that named the SC faces name the JP faces instead: `--header-font` (original L424 → candidate L433, Noto Sans SC → Noto Sans JP) and the serif stack (original L527 → candidate L536, Noto Serif SC → Noto Serif JP; the classifier files this line under DELIVERY-MOVE because the whole stylesheet changed channel, but the change itself is the P7 stack rewrite). Noto Sans JP is not imported by this file; it is the JP fallback the base delivery chain loads (the basalt-family JP pattern, documented in theme:basalt-jp's own fallback comment), and the credit block's font field (candidate L48) lists exactly the three imported faces plus, in the acknowledgment prose, Noto Sans JP — consistent with where each is loaded. No stack names a face that nothing loads. Assets: the theme's images stay on the original's hosts — the author's sandbox files (the ck-01 logo and the thirty burger images on scpsandboxcn.wdfiles.com) and the Parallel logos on ah-sandbox.wikidot.com — which is the ~125-line hotlink population of the T1 baseline; three of those URLs gain the colon-encoded page-name form (B5, B6, B76; KB-01). The Pixabay photo credits ride as CSS comments on both sides.
- **Why:** P7/T5 (JP font in the stacks, with its load), P5 (asset re-hosting) — the asset half is dispositioned, not applied: the files are the author's own sandbox hosting in the original as well, the pages render today, and re-hosting is a posting-time act (KB-58 deferred-404/hosting family; ledger §(c3) P5, class (ii)).
- **Verify:** `grep -n '@import' candidate.txt` (3 lines, L384–386); `grep -c 'scpsandboxcn' original.txt candidate.txt` for the retained asset population.
- **Disposition:** Fonts standing; assets DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** One furniture block changes form: the original's `:root:lang(cn)` block (original L385–388) sets `--title: "SCP厨房"` and an English subtitle; the candidate carries the same block as `:root:lang(ja)` with both strings verbatim (candidate L391–394, B72). The gate rename is what makes the kept strings apply in the JP environment at all; the strings themselves are the header/title language T4 charged as pattern 9. Kitchen sets no `--header-title`/`--header-subtitle`/`--logo-image` overrides on either side; the header presentation otherwise rides on the base.
- **Why:** P9/T6 for the variable block; the language of the kept strings is dispositioned under ruling 2 (2026-11-16: header and title language is translation taste, outside migration correctness).
- **Verify:** Read candidate L391–394 against original L385–388.
- **Disposition:** DISPOSITIONED (ledger §(c3) P9, ruling 2).

### 6. Text translation

- **What:** The documentation body is translated throughout: the meta-title (candidate L15), the intro and usage prose, the color and layout exhibits, and the burger/header sample sections (28 anchored blocks, 40 unanchored; every unanchored block is a one-to-one line translation, resolved by shape in the appendix). Two in-CSS text items are localized separately from reader-visible prose (R1): the color exhibit's comment （德克士， the Dicos brand the sample palette is named for) becomes the phonetic ディコス (B67's COMMENT-TEXT span), and a carried translator-credit comment for a borrowed section is glyph-localized (B38: 原作者：Cryogenchaos 翻譯者：ashausesall → 原作者：Cryogenchaos 翻訳者：ashausesall, traditional forms to Japanese forms). The sample content itself (the thirty burgers, the KFC-red/McDonald's-yellow palette names) is carried as the theme's own content, translated where it is prose.
- **Why:** P10/KB-18 (reader-visible text localizes); R5 (glyph-form conversion) for the credit comment; R1 for in-CSS text stated separately.
- **Verify:** Read candidate L14–380 against original L3–361 section by section.
- **Disposition:** Standing (the port itself); T5's one minor item is recorded in the T4 row and carries no separate ledger item (section 12).

### 7. Links

- **What:** The intro names the base twice, once per role (candidate L51): the CN Parallel page by its absolute URL, as the original work's identity in the attribution sentence, and `theme:parallel-jp` as the delivery the candidate actually includes. The acknowledgment prose (candidate L380) links the EN Bedrock page on scp-wiki inside the attribution chain (Basalt's base); that is a prose credit link to the original work, recorded here and not repointed, per the campaign's rule that attribution links are not delivery references. No prose link in the candidate targets the un-suffixed `theme:kitchen` name, and the credit source link (candidate L47) names the recorded CN host.
- **Why:** P11 (links take the JP counterpart or the serving original under the dead-reference evidence standard); the distinction between delivery references and attribution references is what decides which links repoint.
- **Verify:** `grep -n 'theme:kitchen' candidate.txt`; read candidate L51 and L380.
- **Disposition:** Standing.

### 8. Structure

- **What:** The closing rule is kept for the stylesheet (selectors, variable names, and rule order pair with the original's module), and the documentation keeps the original's section order. Three structural changes are the record's own. (a) The gate's span: the original's gate closes at original L375 and its stylesheet module stands outside it; the candidate's gate runs to the end of the file (candidate L1163) and contains the code block, which is safe because delivery no longer depends on the module's gate position — it is served from the code block by the ungated head (section 3). (b) Exhibit conversions: the color-sample `[[code]]` exhibit (original L351–361) becomes an escaped-text exhibit in a `div.code` (candidate L367–377) with its values intact and its comment translated — a form replacement, not a drop; B10 and B13's EXHIBIT-RESTRUCTURE labels adjudicate the same way (the theme-squares include takes its JP form, the image-block exhibit keeps its image and host with its caption translated; neither exhibit is dropped or replaced in content). (c) The dropped in-gate module (original L363–373): its import leg is the superseded base channel (section 3), and its two page-title rules have no counterpart; the ground is that they were self-presentation for the superseded composition, in which the page imported the base fragment into itself, while the candidate page's presentation is the base include's furniture plus the carried meta-title. CSS integrity: a brace-depth scan of both files ends at depth 0, maximum depth 2, no negative excursion.
- **Why:** The localize closing rule, with deviations named; R3 requires the ground for every exhibit-form change and drop, which (b) and (c) state.
- **Verify:** Compare the structural maps (`grep -n` for `[[module`, `[[code`, `[[iftags` in both files); the depth scan is a five-line brace counter over either file.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** none — WS-ONLY blocks: 0; re-indentation: 0 blocks pair up after leading-whitespace normalization. The relocation of section 3 moves lines between channels but does not re-indent them.
- **Why:** Formatting-only churn is disclosed as its own class (negative-ledger rule R7 is not triggered).
- **Verify:** The class summary's counts and diff.md's nine hunks.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two porter additions stand in the candidate. (1) The acknowledgment section （出典と謝辞, candidate L379–380): a porter-written attribution prose block with no counterpart in the original, stating the full derivation chain (Dr Hormress's Parallel on Basalt, breaddddd's authorship and extension, EstrellaYoshte and Placeholder McD's Basalt on Bedrock, normalize.css's MIT license, and where Parallel's body lives in the JP composition) and the font list. It is the in-file ground for the credit block's holder field (section 1). (2) The FIX5 override comment (candidate L400), one Japanese sentence inside the palette block stating why the two color variables are made explicit; it rides inside the DELIVERY-MOVE block B73 and is the fix's own in-file record (per-theme record). The classifier's ANNOTATION span at B38 is not a porter addition: it is the carried translator-credit comment of section 6, localized in glyph form.
- **Why:** R2 (porter annotation additions are part of the change record, never original content or translation).
- **Verify:** Read candidate L379–380 and L400.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section: (1) the sandbox-hosted asset population (section 4) — class (ii) / KB-58, re-hosting deferred to posting; (2) pattern 1 (the parallel slug and the theme-squares include form) — the posting-procedure convention class (section 2); (3) the kept Chinese header strings under the renamed lang gate — ruling 2 (section 5); (4) the candidate's own local--code /1 URLs — draft form, class (iii) (section 3); (5) two `http://` strings the classifier's HTTP-KEPT presence reports at candidate L437–438: both are W3C namespace declarations inside data-URI SVG masks (`--logo-outside-mask` / `--logo-inside-mask`), not links at all — the signature's known false-fire shape, recorded so the count is explained rather than passed over; (6) the render-row dispositions: the runtime-hotlink chain including candidate-own hosts (class (ii), KB-41/KB-54 family), the sample credit-modal preview form (KB-32; ruling 5), and the machine contrast warn, which the ledger records as corroboration of item 64 with the KB-39 caution that machine contrast warns include false positives on themed surfaces (here the T3 walk confirmed the finding was real, and the fix is the per-theme record's).
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** The evidence behind the stamp. (a) T1 baseline (2026-11-16): exit 1, 126 errors / 1 warning / 2 infos (hotlink ×125, pseudo-ref ×1); the 125 are the section 4 asset population and the 1 is the draft-form delivery reference [T1-ROWS row 230; GOSIGN2-LEDGER (b) row 200]. (b) T2/T3 (RERUN16 (CN8)): the contrast finding was the row's one OPEN item, closed by item 64's fix; the rest of the row is dispositions, including the positive note that sidebar, credit, and footer are otherwise intact [ledger §(c2) row]. (c) T4/T5 (LOCALIZE-S2-D): FINDINGS with four display-affecting items, mapped one to one in section 11 and the per-theme record (pattern 5 → P5 disposition; pattern 3 → item 63; pattern 9 → P9 disposition; pattern 1 → P1 disposition), plus one minor T5 item that the row records without a separate ledger item [LOCALIZE-ROWS row 199]. (d) T4's follow-up half: the original is superseded upstream since revision 9 and the campaign holds the follow-up diff (`diff-kitchen-from9.txt`); this package's mirror stays at revision 9. (e) This package is self-verifying: `python3 review/build_review.py --check`. Counts in this README are the generator's (difflib, autojunk off): +179/−173, 352 changed lines in 9 hunks. A GNU-diff count of the same pair gives 259 changed lines; the difference is alignment choice (the relocation aligns differently), not content.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:kitchen-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### Ledger item 63 [B] — the duplicate bare Rate, re-derived

At ledger time the candidate carried the original's bare `[[module rate]]`, wrapped in its `[[>]]` div, immediately before the preview credit block; because the JP preview block embeds its own rating module, the page rendered two rating widgets (the checker's double-rate info is the machine trace of the same fact). The supplement re-judged the item FIXED by FIX5-FURNB, commit 25bb0b4, and the commit's first hunk for this file is exactly the claimed change: the four lines `[[>]]` / `[[module rate]]` / `[[/>]]` and their blank line deleted, nothing else in that hunk. The current bytes confirm the end state: no `[[module rate]]` or `[[module Rate]]` stands anywhere in the candidate (grep count 0), and the single credit pair stands at candidate L38/L49. The lane's checker control (double-rate infos cleared on all nine files in its set, zero new errors) is consistent with the bytes. The fix is present and complete.

### Ledger item 64 [E] — the contrast failure, re-derived as a value-set argument

The T3 finding: body text (headings, paragraphs, lists, table cells, labels) rendered near-white rgb(254,254,254) on the theme's pale-pink `--BG` (244,240,240) on both pages, contrast 1.06 by the machine warn. The supplement's account has four steps, and each checks against the bytes in this package plus the base candidate in the same repo.

1. **The port did not change the palette.** The candidate's palette block (candidate L396–416) pairs line for line with the original's (original L390–406): `--KRed: 228, 0, 43`, `--McYellow: 255, 188, 13`, `--BG: 244, 240, 240`, and the overtone/undertone chain are identical. Nor does either file's kitchen text define `--basalt-main-text-color` at all — in the original composition that variable came from the base.
2. **The base swap changed the binding underneath.** The original builds on the CN Parallel, whose color schemes are preset-gated: the scheme in force for the original's presentation binds a dark main text color over kitchen's light background. The JP base candidate, theme:parallel-jp, instead sets its default `:root` unconditionally to its 红石 scheme (pages/theme:parallel-jp.txt L416–420: `--basalt-primary-color: 20, 20, 20; --basalt-main-text-color: 254, 254, 254`), so in the JP composition kitchen's light `--BG` inherited near-white text — the port's variable binding, not an intended aesthetic, exactly as the ledger charged.
3. **The fix states the original composition's effective pair explicitly, in kitchen's own block.** FIX5-FURNB's second hunk (commit 25bb0b4) inserts three lines after `--BG` (candidate L400–402): a porter comment giving the reason, `--basalt-primary-color: 254, 254, 254`, and `--basalt-main-text-color: 20, 20, 20`. Because kitchen's block is delivered after the base in its own composition, the explicit pair overrides the base default for every page that applies kitchen, while themes that do not include kitchen keep the base's scheme untouched — the fix is local to the theme whose background requires it, which is why it belongs in this file and not in the base.
4. **The result.** With text at 20,20,20 on 244,240,240, the lane's recomputed contrast is 16.29 (from 1.121 on its pre-fix measurement; the render row's machine warn read 1.06). The override lines are present in the current bytes at candidate L401–402, and the palette around them is unchanged, so the reader can re-derive the whole argument from this package and `pages/theme:parallel-jp.txt` without trusting the supplement.

KB-28 is the pattern this instance confirms: a contrast failure whose cause is a variable binding inherited from a swapped base, fixed by stating the original's effective values in the theme's own palette block.

## Change set outside the two diffed files

(1) `pages/theme-decoration-sample-kitchen-jp.txt` — the decoration sample page the render checks ran against. (2) The base dependency itself: `pages/theme:parallel-jp.txt`, included at candidate L1; its own review package covers its port, and section 3 and the per-theme record cite the specific lines of it this theme's correctness depends on (its default `:root` at L416–420). The original side of the change set is the CN Parallel page and its fragment, which enter this record through the original's own references to them.

## Appendix — heuristic adjudication

The classifier left 35 heuristic blocks (tier C) and no residue: the 34 TRANS-UNANCHORED-primary blocks plus B67. They resolve by shape, not one by one. Thirty-one of the TRANS-UNANCHORED blocks are single-line prose, label, and exhibit translations in the documentation body (B7, B11, B14, B15, B19, B21–B31, B37, B40–B43, B47, B49, B51, B53, B56, B58, B61, B62, B64, B66), each verified against its original line as a one-to-one translation with no content added or dropped. The remaining four carry substance their sections record: B4 (the credit region's realignment, section 1), B67 (the color exhibit's form conversion, sections 6 and 8), and B68/B69 (the same realignment's other half — the exhibit's tail lines and the acknowledgment section's insertion, sections 8 and 10). No heuristic block required a new signature.

Multi-label spans the primary-label listing under-reports, for the record: B1 carries the IFTAGS and DRAFT-HOST spans inside the delivery head (sections 0 and 3); B3 carries TASL-FIELDS and CREDIT-PROSE inside the credit block (section 1); B5/B6 are COLON-ENC blocks on single-line image exhibits (section 4); B38 carries the ANNOTATION span on a carried credit comment (sections 6 and 10); B71 carries JPFONT-LOAD inside the delivery move (section 4); B72 is the lang-gate rename inside the delivery move (section 5); B73 carries the COMMENT-TEXT span of the FIX5 override's own comment (per-theme record); B76 carries a COLON-ENC span inside the delivery move (section 4). The systematic lesson — a FIX5 repair can ride inside a DELIVERY-MOVE block and be invisible to a primary-label reading — is recorded in the lane report as a classifier-precision note.

## License and attribution

- **Title:** 中央厨房 版式
- **Author:** breaddddd & Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:kitchen — revision 9
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
