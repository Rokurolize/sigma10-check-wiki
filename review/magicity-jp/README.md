# Review package — theme:magicity-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:magicity-jp — origin CN, population #204 [GOSIGN2-LEDGER (b) row 204]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 971eaeda0ee6dc2152069d737b88f8c2d2a87b12170d98dc9001921869d7b426); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 15 errors / 2 warns / 1 info (pseudo-ref×15); standing classes dispositioned in register c1 [T1-ROWS row 270; GOSIGN2-LEDGER (b) row 204]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page `hidden-interwiki` (chromium 375/320, webkit 768/375/320), runtime-hotlink site-theme chain only; sample credit-modal (preview-form), `hidden-interwiki` (same 5 combos), `sidebar-not-opening` [webkit 768x1024] (machine line; T3: not reproduced in the webkit 768 sidebar screenshot, drawer open), runtime-hotlink site-theme chain + sample font host; T3 REAL FINDING (sample): table-cell, blockquote and tab-panel body text renders near-black on dark navy panels (the classed-wrapper table cells, "7. 引用と区切り" quotes, "10. タブ" body) and is effectively unreadable at chromium 1366x768; page T3 clean (hamburger present both engines at ≤375, drawer opens); magicity.svg/shujia.png broken = deferred assets; sample webkit 375/320 *-full.png missing (32767px cap). [RENDER-ROWS-RERUN16 (CN9) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN9)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 203, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 203]
- FIX5 re-judgement: item 66 (class E) DISPOSITIONED — FIX5-CONTRA (no edit, no commit): candidate vs original colour value sets byte-identical (line citations both sides) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 66]
- Computed against: canonical commit 18aa301801827f0f49074aa1b59efea49f598270; candidate file pages/theme:magicity-jp.txt sha256:971eaeda0ee6dc2152069d737b88f8c2d2a87b12170d98dc9001921869d7b426; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 66 [E] — sample table-cell, blockquote and tab-panel body text renders near-black on dark navy panels and is effectively unreadable (KB-28 contrast family) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 66: **DISPOSITIONED** (FIX5-CONTRA, no edit), on the colour-identity ground re-derived in the per-theme record below |
| Standing items | **DISPOSITIONED** in their rows — hidden-interwiki and the runtime-hotlink site-theme chain (environment layer); sample credit-modal (preview-form); sample webkit screenshot gaps (32767px ceiling); magicity.svg/shujia.png broken (owner-deferred asset hosting, KB-58) [RENDER-ROWS-RERUN16 (CN9)] |
| Defect flags carried | Three flags and one minor flag stand against the candidate as it stands (sections 1, 2, 4, 7): the original's license line dropped from the credit; the interwiki frame's `type=sidebar` parameter dropped; the font 'ZCOOL QingKe HuangYou' named but loaded nowhere (minor); the fossil cross-reference's missing original-language annotation (minor). None was charged by the campaign's checks; the candidate is not edited by this package |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:magicity | theme:magicity-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 20, as recorded in the candidate's credit block (初訳時参照リビジョン: 20, candidate L29) and in review/sources.tsv | — |
| Source of this copy | Mirror store `review-mirrors/orig-magicity-rev20.txt`, fetched once by the LOCALIZE-S2-D lane at rev 20 (INDEX.tsv class COPY) | Canonical file `pages/theme:magicity-jp.txt`, copied at worktree HEAD f24b7d0; the file is byte-identical to the copy FIX5 judged (its SHA-256 is the one REPORT-GOSIGN2-FIX5-CONTRA.md records), so the verdict stamp as built read PASS, not STALE; the later FIX-RDISP7 landing (canonical commit 18aa301, Post-package repairs) changed the candidate after the build, so the regenerated stamp now reads STALE with the record verdict standing |
| Lines / bytes | 2,510 lines / 60,067 bytes (the last line carries no trailing newline) | 2,617 lines / 66,849 bytes (the last line carries no trailing newline) |
| SHA-256 | 0ff242ec2b12f497d8285ccfd0425f5c8e167d71938c03989bc7349420ed8427 | b6d967cec4b7ee64e2d70a1f8944140c713f0a788a7e8ffe596966ff30d9af1b |

Package files: `original.txt` and `candidate.txt` as tabled above; `classification.json` and the skeleton behind this README are from classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## Summary

Magicity is a large Sigma-Plus based theme, and its port is correspondingly structural: the head delivery is rebuilt so the theme's own first code fragment imports the JP base component (the original's head module imported the CN base directly), the main stylesheet moves from fragment /1 to /2, the font-variable fragment becomes /3, the font program is rewritten from the CN zeoseven service to Google Fonts with Japanese faces, and the whole documentation body is translated. The original's four include-parameter gates survive in their original forms and placements (section 3). The theme's only blocking item was a contrast charge against its sample panels, dispositioned because the candidate's colour values are the original's own, byte for byte — re-derived from this package's two files in the per-theme record. Four defect flags are carried (Status block): a dropped license line, a dropped frame parameter, and two minor flags, none of them charged by the campaign's checks and none edited by this package.

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

- **Provenance route:** derived from the branch original at the reference revision (theme:magicity rev 20 on scp-wiki-cn). This is not an R4 production adoption: no production JP counterpart exists in the record for this theme, and the candidate's body is the S2 localization of the CN original. The evidence is mutually consistent: review/sources.tsv keys the row `standard` with the mirror's SHA-256 equal to this package's original.txt; the candidate's credit block records 初訳時参照リビジョン: 20 (candidate L29); and the T4 follow-up diff (diff-magicity-from20.txt in the campaign record, K5a-i) records rev20 → rev20 with no changes, so the mirror in this package is also the current original, not a superseded revision. The sources.tsv note claiming the opposite is flagged in the per-theme record.


## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 28 |
| COMPONENT-SWAP | 4 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 2 |
| CREDIT-PROSE | 2 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 3 |
| DRAFT-HOST | 15 |
| EXHIBIT-RESTRUCTURE | 2 |
| GLYPH-FORM | 6 |
| HEADERVAR | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 8 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 3 |
| SIGMA-PLUS-JP | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 51 |
| TRANSLATION-ANCHORED | 34 |
| WS-ONLY | 1 |

Counts: 104 blocks, 61 specific, 43 heuristic, 0 residue, 0 skipped (comment text).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B6: orig 22-25 -> cand 19-19 (body -> body)
  - B8: orig 30-33 -> cand 23-31 (body -> body)

- CREDIT-PROSE (C): Translated credit prose (P3/P10): attribution text is reader-visible and localizes with the page.
  Verify: Read the pair in the mirror and the candidate side by side.
  - B7: orig 27-28 -> cand 21-21 (body -> body)

- T7-CREDIT-CSS (B): Credit-module CSS supplement (T7, KB-11/KB-12/KB-62): the JP credit module's DOM needs rules the branch original never shipped, or its inherited rules corrected in place.
  Verify: KB-11/KB-12 recipes: confirm the selectors in the candidate and whether the production counterpart carries them (supplement vs inherited).
  - B64: orig at 259 -> cand 259-378 (body -> code-css)

- **What (this theme):** the original's three-part CN credit (credit:start / credit:more / credit:end with a bare `[[module Rate]]` inside, original L22–33) becomes the preview credit block (candidate L19–31) carrying the eight TASL fields (B8's TASL-FIELDS span): タイトル 魔都 版式 / 翻訳責任者 AI / 翻訳年 2026 / 原題 魔都 版式 / 著作権者 OxygenNine / 作成年 2025 / 初訳時参照リビジョン 20 / 元記事リンク https://scp-wiki-cn.wikidot.com/theme:magicity. The author field names OxygenNine, matching the original credit's `[[*User OxygenNine]]` (original L23) — the name is preserved (in plain-text form), so no pointer-in-place-of-author defect stands. The source link's host is scp-wiki-cn.wikidot.com, the host sources.tsv records for the original. B7 is the credit prose's translation.
- **FLAG — the original's license line is dropped.** The original's credit block states the theme's license in its credit:more part (original L31): 授权协议：CC-BY-SA 4.0 International. The candidate carries no equivalent anywhere: a search for "4.0" over the whole candidate finds nothing, and its only CC mention is the Sigma-Plus base comment (CC BY-SA 3.0, candidate L255), which licenses the base component, not this theme. No license box replaces the line (the candidate has no license-box include). A dropped attribution/license line of the credit family, with both sides' text as cited; flagged for the coordinator, not edited by this package.
- The T7-CREDIT-CSS spans inside B64 (candidate L326–336) are the override layer's credit-module rules for the JP preview module's DOM — the KB-11/KB-12 supplement shape, riding inside the documented override layer of section 8.
- **Disposition:** verdict PASS, with the license-line flag carried above.


## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B5: orig 19-19 -> cand 16-16 (body -> body)

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B13: orig 44-44 -> cand 42-42 (body -> body)
  - B17: orig 52-52 -> cand 50-50 (body -> body)
  - B18: orig 54-54 -> cand 52-52 (body -> body)
  - B19: orig 56-56 -> cand 54-54 (body -> body)

- SIGMA-PLUS-JP (A): Sigma-plus JP form (T8, KB-64): only component:sigma-plus-jp exists in the JP environment; the bare form does not resolve.
  Verify: Grep the candidate for component:sigma-plus without the -jp suffix; none may remain.
  - B63: orig 256-256 -> cand 254-256 (body -> body)

- **What (this theme):** the iftags gate (B5) localizes its tag: `[[iftags +版式]]` (original L19) becomes `[[iftags +テーマ]]` (candidate L16) — the CN 版式 (format) class tag maps to the JP environment's テーマ tag (KB-08). The COMPONENT-SWAP blocks (B13, B17–B19) are the documentation's component demonstration includes, repointed to their JP candidate forms in place. The SIGMA-PLUS-JP span (B63, candidate L254–256) is the base declaration at the head of the main fragment: the candidate's first fragment imports `component:sigma-plus-jp` (section 3), and no bare `component:sigma-plus` remains.
- **FLAG — the interwiki frame's `type=sidebar` parameter is dropped.** The original's frame include (original L10–13) is `component:interwiki-style:scp-wiki-cn:` with `priority=3`, `type=sidebar`, `override=` (empty), `css=` (empty), and `theme=` naming the author's sandbox copy of fragment /2. The candidate's include (candidate L10–13) is the bare `component:interwiki-style` with only `priority=3` and `theme=` naming its own /3. The two empty parameters are no-ops, but `type=sidebar` selects the frame's sidebar form, and its drop is not dispositioned anywhere in the record. The population check run for this package: candidates whose originals carry `type=sidebar` retain it (theme:highlighter-bhl-jp, theme:sci-fi-jp ×2, theme:shancheng-jp) — this candidate is the outlier. The bare (unprefixed) frame form itself resolves on scp-jp and is recorded, not flagged. Flagged with both sides' lines; not edited.


## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B1: orig 3-3 -> cand 3-3 (module-css -> module-css)
  - B2: orig 5-5 -> cand 5-5 (module-css -> module-css)
  - B4: orig 13-16 -> cand 13-13 (body -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B9: orig 36-36 -> cand 34-34 (body -> body)
  - B47: orig 183-183 -> cand 181-181 (body -> body)
  - B75: orig 355-355 -> cand 462-462 (code-css -> code-css)
  - B77: orig 426-426 -> cand 533-533 (code-css -> code-css)
  - B78: orig 446-446 -> cand 553-553 (code-css -> code-css)
  - B81: orig 937-937 -> cand 1044-1044 (code-css -> code-css)
  - B85: orig 1099-1099 -> cand 1206-1206 (code-css -> code-css)
  - B86: orig 1160-1160 -> cand 1267-1267 (code-css -> code-css)
  - B103: orig 2483-2483 -> cand 2590-2590 (module-css -> module-css)
  - B104: orig 2496-2496 -> cand 2603-2603 (module-css -> module-css)

- **What (this theme):** the delivery topology is rebuilt around the fragment renumbering, and the census closes. The original's head `[[module CSS]]` imports two URLs: the CN sigma-plus base's /1 and the theme's own /1 (original L3, L5). The candidate's head module imports the theme's own /1 and /2 (candidate L3, L5). The original's fragment /1 is the main stylesheet (original L258–2332); in the candidate that stylesheet is fragment /2 (candidate L262–2439), because a new fragment /1 (candidate L258–260) carries a single `@import` of `component:sigma-plus-jp/1` — the base now arrives through the theme's own first fragment, mirroring the position the CN base import held in the original's head module. The original's fragment /2 (the font-variable fragment, original L2334–2420) becomes the candidate's /3 (candidate L2441–2527), and the frame's `theme=` names /3 accordingly. Self-delivery census (counting every code-block form — `[[code]]`, `[[code type="CSS"]]`, and typed forms): 2 code blocks in the original, 3 in the candidate, and every self-delivery address names the block that actually holds the content it names, so no FIX-CODEADDR mismatch stands.
- **The gates.** The original carries four include-parameter gates. Three live in its two tail `[[module CSS]]` blocks as inline render-time text — `{$normalPageTitle}` (original L2430–2444), `{$noAnimation}` (L2452–2458), `{$redMode}` (L2460–2508) — and the candidate's tail modules carry the same three gates in the same inline form (candidate L2537–2551, L2559–2565, L2567–2615), the gated CSS byte-identical apart from comment translation. The fourth, `{$toggle-sidebar}`, sits inside the code fragment on both sides (original L2201–2324 / candidate L2308–2431) as a comment gate: inert inside a URL-delivered fragment, but inert on *both* sides — the original's own placement, inherited, not a port regression. All four gates survive in the original's own forms and placements; none was inlined unconditionally or dropped.
- The 15 DRAFT-HOST spans are the theme's own file-area assets (shujia.svg, mgcbg.svg, shujia_skyline.svg, magicity.svg, shujia.png, sigma9-logo.png) repointed from the author's sandbox hosts to the candidate's draft-host file area — class (iii) forms that posting rewrites (KB-41); the broken state of two of them is the KB-58 disposition of section 11.
- **Disposition:** verdict PASS, with the section 2 frame-parameter flag carried.


## 4. Fonts and assets

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B66: orig 275-277 -> cand 395-395 (code-css -> code-css)

- **What (this theme):** B66 is a wholesale font-program rewrite (pattern 7), and it is documented in the file. The original loads two zeoseven (ZSFT) CSS files — CSS 92 （得意黑 / Smiley Sans, display) and CSS 415 (a Sarasa Gothic SC subset, body) at original L275/L277 — plus an `@font-face` for the Latin subset face "zsft-enmin-159" (original L287–291, the B67 block of section 8). Those are CN-subset services: they carry no Japanese glyphs, so the program cannot serve the JP page as it stands. The candidate loads one Google Fonts import (candidate L395: Dela Gothic One; BIZ UDPGothic 400;700; Noto Sans SC 400;500;700; Noto Sans Mono) and rewrites the three font variables in both `:root` copies (candidate L401–403 and L2444–2446; original L294–296 and L2337–2339): title `'Dela Gothic One', 'ZCOOL QingKe HuangYou', sans-serif`; text `'BIZ UDPGothic', 'Noto Sans SC', sans-serif`; mono `'Noto Sans Mono', 'BIZ UDPGothic', monospace`. The substitution is disclosed in the candidate's own prose (candidate L242: the title face is Dela Gothic One as a substitute, the original's being 得意黑） — the in-file record whose absence made the sunside case a flag. The zeoseven loads are gone, not duplicated; the one import sits in the delivered fragment /2, not an inert channel.
- **FLAG (minor) — 'ZCOOL QingKe HuangYou' is named but loaded nowhere.** The title stack names it in second position (candidate L401 and L2444), behind the loaded Dela Gothic One, but no `@import` or `@font-face` in the candidate loads it, and the base `component:sigma-plus-jp` does not load it either (a search over the canonical pages finds ZCOOL loads only for the different family ZCOOL XiaoWei, in other themes). A named-but-unloaded fallback in second position: minor, flagged, not edited.
- **Disposition:** verdict PASS, with the minor flag carried.


## 5. Header, sidebar, site furniture

- HEADERVAR (A): Header/title variables (P9/T6, KB-57): the header text variables are the theme's visible title surface.
  Verify: KB-57: where the value stays in the original's language, the disposition is ruling 2 (section 11).
  - B74: orig 349-350 -> cand 456-457 (code-css -> code-css)

- **What (this theme):** two HEADERVAR loci. B74 (original L348–350 → candidate L455–457) is the in-body header-variable block, translated with the body. B64's HEADERVAR span (candidate L269–271) is in the override layer, which sets `--header-title: "SCP財団"` and `--header-subtitle: "確保、収容、保護"` and points `--sp_header-logo` at the theme's own sigma9-logo.png on the draft host. The title is the JP foundation's own name and the subtitle its established motto — identity strings functioning as marks, not prose sentences — so they stand under ruling 2 as bounded by ruling 7 (a prose-sentence subtitle default would translate; these are not prose sentences).
- **Disposition:** ruling 2 (header/title language out of scope for migration correctness).


## 6. Text translation

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B10: orig 38-38 -> cand 36-36 (body -> body)
  - B11: orig 40-40 -> cand 38-38 (body -> body)
  - B16: orig 50-50 -> cand 48-48 (body -> body)
  - B20: orig 58-58 -> cand 56-56 (body -> body)
  - B26: orig 99-100 -> cand 97-98 (body -> body)
  - B27: orig 102-102 -> cand 100-100 (body -> body)
  - B28: orig 104-104 -> cand 102-102 (body -> body)
  - B29: orig 106-106 -> cand 104-104 (body -> body)
  - B30: orig 108-108 -> cand 106-106 (body -> body)
  - B31: orig 110-110 -> cand 108-108 (body -> body)
  - B32: orig 116-117 -> cand 114-115 (body -> body)
  - B33: orig 119-119 -> cand 117-117 (body -> body)
  - B39: orig 132-132 -> cand 130-130 (body -> body)
  - B41: orig 139-140 -> cand 137-138 (body -> body)
  - B42: orig 144-144 -> cand 142-142 (body -> body)
  - B49: orig 197-197 -> cand 195-195 (body -> body)
  - B57: orig 234-238 -> cand 232-236 (body -> body)
  - B58: orig 244-244 -> cand 242-242 (body -> body)
  - B61: orig 252-252 -> cand 250-250 (body -> body)
  - B68: orig 294-296 -> cand 401-403 (code-css -> code-css)
  - B69: orig 298-300 -> cand 405-407 (code-css -> code-css)
  - B70: orig 302-304 -> cand 409-411 (code-css -> code-css)
  - B71: orig 306-307 -> cand 413-414 (code-css -> code-css)
  - B72: orig 309-310 -> cand 416-417 (code-css -> code-css)
  - B73: orig 312-317 -> cand 419-424 (code-css -> code-css)
  - B95: orig 2337-2339 -> cand 2444-2446 (code-css -> code-css)
  - B96: orig 2341-2343 -> cand 2448-2450 (code-css -> code-css)
  - B97: orig 2345-2347 -> cand 2452-2454 (code-css -> code-css)
  - B98: orig 2349-2350 -> cand 2456-2457 (code-css -> code-css)
  - B99: orig 2352-2353 -> cand 2459-2460 (code-css -> code-css)
  - B100: orig 2355-2360 -> cand 2462-2467 (code-css -> code-css)

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B12: orig 42-42 -> cand 40-40 (body -> body)
  - B14: orig 46-46 -> cand 44-44 (body -> body)
  - B22: orig 81-81 -> cand 79-79 (body -> body)
  - B23: orig 86-86 -> cand 84-84 (body -> body)
  - B24: orig 94-94 -> cand 92-92 (body -> body)
  - B25: orig 96-96 -> cand 94-94 (body -> body)
  - B34: orig 121-121 -> cand 119-119 (body -> body)
  - B35: orig 123-123 -> cand 121-121 (body -> body)
  - B36: orig 125-125 -> cand 123-123 (body -> body)
  - B37: orig 127-127 -> cand 125-125 (body -> body)
  - B38: orig 129-129 -> cand 127-127 (body -> body)
  - B40: orig 134-134 -> cand 132-132 (body -> body)
  - B43: orig 148-148 -> cand 146-146 (body -> body)
  - B44: orig 150-150 -> cand 148-148 (body -> body)
  - B45: orig 152-152 -> cand 150-150 (body -> body)
  - B46: orig 154-154 -> cand 152-152 (body -> body)
  - B48: orig 191-191 -> cand 189-189 (body -> body)
  - B50: orig 199-199 -> cand 197-197 (body -> body)
  - B51: orig 201-201 -> cand 199-199 (body -> body)
  - B52: orig 208-208 -> cand 206-206 (body -> body)
  - B53: orig 210-210 -> cand 208-208 (body -> body)
  - B54: orig 219-219 -> cand 217-217 (body -> body)
  - B55: orig 221-221 -> cand 219-219 (body -> body)
  - B56: orig 223-223 -> cand 221-221 (body -> body)
  - B59: orig 246-246 -> cand 244-244 (body -> body)
  - B60: orig 248-248 -> cand 246-246 (body -> body)
  - B62: orig 254-254 -> cand 252-252 (body -> body)
  - B65: orig 272-272 -> cand 392-392 (code-css -> code-css)
  - B76: orig 401-401 -> cand 508-508 (code-css -> code-css)
  - B79: orig 494-494 -> cand 601-601 (code-css -> code-css)
  - B80: orig 920-920 -> cand 1027-1027 (code-css -> code-css)
  - B82: orig 1025-1025 -> cand 1132-1132 (code-css -> code-css)
  - B84: orig 1080-1080 -> cand 1187-1187 (code-css -> code-css)
  - B87: orig 1404-1404 -> cand 1511-1511 (code-css -> code-css)
  - B88: orig 1486-1486 -> cand 1593-1593 (code-css -> code-css)
  - B89: orig 1539-1539 -> cand 1646-1646 (code-css -> code-css)
  - B90: orig 1543-1543 -> cand 1650-1650 (code-css -> code-css)
  - B91: orig 1685-1685 -> cand 1792-1792 (code-css -> code-css)
  - B92: orig 1713-1713 -> cand 1820-1820 (code-css -> code-css)
  - B93: orig 1915-1915 -> cand 2022-2022 (code-css -> code-css)
  - B94: orig 2197-2197 -> cand 2304-2304 (code-css -> code-css)

- CONTENT-STRING (B): Visible string in CSS (KB-18, R1 reader-visible half): content: strings and string-valued variables render for readers.
  Verify: The string renders in the sample page's DOM text.
  - B83: orig 1055-1055 -> cand 1162-1162 (code-css -> code-css)

- GLYPH-FORM (B): Shinjitai conversion (R5): retained source-language strings converted to Japanese glyph forms; neither translated nor left untouched, and the reviewer must see it separately.
  Verify: Fold-compare the pair; only glyph forms differ.
  - B101: orig 2428-2428 -> cand 2535-2535 (module-css -> module-css)

- **What (this theme):** the documentation body translates in full: 34 TRANSLATION-ANCHORED and 51 TRANS-UNANCHORED spans in the prose, and 28 COMMENT-TEXT spans of CSS comment translation across the two big fragments, adjudicated in the appendix. B83 (CONTENT-STRING) is the page-tags label string, `content: '标签'` → `content: 'タグ'` (candidate L1162) — reader-visible, translated. The GLYPH-FORM spans (B70, B72, B74, B97, B99, B101) are the R5 shape inside translated CSS comments: simplified-Chinese comment words converted to Japanese glyph forms （互补色 → 補色 and the like) while the colour values they annotate stay byte-identical (per-theme record). What remains in Chinese is deliberate: the credit's 原題 field （魔都 版式， the original's own title, kept as the TASL original-title field) and the exhibit code. No untranslated reader prose remains.
- **Disposition:** verdict PASS (T5 judged jointly with T4: FINDINGS on the section 11 items only).


## 7. Links

- LINK-REPOINT (C): Link target repointed (P11): prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.
  Verify: Probe the target; a repoint needs sameness evidence.
  - B15: orig 48-48 -> cand 46-46 (body -> body)

- **What (this theme):** B15 (original L48 → candidate L46) carries two reference changes in one sentence: the mox cross-reference repoints to `[[[theme:mox-jp|mox]]]` (the JP candidate exists in the population), and the magicity2 exhibit — a theme that exists only on the author's own wiki — becomes a prose URL to oxygennine.wikidot.com annotated （原語版のみ） ("original-language only"), with the porter note of section 10 explaining the form.
- **FLAG (minor) — the fossil cross-reference lost its annotation.** Original L46 names the CN theme in a design credit: `[[[theme:fossil|化石 版式]]]`. Candidate L44 renders it as the absolute URL https://scp-wiki-cn.wikidot.com/theme:fossil labelled 化石テーマ， with no （中国語版） annotation — although theme:fossil-jp exists in the population and the sibling magicity2 reference two lines later takes the annotated form. Under the dead-reference standard the reference either repoints to the -jp counterpart or carries the original-language annotation; it does neither. Minor, flagged with both branches recorded; not edited.
- **Disposition:** verdict PASS, with the minor flag carried.


## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B3: orig 11-11 -> cand 11-11 (body -> body)
  - B21: orig 66-68 -> cand 64-66 (body -> body)

- CSS-BODY (C): Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.
  Verify: Writer review; a recurring shape is a new-signature candidate for the patterns loop.
  - B67: orig 281-291 -> cand at 399 (code-css -> body)

- **What (this theme):** B3 (original L11 → candidate L11) is the frame include line itself (section 2); EXHIBIT-RESTRUCTURE false-fires on it. B67 (CSS-BODY, original L281–291 → deleted at candidate L399) is the zsft-enmin-159 `@font-face` removal inside the section 4 font-program rewrite: the face's only consumer was `--mgc-mono-font`, which the same pass rewrote, so nothing dangles — adjudicated here and in section 4, not a silent drop. The override layer at the head of fragment /2 (candidate L264–378, inside B64) is a documented supplement, not a restructure: the original theme applied its own adaptation deltas on top of the Sigma-Plus base; the candidate imports the JP base component instead and preserves those deltas as an in-file override layer whose per-rule comments cite the EN rev.38 differences they carry (its T7-CREDIT-CSS spans are section 1). The layer adds rules; it replaces nothing the original delivered.


- **Exhibit decisions:** B21 (original L66–68 → candidate L64–66), the usage/preset exhibit region — **replaced, not dropped**: the preset exhibits survive, repointed to theme:magicity-jp with their parameters intact, and the self-exhibit `@@[[include theme:magicity-jp]]@@` stands at candidate L40. The bare `[[module Rate]]` inside the original's credit:start (original L24, B6's BARE-RATE-DEL span) — **removed with replacement**: the preview credit block that replaces the credit triple is the rate-bearing form in this environment (P3), so no rating surface is lost.


## 9. Formatting only

- WS-ONLY blocks: 1
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

The skeleton prints "none" for this section, but the ANNOTATION spans in classification.json's per-block `label_spans` say otherwise (the sections are written from the spans, per the package standard):

- B62's span (candidate L251–252): the note under the usage exhibit explaining that the alternative version on the author's own wiki (oxygennine.wikidot.com) is original-language only, and why it is linked in prose URL form — the annotation behind section 7's magicity2 form.
- B63's span (candidate L255–256): the comment at the head of fragment /2 declaring the base arrangement — the original imports the CN Sigma-Plus base; this candidate's first fragment imports `component:sigma-plus-jp`, and the theme's own Sigma-Plus adaptation deltas are preserved as the override layer that follows. Section 3's census confirms the comment states what the bytes do.
- The override layer's per-rule comments (candidate L264–378) are porter annotation mass of the same kind, each citing the EN rev.38 delta its rule preserves; the candidate's prose also gains an attribution the original's sentence lacked — "Sigma+系テーマ（EstrellaYoshte制作）" in the introduction — an added attribution, not a dropped one.

No annotation in this candidate states anything the bytes refute.

## 11. Dispositions and exceptions

- **Item 66 (class E), the unreadable sample panels — DISPOSITIONED.** The full argument is the per-theme record below; its one-sentence form is that every colour value in the candidate is the original's own, byte for byte (whole-file colour-token multisets exactly equal; the charged rules byte-identical), so the near-black text on dark navy the render walk photographed is the original theme's own palette on its own panels, not a defect the port introduced. [GOSIGN2-LEDGER-SUPPLEMENT.md item 66; REPORT-GOSIGN2-FIX5-CONTRA.md §5; KB-28 family, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa]
- **hidden-interwiki (page and sample, 5 combos) and the runtime-hotlink site-theme chain — DISPOSITIONED** as environment-layer phenomena in the render row's separation (the frame's hidden state arrives through the site-theme chain, not this theme's bytes) [RENDER-ROWS-RERUN16 (CN9)].
- **Sample credit-modal errors — DISPOSITIONED, preview-form:** credit:start-preview has no modal mechanism (GOSIGN-TESTS T2 amendment, 2026-11-16; KB-32).
- **Sample webkit *-full.png gaps — DISPOSITIONED:** the 32767px screenshot ceiling (KB-46) is a capture limit, not a page defect [RENDER-ROWS-RERUN16 (CN9)].
- **magicity.svg / shujia.png broken — DISPOSITIONED, owner-deferred asset hosting (KB-58):** the files' hosting state was deferred by owner decision 2026-11-16 [LOCALIZE-S2-C checklist item 1]. Their addresses in the candidate are the draft-host forms of section 3.
- **T1 pseudo-ref ×15 — DISPOSITIONED, class (ii)/(iii):** the fifteen draft-host file references are the sanctioned draft-stage forms; posting rewrites them (register c1) [T1-ROWS row 270]. The re-run's two warns (link-target-missing for theme:mox-jp at candidate L46 and the-melody-left-in-that-night at L123) are posting-order matters — the targets are campaign pages not yet posted to scp-jp — and stand as the baseline's warns.
- **Header strings — DISPOSITIONED (ruling 2),** section 5.
- **Not dispositions:** the four flags of sections 1, 2, 4 and 7 are carried as flags for the coordinator; nothing in the campaign record dispositions them.


## 12. Verification

- **T1 (source check):** baseline 2026-11-16: exit 1, 15 errors / 2 warns / 1 info (pseudo-ref×15) [T1-ROWS row 270]. Re-run for this package (2026-11-17, the campaign checker `check_source.py` on this package's candidate.txt, `--kind theme --translation --check-links`): exit 1, **15 errors / 2 warns / 1 info** — the error multiset is unchanged (pseudo-ref×15, the dispositioned draft-host forms of section 11); the warns are link-target-missing ×2 (candidate L46 theme:mox-jp; L123 the-melody-left-in-that-night, posting-order, section 11); the info is `!important` ×48, inherited from the original's CSS. No class (i) error stands against this candidate.
- **T2/T3 (render):** combined verdict FINDINGS [RENDER-ROWS-RERUN16 (CN9), which supersedes the RENDER-ROWS-2 row for this theme]. The one candidate-specific item is item 66 (dispositioned, section 11); the row's separation assigns the rest to the environment and capture classes named there. No re-render was run for this package: the render record is the lane's, cited, not re-measured here.
- **T4 (follow-up diff):** `diff-magicity-from20.txt` → rev20 → rev20, no change; the original's current revision is still 20. The mirror in this package is therefore also the current original.
- **T5 (translation text):** judged jointly with T4 by the source report: FINDINGS on the items in section 11 [LOCALIZE-ROWS row 203, source LOCALIZE-S2-D]; section 6 confirms the translation against the mirror.
- **This package:** `python3 review/build_review.py --check` — the verdict stamp regenerates identically from the two files in this package, and the package is not in the pre-existing stale set (the refresh-3 population). The censuses in the per-theme record were re-derived from this package's two files while this README was written, not transcribed from the supplement.


## Per-theme record

### The colour-identity disposition (ledger §(e) item 66)

The charge, as the ledger states it: item 66 [E] (KB-28 contrast) — on the sample page, table-cell, blockquote and tab-panel body text renders near-black on dark navy panels and is effectively unreadable at chromium 1366×768 (the classed-wrapper table cells, the "7. 引用と区切り" quotes, the "10. タブ" body); the page itself was T3-clean [GOSIGN2-LEDGER.md §(e) item 66; RENDER-ROWS-RERUN16 (CN9)]. Class E charges a candidate-side defect, so the question the disposition turns on is narrow and decidable from the two files in this package: did the port change any colour on the charged surfaces? The supplement's ground is that it did not: "candidate vs original colour value sets byte-identical (line citations both sides)" [GOSIGN2-LEDGER-SUPPLEMENT.md (a) item 66; REPORT-GOSIGN2-FIX5-CONTRA.md §5]. Re-measured from this package's files:

1. **Whole-file colour-token census.** Every colour token in each file (hex values and `rgb()`/`rgba()`/`hsl()` functions, whitespace-normalized): 40 distinct values on each side, and the *multisets are exactly equal* — the same count of every value. (The FIX5 report, working against the theme's /1 code asset, recorded the sets as identical with count differences; on this package's page sources the identity is exact, so the ground holds in a stronger form.)
2. **Declaration census.** Every colour/background-bearing declaration: 256 declarations on each side. The only raw differences are URL host repoints inside `background-image` values (the author's sandbox hosts → the draft host, section 3); every gradient colour stop (`#6833cd`, `#1c1f2987`, `#170909c7`, `#1c1d2dc7`, …) matches, and with the URLs normalized the multisets are identical.
3. **The charged surfaces themselves.** The block-1 `:root` carries 32 colour-variable lines on each side; every value is identical — `--mgc-text-color: #EDEDED`, `--mgc-bg-color: #1c1d2d`, `--mgc-layer-dark-1: #1c1f29`, `--mgc-layer-dark-2: #2b2c36` (original L306–307 = candidate L413–414) — and the only line differences in that window are the translated trailing comments. The sample's charged rules are byte-identical: `table.wiki-content-table tr td` (original L848 = candidate L955, the 7-line window identical) and `blockquote, div.blockquote` (original L865 = candidate L972). The tab pair the charge names — `--sp_tab-text-color: #000` on `--sp_tab-background: #fefefe` — is the original's own definition, unchanged. The redMode variant definitions of the layer variables (`--mgc-layer-dark-1: #090909`, `--mgc-layer-dark-2: #141414`, third definitions in the tail gate modules) are present identically on both sides.
4. **No structural colour accident.** A brace-depth scan of the main fragment ends at depth −1 on *both* sides (original block 1, candidate block 2), first going negative at a lone `}` at the same relative locus inside the toggle-sidebar comment-gate region (original L2247 / candidate L2354): an inherited imbalance of the original's own text, carried in the same shape — and identical on both sides, so it cannot manufacture a candidate-side colour difference. The remaining fragments end at depth 0 on both sides.

The conclusion the identity licenses: the candidate renders the sample's tables, quotes and tab panels with the original's own palette and the original's own rules, so the unreadability the T3 walk photographed is a property of the original theme's colour design, and "fixing" it would mean departing from the original — an editorial change, not a migration correction. Disposition: **DISPOSITIONED, no edit** [GOSIGN2-LEDGER-SUPPLEMENT.md item 66; FIX5-CONTRA §5].

### Second-reviewer walk

The class asks for the disposition to be walked once more from the third-party perspective: is the ground stated in terms a reader who did none of the work can check, and does it hold? The ground here is two whole-file censuses, one variable window, and two named rules, every one reproducible from `original.txt` and `candidate.txt` alone; no step asks the reader to trust the FIX5 lane's file copies (its citations were taken against the theme's /1 code asset, whose internal line numbers differ from this package's page mirror — the FIX5 report's magicity table is explicitly headed as the /1 asset's — and this record re-derived each number from the package files). The candidate in this package is byte-identical to the file FIX5 judged (Provenance), so the walk covers exactly the judged bytes. Each measurement held, in one case (the token census) in a stronger form than the supplement claims. One limit is stated for completeness: the census proves the port introduced no colour change; it does not prove the original's panels are readable — the render evidence says they are not, on the original's design, which is precisely what the disposition records. Walk outcome: **the disposition is sound as stated.**

### Record discrepancies flagged by this package

1. **The sources.tsv supersession note is wrong.** The magicity row's note claims the original was "superseded upstream since the reference revision; follow-up diff artifact diff-magicity-from20.txt in the campaign record (K5a-i)". The cited artifact records the opposite: the follow-up diff is rev20 → rev20 with no changes (its revision table is empty), and the original's current revision is still the reference revision 20 (section 12). Where the artifact records revN → revN with no changes, the note cannot stand. The correct form, recorded here for the coordinator's harvest correction (this package does not edit sources.tsv): "Upstream latest remains rev 20; the S2 artifact records rev20 to rev20, no changes; follow-up diff artifact diff-magicity-from20.txt in the campaign record (K5a-i)".
2. **The FIX5 report's line citations do not address this package's mirror.** REPORT-GOSIGN2-FIX5-CONTRA.md §5 cites the theme's /1 code asset, whose internal numbering differs from the page sources in this package. The values agree at the package loci cited in the record above; the package's numbers govern.
3. **Four defect flags** stand against the candidate as it stands (sections 1, 2, 4, 7): the dropped license line, the dropped `type=sidebar` frame parameter, and the two minor flags. None was charged by the campaign's checks, and none is dispositioned in the record; they are carried for the coordinator's fix wave, and the candidate is not edited by this package.

### Multi-wave provenance

The candidate's current state is the product of successive waves, not one pass: the Stage 2 CN port (LOCALIZE-S2-D) produced the localization the T4 lane audited; commit 1869877 (FIX-CREDIT-D, translator attribution normalization) settled the credit block's 翻訳責任者 form; FIX5-CONTRA closed the theme's only blocking item as a no-edit disposition, so no FIX5 commit touches this file — its bytes are exactly the ones the FIX5 wave judged (Provenance). Citations, in place of a changelog: GOSIGN2-LEDGER.md §(e) item 66 and the theme's render/localize rows; GOSIGN2-LEDGER-SUPPLEMENT.md item 66; REPORT-GOSIGN2-FIX5-CONTRA.md §5; RENDER-ROWS-RERUN16 (CN9). The go-sign over that record is what the Status block certifies.

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:magicity-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP7, landing `18aa301` (report `R/review-scout/FIX-RDISP7.md`).** Four candidate repairs (+4/−2), postdating this package's build at `1869877` (FIX-CREDIT-D, which the as-built `candidate.txt` matches byte-for-byte).
- **Item 1 — dropped credit license line restored.** The original's credit:more states its own license (original L31, 授权协议：CC-BY-SA 4.0 International); the candidate's only CC mention was the Sigma-Plus base comment (which licenses the base, not this theme). Restored after the last TASL field and before credit:end-preview as `**ライセンス:** CC BY-SA 4.0 International`, the population's field form (frutiger-aero-jp, another-night-jp).
- **Item 2 — interwiki frame `type=sidebar` restored.** The original's frame (original L11–17) is `:scp-wiki-cn:component:interwiki-style` with `priority=3, type=sidebar` and two empty no-ops; the candidate's bare frame kept priority=3 but dropped `type=sidebar`, which no record dispositions. `| type=sidebar` is restored between priority=3 and theme=; the empty no-ops were not restored. The restore adds the standing `interwiki-style-param` warn also carried by the two population files that retain the parameter (shancheng-jp, sci-fi-jp) — a warn, not an error.
- **Item 3 — 'ZCOOL QingKe HuangYou' load added.** The original never names this face (its title face is Smiley Sans Oblique, loaded via the zeoseven import); the name is port-introduced by the disclosed font substitution (Dela Gothic One with ZCOOL QingKe HuangYou fallback in the title stack). The fallback was loaded nowhere in the delivery chain, so `family=ZCOOL+QingKe+HuangYou` was appended to the candidate's one Google Fonts css2 import (L395) — the pastel-skies / cobalt-F3 port-introduced-load remedy. The combined URL serves 200 text/css and declares the family.
- **Item 4 — fossil design-credit link annotation branch.** The original credits fossil as a design reference (original L40); it is not a dependency (Sigma+ is the base), so the drift repoint does not apply. `（中国語版）` was restored after `[*https://scp-wiki-cn.wikidot.com/theme:fossil 化石テーマ]` at candidate L38, in the betwixt-shancheng sibling form. (The report and README cite this link at original L46 / candidate L44; the bytes place it at L40 / L38, pre-repair numbering — substance unchanged.)
Checker per the report: error 15 / warn 2 / info 1 → 15 / 3 / 1. All 15 errors are unchanged class (ii)/(iii) pseudo-refs, class (i) 0; the single warn added is Item 2's interwiki-style-param note. The two pre-existing link-target-missing warns (theme:mox-jp, the-melody-left-in-that-night) are unchanged apart from the +2 line shift.

## Appendix — heuristic and residue adjudication

104 blocks: 61 specific, 43 heuristic, 0 residue. **Heuristic mass by shape:** COMMENT-TEXT (28 spans) is the two big fragments' translated CSS comments, resolved in section 6. The single-line body pairs in the skeleton's appendix listing (R1–R28: B7, B12, B14, B22–B25, B34–B38, B40, B43–B46, B48, B50–B56, B59, B60) are the documentation body's one-to-one translation lines, each verified against the mirror while section 6 was written. The single-line code-css entries (R29–R43: B65, B76, B79, B80, B82, B84, B87–B94) are one-line changes inside the main fragment — comment translations and the `url()` draft-host repoints whose DRAFT-HOST spans sit inside multi-label blocks (section 3 lists them). The GLYPH-FORM blocks (B70, B72, B97, B99, B101) are resolved in section 6 as glyph conversion inside translated comments. B102's WS-ONLY component is a blank line inside the `{$redMode}` gate comment region (candidate L2568) — form only, section 9. No heuristic block conceals a drop: the include census (10 includes in the original, 8 in the candidate — the delta is the credit triple becoming the preview pair and the magicity2 exhibit becoming a prose link, both adjudicated in sections 1 and 7) and the gate census (4 gates on both sides, section 3) close the content-presence check.

## License and attribution

- **Title:** 魔都 版式
- **Author:** OxygenNine
- **Source:** https://scp-wiki-cn.wikidot.com/theme:magicity — revision 20
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
