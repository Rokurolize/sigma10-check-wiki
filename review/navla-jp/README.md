# Review package — component:navla-jp

**Kind:** standalone component port (Wikidot original) — receiver + code fragment  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | scpko.wikidot.com component:navla at rev 119 — local--code/component:navla/1 CSS (15,219 B / 757 lines) | `pages/component:navla-jp.txt` |
| Host / wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:navla (local--code/component:navla/1) | component:navla-jp |
| Revision | rev 119 (component); code/1 | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/scpko.wdfiles.com__local--code__component:navla__1` (fetched once 2026-11-16) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 757 / 15,219 | 1040 / 23,798 |
| SHA-256 | `d6dc858a2ffe472c8ec908d9bd5dcd24c1f65c42a866207d37cc525d0b4a7106` | `e5cacc220df0612718da523e12197c9d072f3879a5e82e0f4cd682ceef3598b6` |

- The percent-encoded twin cache `…component%3Anavla__1` is byte-identical (same SHA-256); the unencoded-path copy is used.
- A component-page cache also exists at `lane-oc-ko3/evidence/live-component-navla.txt` but carries the descriptor; the CSS cache is the ported artifact.

## Summary

The KO Navla component CSS ported for theme:navla-style-jp. The original code/1 CSS is carried in a code block, with JP adaptations: font loads replaced (UnBatang → Noto Serif JP, Google Fonts loads consolidated to the block head), SCP logo and quote-mask URLs re-hosted to the draft host, comments translated, and the original component page's help/toc/Center/Free-DLC sections merged in unconditionally. +300/−18 lines in 7 hunks.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–13 is a JP provenance comment naming rev 119, the code/1 cache, and the adaptation list.
- **Why:** Traceability for a large machine component.
- **Verify:** Read candidate L1–13; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit is deferred to theme:navla-style-jp's credit block (the original's KO author is Navla, CC BY-SA 3.0). The receiver carries no standalone TASL fields.
- **Why:** The component is consumed by the theme; ruling 3 attribution lives on the including theme page.
- **Verify:** Read candidate L1–13.
- **Disposition:** Standing; no TASL defect.

### 2. Includes and components

- **What:** None — no foreign `[[include]]`; the component's own self-delivery is a CSS module.
- **Why:** No cross-wiki include to repoint.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** Self-delivery `[[module CSS]]` @imports `local--code/component%3Anavla-jp/1` (candidate L15–17); the CSS body is a `[[code]]` block, plus merged help/toc/Center sections.
- **Why:** P4/P6; draft-host delivery is sanctioned at draft stage (class (iii)).
- **Verify:** Read candidate L15–17 and the merged sections; diff hunk 1.
- **Disposition:** DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Font loads changed: original's `UnBatang.css` direct link and duplicate Nanum Myeongjo import are dropped; a Noto Serif JP / Noto Sans JP import is added at the block head. Stacks gain JP fallbacks (`'Noto Serif JP', 'Yu Mincho'`, `'Noto Sans JP'`). Logo and quote-mask SVGs re-hosted to `sigma10-jp-test`.
- **Why:** P5/P7: non-allowlisted font host replaced with Google Fonts + JP fallback; KO-file SVGs re-hosted to the JP draft side. Owner ruling 1 (cross-theme delivery) supports the JP side carrying the fix.
- **Verify:** Diff hunks 3–5: `@import` lines, `--scp-logo`, `--title-font-nvl`, `.nmj`/`.ubt`, `.digit`, `.quote::before` masks.
- **Disposition:** Applied; re-hosted assets are draft-host class (ii)/(iii) at posting.

### 5. Header, sidebar and site furniture

- **What:** The `:root:lang(ja)` block in the merged help section sets `--theme-rgb-nvl` etc. in Japanese; no header language change to the base CSS is made (ruling 2).
- **Why:** JP-supplement variables are porter-written, not a rewrite of the original's design.
- **Verify:** Read candidate L24–33.
- **Disposition:** Standing.

### 6. Visible text translation

- **What:** Header comment lines and the help/toc/Center usage prose are translated to Japanese; the original's English note lines are kept verbatim where they are the author's own text.
- **Why:** T5: visible text translated; proper-noun/author text preserved.
- **Verify:** Diff hunk 3 (header comment) and the merged help sections.
- **Disposition:** Applied.

### 7. Links

- **What:** Two KO external links in the merged section point to the original's component/theme introduction; they are documentation references, not live dependencies.
- **Why:** P11: original links retained as references under the dead-reference standard.
- **Verify:** Read candidate L218–220.
- **Disposition:** Standing; no dead references charged.

### 8. Structure

- **What:** Original's gated help/Center sections (present on the component page but not in code/1) are merged in unconditionally in the candidate, as recorded in the provenance header.
- **Why:** R3: the conditional split could not be reproduced from the code/1 cache; carrying the content preserves the original's effective behavior.
- **Verify:** Diff hunk 1 (merged sections) and hunk 7 (Free DLC/Center tail).
- **Disposition:** DISPOSITIONED (recorded, not a defect).

### 9. Formatting only

- **What:** Three trailing-whitespace-only lines were normalized (` ` → empty).
- **Why:** Formatting churn disclosed as its own class.
- **Verify:** Diff hunks at original L578, L657, L753.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The provenance header and translated help prose are porter annotations.
- **Why:** R2.
- **Verify:** Read candidate L1–13 and merged sections.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Draft-host self-delivery and re-hosted KO assets are the two classes to disposition; both are draft-stage, posting-time rewrites.
- **Why:** AGENTS.md §3.
- **Verify:** See Delivery and Fonts/assets.
- **Disposition:** DISPOSITIONED (class (ii)/(iii)).

## Verification

- `cmp review/navla-jp/candidate.txt pages/component:navla-jp.txt` succeeds (byte-identical).
- `sha256sum review/navla-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** component:navla (local--code/1 CSS)
- **Author:** Navla
- **Source:** https://scpko.wikidot.com/component:navla — revision 119; code/1 CSS
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: not applicable — the receiver carries no standalone TASL fields; credit is deferred to theme:navla-style-jp.
