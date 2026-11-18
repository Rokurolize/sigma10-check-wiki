# Review package — theme:walk-in-the-dark-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:walk-in-the-dark-jp — origin CN, population #243 [GOSIGN2-LEDGER (b) row 243]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 8ad895d99e2f82a5190886b3d83e6c0d9d5205fd218d0c0b2fd03e7682ff43d9); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 208; GOSIGN2-LEDGER (b) row 243]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 350px@320 + 382px@375 + 814px@768 (page; sample 884px@768) + runtime-hotlink site-theme chain + candidate hosts fastly.jsdelivr.net, scp-wiki-cn.wdfiles.com; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN17)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN17)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 242, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 242]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 243]
- Computed against: canonical commit f4488f2d2948824238a2d06479f104f4aab0cf5d; candidate file pages/theme:walk-in-the-dark-jp.txt sha256:8ad895d99e2f82a5190886b3d83e6c0d9d5205fd218d0c0b2fd03e7682ff43d9; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 243) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 + pseudo-ref ×1 (class (ii), section 11); the render row's items (overflow at three widths, KB-33/KB-34; candidate hosts on the runtime chain, KB-40 / class (ii)); T4 display-affecting 1. **Two items are flagged by this package beyond the ledger's record: the original's small live head module (four rules) has no counterpart anywhere in the candidate, and the candidate's font specimen lines claim Noto Serif JP for body and mono text whose variables still name Chinese faces that nothing loads (per-theme record). One further difference — the original's gated personal-wiki base include has no counterpart — is recorded as an observation with its evidence, not a flag (section 2).** The verdict stamp reads STALE because the candidate changed after the verdict in the usage-example sweep commit b5cb724 (section 12) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:walk-in-the-dark | theme:walk-in-the-dark-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 72 (first translation; the candidate's credit block records 初訳時参照リビジョン: 72) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-walk-in-the-dark.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:walk-in-the-dark-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 1,202 lines / 28,188 bytes | 1,188 lines / 29,304 bytes |
| SHA-256 | 1e947ddde12ece0af412f061b8ee5745b46dc966a356e2255dc02fe3edf0bf3e | d7ccd40536c6b8e4f87cf508b03b04faa3fac20536daac99971ee066f2d0f7c2 |

Wave history: the candidate was created by the Stage 2 CN17 integration (2e202fc, the LOCALIZE-S2-E wave's port), then touched by FIX-CREDIT-D (1869877) and the usage-example sweep (b5cb724). Provenance note (sources.tsv, class K5a-i): the original is recorded as superseded upstream since the reference revision, with a follow-up diff artifact in the campaign record — that artifact's actual content is reported in section 12, because it does not say what the note implies (the same wording tension as the other three K5a-i themes in this batch).

## Summary

A BHL-family dark theme whose original has the most distributed topology in the batch: a gated live include of the author's personal-wiki BHL copy, a small live head module with four rules, the main CSS in a code block delivered by a tail module, documentation after the code, and a hidden legacy style-frame embed at the tail. The candidate reorders the page into the campaign's order (credit and documentation first, code after), delivers its single code block by tail module plus frame, and translates the documentation — and the reordering is where this package's findings live, because two things did not survive it. The head module's four rules are simply absent: not in the code block the classifier's DELIVERY-MOVE note points at, not anywhere in the file (two of them target CN-only furniture, which may be the porter's unrecorded reason; the record does not say). And the font specimen lines were translated as claims — body and mono specimens now say "Noto Serif JP" — while the variables they describe still name '新宋体' and '仿宋'/'ZCOOL XiaoWei', and Noto Serif JP is loaded by nothing in the candidate, its base candidate, or the production BHL file. Measured churn is deceptive here: the generator's difflib count gives +210/−223 (433 changed lines) in only 17 change blocks / 3 diff sections, because the reordering aligns as a few enormous blocks; GNU diff sums +208/−222 (430). Both flags are set out with verbatim evidence in the per-theme record; this package changes nothing.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 17 change blocks — 7 specific (41.2%), 6 heuristic (35.3%), 4 residue (23.5%), 0 skipped. The block count is small and the residue share the batch's highest precisely because the page reordering merges whole regions into single blocks; the shares should be read with that in mind. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 5 |
| DELIVERY-MOVE | 3 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| GLYPH-FORM | 2 |
| SELF-DELIVERY | 2 |
| TRANSLATION-ANCHORED | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| IFTAGS | 1 |
| RESTORATION | 1 |
| TASL-FIELDS | 1 |

Adjudication of the heuristic mass: the six heuristic blocks are the reordered documentation mass and the CSS-BODY block; they were adjudicated region by region against the mirror, not by shape, because the DELIVERY-MOVE label is known to be able to hide a dropped module — and in this package it does (flag 1). The four residue blocks are all reordering residue and collapse into the appendix. The one RESTORATION label sits on the theme-squares block (section 8).

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:walk-in-the-dark-jp; original theme:walk-in-the-dark on scp-wiki-cn at reference revision 72; candidate `pages/theme:walk-in-the-dark-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard, with the K5a-i note of the Provenance table). Topology frame (the original, in page order): gate `+版式` at L1; a live base include at L2 *inside* the gate (section 2); a head module CSS at L3–21 (flag 1); the main CSS as a code block at L26–991, delivered by a tail module outside the gate; documentation after the code; a second, small code block at L1082–1086 (a documentation snippet); a hidden style-frame embed at the tail. The candidate reorders to: credit block, documentation (with the theme-squares include at its head), the single code block, tail delivery.
- **Why:** Section 0 declares the route and the full topology, because this package's two flags are both topology facts (a module that vanished in the reorder; a base include whose absence needs its evidence stated).
- **Verify:** The sources.tsv row for walk-in-the-dark-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at its head (candidate L3–12) with the eight ruling-3 fields: 著作権者 Etinjat — the name the original's own statements support; the code banner's 羽天一 is the same author's CN display name and is carried in the banner, and the 🐉 banner device is carried with it. The source-link field names the recorded host (scp-wiki-cn), so the host check passes with no probe needed. The original's `[[module rate]]` stood inside its front-title div; the candidate's front-title `[[=]]` region stands empty and the head credit block is the rate-bearing form that replaces it.
- **Why:** P3/T1 and ruling 3; the field-versus-banner check passes — the field's Etinjat and the banner's 羽天一 are one person under his two names, and both sides of the pair say so consistently.
- **Verify:** Read candidate L3–12; the banner is at the code block's head (candidate L208 region).
- **Disposition:** FIXED (ledger §(c3) class outcomes: credit fields FIXED by the credit waves); no credit item is flagged for this theme.

### 2. Includes and components

- **What:** Live includes: the credit pair (section 1), the tail interwiki-style frame (section 3, written `theme= ` with a space before the value — the file's own form, harmless), and the `theme-squares` include, which stands deep in the original's documentation (original L1004) and at the candidate's documentation head (candidate L23) with its color names translated and every variable value identical. The escaped usage examples (candidate L87–88) document the theme's contract as a two-include pair: `:scp-jp:theme:black-highlighter-theme` (the production BHL page) followed by `:scp-jp:theme:walk-in-the-dark-jp`. **The observation:** the original's L2 — `[[include :etinjat:theme:black-highlighter-theme]]`, the author's personal-wiki BHL copy, live inside the gate — has no counterpart in the candidate. The evidence that this is a contract change rather than a silent loss: the candidate's own usage examples name the production BHL page as the base a user applies first; the decoration sample includes the candidate alone (the BHL-family sample form, since delivery of the base is the user's first include); and the render rows record styled pages with no missing-base finding. The original's hidden tail embed (an iframe to `scp-wiki-cn.wdfiles.com/local--files/nav%3Aside/styleFrame.html?bhl`, the legacy BHL style-frame hack) is likewise gone; its function is the interwiki-style frame's, which the candidate has.
- **Why:** P1 (KB-15) and KB-01's family: a dependent theme's base must be the JP delivery — here the production BHL page, named in the usage contract rather than smuggled in as a gated include of a personal wiki. The observation is recorded with its evidence because the standing rule is that a missing base is a flag *unless* the contract shows where the base comes from; here it does.
- **Verify:** Candidate L87–88 for the contract; `grep -n 'etinjat\|styleFrame' candidate.txt` returns nothing.
- **Disposition:** Standing as an observation (evidence above); not flagged.

### 3. Delivery and code loading

- **What:** The candidate delivers its single code block (candidate L208–1177, headed by the porter comment of section 10) from the tail: a module CSS importing the draft host's `local--code/theme%3Awalk-in-the-dark-jp/1` (its `@import` lacks the trailing semicolon the original's has — harmless, as the block's last declaration) plus an interwiki-style frame at priority=1 naming the same /1. Census check: the candidate has exactly one `[[code]]` block, so the /1 address names the block that holds the CSS — correct. (The original's second code block, at L1082–1086, is a documentation snippet for the `cn-hr` element, not a delivery on either side; its region is residue block B14.) The DELIVERY-MOVE labels (×3) record the topology change — head module plus tail-delivered code, to tail-delivered code alone — and flag 1 is the proof that the label must be read, not trusted: one of the moved-looking regions is a deletion.
- **Why:** P6/T3 (the frame) and the delivery classes; the census is the deciding check and it passes for the block that exists.
- **Verify:** `grep -n 'local--code\|interwiki-style\|\[\[code' candidate.txt` — one code block, two delivery lines naming /1.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the dropped head module is FLAGGED (section 8, per-theme record).

### 4. Fonts and assets

- **What:** The header-family variables were partially localized: `--header-font`, `--sub-header-font`, and `--title-font` swap 'Noto Serif SC' → 'Noto Serif JP' (candidate L228 ff.). But `--body-font` (candidate L227) still reads `'新宋体',kaiti,monospace` and `--mono-font` (candidate L232) still reads `'仿宋','ZCOOL XiaoWei', monospace` — while the candidate's specimen lines (candidate L196–198) claim, in translation, 見出しフォントはNoto Serif JPです / 本文フォントはNoto Serif JPです / 等幅表示にはNoto Serif JP系のフォールバックを使います. Worse, Noto Serif JP is loaded by nothing: no `@import` or `@font-face` in the candidate names it, none in the base candidate (`review/black-highlighter-theme-jp/candidate.txt`, searched for this package), and none in the production BHL file (`pages-existing/existing:theme-black-highlighter-theme.txt`, also searched). Whether the production base *page* or the site chain loads it is not provable from this repo — which is itself the point: from the record that decides here, the claimed face is unloaded and two of the three specimen claims contradict the variables they describe. **Flagged** — per-theme record. Kept foreign delivery, class (ii) per the ledger: `--yxh-red-image` names `https://fastly.jsdelivr.net/gh/Etinjat/CSS@SCP/LOGO_YXH_red.svg` (candidate L257), `--hr-image` its `LOGO_CN_white.svg` sibling (candidate L259), the expected-display image stays on scp-wiki-cn.wdfiles.com, and `[[image Logo-YXH-red.png]]` is a bare page-attachment reference on both sides (KB-58).
- **Why:** P7 is a two-half class (load and apply, consistently described); this candidate applies a face it does not load to the headers, loads nothing for the body and mono, and describes all three as the JP face. A specimen line is documentation that makes a checkable claim about the CSS — when the claim and the CSS disagree, one of them is a defect.
- **Verify:** Candidate L196–198 against L227–232; `grep -n 'Noto Serif JP' candidate.txt` returns only the specimen and header-variable loci, no import.
- **Disposition:** **FLAGGED** (the specimen/variable/load contradiction, per-theme record); the foreign asset hosts are DISPOSITIONED (class (ii) / KB-58 family).

### 5. Header, sidebar, and site furniture

- **What:** The header variables keep the original's Chinese values verbatim (candidate L238–239 = original L55–56): `--header-title` "中華異學會", `--header-subtitle` "格異、治學、融會" — the fictional institute's name and motto, in-fiction proper nouns in traditional glyph forms; the credit block's two title fields likewise keep 圣人夜行 BHL 主题 in both. Two rendered `content:` strings remain in Chinese in the delivered CSS — "标签 " at candidate L789 (`"\f02c 标签 "`) and L890 (`"标签 ▼"`) — the tag-label furniture text. All of these stand under the ledger's class line for this theme (header language = ruling 2 family in the §(c3) class outcomes) and are recorded, not flagged: the institute's name is not a UI string awaiting translation, and the content strings ride with it as the class disposition provides.
- **Why:** P9 / ruling 2's scope is exactly this discrimination — designed in-fiction text versus untranslated UI — and the ledger has already drawn it for this theme's row charges.
- **Verify:** Candidate L238–239 against original L55–56; `grep -n '标签' candidate.txt` for the two content strings.
- **Disposition:** DISPOSITIONED (ruling 2 family, per the §(c3) class outcomes).

### 6. Text translation

- **What:** The documentation is translated throughout (2 TRANSLATION-ANCHORED blocks, 5 TRANS-UNANCHORED, the reorder merging most of it into few large blocks), including the theme-squares color names (values untouched, section 2) and the specimen lines — whose translation is flag 2's subject, because the specimens make claims (section 4). GLYPH-FORM ×2 localizes glyph forms inside samples. The banner is translated with the author's two names handled as section 1 records.
- **Why:** P10 and KB-18; specimens are documentation, so their translation is held to the documentation standard (true of the CSS they describe), not only the language standard.
- **Verify:** diff.md's three sections in order; the specimen lines are candidate L196–198.
- **Disposition:** Standing, subject to flag 2.

### 7. Links

- **What:** The credit source link (section 1) names the recorded host. The documentation's expected-display image and the two logo variables are asset references, recorded in section 4 as class (ii) kept delivery. No live prose link in the candidate targets a page that does not exist on its named host.
- **Why:** P11 under the dead-reference evidence standard; nothing here meets it.
- **Verify:** `grep -n 'http' candidate.txt` enumerates every URL.
- **Disposition:** Standing; no link item is flagged for this theme.

### 8. Structure

- **What:** The page is reordered (documentation before code) — the campaign's page order, against the original's code-before-docs — and the closing rule otherwise holds: the gate wraps the page, the delivered block is whole, the tail furniture corresponds. **Flag 1 (the dropped head module):** the original's module CSS at L3–21 carries four live rules — `.heritage-rating-module{display:none!important}`, `.unmargined{…}` (a utility class whose font stack names '等线'), `#breadcrumbs{text-align:center}`, and `#page-content.unmargined + hr{display:none}`. No counterpart exists anywhere in the candidate: `grep` finds neither "heritage-rating-module" nor "unmargined" in it, and the `#breadcrumbs` rule the candidate does carry (candidate L672, `#breadcrumbs, .pseudocrumbs {…}`) is a different, base-derived rule. Context the coordinator needs for disposition: two of the four rules target CN-only furniture (the heritage rating module; the `.unmargined` utility, which the candidate's documentation never uses), one is a one-line cosmetic (centered breadcrumbs), and one hides a rule under `.unmargined` pages. A deliberate CN-furniture removal is plausible — but it is nowhere recorded, and the classifier's DELIVERY-MOVE note for the region points at the code block's head, where the rules are not. The one RESTORATION label sits on the theme-squares block: the include stands at the candidate's documentation head, the position the campaign's order gives it, against the original's deep-docs position.
- **Why:** R3 and the silent-drop rule, in the exact shape the standing lessons warn about: a DELIVERY-MOVE label over a multi-module original must be checked module by module, and this one does not survive the check.
- **Verify:** Original L3–21 against a full-text search of the candidate for the two class names (both absent).
- **Disposition:** **FLAGGED** (the dropped head module, per-theme record); the reorder itself is standing.

### 9. Formatting only

- **What:** None at block level: no WS-ONLY block and no pure re-indent block (reindent_blocks 0). The tail module's missing trailing semicolon (section 3) is a form note, not a formatting change of consequence.
- **Why:** R7's ground for "none".
- **Verify:** classification.json's label counts for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation: the comment `/* ===== walk-in-the-dark ===== */` heading the candidate's code block (candidate L209) — the wave's standard block marker, naming the theme whose CSS follows. It is also the landmark that proves flag 1's negative: the code block it heads does not contain the dropped module's rules.
- **Why:** R2: porter-added text is part of the change record even when it is one line.
- **Verify:** Candidate L209.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The ledger items: (1) T1's three hotlink errors (the jsdelivr and wdfiles asset hosts of section 4) and one pseudo-ref error, all class (ii). (2) The render row's items: overflow 350px at 320, 382px at 375, and 814px at 768 on the page, 884px at 768 on the sample (KB-33/KB-34 family); the candidate hosts on the runtime chain (fastly.jsdelivr.net, scp-wiki-cn.wdfiles.com — KB-40 environment layer plus the class (ii) kept delivery of section 4). (3) T4 row 242: display-affecting 1. (4) The ledger §(c3) class outcomes for the LOCALIZE-S2-E rows (header language ruling 2; asset hosts class (ii); credit fields FIXED) and the population-check row (LEDGER-POPULATION-CHECK row 22). **Flagged by this package:** the dropped head module (flag 1) and the font specimen contradiction (flag 2). Neither is covered by a ledger disposition — the class outcomes address wording and hosts, not module survival or specimen truth — and neither disturbs the verdict: both are small candidate repairs (restore the rules or record their removal; align specimens, variables, and load) for the coordinator to land with a package refresh. The section 2 base observation is recorded with its evidence and is not a flag.
- **Why:** A disposition is a decision with grounds; an undispositioned drop is reported as a flag, not absorbed into a neighboring class outcome.
- **Verify:** Each item names its deciding record above; the flags' evidence is the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); **flags 1 and 2 are FLAGGED**.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 208): exit 1, 4 errors / 2 warn / 1 info — hotlink ×3 and pseudo-ref ×1, all class (ii); no class (i) error. (b) T2/T3 render (RENDER-ROWS-G, CN17): FINDINGS — the items of section 11(2). (c) T4/T5 (LOCALIZE-ROWS row 242): FINDINGS, display-affecting 1. (d) The K5a-i follow-up artifact (`gosign2-lanes/lane-oc-gs-localize-s2-E/diff-walk-in-the-dark-from72.txt`, read for this package): a six-line record whose content is "scp-wiki-cn:theme:walk-in-the-dark rev72 → rev72 変更： なし" with an empty intervening-revision table — it records **no upstream change after the reference revision**, against sources.tsv's "superseded upstream" wording; the artifact's bytes are followed here and the tension is reported in the batch report. (e) This package's own checks: the census (section 3), the dropped-module greps (section 8), and the three-file font-load search (section 4). (f) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares; the stamp reads STALE because the candidate changed after the verdict in the sweep commit b5cb724. Counts in this README are the generator's (difflib, autojunk off): +210/−223 in 17 change blocks / 3 diff sections; its own diff index and GNU diff both sum +208/−222 — a three-line alignment artifact in the reordered head region, recorded rather than smoothed over.
- **Why:** Verification claims name the cheapest deciding check and its result, including reading the artifact instead of its description.
- **Verify:** Re-run the checker on `pages/theme:walk-in-the-dark-jp.txt`; read the follow-up artifact at the path in (d).
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 243; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Flag 1 — the original's head module (four rules) is absent

Original L3–21 is a live `[[module CSS]]` carrying: `.heritage-rating-module{display:none!important}`; `.unmargined{…}` (with `font-family:'等线'` among its declarations); `#breadcrumbs{text-align:center}`; `#page-content.unmargined + hr{display:none}`. In the candidate, searches for "heritage-rating-module" and "unmargined" return nothing, and the only `#breadcrumbs` rule (candidate L672) is the base-derived `#breadcrumbs, .pseudocrumbs {…}`, a different rule. The classifier's DELIVERY-MOVE adjudication for the corresponding block suggests the content moved to the code block's head; it is not there (the code block opens with the section 10 marker and the theme's own `:root`). Disposition context for the coordinator: the heritage module and `.unmargined` are CN-site furniture with no JP counterpart in the candidate's documentation, so a deliberate removal is defensible — but it is unrecorded, and the breadcrumbs centering is a general cosmetic. Recommended: either restore the four rules at the code block's head, or record the removal and its ground in the candidate's documentation; the silent state is the defect.

### Flag 2 — the font specimens contradict the variables, and the claimed face is unloaded

Candidate specimen lines (L196–198) claim Noto Serif JP for headings, body, and mono fallback. The variables: `--body-font` (L227) `'新宋体',kaiti,monospace`; `--mono-font` (L232) `'仿宋','ZCOOL XiaoWei', monospace`; only `--header-font`/`--sub-header-font`/`--title-font` (L228 ff.) name Noto Serif JP. And Noto Serif JP is loaded by no `@import` or `@font-face` in the candidate, the base candidate, or the production BHL file (all three searched for this package). So even the header claim depends on a load this repo cannot show. Recommended repair: load Noto Serif JP (or name the base/site load that provides it) and align the body/mono specimens with the variables — or localize the body/mono variables to match the specimens. Any settled state is defensible; the current three-way disagreement is not.

### The base include: an observation, with its evidence

Recorded in section 2: the original's gated personal-wiki base include (`:etinjat:theme:black-highlighter-theme`, original L2) has no counterpart, and the candidate's contract is the documented pair (production BHL page first, then this theme) at candidate L87–88, with styled render rows and no missing-base finding. It is recorded as an observation rather than a flag because the contract is explicit in the candidate itself — the opposite shape from flag 1, where nothing in the candidate mentions the missing module.

## Appendix — residue blocks

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B4 | L15 | L18–21 | The front-title `[[=]]` region boundary, displaced by the reorder (R3) |
| B6 | L20–21 | L54–55 | The original's module close and a divider line, aligned into the reordered documentation (R3) |
| B8 | L23 | L63–65 | `@@@@` exhibit markers displaced by the reorder (R3) |
| B14 | L1086–1110 | L1177 | The documentation tail region (the cn-hr snippet's neighborhood) compressed at the code block's close by the reorder (R3) |

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:walk-in-the-dark-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-MP12 item 3 (a)(b) — head module restored, JP face loaded and applied (landing `f4488f2d2948824238a2d06479f104f4aab0cf5d`, "pages: skipos delivered channel, the-other-side fonts and subtitle, M-pure-12 repairs", 2026-11-17; record `FIX-MP12.md`).** +21/−2. (a) The original's live `[[module CSS]]` head rules (original L4–19), absent from the candidate, are restored verbatim — byte-exact including the trailing spaces on the `#page-content .unmargined + hr{` line — at the head of the delivered code block after the @imports and before `:root` (new L225–241): `.heritage-rating-module{display:none!important}`, `.unmargined{…}`, `#breadcrumbs{text-align:center}`, `#page-content .unmargined + hr{display:none}`. (b) A Noto Serif JP load is added at L223 beside the existing ZCOOL XiaoWei import (Google Fonts css2, probed once: HTTP 200, `text/css`); `--body-font` at L246 becomes `'Noto Serif JP', '新宋体', kaiti, monospace` (JP face primary) and `--mono-font` at L251 becomes `'仿宋', 'ZCOOL XiaoWei', 'Noto Serif JP', monospace` (JP fallback), making the file's font specimens true. Checker 4/2/1 before and after; the info `important` count rose 11 → 14 because the restored rules carry three `!important` declarations — the same finding, not a new one; no new class (i).

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-walk-in-the-dark-jp.txt` is the decoration sample the render checks ran against (it includes this candidate alone, the BHL-family sample form), and its findings are the sample half of section 11(2). The follow-up diff artifact `gosign2-lanes/lane-oc-gs-localize-s2-E/diff-walk-in-the-dark-from72.txt` (campaign record, not repo) is part of this theme's provenance record and is reported in section 12(d). The base relationship is by contract, not by file: the production BHL page the usage examples name is outside this repo's candidate set, and the base candidate file searched in section 4 is `review/black-highlighter-theme-jp/candidate.txt`.

## License and attribution

- **Title:** 圣人夜行 BHL 主题
- **Author:** Etinjat
- **Source:** https://scp-wiki-cn.wikidot.com/theme:walk-in-the-dark — revision 72
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
