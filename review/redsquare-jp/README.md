# Review package — theme:redsquare-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:redsquare-jp — origin CN, population #220 [GOSIGN2-LEDGER (b) row 220]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 220]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 245; GOSIGN2-LEDGER (b) row 220]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow + candidate-side host lestday-lab.wdfiles.com. [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 219, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 219]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 220]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:redsquare-jp.txt sha256:9ca5669e86631a3e889a5c9be9ab21fc10db1cf0e0342616337f6c38a7f10e5b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 220) |
| Standing items | **DISPOSITIONED** — the theme's three image references on the author's personal-wiki file area stand under the deferred-asset disposition (P5, class (ii) / KB-58, section 4, stated plainly there and in the per-theme record); the T1 pseudo-ref is draft form (class (iii)); the render row's remaining items are the cross-cutting families of section 11. No defect is flagged for this theme |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:redsquare | theme:redsquare-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 4 (first translation; the candidate's credit block records 初訳時参照リビジョン: 4) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-render-s2-f/mirrors/redsquare.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:redsquare-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 505 lines / 10,917 bytes | 515 lines / 12,596 bytes |
| SHA-256 | 538f6facb9b853e51252eb549e9012f9cd2bc5f0f38ff1510f931cdc5b076f9a | 9ca5669e86631a3e889a5c9be9ab21fc10db1cf0e0342616337f6c38a7f10e5b |

Wave history: the candidate was created by the Stage 2 CN12 integration (commit 72e3efa, the RENDER-S2-F wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose redsquare hunk belongs to the credit-field wave. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. Provenance caveat recorded in review/sources.tsv: the original has been superseded upstream since the reference revision, and a follow-up diff artifact (diff-redsquare-from4.txt) sits in the campaign record (the K5a-i treatment); this package documents the port against the frozen revision-4 mirror, the revision the port was made from.

## Summary

红场 (Red Square), a CN theme for the GRU "P" Division, built on the CN BHL derivative 雑踏 (zattou). The port converts the CN branch's own credit module (a non-preview `credit:start` block) plus a bare Rate exhibit into the JP preview credit block, carrying all three of the original's attribution lines inside it — the icon credit, the base-work credit, and the background-image credit — and adding a font-provenance line of its own. The delivery gains the two interwiki frames the original does not have (BHL normalize at priority 1, the theme's own /1 at priority 2), the font load swaps Noto Serif SC for Noto Serif JP with the SC face retained as fallback, the header fallback strings are localized into Japanese (glyph forms converted with them), and the long CN documentation body is translated in full. The theme's three images stay on the author's personal-wiki file area (lestday-lab.wdfiles.com) under the deferred-asset disposition; section 4 names them plainly.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 58 change blocks — 22 specific (37.9%), 35 heuristic (60.3%), 1 residue (1.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 37 |
| TRANSLATION-ANCHORED | 14 |
| CREDIT-PREVIEW | 2 |
| CREDIT-PROSE | 2 |
| DRAFT-HOST | 2 |
| GLYPH-FORM | 2 |
| HEADERVAR | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| JPFONT-STACK | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the two GLYPH-FORM blocks are the header fallback strings of section 5 (simplified-Chinese forms converted as part of their localization, the expected shape for a CN original). The one EXHIBIT-RESTRUCTURE block (B10) is a translated exhibit zone, not a restructuring (the census in section 8). The one residue block (B2) is the inserted BHL frame (appendix; narrated in section 3). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:redsquare-jp; original theme:redsquare on scp-wiki-cn at reference revision 4; candidate `pages/theme:redsquare-jp.txt`. Provenance route: derived from the original at the reference revision by the RENDER-S2-F wave (sources.tsv kind: standard). The upstream page has moved on since (the K5a-i note in the Provenance caveat); the port and this package are anchored to revision 4. The tag gate localizes the CN tag itself (blocks B3, B4: `[[iftags +版式]]` → `[[iftags +テーマ]]`, candidate L15) — the CN branch's theme tag is the word 版式 (format), and its JP counterpart is the population's テーマ tag.
- **Why:** Section 0 declares the provenance route and the frozen baseline; the gate's tag is P2 (iftags tag localization), here including the tag's own vocabulary.
- **Verify:** The sources.tsv row for redsquare-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is P2, applied.

### 1. Credit and attribution

- **What:** The original's credit furniture is the CN branch's own form: a bare Rate exhibit （评分模块：, original L7–10), a second exhibit heading （评分模块与著作信息模块：, L12–14), and a non-preview `[[:scp-wiki-cn:credit:start]]` block (original L15–23) carrying two fields （名称 红场 版式; 作者 [[*user lestday233]]) and two attribution paragraphs: the icon credit (SeymorWu, CC BY-SA 3.0) with the background image's pixabay credit (Juliya8, Pixabay content license), and the base-work credit (the theme is based on sendoh-oroka's 雑踏 theme, CC BY-SA 3.0). The candidate deletes the Rate exhibit (block B3, BARE-RATE-DEL) and converts the CN credit block into the JP preview block (candidate L16–31, block B4): the eight ruling-3 fields （タイトル 赤の広場テーマ版式; 翻訳責任者 AI; 翻訳年 2026; 原題 红场 版式; 著作権者 [[*user lestday233]]; 作成年 2025; 初訳時参照リビジョン 4; the source link, host-verified in section 7), with the original's two attribution paragraphs carried inside the block in translation (blocks B5, B6, candidate L26 and L28) and one porter-added line recording the font provenance (candidate L30: "フォント: Noto Serif JP（Google Fonts, SIL Open Font License）" — accurate against section 4's load). The intro credit sentence (the theme was made by lestday233 at SeymorWu's request for the GRU "P" Division, based on zattou) is carried translated below the block (block B7, candidate L33). So every attribution the original carries survives, and the author field names lestday233 with the user link the original's 作者 field has. T7 credit CSS: no supplement was added; the credit-adjacent rules are inherited on both sides (three matching lines each). The localize row singles this theme's credit handling out as the most honest of its five-theme set, and the bytes bear that out.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form; the CN branch's non-preview credit module does not render on scp-jp, so its content is converted, not duplicated beside the new block (the KB-10 failure shape). Ruling 3 fixes the eight fields; attribution prose rides inside the block where the original's own layout puts it.
- **Verify:** `grep -n 'credit:start\|module Rate' candidate.txt` — only the preview pair remains; read candidate L16–31 against original L15–23.
- **Disposition:** Applied (no ledger P3 item stands for this theme; the FIX-CREDIT-D commit is the population's field wave passing over the file).

### 2. Includes and components

- **What:** Four include events besides the credit pair. The two interwiki frames are added (section 3; the original has none). The usage exhibit (block B9, the COMPONENT-SWAP primary) repoints `@@[[include :scp-wiki-cn:theme:redsquare]]@@` → `@@[[include :scp-jp:theme:redsquare-jp]]@@` (candidate L39): the candidate's real posting name on the right prefix — no self-reference flag for this theme. The style exhibit keeps its unprefixed `[[include component:image-block ...]]` in the multi-line parameter form (candidate L43–47) with the caption and its footnote translated; the component resolves on scp-jp, and the image it displays is section 4's item.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. Ruling 4 is not engaged: the base theme （雑踏） is credited by prose and link (sections 1, 7); its stylesheet is not a component this theme includes — delivery is section 3's frame arrangement.
- **Verify:** `grep -n '\[\[include' candidate.txt` — frames (L5, L10), credit pair (L16, L31), image-block (L43), and the escaped exhibit (L39).
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** The delivery arrangement is rebuilt, by addition. The original has a head module importing its own /1 from the CN wiki's file area (`https://scp-wiki-cn.wdfiles.com/local--code/theme:redsquare/1`, unencoded colon, original L2; the topology pass records `external_own_delivery: true`) and no interwiki frame at all. The candidate repoints the module's import to its own draft-host /1 (candidate L2, block B1) and adds the frame pair the JP environment uses: priority 1 naming the BHL normalize stylesheet from the JP mirror (candidate L5–8, the residue block B2 — an insertion with no original counterpart), and priority 2 naming the candidate's own /1 (candidate L10–13). The CSS itself is the code exhibit on both sides (345 lines each, unchanged in size).
- **Why:** P4/T9 and P6/T3: in the JP environment the theme's live channel is its own local--code delivery framed by interwiki-style, with the base reset framed below it; the CN arrangement (a bare module, no frames) is the branch-local form it replaces. The draft host is KB-41, class (iii).
- **Verify:** `sed -n '1,13p' candidate.txt` against original L1–6 — one import, two frames, then the gate.
- **Disposition:** DISPOSITIONED (draft-host form, class (iii)); the frame arrangement is applied.

### 4. Fonts and assets

- **What:** Fonts (P7): the load swaps the branch face for the JP face (block B54: original L174 → candidate L184): `Noto Serif SC` (weights 200–900) becomes `Noto Serif JP` (weights 200–900), same Google Fonts css2 grammar. The two stack blocks (B55, B58) read `'Noto Serif JP', 'Noto Serif SC', serif` (candidate L258, L327) — the JP face first, the original's SC face retained as the fallback for any glyph the JP face lacks, which for a CN theme carrying simplified-Chinese proper nouns is the correct order, and every named face is loaded or is the platform serif. Assets: three references stay on the author's personal-wiki file area, lestday-lab.wdfiles.com: the exhibit logo (candidate L44, `local--files/theme%3Aredsquare/logo.png`), the page background (candidate L218, `body_bg.jpg`), and the header logo in the CSS (candidate L230, `logo.png` again). These are the localize check's pattern-5 charges (its named items are the background and the logo, display-affecting: header background, logo, and the sample's image-block), and the ledger's answer is a disposition, not a re-host: P5 DISPOSITIONED, class (ii) / KB-58.
- **Why:** P7 (KB-16): the branch's serif is replaced by its JP sibling rather than supplemented, because the theme's identity is a serif display face and Noto Serif JP is that face's Japanese form. P5's re-hosting rule is the default; KB-58 records the deferred class, and the author's own file area is the recorded host for this theme's art — stated plainly here rather than absorbed into the disposition.
- **Verify:** `grep -n 'lestday-lab' candidate.txt` — exactly the three loci named above; `grep -n '@import' candidate.txt` — the delivery import (L2) and the Noto Serif JP load (L184).
- **Disposition:** DISPOSITIONED (assets, P5 class (ii) / KB-58; GOSIGN2-LEDGER §(c3)); the font arrangement is applied.

### 5. Header, sidebar, and site furniture

- **What:** The header furniture is two CSS content strings that read their text from the header variables with Chinese fallbacks (blocks B56, B57): `content: var(--header-title, "军事情报总局")` → `var(--header-title, "参謀本部情報総局")` (candidate L265) and `content: var(--header-subtitle, "\"超心理学\" 部门")` → `var(--header-subtitle, "\"超心理学\"部局")` (candidate L271). The GLYPH-FORM label on both blocks is the simplified-Chinese glyph conversion inside the localization （军事情报总局 → 参謀本部情報総局 is both a translation of the GRU's name and a glyph-form conversion; 部门 → 部局 likewise). No header variables are set by the theme itself on either side; these fallbacks are what renders when a page does not set them.
- **Why:** P8 (KB-19): rendered strings are reader-visible furniture; for a CN original the localization of a Chinese string into Japanese necessarily converts its glyph forms, which is the conversion the classifier names — expected mass for this branch, adjudicated here rather than flagged.
- **Verify:** `grep -n 'header-title\|header-subtitle' candidate.txt` — the two fallback strings at L265 and L271.
- **Disposition:** Applied.

### 6. Text translation

- **What:** The CN documentation body is translated in full: the usage and style sections, the component exhibits' explanatory prose, the image caption with its footnote (a 1950s Beijing People's Art Theatre play is the caption quote's source, carried in the footnote), and the headings. The counted groups are 37 TRANS-UNANCHORED blocks and 14 TRANSLATION-ANCHORED blocks; the anchored blocks were verified line by line, and the unanchored mass is single-line prose translation of the same shapes, with no content class dropped (the census in section 8). Simplified-Chinese text survives in the candidate only in the credit block's 原題 field (the original title, as ruling 3 records it) and in proper nouns inside the stacks' fallback name (Noto Serif SC, section 4).
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings).
- **Verify:** The pairs are diff.md's body sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit block's source link (candidate L24) names `https://scp-wiki-cn.wikidot.com/theme:redsquare` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered; its label is the theme's Chinese title （红场 版式）, a T5 joint-note shape, not a defect. The base-work links `[[[theme:zattou|雑踏テーマ]]]` (candidate L28, inside the credit block, and L33, in the intro) keep the unprefixed same-site form the original uses (`[[[theme:zattou|熙攘版式]]]`, original L21, L24), with the label localized to the base theme's Japanese name; no charge stands against them. The pixabay credit links inside the attribution prose are carried with their targets unchanged (candidate L25).
- **Why:** P11: prose links take the JP counterpart where one exists; a credit reference to the base work in the form the original carries it is a provenance statement, and the population's zattou reference is the same-site name.
- **Verify:** `grep -n 'zattou' candidate.txt` — the two loci named above.
- **Disposition:** Applied.

### 8. Structure

- **What:** The exhibit census corresponds: usage exhibit, style exhibits (image-block, headings, text-formatting examples), and the code exhibit are present on both sides in the same order. The named conversions are the credit form's replacement (section 1) and the delivery frames' addition (section 3). The one EXHIBIT-RESTRUCTURE block (B10) is a translated exhibit zone whose include and text both carry over. Selector and variable names inside the CSS are preserved.
- **Why:** R3: the census is what separates a conversion (this theme) from a silent restructure or drop (the failure class I charges); here every original region has a named candidate counterpart.
- **Verify:** Compare the heading and include sequences of the two files — they correspond at the loci named in sections 1–3.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0) in this pair.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier summary in classification.json (no WS-ONLY label).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter-added line, recorded here: the font-provenance line inside the credit block (candidate L30, section 1). It has no original counterpart; its content is verified accurate against section 4's load. No `[!-- ... --]` comment exists in the candidate.
- **Why:** R2: porter-added text is part of the change record, in whatever form it takes.
- **Verify:** `sed -n '30p' candidate.txt` — the フォント line between the base-work credit and `credit:end-preview`.
- **Disposition:** Standing (recorded; the note's content is verified accurate).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three hotlink errors: class (ii) — the section 4 images on the author's file area, standing under the KB-58 deferred-asset disposition; the render row names the same host on its candidate side. (2) T1's one pseudo-ref error: class (iii), the draft-host delivery of section 3. (3) The render row's remaining items, all cross-cutting: the sample's credit-modal errors (KB-32, ruling 5) and the 884px@768 overflow (KB-33/KB-34 families), over the environment hotlink chain (KB-40). T4's single charge family closes as pattern 5 DISPOSITIONED (section 4).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 245): exit 1, 4 errors / 2 warns / 1 info; the errors are hotlink ×3 and pseudo-ref ×1, all in the dispositioned classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-F (CN12)): FINDINGS, the items of section 11(1)/(3), all dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 219): FINDINGS jointly, display-affecting findings 1 (the pattern-5 family); the ledger §(c3) line records the theme's T4 outcome as P5 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +116/−111 in 58 classifier change blocks / 4 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:redsquare-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 220; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The author's-host images stand by disposition, stated plainly

Section 4 records the three URLs; this note exists so the disposition is not misread as a repair, and it also reconciles a wording tension in the records. The localize row says the two named images "must be dealt with before posting"; the ledger dispositions the family as class (ii). In the AGENTS.md §3 taxonomy those are the same instruction read at two altitudes: class (ii) is precisely the class whose handling happens at posting time, by the posting procedure, rather than in the candidate file. The candidate therefore depends on lestday-lab.wdfiles.com at render time until posting, by recorded decision. If that decision is ever revisited, the three loci are candidate L44, L218, and L230.

## Appendix — residue blocks

| Block | Span | Resolution |
|---|---|---|
| B2 | inserted at orig 5 → cand 5-8 | The added priority-1 interwiki frame (the BHL normalize target, candidate L5–8). An insertion the aligner left unlabeled; narrated in section 3. |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-redsquare-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
