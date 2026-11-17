# Review package — component:the-buck-stops-here-base-1-jp

**Kind:** standalone component port (Wikidot original) — CSS body  
**Status:** Review package only — this record has no `sources.tsv` row and no ledger verdict. It stands outside the 287-row /start verdict; the words below are a hand-written explanation, not a generated verdict stamp.  
**Scope basis:** SITE-SCOPE.md §『The standalone components and fragments』 and the per-kind shape table; brief task line 7.

## Provenance

| | Original (frozen mirror) | Candidate (canonical) |
|---|---|---|
| Identity | scpko.wikidot.com component:the-buck-stops-here-base-1 (included by theme:the-buck-stops-here rev 29) | `pages/component:the-buck-stops-here-base-1-jp.txt` |
| Host / wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Page / file | component:the-buck-stops-here-base-1 | component:the-buck-stops-here-base-1-jp |
| Revision | component cached 2026-11-16; including theme rev 29 | — |
| Source of this copy | campaign cache `stage2-lanes/lane-oc-audit-inline/cache/externals/scpko__component__the-buck-stops-here-base-1.wikitext` (fetched once 2026-11-16) | byte copy of the canonical file at worktree HEAD `01eea37` |
| Lines / bytes | 708 / 16,101 | 660 / 14,944 |
| SHA-256 | `6653600b011d7857bcdcd98166e6a04634b7acccca0fab18aabc355146bc24f7` | `1a55e5fd57598989dc1bb539f9cc715b96393a9542ab67bf672f3365fe26d554` |

- No live re-fetch; the cached wikitext is frozen as original.txt.

## Summary

The CSS body of The Buck Stops Here component, ported for theme:the-buck-stops-here-jp. The CSS is carried byte-for-byte; the diff drops the duplicated component/theme info and usage prose, translates four section headings, and repoints five conditional `local--code` imports plus the interwiki-style theme URL from the KO host to the draft host (with the page-name colon encoded). +27/−74 lines in 9 hunks.

## Change classes

Sections follow the theme-package README's standing-class manner. Where a class does not apply, it reads `none` with its ground. Counts below are from `diff.md`, generated from these two byte-faithful files.

### 0. Framing and provenance comment

- **What:** Candidate L1–6 is a JP provenance comment naming the KO source and deferring credit to the theme page.
- **Why:** Traceability.
- **Verify:** Read candidate L1–6; diff hunk 1.
- **Disposition:** Standing.

### 1. Credit and attribution

- **What:** Credit deferred to theme:the-buck-stops-here-jp (author thd-glasses); component note lists 制作 and 画像/フォント出典 only.
- **Why:** Ruling 3 on the including theme page.
- **Verify:** Read candidate L10–19.
- **Disposition:** Standing.

### 2. Includes and components

- **What:** The original's `:scp-wiki:component:interwiki-style` include is repointed to `:scp-jp:component:interwiki-style` (candidate L600), with `theme=` moved from the KO `local--code/…` to the candidate's own draft-host code page.
- **Why:** P6: the JP production component name resolves; the draft-host theme URL is the sanctioned draft form (class (iii)).
- **Verify:** Diff hunk at original L643 → candidate L598–603.
- **Disposition:** Applied; draft-host URL is class (iii).

### 3. Delivery and code loading

- **What:** Five conditional `local--code` @import URLs are repointed from `scpko.wdfiles.com/local--code/component:the-buck-stops-here-base-1/{n}` to `sigma10-jp-test.wdfiles.com/local--code/component%3Athe-buck-stops-here-base-1-jp/{n}` (n=2..7), with `%3A` in the page-name segment.
- **Why:** P4/P6: own-code delivery on the JP draft host; colon encoding per KB-01.
- **Verify:** Diff hunks at candidate L585, L594, L600, L603, L630, L652, L654.
- **Disposition:** DISPOSITIONED (class (iii), draft form).

### 4. Fonts and assets

- **What:** None — no font or asset URL was edited; the original's Google Fonts imports are carried unchanged.
- **Why:** Allowed hosts stay as-is.
- **Verify:** Diff hunks show unchanged @import lines as context.
- **Disposition:** N/A.

### 5. Header, sidebar and site furniture

- **What:** The subtitle `content:` strings stay in Korean (`제{$n}K{$sa} 내부 데이터베이스` etc.) in the original-language modules; JP variants use Japanese in the candidate's own modules.
- **Why:** Ruling 2: header/title language is translation taste, not a defect; no change made.
- **Verify:** Read candidate L590, L626, L651.
- **Disposition:** DISPOSITIONED (header language, ruling 2).

### 6. Visible text translation

- **What:** Four section headings translated: 애니메이션 키프레임→アニメーションキーフレーム, SCP 서식 요소→SCP 書式要素, 다크 버전→ダークバージョン, and the GoI-format label; the duplicated KO info/usage prose is dropped.
- **Why:** T5; R3 (usage docs on the theme page).
- **Verify:** Diff hunks at orig L466, L481, L531, L576.
- **Disposition:** Applied.

### 7. Links

- **What:** None — no new outbound prose links.
- **Why:** Not applicable.
- **Verify:** No `http` prose links in diff.
- **Disposition:** N/A.

### 8. Structure

- **What:** The original's commented-out `[[code type="CSS"]]` exhibit is retained verbatim; `iftags +컴포넌트` → `+コンポーネント`, info/theme gates and docs dropped, CSS module structure untouched.
- **Why:** Preserve the machine CSS; drop only duplicated docs.
- **Verify:** Diff hunks 2–3.
- **Disposition:** Applied.

### 9. Formatting only

- **What:** None — CSS bytes unchanged; only wrapper/URL lines changed.
- **Why:** Not applicable.
- **Verify:** Diff is wrapper + URL edits.
- **Disposition:** N/A.

### 10. Porter annotations

- **What:** The provenance comment and translated headings are porter annotations.
- **Why:** R2.
- **Verify:** Read candidate L1–19.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Draft-host code URLs and the interwiki-style theme URL are the disposition items; no dead asset or missing include.
- **Why:** AGENTS.md §3.
- **Verify:** See Includes and Delivery.
- **Disposition:** DISPOSITIONED (class (iii)).

## Verification

- `cmp review/the-buck-stops-here-base-1-jp/candidate.txt pages/component:the-buck-stops-here-base-1-jp.txt` succeeds (byte-identical).
- `sha256sum review/the-buck-stops-here-base-1-jp/original.txt` equals the Provenance-table hash above.
- `diff.md` is present and generated from these two files by `review/build_review.py`.
- No T1/T2/T3/T4/T5 verdict is claimed here: those belong to the 287-row theme rollout, not to this record.

