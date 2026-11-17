# Review package — component:excerpts-tool-jp

**Kind:** standalone component port (Wikidot original) — included fragment  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | semimonth.wikidot.com component:excerpts-tool at rev 9 (2022-03-23, Etinjat, CC BY-SA 3.0) | `pages/component:excerpts-tool-jp.txt` |
| Host / wiki | semimonth.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:excerpts-tool | component:excerpts-tool-jp |
| Revision | rev 9 (2022-03-23) | — |
| Source of this copy | campaign cache `fix5-lanes/lane-func/out/semimonth-excerpts-tool-rev9.wikitext.txt` (1,915 B; fetched once during FIX5); the cache named in the candidate provenance header | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 89 / 1,915 | 99 / 2,979 |
| SHA-256 | `dd45d1dcd52628c28a28356379532c82a61ff65765b7b6af2322bcf0a06afbb0` | `dc56e67205e59dd37cb326d2884f82f710e2ccbf327ba7d6591570baab8ada30` |

- Frozen at the cited revision; no live re-fetch.
- A parallel `.txt` cache holds a minified one-line variant and is not used.

## Summary

A small excerpt-card component ported for theme:rima-jp. The markup skeleton and all parameter names are identical; the diff is six visible-label translations (Chinese → Japanese) plus a provenance comment and one escaped-include fix (`]{$title}` → `{$title}`). +17/−7 lines in 7 hunks.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–9 is a JP provenance/TASL comment naming the semimonth source, rev 9, author Etinjat, CC BY-SA 3.0, and 翻訳責任者: AI.
- **Why:** Traceability and TASL for a translated component.
- **Verify:** Read candidate L1–9; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** The header records 翻訳責任者: AI (2026), 原題 节选卡片 组件, 著作権者 Etinjat, 作成年 2022 (source rev date), ライセンス CC BY-SA 3.0, and that the change is label translation only.
- **Why:** Owner ruling 3; values from the fetched original and its revision metadata.
- **Verify:** Read candidate L1–9.
- **Disposition:** Standing; no missing eight fields.

### 2. Includes and components

- **What:** None — the include call lives in theme:rima-jp and was deliberately not edited; this page is only the included target.
- **Why:** Brief prohibition on editing includers; API compatibility is preserved by keeping parameter names.
- **Verify:** Candidate is pure markup with `{$…}` parameters; no `[[include]]` line.
- **Disposition:** N/A.

### 3. Delivery and code loading

- **What:** None — no CSS delivery channel; card styling is supplied by theme:rima-jp as in the original.
- **Why:** Division of labour is unchanged from the original.
- **Verify:** `grep -n 'module CSS\|@import' candidate.txt` returns nothing.
- **Disposition:** N/A.

### 4. Fonts and assets

- **What:** None — no font or asset URL in either file.
- **Why:** Not applicable.
- **Verify:** Diff has no `url(` lines.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** None — no header/sidebar declarations.
- **Why:** Not applicable.
- **Verify:** Diff has no site furniture.
- **Disposition:** N/A.

### 6. Visible text translation

- **What:** Six visible labels translated: 创作者→作成者, 翻译者→翻訳者, 总评分→総合評価, 章节数→章数, 评论数→コメント数, 关键词→キーワード. All `{$…}` parameter names and markup classes are untouched.
- **Why:** T5: visible text translated; parameter identity preserves the caller's API.
- **Verify:** Diff hunks 2–7 (one label each).
- **Disposition:** Applied.

### 7. Links

- **What:** None — no outbound prose links.
- **Why:** Not applicable.
- **Verify:** No `http` in diff.
- **Disposition:** N/A.

### 8. Structure

- **What:** The escaped include example in the title link is normalized from `]{$title}` to `{$title}` (candidate L10).
- **Why:** Removes a stray literal bracket in the copy-paste example without changing the markup skeleton.
- **Verify:** Diff hunk at original L6 → candidate L16.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** None — no re-indentation beyond the noted line.
- **Why:** Not applicable.
- **Verify:** Diff is six label swaps + comment + one char.
- **Disposition:** N/A.

### 10. Porter annotations

- **What:** The provenance comment is the only porter addition.
- **Why:** R2.
- **Verify:** Read candidate L1–9.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** No excludes, dead links, or draft-host references arise; every change is a translation or a one-character fix.
- **Why:** AGENTS.md §3.
- **Verify:** See Text translation and Structure.
- **Disposition:** No exception needed.

## Verification

- `cmp review/excerpts-tool-jp/candidate.txt pages/component:excerpts-tool-jp.txt` succeeds (byte-identical).
- `sha256sum review/excerpts-tool-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

