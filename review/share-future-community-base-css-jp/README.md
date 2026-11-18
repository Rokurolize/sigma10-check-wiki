# Review package — fragment:share-future-community-base-css-jp

**Kind:** standalone fragment port (non-Wikidot original) — vendored author-domain CSS  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | https://hoah.backroomswiki.cn/SCP/theme-share-future-community/main.css — author-domain CSS for scp-wiki-cn theme:share-future-community rev 1 | `pages/fragment:share-future-community-base-css-jp.txt` |
| Host / wiki | hoah.backroomswiki.cn | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | SCP/theme-share-future-community/main.css | fragment:share-future-community-base-css-jp |
| Revision | n/a — fetched file; CN theme:share-future-community rev 1 | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/hoah.backroomswiki.cn__SCP__theme-share-future-community__main.css` (fetched once 2026-11-16); vendored after FIX5 found the live personal-domain import | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 384 / 34,171 | 392 / 13,744 |
| SHA-256 | `a17be3118470a64f7a6875d20ed6471dc678713c41e4d35ce8b28faaff22f4ee` | `ccfe0b8266dc627ab65f9f763ead3601796940d406801b9ee4bf2482566fc5e8` |

- Provenance shape: fetched file with URL/fetch-date, not a Wikidot revision.
- The original's build-generated `sourceMappingURL` base64 comment is removed in the candidate (the only source-line deletion); images/fonts licensing stays on theme:share-future-community-jp.

## Summary

The author-domain main.css vendored as a JP fragment for theme:share-future-community-jp. The CSS rules are byte-identical; the +9/−1 delta is the provenance comment plus the `[[code type="css"]]` wrapper and removal of the build-generated `sourceMappingURL` comment. +9/−1 lines in 2 hunks.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–7 is a JP provenance comment naming the CN source rev 1, the author domain URL, the authors (hoah2333, Agent Phage), and the sourceMappingURL removal.
- **Why:** Traceability for a vendored fetched file.
- **Verify:** Read candidate L1–7; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit deferred to theme:share-future-community-jp for images/fonts licensing; the in-CSS header names the original authors, carried verbatim.
- **Why:** Ruling 3 on the consuming theme page.
- **Verify:** Read candidate L1–7 and L9–12.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — no `[[include]]` in the candidate.
- **Why:** Not applicable.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** The personal-domain import was found and vendored after FIX5; the candidate is a local fragment code page for the theme's @import, not a live @import of the author's domain.
- **Why:** P4/P5: re-hosting to the JP side; FIX5 precedent recorded in the provenance header.
- **Verify:** Read candidate L1–7; diff hunk 1.
- **Disposition:** Applied (vendoring recorded).

### 4. Fonts and assets

- **What:** The CSS's image URLs are carried as in the original (e.g. the 7buy.com/hoah header background); no image URL was rewritten in this fragment.
- **Why:** No-re-uploads standing order: asset references stay direct; deferred 404s are not defects.
- **Verify:** Diff has no `url(` change lines.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** The vendored `:root` header variables (`--header-title`, `--header-subtitle`) are carried verbatim as empty strings; no language edit (ruling 2).
- **Why:** Verbatim CSS body.
- **Verify:** Diff has no variable change lines.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** No visible text translation in the CSS; the only removed text is the non-visible `sourceMappingURL` build comment.
- **Why:** Build artifact, not UI text.
- **Verify:** Diff hunk 2 (sourceMappingURL removal).
- **Disposition:** N/A.

### 7. Links

- **What:** No outbound prose links; the author-domain URL appears in the provenance comment only.
- **Why:** Not applicable.
- **Verify:** Read candidate L1–7.
- **Disposition:** N/A.

### 8. Structure

- **What:** The CSS is wrapped in one `[[code type="css"]]` block; the sourceMappingURL comment is removed.
- **Why:** Fragment structure + remove non-functional build artifact.
- **Verify:** Diff hunks 1–2.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** None — the sourceMappingURL removal is a deliberate artifact removal, not whitespace churn.
- **Why:** Recorded explicitly in the provenance header.
- **Verify:** Diff hunk 2.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The provenance comment is the porter's annotation.
- **Why:** R2.
- **Verify:** Read candidate L1–7.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Vendoring and the sourceMappingURL removal are recorded; no dead asset is charged (deferred condition).
- **Why:** AGENTS.md §3; no-re-uploads standing order.
- **Verify:** See Delivery and Structure.
- **Disposition:** DISPOSITIONED (vendoring; deferred assets).

## Verification

- `cmp review/share-future-community-base-css-jp/candidate.txt pages/fragment:share-future-community-base-css-jp.txt` succeeds (byte-identical).
- `sha256sum review/share-future-community-base-css-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** Share Future Community Theme — main.css (author-domain CSS)
- **Author:** hoah2333, Agent Phage
- **Source:** https://hoah.backroomswiki.cn/SCP/theme-share-future-community/main.css — fetched file (no page revision); CN theme:share-future-community revision 1
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: not applicable — the fragment carries no translated prose; credit is deferred to theme:share-future-community-jp.
