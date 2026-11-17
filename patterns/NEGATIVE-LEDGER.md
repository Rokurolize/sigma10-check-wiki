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

### NL-11 — Well-formed font host repoints and import-only families
- Recipe version: KB-04 / KB-16 @ patterns 9c5e907, patterns-wave3 extraction (2026-11-17)
- Miss kind: observation, no pattern founded (known non-finding)
- Record: several batches proposed a distinct signature for font @imports that are pure host repoints (fonts.bunny.net → fonts.googleapis.com, or bunny → Google Fonts css2 with axis expansion) whose family parameters are well-formed on both sides. These are NOT KB-04's malformed-hyphen-for-plus shape and NOT a KB-16 load gap; the family set is unchanged and nothing that renders is dropped. An import naming a family used by no stack on either side (hr-sigma / offices-sigma's `Basic`) drops nothing. Recorded so a future sweep does not file a host repoint as a malformation or a dropped-font charge (BATCH-MFRAME1 proposal 2, BATCH-MPURE1 P-5, BATCH-MPURE10 proposals 5-6, BATCH-RDISP11 proposal 4).

### NL-12 — Classifier, tooling and ledger proposals that founded no KB pattern
- Recipe version: patterns-wave3 extraction (2026-11-17); no pattern recipe founded by these proposals
- Miss kind: observation, no pattern founded (tooling/process agenda, not a KB defect)
- Record: a large family of batch proposals asks for classifier signature precision, checker/tooling refinements and ledger-generation changes without naming a new defect mechanism: DELIVERY-MOVE companion matching, same-channel pairing, drop screens and alignment-suspect tagging; CSS-BODY sub-signatures (scheme-only rewrites, :lang conversions, token deltas, segmented-widget specimens); table-cell and include-parameter anchored-translation signatures; COMPONENT-SWAP/INFO-DEL/LICENSE-BOX/GLYPH-FORM/DUPIMPORT-DEL false-fire guards; vendored-cell truncation, alias-key lookup, register-citation hygiene, relocation-aware diff counts, skeleton-from-label_spans, universal-claim census, and label-span surfacing. Where the underlying shape is a KB defect, those proposals are dispositioned AMEND or ALREADY-COVERED on the named pattern; the remaining tooling-only items are recorded here as the evidence-backed agenda for instrument work, not promoted to patterns. (36 proposals across BATCH-MPURE1/2/3/4/5/8/9/10/11/12, BATCH-RDISP2/3/6/11, BATCH-RFIX2/3/5/6/8/10, BATCH-U1/2/3/5/7/8, PKG-ALCUR.)

### NL-13 — Supersession-note and wave-attribution protocol proposals
- Recipe version: patterns-wave3 extraction (2026-11-17); governing text is localize.md / the review protocol, not a KB pattern
- Miss kind: observation, no pattern founded (process disclosure, not a defect)
- Record: batches repeatedly proposed protocol changes: sources.tsv "superseded upstream" notes whose cited artifact records revN → revN (ambrose, the-other-side, starbasalt, starry, decay, deepspace, drunken-alley, and others) should be corrected in one central commit and checked against the artifact before being written; ledger outcome lines should narrate wave edits from `git show <commit> -- <file>` (commit subjects understate mixed vehicles such as FIX2-COLON, FIX-P4, 9fbcd94); unconfirmed items should carry a resolution field; disposition text should be written from final bytes. These are documentation/process disciplines, not theme defects; recorded so a future sweep does not mint a pattern for a protocol lapse. (14 proposals.)

### NL-14 — Porter annotation observations (extension of NL-09)
- Recipe version: patterns-wave3 extraction (2026-11-17); NL-09 is the standing record
- Miss kind: observation, no pattern founded (known non-finding)
- Record: further batches recorded porter annotations and claimed facts: prose-form notes and insertion-after-`[[/code]]` heuristics (raisa-sigma, redsquare), a ported banner comment that closes at a later banner line (betwixt), annotation-truth checks where a note asserts facts the delivered bytes refute (SF-3), a prose-carrier variant (vanguard L33), and universal claims the bytes fail ("all attachments re-hosted", golden-wind; "module + code-block CSS consolidated", fmd). These are legitimate port apparatus or documentation defects handled in the explanation, not KB-18 translation residue and not a new pattern; recorded as an extension of NL-09 so a diff census does not file them as unexplained additions. (6 proposals.)

### NL-15 — Inherited http:// inside a CSS source-citation comment
- Recipe version: KB-42 @ patterns 9c5e907, patterns-wave3 extraction (2026-11-17)
- Miss kind: observation, no pattern founded (known non-finding)
- Record: andesite candidate L677 (original L675, byte-identical) carries `/* source: http://… */` — an http string inside a CSS source-citation comment. It is neither a fetched URL nor a link, and it is inherited byte-identically from the original, so it is not KB-42's class-(ii) scheme-rewrite surface and not a KB-02 dead reference. Recorded once so future sweeps do not file the shape; the package's section 11 carries it as an explained HTTP-KEPT count (BATCH-RFIX1 proposal 5).
