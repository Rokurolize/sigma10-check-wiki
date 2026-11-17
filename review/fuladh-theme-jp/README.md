# Review package — theme:fuladh-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:fuladh-theme-jp — origin EN, population #92 [GOSIGN2-LEDGER (b) row 92]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 92]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (hotlink×5, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 82; GOSIGN2-LEDGER (b) row 92]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 page pending (batch exit 1 pre-analysis baseline timeout); sample overflow 337–419px@≤375 + credit-modal; §24 sticky note and §30 static credit panel illegible pale-on-pale both engines. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 92, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 92]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 92]
- Computed against: canonical commit c2a8bee9d16b617b214f78f99e32d0f4be6a1c94; candidate file pages/theme:fuladh-theme-jp.txt sha256:3cd8428b2d1128a2e2215b139915758a13a2ae2fa4fc8c1ff6f1ac426f48da55; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 92) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×5 + pseudo-ref ×1 (classes (ii)/(iii), section 11); the T4 item P5 (section 11). The render check for this theme is coverage-incomplete (its T2 page never ran; section 12) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:fuladh-theme | theme:fuladh-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 23 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-fuladh-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:fuladh-theme-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 927 lines / 24,985 bytes | 903 lines / 25,946 bytes |
| SHA-256 | 7b036d8e077425c937b31c3ed657b8567d7d8deb90ab7fb02af8f86e0e23fb62 | 3cd8428b2d1128a2e2215b139915758a13a2ae2fa4fc8c1ff6f1ac426f48da55 |

Wave history: the candidate was created by the Stage 2 EN10 integration (commit c210f75, the LOCALIZE-S2-A wave's port); 1869877 (FIX-CREDIT-D) normalized the translator attribution; c2a8bee (FIX4-LICENSE) restored the license-box furniture (KB-63) — the box a reviewer sees in the candidate today is that restoration, in the condensed JP form and at the wave-standard position (section 1). No production JP counterpart exists, so the R4 adoption question does not arise.

## Summary

An Amoni-Ram BHL port whose diff is dominated by formatting: 88 of its 155 change blocks are single whitespace-only line deletions inside the CSS body, disclosed as their own class in section 9 so the semantic change set can be seen cleanly. That set is the standard one, completely applied: the triple base delivery rebuilt on the JP BHL distribution (base include, repointed imports, frames at priorities 1 and 2), the EN info pair and bare Rate replaced by the JP preview credit block, the license box restored in JP backend form, the JP font supplement added and the display face's load moved from a third-party mirror to Google Fonts, the tail own-layer delivery repointed to the draft host at priority 3, and the prose translated in full. One recorded item stands by disposition: the five asset references that remain on EN storage (KB-58). Measured churn (diff.md, the generator's difflib count with autojunk off: +204/−228, 432 changed lines in 155 change blocks; the generator's Tier 2 summary for this package carries no separate hunk count).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 155 change blocks — 125 specific (80.6%), 27 heuristic (17.4%), 3 residue (1.9%), 0 skipped. The specific share is inflated by the 88 WS-ONLY blocks; the semantic specific blocks are 37. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 2 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 5 |
| FONT-IMPORT | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 5 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 22 |
| TRANS-UNANCHORED | 27 |
| WS-ONLY | 88 |

Adjudication for this README (every non-WS specific block was read against the bytes): the five EXHIBIT-RESTRUCTURE primaries are include repoints (B3, B5, B152, B154) and the license box's original-position block (B151), adjudicated in sections 1 and 8 — no exhibit was restructured. The three residue blocks resolve as two translated section headings (B8, `+* Info` → `+* 情報`; B15, `+* Examples` → `+* 例`) and a blank-line placement difference at the code exhibit's closer (B150). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:fuladh-theme-jp; original theme:fuladh-theme on scp-wiki at reference revision 23; candidate `pages/theme:fuladh-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard). The candidate's head restructures the original's single gate into the wave's two-part form: an unconditional `[[iftags]]` wrapper carrying the JP BHL base include (candidate L1–3, B1/B2), then the localized gate `[[iftags +テーマ]]` (candidate L5) over the body.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate split is the T9 delivery form (the base include must not depend on the page's own tag), and the gate's tag is P2.
- **Verify:** The sources.tsv row for fuladh-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original carries the full EN furniture: a bare Rate and an info pair (the pair's deletion is B7's INFO-DEL), plus a license box at its tail (original L872–911: `license-box-theme` with blockquote per-file entries). The candidate replaces Rate + info pair with the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L22–31) carrying the eight ruling-3 fields (タイトル Fuladh Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Fuladh Theme; 著作権者 Miss Lapis; 作成年 2024; 初訳時参照リビジョン 23; the source link to scp-wiki.wikidot.com/theme:fuladh-theme). The license box stands in the candidate at L224–235 in the JP backend form (`license-box-backend`/`license-box-end`) with its five file entries condensed to one line each and their labels translated （ファイル名/著作権者/ライセンス/ソースリンク） — the same files, authors, licenses, and source links as the original's entries (amoniram.png, spaces.jpg with its Dragonfish600.jpg composite note, the gear-mask icon, image.png with SPChu.png, the cyberfancy pair). Two position facts matter for a diff reader: the candidate's box stands before the source-code exhibit rather than at the tail, and the diff therefore shows the original's tail box as a 43-line deletion (B151, orig 869–911) — a relocation, not a loss (section 8). The box's current form and position are the FIX4-LICENSE restoration (c2a8bee, KB-63): the EN10 port had dropped the furniture, and the fix wave restored it in the JP form. T7 credit-module CSS: 2 matching lines on each side, inherited unchanged.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate and the EN info pair are deleted rather than duplicated (KB-09, KB-10). Ruling 3 fixes the eight fields. The license box is the TASL record for the theme's third-party artwork; KB-63 is the restoration pattern.
- **Verify:** `grep -n 'module Rate\|component:info' candidate.txt` returns nothing; read candidate L22–31 against the eight fields and L224–235 against original L872–911 entry by entry.
- **Disposition:** Applied (the box's restoration is FIX4-LICENSE's recorded fix, not a disposition).

### 2. Includes and components

- **What:** Every live foreign include is repointed: the two head frames and the tail frame to `:scp-jp:component:interwiki-style` (B3, B5, B154), the hidden tail div's `:scp-jp:theme:extra-black-highlighter-theme` (candidate L892, B152 — its neighbours toggle-sidebar-bhl and betterfootnotes were already `:scp-jp:`-form in the original's tail div and stand unchanged), the credit pair and license pair (section 1), and the base include `:scp-jp:theme:black-highlighter-theme` (candidate L2). The usage exhibit's escaped BHL include follows (`@@[[include :scp-jp:theme:black-highlighter-theme]]@@`, candidate L52–53, B14). No live include in the candidate names a `:scp-wiki:` target.
- **Why:** P1 (KB-15) for the component repoints; T9 for the base include — a dependent theme imports the base's JP port candidate, never the raw upstream delivery.
- **Verify:** `grep -n '\[\[include' candidate.txt` against the list above.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** Base (T9), the triple form: the original imports BHL from the upstream distribution host nu-scptheme.github.io (module imports and both frame parameters, original L3–15); the candidate repoints all of them to the JP distribution scp-jp.github.io/Black-Highlighter (candidate L8–9 imports; frame parameters at candidate L14 and L19, B4/B6), adds the JP BHL candidate include (candidate L2), and keeps the frames at priority=1 (normalize) and priority=2 (BHL). Own layer (T3): the original's tail module and priority=3 frame name its own code on EN storage (`https://scp-wiki.wikidot.com//local--code/theme%3Afuladh-theme/1`, double slash included, original L921–926); the candidate repoints both to its own code on the draft host (candidate L897–902, B153/B155). The delivered body is the candidate's own `[[code]]` block (the /1 index), as in the original.
- **Why:** P4/T9 (base delivery from the JP distribution) and P6/T3 (the layered frame stack: 1 normalize / 2 base / 3 own). The draft-host form of the own-layer lines is KB-41, class (iii).
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` against the list above.
- **Disposition:** DISPOSITIONED (draft-host own-layer lines, class (iii)); the base repoint and frame stack are applied.

### 4. Fonts and assets

- **What:** Fonts (P7), at the head of the delivered CSS (B59, candidate L240–243): the candidate adds the JP supplement load (Google Fonts Noto Sans JP, weights 400;700) and repoints the display face's load — Iceberg was loaded from the third-party mirror fonts.bunny.net (original L223); the candidate loads Iceberg and Domine from fonts.googleapis.com. The stacks follow: `--header-iceberg: Iceberg, "Noto Sans JP"` (candidate L252) gains the JP face as its fallback. Assets: five references stay on EN storage (scp-wiki.wdfiles.com) in the CSS body — the theme's Amoni-Ram artwork and backgrounds; these are the T1 row's five hotlink errors and the T4 row's pattern-5 item.
- **Why:** P7/T5 for the supplement and stack entry; the load repoint is KB-17's shape (a font load moved to its canonical host, family unchanged). P5/KB-58 for the assets: EN-storage hosting is the deferred state — re-upload is barred by owner order, and posting is where the hosting question is settled.
- **Verify:** `grep -n '@import' candidate.txt` — the delivery imports of section 3 plus the three font loads above. `grep -cn 'scp-wiki.wdfiles.com' candidate.txt` — 5.
- **Disposition:** DISPOSITIONED (assets, class (ii) / KB-58; section 11); the font changes are applied.

### 5. Header, sidebar, and site furniture

- **What:** The theme's four header-variable lines (`--header-title`, `--header-subtitle`, `--logo-image` and their kin) stand in both files and do not appear in the diff: they are carried over unchanged, values included, and no record charges them (the T4 row for this theme carries no P9 item). The sidebar furniture comes from the base and the tail div's components (section 2); the theme's own sidebar and topbar rules are inherited unmodified.
- **Why:** P9/T6 is the variable class; unchanged variables are recorded so a reviewer does not have to diff-hunt for a header change that never happened.
- **Verify:** `grep -n -- '--header-' candidate.txt` and compare with the same grep on original.txt — the same lines.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The prose is translated in full: the Info section (candidate L33–45, including the Amoni-Ram description with its rounderhouse link kept, B9), the contents list (L37–41), the Usage section (L45–53), the specimen texts, and the license entries' labels (section 1). The 27 TRANS-UNANCHORED and 22 TRANSLATION-ANCHORED blocks are this mass, resolved by shape in the appendix. Proper names stand (Amoni-Ram, Black Highlighter, the file names and authors in the license entries). No English instruction or label survives outside proper names.
- **Why:** P10 and KB-18: reader-visible strings are translated, license furniture included, because the license box is part of what a user reads and copies.
- **Verify:** diff.md's prose sections in order; `grep -n 'This is\|This theme' candidate.txt` returns nothing.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The candidate's live outbound links are the credit block's source link (candidate L30) and the license entries' source links (candidate L229–233: scp-wiki's rounderhouse-gold-proposal, Wikimedia Commons, game-icons.net, the Wanderers' Library — the original's own attribution links, carried over as the TASL record requires). The credit source link names scp-wiki.wikidot.com/theme:fuladh-theme, the original's recorded host in sources.tsv — the serving form, not a defect. The Info prose's rounderhouse link is likewise the original's, kept.
- **Why:** P11 under the dead-reference evidence standard: a link is charged when its target does not serve or a JP counterpart exists; attribution links are the record itself and are never repointed.
- **Verify:** `grep -n 'https\?://' candidate.txt` outside CSS lines — the links above.
- **Disposition:** Standing.

### 8. Structure

- **What:** One relocation, adjudicated: the license box (section 1) stands before the source-code exhibit in the candidate and at the tail in the original, so the diff shows an insertion at candidate L224–243 (B57/B58) and a deletion at original L869–911 (B151). The entry census decides: all five file entries, with authors, licenses, and source links, are present on both sides — nothing was dropped, so the R3 question does not arise. The classifier's remaining EXHIBIT-RESTRUCTURE primaries (B3, B5, B152, B154) are include repoints in exhibit-adjacent lines. No other structural change: exhibits, specimens, and the CSS body's internal order are preserved.
- **Why:** R3 exists to force exactly this adjudication, because a relocation and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare original L872–911 against candidate L224–235 entry by entry.
- **Disposition:** Standing; no class I item.

### 9. Formatting only

- **What:** 88 WS-ONLY blocks (B60–B149 passim), each the deletion of one whitespace-only line (a line holding a single space) inside the CSS body, plus one residue block (B150): a blank line's placement at the code exhibit's closer (original L868 area; candidate L886). This is the R7 hazard in its disclosed form: any future diff against this candidate will show these 89 formatting differences again, and they are recorded here so that future diff is read as formatting, not as 89 semantic changes. No re-indentation and no line-ending conversion (0 and 0).
- **Why:** Formatting churn is disclosed as its own class (R7) so it is never mistaken for a semantic change; at this volume the disclosure is the section's whole point.
- **Verify:** The WS-ONLY blocks are diff.md's single-space-line deletions; their count is classification.json's label count for WS-ONLY (88).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. This candidate carries no `Ported for SCP-JP` banner, no `[JP]` markers, and no translator-note comments; its provenance record is the credit block and this package.
- **Why:** R2: the absence is recorded so a reviewer does not have to wonder whether annotations were overlooked.
- **Verify:** `grep -n 'Ported for\|\[JP\]\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items. (1) T1's five hotlink errors: class (ii) — the EN-storage asset lines of section 4, posting-time hosting state (KB-58); the ledger's §(c1) hotlink line dispositions the class. (2) T1's one pseudo-ref error: class (iii), draft-wiki form — the candidate's own draft-host delivery lines (section 3). (3) T4's P5 item (the EN-storage assets): DISPOSITIONED, class (ii) / KB-58, per the ledger's §(c3) line. The render row for this theme records no findings because its T2 page never ran (section 12); there is nothing further to disposition.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); KB-58), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 82): exit 1, 6 errors / 1 warn / 1 info (hotlink×5, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN10)): the row records "T2 page pending (batch exit 1 baseline timeout)" — the render comparison for this theme never produced a page, so there is no render verdict to cite; the ledger's PASS for this theme rests on the T1 and T4 records and the dispositions above, and this package records the coverage gap rather than papering over it. (c) T4/T5 (LOCALIZE-ROWS row 92): FINDINGS jointly, display-affecting count 1 (the EN-storage assets); the ledger's §(c3) line dispositions P5 for this theme. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +204/−228 in 155 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance; a check that never ran is reported as never run.
- **Verify:** Re-run the checker on `pages/theme:fuladh-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 92; go-sign, COMPLETION-REPORT §10), with the render coverage caveat recorded above.

## Appendix — heuristic and residue mass, resolved by shape

Class M treatment: the 27 heuristic blocks are not listed one by one; they fall into the shapes below, each verified against the bytes at the cited ranges. The 3 residue blocks are listed in full. The 88 WS-ONLY blocks are treated in section 9.

| Shape | Blocks | Where | Resolution |
|---|---|---|---|
| Prose translation (unanchored) | B9, B12 and the TRANS-UNANCHORED body mass | candidate L33–220 | P10 translation (section 6) |
| License box at its original position | B151 | original L869–911 | Relocation pair with B57/B58 (sections 1, 8) |
| Residue: section heading translation | B8 | candidate L33 (`+* 情報`) | P10 translation of the `+* Info` heading |
| Residue: blank-line placement at the code closer | B150 | candidate L886 | Formatting (section 9) |
| Residue: section heading translation | B15 | candidate L58 (`+* 例`) | P10 translation of the `+* Examples` heading |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-fuladh-theme-jp.txt` is the decoration sample the render checks ran against; for this theme the render page never ran (section 12), so the sample carries no findings of its own. It belongs to this theme's record but carries no port change of its own to explain here. The base include `:scp-jp:theme:black-highlighter-theme` and the extra-BHL include are other candidates in the population with their own packages; this theme's record names them as dependencies, not changes. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
