# Review package — fragment:collapsible-sidebar-jp-base-css

**Kind:** standalone fragment port (Wikidot original) — verbatim code/1 CSS  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | etinjat.wikidot.com component:collapsible-sidebar, code/1 CSS (20,550 B / 449 lines) | `pages/fragment:collapsible-sidebar-jp-base-css.txt` |
| Host / wiki | etinjat.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:collapsible-sidebar (code/1) | fragment:collapsible-sidebar-jp-base-css |
| Revision | code/1; component page cached 2026-11-16 | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/etinjat.wikidot.com__component:collapsible-sidebar__code__1` (fetched once 2026-11-16) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 449 / 20,550 | 458 / 21,113 |
| SHA-256 | `e65374b5beca2632cecf164538296f4e1cac336f15eab3eb928b5516ad089495` | `795a7759e5d734cf52b521c97eec1d3b9068fa7d72a14b360fc0de1b034380cd` |

- Verbatim CSS body; the SVG sidebar-tab mask is an inline data URI, unchanged.

## Summary

A verbatim port of an Etinjat collapsible-sidebar CSS code block for theme:brokedown-database-jp. The 449 CSS lines are unchanged (including the inline SVG data URI); the +9 lines are a provenance comment and the code-block wrapper.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–6 is a JP provenance comment naming the etinjat source and code/1.
- **Why:** Traceability.
- **Verify:** Read candidate L1–6; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit deferred to theme:brokedown-database-jp (Etinjat); no TASL fields in the fragment.
- **Why:** Ruling 3 on the including theme page.
- **Verify:** Read candidate L1–6.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — no include in either file.
- **Why:** Not applicable.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** Delivered by the theme's `@import`; the candidate wraps the verbatim code/1 in `[[code type="css"]]`.
- **Why:** P4: fragment as code page.
- **Verify:** Read candidate L7 and L456–458; diff hunks 1–2.
- **Disposition:** Applied.

### 4. Fonts and assets

- **What:** None — the sidebar-tab mask is an inline `data:` URI, unchanged; no host to repoint.
- **Why:** No-re-uploads standing order; data URI needs no hosting.
- **Verify:** Diff hunk 1 context.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** None — no header furniture; the CSS sets sidebar widths and tab art only.
- **Why:** Not applicable.
- **Verify:** No header rules in diff.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** The original's Chinese file-header comment (可折叠侧边栏) is carried verbatim; it is a source identifier, not a visible UI string.
- **Why:** Verbatim port; no translation of a code comment is required.
- **Verify:** Diff hunk 1 context (comment unchanged).
- **Disposition:** N/A.

### 7. Links

- **What:** None — no outbound links.
- **Why:** Not applicable.
- **Verify:** No `http` prose links.
- **Disposition:** N/A.

### 8. Structure

- **What:** Code-block wrapper added; CSS bytes unchanged.
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

- **What:** No disposition needed: verbatim body plus wrapper.
- **Why:** AGENTS.md §3.
- **Verify:** See Delivery.
- **Disposition:** No exception needed.

## Verification

- `cmp review/collapsible-sidebar-jp-base-css/candidate.txt pages/fragment:collapsible-sidebar-jp-base-css.txt` succeeds (byte-identical).
- `sha256sum review/collapsible-sidebar-jp-base-css/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

