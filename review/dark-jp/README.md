# Review package — theme:dark-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:dark-jp — origin EN, population #75 [GOSIGN2-LEDGER (b) row 75]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 75]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 2 warns / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 75; GOSIGN2-LEDGER (b) row 75]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 runtime-hotlink + dark credit-modal heading contrast-credit 1.46 faint-gray-on-gray (chromium verified); notice clip ≤375 and sidebar×notice at 768 are shared preview chrome; 884px@768 sample overflow. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 75, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 75]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 75]
- Computed against: canonical commit 666f54356acb463c56016c967dc52464b25ba4a2; candidate file pages/theme:dark-jp.txt sha256:8a57a9731dc78c6fd1a0cff752de2c8beaef789cee7de57ca05885ed21823435; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 75) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×4 (class (ii), section 11); the render row's items (KB-40 / KB-32 / KB-33+KB-34, section 11); T4's P1 (posting-procedure convention class, section 11). The credit fields the localize lane found missing were **FIXED** by the credit waves after its row was written |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:dark | theme:dark-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 5 (first translation; the candidate's credit block records 初訳時参照リビジョン: 5) | — |
| Source of this copy | Mirror store, class COPY (hash-verified against review/sources.tsv) | Canonical file `pages/theme:dark-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 378 lines / 6,971 bytes | 377 lines / 7,434 bytes |
| SHA-256 | 08e8b08f4e53dde268d89ed9d065a40df5931dec08d3957528e3cfaf26959799 | 8a57a9731dc78c6fd1a0cff752de2c8beaef789cee7de57ca05885ed21823435 |

Wave history: the candidate was created in the Stage 2 EN wave (its render lane was RENDER-S2-B (EN7), its localize lane LOCALIZE-S2-C) and last touched by FIX-CREDIT-C (commit 5c32672, "complete translator pair in rows 1-22 credit blocks"), which completed the credit block after the localize lane had found its fields missing. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The smallest port in this batch: a Sigma-9 dark-mode variant whose original and candidate are nearly the same length (378 → 377 lines), and whose changes are the standard JP furniture swap plus translation. The head frame's delivery moves from the EN wdfiles host to the draft host; the interwiki-style include drops its `:scp-wiki:` prefix to the bare working form; the credit block is installed in preview form with the eight ruling-3 fields (completed by FIX-CREDIT-C after the localize lane's row); the original's info module furniture is deleted while its prose survives translated; four asset references move to the draft host; and the body prose and exhibits are translated line by line. Two adjudications matter: the usage example at candidate L25 already names `theme:dark-jp`, the correct posting form (the batch's defect flag does not touch this theme), and the classifier's one EXHIBIT-RESTRUCTURE label is a false fire on an include repoint inside the credit block (section 2). Measured churn (diff.md: +36/−37, 73 changed lines in 19 change blocks / 4 diff sections).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 19 change blocks — 10 specific (52.6%), 8 heuristic (42.1%), 1 residue by tier (5.3%; five blocks carry the residue label in total, four of them tiered), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 12 |
| DRAFT-HOST | 5 |
| DELIVERY-HOST | 2 |
| SELF-DELIVERY | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| INCLUDE-REPOINT | 1 |
| BARE-RATE-DEL | 1 |
| IFTAGS | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| INFO-DEL | 1 |
| TRANSLATION-ANCHORED | 1 |
| LINK-REPOINT | 1 |

Adjudication for this README (every block was read against the bytes): the heuristic share is the one-line exhibit translations of section 6, which is what class M expects for a prose-light theme. The residue blocks (B13, B15, B16, B17, and tier-None B7) are adjudicated in the appendix table: three are one-line translations, one is a P11 link repoint, and B7 is a component include repoint with its image re-host. The EXHIBIT-RESTRUCTURE label (inside B2) is a false fire: the block's exhibit-region line is the interwiki-style include losing its `:scp-wiki:` prefix, a P1 repoint, and the exhibit census of section 8 shows no restructuring. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:dark-jp; original theme:dark on scp-wiki at reference revision 5; candidate `pages/theme:dark-jp.txt`. Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; no production JP counterpart, so the R4 adoption question does not arise). The original's tag gate (original L10) and the candidate's (candidate L10) both sit directly under the frame; the gate tag is localized (+テーマ, section 3's IFTAGS pair).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline.
- **Verify:** The sources.tsv row for dark-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The candidate installs the preview credit block at candidate L12–21 with bare includes (`[[include credit:start-preview]]`), carrying the eight ruling-3 fields: title Sigma-10 Dark Mode; 翻訳責任者 AI; 翻訳年 2026; 原題 Sigma-10 Dark Mode; 著作権者 stormbreath; 作成年 2023; 初訳時参照リビジョン 5; the source link (candidate L20) naming scp-wiki.wikidot.com — the original's recorded host. The original's own credit furniture was the info module pair deleted in section 8's B6 plus its prose; no T7 credit-module CSS supplement exists in this theme (no `.creditRate` rules on either side). Historical note, prose against bytes: the localize lane's row (LOCALIZE-ROWS row 75) records the credit fields as missing and charges it display-affecting; that was the state when the lane read the file. FIX-CREDIT-C (commit 5c32672) completed the block afterwards, and the bytes above are the current state — the ledger's (c3) outcome for this theme records P3 as FIXED.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form. Ruling 3 fixes the eight fields; the bare include form is the campaign's settled working form (AGENTS.md §5: the `:scp-jp:`-prefixed credit include does not resolve in the test environment, so the bare form is used and the prefixed form is a posting-procedure item).
- **Verify:** Read candidate L12–21 against the eight fields; `grep -n 'credit:' candidate.txt`.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 FIXED; P1 DISPOSITIONED, section 11).

### 2. Includes and components

- **What:** Three repoints, all P1. The interwiki-style include (original L5 `:scp-wiki:component:interwiki-style` → candidate L5, bare `component:interwiki-style`) — the AGENTS.md §5 working form for this include. The image-block include inside the usage body (original L44 `:scp-wiki:` → candidate L30 `:scp-jp:component:image-block`), with its image name re-hosted in the same block (B7, section 4). The credit pair (section 1). The usage example (candidate L25) reads `@@[[include theme:dark-jp]]@@` — the correct posting name, so the batch's usage-example defect does not apply here. The classifier's EXHIBIT-RESTRUCTURE labels sit on blocks whose exhibit-region lines are include repoints (the interwiki-style line inside B2, and one exhibit include); adjudicated as repoints, not restructuring (section 8's census).
- **Why:** P1 (KB-15): a live include naming the branch wiki resolves only while that wiki serves the component; the JP form is the posting target.
- **Verify:** `grep -n '\[\[include' candidate.txt` — no `:scp-wiki:` include remains.
- **Disposition:** Applied; P1 DISPOSITIONED at the ledger (posting-procedure convention class, GOSIGN2-LEDGER §(c3)).

### 3. Delivery and code loading

- **What:** The theme's CSS is inline in a `[[module CSS]]` on both sides (no code block, no local--code delivery). The frame's one delivery line moves hosts: original L2 imports `theme%3Adark/1` from scp-wiki.wdfiles.com; candidate L2 imports `theme%3Adark-jp/1` from the draft host — the page's own stylesheet module under its JP name (SELF-DELIVERY ×2; the B3 line is the sidebar asset of section 4). The interwiki-style frame (candidate L5–7) names the same /1 delivery.
- **Why:** P4/T9 and P6/T3. The draft-host form is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'wdfiles' candidate.txt` — only draft-host lines remain.
- **Disposition:** DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts: none — neither side declares a `font-family` (0 lines in each file); the theme inherits (the T5-absent shape). Assets: four references move to the draft host's `local--files/theme%3Adark-jp/` folder: the sidebar asset URL (candidate L64, B3), the image-block exhibit's image name (candidate L31, B7), and the two CSS background images bodydark.png (candidate L166, B18) and headerdark.png (candidate L182, B19), file names unchanged. Both are the theme's own background images, carried over with only the host changed.
- **Why:** P5 with KB-17 (asset hosts): the theme's own images are re-hosted to the JP side; the draft-host form is the class (iii) draft stage of that move.
- **Verify:** `grep -n 'local--files\|wdfiles' candidate.txt` — the lines above, all draft-host.
- **Disposition:** DISPOSITIONED (class (ii)/(iii) posting-procedure family).

### 5. Header, sidebar, and site furniture

- **What:** None — the theme sets no `--header-title`, `--header-subtitle`, or `--logo-image` on either side (checked; it is a body-class dark variant that recolors the standard Sigma-9 furniture, and its CSS body is carried over inside the inline module with only the section-4 asset lines changed). No P8 layout adaptation was needed.
- **Why:** P9/T6 do not engage where the original sets no variables; recording the absence is the check.
- **Verify:** `grep -n -- '--header-\|--logo' original.txt candidate.txt` — no hits on either side.
- **Disposition:** Standing (checked, absent).

### 6. Text translation

- **What:** The prose body and exhibits are translated throughout; the counted blocks are twelve TRANS-UNANCHORED one-line translations (usage text, exhibit headings and specimens, the sidebar greeting specimen 「やあ、…」, the dark-mode specimen strings) plus the info-module prose of B6, which survives translated after its module furniture is deleted (section 8). In-CSS comments (R1): the CSS carries no prose comments on either side. The usage instructions are translated and their code specimens kept (candidate L24–25 region: the `[[body class="dark"]]`-style instructions and the include example of section 2).
- **Why:** P10 (body and usage translation); KB-18 for the reader-visible specimen strings.
- **Verify:** A CJK scan of candidate.txt outside the credit block's 原題 field returns only translated text; spot-read candidate L60–90 against original L72–102.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L20) names scp-wiki.wikidot.com, the original's recorded host — the host check passes. One prose repoint: the visited-link exhibit's target moves from the original page to the JP page (original L66 `[[[theme:dark|A visited link.]]]` → candidate L65 `[[[theme:dark-jp|訪問済みリンク。]]]`, B16), so the exhibit demonstrates the link styling against the page a JP reader would actually visit. No hub or tag links exist in this theme to repoint.
- **Why:** P11: prose links take the JP counterpart or the serving original.
- **Verify:** `grep -n 'wikidot.com\|\[\[\[' candidate.txt` — the source link and the exhibit target above.
- **Disposition:** Standing; no dead link.

### 8. Structure

- **What:** The closing rule holds: selectors, rule order, and variable names inside the CSS are preserved; the only deletions are furniture. The info module pair (original L27–39, B6, INFO-DEL) is deleted as a standalone block while its prose survives translated — the preview credit block of section 1 is the theme's credit form, and a kept info pair would duplicate it. Exhibit census (R3): the original's exhibits (usage specimens, the image-block example, the link specimens) all survive in the candidate in the same order; nothing was dropped, replaced, or merged, so the EXHIBIT-RESTRUCTURE labels are discharged as the section-2 repoints they actually are.
- **Why:** R3 forces the census because a restructure and a deletion share a diff shape.
- **Verify:** Compare the exhibit sequence in original.txt L40–200 against candidate.txt L28–190.
- **Disposition:** Standing; no structural deletion beyond the recorded furniture swap, no class I item.

### 9. Formatting only

- **What:** None — the classifier finds no whitespace-only block pair and no re-indentation (0 and 0); the near-equal line counts (378 → 377) match the furniture-for-furniture shape of the port.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The summary counts in classification.json (`reindent_blocks: 0`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — the candidate carries no `[!-- ... --]` translator notes, no editor line, and no CSS comment without an original counterpart (checked explicitly).
- **Why:** R2: porter-added text is part of the change record; its absence is recorded so a reviewer does not have to wonder whether it was checked.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's four pseudo-ref errors: class (ii), posting-procedure — they are the candidate's draft-host delivery and asset lines (sections 3–4), rewritten to the production host at posting. (2) The render row's items, all environment or preview layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample credit-modal heading's contrast-credit 1.46 (KB-32: the preview form renders its heading in the theme's own palette); the notice clip at ≤375px and the sidebar×notice overlap at 768px, and the sample's 884px@768 overflow (KB-33/KB-34 cross-cutting families). (3) T4's P1: DISPOSITIONED under the posting-procedure convention class (GOSIGN2-LEDGER §(c3)) — the include-form items of sections 1–2 are the settled working forms, with the prefixed forms applied by the posting procedure.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above and in the verdict stamp.
- **Disposition:** DISPOSITIONED (items 1–3); P3 FIXED (section 1).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 75): exit 1, 4 errors / 2 warns / 1 info; all four errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-B (EN7)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 75): FINDINGS jointly, display-affecting findings 2 — both describe the localize-time state (credit prefix absent, credit fields missing) and both were closed by the credit waves before the ledger determination; the current bytes are section 1's. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +36/−37 in 19 change blocks / 4 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:dark-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 75; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks adjudicated

| Block | Original → candidate | Adjudication |
|---|---|---|
| B7 (tier None) | L44–45 → L30–31 | P1 include repoint (`:scp-wiki:` → `:scp-jp:` image-block) with its image name re-hosted to the draft host (section 2/4) |
| B13 | L79–80 → L49 area | One-line translation (sidebar greeting specimen 「やあ」, candidate L49) |
| B15 | L92 → L80 | One-line translation (sidebar specimen caption) |
| B16 | L66 → L65 | P11 link repoint: the visited-link exhibit target becomes theme:dark-jp (section 7) |
| B17 | L156 → L144 | One-line translation (dark-mode specimen string) |

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-dark-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Sigma-10 Dark Mode
- **Author:** stormbreath
- **Source:** https://scp-wiki.wikidot.com/theme:dark — revision 5
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
