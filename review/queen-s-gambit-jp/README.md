# Review package — theme:queen-s-gambit-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:queen-s-gambit-jp — origin EN, population #125 [GOSIGN2-LEDGER (b) row 125]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 125]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 150; GOSIGN2-LEDGER (b) row 125]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow. [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 125, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 125]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 125]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:queen-s-gambit-jp.txt sha256:c4d45f751be7df2a35acff7f4ece6454aede929318fd8a3992f3ae9dd102b1e9; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 125) |
| Standing items | **One FIXED, rest DISPOSITIONED** — the credit fields were fixed by the credit waves (P3 FIXED, section 1); the theme's EN-hosted CSS and exhibit images stand under the deferred-asset disposition (P5, class (ii) / KB-58, section 4, stated plainly there and in the per-theme record); the T1 pseudo-ref is draft form (class (iii)); the render row's items are the cross-cutting families of section 11. No defect is flagged for this theme |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:queen-s-gambit | theme:queen-s-gambit-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 21 (first translation; the candidate's credit block records 初訳時参照リビジョン: 21) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-render-s2-2/mirrors/queen-s-gambit.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:queen-s-gambit-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 614 lines / 11,426 bytes | 613 lines / 12,643 bytes |
| SHA-256 | bc89d7cae442a46661812dd5e7f649c6e9c6c855580128e8b0242cc97ecd7f2c | c4d45f751be7df2a35acff7f4ece6454aede929318fd8a3992f3ae9dd102b1e9 |

Wave history: the candidate was created by the Stage 2 EN17 integration (commit b17d7e4, the RENDER-S2-2 wave's port) and has exactly one later commit under its current path, 1869877 (FIX-CREDIT-D), whose queen-s-gambit hunk is the translator-field fix of section 1. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Black Queen chess theme: a single stylesheet with castle-and-flourish background art, delivered by a head module ahead of the gate. The port converts the original's two bare rating exhibits (a Rate module, and an info-pane pair) into the preview credit block, completing the credit fields the localize check charged (the translator placeholder is gone; ledger P3 FIXED); carries the tail license box's attribution as translated prose, preserving the logo artist's credit; repoints the delivery to the candidate's own draft-host /1; extends the sidebar collapsible selector groups to their interwiki counterparts (a P6 supplement visible in five selector blocks); and translates the prose, exhibits, and CSS comments. The one retention a reader must not miss: the theme's two CSS background images and its exhibit logo still load from the original wiki's file area — charged display-affecting by the localize check and dispositioned, not fixed (P5, KB-58). Section 4 states it plainly.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 37 change blocks — 15 specific (40.5%), 21 heuristic (56.8%), 1 residue (2.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 18 |
| COMMENT-TEXT | 11 |
| TRANSLATION-ANCHORED | 8 |
| CSS-BODY | 5 |
| EXHIBIT-RESTRUCTURE | 3 |
| COLON-ENC | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| IFTAGS | 1 |
| INFO-DEL | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the five CSS-BODY blocks are the interwiki selector supplement of section 5, not unclassified CSS changes. The three EXHIBIT-RESTRUCTURE blocks are a frame repoint (B2), a caption translation on a kept exhibit (B11), and the license-box conversion (B37, section 1) — no restructuring in substance. The COMPONENT-SWAP primary (B9) is the usage exhibit's repoint to the candidate's own unprefixed name (section 2). The one residue block (B20) is CSS comment translation (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:queen-s-gambit-jp; original theme:queen-s-gambit on scp-wiki at reference revision 21; candidate `pages/theme:queen-s-gambit-jp.txt`. Provenance route: derived from the original at the reference revision by the RENDER-S2-2 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). Both files open with the delivery module and frame ahead of the tag gate (original L1–8; candidate L1–8), and the gate localizes as usual (block B4: `[[iftags +theme]]` → `[[iftags +テーマ]]`, candidate L10).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization).
- **Verify:** The sources.tsv row for queen-s-gambit-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is P2, applied.

### 1. Credit and attribution

- **What:** The original's credit furniture is two bare exhibits: a right-aligned `[[module Rate]]` under a "Rating:" heading (original L14–17) and a "Rating w/ Info Pane:" heading over an empty unprefixed `[[include info:start]]` / `info:end` pair (original L19–23). The candidate deletes both exhibits (blocks B6, B7: BARE-RATE-DEL and INFO-DEL) and installs the preview credit block at the same position (candidate L14–23): the eight ruling-3 fields （タイトル Queen's Gambit CSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Queen's Gambit CSS Theme; 著作権者 c_bonefish; 作成年 2022; 初訳時参照リビジョン 21; the source link, host-verified in section 7). Two field-level charges from the localize check are closed here: the translator field's `SCP-JP` placeholder is replaced (the FIX-CREDIT-D commit, 1869877), and the fields stand complete — the author field is in the plain-text form the population also uses (the M-pure exemplar package's author field is plain text likewise), naming c_bonefish, the author the original's own prose names (original L25). The theme's second attribution lives at the tail: the original's license box (`:scp-wiki:component:license-box-theme` / `license-box-end`, original L603–612) names Flypurgatorio as author of the "Crown of Flies" logo under CC BY SA 3.0; the candidate deletes the includes and carries the whole attribution as translated prose (candidate L603–611, block B37): a ライセンス line crediting c_bonefish (theme) and Flypurgatorio (logo), the attribution block translated field by field, and a closing sentence recording that both image files and the theme code are CC BY-SA 3.0. No attribution is dropped. T7 credit CSS: no supplement was added; the credit-adjacent rules are inherited on both sides (six matching lines each).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form; a bare Rate exhibit and an empty info pair are the two halves of the class C failure (duplicate furniture, KB-10) when left beside it, so the conversion replaces rather than accumulates. Ruling 3 fixes the eight fields, and a placeholder translator is the P3 defect the credit waves exist to remove. The license box's conversion is KB-60: the EN license-box components are branch furniture, and their content is attribution, which prose carries without loss.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L14–23 against the eight fields and L603–611 against original L603–612.
- **Disposition:** FIXED (P3, credit waves, checker-verified; GOSIGN2-LEDGER §(c3)).

### 2. Includes and components

- **What:** Four include events besides the credit pair. The head frame is repointed to `:scp-jp:component:interwiki-style` (block B2, candidate L5). The license-box pair is deleted with its content carried (section 1). The usage exhibit (block B9, the classifier's COMPONENT-SWAP primary) repoints `@@[[include :scp-wiki:theme:queen-s-gambit]]@@` → `@@[[include theme:queen-s-gambit-jp]]@@` (candidate L29): the unprefixed same-site form naming the candidate's real posting name — the correct-name form, not the plain-slug defect family. The page-elements exhibit keeps its unprefixed `[[include component:image-block ...]]` (candidate L35, block B11) with the caption translated （ロゴ背景）; the unprefixed component resolves on scp-jp, and the image it displays is section 4's item.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — frame (L5), credit pair (L14, L23), image-block (L35), and the escaped exhibit (L29).
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The topology is preserved (the classifier's pass: a head module plus the code exhibit on each side, no moves). The original's delivery is external-form: its module imports its own /1 from the wiki domain itself, `https://scp-wiki.wikidot.com//local--code/theme:queen-s-gambit/1` — double slash, unencoded colon (original L2; the topology pass records `external_own_delivery: true`). The candidate normalizes the same self-delivery to the standard form: `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aqueen-s-gambit-jp/1` (candidate L2, block B1), with the frame at priority 1 naming the same delivery (candidate L5–8, block B3). The CSS itself is the code exhibit on both sides (542 lines each).
- **Why:** P4/T9 and P6/T3: a theme's live channel in the JP environment is its own local--code delivery framed by interwiki-style; the candidate's form is the population's, and the draft host is KB-41, class (iii).
- **Verify:** `sed -n '1,8p' candidate.txt` against original L1–8 — one import, one frame, same order.
- **Disposition:** DISPOSITIONED (draft-host form, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: neither side loads any font (no @import beyond the delivery line, no @font-face, no font stacks to rewrite); the theme renders in the platform's faces, and there is no P7 event in this pair. Assets: this is the section the per-theme record also speaks to. The candidate's live CSS still loads the theme's two background images from the original wiki's file area — `blackqueen-background.png` (candidate L76) and `blackqueen-logo.png` (candidate L82), both `scp-wiki.wikidot.com/local--files/theme%3Aqueen-s-gambit/…`; the only change on those lines is the colon-encoding normalization (blocks B22, B23: `theme:queen-s-gambit` → `theme%3Aqueen-s-gambit` in the URL path). The page-elements exhibit's logo image likewise still names the original wiki's file area (candidate L35: `name=https://scp-wiki.wikidot.com/local--files/theme%3Aqueen-s-gambit/blackqueen-logo-background.png`). These are the localize check's pattern-5 charges (the exhibit image at its L35, the CSS pair at its L76/L82), recorded display-affecting, and the ledger's answer is a disposition, not a re-host: P5 DISPOSITIONED, class (ii) / KB-58 deferred assets. The pixabay source images are credited in the CSS banner comment (section 6), not loaded.
- **Why:** P5's re-hosting rule is the default; KB-58 records the deferred-asset class where the original file area keeps serving and re-hosting is deferred past the go-sign. The colon-encoding change is URL hygiene on a kept reference, not a re-host. A reader of this package should nonetheless see the retention plainly, which is why this section names the three URLs rather than absorbing them into the disposition.
- **Verify:** `grep -n 'scp-wiki.wikidot.com/local--files' candidate.txt` — exactly the three loci named above.
- **Disposition:** DISPOSITIONED (P5, class (ii) / KB-58; GOSIGN2-LEDGER §(c3)).

### 5. Header, sidebar, and site furniture

- **What:** No header variables exist on either side (no `--header-title` / `--header-subtitle`), and no P8 adaptation was needed. This section's real content is the supplement the classifier labels CSS-BODY (blocks B27–B31, candidate L314–337): five selector groups in the sidebar collapsible zone are extended with their `#interwiki` counterparts — e.g. `#side-bar .collapsible-block-folded-link .collapsible-block-link` gains `, #interwiki .collapsible-block-folded-link .collapsible-block-link` (candidate L325), and the `#interwiki .heading` group gains its unfolded-link counterpart (candidate L314). The declarations under the extended selectors are the original's, unchanged; what changes is coverage: the collapsible styling now reaches the interwiki sidebar the JP environment renders beside the main one.
- **Why:** P6: where the original styles a frame the JP environment renders in an additional container, the port extends coverage rather than leaving the frame unstyled — the same supplement family as an interwiki frame parameter, applied at selector level.
- **Verify:** Read candidate L314–337 against original L314–337 — five extended selector lines, no declaration changes in the zone.
- **Disposition:** Applied (supplement; no ledger item stands against it).

### 6. Text translation

- **What:** The prose is translated throughout: the intro and import instructions (blocks B7, B8, B10), the exhibit headings and tab labels (blocks B12, B13), the footnote text, and the license prose of section 1. The CSS comments are translated as a class (eleven COMMENT-TEXT blocks: B18, B19, B21, B24–B26, B32–B36), including the banner comment's image credits, whose pixabay URLs are kept (block B20, the appendix's residue). The anchored blocks (eight) were verified line by line.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings); CSS comments are porter-visible only (R1's comment half), which is why they are counted as a class rather than verified line by line.
- **Verify:** The pairs are diff.md's body and code sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit block's source link (candidate L22) names `https://scp-wiki.wikidot.com/theme:queen-s-gambit` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered; its label is the theme's English title rather than the word ソース, a T5 joint-note shape, not a defect. The intro's hub link (candidate L25) keeps its scp-wiki target (`black-queen-hub`) inside the carried wikilink syntax, its label translated （黒の女王） — the hub is the EN GoI hub the theme was made for, and no charge stands against the link. The link exhibit's examples (block B14: original L48–49 → candidate L48–49) translate the labels and repoint the visited-link example to the candidate's own page name (`theme:queen-s-gambit-jp`), so the exhibit demonstrates against a page that will exist.
- **Why:** P11: prose links take the JP counterpart where one exists; where the original-side page is itself the subject (the hub the theme serves), the serving original stands.
- **Verify:** `grep -n 'black-queen-hub\|元記事リンク' candidate.txt` — the two loci named above.
- **Disposition:** Applied.

### 8. Structure

- **What:** The exhibit census corresponds: import exhibit, page-elements exhibits (image-block, headings, tabview), and the code exhibit are present on both sides in the same order. The named conversions are the rating exhibits' replacement by the credit block (section 1) and the license box's conversion to prose (section 1) — both sanctioned forms, neither a silent drop: the Rate function is carried by the credit module, and the license content is carried verbatim in translation. Selector and variable names inside the CSS are preserved apart from the section 5 supplement.
- **Why:** R3: the census is what separates a conversion (this theme) from a silent restructure or drop (the failure class I charges); here every original region has a named candidate counterpart.
- **Verify:** Compare the heading and include sequences of the two files — they correspond at the loci named in sections 1–3.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0) in this pair.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (no WS-ONLY label).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. An explicit check of the candidate finds no `[!-- ... --]` porter comment and no editor line with no original counterpart; the classifier's ANNOTATION signature does not fire.
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three hotlink errors: class (ii) — they are the section 4 assets (the exhibit image-block and the CSS background pair) standing under the KB-58 deferred-asset disposition. (2) T1's one pseudo-ref error: class (iii), the draft-host delivery of section 3. (3) The render row's items, all cross-cutting: the sample's credit-modal errors (KB-32, ruling 5 — the sample's preview-form credit include has no modal mechanism) and the 884px@768 overflow (KB-33/KB-34 families). The page side of the render row carries no theme-specific item beyond the environment hotlink chain (KB-40). T4's two charges close as: pattern 3 FIXED (section 1), pattern 5 DISPOSITIONED (section 4).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items (1)–(3)); FIXED (the credit charge).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 150): exit 1, 4 errors / 1 warn / 1 info; the errors are hotlink ×3 and pseudo-ref ×1, all in the dispositioned classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-2 (EN17)): FINDINGS, the items of section 11(3), all dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 125): FINDINGS jointly, display-affecting findings 1 (the pattern-5 asset family); the ledger §(c3) line records the theme's T4 outcome as P3 FIXED and P5 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +68/−74 in 37 classifier change blocks / 10 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:queen-s-gambit-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 125; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The EN-hosted assets stand by disposition, stated plainly

Section 4 records the three URLs; this note exists so the disposition is not misread as a repair. The localize check charged the pattern-5 family as display-affecting — the theme's page background, logo background, and exhibit logo all load from scp-wiki's file area in the candidate as it stands — and the ledger dispositions the family (P5, class (ii) / KB-58) rather than fixing it. The candidate therefore depends on the original wiki's file area at render time, by recorded decision. If that decision is ever revisited, the three loci are candidate L35, L76, and L82, and the re-hosting target would be the candidate's own file area, as other themes in this batch do (section 4 of the shark-punching-centre-bhl-jp package shows the applied form).

### Record note — the vendored LOCALIZE row truncates the pattern-5 charge

The vendored LOCALIZE-ROWS copy of this theme's row ends its pattern-5 item mid-sentence ("live image-block L35 + live/exhibit CSS L76/L82 hotlink …"), so the charge's full text is not recoverable from the record. The bytes govern and are stated in section 4: the three loci the row names are exactly the three EN-hosted references the candidate still carries, and the ledger's §(c3) line dispositions the pattern without qualification.

## Appendix — residue blocks

| Block | Span | Resolution |
|---|---|---|
| B20 | orig 68-69 → cand 68-69 | CSS banner-comment translation: the two background-image credit lines are translated （背景画像1/2) with their pixabay URLs kept. Comment mass, resolved here by shape (section 6). |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-queen-s-gambit-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Queen's Gambit CSS Theme
- **Author:** c_bonefish
- **Source:** https://scp-wiki.wikidot.com/theme:queen-s-gambit — revision 21
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
