# Review package — theme:wish-for-miracle-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:wish-for-miracle-jp — origin CN, population #247 [GOSIGN2-LEDGER (b) row 247]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now c187a27d2a47fd07ff5a40a28fcd588f2b5dd78abc29d0de9b840300762cd9d6); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 9 errors / 0 warns / 1 info (hotlink×6, pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 247; GOSIGN2-LEDGER (b) row 247]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 579px@320/375 on page and sample + sidebar-unreachable at 375/320 on both pages + runtime-hotlink site-theme chain + candidate hosts cdn.jsdelivr.net, uploadfile.wdfiles.com, uploadfile.wikidot.com; sample carries NO credit-modal machine line and the report verdict likewise omits it (recorded as-is, unlike the other samples); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN18)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: no credit-modal line recorded — the row states the sample carries NO credit-modal machine line and the report verdict likewise omits it (recorded as-is, unlike the other samples) [RENDER-ROWS-G (CN18)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 246, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 246]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 247]
- Computed against: canonical commit 9b0eb99e5078fae699307945cd45d3f3566f6920; candidate file pages/theme:wish-for-miracle-jp.txt sha256:c187a27d2a47fd07ff5a40a28fcd588f2b5dd78abc29d0de9b840300762cd9d6; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 247) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×6 and pseudo-ref ×3 (class (ii), section 11); the render row's items (posting-rewrite class, KB-41/KB-54 family, section 11); T4's charges (ledger §(c5): header language = ruling 2; asset hosts = class (ii); credit fields FIXED by the credit waves). Two items are **flagged** in the per-theme record: the credit font field's blanket license claim, and sources.tsv's "superseded upstream" note, which its own cited artifact contradicts |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:wish-for-miracle | theme:wish-for-miracle-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 67 (first translation; the candidate's credit block records 初訳時参照リビジョン: 67) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-wish-for-miracle.txt`, via the mirror store `review-mirrors/orig-wish-for-miracle-rev67.txt` (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:wish-for-miracle-jp.txt`, copied at worktree HEAD 662baf3 |
| Lines / bytes | 1,009 lines / 35,173 bytes | 1,015 lines / 37,370 bytes |
| SHA-256 | 6a5bca1bc8a1da4ee8859e565605df2e6284c4275e8df63e1c43533129b362f5 | 1428a6f7f87c5bee53ea33bc2a29098d0d8cecb1e69614c24dfc3280f5477c3a |

Wave history: the candidate was created by the Stage 2 CN18 integration (commit 5b5dbe4) and has two later commits: f1138e4 (FIX-P4, the pattern-4 repoint of the base-layer CSS imports to the JP port candidates, section 3) and b5cb724 (the usage-example sweep, which put the self-references — including the one inside a CSS `content:` string, section 6 — into the -jp posting form). The verdict stamp reads STALE on the sweep commit alone. Provenance kind (sources.tsv): K5b-3 — the candidate layers over base candidates (theme:basalt-jp, theme:darkblue-jp), and this package's diff covers the theme's own layer only.

## Summary

A CN layered theme: a 758-line CSS layer of its own, written over Darkblue (itself a Bedrock-based theme), documented by a long interview-format body with usage exhibits and a font specimen. The candidate converts the delivery to the JP form — the tail module and frame move to the head, the own CSS stays a single `[[code]]` exhibit that is also code/1 — repoints the base imports to the JP port candidates (FIX-P4, after the T4 lane had charged them in their origin-host form), swaps the two SC font loads for JP loads and rewrites the two font stacks, keeps the theme's six image files on the CN file host under the class (ii) disposition, and translates the body throughout, including the one rendered CSS string. Measured churn (diff.md, the generator's difflib count: +162/−156 in 117 change blocks; a GNU-diff count of the same pair gives 318 changed lines). The heuristic share is high because a 758-line stylesheet's comment translations and one-line prose translations classify one line at a time; they are resolved in the appendix by shape. Two items are flagged in the per-theme record: the credit block's font field claims all eight fonts are SIL Open Font License, which is wrong for Special Elite (Apache License 2.0, confirmed for this package), and sources.tsv's note that the original was "superseded upstream" is contradicted by the follow-up diff artifact the note itself cites, which records no change since revision 67.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 117 change blocks — 70 specific (59.8%), 45 heuristic (38.5%), 2 residue (1.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COLON-ENC | 1 |
| COMMENT-TEXT | 24 |
| COMPONENT-SWAP | 2 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| FONT-IMPORT | 1 |
| GLYPH-FORM | 13 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 3 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 3 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 35 |
| TRANS-UNANCHORED | 57 |
| WS-ONLY | 12 |

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:wish-for-miracle-jp; original theme:wish-for-miracle on scp-wiki-cn at reference revision 67; candidate `pages/theme:wish-for-miracle-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN18 integration (sources.tsv kind: K5b-3, a layered port; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself moved: the original places its delivery after the gate (tail module, original L1000–1002; frame, L1004–1008); the candidate places both before the gate (candidate L1–8). One provenance record disagrees with its own evidence: sources.tsv's note says the original was "superseded upstream since the reference revision", but the follow-up artifact the note cites records rev67 → rev67, no change (per-theme record).
- **Why:** Section 0 declares the provenance route and the layering baseline: every count below is read against the theme's own layer only, the base layers being theme:basalt-jp's and theme:darkblue-jp's own records. The relocation is P4/T3 mechanics (section 3); the T4 lane recorded it as behaviorally equivalent (both forms apply unconditionally) while noting it departs from the preserve-the-original-ordering principle.
- **Verify:** The sources.tsv row for wish-for-miracle-jp; `sha256sum original.txt` against the Provenance table; the follow-up artifact `gosign2-lanes/lane-oc-gs-localize-s2-E/diff-wish-for-miracle-from67.txt`.
- **Disposition:** Standing (the route itself); the sources.tsv note is flagged in the per-theme record.

### 1. Credit and attribution

- **What:** The original's credit is the CN form: a `:scp-wiki-cn:credit:start`/`more`/`end` trio (original L3–11) whose inline content gives the title （祈冀 版式）, a version line (Release 1.0.0), and one maker ([[*User Kcorena]]), with the license line 授权协议：CC-BY-SA 4.0 International between `more` and `end`; the interview prose below names the second maker ([[user agent-fs]], original L32). The candidate replaces the trio with the JP form (candidate L14–24): `:scp-jp:credit:start-preview`/`end-preview` carrying the eight ruling-3 fields — title 祈冀テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 祈冀 版式； 著作権者 Kcorena、Agent FS (both makers, following the prose rather than the inline field's single name); 作成年 2025; 初訳時参照リビジョン 67; 元記事リンク https://scp-wiki-cn.wikidot.com/theme:wish-for-miracle, the host sources.tsv records (no probe needed: they agree) — plus a porter-authored 使用フォント field (candidate L23) listing this layer's eight font families and stating that the theme's images are the authors' work under the original's CC BY-SA 4.0. The version line has no field in the JP form and is not carried; the same conversion drops it in the exemplar ports. The bare `[[module Rate]]` (original L15) is deleted. The section's CSS half: the theme styles the CN credit module through its own variables and rules (original L313–320, L599), and the candidate carries them unchanged apart from whitespace (candidate L329–336, L615) — the classifier's T7-CREDIT-CSS primary on the L615 block does not survive the bytes, because the rule is present in the original at L599; it is inherited, not a T7 supplement, and its only change is a trimmed trailing space (section 9).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09), and the CN credit trio is ledger class C furniture, not JP form. Ruling 3 fixes the eight fields. The font field's blanket license claim is the one inaccuracy in the block (per-theme record).
- **Verify:** `grep -n 'credit:start\|module Rate' candidate.txt` — only the preview pair; read candidate L14–24 against the eight fields and original L3–11, L32.
- **Disposition:** FIXED for the fields (GOSIGN2-LEDGER §(c5): credit fields FIXED by the credit waves). The font field's license claim is flagged in the per-theme record, not dispositioned.

### 2. Includes and components

- **What:** The gate's tag is localized, +版式 → +テーマ (original L1 → candidate L12). The usage exhibit's include is repointed (B14): `:scp-wiki-cn:theme:wish-for-miracle` → `:scp-jp:theme:wish-for-miracle-jp`, in the -jp posting form after the sweep. The theme-squares exhibit include is repointed (B25): `:scp-wiki:component:theme-squares` → `:scp-jp:component:theme-squares` — the classifier's EXHIBIT-RESTRUCTURE primary on this block is a false fire; the exhibit's parameters, position, and content are unchanged apart from the repoint and translation. The image-block include stays in the plain form on both sides (its `name=` is section 4). One include is added (residue block B3, adjudicated here): `[[include component:betterfootnotes]]` (candidate L10). The original's body uses `[[footnote]]` exhibits and a `[[footnoteblock]]` (original L106, L139, L163) and its CSS styles the footnote block's variables; the JP environment serves footnotes through this component, and the candidate's one extra footnote mention over the original (8 against 7) is exactly this line.
- **Why:** P1 (KB-15) for the repoints; P2/KB-08 for the gate tag; the footnote component is the environment-adaptation supplement that makes the carried exhibits render in the JP environment.
- **Verify:** `grep -n '\[\[include' candidate.txt` — eight hits: seven includes (frame, footnote component, credit pair, usage exhibit, theme-squares, image-block), all `:scp-jp:` or plain JP components, plus the `content:` string of section 6; the footnote exhibits are at candidate L113, L146, L170 (the original's positions, translated).
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery relocates from tail to head, ungated on both sides. The candidate opens with a `[[module CSS]]` importing its own `local--code/theme%3Awish-for-miracle-jp/1` from the draft host (candidate L1–3, block B1), then the interwiki-style frame in the JP form (`:scp-jp:component:interwiki-style`, priority 1, `theme=` the same /1, candidate L5–8, block B2). Self-delivery census: the candidate has exactly one `[[code]]` block (candidate L254–1011, inside its collapsible), so /1 names the block that holds the CSS. The frame's parameters changed against the original's (original L1004–1008: priority=2, `type=sidebar`): the T4 lane's audit records that the JP component's accepted arguments are priority and theme only, accepts the priority-1 self-naming frame, and marks the dropped `type=` as correct — that record dispositions the change. Inside code/1, the layer imports sit at the block's head (candidate L256–257): the original's basalt normalize file (`cdn.scpwiki.com/theme/en/basalt/normalize-min.css`, original L240) now imports `theme%3Abasalt-jp/1` from the draft host, and the original's Darkblue code (`scp-wiki-cn.wdfiles.com/local--code/theme%3Adarkblue/1`, original L241) now imports `theme%3Adarkblue-jp/1`. At T4 time both lines still named the origin hosts and were charged MISSED (exhibit-counted); FIX-P4 (commit f1138e4) is the repair, and its report records the fetched same-role evidence: darkblue-jp/1 was fetched and confirmed the same role (the JP port of the same theme, self-contained with its own basalt-normalize file), and basalt-jp/1 is the Basalt port's delivery fragment, which itself opens with the same normalize import the original named directly.
- **Why:** P4/T9 (base and own delivery served from the JP side) with the FIX-P4 pattern-4 mapping; P6/T3 for the frame. The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L2 and L7 live (own /1), L256–257 the base layers; the FIX-P4 report's A41/C1 entries carry the before/after checker states.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the base repoints are FIXED by FIX-P4 with fetched evidence, not merely dispositioned.

### 4. Fonts and assets

- **What:** Loads (all inside code/1's head): six @import lines. Two families change host — Special Elite and Playfair Display move from `api.fonts.coollabs.io` to `fonts.googleapis.com` (B76, candidate L259–260), the canonical Google Fonts host, in the same css2 grammar as the file's retained Google imports; the T4 lane verified the replacement as correctly made. Two loads change family — Noto Serif SC → Noto Serif JP (weights 100–900 unchanged) and Noto Sans SC → Noto Sans JP (B77, candidate L262–263). ZCOOL XiaoWei is kept on Google Fonts (candidate L261): it is the logotype face for the 祈冀 wordmark role and has no JP counterpart. The Archivo / IBM Plex Sans / Source Code Pro bundle is kept (candidate L264). Stacks (B78, B79 — CSS-BODY primaries, adjudicated here as the P7 rewrites they are): `--UI-font-primary` "Noto Sans SC" → "Noto Sans JP" (candidate L267), and `--header-font` becomes "Noto Serif JP", "ZCOOL XiaoWei", serif (candidate L269) — the porter prepends the JP serif and changes the generic fallback to match, a design judgment recorded here; every font-family property in the layer uses these two variables (seven lines, both files), and every family named in them is loaded by the lines above or kept deliberately (ZCOOL). One documentation claim rides on the base layer: the font specimen names JetBrains Mono as the monospace face (candidate L238), which this layer does not load — the darkblue-jp base does (its own @import and `--mono-font`), so the claim, inherited from the original (original L230), is satisfied through the base delivery rather than by this layer; the credit font field lists only this layer's loads. Assets: six file URLs on `uploadfile.wikidot.com/local--files/theme%3Awish-for-miracle/` are kept on the CN file host — the title image in the image-block `name=` (candidate L106) and the five header backgrounds inside the CSS (candidate L415–419) — byte-identical to the original's set except that the title image's path colon is encoded (`theme:wish-for-miracle` → `theme%3Awish-for-miracle`, B27), the same file under the canonical wdfiles encoding. The `--header-logo` and `--heading-mask` values (candidate L279, L380) are inline SVG data URIs, carried; the classifier's HTTP-KEPT presence lines for this package are the W3C namespace strings inside those two URIs, not an http residue.
- **Why:** P7 (JP glyph coverage: the SC faces render Japanese text in mainland forms, so load and stacks change together) with KB-16; KB-04 for the font-host grammar. P5 for the assets: the T4 lane charged the un-rehosted set MISSED, and the ledger dispositions asset hosts as class (ii) — the files are re-hosted to JP storage at posting.
- **Verify:** `grep -n '@import' candidate.txt` (six lines, L256–264) against original L240–248; `grep -n 'uploadfile' candidate.txt` (six lines, L106, L415–419).
- **Disposition:** Font loads and stacks applied. Assets DISPOSITIONED (class (ii); GOSIGN2-LEDGER §(c5): asset hosts = class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** No header-variable item arises: neither file sets `--header-title`, `--header-subtitle`, or `--logo-image` (the T4 audit's §9 confirms the same census). The header logo is an inline SVG mask (the `--header-logo` data URI, section 4), and the SVG is path drawing with no text element, so there is no header string to localize. The theme's sidebar and furniture rules ride inside the carried CSS; the T4 structure note records variable names and selector order identical to the original's apart from the items in sections 3–4.
- **Why:** P9/T6 ground: the furniture is inherited CSS over the base layers, and no JP furniture adaptation was needed or made.
- **Verify:** `grep -n -- '--header-' candidate.txt` — the mask/logo variables only, no title strings.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The interview body, the usage prose, and every exhibit are translated (35 TRANSLATION-ANCHORED blocks; the balance of the prose rides in the TRANS-UNANCHORED group below). The one rendered CSS string is translated and repointed (B82): `content: "请使用 [[include :scp-wiki-cn:theme:wish-for-miracle]] 引用此版式。"` → `content: "[[include :scp-jp:theme:wish-for-miracle-jp]]でこのテーマを読み込んでください。"` (original L384 → candidate L400); at T4 time the string still named the non--jp form, and the sweep (b5cb724) is the commit that repaired it. The code exhibit's collapsible label is translated （源代码 → ソースコード, candidate L253). GLYPH-FORM (13 blocks) is the glyph-only half of the translation: simplified forms take Japanese glyph forms where the word is retained （示例 → 例 in a sample heading; the CSS comments' 设置 → 設定）. What remains untranslated is quotation: the credit block's original-title field and the 祈冀 wordmark in the header stack's design role.
- **Why:** P10 (KB-18: reader-visible strings, including `content:` strings) and R5 (glyph-form conversion is a language change, not a formatting one). The content string matters beyond prose: it instructs readers to paste the include, so its target is judged like an exhibit include (section 2).
- **Verify:** The pairs are diff.md's body sections in order; a simplified-Chinese scan of candidate.txt outside the credit quotation returns nothing in this package's read-through.
- **Disposition:** Standing (the port itself); T5 judged the translation jointly with T4 (section 12).

### 7. Links

- **What:** The interview paragraph's relative theme links are expanded to absolute origin URLs (candidate L40): Bedrock → `https://scp-wiki.wikidot.com/theme:bedrock`, Darkblue / Oceanbound / Lampeter Warm → `https://scp-wiki-cn.wikidot.com/theme:...`, and the 祈冀 tag-page link stays on scp-wiki-cn. Both bedrock hosts were probed for this package (2026-11-17): scp-wiki serves "Bedrock Theme" and scp-wiki-cn serves its CN posting of the same theme, so the EN choice is a live link to the theme's original posting, not a dead host. The link-style exhibit is adapted, not repointed at a real page (B38): its visited-link example now names `https://scp-jp.wikidot.com/`. The credit source link is section 1 (host agrees with sources.tsv). No prose link names a JP counterpart page, because none exists for these targets.
- **Why:** P11 under the dead-reference evidence standard: where no JP page exists, the explicit origin URL is the correct form (the T4 lane's note on this paragraph's link set), and a same-site relative form would resolve to a nonexistent scp-jp page.
- **Verify:** Read candidate L40 against original L32; the two bedrock URLs above are the probe pair.
- **Disposition:** Standing; the T4 lane's P11 charge on the tag-page link is among the row charges the ledger §(c5) dispositions.

### 8. Structure

- **What:** Ordering is preserved apart from the delivery relocation of section 3: gate, credit, interview body, exhibits, code exhibit in its collapsible (present on both sides; original L237, candidate L253), then the gate's close and the hidden `-override-warning` anchor, which is the last line of both files, byte-identical. Exhibit census: the interview, the usage exhibit, the theme-squares exhibit, the image-block, the footnote exhibits, and the font specimen are present on both sides in the same order. The two EXHIBIT-RESTRUCTURE primaries adjudicate away from restructuring: B25 is section 2's include repoint, and B117 is the tail delivery relocation (section 3). Residue block B73 adjudicates here: the `++ 代码` heading over the code exhibit is not dropped — the candidate carries it as `++ コード` (candidate L245), separated from the collapsible by a run of added blank lines (candidate L246–252) that the classifier's alignment read as a deletion.
- **Why:** R3: a restructure and a deletion share a diff shape and ledger class I charges the silent form; the census, not the label, decides, and the census is complete.
- **Verify:** Compare the section sequences of the two files (headers and exhibit markers in order); read candidate L242–254 against original L234–238.
- **Disposition:** Standing; no structural deletion, no class I item. The relocation itself is recorded in section 3 with the T4 lane's equivalence note.

### 9. Formatting only

- **What:** Twelve WS-ONLY blocks, all trailing-space trims inside the CSS (one is the credit-back rule line of section 1), plus the blank-line run before the code exhibit (section 8). The classifier finds 0 re-indentation pairs. No WS-only block touches a selector, a value, or a string.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** classification.json's WS-ONLY block list against diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no banner line, port comment, or annotation text: the code block opens directly with its @import lines, as the original's does, and a grep for port/annotation markers in candidate.txt returns nothing. The porter-authored texts that do exist are the credit block's font field (section 1) and the translated prose (section 6), neither of which is an annotation. The skeleton's silence on this section happens to survive the bytes, and the ground is stated here so the "none" is a checked result, not a default.
- **Why:** R2: porter-added text is part of the change record; its absence is recorded with the check that establishes it.
- **Verify:** `grep -n 'Ported\|移植メモ\|porter' candidate.txt` — no hits.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's nine errors: the six hotlink errors are the uploadfile asset lines of section 4, and the three pseudo-ref errors are the draft-host delivery lines of section 3 — both standing classes, dispositioned (ii) as posting-procedure matters (re-hosting and host rewrite at posting); there is no class (i) error. (2) The render row's items — page-overflow 579px at 320/375 on page and sample, sidebar-unreachable at 375/320 on both, the runtime-hotlink site-theme chain, and the candidate's foreign delivery hosts — are all recorded [DISPOSITIONED] in the ledger's render entry for this theme: the posting-time rewrite / original-state delivery class (T1 class (ii); KB-41/KB-54 family), with the note that the pages render styled today and no error-box defect arises from these hosts. The sample's missing credit-modal machine line is likewise dispositioned there as the preview-form property (KB-32). (3) T4's charges (the exhibit base imports in origin-host form, the asset set, the tag-page link) are dispositioned by the ledger §(c5) line — header language = ruling 2; asset hosts = class (ii); credit fields FIXED — with the base-import item additionally repaired in fact by FIX-P4 (section 3). (4) The two flagged items of the per-theme record (the credit font field's license claim; the sources.tsv superseded note) carry no disposition in any record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged, and undispositioned items are flagged rather than absorbed.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 247): exit 1, 9 errors / 0 warns / 1 info (hotlink ×6, pseudo-ref ×3), standing classes only. (b) T2/T3 render (RENDER-ROWS-G, lane RENDER-S2-G (CN18)): FINDINGS, the items of section 11(2), all dispositioned in the ledger's render entry (GOSIGN2-LEDGER L1215); chromium-only coverage; the T3 re-run recorded no new screenshot-grounded visual finding. (c) T4/T5 (LOCALIZE-ROWS row 246, lane LOCALIZE-S2-E): FINDINGS jointly, display-affecting findings 1 (the live image-block hotlink, pattern 5(a)); the lane's per-pattern audit is REPORT-GOSIGN2-LOCALIZE-S2-E §CN18-1. The T4 follow-up diff records rev67 → rev67, no change: the original has not moved since the reference revision, and no unincorporated update exists. (d) Post-T4 repairs: FIX-P4 (f1138e4, section 3) and the sweep (b5cb724, section 6). FIX5 re-judgement: none. (e) This package's own checks: both copies hash-verified (Provenance table); a brace-depth scan of both files' CSS regions ends at depth 0 with no negative excursion; the self-delivery census of section 3 was counted by hand; the bedrock probe pair and the Special Elite license confirmation are recorded in sections 7 and the per-theme record. Counts in this README are the generator's (difflib): +162/−156 in 117 blocks; the GNU-diff count of the same pair is 318 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:wish-for-miracle-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 247; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The credit font field's license claim (candidate L23)

The credit block's porter-authored font field lists this layer's eight families and closes with the blanket claim that all are distributed under the SIL Open Font License (いずれも SIL Open Font License). For seven of them that holds. For Special Elite it does not: the family is Astigmatic's, and the google/fonts repository carries it in its Apache License 2.0 folder; the font's own copyright record reads "Copyright (c) 2010 by Brian J. Bonislawsky DBA Astigmatic (AOETI)… Available under the Apache 2.0 licence" (confirmed for this package, 2026-11-17, from the repository's license-folder census and the embedded notice). The T4 lane raised exactly this item as unconfirmed （要確認） in its §3 note; it was never resolved in the record, and the claim still stands in the candidate's bytes. The practical stakes are small — Apache 2.0 is a permissive license and the theme only links the Google Fonts stylesheet — but the credit block is the package's attribution record, and a license claim in it should be right. Flagged with the evidence; the candidate is not edited here. The repair is one clause: name Special Elite's license separately, or drop the blanket claim to "Google Fonts 配信" alone.

That one-clause repair has since landed — FIX-XMAS, canonical commit `9b0eb99e5078fae699307945cd45d3f3566f6920` ("pages: xmas delivery slots restored, wish-for-miracle license clause", 2026-11-17; report `R/review-scout/FIX-XMAS.md`, item 2). On the current candidate the font field at L23 now reads "Special Elite は Apache License 2.0、その他はいずれも SIL Open Font License" between the two parentheses, excepting Special Elite from the blanket OFL claim while leaving the rest of the line unchanged. The checker's finding set was unchanged. This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:wish-for-miracle-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

### sources.tsv's "superseded upstream" note

sources.tsv's note for this row states that the original was "superseded upstream since the reference revision" and cites the follow-up artifact `diff-wish-for-miracle-from67.txt` (kind K5a-i). The artifact itself records the opposite: "scp-wiki-cn:theme:wish-for-miracle rev67 → rev67 変更： なし", with an empty intervening-revision list, and the T4 report's follow-up section concludes the same (current revision equals the reference revision; no update exists to incorporate). The mirror in this package is therefore current, not stale, and section 0's provenance is stated on that basis. The note's wording, not the mirror, is the defect; it is flagged here and in the batch report so the provenance table can be corrected centrally. The candidate is unaffected.

## Appendix — heuristic and residue blocks by shape

The 45 heuristic and 2 residue blocks resolve by shape, not line by line. COMMENT-TEXT (24 blocks) and the CSS-comment half of TRANS-UNANCHORED are one-line comment translations inside the stylesheet (e.g. `/* Main Content设置 */` → `/* Main Content設定 */`, which also carries its GLYPH-FORM conversion), porter-visible only and rendered nowhere. The prose half of TRANS-UNANCHORED (with TRANSLATION-ANCHORED, 35 blocks) is the interview body and exhibit text of section 6, verified against the mirror in this package's read-through. GLYPH-FORM (13) rides those two groups and is counted in section 6. WS-ONLY (12) is section 9. Residue B3 (the betterfootnotes include) is adjudicated in section 2 and residue B73 (the code heading) in section 8. No heuristic or residue block conceals a deletion: every one pairs a removed line with its translated or repointed counterpart at the position the census of section 8 predicts.

## Change set outside the two diffed files

The diff covers the theme's own layer; the port's record is larger. The base candidates `pages/theme:basalt-jp.txt` and `pages/theme:darkblue-jp.txt` carry the layers this theme imports (section 3); their changes are their own packages' records, and the FIX-P4 fetch evidence for darkblue-jp/1's same-role status is cited in section 3. `pages/theme-decoration-sample-wish-for-miracle-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it carries no port change of its own to explain here.

## License and attribution

- **Title:** 祈冀 版式
- **Author:** Kcorena、Agent FS
- **Source:** https://scp-wiki-cn.wikidot.com/theme:wish-for-miracle — revision 67
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
