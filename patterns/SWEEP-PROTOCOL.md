# SWEEP-PROTOCOL — how a pattern sweep works

## Purpose

Run a pattern-first static sweep across all 287 canonical theme files
(`pages/theme:*-jp.txt` and their originals) before any Playwright
work. Each pattern in this directory is one mechanism the GOSIGN2
reviews actually found, with an executable static recipe that runs in
seconds per theme. A sweep answers, per theme and per pattern, what
the repo files alone can prove. Playwright is then spent only where it
earns its cost: confirming severe cells (a reader-facing defect a
static hit predicts but cannot prove) and uncertain cells (a triage
signal, or a cell this protocol marks undecidable). Reviews stop
re-deriving the same mechanisms from scratch with the same prompts:
the mechanism, its recipe, its confirmed instances and its false
positives are already here.

## Ordering: cheapest detection first

Run patterns in detection-cost order, cheapest first:

1. **pure grep** — a single-file grep or selector scan decides the
   cell (e.g. KB-08, KB-42, KB-64, KB-65).
2. **cross-file diff** — the cell needs a comparison: candidate
   against its branch original, its resolved base, or the production
   counterpart (e.g. KB-11, KB-16, KB-63).
3. **needs live probe** — static evidence cannot decide the cell: a
   HEAD or fullname probe, a live follow-up diff, or a render
   confirmation (e.g. KB-02, KB-19, and all TRIAGE patterns KB-22 to
   KB-31 and KB-62).

Within a cost class, run file-provable patterns before triage
patterns. Record the cost class you actually used per pattern; a
recipe upgraded or downgraded in cost is a protocol change and is
noted in the pattern file.

## Result language and the claim boundary

Per theme and pattern, record one result in the go-sign vocabulary:
PASS, FINDINGS, BLOCKED-ENV, or EXCEPTION, plus, where the finding is
not the theme's own, an attribution class: candidate-inherent,
environment (the check-wiki environment layer, class D patterns), or
by-design (cross-cutting shapes, class C patterns). Capture and
measurement artefacts (class E) are never recorded as theme results.

The claim boundary is asymmetric, and it is the point of this
directory:

- A file-provable pattern hit is defect evidence. It blocks any
  completion claim for that theme in the pattern's own terms until
  the fix lands or a named disposition covers it.
- A clean static sweep never upgrades a row's claim beyond
  production-complete, as the /start hub's how-to-read defines that
  word (our-side production work: reference revision recorded, diffs
  incorporated). The TSV carries no T1-T5 verdicts, and this sweep
  does not create any. A row can be statically clean and still owe
  render, staff-procedure, or follow-up checks that live outside this
  directory.

## UNDECIDABLE-FROM-REPO is a first-class cell value

Where a candidate's operative CSS lives partly outside the repo text,
the cell value is UNDECIDABLE-FROM-REPO, and it is mandatory, not
optional. On the credit axis (axis A4 of the 2026-11-17 repository review, as
corrected by SWEEP-A2) this applies to 47 of 287 candidates: the 45
INHERIT-EXT candidates plus blackinblack and skiesmadestrange. The
v1 figure of 80 of 287 (28 percent) is SUPERSEDED by 47; other axes
count differently by definition (SWEEP-B's all-mechanism axis gives
106 of 287), and each sweep must state its axis. Named watch-list
rows (KB-11: black-serpent, internal-affairs, both INHERIT-EXT) are
undecidable on the credit axis. A
blank cell or a PASS in such a cell is a protocol violation: it
converts "the repo cannot tell" into a false clearance. An undecidable
cell is cleared only by evidence from outside the repo (the published
base file, or a render), cited in the cell.

## The two-channel rule (binding on every recipe)

Candidate CSS lives in two channels: `[[module CSS]]` blocks and
`[[code type="css"]]` blocks delivered through interwiki-style
`local--code` URLs. In the A13 pair population the split was 80 of 105
and 75 of 105, with overlap. Every recipe in this directory must parse
both channels, and must subtract the resolved base (the original, and
the JP base where one is imported) before claiming an absence. A
single-channel absence claim is invalid: the A13 review initially
produced two false instance sets this way and retracted both. The same
rule applies to selector arithmetic in inline-base pairs, where
candidate-only selectors measure base inlining, not supplements
(A13-9).

### Tolerant channel parsing (binding, beside the two-channel rule)

The two channels appear in more forms than the canonical spellings:
`[[module css]]`, `[[code type="CSS"]]`, and attributed forms such as
`[[module CSS show="true"]]` all deliver CSS. Every recipe must match
channel forms case-insensitively and tolerantly of attributes.
Evidence: SWEEP-A2 (2026-11-17) showed a case-sensitive,
attribute-less pass misclassifying 28 themes on the KB-11 axis (OWN
135 instead of 160), and the last 3 divergences all traced to
`[[module CSS show="true"]]` blocks. A recipe run with strict
spellings is a recipe-version defect, recorded in
patterns/NEGATIVE-LEDGER.md, and its absence claims are void.

## Relation to AGENTS.md section 9

Patterns cite AGENTS.md section 9 where they intersect (KB-11, KB-12
and KB-60 do today). Section 9 is the campaign's open-contradiction
list; this directory is the mechanism library. When a section 9 item
generalizes into a reusable mechanism, it migrates here as a pattern
(or a named instance set inside one), leaving a pointer in section 9.
That migration is its own separate commit, never part of a sweep run,
and a sweep never edits section 9.

## Provenance and growth

Each pattern names its evidence sources (the confirming GOSIGN2
report, coordinator adjudication, or repository-review finding) in its
header or in the merged-sections it carries. Confirmed instances are
never dropped when a pattern file is condensed. A new pattern is added
when a review confirms a new mechanism, with the confirming report
cited in the new file; numbering continues from the highest existing
KB number. A variant of an existing mechanism is merged into that
pattern as a named instance set, with the merge decision stated in the
file, rather than minted as a near-duplicate pattern.

## Brief consumption: patterns by ID plus commit hash

Lanes consume patterns by ID plus the patterns/ commit hash, reading
the files in the repository at that commit. Pattern bodies are never
copied into briefs: a copied body strips provenance, ages silently,
and cannot be corrected by a later amendment. A brief names the
pattern IDs in scope and the commit; the lane reads the files.
Proposed pattern changes go in the lane's report, never as brief-local
edits (the inherited-projection rule).

## Support counting

Each pattern header carries `Basis:` (a closed enum: measured-render,
static-diff, live-probe, owner-inspection, lane-report) and
`Support:` (the count of independent evidence bases). Distinct bases
are distinct supports; one basis cited twice is one support. A defect
arriving via AGENTS.md section 9, a pattern file, and a sweep hit
collapses to ONE support line under its dedupe key, because all three
cite the same underlying evidence; section 9-derived patterns are the
likeliest double-count source. Support may only grow from new evidence
rows, never from re-running the same sweep.

## Negative ledgers

patterns/NEGATIVE-LEDGER.md records unfiled observations and recipe
misses: observations that matched no pattern and founded no pattern
(with the reason), and cells a recipe was expected to decide but could
not (beyond the known UNDECIDABLE-FROM-REPO set). Each entry carries
the recipe version (pattern ID plus the commit or sweep that ran it)
and the miss kind, because a miss can mean the recipe was wrong rather
than that nothing was found (A13's two retracted single-channel sets
are the standing example). The negative ledger is the evidence-backed
agenda for new patterns and recipe repairs.

## Sweep outcome card (required)

Each sweep ends with a fixed outcome card, stored at
patterns/sweeps/<date>-<name>.md, with exactly these fields: cells
decided / hit / undecidable / stalled; patterns proposed / merged /
retired; and the false charges prevented by the not-a-defect classes
(C and E, counted per pattern). A sweep without its outcome card is
not complete. The card cites its source reports; where the full
reports live in the campaign record rather than the repo, the card
says so.

