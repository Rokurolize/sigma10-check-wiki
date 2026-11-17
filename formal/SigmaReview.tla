---------------------------- MODULE SigmaReview ----------------------------
(************************************************************************)
(* Formal verification of the sigma10-check-wiki review maintenance        *)
(* protocol, checkout 8db9331. The repo's promise is truthfulness of its   *)
(* review record. Machinery named and mirrored (see SPEC-REPORT.md):       *)
(*                                                                         *)
(*  review/build_review.py                                                 *)
(*    - assemble_stamp(): guard "A changed file must never carry a fresh   *)
(*      PASS" -> a candidate changed since the ledger verdict stamps STALE,*)
(*      never PASS.  MIRRORED BY: stamp[] written by RegenPackage using     *)
(*      StampGuard(): cand=page AND cand=verdictHash.                       *)
(*    - generate(pkg): regenerates diff.md mechanically from original.txt  *)
(*      and candidate.txt.  MIRRORED BY: diffOk[] set TRUE by RegenPackage.*)
(*    - HAND_AUTHORED_DIFFS = {license-box-theme-jp, peroxide-jp-base-css}: *)
(*      the only 2 exceptions; the model abstracts diff truthfulness with  *)
(*      a flag, which is exactly what --check compares.                     *)
(*    - --check: candidate.txt must byte-equal pages/<fullname>.            *)
(*      MIRRORED BY: Commit guard cand=page (I6).                           *)
(*  review/sources.tsv: mirror_sha256 + revision pinned per package;        *)
(*      original.txt is a byte copy of the frozen mirror.                   *)
(*      MIRRORED BY: orig[] initialized to MIRROR and immutable.            *)
(*  build_start.py + start-themes.tsv: /start generated from structured     *)
(*      rows, never hand-edited. MIRRORED BY: page[] changed only by        *)
(*      EditPage (the canonical page is the source, not hand-edited output).*)
(*                                                                         *)
(* Two packages, real names from review/sources.tsv. Abstraction choices:  *)
(*  - page content is a value in {"c0","c1"}; "byte-equal" is value equality*)
(*  - diff.md content is abstracted by diffOk[p] == (diff.md equals         *)
(*    GenDiff(original.txt, candidate.txt)); only the equality is checked. *)
(*  - verdictHash[p] is the candidate hash the external PASS verdict cites.*)
(*  - committed* variables are the committed record; they change only at    *)
(*    Commit, so the invariants are invariants OVER COMMITTED STATES.       *)
(************************************************************************)
EXTENDS TLC

CONSTANT Variant          \* numeric code for the guard configuration:
                          \* 0 BASE = true protocol (all guards intact)
                          \* 1 StampNoCompare, 2 MirrorRecopy,
                          \* 3 RegenSkip, 4 SyncSkip

BASE == 0
STAMPNOCOMPARE == 1
MIRRORRECOPY == 2
REGENSKIP == 3
SYNCSKIP == 4

V == Variant

Pkg == {"aesthetic-theme-jp", "basalt-jp"}
MIRROR == [p \in Pkg |-> "c0"]    \* frozen mirror per sources.tsv pin

PASS == "PASS"
STALE == "STALE"

VARIABLES
    page,                 \* canonical page content, pages/<fullname>.txt
    cand,                 \* candidate.txt content
    orig,                 \* original.txt content (byte copy of frozen mirror)
    diffOk,               \* diff.md == generated diff(original.txt, candidate.txt)
    stamp,                \* verdict stamp word in README.md (PASS / STALE)
    verdictHash,          \* candidate hash cited by the external ledger PASS
    cStamp,               \* committed stamp per package
    cCandEqPage,          \* committed: candidate.txt byte-equals page
    cCandEqVerdict,       \* committed: candidate unchanged since cited verdict
    cDiffOk,              \* committed: diff.md is the generated diff
    cOrigOk               \* committed: original.txt equals frozen mirror

treeVars == <<page, cand, orig, diffOk, stamp, verdictHash>>
committedVars == <<cStamp, cCandEqPage, cCandEqVerdict, cDiffOk, cOrigOk>>
vars == <<treeVars, committedVars>>

\* A fresh PASS is allowed only if the candidate byte-equals the page AND is
\* unchanged since the verdict it cites. This is assemble_stamp's guard.
StampGuard(p) ==
    IF V = STAMPNOCOMPARE
    THEN cand[p] = page[p]                         \* changed-file guard removed
    ELSE /\ cand[p] = page[p]
         /\ cand[p] = verdictHash[p]

Init ==
    /\ page = [p \in Pkg |-> "c0"]
    /\ cand = [p \in Pkg |-> "c0"]
    /\ orig = MIRROR
    /\ diffOk = [p \in Pkg |-> TRUE]
    /\ stamp = [p \in Pkg |-> PASS]       \* legitimate: c0 = c0 = c0
    /\ verdictHash = [p \in Pkg |-> "c0"]
    /\ cStamp = [p \in Pkg |-> PASS]
    /\ cCandEqPage = [p \in Pkg |-> TRUE]
    /\ cCandEqVerdict = [p \in Pkg |-> TRUE]
    /\ cDiffOk = [p \in Pkg |-> TRUE]
    /\ cOrigOk = [p \in Pkg |-> TRUE]

\* EditPage(p): a canonical page changes (build_start.py source row edited).
EditPage(p) ==
    /\ page' = [page EXCEPT ![p] = IF page[p] = "c0" THEN "c1" ELSE "c0"]
    /\ UNCHANGED <<cand, orig, diffOk, stamp, verdictHash, committedVars>>

\* SyncCandidate(p): candidate.txt recopied from the page (--check target).
\* Changing candidate.txt makes diff.md stale => diffOk[p] := FALSE.
SyncCandidate(p) ==
    /\ cand[p] /= page[p]
    /\ cand' = [cand EXCEPT ![p] = page[p]]
    /\ diffOk' = [diffOk EXCEPT ![p] = FALSE]
    /\ UNCHANGED <<page, orig, stamp, verdictHash, committedVars>>

\* RegenPackage(p): build regenerates diff.md from the two files and the
\* verdict stamp via assemble_stamp (generate(pkg) + stamp logic).
RegenPackage(p) ==
    /\ diffOk' = [diffOk EXCEPT ![p] = TRUE]
    /\ stamp' = [stamp EXCEPT ![p] = IF StampGuard(p) THEN PASS ELSE STALE]
    /\ UNCHANGED <<page, cand, orig, verdictHash, committedVars>>

\* LedgerVerdict(p): an external PASS determination recorded against a
\* specific candidate hash (the go-sign ledger verdict for this package).
LedgerVerdict(p) ==
    /\ verdictHash' = [verdictHash EXCEPT ![p] = cand[p]]
    /\ UNCHANGED <<page, cand, orig, diffOk, stamp, committedVars>>

\* MirrorRecopy(p): a refresh that recopies original.txt from the LIVE page.
\* Present ONLY in the MirrorRecopy variant; it removes the "original is
\* frozen" guard that the true protocol keeps by having no writer of orig.
MirrorRecopy(p) ==
    /\ V = MIRRORRECOPY
    /\ orig[p] /= page[p]
    /\ orig' = [orig EXCEPT ![p] = page[p]]
    /\ diffOk' = [diffOk EXCEPT ![p] = FALSE]
    /\ UNCHANGED <<page, cand, stamp, verdictHash, committedVars>>

\* Commit: a tree state becomes the committed record. True protocol guards
\* it with I2 (no unregenerated diff) and I6 (no unsynced candidate).
\* RegenSkip removes the I2 guard; SyncSkip removes the I6 guard.
Commit ==
    /\ ((V = REGENSKIP) \/ (\A p \in Pkg: diffOk[p]))
    /\ ((V = SYNCSKIP)  \/ (\A p \in Pkg: cand[p] = page[p]))
    /\ cStamp' = stamp
    /\ cCandEqPage' = [p \in Pkg |-> cand[p] = page[p]]
    /\ cCandEqVerdict' = [p \in Pkg |-> cand[p] = verdictHash[p]]
    /\ cDiffOk' = diffOk
    /\ cOrigOk' = [p \in Pkg |-> orig[p] = MIRROR[p]]
    /\ UNCHANGED treeVars

Next ==
    (\E p \in Pkg:
        \/ EditPage(p)
        \/ SyncCandidate(p)
        \/ RegenPackage(p)
        \/ LedgerVerdict(p)
        \/ MirrorRecopy(p))
    \/ Commit

Spec == Init /\ [][Next]_vars

\* -------- invariants over committed states -----------------------------
\* I1: a stamp reads PASS only when the candidate byte-equals the page and
\* is unchanged since the verdict it cites. Harm: a changed candidate
\* silently inheriting a stale PASS makes the review record lie about the
\* file that actually ships.
I1 == \A p \in Pkg: cStamp[p] /= PASS \/ (cCandEqPage[p] /\ cCandEqVerdict[p])

\* I2: diff.md is the generated diff of the package's two files. Harm: the
\* published diff describes a different file pair than the one in the tree,
\* so reviewers approve a change that is not the change committed.
I2 == \A p \in Pkg: cDiffOk[p]

\* I3: original.txt always equals the frozen mirror at the pinned revision;
\* no protocol action rewrites it. Harm: the diff baseline drifts, so the
\* review's reference point no longer matches revision mirror_sha256.
I3 == \A p \in Pkg: cOrigOk[p]

\* I6: candidate.txt byte-equals the canonical page. Harm: the port checked
\* in differs from the page the verdict was judged against, so PASS vouches
\* for bytes nobody reviewed.
I6 == \A p \in Pkg: cCandEqPage[p]
=============================================================================
