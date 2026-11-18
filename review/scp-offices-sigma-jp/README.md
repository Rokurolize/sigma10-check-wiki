# Review package — theme:scp-offices-sigma-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:scp-offices-sigma-jp — origin EN, population #134 [GOSIGN2-LEDGER (b) row 134]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now f7cc9677144ca372ddfa5e447d0dc91027734fb4417e947484628fa0b808ef15); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 1 warn / 2 infos (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 129; GOSIGN2-LEDGER (b) row 134]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + sidebar-not-opening; sample T2 no machine verdict (exit 2). [RENDER-ROWS-2 (RENDER-S2-C (EN18))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN18))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 134, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 134]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 134]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:scp-offices-sigma-jp.txt sha256:f7cc9677144ca372ddfa5e447d0dc91027734fb4417e947484628fa0b808ef15; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 134) |
| Standing items | **One FIXED, one DISPOSITIONED class** — the credit fields were completed by a fix wave (P3 FIXED, section 1); the unprefixed-include items stand under the posting-procedure disposition (P1, sections 2–3); the T1 pseudo-ref is draft form (class (iii)); the render row's items are the environment and cross-cutting lines of section 11, and its sample side returned no verdict (exit 2). One item is flagged in the per-theme record: the usage exhibit's plain-slug self-reference |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:scp-offices-sigma | theme:scp-offices-sigma-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10 (first translation; the candidate's credit block records 初訳時参照リビジョン: 10) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-render-s2-3/mirrors/scp-offices-sigma.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:scp-offices-sigma-jp.txt`, copied at worktree HEAD 5506feb |
| Lines / bytes | 634 lines / 14,286 bytes | 637 lines / 15,984 bytes |
| SHA-256 | 83fe29fe1ffa81a8a9079572af70b20ea6665c1e97c3d3625a59a5ac778b006f | 64316420046f9fc2b40ad2ddca2e3187480bc5db6a69431eb2f654997ce86d93 |

Wave history: the candidate was created by the Stage 2 EN18 integration (commit 3c1bcdf, the RENDER-S2-3 wave's port) and has exactly one later commit, 666f543 (FIX2-CREDIT), which completed the credit block of section 1. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The SCP Offices theme's Sigma-9 skin — the base on which the Human Resources sigma theme (its sibling package in this batch) is built. The port converts the original's two bare rating exhibits (a Rate module, and a credit-module exhibit over an info trio) into the preview credit block, completing the fields the localize check found at two of eight (ledger P3 FIXED); adds the interwiki frame the original does not carry, in the unprefixed form the P1 disposition covers; migrates the single font load from bunny.net to Google Fonts and inserts Noto Sans JP into the four font variables every stack references (the P7 arrangement in variable form); makes the logo's three relative references absolute against the base theme's production page on the JP wiki; and translates the prose, exhibits, and CSS comments. The usage exhibit names the plain slug and is flagged in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 76 change blocks — 28 specific (36.8%), 44 heuristic (57.9%), 4 residue (5.3%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 45 |
| COMMENT-TEXT | 23 |
| TRANSLATION-ANCHORED | 18 |
| ASSET-REHOST | 3 |
| DRAFT-HOST | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| WS-ONLY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the single CSS-BODY block (B48) is the P7 font-variable rewrite of section 4 — the theme's stacks are `var()` references, so the stack insertions land in the variable definitions and the classifier's JPFONT-STACK signature does not fire; the standing rule for this batch is that font rewrite blocks are narrated as P7 whatever their label. The one EXHIBIT-RESTRUCTURE block (B11) is the image-block exhibit's re-host, not a restructuring. The four residue blocks are heading and comment translations (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:scp-offices-sigma-jp; original theme:scp-offices-sigma on scp-wiki at reference revision 10; candidate `pages/theme:scp-offices-sigma-jp.txt`. Provenance route: derived from the original at the reference revision by the RENDER-S2-3 wave (sources.tsv kind: standard). The original opens with the delivery module alone — it has no interwiki frame — and the candidate adds the frame ahead of the gate (section 3). The gate localizes as usual (block B3: `[[iftags +theme]]` → `[[iftags +テーマ]]`, candidate L10).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization).
- **Verify:** The sources.tsv row for scp-offices-sigma-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is P2, applied.

### 1. Credit and attribution

- **What:** The original's credit furniture is two bare exhibits: a right-aligned `[[module Rate]]` under a "Rating:" heading (original L6–9), and a "Rating w/ Credit Module:" heading over an unprefixed `:scp-wiki:info:start` / `more` / `end` trio with placeholder texts (original L11–19). The candidate deletes both exhibits (blocks B2, B4: BARE-RATE-DEL and INFO-DEL) and installs the preview credit block (candidate L12–21): the eight ruling-3 fields （タイトル SCP Offices Sigma-9 Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 SCP Offices Sigma-9 Theme; 著作権者 [[*user macro_au_micro]]; 作成年 2020; 初訳時参照リビジョン 10; the source link, host-verified in section 7). At localize time the block stood at two of eight fields (the LOCALIZE row's pattern-3 charge: six of eight missing, the panel rendering but incomplete — the same charge its sibling theme carries); the FIX2-CREDIT wave (commit 666f543) completed it, and the ledger records the outcome as P3 FIXED. The author field names macro_au_micro with the user link, the theme's author; the theme is a standalone work (it is itself the base its sibling extends), so no base-work credit arises. T7 credit CSS: no supplement was added; the credit-adjacent rules the original's credit-module exhibit uses are inherited on both sides (four matching lines each).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form; the two bare exhibits are the class C failure (duplicate furniture, KB-10) when left beside it, so the conversion replaces rather than accumulates. Ruling 3 fixes the eight fields the incomplete panel was missing.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L12–21 against the eight fields; `git log --oneline -- pages/theme:scp-offices-sigma-jp.txt` shows the FIX2-CREDIT commit.
- **Disposition:** FIXED (P3, credit waves; GOSIGN2-LEDGER §(c3)).

### 2. Includes and components

- **What:** Three include events besides the credit pair. The interwiki frame is added where the original has none, in unprefixed form (candidate L5: `[[include component:interwiki-style`, its theme target in section 3) — an unprefixed include resolves on the site that renders it, which on scp-jp is the JP component; this is the localize check's pattern-1/6 family (unprefixed same-site includes), dispositioned under P1 (section 11). The usage exhibit (block B7) repoints the include to `:scp-jp:` with the plain slug — flagged in the per-theme record. The examples exhibit keeps its unprefixed `[[include component:image-block ...]]` (candidate L39, block B11) with the caption translated; the component resolves on scp-jp, and the image it displays is section 4's re-host.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; the unprefixed form names the same component by the site's own resolution, and the ledger's P1 line dispositions the form for this theme rather than charging it. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — frame (L5), credit pair (L12, L21), image-block (L39), and the escaped exhibit (L28).
- **Disposition:** DISPOSITIONED for the unprefixed form (P1, posting-procedure convention class); the exhibit's name form is the flagged item of the per-theme record.

### 3. Delivery and code loading

- **What:** The delivery arrangement gains its frame. The original's delivery is external-form and frameless: its module imports its own /1 from the wiki domain itself, `https://scp-wiki.wikidot.com/local--code/theme:scp-offices-sigma/1` (original L2; the topology pass records `external_own_delivery: true`), and no interwiki-style include exists anywhere in the file. The candidate normalizes the import to the standard form, `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Ascp-offices-sigma-jp/1` (candidate L2, block B1), and adds the frame at priority 1 naming the same delivery (candidate L5–8). The CSS is the code exhibit on both sides (509 → 510 lines; the added line is inside the font-load block, section 4).
- **Why:** P4/T9 and P6/T3: in the JP environment a theme's live channel is its own local--code delivery framed by interwiki-style; the original's frameless module is the branch-local form the port completes. The draft host is KB-41, class (iii).
- **Verify:** `sed -n '1,8p' candidate.txt` against original L1–5 — the candidate has the frame the original lacks.
- **Disposition:** DISPOSITIONED (draft-host form, class (iii)); the frame addition is applied.

### 4. Fonts and assets

- **What:** Fonts (P7): the load migrates hosts and gains the JP face (block B47: original L134 → candidate L136–137). The original loads Basic and IBM Plex Mono from bunny.net in the retired `css?family=` grammar; the candidate loads IBM Plex Mono from Google Fonts css2 and adds `Noto Sans JP:wght@400;700`. The stack insertions land in the `:root` font variables (block B48, the classifier's CSS-BODY): `--body-font`, `--header-font`, `--title-font`, and `--mono-font` each gain `'Noto Sans JP'` behind IBM Plex Mono (candidate L140–143) — and because every font-family declaration in the theme references those variables, the four lines are the whole P7 event, which is why no JPFONT-STACK block fires. As in the sibling theme, `Basic` is named only in the original's import line and in no stack on either side, so its absence drops nothing that renders. Assets (ASSET-REHOST ×3, all applied): the logo's three references are relative in the original — the exhibit's image-block (original L37) and two CSS backgrounds (original L182, L207) all name `/local--files/theme:scp-offices-sigma/scpoffices_logo.svg`, which resolves against whatever wiki serves the page. The candidate makes all three absolute against the base theme's production page on the JP wiki: `https://scp-jp.wdfiles.com/local--files/theme%3Ascp-offices-theme/scpoffices_logo.svg` (candidate L39, L185, L210).
- **Why:** P7 (KB-16): Japanese text must not fall back to a platform default for want of a named JP family; here the family is named in every variable and loaded. P5: a relative file reference is the sharpest form of the original-state dependency — on scp-jp it would resolve against the JP wiki's own (nonexistent) theme:scp-offices-sigma file area — so the port anchors it to the file's actual JP home, the production base theme's page.
- **Verify:** `grep -n '@import' candidate.txt` — two Google Fonts lines at L136–137 plus the delivery import at L2; `grep -n 'scpoffices_logo' candidate.txt` — the three loci named above, all scp-jp.wdfiles.
- **Disposition:** Applied (fonts and re-hosting); no ledger item stands against either.

### 5. Header, sidebar, and site furniture

- **What:** No header variables and no CSS content strings exist on either side, and no P8 adaptation was needed. Sidebar behaviour is a render-record item: the row records a sidebar-not-opening observation on the theme page (section 11) — a line that recurs across its lane's rows, recorded and dispositioned with the row rather than traced to this candidate's CSS, none of which touches the sidebar mechanism beyond the inherited Sigma arrangement.
- **Why:** P8 has no object here; the sidebar line is recorded so a reader does not mistake its absence from this section for an oversight.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing.
- **Disposition:** Standing (the render line is DISPOSITIONED with its row, section 11).

### 6. Text translation

- **What:** The prose is translated throughout: the usage section including the @import warning and the backlinks instructions, the examples' explanatory text, and the headings. The CSS comments are translated as a class (23 COMMENT-TEXT blocks). The counted groups are 45 TRANS-UNANCHORED blocks and 18 TRANSLATION-ANCHORED blocks; the anchored blocks were verified line by line, and the unanchored mass is single-line prose and comment translation of the same shapes, with no content class dropped (the census in section 8). Two residue blocks are headings （使用方法, 使用例） and two are CSS section comments, resolved in the appendix.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings); CSS comments are porter-visible only (R1's comment half), counted as a class.
- **Verify:** The pairs are diff.md's body and code sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** One link item: the credit block's source link (candidate L20) names `https://scp-wiki.wikidot.com/theme:scp-offices-sigma` — the original's recorded host (review/sources.tsv `original_url`), so the host check passes and no probe was triggered; its label is ソース. The candidate carries no other prose links: the theme's documentation names no base work and no hub, in either file.
- **Why:** P11 has no further object here.
- **Verify:** `grep -n '元記事リンク' candidate.txt` — the single locus at L20.
- **Disposition:** Applied.

### 8. Structure

- **What:** The exhibit census corresponds: usage section, examples (image-block, headings, collapsibles), and the code exhibit are present on both sides in the same order. The named conversions are the two rating exhibits' replacement by the credit block (section 1) and the delivery frame's addition (section 3). Selector and variable names inside the CSS are preserved apart from the font variables of section 4.
- **Why:** R3: the census is what separates a conversion (this theme) from a silent restructure or drop (the failure class I charges); here every original region has a named candidate counterpart.
- **Verify:** Compare the heading and include sequences of the two files — they correspond at the loci named in sections 1–3.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** Two whitespace-only blocks (B72, B73), both single lines inside the code exhibit where the candidate's line differs from the original's only in whitespace. No re-indentation occurs (0 reindent blocks).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; inside a code exhibit it is also display-inert, since the exhibit's text is documentation.
- **Verify:** The classifier summary in classification.json (WS-ONLY ×2).
- **Disposition:** Standing.

### 10. Porter annotations

- **What:** None. An explicit check of the candidate finds no `[!-- ... --]` porter comment and no editor line with no original counterpart; the classifier's ANNOTATION signature does not fire.
- **Why:** R2: porter-added text is part of the change record; here there is none to record.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's one pseudo-ref error: class (iii), the draft-host delivery of section 3. There are no hotlink errors — the logo is re-anchored to the JP wiki (section 4) and the base delivery is the candidate's own. (2) The unprefixed-include family (the frame of section 2): the ledger's P1 line, DISPOSITIONED as the posting-procedure convention class. (3) The render row's items: on the page side, the runtime-hotlink site-theme chain (KB-40, the environment layer: the check site's own theme chain, not this candidate) and the sidebar-not-opening observation of section 5, which recurs across the lane's rows and is dispositioned with the row; on the sample side, the capture returned exit 2 — no machine verdict was produced for the sample, a coverage caveat of the capture layer (the KB-44 family), not a defect found in the candidate. T4's charges close as: pattern 3 FIXED (section 1), patterns 1/6 DISPOSITIONED (item (2)).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged, and an exit-2 capture is reported as the absence of a verdict, never as a pass.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items (1)–(3)); FIXED (the credit charge).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 129): exit 1, 1 error / 1 warn / 2 infos; the single error is the pseudo-ref of section 11(1), and there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN18)): FINDINGS on the page side (section 11(3)); the sample side returned exit 2, no machine verdict. (c) T4/T5 (LOCALIZE-ROWS row 134): FINDINGS jointly, display-affecting findings 1 (the pattern-3 credit charge, since fixed); the ledger §(c3) line records the theme's T4 outcome as P1 DISPOSITIONED and P3 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +140/−142 in 76 classifier change blocks / 16 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:scp-offices-sigma-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 134; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage exhibit's self-reference (flagged)

The usage exhibit reads `@@[[include :scp-jp:theme:scp-offices-sigma]]@@` (candidate L28) — the include a user is told to paste names the theme's plain slug on scp-jp, where the candidate's posting name is theme:scp-offices-sigma-jp. The original's exhibit names `:scp-wiki:theme:scp-offices-sigma` (original L26), that page's real name on its own wiki, so the port's repoint changed the site prefix and kept a name that, on the target wiki, will not be the posted page's name. Probes made for this package (2026-11-17): both `https://scp-jp.wikidot.com/theme:scp-offices-sigma` and `https://scp-jp.wikidot.com/theme:scp-offices-sigma-jp` return 404 today, because the theme is not yet posted in either name; the probe therefore cannot decide the point, and the flag rests on the posting-name convention, the same ground on which the M-pure-3 batch flagged five instances of this shape and a population sweep is repairing the family. This package does not edit the candidate; the flag is recorded so the sweep's list is complete.

### Record note — the vendored LOCALIZE row truncates the pattern-1/6 item

The vendored LOCALIZE-ROWS copy of this theme's row truncates its pattern-1/6 item ("same-site includes …"), so the charge's full text is not recoverable from the record. The bytes govern: the candidate's unprefixed references are the frame include (candidate L5) and the image-block include (L39), and the ledger's §(c3) line dispositions P1 without qualification.

## Appendix — residue blocks

Four blocks, resolved here by shape:

| Block | Span | Resolution |
|---|---|---|
| B5 | orig 21-21 → cand 23-23 | Heading translation: `+ Usage` → `+ 使用方法`. |
| B10 | orig 35-35 → cand 37-37 | Heading translation: `+ Examples` → `+ 使用例`. |
| B60 | orig 367-367 → cand 370-370 | CSS section comment: `/* BODY */` → `/* 本文 */`. |
| B70 | orig 489-489 → cand 492-492 | CSS section comment: `/* TABLES */` → `/* 表 */`. |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-scp-offices-sigma-jp.txt` is the decoration sample the render checks ran against (its capture is the exit-2 record of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** SCP Offices Sigma-9 Theme
- **Author:** macro_au_micro
- **Source:** https://scp-wiki.wikidot.com/theme:scp-offices-sigma — revision 10
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
