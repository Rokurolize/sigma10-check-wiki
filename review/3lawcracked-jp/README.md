# Review package — theme:3lawcracked-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:3lawcracked-jp — origin EN, population #46 [GOSIGN2-LEDGER (b) row 46]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2c5a9a8e18b184a17f1da96a3002c0994c151a4b1cda7a8e823c27fba30f3477); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 0 infos (hotlink×5); standing classes dispositioned in register c1 [T1-ROWS row 46; GOSIGN2-LEDGER (b) row 46]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — inherited Third-Law header clipping at ≤375; font-bauhaus ORB single-combo artifact (X7 family); no new candidate-specific defect. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 46, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 46]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 46]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:3lawcracked-jp.txt sha256:2c5a9a8e18b184a17f1da96a3002c0994c151a4b1cda7a8e823c27fba30f3477; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 46) |
| Wave history | Three commits touch the candidate: creation by the Stage 2 EN batch (3205f27), the FIX-P4 commit (f1138e4: frame, translator field, JP font import and stack), and FIX4-CREDIT (9fbcd94: the T7 credit-CSS supplement, +12 lines). Each is narrated in the section it belongs to |
| Standing items | **DISPOSITIONED** — T1 hotlink ×5 (class (ii), section 11); the iftags structural suspicion (FIX3-S2EN §6.11); the render row's inherited header clip (KB-35 family) and ORB artifact (KB-47 family) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:3lawcracked | theme:3lawcracked-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 17 (first translation; the candidate's credit block records 初訳時参照リビジョン: 17) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-3lawcracked.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:3lawcracked-jp.txt`, copied at worktree HEAD 1605bbd; the file's last content change is commit 9fbcd94 (FIX4-CREDIT) |
| Lines / bytes | 44 lines / 1,421 bytes (the last line carries no trailing newline, so `wc -l` reports 43) | 397 lines / 8,656 bytes |
| SHA-256 | 75b1a169c80c54cf1a3eee501740b9d48228212ba2ce081169dc7b4a33f0dddc | 3d65aaeaa1f340dcbe4fff324022f6395f77c334eada638b8938e785b554196c |

This package is the sibling of review/3law-pride-jp/: the same variant shape over the same inlined base, differing in the variant's own rules, its reference revision, and its render record. The shared sections below are stated in full rather than by cross-reference, so this package stands alone; where the two genuinely differ, the text says so.

## Summary

The original is a 44-line variant page: it gates on `+theme`, imports the base Third Law code delivery in a head module, shows a bare Rate module, gives the two include lines (base + variant) as usage, exhibits its own 25 lines of CSS in a `[[code]]` block, and imports its own code delivery in a tail module. The candidate rebuilds it exactly as its sibling was rebuilt: the JP preview credit block with the eight ruling-3 fields replaces the bare Rate; the base stylesheet is inlined into the candidate's single live `[[module CSS]]` (inline since the creation commit); the variant's own CSS (the cracked background, header image, and slogan) follows the base inside the same module; delivery is the campaign frame at priority 1 (added by f1138e4, together with the translator field's ruling-3 form and the JP font supplement); and FIX4-CREDIT appends the credit-module CSS carried from the production base page, which the candidate had dropped (section 1). Measured churn (diff.md, the generator's difflib count with autojunk off: +375/−22 in 11 classifier change blocks; a GNU-diff count of the same pair gives +371/−18 — alignment choice, not content). Almost all of the +375 is the inlined base body.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 11 change blocks — 10 specific (90.9%), 1 heuristic (9.1%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 5 |
| WS-ONLY | 3 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| RESTORATION | 1 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the one heuristic block (B2, the original's base-delivery @import line) resolves as in the sibling package — it is the declared base's delivery line and the port's answer is the inlining (section 3). The RESTORATION primary (B4) is a topology-matcher artefact: it pairs the original's prose lines with the inlined base's comment header, which shares vocabulary with them; nothing was "restored" in this theme, and the prose itself is translated at candidate L20 and counted in section 6. Two DELIVERY-MOVE primaries (B5 and the B6 pairing) are the same artefact family. The EXHIBIT-RESTRUCTURE primary (B6) is adjudicated in section 8. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:3lawcracked-jp; original theme:3lawcracked on scp-wiki at reference revision 17; candidate `pages/theme:3lawcracked-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch (commit 3205f27), with the base theme:3law stylesheet inlined as part of that derivation (candidate L24 declares it: **基盤:** 3law（インライン）). Not adopted from a production JP counterpart (the R4 question): no production page for this variant exists as a separate record, and the inlined base body is the EN base's text. The production counterpart enters at exactly one point, the T7 supplement of section 1. The frame order changed as in the sibling: frame first (candidate L1–5), then the gate (L7), where the original opens with its gate and delivery module.
- **Why:** Section 0 declares the provenance route so the +375 added lines are read as base inlining, not authorship; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for 3lawcracked-jp; `sha256sum original.txt` against the Provenance table; read candidate L20–28.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L6–8) and nothing else. The candidate deletes it (block B3) and installs the JP preview credit block (candidate L9–18) with the eight ruling-3 fields (title 第三法クラックド・テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Third Law Cracked CSS Theme; 著作権者 TyGently; 作成年 2018; 初訳時参照リビジョン 17; the source link, host-verified in section 7). The translator field took its ruling-3 form in f1138e4 (SCP-JP → AI). The wave edit this theme is in class U for is the same as its sibling's: FIX4-CREDIT (commit 9fbcd94, +12 lines) appended the credit-module CSS at candidate L383–394 — a porter comment (L383–385, naming the base family this variant inlines) and the two rules (`.creditModule .rate-box-with-credit-button .creditButton` and its `:hover`, #222e59 / #0c1121 / #404d7e) carried verbatim from the production counterpart `pages-existing/existing:theme-3law.txt` lines 356–365, which carry the identical rules in the identical palette. The candidate as created had no credit-module CSS while the production base page styles the credit button; the repo-level review recorded this defect shape for this theme, and FIX4-CREDIT is the repair. The classifier's T7 block sits at candidate L381–396.
- **Why:** P3/T1 (the preview credit module is rate-bearing, so the bare Rate is deleted, KB-09) and T7 (KB-11: the JP credit module's DOM needs rules the branch original never shipped; where a production counterpart carries them, the supplement is carried verbatim). Ruling 3 fixes the eight fields and the translator form.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L9–18 against the eight fields; read `pages-existing/existing:theme-3law.txt` L356–365 against candidate L386–393 — the rule bodies are identical.
- **Disposition:** FIXED (credit fields by the credit waves per GOSIGN2-LEDGER §(c3); the T7 supplement by FIX4-CREDIT, commit 9fbcd94). No license box exists on either side, so the T4/KB-63 question does not arise.

### 2. Includes and components

- **What:** The candidate's includes are the frame (candidate L1), the credit pair (L9/L18), and no others. The original's usage names two includes (`theme:3law` then `theme:3lawcracked`, original L12–13); the candidate's usage names one (`theme:3lawcracked-jp`, candidate L22), because the base include's content is inline (section 3). No foreign include survives, and no component had to be ported alongside (ruling 4 not engaged).
- **Why:** P1 (KB-15) governs include targets; the operative fact is the base's delivery form (section 3). A kept `:scp-wiki:` include would be a class (i) foreign-include error; there are none.
- **Verify:** `grep -n '\[\[include' candidate.txt` — three includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers by @import twice: the base's code (`local--code/theme%3A3law/1` on scp-wiki.wdfiles.com, original L3, the classifier's heuristic block B2) and its own code (`local--code/theme%3A3lawcracked/1`, original L43). The candidate delivers once: the interwiki-style frame at candidate L1–5 (added by f1138e4) at priority 1, `theme=` naming the candidate's own `local--code/theme%3A3lawcracked-jp/1` on the draft host. The original's tail self-import module was not carried over at all (verified against the creation version, which ends at its `[[/module]]`), and the candidate's single `[[module CSS]]` (L26–395) holds the JP font import (L27), the base's station-font import (L28, section 4), the inlined base body (L30–358), the variant's own rules (L359–381), and the T7 supplement (L383–394). The inlining predates every fix wave (the creation file is already ~379 lines). As with the sibling, the FIX-P4 wave's title ("pattern-4 repoint of base-theme CSS imports to JP port candidates") is broader than this file's diff, which is the frame, the translator field, and the font supplement; flagged here and in the batch report.
- **Why:** P4/T9 and P6/T3, as in the sibling package: the variant cannot @import a JP base candidate that does not exist, and keeping the EN base's delivery line live would keep a foreign delivery. The frame's draft-host `theme=` URL is KB-41, class (iii), rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — one hit, the frame's `theme=` line; `git show 3205f27:pages/theme:3lawcracked-jp.txt | wc -l` returns ~379, proving the inlining is original to the port.
- **Disposition:** DISPOSITIONED (the draft-host frame line, class (iii)); the base-delivery form is the port's standing shape, recorded here.

### 4. Fonts and assets

- **What:** Font load (arrived in f1138e4): candidate L27 adds the Google Fonts Noto Sans JP @import, and candidate L123 adds `"Noto Sans JP"` to the header-title stack (`'stationmedium', Arial, "Noto Sans JP", sans-serif`). The base's font file import is kept verbatim on the EN host (candidate L28: `station-font.css`, scp-wiki.wdfiles.com). Assets: four image URLs stay on scp-wiki.wdfiles.com — the base's `body_bg_7.png` (candidate L68) and `PL_3Law_Logo_2.png` (L73), and the variant's own `body_bg_cracked.png` (L371) and `crackedbase.gif` (L376). Together with the station-font import these five lines are the T1 checker's hotlink ×5 (one more than the sibling, which has one variant image, not two).
- **Why:** P7/T5 with KB-16 (the font load gap): the LOCALIZE row charged "no Japanese font specified"; the fix is the import plus the stack that renders Japanese header text. P5 with KB-17: the five EN-host file lines are posting-procedure re-hosting, class (ii), per the ledger §(c3) outcome for this row ("asset hosts = class (ii)").
- **Verify:** `grep -n 'Noto Sans JP' candidate.txt` — two hits (L27, L123); `grep -n 'wdfiles' candidate.txt` — the frame line plus the five class (ii) lines.
- **Disposition:** Font supplement applied (f1138e4); the five EN-host file lines DISPOSITIONED (class (ii) / KB-58 family).

### 5. Header, sidebar, and site furniture

- **What:** No header variable is overridden (no `--header-title`, `--header-subtitle`, or `--logo-image` in the candidate); the header is the inlined base's rules, including its `content:` strings (`"Third Law "`, candidate L129; `'Scientia Potentia Est '`, L140) and the variant's slogan (`'SOMETHING ISN\'T RIGHT... '`, L380), all kept in English. The render row's items are an inherited Third-Law header clipping at ≤375 and a font-bauhaus ORB single-combo artifact; the row's own closing assessment is "no new candidate-specific defect".
- **Why:** Header language is dispositioned under ruling 2 per the ledger §(c3) outcome for this row (KB-57 family). The clip is the narrow-width header clip/collision family (KB-35; FIX3-S2EN §6.5); the ORB item is the load-block/delivery-MIME artifact class (KB-47 family): a single-combo symptom whose remedy, where the blocked asset is a candidate asset, is the posting-time re-hosting class, and no source defect is identified.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; the items' record is RENDER-ROWS-1 (RENDER-S2-A (EN1)).
- **Disposition:** DISPOSITIONED (ruling 2 for the strings; KB-35 and KB-47 families for the render items).

### 6. Text translation

- **What:** The translated text is the intro prose (original L10–13 → candidate L20, with usage and base restated at L22 and L24) and the credit block's fields (section 1). The inlined base's CSS comments stay in English (porter-visible only), and its `content:` strings stay as designed (section 5). The original's hub link `[[[third-law-hub|Third Law]]]` does not survive into the candidate's compressed intro, as in the sibling; no JP hub counterpart is named in the file. R5 glyph-form conversion: none (English source). R1 in-CSS text: the base's comments are untranslated, stated here rather than passed over; no string-valued variable carries reader-visible text in this theme.
- **Why:** P10 for prose and fields; KB-18 covers reader-visible strings, not comments. The hub link falls under P11's evidence standard (no verified JP counterpart recorded; compression chosen over an unverified repoint).
- **Verify:** Read candidate L20–24 against original L10–13.
- **Disposition:** Standing (the port itself); the dropped hub link is recorded, not hidden.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L16): `[*https://scp-wiki.wikidot.com/theme:3lawcracked ソース]`. Its host is the original's recorded host in review/sources.tsv (scp-wiki.wikidot.com), so the jiha-class defect (a source link naming a non-serving host form) does not arise and no probe was needed. The usage include line is section 2's; the CSS file URLs are section 4's.
- **Why:** P11, under the dead-reference evidence standard.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Standing; no dead reference found in this file.

### 8. Structure

- **What:** The localize.md closing rule holds in the form this port allows: the inlined base keeps its names, selectors, and internal order whole, and every JP correction arrives outside it (frame and credit block before it, font import at the module's head, T7 supplement appended at the module's tail, candidate L383–394). The classifier's EXHIBIT-RESTRUCTURE primary (B6) adjudicates as in the sibling: the original's one exhibit (its own CSS in a `[[code]]` block, original L15–39) is neither dropped nor replaced — the variant's rules survive verbatim inside the candidate's live module (candidate L359–381, comment header included). What changed is the exhibit's status: the CSS is delivered live from the module instead of displayed as a code exhibit, because the candidate is a self-delivering page. Census: exhibits 1 → 0, live modules 2 → 1, variant CSS present on both sides.
- **Why:** R3 forces this adjudication because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare original L15–39 against candidate L359–381 — the comment header and all three rules correspond line for line.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Three WS-ONLY blocks (B7, B8, B9), each a single separator line inside the inlined base or the variant block that differs only in trailing whitespace. The classifier finds no re-indentation anywhere (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Blocks B7–B9 in classification.json; the corresponding diff sections in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation: the T7 supplement's comment at candidate L383–385, naming the production source lines and the base-family ground. It rides inside the T7 block, which is why no separate annotation signature fired. There are no `[!-- --]` translator notes and no editor lines in this candidate; the skeleton's "none" for this section does not survive contact with the bytes and is corrected here.
- **Why:** R2: porter-added text is part of the change record, and this comment is the only in-file statement of where the supplement came from.
- **Verify:** Read candidate L383–385.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's five hotlink errors: class (ii), posting-procedure — the station-font import and the four image URLs on scp-wiki.wdfiles.com (section 4). (2) The LOCALIZE row's structural suspicion (theme CSS only inside the iftags gate): DISPOSITIONED per FIX3-S2EN §6.11 — the render reports did not confirm it; the theme renders with its CSS applied. (3) The render row's inherited header clip (KB-35 family) and font-bauhaus ORB artifact (KB-47 family), with the row's own closing assessment that no new candidate-specific defect stands. (4) Header and slogan language kept in English: ruling 2, per the ledger §(c3) outcome for this row.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above; the T1 lines are enumerable by the grep in section 4.
- **Disposition:** DISPOSITIONED (all four items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 46): exit 1, 5 errors / 1 warn / 0 infos; all five errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A (EN1)): FINDINGS, the two items of section 11(3), both dispositioned, with the row's closing assessment of no new candidate-specific defect; engine coverage the full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 46): FINDINGS jointly, display-affecting findings 3; the ledger §(c3) line closes the row's charges as DISPOSITIONED under the class outcomes, with the credit fields FIXED by the credit waves — and the file's own history adds the two later wave edits: f1138e4 (frame, translator field, font) and 9fbcd94 (T7 supplement). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +375/−22 in 11 change blocks; the GNU-diff count of the same pair is +371/−18, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:3lawcracked-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 46; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The base that is not there

Identical in shape to the sibling's record, and stated again so this package stands alone: there is no `pages/theme:3law-jp.txt` and no @import of one. The creation commit (3205f27) already inlines the EN base's stylesheet body into the candidate's module, the candidate's prose declares the shape (**基盤:** 3law（インライン）), and f1138e4's actual diff in this file is the frame, the translator field, and the font supplement — the FIX-P4 wave title ("pattern-4 repoint of base-theme CSS imports to JP port candidates") is broader than this file's diff. This package documents the form the port actually takes and flags the title mismatch; whether inlining or a standalone base candidate is the better long-term form is a posting-procedure question.

### Wave edits, in the order they landed

1. **3205f27** (Stage 2 EN batch 1, creation): the whole port — credit block, inlined base, variant CSS in the live module. The original's tail self-import module was not carried over.
2. **f1138e4** (FIX-P4): interwiki-style frame added at the head (candidate L1–5); translator field SCP-JP → AI; Noto Sans JP @import added (L27); `"Noto Sans JP"` added to the header-title stack (L123).
3. **9fbcd94** (FIX4-CREDIT): the T7 credit-CSS supplement appended (candidate L383–394, +12 lines), carried from the production base page's JP-localize rules.


### Post-package repairs (REFRESH3-D)

Recopy brought one post-package repair in: built at `f1c2cd0` before 722ceb5, the candidate still carried the dead frame parameter; the recopy removed exactly that line (8,656 → 8,575 bytes).

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3A3lawcracked-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- **Original evidence:** no original frame; self-delivery is an `@import` of its own code/1 at original L43 only. No other repair touches this file.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-3lawcracked-jp.txt` is the decoration sample the render checks ran against. `pages-existing/existing:theme-3law.txt` is the production base page the T7 supplement was carried from (section 1); it is a record source, not a port output. The base theme:3law has no JP candidate file (see the per-theme record). There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Third Law Cracked CSS Theme
- **Author:** TyGently
- **Source:** https://scp-wiki.wikidot.com/theme:3lawcracked — revision 17
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
