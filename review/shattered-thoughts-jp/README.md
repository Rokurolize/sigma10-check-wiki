# Review package — theme:shattered-thoughts-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:shattered-thoughts-jp — origin EN, population #136 [GOSIGN2-LEDGER (b) row 136]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 5ce0222552ea8828beab051d065972830d82e2792f5427866dc678447302c16c); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 0 warns / 2 infos (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 121; GOSIGN2-LEDGER (b) row 136]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only (T3: credit modal opens); sample credit-modal (preview-form) + 884px@768 overflow; T3 broken explanet.png (deferred asset). [RENDER-ROWS-2 (RENDER-S2-D (EN19))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN19))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 136, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 136]
- FIX5 re-judgement: items 27 (class B) FIXED, 28 (class D) FIXED — FIX5-FURNA, commit 9e8931f: duplicate bare Rate block removed; double-rate cleared; pattern-7 Noto Sans JP supplement for this theme (also in the lane commit message) [GOSIGN2-LEDGER-SUPPLEMENT (a) items 27–28]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:shattered-thoughts-jp.txt sha256:5ce0222552ea8828beab051d065972830d82e2792f5427866dc678447302c16c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | PASS (go-sign re-run; 286 of 286 pass-eligible themes, theme:amethyst-v2 the named exception) |
| Blocking items at ledger time | 2 — GOSIGN2-LEDGER §(e) items 27 (class B) and 28 (class D) |
| Re-judgment | Both FIXED (GOSIGN2-LEDGER-SUPPLEMENT, FIX5-FURNA, commit 9e8931f); re-derived from this package's bytes in §Per-theme record |
| Standing items | T1 pseudo-ref ×5 (class (iii) draft-stage deliveries, dispositioned at register (c1)); render-row dispositions (site-theme chain, credit-modal preview form, sample overflow, deferred broken image) |
| Go-sign basis | GOSIGN2-LEDGER-SUPPLEMENT §(c) (ledger (c1)–(c3) + spot checks) |
| Named exception | None |

The stamp above reads STALE by design: it was computed against canonical commit b5cb7241f527a44933e45599b41df210690771c4, whose candidate bytes differ from the frozen verdict bytes (canonical 435a6bb) by exactly one line, the usage-example sweep's posting-name completion (candidate line 55, commit b5cb724). The stamp therefore does not carry the PASS onto changed bytes; the frozen ledger remains the verdict record. The sweep line is recorded in §Per-theme record.

## Provenance

| | |
|---|---|
| Page | theme:shattered-thoughts (EN) → theme:shattered-thoughts-jp |
| Wiki | scp-wiki (EN) |
| Reference revision | 34 (first-translation revision; no supersession note in sources.tsv) |
| Source of this copy | Mirror store, `orig-shattered-thoughts-rev34.txt` (class COPY in the mirror INDEX) |
| original.txt | 681 lines, 13,720 B, SHA-256 d2aaddd69d05bacc4e1049d389ebcd0cb85e1c8aee1ff2ef6098cc8a914c923c (equals the sources.tsv value; the file's last line carries no trailing newline, so `wc -l` reports 680) |
| candidate.txt | 689 lines, 14,894 B, SHA-256 5ce0222552ea8828beab051d065972830d82e2792f5427866dc678447302c16c (byte-identical to the canonical candidate; last line unterminated, `wc -l` 688) |

Wave history: Stage 2 (EN19) integration → FIX2-CREDIT → FIX5-FURNA (the two blocking items) → the usage-example sweep. Full commit list in §Multi-wave provenance.

## Summary

A compact port of a small Sigma-9-era EN theme. The delivery topology is unchanged: a three-line head module imports the page's own code block, an interwiki frame at priority 1 names the same stylesheet, the gated body carries the documentation and exhibits, and the 482-line code block closes the page. Onto that skeleton the port lays the campaign's standard JP layer: the credit block the original never had, the body translation, the JP font supplement that ledger item 28 charged as missing, and the removal of the duplicated bare rating module that item 27 charged. The diff is +182/−180 lines in 105 change blocks, but most blocks are one-line CSS comment translations (32 COMMENT-TEXT blocks) and translated exhibit lines; only 40 blocks carry a specific signature. Both FIX5 closures are re-derived from the fix commit and the current bytes in §Per-theme record. No defect flag is raised for this theme.

## Standing sections

### 0. Provenance and header comments

**What.** The original opens with its delivery header: a `[[module CSS]]` importing its own `theme:shattered-thoughts/code/1` from `scp-wiki.wikidot.com` (original lines 1–3), then the interwiki-style frame at priority=1 naming the same stylesheet (lines 6–9). The candidate keeps both shapes with JP addresses: the head module imports the candidate's own `local--code/theme%3Ashattered-thoughts-jp/1` on the draft host (candidate lines 1–3), and the frame's `theme=` names the same draft-host address (lines 6–9; blocks B1, B3). Neither file carries a porter header comment; the candidate's only header matter is the credit block (§1).

**Why.** Class (iii) draft-stage self-delivery (FIX-CODEADDR.md population form): the candidate must deliver from addresses that will exist as its own page's code files at posting, and the draft host is where the campaign's candidates stage them. Pattern P3's delivery pair (head module + frame naming one stylesheet) is the population's standard shape.

**Verify.** `sed -n '1,9p'` on both files; the two candidate addresses are the same URL.

**Disposition.** Standing class (iii) deliveries, dispositioned at ledger register (c1); not charged by any item.

### 1. Credit block, license box, rating and credit CSS (T1 / T7)

**What.** The original carries no credit apparatus at all: no credit block, no license box, and no author named anywhere in its source (its only rating furniture is a bare `[[module Rate]]` in a `[[>]]` div at original lines 13–15). The candidate adds the T1 preview-form credit block inside the gate (candidate lines 13–22, block B5): タイトル "Shattered Thoughts Theme", 翻訳責任者 AI, 翻訳年 2026, 原題 "Shattered Thoughts Theme", 著作権者 `[[*user Yossipossi]]`, 作成年 2021, 初訳時参照リビジョン 34, and the 元記事リンク naming the original page on scp-wiki.wikidot.com, the host sources.tsv records for the original. The holder field names a person; the original's source carries no credit text that could contradict it (the value is the one the credit waves entered from the page's authorship record; FIX2-CREDIT, commit 666f543, is this file's credit wave). No license box exists in either file: the original carried none and the port added none, so the KB-63 dropped-box shape does not arise. The original's bare Rate was carried into the early port beside the new preview block, which produced ledger item 27 (§Per-theme record); the current candidate contains no `[[module Rate]]` at all. T7: the candidate's credit-rate CSS (the `.rate-box-with-credit-button` rule, candidate line 307) is byte-identical to the original's (original line 299) — inherited theme CSS; no `.creditButton` selector exists in either file and no KB-11 supplement was added.

**Why.** Pattern P3 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): a theme page without the JP credit block fails the JP posting form, and the preview form keeps the rating module embedded so no second rate control stands on the page (KB-09/KB-32 family). Ruling 3 fixes the TASL-style field set.

**Verify.** `sed -n '13,22p' candidate.txt`; `grep -c 'module Rate' candidate.txt` (0); `grep -n 'Yossipossi' original.txt` (no hits — the original names nobody).

**Disposition.** Credit block: the port's T1 supplement, part of the PASS bytes. Item 27's closure is re-derived in §Per-theme record.

### 2. Includes and gates

**What.** Three include repoints, all JP-internal: the interwiki frame's site prefix `:scp-wiki:` → `:scp-jp:` with `priority=1` kept (block B2); the image-block exhibit's prefix `component:image-block` → `:scp-jp:component:image-block` (B14, §4 for its image); the usage exhibit's escaped include repointed to `:scp-jp:theme:shattered-thoughts-jp` (B12; the -jp completion is the sweep's line, §Per-theme record). The gate localizes: `[[iftags +theme]]` → `[[iftags +テーマ]]` (B4, candidate line 11).

**Why.** Include repoints keep every delivery inside the JP wiki's own component namespace (pattern P4 include-graph localization; KB-54's inverse — these components have JP counterparts). The iftags value is the JP tag name for the same gate (KB-08).

**Verify.** `grep -n 'include' candidate.txt` against the original's include lines; `sed -n '11p' candidate.txt`.

**Disposition.** Standard port mechanics; no item charged them.

### 3. CSS delivery (imports, code blocks, cross-imports)

**What.** Topology unchanged. Original: head module CSS (lines 1–3) + one `[[code]]` block (lines 199–680, 482 lines). Candidate: head module CSS (lines 1–3) + one code block (lines 206–688). Both head imports and the frame (§0) name the candidate's own draft-host `local--code/theme%3Ashattered-thoughts-jp/1` — the block that actually holds the stylesheet is the page's first (only) code block, so the address is correct in the FIX-CODEADDR sense. Asset URLs inside the CSS repoint from the original wiki's theme files to the candidate's own draft-host files: the container background (candidate lines 257–258, block B62), the sidebar diamond (lines 416–418, B79) and the interwiki diamond (lines 466–468, B81).

**Why.** Self-delivery from the candidate's own addresses prevents the port from hotlinking the original wiki's files at runtime (the render rows' runtime-hotlink family, KB-40, is charged against environment chains, not against a theme that still points at its origin wiki). Class (iii) draft form is the staging shape of the same rule.

**Verify.** `grep -n 'local--code' candidate.txt` (3 hits: lines 2, 8 and the usage exhibit's escaped form is wikitext, not CSS); brace-depth scan: both files end at depth 0 and never go negative.

**Disposition.** Standing class (iii); the T2/T3 render row's "runtime-hotlink site-theme chain only" is the environment layer's chain, recorded against this theme's row and dispositioned there.

### 4. Fonts and assets

**What.** The code block loads Open Sans from Google Fonts in both files. FIX5 item 28 added the JP half: a Noto Sans JP `@import` at the head of the candidate's code block (candidate line 211, block span JPFONT-LOAD) and `"Noto Sans JP"` suffixed into exactly three stacks — `body` (line 216), `#header h1 a::before` (line 238), `#header h2::before` (line 246). Every font stack in the candidate is the same three-name form `'Open Sans', "Noto Sans JP", sans-serif`; no stack names a font that is not loaded, and the loaded JP face is applied. The exhibit image was re-hosted: the original's image-block borrowed `exoplanet.jpg` from scp-3426's EN files (original line 56); the candidate's names the same file in the candidate's own draft-host files (candidate line 63). The CSS background and diamond images re-host the same way (§3).

**Why.** Pattern P7 / KB-16: a Latin-only stack renders Japanese text in fallback faces; the supplement pairs the load with the stack names so the JP face is both fetched and used. Re-hosting exhibit and CSS images into the candidate's own files is the campaign's asset rule (an image borrowed from another page's files breaks when that page's files move).

**Verify.** `sed -n '209,217p' candidate.txt`; `grep -n 'font-family' candidate.txt` (3 stacks, all the same form); `grep -n 'exoplanet' candidate.txt original.txt`.

**Disposition.** Item 28's closure is re-derived in §Per-theme record. The T3 render row's broken-image note (the capture names "explanet.png") stands as a deferred asset item (KB-58 family) in the render record; the candidate's own re-hosted copy is the port-side half of that record.

### 5. Page furniture (header, sidebar, topbar)

**What.** The theme's title and subtitle are CSS `content:` strings, and both were translated as the visible text they are: `content: "Shattered Thoughts"` → `「砕けた思考」` (candidate lines 236–237 region) and `content: "Broken Minds"` → `「壊れた心」` (lines 244–245). The credit block's タイトル/原題 fields keep "Shattered Thoughts Theme" — the work's name, quoted as a title, not display chrome. Two sidebar selectors gained the JP form in place: `#side-bar div.menu-item img` and `#interwiki.side-block.menu-item img` each acquired the parallel `> .image` alternative (candidate lines 416–418 and 466–468, blocks B79/B81, whose classifier labels record only the asset half). The extended form is the population's JP sidebar shape (29 candidate files carry `menu-item > .image`).

**Why.** KB-18: rendered strings are visible text and translate; a work's title in a credit field is a quotation, not chrome. The selector extension is an R6-shape in-place correction: the JP sidebar markup wraps menu icons in a `.image` element, so the original's bare `img` selector misses the node the rule exists to size.

**Verify.** `grep -n 'content: "' candidate.txt` in the header region; `sed -n '416,418p;466,468p' candidate.txt`.

**Disposition.** No item charged the header strings or the selectors; both stand in the PASS bytes.

### 6. Text translation

**What.** The documentation body and every exhibit are translated: the introduction and the link to the paradigm-shift article (block B9), the feature list, the tabview and collapsible specimens, and the repeated "I thought about" exhibit lines (blocks B31–B48), each carried into Japanese in place. One specimen was replaced rather than translated: the original's Lorem ipsum paragraph (original line 70) becomes a Japanese specimen paragraph exercising the same furniture (link, italic, bold, and the page's live footnote) at candidate line 77 — an R3-shape specimen replacement, since placeholder Latin has no content to translate. The live `[[footnote]]` and its `[[footnoteblock]]` survive as a pair (original lines 70/152 → candidate lines 77/159). CSS section-banner comments translate with the code (32 COMMENT-TEXT blocks; §Appendix).

**Why.** The body of a theme page is its documentation; an untranslated body fails the JP posting (KB-18). Comment translation is porter-visible hygiene (R1): the comments ship inside the delivered code block.

**Verify.** Read diff.md sections for blocks B21 (the specimen) and B31–B48; `grep -n 'footnoteblock' candidate.txt original.txt`.

**Disposition.** Translation mass is the port's core work; no item charged a mistranslation in this theme.

### 7. Links

**What.** The paradigm-shift link repoints to the JP host with a translated label (candidate: `[https://scp-jp.wikidot.com/paradigm-shift パラダイムシフト]`, block B9) — pattern P11, the JP counterpart exists. Links to scp-3426 stay on scp-wiki in the translated prose (blocks B10, B21, B52): the article is the theme's showcase target on the original wiki and no record charges the choice. The credit block's 元記事リンク names the original page on scp-wiki.wikidot.com, matching the host sources.tsv records (no host defect; no probe needed where the forms agree).

**Why.** P11's rule is counterpart-driven: repoint where the JP page exists, keep where the reference is the original itself.

**Verify.** `grep -n 'scp-3426\|paradigm-shift' candidate.txt`.

**Disposition.** Standing; uncharged.

### 8. Structure and exhibits

**What.** Component order is preserved end to end: head module, frame, gate, credit region, documentation exhibits, code block, gate close. No exhibit was dropped: the image-block exhibit, the tabview, the collapsibles and the text specimens all stand in the candidate at their original positions. The classifier's two EXHIBIT-RESTRUCTURE labels (B2, B14) are its forced call on exhibits whose include lines were repointed; adjudicated against the exhibit census, both exhibits survive in place and the label records the repoint, not a restructuring. The one genuine exhibit change is the Lorem ipsum replacement (§6).

**Why.** A theme page's exhibits are its usage documentation; dropping one silently removes the instructions the CSS exists for (the content-presence rule).

**Verify.** Compare the section sequence: `grep -n '^\+\|^++\|collapsible\|tabview' ` on both files.

**Disposition.** No structural item charged.

### 9. Formatting

**What.** Eleven WS-ONLY blocks: trailing spaces after selector commas in the original's CSS (e.g. `#header h1 a span,␣`) are stripped in the candidate. No re-indentation (the classifier's reindent count is 0) and no line-ending change.

**Why.** Whitespace-only normalization inside the delivered code block; it changes no rule.

**Verify.** `grep -c ' $' original.txt candidate.txt` over the CSS regions; the WS-ONLY spans in classification.json.

**Disposition.** Mechanical; uncharged.

### 10. Porter annotations

**What.** None. The candidate contains no `[!-- --]` comment and no prose note without an original counterpart; every comment in its code block is a translation of an original comment (§6, §Appendix). The FIX5 font import (§4) is a bare `@import` line with no annotation attached.

**Why.** The section exists so a reader can find the porter's own voice where it exists; here the port's decisions are recorded in the campaign records instead (the FIX5-FURNA lane record and the ledger supplement).

**Verify.** `grep -n '\[!--' candidate.txt` (no hits).

**Disposition.** Ground stated; nothing to disposition.

### 11. Cross-cutting dispositions

**What.** The standing records that touch this theme without being diff content: T1's five pseudo-ref errors are the class (iii) draft-host delivery addresses (§0, §3), dispositioned at register (c1). The T2/T3 render row records the runtime-hotlink site-theme chain (KB-40, the environment's chain, not this file's addresses), the sample's credit modal in preview form (KB-32 / ruling 5: expected in the check environment), an 884px overflow at 768px width on the sample page, and the broken exhibit image on the T3 capture (KB-58 deferred asset; §4). T4 recorded 3 display-affecting findings, judged jointly with T5.

**Why.** These are the campaign's environment-layer and check-form dispositions; restating them here keeps the package from re-charging what the registers already settled.

**Verify.** The verdict stamp above carries the row citations (T1-ROWS row 121; RENDER-ROWS-2 (RENDER-S2-D (EN19)); LOCALIZE-ROWS row 136).

**Disposition.** All standing items dispositioned in their registers; the two blocking items are §Per-theme record.

### 12. Verification

**What.** This package's own checks: original.txt SHA-256 equals the sources.tsv value (d2aaddd…23c, §Provenance); candidate.txt is byte-identical to the canonical candidate (`cmp` against `pages/theme:shattered-thoughts-jp.txt` in this repo); classification.json regenerates cleanly (`classify_hunks.py --check`); the FIX5 re-derivation below is checkable from the two files plus the cited commit. The campaign-side checks are the stamp's rows (T1 baseline 5 errors / 0 warns / 2 infos, all pseudo-ref class).

**Why.** A review package must let the reader re-run the cheapest deciding check from this repo alone; the hashes and the commit are those checks.

**Verify.** `sha256sum original.txt`; `cmp candidate.txt pages/theme:shattered-thoughts-jp.txt`; `python3 review/build_review.py --check`.

**Disposition.** PASS stands on the frozen ledger; this package adds no new charge.

## Per-theme record

**Ledger item 27 — class B (duplicate bare rate module).** The ledger (§(e) item 27, from LOCALIZE-S2-C) charged: a bare `[[module Rate]]` stood immediately after the preview credit block's `credit:end-preview` (ledger-time candidate line 25), duplicating the rate control the preview block already embeds (KB-09 shape). The FIX5 re-judgment (supplement, FIX5-FURNA) records it FIXED at commit 9e8931f. Re-derived from the bytes: `git show 9e8931f` removes exactly the four lines `[[>]]` / `[[module Rate]]` / `[[/>]]` / blank immediately after `[[include:scp-jp:credit:end-preview]]` and nothing else rate-shaped; the current candidate contains no `[[module Rate]]` (`grep -c` = 0). One distinction the reader should keep: the original itself carries a bare Rate in a `[[>]]` div at its lines 13–15 — that instance stood where the port's credit block now stands and was removed with the P3 swap region (block B5), a separate event from the FIX5 removal of the port's own duplicate. Closure holds.

**Ledger item 28 — class D (no JP font).** The ledger (§(e) item 28) charged: the candidate loaded and named no JP font at all (pattern P7 absent). The supplement records it FIXED at the same commit 9e8931f. Re-derived: that commit adds the Noto Sans JP `@import` at the head of the code block (now candidate line 211) and suffixes `"Noto Sans JP"` into the three stacks (now lines 216, 238, 246) — the classifier's JPFONT-LOAD and three JPFONT-STACK spans cover exactly those lines, and `grep -n 'font-family' candidate.txt` shows all three stacks in the supplemented form. Closure holds.

**The stamp's STALE cause.** Commit b5cb724 (the usage-example sweep) changed exactly one line of this file after the verdict bytes: candidate line 55, the escaped usage include completed from `theme:shattered-thoughts` to `:scp-jp:theme:shattered-thoughts-jp` (the form the sweep applied population-wide; §2). No other post-verdict change exists in the file's history.

## Change set outside the two diffed files

- The candidate's own attachments on the draft host: `exoplanet.jpg`, `diamondblue.png` and `shatteredthoughtsbackground_smaller.png`, re-hosted from the original wiki's files into `theme%3Ashattered-thoughts-jp`'s files (§3, §4). Their bytes live on the check wiki, not in this repo.
- `pages/theme-decoration-sample-shattered-thoughts-jp.txt` — the render-check sample the T2/T3 rows measured.

## Multi-wave provenance

| Commit | Wave | Change to this candidate |
|---|---|---|
| 765e2f8 | Stage 2 (EN19) integration | The port created: translation, credit block, delivery repoints |
| 666f543 | FIX2-CREDIT | Credit fields completed |
| 9e8931f | FIX5-FURNA | Items 27 and 28 repaired (§Per-theme record) |
| b5cb724 | Usage-example sweep | Line 55 posting-name completion (the stamp's STALE cause) |

## Appendix: residue and heuristic resolution

Residue blocks: 3 of 105. All three are CSS section-banner comment translations the classifier left unlabeled — `/* -=- IMAGES -=- */` → 画像 (original lines 521–522 → candidate 529–530), TABLES → 表 (527–528 → 535–536), FOOTNOTES → 脚注 (640–641 → 648–649). Shape: COMMENT-TEXT (R1, porter-visible comment translation), the same class as the 32 labeled COMMENT-TEXT blocks; resolved here so the residue count is explained, not waived.

Heuristic mass: 62 of 105 blocks carry heuristic primaries. Their spans are TRANS-UNANCHORED (63 spans: prose and exhibit translation without a shared anchor token; §6) and COMMENT-TEXT (32 spans: CSS comment translation; R1). Both shapes are the expected heuristic population for a translated theme whose code comments were carried and translated; no heuristic block hides a delivery, credit or font change — those all carry specific signatures (§1, §3, §4).
