# Review package — theme:fandom-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:fandom-jp — origin EN, population #87 [GOSIGN2-LEDGER (b) row 87]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0a404e636e7e155be120c75c52193bdd38e9d8316089347d78bad34bdaab6b27); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 87; GOSIGN2-LEDGER (b) row 87]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — candidate's purple header wordmark overprints account links at ≤375 both engines (notice ends clipped at right); chameleon.gif 404 = owner-deferred EN9. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 87, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 87]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 87]
- Computed against: canonical commit 49a1e493cc9756c0314b065a789dbdb226faf5df; candidate file pages/theme:fandom-jp.txt sha256:0a404e636e7e155be120c75c52193bdd38e9d8316089347d78bad34bdaab6b27; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/fandom-jp/candidate.txt (sha256 86241a24d2613a5e754bef7b7dc8ff586a4f4e54cc98e8afe7515903a30d9efe)
Original: theme:fandom — scp-wiki, revision 6 (sha256 3afab5c105f9d7579022bfff955be8c3490b1445ff08defce17a053c45678ed5)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 87); one of the 286 of 286 pass-eligible themes |
| Post-verdict change | One line: the usage-example sweep (canonical commit b5cb724) completed the usage exhibit's self-include to the `-jp` name. The generated stamp therefore reads **STALE**; its verdict lines describe the pre-sweep file. The wave edits below (1869877) predate the FIX5 head and are inside the judged bytes |
| Standing items | **DISPOSITIONED** — T1 baseline pseudo-ref×2 (class (iii), section 11); the render row's two items (the narrow-width wordmark family, KB-35; the chameleon.gif 404, owner-deferred EN9 / KB-58); T4's P1 (ledger (c3), posting-procedure convention class) |
| Noted, unrepaired | The prose links at cand L28 and L30 still point at EN pages with no （英語版） annotation, although a JP toggle-sidebar component exists (section 7). The LOCALIZE-S2-B lane recorded this as a minor pattern-11 miss; no ledger line dispositions it and no wave repaired it |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:fandom | theme:fandom-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 6, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 6 | — |
| Source of this copy | Campaign mirror store (hash-verified against review/sources.tsv) | Canonical file `pages/theme:fandom-jp.txt`, created in commit 7aed5b7 (Stage 2 EN9 integration); its last content change is commit b5cb724 (the usage-example sweep) |
| Lines | 393 (generator count, diff.md) | 415 (generator count, diff.md) |
| SHA-256 | 3afab5c105f9d7579022bfff955be8c3490b1445ff08defce17a053c45678ed5 | 86241a24d2613a5e754bef7b7dc8ff586a4f4e54cc98e8afe7515903a30d9efe |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart exists, so the R4 question does not arise. Reference-revision currency: revision 6 is still the upstream latest — the T4 follow-up artifact `diff-fandom.txt` in the LOCALIZE-S2-B lane records rev6 → rev6, no changes. sources.tsv carries no superseded-upstream note for this row, correctly.

Wave history: the port itself (7aed5b7) already carried the head-delivery restructure, the JP font supplement and the added license box. One later wave edited the file: FIX3-S2EN's Class 2 repoint of the base include, which rode into commit 1869877 together with the FIX-CREDIT-D translator normalization. The usage-example sweep (b5cb724) is post-verdict. The Multi-wave provenance section gives the full chain.

## Summary

The original is a small Sigma+ theme by Fish^12, written for the Eventyr April Fools 2025 article "Fandation": a gated documentation body whose only CSS exhibit is one `[[code]]` block, with all delivery (the sigma-plus and toggle-sidebar includes, the self-delivery module, the interwiki-style frame) sitting in the tail, after `[[/iftags]]` (orig L382-393).

The port restructured that delivery: everything moved to the head, ahead of the gate (cand L1-11), the gate itself was localized to `+テーマ`, and a license box the original does not carry was added at the tail (cand L405-413), honestly stating that the original has no license notation. The one wave edit of substance is the base repoint at cand L1: `component:sigma-plus` 404s on scp-jp, and FIX3-S2EN repointed the include to the JP fixed base candidate `component:sigma-plus-jp` under ruling 4. Measured churn against the mirror (diff.md, the generator's difflib count: +60/−38 in 4 hunks, Tier 1). What a reviewer should look at hardest is the head restructure (section 3: it is the port's own work, not a wave's, and the wave record's silence about it is correct), and the two prose links no wave touched (section 7).

## Classification

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 11 change blocks — 5 specific (45.5%), 5 heuristic, 1 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Labels are sets per block; the sections below were written from classification.json's label sets, not from the skeleton's per-section lists (the skeleton's sections 2 and 10 print "none" although the SIGMA-PLUS-JP signature and a porter annotation fired inside blocks whose primaries sit elsewhere).

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 7 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| SELF-DELIVERY | 2 |
| SIGMA-PLUS-JP | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Topology (classification.json): the original's two components — code-css orig L38-379 (the CSS exhibit) and module-css orig L386-389 (tail self-delivery) — against the candidate's module-css cand L3-6 (head self-delivery) and code-css cand L58-402. No component is lost; the self-delivery module moved from tail to head, and the exhibit grew by the JP font supplement (section 4).

## 0. Header / provenance

- What: the package diffs the mirror of `theme:fandom` at revision 6 against the canonical candidate `pages/theme:fandom-jp.txt`. Delivery relocation is detected and is real: the original delivers from its tail (orig L382-393), the candidate from its head (cand L1-11).
- Why: the mirror is the reference revision the port was made from; provenance for every row lives in review/sources.tsv, and this package's original.txt hash equals that row's value.
- Verify: `sha256sum review/fandom-jp/original.txt` against review/sources.tsv; `cmp review/fandom-jp/candidate.txt pages/theme:fandom-jp.txt`.
- Disposition: PASS at the ledger determination (GOSIGN2-LEDGER (b) row 87); the stamp above is STALE for the one post-verdict sweep line only.

## 1. Credit and attribution

- What: CREDIT-PREVIEW / TASL-FIELDS (B1): the candidate carries the eight-field preview credit block at cand L16-23, where the original carries none. The author field reads `**著作権者:** [[*user Fish^12]]`, matching the original's own credit ("The theme was created by [[*user Fish^12]]", orig prose) exactly. 作成年 2025 matches the original's April Fools 2025 context. The source link's text is the original title, "Fandom Theme" (cand L21), the localize.md §3 form; most of the population uses the standardized 「ソース」 instead, and the credit waves left this file's form standing.
- Why: P3 / KB-63 family: the JP environment's preview credit module is the rate-bearing form, and the TASL record (Title, Author, Source URL, License) is what ruling 3 requires of a campaign port. The original's bare `[[module rate]]` (orig L3, inside the centered block) is deleted with the block (B2, section 8): the preview module already bears a rate (KB-09).
- Verify: read cand L16-23 against orig L1-4 and the original's prose credit line; the eight fields are all present and the author value is byte-identical in name.
- Disposition: the ledger's T4 line for this theme records no P3 item; the credit block was complete at the port and the only later credit change is the translator normalization (FIX-CREDIT-D, inside 1869877: `SCP-JP` → `AI`), which is the population form for campaign translations under ruling 3.

LICENSE-BOX (B10, cand L405-413): a license box the original does not carry anywhere was ADDED at the tail, in the settled JP form (`:scp-jp:component:license-box-backend` … `license-box-end`, author=Fish^12). Its text states the ground honestly: the original carries no license notation, and the author should be confirmed with before posting; it also cites the chameleon.gif source URL on scp-wiki.wikidot.com. The classifier's LICENSE-BOX label is restoration-shaped; the bytes say addition, and this record follows the bytes.

## 2. Includes and components

- What: SIGMA-PLUS-JP fired twice. At the head, cand L1 `[[include component:sigma-plus-jp]]` is the FIX3-S2EN Class 2 repoint of the original's tail include `[[include :scp-wiki:component:sigma-plus]]` (orig L384). At the tail (B11), that original include has no counterpart line, because the base include now exists once, at the head. The toggle-sidebar include likewise moved and was repointed: orig L385 `:scp-wiki:component:toggle-sidebar` → cand L2 `:scp-jp:component:toggle-sidebar`. The interwiki-style frame (cand L8-11, priority=1, theme= own /1) names the candidate's own delivery.
- Why: ruling 4 (a component a theme needs is ported with the theme; cross-references repoint to the JP fixed base candidate). The FIX3-S2EN report (§4.2) records the ground: `component:sigma-plus` returns HTTP 404 on scp-jp; `component:sigma-plus-jp` is itself a campaign candidate that also 404s on live scp-jp today, so the unprefixed same-site form is the established convention for candidate-only components (the theme:tfnac-jp and theme:sunside-jp precedents) and it resolves on the sigma10-jp-test wiki.
- Verify: `grep -n "sigma-plus" review/fandom-jp/candidate.txt` returns exactly one include (cand L1); the original's two tail includes are at orig L384-385.
- Disposition: FIXED by FIX3-S2EN (report §4.2), verified in the 1869877 diff (one line: `component:sigma-plus` → `component:sigma-plus-jp`). The ledger (c3) records this theme's P1 as DISPOSITIONED (posting-procedure convention class), which is the same fact from the check side: what remains is the posting step, not a code defect.

## 3. Delivery and code loading

- What: SELF-DELIVERY ×2 (B1 span): cand L4-6 `[[module CSS]] @import` of own /1 from sigma10-jp-test.wdfiles.com, and the interwiki-style frame's theme= naming the same /1 (cand L8-11). The address is correct: the page holds exactly one `[[code]]` block (cand L59-402), so /1 names the block that holds the CSS. The whole delivery sits ahead of the `[[iftags +テーマ]]` gate (cand L13), where the original delivers after `[[/iftags]]`.
- Why: class (iii) draft-host form (KB-41): the candidate's own local--code on the draft host is the sanctioned draft-stage form; posting rewrites it (class (ii)). The head placement is the port's own restructure (present since 7aed5b7); no wave moved it, and the FIX3-S2EN diff for this file touches only the L1 include and the translator line, which the reviewer can confirm in the Multi-wave provenance section.
- Verify: count `[[code]]` blocks in the candidate (one) against the /1 references (two channels, both /1); brace-depth scan of the exhibit ends at depth 0 with 52 top-level rules, the same count as the original's exhibit.
- Disposition: T1 baseline pseudo-ref×2 is exactly these two draft-host self-references, dispositioned at class (iii) in register (c1).

## 4. Fonts and assets

- What: JPFONT-LOAD / FONT-IMPORT (B8): inside the exhibit, the original's fonts.bunny.net imports for Roboto Slab and Rubik were repointed to fonts.googleapis.com (cand L66-67), and the port added a JP supplement at cand L69-71: a porter comment (`日本語フォント (JP localization)`) plus Noto Sans JP and Noto Serif JP imports. CSS-BODY (B9) is the matching stack edit, narrated here as the P7 class it is: `--robo` gains `"Noto Serif JP", serif` and `--rubi` gains `"Noto Sans JP", sans-serif` (cand L79-80). Every family named in the two stacks is loaded by the imports at cand L66-71. DRAFT-HOST (B5): the chameleon.gif image was rehosted from scp-wiki.wikidot.com/local--files to the draft host (cand L51).
- Why: P7 (KB-16): Japanese text needs a JP typeface loaded, and the Sigma+ base loads none for this theme's own stacks. P5 (KB-17): bunny.net is not an exception-list font host; Google Fonts is. The gif rehost is the draft-stage asset form (KB-41 family).
- Verify: `grep -n "@import" review/fandom-jp/candidate.txt` (three import lines, all googleapis or the JP supplement) against the stack variables at cand L79-80.
- Disposition: the font work is the port's own (the LOCALIZE-S2-B lane found P7 already APPLIED in the candidate it reviewed). The gif's 404 is dispositioned in the render row as owner-deferred EN9 (KB-58): the file is absent on the draft host because campaign assets are not re-uploaded.

## 5. Header, sidebar, site furniture

- What: none — no signature for this section fired over 11 change blocks, and a hand check agrees: the theme defines no sidebar or top-bar geometry of its own. The one header string, `--header-title: "Foundation Wiki"` (cand L82), is byte-identical to the original (orig L59) and so produces no change block at all.
- Why: the string is the fictional wiki's masthead that the theme imitates, not a UI label awaiting translation.
- Verify: `grep -n "header-title" review/fandom-jp/candidate.txt review/fandom-jp/original.txt` — same value both sides.
- Disposition: the LOCALIZE-S2-B lane counted the string display-affecting (its P9 item); FIX3-S2EN §6 item 1 names fandom among the slogan/brand strings deliberately left unchanged under ruling 2 (header and title language is out of scope for migration correctness). The ledger (c3) records no P9 line for this theme; the disposition ground is the ruling, cited here so the lane's finding is not silently dropped.

## 6. Text translation

- What: TRANS-UNANCHORED (B3, B4, B6, B7): the documentation prose is translated throughout — the design note (cand L38), the intro paragraph (cand L26-31, carried in full: the Fandation article link, all ten credited contributors, and the Fish^12 creation credit), the "Behold the possibilities" line (その可能性をご覧あれ。, cand L53), and the collapsible labels (テーマのソース, cand L58-59). The April Fools heading is rendered as idiom (なんてこったクリス、ここは一体どこなんだ！？), which the lane's T5 read judged a fair rendering with no residue.
- Why: P10 (KB-18): the theme's documentation is part of the deliverable; an untranslated body would ship English instructions to JP users.
- Verify: read cand L26-53 against orig L6-33; every prose unit has a Japanese counterpart and no English prose line survives outside code and links.
- Disposition: T5 FINDINGS at the ledger row, closed by the joint T4/T5 verdict; no translation item for this theme reached section (e).

## 7. Links

- What: no link signature fired, and the usage exhibit's self-include is in the post-sweep form (`@@[[include :scp-jp:theme:fandom-jp]]@@`, cand L35, completed by b5cb724). Two prose links remain as the original had them, pointing at EN pages with no （英語版） annotation: the Fandation article link (cand L28) and the component reference link naming `component:sigma-plus` and `component:toggle-sidebar` (cand L30).
- Why: pattern 11 asks for EN links to carry the annotation, and for a JP counterpart to be preferred where one exists. The toggle-sidebar half is the sharp one: the candidate's own include at cand L2 uses the JP component, so a JP counterpart demonstrably exists, while the prose still sends the reader to the EN page.
- Verify: `grep -n "scp-wiki.wikidot.com" review/fandom-jp/candidate.txt` — the remaining hits are the credit source link (required), the license box's gif source citation, and these two prose links.
- Disposition: recorded here as a noted, unrepaired minor item. The LOCALIZE-S2-B lane's T5 finding 1 and its pattern-11 MISSED (minor) are the record; the ledger (c3) carries no P11 line for this theme and no wave acted on it. This package does not edit the candidate; the item is flagged for the coordinator in the batch report.

## 8. Structure

- What: EXHIBIT-RESTRUCTURE fired twice, and both are adjudicated against the exhibit census. B4 (orig L8-20 → cand L40 region): replaced, not dropped — the original's intro and usage prose exists in the candidate in translation (section 6); the block's shape is the head restructure compressing the alignment, not a deletion. B11 (orig L383-393 → cand L416): the original's tail delivery block has no tail counterpart because its contents moved to the head (section 3); the block's residue is the `[[/iftags]]` line itself, which now closes the page after the license box (cand L415). B2 (the appendix's residue block) pairs the original's bare Rate line with the candidate's usage line for the same reason: both sit inside the head-restructure alignment.
- Why: R3: a sanctioned replacement and a silent deletion have the same diff shape, so the ground must be stated. Here the ground is the census: one code exhibit on each side, one base include on each side, one toggle-sidebar include on each side, one self-delivery on each side.
- Verify: the topology counts in the Classification section; `grep -c "component:sigma-plus" review/fandom-jp/candidate.txt` is 2 (the L1 include and the L30 prose mention), matching the original's include-plus-mention shape.
- Disposition: no exhibit was dropped; the restructure is the port's own form, present since 7aed5b7 and untouched by the waves.

## 9. Formatting only

- What: WS-ONLY blocks: 0. Re-indentation: 0 blocks. The diff's four hunks carry no whitespace-only mass.
- Why / Verify / Disposition: nothing to disposition; the counts are the classifier's (classification.json summary).

## 10. Porter annotations

- What: one porter annotation, riding inside B8: the CSS comment `日本語フォント (JP localization)` at cand L69, introducing the JP font supplement imports. The skeleton prints "none" for this section because the comment's block primary is JPFONT-LOAD; the standing check finds it here.
- Why: the annotation marks the supplement as the port's addition, so a future reader does not mistake the Noto imports for original content.
- Verify: `grep -n "JP localization" review/fandom-jp/candidate.txt` — one hit, cand L69.
- Disposition: retained as documentation; not a defect.

## 11. Dispositions and exceptions

- T1 pseudo-ref×2: DISPOSITIONED, class (iii) — the two draft-host self-references of section 3 (register (c1) preamble; T1-ROWS row 87 baseline: exit 1, 2 errors / 0 warns / 1 info).
- T4 P1 (the sigma-plus include naming a page absent on scp-jp): DISPOSITIONED in the ledger (c3) as the posting-procedure convention class; the substantive half of the same fact is the FIX3-S2EN repoint of section 2, FIXED in the bytes.
- Render items: the purple header wordmark overprinting account links at ≤375px in both engines is DISPOSITIONED in the render row (RENDER-S2-B) under the KB-35 narrow-width family; the chameleon.gif 404 is DISPOSITIONED as owner-deferred EN9 (KB-58).
- P9 (`--header-title`): kept under ruling 2, per section 5.
- P11 prose links: NOT dispositioned by any register line and NOT repaired; recorded in section 7 as this package's one open minor item, flagged to the coordinator. It does not disturb the ledger verdict, which was computed on the joint T4/T5 FINDINGS with the lane's minor marking on record.

## 12. Verification

- T1 (source check): baseline 2026-11-16, T1-ROWS row 87: exit 1, 2 errors / 0 warns / 1 info (pseudo-ref×2); standing classes dispositioned in register (c1). Re-runnable with the staff checker's check_source.py against candidate.txt.
- T2/T3 (render): RENDER-S2-B row for this theme (RENDER-ROWS-1): FINDINGS, both items dispositioned as in section 11.
- T4 follow-up (reference-revision currency): `diff-fandom.txt` (LOCALIZE-S2-B lane): rev6 → rev6, no changes; upstream latest is still revision 6.
- Package checks: `python3 review/build_review.py --check` passes for this package; candidate.txt is byte-identical to the canonical file; original.txt's SHA-256 equals the sources.tsv row.

## Per-theme record

1. **The wave edit, verified.** Commit 1869877's diff for this file has exactly two hunks: cand L1 `component:sigma-plus` → `component:sigma-plus-jp` (FIX3-S2EN §4.2) and the translator field `SCP-JP` → `AI` (FIX-CREDIT-D). The commit's subject names only the translator normalization; the sigma repoint rides inside it. A reader who trusts the subject line alone will miss the batch's most substantive edit.
2. **The head restructure is not a wave edit.** The delivery-at-head form, the JP font supplement and the license box all exist in the port commit 7aed5b7. The FIX3-S2EN report claims only the repoint for this theme, and the bytes agree with the report.
3. **The license box is an addition, not a restoration.** The original carries no license box and no credit block; the candidate's box (cand L405-413) was added by the port and says so in its own text (the original has no license notation; confirm with the author before posting). The classifier's LICENSE-BOX label must not be read as evidence the original had one.
4. **The P9 ground lives outside the ledger.** The ledger (c3) records only P1 for this theme. The `--header-title` disposition rests on ruling 2 as applied in FIX3-S2EN §6 item 1, which names fandom explicitly. Recorded here so the chain is derivable from this package plus the vendored authorities.
5. **Follow-up currency is clean.** Upstream latest = reference revision (6), per the lane's follow-up artifact; no drift is outstanding.

### Post-package repairs (REFRESH3-F)

**FIX-DYN, landing `49a1e49` (report `R/review-scout/FIX-DYN.md`, item 2, "the
EN prose links").** This landing postdates the package build (`a0a5549`)
and repairs the pattern-11 links. Three candidate changes on two lines:
L30's Sigma Plus link
`[[[https://scp-wiki.wikidot.com/component:sigma-plus|Sigma Plus]]]` →
`[[[component:sigma-plus-jp|Sigma Plus]]]` and its toggle-sidebar link →
`[[[component:toggle-sidebar|トグル式サイドバー]]]` (both JP counterparts
exist; the population uses the same-site prose form); L28's Fandation link
keeps its target but gains the in-label annotation `Fandation（英語版）` —
the article has no JP counterpart (probes of
`https://scp-jp.wikidot.com/fandation` and the draft-host form both 404),
so repointing would have replaced a working link with a dead one;
pattern 11's annotation branch was applied instead. Checker per the
report: error 2 / warn 0 / info 1 → 2/1/1 — the one added finding is
`link-target-missing` at L30 for `component:sigma-plus-jp`, the standing
posting-resolution class; no new class (i) error. This package documents
the corrected candidate; its stamp reads STALE against the pre-repair
verdict, by design.

## Change set outside the two diffed files

One companion candidate: `pages/theme-decoration-sample-fandom-jp.txt`, the decoration sample that applies this theme on the check wikis (its own delivery names the candidate). The sample is a separate page with its own review surface; it is not part of this package's diff. (The EN-named `pages/theme:fandom.txt` and `pages/theme-decoration-sample-fandom.txt` also sit in pages/ as composition members of the display-check wikis; they are not the JP candidate.)

## Multi-wave provenance

- Port: Stage 2 EN9 integration, commit 7aed5b7 — head-delivery restructure, credit block, JP font supplement, license box addition, gif rehost.
- Check waves: T1 baseline (T1-ROWS row 87); render walk RENDER-S2-B (RENDER-ROWS-1); localize walk LOCALIZE-S2-B (LOCALIZE-ROWS row 87) with the rev6 follow-up diff.
- Fix waves: FIX3-S2EN §4.2 (base repoint) and FIX-CREDIT-D (translator normalization), both inside commit 1869877.
- Post-verdict: usage-example sweep, commit b5cb724 (one line, the usage exhibit's self-include completed to the `-jp` name).
- Ledger determination: GOSIGN2-LEDGER (b) row 87, PASS, no section (e) items; go-sign COMPLETION-REPORT.md §10.

## Appendix — residue and heuristic blocks

- R1 — B2 (residue; orig L3 → cand L35): the original's bare `[[module rate]]` line paired against the candidate's usage-exhibit line. Alignment artifact of the head restructure: the Rate deletion belongs to section 1 (KB-09, the preview module is rate-bearing) and the usage line to section 7. Resolved there; no new signature proposed.
- R2 — B3 (heuristic, TRANS-UNANCHORED): the design-note paragraph, translated (section 6). The classifier's note ("script delta without the anchor majority") is the expected shape for a full-paragraph translation.
- R3 — B4 (heuristic, EXHIBIT-RESTRUCTURE): intro/usage prose; replaced in translation, not dropped (section 8).
- R4 — B6 (heuristic, TRANS-UNANCHORED): one-line prose translation (section 6).
- R5 — B7 (heuristic, TRANS-UNANCHORED): the collapsible show/hide labels, translated (section 6).
- R6 — B9 (heuristic, CSS-BODY): the `--robo` / `--rubi` stack extensions; adjudicated as the P7 font-stack class and written in section 4, per the standing rule that font-family rewrite blocks are P7 rewrites whatever the classifier's primary label says.

## License and attribution

- **Title:** Fandom Theme
- **Author:** Fish^12
- **Source:** https://scp-wiki.wikidot.com/theme:fandom — revision 6
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
