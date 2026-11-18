# Review package — component:rok-gov-base-jp

**Kind:** standalone component port (Wikidot original) — CSS body  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | scpko.wikidot.com component:rok-gov-base (included by theme:rok-gov-theme rev 81) | `pages/component:rok-gov-base-jp.txt` |
| Host / wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:rok-gov-base | component:rok-gov-base-jp |
| Revision | component cached 2026-11-16; including theme:rok-gov-theme rev 81 | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/scpko__component__rok-gov-base.wikitext` (fetched once 2026-11-16) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 669 / 14,462 | 614 / 13,461 |
| SHA-256 | `3fc5b7640e8d434023a275126e478cf4542f06f84d7fe766920d228046172458` | `755f5e9ff5fc9244328abee57da039fc201dbf2a07befd445385e01e9f4d60c7` |

- No live re-fetch; the cached wikitext is frozen as original.txt.

## Summary

The CSS body of the ROK government component, ported for theme:rok-gov-theme-jp. The candidate drops the original's duplicated component/theme info blocks and usage prose (kept on the theme page), swaps the broken self-delivery wrapper (`[[div …]]` → `[[div_ …]]`), replaces the noonnu font with Google Fonts JP/KR loads, and repoints all image URLs to the draft host. +34/−88 lines in 10 hunks.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–8 is a JP provenance comment naming the KO source, the image URL re-hosting, and the font substitution.
- **Why:** Traceability for a machine CSS page.
- **Verify:** Read candidate L1–8; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit is deferred to theme:rok-gov-theme-jp (author thd-glasses, CC BY-SA). The component page carries only 制作/画像出典/フォント出典 lines.
- **Why:** Ruling 3 attribution lives on the including theme page.
- **Verify:** Read candidate L10–16.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — the original's `:scpko:info:start` blocks are dropped rather than repointed; the candidate has no foreign include.
- **Why:** Info modules belong to the docs, not the machine CSS page.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** The self-delivery wrapper is corrected from `[[div [[iftags -테마]]style=…]]` to `[[div_ [[iftags -テーマ]]style=…]]` (candidate L18) — the original's form is malformed.
- **Why:** Original technical mistake fixed in the port (standing order); recording the exact fix for the author.
- **Verify:** Diff hunk 2 (`[[div ` → `[[div_ `).
- **Disposition:** Applied (original technical mistake fixed).

### 4. Fonts and assets

- **What:** `:root --header` and three `background`/`list-style-image` URLs repointed from `scpko.wdfiles.com` to `sigma10-jp-test.wdfiles.com/local--files/theme%3Arok-gov-theme-jp/…`; the noonnu `EBSHMJESaeronRA` @font-face is replaced by Google Fonts Noto Sans JP / Noto Serif JP / Gothic A1 imports.
- **Why:** P5: non-allowlisted font host replaced; P7: JP/KR fallbacks; draft-bucket image URLs are a campaign-wide deferred condition, not a per-theme defect (no re-uploads rule).
- **Verify:** Diff hunks: font block (orig L93 → cand L35), URL lines (orig L96, L261, L345, L578, L643).
- **Disposition:** Applied; asset 404s are deferred, not defects.

### 5. Header, sidebar and site furniture

- **What:** Header variables (`--title`, `--subtitle`) are carried as `{$title}`/`{$subtitle}` exactly as the original; no language edit (ruling 2).
- **Why:** Values are theme parameters, not port decisions.
- **Verify:** Diff hunk 2 context.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** The original's duplicated KO component/theme info blocks, KO/EN usage instructions and parameter tables are dropped; a one-line JP pointer to the theme page replaces them.
- **Why:** R3: usage docs live on the theme page; the machine page carries only CSS.
- **Verify:** Diff hunk 1 (large deletion) and hunk at orig L531 → cand L473.
- **Disposition:** Applied (documentation moved to theme page).

### 7. Links

- **What:** The `noonnu.cc/font_page/77` font-source URL is retained as provenance in the JP note.
- **Why:** P11: original reference retained as a citation.
- **Verify:** Read candidate L14.
- **Disposition:** Standing.

### 8. Structure

- **What:** The CSS body is gated by `[[iftags -テーマ]]`, preserving the original's non-theme-page restriction; two `[[module CSS]]` blocks (main + GoI-format) remain, with the GoI label translated.
- **Why:** Structure parity with the original; only the docs wrapper changed.
- **Verify:** Diff hunk 2 and the `+ GoI フォーマット用の追加コード` line.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** Whitespace-only changes: a blank line before `[[/module]]`, ` :root {` → `:root {`, and trailing-space normalization in two CSS blocks.
- **Why:** Formatting churn disclosed.
- **Verify:** Diff hunks at orig L473, L550, L601 etc.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The provenance comment and the JP note replacing the KO docs are porter annotations.
- **Why:** R2.
- **Verify:** Read candidate L1–16.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Draft-bucket image 404s are a deferred campaign condition; the noonnu font replacement and technical-mistake fix are recorded. No per-theme display defect is charged.
- **Why:** AGENTS.md §3/§4 (no re-uploads; original mistakes fixed and recorded).
- **Verify:** See Fonts/assets and Delivery.
- **Disposition:** DISPOSITIONED (deferred assets); fix recorded.

## Verification

- `cmp review/rok-gov-base-jp/candidate.txt pages/component:rok-gov-base-jp.txt` succeeds (byte-identical).
- `sha256sum review/rok-gov-base-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** component:rok-gov-base
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/component:rok-gov-base — component cached 2026-11-16; included by theme:rok-gov-theme revision 81
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: not applicable — the component carries no translated prose; credit is deferred to theme:rok-gov-theme-jp.
