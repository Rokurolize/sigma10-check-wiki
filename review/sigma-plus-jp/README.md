# Review package — component:sigma-plus-jp

**Kind:** standalone component port (Wikidot original) — receiver page  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | scp-wiki.wikidot.com component:sigma-plus, code/1 CSS at rev 38 (17,408 B / 690 lines) | `pages/component:sigma-plus-jp.txt` |
| Host / wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:sigma-plus (code/1) | component:sigma-plus-jp |
| Revision | rev 38 (the candidate's provenance header records 「rev.38 由来」) | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/scp-wiki.wikidot.com__component:sigma-plus__code__1` (fetched once 2026-11-16); a second copy is held at `stage2-lanes/lane-oc-cn9/originals/sigma-plus-code1.txt` | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 690 / 17,408 | 771 / 22,391 |
| SHA-256 | `82e0541a80d72a9d73ac69eba4479bbeccba04321b8b9ec41ac58539460f21aa` | `8da12f28750c688793cc56abda25a15588c2e381db34a7f888418d4b32e5fcd1` |

- original.txt is the code/1 CSS, not the component's prose page; that is the artifact the candidate ports verbatim.
- The two cached code/1 copies differ by trailing bytes; the one named in the candidate's provenance header is used.

## Summary

The JP receiver for EN Sigma+. The 690-line CSS body is carried verbatim in the candidate's code block; the +79/−1 delta is the receiver frame plus a translated description and TASL block. The single removed line is a tab-to-spaces normalization inside the CSS (`margin: 0`), not a semantic edit.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–18 is a JP provenance header naming the EN source, rev 38, the code/1 cache, the author and the verbatim-CSS promise.
- **Why:** Traceability for a machine receiver.
- **Verify:** Read candidate L1–18; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** A TASL-form block at candidate L20–27 names 制作: EstrellaYoshte, CC BY-SA 3.0, the source URL, rev.38, and 翻訳責任者: AI, with an explicit 翻訳について note that the CSS is unchanged.
- **Why:** Owner ruling 3: translated prose carries attribution; the CSS is declared adapted only by framing, not edited.
- **Verify:** Read candidate L20–27.
- **Disposition:** Standing; fields evidenced by the source page.

### 2. Includes and components

- **What:** None — the receiver carries no foreign include; its usage example is escaped (`@@[[include component:sigma-plus-jp]]@@`).
- **Why:** No cross-theme include to repoint.
- **Verify:** `grep -n '\[\[include' candidate.txt`.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** Self-delivery `[[module css]]` @imports `local--code/component%3Asigma-plus-jp/1` at the candidate's foot (L769–771), mirroring the original's own-code delivery.
- **Why:** P4/P6; draft-host form is sanctioned at draft stage (class (iii)).
- **Verify:** Read candidate L769–771; diff hunk 3.
- **Disposition:** DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** None — all CSS, including `scp-wiki.wdfiles.com` example-image references inside the translated prose, is carried as in the original.
- **Why:** The example image is documentation, not a live asset of the receiver.
- **Verify:** Diff hunks; the example image line is in the translated prose.
- **Disposition:** Standing; no asset edit.

### 5. Header, sidebar and site furniture

- **What:** None — Sigma+ CSS variables are carried byte-for-byte; no header language edit (ruling 2 territory not triggered).
- **Why:** Header variables live in the verbatim CSS body.
- **Verify:** Diff hunk 2/3 context.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** The original component page's descriptive prose (what Sigma+ is, developer note, example) is translated into JP at candidate L28–74; it has no counterpart in the frozen CSS mirror.
- **Why:** P10: visible prose translated; the mirror is CSS-only so the pairing is mirror-CSS → receiver frame + translation.
- **Verify:** Read candidate L28–74.
- **Disposition:** Applied (translation); no untranslated visible source line in the mirror.

### 7. Links

- **What:** None — the source URL appears only in the TASL block; the example image URL is inside escaped documentation.
- **Why:** No new outbound prose target.
- **Verify:** Read candidate L20–27, L70.
- **Disposition:** N/A.

### 8. Structure

- **What:** The verbatim CSS is enclosed in `[[code type="css"]]` and the visible frame gated by `[[iftags +コンポーネント]]`; a `[[module Rate]]` sits in a quote block.
- **Why:** Receiver structure mirrors the original's info-module/gate pattern in JP form.
- **Verify:** Diff hunk 1 and tail hunk.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** One whitespace-only change: a tab before `margin: 0` becomes four spaces (candidate L681).
- **Why:** Formatting churn from the copy path, disclosed so it is not read as a declaration change.
- **Verify:** Diff hunk 2 (`-	margin: 0;` → `+    margin: 0;`).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The provenance/TASL header is the porter's annotation.
- **Why:** R2.
- **Verify:** Read candidate L1–27.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Draft-host self-delivery is the only dispositions item; no foreign include or dead asset arises.
- **Why:** AGENTS.md §3.
- **Verify:** See Delivery.
- **Disposition:** DISPOSITIONED (class (iii)).

## Verification

- `cmp review/sigma-plus-jp/candidate.txt pages/component:sigma-plus-jp.txt` succeeds (byte-identical).
- `sha256sum review/sigma-plus-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** component:sigma-plus (code/1 CSS)
- **Author:** EstrellaYoshte
- **Source:** https://scp-wiki.wikidot.com/component:sigma-plus — revision 38; code/1 CSS
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: AI (Muse and its delegated agents), as recorded in the receiver's TASL block.
