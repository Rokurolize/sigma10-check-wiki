# Review package — theme:black-rain-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:black-rain-jp — origin CN, population #168 [GOSIGN2-LEDGER (b) row 168]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now bfe8ebac919c49b4374e870f5afd06dea41aa82b47f14bb55904bd26c57d1f36); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 146; GOSIGN2-LEDGER (b) row 168]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form), page-overflow 337px@320 + 389px@375 chromium and 416px@320 + 419px@375 webkit (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host; T3 complete in the final report (pending in the partial) and clean on both pages (sidebar left JP position, mobile hamburger present in both engines and opens; sample 503 warnings were stylesheet resources only, page rendered normally); black-rain-logo 404 = deferred asset. [RENDER-ROWS-RERUN16 (CN2) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN2)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 167, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 167]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 168]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:black-rain-jp.txt sha256:bfe8ebac919c49b4374e870f5afd06dea41aa82b47f14bb55904bd26c57d1f36; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 168) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (iii)); the render items from the RERUN16 re-run (ledger (c2), section 11), the first render run having returned no machine verdict at all (a coverage caveat, section 12); T4's findings per the ledger (c3) line (P9, ruling 2) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:black-rain | theme:black-rain-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14 (the candidate's credit block records 初訳時参照リビジョン: 14) | — |
| Source of this copy | Campaign mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:black-rain-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 421 lines / 19,960 bytes | 436 lines / 21,547 bytes |
| SHA-256 | ea62ca9925bfab006c8cc45d03ef7296bee2d20bb7ec36b00df9f1f2be767be7 | 42fd3a91fe85c7ae9ac8ee6e1a8fa4a7d4e8707c09dfee7916232e1a569c7b18 |

Wave history: the candidate was created by the Stage 2 CN2 integration (commit cf1224e), aligned to the Wikidot source by the same wave (9244a7d), and touched by FIX-CREDIT-D (1869877, translator attribution normalization; the stamp's computed-against commit).

## Summary

A CN Black Highlighter reskin ("Black Rain") whose original delivers through the legacy BHL machinery twice over: two self-delivery modules (head and tail) and two hidden styleFrame iframe embeds, plus a BHL sidebar component include. The candidate strips all of that to the modern JP form: it layers over the production JP Black Highlighter page, frames the BHL CSS from the same github.io host JP's BHL uses, self-delivers its own code once from a head module, and carries the reskin's variables in a single code block. Its header defaults stay Chinese (dispositioned, ruling 2), its author field is a pointer (the original names no author), and its logo is a deferred attachment that 404s on the draft host until posting. Measured churn (diff.md, the generator's difflib count with autojunk off: +131/−122, 253 changed lines in 41 change blocks; a GNU-diff count of the same pair gives 189 changed lines — the difference is alignment choice across the translated body, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 41 change blocks — 22 specific (53.7%), 19 heuristic (46.3%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 19 |
| TRANSLATION-ANCHORED | 16 |
| SELF-DELIVERY | 3 |
| EXHIBIT-RESTRUCTURE | 3 |
| IFTAGS | 2 |
| DRAFT-HOST | 2 |
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: no residue blocks exist to adjudicate. The three EXHIBIT-RESTRUCTURE primaries resolve as the head-body logo delivery change (B5; section 4), the second code block's absorption into the single delivered block (B39; section 3), and the tail collapse where the legacy delivery machinery leaves (B41; section 3) — mechanism changes, not exhibits dropped; the exhibit census is one-to-one (section 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:black-rain-jp; original theme:black-rain on scp-wiki-cn at reference revision 14; candidate `pages/theme:black-rain-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN2 wave (sources.tsv kind: standard; no production JP counterpart of the reskin exists, so the R4 adoption question does not arise — but the theme's BASE does exist in JP production, which is section 2's fact). The frame order: the candidate opens with its base include (candidate L1), its delivery module (candidate L3–5), and a three-part interwiki frame (candidate L7–18), then the localized gate (candidate L20); the original opens with its head delivery module and its hidden embed.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frames are P6/T3 (section 3).
- **Verify:** The sources.tsv row for black-rain-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's only furniture is a `[[module Rate]]` (original L23–25 region); it names no author anywhere in its credit furniture. The candidate deletes the Rate (BARE-RATE-DEL, block B4) and carries a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L22–31) with the eight ruling-3 fields — its 著作権者 field a pointer, "原語版ページの作成者に同じ（scp-wiki-cn の theme:black-rain）" (candidate L27), because there is no name in the original to carry. LOCALIZE-ROWS row 167 records this as a §3 content insufficiency (minor): the field is well-formed and honest, and the insufficiency is the original's silence, not a porting loss (contrast theme:atlas-maniacus-jp in this batch, where the name exists in the file and the field still points). The source link (candidate L30) names `scp-wiki-cn.wikidot.com/theme:black-rain` — the original's recorded host. License box (T4): added at the tail (candidate L427–434): the logo file black-rain-logo.svg, its distribution in the original as the Black Highlighter logo, its license recorded as not stated in the original (posting-time author confirmation), and the 訳注 of section 10; the box's author parameter is the same pointer as the credit field's.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form (KB-09) and ruling 3 fixes the eight fields. A pointer field is the correct port of an original that names nobody; the row's "minor" grading stands.
- **Verify:** Read candidate L22–31 against the original's head furniture in diff.md.
- **Disposition:** FIXED (credit fields, by the credit waves; the ledger (c3) outcomes for this theme's row); the pointer form is standing, grounded on the original's silence.

### 2. Includes and components

- **What:** The load-bearing include is the first line: `[[include :scp-jp:theme:black-highlighter-theme]]` (candidate L1) — the reskin layers over the production JP Black Highlighter page, the cross-theme dependency rule applied (a dependent theme imports the base's JP form, never the raw upstream delivery). The original's corresponding layering ran through its CN BHL machinery (section 3), including a `:scp-wiki:component:bhl-dark-sidebar` include at its tail (original L411), which has no counterpart in the candidate: the JP BHL page supplies the sidebar form. The documentation's component exhibits are repointed to `:scp-jp:` forms, and the usage specimens (candidate L42–43) name two different things: the first, `:scp-jp:theme:black-highlighter-theme` (candidate L42), names the production JP Black Highlighter page, which is correct as built and was not a sweep line; the second as built read `:scp-jp:theme:black-rain` — the repoint changed the branch prefix but kept the plain slug, so it named a page that does not exist on scp-jp. The usage-example population sweep has since completed it to this candidate's posting name, `:scp-jp:theme:black-rain-jp` (candidate L43; SWEEP-USAGE.md; canonical commit b5cb724). One link is unprefixed, as the row notes: the body's `[[[theme:black-highlighter-theme|…]]]` reference (candidate L36), carried from the original's identical form (original L29) — on JP it resolves to the production BHL page, which is the intended target.
- **Why:** P1 (KB-15) for the repoints; the black-rain specimen's repoint as built satisfied the branch half of that rule only, and the sweep's completion is what brings it under it; the dependency rule (dependent themes import the base theme's JP delivery) for L1. The dropped bhl-dark-sidebar is a mechanism part of the CN delivery, succeeded by the base page's own furniture, not a lost component.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every target is `:scp-jp:` or a bare `component:` name; compare original L411.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers through four channels: a head module importing its code from `scp-wiki-cn.wdfiles.com/local--code/theme%3Ablack-rain/1`, a tail module repeating the import (original L412–415), and two hidden `[[embed]]` iframes pointing at the CN styleFrame (original L16–20 and L417–421) — the legacy BHL frame delivery, duplicated at both ends. The candidate delivers through one channel set: a head module (candidate L3–5) importing `local--code/theme%3Ablack-rain-jp/1` from the draft host; three interwiki frames (candidate L7–18: priority 1 and 2 frame the BHL normalize and core CSS from `scp-jp.github.io`, the host JP's own BHL delivery uses; priority 3 frames the theme's own code at the same draft-host address); and the code block's own head @imports of the same two BHL stylesheets (candidate L143–144). The tail module, both embeds, and the second code block's separation all leave (blocks B39, B41): the candidate's CSS is one code block (candidate L134–423) where the original had two. T1's two pseudo-ref errors are the draft-host addresses (the import and the priority-3 frame).
- **Why:** P4 (own-code delivery served from JP hosts) and P6/T3 (the frames). The legacy iframe delivery is the original's BHL-era mechanism; the JP BHL page's own delivery (github.io CSS plus frames) is the form the reskin adopts by layering over it. The draft-host form is KB-41, class (iii), rewritten at posting.
- **Verify:** `grep -n 'local--code\|styleFrame\|embed' candidate.txt` — the first returns the import and frame lines, the other two return nothing; compare original L412–421.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** The reskin declares no font loads of its own in either file: its typography is the BHL base's, inherited through the layering of section 2 and the BHL stylesheets of section 3 — the sample's font-host line in the render record is that base supply, an environment-layer item (section 11). Assets: the theme's logo. The original's body displays the EN BHL logo by raw image (original L25, `scp-wiki.wdfiles.com` black-highlighter-logo.svg) and its usage exhibit loads a jsdelivr logo (original L40). The candidate's exhibit (candidate L33) is an image-block naming `black-rain-logo.svg` on the draft host — the same logo carried as the candidate page's own attachment, per the license box's 訳注 (section 10). That attachment does not exist on the draft host yet: RERUN16 recorded black-rain-logo 404, a deferred asset. At posting the attachment lands and the address resolves; until then the exhibit's logo is a known 404, recorded here and in the register rather than discovered later.
- **Why:** P5 with KB-17/KB-58: own-page attachment in place of a foreign hotlink is the correct end state; the deferral is the posting procedure's, class (ii). Font supply inherited from the base is P7 by reference — the base's own record (the black-highlighter-theme package) carries it.
- **Verify:** Read candidate L33 and the license box (candidate L427–434) against original L25 and L40.
- **Disposition:** DISPOSITIONED (the deferred logo asset, class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The header defaults are Chinese and always displayed: `--header-title: "黑 王"` and `--header-subtitle: "神拘黑白 王宴绯青"` (candidate L159–160) — LOCALIZE-ROWS row 167's one display-affecting item (type 9, header defaults untranslated). The same pair is duplicated in a `:root:lang(cn)` block (candidate L181–185), the original's CN-locale override carried over whole: on a JP page the `:lang(cn)` condition never matches, so the block is dead weight — the row's "dead-rule duplication" observation, recorded as found; it changes nothing rendered, and removing it is a cleanup the coordinator may bundle with any future touch. No other header or sidebar adaptation was made; the RERUN16 T3 walk confirmed the sidebar sits at the JP position and the mobile hamburger opens in both engines (section 12).
- **Why:** P9/T6 for the furniture; ruling 2 grounds the header-language disposition (header/title language is out of scope for migration correctness). The dead `:lang(cn)` block is an observation, not a charge: it is the original's own rule, faithfully carried, inert in the new environment.
- **Verify:** Read candidate L159–160 and L181–185; the original's corresponding defaults are in diff.md's code sections.
- **Disposition:** DISPOSITIONED (P9, ruling 2: header/title language out of scope).

### 6. Text translation

- **What:** The body is translated in place: sixteen TRANSLATION-ANCHORED and nineteen TRANS-UNANCHORED blocks (the usage prose, the 注 note at candidate L36 explaining the BHL dependency, the standard examples), one CSS-BODY heuristic (B38, a single variable line inside the code). The credit block's title fields keep the work's Chinese name (黒色之雨 テーマ as タイトル, the original title as 原題） — names, not prose. The header defaults of section 5 are the one untranslated reader-visible text, charged there.
- **Why:** P10 and KB-18 (reader-visible strings).
- **Verify:** The body sections of diff.md in order; a Han-character scan of the candidate's body returns the credit fields and the section-5 defaults.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L30) names the original's recorded host (section 1). The body's BHL reference link is the unprefixed form of section 2, carried from the original and resolving to the JP production base. No prose link in the candidate targets a CN-wiki page, and no `http://` address remains (the original's protocol-relative iframe addresses left with the embeds).
- **Why:** P11: links name the serving original or the record's home.
- **Verify:** `grep -n 'http://' candidate.txt` returns nothing.
- **Disposition:** Standing; no dead link carried.

### 8. Structure

- **What:** The closing rule holds. The candidate preserves the original's order (furniture, documentation, code exhibit, closing gate) with the delivery machinery consolidated at the head (section 3) and the license box added at the tail (candidate L427–434) before `[[/iftags]]` (candidate L436). The exhibit census is one-to-one: the usage specimens, the examples, and the source exhibit are present on both sides; the original's second code block is absorbed into the candidate's single block at the same position, which is a delivery consolidation, not a content drop.
- **Why:** R3 exists to force this adjudication; the census decides for preservation.
- **Verify:** Compare the section sequences of the two files in diff.md.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** No whitespace-only block pair and no re-indentation signature fires in this file (0 and 0). The code's tab indentation is the original's, carried byte-for-byte in the unchanged regions (visible in the `--header-title` lines of section 5). This section is empty by measurement, stated with its ground.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the measurement is zero.
- **Verify:** classification.json's counts for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One: the 訳注 inside the license box (candidate L432), recording that the original hotlinked the CN BHL distribution's logo directly and that the JP version carries the same logo as the candidate page's own attachment, removing the external-distribution dependency (section 4's change, disclosed in the attribution). `grep -n '\[!--' candidate.txt` returns nothing; the annotation's form is a license-box field because its position is inside the box.
- **Why:** R2: porter-added text is part of the change record; its form follows its position.
- **Verify:** Read candidate L427–434.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two pseudo-ref errors: class (iii) draft form (KB-41), the delivery addresses of section 3. (2) The render items, all DISPOSITIONED in the ledger (c2) register on the RERUN16 evidence: the page's runtime-hotlink site-theme chain (environment-layer, KB-40); the sample's credit-modal (preview form), page-overflow 337px@320 + 389px@375 (chromium) and 416px@320 + 419px@375 (webkit) (the cross-cutting static-credit family), and the runtime-hotlink chain with the sample font host (KB-40); the black-rain-logo 404 as a deferred asset (section 4). The same register records T3 complete and clean on both pages, with positive confirmations (sidebar at the JP position; the mobile hamburger present in both engines and opening; the sample's 503 warnings were stylesheet resources only, the page rendering normally). (3) T4's findings (LOCALIZE-ROWS row 167): the header item DISPOSITIONED (ruling 2); the credit item is section 1's (the original's silence, minor); the `:lang(cn)` duplication is section 5's observation; the unprefixed link is section 2's.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the byte-level claims are the greps of sections 2, 3, and 5.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 146): exit 1, 2 errors / 1 warn / 1 info; the errors are pseudo-ref ×2, the standing class of section 11(1); there is no class (i) error. (b) T2/T3 render, first run (RENDER-ROWS-2, lane RENDER-S2-E): NO machine verdict on either page (render_check exit 2 twice, networkidle, no summary) and T3 recorded nothing pointable — a coverage caveat of the KB-44 family, recorded as a gap, not a result. (c) The re-run (RERUN16, CN2) supplied the missing verdicts: FAIL/FAIL with FINDINGS, the items of section 11(2), all dispositioned, with T3's positive confirmations recorded there. (d) T4/T5 (LOCALIZE-ROWS row 167): FINDINGS jointly, display-affecting findings 1, dispositioned as in section 11(3) and the ledger §(c3) line (P9 DISPOSITIONED, ruling 2). (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +131/−122 in 41 change blocks; the GNU-diff count of the same pair is 189 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance; a missing verdict is reported as missing until a re-run supplies it.
- **Verify:** Re-run the checker on `pages/theme:black-rain-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 168; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The usage example at candidate L43 as built read `@@[[include :scp-jp:theme:black-rain]]@@`: the porting wave's repoint changed the branch prefix but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:black-rain-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. The companion specimen on the line above (candidate L42) names `:scp-jp:theme:black-highlighter-theme`, the production JP page, which is correct as built and was not a sweep line. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-black-rain-jp.txt` is the decoration sample the render checks ran against (its credit-modal and overflow states are section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The candidate layers over `pages/theme:black-highlighter-theme.txt`, the production JP Black Highlighter page, whose own record is the black-highlighter-theme package in this batch; the deferred logo attachment (section 4) lands on this candidate page itself at posting. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 黑色之雨 主题版式
- **Author:** 原語版ページの作成者に同じ（scp-wiki-cn の theme:black-rain）
- **Source:** https://scp-wiki-cn.wikidot.com/theme:black-rain — revision 14
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
