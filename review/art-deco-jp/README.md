# Review package — theme:art-deco-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:art-deco-jp — origin EN, population #58 [GOSIGN2-LEDGER (b) row 58]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now b184b23d97f665d368d6d31d770756916f66eeae1901961355e074d161843c80); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): PASS — baseline 2026-11-16: exit 0, 0 errors / 1 warn / 1 info (no error codes) [T1-ROWS row 58; GOSIGN2-LEDGER (b) row 58]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — malformed Google Fonts `@import` URLs (fonts never load, HTTP 400/ORB, §3) + gold-frame×default-header collisions at PC and 320. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 58, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 58]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 58]
- Computed against: canonical commit 5d951775998e4a1eeccf8e8695a6518b328962ee; candidate file pages/theme:art-deco-jp.txt sha256:b184b23d97f665d368d6d31d770756916f66eeae1901961355e074d161843c80; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 58) |
| Standing items | **DISPOSITIONED** — T1 is clean for this theme (exit 0, no errors); the render row's items (the malformed font imports, since repaired and re-probed; the gold-frame/header collisions) are recorded under their classes below |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:art-deco | theme:art-deco-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 4 (first translation; the candidate's credit block records 初訳時参照リビジョン: 4) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-art-deco.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:art-deco-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 864 lines / 22,295 bytes | 834 lines / 21,527 bytes |
| SHA-256 | bca3634ca8e5a752a91743119b10252f3ee138bff603f135ac55e17b60ec1b56 | f841d0b31ddaa76ace8859db848c9a5cb09cadf1a051759e41db36495182b321 |

Wave history: the candidate was created by the Stage 2 EN batch 1 port (3205f27, 2026-11-15) already missing its base include (the port's one real defect, section 2). Two waves then edited it: FIX-CREDIT-D (1869877, 2026-11-17), which under a translator-normalization title restored the dropped base, corrected the false foundation line, added the frame, and made the JP font insertions; and FIX4-LICENSE (c2a8bee, 2026-11-17), which repaired the malformed Google Fonts imports and restored the license-box furniture (per-theme record). No FIX5 commit touches this file.

## Summary

A 2026 deco theme whose port is byte-close in its CSS (the code body moves into the module at 0.99 similarity) and eventful in its furniture. The port silently dropped the theme's declared base — the original is a Sigma Plus theme, and the candidate shipped with no base include and a foundation line falsely claiming 単体 (standalone). T4 caught it; the wave record (§(c4)) adjudicated it; FIX-CREDIT-D landed the restoration and the corrected line. Separately, the theme's three Google Fonts imports were malformed in the original's own URL grammar (`family=poiret-one:400` and its siblings), a defect the port carried over verbatim until FIX4-LICENSE repaired the grammar, live-probed 400 → 200. Measured churn is small (diff.md, the generator's count: +42/−71, 4 hunks, 16 change blocks) because the body exhibits, like alcur's, are not carried into the candidate (section 8).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 16 change blocks — 13 specific (81.2%), 3 heuristic (18.8%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 5 |
| EXHIBIT-RESTRUCTURE | 4 |
| TRANS-UNANCHORED | 4 |
| SIGMA-PLUS-JP | 3 |
| LICENSE-BOX | 2 |
| WS-ONLY | 1 |

Adjudication for this README: the 5 DELIVERY-MOVE blocks are the code→module relocation (section 3); the 3 SIGMA-PLUS-JP blocks are the restored base include, the corrected foundation line, and the frame region they arrived with (sections 2–3); the 4 EXHIBIT-RESTRUCTURE blocks and all 3 heuristic blocks (B5, B6, B9) adjudicate together in section 8 — they are the body region's replacement, and the classifier's per-block calls there are superseded by the census given in that section. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:art-deco-jp; original theme:art-deco on scp-wiki at reference revision 4; candidate `pages/theme:art-deco-jp.txt`. Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; no production JP counterpart exists, so R4 does not arise). The frame: the original has no interwiki-style frame at all (it opens with the gate and the bare Rate); the candidate opens with the base include, the JP frame (candidate L3–6), the gate, and the credit block.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the base include's history is this package's central event (section 2).
- **Verify:** The sources.tsv row for art-deco-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's only credit furniture is the bare `[[module rate]]` (original L4); it has no credit block and no license box. The candidate deletes the bare Rate and installs the JP forms: the `:scp-jp:credit:start-preview`/`end-preview` block (candidate L10–19) with the eight ruling-3 fields （タイトル: アール・デコ・テーマ; 翻訳責任者: AI; 翻訳年: 2026; 原題: Art Deco Theme; 著作権者: Fish^12; 作成年: 2026; 初訳時参照リビジョン: 4; 元記事リンク: the scp-wiki original), the author and year matching the CSS banner ("Art Deco Theme / [2026 Wikidot Theme] / by Fish^12", candidate L29–33); and the license-box furniture at the tail (candidate L830–832: `:scp-jp:component:license-box-backend`, the `=====` separator, `:scp-jp:component:license-box-end`), restored by FIX4-LICENSE in the campaign's standard form with no file entries — the theme declares no separately-authored files (its one body image is an exhibit asset on the original's host, section 8), so the box renders the standard frame alone. There is no T7 credit-module CSS: the theme never styled the credit module and no supplement adds any.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields. The license furniture's restoration belongs to the FIX4-LICENSE wave's population form (the license-box set, KB-04's wave); an empty entry list is the bytes' fact, stated rather than padded.
- **Verify:** `grep -n 'module rate' candidate.txt` returns nothing; read candidate L10–19 against the eight fields and L830–832 for the furniture.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): credit fields FIXED by the credit waves, checker-verified; the furniture by FIX4-LICENSE).

### 2. Includes and components

- **What:** This section carries the theme's defining event. The original declares itself a Sigma Plus theme in its body prose (original L11: "This theme is a Sigma Plus theme and uses the Toggle Sidebar Component", with links to both component pages) — note the declaration is prose, not an include: the original page itself carries no sigma-plus include line, its base arriving by the EN composition's own route. The port dropped the base entirely: no include, and its foundation line claimed 単体 (standalone). T4's row charged exactly this (pattern 1 family: base dependency silently dropped; the JP `component:sigma-plus-jp` existed but was unused; toggle-sidebar had no JP equivalent; and 基盤： 単体 was false). The restoration, landed by FIX-CREDIT-D and adjudicated in the campaign record (GOSIGN2-LEDGER §(c4): "the silently dropped sigma-plus base was restored and its false foundation line corrected (FIX3-S2EN §5)"): `[[include component:sigma-plus-jp]]` at the candidate's head (candidate L1), and the foundation line corrected to 基盤: Sigma+（component:sigma-plus-jp 経由） (candidate L25). The toggle-sidebar half of the charge stands as T4 recorded it: no JP equivalent exists, no include was or could be restored, and the candidate carries no note about it — the fact is recorded here in its place. The remaining includes are the frame and the credit/license furniture (sections 1, 3).
- **Why:** P1 (KB-15) in its sharpest form: a theme whose declared base is silently absent renders without its foundation — the failure is not a 404 but a quietly wrong page, which is why T4 counted it display-affecting and why the false 単体 line mattered as much as the missing include (a reviewer trusting the line would never look for the base). The toggle-sidebar ground is existence: a component with no JP port cannot be included, and ruling 4 is not engaged (nothing foreign is kept live).
- **Verify:** `grep -n 'sigma-plus' candidate.txt` — the include (L1) and the foundation line (L25); `grep -n 'toggle' candidate.txt` returns nothing; `pages/component:sigma-plus-jp.txt` exists in this repo.
- **Disposition:** FIXED for the base (restored, §(c4) per-theme note; the landing commit is FIX-CREDIT-D 1869877 — the §(c4) text credits the FIX3-S2EN §5 adjudication record, and the bytes' landing is the credit-wave commit, a record-vs-landing distinction this package states rather than smooths over); the toggle-sidebar absence stands as recorded, ground: no JP equivalent exists.

### 3. Delivery and code loading

- **What:** The original delivers its CSS from a `[[code]]` block inside a "Theme Source" collapsible in its body (original L48–847) plus a small tail module (original L857–860), with no frame and no self-import. The candidate delivers by the JP interwiki-style frame naming its own `local--code/theme%3Aart-deco-jp/1` on the draft host (candidate L3–6), the CSS inline in a single `[[module CSS]]` (candidate L26–828) — the classifier's topology pass matches the moved body at 0.99 similarity — and the sigma-plus base by its component include (section 2). The frame is a wave addition (FIX-CREDIT-D): the port shipped without one, the same pattern-6 absence the sibling themes' waves repaired.
- **Why:** P6/T3 (the frame is the environment's delivery contract; priority 1 is the theme's own layer — the sigma-plus base is a component include, not a code-delivered layer, so it does not take a priority number). P4/T9 for the /1 address's host (draft host at draft stage, KB-41 class (iii)).
- **Verify:** `grep -n 'local--code' candidate.txt` — the frame's theme= line only; `grep -n '\[\[module\|\[\[code' candidate.txt` — one module, no code block.
- **Disposition:** Applied (the frame by FIX-CREDIT-D); the draft-host form is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** The theme's three display faces load by `@import` at the module's head (candidate L35–37: Poiret One, Andada Pro, Roboto Flex), and their URL grammar is this theme's second defect story: the original's imports read `family=poiret-one:400`, `family=andada-pro:400`, `family=roboto-flex:400` — kebab-case family names the css (v1) API rejects, so the fonts never loaded (the render lane probed HTTP 400). The port carried the malformed URLs over verbatim; FIX4-LICENSE repaired the grammar to `family=Poiret+One:400` and its siblings, live-probed 400 → 200 (the KB-04 set: lumina, art-deco, oceanbound). The JP face arrived in the other wave: FIX-CREDIT-D added the Noto Sans JP `@import` (candidate L38) and appended `"Noto Sans JP"` to the theme's three font variables (`--poir`, `--anda`, `--robo` — the stacks the body's font-sample spans name). Assets: the theme references no local--files URLs in its CSS; its one body image (the exhibits' black.webp) is treated in section 8. T1 reports no hotlink for this theme.
- **Why:** KB-04 (malformed font URL grammar; the failure is silent — CSS `@import` failure leaves fallback fonts with no error surface, so only the probe decides). P7/KB-16 for the JP load and stacks (the Latin display faces cannot render Japanese; the variables are where the stacks live in this theme, so the insertions land there).
- **Verify:** Read candidate L35–38; `grep -n -- '--poir\|--anda\|--robo' candidate.txt` shows the three variables carrying Noto Sans JP.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c2): KB-04 set FIXED by FIX4-LICENSE with the live probe recorded; the JP font work by FIX-CREDIT-D).

### 5. Header, sidebar, and site furniture

- **What:** No P9 variable override: the theme sets no `--header-title`/`--header-subtitle`/`--logo-image`; its gold-frame header furniture is CSS in the carried-over body. The original's body heading "+ THE GOLDEN AGE WILL RETURN AGAIN" (original L7) is an English slogan line in the body prose, not a header variable; it was not carried into the candidate (the body replacement of section 8), so no header-language item stands in the candidate at all. The render row's collision items (the gold frame overlapping the default header at PC width and at 320) are the theme's own frame geometry meeting the environment's default header, recorded in section 11.
- **Why:** KB-18 and ruling 2 govern header language; here the bytes make the question moot for the candidate, and the package says so rather than inventing an item. The collision family is a render-side observation about the theme's design against the default header, not a port edit.
- **Verify:** `grep -n 'header-title\|header-subtitle\|logo-image' candidate.txt` returns nothing.
- **Disposition:** No item stands (ground stated); the collisions are DISPOSITIONED in section 11.

### 6. Text translation

- **What:** The candidate's body text is the campaign's three standard lines (porter intro, usage, base note; candidate L21–25), and the original's body prose is not translated into it: the GOLDEN AGE heading, the Machina tale series paragraph (original L9), and the Sigma Plus / Toggle Sidebar paragraph (original L11) have no translated counterparts in the candidate. The 4 TRANS-UNANCHORED blocks are these lines and the head furniture. Inside the CSS, the banner comment stands in English on both sides (the original's attribution record), and there are no reader-visible prose strings in the CSS body to translate.
- **Why:** The prose's fate is adjudicated as structure in section 8 (the body replacement), with one exception carved out here: the Sigma Plus paragraph was load-bearing prose — it declared the base — and its informational content survives in corrected form as the foundation line (section 2), which is where a user of the candidate learns the dependency. The Machina paragraph is series context with no JP counterpart page named in any campaign record.
- **Verify:** Read candidate L21–25 against original L7–17.
- **Disposition:** Standing (the port itself), under the section 8 adjudication.

### 7. Links

- **What:** The candidate's one live outbound prose link is the credit block's source link (candidate L18), naming `https://scp-wiki.wikidot.com/theme:art-deco` — the original's own host, exactly as recorded in review/sources.tsv (original_url); no host discrepancy to probe. The original's body links (to `component:sigma-plus` and `component:toggle-sidebar` on scp-wiki, inside the dropped prose paragraph) were not carried over; their informational successors are the section 2 include and foundation line, which name the JP component directly rather than linking the EN page.
- **Why:** P11: prose links take the JP counterpart where one exists; here the counterpart is included, not linked, which is the stronger form of the same rule.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the frame's draft-host address only.
- **Disposition:** Standing.

### 8. Structure

- **What:** The closing rule holds for the CSS: the moved body preserves selectors, variables, and order at 0.99 similarity, and the JP additions arrive as head furniture and the tail license furniture, not interleaved. The body region adjudicates as one event, and the classifier's three heuristic blocks (B5: the Sigma Plus paragraph; B6: the usage lead-in; B9: the exhibits region, original L21–49) plus its 4 EXHIBIT-RESTRUCTURE blocks all describe it: the original's body — two prose paragraphs, a usage exhibit, an hr explanation with a live `----`, an image-block exhibit, a table exhibit, a tabview exhibit, three font-sample spans, and a 300px spacer div — is absent from the candidate, replaced by the three standard body lines. Stated plainly, as in the alcur package: the candidate does not carry the original's documentation body or its exhibits. The grounds are the same and are stated, not assumed: the campaign's candidate form is the includable theme (head, credit, usage, base note, CSS), the campaign's sample page carries the decoration-demonstration role, and no T-row charged the omission (T4's display-affecting count for this theme is 1, the dropped base of section 2; the exhibits' rendering was never a finding). The one exhibit with a delivery consequence — none: the image-block exhibit names an original-host asset as an example, and its absence changes no live behavior of the theme itself.
- **Why:** R3 exists to force exactly this census; the classifier's "replaced versus dropped" ambiguity for B9 is resolved by reading the candidate: dropped, with the ground stated.
- **Verify:** `grep -n 'tabview\|image-block\|collapsible' candidate.txt` returns nothing; compare the body regions (original L7–47, candidate L21–25).
- **Disposition:** Standing under the stated ground; no class I item (no selector, variable, or delivered rule was dropped — the CSS body is entire).

### 9. Formatting only

- **What:** One WS-ONLY block and no re-indentation (0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary in classification.json (WS-ONLY ×1; reindent_blocks: 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter text: the intro line (candidate L21), a porter-written description with no original counterpart, counted in section 6. There are no `[!-- --]` translator notes (in particular, no note about the toggle-sidebar absence — the gap T4 recorded, stated in section 2), no editor line, and no porter comment in the CSS (the banner is the original's own).
- **Why:** R2: porter-added text is part of the change record; the absence of a note where T4 expected one is likewise recorded rather than passed over.
- **Verify:** Read candidate L21; `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (recorded, including the absent note).

### 11. Dispositions and exceptions

- **What:** Three groups. (1) T1 is clean: exit 0, 0 errors — this theme has no standing T1 class at all, the only one of this batch's five. (2) The render row's items: the malformed font `@import` URLs (fonts never load, HTTP 400/ORB) — FIXED by repair and live probe, section 4, so this item is closed by fix, not disposition; and the gold-frame × default-header collisions at PC and 320 widths, dispositioned as the theme's own frame geometry against the environment's default header (a design-collision observation; no port edit caused it and no wave was charged with it). (3) T4's charge as adjudicated: the dropped base FIXED (section 2), the false foundation line FIXED with it, the toggle-sidebar absence standing on the existence ground, and the asset-host/credit-field classes recorded in the theme's §(c3) line as dispositioned under the class outcomes (header language ruling 2; assets class (ii); credit fields FIXED by the credit waves).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; an item closed by a probed fix is distinguished from one closed by disposition.
- **Verify:** Each item names its deciding record above; the font item's probe is the §(c2) KB-04 line of GOSIGN2-LEDGER.
- **Disposition:** DISPOSITIONED (the collision family and the class outcomes); FIXED (the base, the foundation line, the font grammar).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 58): PASS, exit 0, 0 errors / 1 warn / 1 info — the batch's only clean T1. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): FINDINGS, the items of section 11(2); engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 58, LOCALIZE-S2-A): FINDINGS jointly, display-affecting findings 1 (the dropped base); the ledger §(c4) per-theme note records its restoration, and §(c2) records the font repair with its probe. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +42/−71 in 16 change blocks / 4 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:art-deco-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 58; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The wave history, edit by edit

1. **FIX-CREDIT-D (1869877, 2026-11-17).** The commit's message is "translator attribution normalization (AI), 163 files". In this file it made six distinct edits: the sigma-plus base include restored at the head; the interwiki-style frame added; the translator field normalized to AI; the false foundation line 基盤： 単体 corrected to name the Sigma+ base; the Noto Sans JP `@import` added; and the JP face appended to the three font variables. The theme's most consequential repair of the sweep — a dropped base theme — landed inside a 163-file normalization commit whose title gives no sign of it. The campaign record (§(c4)) credits the restoration to "FIX3-S2EN §5", which is the adjudication that ordered it; the landing is this commit. Both facts are recorded so the trail reads correctly from either end.
2. **FIX4-LICENSE (c2a8bee, 2026-11-17).** Two edits: the three font `@import` URLs' grammar repaired (the KB-04 fix, live-probed 400 → 200), and the license-box furniture restored at the tail in the standard form (backend, `=====` separator, end) with no file entries. The wave's name covers the second edit; the first is the one the render row had charged.

### The dropped base, as a documentation case

This theme is the batch's clearest demonstration of why the packages narrate wave edits individually. Every automated layer saw a plausible file: T1 passed it clean (the only clean T1 in the batch), the CSS was byte-close, and the credit block was complete. The defect was an absence — a base the prose declared and the file did not include, compounded by a foundation line affirming the absence. It was caught by a human-standard read (T4), adjudicated in prose (§(c4)), and landed inside an unrelated wave's commit. A reviewer given only the diff sees two one-line additions; this record exists so they also see what those lines repair.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-art-deco-jp.txt` is the decoration sample stub the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The base file `pages/component:sigma-plus-jp.txt` is shared campaign infrastructure (the same component the jiha and suprematism candidates include), not part of this theme's change set.
