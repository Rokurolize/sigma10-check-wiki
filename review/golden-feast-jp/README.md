# Review package — theme:golden-feast-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:golden-feast-jp — origin EN, population #94 [GOSIGN2-LEDGER (b) row 94]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 94]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 84; GOSIGN2-LEDGER (b) row 94]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 328px@320 + sample 884px@768; chromium rate-pill label wrap-and-clip at ≤768; WebKit CC "S"; notice clip. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 94, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 94]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 94]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:golden-feast-jp.txt sha256:b9a9eb4e44af1cbaaea86b7e185488fd3e1cd9309539a3b1c0e3ec4dbfe5b2c5; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 94) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 + pseudo-ref ×1 (classes (ii)/(iii), section 11); the render row's items (KB-40 / KB-36 / KB-34 and the preview-form rate-pill state, section 11); the T4 item P5 (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:golden-feast | theme:golden-feast-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-golden-feast.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:golden-feast-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 428 lines / 8,053 bytes | 434 lines / 8,768 bytes |
| SHA-256 | be0821146e8f83f5f27874b232e6db7a03d05fbc7e4b0daa843ae7c505fd0b64 | b9a9eb4e44af1cbaaea86b7e185488fd3e1cd9309539a3b1c0e3ec4dbfe5b2c5 |

Wave history: the candidate was created by the Stage 2 EN10 integration (commit c210f75, the LOCALIZE-S2-A wave's port) and touched once since, by 1869877 (FIX-CREDIT-D, translator-attribution normalization). No production JP counterpart exists, so the R4 adoption question does not arise.

## Summary

The smallest and cleanest package in this batch: a standalone restaurant theme with no base theme, delivered from its own code by a single import and a single frame. The port repoints that delivery to the candidate's own code on the draft host, replaces the original's labeled bare Rate ("**Rating:**" over a Rate module) with the JP preview credit block, adds the JP font supplement (a Noto Sans JP load and three stack insertions behind the theme's Poiret One display face, whose load moves from a third-party mirror to Google Fonts), percent-encodes the colons in its three EN-storage asset URLs, and translates the short specimen body. One recorded item stands by disposition: the three asset references that remain on EN storage (KB-58). Measured churn (diff.md, the generator's difflib count with autojunk off: +71/−70, 141 changed lines in 47 change blocks / 16 diff hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 47 change blocks — 43 specific (91.5%), 3 heuristic (6.4%), 1 residue (2.1%), 0 skipped. The specific share is the batch's highest; 26 of the specific blocks are WS-ONLY formatting (section 9). Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COLON-ENC | 2 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 2 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 3 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 4 |
| TRANS-UNANCHORED | 5 |
| WS-ONLY | 26 |

Adjudication for this README (every specific block was read against the bytes): the two EXHIBIT-RESTRUCTURE primaries (B2, B9) are include repoints, not restructures (section 8). The single residue block (B47) is a trailing whitespace line deleted at the file's end (section 9). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:golden-feast-jp; original theme:golden-feast on scp-wiki at reference revision 14; candidate `pages/theme:golden-feast-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard). The candidate's head keeps the original's shape exactly: the own-code import module (candidate L1–3), the interwiki frame at priority=1 (L4–7), then the localized gate `[[iftags +テーマ]]` (L9). There is no base-theme layer in this theme on either side.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for golden-feast-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a labeled bare Rate (`**Rating:**` over `[[>]]` / `[[module Rate]]` / `[[/>]]`, original L14–17) and nothing else — no info pair, no license box. The candidate deletes the labeled Rate (B5) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L11–20) carrying the eight ruling-3 fields (タイトル Golden Feast CSS Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Golden Feast CSS Theme; 著作権者 c_bonefish; 作成年 2021; 初訳時参照リビジョン 14; the source link to scp-wiki.wikidot.com/theme:golden-feast). The theme's name stands in English in both title fields, as a proper name; no record charges it. The prose credit sentence is translated in place after the block, its Ambrose Restaurant hub link kept (candidate L24). T7 credit-module CSS: 4 matching lines on each side — the theme's own credit rules are inherited from the original unchanged, and no supplement was needed. No license box is added: the original carried none.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; FIX-CREDIT-D (1869877) is the translator form arriving.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L11–20 against the eight fields.
- **Disposition:** Applied.

### 2. Includes and components

- **What:** Two include changes: the frame include repointed to `:scp-jp:component:interwiki-style` (candidate L4, B2) and the image exhibit's include repointed to `:scp-jp:component:image-block` (candidate L34, B9) while its `name=` asset stays on EN storage (section 4). The usage exhibit's escaped include names the candidate in the recorded convention form (candidate L28: `@@[[include :scp-jp:theme:golden-feast]]@@`, B7). The candidate's remaining includes are the credit pair (section 1). No live include in the candidate names a `:scp-wiki:` target.
- **Why:** P1 (KB-15) for the component repoints.
- **Verify:** `grep -n '\[\[include' candidate.txt` — four live includes plus the escaped usage line, as listed.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** This theme has one delivery layer, its own: the original imports its code from EN storage (`https://scp-wiki.wdfiles.com/local--code/theme%3Agolden-feast/1`, original L2) and names the same URL through its priority=1 frame (original L4–7). The candidate repoints both to its own code on the draft host: `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Agolden-feast-jp/1` (candidate L2, B1; frame parameter at candidate L6, B3), keeping the frame's priority and form. The delivered body is the candidate's own `[[code]]` block (the /1 index), as in the original. There is no base import and no frame stack beyond this one frame, on either side.
- **Why:** P6/T3: the own layer must name the candidate's own code, and on the draft wiki that is the draft-host form (KB-41, class (iii)).
- **Verify:** `grep -n 'local--code' candidate.txt` — the two lines above, both draft-host.
- **Disposition:** DISPOSITIONED (class (iii) draft-wiki form).

### 4. Fonts and assets

- **What:** Fonts (P7), at the head of the delivered CSS: the candidate adds the JP supplement load (Google Fonts Noto Sans JP, weights 400;700, candidate L60, B14); repoints the display face's load — Poiret One was loaded from the third-party mirror fonts.bunny.net (original L69), the candidate loads it from fonts.googleapis.com (candidate L76, B15); and inserts the JP face into all three Poiret One stacks (`font-family: 'Poiret One', "Noto Sans JP", cursive`, candidate L100, L228, L238, B17/B25/B26 — the classifier's JPFONT-STACK signature fires as a specific match on all three). Assets: three references stay on EN storage (scp-wiki.wikidot.com/local--files): the top image named by the image-block exhibit (candidate L34) and by the CSS (candidate L148), and the background image (candidate L86). All three URLs are colon-encoded in the candidate (`theme%3Agolden-feast`, B9/B16/B20). These are the T1 row's three hotlink errors and the T4 row's pattern-5 item.
- **Why:** P7/T5 for the supplement and stack entries; the load repoint is KB-17's shape (a font load moved to its canonical host, family unchanged). P5/KB-58 for the assets: EN-storage hosting is the deferred state — re-upload is barred by owner order, and posting is where the hosting question is settled.
- **Verify:** `grep -n '@import' candidate.txt` — the delivery import of section 3 plus the two font loads above. `grep -cn 'scp-wiki.wikidot.com/local--files' candidate.txt` — 3.
- **Disposition:** DISPOSITIONED (assets, class (ii) / KB-58; section 11); the font changes are applied.

### 5. Header, sidebar, and site furniture

- **What:** This theme sets no `--header-title`/`--header-subtitle`/`--logo-image` variables on either side (grep returns 0/0); its header is the site furniture's. The theme's own masthead is its title heading (`+ Golden Feast CSS Theme`, candidate L22), kept in English as the theme's proper name and matching its credit-block title fields; no record charges it, and the T4 row for this theme carries no P9 item. Sidebar and topbar rules are inherited unmodified.
- **Why:** P9/T6 is the furniture class; the absence of header variables is recorded so a reviewer does not have to diff-hunt for a header change that never happened.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The short specimen body is translated in full: the credit prose (candidate L24), the import instruction (L26), the section headings (ページ要素 L32; CSSテーマのコード L57), the heading specimens （見出し1 and its siblings, L36–41), and the remaining specimen labels. The 5 TRANS-UNANCHORED and 4 TRANSLATION-ANCHORED blocks are this mass. English survives as live text only in proper names (the theme's name, c_bonefish, Poiret One).
- **Why:** P10 and KB-18: reader-visible strings are translated.
- **Verify:** diff.md's prose sections in order; `grep -n 'Page Elements\|To import this theme' candidate.txt` returns nothing.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The candidate's live outbound links are the credit block's source link (candidate L19) and the credit prose's Ambrose Restaurant hub link (candidate L24, kept from the original with a Japanese label). The source link names scp-wiki.wikidot.com/theme:golden-feast, the original's recorded host in sources.tsv — the serving form, not a defect. The asset URLs are CSS and exhibit references, not prose links (section 4).
- **Why:** P11 under the dead-reference evidence standard: a link is charged when its target does not serve or a JP counterpart exists; neither holds here (the hub link is the theme's subject reference, kept as the original had it).
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the two prose links above; the remaining hits are the asset lines of section 4.
- **Disposition:** Standing.

### 8. Structure

- **What:** No structural change. The classifier's two EXHIBIT-RESTRUCTURE primaries do not survive contact with the bytes: B2 is the frame's include repoint and B9 is the image-block include repoint — two repoints the signature matched because they sit in exhibit-adjacent lines, with no exhibit added, removed, or reordered. The exhibit census (image block, heading specimens, source code) stands in the original's order on both sides. The R3 question (a silent structural deletion) does not arise.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a repoint share a diff shape; here the census, not the label, decides.
- **Verify:** Compare the exhibit sequence via `grep -n 'image-block\|見出し\|code' original.txt candidate.txt` and the two blocks in diff.md.
- **Disposition:** Standing; no class I item.

### 9. Formatting only

- **What:** 26 WS-ONLY blocks, each the deletion of a whitespace-only line inside the CSS body, and one residue block (B47): a trailing whitespace line deleted at the file's end (original L425). No re-indentation and no line-ending conversion (0 and 0), so the R7 follow-up-diff hazard is not triggered beyond this disclosure.
- **Why:** Formatting churn is disclosed as its own class (R7) so it is never mistaken for a semantic change.
- **Verify:** The WS-ONLY blocks are diff.md's whitespace-only entries; their count is classification.json's label count for WS-ONLY (26).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. This candidate carries no `Ported for SCP-JP` banner, no `[JP]` markers, and no translator-note comments; its provenance record is the credit block and this package.
- **Why:** R2: the absence is recorded so a reviewer does not have to wonder whether annotations were overlooked.
- **Verify:** `grep -n 'Ported for\|\[JP\]\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items. (1) T1's three hotlink errors: class (ii) — the EN-storage asset lines of section 4, posting-time hosting state (KB-58); the ledger's §(c1) hotlink line dispositions the class. (2) T1's one pseudo-ref error: class (iii), draft-wiki form — the candidate's own draft-host delivery lines (section 3). (3) The render row's four items: the page's runtime-hotlink site-theme chain (KB-40, environment-layer, not charged), the sample's Chromium rate-pill label wrap-and-clip at ≤768px (the preview form's known state, the KB-32 family), the sample's notice clip (KB-34), and the WebKit-only CC-license "S" glyph-coverage artifact (KB-36, engine font coverage, not a theme defect). The T4 P5 item is item (1)'s class, dispositioned per the ledger's §(c3) line.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 84): exit 1, 4 errors / 1 warn / 1 info (hotlink×3, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN10)): FINDINGS, the four items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 94): FINDINGS jointly, display-affecting count 1 (the EN-storage assets); the ledger's §(c3) line dispositions P5 for this theme. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +71/−70 in 47 change blocks / 16 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:golden-feast-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 94; go-sign, COMPLETION-REPORT §10).

## Appendix — heuristic and residue mass, resolved by shape

Class M treatment: the 3 heuristic blocks are not listed one by one; they fall into the shapes below, each verified against the bytes at the cited ranges. The 1 residue block is listed in full. The 26 WS-ONLY blocks are treated in section 9.

| Shape | Blocks | Where | Resolution |
|---|---|---|---|
| Prose translation (unanchored) | B5's prose portion and the TRANS-UNANCHORED blocks | candidate L24–57 | P10 translation (section 6) |
| Residue: trailing whitespace line deleted | B47 | original L425 | Formatting (section 9) |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-golden-feast-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no base-theme dependency, and no inbound-link repairs in other candidates for this theme.
