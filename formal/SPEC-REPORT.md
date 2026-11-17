# SPEC-REPORT — TLA+ verification of the sigma10-check-wiki review maintenance protocol

- Date: 2026-11-18
- Brief: `formal/lane-oc-spec/BRIEF.md` (lane `lane-oc-spec`, worktree checkout `8db9331`)
- Canonical repo: `…/formal/lane-oc-spec/work` — nothing committed; all work is uncommitted
  files under `formal/`.
- Tooling verified present: `java -jar /home/roku/.local/share/tla/tla2tools.jar`
  (TLC2 Version 2026.11.15.002146, rev `bc1b506`; Java 25.0.5).
- Model: one parameterized spec `SigmaReview.tla` with constant `Variant`
  (0 = true protocol / BASE, 1 = StampNoCompare, 2 = MirrorRecopy,
  3 = RegenSkip, 4 = SyncSkip) plus one `.cfg` per variant — the
  "one spec parameterized by variant constants" option the brief permits.
- Raw outputs: `formal/results/SigmaReview{True,StampNoCompare,MirrorRecopy,
  RegenSkip,SyncSkip}.out`.
- Reproduce: `cd …/work/formal && java -jar /home/roku/.local/share/tla/tla2tools.jar -config SigmaReviewTrue.cfg SigmaReview.tla`
  (substitute the config name per variant).

## 1. Machinery named and mirrored

| Repo machinery (checked at this checkout) | Model element |
|---|---|
| `review/build_review.py` `assemble_stamp()` (line 813), guard "A changed file must never carry a fresh PASS" (lines 832–838): a candidate changed since the ledger verdict stamps STALE, never PASS | `stamp[p]` written by `RegenPackage(p)` through `StampGuard(p)`: PASS iff `cand[p]=page[p]` **and** `cand[p]=verdictHash[p]` |
| `review/build_review.py` `generate(pkg)` (line 396): regenerates `diff.md` mechanically from `original.txt` + `candidate.txt` | `RegenPackage(p)` sets `diffOk[p] = TRUE` (diff equals the generated diff of the two files) |
| `review/build_review.py` `HAND_AUTHORED_DIFFS` (line 136) = `{license-box-theme-jp, peroxide-jp-base-css}`: the only 2 hand-authored exceptions | The model abstracts diff content by the truthfulness flag `diffOk[p]` — exactly the equality `--check` compares; the 2 exceptions are outside the modeled packages |
| `review/build_review.py --check` (line 1034+): `candidate.txt` must byte-equal `pages/<fullname>` | `Commit` I6 guard `∀p: cand[p]=page[p]` |
| `review/sources.tsv` (line 1 columns `revision`, `mirror_sha256`): mirror hash + revision pinned per package; `original.txt` is a byte copy of the frozen mirror | `orig[p]` initialized to `MIRROR[p]` and never written by any true-protocol action |
| `build_start.py` + `start-themes.tsv`: `/start` generated from structured rows, never hand-edited | `page[p]` (canonical `pages/<fullname>.txt`) is the source, changed only by `EditPage(p)` |
| External go-sign ledger PASS against a specific candidate hash | `verdictHash[p]`, set by `LedgerVerdict(p)` |
| Committed tree / review record | `committedVars` snapshot, updated only by `Commit` |

Abstractions: two real package names (`aesthetic-theme-jp`, `basalt-jp`); page content in
`{"c0","c1"}` (byte equality = value equality); `diff.md` content abstracted by `diffOk[p]`;
invariants are evaluated on the `committed*` snapshot, so they are invariants over committed
states. State space is intentionally small: every TLC run finished in ~1 s (see §4).

## 2. Properties — one plain sentence each, with the harm prevented

- **I1** — A verdict stamp may read PASS only while `candidate.txt` still byte-equals the
  canonical page and is unchanged since the ledger verdict it cites; this prevents a changed
  candidate from silently inheriting a stale PASS, which would make the review record lie about
  the bytes that actually ship.
- **I2** — `diff.md` must be the mechanically generated diff of the package's two files; this
  prevents the published diff from describing a different file pair than the one committed, so a
  reviewer cannot approve a change that is not the change recorded.
- **I3** — `original.txt` must always equal the frozen mirror pinned in `review/sources.tsv` at
  the recorded revision, and no protocol action may rewrite it; this prevents the diff baseline
  from drifting away from the revision whose `mirror_sha256` the whole review rests on.
- **I6** — `candidate.txt` must byte-equal the canonical page at every commit; this prevents the
  checked-in port from differing from the page the verdict was judged against, so PASS never
  vouches for bytes nobody reviewed.

## 3. True protocol — PASS

`SigmaReviewTrue.cfg` (Variant = 0, all guards intact), `INVARIANT I1 I2 I3 I6`:

```
Starting... (2026-11-18 01:52:06)
Computing initial states...
Finished computing initial states: 1 distinct state generated
Model checking completed. No error has been found.
49717 states generated, 7056 distinct states found, 0 states left on queue.
The depth of the complete state graph search is 22.
Finished in 01s at (2026-11-18 01:52:07)
```

**Result: PASS — all four invariants hold over every reachable committed state.** No guard was
tuned to obtain this; it is the first and only run of the true config.

## 4. Broken variants — each removes exactly one guard; TLC finds a counterexample

Every variant exits 12 with `Error: Invariant <target> is violated.` Each target
invariant is listed first in its config so TLC attributes the shortest counterexample to the
guard actually removed. No variant unexpectedly passed.

### 4.1 StampNoCompare (Variant = 1) — guard removed: `assemble_stamp`'s changed-file compare

`stamp` echoes the ledger verdict (PASS) without checking that the candidate is unchanged since
the verdict it cites. Target **I1** violated. TLC: 30 distinct states, depth 5, ~1 s.

Counterexample, in the repo's words (TLC states 1–5):

1. `EditPage("aesthetic-theme-jp")` — the canonical page changes (c0→c1); `candidate.txt` is still c0.
2. `SyncCandidate("aesthetic-theme-jp")` — `candidate.txt` recopied from the page (now c1); `diff.md` is now stale.
3. `RegenPackage("aesthetic-theme-jp")` — the build regenerates `diff.md` and writes **PASS**; with the changed-file guard gone it ignores that the verdict still cites hash c0.
4. `Commit` — the committed stamp is PASS while `cCandEqVerdict = FALSE`: the candidate changed since the verdict, yet carries a fresh PASS. **I1 violated.**

### 4.2 MirrorRecopy (Variant = 2) — guard removed: `original.txt` immutability

A refresh recopies `original.txt` from the live page instead of leaving the frozen mirror alone.
Target **I3** violated. TLC: 128 distinct states, depth 6, ~1 s.

Counterexample, in the repo's words (TLC states 1–6):

1. `EditPage("aesthetic-theme-jp")` — the canonical page changes (c0→c1).
2. `SyncCandidate("aesthetic-theme-jp")` — `candidate.txt` recopied to c1, so `candidate.txt = page`.
3. `MirrorRecopy("aesthetic-theme-jp")` — `original.txt` is recopied from the live page (now c1, was c0 = the pinned mirror); `diff.md` becomes stale.
4. `RegenPackage("aesthetic-theme-jp")` — the build regenerates `diff.md`; the stamp correctly goes STALE (c1 ≠ verdict hash c0), so this is not an I1 defect.
5. `Commit` — `cOrigOk = FALSE`: `original.txt` no longer equals the frozen mirror at the pinned `revision`/`mirror_sha256`. **I3 violated.**

### 4.3 RegenSkip (Variant = 3) — guard removed: Commit's I2 condition

A commit is allowed while a package's `diff.md` is unregenerated after a sync. Target **I2**
violated. TLC: 13 distinct states, depth 4, ~1 s.

Counterexample, in the repo's words (TLC states 1–4):

1. `EditPage("aesthetic-theme-jp")` — the canonical page changes (c0→c1).
2. `SyncCandidate("aesthetic-theme-jp")` — `candidate.txt` recopied to c1; `diff.md` is now stale.
3. `Commit` — allowed without running the build; `cDiffOk = FALSE`: the committed `diff.md` still describes the old (c0) candidate while the committed candidate is c1. **I2 violated.**

### 4.4 SyncSkip (Variant = 4) — guard removed: Commit's I6 condition

A commit is allowed with an `candidate.txt` not synced to the page. Target **I6** violated.
TLC: 7 distinct states, depth 3, ~1 s.

Counterexample, in the repo's words (TLC states 1–3):

1. `EditPage("aesthetic-theme-jp")` — the canonical page changes (c0→c1); `candidate.txt` is still c0.
2. `Commit` — allowed without syncing; `cCandEqPage = FALSE`: the committed `candidate.txt` byte-differs from the canonical page. **I6 violated.**

## 5. Observations (reported, not tuned away)

- **No unexpected pass.** All four variants failed on their intended invariant on the first
  run, so there is no "check that has never failed" finding.
- **Co-violation in RegenSkip and SyncSkip.** In the shortest trace, RegenSkip also trips I1
  (`cCandEqVerdict=FALSE` beside the stale PASS) and SyncSkip also trips I1 (a PASS whose
  candidate no longer byte-equals the page). This is expected and disclosed: dropping the
  commit-time I2/I6 guard admits a committed state in which the stamp was computed against an
  earlier candidate. The true protocol precludes it because the I2/I6 commit guards force a
  `RegenPackage`/`SyncCandidate` before `Commit`, and `RegenPackage` re-evaluates the stamp. The
  variant whose removed guard is *the* I1 stamp guard (StampNoCompare) is the one attributed to
  I1; MirrorRecopy's shortest trace keeps I1 true (stamp STALE), isolating I3.
- **Tooling quirk.** This TLC build requires config constant substitution with `=`; using the
  traditional `<-` yields `Error: The configuration file substitutes for Variant with the
  undefined identifier …`. All configs therefore use `CONSTANT Variant = <n>`. This was found
  with a minimal probe spec under `/tmp/opencode` and did not require changing the model.
- **Brief-vs-checkout nuance.** The brief attributes `candidate.txt`-byte-equals-`pages/<fullname>`
  to `build_review.py --check`; in this checkout `verify.py` performs that byte check while
  `build_review.py --check` verifies diff/stamp regeneration, stamp citations and vendored
  hashes. The model folds both into the I6 commit guard; this does not change any invariant.

## 6. Deliverables

- `formal/SigmaReview.tla`, `formal/SigmaReview{True,StampNoCompare,MirrorRecopy,RegenSkip,SyncSkip}.cfg`
- `formal/results/SigmaReview{True,StampNoCompare,MirrorRecopy,RegenSkip,SyncSkip}.out`
- `formal/SPEC-REPORT.md` (this file)
- Campaign report `formal/SPEC.md` (one level up), ending `SPEC: COMPLETE`.

Nothing was committed.

SPEC-REPORT: COMPLETE
