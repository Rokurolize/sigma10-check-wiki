# Review package — theme:opinions-broadcaster-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:opinions-broadcaster-jp — origin CN, population #211 [GOSIGN2-LEDGER (b) row 211]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now f9575405fea534bbe3a59a167d7c8e424125b5c48e2b122a04b4b64798bb7616); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 34 errors / 4 warns / 2 infos (hotlink×29, foreign-include×3, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 226; GOSIGN2-LEDGER (b) row 211]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page sidebar-not-opening + candidate-own runtime hosts (cdn.jsdelivr.net, fontsapi.zeoseven.com, sigma9.scpwikicn.com, scp-wiki-cn / scpsandboxcn chains) recorded verbatim; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN10))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN10))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 210, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 210]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 211]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:opinions-broadcaster-jp.txt sha256:f9575405fea534bbe3a59a167d7c8e424125b5c48e2b122a04b4b64798bb7616; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 211) |
| Standing items | **NAMED EXCEPTIONS** — the four Sigma-9 delivery imports (campaign AGENTS.md §6: no JP counterpart exists; Sigma-10 is not a Sigma-9 substitute, never repoint) and the documented companion-component examples, one of which names a component verified never to have existed on any wiki (sources.tsv K5a-ii). **DISPOSITIONED** — the remaining live code references (P4, "delivery class (ii): original-state CDN delivery", GOSIGN2-LEDGER §(c3)); T1's 29 hotlinks (class (ii) / KB-58 family) and 2 pseudo-refs (the draft-host basalt imports, class (iii)); the render row's items (the page's sidebar-not-opening, the runtime host chains; the sample's render run returned no machine verdict and is recorded as such, section 11). **NOTED, not flagged** — the frame's code-block address resolves to the comment-area template block (per-theme record, item 1) and the mono stack's JP fallback face is named but not loaded in this file (item 2) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | The §6 items above are this theme's named exceptions (the sweep's population-level named exception remains theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:opinions-broadcaster | theme:opinions-broadcaster-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 6 (first translation; the candidate's credit block records 初訳時参照リビジョン: 6) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-opinions-broadcaster.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:opinions-broadcaster-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 1,941 lines / 80,954 bytes | 1,975 lines / 97,367 bytes |
| SHA-256 | cecc92a0d763a6f7daed96d3e2fc336e45184e66f28cb5a3090db4d60291abde | 38036dd838821276b141bdf9a9c98feaf4cc89296d236d3e4df4a1e05ab1d15e |

Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave, in the layered form sources.tsv records as kind K5b-3: the candidate layers over theme:basalt-jp, and this package's diff covers the theme's own layer (the base is imported, not carried, on both sides). sources.tsv carries two further notes for this theme (class K5a): the original has been superseded upstream since revision 6 (follow-up diff artifact `diff-opinions-broadcaster-from6.txt` in the campaign record, outside this package's scope), and the original's documented component `:scp-wiki-cn:component:opinions-backend` never existed on any wiki (NOTFOUND-verified twice, plus 404 probes; section 2). Wave history: a89eccf (CN10 integration), f1138e4 (FIX-P4, the base-import repoint), 8c62b7b (FIX4-IWA, the frame wave; the verdict stamp's computed-against commit). No FIX5 commit touches this file.

## Summary

Jonuarl Reden's "Opinions Broadcaster" （谈天说地）, a Basalt derivative built on his in-development "Polished Basalt" fork, and the batch's most documentation-heavy theme: a 596-line main `[[module CSS]]`, a short second module, and some 1,300 lines of usage documentation written in the author's own voice, full of his bracketed asides. The port repoints the Basalt base imports to the basalt-jp candidate on the draft host and adds the font loads the stacks need (the Basalt chain's faces plus the JP pair) at the head of the main module, with an annotated :root override block at its tail setting the JP stacks and the theme's title variables. The four Sigma-9 component deliveries the theme imports (the CN component:theme, acs-animation, and betterfootnotes code, and the EN hoverlinks code) are kept exactly as they are: campaign AGENTS.md §6 names them as exceptions, because no JP counterpart exists and Sigma-10 is not a Sigma-9 substitute. The author's own GitHub Pages CSS (the six Polished-Basalt files) and the remaining live references are T4's charged P4 item ("≈14 live non-sanctioned code references — the theme as posted renders entirely off the CN site and the author's personal GitHub Pages, against the author's own warning"), dispositioned as original-state CDN delivery; the author's warning comment itself is carried, translated, at the head of the module. The credit furniture (a bare Rate and no credit module at all) is swapped for the JP preview block, the documentation's component demos are repointed where a JP form exists, and the whole documentation, asides included, is translated in the author's register. Measured churn (diff.md: +522/−488, 1,010 changed lines in 307 change blocks / 44 diff sections) is mostly that translation.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 307 change blocks — 160 specific (52%), 147 heuristic (48%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 165 |
| TRANSLATION-ANCHORED | 130 |
| ANNOTATION | 38 |
| COMMENT-TEXT | 18 |
| EXHIBIT-RESTRUCTURE | 17 |
| INCLUDE-REPOINT | 15 |
| GLYPH-FORM | 12 |
| DRAFT-HOST | 2 |
| CONTENT-STRING | 2 |
| ESCAPED-INCLUDE | 2 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| DELIVERY-HOST | 1 |
| CSS-BODY | 1 |
| CREDIT-PREVIEW | 1 |
| IFTAGS | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| LINK-REPOINT | 1 |

Adjudication for this README (every specific block was read against the bytes; the heuristic mass was resolved by shape): the 295 translation-family blocks are the documentation and prose translation (section 6). The 38 ANNOTATION blocks need the batch's most careful adjudication: the theme's documentation is written with the author's own `[!-- --]` asides throughout (48 such lines in the original, 48 in the candidate), and the ANNOTATION label fires on those lines as they change under translation — they are the author's content, not porter annotations; exactly one porter annotation exists in the file, a CSS comment in the main module (section 10). The 17 EXHIBIT-RESTRUCTURE primaries are the documentation's demo zone (original L891–1164): live component demos whose include lines are repointed (the INCLUDE-REPOINT second labels are the real change) and translated specimen lines; the exhibit census in section 8 shows every demo carried. The two ESCAPED-INCLUDE blocks are the companion-component examples of section 2. After adjudication no block is left unexplained, and no residue appendix is needed (0 residue blocks).

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:opinions-broadcaster-jp; original theme:opinions-broadcaster on scp-wiki-cn at reference revision 6; candidate `pages/theme:opinions-broadcaster-jp.txt`. Provenance route: derived at the reference revision by the LOCALIZE-S2-E wave, layered over theme:basalt-jp (kind K5b-3; the Provenance note above). The frame moved: the original opens with the author's head annotation and its main module, and its gate stands deep in the file (original L612: `[[iftags +版式 -告诫！！！！！！！！！！]]`, a positive tag plus a negative joke tag naming a branch-local warning tag); the candidate opens the same way, and its gate (candidate L631: `[[iftags +テーマ]]`) converts the positive tag and drops the negative one, which names a CN tag with no JP counterpart. The interwiki-style frame stands immediately before the gate (candidate L626–629).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for opinions-broadcaster-jp (kind K5b-3 and its K5a notes); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` in a centering block (original L620–623) and nothing else — the theme carries no credit module pair; its attribution lives in its documentation (the byline at original L667: "由[[*user Jonuarl Reden]]为SCP基金会中文分部制作", and a resource-attribution table near the tail, original L1912–1939 zone, listing the art resources with their authors, CC-BY-SA 3.0, and hosting). The candidate deletes the Rate exhibit and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block directly under the gate (candidate L633–642) carrying the eight ruling-3 fields (title 談天説地テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 谈天说地 版式, the original's simplified-Chinese title kept as the original-title field; 著作権者 Jonuarl Reden; 作成年 2026; 初訳時参照リビジョン 6; the source link, candidate L641, on scp-wiki-cn.wikidot.com, the host sources.tsv records for the original). Author check against the original: Jonuarl Reden is the theme's author (the byline above; his GitHub Pages host the theme's CSS under jonuarlreden.github.io), and the documentation's component credits name their own authors in place (EstrellaYoshte for betterfootnotes and acs-animation, Croquembouche for hoverlinks, candidate L685–687), carried in translation, so no creator the original names is dropped from the record and no flag of the sibling standing arises. The attribution table is carried in translation at the tail (candidate L1943–1973 zone; its rows are two of the EXHIBIT-RESTRUCTURE false-fires). No license box exists on either side. T7 credit-module CSS: neither file carries a credit-rule group (no `creditButton` selector on either side; the credit styling arrives with the Basalt chain), so no T7 item arises.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (a kept Rate would be the KB-09 duplicate). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` returns only the preview pair at L633 and L642; read candidate L633–642 against the eight fields.
- **Disposition:** Applied; no credit item is charged in the theme's T4 row.

### 2. Includes and components

- **What:** The candidate's live includes are three: the interwiki-style frame (candidate L626–629, section 3) and the credit pair (section 1). The documentation zone carries the theme's component demos: fifteen include lines are repointed to their JP or bare forms where a counterpart exists (the INCLUDE-REPOINT blocks, original L891–1164 → candidate L922–1195), including the component credits list's hoverlinks entry, which converts from an intra-wiki link to a labeled link to the EN component page, its home (original L656 → candidate L687). The usage example changes form: the original's annotated struck-prefix example (original L654–655 zone) becomes the bare `@@[[include theme:opinions-broadcaster-jp]]@@` (candidate L685 zone, in its size-160% line), naming the candidate's own fullname — the correct page under the posting name. Three escaped example includes keep their CN names (candidate L1544, L1567, L1584): the theme's documented companion components, `:scp-wiki-cn:component:opinions-broadcaster-comment-area` (twice, the comment-area head and tail forms) and `:scp-wiki-cn:component:opinions-backend`. These are T1's foreign-include ×3, and their standing is documentary, not accidental: no JP counterpart of either component exists in the composition, and the backend component never existed anywhere — sources.tsv records it as NOTFOUND-verified twice plus 404 probes (class K5a-ii) — so there is nothing to repoint to; the examples document the system as the author published it, and the campaign's standing exception for this theme's foreign components (AGENTS.md §6, quoted in section 3 for the delivery half of the family) covers the shape. The four live Sigma-9 delivery imports are section 3.
- **Why:** P1/T2 are satisfied where a JP counterpart exists; where none exists, the named-exception ground applies instead of a repoint, and a documented-but-nonexistent component is recorded as the original's own defect, not repaired by inventing a target.
- **Verify:** `grep -n '\[\[include :scp-wiki-cn:' candidate.txt` returns exactly the three escaped example lines above; `grep -n '\[\[include' candidate.txt` shows the frame, the credit pair, and the repointed demos.
- **Disposition:** Applied, with the three examples standing as the named exception recorded here.

### 3. Delivery and code loading

- **What:** The theme's own CSS lives in its main `[[module CSS]]` (original L3–598; candidate L3–617), which is also its import head. The original's imports, in order: three CN Sigma-9 component code deliveries (original L4–6: `component:theme/1`, `component:acs-animation/1`, `component:betterfootnotes/1` from scp-wiki-cn.wdfiles.com), Basalt itself (original L7–8: `theme:basalt/1` and `/6` from the same CN host), the EN hoverlinks component code (original L10, scp-wiki.wdfiles.com), Font Awesome from cdnjs (original L11), the author's translated warning comment, and the six Polished-Basalt files from his GitHub Pages (original L29–34 zone: jonuarlreden.github.io/Polished-Basalt/p1–p6). The candidate's import head (candidate L4–34) makes exactly three kinds of change. (a) The Basalt pair is repointed to the base's JP candidate on the draft host (candidate L13–14: `local--code/theme%3Abasalt-jp/1` and `/6`; the FIX-P4 wave's work, class (iii) mechanics). (b) Seven font loads are added ahead of everything (candidate L4–10, section 4). (c) Everything else is kept byte-for-byte in form: the three CN component deliveries and the EN hoverlinks delivery (the §6 named exceptions: "FIX-MECH six foreign includes with no JP equivalent (incl. opinions-broadcaster's Sigma-9 delivery via component:theme, component:acs-animation, component:betterfootnotes, component:hoverlinks) — Named exceptions: no JP counterpart exists; the cross-wiki includes resolve and render identically. Sigma-10 is NOT a Sigma-9 substitute — never repoint these to it."), Font Awesome, and the six GitHub Pages files. T4 charged the kept set as "P4 MISSED (≈14 live non-sanctioned code references — the theme as posted renders entirely off the CN site and the author's personal GitHub Pages, against the author's own warning …)" (LOCALIZE-ROWS row 210); the ledger dispositions the P4 item as delivery class (ii) (§(c3)), and §6 carves the Sigma-9 four out of it as named exceptions. The author's warning comment itself (original L14–25: he advises against hotlinking his internal-development GitHub resources because they may break) is carried in translation directly under the imports (candidate L19–25) — the port preserves the warning alongside the dependence it warns about, which is the honest form of the disposition. The candidate's own delivery is completed by the frame (candidate L626–629, priority=1, naming the candidate's own first code block on the draft host); per-theme item 1 records what that address resolves to. The second module (13 lines, original L607–619 → candidate L642–654, the hover-helper rules) is carried unchanged in substance.
- **Why:** P4/T9 govern code delivery; the base repoint is the FIX-P4 pattern. The kept imports are not narrated as a normal supplement: the Sigma-9 four are named exceptions with the §6 ground quoted, and the rest are the charged P4 item under its ledger disposition.
- **Verify:** `grep -n '@import' candidate.txt` — the seven font loads, the three CN component lines, the basalt-jp pair, the hoverlinks line, Font Awesome, and the six GitHub Pages lines, in the order above.
- **Disposition:** DISPOSITIONED (P4 remainder, delivery class (ii), GOSIGN2-LEDGER §(c3)); NAMED EXCEPTION (the Sigma-9 four, AGENTS.md §6); the basalt repoint is class (iii) mechanics.

### 4. Fonts and assets

- **What:** Loads added: seven Google Fonts lines at the main module's head (candidate L4–10: Inter, Sofia Sans, JetBrains Mono, Noto Sans JP, Noto Serif JP, Domine, and Material Symbols Outlined) — the Basalt chain's faces (Sofia Sans is Basalt's display face; Inter and JetBrains Mono its text and mono faces) loaded explicitly now that the base arrives as the basalt-jp candidate, plus the JP pair. Stacks: the main module's tail carries the annotated :root override block (candidate L605–617): `--header-font`/`--title-font`/`--UI-font: "Sofia Sans", "Empo Sans", "Noto Sans JP", sans-serif`; `--body-font: "Inter", "Noto Sans JP", sans-serif`; `--mono-font: "JetBrains Mono", "Maple Mono NF CN", "Noto Sans Mono", "Noto Sans JP", monospace`; `--serif-font: "Domine", "Noto Serif JP", serif`. First-face check: Sofia Sans, Inter, JetBrains Mono, and Domine are loaded by the added lines; "Empo Sans" and "Maple Mono NF CN" are chain faces arriving with the imported deliveries; the JP faces are fallbacks, loaded on the same page — with one exception noted, not flagged (per-theme record, item 2): "Noto Sans Mono" is named in the mono stack but loaded by no line in this file, the stack falling through to the loaded "Noto Sans JP". Header variables in the same block: `--title: "衆説"` and `--subtitle: "紛 紜 世 間"` (section 5). Assets: the theme's images stay on their original hosts (the author's sandbox, scpsandboxcn.wikidot.com, for the platform logos at candidate L657–667 zone, and the documentation's specimen images) — T1's hotlink ×29, the P5 family, dispositioned class (ii) / KB-58 in register c1.
- **Why:** P7 (the JP faces in load and stack; the chain faces made explicit at the head because the base's delivery form changed). P5's disposition is the register's.
- **Verify:** `grep -n '@import' candidate.txt` for the loads; the :root block is at candidate L605–617.
- **Disposition:** Loads and stacks applied; the images DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** Header strings as variables: the :root block sets `--title: "衆説"` (the platform name, in Japanese glyph form) and `--subtitle: "紛 紜 世 間"` (candidate L615–616) — the KB-57 form, the theme supplying localized defaults for its header variables. The theme's logo block (the platform SVG and the Polished Basalt wordmarks, original L626–640 zone) is carried with its hover-swap intact (candidate L657–667 zone), its images on the sandbox host (section 4). Sidebar: the render row records the candidate page's sidebar not opening; the item is recorded in section 11 with the row's own wording, and no furniture edit in the candidate addresses it (the theme's sidebar behavior rides on its Sigma-9 component chain, the §6 exception family). No `--logo-image` override is set on either side.
- **Why:** P9 (header variables keep their names, their defaults localized) and P8 (sidebar behavior is the base chain's, recorded rather than restructured).
- **Verify:** `grep -n -- '--title:\|--subtitle:' candidate.txt` returns candidate L615–616.
- **Disposition:** Standing; the sidebar item DISPOSITIONED in section 11.

### 6. Text translation

- **What:** The whole documentation is translated in the author's register: the platform introduction and byline (candidate L698 zone), the component credits, the usage documentation with its demos, the specimen articles (including the author's sample news posts with their SCP-CN references converted to labeled CN links), and the tail attribution table. The author's bracketed asides are translated as content (48 `[!-- --]` lines on each side; the head aside is the batch's most visible instance: original L1's "我不是奶龙！！" becomes candidate L1's "私は奶龍じゃない！", the name itself kept in characters). The author's warning comment in the module head is translated with its voice intact (candidate L19–25: "俺がBeta版を出すまで待ってくれ"). In-CSS text beyond that (COMMENT-TEXT, 18 blocks) is the main module's section comments, translated, porter-visible only. Reader-visible CSS strings (CONTENT-STRING, 2 blocks, with GLYPH-FORM): display strings in the module take Japanese forms. R5 glyph-form conversion is stated separately (GLYPH-FORM, 12 blocks across the file): retained strings take Japanese glyph forms where a string survives （众说 → 衆説 in the title variable is the headline instance). Chinese survives in the candidate in the credit block's original-title field (candidate L637), in the kept name 奶龍 in the head aside, and inside specimen text where it is quotation.
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings). R5 is separated per the taxonomy so a reviewer can tell a converted string from a translated one.
- **Verify:** The body sections of diff.md in order; the two `[!--` counts are equal (48) on both sides.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the quotations named.

### 7. Links

- **What:** The documentation's branch references take the labeled CN-link form where no JP counterpart exists (the specimen articles' SCP-CN links, the component pages), and the one LINK-REPOINT block (B298, original L1892–1895 → candidate L1923–1926, in the attribution-table zone) converts a reference to its serving form in the same pattern as the credits list's hoverlinks conversion (section 2). The credit source link (candidate L641) names scp-wiki-cn.wikidot.com, the recorded host, and serves the original. The theme's own platform links inside specimens name the author's sandbox pages and are carried as content.
- **Why:** P11: a prose link takes the JP counterpart where one exists and the serving original where it does not; the dead-reference standard is not engaged by the links that resolve, and the one verified-dead reference in this theme is the section 2 component, which is an include example, not a link.
- **Verify:** `grep -n 'scp-wiki-cn.wikidot.com' candidate.txt` — the source link and the labeled documentation links.
- **Disposition:** Standing.

### 8. Structure

- **What:** The declared deviations are the delivery items of section 3 (the font-load head, the basalt repoint, the frame's addition, the gate's negative-tag drop of section 0) and the furniture swap of section 1. Everything else holds: the module inventory corresponds (main module, hover module), the code block census corresponds (the one plain `[[code]]` block, the comment-area HTML template, original L1644–1687 → candidate L1675–1718, carried in form), and the documentation's demo census corresponds one to one in the same order (the seventeen EXHIBIT-RESTRUCTURE primaries are that zone's repoints and translations, adjudicated in the class summary), so no R3 deletion arises.
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is decided by the census and by naming the deviations, not by the label.
- **Verify:** Compare `grep -n '\[\[module\|\[\[code\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Standing with the deviations declared; no class I item.

### 9. Formatting only

- **What:** No WS-ONLY or re-indentation class fired for this theme (0 blocks of either): the file was edited in place without reformatting, so there is no formatting churn to disclose. The candidate's growth (+34 lines net) is the font-load head, the frame, the credit block, and the :root override block, all content recorded in their sections.
- **Why:** The formatting section states its ground when empty, so a reviewer does not have to infer it from silence.
- **Verify:** classification.json carries no WS-ONLY label for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter annotation exists: at candidate L605, `/* SCP-JP port: JP font fallbacks appended after upstream imports. */`, introducing the main module's :root override block (candidate L606–617, sections 4 and 5). The batch's largest ANNOTATION label count (38 blocks) is adjudicated in the class summary: those blocks are the theme author's own `[!-- --]` asides changing under translation — the original carries the same 48 aside lines — and they are documentation content (section 6), not porter notes. No other porter comment and no `[!-- --]` addition exists.
- **Why:** R2: annotations are part of the port's record, and the distinction between the porter's voice and the author's is exactly what a reviewer of this file needs, because the author's asides are everywhere.
- **Verify:** `grep -n 'SCP-JP port' candidate.txt` returns candidate L605 only; `grep -c '\[!--' original.txt candidate.txt` returns 48 and 48.
- **Disposition:** Standing (part of the candidate as reviewed).

### 11. Dispositions and exceptions

- **What:** Five items, each with its ground. (1) The Sigma-9 delivery four (component:theme, component:acs-animation, component:betterfootnotes, component:hoverlinks): NAMED EXCEPTIONS under campaign AGENTS.md §6, quoted in section 3. (2) The documented companion-component examples (section 2): the comment-area examples have no JP counterpart to repoint to, and the backend component is verified never to have existed on any wiki (sources.tsv, class K5a-ii: NOTFOUND-verified twice plus 404 probes) — an original-side documentation defect, recorded, not repaired by inventing a target. (3) The remaining live code references (P4): the six GitHub Pages Polished-Basalt files and the Font Awesome CDN line, charged by T4 (LOCALIZE-ROWS row 210) and DISPOSITIONED at GOSIGN2-LEDGER §(c3) as delivery class (ii). (4) T1's remaining errors: 29 hotlinks (the section 4 images, class (ii) / KB-58) and 2 pseudo-refs (the draft-host basalt pair, class (iii)), register c1. (5) The render row's items (RENDER-ROWS-2, lane RENDER-S2-F (CN10)): the page's sidebar-not-opening, recorded verbatim (the theme's sidebar rides on its exception-chain components; the row charges it to no one and the ledger determination stands); the candidate-own runtime hosts (cdn.jsdelivr.net, fontsapi.zeoseven.com, sigma9.scpwikicn.com, the scp-wiki-cn and scpsandboxcn chains), recorded verbatim, which are items (1)–(4) seen from the render side; and the sample's render run, which returned no machine verdict (exit 2, no summary) — an inconclusive run, recorded as the row records it. The two per-theme notes are recorded below, not dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries; the §6 exception table), not an omission; an inconclusive check is reported as inconclusive, not as a pass.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED / NAMED EXCEPTION (items 1–5 as stated); the per-theme items noted with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 226): exit 1, 34 errors / 4 warns / 2 infos; 29 hotlink (class (ii)), 3 foreign-include (the section 2 examples, named-exception ground), 2 pseudo-ref (class (iii)); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-F (CN10)): FINDINGS on the page (the section 11(5) items, dispositioned); the sample run inconclusive as recorded; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 210, LOCALIZE-S2-E): FINDINGS / FINDINGS jointly, display-affecting findings 1 (the P4 item), dispositioned at §(c3) with the §6 carve-out. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (diff.md): +522/−488, 1,010 changed lines in 307 change blocks / 44 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:opinions-broadcaster-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 211; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — the frame's code-block address (note)

The candidate's interwiki-style frame (candidate L626–629) names the candidate's own first code block (`local--code/theme%3Aopinions-broadcaster-jp/1`) as its theme address, in the population's standard form. This page's only `[[code]]` block, however, is the comment-area HTML template in the documentation (candidate L1675–1718), not a CSS block: the theme's styling is delivered by its `[[module CSS]]` blocks and their imports, which apply directly. The frame is therefore inert beyond the standard form — its address serves a block of HTML template text where CSS is expected, which a CSS consumer ignores. Recorded so a reviewer does not take the frame's presence as evidence of a code-exhibit delivery this theme does not have; no authority charges it, and the theme's rendering does not depend on it.

### Item 2 — the mono stack's unloaded JP fallback (note)

The :root override block sets `--mono-font: "JetBrains Mono", "Maple Mono NF CN", "Noto Sans Mono", "Noto Sans JP", monospace` (candidate L613). "Noto Sans Mono" is loaded by no line in this file (the added loads at candidate L4–10 are Inter, Sofia Sans, JetBrains Mono, Noto Sans JP, Noto Serif JP, Domine, and Material Symbols Outlined). The face is a mid-stack fallback, not a first face, so the standing flag shape does not arise; if it arrives from nowhere, the stack falls through to "Noto Sans JP", which is loaded. The same shape is noted for theme:normal-jp in this batch, while theme:nameless-jp and theme:obflow-jp do load the face — the population's practice is inconsistent, and a one-line load addition in each naming file would settle it. Recorded for the coordinator's patterns pass; this package does not edit the candidate.


### Post-package repairs (REFRESH3-D)

Recopy was a verified no-op: `candidate.txt` is byte-identical to the current canonical `pages/theme:opinions-broadcaster-jp.txt`. No repair lands after this package's candidate build, so the record below is the slice's sub-shape and remedy, confirmed present in the built bytes.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Aopinions-broadcaster-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L624.
- The frame candidate is a whole introduced include here (the original has no frame and no `theme=`); the (B) remedy dropped its parameter with the include kept.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-opinions-broadcaster-jp.txt` is the decoration sample the render checks ran against (its run is the inconclusive one recorded in section 11(5)). The base theme's candidate, `pages/theme:basalt-jp.txt`, is a separate theme package in this campaign, not part of this change set; this candidate's dependence on it is recorded in section 3. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
