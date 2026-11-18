# Review package — theme:crt-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:crt-jp — origin CN, population #178 [GOSIGN2-LEDGER (b) row 178]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 932de1a087627d8f3a3571c727053898d66f05f7bf7f0e96f319c00ad43b466a); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 2 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 213; GOSIGN2-LEDGER (b) row 178]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 327px@320 + 908px@768. [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 177, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 177]
- FIX5 re-judgement: item 49 (class B) FIXED — FIX5-FURNB, commit 25bb0b4: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 49]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:crt-jp.txt sha256:932de1a087627d8f3a3571c727053898d66f05f7bf7f0e96f319c00ad43b466a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 49 [B] (duplicate bare Rate) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 49: **FIXED** (FIX5-FURNB, commit 25bb0b4) |
| Standing items | **DISPOSITIONED** — ledger §(c2) render row: credit-modal preview form (KB-32), page-overflow in the cross-cutting families (KB-33/KB-34); T1 pseudo-ref ×3 (class (iii) draft form). The candidate's delivery frame still carries the `theme=` parameter the FIX-CODEADDR ruling later removed in canonical (commit 722ceb5); see section 3 and the per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:crt | theme:crt-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 17, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 17 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-crt.txt` (fetched once by the LOCALIZE-S2-D lane; its working diff is `diff-crt-from17.txt` in the same lane directory) | Canonical file `pages/theme:crt-jp.txt`, copied at worktree HEAD 530cb87; the file's last content changes are commit 25bb0b4 (FIX5-FURNB) and commit b5cb724 (usage-example sweep) |
| Lines / bytes | 2,600 lines / 192,455 bytes (the last line carries no trailing newline, so `wc -l` reports 2,599) | 2,615 lines / 197,183 bytes |
| SHA-256 | c81d35bafaa10ab4c88569c3d9eb2b44f24a9cc29981f0b256f05c8897f234af | a2620034e532e2392042969adea30195ecf1e0b4322e146cfbd84d88d8872556 |

Provenance route: derived from the original at the reference revision (the mirror above, hash-verified against review/sources.tsv). No production-counterpart adoption (R4 does not apply).

## Summary

The original is a single very large CSS module (2,334 lines) implementing a CRT-monitor aesthetic, followed by a documentation body whose only furniture is a bare Rate module: the page has no credit block at all. The candidate keeps the module's topology exactly (one module, no delivery relocation; the classifier's topology pass reports zero moves) and makes three kinds of change: JP font stacks and own-host asset repoints inside the module, a translated documentation body, and the campaign's standard furniture around the module — a preview credit block where the original had none, and a delivery frame the frame waves added. The one blocking defect, the bare Rate duplicating the rate-bearing preview credit module the port added, was removed by FIX5; this package re-derives that closure from the bytes and the FIX5 commit (per-theme record). The frame's `theme=` parameter had been removed in canonical before this package's base commit (section 3); the refresh-3 recopy confirmed the copied candidate already carries the remedied frame, so no repair postdates this package.

## Standing sections

### 0. Header and provenance frame

- **What:** Neither file opens with a delivery frame of its own at the head: both open with the single `[[module CSS]]` (original L1, candidate L1). The candidate's delivery frame sits at the tail, after the module (candidate L2336–2339, section 3). Provenance route: this package's original is the lane-cached page source at revision 17 (see Provenance); no live re-fetch was made for this package.
- **Why:** The frame's position and target are the delivery facts of this port; they are recorded where they occur.
- **Verify:** Read original L1 and candidate L1, then candidate L2334–2340.
- **Disposition:** Recorded; argued under section 3.

### 1. Credit and attribution

- **What:** The original has no credit block of any kind; its only rating furniture is the bare `[[module Rate]]` at original L2337, standing after the module closes. The candidate carries the preview credit block at candidate L2343–2352 (`:scp-jp:credit:start-preview` / `end-preview`) with the eight standard fields, and no bare Rate anywhere in the file. The six fields the T4 lane found missing were completed by the credit waves; the bare Rate's removal is the FIX5 item, re-derived in the per-theme record.
- **Why:** P3/T1: the JP preview credit module is the rate-bearing form, so once the port adds it, the original's bare Rate renders a second widget beside it (KB-09; ledger charge class B). Ruling 3 (2026-11-16) fixes the translator credit form used in the block (翻訳責任者: AI).
- **Verify:** `grep -c -i 'module rate' candidate.txt` returns 0; read candidate L2343–2352; the FIX5 removal is visible in `git show 25bb0b4 -- pages/theme:crt-jp.txt` (one 3-line deletion).
- **Disposition:** FIXED (ledger §(e) item 49; supplement row 49). The field completion is FIXED as recorded in ledger §(c3) (P3, credit waves, checker-verified).

Per-theme judgment on the fields: the copyright holder field names `[[*user Mr_J_AND]]`. The original page source names the author nowhere in its text; the in-source trace is the author's sandbox path in the blink-sprite URL (`jand-test`, original L1421), and the credit waves' completion stands checker-verified in the ledger. The title field (candidate L2344) keeps the CN title 显像管 主题版式， the same string as the original-title field (L2347): no Japanese title form exists anywhere in the candidate body for it to match, and no charge names it (title language is out of scope for migration correctness under ruling 2, 2026-11-16).

### 2. Includes and components

- **What:** The original's only include is its own escaped usage example, `@@[[include :scp-wiki-cn:theme:crt]]@@` (original L2350); the page is otherwise one module plus prose. Candidate includes: the delivery frame's `component:interwiki-style` (candidate L2337, section 3), the credit preview pair (candidate L2343/2352), and the escaped usage example `:scp-jp:theme:crt-jp` (candidate L2365). No component port under ruling 4 is involved; the theme is self-contained on both sides.
- **Why:** P1 include repoints (branch form `:scp-jp:` and the posting name with `-jp`) apply to the credit pair and the usage example.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` (1 line against 4).
- **Disposition:** Standing (the port itself).

### 3. Delivery and code loading

- **What:** Delivery topology is unchanged: on both sides a single `[[module CSS]]` (original L1–2334, candidate L1–2334) carries the whole theme, and there is no code-exhibit delivery channel to repoint. What the candidate adds is the frame at candidate L2336–2339: one `component:interwiki-style` include at priority 1 naming, through its `theme=` parameter, the candidate's own code block 1 on the draft host (`theme%3Acrt-jp/1`). The FIX-CODEADDR population audit (R/review-scout/FIX-CODEADDR.md) classes this reference in its no-target set: block 1 of this page is the documentation body's specimen exhibit, not a CSS delivery block, so the parameter names no working stylesheet. The original had no interwiki-style mechanism at all; the T4 lane charged its absence (type 6, display-affecting minor-to-medium; LOCALIZE-ROWS row 177), and the frame waves' P6 fix is this frame (ledger §(c3): P6 FIXED, checker-verified).
- **Why:** P6 is the campaign's frame class; the audit's sub-shape (B) under the main chat's ruling covers exactly this case (a wave-introduced frame parameter naming no target: remove the parameter, keep the frame).
- **Verify:** Read candidate L2336–2339; `grep -n 'local--code' candidate.txt` returns that one line.
- **Disposition:** Recorded as the packaged state. Canonical had applied the ruling before this package's base commit: commit 722ceb5 removed the `theme=` parameter from this file's frame (the frame include itself is kept), under the FIX-FRAMEADDR remedy set (report R/review-scout/FIX-FRAMEADDR.md). The refresh-3 recopy was a verified no-op — the copied candidate already carries the remedied frame — and the stamp reads STALE against the pre-remedy verdict by design; no re-judgement is claimed for the changed bytes.

### 4. Fonts and assets

- **What:** Fonts: the module's two stacks are rewritten from SC faces to JP faces. `--crt-font` (original L33: "Sarasa Mono SC", "Microsoft YaHei") becomes candidate L33 ("Sarasa Mono JP", "Noto Sans Mono CJK JP"); `--crt-font-body` (original L34: "Noto Sans CJK SC", "Microsoft YaHei", "PingFang SC") becomes candidate L34 ("Noto Sans CJK JP", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo"). Neither file carries an `@import` or `@font-face`: these are system-font stacks on both sides, so no load is expected and none is missing. The usage exhibit's sample stacks (candidate L2400–2401) show the same JP forms, as translated exhibits of the module's own lines. Assets: four URLs move from CN-side hosting to the candidate's own attachments on the draft host — the game background (candidate L21), the blink sprite (candidate L1421; the original names the author's sandbox, `scpsandboxcn.wikidot.com/local--files/jand-test/…`), the grid test image (candidate L2565), and the warp SVG download link (candidate L2607). The `url(` count is 32 on both sides; nothing was dropped.
- **Why:** The stack changes are the P7 font-stack rewrite form (JP faces named in CN stacks). The asset moves are P5 re-hosting to the theme's own storage; at draft stage that storage is the draft host (class (iii)).
- **Verify:** `grep -n '@import\|@font-face' original.txt candidate.txt` (none on either side); `grep -c 'url(' original.txt candidate.txt` (32 and 32).
- **Disposition:** Standing (draft-form class (iii) for the re-hosted assets, rewritten at posting).

### 5. Header, sidebar, and site furniture

- **What:** none as a separate change. The theme's furniture is its own full-screen CRT presentation inside the one module, byte-preserved apart from the section 4 lines; neither side defines `--header-title` or `--logo-image` overrides, and the sidebar/interwiki styling question is the frame's, recorded in section 3.
- **Why:** The ground for writing "none" here is the grep record below: there is no P8 layout adaptation and no P9/T6 variable supplement in this diff.
- **Verify:** `grep -n -- '--header-title\|--logo-image' original.txt candidate.txt` returns nothing on either side.
- **Disposition:** None required.

### 6. Text translation

- **What:** The documentation body (original L2336–2600 → candidate L2341–2615) is translated throughout: the usage prose, the parameter explanations, the sample stacks, the download notes. Inside the module, the CSS comments are translated (the classifier's 56 unanchored blocks are predominantly these one-line comment translations, each verified against the mirror line for this package), and one rendered string is localized: the footnote `content:` string 点击查看脚注 becomes 脚注を表示 (CONTENT-STRING, KB-18). Glyph-form conversions (R5) occur where the theme's own prose localizes the same words: 目录 → 目次 in a CSS comment, 曲面效果 → 曲面効果 and 表格 → 表 in body headings. The gate tag is localized （版式 → テーマ）.
- **Why:** P10 body translation is the port's purpose; CSS comments and rendered strings ride with it (R1/R5).
- **Verify:** Read candidate L2341–2615 against original L2336–2600 section by section; the body order is unchanged.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The body's external links are the asset download link (candidate L2607, re-hosted with the asset, section 4) and the credit block's source link (candidate L2351), which points back to the original page on scp-wiki-cn — the host recorded in review/sources.tsv for this theme. No prose link in the candidate targets an un-suffixed `theme:crt` name on scp-jp, and no link names a page the record shows to be absent.
- **Why:** P11 repoints apply where a JP counterpart page exists; the source link's target is the original itself.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` and compare each host against sections 3–4.
- **Disposition:** Standing; no dead-target link is recorded for this theme.

### 8. Structure

- **What:** The structure is preserved exactly: one module, then the documentation body, in the same order, with the body's internal order unchanged. The classifier labels 20 blocks DELIVERY-MOVE; adjudicated against the topology pass (which reports zero moves), every one of them is a false fire — B1 and B6–B20 are CSS comment translations inside the single module, B2/B5 are the section 4 asset repoints, B3 is the font-stack rewrite, B4 is the footnote content string. No module was dropped, split, or relocated; multi-module checks do not arise (one module on each side). The structural deltas are the furniture additions already recorded: the frame (candidate L2336–2339) and the credit block (candidate L2343–2352) stand where the original's bare Rate stood, and the FIX5 deletion removes that Rate. CSS brace balance was checked by depth, not count: both files end at depth 0 with no negative-depth line.
- **Why:** Structural preservation is what keeps the follow-up diff (the T4 mechanism) applicable; the DELIVERY-MOVE adjudication is recorded here so the label mass is not mistaken for 20 relocations.
- **Verify:** Compare the structural maps: `grep -n '\[\[module\|\[\[iftags\|\[\[/iftags' original.txt candidate.txt`.
- **Disposition:** Standing (no checker error arises from the structure).

### 9. Formatting only

- **What:** None as its own class. The classifier finds no whitespace-only or re-indentation block family in this pair; the whole diff (build_review.py, difflib) is +137/−122 changed lines across 21 diff sections, and the classifier's finer SequenceMatcher pass counts 88 change blocks (53 specific, 35 heuristic, 0 residue). Every changed line is accounted for by the sections above.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change (the R7 hazard does not arise here).
- **Verify:** diff.md's summary table and the classifier counts quoted above.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none. No porter annotation block was added inside either file; the explanatory record for this port lives in the campaign record and in this package, not in the candidate's text. The ground: the candidate's non-translated insertions are the frame and the credit block (sections 1 and 3), both furniture, and a full read of the body's added lines for this package found no annotation passage.
- **Why:** Residue class R2 is checked explicitly because annotations elsewhere in this campaign ride inside other labeled blocks.
- **Verify:** Read the added lines in diff.md outside the module.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme: (1) the T1 pseudo-ref ×3 — the candidate's own draft-host file URLs, class (iii), rewritten at posting (sections 3–4); (2) the render-row dispositions: credit-modal preview form (KB-32; ruling 5 — the modal's behavior on a preview-module page is the preview form's property, not a theme defect), page-overflow 327px@320 + 908px@768 in the cross-cutting static-credit/preview-chrome families (KB-33/KB-34); the page-side render row records runtime-hotlink only, an environment-layer item (KB-40 family); (3) the frame `theme=` parameter, dispositioned by the main chat's ruling and removed in canonical 722ceb5 (section 3). No item for this theme is left as an unexplained exception, and no class (i) item stands.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the FIX5 closure is re-derived in the per-theme record below from the current bytes and the FIX5 commit itself; (b) the T1 baseline recorded at 2026-11-16 is exit 1, 3 errors / 1 warn / 2 infos, all 3 errors pseudo-ref (T1-ROWS row 213) — that baseline predates FIX5, and one of its infos is the double-rate info whose clearing the FIX5-FURNB commit message records across its 9 files; (c) T2/T3 produced dispositions only, no open finding (ledger §(c2)); (d) the brace-depth scan run for this package ends at depth 0 on both files; (e) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib): +137/−122.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** `grep -c -i 'module rate' candidate.txt` (0), `git show 25bb0b4 -- pages/theme:crt-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### The FIX5 restoration (ledger item 49)

At ledger time this candidate rendered two rating widgets. The port had added the preview credit module at the end of the documentation body — the campaign's standard credit furniture, on a page whose original has no credit block at all — and had kept the original's bare `[[module rate]]` standing immediately before it, in the position the original's Rate occupies after the module (original L2337). The T4 lane charged it as 評価 UI 二重化 (LOCALIZE-ROWS row 177, at the T4-era line L2343), its row's closing line required the duplicate's removal before posting, and the ledger carried it as §(e) item 49 [B]. FIX5-FURNB (commit 25bb0b4) deleted exactly three lines in this file — the `[[>]]` wrapper and the module — and nothing else. Re-derivation from this package's bytes: the original has exactly one `[[module Rate]]` (original L2337); the candidate has none; the only rating surface left is the preview credit module. The supplement's FIXED (row 49) is confirmed, not merely cited.

### The usage example's posting name and the frame parameter

Two post-verdict changes touch this file, and the stamp's STALE reading covers both honestly. The usage-example population sweep completed the escaped include to the posting name `:scp-jp:theme:crt-jp` (candidate L2365; sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724). Separately, canonical commit 722ceb5 removed the frame's `theme=` parameter under the FIX-FRAMEADDR ruling (section 3). Both landings predate this package's base commit `dd89c80` — the copied candidate carries the remedied frame and has no `theme=` line, and the refresh-3 recopy was a verified no-op (correcting the older claim that the parameter was still present and that the change postdated the base). No verdict is carried over either change: the frozen ledger remains the verdict record for the bytes it judged.


### Post-package repairs (REFRESH3-D)

Recopy was a verified no-op: `candidate.txt` is byte-identical to the current canonical `pages/theme:crt-jp.txt`. No repair lands after this package's candidate build, so the record below is the slice's sub-shape and remedy, confirmed present in the built bytes.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Acrt-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L2336.
- **Record correction:** section 3 and the old per-theme passage stated that 722ceb5 landed *after* this package's base and that the packaged candidate still carried the parameter. Both are wrong: commit ancestry shows 722ceb5 is an ancestor of the package build `dd89c80`, the copied `candidate.txt` has no `theme=` line, and the recopy is a no-op. The passages are corrected here so the record matches the bytes.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) The hosted files the module and body name — the game background webp, `ava-blink-sprite.png`, `Grid-Test.png`, `crt_image_warp.svg` — carried as attachments of theme:crt-jp on the draft host (at posting, of the posted page on the production host); they are hosted files, not repo files. (2) `pages/theme-decoration-sample-crt-jp.txt` — the decoration sample page used by the render checks. The `start-themes.tsv` row records this theme's base as "standalone", which the bytes confirm: no base theme is included or imported on either side.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave produced the initial port (translation, font stacks, asset re-hosting, the added credit block, and, as later found, the retained bare Rate); the credit waves completed the six missing credit fields; the frame waves added the delivery frame (P6); FIX5-FURNB removed the duplicate Rate; the usage-example sweep completed the posting name; and the FIX-FRAMEADDR remedy later removed the frame's `theme=` parameter in canonical. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 49; GOSIGN2-LEDGER-SUPPLEMENT.md row 49; LOCALIZE-ROWS row 177; T1-ROWS row 213; commits cad7c86 (Stage 2 CN4 integration), 666f543 (FIX2-CREDIT), 25bb0b4 (FIX5-FURNB), b5cb724 (usage sweep), 722ceb5 (frameaddr remedy, post-base). The go-sign re-run over that record is what the Status block certifies. Patterns cited in this package are at patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## License and attribution

- **Title:** 显像管 主题版式
- **Author:** Mr_J_AND
- **Source:** https://scp-wiki-cn.wikidot.com/theme:crt — revision 17
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
