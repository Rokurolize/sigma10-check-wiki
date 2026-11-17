# Review package — theme:fmaf-theme-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:fmaf-theme-jp — origin KO, population #262 [GOSIGN2-LEDGER (b) row 262]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 262]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 0 warns / 0 infos (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 266; GOSIGN2-LEDGER (b) row 262]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow (one sample combo http.cat among other hosts); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO3))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 261, source LOCALIZE-S2-F]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 261]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 262]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:fmaf-theme-jp.txt sha256:a40845500602aa29f6c74e3ffa5498042a33248e9aef78dd53f03b31f4818ce8; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 262) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×4 (class (iii), section 11); the render row's three items (KB-40 / KB-32 / KB-33+KB-34, section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:fmaf-theme | theme:fmaf-theme-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 38 (first translation; the candidate's credit block records 初訳時参照リビジョン: 38) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-fmaf-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:fmaf-theme-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 163 lines / 3,756 bytes | 177 lines / 5,009 bytes |
| SHA-256 | 3eecbec0df455349684e878b5354c34828ae85515c3b9f15d87537d8e559f4d3 | a40845500602aa29f6c74e3ffa5498042a33248e9aef78dd53f03b31f4818ce8 |

Wave history: the candidate was created by the Stage 2 KO3 integration (commit 783e87d, the LOCALIZE-S2-F wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D, the population-wide translator-attribution normalization that set the 翻訳責任者 field to its ruling-3 form). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A standard KO port at the small end of the population (the original is 163 lines). The candidate swaps the credit furniture for the JP preview credit block, rebuilds the delivery as a module import plus the interwiki-style frame on the draft host, adds Noto Sans JP to the font load and stacks, re-hosts the theme's three images to the draft host, translates the usage text and the CSS strings, and adds the JP license box the original never carried. Measured churn (diff.md, the generator's difflib count with autojunk off: +59/−45, 104 changed lines in 19 change blocks / 6 diff hunks). T4/T5 judged this theme PASS outright, one of only 19 in the population, and nothing in the bytes contradicts that: the credit source link names the serving host, and Korean survives only inside the credit block's original-title and source-link fields, where it is quotation.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 19 change blocks — 14 specific (73.7%), 3 heuristic (15.8%), 2 residue (10.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 6 |
| TRANSLATION-ANCHORED | 2 |
| DRAFT-HOST | 5 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| WS-ONLY | 2 |
| COMMENT-TEXT | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 2 residue blocks resolve as a tab-title translation (B5, section 6) and the porter annotation line (B12, section 10); the 3 heuristic blocks are the code-comment title translation (B11, R1, section 6), a `content:` string translation the CSS-BODY catch-all held (B15, KB-18, section 6), and the added exhibit heading (B10, section 8). The bare Rate's deletion rides inside B3 and is narrated in section 1, where it belongs. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:fmaf-theme-jp; original theme:fmaf-theme on scpko at reference revision 38; candidate `pages/theme:fmaf-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-F wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved: the original opens with its self-delivery module (L1–3) and its tag gate `[[iftags +테마]]` (L5); the candidate keeps the module first (L1–3), inserts the interwiki-style frame (L5–8), and places the localized gate after it (L10).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for fmaf-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module rate]]` inside a `[[>]]` wrapper (original L7–9) plus an `:scpko:info:start`/`end` pair (original L11–22) carrying the credit prose in Korean (title, 제작 thd-glasses, an images note, and a fonts-used list pointing at fonts.google.com and noonnu.cc). The candidate deletes both (the Rate inside B3, the info pair in B4) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–21) carrying the eight ruling-3 fields (タイトル 機動航空部隊CSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 기동항공대 테마; 著作権者 thd-glasses; 作成年 2020; 初訳時参照リビジョン 38; the source link to scpko.wikidot.com/theme:fmaf-theme). The info block's fonts-used list does not reappear as credit prose: the JP font credit sits in the @import annotation (candidate L59) and in the license box's font line (candidate L175). The candidate also gains the JP license box the original never had (B19, candidate L154–175: `:scp-jp:component:license-box-backend`/`license-box-end` with per-file attribution for the three images and the fonts). T7 credit-module CSS: none on either side (`grep -c 'creditButton' candidate.txt original.txt` returns 0 and 0); the theme carries no credit CSS of its own and inherits the module's styling.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become), and the info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields and the translator credit form; the file's last commit (1869877, FIX-CREDIT-D) is that form arriving population-wide. T4 (license box) is a supplement here, not a swap: the original carried no license furniture at all.
- **Verify:** `grep -n 'info:start\|info:end\|module rate' candidate.txt` returns nothing; read candidate L12–21 against the eight fields; read candidate L154–175 for the license box.
- **Disposition:** Applied. The ledger's (c3) line for this theme records no T4 credit item at all, because T4 judged the theme PASS (LOCALIZE-ROWS row 261).

### 2. Includes and components

- **What:** One live repoint, in the usage exhibit: `@@[[include :scp-jp:theme:fmaf-theme]]@@` (candidate L29), the escaped form of the original's own-theme include (B6, INCLUDE-REPOINT + ESCAPED-INCLUDE spans). The candidate's remaining includes are the frame, credit, and license-box includes of sections 1 and 3; every include in the candidate names a `:scp-jp:` target. No component swap (T8) occurs: this theme includes no sigma-plus or other ported component on either side.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; the theme's own JP candidate is that counterpart. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — five includes plus the escaped usage form, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its CSS by one live self-import from scpko.wdfiles.com, `local--code/theme%3Afmaf-theme/1` (original L2). The candidate keeps the module form and repoints it to its own delivery on the draft host, `local--code/theme%3Afmaf-theme-jp/1` on sigma10-jp-test.wdfiles.com (candidate L2, B1), and adds the interwiki-style frame the original lacked: `:scp-jp:component:interwiki-style` at priority=1 with `theme=` naming the same /1 delivery (candidate L5–8, B2). The tag gate follows the frame (candidate L10, B2/B3). The theme's CSS body itself travels inside the page as a `[[code type="css"]]` exhibit (the source-code tab), on both sides.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame; priority 1 is the theme's own layer in the BHL stack). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L2 and L7, both the candidate's own /1 on the draft host.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Load (B13): the original's Google Fonts import (original L62) loads Chakra Petch 700 only; the candidate's import (candidate L59) adds Noto Sans JP (400;700) to the same load, with the porter's annotation recording that it replaces the original's Korean web font reference. Stacks: the theme's two `font-family` lines (candidate L73, L86) read `"Chakra Petch", "Noto Sans JP", sans-serif`, each carrying a `/* [JP] */` marker; the original stacks named Chakra Petch alone, and the Korean display face the info block credited (noonnu.cc) is not loaded on either side as a live face. Assets: three image URLs move from the original's hosts to the draft host's `theme%3Afmaf-theme-jp` folder with file names unchanged (B8 FMAF-a-17.png, candidate L35; B9 FMAF.png, candidate L37; B14 FMAF_logo.png as the header background, candidate L62). The license box (section 1) records the original scpko URLs of the same files as attribution text; those are provenance lines, not live loads.
- **Why:** P7/T5 with KB-16 (the font load gap): a Latin-only stack cannot render Japanese text, so the JP face joins the load and every stack that can carry Japanese text. P5 with KB-17 (asset hosts): the theme's own images are re-hosted to the JP side; the draft-host form is the class (iii) draft state.
- **Verify:** `grep -n 'font-family\|@import' candidate.txt` — one import line naming both families, two stack lines, both JP forms; `grep -n 'wdfiles' candidate.txt` against the asset list above (the license-box attribution lines are the only scpko hits, at candidate L161–171).
- **Disposition:** Font load and stacks applied; the draft-host asset URLs are DISPOSITIONED (class (iii) draft form; posting rewrites them to the production host).

### 5. Header, sidebar, and site furniture

- **What:** None. Neither side sets a `--header-title`, `--header-subtitle`, or `--logo-image` variable (`grep -n -- '--header-\|--logo' candidate.txt original.txt` returns nothing on either file); the theme's logo travels as the header background asset re-hosted in section 4, and its sidebar and topbar rules are carried over unmodified apart from the font lines of section 4. No P8 layout adaptation was needed: the candidate inherits the JP site furniture through the frame.
- **Why:** P9/T6 and P8 are presence-checked classes; their absence is a checked fact about this theme, not an omission.
- **Verify:** The grep above; the candidate's furniture rules against the original's in diff.md.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The usage text and exhibit strings are translated throughout, in counted groups. Tab titles: 使用方法 (B5, residue, orig L25 → candidate L24) and デザイン (B7, anchored). Usage prose (B6): the heading line and the canon note, translated in place. The code exhibit's comment title (B11, heuristic): `기동항공대 CSS 테마` → `機動航空部隊CSSテーマ` inside the CSS banner comment (candidate L52) — R1 in-CSS text, porter-visible only. Two reader-visible CSS strings: B15 (heuristic, held by the CSS-BODY catch-all) `content: "기동항공대"` → `"機動航空部隊"` (candidate L73 area), and B16 (anchored CONTENT-STRING) `content: '알파-17 작전사령부'` → `'アルファ-17作戦司令部'` (candidate L85). The exhibit heading `+ ソースコード` is added at candidate L46 (B10; section 8). Korean survives in the candidate on exactly two lines, both inside the credit block: the 原題 field (candidate L16) and the source link's label (candidate L20), both quotations of the original's name.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`). R1 comment text is translated for the porter's reader but is not a display surface; it is counted separately here so the two are never conflated.
- **Verify:** A Hangul scan of candidate.txt returns only candidate L16 and L20; the pairs are diff.md's sections in order.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the two credit quotations.

### 7. Links

- **What:** The candidate's live outbound links are two. The credit block's source link (candidate L20) names scpko.wikidot.com/theme:fmaf-theme, the original's recorded host in sources.tsv — the serving form, not a defect (contrast the jiha case in this campaign, where the link named a non-serving host form). The usage prose links the FMAF canon hub on scpko (candidate L26) with its label translated and the parenthetical （韓国語版） marking it as the Korean-language original; the link target itself is unchanged, because the canon hub is the original branch's page and the text says so. The license box's three 出典 lines name scpko URLs as attribution records (section 4), not navigation.
- **Why:** P11: prose links take the JP counterpart or the serving original. The canon hub has no JP counterpart page; keeping the serving original, labelled as the Korean version, is the form the localize lane judged PASS for this theme.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the two live links above plus no others outside the license-box attribution lines.
- **Disposition:** Standing; T4/T5 PASS for this theme (LOCALIZE-ROWS row 261) covers both links.

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and channel order are preserved; the candidate's code exhibit sits where the original's sits, and the JP additions arrive as the head frame (section 3), the credit swap (section 1), and the license box at the tail (B19), not interleaved into the inherited CSS. One exhibit-presentation change: the source-code exhibit gains a `+ ソースコード` heading and a collapsible wrapper (B10, candidate L46–47) where the original showed the code block bare; the exhibit's content is the theme's own CSS, translated as recorded in section 6, with nothing dropped or replaced. An exhibit census confirms the shape: the tabview and its tabs and the code exhibit are present on both sides in the same order, so the R3 question (sanctioned replacement vs silent deletion) does not arise beyond the wrapper itself.
- **Why:** R3 exists to force exactly this adjudication; here the census, not the label, decides, and the only structural delta is presentational.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond, with the candidate's frame/credit/license includes added at the head and tail.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two blocks, both WS-ONLY: B17 (original L139 → candidate L130) and B18 (original L146 → candidate L137), each a whitespace-only line inside the code exhibit. The classifier finds no re-indentation anywhere (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The two blocks in diff.md's code-exhibit hunk.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Four annotations, none with an original counterpart. (1) B12 (residue): the CSS banner comment line `Ported for SCP-JP (theme:fmaf-theme rev 38)` (candidate L56), the port provenance line inside the code exhibit. (2) The @import annotation (candidate L59) recording the Noto Sans JP substitution and its ground. (3) Two `/* [JP] */` stack markers (candidate L73, L86) flagging the lines where the JP face was inserted. The skeleton's section here is written from the bytes: annotations (2) and (3) ride inside blocks whose primary labels are font classes, which is why no annotation signature fired for them.
- **Why:** R2: porter-added text is part of the change record; the [JP] markers are how a later editor tells a port edit from inherited text inside the exhibit.
- **Verify:** `grep -n 'Ported for SCP-JP\|\[JP\]' candidate.txt` — four hits, listed above.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's four pseudo-ref errors: class (iii), draft-wiki form (GOSIGN-TESTS T1 classification; GOSIGN2-LEDGER §(c1)) — they are the candidate's own draft-host delivery and asset lines (sections 3–4), the normal form at draft stage, rewritten to scp-jp at posting; fix lanes never "fix" them in the candidate. (2) The render row's page item, the runtime-hotlink site-theme chain: environment-layer, not charged to the candidate (KB-40). (3) The render row's sample items: the credit-modal errors (KB-32, the preview form has no modal mechanism, ruling 5) and the 884px@768 overflow (KB-33/KB-34 cross-cutting families; one sample combo's host was http.cat, a transient capture host, KB-44 family). No T4/T5 item exists for this theme: both tests judged PASS.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 266): exit 1, 4 errors / 0 warns / 0 infos; all four errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO3)): FINDINGS, the three items of section 11, all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 261): PASS jointly, display-affecting findings 0 — this theme is one of the 19 outright PASS themes in the localize sweep. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +59/−45 in 19 change blocks / 6 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:fmaf-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 262; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-fmaf-theme-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
