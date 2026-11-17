# NEGATIVE-LEDGER — unfiled observations and recipe misses

Records what a sweep or review looked for and did not file: recipe
misses (a recipe that could not decide, or decided wrongly) and
observations that matched no pattern and founded no pattern. Each
entry carries the recipe version (pattern ID plus the commit or sweep
that ran it) and the miss kind. A miss can mean the recipe was wrong;
it is never silently read as "nothing there". See SWEEP-PROTOCOL.md.

## Entries

### NL-01 — A13 retracted set 1 (single-channel audit)
- Recipe version: pre-patterns A13 review pass, 2026-11-17 (sigma10-review-20261117 findings/A13.md, initial form)
- Miss kind: recipe-wrong
- Record: the A13 review's first candidate-CSS audit read only one CSS channel and produced a false inconsistency set, retracted after the two-channel correction (both channels parsed, resolved base subtracted). The corrected method is the protocol's two-channel rule.

### NL-02 — A13 retracted set 2 (single-channel audit)
- Recipe version: pre-patterns A13 review pass, 2026-11-17 (sigma10-review-20261117 findings/A13.md, initial form)
- Miss kind: recipe-wrong
- Record: a second false inconsistency set from the same single-channel pass, likewise retracted. Two independent fabrications from one method defect is why single-channel absence claims are invalid, not merely weak.

### NL-03 — KB-23-1 literal-grep miss
- Recipe version: KB-23 @ 5eb3957, run by SWEEP-B (2026-11-17)
- Miss kind: recipe-wrong (fixed in v2)
- Record: the literal candidate-text grep for fixed min-width found NONE of the pattern's 11 confirmed instances; the overflow arrives via base-family membership. The v2 recipe is family-first (own declarations, base declarations, family membership). Companion gap KB-23-2: black-diamond, chaos and cosmos are confirmed with no repo-visible signal under any layer.

### NL-04 — KB-29-1 total recipe failure
- Recipe version: KB-29 @ 5eb3957, run by SWEEP-B (2026-11-17)
- Miss kind: recipe-wrong
- Record: both confirmed instances (broken-world, magicity) lack the recipe's assumed interwiki hiding rule; the recipe's hits are a cosmetic icon shape instead. The pattern is reclassified render-only in v2 (Status: adopted (render-only)); the static recipe is marked non-working in the pattern file.

### NL-05 — KB-31-1 measured instances missed
- Recipe version: KB-31 @ 5eb3957, run by SWEEP-B (2026-11-17)
- Miss kind: recipe-wrong
- Record: neither measured instance (cosmos, space) carries a fixed modalbox width; the confirmed overflow mechanism is modal content or positioning. The fixed-width risk set (8 themes) stands, but a clear result under this recipe is the weakest in the sweep.

### NL-06 — KB-28-1 same-rule pairing incomplete
- Recipe version: KB-28 @ 5eb3957, run by SWEEP-B (2026-11-17)
- Miss kind: recipe-incomplete
- Record: same-rule foreground/background pairing misses cross-rule composition, the confirmed mechanism for old-money-theme and kitchen. A variable-pair auxiliary added in v2 catches kitchen only; old-money-theme remains missed by both (its pair appears as literals nowhere in its candidate file).

### NL-07 — KB-42 namespace-identifier false-positive class
- Recipe version: KB-42 @ 5eb3957, run by SWEEP-C (2026-11-17)
- Miss kind: recipe hazard (false-positive class)
- Record: a raw grep for http:// inside CSS channels returns 319 hits dominated by w3.org namespace identifiers (http://www.w3.org/2000/svg, .../1999/xlink). Those are XML namespace identifiers, not fetched URLs. Every http recipe must classify by context and exclude namespace identifiers before counting; the fetched-asset count for KB-42 is 7 files / 25 assets, not 319.

### NL-08 — Translated CSS comments (porter-visible text)
- Recipe version: KB-18 @ patterns v2 (0eef991), documentation-pass taxonomy classification (2026-11-17)
- Miss kind: observation, no pattern founded (known non-finding)
- Record: the taxonomy classification found CSS comments translated in place across the sample (sodium, uiu-bhl-theme, ink, magazine comment blocks). Comments are porter-visible only; they render for no reader, so they sit outside KB-18's defect surface even after its string-variable extension. Recorded so future sweeps do not file comment translation as an untranslated-text miss in either direction: translated comments are not a finding, and untranslated comments are not a KB-18 charge. The explanation model carries comment translation in its Text translation section for completeness.

### NL-09 — Porter annotation additions
- Recipe version: documentation-pass taxonomy classification (2026-11-17); no pattern recipe covers the shape
- Miss kind: observation, no pattern founded (known non-finding)
- Record: candidates carry text with no original counterpart added by the porter: [!-- ... --] translator notes (magazine's collapsible-sidebar provenance note) and editor lines ("Edited for SCP-JP by..." in penumbra). P10 sanctions **訳注:** footnotes in body text; it does not name the comment-form annotations or editor lines. These are legitimate port apparatus, not defects and not translation residue; they belong to the review protocol (the explanation's Porter annotations section), where they are listed so they are never mistaken for original content. Recorded so a diff census does not file them as unexplained additions.

### NL-10 — Wholesale re-indentation defeats follow-up diffs
- Recipe version: documentation-pass taxonomy classification (2026-11-17); localize.md's closing structural rule is the governing text
- Miss kind: observation, no pattern founded (disclosure duty, not a defect)
- Record: uiu-bhl-theme's candidate re-indents wholesale (107 of the sample's 142 whitespace-only change blocks; tab-to-space), and whitespace-only change is 9.3% of all sampled blocks. Re-indentation changes no rendering, so it is not a theme defect; its cost lands on the next reviewer, because a follow-up diff against the original no longer applies cleanly, against the spirit of localize.md's closing rule (structure preserved so follow-up diffs apply). Not a pattern: the remedy is disclosure, not repair. Explanations state whitespace and re-indentation block and line counts in their Formatting-only section, so the hazard is on record per theme.
