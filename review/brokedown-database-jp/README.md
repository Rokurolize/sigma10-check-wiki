# Review package — theme:brokedown-database-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:brokedown-database-jp — origin CN, population #170 [GOSIGN2-LEDGER (b) row 170]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 921a7325b13ea6ca57c292a93e23c8b40b8a3e837a60c332d9bcbb062c2fd536); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 2 warns / 1 info (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 148; GOSIGN2-LEDGER (b) row 170]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page page-overflow 328px@320 chromium (8px), runtime-hotlink site-theme chain only; sample credit-modal (preview-form), page-overflow 341px@320 + 389px@375 chromium and 416px@320 + 419px@375 webkit (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host; T3 complete in the final report (pending in the partial) and clean on both pages (sidebar collapsed at PC width with left-edge toggle tab present, mobile hamburger opens in both engines, cyan-on-black readable); missing decorative logos = deferred assets. [RENDER-ROWS-RERUN16 (CN2) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN2)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 169, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 169]
- FIX5 re-judgement: item 46 (class I) FIXED — FIX5-STRUCTB §1, commit 435a6bb: no-animation gated block (L1631-1680), my-logo gated block (L1683-1704) and the photosensitivity warning block (L248-266) restored from original L1623-1698 / L1152-1170; spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) item 46; (c) check 7]
- Computed against: canonical commit 8dede754299cda919702130296e7c2131e4e6fce; candidate file pages/theme:brokedown-database-jp.txt sha256:921a7325b13ea6ca57c292a93e23c8b40b8a3e837a60c332d9bcbb062c2fd536; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 46 [I] (documented feature blocks missing; photosensitivity warning deleted) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 46: **FIXED** (FIX5-STRUCTB, commit 435a6bb) |
| Standing items | **DISPOSITIONED** — ledger §(c2) render row (RENDER-ROWS-RERUN16): runtime-hotlink site-theme chain (KB-40), credit-modal preview form (KB-32), page-overflow in the cross-cutting families (KB-33/KB-34), missing decorative logos as deferred assets (KB-58); T1 pseudo-ref ×5 (class (iii) draft form) |
| Flags raised by this package | 4, none of them dispositioned by any campaign register: the dropped pixel-code attribution line (section 1), the font delivery incoherence (section 4), the un-repointed fragment link, dead on the JP side (section 7), and the dropped Rate/credit exhibit row (section 8). They do not disturb the frozen verdict record; they are repair-queue candidates |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:brokedown-database | theme:brokedown-database-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 43, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 43 | — |
| Source of this copy | Campaign mirror store `review-mirrors/orig-brokedown-database-rev43.txt` (fetched once by the campaign; the LOCALIZE lane's working diff is `diff-brokedown-database-from43.txt`) | Canonical file `pages/theme:brokedown-database-jp.txt`, copied at worktree HEAD 530cb87; the file's last content changes are commit 435a6bb (FIX5-STRUCTB) and commit b5cb724 (usage-example sweep) |
| Lines / bytes | 1,704 lines / 47,277 bytes | 1,704 lines / 51,509 bytes |
| SHA-256 | 8ae0902d4375012b20a243ce5e9dc4779a7ba90ad1fde68812edff91958ed58e | 8191e19176b08f8af4bb46dfad10307d1d843d2f0f8a22c1da0e62344f831fbe |

Provenance route: derived from the original at the reference revision (the mirror above, hash-verified against review/sources.tsv, which classes this row K5b-4, component-bearing: the two companion fragments in the change set below are part of the port). No production-counterpart adoption (R4 does not apply).

## Summary

The original is a Black Highlighter variant by etinjat whose CSS ships as two code files exhibited on the page itself, with a documentation body that teaches two include parameters (`no-animation`, `my-logo`), a photosensitivity warning, and credit exhibits. The candidate re-bases the theme on the JP Black Highlighter candidate, merges the two code files into one self-delivery exhibit, repoints the author's two components to their JP fragment ports, and adds the campaign's standard credit block and license box. The sweep's blocking item was structural: the port had dropped the implementation blocks for both documented parameters and the warning block, so the documentation taught features that did nothing. FIX5 restored all three from the original, translated, with a provenance comment; this package re-derives that closure block by block (per-theme record). Four smaller defects no register records are flagged in the sections below with their evidence.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with its tag gate (original L1) and immediately exhibits its first code file inside a collapsible (original L2–3). The candidate opens with the JP base include `:scp-jp:theme:black-highlighter-theme` (candidate L1), a head `[[module CSS]]` importing the candidate's own code block 1 from the draft host (candidate L3–5), and the delivery frame (candidate L7–18: interwiki-style at priorities 1–3, the third naming the candidate's own block 1), ahead of the credit block. Provenance route: this package's original is the campaign mirror at revision 43 (see Provenance); no live re-fetch was made for this package.
- **Why:** The head module and frame are the candidate's delivery declaration; their targets are recorded in section 3.
- **Verify:** Read original L1–3 against candidate L1–18.
- **Disposition:** Recorded; argued under section 3.

### 1. Credit and attribution

- **What:** The original has no credit block at the head of the page. Its attribution lives in three places: the credit exhibits inside the documentation body (original L1184–1195, section 8), the code files' banner comments, and a footer attribution line (original L1591). The candidate carries the preview credit block at candidate L21–31 (`:scp-jp:credit:start-preview` / `end-preview`) with the eight standard fields （著作権者 `[[*user etinjat]]`, 作成年 2022, reference revision 43, source link to the CN page, which matches the host recorded in review/sources.tsv), and adds a JP license box at candidate L1606–1623 (`license-box-backend` with `author=etinjat`, closed by `license-box-end`) holding four entries: the SCP logo, the wiki-down image, the author's two components, and fonts. Where the original states no license for an entry, the entry says so in those words; the original has no license box at all.
- **Why:** P3/T1: the preview credit module is the campaign's settled credit form, and the license box carries the TASL record ruling 3 (2026-11-16) requires, with adaptations and unknowns stated rather than smoothed over.
- **Verify:** Read candidate L21–31 and L1606–1623; compare the author name against the original's banner and footer line.
- **Disposition:** Standing (the port itself), with one flag. **Flag (attribution line dropped):** the original's footer line (original L1591) credits two things: the layout to etinjat and the on-screen pixel-dot code to the scp-style-resource format-resource page. The etinjat half survives (credit block, license box, banners). The pixel-code half has no prose counterpart anywhere in the candidate: it survives only inside the code exhibit's banner comment (candidate L485, untranslated Chinese, with its original `http://` URL). The T4 lane charged this loss (LOCALIZE-ROWS row 169, display-affecting list); FIX5 did not restore it and no register dispositions it. The repair is one line in the license area or footer naming the pixel-code source; this package records the flag and does not edit the candidate.

### 2. Includes and components

- **What:** Candidate includes: the BHL base include (candidate L1); the credit preview pair (L21/31); the two companion components are not included but imported: inside the code exhibit, the original's `@import`s of the author's CN components (`component:collapsible-sidebar/code/1` and `component:centered-header-bhl/code/2`, original L17–18) are repointed to the JP fragment candidates `fragment:collapsible-sidebar-jp-base-css` and `fragment:centered-header-bhl-jp-base-css` (candidate L459–460), joined by the JP BHL stylesheets (candidate L461–462), with porter comments at candidate L456–458 and L467–474 explaining the substitution. The original's typeface include (`:etinjat:typeface-cn`, original L1613–1615) has no counterpart; its consequence is recorded in section 4. The credit exhibits the original includes inside its body are treated in section 8.
- **Why:** Ruling 4 (2026-11-16): components a theme needs are ported together with the theme; the two fragments are those ports, and the start-themes record names them as this theme's base. P1 repoints cover the base include and the credit pair.
- **Verify:** `grep -n '\[\[include\|@import' original.txt candidate.txt` and compare the two lists against the companion files named in the change set.
- **Disposition:** Standing (the port itself); the typeface include's absence is part of the section 4 flag, not a separate item.

### 3. Delivery and code loading

- **What:** The original exhibits its CSS as two code files on the page (code blocks at original L3 and L1124) and delivers them through a self-import module near the tail (`@import` of its own code/1, original L1618–1620) plus a tail frame naming its own block 2 (original L1701–1704). The candidate consolidates delivery at the head: the head module and the frame's third priority both name the candidate's own block 1 on the draft host, and the candidate exhibits both of the original's code files inside a single `[[code type="css"]]` exhibit (opening at candidate L455; file 1's banner at candidate L478–489, file 2's banner at candidate L1590), so block 1 is the merged stylesheet and the self-delivery address is correct. The original's self-import module and tail frame have no counterparts because their job moved to the head. The FIX-CODEADDR population audit's census is satisfied here: every `local--code/theme%3Abrokedown-database-jp/1` reference names the block that actually holds the CSS.
- **Why:** P4/T9 own-delivery form, with the exhibit consolidation forced by it: one delivery address can only name one block, so the two files merge into one exhibit and the banners keep the boundary visible.
- **Verify:** `grep -n 'local--code' candidate.txt` (the head module and the frame, both naming block 1); read the two banners at candidate L478–489 and L1590.
- **Disposition:** Standing (draft-host URLs are class (iii), rewritten at posting; the T1 baseline's 5 pseudo-ref errors are these lines).

### 4. Fonts and assets

- **What:** The original imports ZCOOL XiaoWei inside code file 1 with a malformed, triple-encoded query (`&amp;amp;amp;`, original L20); the candidate carries the clean form (candidate L463) and adds two JP loads, Noto Sans JP and Noto Serif JP (candidate L464–465). The stacks, however, are byte-identical on both sides (original L23–28 → candidate L498–501) and sit under the file's only `:lang` rule, `:root:lang(cn)`; no `:lang(ja)` rule exists. They name CN faces (Dotted Songti Square, 等线， 华文中宋， 微软雅黑） that no load in the candidate provides: the original's loader for the headline face was the typeface include dropped in section 2. The candidate's prose still teaches Dotted Songti Square as the body font and ZCOOL XiaoWei as the mono font (candidate L163–164); of those two, only ZCOOL is actually loaded. Assets otherwise: the `--icon-scp` URL is repointed to the candidate's own draft-host file `logo-scp.svg` (candidate L783), and the license entries' images are the candidate's own attachments (section 1).
- **Why:** P7 covers stack rewrites and loads; a load no stack names, and a stack naming faces no load provides, are both delivery facts a reviewer needs stated plainly.
- **Verify:** `grep -n '@import' candidate.txt` (L459–465 inside the exhibit); read candidate L498–501 against original L23–28; `grep -n 'lang(' candidate.txt` (one rule).
- **Disposition:** **Flag (font delivery incoherence), raised by this package.** The JP loads were added (the JPFONT-LOAD shape) but the stacks were never rewritten to name them, while the CN faces the stacks do name lost their only loader with the typeface include. Whether the right repair is stack localization, restoring a typeface channel, or both is a porter decision; the bytes as they stand do not deliver the fonts the file's own prose promises. No register records this state.

### 5. Header, sidebar, and site furniture

- **What:** The furniture comes from the base and the companions: the candidate layers on the JP Black Highlighter candidate (candidate L1) and imports the ported collapsible-sidebar and centered-header fragments (section 2), which is the original's own architecture with JP targets. The theme's own furniture CSS (scanline header, logo treatment) lives in the code exhibit on both sides. The render row verified the result: sidebar collapsed at PC width with the left-edge toggle tab, mobile hamburger opening in both engines, cyan-on-black readable (ledger §(c2), RERUN16).
- **Why:** No P8 layout adaptation or P9/T6 variable supplement of the theme's own occurs in this diff; the furniture change is entirely the base/component repointing of section 2.
- **Verify:** The include/import lists of section 2; the exhibit's furniture rules are inside the merged code exhibit (candidate L455 onward).
- **Disposition:** Standing; T3 dispositions recorded in section 11.

### 6. Text translation

- **What:** The documentation body is translated throughout, including the restored blocks (section 12 and the per-theme record): the warning block's three sentences (candidate L248–266, from original L1152–1170, keeping the original's spaced 警 告 heading), and the restored implementation blocks' comments （停止动画 → アニメーション停止 and parallels). The code files' banner comments stay in Chinese verbatim: they are the exhibited files' own headers, carried as content, and the second banner is where the section 1 attribution survives. The gate tag is localized （版式 → テーマ）.
- **Why:** P10 body translation is the port's purpose; exhibited code banners are content, not prose, and translating them would falsify the exhibit.
- **Verify:** Read candidate L248–266 against original L1152–1170; read the banners at candidate L478–489.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit block's source link (candidate L29) points back to the original page on scp-wiki-cn, matching the host recorded in review/sources.tsv. One prose link fails: the base64 postscript (candidate L61, translated from original L1223) links `[/fragment:brokedown-database ロゴ用パラメータ]` — a relative link. On the CN wiki the same relative link resolves to the theme's live companion fragment page (probe 2026-11-17: 200). On the JP check wiki the name does not exist (probe 2026-11-17: 404; the theme page itself returns 200), and the candidate's actual delivery runs through its own block 1 and the two JP fragment companions, not through any `fragment:brokedown-database` page.
- **Why:** P11: a link naming a counterpart page must be repointed to that counterpart or absolutized to the original; carried over unexamined, a relative link silently changes target with the host.
- **Verify:** The two probes above are the deciding check; the link text is at candidate L61.
- **Disposition:** **Flag (un-repointed link), raised by this package.** The repair is to absolutize the link to the CN original or remove it with the delivery change; this package records the flag and does not edit the candidate.

### 8. Structure

- **What:** The port reorders the page: the original runs gate → code exhibit 1 → body (warning, exhibits, prose) → code exhibit 2 → license-less tail with self-import, implementation blocks, and tail frame; the candidate runs base include → delivery head → credit → usage exhibits and body → license box → restored implementation blocks. The two code exhibits merge into one (section 3). One original structure has no counterpart at all: the exhibit flex row (original L1176–1195), a `.flex-wrap` row of three `.flex-cell`s holding a bare `[[module Rate]]` exhibit (original L1180) and the two credit-module exhibits (`credit:start`/`end` and `credit:start-standalone`/`end-standalone`, original L1184–1195). The candidate contains no `[[module Rate]]` and no flex-row markup; only an unrelated CSS `flex-wrap: nowrap` rule survives (candidate L1336). The classifier's RATE-EXHIBIT-KEPT-CANDIDATE label on its block B43 fired from the original-side span alone and is wrong for the candidate side; it is adjudicated here as a drop, not a keep. CSS brace balance was checked by depth, not count: both files end at depth 0 (maximum depth 2) with no negative-depth line. The classifier's three residue blocks resolve as: B35, a blank line inside code file 2 deleted in the exhibit (formatting); B36, the original's comment fence after code file 2 (original L1139–1143) not carried over (a porter-side fence, no content); B49, blank lines before the my-logo gate (formatting).
- **Why:** Structural preservation is the localize.md closing rule; deviations need names. The reordering and the consolidation are the port's declared shape; the exhibit-row drop is not declared anywhere.
- **Verify:** `grep -c -i 'module rate' candidate.txt` (0) against original L1180; read original L1176–1195 and search the candidate for `flex-cell` (absent).
- **Disposition:** **Flag (dropped exhibit row), raised by this package.** Mitigating fact, stated so the flag is not over-read: the page is not rate-less — the preview credit block is rate-bearing — and what was dropped is documentation exhibits, not function. No register records the drop; the FIX5 restoration (which worked from the same original region) did not restore it either.

### 9. Formatting only

- **What:** 29 whitespace-only blocks, each a single blank-line deletion inside the merged code exhibit, plus the two formatting residue blocks named in section 8. The whole diff (build_review.py, difflib) is +534/−535 changed lines across 15 diff sections, presented as Tier 2; the classifier's SequenceMatcher pass counts 51 blocks (37 specific, 11 heuristic, 3 residue, all three residue blocks resolved in section 8).
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change (R7); here it is a small, exactly located part of a large diff.
- **Verify:** diff.md's summary table and the classifier counts quoted above.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three porter annotations ride inside the candidate: the component-substitution comments at candidate L456–458 and L467–474 (why the author's CN components are replaced by the JP fragment ports, section 2), and the FIX5 provenance comment at candidate L1627–1629, which states that the blocks following it were restored, translated, from the original's L1623–1698 because the documented parameters had no effect without them. The second is part of the FIX5 evidence chain and is quoted in the per-theme record.
- **Why:** Residue class R2: porter annotations are part of the change record, and the provenance comment is load-bearing for the FIX5 re-derivation.
- **Verify:** Read candidate L456–458, L467–474, and L1627–1629.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, from the render row (RENDER-ROWS-RERUN16, ledger §(c2)): (1) page-overflow 328px at 320px viewport, chromium, 8px over — the cross-cutting static-credit family (KB-33/KB-34); (2) the sample page's credit-modal behavior is the preview form's property (KB-32; ruling 5), with its overflow readings (341px@320 + 389px@375 chromium; 416px@320 + 419px@375 webkit) in the same cross-cutting families; (3) runtime-hotlink limited to the site-theme chain (KB-40, environment layer); (4) missing decorative logos are deferred assets (KB-58), an asset-hosting item, not a theme defect; (5) the T1 pseudo-ref ×5, class (iii) (section 3). T3 was complete and clean on both pages in both engines. The four flags in sections 1, 4, 7, and 8 are not dispositions: no register decides them, and this section does not pretend otherwise.
- **Why:** A disposition is a decision with grounds, not an omission; open flags are listed as open so the set can be audited in one place.
- **Verify:** Each disposition names its record above; each flag names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (items 1–5); flags open.

### 12. Verification

- **What:** The evidence behind the stamp: (a) the FIX5 closure is re-derived in the per-theme record below from the current bytes and the FIX5 commit itself (`git show 435a6bb` adds 101 lines to this file: the warning block, both gated blocks, and the provenance comment); (b) the supplement's own spot-check (§(c) check 7) confirms the gated blocks at candidate L1631/L1683 with the provenance comment at L1628, matching this package's reading; (c) the T1 baseline recorded at 2026-11-16 is exit 1, 5 errors / 2 warns / 1 info, all 5 errors pseudo-ref (T1-ROWS row 148); (d) T2/T3 produced dispositions only, no open finding (ledger §(c2)); (e) the brace-depth scan run for this package ends at depth 0 on both files; (f) the section 7 probes were run for this package on 2026-11-17 (check wiki 404, CN 200); (g) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib): +534/−535.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** `git show 435a6bb -- pages/theme:brokedown-database-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement), with the four open flags of sections 1, 4, 7, 8 recorded alongside.

## Per-theme record

### The FIX5 restoration (ledger item 46)

The ledger's item 46 [I] charged three losses from the same cause: the S2 port had carried this theme's documentation but not the machinery the documentation describes. (1) The `no-animation` implementation block (original L1632–1671, an `[[iftags [[#ifexpr {$no-animation} …]]]]` gate wrapping a module CSS that kills the scanline animations) was absent; the parameter name occurred in the candidate only inside the usage exhibit. (2) The `my-logo` block (original L1685–1695, the same gate form, setting the header logo from `{$logo-url}`) was likewise absent. (3) The photosensitivity warning block (original L1152–1170) had been deleted outright. The candidate's guide exhibits (candidate L44–60) documented both parameters, so a user following the page got no effect from either.

FIX5-STRUCTB (commit 435a6bb) restored all three from the original, translated, and said so in the file: the provenance comment at candidate L1627–1629 states the blocks were restored from the original page's L1623–1698 because the parameters had no effect without them. Re-derivation from this package's bytes: the warning block stands at candidate L248–266, its three sentences matching original L1152–1170; the no-animation gate stands at candidate L1631–1680, its selectors and rules matching original L1632–1671 with the comments translated; the my-logo gate stands at candidate L1683–1704, matching original L1685–1695 including `background: {$logo-url}`; and the candidate now ends at L1704 with that gate's `[[/iftags]]`, where the original continued to its tail frame (original L1701–1704), whose job the candidate's head frame does instead (section 3). The supplement's FIXED (row 46) is confirmed, not merely cited. What FIX5 did not restore from the same region of the original — the exhibit flex row and the pixel-code attribution line — is flagged in sections 8 and 1 respectively.

### The usage example's posting name

The usage exhibits at candidate L44–60 name this candidate by its posting name, `:scp-jp:theme:brokedown-database-jp`, in split-markup include form. The usage-example population sweep is the last change to this file (canonical commit b5cb724); the stamp reads STALE against the pre-sweep verdict, by design, and no re-judgement is claimed for the changed bytes.

### Post-package repairs (REFRESH3-G)

- **FIX-BROKEDOWN, landing `8dede754299cda919702130296e7c2131e4e6fce`** ("pages: brokedown-database attribution, exhibit row, fragment link, fonts", 2026-11-17, R/review-scout/FIX-BROKEDOWN.md; 1704 → 1731 lines, +34/−7). Four items, all confined to this candidate:
  - **BD-1 — pixel-code attribution restored.** The line `= 本テーマは [[*user etinjat]] が制作し、画面のピクセルドットコードは [*https://scp-wiki-cn.wikidot.com/scp-style-resource 格式资源] に由来します。` stands at refreshed candidate L1650, the end of the gated documentation body after the license box (`license-box-end` at L1648), keeping the original's centered standalone form. The code-exhibit's banner copy is untouched.
  - **BD-2 — exhibit flex row and its layout rule restored.** The `.flex-wrap` row of three `.flex-cell`s stands at L270–289 (bare `[[module Rate]]` at L274, the `credit:start`/`end` exhibit, and the `credit:start-standalone`/`end-standalone` exhibit, the credit includes in the candidate-side `:scp-jp:` form); its `.flex-wrap{display:flex;justify-content:space-between;}` rule is restored verbatim at L1624–1627, immediately before `[[/code]]`. The bare Rate is the original's labelled exhibit specimen, not a head-zone duplicate; the new `double-rate` info adjudicates itself (見本として並べているなら可).
  - **BD-3 — fragment link repointed.** The PS line at L61 now absolutizes `fragment:brokedown-database` to `https://scp-wiki-cn.wikidot.com/fragment:brokedown-database` with the （中国語版） annotation. The fragment was not ported: it is unincluded by the original and its data already ships in the theme's own code (ruling 4 covers needed components).
  - **BD-4 — fonts aligned to the loads.** `:root:lang(cn)` → `:root:lang(ja)` at L517, with the four stacks at L518–521 now naming Noto Serif JP / Noto Sans JP in place of the CN faces; specimen prose at L163 reads 「本文フォントはNoto Serif JPです」. Every loaded family is named and every named family is loaded, a system face, or generic.
The "FIX5 restoration" subsection's note that the flex row and pixel-code attribution were "flagged in sections 8 and 1" is the as-built record; both are now repaired in the recopied candidate. Checker: error 5 / warn 2 / info 1 → error 5 / warn 2 / info 2, all errors pseudo-ref, class (i) 0 before and after.

The regenerated stamp reads `Overall: STALE` against the pre-repair verdict, by design; no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/fragment:centered-header-bhl-jp-base-css.txt` and `pages/fragment:collapsible-sidebar-jp-base-css.txt` — the JP ports of the author's two components, imported by the candidate's code exhibit (section 2); the `start-themes.tsv` row records this theme's base as those two fragments (@import) plus its own code. (2) The hosted files the exhibits and license entries name (the SCP logo SVG, the wiki-down image, and the theme's other attachments) on the draft host — hosted files, not repo files. (3) `pages/theme-decoration-sample-brokedown-database-jp.txt` — the decoration sample page used by the render checks.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave produced the initial port (translation, merged self-delivery, component repoints, credit and license furniture, and, as later found, the dropped implementation blocks, warning, exhibit row, and attribution line); FIX5-STRUCTB restored the three charged losses; and the usage-example sweep completed the posting name in the exhibits. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row, RERUN16), §(e) item 46; GOSIGN2-LEDGER-SUPPLEMENT.md row 46 and §(c) check 7; LOCALIZE-ROWS row 169; T1-ROWS row 148; commits 435a6bb (FIX5-STRUCTB) and b5cb724 (usage sweep). The go-sign re-run over that record is what the Status block certifies. Patterns cited in this package are at patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

## License and attribution

- **Title:** 故障数据库 主题版式
- **Author:** etinjat
- **Source:** https://scp-wiki-cn.wikidot.com/theme:brokedown-database — revision 43
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
