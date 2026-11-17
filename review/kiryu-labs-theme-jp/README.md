# Review package — theme:kiryu-labs-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:kiryu-labs-theme-jp — origin EN, population #104 [GOSIGN2-LEDGER (b) row 104]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 01c72c4c65e02882d4ef97fa5a9ef883d9b907d3c8ea97d63adf6127b7bf6fa0); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 0 warns / 1 info (hotlink×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 94; GOSIGN2-LEDGER (b) row 104]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — notice clip ≤375 + 768px sidebar×notice + WebKit CC "S" (all cross-cutting); sample 884px@768 static-credit-replica overflow; webkit `url-https` 404 = shared artifact; no candidate-CSS defect. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 104, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 104]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 104]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:kiryu-labs-theme-jp.txt sha256:01c72c4c65e02882d4ef97fa5a9ef883d9b907d3c8ea97d63adf6127b7bf6fa0; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 104) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×2 (the EN-storage backgrounds, class (ii) / KB-58, section 4); the render row's cross-cutting items (KB-33/36, section 11) |
| **Defect flag (this package)** | **The credit block's author field contradicts the theme's own banner, and the ledger's "FIXED" for it is not borne out by the bytes.** The original's CSS banner reads "Created by rounderhouse." (original L29), the candidate carries the same banner (candidate L38), and the localize lane verified the author at revision 0 as Rounderhouse (LOCALIZE-ROWS row 104, item (a)) — but the candidate's 著作権者 field reads 作者不明（Kiryu Labs ハブ向けのテーマ） ("author unknown"), dropping the named creator. The only credit-wave commit touching this file (1869877, FIX-CREDIT-D) changed the translator field alone (its report's row for this theme reads "SCP-JP → AI"), so the field stands as the port left it. Section 1 gives both sides' exact text. The package is written against the candidate as it stands; the repair (著作権者: Rounderhouse, the form the campaign's other credit repairs take) is the coordinator's to land |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:kiryu-labs-theme | theme:kiryu-labs-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 29 (first translation; the candidate's credit block records 初訳時参照リビジョン: 29) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-kiryu-labs-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:kiryu-labs-theme-jp.txt`, copied at worktree HEAD 590eedf |
| Lines / bytes | 249 lines / 5,080 bytes | 260 lines / 5,756 bytes |
| SHA-256 | 24fc7afcb4431d8d56d0c99bfe54fe2b23e3b36e97a1d5ee9da67ee8b35c9a6 | d377cb73864b1e83ed7e3b7d9150c27b07f46defe48cadb01fd743458f66fd33 |

Wave history: the candidate was created by the Stage 2 EN12 integration (commit 7604057, the LOCALIZE-S2-B wave's port), normalized by FIX-CREDIT-D (commit 1869877, translator field only for this file), and touched once more by the usage-reference sweep (commit b5cb724: the usage exhibit's self-reference repaired to the -jp posting name, one line). No FIX5 commit touches this file.

## Summary

The smallest theme in this batch (249 lines) and the one with its sharpest record problem, flagged in the Status table and section 1: everything else about the port is the standard shape in miniature. Measured churn (diff.md, Tier 1 format; the generator's difflib count with autojunk off: +46/−35, 81 changed lines in 26 change blocks, presented as 11 hunks). Fourteen of the 26 blocks are whitespace-only; the semantic core is the credit block's installation, one font-stack supplement, the usage exhibit's self-reference (repaired by the sweep), and the two kept EN-storage background lines. The exhibits are minimal (the theme's page is mostly its code exhibit), so the translation mass is the smallest in the batch.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 26 change blocks — 24 specific (92%), 1 heuristic (4%), 1 residue (4%), 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| WS-ONLY | 14 |
| COLON-ENC | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-STACK | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| TRANSLATION-ANCHORED | 1 |

Adjudication for this README: the two COLON-ENC blocks are the usage exhibit's colon-encoded self-reference lines (the sweep's repair site, section 2); the one residue block is the code exhibit's collapsible closer (appendix). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:kiryu-labs-theme-jp; original theme:kiryu-labs-theme on scp-wiki at reference revision 29; candidate `pages/theme:kiryu-labs-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart). The frame is the standard candidate form in miniature: a head module importing the candidate's own delivery, the interwiki-style frame, and the tag gate localized to `+テーマ`.
- **Why:** Section 0 declares the provenance route; the gate tag is P2 and the frame is P6 (section 3).
- **Verify:** The sources.tsv row for kiryu-labs-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is its CSS banner, carried at the head of its code exhibit (original L27–32): "Created by rounderhouse. Based on SCP Sigma 9 Theme created by Aelanna and Dr Devan, and Wilson's Wildlife Solutions theme by Stormbreath. Built for Zyn, #ARTEXCHANGE2019". The candidate installs the JP credit block (`:scp-jp:credit:start-preview`/`end-preview`, candidate L11–21) with the eight ruling-3 fields: タイトル Kiryu Labs Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Kiryu Labs Theme; 著作権者 作者不明（Kiryu Labs ハブ向けのテーマ）; 作成年 2019; 初訳時参照リビジョン 29; 元記事リンク the scp-wiki original, on the recorded host. **The author field is wrong, on the campaign's own evidence.** The banner (which the candidate itself carries verbatim at candidate L38) names rounderhouse as the theme's creator; the localize lane verified the authorship at the original's revision 0 and charged exactly this ("P3 wrong 著作権者 (rev0-verified Rounderhouse; candidate itself carries 'Created by rounderhouse.' — internal contradiction)", LOCALIZE-ROWS row 104 item (a)). The ledger's §(c3) line records "P3 credit fields FIXED (credit waves; checker-verified)", but the bytes do not bear that out for the author field: the only credit-wave commit touching this file is FIX-CREDIT-D (1869877), whose own report records this theme's edit as the translator-field normalization ("SCP-JP → AI"), and the field has read 作者不明 since the port's first commit. The banner's other names (Aelanna, Dr Devan, Stormbreath) are base-theme credits, not this theme's authors, and are not what the field should carry; the field should read Rounderhouse, the form the campaign's other credit repairs take (a dropped creator restored to the field). This README follows the bytes and the lane's verification over the ledger's summary word, and flags the item in the Status table and the batch report; the package is otherwise written against the candidate as it stands, and the stamp above (generated from the ledger) is left as generated.
- **Why:** P3/T1 and ruling 3: the credit block is the attribution of record, and an "author unknown" that contradicts the work's own banner fails the check the field exists to pass. The checker's verification covers field presence and form; authorship truth is a byte-level judgement, which is why this package, not the checker, is where the contradiction surfaces.
- **Verify:** `sed -n '27,32p' original.txt` (the banner) against the credit block at candidate L11–21; `git show 1869877 -- pages/theme:kiryu-labs-theme-jp.txt` shows the translator field as that wave's only credit edit to this file.
- **Disposition:** **FLAGGED** (the ledger records FIXED; the bytes show the author field unrepaired. The P5 half of the row is DISPOSITIONED, section 4).

### 2. Includes and components

- **What:** The candidate's includes are the credit pair (section 1) and the interwiki-style frame (section 3); the theme's page carries almost no exhibit includes. One include-shaped line matters: the usage exhibit's self-reference, which the population sweep repaired after the verdict waves (commit b5cb724): `@@[[include :scp-jp:theme:kiryu-labs-theme]]@@` → `@@[[include :scp-jp:theme:kiryu-labs-theme-jp]]@@` — the exhibit had named a page that will not exist at posting, and the sweep's convention (self-references take the -jp posting name) repaired it. The classifier's two COLON-ENC blocks are this exhibit's colon-encoded reference lines.
- **Why:** P1 (KB-15) for the live includes; the sweep's repair is the campaign's self-reference convention (a usage example must name a page that resolves at posting).
- **Verify:** `grep -n '\[\[include' candidate.txt`; `git show b5cb724 -- pages/theme:kiryu-labs-theme-jp.txt` for the one-line repair.
- **Disposition:** Applied (the sweep repair is inside the current bytes and the stamp's hash).

### 3. Delivery and code loading

- **What:** The standard candidate form: the head module imports the candidate's own `local--code/theme%3Akiryu-labs-theme-jp/1` from the draft host, and the interwiki-style frame names the same /1 delivery (the SELF-DELIVERY and DRAFT-HOST spans at the head). The original's own delivery lines are replaced by these.
- **Why:** P4/T9 and P6/T3. The draft-host form is KB-41, class (iii), and it is T1's one pseudo-ref error for this theme.
- **Verify:** `grep -n 'local--code' candidate.txt` — the head pair, both draft host.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts (one JPFONT-STACK block): one stack gains the JP supplement in place; the theme's typography otherwise rides on its base, and no JP font load is added. Assets: two lines stay on EN storage, and they are exactly T1's hotlink×2 — the body background `kiryubody.png` (candidate L74) and the header background `kiryulabs.png` (candidate L105), both `scp-wiki.wdfiles.com/local--files/theme%3Akiryu-labs-theme/`. These are the localize row's P5 item ("EN-storage backgrounds, display-affecting").
- **Why:** P7/T5 with KB-16 for the stack. The assets are P5/KB-17 territory dispositioned instead: class (ii), KB-58 — re-hosting is a posting-procedure step and the files serve from the original's storage today.
- **Verify:** `grep -n 'scp-wiki.wdfiles' candidate.txt` — the two lines above.
- **Disposition:** Font supplement applied; the two asset lines DISPOSITIONED (class (ii) / KB-58, GOSIGN2-LEDGER §(c3): P5 DISPOSITIONED).

### 5. Header, sidebar, and site furniture

- **What:** None recorded: the candidate sets no header variables of its own beyond the original's CSS (its title recolor rules are the original's, carried in the code exhibit), and T4 recorded no P9 item for this theme — its two items are the credit field (section 1) and the backgrounds (section 4).
- **Why:** P9/T6 not engaged.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` returns nothing.
- **Disposition:** None required.

### 6. Text translation

- **What:** The smallest translation mass in the batch (one anchored block, one unanchored): the usage lead-in ("このテーマを自分のページに適用するには:", candidate L23) and the short prose around it. The theme's page is its code exhibit and its banner; the banner is the author's own English, carried verbatim (and it is the evidence in section 1, which is a further reason it stays untouched).
- **Why:** P10 and KB-18 (reader-visible strings); the banner is porter-facing attribution text, carried as found.
- **Verify:** diff.md's hunks in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link names the recorded host (scp-wiki.wikidot.com, candidate L20). The usage exhibit's self-reference is section 2's repaired line. No other prose link stands in the candidate, and no P11 item was charged.
- **Why:** P11 satisfied.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the credit link.
- **Disposition:** Standing.

### 8. Structure

- **What:** No structural change: the page's parts (head frame, credit area, usage, code exhibit) correspond one-to-one, the classifier records no EXHIBIT-RESTRUCTURE block, and the code exhibit is carried at 227 lines against the original's 226 (the delta is the head lines of sections 3–4). The candidate wraps its exhibit in a collapsible whose closer is the residue block (appendix).
- **Why:** R3 satisfied by the census; no sanction question arises.
- **Verify:** The topology components in classification.json (original code-css 226 lines; candidate 227).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** 14 whitespace-only blocks — the majority of this small diff — blank-line deltas around the head, the credit area, and the exhibit. No re-indentation class is recorded. The count is disclosed so a follow-up diff's padding churn is recognizable against it (R7): on a 26-block diff, 14 blocks of padding is the difference between a quiet file and an apparently busy one.
- **Why:** R7: formatting churn is disclosed as its own class so it is never mistaken for semantic change.
- **Verify:** The classification's section 9 counts (WS-ONLY 14, re-indentation 0).
- **Disposition:** Standing (disclosed; no semantic content).

### 10. Porter annotations

- **What:** None — checked, absent. The candidate carries no `[!-- ... --]` notes and no port provenance comment. (Its one English comment text is the original author's banner, section 1, which is evidence, not annotation.)
- **Why:** R2: porter-added text is part of the change record; here the porter added none in-file.
- **Verify:** `grep -n 'SCP-JP port\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's two hotlink errors and one pseudo-ref: the hotlinks are the background set of section 4, class (ii) / KB-58; the pseudo-ref is the candidate's own draft-host local--code line (section 3), class (ii) posting-procedure. There is no class (i) error. (2) T4's two items: the P3 credit field, recorded FIXED in the ledger but flagged in section 1 as unrepaired in the bytes (the one item in this package where the record and the bytes part company); and the P5 backgrounds, DISPOSITIONED. (3) The render row's items, all cross-cutting, not charged to the candidate: the notice clip at ≤375 and the 768px sidebar×notice shape (KB-34 family), the WebKit CC "S" glyph (KB-36), the sample's 884px@768 static-credit-replica overflow (KB-33), and a webkit `url-https` 404 the row itself attributes to the shared migration artifact (the draft-host addressing form, posting-time rewrite class). The row's closing assessment is recorded in the stamp's source: no candidate-CSS defect.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission — and where a recorded disposition does not match the bytes, this package says so (item 2) rather than repeating it.
- **Verify:** Each item names its deciding record above; item 2's ground is section 1's byte comparison.
- **Disposition:** DISPOSITIONED (items 1 and 3); item 2 is split as stated (P5 DISPOSITIONED; P3 FLAGGED).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 94): exit 1, 3 errors / 0 warns / 1 info; two hotlink (the section 4 backgrounds) and one pseudo-ref, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-B (EN12)): FINDINGS, the items of section 11(3), all dispositioned, with the lane's own closing assessment that no candidate-CSS defect stands; engine coverage full matrix as run by the lane; no credit-modal line is recorded for this theme. (c) T4/T5 (LOCALIZE-ROWS row 104): FINDINGS jointly, display-affecting findings 1 (the P5 backgrounds; the P3 item is a field defect, counted separately in the row's text); the ledger §(c3) line records P3 FIXED and P5 DISPOSITIONED — and section 1 of this README documents, with the commit-level evidence, that the P3 half of that line is not borne out by the current bytes. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +46/−35 in 26 change blocks, presented as 11 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result — including, here, the one place where the deciding check (the bytes) overrules the summary record.
- **Verify:** Re-run the checker on `pages/theme:kiryu-labs-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 104; go-sign, COMPLETION-REPORT §10) — with the section 1 flag standing against the credit field, not against the verdict's other parts.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-kiryu-labs-theme-jp.txt` is the decoration sample the render checks ran against (its 884px@768 overflow is in section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The usage-reference sweep (b5cb724) touched 157 candidate files; the other 156 are those themes' own records. The FIX-CREDIT-D commit (1869877) touched 163 files in one wave; the other 162 are those themes' own records, not this one's change set. There are no companion fragments.

## Appendix — residue and low-signal blocks

Class M treatment: the residue collapses into this table rather than per-block slots.

| Block(s) | Shape | Resolution |
|---|---|---|
| B26 (residue) | One added line at candidate L258–259: `[[/collapsible]]`, the closer of the collapsible wrapping the candidate's code exhibit (its opener aligned as context earlier in the exhibit) | A wrapper line, not content; counted here so the residue count is zero after adjudication |
