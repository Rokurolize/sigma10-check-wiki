# Review package — theme:minimal-scp-foundation-by-cocoonist-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:minimal-scp-foundation-by-cocoonist-jp — origin KO, population #273 [GOSIGN2-LEDGER (b) row 273]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2b7886bfcda2094725915b2d1975ff5bd81e694725b3ab9721dcec8b829e6be2); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 1 warn / 1 info (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 277; GOSIGN2-LEDGER (b) row 273]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page page-overflow 341–342px@320 + 389–535px@375 + hidden-footer + sidebar-unreachable; sample hidden-* cluster across combos (4 of 8 combos carry an http.cat-only hotlink line = transient 503 captures; the rest recorded as-is) + credit-modal (preview-form) + page-overflow 341px@320 + sidebar-unreachable; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 272, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 272]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 273]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:minimal-scp-foundation-by-cocoonist-jp.txt sha256:2b7886bfcda2094725915b2d1975ff5bd81e694725b3ab9721dcec8b829e6be2; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 273). The stamp reads STALE because the candidate changed after the verdict: the source-link repair (2a8a125) and the usage sweep (b5cb724), both in the per-theme record below; the verdict lines describe the pre-change file |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×1 (posting-procedure classes, section 11); the render row's items (page overflow family, sample hidden-* capture cluster, credit-modal preview form, section 11); T4's hotpotato link (P11, section 7). **FIXED** — credit fields (P3) and the interwiki frame (P6, FIX4-IWA). **REPAIRED after the verdict** — the credit source link's dead host (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:minimal-scp-foundation-by-cocoonist | theme:minimal-scp-foundation-by-cocoonist-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 5 (first translation; the candidate's credit block records 初訳時参照リビジョン: 5) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-minimal-scp-foundation-by-cocoonist.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:minimal-scp-foundation-by-cocoonist-jp.txt`, copied at worktree HEAD 2aee861 |
| Lines / bytes | 729 lines / 17,371 bytes | 618 lines / 12,072 bytes |
| SHA-256 | f099dd3500badc91434dc82c87a9eacd856baa75637f9e665c0801b1d277265c | 2b7886bfcda2094725915b2d1975ff5bd81e694725b3ab9721dcec8b829e6be2 |

Wave history: the candidate was created by the Stage 2 KO5 integration (commit 3c781b1); FIX-CREDIT-D (1869877) normalized its credit attribution; FIX4-IWA (8c62b7b) added the interwiki-style frame the T4 record found missing. Two post-verdict commits follow: the source-link repair (2a8a125) and the usage sweep (b5cb724), both recorded in the per-theme record.

## Summary

A minimal Foundation theme by Cocoonist, used by the author's works and the KO weekly Hot Potato series. The original is a single live `[[module CSS]]` carrying the whole stylesheet inline, a fifth of it (144 lines) being eighteen `@font-face` blocks that serve Lora subset files from Google Fonts. The port rebuilds the delivery in the campaign's standard form: the CSS moves into a gated `[[code]]` exhibit, a head module imports it back as the page's own `local--code/1`, and the interwiki-style frame is added at the head. The eighteen `@font-face` blocks collapse into one Google Fonts css2 import that loads Lora together with Noto Serif JP, and the single font stack gains the JP serif fallbacks. The body prose is translated, the credit furniture is the JP preview block (the original had none on this page), and the Userstyles.org links are kept with translated labels. Measured churn (diff.md, the generator's difflib count with autojunk off: +47/−163 in 12 change blocks / 5 hunks) is dominated by the font-face consolidation, not by CSS change: the rule body travels nearly verbatim inside its new exhibit.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 12 change blocks — 10 specific (83.3%), 2 heuristic (16.7%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 5 |
| TRANS-UNANCHORED | 5 |
| TRANSLATION-ANCHORED | 3 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the five DELIVERY-MOVE blocks are one relocation, the CSS body's move from the original's live module into the candidate's code exhibit (B8–B12), with B9 being the deleted `@font-face` run inside it and B11 carrying the one translated `content:` string (section 6); the skeleton's per-section text understates sections 3 and 4 because the delivery and font signatures ride inside those move blocks, and both are written out in full below. After adjudication no block is left unexplained, and there is no residue to append.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:minimal-scp-foundation-by-cocoonist-jp; original theme:minimal-scp-foundation-by-cocoonist on scpko at reference revision 5; candidate `pages/theme:minimal-scp-foundation-by-cocoonist-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme). The frame itself moved: the original opens with its tag gate `[[iftags +테마 -nobhl]]` (original L1) and carries its CSS in a live module after the body (original L22–729); the candidate opens with the delivery module and frame (candidate L1–8), places the localized gate `[[iftags +テーマ -nobhl]]` after them (candidate L10), and holds the CSS in an exhibit inside the gate (candidate L48–614).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (the `-nobhl` qualifier is carried over unchanged), the frame is P6 (section 3).
- **Verify:** The sources.tsv row for minimal-scp-foundation-by-cocoonist-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original carries no credit furniture on this page: no Rate module, no info block; its only attribution is the prose naming [[*user Cocoonist]] as the author (original L7). The candidate installs the JP form at the head of the gated body (candidate L15–24): a `:scp-jp:credit:start-preview`/`end-preview` block carrying all eight ruling-3 fields (title CocoonistのSCP財団ミニマルテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 누에의 미니멀 테마; 著作権者 Cocoonist; 作成年 2020; 初訳時参照リビジョン 5; the source link, on which see the per-theme record). The author field matches the original's own attribution exactly. There is no license box (the original states no per-file licenses) and no T7 credit-module CSS supplement (the theme's CSS predates the credit module's DOM and styles none of its selectors; the preview module's own styling governs).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, installed where the original had prose attribution only, so there is no bare Rate to delete and KB-09 does not arise. Ruling 3 fixes the eight fields; the source link is the one field with a history, and it is carried openly in the per-theme record rather than smoothed over here.
- **Verify:** Read candidate L15–24 against the eight fields; read original L7 for the attribution the author field copies.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified). The source-link field was T4's type-3 finding; its repair landed after the verdict (per-theme record).

### 2. Includes and components

- **What:** One include repoint, in the usage example: `:scpko:theme:minimal-scp-foundation-by-cocoonist` → `:scp-jp:theme:minimal-scp-foundation-by-cocoonist-jp` (original L12 → candidate L32, block B5; the `-jp` half of the repoint is the post-verdict sweep line, per-theme record). The candidate's live includes are the frame (candidate L5) and the credit pair (L15, L24) — every include names a `:scp-jp:` target, and no component include exists on either side.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; the theme is self-contained, so ruling 4 is not engaged — no component had to be ported alongside it.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three includes, all `:scp-jp:`, plus the escaped usage line.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery is rebuilt. The original serves its CSS from a live `[[module CSS]]` inline on the page (original L22–729) — no `local--code` anywhere. The candidate moves the same CSS body into a `[[code type="CSS"]]` exhibit inside the gate (candidate L48–614, inside a collapsible under the ソースコード heading), imports it from a head module (candidate L1–3: `@import` of its own `local--code/theme%3Aminimal-scp-foundation-by-cocoonist-jp/1` on the draft host), and adds the frame. **Frame paragraph (the M-frame addition):** the candidate's frame (candidate L5–8) carries `priority=1` with `theme=` naming the same /1 delivery, written on the production host (`https://scp-jp.wdfiles.com/local--code/theme%3Aminimal-scp-foundation-by-cocoonist-jp/1`). Priority 1 is the theme's own layer, the only layer this self-contained theme has. T4 found no frame (LOCALIZE-ROWS row 272, type 6); FIX4-IWA (commit 8c62b7b) installed it, and the ledger records P6 FIXED. The candidate has exactly one `[[code]]` block, so both delivery lines' /1 address names the block that holds the CSS — verified against the census, not assumed. The two lines' host forms differ (the head import is the draft form, the frame's `theme=` is already the posting form); both name the same fragment.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame). The exhibit-plus-import form is the campaign's standard delivery for a theme whose original inlines its CSS: it makes the delivered bytes a single addressable fragment the frame and the import can share. The draft-host import is KB-41, class (iii); the frame's production-host form is a posting-procedure reference, class (ii) — the pair is T1's one pseudo-ref error (section 11).
- **Verify:** `grep -n 'local--code' candidate.txt` — L2 and L7; `grep -c '\[\[code' candidate.txt` — one; read candidate L46–50 for the exhibit head the fragment serves.
- **Disposition:** FIXED (P6, FIX4-IWA); the delivery lines are DISPOSITIONED (classes (iii) and (ii) by form).

### 4. Fonts and assets

- **What:** The font load is consolidated (blocks B8–B10). The original's eighteen `@font-face` blocks (original L48–191, all for family Lora: italic and normal, weights 400/700, subset woff2 files on fonts.gstatic.com with unicode-range splits) are deleted, and the exhibit opens with one Google Fonts css2 `@import` (candidate L50) loading Lora (400;700, italic and normal) together with Noto Serif JP (400;600;700). The theme's one font stack (original L207 area → candidate L92) becomes `Lora, 'Noto Serif JP', 'Yu Mincho', 'Hiragino Mincho ProN', Georgia, Garamond, Times, serif` — Lora kept first (it is the theme's design face and covers Latin), the JP serif fallbacks added behind it. The candidate's prose discloses the JP font set in its own section (candidate L41–42: 使用フォント（SCP-JP 版）, Lora / Noto Serif JP, Google Fonts / SIL Open Font License). Assets: the theme references no image files on either side; there is nothing to re-host.
- **Why:** P7/T5 with KB-16 (the font load gap): the original's Lora subsets carry no Japanese coverage, so a JP face must be loaded and named in the stack or Japanese text falls back unpredictably; the css2 import serves the same Lora the eighteen blocks served, so the consolidation loses no face, weight, or style — it replaces eighteen subset declarations with the one variable request that covers them. The `@font-face` deletion is a load-mechanism change, not a dropped font.
- **Verify:** `grep -c '@font-face' original.txt candidate.txt` — 18 and 0; read candidate L50 and L92; the stack's first family is the family the import loads.
- **Disposition:** Applied (load and stack); no asset dispositions needed.

### 5. Header, sidebar, and site furniture

- **What:** No header variables are overridden on either side: no `--header-title`, `--header-subtitle`, or `--logo-image` exists in the original or the candidate — the theme styles the site's existing header elements directly (its `#header h1` rules open the CSS body on both sides), and those rules travel verbatim inside the exhibit. The theme's sidebar and footer rules likewise carry over unmodified apart from their relocation (section 3); no P8 layout adaptation was needed, and the render row's sidebar-unreachable reading is the cross-cutting mobile shape recorded in section 11, not a rule in this file.
- **Why:** P9/T6 is a per-theme judgment and none was needed: the original sets no JP-facing header text to convert. KB-57 and ruling 2 are not engaged: no header string was kept in the original's language, because there is none.
- **Verify:** `grep -n -- '--header-\|--logo' candidate.txt` returns nothing; compare the exhibit's opening rules (candidate L51–60) with the original's module head (original L22–31).
- **Disposition:** Standing.

### 6. Text translation

- **What:** The body prose is translated throughout (blocks B2, B4, B6, B7): the title (누에의 미니멀 테마 템플릿 페이지 → CocoonistのSCP財団ミニマルテーマページ, candidate L12), the description (candidate L27, with the hotpotato link treated in section 7), the usage instructions (candidate L30), and the external-links section (candidate L35–39: the Userstyles.org notice translated, both style links kept, their labels translated — 原テーマ and CNメンバーによる改変テーマ). One reader-visible CSS string is translated inside the exhibit (block B11): `content: 'Non-titled Post'` → `content: 'タイトルなしの投稿'` (original L657 → candidate L541). The port adds one prose section with no original counterpart, the JP font note (candidate L41–42, section 4). Korean survives in the candidate in exactly two places, both quotations: the credit block's original-title field (candidate L20) and the porter comment's quoted theme name (candidate L49, section 10). R5 glyph-form conversion: none — the source is Korean.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`). The untitled-post string is the kind of string a skim misses: it renders in the thread view wherever a post has no title, so it is counted here rather than waved through with the CSS body.
- **Verify:** Read candidate L27–43 against original L7–19; a Hangul scan of candidate.txt returns only candidate L20 and L49.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the two quotations.

### 7. Links

- **What:** Three link treatments. (1) The credit block's source link (candidate L22) — the per-theme record's subject: as judged it named the dead host `scp-wiki-ko.wikidot.com`; it now names `scpko.wikidot.com`, the host review/sources.tsv records for the original. (2) The description's hotpotato link: the original's same-wiki wikilink `[[[hotpotato|주간 뜨거운 감자]]]` (original L7) becomes an absolute link to the KO page, `[*https://scpko.wikidot.com/hotpotato 週刊ホットポテト]` (candidate L27) — T4's type-11 item (an unannotated cross-branch link, low severity), which the ledger dispositions P11 as the sibling / batch-posting class: the series' hub is a KO page with no JP counterpart, and the link serves. (3) The Userstyles.org pair (candidate L38–39): kept byte-identical URLs, labels translated (section 6); both are the theme author's own distribution pages, named in the original as external references.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard — which is also the standard the source link failed until its repair (probe pair in the per-theme record).
- **Verify:** `grep -n 'wikidot.com\|userstyles' candidate.txt` — the source link, the hotpotato link, and the two Userstyles URLs.
- **Disposition:** The hotpotato link DISPOSITIONED (P11); the Userstyles links standing; the source link repaired (per-theme record).

### 8. Structure

- **What:** The closing rule is bent in one named place and holds elsewhere. Bent: the CSS body's channel changes — live module in the original, code exhibit plus import in the candidate (section 3) — a delivery rebuild, not an interleaved edit: inside the exhibit, variable names, selectors, and rule order are preserved from the original's module, and the JP changes inside it are exactly the font import at its head (candidate L50), the one stack line (L92), and the one translated string (L541). The exhibit census confirms the rest of the page's shape: the gate, the title block, the prose sections in the original's order (description, usage, external links), and the source-code collapsible the candidate adds to hold the exhibit. Nothing the original carries was dropped: the `@font-face` run is a load consolidation (section 4), and a brace-depth scan of the candidate's CSS closes at depth 0 with no negative excursion, so no rule is swallowed by a displaced brace.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape; here the census and the depth scan, not the DELIVERY-MOVE label, decide.
- **Verify:** Compare `grep -n '\[\[module\|\[\[code\|\[\[iftags' original.txt candidate.txt`; the rule sequence inside candidate L51–613 against original L22–728.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as its own class: the classifier finds no whitespace-only block and no re-indentation (0 and 0). The line-count delta (−111 net) is accounted for by the `@font-face` consolidation (−144) against the added furniture (+47 added lines: delivery head, frame, credit block, font note, exhibit wrappers), not by formatting churn, so the R7 follow-up-diff hazard is not triggered beyond the delivery rebuild itself.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** diff.md's counts (+47/−163, 5 hunks) against sections 3–4's accounting.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation: candidate L49, at the head of the code exhibit — the port provenance comment, naming the theme, the original's URL, and revision 5 (`/* SCP-JP port of the Korean branch theme "누에의 미니멀 테마". Original: https://scpko.wikidot.com/theme:minimal-scp-foundation-by-cocoonist (rev 5). */`). It rides inside B8's delivery block, which is why no separate annotation signature fired. Its URL carried the same non-serving host form as the credit source link until the same repair corrected both (per-theme record). The JP font note (candidate L41–42) is porter-written prose, but it sits in the body as a disclosed section, not as a comment, and is counted in section 6.
- **Why:** R2: porter-added text is part of the change record; this comment is the exhibit's only in-file provenance statement.
- **Verify:** Read candidate L49.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's one pseudo-ref error: the delivery references (candidate L2, L7) — class (ii)/(iii) by form (the frame's production-host `theme=` is a posting-procedure reference; the head module's draft-host import is the sanctioned draft form, KB-41); fix lanes never "fix" them in the candidate. (2) The render row's items, all cross-cutting or capture-layer, not charged to the candidate: the page's overflow readings at 320/375 with hidden-footer and sidebar-unreachable (KB-33/KB-34 families); the sample's hidden-* cluster, four of whose eight combos carry an http.cat-only hotlink line (KB-44: a transient Wikidot 503 capture, not a result); and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5). (3) T4's type-11 hotpotato link, dispositioned P11 (section 7). T4's other two items are not dispositions: the frame (type 6) is FIXED (section 3) and the source link (type 3) was repaired after the verdict (per-theme record). The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record; the ledger §(c3) line for this theme reads P3 FIXED / P6 FIXED / P11 DISPOSITIONED.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 277): exit 1, 1 error / 1 warn / 1 info; the one error is pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO5)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 272): FINDINGS jointly, display-affecting findings 3 (the source link, the missing frame, the hotpotato link); the ledger §(c3) line records the frame and credit outcomes as FIXED and the link as DISPOSITIONED, and the source link's repair is the per-theme record. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +47/−163 in 12 change blocks / 5 hunks; the brace-depth scan of section 8 was run for this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:minimal-scp-foundation-by-cocoonist-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 273; go-sign, COMPLETION-REPORT §10) — for the pre-repair file; see the per-theme record for the two later commits.

## Per-theme record

### The source link (T4's type-3 finding, repaired after the verdict)

LOCALIZE-ROWS row 272 records the finding in the lane's words: type 3, 元記事リンク破損 — the source-article link is broken — one of this theme's three display-affecting findings. The bytes at the FIX5 head bore it out: the credit block's source link and the porter comment both named `scp-wiki-ko.wikidot.com`, the KO branch's old host. The repair landed after the verdict, as canonical commit 2a8a125: the one-word host correction (scp-wiki-ko → scpko) in both places in this candidate (credit link now candidate L22; comment now candidate L49), and in the four sibling candidates carrying the same defect (theme:jiha-jp, theme:kcia10-jp, theme:legend-of-blue-jp, theme:king-s-palace-jp), each probed the same way on 2026-11-17 (the old host returns 404 for the theme page; `scpko.wikidot.com` returns 200 and serves the page this package's mirror was taken from). This package documents the corrected candidate; its diff and stamp are computed against the corrected bytes, which is why the stamp reads STALE and names b5cb724 — the second post-verdict commit, the usage sweep's one-line correction of the escaped usage example (candidate L32) to this candidate's `-jp` posting name. Neither post-verdict change touches delivery, CSS, or credit content beyond the link's host word.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-minimal-scp-foundation-by-cocoonist-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 누에의 미니멀 테마
- **Author:** Cocoonist
- **Source:** https://scpko.wikidot.com/theme:minimal-scp-foundation-by-cocoonist — revision 5
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
