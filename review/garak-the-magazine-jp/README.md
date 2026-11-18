# Review package — theme:garak-the-magazine-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:garak-the-magazine-jp — origin KO, population #265 [GOSIGN2-LEDGER (b) row 265]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 3ec97b9a513e534171c234c2bb5532e3467791784c8586874229c5fe5dc93ca3); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 284; GOSIGN2-LEDGER (b) row 265]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-* cluster confined to chromium-768, whose only hotlink host is http.cat = transient 503 capture, not a result; page-overflow 363–397px@320/375 on page and sample; sample credit-modal (preview-form); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 264, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 264]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 265]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:garak-the-magazine-jp.txt sha256:3ec97b9a513e534171c234c2bb5532e3467791784c8586874229c5fe5dc93ca3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 265) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (classes (ii)/(iii)); the render row's items (section 11); the companion fragment's posting dependency (P1/P4 classes, section 3). **One defect flag from this package:** all five usage snippets name a page that is not this candidate (candidate L70, L79, L87, L93, L112; per-theme record below) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:garak-the-magazine | theme:garak-the-magazine-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 179 (first translation; the candidate's credit block records 初訳時参照リビジョン: 179) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-garak-the-magazine.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:garak-the-magazine-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 1,051 lines / 24,222 bytes | 1,043 lines / 24,230 bytes |
| SHA-256 | 88ca7dba1928fac16caf92a637278dbef1934375b6047722ca6aa863884b2434 | 316420d9890feb8297fd78e800cbbd4507a5514761834af2655477317a0cf018 |

Wave history: the candidate was created by the Stage 2 KO4 integration (commit 56b9d1a, the LOCALIZE-S2-F wave's port); rework2-p1 (95fd1d1) restored its missing base delivery and created the companion fragment page; FIX-P4 (f1138e4) repointed its base-theme CSS imports to the JP candidates; FIX4-IWA (8c62b7b) added the interwiki-style frame, and is the stamp's computed-against commit. (This file has no FIX-CREDIT-D commit; its credit block already carried the ruling-3 translator form.) No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. The port ships a companion file in-repo, `pages/fragment:u-navstyle-jp-base-css.txt` (sources.tsv kind: K5b-4); the change-set section records it.

## Summary

The batch's most mechanical theme: a magazine theme whose pages are assembled by parameterized includes (issue, feature, color, and title variables), delivered in layers — a sidebar base that arrives through a component include, a parameterized variable module, a defaults module, and a 921-line CSS exhibit. The port keeps the whole machine and changes its supply lines: the KO sidebar component is replaced by a companion fragment page carrying the base CSS verbatim (restored by rework2-p1 after the first port dropped the base delivery), the variable system and its documentation are translated in place, the Korean webfonts (Paperlogy in nine weights, NanumSquareRound) are replaced by M PLUS faces, and the Korean masthead artwork is retired in favor of a text title in the theme's own main color. Measured churn (diff.md, the generator's difflib count with autojunk off: +85/−93 in 51 change blocks). One defect flag arises, on all five usage snippets' page name (per-theme record); the companion fragment's posting dependency is a ledger disposition, argued in section 3.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 51 change blocks — 20 specific (39.2%), 29 heuristic (56.9%), 2 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| CSS-BODY | 20 |
| TRANS-UNANCHORED | 12 |
| TRANSLATION-ANCHORED | 8 |
| ESCAPED-INCLUDE | 5 |
| INCLUDE-REPOINT | 5 |
| DRAFT-HOST | 4 |
| COMMENT-TEXT | 3 |
| INFO-DEL | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 20 CSS-BODY blocks resolve as 9 P7 font-stack rewrites (section 4), 6 masthead-treatment lines (blocks B30–B33, B40, B41; per-theme record), 3 `content:` fallback translations riding with CSS-BODY primaries (B34, B38, and B35's anchored pair; section 6), and 2 `rgb()` → `rgba()` declaration repairs (B44, B45; per-theme record). The single EXHIBIT-RESTRUCTURE primary (B1) is the base-delivery restoration at the head, not an exhibit change (section 3). The 2 residue blocks are one-line translations (B22 and the sidebar media-query pair B50–B51, adjudicated in sections 6 and 5). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:garak-the-magazine-jp; original theme:garak-the-magazine on scpko at reference revision 179; candidate `pages/theme:garak-the-magazine-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: K5b-4, multi-delivery composition; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The theme is a parameterized magazine skin: a page adopts it by including the theme page itself with variables (issue, feature, color, alt, title), and its CSS is layered — a sidebar base, a variable-template module, a defaults module, and the exhibit. Every later section reads against that anatomy.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the layered delivery decides how section 3 is read, and the parameterized usage decides why section 2's flag matters more here than in a plain theme.
- **Verify:** The sources.tsv row for garak-the-magazine-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery layers are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L43–45) plus a `:scpko:info:start`/`end` pair (original L47–63) whose body carries the maker line (**제작:** [[*user thd-glasses]]), an image-sources section, and a font-sources section. The candidate deletes both (blocks B6–B7, B9) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L30–39) carrying the eight ruling-3 fields (title 月刊カラククンCSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 월간 가락꾼 테마; 著作権者 thd-glasses; 作成年 2024; 初訳時参照リビジョン 179; the source link, section 7) — the 著作権者 field names the same maker the info block names, so no one is dropped. The info block's non-credit content survives as body prose directly below: the intro paragraph (candidate L68, with the Garak hub link of section 7), and the two source sections under their translated headings (**画像出典**, candidate L63; **フォント出典**, candidate L66). The exhibit's banner comment credits the theme to thd-glasses on both sides (section 6). There is no T7 credit-module CSS supplement; the theme's own `.creditRate` positioning rule rides inside its defaults module, carried unchanged (candidate L52–54).
- **Why:** P3/T1 (KB-09): the preview credit module is rate-bearing, so the bare Rate is deleted rather than duplicated, and the info pair is ledger class C residue, not JP furniture — its substance is carried as prose, the same form as jiha's. Ruling 3 fixes the eight fields; the T4 lane recorded this theme's attribution as good quality (LOCALIZE-ROWS row 264).
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L30–39 against the eight fields and candidate L61–68 against original L47–63.
- **Disposition:** Standing (present from creation; the T4 row charges nothing against this section).

### 2. Includes and components

- **What:** The include census divides three ways. (1) Repointed and correct: the sidebar navigation include, `[[include nav:side]]` → `[[include :scp-jp:nav:side]]` (block B2, candidate L6, inside the restored `#u-side` markup), and the frame and credit includes (sections 3 and 1). (2) Replaced: the base component `:scpko:component:u-navstyle` (original L1) is not repointed but substituted — its CSS arrives from the companion fragment page instead (section 3), because the component itself was never ported as a JP component. (3) Flagged: all five usage snippets. The plain usage line (block B9, candidate L70) and the four parameterized examples in the variable documentation (blocks B11, B13, B14, B19: candidate L79, L87, L93, L112) repoint the prefix (`:scpko:` → `:scp-jp:`) but keep the original's page name, `theme:garak-the-magazine`, without the `-jp` suffix this candidate's own name, file name, and frame `theme=` URL all carry. For a parameterized theme the examples are the documentation a user copies and fills in, so the wrong name sits in five places, not one. Flagged, not edited (per-theme record below).
- **Why:** P1 (KB-15): includes name the JP page that actually exists. Items (1) and (2) follow it, each in the form its target allows; item (3), on the bytes, does not name this candidate.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the fragment module is an @import, not an include; the include list is the nav, the frame, the credit pair, and the five snippets.
- **Disposition:** Repoints and substitution applied; the usage snippets are the package's defect flag (per-theme record).

### 3. Delivery and code loading

- **What:** Three delivery layers, each with its own history. (a) The sidebar base: the original includes `:scpko:component:u-navstyle` (original L1), whose module delivers the base CSS the theme's `#u-side` markup needs. The first port dropped that delivery; rework2-p1 (commit 95fd1d1, "restore missing base deliveries (9 DROP pairs)") restored it as a companion page, `pages/fragment:u-navstyle-jp-base-css.txt`, which carries the component's CSS body verbatim (its own header records the source: scpko:component:u-navstyle rev 4, thd-glasses, CC BY-SA 4.0, with the component's documentation wrapper omitted as a machine page does not need it). The candidate imports it at its head (candidate L1–3, from the draft host). (b) The theme's own code: the original's module imports its block /0 from scpko.wdfiles.com (original L9); the candidate's corresponding module imports its own /1 from the production host (candidate L11, block B3) and carries the parameterized `:root` template unchanged below the import (candidate L13–20) — the template's `{$…}` placeholders are the theme's variable mechanism, not unsubstituted defects. FIX-P4 (f1138e4) is the wave that repointed these base imports to the JP candidates. (c) The defaults module (original L23–41 → candidate L41–59) and the CSS exhibit (original L127–1047 → candidate L134–1039) ride unchanged in form. **Frame paragraph (the M-frame addition):** the original carried no interwiki-style frame (LOCALIZE-ROWS row 264, 型 6); the candidate adds one at candidate L23–26 with `priority=1` and `theme=` naming its own /1 delivery — in the production-host form (`scp-jp.wdfiles.com`) this theme uses for its own code, where the batch's other frames use the draft host; the single-layer own-code form, in the spaced parameter style. The ledger records the outcome as P6 FIXED (frame waves; checker-verified); the frame arrived in FIX4-IWA (8c62b7b). The T4 row's remaining charge is this section's disposition: the fragment page 404s on scp-jp today, so at posting the sidebar base dies unless the fragment page is created on scp-jp or its CSS is inlined — the row itself marks it 要 staff 判断 (a staff call), and the ledger dispositions the class (P1 DISPOSITIONED, posting-procedure convention; P4 DISPOSITIONED, delivery class (ii)).
- **Why:** P4/T9 for the own-code repoint; KB-20's inverse for the base — a base delivery the port needs must arrive from the JP side, and where no JP component exists, a companion page carrying the base verbatim is the campaign's restoration form (the rework2-p1 DROP-pair repairs). P6/T3 (KB-07) for the frame. The fragment's posting dependency is a class (ii) mechanics question the ledger has already placed: the fragment is a posting-batch sibling, like foundation-paper's `news` page.
- **Verify:** Read candidate L1–26; read the fragment's header at `pages/fragment:u-navstyle-jp-base-css.txt` L1–8; `grep -n 'u-navstyle' candidate.txt` — the import at L2 and the porter comment at L938 (section 5).
- **Disposition:** FIXED (P6); the base restoration stands in-repo; the fragment's on-wiki creation is DISPOSITIONED (P1/P4, posting-procedure classes).

### 4. Fonts and assets

- **What:** Fonts, by substitution. The original loads two Korean faces by `@font-face` from jsdelivr noonnu distributions (original L132–142: Paperlogy in nine weights, NanumSquareRound in one) and names them in nine stacks (eight Paperlogy, one NanumSquareRound, each ending in the malformed generic `san-serif`). The candidate replaces the whole load with one Google Fonts `@import` (block B26, candidate L141: M PLUS 1p 400;500;700;800 and M PLUS Rounded 1c 400;700) and rewrites all nine stacks (blocks B29, B36, B37, B39, B42, B43, B46, B47, B48): Paperlogy stacks become `"M PLUS 1p", "Noto Sans JP", sans-serif` and the NanumSquareRound stack becomes `"M PLUS Rounded 1c", "M PLUS 1p", "Noto Sans JP", sans-serif` — each stack's first-named face is one the L141 load delivers, so no KB-16 gap arises, and the generics are well-formed. Assets: the theme's body background (block B28, candidate L151) repoints from scpko.wdfiles.com to the candidate's own production-host file area, name unchanged (body_bg.png). The masthead image (garak-the-magazine.png) is not repointed but retired — the per-theme record's subject. The T4 lane recorded the font substitution as good quality.
- **Why:** P7/T5 with KB-16, in its substitution form: the Korean faces cannot render Japanese and their distribution source falls outside the direct-link exception, so JP faces from an allowed host take their roles, load and stacks changed together — M PLUS Rounded 1c taking the rounded display role NanumSquareRound held, M PLUS 1p the text role Paperlogy held. P5/KB-17 for the one asset's re-hosting.
- **Verify:** `grep -n 'Paperlogy\|NanumSquareRound\|noonnu' candidate.txt` returns nothing; `grep -n 'font-family' candidate.txt` — nine lines, all JP stacks; `grep -n 'wdfiles' candidate.txt` against the asset list above.
- **Disposition:** Substitution applied; the production-host asset URL is the posting form (class (ii) mechanics).

### 5. Header, sidebar, and site furniture

- **What:** The header is the masthead cluster (per-theme record): `#header`'s background, the mask div, and the h1's transparent color are the three lines that change, all in the exhibit. The sidebar is the theme's reason for existing, and its adaptation is porter-commented in the CSS itself (block B49, candidate L938): the candidate restores the `#u-side` markup at the page head (candidate L4–8, wrapping the repointed `nav:side`) and reads the base CSS from the fragment (section 3). Two small media-query changes ride with it (blocks B50–B51, the classifier's residue in this zone): in the ≥768px query the original's `#side-bar { display: none; }` does not survive — the JP layout keeps the standard sidebar rather than suppressing it outright — and in the ≤767px query the candidate adds a `#side-bar` background in the theme's main color. The theme's own `#u-side` rules themselves are carried unchanged. No header variables are overridden as furniture; the `--issue-*` / `--feature-*` / `--index` variables are the theme's content system (sections 0 and 6).
- **Why:** P8: layout rules keyed to the KO branch's sidebar component cannot transfer unchanged when the component itself is substituted; the adaptation is annotated at the point of change (the L938 comment), which is what separates it from a silent furniture loss.
- **Verify:** Read candidate L936–985 against original L937–990; read candidate L4–8.
- **Disposition:** Standing as annotated adaptations; no unannotated furniture loss.

### 6. Text translation

- **What:** The prose and the variable documentation are translated throughout, in the classifier's counts: 8 TRANSLATION-ANCHORED and 12 TRANS-UNANCHORED primary blocks (B5–B23), each verified line by line. In groups: the defaults module's variable values (B5: `--issue-1: "필진모집"` → `"寄稿者募集"`, and its `--feature-1` companion); the intro and source sections (section 1); the variable-usage documentation entire (B10–B21: the headings, the parameter tables' labels — 索引名 for 색인명 (block B22, residue) among them — and the prose rules for alt/color/title); and the exhibit's reader-visible strings, the `content:` fallbacks that render when a page sets no variables (B34: the issue fallback 특별호 → 特別号； B35 and B38: the feature fallback, the interview headline, translated). In-CSS comment text (R1): the exhibit's banner comment is translated (block B24: 月刊カラククンテーマ by thd-glasses) and its section comments carried; the two added comment lines are porter annotations (section 10). Korean survives in the candidate only as quotation: the credit block's original-title field (candidate L34). R5 glyph-form conversion: none as a separate class — retained Korean strings are quotations, and translated strings are translations.
- **Why:** P10 (body, usage, and sample translation is the port's purpose — for this theme the usage documentation *is* the product, since the theme is operated through its variables) and KB-18 (reader-visible strings, including the `content:` fallbacks, which a reader sees on every page that sets no issue or feature). The unanchored group is where a silent deletion would hide, which is why each was read individually.
- **Verify:** The pairs are diff.md's body sections in order; a Hangul scan of candidate.txt returns only candidate L34.
- **Disposition:** Standing (the port itself); the T4 row records the translation quality as good.

### 7. Links

- **What:** Three link matters. (1) The hub link: the original's relative `[[[garak-the-hub|허브]]]` (in the variable documentation, block B16) becomes an absolute link to the KO hub with its label made explicit, `[[[https://scpko.wikidot.com/garak-the-hub|ハブ（韓国語版）]]]` (candidate L102), and the intro names the same hub the same way (candidate L68) — the Garak hub exists only on the KO branch, so the links name the serving original and say so in the label. (2) The credit block's source link (candidate L38) names `https://scpko.wikidot.com/theme:garak-the-magazine` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. (3) No other outbound links: the font and image sources the original's info block linked are carried as text in the フォント出典 / 画像出典 sections (section 1).
- **Why:** P11 under the dead-reference evidence standard: a link whose subject exists only on the original branch names that original, with the label carrying the branch so a JP reader is not sent across branches unknowing.
- **Verify:** Compare candidate L38's host against the sources.tsv row's original_url host (scpko.wikidot.com) — identical; read candidate L68 and L102.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds in form, with one declared substitution. The topology pass finds the exhibit and the two defaults/template modules on both sides; the candidate has one component the original lacks (the head fragment-import module) and lacks one the original has (the u-navstyle include), which is the section 3 substitution, not a restructuring. Variable names, the `{$…}` template mechanism, selectors, and rule order are preserved; the JP corrections arrive at the head (fragment import, frame, credit block) and as the annotated sidebar adaptation (section 5), not interleaved into the inherited CSS. The classifier's one EXHIBIT-RESTRUCTURE primary (B1) adjudicates to the head delivery substitution. An exhibit census confirms the shape: the variable documentation entire, the defaults module, and the full CSS exhibit are present on both sides in the same order — nothing was dropped or replaced inside the body, so the R3 question is confined to the delivery layer, where section 3 answers it.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[module\|\[\[code\|u-navstyle' original.txt candidate.txt` — the sequences correspond, with the head substitution the only difference.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a primary class: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 51 blocks, so the R7 follow-up-diff hazard is not triggered. (The 2 residue blocks are content, adjudicated in sections 5–6, not formatting.)
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three annotations. (1) The exhibit's added banner line (block B25, candidate L139): "/* SCP-JP版: 2026年に日本語版へ移植。作成者: thd-glasses（韓国支部）。翻訳: SCP-JP。 */" — porter-visible provenance; the TASL record proper is the credit block (section 1), whose translator field carries the ruling-3 form (AI), and the two are recorded here so a reviewer is not left to reconcile the banner's collective wording with the field unaided. (2) The sidebar comment (block B49, candidate L938), quoted in section 5: the in-file ground for the base substitution and the restored markup. (3) The companion fragment's own header (pages/fragment:u-navstyle-jp-base-css.txt L1–8): a full provenance note — what the page is, its source component and revision, its license (CC BY-SA 4.0), what was omitted and why, and how the theme's own variables limit the base's effect in the JP environment. The candidate has no `[!-- --]` notes in the theme file itself.
- **Why:** R2: porter-added text is part of the change record, and annotation (2) is load-bearing — it is the only in-file explanation of the sidebar adaptation; annotation (3) is the fragment's TASL-adjacent record.
- **Verify:** Read candidate L139 and L938; read the fragment's first eight lines.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's three pseudo-ref errors: the candidate's own not-yet-posted references (the fragment import, the own-code import, and the frame URL of section 3) — classes (ii)/(iii), posting-procedure and draft-form; the posting procedure creates the fragment page and rewrites the hosts, and fix lanes never "fix" them in the candidate. (2) The render row's items (RENDER-ROWS-2, RENDER-S2-H (KO4)): the page's hidden-* cluster confined to chromium-768 whose only hotlink host is http.cat (KB-44: a transient Wikidot 503 capture, not a result), the page-overflow readings (363–397px at 320/375 on page and sample), and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5) — sample and environment layer, recorded as not charged to the candidate. (3) The fragment's posting dependency: DISPOSITIONED (P1, posting-procedure convention class; P4, delivery class (ii); section 3). (4) The usage-snippet flag (per-theme record) is not in this list: no ledger line dispositions it, which is why it is flagged rather than dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 284): exit 1, 3 errors / 2 warns / 1 info; all three errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO4)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 264): FINDINGS jointly, display-affecting findings 1 — the row's charges are 型 1/型 4 (the companion fragment's 404 on scp-jp, dispositioned as a posting-batch question, with the row itself calling for a staff decision between creating the fragment page and inlining its CSS) and 型 6 (the absent frame, since FIXED by FIX4-IWA); the same row records the translation, attribution, and font substitution as good quality. The ledger §(c3) line records the outcomes: P1 DISPOSITIONED, P4 DISPOSITIONED, P6 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +85/−93 in 51 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:garak-the-magazine-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 265; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports 2 residue blocks; both were adjudicated against the bytes:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B22 | 116-116 → 123-123 (body → body) | no signature | One-line variable-table label translation (`**(색인명)**` → `**(索引名)**`); section 6 |
| B50–B51 | 969-969, 978-984 → deleted (code-css → body) | CSS-BODY heuristic pair | The sidebar media-query adaptation's removed lines (the ≥768px `#side-bar` suppression and its block pairing); section 5 |

The 29 heuristic blocks are the one-line prose and documentation translations counted in section 6 (B8, B12, B15, B18, B20 and companions), the font-stack rewrites and masthead lines counted in section 4 and the per-theme record (B29–B48's CSS-BODY primaries), and the comment translations of section 6 (B24, B25, B49).

## Per-theme record

### The usage snippets name a different page (defect flag)

The usage snippets are the lines a reader copies to adopt the theme, and on the bytes all five name the wrong page. Candidate L70 reads `> @@[[include :scp-jp:theme:garak-the-magazine]]@@`, and the four parameterized examples in the variable documentation (candidate L79, L87, L93, L112) open `@@[[include :scp-jp:theme:garak-the-magazine` with their parameter lines following. This candidate is theme:garak-the-magazine-jp: its canonical file is `pages/theme:garak-the-magazine-jp.txt` and its frame `theme=` URL names `theme%3Agarak-the-magazine-jp`. For this theme the flag weighs more than in a plain port: the parameterized examples are the theme's operating instructions, so a reader who follows the documentation literally assembles an include of a page that will not exist under that name. Probes run for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:garak-the-magazine` returns 404 and `https://scp-jp.wikidot.com/theme:garak-the-magazine-jp` returns 404 — neither page is posted yet, so the probe cannot settle intent; what the bytes settle is that the snippets are inconsistent with the candidate's own identity. No ledger line dispositions the snippets' name (the T1 pseudo-ref classes cover references to the not-yet-posted page itself, which these are not, on the bytes). The candidate is left exactly as it stands, per the standing rule for fix lanes; the repair, if the coordinator confirms it, is the repoint of the five snippet lines to the candidate's own page name, after which this package's diff.md and stamp need no change beyond regeneration (the candidate file's hash in the stamp would change).

### The masthead artwork is retired for a text title

The original's header is a picture: `#header` carries the magazine's masthead artwork (garak-the-magazine.png, a Korean-language masthead) as its background (original L215), a masked overlay div tints it with the theme's main color (original L222–225), and the h1 text is transparent over it (original L238). The candidate retires the artwork on all three lines (blocks B30–B33 and the second instance at B40–B41): `background: none`, the overlay div `display: none` with its masks set to `none`, and the h1 colored `rgb(var(--main))` so the page's own title text renders as the header. The ground is the artwork's language: the masthead is Korean lettering, and a JP page cannot present it as its title; the theme's own variable system (a page-set title in the theme's main color) is the designed fallback the port takes. The geometry is untouched (the 170px header height and spacing survive), and the rest of the header rules are carried. This is a design substitution declared by the bytes and consistent with the theme's variable-first construction; the render sweep passed the candidate in this form, and no ledger line charges it. It is recorded here so the substitution is a judged fact of the package, not a discovery a later reviewer has to make from the diff.

### Two `rgb()` declarations repaired to `rgba()`

Blocks B44 and B45 pair two lines whose only change is the function name: `background: rgb(var(--main), 0.15)` → `rgba(var(--main), 0.15)` (original L588 → candidate L587) and `color: rgb(var(--main), 0.5)` → `rgba(var(--main), 0.5)` (original L600 → candidate L599). The comma-form `rgb()` with a fourth alpha argument is not valid in the legacy syntax these declarations use; `rgba()` is the well-formed spelling of the same value. A KB-03-shape repair in place, recorded here because the classifier's CSS-BODY label does not name it.

## Change set outside the two diffed files

The diff covers two files; the port's record is three files larger. (1) `pages/fragment:u-navstyle-jp-base-css.txt` is this theme's companion: the sidebar base CSS restored by rework2-p1, imported by the candidate's head module (section 3); it carries its own provenance header and belongs to this theme's record. (2) `pages/theme-decoration-sample-garak-the-magazine-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There is no shared base file beyond the fragment, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 월간 가락꾼 테마
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/theme:garak-the-magazine — revision 179
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
