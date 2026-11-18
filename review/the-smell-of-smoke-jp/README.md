# Review package — theme:the-smell-of-smoke-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:the-smell-of-smoke-jp — origin EN, population #149 [GOSIGN2-LEDGER (b) row 149]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now a7abe60d4353de34db2f07a293c3b3f0bce1e800d19df863a43663aa08065b96); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 134; GOSIGN2-LEDGER (b) row 149]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow. [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 149, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 149]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 149]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:the-smell-of-smoke-jp.txt sha256:a7abe60d4353de34db2f07a293c3b3f0bce1e800d19df863a43663aa08065b96; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 149) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (class (ii), section 11); the render row's items (runtime chain, KB-40; credit-modal preview form and the 768px overflow, KB-32/KB-33 families); T4's pattern-5 pair (both draft-host images 404, KB-58) and its pattern-1 demo link (P1 posting-procedure class). The verdict stamp reads STALE because the candidate changed after the verdict in the usage-example sweep commit b5cb724 (section 12) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:the-smell-of-smoke | theme:the-smell-of-smoke-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10 (first translation; the candidate's credit block records 初訳時参照リビジョン: 10) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-the-smell-of-smoke.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:the-smell-of-smoke-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 572 lines / 10,335 bytes | 586 lines / 11,916 bytes |
| SHA-256 | a485cf2110baafb267bd3dbf5d81a7be3d04d15bf9d511d67ed940ed68c00b2d | a7abe60d4353de34db2f07a293c3b3f0bce1e800d19df863a43663aa08065b96 |

Wave history: the candidate descends from the canonical-sources import (d727e92) and the Phase 6 import of JP テーマ-tagged pages (b9b9884), was ported by the Stage 2 EN21 integration (dda4fd3, the LOCALIZE-S2-C wave), then touched by FIX-CREDIT-D (1869877) and the usage-example sweep (b5cb724, section 12). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A small EN theme whose original delivers from the head and whose port keeps that shape — the batch's clearest case of the campaign's fixed form for head-delivered themes: the head module stays (repointed, its double-slash URL typo normalized), an interwiki-style frame is added beside it at priority 1, and everything else is the standard classes. The credit conversion is the tidy version of the shape greatest-education fumbled: the original's two labeled module blocks ("Rating:" with a bare Rate; "Rating w/ Info Pane:" with an info pair) are deleted entire, labels included, and the preview credit block carries the base-code attribution (Denevola) inside its author field, with the banner translated to match. The font story is disclosed in the candidate itself, in a porter prose paragraph: the original loads Vollkorn SC but applies it to no element, and specifies no body font at all; the candidate keeps the load, adds Noto Sans JP, and appends a commented body rule that gives Japanese text a face. Measured churn (the generator's difflib count, autojunk off): +67/−58, 125 changed lines in 31 change blocks / 10 diff hunks; a GNU-diff count gives 112 changed lines (+63/−49). The two items for a reviewer's eye are T4's pattern-5 pair (both own-folder images 404 on the draft host, dispositioned KB-58) and one silent validity repair inside the code block, disclosed in section 9.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 31 change blocks — 12 specific (38.7%), 18 heuristic (58.1%), 1 residue (3.2%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 22 |
| COMMENT-TEXT | 13 |
| TRANSLATION-ANCHORED | 4 |
| DRAFT-HOST | 4 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication of the heuristic mass: the 18 heuristic blocks are documentation and exhibit translations (22 TRANS-UNANCHORED blocks in total across tiers) and the 13 COMMENT-TEXT blocks translating the code block's CSS comments; each was read against the mirror for this README, and none hides a structural change (section 8's census). The single EXHIBIT-RESTRUCTURE primary is an include repoint inside the exhibit region. The one residue block (two banner attribution lines) is in the appendix.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:the-smell-of-smoke-jp; original theme:the-smell-of-smoke on scp-wiki at reference revision 10; candidate `pages/theme:the-smell-of-smoke-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-C wave (sources.tsv kind: standard). Topology frame: the original delivers from the head — a module CSS (original L1–3) importing its own `local--code` block live, ahead of the tag gate at original L10 — and the candidate keeps the head delivery and adds a frame beside it (section 3). The gate's tag is localized (`+theme` → `+テーマ`, IFTAGS ×2 across the pair of gate lines).
- **Why:** Section 0 declares the provenance route and delivery frame; the gate tag is P2.
- **Verify:** The sources.tsv row for the-smell-of-smoke-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is two labeled blocks: a `[[>]]` "Rating:" block with a bare `[[module Rate]]`, and a `[[>]]` "Rating w/ Info Pane:" block with an info pair. The candidate deletes both blocks entire — module, pair, and labels (BARE-RATE-DEL, INFO-DEL) — and installs the preview credit block (candidate L14–23) with the eight ruling-3 fields: タイトル 煙の匂いテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 The Smell of Smoke Theme; 著作権者 `[[*user c_bonefish]]`（ベースコード: Denevola); 作成年 2022; 初訳時参照リビジョン 10; 元記事リンク https://scp-wiki.wikidot.com/theme:the-smell-of-smoke. The base-code attribution rides inside the author field itself, and the code banner is translated to match (candidate, in the code block): 制作： c_bonefish / ベースコード: Denevola, with the two background images' pixabay source URLs kept and the CC BY-SA 3.0 line carried. The source link names scp-wiki.wikidot.com, the host sources.tsv records for the original, in literal-colon form — the host check passes, so no probe was needed.
- **Why:** P3/T1 and ruling 3. The field-versus-banner check this package runs on every credit block passes here in both directions: the field names everyone the banner names, and the banner names no one the field drops.
- **Verify:** Read candidate L14–23 against the original's two blocks; the banner lines are the appendix's residue block (candidate L68–70 region).
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); no credit item is flagged for this theme.

### 2. Includes and components

- **What:** Live includes: the credit pair (section 1), the head interwiki-style frame (section 3), and the exhibit `component:image-block` include whose `name=` is repointed to the draft-host logo (candidate L33, INCLUDE-REPOINT). The escaped usage example (candidate L28) names `:scp-jp:theme:the-smell-of-smoke-jp` — the usage sweep's repair, section 12. The documentation's demo link `[[[theme:the-smell-of-smoke|訪問済みリンク]]]` is a link specimen, not an include (section 7). No component had to be ported alongside this theme; the COMPONENT-SWAP block is the info pair's deletion in the credit conversion.
- **Why:** P1 (KB-15): includes name the JP counterpart or the serving original.
- **Verify:** `grep -n '\[\[include' candidate.txt`.
- **Disposition:** Applied; no foreign include kept.

### 3. Delivery and code loading

- **What:** Dual head delivery. The original's head module (original L1–3) imported `https://scp-wiki.wikidot.com//local--code/theme:the-smell-of-smoke/1` — note the double slash, the original's own typo. The candidate keeps the module (candidate L1–3) repointed to the draft host's `local--code/theme%3Athe-smell-of-smoke-jp/1` with the double slash normalized away, and adds an interwiki-style frame at the head (candidate L5–9, priority=1) naming the same /1 — the campaign's fixed form for themes that keep a head module (the frame is what the Sigma-10 environment serves). Both delivery lines stand ahead of the gate (candidate L10), as the original's module stood ahead of its gate. Census check: exactly one `[[code]]` block (candidate L61), so both /1 addresses name the block that holds the CSS — correct.
- **Why:** P6/T3 (the frame) with the module retained because the original's topology delivers ahead of the gate; the draft-host form of the live lines is KB-41, class (iii).
- **Verify:** `grep -n 'local--code\|interwiki-style' candidate.txt`; count the `[[code]]` blocks (one).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** The font story is disclosed in the candidate's own prose, in a porter paragraph ahead of the code section: the theme uses Noto Sans JP for Japanese; Vollkorn SC comes from Google Fonts; Vollkorn SC is loaded by the original but applied to no element in the original's CSS and is kept as-is; the faces are SIL OFL 1.1. The import itself (candidate L76) is Vollkorn SC plus Noto Sans JP 400;700 from Google Fonts, with a porter CSS comment recording why the host changed (fonts.bunny.net は直リンクの特例外のため Google Fonts へ — bunny is outside the allowed hotlink set). One rule is appended to the code block with its own porter comment: `body { font-family: 'Noto Sans JP', sans-serif;}` （日本語フォールバック（原語版はフォントを指定しておらず、OS依存になるため）) — the original specifies no body font at all, so Japanese text was OS-dependent; this is the CSS-BODY block, adjudicated here as the P7 supplement for a fontless theme. Assets: `logo.png` (candidate L33) and the CSS `background.png` are repointed to the draft host's own folder; T4 probed both on sigma10-jp-test and both returned 404 (section 11).
- **Why:** P2/KB-17 (the bunny-to-Google host change) and P7 (a JP face loaded *and applied* — the appended body rule is what makes the load real, the mirror image of a loaded-but-unapplied flag). P5/KB-58 for the assets.
- **Verify:** Candidate L76 for the import; the prose paragraph and the appended body rule are at the code block's head and tail respectively.
- **Disposition:** Font load and supplement applied; the two asset URLs are DISPOSITIONED (KB-58, class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** This theme sets no `--header-title`/`--header-subtitle` overrides and touches no sidebar rules beyond the font lines of section 4. Its one `content:` string (candidate L101) is the original's own blank string, carried unchanged. The exhibit tab labels are translated （タブ1/タブ2) as part of the section 6 mass.
- **Why:** The honest statement for this section is the absence: no furniture variable was overridden, so no P9 question arises; the blank `content:` string is recorded because the standing check reads rendered strings, and this one is the original's by design.
- **Verify:** `grep -n -- '--header-title\|content:' candidate.txt` — the one blank string only.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The documentation and exhibits are translated throughout: 4 TRANSLATION-ANCHORED blocks, 22 TRANS-UNANCHORED blocks (one-line exhibit translations whose anchor test fails on mixed lines), and 13 COMMENT-TEXT blocks translating the code block's CSS comments. The banner is translated with its attribution intact (section 1). The font-disclosure prose paragraph of section 4 is porter-added body text, recorded there. English survives in the credit block's original-title field and in proper nouns.
- **Why:** P10 and KB-18. The unanchored group was read line by line against the mirror for this README, because it is where a silent deletion would hide.
- **Verify:** diff.md's body sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (section 1) names the recorded host. One prose link is repointed (LINK-REPOINT, block B6): the intro sentence's Factory link, an scp-wiki URL in the original, becomes the JP page form `[[[factory-hub|ザ・ファクトリー]]]` in the candidate — the JP hub page, which exists. The documentation's demo link `[[[theme:the-smell-of-smoke|訪問済みリンク]]]` keeps the original's plain form: it is a visited-link *specimen* inside the link exhibit, and T4's row names it (its "L47 demo link") under pattern 1 — the ledger dispositions it with the P1 posting-procedure class rather than as a live reference. It is recorded here so the plain form is not mistaken for a sweep miss: the sweep repaired the usage *include* (candidate L28), and the specimen is a different line by design.
- **Why:** P11 for the live repoint; the specimen's ground is the ledger's own P1 disposition (§(c3): P1 DISPOSITIONED, posting-procedure convention class).
- **Verify:** Candidate L24–25 region for the intro link; the demo link is in the link exhibit (candidate L46 region).
- **Disposition:** DISPOSITIONED (the specimen, P1 class); the repoint is applied.

### 8. Structure

- **What:** The localize.md closing rule holds. The code block keeps its position and size class (original L53–566 region → candidate L61–578), the gate wraps the page on both sides, and the JP additions arrive as the head frame (section 3), the font prose (section 4), and the appended body rule (section 4) — not interleaved into the inherited CSS. The one EXHIBIT-RESTRUCTURE primary adjudicates against the census: the tabview and its tabs, the image exhibits, the heading samples, and the code exhibit are present on both sides in the same order; the block is an include repoint inside the exhibit region, so no exhibit was restructured or dropped.
- **Why:** R3 forces the adjudication; the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** No WS-ONLY block and no pure re-indent block (reindent_blocks 0). One semantic micro-repair rides inside the code block and is disclosed here rather than as formatting: the original's `.creditButton p a { border-left: 1px #000!important;}` lacks the border style keyword, so browsers drop the declaration; the candidate reads `border-left: 1px solid #000!important;`. The repair changes what renders (the credit button gains its intended left border) and is recorded for that reason.
- **Why:** R7's disclosure rule, extended to the one-character repair class: a fix inside inherited CSS is part of the change record even when it is obviously right.
- **Verify:** `grep -n 'creditButton' candidate.txt original.txt` — the two forms of the declaration.
- **Disposition:** Standing (disclosed repair).

### 10. Porter annotations

- **What:** Two annotations, both in the font area: the prose disclosure paragraph ahead of the code section (section 4), and the CSS comment on the appended body rule （日本語フォールバック（原語版はフォントを指定しておらず、OS依存になるため）), plus the host-change comment on the font import (fonts.bunny.net は直リンクの特例外のため Google Fonts へ). The skeleton's per-section text does not list them because they ride inside the JPFONT-LOAD and CSS-BODY blocks; they are recorded here from the bytes.
- **Why:** R2: porter-added text is part of the change record, and these comments are the only in-file explanation of the font decisions.
- **Verify:** The code block's head (candidate L76 region) and tail.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items. (1) T1's three pseudo-ref errors: class (ii), posting-procedure — the candidate's draft-host delivery and asset lines (sections 3–4). (2) The render row's items: the page's runtime-hotlink site-theme chain only (KB-40, environment layer); on the sample, the credit modal in preview form (KB-32 family — the JP preview module has no modal, by design) and an 884px overflow at 768 (KB-33/KB-34 family). (3) T4 row 149, display-affecting 2: the pattern-5 pair — both images the draft references (the example `logo.png` and the CSS `background.png`) returned 404 on sigma10-jp-test — and the pattern-1 demo link of section 7. The ledger's §(c3) line dispositions P1 (posting-procedure class) and P5 (class (ii) / KB-58) for this theme. No item in this package is flagged beyond the ledger's own record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 134): exit 1, 3 errors / 1 warn / 1 info; all three errors are pseudo-ref, class (ii); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-D (EN21)): FINDINGS — the items of section 11(2); coverage as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 149): FINDINGS jointly, display-affecting findings 2 (the pattern-5 pair). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares; the stamp reads STALE because the candidate's only post-verdict change is the usage sweep's commit b5cb724 (the include line of section 2). Counts in this README are the generator's (difflib, autojunk off): +67/−58 in 31 change blocks / 10 diff hunks; the GNU-diff count of the same pair is 112 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result.
- **Verify:** Re-run the checker on `pages/theme:the-smell-of-smoke-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 149; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The font disclosure is part of the candidate

Most ports in this batch make their font decisions silently and leave the README to reconstruct them. This candidate instead carries a prose paragraph ahead of its code section explaining the font situation (the original loads a display face it never applies; Japanese had no face at all), and comments both the import's host change and the appended body rule. A reviewer comparing the two files should read that paragraph first: it is the porter's own §4, and this package's section 4 follows it because the bytes agree with it — the import (candidate L76) loads exactly the faces the paragraph names, and the appended body rule applies the JP face the paragraph promises. Where a candidate documents itself accurately, the review package's job is to verify the documentation, which was done line by line; where it does not (the batch has both kinds), the package says so instead.

## Appendix — residue blocks

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B18 | L60–62 | L68–70 | The code banner's background-image attribution lines, translated with the pixabay URLs kept (R1; section 1) |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-the-smell-of-smoke-jp.txt` is the decoration sample the render checks ran against (it includes this candidate), and its findings are the sample half of section 11(2). It belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** The Smell Of Smoke CSS Theme
- **Author:** c_bonefish（ベースコード: Denevola）
- **Source:** https://scp-wiki.wikidot.com/theme:the-smell-of-smoke — revision 10
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
