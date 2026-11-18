# Review package — theme:cmst-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:cmst-jp — origin CN, population #174 [GOSIGN2-LEDGER (b) row 174]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0f6c5b0a3f658e1401990ff295dc81bb458283f8ec5e4bfc6ffabfe8557bea0f); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 0 warns / 1 info (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 199; GOSIGN2-LEDGER (b) row 174]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow. [RENDER-ROWS-2 (RENDER-S2-E (CN3))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN3))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 173, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 173]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 174]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:cmst-jp.txt sha256:0f6c5b0a3f658e1401990ff295dc81bb458283f8ec5e4bfc6ffabfe8557bea0f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 174) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×5 (class (ii), section 11); the render row's two items (KB-40 / KB-33+KB-34, section 11); T4's delivery item (class (ii), section 11). One defect is flagged in the per-theme record: the usage example names a page that does not exist on scp-jp |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:cmst | theme:cmst-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 7 (first translation; the candidate's credit block records 初訳時参照リビジョン: 7) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:cmst-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 643 lines / 13,189 bytes | 345 lines / 7,737 bytes |
| SHA-256 | e188ed40dfa234b94469157711857b576cc907b5d5c6a69d25542ef77ef57bc3 | 5b8b8e717ee69c7dba3dd2681472a5a2e98c9f2402254dec54e13e8cd7f96ba2 |

Wave history: the candidate was created by the Stage 2 CN3 integration (commit 6a8eb9d) and last touched by FIX-CREDIT-D (commit 1869877, the translator-attribution normalization over all candidates). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. The original has been superseded upstream since revision 7; the follow-up artifact `diff-cmst-from7.txt` in the campaign record covers that delta (sources.tsv note, K5a-i), and it is not part of this package's diff.

## Summary

A small, dense port whose whole story is a delivery consolidation. The CN original carries its CSS twice: a live `[[module CSS]]` (original L1–314) and, inside the tag gate, a `[[module rate]]` and a full source exhibit (original L328–641) repeating the same CSS. The candidate carries the CSS once, as a `[[code]]` exhibit inside a collapsible (candidate L29–344) that is simultaneously the delivery: the head frame imports the page's own code block 1 from the draft host and the interwiki-style include names the same delivery. The bare Rate is deleted (the preview credit block is rate-bearing), the credit block is installed with the eight ruling-3 fields, the tag gate is localized, the three s3.bmp.ovh images are re-hosted to the draft host, and the header `content:` strings are translated (one with a glyph-form conversion). Measured churn (diff.md, the generator's difflib count with autojunk off: +37/−335, 372 changed lines in 9 change blocks / 7 diff sections; the −335 is dominated by the removed duplicate CSS copy, not by lost content). One item was flagged for repair in the per-theme record and has since been repaired by the population sweep: the usage example at candidate L27 named `:scp-jp:theme:cmst`, a page that does not exist (probe evidence there), and now names `:scp-jp:theme:cmst-jp`.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 9 change blocks — 8 specific (88.9%), 0 heuristic (0.0%), 1 residue (11.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 7 |
| DRAFT-HOST | 5 |
| CONTENT-STRING | 3 |
| IFTAGS | 2 |
| TRANSLATION-ANCHORED | 3 |
| TRANS-UNANCHORED | 1 |
| CREDIT-PREVIEW | 1 |
| TASL-FIELDS | 1 |
| SELF-DELIVERY | 1 |
| EXHIBIT-RESTRUCTURE | 1 |

Adjudication for this README (every block was read against the bytes): the DELIVERY-MOVE labels are the delivery consolidation of section 3 (the CSS body moved from a live module plus a duplicate exhibit into one self-delivered exhibit; the asset and string blocks inside it classify separately, as designed). The one residue block (B9) is the exhibit's closing furniture plus the candidate's added `[[/collapsible]]` line (section 8). The EXHIBIT-RESTRUCTURE primary (inside B8) is not an exhibit change: it is the tail of the duplicate-copy collapse, and the exhibit census of section 8 decides it. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:cmst-jp; original theme:cmst on scp-wiki-cn at reference revision 7; candidate `pages/theme:cmst-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN3 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved: the original opens directly with its live CSS module (original L1) and keeps its tag gate at L316; the candidate opens with the delivery frame (candidate L1–7) and places the localized gate `[[iftags +テーマ]]` at candidate L10.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization), the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for cmst-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module rate]]` (original L319, inside the tag gate). The candidate deletes it and installs the JP form at the head of the gated body: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L12–21) carrying the eight ruling-3 fields (title CMSTテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 CMST 版式; 著作権者 Sifen_Xingfeng; 作成年 2023; 初訳時参照リビジョン 7; the source link, candidate L20, naming scp-wiki-cn.wikidot.com — the original's recorded host). The original carries no info block and no license box, so nothing else is deleted here. No T7 credit-module CSS supplement exists in this theme: the candidate adds no `.creditRate`/`.creditButton` rules (the theme's own CSS has no credit selectors on either side).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become). Ruling 3 fixes the eight fields and the translator credit form; FIX-CREDIT-D normalized the attribution fields across all candidates, this file included.
- **Verify:** `grep -n 'module rate\|module Rate' candidate.txt` returns nothing; read candidate L12–21 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3) class outcome: credit fields FIXED by the credit waves, checker-verified; this theme's row records the P3 completion under that class outcome).

### 2. Includes and components

- **What:** No include repoint blocks: the original includes nothing but its credit-adjacent furniture. The candidate's include list is the frame pair (section 3), the credit pair (section 1), and one exhibit line, the usage example at candidate L27 (`@@[[include :scp-jp:theme:cmst]]@@`). That example is defective in its target, not its form: it names the original's slug on scp-jp, where no such page exists, instead of the candidate's own posting name — see the per-theme record for the probe evidence and the repair that has since landed. The original's corresponding example (in its usage text) named its own page the same way; the port repointed the wiki prefix and kept the slug.
- **Why:** P1 (KB-15) governs live includes; the usage example is governed by the campaign's settled rule that a copy-paste install example must name the page a user can actually include (AGENTS.md §6: usage examples naming `theme:<slug>` instead of `theme:<slug>-jp` are findings, because every copy-paste install breaks).
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, and candidate L27.
- **Disposition:** Live includes applied; the usage example is flagged in the per-theme record (not edited here; the coordinator lands repairs).

### 3. Delivery and code loading

- **What:** The consolidation described in the Summary (blocks B1, B2, B6–B8). The original delivers its CSS as a live `[[module CSS]]` (original L1–314) and repeats the same CSS as a source exhibit (original L328–641, similarity 0.97 by the classifier's body matching — the two copies differ only in their surrounding furniture). The candidate's head module (candidate L1–3) imports the page's own `local--code/theme%3Acmst-jp/1` from the draft host, the interwiki-style include (candidate L5–7) names the same /1 delivery at the frame's priority, and the single remaining copy of the CSS sits in the `[[code]]` exhibit (candidate L30–343) — which is code block 1, so the exhibit is the delivery. The original's delivery was already self-contained (no base theme, no cross-theme import), and the candidate keeps that shape.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame). The duplicate-copy removal follows from the delivery form: once the exhibit is the delivery, a second live copy would double-apply the same rules. The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting. The ledger's T4 line for this theme records the delivery item as DISPOSITIONED, class (ii) (original-state CDN delivery — the s3.bmp.ovh hosts of section 4 are the same item seen from the asset side).
- **Verify:** `grep -n 'local--code' candidate.txt` — candidate L2 and L7 only; compare the exhibit census in section 8.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii); the T4 delivery item, class (ii)).

### 4. Fonts and assets

- **What:** Fonts: none — neither side declares a `font-family` (0 lines in each file), so there is no font load and no stack to rewrite; the theme inherits the environment's JP fonts (the T5-absent shape: SUPPLEMENT-TYPES counts themes that declare no font-family and inherit). Assets: three images move from the CN image host s3.bmp.ovh to the draft host's `local--files/theme%3Acmst-jp/` folder with file names unchanged (B2: ff61cb0a740bd562.png, candidate L60; B6: 2728e34748fe1a1b.png, candidate L111; B7/B8: ed776c70c7ff51e6.png, candidate L124 and L330 — the rule appears twice in the single remaining CSS copy, in two different selectors). The localize lane called this migration exemplary (「s3.bmp.ovh 画像の全移行は模範的」, LOCALIZE-ROWS row 173).
- **Why:** P5 with KB-17 (asset hosts): the theme's own images are re-hosted to the JP side; s3.bmp.ovh is an outside host that serves today, so the re-host is the posting-procedure class (ii) shape, executed early at draft stage in the draft-host form (KB-41/KB-58 family).
- **Verify:** `grep -n 'bmp.ovh' candidate.txt` returns nothing; `grep -n 'local--files' candidate.txt` returns the four lines above.
- **Disposition:** DISPOSITIONED (class (ii) / KB-58: asset hosts are a posting-procedure item; the draft-host form stands at draft stage).

### 5. Header, sidebar, and site furniture

- **What:** None — the theme overrides no header variable on either side (no `--header-title`, `--header-subtitle`, or `--logo-image` in either file), and its sidebar rules are carried over unmodified inside the consolidated CSS copy. The site-name strings a reader sees are the `content:` values of section 6, not header variables. No P8 layout adaptation was needed: the candidate inherits the JP site furniture through the frame.
- **Why:** P9/T6 do not engage where the original sets no variables; recording the absence is the check.
- **Verify:** `grep -n -- '--header-\|--logo' original.txt candidate.txt` — no hits on either side.
- **Disposition:** Standing (checked, absent).

### 6. Text translation

- **What:** The prose body of this theme page is small (usage text around the exhibits), and it is translated throughout; the counted translation blocks are the three CONTENT-STRING blocks, which are the reader-visible strings inside the CSS: B3 and B4, the organization name in two `content:` rules (original L33/L37 「开米斯特超化研究中心」 → candidate L62/L66 「ケミスト超化研究センター」, the name transliterated into katakana with 研究中心 rendered 研究センター), and B5, the slogan string (original L67 「化学·唯物·探索·技术」 → candidate L96 「化学・唯物・探索・技術」). B5 is also an R5 glyph-form conversion: simplified 技术 becomes shinjitai 技術 and the middle-dot takes its Japanese form. In-CSS comment text (R1): the original's CSS carries no prose comments to translate (its section comments are the fork's structural markers, carried over). The localize lane's one display-affecting note stands in the bytes: the credit block's title field reads 「CMSTテーマ」 while the header strings read 「ケミスト超化研究センター」 — the organization-name notation variance the lane recorded (LOCALIZE-ROWS row 173, its item #1), left as a staff-judgment item.
- **Why:** P10 (body and usage translation) and KB-18 (reader-visible strings, including `content:`). R5 is named separately because a retained string can be neither translated nor untouched; a reviewer checking "was this string translated or left?" needs the third answer.
- **Verify:** `grep -n 'content:' candidate.txt` — the three strings above; a CJK scan of candidate.txt outside the credit block's 原題 field returns only translated text.
- **Disposition:** Standing (the port itself); the notation variance is carried in section 11.

### 7. Links

- **What:** One live outbound link: the credit block's source link (candidate L20), naming scp-wiki-cn.wikidot.com — the original's recorded host in sources.tsv, so the host check passes. The usage example at candidate L27 is an include, not a link, and is section 2's item. No prose link in the candidate targets a branch-wiki page; the original carried no hub or tag links to repoint.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — candidate L20 only.
- **Disposition:** Standing; no dead link, no repoint owed.

### 8. Structure

- **What:** The localize.md closing rule holds in its delivery form: variable names, selectors, and rule order inside the CSS are preserved — the candidate's single CSS copy is the original's CSS, with the section-4 asset lines and section-6 strings changed in place. The structural change is the consolidation itself (section 3): two copies become one. An exhibit census decides the R3 question: the original has one exhibit (the source `[[code]]` block) plus the live module; the candidate has one exhibit, which is also the delivery. Nothing was dropped or replaced — the removed 335 lines are the second copy of material that survives once, and the candidate wraps its exhibit in a `[[collapsible]]` (candidate L29/L344, block B9) where the original presented it bare; the collapsible is the JP source-exhibit framing form, and its show/hide labels are translated (「ソースコード」/「ソースコードを隠す」).
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[module\|\[\[code\|\[\[collapsible' original.txt candidate.txt`; the CSS rule sequence inside candidate L30–343 against original L1–314.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0). The line-count drop (643 → 345) is the duplicate-copy removal of section 3, a delivery change, not formatting churn, so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — the candidate carries no `[!-- ... --]` translator notes, no editor line, and no CSS comment without an original counterpart (checked explicitly against the candidate's comment lines; the head comment of the CSS copy is the original's own, carried over inside the consolidated copy).
- **Why:** R2: porter-added text is part of the change record; its absence is recorded so a reviewer does not have to wonder whether it was checked.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; compare comment lines against original.txt.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's five pseudo-ref errors: class (ii), posting-procedure — they are the candidate's draft-host self-delivery frame and its re-hosted asset URLs (sections 3–4); the posting procedure rewrites them to the production host, and fix lanes never "fix" them in the candidate. (2) The render row's two items, both environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40), and the sample's credit-modal errors plus its 884px@768 overflow (KB-32 preview form; KB-33/KB-34 cross-cutting families). (3) The T4 delivery item: DISPOSITIONED, class (ii) (original-state CDN delivery, GOSIGN2-LEDGER §(c3) for this theme). (4) The T4/T5 notation item: the organization-name variance between the credit title and the header strings (section 6) stands as the localize lane recorded it, a staff-judgment item on name unification and the readability of 「超化」; the ledger's determination for this theme is PASS and this package does not re-open it. Separately, the usage example of section 2 is flagged below as a defect the ledger did not record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–4); the usage example is flagged with evidence in the per-theme record.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 199): exit 1, 5 errors / 0 warns / 1 info; all five errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN3)): FINDINGS, the two items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 173): FINDINGS jointly, display-affecting findings 1 (the notation variance); the lane judged patterns 1/2/3/4/5/6 all correctly applied and the credit/interwiki additions and image migration exemplary. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +37/−335 in 9 change blocks / 7 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:cmst-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 174; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example names a page that does not exist (defect flag, repaired)

Candidate L27 reads `> @@[[include :scp-jp:theme:cmst]]@@` — the install example a reader copies to apply this theme. Probe made for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:cmst` returns 404; the candidate posts to scp-jp under its own name, theme:cmst-jp, so the example as written cannot be followed on the site it instructs for. The campaign's settled rule (AGENTS.md §6) names this exact shape a finding: usage examples inside candidate docs naming `theme:<slug>` instead of `theme:<slug>-jp` break every copy-paste install. The localize lane did not record it (its row covers patterns 1–11 against the original, and the original's own example named its own page correctly for its own wiki), and the ledger's determination for this theme is PASS; this package therefore carries the item as a flagged defect with its probe evidence, for the coordinator's repair wave. The candidate is documented as it stands; no byte of it was edited here. The same shape appears in several sibling candidates (the jiha exemplar's usage example among them), so the repair is a population question, not a one-file question. It has since been answered at that level: the repair has landed as the usage-example population sweep (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), which repaired this shape across all 157 affected candidates; candidate L27 now reads `> @@[[include :scp-jp:theme:cmst-jp]]@@`, and this package documents the corrected candidate (its stamp reads STALE against the pre-repair verdict, by design).

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-cmst-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The follow-up artifact `diff-cmst-from7.txt` sits in the campaign record (R), outside this repo. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** CMST 版式
- **Author:** Sifen_Xingfeng
- **Source:** https://scp-wiki-cn.wikidot.com/theme:cmst — revision 7
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
