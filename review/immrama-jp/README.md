# Review package — theme:immrama-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:immrama-jp — origin EN, population #101 [GOSIGN2-LEDGER (b) row 101]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2de829abaf45adab8882c18c71d4e1ac3a0f48af575f162d1cdeeea88b5e527a); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 0 infos (hotlink×7, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 91; GOSIGN2-LEDGER (b) row 101]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — notice clip ≤375 + 768px sidebar×notice + WebKit CC "S" (all cross-cutting); sample h1 clipped at 320, 評価 label crush (6 shots), `.open-menu` overprint; page-overflow 367–552px. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 101, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 101]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 101]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:immrama-jp.txt sha256:2de829abaf45adab8882c18c71d4e1ac3a0f48af575f162d1cdeeea88b5e527a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 101) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×7 (the EN-storage assets, class (ii) / KB-58, section 4); T4's P5 assets and P9 subtitle (section 11); the render row's cross-cutting items (KB-32/33/34/36, section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:immrama | theme:immrama-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 17 (first translation; the candidate's credit block records 初訳時参照リビジョン: 17) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-immrama.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:immrama-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 503 lines / 11,626 bytes | 450 lines / 11,286 bytes |
| SHA-256 | 7a20c86c0e5f731e744139232d73f9182fa92302a1aff3d3d5ce7c0fbb0803af | 3d92a47cab1f52fab0e2bc80927ed695142f4261ceb08198a875a928a4eca664 |

Wave history: the candidate was created by the Stage 2 EN12 integration (commit 7604057, the LOCALIZE-S2-B wave's port) and has exactly one later commit, f1138e4 (FIX-P4: the base-theme import repoint of section 2). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The smallest block count in this batch (5 blocks) hides the batch's most structural port. The original is a Basalt-based theme whose own CSS sits in a live `[[module css]]` at the head of its page (168 lines), ahead of its exhibits. The candidate keeps the page's shape but changes the CSS's delivery channel: the head module now imports the candidate's own local--code delivery on the draft host, and the CSS body itself moves to a `[[code]]` exhibit in a collapsible at the page's tail (the topology pass matches the two bodies at 0.962 similarity), with a JP font load added at its head and Noto Sans JP appended to its two font stacks. Everything else is the standard port: the hidden Basalt include repoints to the JP Basalt candidate (FIX-P4), the bare Rate gives way to the preview credit block, and the exhibits translate. Measured churn (diff.md, Tier 2 format; the generator's difflib count with autojunk off: +283/−336, 619 changed lines in 5 change blocks / 4 diff sections — the counts are dominated by the CSS body's relocation, which is one move, not 619 independent changes). The one standing peculiarity is the asset set: all seven of the theme's EN-storage asset URLs are kept, dispositioned as a posting-procedure matter (section 4).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 5 change blocks — 5 specific (100%), 0 heuristic, 0 residue, 0 skipped. The block count is this low because the topology pre-pass matched the relocated CSS body as one DELIVERY-MOVE; the per-label spans below are the honest granularity. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 3 |
| IFTAGS | 2 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README: the RATE-EXHIBIT-KEPT-CANDIDATE label does not survive the bytes — the candidate does not keep the original's bare Rate anywhere; it replaces it with the credit block at the same anchor (section 1). The EXHIBIT-RESTRUCTURE primary on B5 is the tail alignment of the CSS move plus the exhibit translations, not an exhibit change (section 8's census). After adjudication no block is left unexplained, and there is no residue.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:immrama-jp; original theme:immrama on scp-wiki at reference revision 17; candidate `pages/theme:immrama-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the original opens with a hidden div including its Basalt base (original L1–3), then its live CSS module (original L5–172), then the tag gate `[[iftags +theme]]` (original L174). The candidate opens with the same hidden include repointed (candidate L1–3), a head module importing its own delivery plus the interwiki-style frame (candidate L5–10), and the localized gate `[[iftags +テーマ]]` (candidate L12).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3), and the delivery-channel change is declared here because it shapes the whole diff (section 3).
- **Verify:** The sources.tsv row for immrama-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame and delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a centered bare `[[module Rate]]` (original L176–178, inside a `[[=]]` wrapper) and the attribution carried in its CSS banner ("by Arthcymro", original L7–9) and its Info prose ("created by arthcymro", original L186). The candidate deletes the bare Rate and installs the JP form at the same anchor: a `:scp-jp:credit:start-preview`/`end-preview` block inside the same `[[=]]` wrapper (candidate L14–25) carrying the eight ruling-3 fields (title Immrama Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Immrama Theme; 著作権者 arthcymro; 作成年 2025; 初訳時参照リビジョン 17; 元記事リンク the scp-wiki original, on the recorded host). The author field was checked against the original's credit: the banner and the Info prose name arthcymro alone, and no second creator, co-author, or license-box author appears anywhere in the original — the field drops nobody. The CSS banner itself is carried verbatim inside the moved code exhibit (candidate L283–285). There is no license box on either side, and no T7 credit-module CSS: the theme never styled the credit module and no supplement adds any (the credit block's styling is inherited).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). The classifier's RATE-EXHIBIT-KEPT-CANDIDATE label (original span L176–177) is an artefact of the block alignment — it saw the original's Rate line inside B5's range; the candidate side of that range holds no Rate. Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L14–25 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3) records this theme's T4 outcome through its P5/P9 lines; the credit swap is the standing P3 form, checker-verified in the sweep).

### 2. Includes and components

- **What:** Two include changes. (1) The base include: `:scp-wiki:theme:basalt` → `theme:basalt-jp` inside the hidden div (original L2 → candidate L2, block B1) — the candidate imports the JP port candidate of its Basalt base, in the prefix-free same-wiki form the FIX-P4 wave standardized. (2) The usage exhibit's include: `:scp-wiki:theme:immrama` → `:scp-jp:theme:immrama` (in the Info section's code sample). The image-block exhibits' includes also repoint (`:scp-wiki:component:image-block` → `:scp-jp:component:image-block`, candidate L155 and L157; only their `name=` asset URLs stay on the EN host, section 4). The credit includes (section 1) and the interwiki-style include (section 3) complete the candidate's include list.
- **Why:** P1 (KB-15) for the exhibit and component includes; ruling 1 with FIX-P4 for the base: a dependent theme imports the base theme's JP port candidate delivery, never the raw upstream branch delivery, and `theme:basalt-jp` is that candidate. Ruling 4 is not engaged: the base was already ported, no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every target is `:scp-jp:` or the prefix-free `theme:basalt-jp`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery channel itself changes, and this is the theme's defining port decision. The original delivers its own CSS from a live `[[module css]]` on the page (original L5–172, 168 lines). The candidate's head module instead imports the candidate's own `local--code/theme%3Aimmrama-jp/1` from the draft host (candidate L6), with the interwiki-style include at priority 1 naming the same /1 delivery (candidate L7–10) — and the CSS body the /1 delivery serves is present in the page as a `[[code]]` exhibit inside a collapsible at the tail (candidate L279–447), matched to the original's module body by the topology pass at 0.962 similarity (the delta is the font load and stack changes of section 4). So the candidate follows the campaign's standard candidate form (live delivery by local--code, body exhibited as code) where the original used the older inline-module form. The base's delivery is untouched by this: Basalt arrives through the hidden include (section 2) on both sides.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame, priority 1 for the theme's own layer). The draft-host form of the live lines is KB-41, class (iii). The channel change is a form conversion, not a content change: the same CSS reaches the page, and the exhibit is its inspectable source.
- **Verify:** `grep -n 'local--code' candidate.txt` — L6 and L9, both draft host; read the code exhibit (candidate L281–447) against original L5–172 in diff.md.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts (blocks B2–B4 spans): the candidate adds a Noto Sans JP load (Google Fonts, wght 400;700) at the head of the moved code exhibit (candidate L281), moves the original's retained Latin face load — Benne, from fonts.bunny.net (original L15) — to Google Fonts at the same relative position inside the exhibit (candidate L291), and appends `"Noto Sans JP"` to the two font stacks that name Benne (`--header-font-primary` and `--UI-font-primary`, original L23–25 → candidate L299–301). Assets: nothing is re-hosted. All seven of the theme's asset URLs stay on `scp-wiki.wdfiles.com/local--files/theme%3Aimmrama/` — the logo variable (candidate L304), the four line/background images in the CSS (candidate L409, L419, L429, L439), and the two image-block exhibits' `name=` values (candidate L155, L157). These seven lines are exactly T1's hotlink×7.
- **Why:** P7/T5 with KB-16: the original's stacks are Latin-only (Benne), so Japanese text needs the JP face loaded and named in the stacks; the Benne load's host change keeps the retained face on a sanctioned font host (P5's hotlink whitelist). The assets are the deliberate exception: P5/KB-17 would re-host them, and the ledger dispositions them instead — class (ii), KB-58 — because re-hosting is a posting-procedure step and the files serve from the original's storage today. They are recorded here, not silently passed over.
- **Verify:** `grep -n 'wdfiles' candidate.txt` — the seven lines above, all scp-wiki storage; `grep -n 'fonts.googleapis' candidate.txt` — the two loads.
- **Disposition:** Font supplement applied; the seven asset lines DISPOSITIONED (class (ii) / KB-58, GOSIGN2-LEDGER §(c3): P5 DISPOSITIONED).

### 5. Header, sidebar, and site furniture

- **What:** None in the candidate's own lines — and one ledger item to account for. The candidate sets no `--header-title`, `--header-subtitle`, or `--logo-image` (verified by grep; the logo travels as the `--logo` asset variable, section 4), and its sidebar/topbar rules are the original's, carried inside the moved CSS apart from section 4's font lines. T4's P9 item for this theme is an untranslated subtitle, display-affecting in the rendered sample; it has no locus in this file (no header variable exists on either side to carry it), and the ledger dispositions it under ruling 2: header and title language is out of scope for migration correctness.
- **Why:** P9/T6 not engaged in the file; ruling 2 governs the ledger item.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle\|--logo-image' candidate.txt original.txt` returns nothing on either side.
- **Disposition:** DISPOSITIONED (the P9 item, ruling 2; GOSIGN2-LEDGER §(c3)).

### 6. Text translation

- **What:** The exhibits translate throughout (inside block B2's and B5's ranges, since the topology pass folds them into the two giant blocks): the Info prose (original L184–190 → candidate L30–36, including the arthcymro attribution line), the section headings (Info → 情報, Elements → 要素， and the sub-headings), the blockquote and element samples' prose, and the image-block captions (candidate L155, L157: "Image block, to the right hand side." → 画像ブロック、右寄せ。). The CSS comments inside the moved exhibit are the original's own English banner and section markers, carried untranslated as porter-facing text (R1's boundary: comments are not reader-visible, and these are the author's, not the porter's). One link text point is recorded in section 7. No reader-visible English prose remains outside the exhibits' quoted code samples, which are form, not prose.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored mass is expected heuristic shape for a restructure-led diff; each exhibit was read against the mirror for this README rather than waved through.
- **Verify:** The exhibit pairs are diff.md's body sections in order; read candidate L30–60 against original L184–214.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** One kept link to name: the Info prose links the base theme by its original page name, `[[[theme:basalt|Basalt]]]` (candidate L32), exactly as the original does (original L184). It is exhibit prose describing what the theme is built on; the operative base include was repointed in section 2. On scp-jp the name `theme:basalt` does not resolve to the JP candidate (`theme:basalt-jp`), so a reader following the prose link leaves the candidate set — recorded here because the bytes show it, and weighed as prose, not delivery: the sentence's subject is the original Basalt theme, whose page the link names correctly on the EN wiki's namespace as written for the source text. No other prose link in the candidate targets a foreign page; the credit source link names the recorded host (scp-wiki.wikidot.com, candidate L23).
- **Why:** P11: prose links take the JP counterpart or the serving original; this one names the original as its subject, which is the serving-original case in prose form.
- **Verify:** `grep -n 'wikidot.com\|\[\[\[theme' candidate.txt` — the credit link and the Basalt prose link.
- **Disposition:** Standing (prose naming its subject); not a delivery line.

### 8. Structure

- **What:** The structure changes are the delivery conversion of section 3 and nothing else. The exhibit census decides the R3 question: the Info section, the Elements exhibits (blockquote set, div samples, image blocks, tabview material), and the closing furniture are present on both sides in the same order — nothing was dropped or replaced, so the sanctioned-replacement vs silent-deletion question does not arise. The classifier's EXHIBIT-RESTRUCTURE primary (B5, original L171–501 → candidate L447–448) is the tail alignment of the moved CSS plus those translations, not an exhibit change. The candidate's own additions to the page's furniture are the collapsible around the code exhibit (candidate L278–279 and its closer at L448), the standard candidate-form wrapper for an exhibited code body, with translated labels (ソースコードを表示 / ソースコードを閉じる）. Variable names, selectors, and the CSS's internal order are preserved inside the move (0.962 similarity is the font delta, not a reshuffle).
- **Why:** R3 exists to force exactly this adjudication; the census, not the label, decides. The closing rule (structure preserved, corrections appended) is satisfied in the form this campaign's candidates take: the corrections sit in the head frame and at the exhibit's head, not interleaved into the inherited CSS.
- **Verify:** Compare `grep -n '^+\*\|^\[\[div\|^\[\[code\|^\[\[module' original.txt candidate.txt` — the exhibit sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a class of its own: the classifier finds no whitespace-only block pair and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered. The relocation of the CSS body is a channel change (section 3), not formatting churn, and is not counted here.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here there is none to disclose.
- **Verify:** The classification's section 9 counts (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked, absent. The candidate carries no `[!-- ... --]` notes and no port provenance comment; the only comments in the file are the original author's own banner and section markers inside the moved CSS, carried verbatim. The skeleton's "none" for this section survives contact with the bytes.
- **Why:** R2: porter-added text is part of the change record; here the porter added none, which is itself the record (the port's provenance lives in the credit block and this package, not in in-file comments).
- **Verify:** `grep -n 'SCP-JP port\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's seven hotlink errors and one pseudo-ref: the hotlinks are the EN-storage assets of section 4, class (ii) / KB-58, re-hosted at posting if at all; the pseudo-ref is the candidate's own draft-host local--code line (section 3), class (ii) posting-procedure. There is no class (i) error. (2) T4's two display-affecting findings, both dispositioned in the ledger: the P5 asset set (the same seven lines, from the localize side) and the P9 untranslated subtitle (ruling 2; no locus in this file, section 5). (3) The render row's items, all cross-cutting, not charged to the candidate: the notice clip at ≤375 and the 768px sidebar×notice shape (KB-34 family); the WebKit CC "S" glyph (KB-36); the sample's h1 clipping at 320, the 評価 label crush, and the `.open-menu` overprint (KB-32/KB-34: the preview rate module's label rendering at narrow widths); and the page-overflow readings 367–552px (KB-33/KB-34). (4) No exception is claimed for this theme: no foreign include is kept, no asset is silently passed, and the verdict is a plain PASS.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries and ruling 2), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 91): exit 1, 8 errors / 1 warn / 0 infos; seven hotlink (the section 4 assets) and one pseudo-ref, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN12)): FINDINGS, the items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 101): FINDINGS jointly, display-affecting findings 2 (the P5 assets; the P9 subtitle), no display-collapse item, and no unincorporated upstream updates; the ledger §(c3) line records both as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +283/−336 in 5 change blocks / 4 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:immrama-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 101; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-immrama-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The FIX-P4 commit (f1138e4) that repointed this theme's base include touched 39 files in one wave; the other 38 are those themes' own records, not this one's change set. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Immrama Theme
- **Author:** arthcymro
- **Source:** https://scp-wiki.wikidot.com/theme:immrama — revision 17
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
