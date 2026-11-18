# Review package — theme:dia-de-muertos-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:dia-de-muertos-jp — origin EN, population #80 [GOSIGN2-LEDGER (b) row 80]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 80]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 0 infos (pseudo-ref×8); standing classes dispositioned in register c1 [T1-ROWS row 100; GOSIGN2-LEDGER (b) row 80]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — webkit-320 page-overflow 322px, sample overflow 337–419px@≤375, anom-bar specimen unreadable dark-magenta-on-black at 1366 both engines; decoration assets 404 = EN8 owner-deferred, not defects. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 80, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 80]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 80]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:dia-de-muertos-jp.txt sha256:441dc620b615f2c5ebdae40a0b25f0f8ddc238bad85b8344d475e5f45b374131; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 80) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×8 (class (ii), section 11); the render row's items (KB-33/KB-34 overflow family; the anom-bar specimen; decoration assets 404 as owner-deferred, KB-58, section 11); T4's P7 and P9 items dispositioned in the ledger §(c3) line (sections 4 and 5) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:dia-de-muertos | theme:dia-de-muertos-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 28 (first translation; the candidate's credit block records 初訳時参照リビジョン: 28) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-dia-de-muertos.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:dia-de-muertos-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 411 lines / 11,810 bytes | 431 lines / 13,979 bytes |
| SHA-256 | 73ab128113eaeb45eee16841b0dd24c958f05caa49596e9ac308acae76f24d29 | 441dc620b615f2c5ebdae40a0b25f0f8ddc238bad85b8344d475e5f45b374131 |

Wave history: the candidate was created by the Stage 2 EN8 integration (commit 184cb65, the LOCALIZE-S2-A wave's port), reshaped by c65ec92 (rework2-p2: embedded bases swapped for references across 9 inlined pairs, this theme among the receivers), and touched last by 1869877 (FIX-CREDIT-D, the population-wide translator-attribution normalization). No FIX5 commit touches this file. Recorded drift: the original has been superseded upstream since rev 28; the campaign record carries the follow-up diff artifact `diff-dia-de-muertos-from28.txt` (sources.tsv K5a-i note), and this package documents the port against the rev-28 mirror it was made from.

## Summary

A layered theme, and the layering is the port. Día de Muertos is an override theme: it sits on Black Highlighter (delivered at frame priorities 1–2) and on the Old Money theme (delivered by a hidden include), and its own CSS is a thin override layer at priority 4. The candidate rebuilds exactly that stack on JP distributions: BHL from scp-jp.github.io, the base as the JP port theme:old-money-theme-jp, its own three deployed CSS attachments re-hosted to the draft host, and its source exhibit reduced to the Día de Muertos overrides alone, with a porter banner in the exhibit explaining the arrangement. The body (theme-colors exhibit, usage prose, logo exhibits) is translated throughout. Measured churn (diff.md, the generator's difflib count with autojunk off: +159/−144, 303 changed lines in 70 change blocks / 6 hunks). Nothing in the diff repairs a defect; the two T4 items (no JP font declared in this layer; the Spanish subtitle kept) are dispositioned, and the decoration-asset 404s are the owner-deferred hosting state, not findings against the candidate.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 70 change blocks — 41 specific (58.6%), 25 heuristic (35.7%), 4 residue (5.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 2 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 4 |
| DRAFT-HOST | 7 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 4 |
| HEADERVAR | 1 |
| INCLUDE-REPOINT | 6 |
| RESTORATION | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 25 |
| TRANS-UNANCHORED | 25 |
| IFTAGS | 2 |

Adjudication for this README (every block was read against the bytes): the four EXHIBIT-RESTRUCTURE primaries (B2, B4, B8, B69) are all include repoints whose secondary label says so — the interwiki-style prefix drops and the tail frame — adjudicated in sections 2 and 8 against the exhibit census, not restructurings. The RESTORATION block (B63) is the code exhibit's banner, adjudicated in section 10. The four residue blocks resolve in the appendix (two formatting seams, one one-line heading translation, one exhibit-tail blank-line group). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:dia-de-muertos-jp; original theme:dia-de-muertos on scp-wiki at reference revision 28; candidate `pages/theme:dia-de-muertos-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the original opens with its tag gate `[[iftags +theme]]` (original L1) and its BHL frame; the candidate opens with the localized gate `[[iftags +テーマ]]` (candidate L1), the credit block, and the same frame on JP hosts (candidate L14–35). The layering the frame encodes is the theme's anatomy: priorities 1–2 BHL (normalize, black-highlighter), the Old Money base arriving by hidden include at the tail (its own frame carries priority 3), and this theme's overrides at priority 4 (candidate L428–431).
- **Why:** Section 0 declares the provenance route and the layer stack so every later count is read against the right baseline; the gate's tag is P2, the stack is P6/T3 with T9 base delivery (sections 2–3).
- **Verify:** The sources.tsv row for dia-de-muertos-jp; `sha256sum original.txt` against the Provenance table; the frame lines at candidate L27–35 and L421–431.
- **Disposition:** Standing (the route itself); the frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` in a right-aligned div (original L28–30, block B6) and no info pair. The candidate deletes it and installs the JP form at the head: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L3–12) carrying the eight ruling-3 fields (title ディア・デ・ムエルトス・テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Día De Muertos Theme; 著作権者 Kilerpoyo（Día de Muertos部分）、djkaktus・Woedenaz（Old Money基盤部分）— the split credit the layered anatomy requires; 作成年 2022; 初訳時参照リビジョン 28; the source link, candidate L11, naming scp-wiki.wikidot.com, the original's recorded host). T4's two credit-notation notes (the source-link field's form, the translator field's form) are closed in the bytes as they stand: the field set is the standard eight in the FIX-CREDIT-D final form. No T7 credit-module CSS supplement was added; neither side styles the credit module's DOM in this layer.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields and the translator credit form; the author field's split form is the ruling's accuracy requirement applied to a two-author layered theme.
- **Verify:** `grep -n 'module Rate\|credit:' candidate.txt` — only the `:scp-jp:` preview pair returns; read candidate L3–12 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Three include shapes change. (a) The head frame's two interwiki-style includes drop their `:scp-wiki:component:` prefix to the bare `component:` form and swap their delivery host (blocks B2–B5; candidate L27–35, section 3). (b) The usage exhibit's base includes are swapped for JP references (block B22, the rework2-p2 edit): the original's three escaped lines (`:scp-wiki:theme:black-highlighter-theme`, `:scp-wiki:theme:old-money-theme`, `:scp-wiki:theme:dia-de-muertos`, original L104–106) become two (candidate L109–110: `:scp-jp:theme:black-highlighter-theme` and `theme:dia-de-muertos-jp`); the Old Money line disappears from the exhibit because users no longer paste it — the base arrives by the candidate's own hidden include. (c) The tail's hidden base include is repointed `:scp-wiki:theme:old-money-theme` → `theme:old-money-theme-jp` (block B67, candidate L421), and the tail interwiki-style include takes the same bare form (B69). The theme-squares exhibit include is bare `component:theme-squares` on both sides and does not change; its color-name parameters (Mexican Pink, Cempasuchil Fields, …) are the exhibit's data names and are carried untranslated, with the exhibit's heading translated (section 6).
- **Why:** P1 (KB-15) for the repoints: each names the JP counterpart that exists. The prefix-drop form is the campaign's BHL-frame convention: a bare `component:` include resolves on the reader's own wiki, which is what a layered base frame needs. T8 covers the base-theme swap to the JP port (old-money-theme-jp), and ruling 4 is satisfied by that port existing as its own candidate.
- **Verify:** `grep -n '\[\[include' candidate.txt` — seven includes; every live one is a `:scp-jp:` or bare JP-resolving form, and no `:scp-wiki:` survives outside the diff's removed side.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** Three delivery channels, all re-based. (a) BHL: the frame's `theme=` URLs move from nu-scptheme.github.io to scp-jp.github.io (blocks B3, B5: candidate L29, L34), the JP distribution of Black Highlighter. (b) The theme's own deployed CSS attachments — three files the original imports from scp-wiki.wdfiles.com/local--files/theme%3Adia-de-muertos/ (original L244–246: papelpicadostyle.css, doubled-crossed.css, colus.css) — are re-hosted to the draft host's theme%3Adia-de-muertos-jp folder (block B64: candidate L262–264). (c) The theme's own code page: the tail module import and the priority-4 frame move from the original's scp-wiki.wdfiles.com local--code /1 to the candidate's own /1 on the draft host (blocks B68, B70: candidate L425, L430). The source exhibit (candidate L240–417) carries only the Día de Muertos overrides; its banner states the arrangement (section 10).
- **Why:** T9 (base delivery from JP distributions) for (a); P4/T9 for (b) and (c): own-code and own-file delivery served from JP hosts, with the draft-host form of the live lines being KB-41, class (iii) — sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'github.io\|wdfiles' candidate.txt` against the lines above; no scp-wiki.wdfiles.com or nu-scptheme.github.io line survives.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** This layer loads no font of its own: there is no `@import` for a typeface and no JP font declaration in the candidate's own CSS (T4's P7 item: 和文字体の自前宣言なし). The stacks it names are variables (`--decorative-font: 'papel_picadoregular', 'Colus', Verdana`, candidate L281; `--header-font`, `--mono-font` likewise variable-driven) whose faces arrive through the bases — and the Old Money JP base substitutes Google Fonts for the original's Adobe Fonts (Typekit) imports, as the exhibit banner records (candidate L248–252). Assets: the three CSS attachments of section 3 are the theme's files, re-hosted; the render record's decoration-asset 404s are image assets whose hosting is the owner-deferred state (below), not files this layer mis-points.
- **Why:** P7/T5 with KB-16: the load gap the class exists to prevent is a theme whose own text renders in a fallback because no JP face is loaded anywhere in its stack; here the stack's base layer carries the JP font load, and the ledger judged the layer-local absence under the T4 bar and dispositioned it. KB-58 covers the deferred decoration assets (owner decision 2026-11-16, recorded in the render register).
- **Verify:** `grep -n '@import' candidate.txt` — the three attachment imports of section 3 and the delivery imports only; the banner's font statement is candidate L248–252.
- **Disposition:** DISPOSITIONED — P7 (GOSIGN2-LEDGER §(c3): recorded without a display-affecting mark; T4 bar) and the decoration assets (KB-58, owner-deferred).

### 5. Header, sidebar, and site furniture

- **What:** One header variable is set in this layer: `--header-subtitle: "Nadie sale vivo de esta vida."` (candidate L273), the original's Spanish subtitle carried byte-identical — T4's P9 item (サブタイトルのスペイン語残存）. The theme sets no `--header-title` and no `--logo-image` in its own layer (the logo exhibits in the body are content, section 6); header and sidebar structure arrive from the BHL and Old Money bases.
- **Why:** P9/T6 is the class that would override the subtitle; the ledger dispositioned this theme's P9 under ruling 2, which takes header and title language out of migration-correctness scope. The subtitle is also the theme's namesake motto, which is the circumstance the ruling's case-by-case taste reservation exists for.
- **Verify:** Read candidate L273 against original L255 in diff.md (unchanged line inside the exhibit's variable block).
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P9, ruling 2).

### 6. Text translation

- **What:** The body is translated throughout, in the two counted groups: 24 TRANSLATION-ANCHORED primaries (the theme-colors exhibit headings and values, the usage prose anchors, the logo exhibit captions, the collapsible labels) and 24 TRANS-UNANCHORED primaries (one- and two-line prose translations, verified against the mirror for this README), plus the heading translation the differ left unlabeled (appendix, B23). The theme-squares exhibit's parameter values (color names and RGB tuples) are data, carried unchanged (section 2). In-CSS text (R1): the exhibit's comments are the original's English comments, kept, apart from the banner (section 10); the decorative-font specimen line is translated (candidate L226: 装飾フォントはPapel Picadoです). Spanish survives reader-visible only in the subtitle (section 5) and the credit original-title field (candidate L7).
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored group is where a silent deletion would hide, which is why each was read individually rather than waved through as a class.
- **Verify:** The pairs are diff.md's six hunks in order; a Spanish scan of candidate.txt returns the subtitle (candidate L273, inside the exhibit's variable block), the credit original-title field (candidate L7), and the theme's own name inside translated captions (candidate L72, L80), and nothing else.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the items named.

### 7. Links

- **What:** No LINK-REPOINT block fired. The candidate's one live outbound link is the credit source link (candidate L11), naming scp-wiki.wikidot.com — the original's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed. The body contains no prose links to EN-wiki pages; its exhibits are the include samples of section 2.
- **Why:** P11 under the dead-reference evidence standard: a link that already names the serving original needs no change.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and channel order are preserved; the candidate's code exhibit sits where the original's sits (original L235 → candidate L240), the head module and frame keep their order, and the tail stack (hidden base include, own module, own frame) mirrors the original's tail (original L401–411 → candidate L421–431). The classifier's four EXHIBIT-RESTRUCTURE primaries adjudicate to section 2's include repoints: in B2/B4 the interwiki-style exhibits keep their includes and parameters (only the prefix and host change), in B8 the theme-squares exhibit keeps its include and data, and in B69 the tail frame keeps its form. An exhibit census confirms the shape: theme-colors exhibit, usage exhibits, logo exhibits, and the code exhibit are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise for this theme.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[include\|\[\[code\|\[\[collapsible' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two small seams, both in the appendix: a blank-line pair in the body (B11) and a rule-length seam inside the formatting exhibit (B17, the original's `----` sample rule against the candidate's `-----`). The classifier finds no whitespace-only block and no re-indentation pair (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The appendix rows name the lines; diff.md's hunks show both seams in context.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation with no original counterpart, in CSS-comment form inside the code exhibit's banner (candidate L248–252): the JP-port paragraph stating that the Old Money base CSS is delivered by the hidden include of theme:old-money-theme-jp, that that base substitutes Google Fonts for the Adobe Fonts (Typekit) imports and re-hosts assets to JP file storage, and that this exhibit carries only the Día de Muertos overrides. It rides inside block B63 (the classifier's RESTORATION label: the banner's first lines match the original's banner, and the paragraph is the addition). It is load-bearing — it is the only in-file explanation of why the exhibit is a fraction of the original's CSS. No `[!-- --]` translator notes and no editor lines exist in the candidate.
- **Why:** R2: porter-added text is part of the change record, and this one carries a delivery fact (the base's font substitution) that sections 3 and 4 rely on.
- **Verify:** Read candidate L241–253 (the whole banner).
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's eight pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host local--code and local--files lines and the frame's delivery references (section 3); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. (2) The render row's overflow items (webkit-320 page-overflow 322px; sample overflow 337–419px at ≤375): the recorded cross-cutting families, static credit replica fixed width (KB-33) and preview chrome (KB-34), not charged to the candidate. (3) The render row's anom-bar specimen (unreadable dark-magenta-on-black at 1366, both engines): a specimen-shape reading recorded in the same register block, in the KB-37 family of by-design specimen content. (4) The decoration assets 404: KB-58, the owner-deferred hosting state (owner decision 2026-11-16), expressly not a theme defect in the register's own words. T4's two items (P7, P9) are argued in sections 4 and 5.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 100's, the render items are the ledger §(c2) block for this theme (RENDER-S2-B (EN8)).
- **Disposition:** DISPOSITIONED (all four).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 100): exit 1, 8 errors / 1 warn / 0 infos; all eight errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN8)): FINDINGS, the items of section 11(2–4), all dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 80): FINDINGS jointly, display-affecting findings 2 (the P7 font item and the P9 subtitle); the ledger §(c3) line records the theme's T4 outcome as P7 and P9 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +159/−144 in 70 change blocks / 6 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:dia-de-muertos-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 80; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The layered stack, stated plainly

A reviewer comparing the two files cold could misread this port twice: first as a theme whose CSS shrank (the exhibit carries overrides only), and second as a theme whose frame priorities (1, 2, 4) have a hole at 3. Both readings are answered by the same fact, which the candidate's own banner states (candidate L248–252): the Old Money base is a separate JP candidate (theme:old-money-theme-jp), included hidden at the tail, and its frame occupies priority 3. This theme's package therefore documents one layer of a four-layer stack, and the layer boundaries — BHL from the JP distribution, the base by hidden include, the overrides in the exhibit and the three re-hosted attachments — are the port's actual content.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots.

| Block | Shape | Resolution |
|---|---|---|
| B11 (no signature) | Original L69–70 → candidate L75: a blank-line pair in the body prose | Formatting seam where the translated prose re-flows; no content on either side (section 9) |
| B17 (no signature) | Original L86–87 → candidate L91–92: `[[/div]]` plus the sample rule (`----` → `-----`) | Formatting seam inside the syntax exhibit; the rule is sample text and its length carries no meaning (section 9) |
| B23 (no signature) | Original L110–111 → candidate L114–115: the exhibit heading `+ Examples` → `+ 例` | A one-line heading translation the differ left unlabeled; counted in section 6 |
| B66 (no signature) | Original L396–397 → candidate L414–416: blank lines at the code exhibit's tail | Exhibit-tail formatting where the candidate's exhibit closes with two blank lines against the original's one (section 9) |
| B63 (heuristic, RESTORATION) | Candidate L241–253: the exhibit banner, whose added lines match the original's own banner region | The porter banner paragraph (JP delivery and font substitution), adjudicated in section 10 |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-dia-de-muertos-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). The candidate layers over `pages/theme:old-money-theme-jp.txt` by hidden include (section 0) — that base is its own candidate with its own review package, and the layering relationship, not the base's content, is what this package documents. The follow-up diff artifact for the upstream drift since rev 28 (`diff-dia-de-muertos-from28.txt`) sits in the campaign record, outside this repo. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Día De Muertos Theme
- **Author:** Kilerpoyo（Día de Muertos部分）、djkaktus・Woedenaz（Old Money基盤部分）
- **Source:** https://scp-wiki.wikidot.com/theme:dia-de-muertos — revision 28
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
