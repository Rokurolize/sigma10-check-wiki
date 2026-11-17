# Review package — theme:anon-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:anon-jp — origin EN, population #57 [GOSIGN2-LEDGER (b) row 57]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9fdb2295aaffbad6e4e6aa0693682ffcdeb86e6332d1c14b4d4e4f767e47d26a); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 57; GOSIGN2-LEDGER (b) row 57]
- T2/T3 (render, combined verdict): PASS-WITH-NOTES — [combined T2/T3] report `NO candidate-specific blocking defect` — machine lines cross-cutting/draft-form/by-design; only a small 320 sample min-width overrun (330/335px) to note; 503/http.cat is transient. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 57, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 57]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 57]
- Computed against: canonical commit 662baf3a32f2f833d49604ec1be60b33ed834d65; candidate file pages/theme:anon-jp.txt sha256:9fdb2295aaffbad6e4e6aa0693682ffcdeb86e6332d1c14b4d4e4f767e47d26a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 57) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 and pseudo-ref ×1 (original-state and draft-host lines, section 11); P5 asset hosting (section 11). **REPAIRED since** — the original's three image license entries, flagged by this package at build, have been restored as a JP license box after the credit block (canonical commit 662baf3; per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:anon | theme:anon-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 91 (first translation; the candidate's credit block records 初訳時参照リビジョン: 91) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-anon.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:anon-jp.txt`, copied at worktree HEAD 5c04bbe; the file's last content change is commit 662baf3 (the license-box repair) |
| Lines / bytes | 568 lines / 12,941 bytes | 441 lines / 10,629 bytes |
| SHA-256 | dc63368bada2f1ed0bdb0c90c46f6197143ea3f42f7ecd6d4ff8006953d22f77 | 9fdb2295aaffbad6e4e6aa0693682ffcdeb86e6332d1c14b4d4e4f767e47d26a |

Wave history: the candidate was created by the Stage 2 EN batch 1 integration (commit 3205f27); the rework2-p2 commit c65ec92 swapped its embedded base for the JP base reference (section 3); FIX-CREDIT-D (1869877, translator attribution normalization over 163 files) was the last commit at the verdict; the post-verdict license-box repair (662baf3) is now the last content change and the stamp's computed-against commit. The original has been superseded upstream since revision 91; the follow-up diff artifact `diff-anon-from91.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

A Creepypasta colour variant for Parawatch: the original delivers two code layers by head imports (the Creepypasta base and its own CSS, the latter carried as a "Source Code" exhibit at the tail), frames them with an EN interwiki-style include at priority 2, and fills its gated body with credit furniture, three image license entries, and a full demonstration body. The candidate restructures the delivery (its own CSS moves from the tail exhibit into the CSS module; the base becomes the JP Creepypasta port), rebuilds the head as the JP frame at priority 1 plus the eight-field credit block and three compressed JP prose lines (the later repair adds the JP license box after the credit block), and drops the demonstration body — except the optional pastel-yellow exhibit, which survives relocated into the CSS module's tail. Measured churn (diff.md, Tier 2 format: +62/−189, 251 changed lines in 14 change blocks / 2 diff sections) is dominated by that one body deletion (block B9, −133 lines). One item was flagged in the per-theme record: the original's image license entries (The Great Hippo, CC BY-SA 3.0) were not carried, although two of the assets they covered remain live in the candidate's CSS; the repair has since restored the entries as a JP license box (per-theme record).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 14 change blocks — 11 specific (78.6%), 3 heuristic (21.4%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 5 |
| WS-ONLY | 4 |
| DELIVERY-MOVE | 3 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| INFO-DEL | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| RESTORATION | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 3 heuristic blocks are the compressed head lines (B4, B6, section 6) and the demonstration-body deletion (B9, section 8); the 2 EXHIBIT-RESTRUCTURE primaries split — B1 is the head delivery swap (section 3), B9 is the genuine body deletion (section 8); the RESTORATION block (B14) is the pastel exhibit's relocation, adjudicated in section 8; the 4 WS-ONLY blocks are blank lines that gained a single space in the CSS (section 9). After adjudication no block is left unexplained. The classification and the block numbers describe the pair as built at the verdict; the license-box repair (per-theme record) postdates them, and diff.md is regenerated against the repaired candidate.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:anon-jp; original theme:anon on scp-wiki at reference revision 91; candidate `pages/theme:anon-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch 1 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself changed value: the original already carried an interwiki-style frame (original L6–9, `:scp-wiki:` form, `priority=2`, theme= its own /1 on scp-wiki.wdfiles.com); the candidate's frame is the JP form at `priority=1` (candidate L1–4; section 3).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for anon-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture fills its gated head (original L11–52): a bare `[[module Rate]]` with its rating label, an `:scp-wiki:info:start`/`end` pair wrapping a ListPages credit module, a thank-you line, and three image license entries (gradient-anon.png, parawatch-anon.png, rook-anon.png — all by [[*user The Great Hippo]], CC BY-SA 3.0, edited by [[*user Lt Flops]]). The candidate deletes the Rate and the info pair (blocks B2–B3) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L8–17) carrying all eight ruling-3 fields (title パラウォッチ・アノン・テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Parawatch Anon Theme; 著作権者 Lt Flops; 作成年 2021; 初訳時参照リビジョン 91; the source link, section 7). As built, the three image license entries had no counterpart in the candidate — there was no license box on either side, and the entries lived inside the deleted info block — although two of the covered assets remain in use (section 4). That gap was flagged in the per-theme record and has since been repaired: the entries now stand as a JP license box immediately after the credit block (candidate L19–40), in the crayon form the flag named (per-theme record).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09), and the info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields. T4/KB-63 is the license-entry side: the original had no license-box include, so there was no box to swap — but the entries themselves were attribution content, which is why their absence was a flag and not a silent pass; the repair took exactly the T4 form the flag prescribed.
- **Verify:** `grep -n 'info:start\|info:end\|module Rate\|license-box' candidate.txt` returns the license-box pair only (candidate L19, L39); read candidate L8–17 against the eight fields and candidate L19–40 against original L26–43 (the entries). As built, the same grep returned nothing.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified) for the eight fields; the image license entries were FLAGGED (per-theme record) and have since been REPAIRED (canonical commit 662baf3).

### 2. Includes and components

- **What:** The candidate's includes are the frame (section 3) and the credit pair (section 1); its usage line is exhibit text in bare local form (`@@[[include theme:anon-jp]]@@`, candidate L21). The base swap is the section's component event: the original's head module imported the EN Creepypasta base (`local--code/theme%3Acreepypasta/1`, original L2); the candidate's module imports the JP port of that base, `local--code/theme%3Acreepypasta-jp/1` (candidate L27, block B8) — a T8 component swap to the JP port, executed by the rework2-p2 base-reference swap (commit c65ec92, which names creepypasta among its receivers). Every include in the candidate names a `:scp-jp:` target.
- **Why:** P1 (KB-15) for include targets; T8 for the base: a variant theme must layer the JP port of its base, not the EN original, or the JP page would inherit the foreign base's unlocalized form. Ruling 4 is not engaged: the base's JP port already existed as a campaign candidate.
- **Verify:** `grep -n '\[\[include\|@import' candidate.txt` — the frame, the credit pair, and the creepypasta-jp import.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery topology moved (classifier topology: one DELIVERY-MOVE, content similarity 0.994). In the original, the theme's own CSS sits in a `[[code]]` exhibit inside a "Source Code" collapsible at the tail (original L195–565) and is delivered by the head module's second import (`local--code/theme%3Aanon/1`, original L3). In the candidate, that CSS is inline in the `[[module CSS]]` at the head (candidate L25–417), and the module's only import is the base's (section 2). **Frame paragraph (the M-frame addition):** the original's EN frame named its own delivery at `priority=2` on scp-wiki.wdfiles.com; the candidate's JP frame (candidate L1–4) names the candidate's own `local--code/theme%3Aanon-jp/1` on the draft host at `priority=1` — the theme's own layer takes priority 1 in the JP convention for this single-base variant, with the base arriving by the module @import rather than by a frame layer. The ledger records the outcome as P6 FIXED (frame waves; checker-verified).
- **Why:** P6/T3 (the interwiki-style frame and its priority stack, KB-07) and P4/T9 (own-code delivery served from JP hosts). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — L3 (frame) and L27 (base import), both draft-host; the topology section of classification.json records the move.
- **Disposition:** FIXED (P6, frame waves); the draft-host lines are DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** No font load changes: neither side loads a font (the theme is a colour variant; its stacks come from the Creepypasta base), and no JPFONT label fired. Assets: three URLs, all kept on their original hosts. The candidate's CSS loads gradient-anon.png from the original's own folder (candidate L119) and parawatchPRIDE.png from the mkwhiteout-cia-pride folder (candidate L132), both on scp-wiki.wdfiles.com; the relocated pastel exhibit names parawatch.png from the creepypasta folder (candidate L432). These are the T1 baseline's three hotlink errors and the T4 lane's P5 finding (EN local--files direct links, LOCALIZE-ROWS row 57 item 2). The first two assets are the ones whose license entries section 1 flags; the restored license box (candidate L19–40) now credits both, its gradient entry's source link being the very URL this CSS loads and its parawatch entry naming the loaded PRIDE file (per-theme record).
- **Why:** P5 with KB-17 (asset hosts) and KB-58 (the owner-deferred hosting state): the campaign does not re-upload assets, and original-state hosts are rewritten at posting — the ledger's per-theme outcome is DISPOSITIONED (class (ii) / KB-58), so the lines stand as they are and are recorded, not silently passed.
- **Verify:** `grep -n 'wdfiles' candidate.txt` — the frame and import lines (draft host) plus the three asset lines above.
- **Disposition:** DISPOSITIONED (class (ii) / KB-58; GOSIGN2-LEDGER §(c3) P5).

### 5. Header, sidebar, and site furniture

- **What:** None as a separate change. The candidate overrides no header variable (no `--header-title`, `--header-subtitle`, or `--logo-image`); the theme's own `--fg*` colour variables are its CSS body, carried over in the delivery move (section 3) with their values unchanged. The sidebar filter rule from the pastel exhibit (`#side-bar div.menu-item img`) survives only inside the relocated exhibit text (section 8).
- **Why:** P9/T6 and P8 are per-theme judgments; a colour variant's furniture is its palette, and no JP furniture adaptation was needed.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 6. Text translation

- **What:** The candidate's prose is three compressed lines at the head: the theme description (candidate L41, block B4), the usage line (L43, block B5's counterpart content), and the base line (L45, block B6) — Parawatch Anon向けのCreepypastaベーステーマです / **使い方:** @@[[include theme:anon-jp]]@@ / **基盤:** Creepypasta（theme:creepypasta-jp を @import で読み込み）. They replace, in compressed form, the original's gated-head prose — the info-block entries and the "What Is This?" and "How to Use" blockquote sections (original L24–63). The CSS comment header (`/* Parawatch "Anon" Theme … Created by Lt Flops … */`, candidate L51–55) is the original's own comment, carried with the moved CSS (porter-visible text, R1 comment form). English survives in the credit block's original-title field (a proper name) and in that comment. There are no reader-visible `content:` strings in this theme's CSS.
- **Why:** P10 for the usage prose; KB-18 for reader-visible strings; the R1 line separates the porter-visible comment from reader-visible text.
- **Verify:** Read candidate L19–23 against original L24–63; a Hangul/CJK scan of the candidate's CSS returns only the comment header's Latin text.
- **Disposition:** Standing; the dropped English prose is adjudicated in section 8, not hidden here.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L16): `https://scp-wiki.wikidot.com/theme:anon`. That is the original's recorded host — review/sources.tsv records the original at scp-wiki.wikidot.com, the same host the mirror was taken from — so the link names the serving original and no host defect arises. The original's body links ([[parawatch-hub]], user links) sat in the dropped demonstration prose (section 8); the candidate's compressed head carries no prose links.
- **Why:** P11, under the dead-reference evidence standard; here the recorded host and the link agree, which is the check the jiha package's finding taught this batch to run on every theme.
- **Verify:** Compare candidate L16's host against the sources.tsv row's original_url host (scp-wiki.wikidot.com) — identical.
- **Disposition:** Standing; no defect flag.

### 8. Structure

- **What:** The CSS core is preserved: variable names, selectors, and order correspond (the delivery move of section 3, similarity 0.994), and the JP additions sit at the head, not interleaved — the localize.md closing rule holds for the code. The body does not follow it, and the two EXHIBIT-RESTRUCTURE primaries adjudicate as follows. B1 is the head delivery swap (section 3), not an exhibit change. B9 (original L64–196, −133 lines) is a genuine demonstration-body deletion: the "What is this theme used for?" prose, the Example Formatting exhibits (image-block, headings, formatting specimens, table, toc, code exhibit, link specimens, collapsible, lists, a five-tab tabview), and the Source Code collapsible's head were dropped as rendered body. Replaced vs dropped, precisely: the usage syntax is *replaced* by the compressed head line (section 6); the pastel-yellow optional exhibit is *relocated*, surviving as @@-escaped text at the tail of the candidate's CSS module (candidate L420–438, block B14, RESTORATION) — preserved as text, inert inside a CSS module, no longer a rendered exhibit; the remaining demonstrations are *dropped* without a translated counterpart. The ground, stated plainly: the JP theme-page form carries the credit, the compressed usage head, and the CSS; demonstrations live on the decoration sample (`pages/theme-decoration-sample-anon-jp.txt`), which is where the render checks exercised this theme's formatting. No ledger record charges the drop as a class I item, and the theme's T4 findings (section 12) do not name it; it is recorded here because R3 requires the ground to be stated.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** An exhibit census — `grep -n '\[\[tab\|\[\[code\|\[\[collapsible\|image-block' original.txt candidate.txt` — shows the original's exhibits with no candidate counterparts outside the head lines and the module tail.
- **Disposition:** Standing as documented; no class I item was charged by any record.

### 9. Formatting only

- **What:** Four blocks (B10–B13, WS-ONLY): single blank lines inside the CSS that gained one trailing space in the candidate (candidate L379, L383, L388, L392). No re-indentation (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered beyond these four disclosed lines.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** Section 2 of diff.md (the four one-line hunks).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added. The candidate carries no `[!-- --]` translator notes and no editor line; its CSS comments are the original's own (the theme header comment and its section comments), carried with the moved CSS (section 6).
- **Why:** R2: porter-added text is part of the change record; here the check was run explicitly and the answer is none.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; the `/*` lines in candidate.txt all have original counterparts.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three hotlink errors and one pseudo-ref error: the hotlinks are the original-state asset URLs of section 4 — DISPOSITIONED in register c1 (hotlink, class (ii)) and per-theme as P5 (class (ii) / KB-58); the pseudo-ref is the draft-host base import (candidate L49) — class (iii) draft form, DISPOSITIONED in c1. (2) The T2/T3 row's notes: a small 320px sample min-width overrun (330/335px) and the transient 503/http.cat capture (KB-44 family) — cross-cutting or capture-layer, recorded as not-charged; the row's verdict is no candidate-specific blocking defect. (3) The image license entries: the ledger's §(c3) line records P3 FIXED for this theme, and the eight credit fields are indeed complete in the bytes; the three image entries are a different object and were absent — FLAGGED in the per-theme record at build and since REPAIRED (canonical commit 662baf3): they now stand as a JP license box after the credit block (candidate L19–40). The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (item 1); item 2 not-charged; item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 57): exit 1, 4 errors / 2 warns / 1 info (hotlink×3, pseudo-ref×1); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A (EN3)): PASS-WITH-NOTES on both pages — no candidate-specific blocking defect; only the small 320 sample overrun to note; the 503/http.cat lines are transient. (c) T4/T5 (LOCALIZE-ROWS row 57): FINDINGS jointly, display-affecting findings 3 — the missing image attributions and the uncredited parawatchPRIDE.png (item 1; flagged at build and since repaired — the per-theme record carries the closing record), the EN local--files direct links (item 2; dispositioned, section 11), and the frame pattern (item 3; since FIXED, section 3). The ledger §(c3) line records the outcomes: P3 credit fields FIXED, P5 DISPOSITIONED, P6 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +62/−189 in 14 change blocks / 2 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:anon-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 57; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The image license entries that the credit fix did not carry

LOCALIZE-ROWS row 57 records the T4 lane's first finding: the image attributions inside the original's info:start (The Great Hippo, CC BY-SA 3.0, three files at original L26–43) were missing from the candidate, and parawatchPRIDE.png (candidate L105 at measurement) was uncredited. The bytes at the FIX5 head bore out the finding's state at the verdict. The candidate's credit block was complete in its eight fields, and the ledger (§(c3)) records P3 FIXED for this theme — but the three entries themselves appeared nowhere in the candidate: `grep -n 'Great Hippo' candidate.txt` returned nothing, and there was no license box. Two of the covered assets remain live in the candidate's CSS: gradient-anon.png (candidate L119, one of the three entry files) and parawatchPRIDE.png (candidate L132, the finding's separately named file). The other two entry files (parawatch-anon.png, rook-anon.png) are not referenced by the candidate's CSS — rook-anon.png appeared only in the dropped image-block exhibit — so the live gap is the gradient image's attribution and the PRIDE image's credit. The flag was recorded so the ledger's P3 FIXED line is not read as covering more than the eight fields it in fact covers. The repair has since been made, in exactly the form this item prescribed: canonical commit 662baf3 (full record FIX-ADMO-ANON.md, campaign record R/review-scout/, item 4) restores the three entries as a JP license box immediately after the credit block (candidate L19–40), in theme:crayon-jp's form (`[[include :scp-jp:component:license-box-backend |author=The Great Hippo]]`, one blockquote entry per file with Japanese labels, `[[include :scp-jp:component:license-box-end]]`), inside the candidate's `[[iftags +テーマ]]` gate. Two entry-level decisions are recorded in the box itself. The parawatch entry names parawatchPRIDE.png, the file the candidate's CSS actually loads (candidate L132, from the mkwhiteout-cia-pride file area — as the original's own CSS also did), with its real source link; its 備考 states plainly that the original's entry named parawatch-anon.png, and the 作者 credit to The Great Hippo rests on that original entry for the underlying logo. The rook-anon.png entry is restored with its original source link (which serves), and its 備考 discloses that the candidate does not load the file at all — it appeared only in the original's dropped image-block exhibit — so the entry documents the original's attribution set without claiming a use the candidate does not make. All three entries' source URLs serve 200 image/png. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B4 | 32-36 → 19-19 (body → body) | heuristic TRANS-UNANCHORED | Compressed replacement: the original's license-entry region aligns to the one-line theme description; the entries themselves are section 1's item (flagged at build, since restored in the head — per-theme record) |
| B6 | 47-52 → 23-23 (body → body) | heuristic TRANS-UNANCHORED | The base line, naming the JP base port; sections 2 and 6 |
| B9 | 64-196 → — (body → —) | heuristic EXHIBIT-RESTRUCTURE | Demonstration-body deletion, adjudicated replaced / relocated / dropped per exhibit; section 8 |

The tier-B blocks B7 (DELIVERY-MOVE, the CSS's move from tail exhibit to head module) and B14 (RESTORATION, the pastel exhibit's relocation) are adjudicated in sections 3 and 8 respectively.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-anon-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row, and it is where this theme's demonstration formatting lives after the section 8 drop); it belongs to this theme's record but carries no port change of its own to explain here. The base swap of section 2 names `pages/theme:creepypasta-jp.txt`, the JP port of the base theme, which is another candidate in the same population with its own record. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
