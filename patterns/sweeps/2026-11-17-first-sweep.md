# Sweep outcome card — first patterns sweep, 2026-11-17

Fixed outcome card per patterns/SWEEP-PROTOCOL.md. Sources: the five
sweep reports SWEEP-A1.md (KB-01 to KB-10), SWEEP-A2.md (KB-11 to
KB-22), SWEEP-B.md (KB-23 to KB-31), SWEEP-C.md (KB-32 to KB-51) and
SWEEP-D.md (KB-52 to KB-65). The full reports live in the campaign
record, not the repo: /home/roku/.local/state/wikijump/muse-bhl/theme-port-readiness-20261114/sweep/
on the WSL host. Per-pattern numbers are in patterns/SWEEP-RESULTS.tsv.

## Card

- Patterns run: 65 of 65 (KB-01 to KB-65), cheapest first per the protocol.
- Population: 287 themes (286 candidate files plus the suffix-less FR candidate where a report counts it; KB-19 and KB-48 are undecidable over the whole population by design).
- Cells nominal: 18655 (65 patterns x 287 themes).
- Cells decided: 16794 (nominal minus undecidable).
- Cells hit: 2038 (sum of the hits column in SWEEP-RESULTS.tsv; for TRIAGE patterns this is a risk count, not a verdict count; units follow each source report, themes for most patterns, occurrences, rows or report mentions where the report counts those).
- Cells undecidable: 1861 (UNDECIDABLE-FROM-REPO and probe-pending cells, summed from SWEEP-RESULTS.tsv; includes KB-19 at 287 and KB-48 at 287 by design, and the probe queues KB-02 at 80 and KB-05 at 251).
- Cells stalled: 0 (the stalled flag needs three sweeps of one cell with an unchanged verdict and no new evidence; this is the first sweep).
- New hits: 178. Missing or fixed confirmed instances: 40.
- Patterns proposed: 0. Patterns merged: 0. Patterns retired: 0.
- Patterns amended in the v2 amendment following this sweep: 39 with content amendments, 26 with the header upgrade and a sweep citation only. Repairs: KB-42 (framing rewrite), KB-44 (threshold clarification), KB-48 (scpedia downgraded), KB-49 (caution label), KB-50 (shape-(a) wording). Growth rulings applied: KB-54 (+2), KB-59 (scope restated, 16 carriers), KB-64 (+2 files), KB-65 (recipe restated file-level, 40 files). Reclassified: KB-29 (render-only). Recipe rewrites or gap records: KB-23, KB-24, KB-25, KB-26, KB-27, KB-28, KB-30, KB-31.
- Coordinator correction carried by this sweep: the KB-11 undecidable figure is 47, superseding the v1 figure of 80 (tolerant channel parsing; 28 themes had been misclassified by a case-sensitive pass).

## Hits by class

- A. Theme defect, file-provable (KB-01 to KB-22, KB-63 to KB-65): 267 hits, 902 undecidable, 158 new, 26 missing/fixed.
- B. Theme defect, triage only (KB-23 to KB-31, KB-62): 552 risk-count hits, 672 undecidable, 0 new, 14 missing/fixed.
- C. Cross-cutting, not a defect (KB-32 to KB-39): 592 recorded occurrences or rows dispositioned not-a-defect.
- D. Environment-layer (KB-40 to KB-43): 402 recorded occurrences or rows.
- E. Capture/measurement artefact (KB-44 to KB-51): 191 recorded occurrences or rows, 287 undecidable (KB-48 by design).
- F. Named exception / standing disposition (KB-52 to KB-61): 34 verified exception carriers or census counts, 15 new (the KB-54 and KB-59 growth rulings).

## False charges prevented by the not-a-defect classes

- KB-32: 282 of 286 candidate pages are preview-form by construction, so every credit-modal machine line on those pages is dispositioned, not charged.
- KB-09 (class A, labelling rule): 43 raw both-present themes all classified as labelled exhibits, 0 charged.
- KB-44: 23 themes carry explicit transient-503 capture dispositions, so those captures are not theme results.
- KB-50: 14 ledger rows mention hidden-rate; both named shapes are dispositioned as false shapes, not defects.
- KB-33: the 884px replica band appears in 68 rows and the 337 band in 28 rows, dispositioned cross-cutting (BHL-family samples excepted, attribution open).
- KB-35, KB-36, KB-38, KB-39: subtitle doubling (4 rows, environment), the CC-badge glyph, 182 sidebar-position report mentions against the Sigma-9 baseline, and 20 contrast-mentioning rows are dispositioned by pattern rather than charged per theme.

## Counting notes

- KB-12: 0 charged; its 36 omission-shape carriers are recorded as undecidable for the charge, and 33 of them are beyond the named set (counted as new shape flags in SWEEP-RESULTS.tsv).
- KB-16: the hits column counts the 1 confirmed charged instance (aesthetic); the 69-theme unrestricted superset and the 66-theme general scan are explicitly not charges, and 23 themes sit in the outside-supply triage subset recorded as undecidable.
- KB-22: the 92-theme enumeration is itself the triage output; betwixt, ordopharm and broken-world were not reproduced at source level for mechanism reasons recorded in the pattern, and are not counted as missing confirmed instances (ordopharm and broken-world are the 2 undecidable cells).
- KB-38 (182) and KB-47 (71) count report mentions, not themes, because that is the unit their source reports count.
