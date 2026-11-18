# Review package — theme:turbo-vision-jp (EN → JP port, K6 production-migration route)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:turbo-vision-jp — origin EN, population #41 [GOSIGN2-LEDGER (b) row 41]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now d5c7e1a5aa596a6d15687fb7857c01b572e77b9c7f0a01680934600ff3b58eba); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 41; GOSIGN2-LEDGER (b) row 41]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 sample no machine verdict (webkit screenshot pixel-cap, deterministic); page error only runtime-hotlink; JFDot pixel-font stylesheet ORB-blocked at chromium-768 (candidate-inherent flakiness); offset blocks by design. [RENDER-ROWS-1 (RENDER-D2 row 41)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-D2 row 41)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 41, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 41]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 41]
- Computed against: canonical commit f4488f2d2948824238a2d06479f104f4aab0cf5d; candidate file pages/theme:turbo-vision-jp.txt sha256:d5c7e1a5aa596a6d15687fb7857c01b572e77b9c7f0a01680934600ff3b58eba; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 41) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (ii), section 11); the render row's four items (sample T2 no machine verdict, webkit pixel-cap; runtime-hotlink chain; the JFDot stylesheet ORB block, KB-47; offset blocks by design); T4 display-affecting 0. **One drift item is flagged by this package: at five link loci the candidate carries older forms than the current production page it would replace (per-theme record).** The verdict stamp as built read PASS: the candidate had not changed since the gosign2 T1-fix commit it was computed against; the FIX-MP12 landing (canonical commit f4488f2, Post-package repairs) changed eight loci after the build, so the regenerated stamp reads STALE with the record verdict standing |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:turbo-vision | theme:turbo-vision-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 54 (reference edition; upstream rev 54 changed only the font delivery host) | — |
| Source of this copy | Fetched 2026-11-17 (sources.tsv source: FETCH 2026-11-17), via the mirror store (class FETCH-REGEN, hash-verified against review/sources.tsv) | Canonical file `pages/theme:turbo-vision-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 1,445 lines / 37,780 bytes | 1,739 lines / 57,734 bytes |
| SHA-256 | c28a37187cdc6bcb768921c8a05f805b18d153a929411db17971dd8e9019f97f | 620613175be14bf1549ec0238eedcd738e6423d6be94c521ceb5ac56e3f7466f |

Wave history: the candidate descends from the canonical-sources import (d727e92) through the reconcile of 15 theme pages (ffad285), a trailing-whitespace normalization (3010ef7), the /start labels pass (ab71620), and the gosign2 T1 fixes for rows 1–44 (b816e10). Its substance is older than all of these: it is the pre-existing JP translation of the theme (translator oplax-counterpoint, 2024) carried into the campaign as the migration candidate — ledger kind K6, section 0.

## Summary

This package's diff is not a port performed by the campaign; it is the distance between the EN original at revision 54 and the JP translation that has served on scp-jp since 2024, adopted as the Sigma-10 migration candidate. That is why the churn is the batch's largest and its heuristic share the batch's highest: +563/−274, 837 changed lines in 173 change blocks / 32 diff sections by the generator's difflib count (GNU diff: 670 changed lines, +482/−188) — most of it the independent translation's line-level wording, not wave edits. The campaign's own delta against the production page is tiny and is recorded in `pages/phase17-diff-turbo-vision-jp.txt`: exactly one change, the credit reference revision 53→54 (per-theme record). What this package adds beyond that record is the three-way comparison a reviewer actually needs — original, candidate, and current production — and it finds one thing the phase-17 record does not mention: at five link loci the candidate preserves older forms (http:// URLs, a full-URL toggle-sidebar link) that production has since cleaned up, so posting the candidate as-is would revert production's link hygiene at those loci. That drift is flagged, with loci, in the per-theme record; it is not a port defect, and this package changes nothing.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 173 change blocks — 48 specific (27.7%), 116 heuristic (67.1%), 9 residue (5.2%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 91 |
| TRANSLATION-ANCHORED | 32 |
| CSS-BODY | 29 |
| INCLUDE-REPOINT | 5 |
| DRAFT-HOST | 4 |
| LINK-REPOINT | 4 |
| DELIVERY-HOST | 3 |
| ESCAPED-INCLUDE | 3 |
| EXHIBIT-RESTRUCTURE | 3 |
| SELF-DELIVERY | 3 |
| ASSET-REHOST | 2 |
| FONT-IMPORT | 2 |
| T7-CREDIT-CSS | 2 |
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication of the heuristic mass: for a K6 package the heuristic share measures the wrong thing if read as wave quality — the 116 heuristic blocks (91 unanchored translations, 29 CSS-BODY blocks) are the 2024 translation's divergence from the EN source, taken as data. They were shape-checked, not line-checked: the exhibit census (section 8) and the delivery census (section 3) are the checks that decide this package, and both are exact. The three EXHIBIT-RESTRUCTURE primaries adjudicate as repoints and the footnoteblock escape (section 8). The nine residue blocks collapse into the appendix, six of them one-word exhibit labels.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:turbo-vision-jp; original theme:turbo-vision on scp-wiki at reference revision 54; candidate `pages/theme:turbo-vision-jp.txt`. Provenance route: **K6** — a production JP page (`theme:turbo-vision` on scp-jp) already exists, and the candidate is that page's translation lineage carried as the migration candidate; sources.tsv records "production page theme:turbo-vision exists; migration is delivered as pages/phase17-diff-turbo-vision-jp.txt; production drift （一致）". The EN original is therefore the *reference edition*, not the translation's direct parent in the campaign's sense: the translation was made in 2024 against earlier revisions, and the phase-17 record reconciles it to rev 54.
- **Why:** Section 0 declares the route because it changes what every count means: the diff measures a translation's distance from its source, and the migration claim lives in the phase-17 delta (per-theme record), not in this diff's size.
- **Verify:** The sources.tsv row for turbo-vision-jp; `pages/phase17-diff-turbo-vision-jp.txt` (948 bytes, one change); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself, recorded in the ledger as LOCALIZE-B).

### 1. Credit and attribution

- **What:** The candidate's credit block (candidate L22–35) carries twelve field lines: the production page's legacy set （翻訳責任 / 原著者 / 参照版 — bumped to 54 / 原語版URL， with the URL values de-linked) *plus* the eight ruling-3 fields （翻訳責任者 oplax-counterpoint; 翻訳年 2024; タイトル; 原題； 著作権者 JakdragonX, Croquembouche; 作成年 2021; 初訳時参照リビジョン 54; 元記事リンク）. The two sets agree in value wherever they overlap — the duplication is the migration's belt-and-braces form, keeping the production page's own credit data readable while adding the standard fields. The original's bare Rate is deleted (BARE-RATE-DEL). T4's P3 charge for this theme was aimed at the production form (missing 原題 and four item-name variants); the candidate's block answers it, and the ledger records P3 FIXED. The credit module's CSS correction is one of the appended tail modules (section 10): the EN theme styles the credit anchor through a `<p>` wrapper inside `.creditButton`, while the JP credit module emits the anchor as a direct child, so the rule is retargeted to the JP structure with the EN declarations unchanged (T7-CREDIT-CSS ×2).
- **Why:** P3/T1 and ruling 3, applied to a K6 credit block whose first duty is not to lose the production page's recorded attribution; the field-versus-banner check passes (the banner and the fields name the same two authors).
- **Verify:** Read candidate L22–35; compare the legacy fields against `pages-existing/existing:theme-turbo-vision.txt`'s credit block.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3), LOCALIZE-B line: P3 FIXED).

### 2. Includes and components

- **What:** Live includes: the credit pair (section 1), the head interwiki-style frame (section 3), and the exhibit component includes, repointed to their JP forms (INCLUDE-REPOINT ×5). The escaped usage examples (candidate L48/L58, ESCAPED-INCLUDE ×3 across the docs) name `:scp-jp:theme:turbo-vision` — the *production* page, without `-jp` — and that is the correct K6 form, not a sweep miss: this candidate migrates an existing page, and the usage text speaks of the page readers apply. The batch's plain-form check was run with that distinction: every other theme's self-reference names its -jp candidate; this theme's names its production fullname, which exists.
- **Why:** P1 (KB-15), read through the K6 route of section 0.
- **Verify:** `grep -n '\[\[include' candidate.txt`; the usage examples are at candidate L48 and L58.
- **Disposition:** Applied; no foreign include kept.

### 3. Delivery and code loading

- **What:** The topology mirrors the original 1:1, which is the K6 expectation. The original delivers block 2 first (head module importing its own `/code/2`), frames it, then imports block 1 in a second module via the `theme:turbo-vision/code/1` form. The candidate does the same from the draft host under its own name: head module importing `local--code/theme%3Aturbo-vision-jp/2` (candidate L6), head frame naming the same /2 (candidate L11), second module importing `/1` (candidate L17). Census check: exactly two `[[code]]` blocks — #1 at candidate L658 (the theme-mode CSS) and #2 at candidate L1054 — so both addresses name the blocks that hold the CSS, in the original's order. Against production, the only delivery difference is the host-and-name form (production serves `scp-jp.wdfiles.com` under the production name `theme%3Aturbo-vision/1|2`; the candidate serves the draft host under `theme%3Aturbo-vision-jp/1|2`) — three lines, the standard class (iii) draft form.
- **Why:** P6/T3 and the delivery classes; for K6 the deciding property is that nothing about the delivery *shape* changes at migration.
- **Verify:** `grep -n 'local--code\|interwiki-style' candidate.txt`; count the `[[code]]` blocks (two, at L658 and L1054).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** The font architecture is the production translation's own, and it is the package's most distinctive layer. The original's code block 1 imports the Mx437 IBM VGA pixel font CSS from its own local--files plus IBM Plex Mono from fonts.bunny.net (the rev 54 form — rev 54's only change was moving that import from Google Fonts to bunny). The candidate instead imports: IBM Plex Mono in its full weight/italic range from Google Fonts; the JFDot pixel font (`jfdot-mp12.css`) from scp-jp-storage (`local--files/file%3A9042763-13-vzwf/jfdot-mp12.css`), replacing Mx437; IBM Plex Sans JP; and Noto Sans JP. The stacks run through the translation's variable split — `--body-font: var(--lafont-body), var(--jafont-body), sans-serif`, with a `--font-turbo-block` defined in both the Latin and JP variable blocks — so JP text takes the JP faces without disturbing the Latin design. The JFDot font is credited in the body furniture (its file page `file:9042763-13-vzwf`, source jikasei.me, 著作権者 森下浩司， candidate L605–622 region). T2 recorded the JFDot stylesheet ORB-blocked at chromium-768: KB-47 dispositions it as candidate-inherent flakiness whose remedy is the posting-time re-hosting class. Asset ソース links in the docs are repointed to the draft host's own folder (ASSET-REHOST ×2 blocks, ~8 lines).
- **Why:** P2/KB-17 is satisfied by the candidate's Google Fonts form — which is also why the candidate does not follow rev 54's bunny move (per-theme record): following it would have *introduced* a disallowed host. P7 is the variable split. The JFDot delivery is the KB-47 item.
- **Verify:** The import lines at code block 1's head (candidate L658 region); `grep -n 'jfdot\|JFDot' candidate.txt`.
- **Disposition:** Loads applied (production lineage); the JFDot stylesheet is DISPOSITIONED (KB-47).

### 5. Header, sidebar, and site furniture

- **What:** The furniture corrections are the appended tail modules (section 10): masthead and top-bar bounds, navigation corrections, the native history list, narrow-pane rules — all production-lineage supplements the EN original does not have, each headed by its English comment. The header variables themselves are the translation's (the lafont/jafont split of section 4). Several `http://` link forms survive in the docs (candidate L169, L557, L563, L605, L620, and the jikasei.me source link at L621): these are carried production-translation forms (the classifier's HTTP-KEPT shape), and five of the loci are exactly where production has since moved to https or to a bare page form — the drift item of the per-theme record, recorded here so the furniture section does not pass over it.
- **Why:** P9 is not engaged (no header string was kept untranslated by a wave decision; the strings are the 2024 translation's). The http forms are a posting-hygiene question, dispositioned as the drift flag rather than as translation debt.
- **Verify:** The loci are listed in the per-theme record with both forms.
- **Disposition:** Standing; the drift is FLAGGED (per-theme record).

### 6. Text translation

- **What:** The translation is the 2024 production translation, complete: 32 TRANSLATION-ANCHORED blocks and the 91-block unanchored mass are its wording against the EN source. CSS-BODY ×29 is the same fact inside the code blocks — the translation's JP variable layer and stack wording, not wave edits (the waves that touched this file are listed in Provenance and are small). COMMENT-TEXT ×1 only, because the translation kept most CSS comments in English or dropped them with their rules.
- **Why:** P10 is satisfied by adoption rather than by wave work; the class summary's adjudication paragraph states the reading rule for this package's shares.
- **Verify:** The exhibit census of section 8; the wave list in Provenance bounds the campaign's own edits.
- **Disposition:** Standing (adoption, K6).

### 7. Links

- **What:** The credit source link (section 1) names the recorded host. The docs' asset-credit blockquotes carry one regression against production: their 著作者 values are de-linked plain names in the candidate where production has `[[*user]]` links — part of the drift item. The five http:// loci are listed in the per-theme record. No live link in the candidate targets a page that does not exist on its named host; the drift is about *form* (protocol and link shape), not about dead targets.
- **Why:** P11 under the dead-reference evidence standard: nothing here is a dead reference, so nothing is charged as one; form drift against the page being replaced is the accurate charge, and it is flagged as such.
- **Verify:** The per-theme record's locus list; each pair is one `grep -n` away in the two files named there.
- **Disposition:** FLAGGED (drift, per-theme record); otherwise standing.

### 8. Structure

- **What:** The localize.md closing rule holds. The two code blocks keep the original's order and roles; the gate and page furniture correspond; the appended tail modules sit after the inherited body (candidate L1672–1739), not interleaved. One three-way structural fact belongs here: `[[footnoteblock]]` — the EN original has none; the production page runs it *live* (production L643); the candidate *escapes* it (candidate L648, `@@[[footnoteblock]]@@`), the KB-59 exhibit form, ledger-dispositioned as a specimen shape. Whether footnotes still collect under the escaped form is a T2/T3 question the KB-59 disposition leaves as pending evidence; it is recorded here so the next reviewer does not rediscover the asymmetry from the diff alone. The three EXHIBIT-RESTRUCTURE primaries adjudicate against the census (turbo-block exhibits, tabview, image exhibits, code exhibits all present in the same order): they are repoints and the footnoteblock escape, not restructurings.
- **Why:** R3 forces the adjudication; the footnoteblock three-way state is exactly the kind of fact a two-file diff cannot show.
- **Verify:** `grep -n 'footnoteblock' candidate.txt` (escaped, L648) against the production file (live, L643) and the mirror (absent).
- **Disposition:** Standing; the footnoteblock form is DISPOSITIONED (KB-59, pending-evidence note recorded).

### 9. Formatting only

- **What:** No WS-ONLY block and no pure re-indent block in this pair. The file did pass through a trailing-whitespace normalization wave (3010ef7, Provenance), whose effect is wave-level, not block-level: it rides inside the translation-mass blocks and cannot be separated from them in this diff.
- **Why:** R7's ground for the block-level "none", with the wave-level fact disclosed so the absence is not misread.
- **Verify:** classification.json's label counts for this package (no WS-ONLY); the wave commit is in the file's git log.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The appended tail modules (candidate L1672–1739) are each headed by an English `/* */` comment of the form "SCP-JP Wikidot …" — eleven supplements in all (enumerated in this package's per-theme record): navigation correction, invisible masthead bound, desktop top-bar bound, narrow image-block correction, mobile top-bar bound, native history list, narrow navigation rows, heading correction, narrow panes, documentation blockquote wrap, and the credit module correction of section 1. One comment cites a recorded owner decision (the blockquote-wrap module cites owner OPTION C, 2026-10-29 — accepting divergence from verbatim upstream for this package). By contrast, the empty comment at candidate L14 (`[!-- --]`) is *not* an annotation: it stands in the original (original L14) and in production alike, carried verbatim.
- **Why:** R2, with the discrimination the class exists for: porter-added text is recorded, inherited text is not charged as porter text. The classifier's single ANNOTATION block is the tail-module group.
- **Verify:** Read candidate L1672–1739; the L14 comment is checkable against original L14.
- **Disposition:** Standing (production lineage; the OPTION C divergence is owner-recorded).

### 11. Dispositions and exceptions

- **What:** The ledger items: (1) T1's two pseudo-ref errors, class (ii) (the draft-host delivery lines). (2) The render row's four items: the sample's T2 run returned no machine verdict (webkit screenshot pixel-cap, deterministic — a coverage caveat under GOSIGN-TESTS (a)); the page's only error is the runtime-hotlink chain (KB-40, environment layer); the JFDot stylesheet ORB block at chromium-768 (KB-47, section 4); offset blocks by design. (3) T4 row 41: display-affecting findings 0. (4) The ledger §(c3) LOCALIZE-B line: P3 FIXED. **Flagged by this package:** the candidate-versus-production drift at five link loci plus the de-linked asset-credit authors (per-theme record). The flag does not disturb the verdict — the migration claim (the phase-17 delta) is unaffected — but a posting made from this candidate without the drift repair would visibly regress the production page's links, so the coordinator should land the five loci (and the author links) as a candidate fix or record the acceptance explicitly.
- **Why:** A disposition is a decision with grounds; drift against a *living* page is the one K6-specific failure mode, and it belongs in the open where the posting decision will see it.
- **Verify:** Each item names its deciding record above; the flag's evidence is the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); **the production drift is FLAGGED** (per-theme record).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 41): exit 1, 2 errors / 0 warn / 1 info; both errors pseudo-ref, class (ii); no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-D2): FINDINGS — the four items of section 11(2), including the deterministic no-verdict sample run. (c) T4/T5 (LOCALIZE-ROWS row 41): display-affecting findings 0; the P3 charge and its FIXED outcome are section 1. (d) This package's own checks: the delivery census (section 3), and the candidate-versus-production byte comparison behind the per-theme record (127 changed lines over the production file's 1,665 lines, run for this package). (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares; the stamp as built read PASS because the candidate had not changed since b816e10; the later FIX-MP12 landing (canonical commit f4488f2, Post-package repairs) changed the candidate, so the stamp now reads STALE, with the record verdict standing. Counts in this README are the generator's (difflib, autojunk off): +563/−274 in 173 change blocks / 32 diff sections; the GNU-diff count of the same pair is 670 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result; for K6 the deciding checks are the delta record and the three-way comparison, both named.
- **Verify:** Re-run the checker on `pages/theme:turbo-vision-jp.txt`; re-run the candidate/production comparison with `diff pages/theme:turbo-vision-jp.txt pages-existing/existing:theme-turbo-vision.txt`.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 41; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The K6 route and the phase-17 delta

The migration claim for this theme is deliberately small, and this package states it exactly: upstream rev 54 changed only the font delivery host (Google Fonts → fonts.bunny.net) with no design or CSS change; the JP candidate does not follow that change, both because its font architecture is its own (section 4) and because bunny is outside the allowed host set. The phase-17 record (`pages/phase17-diff-turbo-vision-jp.txt`) therefore contains exactly one migration change: the credit block's reference revision, 53→54. Everything else in this package's large diff is the pre-existing translation's distance from the EN source — context for a reviewer, not migration work awaiting judgment.

### Candidate versus current production: the drift (FLAGGED)

Byte comparison of the candidate against the production capture (`pages-existing/existing:theme-turbo-vision.txt`, 1,665 lines) gives 127 changed lines (~92% identical). Most are the intended migration deltas: delivery host-and-name (3 lines, section 3), the twelve-field credit block (section 1), the draft-host asset ソース links (~8 lines), the escaped footnoteblock (section 8), and the ten appended tail modules production does not have (section 10). The remainder is drift — loci where production moved *after* the candidate's lineage froze, all in link form:

| Locus (candidate) | Candidate form | Current production form |
|---|---|---|
| L169 | `[[[http://scp-jp.wikidot.com/scp-0110-j\|LIGMA]]]` | https:// form |
| L557 | `[[[http://scp-jp.wikidot.com/component:toggle-sidebar\|…]]]` | bare `[[[component:toggle-sidebar]]]` |
| L563 | same full-URL form | bare page form |
| L605 | `http://scp-jp-storage.wikidot.com/…` file link | https:// form |
| L620 | `http://scp-jp-storage.wikidot.com/…` file link | https:// form |

Plus, in the docs' asset-credit blockquotes, 著作者 values that production carries as `[[*user]]` links stand de-linked in the candidate, and three blockquote markers lost trailing spaces production keeps (immaterial). None of this makes the candidate wrong as a port — every drifted form still resolves — but posting it unchanged would revert five pieces of production link hygiene. Flagged for the coordinator's posting decision; this package leaves the candidate byte-identical.

### The appended tail modules

Eleven live CSS modules appended at candidate L1672–1739, absent from production, each with its English "SCP-JP Wikidot …" comment (section 10): (1) navigation correction (rightmost submenu anchors); (2) invisible masthead bound; (3) desktop top-bar bound; (4) narrow image-block correction; (5) mobile top-bar bound; (6) native history list (seven columns in its own scroller); (7) narrow navigation rows; (8) heading correction (wrapped pixel-font headings' line-height); (9) narrow panes (revision/file tables); (10) documentation blockquote wrap (owner OPTION C, 2026-10-29); (11) the credit module correction of section 1. They are Sigma-10-environment corrections of the closing rule's appended form: the JP environment's furniture differs from the 2024 page's assumptions, and the corrections arrive as separate modules so the inherited body stays byte-close to the production lineage.

## Appendix — residue blocks

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B44 | L139–140 | L150–151 | A turbo-block exhibit line, translated inside its markup (R1) |
| B56 | L184–185 | L195–196 | The exhibit label "**DESCRIPTION**" → "**説明**" (R1) |
| B70 | L232–233 | L242–243 | The exhibit label "BACKGROUND COLOR" → "背景色" (R1) |
| B72 | L268–269 | L278–279 | The exhibit label "BORDER COLOR" → "境界色" (R1) |
| B75 | L276–277 | L286–287 | The exhibit label "TEXT COLOR" → "文字色" (R1) |
| B91 | L333–334 | L343–344 | A turbo-block exhibit line, translated inside its markup (R1) |
| B118 | L449–450 | L459–460 | The exhibit label "EXAMPLES" → "例" (R1) |
| B139 | L595 | L676–698 | The production translation's JP font-variable layer added at code block 1's head; no single original line corresponds (R2 mass, section 4) |
| B146 | L966 | L1066–1103 | The same JP layer at code block 2's head (R2 mass, section 4) |

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:turbo-vision-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-MP12 item 5 — production drift, eight loci (landing `f4488f2d2948824238a2d06479f104f4aab0cf5d`, "pages: skipos delivered channel, the-other-side fonts and subtitle, M-pure-12 repairs", 2026-11-17; record `FIX-MP12.md`).** +8/−8. Eight named loci are corrected to the production predecessor (`pages-existing/existing:theme-turbo-vision.txt`), leaving the intended migration deltas (draft-host asset ソース lines, credit block, delivery) untouched: L169 `http://…/scp-0110-j` → `https://…`; L557 and L563 `[[[http://scp-jp.wikidot.com/component:toggle-sidebar|component:toggle-sidebar]]]` → `[[[component:toggle-sidebar]]]`; L605 and L620 storage `http://` → `https://`; L598/L607/L613 bare `**著作者:** X` → `[[*user X]]` for Croquembouche, Placeholder McD and JakdragonX. Checker 2/0/1 before and after, findings identical modulo line numbers; no new class (i). The AGENTS.md §6 NO-FOLLOW for Turbo Vision's bulk-only upstream revisions (53→54) is not disturbed — only these eight loci moved.

## Change set outside the two diffed files

The diff covers two files; this theme's record is three files larger. `pages/phase17-diff-turbo-vision-jp.txt` is the migration delta record the whole K6 claim rests on (per-theme record). `pages-existing/existing:theme-turbo-vision.txt` is the production capture the drift comparison was run against. And `pages/theme-decoration-sample-turbo-vision-jp.txt` is the decoration sample the render checks ran against, whose T2 run returned no machine verdict (section 11). The base relationship runs the other way as well: theme:turbo-vision-dark-jp's candidate (same batch) imports this candidate's two code blocks, so this file is part of that package's record by reference.

## License and attribution

- **Title:** Turbo Vision Theme
- **Author:** JakdragonX, Croquembouche
- **Source:** https://scp-wiki.wikidot.com/theme:turbo-vision — revision 54 (revision date 2026-04-12 05:37:45)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: oplax-counterpoint — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
