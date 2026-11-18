# Review package — theme:inland-empire-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:inland-empire-jp — origin CN, population #199 [GOSIGN2-LEDGER (b) row 199]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 743163107d1548af7f34fdfffa811ba621dda1d1a8505759b1ab17152950a69f); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 3 warns / 2 infos (hotlink×5, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 229; GOSIGN2-LEDGER (b) row 199]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-login (4 combos) + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN8))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN8))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 198, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 198]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 199]
- Computed against: canonical commit 1c96ee4f6dbe58243d8c4ba0136a4a4dde806972; candidate file pages/theme:inland-empire-jp.txt sha256:743163107d1548af7f34fdfffa811ba621dda1d1a8505759b1ab17152950a69f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 199) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×5 (the CN-side asset set, class (ii) / KB-58, section 4); T4's P11 red link (section 7); the render row's environment-layer items (KB-40, section 11) and its recorded coverage caveat (the sample's T2 run returned no machine verdict, section 12) |
| Record correction | The sources.tsv note for this row claims the original was superseded upstream after the reference revision (a "K5a-i" note). The campaign's own follow-up artifact refutes it: `gosign2-lanes/lane-oc-gs-localize-s2-D/diff-inland-empire-from25.txt` records "rev25 → rev25, no changes, no revisions in between". The mirror at revision 25 is the original's current state, not a superseded one. The same note shape was already found wrong for theme:ambrose-chapter-two-jp; this README follows the artifact, and the discrepancy is flagged for the record layer |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:inland-empire | theme:inland-empire-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 25 (first translation; the candidate's credit block records 初訳時参照リビジョン: 25; the follow-up artifact confirms no later upstream revision exists) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-inland-empire.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:inland-empire-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 1,102 lines / 26,251 bytes | 1,119 lines / 28,103 bytes |
| SHA-256 | a8207f80970bcfe70a48bf1ba1c94c56a1ab3a58a04b5ecf31b8ad9a4b3d7ce67 | 29e24545828ecab1d86f8e4794579d5ebe95e5c97478b6de7c4d634685cd128b |

Wave history: the candidate was created by the Stage 2 CN8 integration (commit e469417, the LOCALIZE-S2-D wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D: the campaign-wide translator-attribution normalization, 163 files). No FIX5 commit touches this file.

## Summary

A large CN Sigma-9 theme (its exhibited CSS body alone is 913 lines) whose port the localize lane itself recorded as exemplary in structure: the CN lang frame is gone, an external CN font delivery on deno.dev is excluded, JP fonts are loaded and named, the prologue is translated, the labelled paired Rate exhibit is kept under its recorded exception, and the credit block carries the full field set. Measured churn (diff.md, Tier 2 format; the generator's difflib count with autojunk off: +211/−194, 405 changed lines in 130 change blocks / 29 diff sections). The block count is dominated by counted classes: 49 whitespace-only blocks (all of them blank-line padding inside the code body), 36 anchored and 34 unanchored translation blocks (the CN→JP prose and comment mass), and 19 comment-text blocks. The semantic core is small: the delivery repoint, the credit furniture, the font replacement (the deno.dev CN font CSS out, Noto Serif JP / Noto Sans JP in), five kept CN asset lines, and one kept red link, the last two dispositioned in sections 4 and 7.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 130 change blocks — 98 specific (75%), 31 heuristic (24%), 1 residue (1%), 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| WS-ONLY | 52 |
| TRANSLATION-ANCHORED | 36 |
| TRANS-UNANCHORED | 34 |
| COMMENT-TEXT | 19 |
| T7-CREDIT-CSS | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| GLYPH-FORM | 2 |
| COLON-ENC | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| COMPONENT-SWAP | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudications applied for this README: the single CSS-BODY block is a P7 font-stack rewrite (section 4); the three T7-CREDIT-CSS blocks are the original's own credit-button rules re-emitted by alignment, not a supplement (section 1); the two EXHIBIT-RESTRUCTURE blocks are an include-line translation and the code exhibit's boundary (section 8); the two COLON-ENC spans are the kept percent-encoded asset URLs of section 4; the two GLYPH-FORM spans sit inside translated CSS comments (appendix). The one residue block is resolved in the appendix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:inland-empire-jp; original theme:inland-empire on scp-wiki-cn at reference revision 25; candidate `pages/theme:inland-empire-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind: standard; no production JP counterpart). The frame: the original opens with a head module importing its own CN local--code delivery (original L1–3), a second small module (the `strong` weight fix, original L5–9, kept verbatim on both sides), and the tag gate `[[iftags +版式]]` (original L11). The candidate keeps both head modules, repoints the delivery host (candidate L1–3), adds the interwiki-style frame at priority 3 (candidate L5–8), and localizes the gate to `+テーマ` (candidate L15).
- **Why:** Section 0 declares the provenance route; the gate tag is P2, the delivery repoint and frame are P4/P6 (section 3). The Status table's record correction also belongs to this frame: the provenance claim a reviewer would otherwise read in sources.tsv (original superseded upstream) is refuted by the campaign's own follow-up artifact, and the mirror's standing is "current at rev 25", not "stale copy".
- **Verify:** The sources.tsv row for inland-empire-jp; the follow-up artifact named in the Status table (campaign record, one read); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture has two parts: a labelled Rate pair near the head — `[[>]]`, the label `**评分：**`, `[[module Rate]]`, `[[/>]]` (original L13–17) — and the attribution in its prologue prose (the theme is Flea_ZER0's work, original L29). The candidate keeps the pair, with the label translated (**評価モジュール:**, candidate L18–21), and adds the JP credit block after it (`:scp-jp:credit:start-preview`/`end-preview`, candidate L27–38) carrying the ruling-3 fields: title 内陸帝国テーマ； original title 内陆帝国 版式； 著者 [[*user Flea_ZER0]]; 作成年 2024; 翻訳責任者 AI; 翻訳年 2026; 著作権者 Flea_ZER0; 初訳時参照リビジョン 25; 元記事リンク the scp-wiki-cn original, on the recorded host; plus a 使用フォント line declaring the two JP faces and their license (a supplement line, section 4). The author field was checked against the original's credit: the prologue names Flea_ZER0 alone as the theme's maker, there is no info module and no license box in the original, and no second creator appears anywhere — the field drops nobody. The candidate's code body also carries `#page-content .creditButton p a` rules (candidate L449–464, the classifier's three T7-CREDIT-CSS blocks): these are the original's own rules, not a supplement — `creditButton` occurs exactly twice in each file with the same selectors, and the blocks re-emit only on alignment deltas around them.
- **Why:** The kept pair is the recorded pattern-3 exception (the FIXPREP paired-exhibit list names inland-empire): a Rate shown beside its own label is the theme's exhibit furniture, kept deliberately rather than deleted as a duplicate; the credit block is the P3/T1 JP form added alongside it, and KB-09's duplicate rule is not engaged because the exception is the standing disposition for this shape. Ruling 3 fixes the credit fields.
- **Verify:** Read candidate L18–38; `grep -c 'creditButton' original.txt candidate.txt` — 2 and 2.
- **Disposition:** Standing (the pair, by the named exception); the credit block is the standard form, checker-verified in the sweep (the localize row records "8/8 credit" for this theme).

### 2. Includes and components

- **What:** The candidate's includes are the credit pair (section 1), the interwiki-style frame (section 3), and one component swap inside the exhibits: an image-block include repointed to the JP component form (block B15, original L66–67 → candidate L77–78), whose `name=` asset stays on the CN sandbox host (section 4). No foreign include survives: `grep` finds no `:scp-wiki-cn:` include target in the candidate.
- **Why:** P1 (KB-15). Ruling 4 is not engaged: the theme needs no component ported alongside it.
- **Verify:** `grep -n '\[\[include' candidate.txt`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original already delivers its own CSS by local--code (original L2 imports `scp-wiki-cn.wikidot.com/local--code/theme:inland-empire/1`), so there is no channel conversion here: the candidate repoints the same /1 delivery to the draft host (candidate L2) and adds the interwiki-style frame naming it at priority 3 (candidate L5–8) — priority 3 because the theme's own layer sits above the Sigma-10 base layers in this candidate's stack. One delivery line is deleted outright: the original's code body opened with an `@import` of a CN font stylesheet from `chinese-fonts-cdn.deno.dev` (original L189, the SourceHanSerifCN result.css); the candidate has no deno.dev line anywhere (the replacement is section 4's JP font load). The candidate's own delivery lines are the two draft-host lines (candidate L2 and L7).
- **Why:** P4/T9 (delivery served from JP hosts) and P6/T3 (the supplement frame). The draft-host form is KB-41, class (iii). The deno.dev exclusion is P5 from the delivery side: an external third-party font CDN has no place in the JP delivery set, and the localize row records the exclusion as part of this port's exemplary structure.
- **Verify:** `grep -n 'local--code\|deno' candidate.txt original.txt` — the candidate shows the two draft-host lines and no deno.dev; the original shows its CN delivery and the deno.dev import.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: the CN font delivery (section 3) is replaced by a JP load at the code body's head (block B56, candidate L203–205), and the stacks are rewritten to JP faces — the classifier's one CSS-BODY block is the title stack: `'Source Han Serif CN VF', serif` → `'Noto Serif JP', 'Source Han Serif JP', serif` (original L194–195 → candidate L210–211), a P7 font-stack rewrite wearing a heuristic label; the remaining stack lines ride inside the translation and whitespace mass of the code body. The credit block's 使用フォント line (candidate L37) declares Noto Serif JP and Noto Sans JP with their SIL OFL 1.1 license. Two GLYPH-FORM spans (blocks B57 and B114) sit inside translated CSS comments, where CN character forms became their JP forms as part of the comment translation (appendix). Assets: five lines stay on CN hosts, and they are exactly T1's hotlink×5 and the localize row's pattern-5 list — the image-block exhibit's `name=` on the author's sandbox storage (`scpsandboxcn.wdfiles.com`, the xiaomao2.png cat image, candidate L96), a background shorthand on `scpsandboxcn.wikidot.com` (ie_bg_bw.gif, candidate L283), a background image on the sandbox storage (ie_bq.gif, candidate L576), and the percent-encoded sequence GIF on `scpsandboxcn.wikidot.com` referenced twice (candidate L788 and L807; the classifier's two COLON-ENC spans are these lines' `theme%3A` encodings, kept identically on both sides).
- **Why:** P7/T5 with KB-16 for the fonts (the CN faces cannot render the JP text the port introduces, and the deno.dev delivery is excluded with them). The assets are P5/KB-17 territory dispositioned instead: class (ii), KB-58 — re-hosting is a posting-procedure step, and the files serve from the CN hosts today.
- **Verify:** `grep -n 'scpsandboxcn' candidate.txt` — the five lines above; `grep -n 'SourceHanSerifCN\|deno' candidate.txt` returns nothing.
- **Disposition:** Font replacement applied; the five asset lines DISPOSITIONED (class (ii) / KB-58, GOSIGN2-LEDGER §(c3): P5 DISPOSITIONED).

### 5. Header, sidebar, and site furniture

- **What:** None as candidate changes: the candidate sets no header variables of its own (the theme's header, sidebar, and topbar styling is the original's CSS, carried in the code body with section 4's font lines as the only furniture-adjacent deltas), and T4 recorded no P9 item for this theme. The render row's one page-side item (the hidden-login shape across four engine/viewport combinations) is an environment-layer property of the check wiki, recorded in section 11, not a furniture change.
- **Why:** P9/T6 not engaged; nothing to translate or repoint in the furniture variables because the theme defines none beyond its inherited CSS.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle\|--logo-image' candidate.txt` returns nothing.
- **Disposition:** None required.

### 6. Text translation

- **What:** The CN→JP translation mass, in three counted shapes. Anchored prose (36 blocks): headings, usage instructions, and exhibit labels with enough invariant anchors to pair line by line. Unanchored prose (34 blocks): the prologue (original L29 → candidate L40: the Flea_ZER0 attribution paragraph, translated in full), the usage lead-ins, and the long-tab sample lines (the same sample sentence translated across blocks B34–B44 — one repeated exhibit string, counted per occurrence). Comments (19 blocks): the code body's CN section comments translate to JP (/* 标题 */ → /* 見出し */, /* 顶栏菜单 */ → /* トップバーメニュー */, /* 折叠 */ → /* 折りたたみ */), porter-visible text under R1's rule that comments translate as part of the porter's working surface. The localize lane's T5 judgement covers this mass jointly with T4 (one verdict word for both in its row), and its row singles the prologue translation out as part of the exemplary structure.
- **Why:** P10 and KB-18 (reader-visible strings); R1 for the comments. CN→JP translation loses the anchor majority more often than EN→JP does (no shared vocabulary to anchor on), which is why the unanchored share is high; each unanchored block was read against the mirror for this README.
- **Verify:** The exhibit pairs are diff.md's body sections in order; the comment pairs are greppable (`grep -n '/\*' candidate.txt` against the original).
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** One kept red link and one repointed exhibit. The red link: the translated prologue links the theme's inspiration as `[[[theme:oneiroi-west|オネイロイ・ウェスト テーマ]]]` (candidate L40) — theme:oneiroi-west has no JP candidate in this set, so the link is red on scp-jp today; it is the localize row's pattern-11 finding, dispositioned as the sibling/batch-posting class (the link resolves when the sibling theme is posted, and rewriting the prose to avoid naming the inspiration was not the port's call). The repoint (block B51, original L159 → candidate L174): the link exhibit's examples are localized as a set — `theme:inland-empire` → `theme:inland-empire-jp` (the visited-link example now points at the candidate itself) and `SCP-CN-10000` → `SCP-10000-JP` (the new-link example takes the JP numbering form). The credit source link names the recorded host (scp-wiki-cn.wikidot.com, candidate L36).
- **Why:** P11: prose links take the JP counterpart or the serving original. The oneiroi-west link has no JP counterpart yet (the disposition's ground); the exhibit links do, and took them.
- **Verify:** `grep -n 'oneiroi\|\[\[\[' candidate.txt` — the prologue link and the exhibit pair.
- **Disposition:** The red link DISPOSITIONED (sibling / batch-posting class, GOSIGN2-LEDGER §(c3): P11 DISPOSITIONED); the exhibit repoints applied.

### 8. Structure

- **What:** No structural change to the exhibits. The census decides the two EXHIBIT-RESTRUCTURE blocks: B21 (original L85 → candidate L96) is the image-block exhibit line itself, whose caption translated while the exhibit (same image, same geometry) stands unchanged — the label false-fired on the include line; B55 (original L187 → candidate L202) is the code exhibit's opening boundary, where the deno.dev import's deletion and the JP font load's insertion re-aligned the exhibit's head. Every exhibit present in the original (the blockquote and div samples, the tabview with its repeated long-tab strings, the image blocks, the code body) is present in the candidate in the same order. Variable names and selectors are preserved throughout the code body; the corrections sit at its head (font load) and in its stacks, per the closing rule.
- **Why:** R3's adjudication, decided by the census rather than the label.
- **Verify:** Compare the exhibit sequences (`grep -n '^\[\[div\|^\[\[code\|include component:image-block' original.txt candidate.txt`).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** 52 blocks carry the WS-ONLY label and 49 take it as their primary: every one of the 49 sits inside the code body (blocks B60–B128's range, all in the code-css channel — the CN original's exhibited CSS pads its sections irregularly and the candidate's exhibit re-emits with normalized padding). No declaration, selector, or prose line changes in any of them. This is the R7 hazard in its pure form: a follow-up diff that re-pads the exhibit would manufacture apparent churn of exactly this size, and the count is recorded so that churn is recognizable.
- **Why:** R7: formatting churn is disclosed as its own class so it is never mistaken for semantic change.
- **Verify:** The classification's section 9 counts (WS-ONLY 52 labeled, 49 primary, re-indentation 0).
- **Disposition:** Standing (disclosed; no semantic content).

### 10. Porter annotations

- **What:** None — checked, absent. The candidate carries no `[!-- ... --]` notes and no port provenance comment; its comments are the original author's own section markers, translated in place (section 6). The port's provenance lives in the credit block and this package.
- **Why:** R2: porter-added text is part of the change record; here the porter added none in-file.
- **Verify:** `grep -n 'SCP-JP port\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's five hotlink errors and one pseudo-ref: the hotlinks are the CN asset set of section 4, class (ii) / KB-58; the pseudo-ref is the candidate's own draft-host local--code line (section 3), class (ii) posting-procedure. There is no class (i) error. (2) T4's two display-affecting findings: the P5 asset set (the same five lines) and the P11 red link (section 7), both dispositioned in the ledger. (3) The render row's items: the page's hidden-login shape (four combinations) and the runtime-hotlink chain are environment-layer — the runtime hosts arrive via the shared site theme chain, not the candidate (KB-40) — and the sample's T2 run returned no machine verdict (render_check exit 2, no summary), a coverage caveat the ledger records as not a theme defect (section 12 carries it as this package's one verification gap). (4) Two standing exceptions are claimed and named, not silent: the labelled paired Rate exhibit (section 1, the FIXPREP pattern-3 exception list) and the Status table's record correction (the sources.tsv supersession note refuted by the follow-up artifact).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); KB-40, KB-58; the sibling/batch-posting class), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3); the exceptions in item 4 stand as recorded.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 229): exit 1, 6 errors / 3 warns / 2 infos; five hotlink (the section 4 assets) and one pseudo-ref, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-F (CN8)): FINDINGS — the page's hidden-login and runtime-hotlink items (section 11(3)); the sample's T2 run returned no machine verdict (exit 2, no summary), so the sample half of T2 is a coverage gap, recorded in the ledger as a caveat rather than a pass; no credit-modal line is recorded for this theme. (c) T4/T5 (LOCALIZE-ROWS row 198): FINDINGS jointly, display-affecting findings 2 (the P5 assets; the P11 red link), and the row's own structural assessment is positive (the localization structure called exemplary, 8/8 credit fields); the ledger §(c3) line records both findings as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +211/−194 in 130 change blocks / 29 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, including the one gap.
- **Verify:** Re-run the checker on `pages/theme:inland-empire-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 199; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:inland-empire-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RATES — head-zone bare Rate removed (landing `1c96ee4f6dbe58243d8c4ba0136a4a4dde806972`, "pages: head-zone bare Rates removed in five themes", 2026-11-17; record `FIX-RATES.md`).** +0/−5. Same shape as horn: the five-line bare-Rate block is removed from inside the `[[iftags +テーマ]]` gate directly above the preview credit block. Residue kept, not edited: the combined heading `**評価モジュールとクレジットモジュール:**` now heads the credit block alone (the same coordinator wording call). Checker 6/3/2 → 6/3/1 (the `double-rate` info clears); every other finding unchanged in kind and count; class (i) 0.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-inland-empire-jp.txt` is the decoration sample the render checks ran against (its T2 run is the coverage caveat of section 12); it belongs to this theme's record but carries no port change of its own to explain here. The FIX-CREDIT-D commit (1869877) that normalized this candidate's attribution touched 163 files in one wave; the other 162 are those themes' own records, not this one's change set. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## Appendix — residue and low-signal blocks

Class M treatment: the residue and the low-signal shapes collapse into this table rather than per-block slots.

| Block(s) | Shape | Resolution |
|---|---|---|
| B130 (residue) | One added blank line at candidate L1116, the code exhibit's tail (the block's channels read body → code-css: a pure alignment tail) | No content; counted here so the residue count is zero after adjudication |
| B57, B114 (GLYPH-FORM, inside COMMENT-TEXT blocks) | CN comment lines whose characters took JP glyph forms as the comments translated (section 6's comment mass) | Translation surface, not a separate change class |
| B60–B128 subset (WS-ONLY, 49 primary blocks) | Blank-line padding deltas inside the code body | Section 9's counted class |
| B34–B44 subset (TRANS-UNANCHORED) | One repeated sample sentence (the long-tab string) translated at each of its occurrences | One translation decision, counted per occurrence by the classifier |

## License and attribution

- **Title:** 内陆帝国 版式
- **Author:** Flea_ZER0
- **Source:** https://scp-wiki-cn.wikidot.com/theme:inland-empire — revision 25
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
