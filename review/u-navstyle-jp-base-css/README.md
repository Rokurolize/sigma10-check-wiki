# Review package — fragment:u-navstyle-jp-base-css

**Kind:** standalone fragment port (Wikidot original) — CSS body only  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | scpko.wikidot.com component:u-navstyle at rev 4 (thd-glasses, CC BY-SA 4.0) — CSS body only | `pages/fragment:u-navstyle-jp-base-css.txt` |
| Host / wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:u-navstyle | fragment:u-navstyle-jp-base-css |
| Revision | rev 4 | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-ko4/work/live-component_u-navstyle.txt` (live 2026-11-16, read-only probe; not re-fetched) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 195 / 5,442 | 152 / 4,158 |
| SHA-256 | `84600e78681e2a7f1bfa1c0a4b2af4a85059cb5615c81704ebac1a747e4a3717` | `d9bd47141798ded1b36950a50410c2789206f5f2be7a2b11771208f3e6b26a0f` |

- The original's descriptor half (KO `iftags +구성요소` prose, Rate block, display:none CSS wrapper) is deliberately not carried — only the CSS body is frozen and ported.
- The original is KO Sigma-9 CSS; the JP theme overrides `#u-side` colours with its own variables, so only the structural rules take effect (recorded in the provenance header).

## Summary

The CSS body of the KO u-navstyle component, ported for theme:garak-the-magazine-jp. The 195-line CSS body is carried verbatim; the diff removes the original's KO descriptor/usage block and display:none wrapper (−53) and adds a JP provenance comment. +10/−53 lines in 2 hunks.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–12 is a JP provenance comment naming rev 4, author thd-glasses, CC BY-SA 4.0, the cache, and the reason the descriptor half is dropped.
- **Why:** Traceability and the R3 drop ground.
- **Verify:** Read candidate L1–12; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit deferred to theme:garak-the-magazine-jp (thd-glasses, CC BY-SA 4.0); no TASL fields in the fragment.
- **Why:** Ruling 3 on the including theme page.
- **Verify:** Read candidate L1–12.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — the original's `[[include :scpko:component:u-navstyle]]` usage examples are in the dropped descriptor, not the ported CSS.
- **Why:** The machine page is CSS only.
- **Verify:** Diff hunk 1 (descriptor removal).
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** The original's self-CSS import wrapper (`[[module CSS]] @import local--code/component:u-navstyle/1`) is dropped with the descriptor; the candidate's CSS body is delivered by the theme's own @import.
- **Why:** P4: fragment as code page; the theme owns delivery.
- **Verify:** Diff hunk 1 and candidate L13.
- **Disposition:** Applied.

### 4. Fonts and assets

- **What:** No asset URLs changed; the CSS has no `url(` assets.
- **Why:** Not applicable.
- **Verify:** Diff has no `url(` lines.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** The CSS is written for KO Sigma-9 `#u-side`; the JP theme overrides its colours via `rgb(var(--main))`/`rgb(var(--bg))`, so only structural rules (weights, arrows, list resets) remain effective — recorded in the provenance header.
- **Why:** Ruling 2/structure: the port does not rewrite design intent; the consuming theme's override is the design decision.
- **Verify:** Read candidate L5–9.
- **Disposition:** DISPOSITIONED (recorded, not a defect).

### 6. Visible text translation

- **What:** The KO descriptor prose (usage, cautions, English note) is dropped with the original's descriptor half, not translated — it belongs to the docs, not the CSS body.
- **Why:** R3: docs live on the theme/component page, not the machine CSS page.
- **Verify:** Diff hunk 1 (−53 lines).
- **Disposition:** Applied (R3 drop).

### 7. Links

- **What:** None — no outbound links in the ported CSS; the KO component link is in the dropped descriptor.
- **Why:** Not applicable.
- **Verify:** Diff has no live links.
- **Disposition:** N/A.

### 8. Structure

- **What:** The `[[code type="CSS"]]` wrapper is kept; only the surrounding descriptor and display:none wrapper are removed.
- **Why:** Preserve the CSS body as a clean fragment.
- **Verify:** Diff hunks 1–2.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** None — CSS body bytes unchanged.
- **Why:** Not applicable.
- **Verify:** Diff is descriptor removal + comment.
- **Disposition:** N/A.

### 10. Porter annotations

- **What:** The provenance comment is the porter's annotation and carries the R3 ground.
- **Why:** R2.
- **Verify:** Read candidate L1–12.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The R3 documentation drop and the Sigma-9→JP override interaction are recorded; no display defect charged.
- **Why:** AGENTS.md §3.
- **Verify:** See Structure and Header.
- **Disposition:** DISPOSITIONED (recorded).

## Verification

- `cmp review/u-navstyle-jp-base-css/candidate.txt pages/fragment:u-navstyle-jp-base-css.txt` succeeds (byte-identical).
- `sha256sum review/u-navstyle-jp-base-css/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** component:u-navstyle (CSS body)
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/component:u-navstyle — revision 4
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
  - The package record names CC BY-SA 4.0 for this original; this line states this repository's CC BY-SA 3.0 release position, per the campaign's attribution standard.
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: not applicable — the fragment carries no translated prose; credit is deferred to theme:garak-the-magazine-jp.
