# Review package — theme:atlas-maniacus-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:atlas-maniacus-jp — origin KO, population #253 [GOSIGN2-LEDGER (b) row 253]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now cbde0b50460589baef4019781f8428990ca1acce808a5d247461e767000f832e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 0 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 236; GOSIGN2-LEDGER (b) row 253]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + runtime-hotlink; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 252, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 252]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 253]
- Computed against: canonical commit 780e0485dc89a41ccdf8671591c08bc887984edb; candidate file pages/theme:atlas-maniacus-jp.txt sha256:cbde0b50460589baef4019781f8428990ca1acce808a5d247461e767000f832e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 253) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (class (iii)); the render row's hotlink-chain and credit-modal items (ledger (c2), section 11); T4's findings per the ledger (c3) line (P3 FIXED; P5, class (ii) / KB-58; P9, ruling 2) |
| Surviving items recorded — REPAIRED | Three localize-row charges were visible in the as-built bytes in whole or in part: the duplicated `toggle-sidebar` include (candidate L1 and old L23), the duplicated Do Hyeon @import in two URL grammars (old candidate L179–180), and the credit furniture pairing (preview credit block AND a repointed info block) whose credit field and license box both used a pointer instead of the author's name the file itself carries (per-theme record). All three repairs have since landed (canonical commit 0c327f3, with the usage-example sweep lines re-applied on top in 780e048): the duplicated include and the duplicated legacy-grammar @import are removed, and the credit field (candidate L17) and the license-box author now name thd-glasses. This package documents the corrected candidate |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:atlas-maniacus | theme:atlas-maniacus-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 4 (the candidate's credit block records 初訳時参照リビジョン: 4) | — |
| Source of this copy | Campaign mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:atlas-maniacus-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 383 lines / 10,769 bytes | 414 lines / 12,930 bytes |
| SHA-256 | db52e605a85d6acd4e051846400aecb27f7f54770e38cab8e3489679703c9643 | b55ca8490c7d65dc7b088afa9d97548750d3dc7131045d5c406fa385e6886a7b |

Wave history: the candidate was created by the Stage 2 KO1 integration (commit 18280b3); FIX-CREDIT-D (1869877, translator attribution normalization; the stamp's computed-against commit) touched it later. FIX4-MECH's duplicate-@import sweep did not touch this file, which matters for section 4.

## Summary

A KO theme for the Atlas Maniacus canon whose original keeps its CSS split between a body code exhibit and a tail delivery module. The candidate assembles the CSS into one code block, self-delivers it from a head module on the draft host, replaces the Rate with the preview credit block, translates the documentation and its tabview exhibits, and adds a license box. Three of the localize lane's charges survived in the as-built bytes in whole or in part (duplicated sidebar-toggle include, duplicated font import, pointer-form credit where the file knows the author's name), each recorded below with its disposition tension rather than silently absorbed; all three have since been repaired (canonical commit 0c327f3; fix report FIX-MPURE1.md in the campaign record, R/review-scout/), with the usage-example sweep lines re-applied on top in 780e048, and this package documents the corrected candidate. Measured churn (diff.md, the generator's difflib count with autojunk off: +131/−108, 239 changed lines in 50 change blocks; a GNU-diff count of the same pair gives 190 changed lines — the difference is alignment choice across the delivery move, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 50 change blocks — 31 specific (62.0%), 13 heuristic (26.0%), 6 residue (12.0%), 0 skipped. The residue share is the batch's largest, and every residue block is adjudicated below. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 18 |
| TRANSLATION-ANCHORED | 15 |
| DELIVERY-MOVE | 6 |
| INCLUDE-REPOINT | 6 |
| DRAFT-HOST | 4 |
| ESCAPED-INCLUDE | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| INFO-DEL | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: the six residue blocks resolve as the repointed info block's opening line (B5; sections 1–2), three one-line translations the anchor heuristic missed (B8, a section heading; B15 and B23, tab titles; section 6), an exhibit parameter translation (B30; section 6), and the delivery move's tail seam (B47; section 3). The two EXHIBIT-RESTRUCTURE primaries co-fire with INCLUDE-REPOINT inside kept exhibits and adjudicate to repoints (section 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:atlas-maniacus-jp; original theme:atlas-maniacus on scpko at reference revision 4; candidate `pages/theme:atlas-maniacus-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 KO1 wave (sources.tsv kind: standard; no production JP counterpart exists, so the R4 adoption question does not arise). The frame order: the candidate opens with the sidebar-toggle include the original opens with (candidate L1), then its delivery module and frame (candidate L2–9), then the localized gate (candidate L10); the original opens with the toggle, its gate, its Rate, and its info block.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for atlas-maniacus-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's furniture is a `[[module Rate]]` in a right-aligned div (original L5–7) plus a `:scpko:info:start`/`end` block (original L9–22) naming the maker ([[*user thd-glasses]], original L13), the setting/text providers (referred to a remarks table), the font (Do Hyeon), and the images (a Pixabay photograph; the Atlas & Foundation logo by thd-glasses). The candidate deletes the Rate (BARE-RATE-DEL) and carries a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–21) with the eight ruling-3 fields — but as built its 著作権者 field was a pointer, not a name: "原語版ページの作成者に同じ（scpko の theme:atlas-maniacus)" (as-built candidate L17), and the license box's author parameter was the same pointer in longer form. The repair has since landed (canonical commit 0c327f3): both fields now name the author in plain form — the credit field reads `**著作権者:** thd-glasses` (candidate L17) and the license box's author line reads `|author=thd-glasses` (candidate L405). The name itself was present in the file all along: the candidate ALSO carries the info block, repointed to `:scp-jp:info:start`/`end` (candidate L23, and its end at candidate L37), with the maker's line translated inside it (制作： [[*user thd-glasses]], candidate L27; the logo credit at candidate L35). So the candidate runs both furniture sets (preview credit AND info block) — the localize row's type-3 charge was that the info block's survival creates a double evaluation area; in the JP form the preview block is the rate-bearing one, and whether the JP info frame adds a second rating surface is not decidable from this repo alone. What is decidable, and recorded in the per-theme record, is the pointer-form credit: the fields were normalized by FIX-CREDIT-D and verified by the checker, and the author's name was in the file the whole time. The source link (candidate L20) names `scpko.wikidot.com/theme:atlas-maniacus` — the original's recorded host. License box (T4): added at the tail (candidate L404–409 in the current numbering, section 8), its prose deferring to the original's record and flagging unlicensed images for author confirmation before posting.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form (KB-09) and ruling 3 fixes the eight fields; the fields are present and well-formed, which is what the credit waves' checker verifies. A field that pointed instead of naming, in a file that names, was a completeness gap of the same family as theme:asagao-jp's dropped attribution (this batch), recorded rather than certified away; it is closed by the repair recorded in the What above.
- **Verify:** Read candidate L12–21 and L23–37 against original L9–22; `grep -n 'thd-glasses' candidate.txt` — the hits now include the credit field at candidate L17 and the license-box author at candidate L405.
- **Disposition:** FIXED as to the eight fields (credit waves, checker-verified; the ledger (c3) outcomes); the pointer-form author field was recorded in the per-theme record as a surviving item under that disposition and has since been repaired (0c327f3). The double furniture (preview credit block AND repointed info block) stands as built; the repair did not touch it.

### 2. Includes and components

- **What:** Six INCLUDE-REPOINT blocks. The documentation's component exhibits are repointed from `:scpko:` forms to `:scp-jp:` or bare `component:` counterparts (the image-block exhibit at candidate L56, the ACS and group-table exhibits in the tabview), and three ESCAPED-INCLUDE blocks are the usage text's escaped include specimens, kept escaped (R1 text). Two include facts stand apart from the repoints: as built, the sidebar-toggle include appeared TWICE in the candidate (candidate L1, the original's own position, and old candidate L23, between the credit block and the info block) against the original's once (original L1) — the localize row's duplicated-include charge. The repair has since landed (canonical commit 0c327f3): the old L23 copy was removed together with the blank line that followed it, so the include now stands once, at candidate L1, and the credit block is followed by a single blank line and the info block; and the info pair of section 1 is a repoint that keeps a furniture set the credit block was meant to succeed. No live include names a foreign-wiki target.
- **Why:** P1 (KB-15) for the repoints. The duplication was not a repoint but a repetition: whichever wave added the second toggle include, the file included the same component twice, and the charge was never dispositioned by name; it is closed by the removal recorded above, not by a disposition.
- **Verify:** `grep -n 'toggle-sidebar' candidate.txt` returns candidate L1 only; `grep -n '\[\[include' candidate.txt` for the full sequence against the original's.
- **Disposition:** Repoints applied; the duplicated toggle include was recorded in the per-theme record as a surviving item, not dispositioned, and has since been repaired (0c327f3).

### 3. Delivery and code loading

- **What:** The original's CSS lives in two places: a source exhibit in the body and a tail `[[module CSS]]` (original L324–382) that applies it. The candidate assembles one `[[code type="css"]]` block (candidate L175–404) from both (the classifier's content move: module-css [324,382] → code-css [175,404], similarity 0.96; six DELIVERY-MOVE blocks, B43–B46, B49, B50), and delivers it from a head module (candidate L2–4) importing `local--code/theme%3Aatlas-maniacus-jp/1` from the draft host, with the interwiki frame after it (candidate L6–9, priority 1). The tail seam of the move is residue block B47 (the original's module/div closers at original L318–320 map to a blank at candidate L347). T1's three pseudo-ref errors are the draft-host addresses (import, frame, and the CSS icon address of section 4).
- **Why:** P4 (own-code delivery served from JP hosts) and P6/T3 (the frame); the draft-host form is KB-41, class (iii), rewritten at posting. Assembling split CSS into one delivered block is the standard JP form for a theme whose original split exhibit from application.
- **Verify:** `grep -n 'local--code' candidate.txt` — the head import and the frame line; the code block's head against the original's exhibit and tail module in diff.md.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts: the theme's display face is Do Hyeon (named in the original's info block by its Google Fonts specimen link). At the code block's head the candidate as built imported it TWICE, in two different URL grammars on adjacent lines (as-built candidate L179: `css2?family=Do+Hyeon&display=swap`; as-built candidate L180: `css?family=Do+Hyeon`) — the localize row's duplicated-import charge. One import would do; the pair was harmless to rendering (the second was a redundant fetch of the same family) but it is exactly the shape FIX4-MECH's duplicate-@import sweep (KB-65) removed from 29 other themes, and this file was not in that sweep's set, so the pair survived that sweep untouched. The repair has since landed (canonical commit 0c327f3): the legacy `css?family=` line was removed, and the `css2` form remains as the file's only Do Hyeon import (candidate L177 in the current numbering, the form the head block's other two imports also use). The stack names the family correctly ('Do Hyeon', candidate L230) — with the generic tail misspelled `san-serif` in BOTH files (carried from the original, not introduced; recorded so a future editor does not mistake it for a port slip). JP font loads ride in the same head region (JPFONT-LOAD/FONT-IMPORT, block B43). Assets: the theme's own files are re-hosted to the draft host in the CSS (the logo as `--icon-scp`, candidate L196; the hero background, candidate L219). The documentation's image-block exhibit keeps a BARE file name (`|name=atlasandfoundation.png`, candidate L57) — carried from the original's identical form (original L41), where it resolves against the theme page's own attachments; the localize row charged it as posting-blocker class, which is the class (ii) ground in other words: at posting, the candidate page's attachments make the name resolve, and the CSS already names the same file in full.
- **Why:** P7/T5 with KB-16 for the font supply; KB-65 for the duplication (a dedup that keys on exact URL strings misses a css/css2 grammar pair — the batch report proposes the amendment). P5 with KB-17/KB-58 for the assets: original-state delivery forms, class (ii), resolved by the posting procedure.
- **Verify:** `grep -n 'Do+Hyeon' candidate.txt` — the specimen link in the info block and the single remaining `css2` import at candidate L177; `grep -n 'name=atlasandfoundation' candidate.txt original.txt` — both files, same bare form.
- **Disposition:** DISPOSITIONED (assets, class (ii) / KB-58); the duplicated import was recorded in the per-theme record as a surviving item and has since been repaired by the one-line deletion (0c327f3).

### 5. Header, sidebar, and site furniture

- **What:** No `--header-title`/`--header-subtitle`/`--logo-image` override exists on either side; the theme's header identity is its CSS icon and hero variables (section 4). The sidebar furniture is the toggle include of section 2 (once, at candidate L1, in the corrected candidate; twice as built). LOCALIZE-ROWS row 252's type-9 item (four Korean default header strings, with an in-page inconsistency) belongs to this family; the ledger dispositions it under ruling 2.
- **Why:** P9/T6 names no override change here; ruling 2 grounds the header-language disposition.
- **Verify:** `grep -n 'header-title' candidate.txt` returns nothing; the toggle line is candidate L1 (the as-built second copy at old L23 has been removed; section 2).
- **Disposition:** DISPOSITIONED (P9, ruling 2: header/title language out of scope).

### 6. Text translation

- **What:** The documentation and exhibits are translated in place: fifteen TRANSLATION-ANCHORED and eighteen TRANS-UNANCHORED blocks (the introduction, the usage tabs, the ACS and group exhibits), one COMMENT-TEXT block (R1), and the residue singles adjudicated in the class summary (the 使用画像 heading, B8; the tab titles 構文例 and 応用方法， B15 and B23; the exhibit parameter 要注意団体識別子， B30). The info block's contents are translated with the body (section 1). One text artifact needs its ground stated: the candidate's only `[!-- … --]` block (candidate L149–155) is a commented-out specimen table inside an exhibit, present in the original in the same form and translated with the body — it is exhibit material, not a porter annotation (section 10).
- **Why:** P10 and KB-18 (reader-visible strings); R5 glyph conversion is not separately labeled in this file's blocks and no retained string required it beyond the anchored pairs.
- **Verify:** The body sections of diff.md in order; a Hangul scan of candidate.txt returns the 原題 field and the canon-name strings only.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L20) names the original's recorded host (section 1). The info block's source links (the Google Fonts specimen link, the Pixabay photograph page) are carried in translation inside the info block, where the original put them — they name the records' homes. No prose link in the candidate targets a KO-wiki page; no `http://` address remains.
- **Why:** P11: links name the serving original or the record's home.
- **Verify:** `grep -n 'http://' candidate.txt` returns nothing.
- **Disposition:** Standing; no dead link carried.

### 8. Structure

- **What:** The closing rule holds. The candidate preserves the original's order (toggle, gate, furniture, documentation with tabview exhibits, code, license region) with two mechanism-level changes charged to their own sections: the CSS assembled into one delivered block (section 3) and the license box added at the tail (candidate L404–409 in the current numbering, block B50) where the original ends at its module. The exhibit census is one-to-one; the two EXHIBIT-RESTRUCTURE primaries co-fire with INCLUDE-REPOINT inside kept exhibits and adjudicate to repoints. Nothing was dropped, so the R3 question does not arise.
- **Why:** R3 exists to force this adjudication; the census decides for preservation.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|license-box' original.txt candidate.txt` — the sequences correspond, with the license pair added at the tail.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** No whitespace-only block pair and no re-indentation signature fires in this file (0 and 0); the delivery move's seam (B47) is charged to section 3, not here. This section is empty by measurement, stated with its ground.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the measurement is zero.
- **Verify:** classification.json's counts for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None in the annotation sense. The candidate carries no `[!-- … --]` porter note and no 訳注： its only bracket-comment block (candidate L149–155) is a commented-out specimen table inside an exhibit, carried from the original and translated with the body (section 6). The port's explanations ride in the license box's prose (section 1) instead.
- **Why:** R2: porter-added text is part of the change record; here the check was run and the answer is genuinely none, stated with its ground rather than left blank.
- **Verify:** `grep -n '\[!--' candidate.txt` returns the specimen table only; read candidate L149–155 against the original's corresponding exhibit.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three pseudo-ref errors: class (iii) draft form (KB-41), the delivery addresses of section 3; its two warnings stand below error level and name no class (i) item. (2) The render row's items, both DISPOSITIONED in the ledger (c2) register: the page's runtime-hotlink site-theme chain (environment-layer, KB-40) and the sample's credit-modal with runtime-hotlink (preview-form property: credit:start-preview has no modal mechanism — GOSIGN-TESTS.md T2 note, 2026-11-16 ruling; KB-32); T3 recorded nothing beyond cross-cutting items. (3) T4's findings (LOCALIZE-ROWS row 252): the credit item FIXED as to fields with the pointer-form gap recorded in section 1; the asset item DISPOSITIONED (class (ii) / KB-58); the header item DISPOSITIONED (ruling 2). The duplicated toggle include and the duplicated font import (sections 2 and 4) are not named in any (c3) disposition; they were carried as surviving items in the per-theme record, not folded into dispositions they never received, and have since been repaired (0c327f3), as has the pointer-form credit of section 1.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 1, 2, and 4.
- **Disposition:** DISPOSITIONED (items 1–3); the two duplications and the pointer-form credit were recorded, not dispositioned, and have since been repaired (0c327f3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 236): exit 1, 3 errors / 2 warns / 0 info; the errors are pseudo-ref ×3, the standing class of section 11(1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H): FAIL/FAIL with FINDINGS, the items of section 11(2), all dispositioned. (c) T4/T5 (LOCALIZE-ROWS row 252): FINDINGS jointly, display-affecting findings 2, dispositioned as in section 11(3) and the ledger §(c3) line (P3 FIXED; P5 DISPOSITIONED, class (ii) / KB-58; P9 DISPOSITIONED, ruling 2). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +131/−108 in 50 change blocks; the GNU-diff count of the same pair is 190 changed lines, and the difference is alignment choice across the delivery move, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:atlas-maniacus-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 253; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### What survived the fix waves (three small items, one file; repaired)

This theme's record is a study in what field-level verification cannot see. The credit waves normalized and checker-verified the eight fields, and the fields are impeccable — while the author field points instead of naming, in a file whose own info block names thd-glasses twelve lines later. The duplicate-@import sweep cleaned 29 themes, and this file was not among them, so its Do Hyeon pair (two URL grammars, adjacent lines) survived — a reminder that a sweep's coverage list is part of its result. And the sidebar-toggle include stands twice, once from the original and once from an unrecorded addition, a duplication no checker counts because includes are verified one by one, never as a multiset. None of the three changes the ledger's verdict on the evidence the ledger weighed; all three are the kind of item a documentation pass exists to catch, because each is provable from the candidate's bytes alone and each has a one-line repair. They were flagged here and in the batch report for the coordinator. The repairs have since landed (fix report FIX-MPURE1.md in the campaign record, R/review-scout/; canonical commit 0c327f3, with the usage-example sweep lines re-applied on top in 780e048): the duplicated toggle-sidebar include at old candidate L23 was removed (the candidate L1 include, the original's position, is retained); the duplicated Do Hyeon @import in the legacy `css?family=` grammar was removed (the `css2` form remains, candidate L177); and the credit field and the license-box author, which as built were pointers to the original page, now name thd-glasses (candidate L17 and candidate L405). This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

### The usage example's posting name

The usage references at candidate L44, L91, and L104 as built named the theme by its plain slug on the JP branch — `:scp-jp:theme:atlas-maniacus` at L44 and the opened include forms at L91 and L104 — so the examples named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed all three references to `:scp-jp:theme:atlas-maniacus-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), three of its 287 repairs across 157 candidates; after the M-pure-1 repairs landed on top, the sweep lines were re-applied in canonical commit 780e048, which is the form this package documents (candidate L44, L91, and L104 in the current numbering). This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-atlas-maniacus-jp.txt` is the decoration sample the render checks ran against (its credit-modal state is section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The candidate has no base-theme include (its CSS is self-contained, section 3); there are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 아틀라스 마니아쿠스 테마
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/theme:atlas-maniacus — revision 4
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
