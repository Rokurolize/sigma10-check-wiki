# Review package — theme:lead-by-example-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:lead-by-example-jp — origin CN, population #201 [GOSIGN2-LEDGER (b) row 201]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 201]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 16 errors / 0 warns / 2 infos (hotlink×16); standing classes dispositioned in register c1 [T1-ROWS row 231; GOSIGN2-LEDGER (b) row 201]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-F (CN8))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN8))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 200, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 200]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 201]
- Computed against: canonical commit a497307c6e7eedc2580739ba55d2c3212d9cacd2; candidate file pages/theme:lead-by-example-jp.txt sha256:0e7155e693b3ff955b713cb152bd447b9f7c57daa4617fc55bacb286f816a381; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 201) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×16 (section 4); the render row's chain item (section 11); T4's three findings (P5, P7, P11) each dispositioned on its named ground (section 11). The localize row calls this the best port of its batch, and the bytes bear that out; the dispositions are recorded, not hidden |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:lead-by-example | theme:lead-by-example-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 146 (first translation; the candidate's credit block records 初訳時参照リビジョン: 146) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-lead-by-example.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:lead-by-example-jp.txt`, byte-identical at canonical HEAD c635d01 (this file was not touched by the post-snapshot usage sweep; its examples already used the correct form, section 7) |
| Lines / bytes | 2,695 lines / 72,104 bytes | 2,960 lines / 83,732 bytes |
| SHA-256 | 452b7efb063164901044fe116275d40668d8f004b755e8542f3d3d4d09fd585d | 0e7155e693b3ff955b713cb152bd447b9f7c57daa4617fc55bacb286f816a381 |

Upstream note (sources.tsv, kind standard, K5a-i): the original has been superseded upstream since the reference revision; the follow-up diff artifact `diff-lead-by-example-from146.txt` sits in the campaign record. This package's diff is against revision 146, the revision the port was made from, as recorded. Wave history: the candidate was created by the Stage 2 CN8 integration (commit e469417), then touched by 1869877 (FIX-CREDIT-D, translator-attribution normalization) and a497307 (FIX4-MECH, duplicate @import removal, KB-65). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The largest and, by its localize row's own judgment, the best port in this batch （本バッチ最良の移植 — "the best port of this batch"). The original is a CN Black Highlighter-based theme with a variant architecture: a base delivery plus three conditional variant deliveries (army, navy, alert) gated on page variables, all of it mirrored in a code exhibit, with the base theme imported from the CN BHL host inside the tag gate. The candidate repoints the base delivery to the JP mirror host and moves it outside the gate with the population's interwiki frame added, re-gates every `:root:lang(cn)` block to `:root:lang(ja)` with its strings translated, replaces the CN font loads with their JP counterparts (deleting one font's load under a documented partial disposition), swaps the CN credit module for an expanded JP preview block, keeps the theme's labeled Rate exhibit as an exhibit under the pattern-3 exception, and — the quiet centerpiece — restores the code exhibit to agreement with the live delivery, repairing drift the original's exhibit had accumulated against its own modules. Its three T4 findings are all dispositioned with named grounds (served-source assets, the partially handled font, a sibling-branch absolute link), and its sixteen T1 hotlinks are the same served-source asset set. Measured churn (diff.md, the generator's count: +583/−318, 901 changed lines in 189 change blocks; a GNU-diff count of the same pair gives 903 changed lines — the counts agree to alignment noise). The diff is Tier 2 format, and this README is the adjudicated explanation the Tier 2 header points to.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 189 change blocks — 109 specific (57.7%), 66 heuristic (34.9%), 14 residue (7.4%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 68 |
| DELIVERY-MOVE | 66 |
| TRANSLATION-ANCHORED | 43 |
| JPFONT-STACK | 14 |
| HEADERVAR | 10 |
| RESTORATION | 8 |
| GLYPH-FORM | 6 |
| INCLUDE-REPOINT | 5 |
| COMPONENT-SWAP | 3 |
| EXHIBIT-RESTRUCTURE | 3 |
| FONTLOAD-CJK-STACK | 2 |
| IFTAGS | 2 |
| ASSET-REHOST | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DUPIMPORT-DEL | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (the blocks were read against the bytes, in groups where the class treatment applies): DELIVERY-MOVE (66) is the classifier's name for the mass of CSS lines whose pairing crosses between the live modules and the mirrored exhibit — the topology record shows the cross-matching explicitly (similarities 0.72–0.99). It does not mean the structure inverted: both files carry the same architecture (live modules first, mirrored exhibit after), and section 3 adjudicates the mass as container-consistent churn plus the lang re-gating and stack changes that ride in it. RESTORATION (8) is real and is section 8's subject. The 3 EXHIBIT-RESTRUCTURE blocks are component-exhibit zones whose change is include repoints (section 2), not restructuring; the exhibit census is complete. The 14 residue blocks are alignment artifacts inside the moved CSS mass and single exhibit lines, resolved by shape. GLYPH-FORM (6) rides on the header/lang blocks: rendered strings whose characters take JP glyph forms in translation (section 5). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:lead-by-example-jp; original theme:lead-by-example on scp-wiki-cn at reference revision 146; candidate `pages/theme:lead-by-example-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN8 wave (sources.tsv kind: standard; the upstream-superseded note and its follow-up artifact are recorded in the Provenance table). The original opens with its tag gate (`[[iftags +版式]]`) wrapped around its base-theme delivery module (original L1–6); the candidate opens with the delivery module ungated and the body gate (`+テーマ`) deferred to the body (candidate L1255) — delivery outside the gate is one of the points the localize row praises, and section 3 treats it.
- **Why:** Section 0 declares the provenance route and the revision baseline so every later count is read against the right baseline — for this theme, against revision 146 specifically, since the upstream page has moved since.
- **Verify:** The sources.tsv row for lead-by-example-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route and baseline themselves).

### 1. Credit and attribution

- **What:** The original's credit furniture is the CN credit module: a `:scp-wiki-cn:credit:start`/`more`/`end` triple with the labels 页面信息 and 更多页面信息 (original L1265–1269's zone). The candidate swaps it for the JP preview block (candidate L1267–1278, block B27), whose field set is wider than the standard eight: alongside タイトル （率先垂範テーマ), 原題 （身先士卒 主題版式）, 作成年 (2025), 翻訳責任者 (AI), 翻訳年 (2026), 初訳時参照リビジョン (146), and the source link (section 7), it carries both a 著者 field and a 著作権者 field — both naming Agt Darkwall, so the author is recorded under both of the block's author slots and no reading of the field drops him — and a 使用フォント field documenting the fonts the theme uses, including the VonwaonBitmap entry that carries section 4's font disposition in the file itself ("VonwaonBitmap 12px（鳳凰点阵体、CC0 1.0、ローカル環境のみ）" — local environment only). The original's prose attribution agrees with the fields: the intro names Agt Darkwall as the maker (candidate L1282 mirrors it), and the font-documentation prose keeps the original's acknowledgment that ChatGPT provided partial code support (candidate L1709–1714, block B130) — an authorship-relevant disclosure the port retains rather than tidies away. The labeled Rate exhibit is a separate matter: the body exhibits the rate module live under its label 評価モジュール： (candidate L1258–1261), followed by the credit block under its own label — the labeled paired-exhibit form, which the ledger's pattern-3 exception list names this theme for (GOSIGN2-LEDGER line 1711). It is documentation the theme itself performs, not the page's credit furniture, and it is kept as the original kept it.
- **Why:** P3/T1 with the pattern-3 exception: the preview credit module replaces the CN credit module as the page's credit record, while a labeled, paired Rate exhibit is the theme's own documentation and is not the duplicate-Rate failure (KB-09) — the distinction is the pairing and the label, both present. Ruling 3 fixes the standard fields; the extra fields are this theme's own record-keeping (the font field does disposition work, section 4).
- **Verify:** Read candidate L1255–1282 against original L1253–1295; `grep -n 'credit:start' candidate.txt` — the JP preview form only.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the Rate exhibit stands under the pattern-3 exception as recorded.

### 2. Includes and components

- **What:** The include acts: the two interwiki-style includes added at the head (candidate L6–13, block B3's zone) are delivery lines, treated in section 3. The credit includes are section 1. The exhibit component repoints (INCLUDE-REPOINT 5, COMPONENT-SWAP 3): the usage examples' escaped includes (blocks B31, B39, B41 — their name forms are section 7) and the component exhibits in the body documentation (blocks B38, B40, B43's zones), whose `:scp-wiki-cn:` targets become `:scp-jp:` targets. No live include in the candidate names a CN or EN component.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; the repointed components have verified JP counterparts, so all are repointed and none is kept as an exception. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the interwiki pair, the credit pair, and exhibit text; no `:scp-wiki-cn:` include remains.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery architecture, which the classifier's DELIVERY-MOVE mass (66 blocks) and the topology record describe from the side. The original delivers in five live modules: a base-theme module inside the tag gate importing Black Highlighter's two stylesheets from the CN BHL host bhl.scpwikicn.com (original L1–5); a base module (original L8–764); and three variant modules gated on page variables by ifexpr — army (original L768–855), navy (L858–954), alert (L958–1249) — the variants restyle the theme for the author's military sub-presets. The whole delivery is then mirrored as a code exhibit later in the page (original L1725 onward), module for module, gates included. The candidate keeps the architecture and changes its coordinates: the base-theme module leaves the gate and imports from the JP mirror host scp-jp.github.io (candidate L1–4), with the population's interwiki-style frame added at priorities 1 and 2 naming the same files (candidate L6–13); the base and variant modules follow in the same order with the same ifexpr gates (candidate L15–770, 772–859, 861–957, 960–1251); and the exhibit mirror follows as before (candidate L1721 onward). Inside the modules, two systematic changes ride: every `:root:lang(cn)` block is re-gated to `:root:lang(ja)` (the localize row's 全再ゲート — the lang-gated variable sets are where the theme keeps its per-language strings, so the re-gate is what makes the JP page use them), and the font loads and stacks change as section 4 records. The CN BHL host disappears completely (the row's bhl.scpwikicn 完全置換）: no line in the candidate names it. The topology record's cross-matches (the original's live modules matching the candidate's exhibit at 0.95–0.99 and vice versa) are the expected artifact of mirroring: the CSS text exists twice in each file, so the aligner pairs copies across containers; the adjudicated reading is the container census above, which is identical in both files.
- **Why:** Ruling 1's delivery principle in its BHL form: the base is imported from the JP side's delivery of it (here the JP mirror host, the population's form for BHL-based themes), not from the source branch's CDN host. P4/T9 (delivery served from JP hosts) and P6/T3 (the interwiki frame). The ungated placement matters mechanically: inside the tag gate, the base import would only fire for pages already tagged as themes, which is the original's CN arrangement; the JP population delivers outside the gate, and the localize row counts the move as part of why this port is its batch's best.
- **Verify:** The container census: `grep -n '\[\[module\|\[\[code\|iftags' candidate.txt` against the same grep on original.txt — same architecture, JP coordinates; `grep -n 'bhl.scpwikicn' candidate.txt` returns nothing; `grep -c 'lang(ja)' candidate.txt` against `grep -c 'lang(cn)' original.txt` for the re-gating mass.
- **Disposition:** Applied (the delivery itself carries no disposition; the dispositions are its assets and fonts, sections 4 and 11).

### 4. Fonts and assets

- **What:** Fonts. Loads: the original's live module loads three fonts — VonwaonBitmap 12px from fastly.jsdelivr.net (a GitHub-hosted CN bitmap font), Ma Shan Zheng from Google Fonts, and Noto Sans SC from Google Fonts (original L9–11) — and its exhibit head duplicates the trio (the original's Ma Shan Zheng import appears three times across the file). The candidate's live module loads two: Ma Shan Zheng (kept — it is a calligraphic face whose glyphs cover the JP use) and Noto Sans JP in place of Noto Sans SC (candidate L16–17, block B5); the exhibit mirror's loads match, with the duplicate import at the original exhibit's head deleted (block B132, DUPIMPORT-DEL — the a497307 KB-65 pass). The VonwaonBitmap load is deleted in both places, while its name stays first in the monospace stacks, now with a JP fallback appended: `'VonwaonBitmap 12px', 'Noto Sans JP', monospace` (14 stack lines across live and exhibit, JPFONT-STACK 14; the FONTLOAD-CJK-STACK pair, blocks B16 and B158, is the same change at the load-adjacent stack sites). That is T4's pattern-7 partial, and it is documented in the file: the credit block's font field records VonwaonBitmap as ローカル環境のみ (local environment only) — the stacks resolve to it where a reader's machine has the font installed, and to Noto Sans JP everywhere else. Assets: the variant backgrounds stay at their served addresses byte-identically — the tropmulti.png texture on the CN sandbox host (scpsandboxcn.wdfiles.com, theme:eatshit folder) and the NFP-navy.jpg photograph on upload.wikimedia.org, across the live modules and their exhibit mirrors, plus the army2.png image-block exhibit on the same sandbox host (candidate L1319's zone) — T4's pattern-5 set (14 URLs, with the navy2/army2 exhibits making T1's hotlink count 16). One asset is re-hosted: the base theme's logo image in the body moves from EN storage to JP storage at the same path (scp-wiki.wdfiles.com → scp-jp.wdfiles.com, block B24, ASSET-REHOST).
- **Why:** P7/T5 for the fonts: the SC→JP load swap is the standard CJK counterpart replacement; the Vonwaon partial is the judgment call — a CC0 bitmap font with no JP-hosted load, kept as a name for local environments and disclosed as such in the credit block, rather than loaded from a third-party CDN the campaign does not control. T4 dispositioned P7 without a display-affecting mark (section 11), which is the ledger accepting exactly that reasoning; the section records it so the named-but-unloaded shape here is not mistaken for the undocumented defects flagged in this batch's laruetheme and laughter-and-knives packages. P5 with KB-58 for the assets: served-source lines naming the author's chosen hosts are class (ii); the logo's re-host is P5's ordinary form (the base's asset, moved to the JP side's storage at the production host).
- **Verify:** `grep -n '@import' candidate.txt` — the BHL pair, the interwiki frame's targets aside, Ma Shan Zheng and Noto Sans JP only; `grep -n 'VonwaonBitmap' candidate.txt` — stack lines and the credit field, no load; `grep -n 'scpsandboxcn\|wikimedia' candidate.txt` — the kept served-source addresses.
- **Disposition:** Loads applied; P7 DISPOSITIONED (T4 bar, section 11); assets DISPOSITIONED (class (ii) / KB-58); the logo re-host applied.

### 5. Header and sidebar furniture

- **What:** The header strings translate inside every lang-gated variable set (HEADERVAR 10 blocks): the base set's `--header-title: "基金会武装部队"` → `"財団武装部隊"` and `--header-subtitle: "搜索，作战，守护"` → `"捜索、交戦、防護"` (original L24–25 → candidate L30–31, block B7), with the variant modules' sets following the same treatment (blocks B18, B20, B23 and their exhibit mirrors B135, B173, B178). The GLYPH-FORM signature (6 blocks) rides on these: the translated strings take JP glyph forms where the CN and JP standards write the same word with different characters （部队 → 部隊， 守护 → 防護's 防， and their kin). The documentation's escaped sample of the header variables is re-gated and translated too (`@@:root:lang(cn) {@@` with `--header-title: "标题"` → `@@:root:lang(ja) {@@` with `"タイトル"`, block B35), so the page's own instructions show the JP form a user should copy. No sidebar-specific variable change fires beyond the restorations of section 8.
- **Why:** The lang-gated sets are this theme's localization mechanism: the strings exist per-language by design, so translating them and re-gating the sets to lang(ja) is the port's core act, not a ruling-2 taste case — the theme was built to carry its header text in the page language's set. (Ruling 2's taste space concerns themes whose headers are single fixed strings; this theme's are language-keyed variables.)
- **Verify:** `grep -n 'header-title' candidate.txt` — every set in JP form under lang(ja); `grep -n 'lang(cn)' candidate.txt` returns nothing.
- **Disposition:** Applied (part of the port's core; nothing charged on the point).

### 6. Text translation

- **What:** The body and documentation translate throughout (111 translation-labeled blocks): the intro and usage prose, the variant documentation (the navy and army preset sections, with their include examples in section 7), the component exhibits, and the font-documentation prose (block B130, candidate L1709–1714) — which translates the original's font credits, repoints its Black Highlighter link to the JP production page (section 7), adjusts its Noto reference from Noto Sans SC to Noto Sans JP to match the loads, adds the CC0 clarification to the license line （フォントはすべて SIL Open Font License Ver. 1.1 のもとにあります（鳳凰点阵体は CC0 1.0)) where the original had folded the bitmap font into the OFL sentence, and keeps the ChatGPT assistance acknowledgment (section 1). The theme's proper names keep their forms: the font's own name 鳳凰点阵体 is printed with its first character in the traditional form and the rest as the font names itself — a proper-name rendering, not a glyph error. The CSS comments translate as a class with the code.
- **Why:** P9/P10 (prose, documentation, and comments into Japanese). The license-line clarification is the porter correcting the record where the original's sentence was imprecise about its own fonts — a documentation repair of the same family as section 8's restorations, and it agrees with the credit block's font field (section 1).
- **Verify:** Read candidate L1709–1714 against original L1713–1718 for the font prose; `grep -n 'ChatGPT' candidate.txt` — the acknowledgment stands.
- **Disposition:** Applied (the theme's T4 record shows no translation finding; its three findings are sections 4 and 7).

### 7. Links and references

- **What:** Four link acts. (1) The credit block's source link names the original at its recorded host (scp-wiki-cn.wikidot.com, section 1) — host check clean. (2) The font prose's Black Highlighter link: the original's relative `[[[theme:black-highlighter-theme|黑色标记笔主题]]]` becomes an absolute link to the JP production page, `https://scp-jp.wikidot.com/theme:black-highlighter-theme` (block B130) — the base the candidate actually imports. (3) The usage examples (blocks B31, B39, B41): the original's escaped examples name `:scp-wiki-cn:theme:lead-by-example`, with variant parameters on two of them (`|navy=true`, `|army=true`); the candidate's examples drop the wiki prefix and name the posting page directly — `@@[[include theme:lead-by-example-jp]]@@`, `@@[[include theme:lead-by-example-jp |navy=true]]@@`, `@@[[include theme:lead-by-example-jp |army=true]]@@` (candidate L1287, L1316, L1322) — the bare form, which resolves on the hosting wiki to the candidate's own posting name. This is the correct self-reference form, which is why the post-verdict usage sweep did not touch this file. (4) The intro's sibling-branch link (candidate L1282): the author's related setting page is linked absolutely to the CN wiki, `https://scp-wiki-cn.wikidot.com/slipping-desolation` — kept absolute because its target is a CN-branch page with no JP counterpart; that is T4's pattern-11 item, dispositioned in section 11. The same sentence's base link is repointed to the JP production BHL page, so the sentence shows both treatments side by side: JP counterpart where one exists, serving original where none does.
- **Why:** P1/P9 link hygiene under the dead-reference standard: name the JP counterpart when there is one, the serving original when there is not, and the theme's own posting name in its examples. Item (4)'s ground is the sibling class: a link into another branch's content, whose correct target is that branch's page.
- **Verify:** `grep -n 'scp-wiki-cn' candidate.txt` — the source link and the sibling link only; `grep -n 'theme:lead-by-example' candidate.txt` — the three examples, all in -jp bare form.
- **Disposition:** (1)–(3) applied; (4) DISPOSITIONED (sibling / batch-posting class, section 11).

### 8. Structure and exhibits

- **What:** The exhibit census is complete against the original (usage and variant documentation, component exhibits, image exhibits, the full mirrored code exhibit, the font documentation), and the classifier's 3 EXHIBIT-RESTRUCTURE blocks are the component-exhibit repoint zones of section 2. The structural story is the RESTORATION mass (8 blocks, all inside the exhibit mirror): the original's code exhibit had drifted from its own live delivery — variable values that differ from the live modules' and whole variable lines the live modules carry and the exhibit lacks. The candidate's exhibit agrees with the live delivery: block B138 is the type case, where the exhibit's `--swatch-topmenu-border-color` takes the live value (var(--dark-accent), not the exhibit's stale var(--bright-accent)), its background becomes transparent, and the sidebar variable lines the live module defines (`--sidebar-bg-color`, the sideblock-menu set, and their kin) stand in the exhibit where the original's exhibit had none. Blocks B141, B142, B144, B169, B176, B180, and B182 are the same act at other sites, B180 the largest (a ~190-line stretch of the exhibit brought back into agreement, HEADERVAR riding in it). The restorations change no live rule: the live modules are the comparison baseline, and the exhibit is what was repaired.
- **Why:** An exhibit that disagrees with the delivery it documents is a defect of the documentation — a user copying the exhibit gets a different theme than the page delivers. The port's treatment (regenerate the exhibit from the live text) is the honest repair, and the classifier's RESTORATION label exists for exactly this shape: content present in the candidate because the original's own primary text has it, restored to the place the original's secondary text had lost it.
- **Verify:** Compare any restored site across the three texts (for example candidate L1747–1758 against original L1756–1757 for the exhibit and the live module's matching lines earlier in each file); the topology record's similarities quantify the agreement.
- **Disposition:** Applied (the restorations are part of the port as delivered; no ledger item charges the exhibit's drift, because the drift was the original's).

### 9. Formatting only

- **What:** No whitespace-only or reindent blocks fire (WS-ONLY and REINDENT both absent from the label counts), despite the file's size: the churn is content churn — re-gating, translation, stacks, and restorations — plus the alignment noise the residue count (14 blocks) absorbs inside the moved CSS mass. Those residue blocks are single lines and small runs the aligner could not pair inside near-identical CSS; read against the bytes they are unchanged or translation-carrying lines, resolved here by shape as the class treatment prescribes.
- **Why:** Stated so the formatting account is a checked fact: in a 901-changed-line diff, the absence of a formatting class is itself information about how the port was made (line-targeted edits, not reflows).
- **Verify:** The label counts in the class summary; the residue list in classification.json.
- **Disposition:** Standing (nothing to disposition).

### 10. Porter annotations

- **What:** None in the file. Checked explicitly: the candidate carries no porter comment and no translator's note (a grep for the annotation forms the population uses returns only the credit block's own fields and the theme's documentation). This port's judgment calls — the Vonwaon partial, the exhibit restorations — are documented in the credit block's font field and in the ledger records rather than in comments.
- **Why:** T11 asks that judgment calls stay auditable; here the audit trail is the credit block's font field (section 4, which is itself an in-file record at the place a user looks) plus the T4 row and its dispositions. The section states the absence of comment-form annotations as a checked fact.
- **Verify:** `grep -n 'SCP-JP port\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing (absence recorded).

### 11. Dispositions and exceptions

- **What:** Four standing items, all closed, plus the render readings. (1) T1's hotlink ×16 and T4's pattern-5 finding (section 4): the variant backgrounds and image exhibits on the CN sandbox host and Wikimedia, DISPOSITIONED class (ii) / KB-58 (GOSIGN2-LEDGER line 1586). (2) T4's pattern-7 partial (section 4): the VonwaonBitmap load's deletion with its name kept in the stacks, DISPOSITIONED as recorded without a display-affecting mark, at the T4 bar — the ledger's phrasing, reflecting that the credit block discloses the font as local-only and the stacks fall back to Noto Sans JP. (3) T4's pattern-11 item (section 7): the CN absolute link to the author's sibling-branch setting page, DISPOSITIONED (sibling / batch-posting class). (4) The render row's items: a runtime-hotlink in the site-theme chain on the theme page, and on the sample the credit-modal reading (dispositioned preview-form, the standing GOSIGN-TESTS T2 amendment) plus the same chain hotlink — the KB-40 shape, a hotlink in what the page loads rather than in this file's text, recorded as the row records it. The localize row's overall judgment is also part of the record: it names this the best port of its batch, citing the ungated delivery, the complete bhl.scpwikicn replacement, and the full lang(ja) re-gating with JP wording.
- **Why:** A disposition names its ground: class (ii) / KB-58 for served-source assets, the T4 bar for the disclosed font partial, the sibling class for the cross-branch link, and the preview-form amendment for the modal reading. Nothing in this theme rests on an unnamed exception.
- **Verify:** The theme's rows in T1-ROWS, LOCALIZE-ROWS, and RENDER-ROWS-2; the disposition line in GOSIGN2-LEDGER (line 1586).
- **Disposition:** DISPOSITIONED (all four, on the grounds named).

### 12. Verification record

- **What:** T1 (source check, T1-ROWS row 231): hotlink ×16 (exit 1, 16 errors / 0 warns / 2 infos) — every error is one of the served-source asset lines dispositioned above; notably, no pseudo-ref errors: this candidate's delivery names no draft host (its frame is the production JP mirror host). T4 (localize check, LOCALIZE-ROWS row 200, wave LOCALIZE-S2-D): FINDINGS, 3 findings — pattern 5 (the army/navy/alert backgrounds, 14 URLs plus navy2/army2), pattern 11 (the L1282 CN absolute link — the candidate's line number matches the finding's), and pattern 7 partial (VonwaonBitmap) — with the row's praise and the note of no unincorporated upstream updates at check time (the upstream supersession recorded in sources.tsv is the K5a-i follow-up's subject, not a T4 item). T2/T3 (render check, RENDER-ROWS-2, wave RENDER-S2-F (CN8)): the readings of section 11. The go-sign ledger row (§(b) row 201) aggregates T1 FINDINGS (classified), T2 FINDINGS, T3 FINDINGS, T4 FINDINGS, T5 PASS — every finding classified, none OPEN.
- **Why:** The counts are the acceptance evidence for the sections above: each checker's scope is stated so a clean result is not read past what the checker can see (T1 reads this file, and its 16 errors are the asset set; the render check is what saw the loaded chain).
- **Verify:** The three ledger-part files named above, rows 231 and 200 and the theme's render row; GOSIGN2-LEDGER §(b) row 201 for the aggregate.
- **Disposition:** PASS at the ledger determination, with the items of section 11 dispositioned as recorded.

## Per-theme record

Two items belong to this theme alone.

**The localize row's "best port of the batch" judgment, and what it rests on.** LOCALIZE-ROWS row 200 calls this 本バッチ最良の移植 (the best port of its batch) and names its grounds: delivery outside the iftags gate, the complete replacement of the CN BHL host, and the full re-gating of the `:root:lang()` sets to lang(ja) with JP wording. This package's reading adds the fourth ground the row does not name: the exhibit restorations of section 8, which repaired the original's own documentation drift. The judgment is recorded here because it is part of the theme's verification history — and because it makes the theme the batch's reference case for how the dispositioned items (sections 4 and 7) look when they are handled with disclosure: the same shapes that are defects elsewhere in this batch (a font named without a load, foreign-host assets) are here either repaired or documented in the file and dispositioned on stated grounds.

**The upstream page has moved since the reference revision.** Sources.tsv records that the original was superseded upstream after revision 146, with the follow-up diff kept as the campaign artifact `diff-lead-by-example-from146.txt` (kind K5a-i). The port, this package, and the verdict all stand against revision 146; a future refresh against the newer upstream text is a separate act, and nothing in this package should be read as covering it.

## Change set outside the two diffed files

| File | Change |
|---|---|
| `pages/theme-decoration-sample-lead-by-example-jp.txt` | The theme's decoration sample: a JP page applying the candidate, the surface the T2/T3 render checks measured (section 11's sample readings) |

## License and attribution

- **Title:** 身先士卒 主題版式
- **Author:** Agt Darkwall
- **Source:** https://scp-wiki-cn.wikidot.com/theme:lead-by-example — revision 146
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
