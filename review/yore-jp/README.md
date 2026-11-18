# Review package — theme:yore-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:yore-jp — origin CN, population #248 [GOSIGN2-LEDGER (b) row 248]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 30b077a5a91d580b88576f6276559f749410bd06ba344ce70940435a937eb0c7); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 12 errors / 0 warns / 1 info (hotlink×9, pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 248; GOSIGN2-LEDGER (b) row 248]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 513px@320/375 on page and sample (+ 899px@768 on sample) + sidebar-unreachable at 375/320 on both pages + runtime-hotlink site-theme chain + candidate hosts ah-sandbox.wdfiles.com, ah-sandbox.wikidot.com, hormress.github.io, scpsandboxcn.wdfiles.com; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN18)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN18)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 247, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 247]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 248]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:yore-jp.txt sha256:30b077a5a91d580b88576f6276559f749410bd06ba344ce70940435a937eb0c7; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 248) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×9 and pseudo-ref ×3 (class (ii), section 11); the render row's items (posting-rewrite class, section 11); T4's charges (ledger §(c5): header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves), with T4's most serious charge — the live delivery's dependence on the author's personal GitHub Pages — repaired in fact by FIX-P4 before the determination (section 3). One record item is **flagged** in the per-theme record: sources.tsv's "superseded upstream" note, which its own cited artifact contradicts |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:yore | theme:yore-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 9 (first translation; the candidate's credit block records 初訳時参照リビジョン: 9) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-yore.txt`, via the mirror store `review-mirrors/orig-yore-rev9.txt` (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:yore-jp.txt`, copied at worktree HEAD 662baf3 |
| Lines / bytes | 1,154 lines / 29,898 bytes | 1,177 lines / 32,881 bytes |
| SHA-256 | f0ee36a6dce9abd1c2a3bebbd951779a09c4e789090190c3c46e180e8f5ee267 | 30b077a5a91d580b88576f6276559f749410bd06ba344ce70940435a937eb0c7 |

Wave history: the candidate was created by the Stage 2 CN18 integration (commit 5b5dbe4) and has three later commits: f1138e4 (FIX-P4, the repoint of the base delivery from the author's GitHub Pages to theme:parallel-jp, section 3), a497307 (FIX4-MECH, removal of the duplicate base import the FIX-P4 convergence produced, section 3), and b5cb724 (the usage-example sweep). The verdict stamp reads STALE on the sweep commit alone. Provenance kind (sources.tsv): K5b-3 — the candidate layers over the base candidate theme:parallel-jp, and this package's diff covers the theme's own layer only.

## Summary

A CN theme layered over Parallel, distributed in an unusual form: the original carries no `[[code]]` exhibit and no frames of its own — its CSS lives in two live modules (a gated head module importing the Parallel fragment plus a handful of inline overrides, and a tail module holding the full variable and rule set), and its frames live on the base theme's page, which a user includes first. The candidate rebuilds that as the JP form: a head module importing parallel-jp/1 and its own code/1, three interwiki frames staging the merged base (priorities 1–2) and its own layer (priority 3), and the two CSS sources merged into a single `[[code]]` block held in a display:none div, with the documentation body after it. Measured churn (diff.md, the generator's difflib count: +377/−355; a GNU-diff count of the same pair gives 734 changed lines) in only 13 change blocks, because the moved CSS aligns as a few giant blocks — the classifier's topology record names the core move (module-css → code-css, body similarity 0.86). Two states of the delivery must be kept apart: the T4 lane audited the pre-FIX-P4 candidate, whose live imports named the author's personal GitHub Pages, and charged that as its most serious item; the current bytes carry FIX-P4's repair. The T4 lane also recorded the display:none exhibit presentation as a regression against the collapsible form its sibling in this batch (theme:wish-for-miracle-jp) kept; that observation is carried in section 8 and the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 13 change blocks — 10 specific (76.9%), 3 heuristic (23.1%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COLON-ENC | 1 |
| COMMENT-TEXT | 3 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DELIVERY-MOVE | 9 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 2 |
| RESTORATION | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |
| TRANS-UNANCHORED | 6 |
| WS-ONLY | 1 |

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:yore-jp; original theme:yore on scp-wiki-cn at reference revision 9; candidate `pages/theme:yore-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN18 integration (sources.tsv kind: K5b-3, a layered port over theme:parallel-jp; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The delivery topology is transformed, not merely moved (section 3): the original's two live modules become a head import module plus a code exhibit. One provenance record disagrees with its own evidence: sources.tsv's note says the original was "superseded upstream since the reference revision", but the follow-up artifact the note cites records rev9 → rev9, no change (per-theme record).
- **Why:** Section 0 declares the provenance route and the layering baseline: every count below is read against the theme's own layer only; the base layer is theme:parallel-jp's own record.
- **Verify:** The sources.tsv row for yore-jp; `sha256sum original.txt` against the Provenance table; the follow-up artifact `gosign2-lanes/lane-oc-gs-localize-s2-E/diff-yore-from9.txt`.
- **Disposition:** Standing (the route itself); the sources.tsv note is flagged in the per-theme record.

### 1. Credit and attribution

- **What:** The original's credit area is the CN trio (original L41–45) with placeholder inline content （页面信息 / 更多页面信息 — "page information" / "more page information") and a bare `[[module rate]]` in a `[[>]]` wrapper above it (original L37–39). No author is named anywhere in the original's credit furniture; the attribution rests on the theme's provenance — the work is Dr Hormress's (the ARED logos are his files on his sandbox hosts, the base theme Parallel is his, and the FIX-P4 report names him as Parallel's author). The candidate installs the JP form (candidate L25–35): `:scp-jp:credit:start-preview`/`end-preview` carrying the eight ruling-3 fields — title 往昔テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 往昔 版式； 著作権者 Dr Hormress; 作成年 2024; 初訳時参照リビジョン 9; 元記事リンク https://scp-wiki-cn.wikidot.com/theme:yore, the host sources.tsv records (no probe needed: they agree) — plus a porter-authored 使用フォント field (candidate L34) that discloses the font situation honestly: the fonts are loaded by the Parallel base (Lexend, Jost, Inter, JetBrains Mono, Noto Sans SC, Noto Serif SC, all SIL Open Font License as claimed), and the images are the author's work under the original wiki's terms. The bare rate module is deleted. Neither file carries a license box, and the T4 audit records that absence as conforming for this theme.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09); the CN trio is ledger class C furniture. Ruling 3 fixes the eight fields. The author field is the port's attribution judgment, grounded in the provenance above rather than in a credit line the original never wrote.
- **Verify:** `grep -n 'module rate\|credit:start' candidate.txt` — only the preview pair; read candidate L25–35 against original L37–45.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c5): credit fields FIXED by the credit waves; the T4 audit's §3 verdict is APPLIED with notes).

### 2. Includes and components

- **What:** The gate's tag is localized, +版式 → +テーマ (original L1 → candidate L23). The anomaly-class-bar include is repointed (candidate L1168): `:scp-wiki-cn:component:anomaly-class-bar-source` → `:scp-jp:component:anomaly-class-bar-source`, and its parameters are localized with it — the original's `lang=cn` argument is dropped and its CN-XXX placeholder becomes JP-XXX (candidate L1170); the T4 audit verified the JP backend component exists on scp-jp. The image-block include stays in the plain form on both sides (its `name=` is section 4) with its caption translated. One include is added: `[[include component:betterfootnotes]]` (candidate L21), the JP environment's footnote component, for the footnote exhibits the body carries (e.g. candidate L926). The usage exhibit changes shape, not just host: the original's two lines (`[[include :scp-wiki-cn:theme:parallel]]` then `[[include :scp-wiki-cn:theme:yore]]`, original L65–66) become one (`[[include :scp-jp:theme:yore-jp]]`, candidate L872), because the candidate's head module imports the base itself (section 3); the surrounding prose is rewritten to match (section 8).
- **Why:** P1 (KB-15) for the repoint; P2/KB-08 for the gate tag; the footnote component is the environment-adaptation supplement. The usage form follows the delivery architecture rather than the original's two-include instruction, which would now double-apply the base.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame trio, footnote component, credit pair, image-block, and anomaly-class-bar, all `:scp-jp:` or plain JP components, plus the one escaped usage line.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers through two live modules and no code exhibit. Inside the gate, a head module (original L3–29) imports the Parallel fragment (`scp-wiki-cn.wikidot.com/fragment:parallel/code/1`) and adds the theme's inline overrides (the hover/ctn image rules and the meta-title rule). After the gate, a tail module (original L374–1154) holds the full CSS as inline module text. The candidate merges both into one `[[code]]` block (candidate L38–844, held in a `[[div id="default" style="display: none;"]]` at L37): the head module's overrides first (candidate L40–63, the "Fuck ACS" comment carried with them), then the tail module's body in its original order (the pixabay attribution comment at candidate L65, the lang blocks, the palette, the rules). A head module before the gate (candidate L1–4) imports `theme%3Aparallel-jp/1` and the candidate's own `theme%3Ayore-jp/1` from the draft host; self-delivery census: the candidate has exactly one `[[code]]` block, so /1 names the block that holds the CSS. Three interwiki frames follow (candidate L6–19): priority 1 and 2 naming parallel-jp/1, priority 3 naming yore-jp/1. The pair mirrors the base page's own frame set — the CN Parallel original (mirror `orig-parallel-rev41.txt` L29–38) carries two sidebar frames at priorities 1 and 2 naming normalize-min.css and parallel-min.css — with both targets merged to parallel-jp/1 under FIX-P4's mapping (Parallel's JP candidate merges both files into its /1, as its report entry verifies by fetch); the third frame is this theme's own, which the CN distribution never needed because the base page's frames came with the required first include. The frames carry the JP argument set (priority/theme only), the same form the T4 audit judged exemplary in design. Two repair waves then touched this delivery, and their order matters. At T4 time the head module imported the two hormress.github.io files directly and frames 1–2 named the same host — the author's personal GitHub Pages, outside the sanctioned delivery hosts — and the lane charged it MISSED, live and display-critical (pattern 4). FIX-P4 (commit f1138e4) repointed all four references to parallel-jp/1 with fetched same-role evidence. That convergence left the head module importing parallel-jp/1 twice in adjacent lines, and FIX4-MECH (commit a497307) removed the duplicate — KB-65's core case, a true same-module duplicate, correctly removed (contrast theme:xmas-jp in this batch, where the same wave's file-level rule emptied conditional delivery slots). On the current bytes no hormress.github.io reference remains anywhere (grep count 0).
- **Why:** P4/T9 (delivery served from the JP side) with the FIX-P4 pattern-4 mapping; P6/T3 for the frames. The draft-host form of the own-delivery lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code\|hormress.github.io' candidate.txt` — the two head imports and three frame targets, all draft-host; the FIX-P4 report's Parallel entry carries the mapping and its fetch evidence.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the personal-CDN dependence is FIXED by FIX-P4, and the duplicate it produced is FIXED by FIX4-MECH — neither is merely dispositioned.

### 4. Fonts and assets

- **What:** Fonts: this layer loads no font and names no font stack (a grep for JP font names returns 0, as the T4 audit's pattern-7 census recorded). CJK rendering rides on the base layer's stacks (Noto Sans SC / Noto Serif SC via theme:parallel-jp), so Japanese-specific glyphs render in mainland forms through the base — charged at T4 as pattern 7 and dispositioned under the ledger §(c5) class outcomes; the stacks themselves are theme:parallel-jp's own layer and its package's record, and this theme's credit field discloses the dependency rather than hiding it (section 1). The theme's own translated strings use Japanese glyph forms in the text (section 6); what is missing is a JP face in the delivery chain, and the chain's font layer is the base's. Assets: nine external files are kept on the author's and the CN sandbox hosts (the T4 pattern-5 census): on ah-sandbox.wikidot.com — the `--title` ARED text SVG (candidate L68), the `--logo` ARED_2_i.svg (candidate L92), the `--yore-bg` background (candidate L93; its path colon is encoded, `theme:yore` → `theme%3Ayore`, block B7), and the two Parallel logo images in the body (candidate L862, L864, the second being the Chinese-logo hover image, the original's design, carried); on ah-sandbox.wdfiles.com — ARED_2.svg as a body image (candidate L858) and as the image-block's `name=` (candidate L923); on scpsandboxcn.wdfiles.com — the chapter-title background JPG, in the live text and its exhibit (candidate L1042, L1047), the host the T4 lane rated the most expiry-prone of the set.
- **Why:** P5 (asset hosts): the files were not re-hosted to JP storage; the ledger dispositions asset hosts as class (ii), which is where re-hosting happens (at posting). P7 for the font gap, with the base-layer ground stated above.
- **Verify:** `grep -n 'ah-sandbox\|scpsandboxcn' candidate.txt` against the census above; the T4 audit's pattern-5 itemization (i)–(viii) is the same set.
- **Disposition:** DISPOSITIONED (class (ii); GOSIGN2-LEDGER §(c5): asset hosts = class (ii)). The P7 item is dispositioned under the same §(c5) class outcomes.

### 5. Header, sidebar, and site furniture

- **What:** The header variables live in the moved CSS. The `:root:lang(cn)` block is re-scoped to `:root:lang(ja)` (B5, candidate L67–70): it keeps the `--title` ARED text SVG (section 4) and its subtitle is translated, 凡人终不朽 → 死すべき者はついに不朽ならず (B6, candidate L69). The `:root:lang(en)` block is kept with the Latin motto "Mortales Desinunt Immortales" (candidate L72–74) — an intentional design motto, not an untranslated string (the T4 audit's §9 excepts it on exactly that ground). The meta-title exhibit's text is localized （往昔 版式 → 往昔テーマ, candidate L849). The theme's furniture proper — the grid layout that places the content area on CSS grid tracks — is inherited unchanged; the T4 audit's §8 records the sidebar/topbar item as N-A (original-inherited), with the mobile `.open-menu` behavior (candidate L824–826 region, the original's own rule) noted for a posting-time device check rather than charged.
- **Why:** P9/T6 for the lang-scoped header strings: the ja scope is the JP environment's form of the original's cn scope, and the rendered subtitle is reader-visible header text (P10/KB-18 carried in a variable).
- **Verify:** Read candidate L65–95 against original L375–405.
- **Disposition:** Standing; the header-language item is among the charges the ledger §(c5) dispositions (header language = ruling 2).

### 6. Text translation

- **What:** The whole documentation body is translated; because the body aligns against the restructure as a few giant blocks, the translation mass rides inside B4, B12, and B13 rather than in per-line blocks. Counted separately: the CSS comments inside the moved code (COMMENT-TEXT, B8–B10: 自定义 DIVs → カスタム DIV; 页面标签 → ページタグ; 数不清的适配 → 数え切れないほどの調整）, porter-visible only, and the one TRANSLATION-ANCHORED pair (B6, the subtitle, section 5). The CSS `content:` strings are empty on both sides (the T4 audit's §9 census), so no rendered-string item arises in the code; the reader-visible strings are the prose, the exhibit labels, and the section 5 variables, all translated. The T5 audit found no simplified-Chinese residue anywhere in the body (mechanical scan 0) and recorded its findings at the level of notes — a dropped plural "s" on one heading （自定义 DIVs → カスタム DIV, candidate L1146 region) is the largest.
- **Why:** P10 (KB-18). The comment translations are the reader-invisible half of the same duty: they keep the delivered source maintainable by JP readers.
- **Verify:** The body pairs are diff.md's sections in order; the T5 section of REPORT-GOSIGN2-LOCALIZE-S2-E §CN18-2 carries the line-level notes.
- **Disposition:** Standing (the port itself); T5 judged jointly with T4 (section 12).

### 7. Links

- **What:** Three prose links are expanded from the original's relative forms to absolute scp-wiki-cn URLs (candidate L870–876): the ARED hub （異常宗教表現部門）, theme:parallel, and theme:lumina. No JP counterpart pages exist for any of the three. The T4 lane charged the set as pattern 11, minor — the hub link is a direct hub link, the type the pattern names — and the ledger §(c5) dispositions the row's charges. The credit block's source link (section 1) is the prescribed origin form and is not a pattern-11 item, as the T4 audit itself notes.
- **Why:** P11: prose links take the JP counterpart or the serving original; here there is no counterpart, so the choice is between the origin URL and a dead same-site form, and the candidate takes the origin URL with the charge recorded.
- **Verify:** Read candidate L870–876 against original L62–69.
- **Disposition:** DISPOSITIONED (ledger §(c5), among the row charges).

### 8. Structure

- **What:** The restructure of section 3 is this theme's structural fact, and the T4 lane's structure note is its record: the original's two-module ordering is lost, the delivered source is hidden in a display:none div rather than presented in a reader-openable collapsible (theme:wish-for-miracle-jp in this batch keeps the collapsible form), and upstream-following diffs can no longer be applied directly — against which the note also records that variable names and selector order are preserved and the result is functionally near-equivalent (unconditional CSS served via local--code). The exhibit census decides the deletion question: the documentation body is present in full after the code block — the meta-title div, the intro grid with its hover image pair, the usage exhibit, the two module-CSS customization exhibits (candidate L879–888, L892–905 = original L73–82, L86–99), the image-block, the five HTML exhibits (candidate L1033–1143 = original L227–337), the pseudo-title section, the ACS section, and the anomaly-class-bar include — in the original's order. The classifier's two remaining primaries adjudicate against this census: B4 (EXHIBIT-RESTRUCTURE over the whole body region) is the relocation-plus-translation of that body, and B12 (RESTORATION, the post-code region) is the classifier's name for content that re-presents the original's own earlier region after a move — the documentation body sitting after the delivery block — not a restoration event and not new content.
- **Why:** R3: a restructure and a deletion share a diff shape and ledger class I charges the silent form; the census is complete, so no class I item arises. The presentation point (display:none against collapsible) is a reader-facing regression the T4 lane recorded; it does not affect delivery, because local--code serves the block either way.
- **Verify:** Compare the exhibit marker sequences of the two files (`grep -n '\[\[code\|\[\[include\|class="meta-title"'` on both).
- **Disposition:** Standing, with the T4 structure note carried as the record; no ledger charge arose from it.

### 9. Formatting only

- **What:** One WS-ONLY block (B11): a trailing space trimmed on a grid-template-areas line inside the moved CSS. The classifier finds 0 re-indentation pairs. The +377/−355 churn is the section 3 restructure re-presenting the CSS, not formatting churn.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** classification.json's WS-ONLY entry against diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added. The one attribution comment at the CSS head — the pixabay URL above the lang blocks (candidate L65) — is the original's own source credit for the background photograph, carried from original L375, not a porter annotation. A grep for port/annotation markers in candidate.txt returns nothing, and the porter-authored texts that exist are the credit block's font field (section 1) and the translated prose (section 6).
- **Why:** R2: porter-added text is part of the change record; its absence is recorded with the check that establishes it, and inherited attribution text is not misclassified as porter text.
- **Verify:** `grep -n 'Ported\|pixabay' candidate.txt` — the pixabay line only, present in the original at the same position.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's twelve errors: the nine hotlink errors are the personal/sandbox-host references of sections 3–4 (in their pre-FIX-P4 form for the delivery lines), and the three pseudo-ref errors are the draft-host delivery lines — both standing classes, dispositioned (ii) as posting-procedure matters; there is no class (i) error. (2) The render row's items — page-overflow 513px at 320/375 on page and sample (plus 899px at 768 on the sample), sidebar-unreachable at 375/320 on both, the runtime-hotlink site-theme chain, and the candidate's sandbox/personal hosts — are recorded in RENDER-ROWS-G and dispositioned in the ledger's render entry for this theme (GOSIGN2-LEDGER L1220) as the posting-rewrite / original-state delivery class (KB-41/KB-54 family); the sample's credit-modal errors are the preview-form property (KB-32). (3) T4's charges are dispositioned by the ledger §(c5) line (header language = ruling 2; asset hosts = class (ii); credit fields FIXED), with the pattern-4 live-delivery item additionally repaired in fact by FIX-P4 (section 3) and the pattern-7 font item resting on the base layer's record (section 4). (4) The sources.tsv superseded note (per-theme record) carries no disposition; it is a provenance-table wording defect, flagged for central correction.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 248): exit 1, 12 errors / 0 warns / 1 info (hotlink ×9, pseudo-ref ×3), standing classes only. (b) T2/T3 render (RENDER-ROWS-G, lane RENDER-S2-G (CN18)): FINDINGS, the items of section 11(2), dispositioned in the ledger's render entry; chromium-only coverage; the T3 re-run recorded no new screenshot-grounded visual finding; the sample's credit-modal line is the preview-form property. (c) T4/T5 (LOCALIZE-ROWS row 247, lane LOCALIZE-S2-E): FINDINGS jointly, display-affecting findings 1 as the row records; the lane's per-pattern audit and theme verdict (REPORT-GOSIGN2-LOCALIZE-S2-E §CN18-2) itemize the pattern 4/5/7/11 sets behind that count. The T4 follow-up diff records rev9 → rev9, no change: the original has not moved since the reference revision, and no unincorporated update exists. (d) Post-T4 repairs: FIX-P4 (f1138e4) and FIX4-MECH (a497307), section 3; the sweep (b5cb724). FIX5 re-judgement: none. (e) This package's own checks: both copies hash-verified (Provenance table); a brace-depth scan of both files' CSS regions ends at depth 0 with no negative excursion (the original tail module's doubled closing brace at its end balances an earlier open, and the candidate's merged block preserves the balance); the hormress.github.io grep returns 0 in the candidate; the self-delivery census of section 3 was counted by hand; the base page's frame pair was read from its mirror (section 3). Counts in this README are the generator's (difflib): +377/−355 in 13 blocks; the GNU-diff count of the same pair is 734 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:yore-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 248; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### sources.tsv's "superseded upstream" note

sources.tsv's note for this row states that the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-yore-from9.txt` (kind K5a-i). The artifact itself records the opposite: "scp-wiki-cn:theme:yore rev9 → rev9 変更： なし", with an empty intervening-revision list, and the T4 report's follow-up section states the conclusion in words — the current original is at revision 9, the reference revision, and no update exists to incorporate. The mirror in this package is therefore current, not stale, and section 0's provenance is stated on that basis. The note's wording, not the mirror, is the defect; it is flagged here and in the batch report so the provenance table can be corrected centrally. The candidate is unaffected. (The same wording defect appears in theme:wish-for-miracle-jp's row in this batch, with the same artifact evidence.)

### No defect flag for this theme

For the record: this package raises no candidate defect flag for theme:yore-jp. The two waves that touched its delivery after the port (FIX-P4, FIX4-MECH) both repaired real items in it (section 3), the exhibit census is complete (section 8), the credit author is grounded in the theme's provenance (section 1), and every remaining standing item carries a ledger disposition (section 11). The display:none exhibit presentation (section 8) is the T4 lane's recorded observation, carried here as part of the theme's record; if a future wave normalizes exhibit presentation across the CN layered ports, this theme is one of the ones it would touch.

## Appendix — heuristic blocks by shape

The 3 heuristic blocks are the restructure's alignment artifacts, adjudicated where they belong: B4 (the documentation body region) in section 8, B12 (the post-code re-presentation) in section 8, and B13 (the tail exhibits region, TRANS-UNANCHORED) as the translated exhibits of sections 6 and 8. The 9 DELIVERY-MOVE labels ride the same moved CSS and are counted once, in section 3, not per block. No heuristic block conceals a deletion: each pairs against content the exhibit census of section 8 finds present.

## Change set outside the two diffed files

The diff covers the theme's own layer; the port's record is larger. The base candidate `pages/theme:parallel-jp.txt` carries the layer this theme imports and the frame design this theme stages (section 3); its changes are its own package's record, and the FIX-P4 fetch evidence for parallel-jp/1's merged-fragment status is cited in section 3. `pages/theme-decoration-sample-yore-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it carries no port change of its own to explain here.

## License and attribution

- **Title:** 往昔 版式
- **Author:** Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:yore — revision 9
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
