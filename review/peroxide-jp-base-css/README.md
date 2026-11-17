# Review package — fragment:peroxide-jp-base-css + fragment:peroxide-jp-elements-css (one record)

**Kind:** standalone fragment pair (CN Wikidot original) — split CSS delivery  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | scp-wiki-cn.wikidot.com theme:peroxide at rev 27 (page wrapper; CSS delivered from oxygennine.github.io) | `pages/fragment:peroxide-jp-base-css.txt` + `pages/fragment:peroxide-jp-elements-css.txt` |
| Host / wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | theme:peroxide | fragment:peroxide-jp-base-css + fragment:peroxide-jp-elements-css (one record) |
| Revision | rev 27 | — |
| Source of this copy | mirror `R/review-mirrors/orig-peroxide-rev27.txt` (frozen CN page source); the delivered CSS is cached at `stage2-lanes/lane-oc-audit-inline/cache/externals/oxygennine.github.io__Peroxide__peroxide.css` (fetched once 2026-11-16) and at `stage2-lanes/lane-oc-cn12/evidence/peroxide/css-as-shipped.css` | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 450 / 14,311 | 3293 / 111,817 (candidate-2: 2889/110867) |
| SHA-256 | `e532c954ae59923d454b89ddc8bcd23bf057c585581e6b0b3290d86df6d422e5` | `943b542fac7ba648318c9dfc708ba56acab33797315f44f8f7ddfafe44edba84`; candidate-2 `2d961b1567ef79afc03c236db04bb53664e2ecff1a23498b79eff5614483c82a` |

- One original against two candidate files: candidate.txt = fragment:peroxide-jp-base-css (Variables + Base), candidate-2.txt = fragment:peroxide-jp-elements-css (Elements + Capabilities + Localization).
- The dir key is `peroxide-jp-base-css` (first candidate minus its category prefix); `peroxide-jp` is already taken by the theme:peroxide-jp theme package and is left untouched.
- The candidate split exists because a single page cannot hold the full CSS under Wikidot's 200,000-char limit. The page-source diff therefore shows a delivery relocation; the per-side numbers are in diff.md.

## Summary

The CN Peroxide theme's CSS, vendored to the JP side and split into two fragment pages at the 200,000-char limit. The original is a thin page wrapper that @imports `oxygennine.github.io/Peroxide/peroxide.css`; the candidates carry the CSS in two code blocks with JP adaptations (Noto JP/JetBrains Mono loads, translated section comments, localized strings). One diff presents both sides: +3,208/−365 and +2,861/−422 lines. The contrast with the companion theme:peroxide-jp package is that this record documents the CSS delivery, not the theme wrapper.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Both candidate files open with JP provenance comments naming the CN source rev 27, the 2-way split, and deferring credit to theme:peroxide-jp (OxygenNine, CC BY-SA 4.0).
- **Why:** Traceability for a split machine-port record.
- **Verify:** Read candidate L1–7 and candidate-2 L1–7; diff.md sides 1–2.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit deferred to theme:peroxide-jp (author OxygenNine, CC BY-SA 4.0). The fragments add no standalone TASL fields.
- **Why:** Ruling 3 on the including theme page.
- **Verify:** Read candidate L1–7.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** None — no `[[include]]` in either candidate; the original's `:scp-wiki-cn:component:interwiki-style` includes belong to the theme wrapper (documented in the companion theme:peroxide-jp package), not to the CSS fragments.
- **Why:** Separation of concerns: this record is the CSS delivery half.
- **Verify:** `grep -n '\[\[include' candidate*.txt` returns nothing.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** TOPOLOGY: original delivers CSS from `oxygennine.github.io/Peroxide/peroxide.css` via @import inside the page; candidates re-host the adapted CSS as two local `[[code type="css"]]` fragments for draft-host `local--code` delivery. This is the primary change the diff shows.
- **Why:** P4/P5/Tier-3: the external host is not the JP candidate's own code page and the oversize limit forces a split; DIFF-PRESENTATION requires the delivery map to lead the diff for relocation cases.
- **Verify:** diff.md 'Diff' preamble and the two per-side tables; original @import lines at orig L3, L29.
- **Disposition:** Applied (relocation recorded).

### 4. Fonts and assets

- **What:** The CSS's font delivery is changed to Google Fonts with JP families (Noto Sans JP, Noto Serif JP, JetBrains Mono, M PLUS 1 Code) in the base fragment's first @import; the original's CN-hosted font references are not carried.
- **Why:** P5/P7: allowed host + JP fallback. The face names are from the ported CSS, evidenced by the diff.
- **Verify:** Read candidate L14 (font @import).
- **Disposition:** Applied.

### 5. Header, sidebar and site furniture

- **What:** No header/sidebar variable rewrite is performed here beyond the vendored CSS's own declarations; design language is left to theme:peroxide-jp (ruling 2).
- **Why:** Ruling 2: header language is not a defect.
- **Verify:** Candidate rule bodies carried from the adapted CSS.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** Section comments are translated/re-localized (e.g. `版式グローバル変数の定義`, `ベース調色盤`) and any CN display strings in the ported CSS are JP-localized; these are within the vendored CSS text.
- **Why:** T5: visible/embedded text localized in the port.
- **Verify:** Read candidate L8–20 and candidate-2 headings; diff.md sides.
- **Disposition:** Applied.

### 7. Links

- **What:** The original page's external CSS URL is retained only in the frozen mirror/provenance, not as a live @import in the candidates.
- **Why:** P11/dead-reference standard: the vendored copy is now the source of truth for the JP side.
- **Verify:** Read candidate L1–7; diff.md preamble.
- **Disposition:** Standing.

### 8. Structure

- **What:** The CSS is split into two code blocks at a section boundary (Variables+Base / Elements+Capabilities+Localization); block indices and order are preserved from the build artifact. See `stage2-lanes/lane-oc-cn12/work/build_peroxide.py` and `css-port.diff`.
- **Why:** Oversize rule: mirror the original's file separation and never inline a whole base into one page; the 200,000-char limit forced the split.
- **Verify:** diff.md per-side tables; candidate L8 / candidate-2 L8 section banners.
- **Disposition:** Applied (split recorded).

### 9. Formatting only

- **What:** The ported CSS is a reformatted/adapted text, so the diff against the page wrapper is dominated by relocation rather than line-level edits; no silent normalization is applied.
- **Why:** DIFF-PRESENTATION cross-cutting rule: raw diff is canonical; auto-class labels are heuristic.
- **Verify:** diff.md is generated with difflib autojunk off.
- **Disposition:** Standing.

### 10. Porter annotations

- **What:** The provenance comments and the split rationale are porter annotations.
- **Why:** R2.
- **Verify:** Read candidate L1–7.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** This is a Tier-3 relocation by DIFF-PRESENTATION (delivery topology differs), so the diff leads with the delivery map. No dead asset is charged: the CSS is vendored as text.
- **Why:** AGENTS.md §3; DIFF-PRESENTATION Tier 3.
- **Verify:** See Delivery/topology.
- **Disposition:** DISPOSITIONED (relocation documented).

## Verification

- `cmp review/peroxide-jp-base-css/candidate.txt pages/fragment:peroxide-jp-base-css.txt` succeeds (byte-identical). The same holds for `candidate-2.txt` against `pages/fragment:peroxide-jp-elements-css.txt`.
- `sha256sum review/peroxide-jp-base-css/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py` (peroxide: one diff presenting both candidate sides).
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

