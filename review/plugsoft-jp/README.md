# Review package — theme:plugsoft-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:plugsoft-jp — origin KO, population #282 [GOSIGN2-LEDGER (b) row 282]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ea2ddebe31ff3984528a32084ebb9ff2700442e8808316f1f48c9d0df2f2547c); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (pseudo-ref×2, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 252; GOSIGN2-LEDGER (b) row 282]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink incl. scpko.wdfiles.com on both pages; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 5 [LOCALIZE-ROWS row 281, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 281]
- FIX5 re-judgement: item 107 (class C) FIXED — FIX5-INFO, commit 9a1c86a: info-module / duplicate credit residue removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 107]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:plugsoft-jp.txt sha256:ea2ddebe31ff3984528a32084ebb9ff2700442e8808316f1f48c9d0df2f2547c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 107 [C] (info-module residue: a second credit/info furniture set rendering beside the credit module) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 107: **FIXED** (FIX5-INFO, commit 9a1c86a); re-derived from this package's bytes in the per-theme record below |
| Standing items | **DISPOSITIONED** — ledger §(c3): P5 (class (ii) / KB-58), P7 (recorded without a display-affecting mark; T4 bar), P9 (ruling 2: header/title language out of scope); ledger §(c2) render row: 884px@768 overflow, runtime-hotlink incl. scpko.wdfiles.com, sample credit-modal preview form (KB-32) |
| Flagged in this package | **Three defect flags**, all in the credit/font apparatus and none of them the item FIX5 closed: (1) the credit block's author field is a pointer naming nobody, and the license box's author parameter repeats the shape (section 1); (2) the candidate loads three Google font families no stack names, while the two Gmarket Sans faces every header stack names are loaded nowhere (section 4); (3) the retained Info Rating Module CSS keeps the pre-KB-11 `.creditButton p a` descendant form (section 1). Exact lines and both sides' text are given in the sections cited and in the batch report |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:plugsoft | theme:plugsoft-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 20, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 20 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-plugsoft.txt` (fetched once by the LOCALIZE-S2-F lane), via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:plugsoft-jp.txt`, copied at worktree HEAD 933c416 |
| Lines / bytes | 541 lines / 12,106 bytes (the last line carries no trailing newline, so `wc -l` reports 540) | 557 lines / 13,680 bytes |
| SHA-256 | a3cb2b4000529c8d46de8abea44d2ab737ff0c89aff31fcac995af58ac0e4ac4 | ea2ddebe31ff3984528a32084ebb9ff2700442e8808316f1f48c9d0df2f2547c |

## Summary

A Korean Sigma-9 theme for the Plugsoft group of interest, designed as a parameterized include: the including page passes `alt` / `theme` / `subtitle` / `custom` arguments and the stylesheet's `:root` resolves them into one of several color variants (green, red, blue, space, blank, black, and a grey default). The candidate keeps that architecture, fixes the parameters to the default variant inside the delivered code, retains the original's own default-supply self-include for direct views, and moves delivery from an inline module to the standard code-exhibit-plus-frame form. Measured churn (diff.md, the generator's difflib count): +131/−115 in 3 hunks; the CSS body below the `:root` block is byte-identical to the original's module. The one blocking item (the leftover info module) is closed and re-derived below; three further defects in the credit and font apparatus are flagged for repair.

## Per-theme record — the FIX5 closure of ledger item 107, re-derived

- **The item.** GOSIGN2-LEDGER.md §(e) item 107 [C]: the LOCALIZE-S2-F row's pattern-3 finding. The candidate carried the EN info module's JP-branch copy (`:scp-jp:info:start` at its L22, `:scp-jp:info:end` at L45) alongside the preview credit module, so two credit/info furniture sets rendered on one page. The pattern-3 exception covers labelled pairs only; this pair was unlabelled residue. The mirror shows the shape's origin: the original itself carries `:scp-wiki:info:start` / `info:end` (original L3/L26) as its credit surface.
- **The re-judgement.** GOSIGN2-LEDGER-SUPPLEMENT.md row 107: FIXED, by FIX5-INFO, commit 9a1c86a: "info-module / duplicate credit residue removed".
- **What the fix was supposed to change.** Delete the candidate's whole info block (both includes and the body between them), leaving the preview credit block as the page's only credit furniture; the preview module is rate-bearing, so no rating surface is lost with it.
- **Re-derivation from this package's bytes.** (1) The fix commit's diff for this file is exactly −25 lines at one locus: the `:scp-jp:info:start` include, the translated info body (title, 制作 line, font/image source lines, spacer lines, the hub div), and the `:scp-jp:info:end` include, removed from between the credit block and the usage heading. (2) Current bytes: `grep -n 'info:start\|info:end' candidate.txt` returns no matches; exactly one credit furniture set stands (candidate L11–20). (3) Completeness: nothing else in the file references the info module's rendering; the CSS that styled it is a separate question, flagged below as flag 3. The closure holds on the current bytes.
- **A consequence the reviewer should see.** The removed info body carried the candidate's only *named* author line in the credit apparatus (制作： [[*user thd-glasses]], from original L5). After the removal, the credit block's author field is the pointer of flag 1. The FIX5 removal was correct; the pointer predates it (the credit waves set the field), but the removal is what left the pointer as the apparatus's only author statement.
- **Post-verdict change.** The usage-example population sweep (b5cb724) completed the usage examples' posting names to `:scp-jp:theme:plugsoft-jp` (candidate L25 and the seven tab exhibits). The generated stamp therefore reads STALE rather than carrying the PASS onto changed bytes; the sweep lines are outside item 107's scope.

## 0. Header / provenance

- What: the original opens with its gate `[[iftags +테마]]` and the info block (original L1–26). The candidate opens with its delivery head (module, L1–3; interwiki frame, L5–8), then the localized gate `[[iftags +テーマ]]` (L9) and the credit block. Provenance route: derivation from the original at revision 20 (mirror class COPY); no supersession note stands against this theme in review/sources.tsv (its notes cell is empty, and nothing in the record contradicts it).
- Why: the delivery head is where this candidate declares its delivery (section 3); the gate and credit furniture follow the JP environment's order (P2/P3).
- Verify: `sha256sum original.txt` against the review/sources.tsv row; read candidate L1–20 against original L1–28.
- Disposition: provenance recorded; nothing to disposition.

## 1. Credit and attribution

- What: the original's credit surface is its info block (original L3–26): title, **제작:** [[*user thd-glasses]], a font-information line (the Gmarket page), image sources (a pixabay illustration; the Plugsoft logo by [[*user lanlanmag]]), and a hub link div. The candidate replaces it with the eight-field preview credit block (candidate L11–20) and adds a JP license box at the tail (L550–555). **Flag 1 (credit pointer).** The block's 著作権者 field (candidate L16) reads 原語版ページの作成者に同じ（scpko の theme:plugsoft) — "the same as the creator of the original-language page": it names nobody. The original names the author in two places (info block L5, 제작 thd-glasses; CSS banner, original L143, "Edited by thd-glasses", with the logo credited to lanlanmag & thd-glasses at L147). The license box repeats the shape: its backend include parameter (candidate L551) is `|author=scpko theme:plugsoft の作者` ("the author of scpko's theme:plugsoft"). The author's name does survive inside the file, in the code banner comment (candidate L163), but no field of the credit apparatus carries it. This is the pointer-in-place-of-a-named-author shape the campaign's credit-repair family exists to fix (compare the alexylva and jiha repairs); it is flagged, not narrated past. The license prose itself (candidate L553) is an honest pointer of a different kind: it defers image/font sources to the original page's record and warns that images without a license statement need author confirmation before posting.
- Why: P3/T1 credit swap and ruling 3 (the eight TASL fields, values evidenced): a field whose value is a direction to look elsewhere fails the field's purpose, which is that the posted page states its attribution.
- Verify: read candidate L16 and L551 against original L5 and L143–147.
- Disposition: P3 FIXED in the ledger's terms (the block exists with all eight fields); **flag 1 stands as a defect for a repair lane**: name thd-glasses in the 著作権者 field and the license-box author parameter (the banner's base-work credits — Sigma-9 by Aelanna and Dr Devan, code adopted from stormbreath's Wilsons and Minimal themes, logo by lanlanmag & thd-glasses — are carried in the banner comment on both sides and need no change).
- **Flag 3 (credit-module CSS form).** The candidate retains the original's "Info Rating Module" CSS section (candidate L456–481), including `.rate-box-with-credit-button .creditButton p a` (L464) and its `:hover` (L469), byte-identical to original L444/L449. In the original that section styled the info module's rate box. The info module is gone (item 107); the rate box that renders now is the JP credit module's, whose frozen markup takes the direct-child form `.creditButton > a` (KB-11's canonical form; the creditbtn landing, canonical 1db8300, corrected six inherited copies of the descendant form, and sodium's was corrected in place as R6). Minor, but it is the same mechanism: flagged for the same in-place correction, with the rate-box prefix kept.

## 2. Includes and components

- What: the candidate's includes are: the interwiki frame (L5–8), the credit pair (L11/20), the defaults self-include (L132–137, section 3), and the license-box pair (L550/555). The usage exhibits (the main example, L25, and the seven variant tabs) are escaped self-includes repointed from `:scpko:theme:plugsoft` to `:scp-jp:theme:plugsoft-jp` (ESCAPED-INCLUDE blocks B7–B26; the posting names were completed by the usage sweep, per-theme record). The info includes stand only in the original (and in the pre-FIX5 candidate; item 107). No include is duplicated: the self-include occurs once live and eight times as escaped exhibits, by design.
- Why: P1 include repointing (branch forms of the same page), with the sweep's settled rule that usage examples name the posting name.
- Verify: `grep -n '\[\[include' original.txt candidate.txt` and compare; the escaped exhibits are the `@@[[include …@@` lines.
- Disposition: standing; no include in the candidate points at scpko.

## 3. Delivery and code loading

- What: a topology consolidation, module-css → code-css. The original delivers from an inline `[[module CSS show="true"]]` inside the hidden `-테마` div (original L135–527) and is parameterized by its include arguments. The candidate consolidates the stylesheet into one `[[code type="css"]]` exhibit (candidate L145–547, inside a collapsible under the ソースコード heading) and delivers it through the head module's @import (L2) and the interwiki frame's theme= (L7), both naming `local--code/theme%3Aplugsoft-jp/1` on the draft host. Self-delivery census: exactly one code block in the candidate, counting every form; both references name block 1, and block 1 is the stylesheet itself (401 content lines), not a small exhibit beside an unreferenced larger block; no entry in FIX-CODEADDR.md or FIX-NAVLA.md names this theme. Parameter handling: the `:root` block fixes the variant parameters to the default set (candidate L170–188: logo `ps_logo_90px_default.png`, `--header-sub: var(--subtitle-0, …)`, `--theme-color: var(--default)`, `--blank: 0`, `--font: var(--default-font, #444)`), and the candidate retains the original's own default-supply mechanism — a hidden self-include passing `alt=0, theme=grey, subtitle=社員急募, custom=#EEE` (candidate L129–140; the original's stands at its tail, L530–541, with the Korean subtitle 직원 급구） — so direct views render the grey default while includers can still pass the documented parameters (the `--subtitle-2: "{$subtitle}"` line, candidate L174, is that contract working, not residue). The porter comment at the code head (L150–155) states the fixing rationale.
- Why: own-code delivery via the standard frame is the campaign's delivery form for page-source themes (P4/T3); the parameter fixing is this theme's judgment call, required because the check environment views the page without include arguments (the KB-06 family concern), and it is executed without deleting the parameter interface.
- Verify: `grep -n 'local--code' candidate.txt` (the two L2/L7 references); count code blocks (one, L145); read candidate L129–140 against original L530–541.
- Disposition: the two draft-host references are class (iii) draft form (the T1 register's pseudo-ref×2), rewritten at posting; the parameter fixing is standing as argued.

## 4. Fonts and assets

- What: **Flag 2 (font load/use gap, KB-16 family, both directions).** The original loads its header faces: `@import url('https://scpko.wdfiles.com/local--files/korean-font/GmarketSans.css')` (original L138), and its stacks name 'GmarketSansLight' (original L177, L288) and 'GmarketSansMedium' (L274). The candidate drops that import (the deletion is residue block B31, aligned at candidate L158 where only `@charset` survives) and instead imports three Google families at the code head (candidate L146–148: Noto Sans JP, Noto Serif JP, Gothic A1). But the candidate's stacks are the original's, unchanged: 'GmarketSansLight' (candidate L197, L308) and 'GmarketSansMedium' (L294) are the only font-family declarations in the file, and no `@font-face` exists anywhere in it. So the two faces every header stack names are loaded nowhere in the file or its delivery chain (the head module and frame point only at fragment 1), and all three loaded families are named by no stack. The porter comment (candidate L154) declares the substitution — 原語版の Gmarket Sans は Google の Gothic A1 で代替しています ("the original's Gmarket Sans is substituted by Google's Gothic A1") — but the substitution is not executed in any declaration. As the file stands, the header surfaces fall back to Arial/sans-serif. Assets: the space-variant background is re-hosted to the candidate's own attachments on the draft host (candidate L182); the header logo stays on scpko.wdfiles.com with the default-variant filename (candidate L171), which is the ledger's P5 disposition (class (ii) / KB-58) and the T2 row's runtime-hotlink line; the T1 hotlink×1 is the same host family.
- Why: KB-16 (a font named in a stack but loaded by no import or font-face in the file or its base delivery is a defect, and the mirror case — loaded but unapplied — is the same census); P5 for the asset hosts.
- Verify: `grep -n 'Gmarket\|Gothic\|font-face\|Noto' candidate.txt` (imports L146–148, comment L154, stacks L197/294/308, and no font-face); `grep -n 'GmarketSans.css' original.txt` (L138).
- Disposition: P5 DISPOSITIONED (class (ii) / KB-58) for the asset hosts; **flag 2 stands as a defect for a repair lane**: either execute the declared substitution in the three stacks or restore a Gmarket Sans load; the ledger's P7 disposition (T4 recorded the JP-font question without a display-affecting mark) does not cover this gap, which concerns the original font's load, not the JP supplement.

## 5. Header, sidebar, site furniture

- What: the header content string is retained in Korean with its ™ (`content: "플러그소프트™"`, candidate L301 = original L281), and the default subtitle fallback string is retained verbatim, mathematical-bold 𝟎 glyph included: `--header-sub: var(--subtitle-0, '제𝟎칙 : 규칙은 없다')` (candidate L173 = original L153, with only the parameter index fixed from `{$alt}` to `0`). The candidate's own credit title fields add the ™ the original's info title lacks (candidate L12/L15 against original L4); the mark matches the theme's own header string, so the fields contradict nothing in the file — recorded as an observation. Sidebar and top-bar CSS is carried byte-identical (section 8).
- Why: P9 header variables are this theme's variant mechanism (section 3); the retained Korean strings are the ledger's P9 disposition under ruling 2 (header/title language is translation taste, out of migration scope).
- Verify: `grep -n '플러그소프트™\|제𝟎칙' candidate.txt original.txt` and compare the pairs.
- Disposition: DISPOSITIONED (P9, ruling 2); the ™ observation is recorded above.

## 6. Text translation

- What: the usage body is translated throughout (original L28–128 → candidate L22–124): the instructions, the seven variant tabs and their captions, and the application-example link texts (TRANSLATION-ANCHORED blocks B6–B28, the batch's dominant class: 16 anchored blocks). The defaults self-include's subtitle is translated (직원 급구 → 社員急募， section 3). The CSS banner comment is retained verbatim in its original Korean/English (candidate L160–168 = original L140–148), including the base-work credits; in-CSS reader-visible strings are the header strings of section 5 (R1: no other string-valued variables carry prose).
- Why: P10 body translation; the banner is porter-visible provenance text and is preserved as the original's record (its translation would erase the attribution form the original chose).
- Verify: read candidate L22–124 against original L28–128 tab by tab; the tab order and the include parameters align one-to-one.
- Disposition: standing (the port itself).

## 7. Links

- What: the credit source link (candidate L19) names the KO original on scpko.wikidot.com, the host recorded in review/sources.tsv (no host substitution). The seven application-example links point at the author's own test pages on scpkosb3.wikidot.com (candidate L38–119), kept with translated captions: they are the original's worked examples on the KO sandbox wiki and no JP counterparts exist. The original info block's hub link (thd-glasses-hub) left the file with the info block in FIX5; it was info-block furniture, not a prose link.
- Why: P11 link localization applies to hub/tag links with JP counterparts; worked-example links to the author's sandbox applications are evidence links and stand.
- Verify: `grep -n 'wikidot.com' candidate.txt` (the credit link and the seven scpkosb3 examples).
- Disposition: standing; no dead-target prose link stands in this file.

## 8. Structure

- What: four structural changes beyond translation. (a) The delivery consolidation of section 3 (module → code exhibit + frame). (b) The defaults self-include is repositioned from the original's tail (original L530–541) to ahead of the code exhibit (candidate L129–140), so the default parameters are established before the exhibit the frame delivers. (c) The original's hidden `-테마` div, which wrapped its delivery module, stands empty in the candidate (L126–127): the module's content moved into the code exhibit, and the div is inert residue of the original's structure, retained rather than silently deleted. (d) The JP license box is appended at the tail (candidate L550–555), after the code exhibit, per the localize.md closing rule that JP additions go at the end. Everything else is preserved: between the `:root` block and the code tail, the candidate's CSS is byte-identical to the original's module (no change blocks between B36 and B37), selectors, variable names, and channel order included. A brace-depth scan of both files' CSS regions (comments and strings stripped) ends at depth 0 in every region with no negative excursion.
- Why: the closing rule (structure preserved, deviations named): each deviation is named here with its ground.
- Verify: compare the structural maps: `grep -n '\[\[module\|\[\[code\|\[\[div\|\[\[iftags' original.txt candidate.txt`.
- Disposition: standing (each change grounded above).

## 9. Formatting only

- What: none of consequence. The classifier counts 0 re-indentation blocks; the code block retains the original's leading-space indentation style throughout, and the translated body keeps the original's layout. The purely mechanical residue is the set of token-level repoints counted in sections 2–3.
- Why: formatting churn is disclosed as its own class (R7); here there is essentially none to disclose, which is itself the follow-up-diff property the closing rule wants.
- Verify: diff.md's 3 hunks; no hunk is whitespace-only.
- Disposition: none required.

## 10. Porter annotations

- What: two annotations. (a) The code-head comment (candidate L150–155, classifier ANNOTATION in B30): it states the port's source (theme:plugsoft rev 20 on scpko), explains that the JP candidate fixes the include parameters to defaults for self-containment, and declares the Gmarket→Gothic A1 font substitution — the declaration flag 2 shows is not executed in the stacks, which is why the annotation is quoted in section 4 rather than trusted. (b) The one-line comment 日本語フォント (JP localization) at candidate L156, marking the import block.
- Why: R2 (porter annotations are part of the change record); an annotation that asserts a change the bytes do not carry is itself evidence, and this package treats it that way.
- Verify: read candidate L150–156.
- Disposition: standing, with flag 2 recorded against (a)'s font claim.

## 11. Dispositions and exceptions

- What: the standing dispositions for this theme, each argued in its own section: (1) P5 asset hosts, class (ii) / KB-58 (section 4); (2) P9 header/title language under ruling 2 (section 5); (3) the P7 JP-font question as T4 recorded it (section 4 states the boundary of that disposition against flag 2); (4) the two draft-host delivery references, class (iii) (section 3); (5) render-row dispositions: 884px@768 overflow and the credit-modal preview form (ruling 5; KB-32). The class (i) defect (item 107) was fixed, not dispositioned. Flags 1–3 are not dispositions; they are open defects this package reports for repair.
- Why: a disposition is a decision with grounds, not an omission; open defects are kept visibly separate from dispositions so the two are never confused.
- Verify: each item names its deciding check in its own section.
- Disposition: DISPOSITIONED (items 1–5 above). Patterns cited in this package are patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa (KB-06, KB-11, KB-16, KB-32, KB-58).

## 12. Verification

- What: (a) T1 baseline for this file: exit 1, 3 errors / 1 warning / 1 info (pseudo-ref×2, hotlink×1, the standing classes of sections 3–4), recorded in the stamp; (b) T2/T3 produced dispositions only (the render row above); (c) T4 records 5 display-affecting findings for this row, of which the pattern-3 charge became item 107 and is closed in the per-theme record; (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and the stamp's STALE state is explained by the post-verdict sweep lines in the per-theme record. Counts in this README are the generator's (difflib, autojunk off): +131/−115.
- Why: verification claims must name the cheapest deciding check and its result, not a general assurance.
- Verify: re-run `python3 review/build_review.py --check` in this repo; `grep -c 'info:start' candidate.txt` (0) for the item-107 closure.
- Disposition: PASS (go-sign re-run, supplement), with flags 1–3 reported for repair.

## Appendix — residue blocks and unanchored mass

- R1 — B31 (residue; orig L138 → cand L158): the GmarketSans.css @import deletion, aligned against the retained `@charset` line. Assigned to section 4 (flag 2).
- Heuristic B4 (orig L10–12 → cand L22–25): the differ pairs the info block's source lines with the usage heading block; the substance is item 107's deletion (the lines left with the block) and the license prose that now points back to them (candidate L553). Assigned to sections 1 and 8.
- Heuristic B37 (orig L527–528 → cand L547–548, CSS-BODY): the code block's closing lines; no content change. Assigned to section 9.
- Heuristic B39 (orig L533–538 → cand L553): the license-box prose paragraph. Assigned to section 1.
- Unanchored translation mass (TRANS-UNANCHORED spans in B2, B3, B5): the head/credit/info-removal zone, where the differ cannot anchor the KO→JP lines. Resolved by shape: sections 0, 1, and the per-theme record, with no content class of their own.

## Change set outside the two diffed files

The diff covers two files; the port's full record is slightly larger. (1) `pages/theme-decoration-sample-plugsoft-jp.txt` — the decoration sample page used by the render checks. (2) The deliveries themselves: the local--code fragment 1 served from the draft host, which is the runtime form of the candidate's code block. No companion fragment or component files belong to this theme; the base is the stock Sigma-9 the theme was written against, inherited from the environment rather than imported by the page.

## Multi-wave provenance

The candidate's current state is the product of successive waves: the Stage 2 KO7 integration (6889a0a) produced the initial port (translation, delivery frame, and, as later found, the leftover info block); FIX-CREDIT-D (1869877) normalized the translator attribution; FIX5-INFO (9a1c86a) removed the info residue (item 107); and the usage-example sweep (b5cb724) completed the posting names. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 107; GOSIGN2-LEDGER-SUPPLEMENT.md row 107; REPORT-GOSIGN2-FIX5-INFO.md (plugsoft section). The go-sign re-run over that record is what the Status block certifies.
