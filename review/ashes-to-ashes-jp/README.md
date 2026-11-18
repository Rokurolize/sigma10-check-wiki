# Review package — theme:ashes-to-ashes-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ashes-to-ashes-jp — origin EN, population #59 [GOSIGN2-LEDGER (b) row 59]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 4f6f68937d6f65101da4a757d9cf41545ca2567a766fe5792b5c6783eb575fbc); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 0 infos (hotlink×3); standing classes dispositioned in register c1 [T1-ROWS row 59; GOSIGN2-LEDGER (b) row 59]
- T2/T3 (render, combined verdict): PASS-WITH-NOTES — [combined T2/T3] report `NO candidate-specific defect beyond cross-cutting X2/X3/X5/X7` — only borderline license legibility (observation); no BLOCKED-ENV. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 5 [LOCALIZE-ROWS row 59, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 59]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 59]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:ashes-to-ashes-jp.txt sha256:4f6f68937d6f65101da4a757d9cf41545ca2567a766fe5792b5c6783eb575fbc; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 59) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 (original-state asset URLs, section 11); P4/P5 delivery and asset classes (section 11). **REPAIRED since** — the two items this package flagged at build (the header font named in `--header-font` loaded nowhere, and the absent BHL base delivery) were repaired by the delivery rebuild, which also restored the demonstration body and corrected the base declaration (canonical commit 2aee861; per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ashes-to-ashes | theme:ashes-to-ashes-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 8 (first translation; the candidate's credit block records 初訳時参照リビジョン: 8) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-A/orig-ashes-to-ashes.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ashes-to-ashes-jp.txt`, copied at worktree HEAD 5c04bbe; the file's last content change is commit 2aee861 (the delivery rebuild) |
| Lines / bytes | 211 lines / 5,694 bytes | 228 lines / 6,677 bytes |
| SHA-256 | 10ff775e828cfe51a3d46f3f114532cda64d2bf834d1a53ccf92080e69a62349 | 7ddb45d1401652f446d60077ef3222c8f4eb436c684cbf3edb4461d8e3f01870 |

Wave history: the candidate was created by the Stage 2 EN batch 1 integration (commit 3205f27), had exactly one later commit at the verdict, f931619 (FIX2-COLON, unencoded-colon URL fixes over 18 themes; the source of the three colon encodings in section 4), and has since been rebuilt (commit 2aee861, the delivery rebuild recorded in the per-theme record), which is now the stamp's computed-against commit. The original has been superseded upstream since revision 8; the follow-up diff artifact `diff-ashes-to-ashes-from8.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

A Black Highlighter override theme built for Yoshihide's Proposal (Public Domain Contest 2025): the original pairs a BHL base delivered by GitHub Pages @imports with a single override CSS module, and closes with a long English demonstration body (story quote, usage prose, syntax exhibits) behind a second tag gate. As built, the candidate kept the override module nearly intact — its only CSS edits were the font load, one font stack, and three colon encodings — and rebuilt everything around it by subtraction: the BHL import head was deleted, the frame and credit block were added at the head with three compressed JP prose lines, the two EN BHL furniture includes were removed, and the demonstration body and its bare Rate module were dropped. The post-verdict rebuild (commit 2aee861; FIX-ASHES.md in the campaign record, R/review-scout/) has since reversed the subtractions that were defects: the BHL base is delivered by the JP base candidate's include at the head with the frame at priority 3, the original's two bunny.net font loads are restored verbatim, the demonstration body is restored translated behind its own gate with its bare Rate kept, and the base declaration now states the delivered form. The override CSS itself is byte-preserved through the rebuild (removing the two restored import lines makes the module identical to the as-built module, line for line). Measured churn (diff.md, the generator's count: +59/−47 in 9 change blocks / 8 hunks) understates the structural change, because the override CSS (the bulk of the file) is carried over almost line for line. Two items were flagged in the per-theme record at build: the header font the candidate names was not loaded anywhere in it, and the candidate contained no delivery of the BHL base its prose declared. Both are repaired by the rebuild, and the per-theme record carries their closing records.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 9 change blocks — 7 specific (77.8%), 1 heuristic (11.1%), 1 residue (11.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| IFTAGS | 3 |
| COLON-ENC | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| BARE-RATE-DEL | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic CSS-BODY block is a P7 font-stack rewrite (section 4); the residue block is a single blank line (section 9); the two EXHIBIT-RESTRUCTURE primaries split — B2 is the head furniture swap (sections 1–2), and B9 is a genuine exhibit-body deletion, adjudicated in section 8 with its ground. After adjudication no block is left unexplained. The classification and the block numbers describe the pair as built at the verdict; the delivery rebuild (per-theme record) postdates them, and diff.md is regenerated against the rebuilt candidate.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ashes-to-ashes-jp; original theme:ashes-to-ashes on scp-wiki at reference revision 8; candidate `pages/theme:ashes-to-ashes-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN batch 1 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved to the head: the original opens with a tag-gated head module carrying the BHL @imports (original L1–6) and closes with a second tag gate around its demonstration body (original L143); as built, the candidate opened with the frame include (candidate L1–4) and a single gate around the whole page. The rebuild restores the original's two-gate shape in the campaign's form: the JP base include at candidate L1, the frame at L3–6, the first gate around the credit/prose/CSS zone (opening at L8), and a second gate around the restored demonstration body (candidate L160–228).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3), and the head module's deletion is P4 (section 3).
- **Verify:** The sources.tsv row for ashes-to-ashes-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original carries no credit block at all: no credit include, no license entries; its only credit-shaped furniture is the bare `[[module Rate]]` centred in the tail gate (original L145–147), which the candidate as built deleted with the tail body (block B9) — and which the rebuild restored with that body, in the population form (see the disposition). The candidate installs the JP form at the head: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L10–19) carrying all eight ruling-3 fields (title 灰から灰へテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Ashes To Ashes Theme; 著作権者 Yossipossi; 作成年 2025; 初訳時参照リビジョン 8; the source link, section 7). The fields were present from the file's creation commit; no credit wave needed to complete them. There is no license box on either side (the original had none, so the T4/KB-63 dropped-box shape does not arise).
- **Why:** P3/T1 as applied at build: the preview credit module is the rate-bearing JP form, so the bare Rate was deleted rather than duplicated (the KB-09 duplicate-Rate concern). That rationale is superseded for this file by the rebuild's evidence: of the 22 candidates carrying a `[[module Rate]]`, 20 carry it alongside the JP credit block (theme:classic-jp sets the pair side by side under the labels 評価モジュール / クレジットモジュール; theme:crayon-jp likewise), and the source checker's `double-rate` info allows the specimen case expressly — so the restored body's Rate stands in the population form, and the KB-09 drop rationale no longer holds (per-theme record). Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module Rate\|license-box' candidate.txt` returns the restored body's Rate (candidate L162) and no license box; read candidate L10–19 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified — for this file the form arrived at creation).

### 2. Includes and components

- **What:** The original's two EN furniture includes, `:scp-wiki:component:toggle-sidebar-bhl` and `:scp-wiki:component:centered-header-bhl` (original L8–9), are deleted (block B2, COMPONENT-SWAP label); nothing replaces them one-for-one, because the JP environment supplies its own header and sidebar furniture and the BHL component pair has no place in the JP candidate. The candidate's includes are the JP base include (candidate L1, added by the rebuild), the frame (section 3), and the credit pair (section 1); its usage exhibits name the candidate itself in bare local form (`@@[[include theme:ashes-to-ashes-jp]]@@` at candidate L23, and the restored body's exhibit at L182), and the restored body carries the image-block exhibit include (candidate L197, `component:image-block`). Every live include in the candidate names a `:scp-jp:` target or the local namespace.
- **Why:** P1 (KB-15) governs repoints; a deletion is the right outcome where the included furniture belongs to the foreign base's page furniture rather than to the theme — keeping either include would be a foreign-include error, class (i). Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the base include, the frame, the credit pair, and the body's image-block exhibit; no foreign include.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its base by a tag-gated head module (original L2–5): `@import`s of BHL normalize and black-highlighter from `nu-scptheme.github.io`. As built, the candidate deleted that module outright (block B1) and added the frame the original lacked: an interwiki-style include at the head (candidate L1–4) with `priority=1` and `theme=` naming the candidate's own `local--code/theme%3Aashes-to-ashes-jp/1` on the draft host — a frame with no base layer in it, while the candidate's prose declared **基盤:** BHL（インライン）. The rebuild (commit 2aee861) puts the delivery in the campaign's BHL form, point for point with theme:doap-bhl-jp: `[[include :scp-jp:theme:black-highlighter-theme]]` at the head (candidate L1, doap-bhl's exact head), and the interwiki-style frame at `priority=3` (candidate L3–6) naming the candidate's own `local--code/theme%3Aashes-to-ashes-jp/1`. The base declaration now states the delivered form (candidate L25: Black Highlighter をインクルードし、独自レイヤーはフレームの priority=3). One deliberate difference from doap-bhl is recorded in the fix report: doap-bhl carries a stub module importing its own local--code plus a `[[code]]` exhibit of its CSS, while this candidate already carried its full CSS in the gated module (the frame's local--code/1 target); that mechanism is preserved untouched, so the frame target and the code-block numbering do not change. **Frame paragraph (the M-frame addition):** the frame is now the campaign's two-layer form — the JP base candidate included at the head and the theme's own layer framed at priority 3 — where as built it was the single-layer own-code form at priority 1 with no base anywhere in the file. The ledger records the frame outcome as P6 FIXED (frame waves; checker-verified); the base-delivery gap this package flagged against that form is repaired by the rebuild (per-theme record).
- **Why:** P6/T3 for the frame; P4/T9 for delivery sources generally — the campaign's BHL form, visible in this batch's theme:doap-bhl-jp, delivers the base through the JP BHL theme include with the own layer at priority 3, which is the comparison the flag rested on and the form the rebuild adopts. The draft-host form of the theme= URL is KB-41, class (iii).
- **Verify:** `grep -n '\[\[include\|priority=' candidate.txt` — the base include at L1 and the frame at priority 3; compare theme:doap-bhl-jp's head in `pages/`.
- **Disposition:** FIXED (P6, frame waves) for the frame itself; the base-delivery gap was FLAGGED (per-theme record) and has since been REPAIRED by the rebuild (commit 2aee861).

### 4. Fonts and assets

- **What:** Font load (block B3, JPFONT-LOAD): as built, the original's two bunny.net @imports (`Protest Revolution`, `Fredericka the Great`, original L13–14) were deleted, and the candidate loaded one family from Google Fonts at the head of its CSS module: Noto Sans JP (400;700). The rebuild restored the original's two imports verbatim (extracted programmatically from the original, not retyped) immediately after the JP load (candidate L29–30, the Noto Sans JP import now at L28). Stack (block B4, the heuristic CSS-BODY block, adjudicated here as the standing lesson directs): the `--header-font` value gains the JP face in second position — `'Fredericka the Great', 'Noto Sans JP', Times New Roman` (candidate L73) — a P7 font-stack rewrite, not a body-CSS change; its values are untouched by the rebuild, so the first-named face is now actually loaded. `Protest Revolution` is restored with its pair: the original loaded it and referenced it in no stack, on either side, as before. Assets (blocks B5–B7, COLON-ENC): the three background images (fire.webp candidate L89, bamboo.webp L106, parchment.webp L120) keep the original's host and folder (`scp-wiki.wikidot.com/local--files/theme:ashes-to-ashes/`) with only the colon encoded (`theme:` → `theme%3A`), the KB-01 form, executed by FIX2-COLON (f931619). The restored body adds one more original-state asset, the image-block exhibit's overseer4.webp (candidate L197).
- **Why:** P7/T5 with KB-16 for the JP load and stack (Japanese header text needs a JP-capable face in the stack); KB-01 for the colon encoding (an unencoded colon in a local--files URL is the checker's unencoded-colon class); P5/KB-58 for the assets' hosting state, which the ledger dispositions rather than fixes (section 11).
- **Verify:** `grep -n '@import\|Fredericka' candidate.txt` — the three import lines (L28–30) and the stack line (L73), the first-named face among the loads; `grep -n 'local--files' candidate.txt` — the three encoded CSS URLs and the body's exhibit asset.
- **Disposition:** JP load and stack applied; the asset URLs are DISPOSITIONED (class (ii) / KB-58, original-state hosting); the Fredericka load gap was FLAGGED (per-theme record) and has since been REPAIRED by the rebuild's verbatim restore (commit 2aee861). The restored bunny.net imports are themselves class (ii) original-state CDN delivery, the ledger's P4 disposition family for this theme (section 11).

### 5. Header, sidebar, and site furniture

- **What:** One variable group is carried, none is overridden for JP: the candidate keeps the original's act-specific `:root` strings (`--head-prelude`, `--head-1`..`--head-3`, `--sub-*`, candidate L33–41) in English — they are the theme's own act titles for Yoshihide's Proposal, reader-visible through the BHL header machinery — and the `--header-font` stack of section 4 is the only header variable whose value changes. There is no `--header-title` or `--logo-image` override. The EN BHL furniture includes are section 2.
- **Why:** P9/T6 is a per-theme judgment; KB-57 (header language) is the standing disposition family for kept original-language header text — the act titles are the work's own proper titles, not UI prose awaiting translation.
- **Verify:** `grep -n -- '--head-\|--sub-\|--header-' candidate.txt original.txt` — the values correspond one to one apart from section 4's stack.
- **Disposition:** Standing; the kept English act titles are recorded here so they are not mistaken for untranslated prose (section 6).

### 6. Text translation

- **What:** The candidate's head prose is three compressed lines (candidate L21–25, inside block B2): the theme description (Black Highlighterを基盤にしたAshes to Ashesテーマです), the usage line, and the base line (its text corrected by the rebuild, section 3). They replace, in compressed form, the original's usage prose that sat in its tail body (section 8). As built, the original's story quote and contest note were not translated; they were dropped with that body. The rebuild restored the body translated (candidate L160–228): the story quote (L165–167), the contest note with its Public Domain Contest 2025 link kept as the original's (L178), the import prose and presets prose (L180–186), and the specimen texts, with the Lorem ipsum paragraph and the `@@ @@` spacers carried verbatim. The CSS carries no translated strings: the act titles of section 5 are kept in English, there are no `content:` strings, and the one CSS comment (`/* ACT-SPECIFIC CSS */`, `/* REGULAR STUFF */`) is carried untranslated as porter-visible text (R1 comment form, a known non-finding shape). R5 glyph-form conversion: none (the source is English).
- **Why:** P10 for the usage prose; the distinction between reader-visible strings (KB-18) and porter-visible comments is the R1 line — comments are documented here, not charged.
- **Verify:** Read candidate L21–25 against the original's tail prose (original L152–160), and candidate L160–228 against original L143–211; a CJK scan of the candidate's CSS returns only the font names of section 4.
- **Disposition:** Standing; the restored body is adjudicated in section 8, not hidden here.

### 7. Links

- **What:** The candidate's credit-block source link (candidate L18) is `https://scp-wiki.wikidot.com/theme:ashes-to-ashes`. That is the original's recorded host — review/sources.tsv records the original at scp-wiki.wikidot.com, the same host the mirror was taken from — so the link names the serving original and no host defect arises. The original's contest link (to the Public Domain Contest 2025 page) sat in the tail body; the restored body carries it again (candidate L178), kept as the original's, and the body's Lorem ipsum paragraph carries its own links verbatim (candidate L211), one of them the UUID link the checker records as a warning (section 11).
- **Why:** P11, under the dead-reference evidence standard; here the recorded host and the link agree, which is the check the jiha package's finding taught this batch to run on every theme.
- **Verify:** Compare candidate L18's host against the sources.tsv row's original_url host (scp-wiki.wikidot.com) — identical.
- **Disposition:** Standing; no defect flag.

### 8. Structure

- **What:** Two structural facts. First, the preserved core: the override CSS module keeps the original's variable names, selectors, and order (original L11–141 → candidate L27–156), with the JP edits arriving as the head delivery and credit block, not interleaved into the inherited CSS — the localize.md closing rule holds for the CSS, and the rebuild preserved the module byte-for-byte apart from the two restored import lines. Second, the body (block B9, EXHIBIT-RESTRUCTURE with BARE-RATE-DEL): as built, the original's entire tail body (original L143–209) — the centred bare Rate, the Yoshihide story quote, the contest note and usage prose, the image-block exhibit, the header/format specimens, the collapsible and footnoteblock exhibits — was dropped, and the candidate ended at its CSS module. The adjudication then ran: the usage prose *replaced* in compressed form at the head (section 6); the Rate *replaced* by the rate-bearing credit block (section 1); the demonstration exhibits and the story quote *dropped* without a translated counterpart, on the ground that the JP theme-page form carries the credit, the compressed usage head, and the CSS, with demonstrations living on the decoration sample. The rebuild (commit 2aee861), under the main chat's ruling that bodies are restored in their original gated positions, reversed the drop: the body stands again at candidate L160–228 (69 lines including both gate tags, matching the original's L143–211 line for line in structure), translated, behind a second `[[iftags +テーマ]]` gate in the tail position — the story quote and prose translated, the Lorem ipsum paragraph and `@@ @@` spacers verbatim, the include exhibit repointed to the candidate's own bare local form, the headers in doap-bhl's 見出しレベル form, the image-block exhibit's asset colon-encoded to the candidate's own form. The bare Rate is kept verbatim at the body's head (candidate L161–163), in the population form alongside the credit block; the KB-09 rationale that had sanctioned its deletion is superseded (section 1). What remains dropped is only the original's two EN furniture includes (section 2), which belong to the foreign base's page furniture, not to this body.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides — and the restore follows the campaign's population standard for theme bodies, ruled for this file by the main chat on the owner's behalf.
- **Verify:** An exhibit census — `grep -n '\[\[tab\|\[\[code\|\[\[collapsible\|\[\[include\|image-block' original.txt candidate.txt` — now shows the candidate's counterparts for the body's exhibits (the image-block include at candidate L197, the collapsible at L213–217, the footnoteblock at L226), where as built it showed none outside the head lines. The fix record's correspondence table (FIX-ASHES.md, section 3) maps every original element to its candidate lines.
- **Disposition:** The drop was documented with its ground at build; it has since been REPAIRED by the rebuild (commit 2aee861). No class I item was charged by any record.

### 9. Formatting only

- **What:** One block: B8, the classifier's residue — a single blank line added ahead of the candidate's `[[/module]]` (candidate L152). No whitespace-only block pair and no re-indentation anywhere else (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The last hunk of diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added. The candidate carries no `[!-- --]` translator notes and no editor line; its only CSS comments are the original's own section comments, carried untranslated (section 6).
- **Why:** R2: porter-added text is part of the change record; here the check was run explicitly and the answer is none.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; the `/*` lines in candidate.txt all have original counterparts.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three hotlink errors: the three original-state asset URLs of section 4 — DISPOSITIONED in register c1 (hotlink, class (ii): original-state asset hosts are rewritten at posting or kept as original state; re-upload is barred by owner order), and per-theme in §(c3) as P5 DISPOSITIONED (class (ii) / KB-58). (2) P4 delivery: §(c3) records P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery) — the original-state delivery lines that remain are the section 4 assets and, since the rebuild, the restored bunny.net font imports and the body's exhibit asset, all of the same class (ii) family; the BHL base itself is now delivered by the JP base candidate's include, not by an original-state line (section 3). (3) The T2/T3 row's only note is borderline license legibility (an observation, cross-cutting X2/X3/X5/X7 family), recorded as not-charged. The rebuild's checker run (FIX-ASHES.md, section 5) reports 6 errors / 1 warn / 1 info on the rebuilt file: the three baseline hotlinks unchanged in substance; hotlink ×2 on the restored bunny.net imports (class (ii), the P4 family above); hotlink ×1 on the body's image-block exhibit asset (class (ii) / KB-58); one warning, the UUID link inside the verbatim Lorem ipsum exhibit (recorded verbatim per AGENTS.md §2, not classified or fixed); and one info, `double-rate` for the restored body Rate, whose own text allows the specimen case. No class (i) error is introduced. The two FLAGGED items (the unloaded header font; the absent BHL base delivery) were argued in the per-theme record and are repaired by the rebuild; the ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 not-charged; the two flagged items have since been repaired (per-theme record).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 59): exit 1, 3 errors / 1 warn / 0 infos; all three errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A (EN3)): PASS-WITH-NOTES on both pages — no candidate-specific defect beyond the cross-cutting families; only borderline license legibility (observation); no BLOCKED-ENV. (c) T4/T5 (LOCALIZE-ROWS row 59): FINDINGS jointly, display-affecting findings 5 — the destroyed font @import with the header falling back (finding 1; flagged at build in the per-theme record and since repaired by the verbatim restore), the three EN local--files direct links (finding 2; dispositioned, section 11), the absent interwiki-style (finding 3; since FIXED, section 3), and the balance of the row's five. The ledger §(c3) line records the outcomes: P4 DISPOSITIONED, P5 DISPOSITIONED, P6 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +59/−47 in 9 change blocks / 8 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ashes-to-ashes-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 59; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The header font that is named but never loaded

LOCALIZE-ROWS row 59 records the T4 lane's first finding: the font `@import` was destroyed wholesale, `'Fredericka the Great'` did not load, and the header fell back to Times New Roman; the lane's stated remedy was a repoint to Google Fonts. The bytes at the FIX5 head show a half-repair. The candidate's only font load (candidate L26) is a Google Fonts import of Noto Sans JP; the two bunny.net loads (Fredericka the Great, Protest Revolution) are deleted; and the header stack (candidate L69) reads `'Fredericka the Great', 'Noto Sans JP', Times New Roman`. So the named first-choice face is still loaded nowhere in the candidate — `grep -n 'Fredericka' candidate.txt` returns exactly the stack line — and the header now falls back to Noto Sans JP instead of Times New Roman. No ledger outcome line for this theme names the font load (the §(c3) line covers P4, P5, P6), so the package carried the item as a flag. The repair has since been made, in a different form from the one this item proposed: the rebuild (canonical commit 2aee861; FIX-ASHES.md, section 2) restored the original's two bunny.net imports verbatim at candidate L29–30, immediately after the Noto Sans JP load, rather than repointing Fredericka to Google Fonts as the T4 lane had suggested — the ruling ordered the original's lines verbatim. The stack values are untouched, so the first-named header face is now actually loaded, and the flag is closed. Protest Revolution is restored with it, as the original had it: loaded, and referenced by no stack on either side. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

### The BHL base that the prose declares and the file does not deliver

The original delivered the Black Highlighter base by two @imports from nu-scptheme.github.io (original L3–4); the candidate as built deleted them and contained no BHL load of any form — no @import, no JP BHL theme include — while its own prose declared **基盤:** BHL（インライン） (candidate L23) and its frame names only its own code at priority 1 (section 3). The campaign's BHL form elsewhere (this batch's theme:doap-bhl-jp) delivers the base through `[[include :scp-jp:theme:black-highlighter-theme]]` with the theme's own layer framed at priority 3. Against that form, this candidate's base delivery was absent from the two files in this package. The counter-evidence is the render record: T2/T3 ran the composition and returned PASS-WITH-NOTES with no candidate-specific defect, so in the check environment the override layer rendered as a theme. The package records both sides and flags the gap for the coordinator: either the environment supplies the base (in which case the prose line is right and the delivery is environmental), or the candidate is missing its base layer (in which case the fix is the doap form). The two files in this package cannot decide between those, and the package does not pretend they can.

The coordinator's ruling decided it: the candidate was missing its base layer. The rebuild (canonical commit 2aee861; FIX-ASHES.md, section 1) delivers the base in the doap form — `[[include :scp-jp:theme:black-highlighter-theme]]` at candidate L1, the frame at priority 3 — and corrects the declaration to state the delivered form (candidate L25). A record stating the opposite of the delivered files is itself a documentation defect, which is why the declaration was corrected in the same change rather than left to a later pass. The flag is closed.

### The demonstration body, and the Rate that came back with it

The third repair in the rebuild is the body itself (FIX-ASHES.md, section 3). The original's second gate (original L143–211) is restored at candidate L160–228, translated, element for element: the centred bare Rate, the Hell Screen story quote, the contest note, the import prose with its include exhibit in the candidate's own bare local form, the presets prose, the image-block exhibit, the six header specimens, the Lorem ipsum paragraph verbatim, the collapsible, the blockquote specimens, and the footnoteblock. The Rate is the item this package's earlier sections reasoned about most carefully, and the rebuild supersedes that reasoning on evidence: sections 1 and 8 recorded its deletion under the KB-09 duplicate-Rate concern (the preview credit module is rate-bearing, so a kept Rate would duplicate it). The population says otherwise — of the 22 candidates carrying a `[[module Rate]]`, 20 carry it alongside the JP credit block, theme:classic-jp setting the pair side by side under the labels 評価モジュール / クレジットモジュール and theme:crayon-jp, this theme's batchmate, likewise — and the source checker's `double-rate` info names the specimen case as allowed in its own text. Under the ruling that an undispositioned drop defaults to the population standard, the Rate is restored verbatim at the body's head, and the KB-09 drop rationale recorded in sections 1 and 8 no longer holds for this file. Those sections now state both the as-built reasoning and its supersession, so the record shows why the file changed its mind.


### Post-package repairs (REFRESH3-D)

Recopy was a verified no-op: `candidate.txt` is byte-identical to the current canonical `pages/theme:ashes-to-ashes-jp.txt`. No repair lands after this package's candidate build, so the record below is the slice's sub-shape and remedy, confirmed present in the built bytes.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Aashes-to-ashes-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L3.
- This is the (B) remedy **atop the refresh-2 rewrite**: the rebuild (`2aee861`, FIX-ASHES.md) and its body/font restoration are recorded in the per-theme record; 722ceb5 then dropped the rebuilt frame's dead `theme=` parameter at L3–6. Both landings predate this package's refresh-2 build (`4b46183`) and are present in the copied bytes.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Appendix — residue blocks

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B4 | 58-58 → 69-69 (module-css → module-css) | heuristic CSS-BODY | P7 font-stack rewrite: `'Noto Sans JP'` inserted into the `--header-font` stack; section 4 |
| B8 | at 141 → at 152 (module-css → body) | residue, no signature | Single blank line added ahead of `[[/module]]`; section 9 |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-ashes-to-ashes-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row, and it is where this theme's demonstration formatting lives after the section 8 drop); it belongs to this theme's record but carries no port change of its own to explain here. The rebuild's base include names theme:black-highlighter-theme, a production JP page rather than a population candidate, so no companion candidate file enters this theme's record through it. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Ashes To Ashes Theme
- **Author:** Yossipossi
- **Source:** https://scp-wiki.wikidot.com/theme:ashes-to-ashes — revision 8
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
