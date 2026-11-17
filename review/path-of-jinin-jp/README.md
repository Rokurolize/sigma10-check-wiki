# Review package — theme:path-of-jinin-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:path-of-jinin-jp — origin KO, population #281 [GOSIGN2-LEDGER (b) row 281]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now d39bac770b807e80428a7b11decc2a1306c7632c72654e46ed936fa2c7f17058); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 251; GOSIGN2-LEDGER (b) row 281]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-* cluster confined to webkit-768, whose only hotlink host is http.cat = transient 503 capture, not a result; page runtime-hotlink site-theme chain otherwise; sample credit-modal (preview-form) + runtime-hotlink; T3 none beyond cross-cutting items. [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO7))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 280, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 280]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 281]
- Computed against: canonical commit 967ec2f4a240dfaf825b2c3152610ed8c4a23b5a; candidate file pages/theme:path-of-jinin-jp.txt sha256:d39bac770b807e80428a7b11decc2a1306c7632c72654e46ed936fa2c7f17058; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 281). The stamp reads STALE because the usage sweep changed one line after the verdict (per-theme record) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×6 (posting classes, section 11); the render row's items (hidden-* capture cluster, runtime-hotlink chain, credit-modal preview form, section 11). **FIXED** — the duplicate frame priority (P6, FIX4-IWB). **Three flags from this package:** the in-gate frame still names a fragment that does not exist (probe-verified, per-theme record); the credit author field names no one, though the original names two creators (per-theme record); the T5 title inconsistency and the two empty labels stand in the bytes (section 6) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:path-of-jinin | theme:path-of-jinin-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 12 (first translation; the candidate's credit block records 初訳時参照リビジョン: 12) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-F/orig-path-of-jinin.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:path-of-jinin-jp.txt`, copied at worktree HEAD 2aee861 |
| Lines / bytes | 624 lines / 11,649 bytes | 651 lines / 13,323 bytes |
| SHA-256 | 4952b36e256a7c89e42dee5d75e75f092a39a55328729883e112dc0e6bb66bf1 | 7f1b0d747f711bc7952ab621d72b642f07cc101c66742f7df6acf37a7dd13b75 |

Wave history: the candidate was created by the Stage 2 KO7 integration (commit 6889a0a); FIX-P4 (f1138e4) repointed its base-theme CSS imports to the JP port candidates; FIX4-IWB (5559209) split its duplicate interwiki-style priority (section 3); the usage sweep (b5cb724) made the one post-verdict line change recorded below.

## Summary

A theme for the Seulga (世乙加） GoI format, by c_bonefish and thd-glasses, on Denevola's base code. The original is a conventional KO theme page: head delivery module and frame, a gated body with a floated bare Rate and an info pair, specimens, and the CSS in one code exhibit delivered from the tail of the page's own code. The candidate follows the same shape — head module and frame, preview credit block, translated specimens, the exhibit with JP font imports at its head and the asset hosts repointed — with measured churn of +80/−58 in 39 change blocks / 9 hunks, sixteen of the blocks being whitespace-only lines inside the exhibit. Three things in this candidate need a reviewer's eye rather than a skim, and all three are stated with their evidence in the per-theme record: a second, in-gate interwiki-style frame that names a code fragment which does not exist; a credit author field that points at the original page instead of naming the two creators the original names; and the T5 record's two editorial residues (a title that disagrees with itself between the credit block and the body heading, and two section labels left empty by the furniture swap). The frame-priority defect the campaign charged against this theme is genuinely fixed in the bytes; the rest of T4's frame finding is not.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 39 change blocks — 33 specific (84.6%), 6 heuristic (15.4%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| WS-ONLY | 16 |
| TRANS-UNANCHORED | 11 |
| DRAFT-HOST | 7 |
| TRANSLATION-ANCHORED | 4 |
| SELF-DELIVERY | 3 |
| DELIVERY-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| ESCAPED-INCLUDE | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| COMMENT-TEXT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 16 WS-ONLY blocks are blank-line changes inside the CSS exhibit, counted in section 9; B38's CSS-BODY primary is the exhibit's closing furniture (the `[[/code]]` and the added `[[/collapsible]]`), not a CSS edit; B2's EXHIBIT-RESTRUCTURE primary is the head furniture arriving (credit block, frame replica, gate), adjudicated in sections 1–3; B10's is the image-block specimen's host repoint. The skeleton's per-section "none" readings do not survive for sections 3–4, whose signatures ride inside the delivery blocks. After adjudication no block is left unexplained, and there is no residue to append.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:path-of-jinin-jp; original theme:path-of-jinin on scpko at reference revision 12; candidate `pages/theme:path-of-jinin-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 KO7 wave (sources.tsv kind: standard; no production JP counterpart is recorded for this theme — a fact the frame discussion in section 3 depends on). Both sides open with the delivery module and a frame ahead of the gate; the candidate's gate is `[[iftags +テーマ]]` (candidate L8) where the original's is `[[iftags +테마]]` (original L9).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the delivery pair is section 3.
- **Verify:** The sources.tsv row for path-of-jinin-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a floated bare `[[module Rate]]` under the label 評価モジュール (original L13–17) and an `[[include info:start]]`/`info:end` pair under the label 情報モジュール付き評価モジュール (original L19–23) — the info pair is empty, carrying no fields at all. The attribution lives in the prose (original L24: the theme was made by [[*user c_bonefish]] and [[*user thd-glasses]] for the Seulga GoI format) and in the exhibit's banner ("Created by c_bonefish and thd-glasses. Base Code by Denevola. CC BY-SA 3.0", original L61–68). The candidate deletes both modules (blocks B6, B7) and installs the JP credit block (candidate L11–20): a `:scp-jp:credit:start-preview`/`end-preview` block with the eight ruling-3 fields — title 真人の道 テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 진인의 길 CSS 테마; **著作権者： 原語版ページの作成者に同じ（scpko の theme:path-of-jinin)**; 作成年 2022; 初訳時参照リビジョン 12; the source link (section 7). The author field is this package's second flag: it names no one (per-theme record). The license box at the tail (candidate L644–650) repeats the pointer in its include parameter (`author=scpko theme:path-of-jinin の作者`) and carries one combined image/font provenance entry, which states that images without a license statement in the original are to be confirmed with the author before posting. Denevola's base-code credit survives verbatim in the exhibit banner (candidate L81–89), and both creators are named in the candidate's prose (candidate L33).
- **Why:** P3/T1 (KB-09) for the furniture: the preview credit module is rate-bearing, so the floated bare Rate is deleted rather than duplicated, and the empty info pair has nothing to convert. Ruling 3's fields are the attribution record of the port; a field that points instead of naming fails the purpose the fields exist for, which is why the flag is raised even though the names are present elsewhere in the file.
- **Verify:** Read candidate L10–20 against the eight fields; read original L24 and L61–68 for the names the field should carry.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified) as to the furniture; the author field's content is **flagged** (per-theme record).

### 2. Includes and components

- **What:** The candidate's live includes are the two frames (section 3), the credit pair (candidate L11, L20), the image-block specimen (candidate L41: unprefixed `component:image-block` as in the original, its `name=` repointed in section 4), and the license-box pair (candidate L644, L650). The one include repoint with a target change is the usage example: `:scpko:theme:path-of-jinin` → `:scp-jp:theme:path-of-jinin-jp` (original L26 → candidate L36, the post-sweep form; the example sits in a blockquote on both sides). Every live include names a `:scp-jp:` target or the local component form the original itself used.
- **Why:** P1 (KB-15) for the repoint; ruling 4 is not engaged — no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — frames, credit pair, image-block, license-box pair, and the escaped usage line.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** Both sides deliver the theme's own code the same way at the head: a `[[module CSS]]` importing its own `local--code/1` (original L2 from scpko.wikidot.com; candidate L2 from the draft host) ahead of a frame naming the same fragment. The candidate has exactly one `[[code]]` block (the exhibit, candidate L72–641), so both head lines' /1 address names the block that holds the CSS — verified against the census. **Frame paragraph (the M-frame addition):** this candidate carries two frames, and their history is the theme's T4 story. The head frame (candidate L5–8) is at `priority=2` with `theme=` naming the candidate's own /1 on the draft host. Inside the gate, after the credit block, sits a second frame (candidate L22–25) at `priority=1` whose `theme=` names `https://scp-jp.wikidot.com/local--code/theme%3Apath-of-jinin/1` — the production wiki's fragment for the *original's* page name, not this candidate's. As the campaign found it, both frames were at priority=1 (a duplicate-priority defect, KB-07, charged in register c2); FIX4-IWB (commit 5559209) split the duplicate by moving the head frame to priority=2, and that half of the repair is visible in the bytes and in this file's history. The other half of T4's finding (LOCALIZE-ROWS row 280, type 6) is that the in-gate replica points at a local--code that does not exist — and that half stands: the production page theme:path-of-jinin returns 404, and the fragment URL serves the twelve bytes "No such page" (probe, per-theme record). The taxonomy's T10 entry (remote-original layering) names this candidate as one of its two instances; whatever the layering was meant to bind, the named target is absent, so the priority=1 layer loads nothing. The original's own head frame, for comparison, was a single frame at priority=1 naming its own /1 on its own wiki (original L5–8) — the candidate's in-gate replica has no counterpart in the original at all.
- **Why:** P4/T9 for the head pair (own-code delivery from JP hosts; the draft-host form is KB-41, class (iii)) and P6/T3 (KB-07) for the frame stack: priorities order the layers, a duplicate priority is a console-error defect on every page, and a frame entry naming a nonexistent fragment is a broken layer, not a convention.
- **Verify:** Read candidate L1–8 and L22–25; `grep -c '\[\[code' candidate.txt` — one; the probe pair is in the per-theme record and re-runnable from the URLs there.
- **Disposition:** FIXED (the duplicate priority, FIX4-IWB; ledger §(c3) P6 FIXED); the in-gate frame's target is **flagged as a defect** (per-theme record), not dispositioned; the head import is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** The load (block B17): the candidate's exhibit opens with two Google Fonts `@import`s (candidate L73–74: Noto Sans JP 400;700 and Noto Serif JP 400;700), ahead of the porter comments and the author's banner. Neither side declares a `font-family` stack anywhere (verified by grep on both files) — the theme inherits the site fonts — so the load is an availability supplement, not a stack conversion: it makes the two JP faces present for the elements the site chain assigns them to. The original exhibit has no font load at all. Assets (blocks B10, B18–B20): the header background (back-1.png), the logo strip (logo-2.png), and the image-block specimen's image (logo-1.png) all move from scpko.wikidot.com's file area to the candidate's own draft-host file area, file names unchanged (candidate L41, and L93–99 in the exhibit).
- **Why:** P7/T5 for the load (the JP faces are the population's standard supplement; KB-16's gap is stated here in its weak form — no stack names them in this file, and this package records that rather than inventing a conversion). P5/KB-17 for the asset re-hosting.
- **Verify:** `grep -n 'font-family' original.txt candidate.txt` returns nothing on either side; `grep -n 'local--files' candidate.txt` — the three repointed assets.
- **Disposition:** Load applied; the draft-host asset URLs are DISPOSITIONED (class (iii) draft form).

### 5. Header, sidebar, and site furniture

- **What:** No `--header-*` variable overrides exist on either side; the header is styled by element rules inside the exhibit (the `div#container-wrap` background and the extra-div logo strip, section 4's repoints), which travel verbatim apart from their hosts. The theme's sidebar rules likewise carry over inside the exhibit (including the `@media (max-width: 767px)` sidebar background at the exhibit's tail, identical on both sides). No P8 layout adaptation was needed; the render row's sidebar-adjacent item is the capture cluster of section 11, not a rule in this file.
- **Why:** P9/T6 is a per-theme judgment and none was needed: the original sets no header text variables to convert, and KB-57 / ruling 2 are not engaged.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; compare the exhibit tails (original L615–622, candidate L635–641).
- **Disposition:** Standing.

### 6. Text translation

- **What:** The body is translated throughout (blocks B5, B9, B11–B15): the intro prose (candidate L33, naming both creators and the Seulga format), the usage instruction, and the specimen set (headings retitled from the bare 제목1–6 form to the level-explicit 1階層目の見出し form, the tabview specimens with their sample text and footnote, the link specimens). Two T5 residues stand in the translated bytes, both recorded by LOCALIZE-ROWS row 280 and both still present. (1) Title inconsistency: the credit block's title is 真人の道 テーマ (candidate L12) while the body's own heading is 真人之道CSSテーマ (candidate L27) — the two renderings of 진인의 길 disagree (the body form also keeps the Chinese-style 之）. (2) Empty labels: the labels 評価モジュール： (candidate L29) and 著作情報欄： (candidate L31) head nothing — the modules they introduced in the original (the bare Rate, the info pair) were deleted by the furniture swap (section 1), and the labels were carried over as bare bold lines with no content under them. Korean survives in the candidate in the credit block's original-title field (candidate L15) and in the exhibit's author banner, which is carried in its original bilingual form (candidate L76–89: the porter's Korean-titled banner line 진인의 길 heads the author's English credit block) — both quotations.
- **Why:** P10 for the translation; KB-18 for the residues — both are reader-visible, and an empty section label is exactly the kind of editorial residue a reviewer should not have to discover unaided. They are recorded here as standing T5 items, not silently normalized in this package's prose.
- **Verify:** Read candidate L27–33; compare the original's corresponding span (original L11–24).
- **Disposition:** Standing (the port itself); the two residues are recorded T5 items, neither fixed in the candidate nor hidden.

### 7. Links

- **What:** The credit block's source link (candidate L19) names `https://scpko.wikidot.com/theme:path-of-jinin` — the host review/sources.tsv records for the original; no host defect. The specimen body keeps one branch link in translated form (candidate L57: `[[[theme:path-of-jinin|訪問済みリンク]]]`, a visited-link specimen naming the original page, as the original's specimen did). No prose link in the candidate targets a KO-wiki page for navigation.
- **Why:** P11: prose links take the JP counterpart or the serving original; specimen links are sample text and follow P10, which is what the bytes show.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the delivery hosts of section 3.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds for the CSS: variable names, selectors, and rule order inside the exhibit match the original's code block, and a brace-depth scan of the candidate closes at depth 0 with no negative excursion. The exhibit gains furniture at both ends (the font imports and porter comments at its head, the collapsible wrapper around it, the license box after it) without interleaved edits to the inherited rules — the sixteen whitespace-only blocks of section 9 are the one systematic exception, and they change blank lines, not rules. The page-level structure changes are the furniture swap (section 1), the second frame (section 3), and the exhibit's collapsible; the specimen census (tabview and tabs, image-block, headings, blockquote specimens) is present on both sides in the same order.
- **Why:** R3's distinction is met by the census; the two EXHIBIT-RESTRUCTURE primaries adjudicate to the head furniture (B2) and the image-block repoint (B10), not to exhibit changes.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt`; the depth scan is re-runnable over candidate.txt's exhibit.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Sixteen WS-ONLY blocks (B21, B23–B37), all inside the CSS exhibit: single blank lines added or removed between rules across the exhibit's span (from candidate L142 to L551). They change no rule, selector, or declaration, but they are inside the delivered code, so a follow-up diff of the code block against the original's will show them — the R7 hazard in its mildest form, disclosed here so the count is on record. No re-indentation accompanies them (the classifier's reindent count is 0).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so the exhibit's drift from the original's blank-line pattern is a known quantity.
- **Verify:** diff.md's exhibit hunks; each WS-ONLY block is a blank-line pair in the diff.
- **Disposition:** None required; disclosed.

### 10. Porter annotations

- **What:** Two annotations, both at the exhibit's head. (1) Candidate L76: the port provenance comment, `/* 진인의 길 / Path of Jinin — Ported for SCP-JP (theme:path-of-jinin rev 12 on scpko). */`, riding inside B17's font-load block. (2) Candidate L79: `/* 日本語フォント (JP localization) */`, the one-line label for the font imports above it. The author's own banner follows verbatim (candidate L81–89). No other porter comment exists in the file; in particular, neither frame carries an explanatory comment, which is part of why the in-gate replica's purpose has to be reconstructed from the records (section 3).
- **Why:** R2: porter-added text is part of the change record.
- **Verify:** Read candidate L72–89.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's six pseudo-ref errors: the candidate's references to not-yet-posted JP addresses (the delivery lines and the exhibit's production-form references among them) — classes (ii)/(iii) by form; the posting procedure resolves them, and fix lanes never "fix" them in the candidate. (2) The render row's items, all environment or capture layer, not charged to the candidate: the page's hidden-* cluster confined to webkit-768, whose only hotlink host is http.cat (KB-44: a transient Wikidot 503 capture, not a result); the page's and sample's runtime-hotlink site-theme chain (KB-40); and the sample's credit-modal errors (KB-32, ruling 5). (3) The T10 remote-layering form itself: the taxonomy records this candidate as a layering instance, and section 3 states what the named layer resolves to today. **Not dispositions:** the in-gate frame's nonexistent target and the credit author field — both are flagged below with their evidence, and the ledger's P6/P3 FIXED lines are quoted there alongside the bytes. The ledger's determination for this theme is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a byte-level defect is flagged, never dispositioned by relabeling.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); the two flags stand as flags.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 251): exit 1, 6 errors / 1 warn / 1 info; all six errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-H (KO7)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 280): FINDINGS jointly, display-affecting findings 1 (the frame item); the row's T5 half records the title inconsistency and the empty-label residue, and its type-3 item is the vague credit field; the ledger §(c3) line records P3 and P6 as FIXED by the credit and frame waves. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +80/−58 in 39 change blocks / 9 hunks; the brace-depth scan and the delivery probes were run for this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:path-of-jinin-jp.txt`, `python3 review/build_review.py --check` in this repo, and the probe pair in the per-theme record.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 281; go-sign, COMPLETION-REPORT §10) — for the pre-sweep file, with this package's flags standing against the current bytes.

## Per-theme record

### The in-gate frame names a fragment that does not exist (defect flag, probe-verified) Repaired after this package was built: commit 967ec2f repointed the in-gate `theme=` to the candidate's own `/1` on the draft host; see the post-package repairs item below.

Candidate L22–25 is a second interwiki-style include, inside the gate, at priority=1, naming `https://scp-jp.wikidot.com/local--code/theme%3Apath-of-jinin/1`. Probe made for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:path-of-jinin` returns 404 — the page does not exist on the production wiki — and the fragment URL itself, followed through its redirect, serves twelve bytes of plain text: "No such page". The fragment exists nowhere else either: this repo's composition carries the candidate under its `-jp` name, and the check wikis mirror the repo. T4 recorded the shape before the fix waves (LOCALIZE-ROWS row 280, type 6: the in-gate interwiki replica points at a nonexistent local--code, display-affecting). The fix the campaign then landed (FIX4-IWB, commit 5559209; register c2) repaired the duplicate priority — the head frame now sits at priority=2 — and the ledger's c3 line records P6 FIXED. That repair is real, and it is the half of the finding that concerned the frame stack's integrity. The target's nonexistence is the other half, and it is unchanged in the current bytes: at posting, the priority=1 layer of any page using this theme would request a fragment that serves "No such page". Whether the replica was meant to bind the production original (the T10 layering reading), a posting-name the porters expected the original to take, or is simply a duplicated frame line whose target was never corrected, the records do not say; the bytes say what it does today. The repair is small (the replica's removal, or its repointing at a target that exists); this package makes neither edit, per the review protocol, and flags the defect with its evidence for the coordinator's fix lane.

### The credit author field names no one (defect flag) Repaired after this package was built: commit 967ec2f named c_bonefish & thd-glasses in both carriers; see the post-package repairs item below.

The original names its creators in two places a credit check reads: the prose (original L24, c_bonefish and thd-glasses, for the Seulga GoI format) and the exhibit banner ("Created by c_bonefish and thd-glasses. Base Code by Denevola"). The candidate's 著作権者 field (candidate L16) reads 原語版ページの作成者に同じ（scpko の theme:path-of-jinin) — "same as the original page's creators" — and the license box's author parameter (candidate L645) repeats the pointer form. T4 charged exactly this (LOCALIZE-ROWS row 280, type 3: 著作権者 vague); the ledger's c3 line records P3 FIXED by the credit waves, whose population-wide completion filled the eight fields in every candidate — and for this theme the filled value is the pointer. The names are not lost to the file (the prose at candidate L33 names both creators, and the banner is carried verbatim in the exhibit), but the field whose purpose is to carry the attribution carries a direction to look elsewhere instead. Under the campaign's own credit standard — the field is checked against the original's credit, including attribution lines beyond the field itself — that is a defect in the field, recorded here with both sides' text; the one-line repair (naming c_bonefish & thd-glasses, with Denevola's base-code credit already preserved in the banner) is the coordinator's to land.

### The post-verdict line (why the stamp reads STALE)

The candidate changed once after the FIX5 head: the usage sweep (commit b5cb724) corrected the escaped usage example at candidate L36 from `@@[[include :scp-jp:theme:path-of-jinin]]@@` to the `-jp` posting name. That is the whole of the drift the stamp reports: one documentation line inside a blockquote, no delivery, credit, or CSS change. This package documents the corrected candidate; the verdict lines under the stamp describe the file as judged, one line earlier.

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-JININ — frame target and credit author (landing 967ec2f, 2026-11-17).** `FIX-JININ.md` records two repairs, both in commit 967ec2f (pages: path-of-jinin frame and credit, rok-gov agency name). (1) The in-gate frame's `theme=` (candidate L24) was repointed from the nonexistent production `theme%3Apath-of-jinin/1` to the draft-host `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Apath-of-jinin-jp/1`, byte-identical to the head frame's line (L7); the priority=1 parameter and the frame include are untouched. (2) The 著作権者 field (L16) and license-box `author=` (L645) changed from the pointer form to `c_bonefish & thd-glasses`; Denevola's base-code credit stays in the exhibit banner. The earlier record items that flag the dead frame and the empty author field describe the as-built state; this candidate carries both repairs. T1 before/after identical (6/0/1).

## Change set outside the two diffed files

The diff covers two files; this theme's record is one file larger. `pages/theme-decoration-sample-path-of-jinin-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
