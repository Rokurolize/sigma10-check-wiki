# Review package — component:collapsible-topbar-jp

**Kind:** standalone component port (Wikidot original) — translated component (ported 2026-11-17, ruling 4)  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | scpko.wikidot.com component:collapsible-topbar at rev 3 (2023-10-18, thd-glasses, CC BY-SA 3.0) | `pages/component:collapsible-topbar-jp.txt` |
| Host / wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:collapsible-topbar | component:collapsible-topbar-jp |
| Revision | rev 3 (2023-10-18) | — |
| Source of this copy | campaign cache `R/evidence/scpko-collapsible-topbar-rev3.wikitext.txt` (2,205 B, SHA-256 572a40518cde0dad4a0bd8fdd03d99fbc67b191e3e9564345d3768e5000e91be; fetched once 2026-11-17) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 99 / 2,205 | 127 / 4,239 |
| SHA-256 | `572a40518cde0dad4a0bd8fdd03d99fbc67b191e3e9564345d3768e5000e91be` | `5a47b9883171414ff543305f17910baeb8e899d6585ad384d9b34f1835d2c782` |

- The brief names this cache explicitly; it is frozen as original.txt with the recorded hash.
- Ported under owner ruling 4 together with theme:creature-jp, whose original included this component but whose JP candidate had dropped the include.

## Summary

A full KO→JP component translation. The markup skeleton, CSS declarations and all three parameter names (`{$maxw}`, `{$top-color}`, `{$top-bg}`) are preserved; visible prose is translated, the single CSS display string `content: "둘러보기"` becomes `"メニュー"`, and the two self-includes are repointed to the candidate name. +40/−12 lines in 3 hunks.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–22 is a JP provenance/TASL header naming rev 3, the evidence cache and its SHA-256, and the ruling-4 port rationale.
- **Why:** Traceability and TASL for a newly ported component.
- **Verify:** Read candidate L1–22; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** TASL fields are present in the frame: author thd-glasses, CC BY-SA 3.0, source URL, rev 3, 翻訳責任者: AI (2026).
- **Why:** Owner ruling 3; values from the original page.
- **Verify:** Read candidate L21–30.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** The two self-includes are repointed from `:scpko:component:collapsible-topbar` to the bare candidate name `component:collapsible-topbar-jp` (usage example and display:none fallback).
- **Why:** P1: self-reference to the JP port; bare form is the working form on the check wikis.
- **Verify:** Diff hunks at orig L15 and L99 → candidate L43 and L127.
- **Disposition:** Applied.

### 3. Delivery and code loading

- **What:** None — the component delivers its CSS inline in a `[[module CSS]]` block; no separate code page or @import was introduced.
- **Why:** Original delivery form preserved.
- **Verify:** Read candidate L51–124.
- **Disposition:** N/A.

### 4. Fonts and assets

- **What:** None — no font or asset URL in the CSS.
- **Why:** Not applicable.
- **Verify:** Diff has no `url(` lines.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** The CSS operates on `#top-bar`/`.mobile-top-bar`; no header variables were edited.
- **Why:** Not applicable.
- **Verify:** Diff CSS is declaration-identical.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** All visible Korean prose translated to Japanese (description, parameter docs). The one CSS `content:` string is translated `"둘러보기"` → `"メニュー"`.
- **Why:** T5: visible text including CSS content strings.
- **Verify:** Diff hunk 1 (prose) and hunk 2 (`content:` line).
- **Disposition:** Applied.

### 7. Links

- **What:** The source link in the frame points to the original KO page as a citation.
- **Why:** P11 reference.
- **Verify:** Read candidate L26.
- **Disposition:** Standing.

### 8. Structure

- **What:** The `iftags +구성요소` gate becomes `+コンポーネント`; the Rate quote, `module CSS` and display:none self-include structure are otherwise preserved.
- **Why:** Structure parity with the original, JP tag name.
- **Verify:** Diff hunk 1 and tail hunk.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** None.
- **Why:** Not applicable.
- **Verify:** No whitespace-only churn in diff.
- **Disposition:** N/A.

### 10. Porter annotations

- **What:** The provenance/TASL frame is the porter's annotation.
- **Why:** R2.
- **Verify:** Read candidate L1–30.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** No draft-host delivery, foreign include or dead asset is introduced; every change is a translation, a self-reference repoint, or framing.
- **Why:** AGENTS.md §3.
- **Verify:** See Text translation and Includes.
- **Disposition:** No exception needed.

## Verification

- `cmp review/collapsible-topbar-jp/candidate.txt pages/component:collapsible-topbar-jp.txt` succeeds (byte-identical).
- `sha256sum review/collapsible-topbar-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

## License and attribution

- **Title:** component:collapsible-topbar
- **Author:** thd-glasses
- **Source:** https://scpko.wikidot.com/component:collapsible-topbar — revision 3 (2023-10-18)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Change classes" in this README for what changed and why. Translator: AI (Muse and its delegated agents), as recorded in the receiver's TASL block.
