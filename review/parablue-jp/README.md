# Review package — theme:parablue-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:parablue-jp — origin CN, population #212 [GOSIGN2-LEDGER (b) row 212]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 7996a1be8d0e2729b7440162da5e3dcd7574057fd5750f1922193d8b54efb7fa); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 16 errors / 7 warns / 3 infos (hotlink×12, http×2, foreign-include×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 182; GOSIGN2-LEDGER (b) row 212]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 331px@320 (page) and 366–380px@320/375 (sample); page sidebar-not-opening; runtime-hotlink incl. candidate host paraarc-sandbox.wikidot.com on both pages; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-F (CN11))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN11))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 211, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 211]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 212]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:parablue-jp.txt sha256:7996a1be8d0e2729b7440162da5e3dcd7574057fd5750f1922193d8b54efb7fa; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items (GOSIGN2-LEDGER (b) row 212) |
| Standing items | **DISPOSITIONED** — the P4 delivery lines (class (ii); section 3), the P5 external font/asset lines (class (ii), KB-58; section 4), and the P9 kept Chinese title (ruling 2; section 5). **FLAGGED by this package** — the usage exhibit names the plain slug on the JP side (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:parablue | theme:parablue-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 5 (first translation; the candidate's credit block records 初訳時参照リビジョン: 5) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-parablue.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:parablue-jp.txt`, copied at worktree HEAD a497307 |
| Lines / bytes | 2,040 lines / 44,363 bytes | 3,250 lines / 75,841 bytes |
| SHA-256 | 0ff765fcda14c6e8a3c6ff30f31de56cc7b51d68c74ce9be9dbb51cccd1ca88b7 | e9d26bf1000156dfea28c281d537f41869d771c79dbbb443e6031ed11efbd75b |

Wave history: the candidate was created by the Stage 2 CN11 integration (commit b8ee399, the LOCALIZE-S2-E wave's port), then touched by d8969c7 (Wikidot normalization alignment), b89741d (rework2-p5), f931619 (FIX2-COLON, the colon-encoded sandbox paths), 1869877 (FIX-CREDIT-D, the translator-field normalization), and most recently a497307 (FIX4-MECH, the duplicate @import removal). The verdict stamp is computed against that head. No FIX5 commit touches this file.

## Summary

A CN theme built for the paraarc wiki on the Penumbra base, and the batch's most delivery-heavy port. The original carries its stylesheet twice (a live module copy and a code-exhibit copy, some 920 lines each), pulls its Penumbra base in through a sandbox-wiki include and two sandbox file imports, and puts its prose body between and after the copies. The candidate consolidates all of it into a single 3,048-line code block: the Penumbra base CSS inlined first (its banner carried), then the theme's own CSS with both of its banner comments preserved at the joints, the whole introduced by a porter comment that states what was merged and what was removed (the Sigma-9 base layer, which the JP site theme provides). The original's duplicated Inter @import is gone (FIX4-MECH), its Noto Sans SC becomes a loaded Noto Sans JP, and its sandbox imports of the base stylesheet and the AiDeep font file are kept in https form inside the theme's CSS head, inside the P4/P5 class (ii) dispositions that T1's hotlink count records. The prose body moves to the head, translated, under a preview credit block; delivery moves to a tail module-plus-frame pair in the original's own tail style. The one flag is the population family's: the usage exhibit keeps the plain slug on the JP side. Measured churn (diff.md, the generator's difflib count with autojunk off: +1,428/−218 in 20 change blocks / Tier 2 block volume — the low block count is the consolidation's signature: a few giant blocks, not many small ones).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 20 change blocks — 16 specific (80.0%), 1 heuristic (5.0%), 3 residue (15.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 12 |
| COLON-ENC | 2 |
| FONTLOAD-CJK-STACK | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| DUPIMPORT-DEL | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the DELIVERY-MOVE mass is the consolidation itself — B3 (original L4 → candidate L13–1410) carries the prose relocation and the inlined base, B4–B16 are the single-line loci inside the merged CSS (the font loads and stacks, the paraarc-sandbox asset lines, the colon-encoded commented imports), and B20 is the tail delivery pair. Unlike the our-open-veins case in this batch, the label hides no drop here: the merged block's contents were checked against both of the original's copies and the base, and section 8 states the census. The 3 residue blocks (B17–B19) are the code block's closing lines, alignment pairings at the merge's tail. The single heuristic block is B9 (original L952–1120 → candidate at L2332), the body zone between the original's two CSS copies, whose prose stands at the candidate's head in translated form. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:parablue-jp; original theme:parablue on scp-wiki-cn at reference revision 5; candidate `pages/theme:parablue-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame order is rebuilt: the original opens with its sandbox base include and its live CSS module, and delivers from the head (original L1–3); the candidate opens with the localized gate `[[iftags +テーマ]]` and the credit block (candidate L1–12), carries its CSS as one code exhibit, and delivers from the tail (candidate L3244–3251).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the delivery pair is P6/T3 (section 3).
- **Verify:** The sources.tsv row for parablue-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` standing between its two CSS copies (original L925) and the banner comment at the head of each CSS copy ("ParaBlue Theme [2022 Wikidot Theme] By OxygenNine, Based on: Penumbra Theme by EstrellaYoshte", original L10–16 and L1126–1132). There is no credit module and no license box anywhere in the original. The candidate deletes the bare Rate (BARE-RATE-DEL inside block B8) and installs the preview credit block at the head (candidate L3–12) carrying the eight ruling-3 fields (title 悖蓝 版式 — the Chinese title kept, section 5; 翻訳責任者 AI; 翻訳年 2026; 原題 悖蓝 版式； 著作権者 OxygenNine, in the plain-name form the original's own banner uses; 作成年 2022, matching the banner's [2022 Wikidot Theme]; 初訳時参照リビジョン 5; the source link https://scp-wiki-cn.wikidot.com/theme:parablue, whose host matches the sources.tsv record). The base attribution the banner carries is preserved twice over: the candidate's prose states the Penumbra basis (candidate L14), and both banner comments survive at the joints of the merged CSS (candidate L1416–1422 and L2338–2344), so the base's author credit stands in the delivered stylesheet as the original's did. No license box exists on either side and none was installed; the theme's attribution surface is the credit block and the banners, and T4 raised no box item for this theme. T7: the classifier's T7-CREDIT-CSS signature fires inside block B3, on the credit rules the inlined Penumbra base ships; the theme adds no credit-module CSS of its own.
- **Why:** P3/T1 with KB-09 (the preview module is rate-bearing; a kept bare Rate would double-render). Ruling 3 fixes the eight fields and the translator form; 1869877 is that form arriving.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L3–12 against the eight fields; `grep -n 'ParaBlue Theme' candidate.txt` — the two banner survivals.
- **Disposition:** FIXED by construction at creation (P3 credit fields).

### 2. Includes and components

- **What:** The original's one page-level include is its base: `[[include :bettersandbox:pnmcss]]` (original L1), pulling the Penumbra base component from a sandbox wiki. The candidate has no counterpart include: the base's CSS is carried inline in the merged code block (section 3), and the sandbox wiki has no JP counterpart to repoint to. T1's baseline counts one foreign-include error for the pair, which is this line's original form recorded against the baseline commit; in the candidate the include is gone, not repointed. The candidate's remaining includes are the credit pair (section 1) and the tail frame (section 3). The light-variant exhibit in the prose keeps its foreign form deliberately: `{{@@[[include :paraarc:theme:light-parablue]]@@}}` (candidate L25) names the light version on paraarc, the wiki this theme was built for — the JP port covers the main theme, and the exhibit documents where the light variant lives, as the original's prose did.
- **Why:** P1 (KB-15): includes name the JP counterpart that exists; where the delivery is a foreign component with no counterpart, the campaign's form is the inline carry with attribution (sections 1, 3), not a repoint to a page that is not there.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the credit pair and the frame only; `grep -n 'bettersandbox' candidate.txt` returns nothing.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The original delivers from its head: the sandbox base include (original L1), then a live `[[module CSS]]` carrying the theme's stylesheet (original L3–~940), whose head imports the base's stylesheet file and the AiDeep font file from scpsandboxcn (original L24, L26) alongside its Google Fonts loads. A second, exhibit copy of the same stylesheet follows (original L1117–2039), and the prose body stands between and after the copies. The candidate consolidates the whole delivery into one code file and a tail pair. The single code block (candidate L192–3240) opens with a porter comment (candidate L192–193) stating the merge: the original's Penumbra-lineage CSS gathered into one place, with the Sigma-9 base (paraarc's s9.css) removed because the JP site-theme layer provides it. Inside, the Penumbra base CSS stands first (its banner at the block's head), then the theme's own CSS (its banner at candidate L1416–1422, and the second copy's banner at L2338–2344 where the exhibit copy's material joins). The theme CSS head keeps its sandbox imports in https form — the AiDeep font file and pnmcss.css from scpsandboxcn (candidate L1430, L1432) — so the base stylesheet is both inlined above and imported at the theme layer, exactly the redundancy the original itself had (its page included the base component and its CSS imported the base file); T1's hotlink count is this family's size, and the (c3) register dispositions the theme's P4 line as delivery class (ii). The original's commented-out paraarc imports (s9.css, pn.css) are kept as comments with their colon-encoded paths (candidate L2347, L2349; the FIX2-COLON wave's normalization, COLON-ENC blocks B11–B12). Delivery proper is the tail pair (block B20): a module CSS importing `local--code/theme%3Aparablue-jp/1` from the draft host (candidate L3246–3248) and the interwiki frame at priority 1 with `theme=` naming the same /1 on the draft host (candidate L3249–3251).
- **Why:** P4/T9 and P6/T3 for the tail pair and the import form; KB-41 for the draft lines (class (iii)). The consolidation is a delivery decision the porter documented at the block's head (section 10); the kept sandbox lines are the P4 class (ii) disposition, the posting-form deliveries the register records rather than edits.
- **Verify:** Read candidate L192–193 (the merge note) and L1424–1432 (the theme CSS head); `grep -n 'local--code' candidate.txt` — the tail pair.
- **Disposition:** DISPOSITIONED (the sandbox delivery lines, P4 class (ii); the draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Loads, base layer: the inlined Penumbra CSS loads Josefin Sans 700, Roboto, and Fira Code from Google Fonts (candidate L208–210), the base's own set. Loads, theme layer (candidate L1424–1429): Work Sans, Roboto, and Fira Code in their full axis ranges, Inter — and Noto Sans JP, where the original loaded Noto Sans SC (original L21–24): the CJK face is substituted and loaded (JPFONT-LOAD inside block B4), and the stacks take the JP face at two loci (FONTLOAD-CJK-STACK, blocks B5 and B14). The original's duplicated Inter @import (it stood twice on one line, original L24) is carried once; the FIX4-MECH wave's duplicate removal is block B10's DUPIMPORT-DEL, at the second copy's import zone. Two font files stay external by disposition: the AiDeep .otf from scpsandboxcn (candidate L1430, https form; the original's was http, original L24 — T1's http×2 baseline items are this line and its twin in the second copy) — a display face distributed only as that sandbox file, kept under the P5 class (ii) disposition (KB-58). Assets: the merged CSS's image URLs name the paraarc sandbox file area (eidicons1.svg at four loci, the arc.svg logo at candidate L2482) — the theme was built for paraarc and its icon set lives there; the render row records the candidate host paraarc-sandbox.wikidot.com among its runtime hotlinks, and the (c3) P5 line covers the family. The Penumbra logo URL in the base layer still names the EN penumbra file area (candidate L217), carried with the base as its own asset reference.
- **Why:** P5 with KB-58 (branch sandbox deliveries carried in posting form, class (ii)) and P7/T5 with KB-16 (the substituted CJK face loaded and stacked together, so the named-but-unloaded gap does not arise for the theme's own stacks).
- **Verify:** `grep -n '@import' candidate.txt` — the base loads at L208–210 and the theme loads at L1424–1432; `grep -n 'paraarc-sandbox' candidate.txt` — the five asset loci.
- **Disposition:** DISPOSITIONED (P5, class (ii), KB-58; (c3) register, parablue line).

### 5. Header, sidebar, and site furniture

- **What:** No header-variable translation: the theme's title surface is its credit-block title and its CSS masthead rules, and the title is kept in Chinese （悖蓝 版式, candidate L4 and L8) — the P9 item T4 counted among this theme's findings and the (c3) register dispositions under ruling 2. The HEADERVAR signature inside block B3 fires on the inlined base's header variables, which are carried as the base ships them (the base layer's own variables, under the same ruling-2 ground as pastel-skies' inlined defaults in this batch). The sidebar behaviour the base provides is carried with the base CSS; no P8 layout adaptation was needed, though the render row records a page sidebar-not-opening item, which is an interaction-layer finding of the capture, listed in section 11.
- **Why:** P9/T6 with ruling 2: the theme's name and the base's defaults are their authors' display text, and header/title language is case-by-case translation taste, out of scope for migration correctness.
- **Verify:** The credit title is candidate L4; LOCALIZE-ROWS row 211 counts the theme's findings (3, the P4/P5/P9 items of sections 3–5).
- **Disposition:** DISPOSITIONED (ruling 2; (c3) register, parablue line).

### 6. Text translation

- **What:** The prose body (which stands between and after the original's CSS copies) is translated from Chinese and moved to the candidate's head: the introduction (the theme's purpose and its Penumbra basis, candidate L14–16), the usage instructions, and the long exhibit sequence (blockquote, note, typer, modal and the remaining decoration samples), in the TRANS-UNANCHORED mass that rides inside blocks B2–B3 and B9, each passage verified against the mirror for this README. The Q&A-style prose links keep their paraarc targets with translated labels (candidate L14, L25–29). R1 in-CSS text: the CSS's Chinese comments are translated in the theme layer (COMMENT-TEXT inside B3's spans), the banner comments are carried verbatim as attribution (section 1), and the porter's merge comment is section 10. The theme's Chinese proper nouns that function as names (the title, the archive's name in its translated form インターネット超常記録館) follow sections 5 and 7.
- **Why:** P10 and KB-18 (reader-visible strings localize). The unanchored grain is where a silent deletion would hide; at this block granularity the check is the census of section 8, which was run passage by passage.
- **Verify:** The pairs are diff.md's body sections; the candidate's prose occupies L13–190, before its code block.
- **Disposition:** Standing (the port itself); T4/T5 judged the theme FINDINGS with the three dispositioned items of sections 3–5 (LOCALIZE-ROWS row 211).

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L11), naming the original on scp-wiki-cn.wikidot.com, the host the campaign's provenance records name for it. The prose links to paraarc (the archive's home and the light variant's page and include exhibit, candidate L14, L25, L29) keep their targets: paraarc is the wiki this theme serves, the JP environment does not replace it, and the light variant is not part of this port, so the serving originals are the correct targets with translated labels. No link in the candidate is dead on the evidence of the mirror.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.
- **Verify:** `grep -n 'paraarc.wikidot.com' candidate.txt` — the prose loci.
- **Disposition:** Standing.

### 8. Structure

- **What:** This theme is the closing rule's stress test, because its candidate is a consolidation: the census was therefore run at the level of content, not blocks. The original's two stylesheet copies were checked against the candidate's single code block: the base CSS (which the original delivered by include and import, not as page text) stands at the block's head; the theme's stylesheet stands after it, with both of the original's banner comments preserved at the joints (candidate L1416–1422, L2338–2344) marking where the module copy's and the exhibit copy's materials join; the commented paraarc imports survive as comments (candidate L2347, L2349); and the prose body stands complete at the candidate's head. What left, by the porter's own head note, is one layer: the Sigma-9 base (paraarc's s9.css), removed because the JP site-theme layer provides the Sigma base — a stated removal with an environment ground, not a silent drop, and the same base the JP candidate set as a whole stands on. The classifier's EXHIBIT-RESTRUCTURE primaries (B8, B9) adjudicate to the credit-zone replacement and the body relocation. No brace-depth anomaly was found in the merged block (the depth scan balances).
- **Why:** R3: a restructure and a silent deletion share a diff shape; at Tier 2 volume the census, not the label, decides, and here it passes with the one stated removal.
- **Verify:** `grep -n 'ParaBlue Theme\|Penumbra Theme' candidate.txt` — the banners at the block's head and joints; read the merge note at candidate L192–193.
- **Disposition:** Standing; no structural deletion beyond the stated Sigma-9 layer, no class I item.

### 9. Formatting only

- **What:** None as a class: the classifier finds no whitespace-only block and no re-indentation pairing (0 and 0). The consolidation's churn is real but semantic (relocation and merge), and it is counted in sections 3 and 8 rather than here; the R7 hazard in its follow-up form (a future diff re-showing the merge) is inherent to a one-time consolidation and is the reason this README describes the merge's joints explicitly.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the class is empty and the semantic churn is documented where it belongs.
- **Verify:** The classification summary's WS-ONLY count is 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation, and it is the port's key document: the comment at the merged code block's head (candidate L192–193): "parablue：原語版の CSS（Penumbra 系の独自 CSS）をまとめたもの。Sigma-9 ベース（paraarc s9.css）は SCP-JP ではサイトテーマ層が提供するため除去しています。" — the original's CSS (its Penumbra-lineage custom CSS) gathered into one place; the Sigma-9 base removed because on SCP-JP the site-theme layer provides it. It rides inside block B3, which is why no separate annotation signature fired; the skeleton's "none" for this section does not survive contact with the bytes and is corrected here. There are no other porter comments and no editor lines in the candidate.
- **Why:** R2: porter-added text is part of the change record; this one carries the consolidation and the removal, and sections 3 and 8 cite it as their in-file evidence.
- **Verify:** Read candidate L192–193.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) The P4 delivery lines (section 3): the kept sandbox deliveries (the base stylesheet and font file imports) carried in posting form, dispositioned as delivery class (ii) in the (c3) register; T1's baseline counts the family (hotlink×12, http×2, foreign-include×1 across the pair's baseline form). (2) The P5 external font and asset lines (section 4): the AiDeep file and the paraarc-sandbox asset URLs, dispositioned as class (ii) under KB-58. (3) The P9 kept Chinese title (section 5): dispositioned under ruling 2. The render row's remaining items are environment or capture layer, not charged to the candidate: the page and sample overflow readings (331px at 320 on the page; 366–380px at 320/375 on the sample), the page's sidebar-not-opening item, the runtime-hotlink chain including the paraarc-sandbox host (KB-40's family, with the candidate-host lines counted under item 2), and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5). The T1 register's one pseudo-ref error is the candidate's own draft-host delivery line, class (iii).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (ii)/(iii); ruling 2; the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 182 and register (c1).
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 182): exit 1, 16 errors / 7 warns / 3 infos; the errors are hotlink×12, http×2, foreign-include×1, pseudo-ref×1, all in the dispositioned classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-F (CN11)): FINDINGS, the items of section 11, all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 211): FINDINGS jointly, display-affecting findings 3 (the P4, P5, and P9 items); the (c3) register dispositions all three. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +1,428/−218 in 20 change blocks / Tier 2 block volume.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:parablue-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 212; go-sign, COMPLETION-REPORT §10), with the per-theme flag below standing as this package's addition to the record.

## Per-theme record

### The usage exhibit's slug (flagged by this package)

The usage exhibit (candidate L20) was repointed from `:scp-wiki-cn:theme:parablue` to `:scp-jp:theme:parablue` at creation, keeping the plain slug. The candidate's own posting name is theme:parablue-jp, so the documented syntax names a page that will not exist under that name on scp-jp; the file's own delivery lines use the -jp form (candidate L3247, L3250). This is the population-sweep family (the same shape is flagged in the plant, parawatch-pumpkin, pack-of-peanuts, paramycota, past-oriented, and pastel-skies packages in this batch). The neighbouring light-variant exhibit (candidate L25) is not part of the flag: it names the light version on paraarc, its home wiki, in both the original and the candidate. The ledger's determination for this theme is PASS and this package does not re-open it; the line is flagged here with its locus, and the candidate is left unedited, as the sweep repairing this family is a coordinator matter.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-parablue-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11); it belongs to this theme's record but carries no port change of its own to explain here. The light variant (theme:light-parablue on paraarc) is a separate page on its home wiki and is not part of this port. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 悖蓝 版式
- **Author:** OxygenNine
- **Source:** https://scp-wiki-cn.wikidot.com/theme:parablue — revision 5
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
