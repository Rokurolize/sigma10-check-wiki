# Review package — theme:basalt-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:basalt-jp — origin EN, population #3 [GOSIGN2-LEDGER (b) row 3]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 3]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 33 errors / 2 warns / 2 infos (pseudo-ref×23, hotlink×10); standing classes dispositioned in register c1 [T1-ROWS row 3; GOSIGN2-LEDGER (b) row 3]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — body blank (test-wiki tag mismatch), page-overflow on PC 1489px + all mobile 441/788px, content-overflow (code/table/floatbox), sample credit-modal; jsdelivr-gh + fonts.bunny.net direct links. [RENDER-ROWS-1 (RENDER-A row 3)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 3)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 4, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 4]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 3]
- Computed against: canonical commit f1138e4f4c7bcce523971efdee87d55f90302d3c; candidate file pages/theme:basalt-jp.txt sha256:ffd0dfa32aa2c0a5c1067f07f2ee7ec2a42947c9493c363ec596ec0d73e1a9b9; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 3) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×23 (class (iii), the draft-host delivery addresses) and hotlink ×10 (class (ii), the original-host asset addresses); the render row's items (the test-wiki tag-mismatch blank body, the KB-33/KB-34 overflow families, the KB-32 sample credit-modal, the jsdelivr-gh and bunny direct links under class (ii)) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:basalt | theme:basalt-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 304 (first translation; the candidate's credit block records 初訳時参照リビジョン: 304) | — |
| Source of this copy | Fetched from the live original 2026-11-17 into the mirror store (class FETCH-REGEN, hash-verified against review/sources.tsv) | Canonical file `pages/theme:basalt-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 1,753 lines / 46,385 bytes | 1,946 lines / 53,124 bytes |
| SHA-256 | df4b78d344536f5b7c363ac86b2ddc6f3c31b3647693f473169550e03fca17c5 | ffd0dfa32aa2c0a5c1067f07f2ee7ec2a42947c9493c363ec596ec0d73e1a9b9 |

Kind **K6**: a production JP counterpart exists (`old:theme:basalt` on SCP-JP, iti119's adaptation), and the candidate's translation is that existing translation adapted, not a fresh one — the credit block's 翻訳責任者 is iti119 and its 翻訳について line (added by the FIX-P4 wave) states the adaptation in the ruling-3 form. The production-side delivery of this migration is a separate one-line diff page (change-set section). Wave history: created at the campaign's start (d727e92, 2026-11-14), then seven further commits — three small body fixes (ffad285, 4b52123, b2c7917), the Phase 17 credit completion (8dcac74), the T1 field fixes (b816e10), the credit wave's translator fields (5c32672), and FIX-P4 (f1138e4), the wave that also repointed the dependent themes onto this candidate (per-theme record).

## Summary

Basalt is the composition's base theme: the bedrock layer under a large share of the JP candidates, and the one theme in this batch whose documentation body is carried entire — the full translated user documentation (usage, settings, memo system, ACS, exhibits) stands in the candidate alongside the CSS. Its port is therefore mostly translation (iti119's existing JP text, adapted) plus delivery repointing: the original's dual delivery (CDN minified layers plus local code blocks) is preserved address by address, the JP font support arrives by wave, and a run of malformed `url(...;` declarations the port inherited is repaired in the same wave. Measured churn (diff.md, the generator's count: +341/−148, 17 sections) is the batch's largest in absolute lines and the smallest in proportion. This package's change-set section carries the cross-theme record the brief asks for: 27 other candidates name this file as their base delivery.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 103 change blocks — 74 specific (71.8%), 24 heuristic (23.3%), 5 residue (4.9%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 33 |
| DRAFT-HOST | 25 |
| TRANS-UNANCHORED | 21 |
| EXHIBIT-RESTRUCTURE | 13 |
| INCLUDE-REPOINT | 13 |
| DELIVERY-HOST | 8 |
| SELF-DELIVERY | 8 |
| CSS-BODY | 4 |
| COMPONENT-SWAP | 3 |
| LINK-REPOINT | 3 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: the 13 EXHIBIT-RESTRUCTURE blocks adjudicate in section 8 (the exhibits are all carried; the label fires on repoints and translations inside exhibit regions). The 4 CSS-BODY blocks are the FIX-P4 wave's in-body edits (the font import swap, the `:root:lang(ja)` fallback block, the parenthesis repairs), narrated in sections 4 and the per-theme record as that wave's work. The 5 residue blocks are adjudicated individually: B2 and B4 in section 3 (the frames' CDN address repoints, for which the signature table has no label), B41 in section 4 (the body logo's address form), B43 in section 6 (a translated prose paragraph), B85 in section 8 (a translated table cell plus the footnoteblock escape). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:basalt-jp; original theme:basalt on scp-wiki at reference revision 304; candidate `pages/theme:basalt-jp.txt`. Provenance route: K6 (sources.tsv kind) — derived from the original at the reference revision, with the translation taken from the existing production JP adaptation by iti119 (production page `old:theme:basalt`, fullname `existing:old-theme-basalt` in this repo's import) and adapted; R4 therefore arises and is answered by the credit block's 翻訳について line and by the production record in the change-set section. The frame: four interwiki-style includes at the head (candidate L1–15, section 3), the gate at candidate L70, the credit block at L72–82.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; for a K6 theme the baseline is double (the EN original and the production adaptation), and this package diffs against the EN original while recording the production relationship where it bites.
- **Verify:** The sources.tsv row for basalt-jp (kind K6, the production note); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the production drift items are recorded in the change-set section.

### 1. Credit and attribution

- **What:** The candidate's credit block (candidate L72–82) is the `:scp-jp:credit:start-preview`/`end-preview` form carrying the eight ruling-3 fields plus the adaptation line: タイトル: Basalt Theme (the title field keeps the English title, as does 原題）; 翻訳責任者: iti119; 翻訳年: 2022; **翻訳について: iti119 による既存の翻訳を基に改変したものです。** (added by FIX-P4); 著作権者: Liryn、Placeholder McD; 作成年: 2021 (the original's banner year, "[2021 Wikidot Theme]"); 初訳時参照リビジョン: 304; 元記事リンク: the scp-wiki original (candidate L81 — the recorded host, no discrepancy). The fields arrived in layers: the preview pair, the revision, and the source link by Phase 17 (8dcac74); title/author/year by the T1 fixes (b816e10); translator and translation year by FIX-CREDIT-C (5c32672); the adaptation line by FIX-P4. A bare `[[module Rate]]` stood in the body region of the candidate's early form (as in the original); FIX-P4 removed it, the preview module being rate-bearing (BARE-RATE-DEL). There is no license box on either side: the original carries none, the theme's licensing rides on the credit block and the banner comment inside the bedrock code (candidate L86–102: "by Liryn & Placeholder McD / with thanks to EstrellaYoshte / Built on Bedrock", retained verbatim). The T7 item is this theme's own tail module (section 3 of the taxonomy's T7 entry): the credit-controls module at candidate L1758–1814, whose selector set is the canonical form the other themes' supplements copy — here it is not a supplement received but the family's source text, scoped by its own porter comment to the two credit-module containers (section 10).
- **Why:** P3/T1 (KB-09 for the bare Rate's removal; ruling 3 for the fields, including its adaptation clause, which is what makes an adapted existing translation honest in the credit block rather than a silent overwrite of a human translator's work — the owner's attribution rule keeps the human name where it matches the live JP creator, and iti119 is that name).
- **Verify:** Read candidate L72–82 against the fields; `grep -n 'module Rate' candidate.txt` returns nothing; the T7 module is candidate L1758–1814.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified; the adaptation line and the Rate removal by FIX-P4).

### 2. Includes and components

- **What:** The candidate's head includes are the four interwiki-style frames (section 3) plus two bare component includes carried from the original's composition: `component:betterfootnotes` (candidate L15) and `component:acs-animation` (inside the argument-gated region, candidate L67) — the COMPONENT-SWAP ×3 blocks are these and the frames losing their `:scp-wiki:` site prefix to local resolution (the candidate's frames read `[[include component:interwiki-style`, not `:scp-jp:component:...`; on the JP wiki the bare name resolves to the same component). The credit pair is section 1. Inside the body, the exhibit includes are the image-block exhibits (section 8) and the usage exhibits whose include lines the FIX-P4 wave repointed from `theme:basalt` to `theme:basalt-jp` (three lines, candidate L1430 region and L1452–1454 region; INCLUDE-REPOINT ×13 counts these with the frames' address repoints). No foreign include is kept in a live position: every `:scp-wiki:` include prefix in the original is gone from the candidate.
- **Why:** P1 (KB-15): live includes name the counterpart that exists on the JP wiki; for shared components the bare local name is that form. The usage-exhibit repoints are the same rule inside exhibits (an exhibit teaching the EN include name would teach a form that does not resolve to this candidate).
- **Verify:** `grep -n '\[\[include' candidate.txt` — no `:scp-wiki:` prefix remains; the three exhibit lines name theme:basalt-jp.
- **Disposition:** Applied (the exhibit repoints by FIX-P4); no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** Basalt's delivery is dual, and the candidate preserves the original's architecture address by address. Layer one is external and prebuilt: the head frames at priorities 1 and 2 name the minified normalize and bedrock files, and the bedrock code block repeats the same two addresses as `@import`s at its head. The original names `cdn.scpwiki.com/theme/en/basalt/...` in all four places; the candidate names `cdn.jsdelivr.net/gh/Rokurolize/Basalt@gh-pages/...` (five jsdelivr lines in total: the two frame addresses, the two code-block imports, and one documentation exhibit naming the normalize file) — residue blocks B2 and B4 are the two frame lines of this repoint, for which the signature table has no label. Layer two is local: frame priority 3 and the six head module fragments import this page's own code blocks /1 through /6 (the bedrock main in the hidden `default` div, candidate L83–1143; the second vars block L1146–1349; the small blocks L1352–1401; the module at L1403–1419), their addresses repointed from scp-wiki.wdfiles.com to the candidate's own /1../6 on the draft host (the 25 DRAFT-HOST blocks count these with the asset addresses of section 4; DELIVERY-HOST ×8, SELF-DELIVERY ×8). Layer three is the wave's addition: FIX-P4 appended the full NORMALIZE source as a local code block in a hidden div at the tail (candidate L1830–1946), so the page now carries locally the text its first frame still loads from the mirror. The frames' priorities (1 normalize, 2 bedrock-min, 3 own /1, 4 own /2) are the original's own numbering, retained.
- **Why:** P4/T9 in both its forms. The local layers take the candidate's own addresses (draft host at draft stage, KB-41 class (iii)). The external layers are the theme author's own delivery architecture — Basalt is distributed as prebuilt files, and the original page itself loads them from a CDN rather than from its code blocks — so the candidate mirrors the architecture onto the campaign's own mirror of the author's repository and the item is dispositioned class (ii) (original-state CDN delivery), which is the ledger's P4 verdict for this theme. The FIX-P4 normalize append narrows the exposure without changing the architecture: the source text is now in the page, so a future repoint of frame 1 to the local block is a one-line change with the content already present.
- **Verify:** `grep -n 'jsdelivr\|local--code' candidate.txt` — five jsdelivr lines, the frame and module addresses on the draft host; `sed -n '1830,1845p' candidate.txt` shows the appended NORMALIZE block.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P4 DISPOSITIONED, delivery class (ii)); the draft-host forms are DISPOSITIONED (class (iii)); the normalize localization is FIXED in content by FIX-P4 (the frame address itself stands under the class (ii) disposition).

### 4. Fonts and assets

- **What:** Fonts: the bedrock block imports Sofia Sans (the theme's header/UI face), and the original's import names fonts.bunny.net (original L100 — T4's pattern-5 live item). FIX-P4 repointed it to the identical Google Fonts URL (candidate, bedrock imports region) and added the Noto Sans JP import beside it (FONT-IMPORT, JPFONT-LOAD), together with a `:root:lang(ja)` fallback block defining the four `--*-font-fallback` variables to a Noto Sans JP stack — Basalt's JP font mechanism is variable-level (its stacks are assembled from variables), so the insertion lands as fallback definitions rather than per-stack edits, preceded by the porter's Japanese comment explaining that Sofia Sans has no Japanese glyphs (section 10). Assets: the theme's functional logo variables (`--logo`, the `--memo-logo` sets) name the candidate's own uploaded files on the draft host (`local--files/theme%3Abasalt-jp/...`), and FIX-P4 repaired the run of malformed `url(...;` declarations (missing closing parentheses) across the LIGHTLOGO/DARKLOGO memo sets and the dark-mode logo in both bedrock blocks — in the pre-wave candidate those declarations were invalid and the memo logos could not load. The documentation's image exhibits name the original's logo file on the original's host: the body logo line (residue B41: `scp-wiki.wikidot.com/local--files/...` in the original, `scp-wiki.wdfiles.com/local--files/theme%3Abasalt/basalt-theme-logo.svg` in the candidate, the 4b52123 repoint from a draft-host Japanese-named form) and the six table exhibits (candidate L1671–1726, repointed by b2c7917 from jsdelivr addresses to the same wdfiles file). T1's hotlink ×10 and T4's pattern-5 count (7× scp-wiki.wdfiles local--files) are these exhibit addresses.
- **Why:** P7/KB-16 for the font work (the bunny item is the ledger's named FIXED-where-named case: the §(c3) preamble records the bunny.net repoint as FIXED for the named set including basalt). P5's asset rule meets its standing disposition for the exhibits (original state, class (ii) / KB-58), while the theme's own functional assets are JP-side uploads as the rule requires. The parenthesis repairs are a plain validity fix: a `url(` left unclosed invalidates the declaration.
- **Verify:** `grep -n 'bunny' candidate.txt` returns nothing; `grep -n 'lang(ja)' candidate.txt` shows the fallback block; `grep -n 'url(https://sigma10-jp-test' candidate.txt | grep -v ');'` returns nothing (no unclosed url remains).
- **Disposition:** Font repoint and fallback FIXED (FIX-P4; the ledger's bunny preamble); exhibit assets DISPOSITIONED (class (ii) / KB-58); functional-asset addresses DISPOSITIONED (class (iii) draft form).

### 5. Header, sidebar, and site furniture

- **What:** The P9 question inverts for this theme: Basalt does not override the site's header variables, it *is* the header furniture for every page that includes it — its bedrock variables (`--header-title`-family, `--logo`, the memo system) are the composition's defaults, carried from the original unchanged in name and role. No JP-side variable override was added by the port. The reader-visible furniture strings that stand in English are the memo headings inside the bedrock variables (e.g. `--memo-heading: "NOTICE FROM THE DEPARTMENT OF MISCOMMUNICATIONS"`), which are the fictional departments' names as the theme's design text; iti119's translation, which the candidate adapts, keeps them, and the candidate keeps them likewise.
- **Why:** Ruling 2 covers header and title language as translation taste; for the base theme the stronger ground is fidelity to the existing JP adaptation, whose choices the candidate is chartered to carry (K6), not to re-translate.
- **Verify:** `grep -n 'memo-heading' candidate.txt` — the English department strings; compare the variable names against the original's bedrock vars block.
- **Disposition:** Standing (carried from the existing adaptation; ruling 2 for the language point).

### 6. Text translation

- **What:** The documentation body is translated entire (TRANSLATION-ANCHORED ×33, TRANS-UNANCHORED ×21, and the residue translations of section 8): the usage and settings prose, the memo and ACS documentation, the tabview and table exhibits' text, and the section headings (+* Info → +* 情報， +* Coloring → +* 色付け）. The translation is iti119's existing JP text adapted (section 0), which is why the anchored share is the batch's highest: most pairs match the original's structure line for line. Residue B43 (original L1435 → candidate L1440) is the Info paragraph: translated, its user links dropped to plain names, and its two outbound links (Bedrock's wiki page, the Basalt GitHub home) kept in their full original URL form — recorded in section 7. The CSS-internal text is the banner comment (retained in English, the original's attribution record) and the memo headings (section 5).
- **Why:** P10 with the K6 ground: where a human JP translation exists and is the production text, the port adapts it rather than re-translating (the credit block's 翻訳について line is the disclosure of exactly this). R1's comment half stands as in the sibling packages: the banner is the original's own record.
- **Verify:** Sample any anchored pair from classification.json against the two files; the adaptation disclosure is candidate L76.
- **Disposition:** Standing (the port itself, on iti119's text); no translation charge stands in any T-row for this theme.

### 7. Links

- **What:** The credit source link (candidate L81) names `https://scp-wiki.wikidot.com/theme:basalt`, the recorded host in review/sources.tsv — no discrepancy to probe. Inside the body, LINK-REPOINT ×3 and the residue pairs record the localization pattern of iti119's text: the ACS guide link repointed from the full scp-wiki URL to the local page name `[[[anomaly-classification-system-guide|...]]]` (B87, candidate L1663–1664, with its section prose translated); the "Included with Basalt" list repointed from full component URLs to local `component:betterfootnotes` / `component:acs-animation` names, with the `[[*user EstrellaYoshte]]` links rendered as 作者： EstrellaYoshte text (B101, candidate L1743–1744 — the JP form drops the user-link markup, the name survives); and, in the other direction, the Info paragraph's Bedrock and GitHub links kept as full original URLs (B43, section 6). The exhibit include repoints are section 2.
- **Why:** P11: prose links take the JP counterpart where the translation does so; the package records the mixed practice exactly as the bytes show it (two localized, one paragraph's links kept full-form) rather than harmonizing the record. The user-link rendering is the existing translation's form.
- **Verify:** Read candidate L1663–1664 and L1743–1744 against original L1659–1660 and L1739–1740.
- **Disposition:** Standing (the existing translation's practice, carried); no dead reference stands (each kept URL resolves to the original's own pages).

### 8. Structure

- **What:** The closing rule holds: the candidate preserves the original's architecture in order — head frames and conditional modules, gate and credit, the bedrock code blocks, the documentation body with its exhibits in the original's order, the tail modules — and the JP additions arrive at the head (frame addresses), inside the bedrock head (font imports and the fallback block), and at the tail (the T7 module predates the waves; the NORMALIZE block is FIX-P4's append). The exhibit census decides the 13 EXHIBIT-RESTRUCTURE blocks: every exhibit in the original stands in the candidate — the tabview set (including the long-tab and footnote exhibits), the six table image-block exhibits, the memo exhibits, the ACS exhibits — translated and, where their addresses named the EN theme, repointed (sections 2, 4). Nothing was restructured; the label is the standing false-fire on repoints and translations inside exhibit regions. Two one-line body events belong here: the ffad285 escape, which renders the documentation's `[[footnoteblock]]` as escaped text `@@[[footnoteblock]]@@` where the original calls the module live (candidate L1658 region; residue B85 pairs it with the translated table cell でも本当に？ above it) — in the candidate's composition the live call at that point would render the page's footnote block inside the exhibit flow, and the port's fix keeps the token visible as the exhibit's subject; and the FIX-P4 removal of the body's duplicate bare Rate (section 1).
- **Why:** R3's census is the deciding check, and here it comes out clean: no exhibit, section, or rule was dropped. The escape is recorded as a rendering-form change with its visible effect, the smallest class of structural edit.
- **Verify:** `grep -n 'tabview\|image-block\|collapsible' candidate.txt` — the exhibits present; compare the section order of the two files' bodies.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** No WS-ONLY blocks are recorded for this pair, and no re-indentation class arises: the carried-over bedrock and body text keeps the original's formatting, and the wave edits are line-level (imports, addresses, single declarations), so there is no formatting churn to disclose.
- **Why:** The section states its ground rather than standing empty: for this pair the classifier's formatting classes do not fire.
- **Verify:** The label table in classification.json (no WS-ONLY entry).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three porter texts, all disclosed. (1) The Japanese comment above the `:root:lang(ja)` fallback block (bedrock imports region): 「JP 字形のフォールバック: Sofia Sans には日本語グリフが無いため、読み込んだ Noto Sans JP を各フォントスタックのフォールバックとして指定する。」 — the FIX-P4 wave's explanation of its own font mechanism, COMMENT-TEXT ×1's basalt instance. (2) The two English comments at the T7 module's head (candidate L1760–1761): "SCP-JP Wikidot Basalt credit controls: support the native direct-child anchor shape." and the explanation that the frozen JP component markup emits `.creditButton > a` while the source Basalt rules cover `.creditButton > p > a`, scoping the correction to the two current credit-module containers — the module's own design note, and the reason the taxonomy cites this set as canonical with its scope stated. (3) The credit block's 翻訳について line is attribution, not annotation, and is counted in section 1. There are no `[!-- --]` notes.
- **Why:** R2: porter-added text is part of the change record; here two of the three carry mechanism explanations a future porter needs, which is the annotation class working as intended.
- **Verify:** Read the three texts at the places named.
- **Disposition:** Standing (recorded).

### 11. Dispositions and exceptions

- **What:** Four groups. (1) T1's standing classes: pseudo-ref ×23, class (iii) — the draft-host delivery and asset addresses of sections 3–4; hotlink ×10, class (ii) — the original-host exhibit addresses of section 4. (2) The render row's items: the blank body (the test wiki's `[[iftags +テーマ]]` tag mismatch — the candidate's gate names the JP tag while the test wiki's pages carry the EN tag set; an environment artifact of the check composition, the same family as the al-slop row's); the page-overflow (PC 1489px and all mobile widths) and content-overflow (code/table/floatbox) items, dispositioned in the KB-33/KB-34 overflow families; the sample credit-modal item (KB-32: the preview form has no modal mechanism, by design of the check composition); and the jsdelivr-gh + fonts.bunny.net direct links, class (ii) — with the bytes' footnote that the bunny import no longer stands in the candidate at all (FIX-P4 repointed it, section 4), so that half of the item is closed by fix in the current file. (3) T4's charges as adjudicated in §(c3): P4 DISPOSITIONED (delivery class (ii)), P5 DISPOSITIONED (class (ii) / KB-58), with the bunny half of pattern 5 in fact FIXED by the wave as the preamble records. (4) The K6 production relationship: the candidate is not the production page; the production drift recorded in sources.tsv (collapsible difference, tab difference) and the one observed credit difference (the production page's credit block reads 作成年: 2022 where the candidate reads 2021, the original's banner year) are production-side facts, recorded in the change-set section, not charges against this candidate.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; items closed by fix are distinguished from items closed by disposition.
- **Verify:** Each item names its deciding record above; the T1 classes are register c1 of GOSIGN2-LEDGER, the render items are the theme's c2 block, the production facts are the sources.tsv row and the phase17-diff page.
- **Disposition:** DISPOSITIONED (groups 1, 2, 3 as classed); group 4 recorded.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 3): exit 1, 33 errors / 2 warns / 2 infos; the errors split pseudo-ref ×23 and hotlink ×10, the standing classes of section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-A row 3): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 4, LOCALIZE-A): FINDINGS jointly, display-affecting findings 1 (the pattern-4 delivery item); the ledger §(c3) line records P4 DISPOSITIONED and P5 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +341/−148 in 103 change blocks / 17 sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:basalt-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 3; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The wave history, edit by edit

Eight commits touch this file; the ledger's class-level outcomes (§(c3): P4 DISPOSITIONED, P5 DISPOSITIONED, P3 FIXED by the credit waves) sit on top of them.

1. **d727e92 (2026-11-14), creation.** The candidate enters the canonical repo at the campaign's start, already in its dual-delivery form (jsdelivr mirror addresses in the frames and imports, draft-host local addresses, iti119's translated body, the T7 tail module).
2. **ffad285.** One line: the documentation body's `[[footnoteblock]]` escaped to `@@[[footnoteblock]]@@` (section 8).
3. **4b52123.** One line: the body logo image repointed from a draft-host Japanese-named file (`basalt-テーマ-logo.svg`) to the original's logo on scp-wiki.wdfiles.com (residue B41, section 4).
4. **b2c7917.** Six lines: the table image-block exhibits' logo addresses repointed from jsdelivr addresses to the same wdfiles file (section 4).
5. **8dcac74 (Phase 17).** The credit block completed to the preview pair form, with 初訳時参照リビジョン: 304 and the 元記事リンク source field added; the same phase produced the production delivery page (change-set section).
6. **b816e10 (gosign2 T1 fixes).** The credit fields タイトル / 原題 (Basalt Theme), 著作権者 (Liryn、Placeholder McD), 作成年 (2021) added.
7. **5c32672 (FIX-CREDIT-C).** 翻訳責任者: iti119 and 翻訳年: 2022 added — recording, correctly, that this translation is the existing human one.
8. **f1138e4 (FIX-P4).** The wave named for repointing the dependent themes' base imports (39 files repo-wide) makes, in this file, the largest single edit set of the theme's history: the 翻訳について adaptation line; the Sofia Sans import repointed from bunny to Google Fonts and the Noto Sans JP import added; the `:root:lang(ja)` fallback block with its porter comment; the run of unclosed `url(...;` declarations repaired across both bedrock blocks; the body's duplicate bare Rate removed; the three usage exhibits repointed to `theme:basalt-jp` (one also repairing a mixed-language setting name, `another-テーマsetting` → `another-themesetting`); and the NORMALIZE source appended as a local code block. A reader who meets this commit by its subject ("pattern-4 repoint of base-theme CSS imports") will not guess that the base theme's own JP font support and validity repairs are inside it; the package record follows the diff.

### Why this theme's record is written from the bytes

Basalt is the theme other packages cite. The alcur package records what depending on this file means from the dependent side (an import plus an inline copy that will not inherit this file's future fixes); this package records the base side: every fix landed here (the font fallback, the parenthesis repairs, the normalize localization) propagates to the 27 dependents that import the delivery, and none of it propagates to inline copies. That asymmetry is the practical content of ruling 1 (dependents import the JP base candidate), and it is visible only when the base's own wave history is written out in full, as above.

## Change set outside the two diffed files

The diff covers two files; this theme's record is the widest in the batch, in four parts.

**The production delivery.** `pages/phase17-diff-basalt-jp.txt` is how this migration reaches the live SCP-JP wiki: a 22-line instruction page carrying a one-line diff against the production page `old:theme:basalt` (add 初訳時参照リビジョン: 304 to its credit block). The production page itself — imported here as `pages-existing/existing:old-theme-basalt.txt`, 4,121 lines, iti119's adaptation ("Edited by iti119 for SCP-JP" in its CSS) — stays the live theme; the candidate in this package is the Sigma-10 review copy of the same migration. The recorded production drift (sources.tsv: collapsible difference, tab difference) and the observed credit-year difference (production 作成年: 2022; candidate 2021, the EN banner year) stand as production-side facts; neither is a charge against the candidate, and the phase17-diff page is the whole of the production-side change set.

**The sample.** `pages/theme-decoration-sample-basalt-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)).

**The inbound set.** 33 files under `pages/` name `theme:basalt-jp` or its colon-encoded form. Setting aside this candidate itself, its sample, one further sample (enlightened-eyes), and the two `/start` index pages that list it, **27 theme candidates** depend on this file by import, frame address, or foundation line: 512-onwards-jp, admo-jp, alcur-theme-jp, andesite-jp, another-night-jp, bedrock-jp, candela-jp, deepspace-jp, eigenmachine-jp, eigenvector-jp, enlightened-eyes-jp, gp-refresh-jp, hytoth-two-jp, immrama-jp, lumina-jp, marchen-jp, monotypical-jp, opinions-broadcaster-jp, ordopharm-jp, shivering-night-jp, skipos-jp, starbasalt-jp, stargazer-jp, stellar-jp, winddew-in-hand-jp, wish-for-miracle-jp, and 5k-jp. The FIX-P4 wave (39 files) is the commit set that aligned these dependents' base addresses to this candidate, per ruling 1: a dependent imports the JP port candidate's delivery, never the upstream branch's. Any future change to this file's delivery addresses or fallback variables is therefore a 27-file event, and this package's sections 3–4 are written to be read by the porters of those files as well.

**The mirror.** The frames' and imports' jsdelivr addresses name the repository `Rokurolize/Basalt@gh-pages` — the campaign owner's mirror of the theme author's Basalt repository, which is the file set the EN theme itself is distributed from. It is not part of this repo, and the class (ii) disposition in section 3 is the record that governs it.

## License and attribution

- **Title:** Basalt Theme
- **Author:** Liryn、Placeholder McD
- **Source:** https://scp-wiki.wikidot.com/theme:basalt — revision 304 (revision date 2026-07-22 01:52:12)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: iti119 — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
