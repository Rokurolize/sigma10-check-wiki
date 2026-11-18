# Review package — theme:eigenvector-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:eigenvector-jp — origin EN, population #84 [GOSIGN2-LEDGER (b) row 84]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 84]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 0 warns / 0 infos (pseudo-ref×8); standing classes dispositioned in register c1 [T1-ROWS row 104; GOSIGN2-LEDGER (b) row 84]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 483/502px@320/375 + sample overflow everywhere incl. desktop 1427–1441px@1366; WebKit CC "S"; cdn.jsdelivr.net/fonts.bunny.net direct links; no candidate-CSS defect. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 84, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 84]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 84]
- Computed against: canonical commit a497307c6e7eedc2580739ba55d2c3212d9cacd2; candidate file pages/theme:eigenvector-jp.txt sha256:3499368d14d4ddb88a52aea75661ef446ff5f9f159aba0cc48b0fef483ca79bc; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/eigenvector-jp/candidate.txt (sha256 3499368d14d4ddb88a52aea75661ef446ff5f9f159aba0cc48b0fef483ca79bc)
Original: theme:eigenvector — scp-wiki, revision 19 (sha256 f3356116a3fa7ba9be56c56a7fb492e3cc4b9b588352dc89c2a35448cb21af79)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 84); one of the 286 of 286 pass-eligible themes. The generated stamp above also reads PASS |
| Wave edits | Three wave commits touched this file: FIX-P4 (base repoint + the FIX3-S2EN font fix riding inside it), FIX4-MECH (duplicate-import removal), and the credit normalization inside the FIX-P4 commit. Each is verified hunk by hunk in the Per-theme record |
| Layered kind | K5b-3: the candidate layers over theme:basalt-jp, as the original layers over EN Basalt/Bedrock. This package's diff covers the theme's own layer only; the base's content is the basalt-jp package's subject |
| Coverage caveat recorded | The font fix extended two of the theme's three primary stacks; `--mono-font-primary` still names 'Inconsolata' alone (section 4) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:eigenvector | theme:eigenvector-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 19, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 19 | — |
| Source of this copy | Campaign mirror store (hash-verified against review/sources.tsv) | Canonical file `pages/theme:eigenvector-jp.txt`, created in commit 184cb65 (Stage 2 EN8 integration); later changed by f1138e4 (FIX-P4) and a497307 (FIX4-MECH) |
| Lines | 669 (generator count, diff.md) | 679 (generator count, diff.md) |
| SHA-256 | f3356116a3fa7ba9be56c56a7fb492e3cc4b9b588352dc89c2a35448cb21af79 | 3499368d14d4ddb88a52aea75661ef446ff5f9f159aba0cc48b0fef483ca79bc |

Provenance route: derived from the original at the reference revision (sources.tsv kind: K5b-3, the layered kind — the candidate layers over theme:basalt-jp, so this package's diff covers the theme's own layer only; the base arrives by `@import` on both sides and is not part of either file). No production counterpart exists, so the R4 question does not arise. Reference-revision currency: revision 19 is still the upstream latest — the T4 follow-up artifact `diff-eigenvector-from19.txt` records rev19 → rev19, no changes (exit 0).

Wave history: the port (184cb65) kept the original's EN CDN base imports and Latin-only stacks. FIX-P4 (f1138e4) repointed the base imports to the JP base candidate's delivery, and the same commit also carried the FIX3-S2EN font fix (the JP import and the two stack extensions) and the FIX-CREDIT-D translator normalization. FIX4-MECH (a497307) then removed the duplicate base import that the repoint's line-for-line rule had created (KB-65). The Per-theme record verifies each step.

## Summary

A Basalt/Bedrock-based theme by EstrellaYoshte adapting the MediaWiki Vector 2022 skin: a head module importing the base bundle, a documentation body, two CSS exhibits (the light layer, 430 lines, and a 31-line darkmode layer), and a two-channel self-delivery (light at priority 3, darkmode at priority 4, the second gated by a parameterised iftags). The port's own work is the standard shape (credit block, bare-Rate deletion, asset rehosts, exhibit font-host repoint). The wave story is the base: the port initially read EN Basalt straight from cdn.scpwiki.com, exactly as the original does; FIX-P4 replaced both EN import lines with the JP base candidate's code block /1, which the FIX-P4 report verifies is the JP edition of the same basalt-bedrock bundle (the normalize reset rides as its leading `@import` line). Measured churn (diff.md, the generator's difflib count: +125/−120 in 6 hunks, Tier 1) understates the delivery change, because the two-for-one import replacement is only two lines. A reviewer should look hardest at the head module (section 3: what the base is now, and why the duplicate that briefly existed was deliberate), and at the font coverage boundary (section 4).

## Classification

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 66 change blocks — 32 specific (48.5%), 34 heuristic, 0 residue, 0 skipped. The heuristic share is translation mass (TRANS-UNANCHORED ×35), not uncertainty about mechanisms: every delivery, credit and font block is specific. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Labels are sets per block; the sections below were written from classification.json's label sets, not from the skeleton's per-section lists.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 35 |
| TRANSLATION-ANCHORED | 17 |
| DRAFT-HOST | 9 |
| DELIVERY-HOST | 5 |
| SELF-DELIVERY | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| INCLUDE-REPOINT | 3 |
| CSS-BODY | 2 |
| CREDIT-PREVIEW | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |

Topology (classification.json): the original's components — module-css (head base imports), code-css ×2 (light and darkmode exhibits), module-css ×2 (the two self-delivery channels) — against the candidate's matching set. No component moved, was added, or was dropped; the head module's contents changed (section 3), not its position or kind.

## 0. Header / provenance

- What: the package diffs the mirror of `theme:eigenvector` at revision 19 against the canonical candidate `pages/theme:eigenvector-jp.txt`, covering the theme's own layer only (the base is imported on both sides).
- Why: the mirror is the reference revision the port was made from; provenance for every row lives in review/sources.tsv, and this package's original.txt hash equals that row's value.
- Verify: `sha256sum review/eigenvector-jp/original.txt` against review/sources.tsv; `cmp review/eigenvector-jp/candidate.txt pages/theme:eigenvector-jp.txt`.
- Disposition: PASS at the ledger determination (GOSIGN2-LEDGER (b) row 84), stamp PASS.

## 1. Credit and attribution

- What: CREDIT-PREVIEW / TASL-FIELDS (B1): the eight-field preview credit block at cand L3-11, where the original carries none. The author field reads `**著作権者:** EstrellaYoshte`, matching the original's own credit ("created by [[*user EstrellaYoshte]]", orig prose). The source link's text is 「ソース」, the population-standard form.
- Why: P3 / ruling 3 (the TASL record). The original's bare Rate, with its `[[>]]` "Rating:" wrapper (orig L10-14), is deleted (BARE-RATE-DEL, B4): the preview module already bears a rate (KB-09).
- Verify: read cand L3-11 against the original's prose credit line; all eight fields present, author value identical in name.
- Disposition: no P3 item stands against this theme beyond the EN8 credit-notation pair (translator in non-user form, since normalized to AI inside f1138e4; the 「ソース」 link text, the settled population form).

## 2. Includes and components

- What: INCLUDE-REPOINT ×3 and COMPONENT-SWAP ×1 (B6): the documentation's component references (interwiki-style, image-block) are local same-site includes (cand L32, L663, L673 region), where the original names `:scp-wiki:` forms. The usage exhibits (cand L26-29) instruct users to include `theme:bedrock-jp` and then `theme:eigenvector-jp` (with a `darkmode=a` variant), repointed from the original's `:scp-wiki:theme:bedrock` / `:scp-wiki:theme:eigenvector`.
- Why: ruling 1's same-site form. The bedrock dependency needs its ground stated: at the localize lane's check (2026-11-16) `theme:bedrock-jp` returned HTTP 404 on live scp-jp, because it is itself a campaign candidate (a class U theme in this rollout), not a posted page. The dependency resolves when the batch posts together; it is not a dangling reference in the deliverable set.
- Verify: `grep -n "bedrock" review/eigenvector-jp/candidate.txt` — the prose link (annotated （英語版）, section 7) and the usage exhibits name distinct targets correctly.
- Disposition: the ledger (c3) records P1 for this theme as DISPOSITIONED (posting-procedure convention class), which is this dependency's ground.

## 3. Delivery and code loading

- What: DELIVERY-HOST ×5, DRAFT-HOST ×9, SELF-DELIVERY ×4. Three facts. (1) The head module (cand L13-16): a Noto Sans JP `@import`, then ONE `@import` of the JP base candidate's delivery, `sigma10-jp-test.wdfiles.com/local--code/theme%3Abasalt-jp/1`. The original's head module (orig L2-5) imports two files from cdn.scpwiki.com: `theme/en/basalt/normalize-min.css` and `theme/en/basalt/basalt-bedrock-min.css`. (2) The two-channel self-delivery is preserved exactly: light by module `@import` of own /1 (cand L660) and the priority=3 frame (cand L663-666); darkmode by own /2 (cand L671) and the priority=4 frame (cand L673-676), the darkmode channel gated by the parameterised `[[ift{$darkmode}gs -テーマ]]` epilogue. Both addresses are correct: the page holds exactly two `[[code]]` blocks (light exhibit cand L193-623, darkmode exhibit cand L624-654), so /1 and /2 name the blocks that hold the CSS. (3) The base replacement's history has three steps, all verified in the Per-theme record: FIX-P4 rewrote BOTH EN lines to the same basalt-jp/1 URL (its brief's line-for-line rule; the report records the resulting duplicate as a deliberate, idempotent redundancy, not an error); FIX4-MECH later removed one of the two under KB-65 (duplicate @import removal). The current file imports the base exactly once.
- Why: the FIX-P4 report's mapping table is the ground for the two-to-one replacement: no standalone JP reset fragment exists, and basalt-jp/1 serves the reset as its leading `@import` line; the same /1 IS the JP edition of the basalt-bedrock bundle (full light-mode Basalt + Bedrock) carrying the JP fixes. Both EN lines therefore map to the one JP resource, and nothing the original loaded is lost. The localize lane's P4(a) finding (a non-exception external host reading another theme's code, against localize.md §4) is what the repoint closed. The self-delivery's draft-host form is class (iii) (KB-41).
- Verify: `grep -n "@import" review/eigenvector-jp/candidate.txt` at the head — two imports (Noto Sans JP, basalt-jp/1 once). `grep -c "theme%3Abasalt-jp/1" review/eigenvector-jp/candidate.txt` is 1 in the head module. Brace-depth scans of both exhibits end at depth 0 (66 and 4 top-level rules), matching the original's exhibits rule for rule.
- Disposition: the ledger (c3) records P4 as DISPOSITIONED (delivery class (ii)). Read precisely: the finding's substance (the EN CDN read) was FIXED by FIX-P4; the disposition line covers the delivery form that replaced it, the base arriving as a JP candidate's draft-host code block, which posting rewrites (class (ii)). The T1 baseline pseudo-ref×8 (T1-ROWS row 104) is this delivery's draft-form references, dispositioned at class (iii) in register (c1).

## 4. Fonts and assets

- What: FONT-IMPORT (B55): inside the exhibits, the original's font loading (orig L184-186: fonts.bunny.net plus a Libertinus Serif stylesheet read straight from scp-wiki.wdfiles.com local--files) became Google Fonts imports (cand L194-196: Libertinus Serif, Roboto, Inconsolata). JPFONT-LOAD (B2): the head module's Noto Sans JP `@import` (cand L14). The stack extensions, which the classifier labels CSS-BODY (B56, B57), are narrated here as the P7 class they are: `--header-font-primary: 'Libertinus Serif', 'Noto Sans JP'` (cand L213) and `--body-font-primary: 'Roboto', 'Noto Sans JP'` (cand L215). The third primary stack was not extended: `--mono-font-primary: 'Inconsolata'` (cand L216) names no JP face, so Japanese in mono contexts falls back to the generic tail. DRAFT-HOST asset rehosts: raisa.png (cand L32 and L219, the credit image and `--header-logo`), u2.png (cand L158), raisa-dark.png (cand L626), all from EN file hosts to the draft host.
- Why: P7 (KB-16) for the supplement; the FIX3-S2EN §4.4 row for this theme itemizes exactly the two stacks that were extended (its L214/L216 in edit-time numbering), so the mono stack's state is the wave's documented boundary, not an oversight this package can silently widen. P5 (KB-17) for the bunny.net repoint; the original's direct read of an EN local file (the Libertinus stylesheet) is subsumed by the Google Fonts family import.
- Verify: `sed -n '213,216p' review/eigenvector-jp/candidate.txt` — two extended stacks, then the unextended mono stack.
- Disposition: P7 FIXED per the ledger (font wave), on the scope stated. The render row's delivery-host line (cdn.jsdelivr.net / fonts.bunny.net direct links) is DISPOSITIONED in the render record under the delivery-host class (ii), with theme-level items adjudicated in (c3).

## 5. Header, sidebar, site furniture

- What: no furniture geometry is the theme's own (the sidebar and top-bar are the Basalt base's, per the localize lane's P8 N-A). The header variables: `--header-title` is undefined by design (the header is the Vector-2022-style logo alone); `--header-subtitle: "Source - Catalog - Profile"` (cand L220) is byte-identical to the original (orig L210).
- Why: ruling 2 (header and title language is out of scope for migration correctness) covers the subtitle.
- Verify: `grep -n "header-subtitle" review/eigenvector-jp/candidate.txt review/eigenvector-jp/original.txt` — same string both sides.
- Disposition: P9 DISPOSITIONED under ruling 2 (ledger (c3)).

## 6. Text translation

- What: TRANSLATION-ANCHORED ×17 and TRANS-UNANCHORED ×35: the documentation body (usage, the s-title/oheader/wikibox explanations, tables, footnotes) is translated throughout in です・ます register. Lorem ipsum specimen text is carried as dummy text, as the lane's P10 read allows. The parameterised epilogue tags are localized (`-テーマ` in the `ift{$darkmode}gs` forms, cand L668, L678).
- Why: P10 (KB-18).
- Verify: read cand L18-191 against orig L15-181; every prose unit has a Japanese counterpart.
- Disposition: T5 FINDINGS at the ledger row, closed by the joint T4/T5 verdict; no translation item for this theme reached section (e).

## 7. Links

- What: the prose's EN references are annotated in the form pattern 11 asks for: `SCPediaテーマ（英語版）` (cand L19) and `Bedrock（英語版）` (cand L22), both pointing at scp-wiki.wikidot.com pages for which no JP counterpart exists (the lane verified theme:scpedia, theme:scpedia-jp and theme:bedrock all 404 on scp-jp, 2026-11-16). The MediaWiki Vector 2022 reference link is an external reference, carried.
- Why: where no JP target exists, an annotated EN link is the correct form; where a JP candidate exists (bedrock, section 2), the usage exhibits, not the prose, carry the include instruction.
- Verify: `grep -n "英語版" review/eigenvector-jp/candidate.txt` — the annotations are present at both prose references.
- Disposition: the lane's P11 read is N-A with the note recorded; no ledger item stands.

## 8. Structure

- What: EXHIBIT-RESTRUCTURE ×3 (B7, B61, B65), each on a frame include or exhibit-adjacent line: mere repoints, adjudicated against the census (two code exhibits, two self-delivery channels, one head module, on each side). No exhibit was restructured or dropped, and no CSS module is missing: the original's tail structure (two module-css delivery blocks) has its exact counterpart in the candidate.
- Why: R3's ground-stating rule; the census is the deciding evidence.
- Verify: topology counts in the Classification section; `grep -c "\[\[code" review/eigenvector-jp/candidate.txt` is 2, as in the original.
- Disposition: nothing to disposition; the label is resolved here as a false fire.

## 9. Formatting only

- What: WS-ONLY ×0 as a primary label; the classifier records no re-indentation blocks for this pair. The diff's six hunks are content hunks.
- Why / Verify / Disposition: nothing to disposition; the counts are the classifier's (classification.json summary).

## 10. Porter annotations

- What: none. A hand check finds no porter comment in the candidate; the head module's JP import carries no annotation, and the credit block is the only campaign-added prose.
- Verify: `grep -n "localization" review/eigenvector-jp/candidate.txt` — no hits.
- Disposition: nothing to disposition; the section is present with its ground, per the format.

## 11. Dispositions and exceptions

- T1 pseudo-ref×8: DISPOSITIONED, class (iii) (register (c1) preamble; T1-ROWS row 104 baseline: exit 1, 8 errors / 0 warns / 0 infos).
- Render items (RENDER-S2-B block): page overflow (483/502px at 320/375px) and sample overflow at every width including desktop DISPOSITIONED under KB-33/KB-34; the WebKit CC "S" reading under KB-36; the direct font-host links under the delivery-host class (ii). The lane's closing assessment stands: no candidate-CSS defect.
- T4 P1 (the bedrock-jp dependency): DISPOSITIONED, posting-procedure convention class (section 2). T4 P4: the EN CDN read FIXED by FIX-P4; the replacement delivery form DISPOSITIONED at class (ii) (section 3). T4 P7: FIXED (font wave), scope as in section 4. T4 P9: DISPOSITIONED under ruling 2 (section 5).

## 12. Verification

- T1 (source check): baseline 2026-11-16, T1-ROWS row 104: exit 1, 8 errors / 0 warns / 0 infos (pseudo-ref×8); standing classes dispositioned in register (c1). Re-runnable with the staff checker's check_source.py against candidate.txt.
- T2/T3 (render): RENDER-S2-B block (RENDER-ROWS-1): FINDINGS, items dispositioned as in section 11.
- T4 follow-up (reference-revision currency): `diff-eigenvector-from19.txt` records rev19 → rev19, no changes (exit 0); upstream latest is still revision 19.
- Package checks: `python3 review/build_review.py --check` passes for this package; candidate.txt is byte-identical to the canonical file; original.txt's SHA-256 equals the sources.tsv row.

## Per-theme record

1. **Three waves in three commits, and the subjects name only two of them.** f1138e4 (subject: FIX-P4's base repoint, 39 files) contains, for this file, the repoint AND the FIX3-S2EN §4.4 font fix (the JP import at cand L14 and the two stack extensions) AND the FIX-CREDIT-D translator normalization. a497307 (subject: FIX4-MECH) contains the duplicate removal. A reader working from commit subjects would attribute the font fix to no commit; the FIX3-S2EN report's itemized row for this theme (its L214/L216) is what ties the edit to its wave, and the bytes confirm the tie.
2. **The duplicate import was deliberate, then cleaned.** FIX-P4's brief kept each import line intact and rewrote both EN lines to basalt-jp/1; its report (§"pages with BOTH a normalize line and a bedrock line", eigenvector named among 16) records the duplicate as a deliberate idempotent redundancy. FIX4-MECH's KB-65 pass removed it. Neither state was an error; the package records the sequence so the current single import is not misread as the repoint's direct output.
3. **The base mapping is verified, not assumed.** basalt-jp/1 serves the normalize reset as its leading `@import` line and is the JP edition of the basalt-bedrock bundle (FIX-P4 report's mapping table, fetch-verified by that lane). The two-to-one replacement therefore loses no CSS the original loaded.
4. **The ledger's P4 line needs the section-3 reading.** "DISPOSITIONED (delivery class (ii))" alone would suggest the EN CDN delivery still stands and was merely dispositioned. It does not stand: FIX-P4 removed it. The disposition covers the replacement form. Recorded here so the package and the ledger do not tell different stories.

## Change set outside the two diffed files

One companion candidate: `pages/theme-decoration-sample-eigenvector-jp.txt`, the decoration sample that applies this theme on the check wikis. The base dependency theme:basalt-jp and the usage dependency theme:bedrock-jp are separate rows with their own packages; the EN-named `pages/theme:eigenvector.txt` and `pages/theme-decoration-sample-eigenvector.txt` are composition members of the display-check wikis, not the JP candidate.

## Multi-wave provenance

- Port: Stage 2 EN8 integration, commit 184cb65 — credit block, bare-Rate deletion, asset rehosts, exhibit font-host repoint; the EN CDN base imports and Latin-only stacks carried as the original had them.
- Check waves: T1 baseline (T1-ROWS row 104); render walk RENDER-S2-B (RENDER-ROWS-1); localize walk LOCALIZE-S2-A (LOCALIZE-ROWS row 84), which raised P4(a), P7 and P9; the rev19 follow-up diff (no changes).
- Fix waves: FIX-P4 (f1138e4: base repoint; the FIX3-S2EN font fix and FIX-CREDIT-D normalization inside the same commit); FIX4-MECH (a497307: duplicate @import removal, KB-65).
- Ledger determination: GOSIGN2-LEDGER (b) row 84, PASS, no section (e) items; go-sign COMPLETION-REPORT.md §10.

## Appendix — heuristic blocks

No residue blocks (0). The 34 heuristic blocks resolve by shape: TRANSLATION-ANCHORED and TRANS-UNANCHORED mass in the documentation body (section 6), and the two CSS-BODY blocks (B56, B57), which are the P7 font-stack extensions adjudicated in section 4 per the standing rule that font-family rewrite blocks are P7 rewrites whatever the classifier's primary label says. No new signature is proposed from this theme.

## License and attribution

- **Title:** Eigenvector Theme
- **Author:** EstrellaYoshte
- **Source:** https://scp-wiki.wikidot.com/theme:eigenvector — revision 19
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
