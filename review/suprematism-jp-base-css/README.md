# Review package — fragment:suprematism-jp-base-css

**Kind:** standalone fragment port (non-Wikidot original) — fetched CSS file  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | https://lemoncat233.github.io/supreroomartists/Suprematism/suprematism.css — fetched CSS file (94,086 B / 3,478 lines) | `pages/fragment:suprematism-jp-base-css.txt` |
| Host / wiki | lemoncat233.github.io | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | supreroomartists/Suprematism/suprematism.css | fragment:suprematism-jp-base-css |
| Revision | n/a — fetched file, no page revision | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/lemoncat233.github.io__supreroomartists__Suprematism__suprematism.css` (fetched once 2026-11-16) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 3478 / 94,086 | 3482 / 94,896 |
| SHA-256 | `044b0f3ab869954cefe450e26459902e6e8582af4855bbbe71e307156b14f6ad` | `d6694178bacbcf45692af562c2e76f92777f5ecd7003fe1486d8a9a32df50f1e` |

- Cross-reference the companion `review/suprematism-jp` theme package (CN origin; its related material is held there). This record is the CSS-fragment half only.
- Provenance shape: fetched file with URL/fetch-date, not a Wikidot revision.

## Summary

The fetched Suprematism CSS re-hosted as a JP fragment for theme:suprematism-jp / theme:trauma-jp. The CSS is carried almost verbatim: +11/−7 lines in 5 hunks. Changes are the provenance/comment wrapper, Noto Sans SC→JP in the import and four font stacks, and removal of the non-allowlisted Zhuque Fangsong import. Bootstrap Icons (jsDelivr) is kept.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–5 is a JP provenance comment naming the fetched URL and the font substitution; the code block wraps the CSS.
- **Why:** Traceability for a fetched-file original.
- **Verify:** Read candidate L1–5; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit is deferred to theme:suprematism-jp / theme:trauma-jp; the fragment keeps the original's in-CSS comments and adds no standalone TASL fields.
- **Why:** Ruling 3 on the consuming theme pages.
- **Verify:** Read candidate L1–5.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — no `[[include]]` in the candidate.
- **Why:** Not applicable.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** The fetched CSS is re-hosted as `local--code/fragment%3Asuprematism-jp-base-css/1` for the two themes' @import; theme-specific CSS stays in the themes' own code files (recorded in the provenance header).
- **Why:** P4/P5; division of labour between fragment and themes preserved.
- **Verify:** Read candidate L1–4; diff hunk 1.
- **Disposition:** Applied (re-hosting recorded).

### 4. Fonts and assets

- **What:** Noto Sans SC import and four font stacks (`--header-font`, `--title-font`, `--body-font`, `--ui-font`) changed to Noto Sans JP; the `chinese-fonts-cdn.deno.dev` Zhuque Fangsong import is removed (not an allowlisted direct-link host); Bootstrap Icons on jsDelivr kept.
- **Why:** P5/P7: allowed hosts and JP fallback; the removed font was not in the direct-link exception list.
- **Verify:** Diff hunks 2–5 (import + four stack lines).
- **Disposition:** Applied; removed font documented.

### 5. Header, sidebar and site furniture

- **What:** None — no header/sidebar variable language change beyond the font stacks (ruling 2 not triggered).
- **Why:** Not applicable.
- **Verify:** Diff has no `--header-title` edit.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** No visible string translation; the CSS section comments are Chinese source identifiers carried verbatim, and the original's own text was not translated in this fragment.
- **Why:** Verbatim CSS body apart from fonts; comments are not UI strings.
- **Verify:** Diff hunks show unchanged comments as context.
- **Disposition:** N/A.

### 7. Links

- **What:** None — no outbound prose links.
- **Why:** Not applicable.
- **Verify:** No `http` prose links.
- **Disposition:** N/A.

### 8. Structure

- **What:** The full CSS is wrapped in one `[[code type="css"]]` block; all other content is unchanged.
- **Why:** Fragment structure requirement.
- **Verify:** Diff hunks 1 / tail.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** None — no whitespace churn beyond the wrapper.
- **Why:** Not applicable.
- **Verify:** Diff is +11/−7.
- **Disposition:** N/A.

### 10. Porter annotations

- **What:** The provenance comment is the porter's annotation.
- **Why:** R2.
- **Verify:** Read candidate L1–5.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Re-hosting of the fetched CSS and removal of the non-allowlisted font are the disposition items; no dead asset is charged.
- **Why:** AGENTS.md §3.
- **Verify:** See Fonts/assets and Delivery.
- **Disposition:** DISPOSITIONED (re-hosting).

## Verification

- `cmp review/suprematism-jp-base-css/candidate.txt pages/fragment:suprematism-jp-base-css.txt` succeeds (byte-identical).
- `sha256sum review/suprematism-jp-base-css/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** Suprematism base CSS (suprematism.css)
- **Author:** LemonCat233 & Liurd (as credited on theme:suprematism-jp, to which this fragment defers credit)
- **Source:** https://lemoncat233.github.io/supreroomartists/Suprematism/suprematism.css — fetched file, no page revision
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: not applicable — the fragment carries no translated prose; credit is deferred to theme:suprematism-jp / theme:trauma-jp.
