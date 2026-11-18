# Review package — theme:kcia10-jp (KO → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:kcia10-jp — origin KO, population #270 [GOSIGN2-LEDGER (b) row 270]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 307ed123078ecb34bba945ad348cd1b03db748aa2275f2ed291d38b55773607e); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 4 warns / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 274; GOSIGN2-LEDGER (b) row 270]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample credit-modal (preview-form) + page-overflow 532–537px@320/375 + 884px@768; page runtime-hotlink site-theme chain only; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 269, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 269]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 270]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:kcia10-jp.txt sha256:307ed123078ecb34bba945ad348cd1b03db748aa2275f2ed291d38b55773607e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** at the ledger determination (GOSIGN2-LEDGER (b) row 270); the stamp above reads **STALE** because the candidate was repaired after that verdict (commit 2a8a125, the source-link host correction), and the stamp does not carry a verdict onto changed bytes |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (ii), section 11); the render row's items (KB-33/KB-34/KB-40, section 11); T4's type-11 unannotated KO links (P11 DISPOSITIONED, section 7) |
| Repaired after verdict | T4's type-3 finding, the broken credit source link: repaired in 2a8a125 (see the per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:kcia10 | theme:kcia10-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 161 (first translation; the candidate's credit block records 初訳時参照リビジョン: 161) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-kcia10.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:kcia10-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 645 lines / 13,313 bytes | 656 lines / 14,318 bytes |
| SHA-256 | d7d3e2badf50a32aa8216a29fcc1570ce8f251808a37f6acb30ef4106e62b257 | 1f1cb08f242192004d02aff737fd36e5b0d538107358d9d2f20aa42795912052 |

Wave history: the candidate was created by the Stage 2 KO5 integration (commit 3c781b1, the LOCALIZE-S2-F wave's port), then touched by FIX-CREDIT-D (1869877, the translator-attribution normalization), and finally by the post-verdict repair 2a8a125 (the source-link host correction, per-theme record). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A standard KO port by the same porter as theme:jiha (thd-glasses), with the same shape: the credit furniture swaps to the JP preview credit block, delivery rebuilds as the wave-standard frame on the draft host, the Korean webfonts are deleted and replaced by a Google Fonts load with JP stacks, and the usage body is translated in both its Korean and English halves. Measured churn (diff.md, the generator's difflib count with autojunk off: +76/−66, 142 changed lines in 24 change blocks / 7 diff hunks). Two things distinguish it from jiha: the source-code exhibit gains a collapsible wrapper the original does not have (section 8, adjudicated there), and this candidate is one of the five repaired in 2a8a125 after T4 found its credit source link pointing at the KO branch's dead old host (per-theme record). That repair is why the verdict stamp reads STALE: the PASS was computed against the pre-repair bytes.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 24 change blocks — 13 specific (54.2%), 9 heuristic (37.5%), 2 residue (8.3%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 7 |
| CSS-BODY | 5 |
| TRANSLATION-ANCHORED | 4 |
| DRAFT-HOST | 3 |
| COMMENT-TEXT | 2 |
| IFTAGS | 2 |
| INFO-DEL | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| RESTORATION | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 5 heuristic CSS-BODY blocks are all P7 font-stack rewrites (section 4); the 2 COMMENT-TEXT blocks are in-CSS text translations, R1 (section 6); the block the classifier primaries as RESTORATION (B24) is the appended T7 credit-correction module, not a restoration (sections 1 and 10); the 2 residue blocks are tail alignment produced by the added exhibit closers (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:kcia10-jp; original theme:kcia10 on scpko at reference revision 161; candidate `pages/theme:kcia10-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved as in jiha: the original opens with its delivery module (original L1–3) and then its tag gate `[[iftags +테마]]` (original L5); the candidate opens with the delivery module and the interwiki-style frame (candidate L1–8) and places the localized gate `[[iftags +テーマ]]` after it (candidate L10).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for kcia10-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a `[[>]]`-wrapped bare `[[module Rate]]` (original L7–9) plus an `info:start`/`end` pair (original L11–31) whose body carries the credit prose in Korean: the title, the author (제작: thd-glasses), the all-images note, and the logo note. The candidate deletes both (blocks B3, B4, B8) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–21) carrying the eight ruling-3 fields (title 中央情報部第十局テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 중앙정보부 제10국 테마; 著作権者 thd-glasses; 作成年 2020; 初訳時参照リビジョン 161; the source link, on which see the per-theme record). The author field was checked against the original's credit: the info block names thd-glasses as maker, the images note names the same author, and no second creator or co-author appears anywhere in the original — the field drops nobody. The info block's non-credit content survives as body prose directly below (candidate L23–29): the images note and logo note translated, and a JP fonts-used list that replaces the original's font prose (section 4). The section's CSS half is the appended tail module (candidate L647–656, block B24): the credit-button rules restated for the JP credit module's DOM (see section 10 for its comment). The candidate also keeps the original's own in-body `.creditButton p a` rules (candidate L113, L342, L347, matching original L118, L347, L352) — the appended module corrects the anchor's parentage for the JP module without editing the inherited rules.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become), and the info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields and the translator credit form; FIX-CREDIT-D (1869877) is that form arriving (翻訳責任者 normalized to AI). T7 (KB-11/KB-12): the KO theme styles the credit anchor through a `<p>` wrapper (`.creditButton p a`), but the JP credit module emits the anchor as a direct child of `.creditButton`, so the rules are restated against the JP structure with their declarations unchanged — the R6 correction delivered as an appended module.
- **Verify:** `grep -n 'info:start\|info:end\|module Rate' candidate.txt` returns nothing; read candidate L12–21 against the eight fields; `grep -n 'creditButton' candidate.txt` shows the inherited rules and the appended restatement.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified). The source-link field is the item T4 flagged and 2a8a125 repaired; it is carried openly in section 11 and the per-theme record.

### 2. Includes and components

- **What:** One repoint class, in the usage exhibits: the include a user pastes, `:scpko:theme:kcia10` → `:scp-jp:theme:kcia10`, in both usage sections (original L36 and L42 → candidate L44 and L50; block B9 covers the first, the second rides in B10's range). The credit includes (section 1) and the interwiki-style include (section 3) complete the candidate's include list; every include in the candidate names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; a kept `:scpko:` include is a foreign-include error, class (i), and the theme's own JP page is the counterpart, so it is repointed and no exception is needed. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — all targets `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS by one live self-import from scpko.wdfiles.com: `local--code/theme%3Akcia10/0` in the head module (original L2). The candidate replaces it with the wave-standard frame (candidate L1–8, blocks B1–B2): a `[[module CSS]]` importing the candidate's own `local--code/theme%3Akcia10-jp/1` from the draft host (candidate L2), and an interwiki-style include at priority 1 with `theme=` naming the same /1 delivery (candidate L4–8). The single-index frame is the producing wave's convention, not a per-theme omission: the sibling KO candidates carry the identical /1 frame (theme:jiha-jp, theme:bulgunae-jp, theme:chatscp-jp in `pages/`), and this theme's T2/T3 record reports no unstyled-content finding. Topology check: the original imports its base (Sigma-9 lineage) through the site theme chain and carries its own CSS in one code block; the candidate does the same — no base stylesheet is inlined on either side (the candidate's code block is 584 lines against the original's 600, and the overlap question that arises for inlined bases does not arise here).
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame, priority 1 for the theme's own layer). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L2 and L6 live lines, both draft host; compare the sibling heads in `pages/`.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Load (blocks B11, B13): the original loads its Korean faces inside the code block — a protocol-relative earlyaccess import for Nanum Myeongjo (original L53) and `@font-face` blocks for locus_sangsang and others served from cdn.jsdelivr.net's noonfonts (original L55–72). All of that is deleted, and the candidate loads four families in one Google Fonts `@import` at the head of its code block (candidate L59): Nanum Myeongjo (kept — it serves the retained Korean strings and the serif stacks), Noto Sans JP, Noto Serif JP, and Klee One. Stacks (the 5 CSS-BODY blocks B16–B18, B20, B21, adjudicated to this section): `--font: 'locus_sangsang'` → `'Noto Sans JP'` (candidate L81); `'ChosunGu'` → `'Noto Sans JP'` (candidate L97); `"Nanum Gothic"` → `'Noto Sans JP'` inside the verdana stack (candidate L106); `'Merriweather', 'Nanum Myeongjo'` → `'Noto Serif JP', 'Nanum Myeongjo'` (candidate L231 — the Latin serif is replaced, the Korean serif kept); `'BBTreeCB'` → `'Klee One', sans-serif` (candidate L503). Assets: the header image URL moves from `scpko.wdfiles.com/local--files/theme%3Akcia10/kcia10_title.png` to the draft host's `theme%3Akcia10-jp` folder with the file name unchanged (candidate L201, the DRAFT-HOST span inside B19's range).
- **Why:** P7/T5 with KB-16 (the font load gap): the KO display faces cannot render Japanese text, so the load and every stack that names them change together; Noto Serif JP takes Merriweather's serif role and Klee One takes the hand-written display role BBTreeCB held. P5 with KB-17 (asset hosts): the theme's own image is re-hosted to the JP side; the jsdelivr font loads disappear because the faces they served are gone, not as a separate host fix.
- **Verify:** `grep -n 'font-family\|--font' candidate.txt` — the five rewritten lines above, no locus_sangsang, ChosunGu, Nanum Gothic, or BBTreeCB; `grep -n 'wdfiles' candidate.txt` against the asset line.
- **Disposition:** Font load and stacks applied; the draft-host asset URL is DISPOSITIONED (class (iii) draft form; posting rewrites it to the production host).

### 5. Header, sidebar, and site furniture

- **What:** None — no signature for this section fired over 24 change blocks, and the bytes confirm it: the candidate sets no `--header-title`, `--header-subtitle`, or `--logo-image` (the header image travels as a background URL, host-repointed in section 4), and its sidebar and topbar rules are carried over unmodified apart from the font lines of section 4. No P8 layout adaptation was needed: the candidate inherits the JP site furniture through the frame.
- **Why:** P9/T6 not engaged (the theme does not override the header variables); KB-57 and ruling 2 are likewise not engaged.
- **Verify:** `grep -n -- '--header-\|--logo-image' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 6. Text translation

- **What:** The body is translated throughout, in both of the original's language halves. The original carries its usage text twice, Korean first and then an English rendering (original L33–43); the candidate carries it twice too, both times in Japanese (candidate L40–50), so the port translates two source texts into one language pair of sections. Anchored blocks (B5, B7, B9, B14): the credit-adjacent prose lines, the usage lines, and one CSS-side pair. Unanchored blocks (B6, B10, and the prose inside B3/B4/B8): the fonts-used heading and list (B6: the `@@@@` separator line gives way to the **使用フォント（SCP-JP 版）** heading, candidate L27), the two usage sections (B10), each verified against the mirror for this README. In-CSS text (R1, the 2 COMMENT-TEXT blocks): B12, the code block's title comment (중앙정보부 제10국 CSS 테마 → 中央情報部第十局CSSテーマ, candidate L61), and B15, a section comment (/* EN translation → /* 英語版の表記, candidate L77) — porter-visible text, translated with the file. Korean survives in the candidate where it is quotation or retained credit: the credit block's original-title field (candidate L16), the porter comment's quoted theme name (candidate L58, section 10), and the Nanum Myeongjo stack names (section 4). R5 glyph-form conversion: none — the source is Korean; no retained string changes glyph form (the title comment's 第十局 is the translation's own kanji, not a converted retention).
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings); R1 names the in-CSS half (comments and the banner title), which KB-18's reader-visible scope does not cover but the port translates anyway.
- **Verify:** The pairs are diff.md's body sections in order; a Hangul scan of candidate.txt returns only the quotation and credit lines named above.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the named quotations.

### 7. Links

- **What:** Two live prose links point at scpko pages, both translated in text and both serving: the author's hub link (candidate L34: `[*https://scpko.wikidot.com/thd-glasses-hub thd-glassesの作品をもっと見る]`, from the original's `[[[thd-glasses-hub|...]]]` inside the info block) and the hub-page link in the usage text (candidate L41: `[*https://scpko.wikidot.com/kcia10 中央情報部第十局]`). These are T4's type-11 finding (unannotated KO hyperlinks ×2): the links work and name the right pages, but nothing on the page tells a JP reader they lead to the KO wiki. The candidate's third scpko link is the credit block's source link (candidate L20), which is the repaired item of the per-theme record, not part of this finding. No prose link in the candidate targets a dead host.
- **Why:** P11: prose links take the JP counterpart or the serving original; neither linked page has a JP counterpart (the author's hub and the branch hub page are KO-side pages), so the serving original is the right target, and the missing piece is the annotation, which the ledger dispositions as a sibling/batch-posting matter rather than a per-theme fix.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — L20 (credit source link), L34, L41, and the porter comment at L58.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P11 DISPOSITIONED, sibling / batch-posting class).

### 8. Structure

- **What:** One real structural change, adjudicated here: the candidate wraps its source-code exhibit in a collapsible the original does not have. The original presents the code directly after the usage sections (original L44, `[[code type="CSS"]]`); the candidate inserts a `+ ソースコード` heading and a `[[collapsible show="+ 展開" hide="- 折り畳む"]]` / `[[<]]` wrapper (candidate L52–55, inside block B10's range) whose closers land at the file's tail (candidate L642–643, inside residue block B23). The exhibit census decides what kind of change this is: the code block itself is present on both sides with its full content (600 original lines → 584 candidate lines, the delta being the font deletions of section 4), nothing inside the wrapper was dropped or replaced, and the collapsible's labels are translated. So this is an R3 exhibit-form change (a presentation wrapper added around a complete exhibit), not a class I deletion: the R3 question — sanctioned replacement vs silent deletion — resolves to neither, because nothing was replaced or deleted; a wrapper was added. Everything else about the structure follows the closing rule: variable names, selectors, and channel order are preserved, the candidate's one code block sits where the original's sits, and the JP corrections arrive as the head frame (section 3) and the appended tail module (section 1), not interleaved into the inherited CSS.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape; here the census, not the label, decides. The wrapper's cost is real and recorded: the exhibit is folded by default where the original shows it open.
- **Verify:** `grep -n 'collapsible\|\[\[code' original.txt candidate.txt` — the opener exists only in the candidate; compare the code blocks' contents in diff.md.
- **Disposition:** Standing as an exhibit-form change, recorded here; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a class of its own: the classifier finds no whitespace-only block pair and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered. The only formatting-level additions are the blank lines around the added exhibit closers at the tail (appendix, B22/B23), which belong to section 8's wrapper, not to formatting churn.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here there is none to disclose.
- **Verify:** Section 9 of the skeleton classification (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotations, both CSS comments with no original counterpart. (1) Candidate L58, at the head of the code block: the port provenance comment, naming the theme, the original's URL, and revision 161; it rides inside B13's font-load range, which is why no separate annotation signature fired. Its URL is the post-repair form (scpko.wikidot.com) — the repair commit rewrote this line together with the credit source link (per-theme record). (2) Candidate L648, in the appended tail module: the credit-correction comment, explaining that the KO theme styles the credit anchor through a `<p>` wrapper while the JP credit module emits the anchor as a direct child, and that the declarations are unchanged (the rule it introduces is section 1's T7 restatement). The skeleton's "none" for this section does not survive contact with the bytes and is corrected here.
- **Why:** R2: porter-added text is part of the change record, and annotation (2) is load-bearing — it is the only in-file explanation of why the tail module exists.
- **Verify:** Read candidate L58 and L648.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's two pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host local--code lines (section 3); the posting procedure rewrites them, and fix lanes never "fix" them in the candidate. (2) The render row's items, all cross-cutting families, not charged to the candidate: the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); the page-overflow readings 532–537px at 320/375 and 884px at 768 (KB-33/KB-34: the static credit replica's fixed width and the preview chrome, the campaign-wide shapes); and the page's runtime-hotlink site-theme chain (KB-40). (3) T4's type-11 finding, the two unannotated KO links: DISPOSITIONED as a sibling/batch-posting matter (section 7). (4) T4's type-3 finding, the credit source link: the one item in this theme that was a real defect in the candidate; it is repaired, and the repair is what makes the stamp STALE (per-theme record). The ledger's determination for this theme is PASS and this package does not re-open it; the STALE stamp is the documentation doing its job, because the bytes the verdict judged are no longer the bytes on file.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 repaired post-verdict (2a8a125).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 274): exit 1, 2 errors / 4 warns / 1 info; both errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO5)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 269): FINDINGS jointly, display-affecting findings 2 (the source link, type 3; the unannotated KO links, type 11), no display-collapse item; the ledger §(c3) line records the theme's T4 outcome as the P3 credit fields FIXED by the credit waves and P11 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +76/−66 in 24 change blocks / 7 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:kcia10-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS at the ledger determination (GOSIGN2-LEDGER (b) row 270; go-sign, COMPLETION-REPORT §10); the stamp's STALE state records the post-verdict repair.

## Per-theme record

### The source link (T4's type-3 finding, repaired in 2a8a125)

LOCALIZE-ROWS row 269 records two display-affecting findings for this theme; the first is type 3, 元記事リンク破損 — the source-article link is broken. The bytes at the FIX5 head bore it out: candidate L20's credit source link and the porter comment at L58 both named `scp-wiki-ko.wikidot.com`, the KO branch's old host. Probe evidence (made for the jiha package, 2026-11-17, and covering this theme as one of the five): `https://scpko.wikidot.com/theme:kcia10` returns 200 and serves the original page whose content matches this package's mirror; `https://scp-wiki-ko.wikidot.com/theme:kcia10` returns 404. The campaign's own provenance records (review/sources.tsv, the mirror store index) name scpko.wikidot.com as the original's host. The candidate file's history shows why no wave repaired it before the review pass: the KO5 integration (3c781b1) set the link in the old-host form, FIX-CREDIT-D (1869877) touched only the translator field, and the theme had no FIX5 item. The repair landed as canonical commit 2a8a125, which makes the one-word host correction (scp-wiki-ko → scpko) in both places, in this candidate and in the four sibling candidates carrying the same defect (theme:jiha-jp, theme:minimal-scp-foundation-by-cocoonist-jp, theme:legend-of-blue-jp, theme:king-s-palace-jp), each probed the same way (old host 404, scpko 200). This package documents the corrected candidate; its diff is computed against the corrected bytes, and its stamp reads STALE because the go-sign verdict was computed against the pre-repair file, not the current one (sha256 1f1cb08f…, named in the stamp).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-kcia10-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## Appendix — residue blocks

For class M the residue blocks are resolved here in one table rather than as per-block slots. Both of this theme's residue blocks sit at the file tail and are alignment artefacts of section 8's exhibit wrapper, not content changes.

| Block | Position | Resolution |
|---|---|---|
| B22 | orig at 644 → cand 639–639 (body → code-css) | The last CSS line / blank-line alignment where the original's `[[/code]]` (original L644) meets the candidate's re-flowed tail (candidate L639–641). No line's content changes; the shift is the knock-on of the font deletions above it. Counted in section 8's tail, not a change class of its own. |
| B23 | orig at 645 → cand 641–644 (body → body) | The candidate's added exhibit closers (`[[/<]]`, `[[/collapsible]]`, candidate L642–643) plus the `[[/iftags]]` line realigning around them. This is the closing half of section 8's collapsible wrapper; the opener half is in B10. No original line is removed. |

## License and attribution

- **Title:** 중앙정보부 제10국 테마
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/theme:kcia10 — revision 161
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
