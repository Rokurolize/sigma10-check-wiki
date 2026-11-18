# Review package — theme:jiha-jp (KO → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:jiha-jp — origin KO, population #269 [GOSIGN2-LEDGER (b) row 269]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 54fb1acce3aa7d2cb27e9daefc6875567760f9835026a8fd2ddc0ec937ceb908); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 3 warns / 1 info (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 273; GOSIGN2-LEDGER (b) row 269]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample hidden-* cluster + sidebar-unreachable confined to chromium-320, whose only hotlink host is http.cat = transient 503 capture, not a result; sample credit-modal (preview-form); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO5))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 268, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 268]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 269]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:jiha-jp.txt sha256:54fb1acce3aa7d2cb27e9daefc6875567760f9835026a8fd2ddc0ec937ceb908; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 269) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×7 (class (ii), section 11); the render row's three items (KB-40 / KB-44 / KB-32, section 11); T4's one display-affecting finding is flagged in the per-theme record, not hidden |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:jiha | theme:jiha-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 11 (first translation; the candidate's credit block records 初訳時参照リビジョン: 11) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-jiha.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:jiha-jp.txt`, copied at worktree HEAD 939d257 |
| Lines / bytes | 903 lines / 19,994 bytes | 894 lines / 21,141 bytes |
| SHA-256 | 8849387cec2d8e94e8297d7ff971f6a1aef86098dbf18d3efbcc71eef5d37a31 | 796568cb888a61560d1ed56f7e0fbf526a7836f6117ed9c10b1026231804e2cf |

Wave history: the candidate was created by the Stage 2 KO5 integration (commit 3c781b1, the LOCALIZE-S2-F wave's port) and has exactly one later commit, f1138e4, whose jiha hunk is a one-line credit-field correction (the translator field taking its ruling-3 form, section 1). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

This is the mechanical end of the campaign: a standard port whose changes are the standard classes, applied once each, with no defect repair and no structural surprise. The original is a self-contained KO theme page (two own code blocks, self-delivered by local--code imports, a bare Rate module and an info block for its credit). The candidate swaps the credit furniture for the JP preview credit block, rebuilds the delivery as the wave-standard interwiki-style frame on the draft host, replaces the Korean webfonts with a JP font load and JP stacks, repoints every include and asset to the JP side, and translates the exhibit body. Measured churn (diff.md, the generator's difflib count with autojunk off: +103/−112, 215 changed lines in 59 change blocks / 22 diff sections; a GNU-diff count of the same pair gives 217 changed lines, +104/−113 — the difference is alignment choice, not content). One item deserves a reviewer's eye rather than a skim: the credit block's source link named a host that did not serve the original, which is T4's one display-affecting finding for this theme. It is recorded in the per-theme record with its probe evidence, and the repair has landed (see there).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 59 change blocks — 33 specific (55.9%), 20 heuristic (33.9%), 6 residue (10.2%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 17 |
| TRANS-UNANCHORED | 17 |
| CSS-BODY | 8 |
| DRAFT-HOST | 7 |
| SELF-DELIVERY | 4 |
| INCLUDE-REPOINT | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| INFO-DEL | 2 |
| LINK-REPOINT | 2 |
| ASSET-REHOST | 1 |
| BARE-RATE-DEL | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 6 residue blocks resolve as 4 one-line translations (section 6) and 2 blank-line deletions (section 9); the 8 heuristic CSS-BODY blocks are all P7 font-stack rewrites (section 4); the 11 primary TRANS-UNANCHORED blocks are one-line prose translations, verified line by line (section 6); the 2 EXHIBIT-RESTRUCTURE primaries are include repoints, not exhibit changes (sections 2 and 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:jiha-jp; original theme:jiha on scpko at reference revision 11; candidate `pages/theme:jiha-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself moved: the original opens with its tag gate `[[iftags +테마]]` (original L1) ahead of its delivery module (L3–5); the candidate opens with the delivery frame (candidate L1–7) and places the localized gate `[[iftags +テーマ]]` after it (candidate L9).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization), the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for jiha-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L7) plus an `:scpko:info:start`/`end` pair (original L9–20) whose body carries the credit prose in Korean: the title, the author (thd-glasses), the all-images note, and a fonts-used list pointing at noonnu.cc. The candidate deletes both (blocks B3–B5) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L11–20) carrying the eight ruling-3 fields (title 埋もれたテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 파묻힌 테마; 著作権者 thd-glasses; 作成年 2025; 初訳時参照リビジョン 11; the source link, on which see the per-theme record). The info block's non-credit content survives as body prose directly below: the images line, translated (candidate L22), and a JP fonts-used list (candidate L24–26) that replaces the KO list, whose noonnu.cc links disappear with the fonts they credited (section 4). The section's CSS half is the tail module (candidate L887–894, block B59): one hover rule for the credit button, restated for the JP credit module's DOM (see section 10 for its comment).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become), and the info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields and the translator credit form; the file's last commit (f1138e4) is exactly that form arriving (翻訳責任者: SCP-JP → AI). T7 (KB-11/KB-12): the KO theme styles the credit anchor through a `<p>` wrapper (`.creditButton p a`, present in the original's own CSS), but the JP credit module emits the anchor as a direct child of `.creditButton`, so the hover rule is restated against the JP structure with its declarations unchanged — the R6 in-place correction, delivered as an appended module rather than by editing the inherited rules.
- **Verify:** `grep -n 'info:start\|info:end\|module Rate' candidate.txt` returns nothing; read candidate L11–20 against the eight fields; the KB-11 recipe confirms the tail module's selector matches the JP credit DOM form.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified). The source-link field is the one item in this block that T4 later flagged; it is carried openly in section 11 and the per-theme record.

### 2. Includes and components

- **What:** Three repoint blocks, and no other include change. B8: the usage example's include, `:scpko:theme:jiha` → `:scp-jp:theme:jiha` as built (original L30 → candidate L36): the wave repoint changed the branch prefix but left the plain name, so the example named a page that does not exist on scp-jp; the usage-example population sweep has since completed the reference to `:scp-jp:theme:jiha-jp` (per-theme record), and this package documents the corrected candidate. B14: the image-block exhibit's include, `:scpko:component:image-block` → `:scp-jp:component:image-block` (original L61–63 → candidate L67–69; its asset and caption are sections 4 and 6). B58: the closing furniture pair after `[[/iftags]]`, `:scpko:component:centered-header-sigma-9` and `:scpko:component:toggle-sidebar` → their `:scp-jp:` forms (original L899–900 → candidate L884–885). The credit includes (section 1) and the interwiki-style include (section 3) complete the candidate's include list; every include in the candidate names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; a kept `:scpko:` include is a foreign-include error, class (i), and all three targets have verified JP counterparts (for B8, this candidate itself under its posting name, theme:jiha-jp), so all three are repointed and none is kept as an exception; B8's repoint as built stopped at the branch prefix and was completed by the population sweep. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — seven includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS by two live self-imports from scpko.wdfiles.com: `local--code/theme:jiha/2` in the head module (original L4) and `local--code/theme:jiha/0` in the tail module (original L902); the head import is repeated as a usage exhibit at original L111 (escaped, documentation only). The candidate replaces both with the wave-standard frame at the head (candidate L1–7, blocks B1–B2): a `[[module CSS]]` importing the candidate's own `local--code/theme%3Ajiha-jp/1` from the draft host (candidate L2), and an interwiki-style include at priority 1 with `theme=` naming the same /1 delivery (candidate L4–7). The candidate's tail module imports nothing; it carries the T7 correction (section 1). The single-index frame is the producing wave's convention, not a per-theme omission: the sibling KO candidates carry the identical /1 frame (theme:bulgunae-jp, theme:chatscp-jp, theme:kcia10-jp in `pages/`), and this theme's T2/T3 record reports no unstyled-content finding. The usage exhibit is repointed in host only (candidate L117: `local--code/theme:jiha/2` on scp-jp.wdfiles.com, the posting form); its address keeps the original's name and index because the exhibit documents the snippet a user pastes, whose JP form is a posting-procedure matter.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame, priority 1 for the theme's own layer). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L2 and L6 live, L117 the exhibit; compare the sibling heads in `pages/`.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii); the exhibit's production-host form, class (ii) mechanics).

### 4. Fonts and assets

- **What:** Load (block B38): the original's three `@font-face` blocks (original L190–208 — Tenada, PyeongChang 700, PyeongChang 400, all served from fastly.jsdelivr.net noonfonts) are deleted, and the candidate loads two families in one Google Fonts `@import` at the head of its main code block (candidate L196): Black Han Sans and Noto Sans JP (400;700). Stacks (the 8 CSS-BODY blocks B41–B45, B53–B55, adjudicated to this section, plus the font line inside B56): all nine `font-family` lines in the theme's own CSS are rewritten — the display stack `'Tenada'` → `'Black Han Sans', 'Noto Sans JP', sans-serif` (candidate L241, L837) and the body stack `'PyeongChang'` → `'Noto Sans JP', 'Yu Gothic', 'Hiragino Kaku Gothic ProN', sans-serif` (candidate L271, L288, L299, L473, L784, L793, L849). Each rewritten line also corrects the original's recurring generic-family typo `san-serif` → `sans-serif`; the one doubled semicolon (original L863) is carried over unchanged. Assets: five image URLs move from `scpko.wdfiles.com/local--files/theme:jiha/` to the draft host's `theme%3Ajiha-jp` folder with file names unchanged (B40 `--lgurl` SCP_Nx50.png, candidate L201; B46 nexus50.png, L502; B47 nx50_btn.png, L522; B51 cgpch.png, L620; B52 cgpchtxt.png, L632), and the image-block exhibit's `name=` takes the same draft-host form (B14, candidate L68).
- **Why:** P7/T5 with KB-16 (the font load gap): the KO faces cannot render Japanese text, so the load and every stack that names them change together; Black Han Sans keeps a heavy display face in the heading role the original gave Tenada, and Noto Sans JP is the JP body face (its credit line is in the credit prose, section 1). P5 with KB-17 (asset hosts): the theme's own images are re-hosted to the JP side; the jsdelivr font loads disappear because the faces they served are gone, not as a separate host fix.
- **Verify:** `grep -n 'font-family' candidate.txt` — nine lines, all JP stacks, no Tenada or PyeongChang; `grep -n 'wdfiles' candidate.txt` against the asset list above.
- **Disposition:** Font load and stacks applied; the draft-host asset URLs are DISPOSITIONED (class (iii) draft form; posting rewrites them to the production host).

### 5. Header, sidebar, and site furniture

- **What:** One block: B39, the `--header-subtitle` value translated in place (original L212, "유사세계 시뮬레이션" → candidate L199, "疑似世界シミュレーション"). The candidate overrides no other header variable: there is no `--header-title` and no `--logo-image` (the logo travels as the `--lgurl` asset, host-repointed in section 4). The theme's sidebar and topbar rules are carried over unmodified apart from the font lines of section 4, and no P8 layout adaptation was needed: the candidate inherits the JP site furniture through the frame, and the theme's own furniture rules needed no structural change to sit on it.
- **Why:** P9/T6 for the variable itself; the value is reader-visible header text, so its translation is P10/KB-18 carried in a string variable (the reader-visible half of R1). KB-57 and ruling 2 are not engaged: the subtitle was translated, not kept in the original's language.
- **Verify:** `grep -n -- '--header-' candidate.txt` — one line; read original L211–216 against candidate L198–203.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The exhibit body is translated throughout, in three counted groups. Fifteen TRANSLATION-ANCHORED blocks (B6, B12, B13, B16–B18, B21, B24, B27, B31, B35–B37, B49, B50): tab titles, the heading-level samples (B13), the table sample (B16), the collapsible labels (B37, B50: 펼치기/접기 → 展開/折り畳む), and the closed-tabview instructions (B35). Eleven TRANS-UNANCHORED blocks (B7, B9, B20, B22, B23, B26, B28, B30, B32–B34), each a one-line prose or exhibit-string translation, verified line by line against the mirror for this README. Four of the six classifier-residue blocks are the same shape and are counted here, not in the appendix: B10 (tab title 対応構文一覧), B11 (tab title 基本構文), B15 (the 水平線 heading sample), B19 (the pseudo-tab body word 内容). The one reader-visible CSS string is B56's `content:` ("맨 위로" → "上へ", candidate L848). Korean survives in the candidate on exactly two lines, both quotations: the credit block's original-title field (candidate L15) and the porter comment's quoted theme name (candidate L195, section 10). R5 glyph-form conversion: none — the source is Korean, and no retained string changes glyph form.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`). The unanchored and residue groups are where a silent deletion would hide, which is why each was read individually rather than waved through as a class.
- **Verify:** The pairs are diff.md's body sections in order; a Hangul scan of candidate.txt returns only candidate L15 and L195.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the two quotations.

### 7. Links

- **What:** The two LINK-REPOINT-labeled blocks are exhibit text, not navigation. B12's component list keeps the component page names and translates their link text (candidate L55–56); B29 translates the placeholder strings inside the stand exhibit's sample code (original L131–133 → candidate L137–139: リンクタイトル, リンク先, 引用文). No prose link in the candidate targets a KO-wiki page. The candidate's one live outbound link is the credit block's source link (candidate L19), which names a host that does not serve the original — that is T4's finding, recorded in section 11 and argued in the per-theme record.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; exhibit placeholders are sample text and follow P10 instead, which is what the bytes show.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Exhibit text standing; the source link is the flagged item of section 11.

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and channel order are preserved; the candidate's two code blocks sit where the original's sit (original L188 and L592 → candidate L194 and L578), and the JP corrections arrive as the head frame (section 3) and the appended tail module (section 1), not interleaved into the inherited CSS. The classifier's two EXHIBIT-RESTRUCTURE primaries adjudicate to section 2's include repoints: in B14 the image-block exhibit keeps its include, its image, and its caption (translated); in B58 the closing component includes keep their components. An exhibit census confirms the shape: the tabview and its tabs, the pseudo-tab exhibits, the stand exhibit, and both code exhibits are present on both sides in the same order — nothing was dropped or replaced, so the R3 question (sanctioned replacement vs silent deletion) does not arise for this theme.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two blocks, both single blank-line deletions at the tails of the two code blocks: B48 (original L576, the blank line between the main CSS's last rule and its `[[/code]]`) and B57 (original L890, the same position in the extension block). The classifier finds no whitespace-only block pair and no re-indentation anywhere else (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The diff sections at original L570–577 and L885–891 in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotations, both CSS comments with no original counterpart. (1) Candidate L195, at the head of the main code block: the port provenance comment, naming the theme, the original's URL, and revision 11; it rides inside B38's font-load block, which is why no separate annotation signature fired. (2) Candidate L888, in the tail module: the credit-correction comment, explaining that the KO theme styles the credit anchor through a `<p>` wrapper while the JP credit module emits the anchor as a direct child, and that the declarations are unchanged (the rule it introduces is section 1's T7 restatement). The skeleton's "none" for this section does not survive contact with the bytes and is corrected here.
- **Why:** R2: porter-added text is part of the change record, and annotation (2) is load-bearing — it is the only in-file explanation of why the tail module exists. Annotation (1)'s URL carries the same non-serving host form as the credit source link (per-theme record).
- **Verify:** Read candidate L195 and L888.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's seven pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host local--code and local--files lines and the exhibit's production-host line (sections 3–4); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. (2) The render row's three items, all environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample's hidden-* cluster and sidebar-unreachable reading confined to chromium-320, whose only hotlink host is http.cat (KB-44: a transient Wikidot 503 capture, not a result); and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5). (3) T4's one display-affecting finding, the credit source link: recorded by LOCALIZE-ROWS row 268, still present in the bytes at the FIX5 head (candidate L19), and flagged in the per-theme record with its probe evidence. The ledger's determination for this theme is PASS and this package does not re-open it; the flag is the documentation doing its job, because a reviewer following the credit dialog today reaches a 404.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 273): exit 1, 7 errors / 3 warns / 1 info; all seven errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO5)): FINDINGS, the three items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 268): FINDINGS jointly, display-affecting findings 1 (the source link), no display-collapse item; the ledger §(c3) line records the theme's T4 outcome as the P3 credit fields FIXED by the credit waves. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +103/−112 in 59 change blocks / 22 diff sections; the GNU-diff count of the same pair is 217 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:jiha-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 269; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The source link (T4's one display-affecting finding)

LOCALIZE-ROWS row 268 records the finding in the lane's words: type 3, 元記事リンク破損 — the source-article link is broken, and from the attribution dialog the original cannot be reached — display-visible, with the T5 note that the link's label is the word ソース. The bytes at the FIX5 head bear it out. Candidate L19 reads `**元記事リンク:** [*https://scp-wiki-ko.wikidot.com/theme:jiha ソース]`, and the porter comment at candidate L195 names the same host. Probe made for this package (2026-11-17): `https://scpko.wikidot.com/theme:jiha` serves the original page, whose content matches this package's mirror; `https://scp-wiki-ko.wikidot.com/theme:jiha` returns 404. The campaign's own provenance records (review/sources.tsv, the mirror store index) name scpko.wikidot.com as the original's host. So the link as written cannot be followed, exactly as the localize lane recorded, and no later wave repaired it: the candidate file has two commits (the KO5 integration 3c781b1, which set the link in this form, and f1138e4, whose only jiha hunk is the translator field). The ledger's §(c3) disposition line for this theme records only the P3 credit-fields fix, and the theme's determination is PASS; this package therefore carries the finding as a flagged item rather than a silent pass. The repair has since landed: canonical commit 2a8a125 makes the one-word host correction (scp-wiki-ko → scpko) in both places, in this candidate and in the four sibling candidates carrying the same defect (theme:kcia10-jp, theme:minimal-scp-foundation-by-cocoonist-jp, theme:legend-of-blue-jp, theme:king-s-palace-jp), each probed the same way (old host 404, scpko 200). This package documents the corrected candidate; its diff and stamp are computed against the corrected bytes.

### The usage example's posting name

The usage example at candidate L36 as built read `@@[[include :scp-jp:theme:jiha]]@@`: the porting wave's repoint changed the branch prefix from `:scpko:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6; the sweep's probes corroborate: the plain form returns 404 on the check wiki and on live scp-jp, and theme:jiha-jp returns 200 on sigma10-jp-test). The usage-example population sweep has since completed the reference to `:scp-jp:theme:jiha-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design, as it already did for the source-link repair above.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-jiha-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 파묻힌 테마
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/theme:jiha — revision 11
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
