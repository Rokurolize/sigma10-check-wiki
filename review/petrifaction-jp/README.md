# Review package — theme:petrifaction-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:petrifaction-jp — origin CN, population #218 [GOSIGN2-LEDGER (b) row 218]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 218]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 9 errors / 0 warns / 2 infos (hotlink×8, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 243; GOSIGN2-LEDGER (b) row 218]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-login (4 combos) on page and sample + runtime-hotlink site-theme chain; sample credit-modal (preview-form) + page-overflow 332–335px@320. [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 217, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 217]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 218]
- Computed against: canonical commit 443c60879a7c53fa5dfe6e5fc9f72e8785196d05; candidate file pages/theme:petrifaction-jp.txt sha256:990bf6a65e7f51af28ceaafc7e8c5980a20061901b709045feaee2b571af9a8b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items (GOSIGN2-LEDGER (b) row 218) |
| Standing items | **DISPOSITIONED** — the P5 external-background hotlinks (class (ii), KB-58; sections 4, 11) and the P9 kept Chinese display strings (ruling 2; section 5). No defect flags from this package: the usage exhibit already names the -jp form, every named font face is loaded, and the two apparent anomalies a skim finds (the doubled credit-preview install and the surviving `[[module Rate]]`) are the original's own demo structure, explained in sections 1–2 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:petrifaction | theme:petrifaction-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14 (first translation; the candidate's credit block records 初訳時参照リビジョン: 14) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-petrifaction.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:petrifaction-jp.txt`, copied at worktree HEAD 443c608 |
| Lines / bytes | 885 lines / 20,455 bytes | 952 lines / 24,096 bytes |
| SHA-256 | c0ee13b8d57ec9a7a5ba0a56ba1c94cb2ac2ac9d2f41f1ebfe7a92b67c0a8a | 990bf6a65e7f51af28ceaafc7e8c5980a20061901b709045feaee2b571af9a8b |

Wave history: the candidate was created by the Stage 2 CN12 integration (commit 72e3efa, the LOCALIZE-S2-E wave's port), then touched by 1869877 (FIX-CREDIT-D, the translator-field normalization), and most recently by 443c608 (FIX4-REPOINT, the wave that repointed this candidate's exhibits and delivery lines; the verdict stamp is computed against that head). No FIX5 commit touches this file.

## Summary

A CN branch theme (for the Petrification City setting) whose port is the standing classes plus three deliberate, in-file-documented adaptations. First, delivery gains a layer the original does not have: where the original imports its stylesheet through a single head module in the page-URL form, the candidate adds the campaign's two-layer frame structure, the Black Highlighter normalize stylesheet as layer 1 and its own code file as layer 2. Second, the original's credit-module demonstration tab (it demos the CN credit:start / more / end and standalone forms) is reworked into a demo of the JP preview form, with a translator's note in the tab explaining that the CN forms have no JP counterparts — so the candidate's two credit-preview installs are one real block and one labelled demo, not a duplication. Third, the original's imported non-savingpage component CSS is carried inline, with a CSS comment recording its provenance (built on component:non-savingpage, preserving the evernight-aquarium version's behaviour, its strings matched to the scp-jp-sandbox3 version). The font system is substituted family-for-family from CN faces to JP faces, every substituted face loaded, and the usage exhibit already names the -jp posting form — this is the batch's one theme with no exhibit flag. Measured churn (diff.md, the generator's difflib count with autojunk off: +172/−105 in 78 change blocks / Tier 2 block volume).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 78 change blocks — 32 specific (41.0%), 44 heuristic (56.4%), 2 residue (2.6%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 22 |
| TRANS-UNANCHORED | 21 |
| CSS-BODY | 10 |
| TRANSLATION-ANCHORED | 9 |
| DRAFT-HOST | 6 |
| GLYPH-FORM | 5 |
| JPFONT-STACK | 5 |
| CONTENT-STRING | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic mass is dominated by COMMENT-TEXT (22 counts), the translation of the CSS's Chinese section comments — expected R1 mass for a CN original, resolved by shape in section 6 rather than line by line. The 10 CSS-BODY blocks are the font-stack rewrites and the inlined component CSS of sections 3–4 (P7-class content with no mechanism signature), adjudicated there. GLYPH-FORM (5 counts, R5) is the shinjitai conversion of retained Chinese strings, counted separately in section 6 as the taxonomy requires. The 2 residue blocks (B6, B42) are translation pairings (the Wikiwalk exhibit's branch repoint and a caption pair), resolved in the appendix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:petrifaction-jp; original theme:petrifaction on scp-wiki-cn at reference revision 14; candidate `pages/theme:petrifaction-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame order is the original's own at the head (delivery module, then the tag gate, original L1–4), with the candidate inserting its two frame layers between the module and the gate (candidate L1–13) and localizing the gate's tag from the CN form +版式 to +テーマ (candidate L15).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame layers are P6/T3 (section 3).
- **Verify:** The sources.tsv row for petrifaction-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture lives in its page-elements demo tab: a `[[module Rate]]` (original L37) and demos of the CN credit modules, `:scp-wiki-cn:credit:start` / `credit:more` / `credit:end` (original L39–45) and the standalone pair `credit:start-standalone` / `credit:end-standalone` (original L47–53). There is no head credit block and no license box anywhere in the original. The candidate installs the preview credit block at the head (candidate L17–28) carrying the eight ruling-3 fields (title 大梦一场 テーマ版式 — the Chinese title kept, section 5; 翻訳責任者 AI; 翻訳年 2026; 原題 大梦一场 主题版式； 著作権者 [[*user AsWheat]], matching the campaign's provenance record; 作成年 2024; 初訳時参照リビジョン 14; the source link https://scp-wiki-cn.wikidot.com/theme:petrifaction, whose host matches the sources.tsv record) plus a trailing font line inside the block listing the six Google Fonts faces and their license (SIL Open Font License). The demo tab is then reworked, not deleted (candidate L58–68): the Rate module demo is carried as-is (`[[module Rate]]`, candidate L60 — a labelled exhibit inside the demo tab, exactly as the original demos it, not a live second widget), and the credit demo becomes one preview pair (candidate L62–66) with a translator's note stating that the CN credit forms the original demonstrated have no JP counterparts, so the preview form is demonstrated instead, and that the theme's CSS also covers the creditRate classes (candidate L68; section 10). So the candidate's two credit-preview installs are one furniture block and one demo, mirroring the original's structure. No license box exists on either side and none was installed: the theme's attribution surface beyond the credit block is its Q&A image-source lines (Pixabay, both images), which the candidate translates in place (candidate L52–56); T4 raised no box item for this theme. T7 credit-module CSS: the theme's CSS carries the credit and creditRate rule families on both sides (the tail rules are visible at original L870–876 and their candidate counterparts), carried and, per the demo note, covering the preview form's classes.
- **Why:** P3/T1 with KB-09 (the preview module is rate-bearing; the demo tab's Rate is exhibit text inside a tab, the form the original itself uses, so it is not the double-render the rule targets). Ruling 3 fixes the eight fields and the translator form; 1869877 is that form arriving, and 443c608 repointed this file's exhibits afterward.
- **Verify:** Read candidate L17–28 against the eight fields; read the demo tab at candidate L58–68 against original L37–53; `grep -n 'module Rate' candidate.txt` — one hit, inside the tab.
- **Disposition:** FIXED by construction at creation (P3 credit fields; the demo rework is documented in-file).

### 2. Includes and components

- **What:** The candidate's include list is short: the two frame layers (candidate L5–13, section 3), the credit pair twice (head and demo tab, section 1), and the license-free tail has none. The original's only component-level include beyond its credit demos is none at page level — its component dependency rides as a CSS @import (the non-savingpage component, section 3). One repoint block covers the frame's theme= line. No component swap (T8) was needed; the theme-squares-class exhibits this theme lacks are absent from the original too.
- **Why:** P1 (KB-15): includes name the JP counterpart that exists; this theme's component surface is CSS-level and is handled in section 3.
- **Verify:** `grep -n '\[\[include' candidate.txt` — six includes, all JP-side.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The original delivers through a single head module importing its stylesheet in the page-URL form, `https://scp-wiki-cn.wikidot.com/theme:petrifaction/code/1` (original L2), with no interwiki frame. The candidate keeps a head module (importing `local--code/theme%3Apetrifaction-jp/1` from the draft host, candidate L2) and adds the campaign's two-layer frame structure the original does not have: a priority-1 frame whose `theme=` is the Black Highlighter normalize stylesheet on scp-jp.github.io (candidate L5–8) and a priority-2 frame whose `theme=` is the theme's own /1 on the draft host (candidate L10–13) — the JP environment's base layer applied under the theme's own layer, in the frame form. Inside the CSS, one delivery conversion: the original imports the non-savingpage component's stylesheet from its home wiki, `https://evernight-aquarium.wikidot.com/component:non-savingpage/code/1` (original L158); the candidate carries those rules inline in its own CSS (from candidate L898), under a comment recording the provenance (built on component:non-savingpage (R74), preserving the evernight-aquarium version's behaviour, strings matched to the scp-jp-sandbox3 version) — an import-to-inline conversion of a small utility component, documented at the point of carry, with its Japanese lock-info strings visible at the file's tail (candidate L937–951). The component's rules are present; only their delivery form changed.
- **Why:** P4/T9 and P6/T3 for the module form and the frame layers (the JP base layer is the environment's foundation; a theme delivered without it would miss the normalize base every JP page assumes). The component conversion follows the same ground as the pastel-skies base carry in this batch (a foreign delivery the JP environment does not keep becomes an inline carry with attribution), at utility-component scale. The draft-host line is KB-41, class (iii).
- **Verify:** `grep -n 'interwiki-style\|local--code' candidate.txt` — L2, L5–13; read the provenance comment at candidate L898.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** The original loads seven font imports plus the component import (original L151–158): SourceHanSerifCN from a deno CDN, Noto Sans SC, Zhi Mang Xing, Noto Serif (with subset parameters), Noto Serif SC, Oswald (old css grammar), and Ma Shan Zheng. The candidate loads six Google Fonts imports (candidate L166–171): Noto Serif JP, Noto Sans JP, Shippori Mincho, Noto Serif (css2 grammar), Oswald (css2 grammar), Yuji Syuku. The stack mapping is one-for-one and verifiable: --title-font 'Source Han Serif CN VF' → 'Noto Serif JP', 'Shippori Mincho' (candidate L175); --body-font "Noto Sans SC" → "Noto Sans JP" (candidate L176); the Oswald display pairings "Oswald", "Zhi Mang Xing" → "Oswald", "Shippori Mincho" (original L253 → candidate L266) and "Oswald", "Ma Shan Zheng" → "Oswald", "Yuji Syuku" (original L279 → candidate L292). Every family the candidate's stacks name is loaded in-file — the KB-16 check passes clean for this theme. The theme's background images are the T4 row's P5 item: eight external background references (CN sandbox backgrounds and EN storage images, bg-marble / school.png among them) that the delivery CSS and page carry as hotlinks; T1's baseline counts the same family (hotlink×8), and the (c3) register dispositions the theme's P5 line as class (ii) under KB-58 — posting-form lines the posting procedure handles, recorded here with their count.
- **Why:** P5 with KB-58 (CN font and asset sources the JP environment substitutes or carries in posting form) and P7/T5 with KB-16 (substituted faces loaded, stacks rewritten together).
- **Verify:** `grep -n '@import' candidate.txt` — L2 and L166–171; compare the stacks at original L162–163, L253, L279 against candidate L175–176, L266, L292.
- **Disposition:** DISPOSITIONED (P5, class (ii), KB-58; (c3) register, petrifaction line).

### 5. Header, sidebar, and site furniture

- **What:** No header-variable change: the theme styles its header through rules and the inlined furniture, so no HEADERVAR signature fired. The dispositioned item is the kept Chinese display text: the credit block's title field keeps 大梦一场 (candidate L18), and a CSS `content:` string keeps "石化" — T4's row names both ("`content: \"石化\"`・クレジットタイトル `大梦一场` の中国語 display 残存", LOCALIZE-ROWS row 217) under its P9/T5 item, and the (c3) register dispositions the theme's P9 line under ruling 2. These are the theme's proper name and in-universe seal text, kept as the original's display form while the surrounding prose is translated; other retained Chinese strings were converted to Japanese glyph forms where the character differs (the GLYPH-FORM counts of section 6), which is why the kept pair stands out as a decision rather than an oversight.
- **Why:** P9/T6 with ruling 2: the theme's title and seal strings are its name, and header/title language is case-by-case translation taste, out of scope for migration correctness; the ledger recorded the retention and its display effect openly.
- **Verify:** LOCALIZE-ROWS row 217 states the item in the words quoted above; the strings are at candidate L18 and in the CSS's content: rules.
- **Disposition:** DISPOSITIONED (ruling 2; (c3) register, petrifaction line).

### 6. Text translation

- **What:** The body translates from Chinese throughout: the basic-information tab, the Q&A (including the design acknowledgements to Dr Hormress and Flea-zer0, carried with their user links), the page-elements samples, and the formatting exhibits, in nine TRANSLATION-ANCHORED blocks and the one-line TRANS-UNANCHORED grain (21 counts), each verified against the mirror for this README. Three counted sub-classes deserve their own lines. (1) COMMENT-TEXT, 22 counts: the CSS's Chinese section comments are translated (the R1 porter-visible half; a CN original carries more comment mass than an EN one, and it is resolved here by shape — section banners and rule-group labels — rather than line by line). (2) GLYPH-FORM, 5 counts (R5): retained Chinese strings converted to Japanese glyph forms (shinjitai) where the port keeps the word but not the glyph — neither translated nor left untouched, and counted separately so the reviewer sees the third state. (3) CONTENT-STRING, 2 counts: reader-visible CSS strings localized (the lock-info family among them; the kept "石化" of section 5 is the stated exception). The exhibits show the port's care at small scale: the Wikiwalk sample's branch markers are repointed (SCP-CN-XXX → SCP-JP-XXX, appendix), and the usage exhibit names the -jp form (section 2's census; no flag for this theme).
- **Why:** P10 and KB-18 (reader-visible strings localize); R5 exists because glyph conversion is a distinct act from translation, and conflating them hides both.
- **Verify:** The pairs are diff.md's body sections in order; the comment translations are visible throughout the CSS exhibit on both sides.
- **Disposition:** Standing (the port itself); T4/T5 judged the theme FINDINGS with the items of sections 4–5 (LOCALIZE-ROWS row 217, whose text also records that the translation quality is high and the credit requirements are met).

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L26), naming the original on scp-wiki-cn.wikidot.com, the host the campaign's provenance records name for it. The Q&A's links to the setting page and the two reference themes (deserted-years, inland-empire) keep their CN targets with translated labels (candidate L44–46): those pages are the theme's design sources on the original wiki, and the JP environment does not replace them, so the serving originals are the correct targets. The image-source links (Pixabay) are carried in the Q&A (candidate L52–56). One http:// string survives in the file, inside a CSS source-attribution comment (`/* source: http://1nu.wikidot.com/iikanji */`, candidate L480): it is a comment recording where a rule set came from, it loads nothing, and the classifier's HTTP-KEPT note files it as a class (ii) posting-rewrite line; it is recorded here so the string is not mistaken for a kept external delivery.
- **Why:** P11: prose links take the JP counterpart or the serving original; attribution comments are records, not links.
- **Verify:** `grep -n '1nu.wikidot' candidate.txt` — candidate L480, inside a comment.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds: the exhibit census corresponds one to one (the basic-information tab with its usage exhibit, the page-elements demo tab, the collapsible and formatting samples, and the CSS code exhibit), and the JP corrections arrive as the head delivery set, the credit install, and the demo rework. The demo tab's rework (section 1) is a replacement with its ground stated in the tab itself, so the R3 question (sanctioned replacement vs silent deletion) is answered by the file: the CN credit demos left because their components do not exist on JP, and the note saying so stands where they stood. The 10 CSS-BODY blocks adjudicate to the font-stack rewrites and the inlined component rules (sections 3–4). No brace-depth anomaly was found in this pair (the depth scan balances on both sides).
- **Why:** R3 exists to force exactly this adjudication; here the file itself carries the ground, which is the strongest form of it.
- **Verify:** Compare `grep -n '\[\[tab \|code type' original.txt candidate.txt` — the tab sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation anywhere in the pair (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary's WS-ONLY count is 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotations. (1) The translator's note in the demo tab (candidate L68): "訳注: 原語版がデモしていた :scp-wiki-cn: の credit:start / credit:more / credit:start-standalone に対応するJPのコンポーネントは存在しないため、ここでは credit:start-preview をデモする。このテーマのCSSは creditRate 系のクラスもカバーする。" — the demo rework's ground, stated where a reader meets it. (2) The CSS comment at the inlined component rules (candidate L898), recording the non-savingpage carry's provenance and string source (section 3). The skeleton's "none" for this section does not survive contact with the bytes and is corrected here: both annotations exist, and both carry decisions a reviewer would otherwise have to guess at.
- **Why:** R2: porter-added text is part of the change record; these two are the file's own explanations of its two least obvious choices.
- **Verify:** Read candidate L68 and L898.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) The P5 external-background hotlinks (section 4): eight references carried in posting form, dispositioned as class (ii) under KB-58 in the (c3) register; T1's baseline counts the same eight as its hotlink errors. (2) The P9 kept Chinese display strings (section 5): counted by T4 as the theme's display-affecting finding (with the P5 item), dispositioned under ruling 2 in the (c3) register. (3) The render row's items, all environment, capture, or interaction layer, not charged to the candidate: the hidden-login findings (4 combos) on page and sample and the runtime-hotlink site-theme chain (KB-40); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the page-overflow readings (332–335px at 320). The T1 register's remaining error is the one pseudo-ref, the candidate's own draft-host delivery line, class (iii).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (ii)/(iii); ruling 2; the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 243 and register (c1).
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 243): exit 1, 9 errors / 0 warns / 2 infos; the errors are hotlink×8 (item 1 above) and pseudo-ref×1 (class (iii)); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-F (CN12)): FINDINGS, the items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 217): FINDINGS jointly, display-affecting findings 1, the row's text naming the P5 backgrounds and the P9/T5 kept strings, and recording that the translation quality is high and the credit requirements are met; the (c3) register dispositions both items. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +172/−105 in 78 change blocks / Tier 2 block volume.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:petrifaction-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 218; go-sign, COMPLETION-REPORT §10).

## Per-theme record

No defect flags for this theme. The three findings a reviewer is most likely to raise from a skim are answered on the record above, and are collected here so they are not re-raised as discoveries: the doubled credit-preview install is one furniture block (candidate L17–28) and one labelled demo inside the page-elements tab (candidate L62–66), mirroring the original's demo structure, with the rework's ground stated in the tab (candidate L68); the surviving `[[module Rate]]` (candidate L60) is the original's own demo exhibit inside that tab, not a live widget beside the credit block; and the usage exhibit already names the posting form (`[[includ@@e :scp-jp@@:theme:petrifaction-jp]]`, candidate L36), so the plain-slug family flagged in seven sibling packages of this batch does not occur here — this candidate passed through the FIX4-REPOINT wave (443c608), whose repoints included its exhibits.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-petrifaction-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 大梦一场 主题版式
- **Author:** AsWheat
- **Source:** https://scp-wiki-cn.wikidot.com/theme:petrifaction — revision 14
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
