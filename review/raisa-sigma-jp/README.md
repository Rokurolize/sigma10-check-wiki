# Review package — theme:raisa-sigma-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:raisa-sigma-jp — origin EN, population #129 [GOSIGN2-LEDGER (b) row 129]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 129]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 0 warns / 1 info (hotlink×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 154; GOSIGN2-LEDGER (b) row 129]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page T2 no machine verdict (exit 2); sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 129, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 129]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 129]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:raisa-sigma-jp.txt sha256:eeebef0f02b53034ffd97dd2d51aa076a6fa6361195d89385c583453443dfbd2; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 129) |
| Standing items | **DISPOSITIONED** — the theme's two EN-hosted asset references stand under the deferred-asset disposition (P5, class (ii) / KB-58, section 4, stated plainly there and in the per-theme record); the base-theme prose link stands under the sibling disposition (P11, section 7); the T1 pseudo-ref is draft form (class (iii)); the render row's page side returned no verdict (exit 2, a capture-layer item, section 12). No defect is flagged for this theme; one porter-added line is recorded in section 10 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:raisa-sigma | theme:raisa-sigma-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 13 (first translation; the candidate's credit block records 初訳時参照リビジョン: 13) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-render-s2-2/mirrors/raisa-sigma.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:raisa-sigma-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 716 lines / 20,574 bytes | 725 lines / 22,750 bytes |
| SHA-256 | 78188b2bb976fee73044a8f0eb590cea90a364a9181ac3c167b547fdf74d8da4 | eeebef0f02b53034ffd97dd2d51aa076a6fa6361195d89385c583453443dfbd2 |

Wave history: the candidate was created by the Stage 2 EN17 integration (commit b17d7e4, the RENDER-S2-2 wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose raisa-sigma hunk is the translator-field normalization. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. The diff for this pair is Tier 2 (diff.md, 26 diff sections): the classifier's 103 blocks are the unit the sections below cite.

## Summary

A Sigma-9 skin of the RAISA Black Highlighter theme: one large stylesheet (594 lines) with a records-office aesthetic, delivered by a head module ahead of the gate. The port replaces the original's bare Rate exhibit with the preview credit block, migrates the font loads from bunny.net to Google Fonts and adds the Noto Sans JP load with its 24 stack insertions (the P7 arrangement, documented by a porter-added note after the code exhibit), translates the header content strings and the prose, extends one interwiki selector group, and repoints the delivery to the candidate's own draft-host /1. Two asset references stay on the EN wiki's file area — the page background and the exhibit logo — charged display-affecting and dispositioned, not re-hosted (P5, KB-58); section 4 names them plainly.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 103 change blocks — 48 specific (46.6%), 48 heuristic (46.6%), 7 residue (6.8%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 48 |
| COMMENT-TEXT | 25 |
| JPFONT-STACK | 24 |
| TRANSLATION-ANCHORED | 19 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| SELF-DELIVERY | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| INCLUDE-REPOINT | 2 |
| CONTENT-STRING | 2 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| COMPONENT-SWAP | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 24 JPFONT-STACK blocks are the P7 stack insertions of section 4 (one of them, B44, sits in the body's font exhibit spans), and the single CSS-BODY block is the interwiki selector supplement of section 5. The two EXHIBIT-RESTRUCTURE blocks are a frame repoint (B2) and the image-block exhibit's caption/URL line (B11). The seven residue blocks are all heading or comment translations (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:raisa-sigma-jp; original theme:raisa-sigma on scp-wiki at reference revision 13; candidate `pages/theme:raisa-sigma-jp.txt`. Provenance route: derived from the original at the reference revision by the RENDER-S2-2 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). Both files open with the delivery module and frame ahead of the tag gate, and the gate localizes inside the credit conversion block (block B4: `[[iftags +theme]]` → `[[iftags +テーマ]]`, candidate L10).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization).
- **Verify:** The sources.tsv row for raisa-sigma-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is P2, applied.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare rating exhibit: a right-aligned `[[module rate]]` under a "Rating:" heading (original L11–14). The candidate deletes it and installs the preview credit block at the head of the gated body (candidate L11–20, block B4): the eight ruling-3 fields （タイトル RAISA Sigma-9テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 RAISA Sigma-9 Theme; 著作権者 macro_au_micro; 作成年 2024; 初訳時参照リビジョン 13; the source link, host-verified in section 7). The base-work credit stands where the original puts it, in the intro sentence: the theme is "based on the RAISA Black Highlighter CSS Theme", carried translated with its link made absolute (candidate L24, section 7) — the base is credited, not dropped. There is no license box on the original and no T7 credit CSS on either side (zero credit-rule lines in both files; the theme's credit styling is its own base arrangement).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, replacing the bare exhibit rather than accumulating beside it (the class C / KB-10 shape). Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module rate' candidate.txt` returns nothing; read candidate L11–20 against the eight fields.
- **Disposition:** Applied (no ledger P3 item stands for this theme; the FIX-CREDIT-D commit normalized the translator field as part of the population wave).

### 2. Includes and components

- **What:** Three include events besides the credit pair. The head frame is repointed to `:scp-jp:component:interwiki-style` (block B2, candidate L5). The usage exhibit (block B8, the COMPONENT-SWAP primary) repoints `@@[[include :scp-wiki:theme:raisa-sigma]]@@` → `@@[[include theme:raisa-sigma-jp]]@@` (candidate L29): the unprefixed same-site form naming the candidate's real posting name — the correct-name form, not the plain-slug defect family. The examples exhibit keeps its unprefixed `[[include component:image-block ...]]` (candidate L38, block B11) with the caption translated (RAISAテーマ）; the component resolves on scp-jp, and the image it displays is section 4's item.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. Ruling 4 is not engaged: the base theme is credited by link (section 7); its stylesheet is not a component this theme includes — the candidate's CSS is self-contained, as the original's is.
- **Verify:** `grep -n '\[\[include' candidate.txt` — frame (L5), credit pair (L11, L20), image-block (L38), and the escaped exhibit (L29).
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The topology is preserved (the classifier's pass: a head module plus the code exhibit on each side, no moves). The original's delivery is external-form: its module imports its own /1 from the wiki domain itself, `https://scp-wiki.wikidot.com/local--code/theme:raisa-sigma/1` (original L2; the topology pass records `external_own_delivery: true`). The candidate normalizes the same self-delivery to the standard form: `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Araisa-sigma-jp/1` (candidate L2, block B1), with the frame at priority 1 naming the same delivery (candidate L5–8, block B3). The CSS is the code exhibit on both sides (594 → 595 lines; the one added line is inside the font-load block, section 4).
- **Why:** P4/T9 and P6/T3: a theme's live channel in the JP environment is its own local--code delivery framed by interwiki-style; the candidate's form is the population's, and the draft host is KB-41, class (iii).
- **Verify:** `sed -n '1,8p' candidate.txt` against original L1–8 — one import, one frame, same order.
- **Disposition:** DISPOSITIONED (draft-host form, class (iii)).

### 4. Fonts and assets

- **What:** Fonts (P7, the theme's largest class): the load migrates hosts and gains the JP face (block B47: original L132–133 → candidate L138–140). The original loads PT Mono and Share Tech Mono from bunny.net in the retired `css?family=` grammar plus Oxanium from a bunny css2 URL; the candidate loads all three from Google Fonts css2 and adds `Noto Sans JP:wght@400;700`. The 24 JPFONT-STACK blocks insert `'Noto Sans JP'` into the stacks behind the Latin faces — in the CSS (e.g. `'Share Tech Mono', 'Noto Sans JP', monospace` at candidate L186) and in the body's three font exhibit spans (block B44, candidate L119–121), so the documentation demonstrates the stacks the code declares. Every named face is loaded: PT Mono, Share Tech Mono, and Oxanium from the Google imports, Noto Sans JP from its own. Assets: two references stay on the EN wiki's file area. The page background (candidate L170): `url(https://scp-wiki.wdfiles.com/local--files/theme%3Araisa-sigma/raisabg.png)`. The exhibit logo (candidate L38): the original's bare relative `name=raisa-logo-vs2.svg` is made absolute against the base theme's file area, `https://scp-wiki.wdfiles.com/local--files/theme%3Araisa/raisa-logo-vs2.svg`. These are the localize check's pattern-5 charges (its L170 live CSS and L38 body image-block, the background named explicitly), recorded display-affecting, and the ledger's answer is a disposition, not a re-host: P5 DISPOSITIONED, class (ii) / KB-58 deferred assets.
- **Why:** P7 (KB-16): Japanese text must not fall back to a platform default for want of a named JP family; here the family is both named in every stack and loaded. The load's host migration follows the population's settled form (bunny.net's split grammars are the fragile half of the original arrangement). P5's re-hosting rule is the default for assets; KB-58 records the deferred class where the original file area keeps serving, which is where these two references stand — stated plainly here rather than absorbed into the disposition.
- **Verify:** `grep -n '@import' candidate.txt` — three Google Fonts lines at L138–140 plus the delivery import at L2; `grep -n 'scp-wiki.wdfiles' candidate.txt` — exactly the two asset loci named above.
- **Disposition:** DISPOSITIONED (assets, P5 class (ii) / KB-58); the font arrangement is applied, and the porter note of section 10 documents it in the candidate itself.

### 5. Header, sidebar, and site furniture

- **What:** No header variables exist on either side. The header furniture is two CSS content strings, both translated (blocks B49, B52): `content: "RAISA ARCHIVE"` → `"RAISAアーカイブ"` (candidate L183) and `content: "Records And Information Security Administration"` → `"記録・情報保安管理局"` (candidate L200) — the acronym's expansion rendered in its official Japanese form. The one CSS-BODY block (B66, candidate L355) is a P6 selector supplement: `#interwiki .menu-item img` is extended to `#interwiki .menu-item img, #interwiki .menu-item > .image, #side-bar .side-block .menu-item > .image`, widening the menu-item image coverage across the two sidebars' shapes; the declarations under it are the original's.
- **Why:** P8 (KB-19) for the rendered strings: they are what a reader sees in the header zone, and both are genuine prose (an archive name and an administration name), not proper-noun marks to carry. P6 for the selector supplement, as in section 5 of the queen-s-gambit package.
- **Verify:** `grep -n 'content: "' candidate.txt` — the two translated strings; read candidate L355 against original L348.
- **Disposition:** Applied.

### 6. Text translation

- **What:** The prose is translated throughout: the usage section, the backlinks instructions, the examples' explanatory text, the font exhibit sentences (block B44), and the headings (two of the residue blocks are headings: 使用方法， 例）. The CSS comments are translated as a class (25 COMMENT-TEXT blocks), including the section banners （ヘッダー at candidate L168 and its kin). The anchored blocks (19) were verified line by line; the unanchored mass (48) is single-line prose and comment translation of the same shapes, with no content class dropped (the census in section 8).
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings); CSS comments are porter-visible only (R1's comment half), counted as a class.
- **Verify:** The pairs are diff.md's body and code sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit block's source link (candidate L19) names `https://scp-wiki.wikidot.com/theme:raisa-sigma` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered; its label is the theme's English title rather than the word ソース, a T5 joint-note shape, not a defect. The base-theme link (block B6: original L18 → candidate L24): the original's same-site `[[[theme:raisa|RAISA Black Highlighter CSS Theme]]]` becomes an absolute URL link `[[[https://scp-wiki.wikidot.com/theme:raisa|RAISA Black Highlighter CSSテーマ]]]` — from scp-jp, the same-site form would name a page that is not the base work, so the port names the base where it lives. This is the localize check's pattern-11 family (sibling links), dispositioned in the ledger (P11, sibling / batch-posting class).
- **Why:** P11: a provenance link's job is to reach the work it credits; the absolute original is the serving target, and the sibling/batch-posting disposition records the choice for the population of base-crediting links.
- **Verify:** `grep -n 'theme:raisa' candidate.txt` — the credit source link (L19) and the base link (L24), both absolute scp-wiki URLs.
- **Disposition:** DISPOSITIONED (P11; GOSIGN2-LEDGER §(c3)).

### 8. Structure

- **What:** The exhibit census corresponds: usage section, examples (image-block, headings, font spans), and the code exhibit are present on both sides in the same order. The named conversions are the rating exhibit's replacement by the credit block (section 1) and the porter's font note added after the code exhibit (section 10). Selector and variable names inside the CSS are preserved apart from the section 5 supplement.
- **Why:** R3: the census is what separates a conversion (this theme) from a silent restructure or drop (the failure class I charges); here every original region has a named candidate counterpart.
- **Verify:** Compare the heading and include sequences of the two files — they correspond at the loci named in sections 1–4.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0) in this pair.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (no WS-ONLY label).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter-added line, and it is recorded here rather than passed over: after the code exhibit, the candidate adds a font note with no original counterpart (block B103, candidate L723): "**フォント:** 使用している欧文・和文書体はいずれもGoogle Fontsで配信されるオープンライセンスの書体です（SIL Open Font License など）。日本語文字はNoto Sans JPにフォールバックします。" The note is accurate against section 4's bytes (the loads are Google Fonts; the stacks do fall back to Noto Sans JP) and functions as the port's own documentation of its P7 arrangement. No `[!-- ... --]` comment exists in the candidate.
- **Why:** R2: porter-added text is part of the change record, in whatever form it takes; a prose note is an annotation for this section's purposes exactly as a bracket comment would be.
- **Verify:** `sed -n '722,725p' candidate.txt` — the note between `[[/code]]` and `[[/iftags]]`; original L715–716 has no counterpart line.
- **Disposition:** Standing (recorded; the note's content is verified accurate).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two hotlink errors: class (ii) — the section 4 assets standing under the KB-58 deferred-asset disposition. (2) T1's one pseudo-ref error: class (iii), the draft-host delivery of section 3. (3) The render row's items: the sample's credit-modal errors (KB-32, ruling 5) and 884px@768 overflow (KB-33/KB-34 families), the runtime-hotlink site-theme chain (KB-40, environment layer), and the page side's exit 2, which is a capture failure, not a finding (section 12). T4's two charges close as: pattern 5 DISPOSITIONED (section 4), pattern 11 DISPOSITIONED (section 7).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 154): exit 1, 3 errors / 0 warns / 1 info; the errors are hotlink ×2 and pseudo-ref ×1, all in the dispositioned classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-2 (EN17)): FINDINGS on the sample side (section 11(3)); the theme page's own capture returned exit 2 — no machine verdict was produced for the page, a coverage caveat of the capture layer (the KB-44 family), not a defect found in the candidate; the ledger's determination rests on the sample and the source-side checks. (c) T4/T5 (LOCALIZE-ROWS row 129): FINDINGS jointly, display-affecting findings 2 (the pattern-5 asset family, counted with its two loci); the ledger §(c3) line records the theme's T4 outcome as P5 and P11 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +129/−120 in 103 classifier change blocks / 26 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance; an exit-2 capture is reported as the absence of a verdict, never as a pass.
- **Verify:** Re-run the checker on `pages/theme:raisa-sigma-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 129; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The EN-hosted assets stand by disposition, stated plainly

Section 4 records the two URLs; this note exists so the disposition is not misread as a repair. The localize check charged the pattern-5 family as display-affecting — the theme's page background (raisabg.png) and its exhibit logo both load from the EN wiki's file area in the candidate as it stands, the logo resolved against the base theme's (theme:raisa's) file area — and the ledger dispositions the family (P5, class (ii) / KB-58) rather than fixing it. The candidate therefore depends on the original wiki's file area at render time, by recorded decision. If that decision is ever revisited, the two loci are candidate L38 and L170.

### Record note — the vendored LOCALIZE row truncates the pattern-11 charge

The vendored LOCALIZE-ROWS copy of this theme's row ends its pattern-11 item at "L24 …", so the charge's full text is not recoverable from the record. The bytes govern: candidate L24 is the base-theme link of section 7, in the absolute form the disposition contemplates, and the ledger's §(c3) line dispositions P11 without qualification.

## Appendix — residue blocks

Seven blocks, one shape family (heading and comment translation the aligner left unlabeled), resolved here by shape rather than line by line:

| Block | Span | Resolution |
|---|---|---|
| B5 | orig 16-16 → cand 22-22 | Heading translation: `+ Usage` → `+ 使用方法`. |
| B10 | orig 30-30 → cand 36-36 | Heading translation: `+ Examples` → `+ 例`. |
| B68 | orig 365-365 → cand 372-372 | CSS section comment: `/* BODY */` → `/* 本文 */`. |
| B75 | orig 389-389 → cand 396-396 | CSS section comment: `/* BARS */` → `/* 線 */`. |
| B77 | orig 416-416 → cand 423-423 | CSS section comment: `/* FOOTNOTES */` → `/* 脚注 */`. |
| B89 | orig 553-553 → cand 560-560 | CSS section comment: `/* TABLES */` → `/* 表 */`. |
| B95 | orig 643-643 → cand 650-650 | Inline rule comment: `/* == Selection Modifier == */` → `/* == 選択項目調整 == */`, the rule itself unchanged. |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-raisa-sigma-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** RAISA Sigma-9 Theme
- **Author:** macro_au_micro
- **Source:** https://scp-wiki.wikidot.com/theme:raisa-sigma — revision 13
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
