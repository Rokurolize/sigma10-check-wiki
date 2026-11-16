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
optional. This applies to 80 of 287 candidates (28 percent, axis A4
of the 2026-11-17 repository review: INHERIT-EXT bases and candidates
whose operative CSS sits in attached files outside the repo), and to
named watch-list rows (KB-11: black-serpent, internal-affairs). A
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
