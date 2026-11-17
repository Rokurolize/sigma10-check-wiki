# Review package — theme:dustframe-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:dustframe-jp — origin CN, population #185 [GOSIGN2-LEDGER (b) row 185]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 185]
- T1 (source check): PASS — baseline 2026-11-16: exit 0, 0 errors / 1 warn / 1 info (no error codes) [T1-ROWS row 220; GOSIGN2-LEDGER (b) row 185]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 332px@320 + 387px@375 (page) and 337px@320 + 387px@375 (sample); sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-E (CN5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN5))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 185, source LOCALIZE-S2-D]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 185]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 185]
- Computed against: canonical commit 379eb44032d541453098c3177e0b1e3fc62c5964; candidate file pages/theme:dustframe-jp.txt sha256:8221e062f45516f4c7dd6c2a7224aa918b12b13852d4ad81708beaecfad74c55; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 185) |
| Standing items | **DISPOSITIONED** — the render row's two items only (page-overflow in the KB-33/KB-34 families; sample credit-modal preview-form, KB-32; section 11). T1 passed clean and T4/T5 passed with zero display-affecting findings, so this theme carries no source-check or localize dispositions |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:dustframe | theme:dustframe-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 7 (first translation; the candidate's credit block records 初訳時参照リビジョン: 7) | — |
| Source of this copy | Campaign cache `review-wave2-frozen/k2/orig-dustframe.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:dustframe-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 6,621 lines / 192,156 bytes | 6,620 lines / 199,268 bytes |
| SHA-256 | 9b144c10bb5a5a30fe9a2b06251773e797fc8e62edfff9b8a1e92b07a263a706 | 8221e062f45516f4c7dd6c2a7224aa918b12b13852d4ad81708beaecfad74c55 |

Wave history: the candidate was created by the Stage 2 CN5 integration (commit 04b38eb, the LOCALIZE-S2-D wave's port), then touched by 1869877 (FIX-CREDIT-D), by 8c62b7b (FIX4-IWA: the missing interwiki frame added, KB-07a — section 3), and last by 379eb44 (FIX4-MOPUP: KB-65 duplicate declarations left by the overlap clause removed; the verdict stamp is computed against this commit). Recorded drift: the original has been superseded upstream since rev 7; the campaign record carries the follow-up diff artifact `diff-dustframe-from7.txt` (sources.tsv K5a-i note), and this package documents the port against the rev-7 mirror it was made from.

## Summary

DustFrame （塵封） is the largest file in this batch: a Sigma-9 variant of the Wanderers' DustJacket theme whose CSS exists twice in the page, once as the live head module and once as the source exhibit that becomes its code page, and the port edits both copies in parallel. The edits themselves are few in kind: the font imports are rebuilt around a Japanese Mincho (the Chinese font CDNs and the DustJacket typeface bundle go, Zen Old Mincho comes in), every image asset moves from the Wanderers' Library file host to JP storage, the credit furniture becomes the JP preview block with the CN credit pair and the bare Rate deleted, the credit-area CSS selectors are corrected to the JP credit module's DOM in 30 places, the CSS comments and content strings are translated, and a delivery frame the original never had is added (FIX4-IWA). Because the same CSS appears twice, the differ's 190 blocks overstate the number of distinct decisions by roughly a factor of two; section 8 adjudicates the dominant DELIVERY-MOVE label on exactly that basis. Measured churn (diff.md, Tier 2 format, the generator's difflib count with autojunk off: +225/−226, 451 changed lines in 190 change blocks / 89 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 190 change blocks — 173 specific (91.1%), 15 heuristic (7.9%), 2 residue (1.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| ASSET-REHOST | 14 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 84 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 6 |
| CREDIT-PREVIEW | 2 |
| CREDIT-PROSE | 1 |
| DELIVERY-MOVE | 144 |
| DRAFT-HOST | 1 |
| FONT-IMPORT | 2 |
| GLYPH-FORM | 7 |
| HEADERVAR | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| LINK-REPOINT | 1 |
| SELECTOR-CORRECTION | 28 |
| SELF-DELIVERY | 1 |
| T7-CREDIT-CSS | 30 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 102 |
| TRANSLATION-ANCHORED | 25 |

Adjudication for this README (the block census was read against the bytes; the CSS mass was verified by shape and by spot pairs in both copies): the 114 DELIVERY-MOVE primaries are the differ pairing the two parallel CSS copies' edits (section 8), not content relocating — the theme's live module and exhibit both begin and end where the original's do. The 30 T7-CREDIT-CSS primaries are the credit-DOM selector corrections (section 1). The COMMENT-TEXT and TRANS-UNANCHORED mass is the expected CN-theme heuristic shape (CSS comment and prose translation), resolved by shape in sections 6 and 9's terms. The two residue blocks resolve in the appendix (the interwiki iframe repoint; a tail blank line). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:dustframe-jp; ancestor theme:dustframe on scp-wiki-cn at reference revision 7; candidate `pages/theme:dustframe-jp.txt`. Provenance route: derived from the ancestor at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame differs from the ancestor's in one deliberate way: the original has no interwiki frame at all — its live module is followed by a bare `====` separator (original L3164) and the tag gate `[[iftags +_版式框架]]` — while the candidate carries the standard frame, an `:scp-jp:component:interwiki-style` include at priority 1 delivering its own /1 from the draft host (candidate L3163–3166), added late by FIX4-IWA, and the localized gate `[[iftags +テーマ]]` (candidate L3168). The page's dual anatomy (live head module, candidate L1–3161; body and credit at L3168–3460; source exhibit at L3463 to the tail) mirrors the ancestor's exactly.
- **Why:** Section 0 declares the route so later counts are read against the right baseline; the gate's tag is P2, and the frame is P6/T3 with the KB-07a ground stated in section 3.
- **Verify:** The sources.tsv row for dustframe-jp; `sha256sum original.txt` against the Provenance table; the frame region at candidate L3161–3170 against original L3161–3170 in diff.md.
- **Disposition:** Standing (the route itself); the frame change is recorded in section 3.

### 1. Credit and attribution

- **What:** The ancestor's credit furniture is the CN credit-module pair (`:scp-wiki-cn:credit:start`/`end`, original L3289/L3295) with its prose, plus a bare `[[module Rate]]` in a right-aligned div immediately before it (original L3285–3287). The candidate deletes the bare Rate (block B77) and replaces the pair with the JP preview pair (blocks B78, B79: candidate L3287–3299) carrying the eight ruling-3 fields (title 塵封 Sigma-9テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 尘封 Sigma-9 版式； 著作権者 [[*user Mercuresphere]]; 作成年 2024; 初訳時参照リビジョン 7; the source link, candidate L3296, naming scp-wiki-cn.wikidot.com, the ancestor's recorded host) plus a ninth attribution field the theme's own record requires, ヘッダー画像 pointing at the header image's Pixabay source (candidate L3297). The T7 supplement takes in-CSS form here: the theme styles the credit area heavily, and 30 blocks across the two CSS copies correct its credit-area selectors and declarations to the JP credit module's DOM (T7-CREDIT-CSS primaries, most with SELECTOR-CORRECTION secondaries) — the supplement is selector correction inside the theme's own CSS rather than an added style block.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate and the foreign credit pair are replaced rather than duplicated (KB-09). T7 (KB-23) is the class the selector corrections discharge: production JP themes style the credit module's DOM, and a port whose credit CSS still targets the CN module's selectors leaves the module unstyled.
- **Verify:** `grep -n 'module Rate\|credit:' candidate.txt` — only the `:scp-jp:` preview pair returns; read candidate L3287–3299 against the fields; the T7 blocks are B29–B31, B44–B55, B146–B148, B161–B172 in classification.json, each present once per CSS copy.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified; the T7 corrections are part of the port as integrated and FIX4-verified).

### 2. Includes and components

- **What:** The candidate's includes are few: the frame (section 3), the credit pair (section 1), and the usage exhibit's escaped include, repointed `:scp-wiki-cn:theme:dustframe` → `theme:dustframe-jp` (block B85, candidate L3360). The interwiki iframe embed beside the credit block is repointed from the CN file host's styleFrame to the JP interwiki host (candidate L3283: `//interwiki.scp-jp.org/styleFrame.html?bhl`; appendix block B76). No component include changes were needed: the theme is self-contained CSS over the Sigma-9 base it assumes, on both sides.
- **Why:** P1 (KB-15) for the exhibit repoint: it names the JP counterpart that exists. The iframe is part of the interwiki frame machinery, so its host follows the frame's (T9).
- **Verify:** `grep -n '\[\[include\|iframe' candidate.txt` — the frame, the credit pair, the exhibit line, and the one iframe, all JP forms.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The theme delivers twice over, as the ancestor does: the live head module (candidate L1–3161) renders on the theme page and on pages that include it, and the source exhibit (candidate L3463 to the tail) is the page's /1 code block. Two changes matter. (a) The frame: FIX4-IWA (commit 8c62b7b, KB-07a — missing interwiki frames added to 31 themes) inserted the priority-1 frame delivering the candidate's own /1 from the draft host (block B73, candidate L3163–3166) where the ancestor has only its `====` separator; FIX4-MOPUP (commit 379eb44, KB-65) then removed duplicate declarations the overlap clause had left in this file, and the verdict stamp is computed against that final state. (b) The exhibit copy's import block is deleted (block B118: the ancestor's exhibit repeats all six @imports at original L3465–3471; the candidate's exhibit opens directly at its `#region MAIN`), so font loading is carried by the head module's import set alone (section 4) in both delivery paths' shared page.
- **Why:** P4/T3 for the frame: a Sigma-10 candidate's code page must be framable by the interwiki-style mechanism at a stated priority, which the ancestor's page never needed on its home wiki. KB-41 covers the draft-host form of the frame's `theme=` URL (class (iii), rewritten at posting). The exhibit import deletion is the same deduplication instinct as KB-65: the imports exist once, in the live module, instead of twice.
- **Verify:** Read candidate L3161–3166 (the frame) and L3463–3470 (the exhibit head, no imports) against original L3161–3165 and L3459–3472 in diff.md.
- **Disposition:** DISPOSITIONED (the frame's draft-host line, class (iii)); the frame addition and the deduplication are FIX4 changes recorded in the FIX4 reports and carried in the ledger's FIX5-era state.

### 4. Fonts and assets

- **What:** The head import set is rebuilt (block B1, live copy; the exhibit copy's is deleted, section 3). Out: the DustJacket typeface bundle (fastly.jsdelivr.net/gh/Crimone/wanderers-dustjacket-fonts), the 王汉宗 face (crimone.github.io/typefaces/whz/whz.css), and the 朱雀仿宋 face (chinese-fonts-cdn.deno.dev ZhuqueFangsong) — the three Chinese/fan font CDNs. In: Zen Old Mincho (Google Fonts, weights 400;700;900), the JP Mincho this port loads. Kept: Anonymous Pro, EB Garamond, and Recursive from Google Fonts, with their URLs' `&amp;` unescaped to `&`. The stacks follow: the ancestor's `"zuijinregular"` （醉金） stack entries become `'Zen Old Mincho'` in the candidate's `font-family` values; 'Nanum Gothic' is kept where the ancestor has it. Assets: every `url()` artwork reference moves from wanderers-library.wdfiles.com to scp-jp-storage.wdfiles.com under `file:` page folders (14 ASSET-REHOST label occurrences across both copies; e.g. --logo-image, candidate L17, and the goldfoil background, candidate L457). The rate-widget masks are inline SVG data URIs carried on both sides (candidate L2142–2145 and their exhibit twins); their `http://www.w3.org/2000/svg` strings are namespaces inside data URIs, not external references.
- **Why:** P7/T5 with KB-16: the ancestor's stacks name faces served from Chinese font CDNs that a JP page cannot rely on; the port loads a JP Mincho from Google Fonts and re-points the stacks at it, which is the font-stack rewrite shape. The asset move is the display-test rule (loadable Wikidot assets stored in JP-side storage with sources rewritten), applied to the base theme's file host. T4 recorded no font item for this theme and passed it, which is the checker's confirmation that the rebuilt set loads.
- **Verify:** Read candidate L9–12 against original L9–14; `grep -n 'wanderers-library\|jsdelivr\|crimone.github.io\|deno.dev' candidate.txt` returns nothing; `grep -n 'scp-jp-storage' candidate.txt` returns the re-hosted assets in both copies.
- **Disposition:** Standing (part of the port); no font or asset item dispositioned.

### 5. Header, sidebar, and site furniture

- **What:** The header variables are set in both CSS copies and change together: `--header-title: "放浪者の図書館"` (candidate L18), the Japanese form of the ancestor's 被放逐者之图书馆 (the Wanderers' Library name, translated); `--logo-image` re-hosted to JP storage (candidate L17, section 4); `--header-subtitle` is a blank string on both sides and does not change. Sidebar and header structure arrive from the Sigma-9 base the theme styles; this file's furniture content is the variables above.
- **Why:** Header text translation is P10 applied to furniture strings; no P9 item was recorded for this theme, because the header language was translated rather than kept. The logo move is T9 re-hosting (section 4).
- **Verify:** Read candidate L16–18 against original L18–20 (block B2) and its exhibit twin (block B119).
- **Disposition:** Standing (part of the port); no header item dispositioned.

### 6. Text translation

- **What:** Translation runs at three depths. Body prose: the usage and exhibit text is translated (TRANSLATION-ANCHORED 25 label occurrences; TRANS-UNANCHORED 102, the expected unanchored mass on a CN theme, verified by shape against the mirror for this README), with GLYPH-FORM corrections (7 label occurrences) normalizing simplified-Chinese glyph forms to Japanese forms where the translation carries characters over. In-CSS text (R1): the CSS comments are translated in both copies (COMMENT-TEXT 84 label occurrences — the ancestor annotates its CSS densely in Chinese, e.g. the iOS region note at candidate L3157), and the `content:` strings are translated (CONTENT-STRING 6; blocks B66–B68, B183–B185). Chinese survives reader-visible only in the credit block's 原題 field (candidate L3292). T5 passed this theme jointly with T4.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, which on this theme include its CSS comments and generated content). The glyph-form point is recorded because a translation that keeps simplified glyph forms renders the wrong characters in Japanese text; the classifier's GLYPH-FORM signature exists to catch exactly that carry-over.
- **Verify:** The pairs are diff.md's 89 sections in order; a simplified-Chinese-specific character scan of candidate.txt outside the exhibit comments returns the credit 原題 field.
- **Disposition:** Standing (the port itself); T4/T5 PASS with zero display-affecting findings (LOCALIZE-ROWS row 185).

### 7. Links

- **What:** One LINK-REPOINT block (B82, in the usage prose at candidate L3353–3354): a prose link repointed to its JP counterpart alongside its sentence's translation. The candidate's one attribution link is the credit source link (candidate L3296), naming scp-wiki-cn.wikidot.com — the ancestor's recorded host in review/sources.tsv — so the mis-hosted-link defect class does not occur and no probe was needed. The header-image attribution field (candidate L3297) names its Pixabay source page, an attribution record kept verbatim.
- **Why:** P11 under the dead-reference evidence standard: repoint what has a JP counterpart, keep attribution records as provenance data.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit source link is the only hit.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** The localize.md closing rule holds, and this section carries the batch's largest adjudication. The classifier's dominant label, DELIVERY-MOVE (144 label occurrences, 114 primaries), does not describe content moving: the candidate is one line shorter than the ancestor (6,620 against 6,621), its live module and exhibit occupy the same spans, and a census of the CSS regions shows every region of the ancestor present in the candidate in order, in both copies. What the label actually pairs is the port's parallel editing of the two copies — each font, asset, selector, comment, and content-string edit exists twice, and difflib's block pairing across two near-identical 3,000-line copies presents those twin edits as moves. The real structural facts are the three already recorded: the frame inserted (section 3), the exhibit's import block deleted (section 3), and the credit furniture replaced in place (section 1). Nothing else was dropped, merged, or reordered, so the R3 question does not arise.
- **Why:** R3 exists to force exactly this adjudication, because on a dual-copy file the differ's move label is the expected artifact of twin edits, and only a census distinguishes it from a genuine relocation or deletion.
- **Verify:** Compare region markers: `grep -n '#region\|#endregion' original.txt candidate.txt` — the sequences correspond; the line counts are in the Provenance table.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** No whitespace-only or re-indentation primary fired on this theme (0 and 0 in the primary census): the port's edits are dense enough that formatting seams were absorbed into their neighbouring blocks, and the one pure seam is the tail blank line in the appendix. The R7 follow-up-diff hazard is therefore not separately triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the honest statement is that the class is empty at block level.
- **Verify:** The primary census in classification.json shows no WS-ONLY or reindent primary.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. A comment scan of the candidate finds no porter-added comment, banner, or `[!-- --]` note: the CSS banner at the head of both copies (candidate L3–7) is the ancestor's own English banner, carried unchanged, and the exhibit's JP-port explanation that other themes carry in a banner is absent here — the layering and delivery facts for this theme live in the frame and in this package instead. This is stated as a positive check, not an omission: the annotation-ish comment grep over the candidate returns no hits.
- **Why:** R2: porter-added text is part of the change record; where there is none, the section says so on the evidence of the scan.
- **Verify:** `grep -n 'JP port\|ポーター\|移植' candidate.txt` returns nothing.
- **Disposition:** Standing; nothing to record.

### 11. Dispositions and exceptions

- **What:** Two items, both from the render row, each with its ground. (1) Page-overflow 332px@320 and 387px@375 on the theme page, 337px@320 and 387px@375 on the sample: the recorded cross-cutting families — the static credit replica's fixed width at mobile widths (KB-33) and preview chrome (KB-34) — with the register noting the per-theme figures match the campaign-wide shapes. (2) The sample credit-modal item: preview-form property (KB-32) — candidate and sample pages use `credit:start-preview`, which has no modal mechanism (GOSIGN-TESTS.md T2 note, 2026-11-16 ruling). There are no T1 items (the source check passed clean) and no T4 items (the localize check passed with zero display-affecting findings), so this section is shorter than most in the batch, on the records.
- **Why:** A disposition is a decision with grounds (the named KB entries), not an omission; the overflow and modal shapes are properties of the shared preview environment, recorded as not-charged to the candidate.
- **Verify:** Each item names its deciding record above; the render items are the ledger §(c2) block for this theme (RENDER-S2-E (CN5)).
- **Disposition:** DISPOSITIONED (both).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 220): PASS — exit 0, 0 errors / 1 warn / 1 info, no error codes; this theme is one of the batch's clean source checks. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN5)): FINDINGS, the two items of section 11, both dispositioned; engine coverage is the full matrix as run by the lane, not separately caveated in the row. (c) T4/T5 (LOCALIZE-ROWS row 185): PASS jointly, display-affecting findings 0. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +225/−226 in 190 change blocks / 89 diff sections (Tier 2 format).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:dustframe-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 185; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Two copies of one stylesheet, and what the diff does with them

A reviewer opening this package's diff.md cold sees 190 blocks and a dominant DELIVERY-MOVE label and could reasonably conclude the port rearranged the theme. It did not, and the reason is worth stating once, plainly: DustFrame's author ships the same CSS twice in one page (live module and code exhibit), the port edits both copies identically, and a line differ working on two near-identical 3,000-line copies pairs those twin edits in ways that read as movement. The distinct decisions in the port number about a dozen (imports, stacks, asset host, credit furniture, credit selectors, comments, content strings, frame, exhibit imports, header title), each appearing twice. The classification shares in this package (91.1% specific) are therefore computed over blocks, not decisions, and section 8's census is the evidence that the structure survived.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots.

| Block | Shape | Resolution |
|---|---|---|
| B76 (no signature) | Original L3280–3281 → candidate L3282–3283: the interwiki iframe embed beside the credit block, its src moving from the CN file host's styleFrame to `//interwiki.scp-jp.org/styleFrame.html?bhl` | The frame machinery's host repoint, adjudicated in section 2; the differ left it unlabeled because the line is raw HTML inside an embed |
| B190 (no signature) | Candidate L6618–6619: a blank line at the file tail with no counterpart at the ancestor's tail | Formatting seam at the exhibit's close (section 9) |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-dustframe-jp.txt` is the decoration sample the render checks ran against (its overflow and credit-modal items are section 11). One inbound dependency is recorded in another theme's T4 row: theme:paradigm-inapplicable-sigma-jp's row notes a P1 item for depending on this candidate (its own package carries that record; it is not an item against dustframe-jp). The follow-up diff artifact for the upstream drift since rev 7 (`diff-dustframe-from7.txt`) sits in the campaign record, outside this repo. There are no companion fragments for this theme.
