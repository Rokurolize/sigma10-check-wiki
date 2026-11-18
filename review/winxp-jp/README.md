# Review package — theme:winxp-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:winxp-jp — origin CN, population #246 [GOSIGN2-LEDGER (b) row 246]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now bcf1f7fc416c7f1f3331a5bacf8254ab58330c16db38809ba846e40b7cb8b513); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 9 errors / 2 warns / 1 info (hotlink×8, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 211; GOSIGN2-LEDGER (b) row 246]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + candidate hosts scpsandboxcn.wdfiles.com, scpsandboxcn.wikidot.com; sample credit-modal (preview-form) + runtime-hotlink incl. scp-wiki-cn.wdfiles.com; T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN17)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN17)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 245, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 245]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 246]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:winxp-jp.txt sha256:bcf1f7fc416c7f1f3331a5bacf8254ab58330c16db38809ba846e40b7cb8b513; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 246) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×8 + pseudo-ref ×1 (class (ii), section 11); the render row's items (credit-modal preview form, KB-32; runtime chain incl. sandbox hosts, KB-40 / class (ii)); T4 display-affecting 1. The verdict stamp reads STALE because the candidate changed after the verdict in the usage-example sweep commit b5cb724 (section 12) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:winxp | theme:winxp-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 4 (first translation; the candidate's credit block records 初訳時参照リビジョン: 4) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-winxp.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:winxp-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 1,947 lines / 54,925 bytes | 1,984 lines / 90,265 bytes |
| SHA-256 | f1e2d198987913f768987e7a0077634cad924ac2d4e320b929f0863ea501a7bc | bcf1f7fc416c7f1f3331a5bacf8254ab58330c16db38809ba846e40b7cb8b513 |

Wave history: the candidate was created by the Stage 2 CN17 integration (2e202fc, the LOCALIZE-S2-E wave's port), then touched by rework2-p5 (b89741d — the Sigma-9 base family and small-embeds wave over 11 pairs; the Bauhaus inlining of section 4 is its shape), by FIX-CREDIT-D (1869877), and by the usage-example sweep (b5cb724). Provenance note (sources.tsv, class K5a-i): the original is recorded as superseded upstream since the reference revision, with a follow-up diff artifact in the campaign record — that artifact's actual content is reported in section 12, because it does not say what the note implies. The candidate's byte growth (+35 KB over the original at nearly equal line count) is the inlined base64 font of section 4, not added prose.

## Summary

A Windows XP theme whose documentation is small (some 116 lines) and whose CSS is an 1,800-line Sigma-9-derived block carried nearly verbatim — which is why this large file has the batch's second-smallest churn: +103/−71, 174 changed lines in 42 change blocks / 5 diff sections (GNU diff: 145, +91/−54). The port's real work is at the delivery edges: the original's head module is removed and the block is delivered from the tail in the campaign's form; and the Bauhaus display face, which the original imported as a stylesheet from a jsdelivr GitHub mirror, is *inlined* into the candidate as the two `@font-face` blocks that stylesheet contained — base64 woff and all, with the font file's own 2013 Font Squirrel comment carried along. The other imports (the same repo's colstyle stylesheet, kept verbatim under KB-14; the Nanum earlyaccess faces; Font Awesome from BootstrapCDN) are the original's own and stay. No item in this package is flagged: the credit check passes, the census holds, no JP font is loaded or needed (the design's faces are the XP system set), and the one typo in a font stack (`san-serif`) is the original's own, carried faithfully and recorded so nobody "fixes" the record instead of the theme. Two micro-facts are disclosed in the per-theme record: a silent http→https repair on a sandbox asset, and the `@charset` line's benign displacement by the inlining.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 42 change blocks — 22 specific (52.4%), 19 heuristic (45.2%), 1 residue (2.4%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 18 |
| TRANSLATION-ANCHORED | 18 |
| CSS-BODY | 3 |
| GLYPH-FORM | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| INCLUDE-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication of the heuristic mass: the 19 heuristic blocks are the documentation's in-fiction prose translations (18 unanchored blocks across tiers) and the CSS-BODY blocks inside the carried Sigma-9 CSS. The single EXHIBIT-RESTRUCTURE primary is a repoint inside the exhibit region (section 8). The one residue block (the code-head import region) is in the appendix.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:winxp-jp; original theme:winxp on scp-wiki-cn at reference revision 4; candidate `pages/theme:winxp-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard, with the K5a-i note of the Provenance table). Topology frame: the original delivers from the head — a module importing `https://scp-wiki-cn.wikidot.com/theme:winxp/code/1` (unquoted `url()`) — ahead of small documentation and one very large code block (original L117–1944). The candidate removes the head module and delivers from the tail (section 3); the code block grows by the inlined font (section 4).
- **Why:** Section 0 declares the route and frame; the gate tag's localization is P2.
- **Verify:** The sources.tsv row for winxp-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's credit furniture is a `[[>]]` block carrying the label 评分： and a bare `[[module Rate]]`. The candidate deletes the Rate (BARE-RATE-DEL) and installs the preview credit block at its head with the eight ruling-3 fields — its 著作権者 field names Meowait (candidate L8), the author the original's documentation names (and the name its sandbox asset folder, `meowait2`, echoes) — and the source-link field names scp-wiki-cn.wikidot.com, the host sources.tsv records for the original, so the host check passes with no probe needed. The field-versus-banner check this package runs on every credit block passes: no attribution line in the original (documentation or CSS banner) is dropped by the candidate.
- **Why:** P3/T1 and ruling 3; the ledger's class outcome records the credit fields FIXED for this row set, and the value check agrees with the form check here.
- **Verify:** Read the credit block at the candidate's head against the original's documentation head.
- **Disposition:** FIXED (ledger §(c3) class outcomes: credit fields FIXED by the credit waves); no credit item is flagged for this theme.

### 2. Includes and components

- **What:** Live includes: the credit pair (section 1) and the tail interwiki-style frame (section 3). The escaped usage example names the candidate in its -jp form (ESCAPED-INCLUDE). The documentation's image-block example (candidate L24) is a bare `component:image-block` include — *the original's own form*, kept — with its sandbox image URL unchanged and only its caption glyph-localized （新纪元 → 新紀元， GLYPH-FORM). No component had to be ported alongside this theme; the COMPONENT-SWAP block is the credit conversion.
- **Why:** P1 (KB-15): the example's bare component form is the shared component's own usage form on both sides; nothing foreign is kept live.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the full live set.
- **Disposition:** Applied; no foreign include kept.

### 3. Delivery and code loading

- **What:** Delivery moves from head to tail. The original's head module imported its code block live from scp-wiki-cn; the candidate removes it and delivers its single code block (candidate L129–1973, headed by the porter comment of section 10) by a tail module importing the draft host's `local--code/theme%3Awinxp-jp/1` plus an interwiki-style frame at priority=1 naming the same /1. Census check: exactly one `[[code]]` block in the candidate, so the /1 address names the block that holds the CSS — correct.
- **Why:** P6/T3 (the frame) and the delivery class generally: one delivered block, addressed once, from the tail. The draft-host form of the live lines is KB-41, class (iii).
- **Verify:** `grep -n 'local--code\|interwiki-style' candidate.txt`; count the `[[code]]` blocks (one).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** The Bauhaus face is the section. The original imports its stylesheet from a jsdelivr GitHub mirror (`cdn.jsdelivr.net/gh/scp-cn-tech/sigma9@cn/fonts/font-bauhaus.css`). The candidate *inlines* that stylesheet's content: two `@font-face 'BauhausLTDemi'` blocks (candidate L133 and L138) — the first sourcing the `.eot` from `sigma9.scpwikicn.com/cn/fonts/`, the second a base64 data-URI woff (the bulk of the candidate's byte growth) plus the `.ttf` on the same host — with the font file's own comment ("Font Squirrel, 2013") carried at candidate L131. Inlining is not a flag here: the inlined content is exactly the file the original imported, the rework2-p5 wave's recorded shape for the Sigma-9 family, and the face is thereby delivered *by the candidate itself* rather than by a third-party mirror. The same repo's `colstyle.min.css` import is *kept* as an import (candidate L153) — KB-14's verbatim-import class, and winxp is named in the ledger §(c3) preamble's KB-14 set. The Nanum Gothic and Nanum Gothic Coding earlyaccess imports and Font Awesome 4.3.0 from `maxcdn.bootstrapcdn.com` (BootstrapCDN, an allowed host) are the original's own, carried unchanged. No JP font is loaded or named, and none was charged: the design's faces are the XP system set (Tahoma, Verdana, Trebuchet MS, Marlett) plus Nanum — a faithful XP chrome has no JP face to add, so section 4's honest statement is that P7 is not engaged. One carried defect of the *original*, recorded so it is not mistaken for the port's: the stack at candidate L1896 reads `'Nanum Gothic', san-serif;` — the typo is the original's own (original L1867), carried byte-faithfully; browsers fall back to the generic family either way, so it is cosmetic in both files.
- **Why:** KB-14 (verbatim import of a base family's stylesheet) for colstyle; the inlining is the delivery class's self-hosting form for the font. The classifier's HTTP-KEPT-style readings on this file's data URI are the known false-fire shape (the woff's data contains no external reference; the `@font-face` sources are the two recorded hosts).
- **Verify:** Candidate L131–153 for the inlined faces and the kept import; `grep -n 'san-serif' candidate.txt original.txt` for the carried typo at the matching loci.
- **Disposition:** Applied (inlining and kept import, per the records above); the sandbox asset hosts are DISPOSITIONED (class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The theme's rendered `content:` strings are its designed UI text and stay as designed: the in-fiction distorted title "倒措哋噺姩芉" (candidate L407), and the XP window-chrome English — "Sidebar", "Document Viewer", "Image Viewer", the "─ □ ×" glyphs — which is English *by design* in the original (an XP desktop's chrome is English in the CN theme too). The CSS-BODY ×3 blocks ride inside the carried Sigma-9 CSS.
- **Why:** P9 / ruling 2's family, in its clearest form: strings that are the artifact's fiction are not untranslated UI. The ledger's class line for this theme records its wording charges under the same outcome.
- **Verify:** `grep -n 'content:' candidate.txt` — the strings above.
- **Disposition:** DISPOSITIONED (ruling 2 family, per the §(c3) class outcomes).

### 6. Text translation

- **What:** The documentation — including its long in-fiction tab prose, the XP desktop's little fiction — is translated in full: 18 TRANSLATION-ANCHORED blocks and 18 TRANS-UNANCHORED blocks, a higher anchored share than the batch's norm because the docs are prose-dense and markup-light. GLYPH-FORM ×2 localizes glyph forms in samples (the image caption's 新纪元 → 新紀元 of section 2, and one in the prose). The CSS comments of the Sigma-9 block are carried as the original carries them (the block is a base-family artifact; its comments are part of its verbatim carriage).
- **Why:** P10 and KB-18.
- **Verify:** diff.md's documentation sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (section 1) names the recorded host. The documentation's image URL stays on its sandbox host (scpsandboxcn.wikidot.com) — original-state delivery, class (ii) — with one silent protocol repair disclosed in section 9. No live link targets a page that does not exist on its named host.
- **Why:** P11 under the dead-reference evidence standard; nothing here meets it.
- **Verify:** `grep -n 'http' candidate.txt` enumerates every URL.
- **Disposition:** Standing; no link item is flagged for this theme.

### 8. Structure

- **What:** The localize.md closing rule holds. The single code block keeps its position after the documentation and its role; the gate wraps the page on both sides; delivery externalizes to the tail (section 3) and the font inlines at the block's head (section 4) without interleaving into the carried CSS. The one EXHIBIT-RESTRUCTURE primary adjudicates against the census — the tabview exhibits, image exhibits, and code exhibit are present on both sides in the same order; the block is a repoint inside the exhibit region.
- **Why:** R3 forces the adjudication; the census decides.
- **Verify:** Compare `grep -n '\[\[code\|\[\[tab\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** No WS-ONLY block and no pure re-indent block (reindent_blocks 0). Two micro-facts ride in the code-head region and are disclosed here: the `@charset "utf-8"` line, the original code block's first line (original L118), stands at candidate L146 in the candidate — displaced below the inlined `@font-face` pair; the displacement is benign (the served `local--code` CSS's parsing does not turn on the embedded block's charset line, and the inlined font data is ASCII-safe base64), and the residue block in the appendix covers the region. And the 404-image background URL is silently protocol-repaired: `url('http://scpsandboxcn.wikidot.com/local--files/meowait2/404-not-found')` in the original becomes the https form in the candidate, same host and path.
- **Why:** R7's disclosure rule extended to micro-repairs: both are one-line changes inside inherited CSS that a formatting "none" would otherwise hide.
- **Verify:** `grep -n '@charset' candidate.txt original.txt`; `grep -n '404-not-found' candidate.txt original.txt`.
- **Disposition:** Standing (disclosed).

### 10. Porter annotations

- **What:** One porter annotation: the comment `/* ===== winxp ===== */` heading the candidate's code block (candidate L130) — the rework wave's standard block marker. One inherited comment must not be confused with it: the Font Squirrel 2013 comment at candidate L131 is the *font file's own* text, carried with the inlining of section 4 — the discrimination of section 10 in the turbo-vision package, applied the same way.
- **Why:** R2: porter-added text is recorded; inherited text is not charged as porter text.
- **Verify:** Candidate L130 and L131.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items. (1) T1's nine errors — hotlink ×8 (the sandbox and sigma9 hosts of sections 4 and 7) and pseudo-ref ×1 (the draft-host delivery line) — all class (ii). (2) The render row's items: the credit modal in preview form (KB-32 family — the JP preview module has no modal, by design); the runtime-hotlink chain including scp-wiki-cn.wdfiles.com (KB-40, environment layer); the candidate hosts scpsandboxcn.wdfiles.com and scpsandboxcn.wikidot.com recorded on the row (the class (ii) sandbox delivery of section 7). (3) T4 row 245: display-affecting 1. The ledger §(c3) class outcomes cover this row set (header language ruling 2; asset hosts class (ii); credit fields FIXED), its preamble names winxp in the KB-14 verbatim-import set (section 4), and the population-check row (LEDGER-POPULATION-CHECK row 25) confirms the theme's population membership. No item in this package is flagged beyond the ledger's own record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 211): exit 1, 9 errors / 2 warn / 1 info — hotlink ×8 and pseudo-ref ×1, all class (ii); no class (i) error. (b) T2/T3 render (RENDER-ROWS-G, CN17): FINDINGS — the items of section 11(2). (c) T4/T5 (LOCALIZE-ROWS row 245): FINDINGS, display-affecting 1. (d) The K5a-i follow-up artifact (`gosign2-lanes/lane-oc-gs-localize-s2-E/diff-winxp-from4.txt`, read for this package): a six-line record whose content is "scp-wiki-cn:theme:winxp rev4 → rev4 変更： なし" with an empty intervening-revision table — it records **no upstream change after the reference revision**, against sources.tsv's "superseded upstream" wording; the artifact's bytes are followed here and the tension is reported in the batch report. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares; the stamp reads STALE because the candidate changed after the verdict in the sweep commit b5cb724. Counts in this README are the generator's (difflib, autojunk off): +103/−71 in 42 change blocks / 5 diff sections; the GNU-diff count of the same pair is 145 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result, including reading the artifact instead of its description.
- **Verify:** Re-run the checker on `pages/theme:winxp-jp.txt`; read the follow-up artifact at the path in (d).
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 246; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The Bauhaus inlining, and why it is not a delivery flag

The standing check for delivery topology asks whether a mechanism the original imports has been replaced by something else — an inlined base, a missing base, an absent definition. The Bauhaus case is the reverse shape: the original imported a *font stylesheet* from a third-party GitHub mirror, and the candidate carries that stylesheet's exact content (both `@font-face` blocks, the Font Squirrel comment, the same font hosts for the `.eot`/`.ttf` sources, the woff as the data URI the stylesheet itself used). Nothing is substituted and nothing is dropped; the dependency on the mirror is removed by carriage, which is the self-hosting direction the campaign prefers, and the rework2-p5 record names the wave that did it across the Sigma-9 family. It is recorded at this length because the candidate's byte size (+35 KB) otherwise looks like unexplained growth in the provenance table: it is one woff file, in base64, doing exactly the job the imported stylesheet did.

### The carried typo

Section 4 records the `san-serif` stack typo (original L1867 = candidate L1896) as the original's own. It is given a paragraph here so the record is unambiguous: a reviewer who finds it has found a faithful carriage, not a port error, and the place to fix it — if it is ever fixed — is a candidate repair decision by the coordinator, not a review-package edit.

## Appendix — residue blocks

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B40 | L125 | L153–154 | The code-head import region: the inlined `@font-face` pair and the displaced `@charset` leave a blank-line pair where the original has a single line (R7; sections 4 and 9) |

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/theme-decoration-sample-winxp-jp.txt` is the decoration sample the render checks ran against (it includes this candidate), and its findings are the sample half of section 11(2). The follow-up diff artifact `gosign2-lanes/lane-oc-gs-localize-s2-E/diff-winxp-from4.txt` (campaign record, not repo) is part of this theme's provenance record and is reported in section 12(d). There are no companion fragments in the repo and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 倒错的新千年 版式
- **Author:** Meowait
- **Source:** https://scp-wiki-cn.wikidot.com/theme:winxp — revision 4
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
