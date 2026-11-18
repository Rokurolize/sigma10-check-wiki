# Review package — theme:turbo-vision-dark-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:turbo-vision-dark-jp — origin EN, population #150 [GOSIGN2-LEDGER (b) row 150]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 150]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 2 warns / 1 info (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 135; GOSIGN2-LEDGER (b) row 150]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 365–372px@320 on page and sample; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 150, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 150]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 150]
- Computed against: canonical commit 666f54356acb463c56016c967dc52464b25ba4a2; candidate file pages/theme:turbo-vision-dark-jp.txt sha256:07a2a49f2845242efcf304225807f5ed97e98934b4df2d9a48128b5317910388; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 150) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×7 (class (ii), section 11); the render row's items (page and sample overflow at 320, KB-33/KB-34; credit-modal preview form, KB-32); T4 display-affecting 3 (the pattern-5 font stylesheet and images, KB-58). The verdict stamp reads PASS, not STALE: the candidate has not changed since the FIX2-CREDIT commit the stamp was computed against |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:turbo-vision-dark | theme:turbo-vision-dark-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 50 (first translation; the candidate's credit block records 初訳時参照リビジョン: 50) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-turbo-vision-dark.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:turbo-vision-dark-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 917 lines / 20,177 bytes | 929 lines / 22,167 bytes |
| SHA-256 | 3862bec176da2f621c07efc10251b5cca7cfcc607fd1110fb162cd4b11b97626 | 07a2a49f2845242efcf304225807f5ed97e98934b4df2d9a48128b5317910388 |

Wave history: the candidate was created by the Stage 2 EN22 integration (6fa35a9, the LOCALIZE-S2-C wave's port) and touched once since, by FIX2-CREDIT (666f543, the credit wave over 36 themes). The usage-example sweep did not touch this file: its self-references already stand in forms the sweep leaves alone (section 2). Layering note (sources.tsv): this candidate layers over theme:turbo-vision-jp; this package's diff covers the theme's own layer only, and the base's package is review/turbo-vision-jp/ in the same batch.

## Summary

A dark variant layered over the Turbo Vision base (ledger kind K5b-3), and the port preserves the layering exactly: the original's head module imported the base's two code blocks from scp-wiki plus its own block; the candidate's head module imports the base candidate's two blocks plus its own, all from the draft host, and an interwiki-style frame is added beside the module as in the batch's other dual-delivery themes. Inside the layer, the work is the standard classes at this theme's scale — the documentation and exhibits translated, fourteen exhibit link samples localized, twelve font stacks given a JP second face (including the four live `.font` rules in the in-gate module, not just the code exhibit), the two webfont imports moved from bunny to Google Fonts, and the pixel-font stylesheet repointed to the draft host's own folder, where T4 found it and three images 404 (dispositioned KB-58; on the draft host the pixel faces fall back to the inserted Noto Sans JP, which the base layer loads). Measured churn (the generator's difflib count, autojunk off): +155/−146, 301 changed lines in 105 change blocks / 21 diff sections; a GNU-diff count gives 270 changed lines (+141/−129). One unmarked functional supplement is disclosed in the per-theme record (an `#interwiki` selector variant added to a sidebar rule).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 105 change blocks — 52 specific (49.5%), 51 heuristic (48.6%), 2 residue (1.9%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 52 |
| TRANSLATION-ANCHORED | 30 |
| COMMENT-TEXT | 16 |
| LINK-REPOINT | 14 |
| JPFONT-STACK | 12 |
| DRAFT-HOST | 6 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| TASL-FIELDS | 1 |
| WS-ONLY | 1 |

Adjudication of the heuristic mass: the 51 heuristic blocks are one-line exhibit and documentation translations, the fourteen exhibit link samples (LINK-REPOINT), and CSS comment translations (COMMENT-TEXT ×16 across tiers); each shape was read against the mirror for this README and none hides a structural change (section 8's census). The single CSS-BODY block is inside the font-stack mass adjudicated in section 4. The two residue blocks (a heading translation; a profanity comment neutralized in translation) are in the appendix.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:turbo-vision-dark-jp; original theme:turbo-vision-dark on scp-wiki at reference revision 50; candidate `pages/theme:turbo-vision-dark-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-C wave (sources.tsv kind: K5b-3 — a layer over a base theme, here theme:turbo-vision). Topology frame: the original's first module (head, outside the gate) imports base blocks 1–2 and its own block 1; a second module inside the gate carries the live `.font1`–`.font4` utility rules. The candidate mirrors both positions (section 3).
- **Why:** Section 0 declares the route and the layering, because every delivery claim in section 3 is a claim about two files (this layer and the base candidate), not one.
- **Verify:** The sources.tsv row for turbo-vision-dark-jp (its note states the layering); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original's bare `[[module Rate]]` is deleted (BARE-RATE-DEL) and the preview credit block is installed in the campaign's bare form (candidate L37/L46: `[[include credit:start-preview]]` / `credit:end-preview`, no `:scp-jp:` prefix). Its eight ruling-3 fields include 著作権者 `[[*user JackalRelated]]` and 元記事リンク https://scp-wiki.wikidot.com/theme:turbo-vision-dark — scp-wiki.wikidot.com is the host sources.tsv records for the original, so the host check passes with no probe needed. The code banner is translated with the base attribution intact: the dark layer's author and, for the base Turbo Vision, JakdragonX and Croquembouche are all named, matching the field's own statement. The bare credit form is a population fact, recorded here rather than flagged: 10 of the 285 candidate files use the bare credit include against 275 prefixed, and T1's charge against this file (pseudo-ref ×7) covers the bare forms as class (ii).
- **Why:** P3/T1 and ruling 3 for the block; the field-versus-banner check passes in both directions. The bare form is P1's class (ii): the include resolves on the posting wiki, and the posting procedure owns the form.
- **Verify:** Read the credit block at candidate L37–46; `grep -c 'include credit:start-preview' pages/theme:*.txt` reproduces the population count's numerator shape (bare forms across candidates).
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED by the FIX2-CREDIT wave); the bare form is DISPOSITIONED (class (ii)).

### 2. Includes and components

- **What:** Live includes: the credit pair (section 1, bare form), the head interwiki-style frame (candidate L9, also in bare form: `[[include component:interwiki-style` — 36 of 285 candidates use the bare frame form against 251 prefixed), and the toggle-sidebar repoint at candidate L1 (`:scp-wiki:` → `:scp-jp:`). The escaped usage example (candidate L73) names the theme in plain same-wiki form, `@@[[include theme:turbo-vision-dark-jp]]@@`, which resolves to the candidate's own page on the posting wiki and is the form the usage sweep leaves standing. The base is *not* included as a page: it is delivered by `@import` (section 3), exactly as the original imports it. INCLUDE-REPOINT ×2 are the frame and the toggle-sidebar.
- **Why:** P1 (KB-15) for the repoints; the bare forms are the class (ii) population recorded in section 1.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the full live set.
- **Disposition:** Applied; the bare forms are DISPOSITIONED (class (ii)).

### 3. Delivery and code loading

- **What:** The original's head module imported, in order, `https://scp-wiki.wikidot.com/theme:turbo-vision/code/1`, `/code/2`, and its own `local--code/theme:turbo-vision-dark/1`. The candidate's head module (candidate L3–7) imports, in the same order, the draft host's `theme%3Aturbo-vision-jp/1`, `theme%3Aturbo-vision-jp/2`, and `theme%3Aturbo-vision-dark-jp/1`; an interwiki-style frame (candidate L9–13, priority=1) naming the candidate's own /1 is added beside it (dual delivery, the batch's fixed form). Both stand outside the gate (candidate L14), as the original's module stood outside its gate; the second module, inside the gate on both sides (candidate L16–35), carries the `.font` rules. Census checks, both directions: the base candidate (review/turbo-vision-jp/candidate.txt) has exactly two `[[code]]` blocks, so the /1 and /2 imports name the blocks that hold the base CSS; this candidate has exactly one, so its /1 is correct.
- **Why:** P4/T9 (base and own delivery from JP-side hosts) and P6/T3 (the frame). The draft-host form of the live lines is KB-41, class (iii).
- **Verify:** `grep -n 'local--code\|interwiki-style' candidate.txt`; count `[[code]]` blocks in this candidate (one) and in the base candidate (two).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Loads (FONT-IMPORT): the original's Jost and Michroma imports from fonts.bunny.net become Google Fonts imports (candidate L297–298). The pixel faces (Terminus, Hermit, Mx437) load through an `@font-face` stylesheet file, `stylesheet.css`, which the candidate repoints to the draft host's own folder (candidate L299); T4 probed it there and it returned 404, as did `tb-bga.png`, `logo-new.png`, and `spread-log.png` (section 11) — so on the draft host the pixel faces do not load, and the stacks fall back. Stacks (JPFONT-STACK ×12): every font stack in the layer gains `"Noto Sans JP"` as its second family — including the four live rules in the in-gate module (`.font1`–`.font4`, candidate L16–35), not only the code exhibit's stacks — and Noto Sans JP is genuinely loaded, by the base layer's import (the base candidate's code block 1), so the insertion is applied, not decorative. Specimens: the EN pangram samples become JP pangrams （いろはにほへと、ちりぬるを / あめつちほしそら、やまかわみねたに) as part of the section 6 mass.
- **Why:** P2/KB-17 (bunny is outside the allowed set; Google Fonts is in it) and P7 (JP second face in load and stacks together, across both delivery layers). The 404 stylesheet is P5/KB-58: own-folder re-hosting is the posting-time class.
- **Verify:** Candidate L297–299 for the three delivery lines; `grep -n 'Noto Sans JP' candidate.txt` counts the stack insertions (twelve blocks).
- **Disposition:** Loads and stacks applied; the stylesheet and images are DISPOSITIONED (KB-58, class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** Header furniture is the base layer's; this layer's own furniture work is in its sidebar rules. One unmarked functional supplement rides there and is disclosed: in the code block, the resources rule (candidate L462–463) gains its `#interwiki`-rooted selector twins in the candidate (`#interwiki .side-block.resources` and `#interwiki .side-block.resources .heading p` alongside the `#side-bar` forms), extending the resources-block styling to the interwiki block. The addition is consistent with the file's own neighboring rules, several of which already carry `#interwiki` variants in the original; it is an addition, not a repair, and no ledger row names it — recorded here and in the per-theme record so it is not mistaken for carried CSS.
- **Why:** The standing furniture check reads this layer for overrides the base does not make; the supplement is disclosed under the same rule as section 9's repairs (a change inside inherited CSS is part of the record).
- **Verify:** `grep -n 'side-block.resources' candidate.txt original.txt` — the selector sets differ exactly as stated.
- **Disposition:** Standing (disclosed supplement).

### 6. Text translation

- **What:** The documentation and exhibits are translated throughout: 30 TRANSLATION-ANCHORED blocks, 52 TRANS-UNANCHORED blocks (one-line exhibit translations), and 16 COMMENT-TEXT blocks (CSS comments). The fourteen LINK-REPOINT blocks are the exhibit link samples, `[[[LINK]]]` → `[[[link|リンク]]]` and its siblings — specimen localization, counted here rather than in section 7. The font specimens become JP pangrams (section 4). The banner is translated with attribution intact (section 1). One comment's register is neutralized in translation (appendix, B96).
- **Why:** P10 and KB-18; the unanchored mass was read line by line against the mirror for this README.
- **Verify:** diff.md's body sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (section 1) names the recorded host. One live prose link is repointed: the intro's base-theme link, `https://scp-wiki.wikidot.com/theme:turbo-vision` in the original, becomes `https://scp-jp.wikidot.com/theme:turbo-vision` in the candidate — the *production* JP page, which is the right target: the prose speaks of the published base the reader can apply today, not of the base's migration candidate (whose own package is in this batch). The fourteen exhibit link samples are specimens (section 6).
- **Why:** P11: a prose link names the serving JP counterpart; for a published base, that is the production page.
- **Verify:** `grep -n 'turbo-vision"' candidate.txt` region — the intro link at the docs head.
- **Disposition:** Standing; no link item is flagged for this theme.

### 8. Structure

- **What:** The localize.md closing rule holds, and the layering is preserved structurally: head module outside the gate, utility module inside it, code exhibit in place (original L288–916 region → candidate L300–928), tail furniture in the original's order. The one EXHIBIT-RESTRUCTURE primary adjudicates against the census — the tabview, font specimens, image exhibits, and code exhibit are present on both sides in the same order; the block is a repoint inside an exhibit region. Exhibit census 1:1, code census 1:1.
- **Why:** R3 forces the adjudication; the census decides.
- **Verify:** Compare `grep -n '\[\[module\|\[\[code\|\[\[tab' original.txt candidate.txt`.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** One WS-ONLY block, and whitespace normalization riding inside the font-stack lines (trailing spaces dropped; `"Terminus","Mx437` gains its space after the comma) — disclosed here because those lines also carry the section 4 stack change, so the classifier counts no pure formatting block for them.
- **Why:** R7: formatting churn is disclosed as its own class wherever it rides.
- **Verify:** The stack lines in diff.md's code sections.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no `[!-- --]` comments and no porter comment lines: no wave marker comment heads its code block (its first lines are the font imports of section 4), and a scan for comment-only added lines returns only the translated CSS comments of section 6, which are the original's comments in translation, not additions.
- **Why:** R2's ground for "none": the annotation classes were searched for explicitly (the brief's standing warning is that annotations ride inside other labeled blocks; here the labeled blocks' added lines were read, and none is an annotation).
- **Verify:** `grep -n '=====\|!--' candidate.txt` returns nothing.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Three items. (1) T1's seven pseudo-ref errors: class (ii) — the bare credit and frame forms and the draft-host delivery lines (sections 1–3), all posting-procedure forms. (2) The render row's items: page and sample overflow of 365–372px at 320 (KB-33/KB-34 wide-content family) and the credit modal in preview form (KB-32 family — the JP preview module has no modal, by design). (3) T4 row 150, display-affecting 3: the pattern-5 set — `stylesheet.css` (the pixel faces' `@font-face` file), `tb-bga.png`, `logo-new.png`, `spread-log.png`, all 404 on sigma10-jp-test. The ledger's §(c3) line dispositions P5 for this theme as class (ii) / KB-58: re-hosting is a posting-time act and re-upload is barred before it. No item in this package is flagged beyond the ledger's own record; the section 5 supplement is disclosed, not flagged, because it extends the theme's own existing selector pattern and breaks nothing the checks measure.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes; the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 135): exit 1, 7 errors / 2 warn / 1 info; all seven errors are pseudo-ref, class (ii); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-D (EN22)): FINDINGS — the items of section 11(2). (c) T4/T5 (LOCALIZE-ROWS row 150): FINDINGS, display-affecting 3 (the pattern-5 set). (d) This package's own checks: the two census counts of section 3 (own blocks 1, base blocks 2), run against both candidates in this repo. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares; the stamp reads PASS because the candidate has not changed since the stamp's computed-against commit 666f543. Counts in this README are the generator's (difflib, autojunk off): +155/−146 in 105 change blocks / 21 diff sections; the GNU-diff count of the same pair is 270 changed lines.
- **Why:** Verification claims name the cheapest deciding check and its result.
- **Verify:** Re-run the checker on `pages/theme:turbo-vision-dark-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 150; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The layering, verified from both files

The K5b-3 claim — this theme is a layer over theme:turbo-vision, and the candidate layers over the base's candidate — is checkable from this repo alone, and was checked: the base candidate has exactly two `[[code]]` blocks (its theme-mode CSS and its main CSS), and this candidate's head module imports those two blocks in the original's order before its own single block. A reviewer who reads only this package's diff sees the import lines change hosts; the census is what makes the lines *correct*, because a /2 import against a one-block base would deliver the wrong layer silently. The base's own package (review/turbo-vision-jp/, same batch) records the production-migration route by which the base candidate exists.

### The `#interwiki` selector supplement

Recorded in section 5: one sidebar rule gains `#interwiki` selector variants with no original counterpart and no comment. It is consistent with the file's own pattern (neighboring rules carry such variants in the original), it changes rendering only by extending an existing style to the interwiki block, and no check row charges it. It is disclosed here so the supplement is a known fact of the port rather than a discovery for the next reviewer.

## Appendix — residue blocks

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B17 | L68–69 | L80–81 | The "++ WHAT'S NEW?" exhibit heading translated to "++ 新要素" (R1; section 6) |
| B96 | L645–646 | L657–658 | A CSS comment ("/* BOTTOM SHIT YOU PROLLY WOULDN'T HAVE NOTICED */") translated with its register neutralized to "/* 下部表示 */" (R1 comment translation; section 6) |

## Change set outside the two diffed files

The diff covers two files; the port's record is larger in two directions. `pages/theme-decoration-sample-turbo-vision-dark-jp.txt` is the decoration sample the render checks ran against (it includes this candidate), and its findings are the sample half of section 11(2). And the base candidate `pages/theme:turbo-vision-jp.txt` is this theme's delivery dependency: the head module imports its two code blocks, so the base's package (review/turbo-vision-jp/) is part of this theme's record by reference. Neither file carries a port change of this theme's own to explain here.

## License and attribution

- **Title:** Turbo Vision Dark Theme
- **Author:** JackalRelated
- **Source:** https://scp-wiki.wikidot.com/theme:turbo-vision-dark — revision 50
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
