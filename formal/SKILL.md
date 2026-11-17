---
name: sigma10-check-wiki-verification
description: Verify sigma10-check-wiki's truthfulness invariants (verdict stamps, diffs, mirror hashes, /start consistency, lint coverage, candidate sync) with the TLA+ protocol model and the byte-level audit in formal/. Use before and after any change to review/build_review.py, review/lint_patterns.py, build_start.py, patterns/build_index.py, review/sources.tsv, start-themes.tsv, or the package generation/stamp machinery.
---

# Verify sigma10-check-wiki

The repository's promise is that its review record never lies about the bytes
it describes. Two checks guard it, both under `formal/` (read
`formal/README.md` first for the six invariants in plain words):

1. Byte-level audit of the current tree: from the repo root,
   `python3 formal/audit_repo.py`. Exit 0 is a pass with per-invariant counts;
   exit 1 names every violation; exit 2 means the vendored coverage ledger
   `formal/coverage-ledger.md` is missing, which is an instrument error, not
   a repository finding.
2. TLA+ protocol model: from `formal/`, run TLC
   (`java -jar <tla2tools.jar> -config SigmaReviewTrue.cfg SigmaReview.tla`)
   for the true protocol, which must report no error, and once per broken
   variant (`StampNoCompare`, `MirrorRecopy`, `RegenSkip`, `SyncSkip`), each
   of which must report its invariant violated. Read traces with the pstack
   `/statechart` skill.

## Coverage record

Covered code: `review/build_review.py` (stamp assembly, diff generation,
--check), `review/lint_patterns.py` (RULES, SUPPRESSIONS), `build_start.py`,
`patterns/build_index.py`, and the data contracts `review/sources.tsv` and
`start-themes.tsv`. Sync commit: the verification describes the tree at
8db9331 plus the additive `formal/` directory; `formal/README.md`
("Verification history") carries the current sync point.

## Telling a real bug from a modeling error

- An audit violation names the package, invariant, and bytes; reproduce it by
  hand (hash the file, compare the pair) before believing it. If the hand
  check disagrees, the audit's import of the machinery has drifted from the
  machinery; fix the audit, not the tree.
- A TLC counterexample on the TRUE protocol means either the protocol gained
  an action the model does not know, or a guard was genuinely weakened. Map
  the trace's actions back to `formal/SPEC-REPORT.md`'s machinery table: an
  action with no machinery counterpart is a modeling gap (extend the model);
  a trace using only modeled actions is a real protocol bug.
- A broken variant that stops failing means the variant no longer removes
  its guard (the spec drifted), not that the repository improved.

## After an intended change

If a change deliberately alters the machinery's semantics (a new stamp word,
a new exception shape), update the audit's named exceptions and the model's
guards in the same change, rerun both layers plus the four variants, refresh
`formal/audit-results.txt` and `formal/results/`, and move the sync commit in
`formal/README.md` forward. Never weaken an invariant to make a check pass;
a finding stays a finding until the bytes or the protocol actually change.
