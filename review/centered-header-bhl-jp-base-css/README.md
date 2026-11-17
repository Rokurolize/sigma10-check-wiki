# Review package — fragment:centered-header-bhl-jp-base-css

**Kind:** standalone fragment port (Wikidot original) — verbatim code/2 CSS  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | etinjat.wikidot.com component:centered-header-bhl, code/2 CSS (7,885 B / 271 lines) | `pages/fragment:centered-header-bhl-jp-base-css.txt` |
| Host / wiki | etinjat.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:centered-header-bhl (code/2) | fragment:centered-header-bhl-jp-base-css |
| Revision | code/2; component page cached 2026-11-16 | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/etinjat.wikidot.com__component:centered-header-bhl__code__2` (fetched once 2026-11-16) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 271 / 7,885 | 280 / 8,442 |
| SHA-256 | `7d5e944ec84038858d162c08a964b897906a68501aec383b71686881d6c10196` | `de00fd4fb357441e1c799e06cb98b91ab49ef3c3550b275327fc2401ff1cff2a` |

- Verbatim CSS body; the only candidate-side additions are the provenance comment and the code-block wrapper.

## Summary

A verbatim port of an Etinjat centered-header CSS code block for theme:brokedown-database-jp. The 271 CSS lines are unchanged; the +9 lines are a JP provenance comment plus `[[code type="css"]]` … `[[/code]]`. This is the cleanest 'verify, don't churn' record in the lane.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–6 is a JP provenance comment naming the etinjat source, code/2, and deferring credit to the theme page.
- **Why:** Traceability.
- **Verify:** Read candidate L1–6; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit deferred to theme:brokedown-database-jp (original author Etinjat); the fragment adds no TASL fields of its own.
- **Why:** Ruling 3 on the including theme page.
- **Verify:** Read candidate L1–6.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — no include in either file.
- **Why:** Not applicable.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** The CSS is delivered by `@import` from the theme's `[[module CSS]]`; the candidate wraps the verbatim block in `[[code type="css"]]`.
- **Why:** P4: fragment as code page.
- **Verify:** Read candidate L7 and L278–280; diff hunks 1–2.
- **Disposition:** Applied.

### 4. Fonts and assets

- **What:** None — no font or asset URL changed.
- **Why:** Not applicable.
- **Verify:** Diff has no `url(` lines.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** The CSS defines header measurements (`--header-h1-font-size`, `#header::before`) — carried verbatim, no language edit (ruling 2).
- **Why:** Design values are the original's.
- **Verify:** Diff hunk 1 context.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** None — no visible prose or CSS display string.
- **Why:** Not applicable.
- **Verify:** No translated text in diff.
- **Disposition:** N/A.

### 7. Links

- **What:** None — no outbound links.
- **Why:** Not applicable.
- **Verify:** No `http` prose links.
- **Disposition:** N/A.

### 8. Structure

- **What:** The block is wrapped in a code block so the theme's @import can address it; CSS bytes unchanged.
- **Why:** Fragment structure requirement.
- **Verify:** Diff hunks 1–2.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** None — no whitespace churn.
- **Why:** Not applicable.
- **Verify:** Diff is +9 wrapper lines only.
- **Disposition:** N/A.

### 10. Porter annotations

- **What:** The provenance comment is the porter's annotation.
- **Why:** R2.
- **Verify:** Read candidate L1–6.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** No class requires disposition: the record is a verbatim body-plus-wrapper port.
- **Why:** AGENTS.md §3.
- **Verify:** See Delivery.
- **Disposition:** No exception needed.

## Verification

- `cmp review/centered-header-bhl-jp-base-css/candidate.txt pages/fragment:centered-header-bhl-jp-base-css.txt` succeeds (byte-identical).
- `sha256sum review/centered-header-bhl-jp-base-css/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

