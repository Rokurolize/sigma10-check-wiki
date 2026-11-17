# Review package — component:betterbetterfootnote-jp

**Kind:** standalone component port (Wikidot original) — receiver page  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | fendsfox.wikidot.com component:betterbetterfootnote, code/1 CSS (2,402 B / 96 lines) | `pages/component:betterbetterfootnote-jp.txt` |
| Host / wiki | fendsfox.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:betterbetterfootnote (code/1) | component:betterbetterfootnote-jp |
| Revision | code/1; no page revision number recorded in the cache | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/fendsfox__component:betterbetterfootnote__code__1` (fetched once from live Wikidot 2026-11-16); the full component page wikitext is also cached as `fendsfox__component:betterbetterfootnote.wikitext` | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 96 / 2,402 | 143 / 4,975 |
| SHA-256 | `a33eabee904e7c2356de8572770b15e4a296ad20a71da7f4b14f0693a12f986b` | `f0a06f533b148f2662b75a0193b488c3000cd8073f02d8d26cbac202a3da6c55` |

- Only the CSS actually ported (code/1) is frozen as original.txt; the candidate's own provenance header names this cache as its source of copy.
- No live re-fetch was made; the cached copy was reused under the fetch-once standing order.

## Summary

A receiver page for fendsfox's hovertip component. The whole CSS body (code/1, 96 lines) is carried byte-for-byte into the candidate's single `[[code type="CSS"]]` block; everything the diff shows is the JP receiver frame added around it — a provenance header, a self-delivery CSS module, a localized `iftags` description, and the code-block wrapper. +47/−0 lines in 2 hunks; no CSS declaration was edited.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** The candidate opens with a JP [!-- … --] provenance block naming the original wiki/page, the code/1 cache, and the fact that the CSS body is untouched.
- **Why:** Porter orientation and TASL traceability for a machine page that otherwise has no visible header.
- **Verify:** Read candidate L1–17; diff hunk 1.
- **Disposition:** Standing (porter-added frame).

### 1. Credit and attribution

- **What:** The source page's author is fendsfox; the candidate records 作者: fendsfox and points licensing to the source page and to the including themes' credits. It adds no 著作権者/作成年 fields of its own because it is a receiver, not a translated text page.
- **Why:** AGENTS.md ruling 3 / localize.md §3 fields apply to translated text; a receiver that forwards credit is not a translation of the CSS.
- **Verify:** Read candidate L13–16.
- **Disposition:** Standing; no TASL defect.

### 2. Includes and components

- **What:** None — no foreign `[[include]]` is carried. The candidate's only include is its own `[[module CSS]]` self-delivery, and the usage example uses the bare candidate name.
- **Why:** The original component page includes itself for delivery; the candidate does the same against its own name.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns the self-CSS module only.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** A `[[module css]]` block at candidate L18–20 @imports the candidate's own draft-host delivery `local--code/component%3Abetterbetterfootnote-jp/1`, added ahead of the original CSS body.
- **Why:** P4/P6: own-code delivery from the JP side. The draft-host form is the sanctioned draft-stage class (class (iii)), rewritten to the production host at posting.
- **Verify:** Read candidate L18–20; diff hunk 1.
- **Disposition:** DISPOSITIONED (draft-host form, class (iii)).

### 4. Fonts and assets

- **What:** None — no font or asset URL was changed. The CSS body, including its two `cdn.scpwiki.com` Jost @font-face URLs, is byte-identical to code/1.
- **Why:** The original's font host is already an allowed delivery host; changing it would be churn.
- **Verify:** Diff hunk 2/3 show only the code-block wrapper changing around unchanged CSS.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** None — the theme owns the header/sidebar furniture; this component only supplies the hovertip style.
- **Why:** Receiver pages carry no site-furniture declarations of their own.
- **Verify:** No `#header`/`#side-bar` rules in the diff.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** The description and footnote jokes in the original component page are not present in this mirror: original.txt is the code/1 CSS, not the prose page. The candidate's JP prose is porter-written orientation, not a translation of a frozeen source line.
- **Why:** The frozen mirror is the CSS the candidate ports, so there is no source prose to pair with the candidate's prose.
- **Verify:** Compare original.txt (pure CSS) to candidate L19–44.
- **Disposition:** Standing; porter-written text only.

### 7. Links

- **What:** None — no prose links. The source URL appears only inside the provenance comment.
- **Why:** No dead-reference or link target was introduced.
- **Verify:** `grep -n 'http' candidate.txt` shows the source reference and the draft-host import only.
- **Disposition:** N/A.

### 8. Structure

- **What:** The original CSS is wrapped in `[[code type="CSS"]]` … `[[/code]]` and the whole is gated by `[[iftags +component]]` … `[[/iftags]]` (candidate L45, L141–143).
- **Why:** The receiver form needs a code block to hold verbatim CSS and a tag gate so it renders only on component-tagged pages, mirroring the original's `+组件` gate.
- **Verify:** Diff hunk 1 and the tail hunk at candidate L138–143.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** None — CSS body bytes are unchanged; no re-indentation or whitespace churn in the ported content.
- **Why:** The port is verbatim by design.
- **Verify:** Diff hunk 2 shows unchanged CSS lines as context only.
- **Disposition:** N/A.

### 10. Porter annotations

- **What:** The provenance header is the porter's only annotation; it is load-bearing for the receiver's identity.
- **Why:** R2: porter-added text is part of the change record.
- **Verify:** Read candidate L1–17.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Draft-host self-delivery (Delivery) is the one class to disposition; foreign includes, fonts, and asset re-hosting do not arise because the mirror is the CSS itself.
- **Why:** AGENTS.md §3 classes; nothing here is a display defect.
- **Verify:** See Delivery section.
- **Disposition:** DISPOSITIONED (class (iii)); no other exception needed.

## Verification

- `cmp review/betterbetterfootnote-jp/candidate.txt pages/component:betterbetterfootnote-jp.txt` succeeds (byte-identical).
- `sha256sum review/betterbetterfootnote-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

