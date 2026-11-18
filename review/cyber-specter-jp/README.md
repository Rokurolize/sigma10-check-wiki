# Review package — theme:cyber-specter-jp (KO → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:cyber-specter-jp — origin KO, population #258 [GOSIGN2-LEDGER (b) row 258]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ec3ce81023d9aa4e0ef09b73dd357b227e638f078260577a67041dc9b42fb02c); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 241; GOSIGN2-LEDGER (b) row 258]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink incl. scpko hosts (one combo http.cat among other hosts); T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO2))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 257, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 257]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 258]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:cyber-specter-jp.txt sha256:ec3ce81023d9aa4e0ef09b73dd357b227e638f078260577a67041dc9b42fb02c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 258) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 + pseudo-ref ×1 (class (ii), section 11); the render row's items (KB-41/KB-54 family; KB-33/KB-34, section 11); T4's P1, P5, P9, P10, P11 (section 11). One defect is flagged in the per-theme record: the usage examples name a page that does not exist on scp-jp |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:cyber-specter | theme:cyber-specter-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 35 (first translation; the candidate's credit block records 初訳時参照リビジョン: 35) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:cyber-specter-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 743 lines / 15,422 bytes | 752 lines / 16,138 bytes |
| SHA-256 | 360936755bab2abf5e8bdc0248cf6a88e63cbc4ece1d1ce0798ed50b085ccfc0 | d34eacf99103de4041921d2819882827c529f18b5d587bc06b83113ee74af1a7 |

Wave history: the candidate was created by the Stage 2 KO2 integration (commit d72b7b9) and last touched by FIX-CREDIT-D (commit 1869877, the translator-attribution normalization over all candidates). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Korean fandom-division theme (for the WoI research division) whose original has no delivery frame at all: it opens with its tag gate and its rate/info exhibits and carries its CSS inline. The port adds the JP furniture without disturbing that shape — the preview credit block goes in at the head of the gated body (candidate L3–12), the exhibits' live modules come out (the Rate deleted, the info pair deleted; their translated headings remain as the exhibit labels), and the delivery frame is appended at the file's end (candidate L747–751), the closing-rule position for a theme whose original has no head frame. The theme's own assets stay on the scpko host with only their colons percent-encoded — the T1 hotlink item, dispositioned as a posting-time re-host — and the header defaults keep their Korean strings under ruling 2. Both usage examples (candidate L35, L42) named `:scp-jp:theme:cyber-specter` as built, a page that does not exist; that was the per-theme record's flagged defect, since repaired by the population sweep (both now name `:scp-jp:theme:cyber-specter-jp`). Measured churn (diff.md: +63/−59, 122 changed lines in 30 change blocks / 3 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 30 change blocks — 14 specific (46.7%), 11 heuristic (36.7%), 5 residue (16.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 13 |
| TRANSLATION-ANCHORED | 5 |
| IFTAGS | 2 |
| INFO-DEL | 2 |
| COLON-ENC | 2 |
| DRAFT-HOST | 2 |
| SELF-DELIVERY | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| BARE-RATE-DEL | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| CSS-BODY | 1 |

Adjudication for this README (every block was read against the bytes): the one EXHIBIT-RESTRUCTURE label sits on B18, the image-block repoint inside its exhibit — the standing false-fire, discharged by the census in section 8. The one CSS-BODY block (B27) is the tail CSS rule adjoining the appended frame: the rule is carried, and its span difference is the frame's arrival (section 3). The five residue blocks are adjudicated in the appendix: two are the flagged usage examples, one is the tag gate's closing line becoming a separator (the gate now wraps the appended frame), and two are blank-line alignment. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:cyber-specter-jp; original theme:cyber-specter on scpko at reference revision 35; candidate `pages/theme:cyber-specter-jp.txt`. Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; no production JP counterpart, so the R4 adoption question does not arise). The original's tag gate (original L1, +테마) opens the file; the candidate's localized gate (+テーマ) opens it too, and now wraps the whole file including the appended frame (section 3).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline.
- **Verify:** The sources.tsv row for cyber-specter-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at candidate L3–12 with `:scp-jp:`-prefixed includes, carrying the eight ruling-3 fields: title 사이버 망령 CSS 테마 (the theme's Korean title, kept as the title field; the page's own heading is translated, サイバー・スペクター・テーマ, candidate L14); 翻訳責任者 AI; 翻訳年 2026; 原題 사이버 망령 CSS 테마; 著作権者 romrom; 作成年 2022; 初訳時参照リビジョン 35; the source link (candidate L11) naming scpko.wikidot.com, the original's recorded host — its link text is the Korean title rather than the standard 「ソース」, the standing uniform wording nit the campaign records once per report rather than as a per-theme failure (AGENTS.md, T5 name-normalization note). The original's credit furniture was the exhibit pair: a live `[[module Rate]]` under its 評価モジュール heading and an info:start/end pair under its クレジット付き heading. Both modules are deleted (BARE-RATE-DEL; INFO-DEL ×2) and their headings survive translated (candidate L17, L21) as the labels of the now-empty exhibit frames, because the preview block at the head is the theme's single rate+credit form. No T7 credit-module CSS supplement exists in this theme.
- **Why:** P3/T1 and ruling 3; KB-09 for the duplicate a kept Rate would make beside the preview block.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L3–12 against the eight fields.
- **Disposition:** FIXED (the ledger's class outcome: credit fields FIXED by the credit waves; this file's last touch is FIX-CREDIT-D).

### 2. Includes and components

- **What:** The frame pair (section 3) and the credit pair (section 1). The image-block include inside the exhibits is repointed to `:scp-jp:` (candidate L50), while its image name stays on the scpko host with the colon percent-encoded (candidate L51, section 4). The two escaped usage examples (candidate L35 and L42, each opening a multi-line include with parameters) named `:scp-jp:theme:cyber-specter` as built — the original's slug, not this candidate's posting name, and the per-theme record's flagged defect, since repaired by the population sweep (both now name `:scp-jp:theme:cyber-specter-jp`).
- **Why:** P1 (KB-15) for the live includes; the usage examples under the campaign's settled rule (AGENTS.md §6).
- **Verify:** `grep -n '\[\[include' candidate.txt` — the credit pair, the image-block line, the tail frame, and the two escaped examples.
- **Disposition:** Live includes applied; the usage examples are flagged in the per-theme record (not edited here; the coordinator lands repairs).

### 3. Delivery and code loading

- **What:** The original delivers its CSS inline with no frame and no code block. The candidate keeps the inline delivery and appends the frame at the end: the head-of-tail module imports the page's own /1 from the draft host (candidate L747) and the interwiki-style include follows (candidate L749–751) naming the same delivery (SELF-DELIVERY ×2, DRAFT-HOST ×2). The tag gate's closing line moves with it: where the original closed its gate mid-file, the candidate's gate wraps the frame too, and the original's closing line becomes a `----` separator in the exhibit flow (residue B23, appendix). B27, the classifier's CSS-BODY block, is the tail CSS rule adjoining the appended frame.
- **Why:** P6/T3 (the interwiki-style supplement frame) and P4/T9; the end position is the closing rule for a theme whose original carries no head frame, so the theme's own opening (gate, credit, exhibits) is undisturbed. The draft-host form is KB-41, class (iii).
- **Verify:** Read candidate L745–752; `grep -n 'local--code' candidate.txt` — the tail frame only.
- **Disposition:** DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts: the Do Hyeon display face load is kept as it stands (candidate L99) and its stacks (`'Do Hyeon', sans-serif`, candidate L132/L153) are unchanged — no font block appears in the classification, and no row charged this theme's fonts; the theme's display typography is its Korean display face, carried over. Assets: the theme's own images are NOT re-hosted at draft stage. Two CSS asset URLs keep the scpko host with only the colon percent-encoded (COLON-ENC ×2: woiwall5.png, candidate L108; WoI2.png, candidate L114), and the image-block exhibit's image name does the same (candidate L51). These three lines are T1's hotlink ×3.
- **Why:** P5's re-host is owed for a theme's own assets, and the ledger dispositions exactly these lines as the posting-time half of that move: candidate-own foreign delivery hosts are rewritten at posting, or the original-state delivery stands as a class (ii) item (KB-41/KB-54 family; GOSIGN2-LEDGER §(c2)/(c3) for this theme, P5 class (ii)/KB-58). The colon encoding itself is the settled URL form for wdfiles paths.
- **Verify:** `grep -n 'scpko' candidate.txt` — the three asset lines and the credit source link; `grep -n '%3A' candidate.txt`.
- **Disposition:** DISPOSITIONED (class (ii): re-host at posting).

### 5. Header, sidebar, and site furniture

- **What:** The header defaults keep their Korean strings: the subtitle default inside the CSS (candidate L102) and the WoI研究科 name strings stand as the original set them. The localize lane charged this as P9 (LOCALIZE-ROWS row 257); ruling 2 settles header language as translation taste outside migration correctness, and the ledger dispositions P9 on that ground. The page heading itself is translated (candidate L14). No P8 layout adaptation was needed.
- **Why:** P9's charge and ruling 2's settlement are both recorded so the kept Korean reads as a decision, not an oversight.
- **Verify:** `grep -n 'header-sub\|header-title' candidate.txt` against original.txt — the defaults match the original's.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3)).

### 6. Text translation

- **What:** The prose and exhibits are translated throughout (TRANSLATION-ANCHORED ×5, TRANS-UNANCHORED ×13, CREDIT-PROSE ×1), including the exhibit headings of section 1 and the keyboard-sample specimen, whose Korean key-mash string (ㅁㄴㅇㄹ) becomes the Japanese kana sample (あいうえお) — a specimen translated by function, not by glyph. The localize lane's P10 items stand in the bytes as recorded: an orphan `]`, an empty collapsible, and an empty label in the exhibit specimens (LOCALIZE-ROWS row 257), dispositioned at lane severity as specimen-layer items (section 11). The credit block's title fields keep the Korean title (section 1), which is a credit-field form, not untranslated prose.
- **Why:** P10 (body and usage translation); the specimen items are recorded with their lane severity rather than silently normalized.
- **Verify:** A CJK scan of candidate.txt outside the credit block's Korean title fields and the section-5 header defaults returns translated text and the recorded specimens.
- **Disposition:** Standing (the port itself); P10 DISPOSITIONED (section 11).

### 7. Links

- **What:** The credit source link (candidate L11) names scpko.wikidot.com, the original's recorded host — the host check passes. The prose's hub link is the lane's P11/P1 item: the original links its WoI research division hub page, which has no JP counterpart (the lane probed it: 404, no target); the candidate carries the reference in the batch-posting class, and the ledger dispositions it as sibling/batch-posting (the hub is a sibling page whose port is a separate batch item, not this theme's defect).
- **Why:** P11, under the dead-reference evidence standard: a link whose target does not exist on the JP side is either repointed to a serving page or recorded with its probe; here the record is the lane's, with its disposition class named.
- **Verify:** `grep -n 'woi-research' candidate.txt` — the hub reference; the lane's probe is LOCALIZE-ROWS row 257.
- **Disposition:** DISPOSITIONED (sibling/batch-posting; GOSIGN2-LEDGER §(c3)).

### 8. Structure

- **What:** The closing rule holds inside the CSS: selectors, rule order, and variable names are preserved; the internal changes are the section-4 colon encodings. Exhibit census (R3): the original's exhibits (the two credit-form exhibits, the usage examples, the image specimen, the sample strings) all survive in the candidate in the same order; the two credit-form exhibits keep their headings and lose their live modules (section 1), which is the recorded furniture swap, not a restructuring; B18's EXHIBIT-RESTRUCTURE label is its include repoint, discharged on that ground.
- **Why:** R3 forces the census because a restructure and a deletion share a diff shape.
- **Verify:** Compare the exhibit sequence in original.txt L1–60 against candidate.txt L1–70.
- **Disposition:** Standing; no structural deletion beyond the recorded furniture swap, no class I item.

### 9. Formatting only

- **What:** None — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0). The two blank-line residue blocks (appendix) are alignment around the moved furniture, not formatting churn.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — the candidate carries no `[!-- ... --]` translator notes, no 訳注 footnote, and no editor line (checked explicitly). The Korean title kept in the credit fields (section 1) is credit furniture, not an annotation.
- **Why:** R2: porter-added text is part of the change record; its absence is recorded so a reviewer does not have to wonder whether it was checked.
- **Verify:** `grep -n '\[!--\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's errors: hotlink ×3 (the section-4 scpko asset lines, class (ii), re-host at posting) and pseudo-ref ×1 (the tail frame's draft-host import, class (iii)). (2) The render row's items: the sample's credit-modal errors and 884px@768 overflow (KB-32 preview form; KB-33/KB-34 cross-cutting families), and the runtime-hotlink lines including scpko hosts, dispositioned with item (1)'s class (KB-41/KB-54 family). (3) T4's P5: DISPOSITIONED, class (ii)/KB-58 — the KO wdfiles direct links are the same asset lines as item (1), seen from the localize side. (4) T4's P9, P10, P11: DISPOSITIONED (ruling 2; lane severity/specimen; sibling/batch-posting), sections 5–7. Separately, the usage examples of section 2 are flagged below as a defect the ledger did not record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–4); the usage examples are flagged with evidence in the per-theme record.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 241): exit 1, 4 errors / 2 warns / 1 info; the errors are hotlink ×3 and pseudo-ref ×1, both posting-procedure classes; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO2)): FINDINGS, the items of section 11(2), all dispositioned; T3 recorded nothing beyond the cross-cutting items; engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 257): FINDINGS jointly, display-affecting findings 3 (P5, P9, and the P11/P1 hub item, with P10's specimen items noted), all dispositioned. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +63/−59 in 30 change blocks / 3 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:cyber-specter-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 258; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage examples name a page that does not exist (defect flag, repaired)

Both install examples name the original's slug on scp-jp: candidate L35 and candidate L42 each open `@@[[include :scp-jp:theme:cyber-specter@@` (the include continues with parameters on the following lines). Probe made for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:cyber-specter` returns 404; the candidate posts to scp-jp under its own name, theme:cyber-specter-jp, so neither example can be followed on the site it instructs for. The campaign's settled rule (AGENTS.md §6) names this exact shape a finding: usage examples inside candidate docs naming `theme:<slug>` instead of `theme:<slug>-jp` break every copy-paste install. The localize lane did not record it, and the ledger's determination for this theme is PASS; this package carries the item as a flagged defect with its probe evidence, for the coordinator's repair wave. The candidate is documented as it stands; no byte of it was edited here. The repair has since landed: the usage-example population sweep (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), which repaired this shape across all 157 affected candidates; candidate L35 and L42 now open `@@[[include :scp-jp:theme:cyber-specter-jp@@`, and this package documents the corrected candidate (its stamp reads STALE against the pre-repair verdict, by design).

## Appendix — residue blocks adjudicated

| Block | Original → candidate | Adjudication |
|---|---|---|
| B12 | L26–27 → L34–35 | The first usage example (flagged defect, per-theme record) |
| B14 | L33–34 → L41–42 | The second usage example (flagged defect, per-theme record) |
| B16 | L37–38 → L45 | Blank-line alignment after the exhibit prose |
| B23 | L71–72 → L78–79 | The original's mid-file `[[/iftags]]` becomes a `----` separator: the candidate's gate wraps the appended tail frame (section 3) |
| B30 | L740–743 → L752 | The file's tail blank lines after the appended frame |

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-cyber-specter-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The WoI hub page of section 7 is a sibling page with its own record, not part of this change set. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 사이버 망령 CSS 테마
- **Author:** romrom
- **Source:** https://scpko.wikidot.com/theme:cyber-specter — revision 35
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
