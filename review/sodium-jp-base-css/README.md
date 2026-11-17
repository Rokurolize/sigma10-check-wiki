# Review package — fragment:sodium-jp-base-css

**Kind:** standalone fragment port (non-Wikidot original) — fetched CSS file  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | https://3nkv.github.io/Sodium/sodium.min.css — fetched Sodium CSS file (30,440 B, minified to 1 line) | `pages/fragment:sodium-jp-base-css.txt` |
| Host / wiki | 3nkv.github.io | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | Sodium/sodium.min.css | fragment:sodium-jp-base-css |
| Revision | n/a — fetched file, no page revision | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/3nkv.github.io__Sodium__sodium.min.css` (fetched once 2026-11-16); second copy at `stage2-lanes/lane-oc-cn14/evidence/sodium.min.css` | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 1 / 30,440 | 1636 / 41,034 |
| SHA-256 | `441e22418e334d780a7901cbdab68745d76069efa82e970ea60f10ac58f59fbe` | `c6ab8ac43abec2d3096529c3da728de509bca37d0c0de564d5cf3d858440954f` |

- Provenance shape follows the site-capture bundle: the original is a fetched CSS file with host/URL/fetch-date, not a Wikidot page revision.
- The original is minified to a single line; build_review.py therefore emits a Tier 2 diff (one +1636/−1 change block). This is a presentation artifact of the minified source, not a defect.
- theme:sodium-pentasulfide-jp receives this base through the documented two-level include chain on theme:sodium-jp (recorded in the candidate provenance header).

## Summary

The fetched Sodium CSS re-hosted as a JP fragment for theme:sodium-jp. The original is a one-line minified CSS file; the candidate is the de-minified, JP-adapted CSS in a code block (Noto Serif SC→JP, CN header text→JP, 幼圆→Yu Gothic, CN image URLs→draft-host attachments, shorthand normalization). The line diff is necessarily large because the original is one line; the substantive change is the JP adaptation, not the reformat.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–3 is a JP provenance comment naming the fetched URL and the JP adjustment list; the code block wraps the CSS.
- **Why:** Traceability for a fetched-file original.
- **Verify:** Read candidate L1–5; diff.md.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit: the CSS header inside the block names the author (Ankv) and year, carried from the fetched file; no theme-level TASL fields are added here.
- **Why:** The fragment attributes the original in-CSS; detailed licensing stays on the consuming theme pages.
- **Verify:** Read candidate L6–9 (`/* Sodium Theme … By Ankv */`).
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — no `[[include]]` in the candidate; theme:sodium-jp imports the fragment's local--code delivery.
- **Why:** P4; no cross-theme include to repoint.
- **Verify:** `grep -n '\[\[include' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** The fetched CSS is re-hosted as a JP fragment code page (`local--code/fragment%3Asodium-jp-base-css/1`) rather than imported from 3nkv.github.io — the original's host is not the JP candidate's own code page.
- **Why:** P4/P5/Tier-3: re-hosting a fetched CSS file to the JP side; DIFF-PRESENTATION's sodium exemplar is exactly this case.
- **Verify:** diff.md preamble (Tier 2) and candidate L5 `[[code type="css"]]`.
- **Disposition:** Applied (re-hosting recorded).

### 4. Fonts and assets

- **What:** Fonts: Google Fonts imports for Raleway, Ubuntu, Noto Serif JP (replacing Noto Serif SC) and JetBrains Mono are present at the block head. CN-host image URLs are repointed to `sigma10-jp-test.wdfiles.com/local--files/theme%3Asodium-jp/…`.
- **Why:** P5/P7: allowed font host + JP family; draft-bucket image URLs are a deferred campaign condition, not a defect.
- **Verify:** Read candidate L10–13; diff.md change block.
- **Disposition:** Applied; asset 404s deferred.

### 5. Header, sidebar and site furniture

- **What:** CN header strings are replaced with JP ones and `幼圆` with `Yu Gothic`; these are design-language choices carried in the adapted CSS.
- **Why:** Ruling 2 / T5: JP localization of visible CSS text.
- **Verify:** diff.md change block (JP strings).
- **Disposition:** Applied.

### 6. Visible text translation

- **What:** The minified original has no prose to translate; all visible text in the candidate is either the original's CSS comment header or JP localization strings.
- **Why:** Fetched-file originals have no documentation prose.
- **Verify:** Read candidate L6–9.
- **Disposition:** N/A.

### 7. Links

- **What:** No outbound prose links; the only URLs are CSS font/asset imports (Fonts/assets section).
- **Why:** Not applicable.
- **Verify:** diff.md change block.
- **Disposition:** N/A.

### 8. Structure

- **What:** The whole CSS is wrapped in one `[[code type="css"]]` block; block structure is the fragment's delivery unit.
- **Why:** Fragment structure requirement.
- **Verify:** Read candidate L5 and L1634–1636.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** The original being one line makes a line diff show +1636/−1 regardless of content; this is presentation, not churn. The generator's Tier 2 index labels the single block 'supplement' heuristically.
- **Why:** DIFF-PRESENTATION: auto-class labels are heuristic; the README carries the adjudicated explanation.
- **Verify:** diff.md summary table and change-block index.
- **Disposition:** Standing (presentation caveat).

### 10. Porter annotations

- **What:** The provenance comment is the porter's annotation.
- **Why:** R2.
- **Verify:** Read candidate L1–3.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Re-hosting and draft-bucket asset 404s are the disposition items; both are deferred/draft-stage, not per-theme display defects. The minified-origin diff shape is a presentation caveat.
- **Why:** AGENTS.md §3; no-re-uploads standing order.
- **Verify:** See Delivery and Formatting.
- **Disposition:** DISPOSITIONED (re-hosting; deferred assets).

## Verification

- `cmp review/sodium-jp-base-css/candidate.txt pages/fragment:sodium-jp-base-css.txt` succeeds (byte-identical).
- `sha256sum review/sodium-jp-base-css/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`. Tier 2 presentation because the original is a minified one-line file.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

