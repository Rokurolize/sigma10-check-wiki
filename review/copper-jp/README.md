# Review package — theme:copper-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:copper-jp — origin CN, population #177 [GOSIGN2-LEDGER (b) row 177]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now d8a336f94e44f9231d32ceb930105c05b93f366617fbf15d63c4d537baaf948c); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 0 warns / 2 infos (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 212; GOSIGN2-LEDGER (b) row 177]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 340px@320 + 896px@768. [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 176, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 176]
- FIX5 re-judgement: item 48 (class B) FIXED — FIX5-FURNB, commit 25bb0b4: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 48]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:copper-jp.txt sha256:d8a336f94e44f9231d32ceb930105c05b93f366617fbf15d63c4d537baaf948c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 48 [B] (duplicate bare Rate) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 48: **FIXED** (FIX5-FURNB, commit 25bb0b4) |
| Standing items | **DISPOSITIONED** — ledger §(c3): P7 (JP font named without an actual load; recorded without a display-affecting mark, T4 bar); ledger §(c2) render row: runtime-hotlink site-theme chain (KB-40), credit-modal preview form (KB-32), page-overflow in the cross-cutting families (KB-33/KB-34); T1 pseudo-ref ×7 (class (iii) draft form) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:copper | theme:copper-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 3, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 3 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-copper.txt` (fetched once by the LOCALIZE-S2-D lane; its working diff is `diff-copper-from3.txt` in the same lane directory) | Canonical file `pages/theme:copper-jp.txt`, copied at worktree HEAD 530cb87; the file's last content changes are commit 25bb0b4 (FIX5-FURNB) and commit b5cb724 (usage-example sweep) |
| Lines / bytes | 372 lines / 9,257 bytes (the last line carries no trailing newline, so `wc -l` reports 371) | 386 lines / 11,201 bytes |
| SHA-256 | 63824ee2dd6f6788cb8cb79cc95ca744d889af865db4cfbfc9a821db1916ac69 | d8a336f94e44f9231d32ceb930105c05b93f366617fbf15d63c4d537baaf948c |

Provenance route: derived from the original at the reference revision (the mirror above, hash-verified against review/sources.tsv). No production-counterpart adoption (R4 does not apply; there is no pages-existing counterpart in this package's record).

## Summary

The original is a small aesthetic variant of the CN Parallel theme: two CSS modules (a gated head module that imports the Parallel base from a CN-wiki code fragment, and an ungated tail module with the theme's own variables) wrapped around a translated exhibit body. The candidate keeps that shape and changes the delivery underneath it: the Parallel base now travels with the theme as its own hosted attachments, loaded through a two-priority interwiki-style frame and again at the head of the tail module, because theme:parallel has no posted JP page. The one blocking defect the sweep found here, a bare Rate module duplicating the rate-bearing preview credit module, was removed by FIX5; this package re-derives that closure from the bytes and the FIX5 commit (per-theme record). The remaining oddities (a JP font named in the stacks with no load of its own, a one-word T5 mistranslation the lane recorded as minor) are standing dispositions, argued in the sections below rather than hidden.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens directly with its tag gate `[[iftags +版式]]` (original L1) and the gated head module; it has no delivery frame. The candidate opens with the delivery frame (candidate L1–8, two interwiki-style includes, section 3), then the localized gate `[[iftags +テーマ]]` (candidate L10) and the head module. Provenance route: this package's original is the lane-cached page source at revision 3 (see Provenance); no live re-fetch was made for this package.
- **Why:** The frame is where the candidate declares its base delivery; its content and its position ahead of the gate are recorded in section 3.
- **Verify:** Read original L1–2 against candidate L1–11.
- **Disposition:** Recorded; part of the delivery change argued under section 3.

### 1. Credit and attribution

- **What:** The original carries the CN credit module as three includes (`:scp-wiki-cn:credit:start` / `credit:more` / `credit:end`, original L45–49) with only the module's own prose lines in source, and a bare `[[module rate]]` in a `[[>]]` wrapper immediately before it (original L41–43). The candidate carries one credit block at candidate L48–57 (`:scp-jp:credit:start-preview` / `end-preview`) with the eight standard fields, and no bare Rate anywhere in the file. The six fields the T4 lane found missing were completed by the credit waves (FIX2-CREDIT, commit 666f543); the bare Rate's removal is the FIX5 item, re-derived in the per-theme record.
- **Why:** P3/T1: the JP preview credit module is the rate-bearing form, so the port replaces the CN credit module and must not keep the original's bare Rate beside it (KB-09; ledger charge class B). Ruling 3 (2026-11-16) fixes the translator credit form used in the block (翻訳責任者: AI).
- **Verify:** `grep -c -i 'module rate' candidate.txt` returns 0; read candidate L48–57 against original L41–49; the FIX5 removal is visible in `git show 25bb0b4 -- pages/theme:copper-jp.txt` (one 3-line deletion).
- **Disposition:** FIXED (ledger §(e) item 48; supplement row 48). The field completion is FIXED as recorded in ledger §(c3) (P3, credit waves, checker-verified).

Per-theme judgment on the fields: the copyright holder field names `[[*user Dr Hormress]]`. The original page source carries no in-source author field (the CN credit module renders attribution from page metadata); the in-source trace is the author's own hosting path in the theme's logo URL (`hormress-s-logos`, original L54), and the credit waves' completion stands checker-verified in the ledger. The title field (candidate L49) keeps the CN title 铜器时代 版式， the same string as the original-title field (L52): no Japanese title form exists anywhere in the candidate body for it to match, and no charge names it (contrast theme:suprematism-jp, item 91, where the body did carry a JP form and the title was fixed to match it).

### 2. Includes and components

- **What:** Original includes: the CN credit trio (L45–49) and `component:image-block` (L87). Candidate includes: the credit preview pair (L48/57), `component:image-block` (L95, same component, its `name=` image re-hosted, section 4), and the two delivery-frame includes (L1–8, section 3). The escaped usage examples change shape: the original shows two includes, `theme:parallel` then `theme:copper` (original L69–70, and again with the `bronze=*` parameter at L76–77); the candidate shows one, `:scp-jp:theme:copper-jp` (candidate L79, and L85 with `bronze=*`), because the candidate bundles the Parallel base itself (section 3) and the porter note at candidate L76 says so.
- **Why:** P1 include repoints (branch form `:scp-jp:` and the posting name with `-jp`). No ruling-4 component port is involved: Parallel is a theme, not a component, and it is bundled as hosted files rather than ported as an include target. A `theme:parallel-jp` candidate exists separately in the population (other themes layer over it); this candidate's delivery does not depend on it.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists; the classifier labels the two usage-example blocks COMPONENT-SWAP and ESCAPED-INCLUDE for the same lines — they are the escaped repoints described here, not component swaps.
- **Disposition:** Standing (the port itself); no include in the candidate points at a CN-wiki page.

### 3. Delivery and code loading

- **What:** Original delivery is split: the gated head module imports the Parallel base CSS from the CN wiki (`@import url("https://scp-wiki-cn.wikidot.com/fragment:parallel/code/1")`, original L3) and adds the theme's override variables; the ungated tail module (original L167–372) is self-contained. Candidate delivery: the ungated frame at L1–8 loads two of the page's own hosted files through interwiki-style, `normalize.min.css` at priority 1 and `parallel.min.css` at priority 2, both on the draft host; the gated head module (candidate L11–42) keeps the override variables and drops the import; the ungated tail module (candidate L176–386) opens by importing the same two hosted files again (candidate L177–178) and adding one `:root { --set-safari-mode-disabled: set; }` line (candidate L180) before the theme's own CSS. The two hosted files are the Parallel base (its normalize layer and its stylesheet) carried as this page's own attachments. The candidate has no `local--code` self-reference at all, so the FIX-CODEADDR audit's census has nothing to check here.
- **Why:** P4/T9 own-delivery form: the base the original fetched from a foreign wiki's code fragment is re-hosted with the theme, because theme:parallel has no posted JP page (the porter note at candidate L76 states this ground). Draft-host URLs are the draft-form class (iii): they are rewritten to the production host at posting time.
- **Verify:** Read candidate L1–8 and L176–180; every delivery URL in the candidate names the candidate's own page files (`theme%3Acopper-jp/…`) on the draft host.
- **Disposition:** DISPOSITIONED (class (iii); the T1 baseline's 7 pseudo-ref errors are these draft-host lines). One redundancy is recorded so a reviewer does not have to re-derive it: the base files are requested twice, once by the frame and once by the tail module's imports, at identical URLs (one fetch after caching). No ledger item charges it and the styling result is the same either way; it is the as-built form of the delivery, not a hidden defect.

### 4. Fonts and assets

- **What:** Fonts: the two stacks in the tail module change their CJK faces. `--mono-font` (original L206: "JetBrains Mono", "Noto Sans SC", monospace) becomes candidate L220 ("JetBrains Mono", "Noto Sans JP", "Noto Sans CJK JP", monospace); `--body-font` (original L209: "Noto Sans", "Noto Sans SC", sans-serif) becomes candidate L223 ("Noto Sans JP", "Noto Sans CJK JP", "Noto Sans", sans-serif). Neither file carries an `@import` or `@font-face` font load: "JetBrains Mono" is named on both sides and loaded by neither, and the JP faces are named without a load of their own. Assets: the three exhibit images move from the author's sandbox hosting (original L54/L58/L60, ah-sandbox) to the candidate's own attachments (candidate L62/L66/L68); the image-block sample logo moves from `bhl.scpwikicn.com` (original L87) to the candidate's own `bhl-logo.svg` attachment (candidate L95); the background photograph moves from the sandbox (original L171) to the candidate's own `quarry.jpg` attachment (candidate L185).
- **Why:** The stack changes are the P7 font-stack rewrite form (JP faces named in Latin/CN stacks). The asset moves are P5 re-hosting to the theme's own storage; at draft stage that storage is the draft host (class (iii)/(ii)).
- **Verify:** `grep -n '@import\|@font-face' original.txt candidate.txt` (no font load on either side); read the stacks at original L206–209 against candidate L220–223.
- **Disposition:** The T4 lane charged the font state as pattern 7 (JP font name only, no actual loading; LOCALIZE-ROWS row 176, at the T4-era lines L217/L220). Ledger §(c3) DISPOSITIONED it: recorded without a display-affecting mark, under the T4 bar. The asset re-hosting is standing (draft-form classes as above).

### 5. Header, sidebar, and site furniture

- **What:** none as a separate change. The theme's furniture-relevant rules are the gated head module's `:root` overrides (original L5–11 → candidate L12–18, byte-preserved) and the light-switch exhibit (original L80–83 → candidate L88–91, an empty collapsible inside `div.light-switch`, preserved in the same shape; the head module's `:root:not(:has(div.light-switch …))` rule keys off it). Neither side defines `--header-title`, `--header-subtitle`, or `--logo-image` overrides; those come from the Parallel base.
- **Why:** The ground for writing "none" here is the grep record below: there is no P8 layout adaptation and no P9/T6 variable supplement in this diff.
- **Verify:** `grep -n -- '--header-title\|--logo-image' original.txt candidate.txt` returns nothing on either side.
- **Disposition:** None required.

### 6. Text translation

- **What:** The exhibit body is translated throughout (original L37–165 → candidate L44–174): the pseudocrumbs alias line, the introduction, the usage prose, the bronze-variant note, the collapsible and tabview labels, the heading samples, the blockquote and table samples. The classifier counts 15 anchored translation blocks and 22 unanchored ones; the unanchored set is the repeated sample lines (the long-tab text alone accounts for eleven of them) and the one-line samples, each verified against the mirror line by line for this package. In-CSS text (R1) is minimal: the one CSS comment in the tail module (the pixabay source URL, candidate L182) is kept verbatim, as in the original. Retained CN strings (R5-adjacent): the credit title fields (section 1) and the `{$bronze}` comment markers around the variant block (candidate L226/L234, the include-parameter's own name, kept as in the original).
- **Why:** P10 body translation is the port's purpose. The T5 half of the T4 row records one mistranslation, treated below.
- **Verify:** Read candidate L44–174 against original L37–165 section by section; the exhibit order is unchanged.
- **Disposition:** Standing (the port itself), with one recorded T5 finding: the bronze-variant note at candidate L82 renders the original's 青色 (original L73, blue-green) as 青銅色 (bronze). The T4 lane judged it a mistranslation (minor; LOCALIZE-ROWS row 176). It was not charged in §(e) and stands unchanged; a reviewer should know the rendered word matches the variant's own CSS block name `{$bronze}` (candidate L226–234), which is the only mitigating fact, not a correction.

### 7. Links

- **What:** The introduction's prose links: the original links `[[[theme:parallel|平行]]]` and `[[[SCP-CN-088|破茧]]]` on the CN wiki (original L66). The candidate renders both as absolute URLs to the same CN pages with Japanese link text (candidate L74), marking Parallel as the Chinese edition （中国語版）; neither target has a JP counterpart the candidate could name instead. The credit block's source link (candidate L56) points back to the original page on scp-wiki-cn, which matches the host recorded in review/sources.tsv. No prose link in the candidate targets an un-suffixed `theme:copper` or `theme:parallel` name on scp-jp.
- **Why:** P11 repoints apply where a JP counterpart page exists; where the linked page is the original itself or a CN-only subject, the link stays pointed at the original and says so.
- **Verify:** `grep -n 'theme:parallel\|scp-cn-088' candidate.txt` (only the absolute CN URLs and the bundled-delivery prose should appear).
- **Disposition:** Standing; no dead-target link is recorded for this theme.

### 8. Structure

- **What:** The page's three-part order is preserved exactly: gated head module, exhibit body, ungated tail module; the localize.md closing rule (structure, variable names, selectors, module ordering preserved) holds. The structural deltas are the delivery ones already recorded: the head module loses its one `@import` line (section 3), the tail module gains two `@import` lines and one `:root` line at its head (candidate L177–180), and the frame is added above the gate (candidate L1–8). The classifier's EXHIBIT-RESTRUCTURE block (original L87 → candidate L95) is the image-block exhibit line: the exhibit is present in the same position with its `name=` image re-hosted — an adjudicated false fire on the URL change, not a restructure. Its CSS-BODY blocks are the removed head `@import` (B2) and the two font stacks (B46/B47, section 4). CSS brace balance was checked by depth, not count: both files end at depth 0 with no negative-depth line.
- **Why:** Structural preservation is what keeps the follow-up diff (the T4 mechanism) applicable; deviations need a name, and the three above are the complete set.
- **Verify:** Compare the structural maps: `grep -n '\[\[module\|\[\[iftags\|\[\[/iftags' original.txt candidate.txt`.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** None. The classifier finds 0 whitespace-only blocks and 0 re-indentation blocks in this pair. The whole diff (build_review.py, difflib) is +109/−100 changed lines in 3 hunks; the classifier's finer SequenceMatcher pass counts 47 change blocks (25 specific, 22 heuristic, 0 residue). Every changed line is accounted for by the sections above.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change (the R7 hazard does not arise here).
- **Verify:** diff.md's summary table and the classifier counts quoted above.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter annotation was added inside the candidate: the **訳注** at candidate L76, stating that Parallel is an SCP-CN theme not posted on SCP-JP, that the JP candidate loads its own bundled copy of it (the attachments of section 3), and that the form is to be replaced once Parallel itself is posted. It is the explanation a reader needs for why the usage example in section 2 has one include where the original has two.
- **Why:** Residue class R2 (porter annotation additions): annotations added by the porter are part of the change record, and this one is load-bearing — it documents a delivery decision.
- **Verify:** Read candidate L76 against the usage examples at candidate L79 and L85.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section or the ledger rows cited: (1) the T1 pseudo-ref ×7 — the candidate's own draft-host file URLs, class (iii), rewritten at posting (sections 3–4); (2) the render-row dispositions: runtime-hotlink site-theme chain (KB-40, environment layer, not the candidate), credit-modal preview form (KB-32; ruling 5), page-overflow 340px@320 + 896px@768 in the cross-cutting static-credit/preview-chrome families (KB-33/KB-34); (3) the P7 font disposition (section 4); (4) the T5 青銅色 finding (section 6). No item for this theme is left as an unexplained exception, and no class (i) item stands.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the FIX5 closure is re-derived in the per-theme record below from the current bytes and the FIX5 commit itself; (b) the T1 baseline recorded at 2026-11-16 is exit 1, 7 errors / 0 warns / 2 infos, all 7 errors pseudo-ref (T1-ROWS row 212) — that baseline predates FIX5, and one of its two infos is the double-rate info whose clearing the FIX5-FURNB commit message records across its 9 files; (c) T2/T3 produced dispositions only, no open finding (ledger §(c2)); (d) the brace-depth scan run for this package ends at depth 0 on both files; (e) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib): +109/−100.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** `grep -c -i 'module rate' candidate.txt` (0), `git show 25bb0b4 -- pages/theme:copper-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### The FIX5 restoration (ledger item 48)

At ledger time this candidate rendered two rating widgets: the preview credit module at the top of the body is rate-bearing, and the port had kept the original's bare `[[module rate]]` (in its `[[>]]` wrapper) standing immediately before the credit block — the original's own arrangement (original L41–49), where the CN credit module is not rate-bearing and the bare module is the page's only rating surface. The T4 lane charged it as 評価 UI 二重化 (display-affecting, minor; LOCALIZE-ROWS row 176, at the T4-era lines L52–54), and the ledger carried it as §(e) item 48 [B], noting the defined fix (delete the bare module) had been executed for other row sets but never for this row. FIX5-FURNB (commit 25bb0b4) deleted exactly three lines in this file — the wrapper and the module — and nothing else; the commit message records the double-rate infos clearing on all 9 files of its set. Re-derivation from this package's bytes: the original has exactly one `[[module rate]]` (original L42); the candidate has none; the only rating surface left is the preview credit module, which is the campaign's settled form. The supplement's FIXED (row 48) is confirmed, not merely cited.

### The usage example's posting name

The include census in section 2 covers the corrected candidate. As built, the candidate's two escaped usage examples named `:scp-jp:theme:copper`, the original's slug on the JP branch — a page that does not exist on scp-jp, under the campaign's settled rule for usage examples (AGENTS.md §6). The usage-example population sweep has since completed the name to this candidate's posting name, `:scp-jp:theme:copper-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724). This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) The hosted files the delivery and exhibits name — `normalize.min.css`, `parallel.min.css`, `ARED_2.svg`, `parallel-theme-logo.svg`, `parallel-theme-logo-zh.svg`, `bhl-logo.svg`, `quarry.jpg` — carried as attachments of theme:copper-jp on the draft host (at posting, of the posted page on the production host); they are hosted files, not repo files, and the two CSS files among them are the Parallel base this port depends on. (2) `pages/theme-decoration-sample-copper-jp.txt` — the decoration sample page used by the render checks. The original side of the change set is the CN fragment the shell pointed at (`fragment:parallel` on scp-wiki-cn), whose content enters the record only through hosted file set (1). The `start-themes.tsv` row records this theme's base as "standalone".

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave produced the initial port (translation, bundled-Parallel delivery, exhibit body, and, as later found, the retained bare Rate); FIX2-CREDIT completed the six missing credit fields; FIX5-FURNB removed the duplicate Rate; and the usage-example sweep completed the posting name. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 48; GOSIGN2-LEDGER-SUPPLEMENT.md row 48; LOCALIZE-ROWS row 176; T1-ROWS row 212; commits cad7c86 (Stage 2 CN4 integration), 666f543 (FIX2-CREDIT), 25bb0b4 (FIX5-FURNB), b5cb724 (usage sweep). The go-sign re-run over that record is what the Status block certifies. Patterns cited in this package are at patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
