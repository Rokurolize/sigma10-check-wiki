# Review package — fragment:broken-world-jp

**Kind:** standalone fragment port (Wikidot original) — verbatim SVG logo CSS  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | scp-wiki.wikidot.com fragment:broken-world at rev 4 (2022-09-18 last edit) | `pages/fragment:broken-world-jp.txt` |
| Host / wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | fragment:broken-world | fragment:broken-world-jp |
| Revision | rev 4 (2022-09-18 last edit) | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-cn3/work/en-fragment-broken-world.txt` (fetched once during Stage 2 CN3) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 55 / 37,149 | 69 / 38,478 |
| SHA-256 | `7abb37297f0c79f7592e617a32a5939a07d7e097fa0db88e32832e72797ce581` | `8e207de1e4f5623413549ce9b30e44e579ccaf5fef3cc990c003183aa0518e2c` |

- The companion theme:broken-world-jp package (CN origin) is a different record and is left untouched; this dir uses the disambiguated key `fragment-broken-world-jp`.
- The SVG data URIs are embedded inline in the CSS; no asset upload was made (no-re-uploads standing order).

## Summary

A verbatim port of the EN Broken World logo fragment. Both original code blocks (code/1 and code/2) are carried byte-for-byte, including all six SVG data URIs; the diff is a TASL/provenance frame, the code-block markup being retyped from `[[code type="CSS"]]` to `[[code]]`, and the removal of a decorative separator comment. +21/−7 lines in 3 hunks; no CSS byte changed.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–21 is a JP provenance/TASL block naming rev 4, the two code blocks, and the credit chain (Etinjat / SunnyClockwork / Aelanna / Woedenaz, CC BY-SA 3.0).
- **Why:** Traceability and TASL for a verbatim asset fragment.
- **Verify:** Read candidate L1–21; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Full TASL block present: title, original authors, source URL, CC BY-SA 3.0, 翻訳責任者: AI, and a 翻訳について note stating this is a verbatim machine port, not a modification of an existing JP translation.
- **Why:** Owner ruling 3; credit names come from the original fragment page.
- **Verify:** Read candidate L10–20.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — no `[[include]]` in either file.
- **Why:** Not applicable.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** The fragment is delivered by `[[module CSS]] @import` on theme:broken-world-jp; the candidate keeps the two code blocks, with code/2 holding the `--Set-logo-1..6` data URIs the theme imports.
- **Why:** P4: own-code delivery; code-block structure preserved verbatim as the original's.
- **Verify:** Read candidate L22–69; diff hunks 2–3.
- **Disposition:** Applied (structure preserved).

### 4. Fonts and assets

- **What:** The logo assets are inline `data:` URIs, so there is no host to repoint and no upload to make. Byte-identical to the original.
- **Why:** No-re-uploads standing order; data URIs need no hosting.
- **Verify:** Diff hunks 2–3 show unchanged data URIs as context.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** None — no header/sidebar rules beyond the logo variables.
- **Why:** Not applicable.
- **Verify:** No site furniture in diff.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** None — no visible prose beyond the provenance comment; the CSS contains no display strings.
- **Why:** Not applicable.
- **Verify:** Diff has no translated CSS text.
- **Disposition:** N/A.

### 7. Links

- **What:** No outbound prose links introduced; the source URL is in the provenance comment only.
- **Why:** Not applicable.
- **Verify:** Read candidate L1–21.
- **Disposition:** N/A.

### 8. Structure

- **What:** The two `[[code type="CSS"]]` wrappers become `[[code]]`, the decorative `!---2222…---` separator is dropped, and `[[iftags]]`-free framing is kept; both code bodies are unchanged.
- **Why:** Presentation-only normalization; the theme imports code/2 by index, so block order/count is preserved.
- **Verify:** Diff hunks 2–3.
- **Disposition:** Applied (markup only).

### 9. Formatting only

- **What:** A few blank lines around the data URIs were collapsed; no CSS declaration changed.
- **Why:** Formatting churn disclosed.
- **Verify:** Diff hunk 3 tail (removed blank lines).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The provenance/TASL block is the porter's annotation.
- **Why:** R2.
- **Verify:** Read candidate L1–21.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Inline data URIs mean no dead asset or host disposition is required; the change set is framing and markup only.
- **Why:** AGENTS.md §3.
- **Verify:** See Structure.
- **Disposition:** No exception needed.

## Verification

- `cmp review/fragment-broken-world-jp/candidate.txt pages/fragment:broken-world-jp.txt` succeeds (byte-identical).
- `sha256sum review/fragment-broken-world-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** Broken World theme: logos (fragment:broken-world, code/1 + code/2)
- **Author:** Etinjat (broken-world theme); logo images by SunnyClockwork, Aelanna and Woedenaz
- **Source:** https://scp-wiki.wikidot.com/fragment:broken-world — revision 4 (2022-09-18 last edit)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: AI (Muse and its delegated agents) — verbatim machine port of the CSS, as recorded in the fragment's TASL block.
