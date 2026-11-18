# Review package — component:license-box-theme-jp

**Kind:** thin receiver (JP-native glue) — NO DIFF by design  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | counterpart named for reference only: scp-wiki.wikidot.com component:license-box-theme (4 revisions at fetch) — not a derivation base | `pages/component:license-box-theme-jp.txt` |
| Host / wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:license-box-theme (reference counterpart only) | component:license-box-theme-jp |
| Revision | 4 revisions at fetch time (no exact revision number recorded); sigma10-jp-test counterpart rev 2 also confirmed | — |
| Source of this copy | reference source cached at `gosign2-lanes/lane-oc-gs-fix3-deps-gaps/cache/scp-wiki__component%3Alicense-box-theme.json` (2026-11-17) and `stage2-lanes/lane-oc-en20/work/en-license-box-theme.txt` (92 B); original.txt holds the EN counterpart body for reference, not as a diff base | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 3 / 92 | 41 / 2,570 |
| SHA-256 | `fe760774f2d6809a88a311d8fa8a0813cbe6bc701e933c217b49143e5d057c61` | `52aefc594be622b0e606b98555ed7fff1416b9e60be23458f41b111289c8b76d` |

- SITE-SCOPE per-kind shape: thin receiver — Part 1 is a counterpart named for reference only; Part 3 (diff) is N/A because a source diff against the counterpart would show two unrelated texts and prove nothing; Part 4 (this README) is the whole record.
- The body is a three-line parameter-forwarding include of the pre-existing JP machinery `[[include :scp-jp:component:license-box-backend …]]`, which already exists on real SCP-JP and is already Japanese (deps class (a)).
- No diff.md is produced for this package. A signed statement stands in its place (below).

## Summary

A JP-native shim, not a port of the EN source text: it forwards the theme-license box's parameters to the existing JP `component:license-box-backend`. The only body difference from the EN counterpart is the site prefix `:scp-wiki:` → `:scp-jp:`; the backend is a different implementation, so no line diff is presented. The explanation is the whole record.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–34 is a JP provenance/TASL comment naming the EN counterpart, the sigma10-jp-test body check, and the role of the shim.
- **Why:** Traceability for a DEPS-created gap page.
- **Verify:** Read candidate L1–34.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** TASL fields recorded: 翻訳責任者 AI (2026), 原題 License Box (Theme), 著作権者 stormbreath, 作成年 2022, 初訳時参照リビジョン 4, 元記事リンク URL; the original page's lack of a license notice is stated as fact, and the backend's CC BY-SA 4.0/3.0 conditional notices are noted separately.
- **Why:** Owner ruling 3; values evidenced by the fetched counterpart pages, no invention.
- **Verify:** Read candidate L14–28.
- **Disposition:** Standing; honest on absent license.

### 2. Includes and components

- **What:** The entire body is one include: `[[include :scp-jp:component:license-box-backend |author={$author} |author=%%created_by%%]]` (candidate L36–41). The only change from the EN counterpart is the site prefix `:scp-wiki:` → `:scp-jp:`; the target exists on real SCP-JP with JP body (deps class (a)).
- **Why:** Ruling 4/DEPS: the JP backend is the real implementation; the shim only routes to it. The `:scp-jp:` form is correct here because the backend is a production page, not a campaign candidate.
- **Verify:** Read candidate L36–41 and candidate provenance note L22–25; compare original.txt (2-line EN counterpart).
- **Disposition:** Applied; no repoint needed.

### 3. Delivery and code loading

- **What:** None — the shim has no CSS delivery; the backend owns rendering.
- **Why:** Not applicable.
- **Verify:** No `module CSS` in candidate.
- **Disposition:** N/A.

### 4. Fonts and assets

- **What:** None — no font or asset URLs.
- **Why:** Not applicable.
- **Verify:** No `url(` lines.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** None — no header/sidebar declarations.
- **Why:** Not applicable.
- **Verify:** No site furniture.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** None — no visible text is translated: the body is a parameter-forwarding include and the EN counterpart's body is identical apart from the site prefix.
- **Why:** The explanation page is the record; there is no prose to translate.
- **Verify:** Compare candidate L36–41 to original.txt.
- **Disposition:** N/A (thin receiver).

### 7. Links

- **What:** None — no outbound prose links in the body.
- **Why:** Not applicable.
- **Verify:** No `http` in body.
- **Disposition:** N/A.

### 8. Structure

- **What:** The shim body mirrors the EN counterpart's three-line include shape; only the site prefix differs. No diff file is generated because the texts are unrelated in role, not comparable in content.
- **Why:** SITE-SCOPE Part 3 N/A: a source diff would prove nothing.
- **Verify:** See the signed statement below.
- **Disposition:** N/A (no diff by design).

### 9. Formatting only

- **What:** None.
- **Why:** Not applicable.
- **Verify:** No formatting churn.
- **Disposition:** N/A.

### 10. Porter annotations

- **What:** The provenance/TASL comment is the record's explanation.
- **Why:** R2; SITE-SCOPE Part 4.
- **Verify:** Read candidate L1–34.
- **Disposition:** The explanation is the whole record.

### 11. Dispositions and exceptions

- **What:** SITE-SCOPE Part 1 mirror is a counterpart named for reference only (original.txt holds that counterpart for citation, not as a derivation base). Part 3 is N/A. No exception to a verdict is claimed: this record stands outside the 287-row verdict.
- **Why:** Per-kind shape table, SITE-SCOPE.
- **Verify:** See the signed statement and the status line above.
- **Disposition:** N/A.

## Statement in place of a diff (signed)

No `diff.md` exists for this package, by design. The EN counterpart (`original.txt`) and the JP candidate are not two revisions of one text: the candidate is a three-line parameter-forwarding shim whose only body change is the `:scp-wiki:` → `:scp-jp:` site prefix, and whose implementation lives in the separate, pre-existing JP page `component:license-box-backend`. A line diff would compare a wrapper to a different implementation and prove nothing about the port. Per SITE-SCOPE the explanation (this README) is the whole record; Part 3 is N/A.

Signed: lane-oc-components, 2026-11-17 — review-package author. Ground: SITE-SCOPE.md per-kind shape table, thin-receiver row; candidate provenance header L1–34; candidate body L36–41.

## Verification

- `cmp review/license-box-theme-jp/candidate.txt pages/component:license-box-theme-jp.txt` succeeds (byte-identical).
- `sha256sum review/license-box-theme-jp/original.txt` equals the Provenance-table hash above.
- No diff.md by design; the signed statement above stands in its place.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** License Box (Theme) / component:license-box-theme
- **Author:** stormbreath
- **Source:** https://scp-wiki.wikidot.com/component:license-box-theme — reference counterpart, 4 revisions at fetch time (no exact revision recorded)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
  - The candidate records that the original page carries no license notice; the backend it forwards to carries conditional CC BY-SA 4.0/3.0 notices. No license is invented for the original.
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: AI (Muse and its delegated agents), as recorded in the receiver's TASL block.
