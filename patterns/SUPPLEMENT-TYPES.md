# SUPPLEMENT-TYPES — the JP localization supplement catalogue (A13)

Reference for KB-11 and KB-16 and for any supplement sweep. Source:
sigma10-review-20261117 findings/A13.md, which classified all 105
candidate/original pairs present in the repo (structural features) and
hand-read 16 pairs. A candidate is the original theme plus these
supplements; inverting each type (finding candidates that lack a
supplement their siblings carry) is how the A13 instance sets in
KB-11, KB-16, KB-63 and KB-64 were produced.

| # | Supplement type | Count (of 105 pairs) | Notes |
|---|---|---|---|
| T1 | Credit block: `:scp-jp:credit:start-preview` include with translated credit prose | 104 | Sole exception: min-theme-jp (JP original, named exception). |
| T2 | Tag localization: `[[iftags +theme]]` becomes `[[iftags +テーマ]]` | 105 | Universal, no exceptions. |
| T3 | Own-code delivery via `:scp-jp:component:interwiki-style` with layered `priority=` params | 103 | Exceptions: min-theme-jp, rok-gov-theme-jp (named exceptions). |
| T4 | JP license box: `license-box-backend` plus `license-box-end` | 54 | Added in 44 pairs whose originals had none: a systematic supplement, not a swap. See KB-63 for the dropped set. |
| T5 | Japanese font: Noto Sans JP (@import URL form or font-family form) | 81 | 13 further candidates declare no font-family and inherit the site theme's fonts. See KB-16 for the override-without-Noto set. |
| T6 | Header/site-title variables: `--header-title` / `--header-subtitle` | 58 | Japanese `content:` strings appear in 9 candidates. Header language itself is out of scope for migration correctness (KB-57). |
| T7 | Credit-module CSS (`.creditRate`, `.creditButton`, `.rate-box-with-credit-button` surfaces) | 54 candidates (53 originals) | Canonical form below. See KB-11 / KB-12 / KB-62. |
| T8 | Component swaps to JP ports | sigma-plus-jp: 6; rok-gov-base-jp: 1; betterfootnotes via `:scp-jp:`: 3 | See KB-64 for the bare-include bypass set and KB-07 for the dropped footnote include. |
| T9 | Base delivery from JP distributions | pattern, not counted once | BHL family: `scp-jp.github.io/Black-Highlighter` CSS as interwiki-style `theme=` URLs. Basalt family: @import of theme:basalt-jp's `local--code`. |
| T10 | Remote-original layering (candidate layers the live original's code by URL) | 2 | animal-instead-of-beast-jp, path-of-jinin-jp. Merged into KB-14 as a variant. |
| T11 | Mobile / @media rules | no supplement pattern | Recorded NEGATIVE result: after the two-channel correction (A13-9), no pair loses its original's @media rules and no JP-specific mobile supplement pattern exists. Responsive rules arrive with the bases. Do not re-chase this. |
| T12 | http:// residue in candidates | 13 files | All prose or license links except one CSS asset (admo-jp, merged into KB-42). Own-code `local--code` URLs on the EN host: 0 (that rewrite is universal). |

## T7 canonical form: the basalt 8-selector credit set

The canonical credit-module supplement lives in the JP base:
`pages/theme:basalt-jp.txt` lines 1761-1763 carry an 8-selector
supplement set over the credit-module surfaces (`.creditRate`,
`.creditButton`, `.rate-box-with-credit-button`), with the explanatory
comment: "The frozen JP component markup emits .creditButton > a,
while the source Basalt rules cover .creditButton > p > a. Keep this
correction scoped to those two current credit-module containers."
Basalt descendants inherit the set by importing basalt-jp's code.
Standalone carriers include anon-jp (full set including
`.close-credits`, `.credit-back`, `.creditButton p a`),
ambrose-chapter-two-jp (`.creditRate` plus `.fa-info` styling) and
angel-jp (single selector `#page-content .rate-box-with-credit-button`).
Added where the original had none: basalt-jp, gp-refresh-jp. Dropped
where the original had it: exactly one pair, share-future-community
(KB-11 confirmed set).
