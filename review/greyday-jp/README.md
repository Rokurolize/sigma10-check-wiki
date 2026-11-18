# Review package — theme:greyday-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:greyday-jp — origin CN, population #194 [GOSIGN2-LEDGER (b) row 194]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 8c6e6551e4b056601ec7357a67954f06e69a47548ceadc0f73e075446eb350dd); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 1 warn / 2 infos (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 177; GOSIGN2-LEDGER (b) row 194]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-login (4 combos) on page and sample + runtime-hotlink site-theme chain; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-F (CN7))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN7))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 193, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 193]
- FIX5 re-judgement: items 60 (class D) FIXED, 61 (class H) FIXED — FIX5-FONTSB, commit 3911f7b: body stack rewired to loaded faces; Chinese edit-lock strings translated using petrifaction's exact accepted Japanese wording [GOSIGN2-LEDGER-SUPPLEMENT (a) items 60–61]
- Computed against: canonical commit 9e0c700e350cc97ee0f0c009d6ac8a4f6c44a595; candidate file pages/theme:greyday-jp.txt sha256:8c6e6551e4b056601ec7357a67954f06e69a47548ceadc0f73e075446eb350dd; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes). The generated stamp reads STALE because the candidate changed after the verdict was computed; the change is identified below and is two lines of the usage sweep, and this package re-derives both FIX5 closures against the current bytes |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 60 [D] (body font stack names a face loaded nowhere) and item 61 [H] (untranslated Chinese edit-lock strings) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md items 60 and 61: both **FIXED** (FIX5-FONTSB, commit 3911f7b); both re-derived from this package's bytes in the per-theme record below — both closures hold on the current file |
| The STALE cause | Commit b5cb724 (usage sweep, "usage-example references name the -jp posting names"): candidate L36 and L68, `theme:greyday` → `theme:greyday-jp` in the two escaped usage exhibits. Nothing else in the file changed after 3911f7b (`git diff 3911f7b..HEAD` is exactly those two lines) |
| Standing items | **DISPOSITIONED** — ledger §(c2) render row: hidden-login and runtime-hotlink site-theme chain; sample credit-modal preview form (KB-32). Ledger §(c3): row charges → (e), no separate P-item dispositions |
| Defect flags from this review | One minor: the visited-link exhibit at candidate L103 still names the CN page name (§7). FONTSB saw the same line as a checker warning and left it deliberately as not-a-ledger-item; the population sweep's rule cuts the other way, so it is flagged for the coordinator's call, with both records cited |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:greyday | theme:greyday-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 16, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 16 | — |
| Source of this copy | Mirror store `review-mirrors/orig-greyday-rev16.txt` (INDEX.tsv, class COPY) | Canonical file `pages/theme:greyday-jp.txt`, copied at worktree HEAD 20bb8c0; the file's last content changes are commits 3911f7b (FIX5-FONTSB) and b5cb724 (usage sweep) |
| Lines / bytes | 1,603 lines / 39,546 bytes | 1,630 lines / 43,077 bytes |
| SHA-256 | 5aadae1c458fdad5e747b90367974af58a9ed648399c7bb1b543120b5f001b83 | 6b244210624e02011bbd9d614af895771bd654e3962906038e9da815859d7a66 |

Provenance route: derived from the original at the reference revision (sources.tsv row, kind standard).

## Summary

The original delivers its stylesheet three ways at once: a head module @importing its own code fragment /1, a second `[[module css]]` at L7–61, and a third module at the tail (L1591–1602) behind blockquoted pseudo-gate lines. The candidate consolidates all of it into a single `[[code type="css"]]` block (candidate L325–1620) delivered as /1 by both the head module and the frame, which the census in §3 verifies is the correct address here. The measured churn (diff.md: 83 change blocks) is mostly that consolidation plus the exhibit-body translation. The theme carried two blocking items, one about its body font and one about its edit-lock strings; both were fixed by FIX5-FONTSB and both fixes are re-verified byte for byte below, including a direct comparison against petrifaction's accepted wording for the lock strings.

## Standing sections

### 0. Header and provenance frame

- **What:** Candidate head (L1–9): a `[[module CSS]]` @importing the candidate's own /1 on the draft host, an interwiki-style frame at priority 1 naming the same /1, the credit preview block, and `[[iftags +テーマ]]` at L9 (the original's gate at L5 reads `+版式`, the CN tag form). Classifier topology prints two module-css → code-css lines (similarities 0.94 and 0.83), one per original module body folded into the code block (§3).
- **Why:** The supplement frame is the campaign's standard delivery frame; draft-host URLs are the draft-form class (iii). The tag gate's JP form (+テーマ) matches the population's JP tag for theme pages.
- **Verify:** Read candidate L1–20 against original L1–70.
- **Disposition:** DISPOSITIONED (delivery class (ii)/(iii) family, ledger §(c1) standing classes).

### 1. Credit and attribution

- **What:** Block B3 (CREDIT-PREVIEW, TASL-FIELDS, CREDIT-PROSE): the candidate's credit block (L11–20) is the preview form with the full TASL field set, and its 著作権者 names the author: `[[*user AI_Mayca]]`. The original's credit block carries no fields at all — its body between `credit:start` and `credit:end` is the single line `N/A` (original L63–65) — so the candidate's fields are sourced from the theme's own CSS banner ("By AI_Mayca", in the code block header), which is where the port took the name. The tail license box (candidate L1622–1628, block B83) uses the population's license-box-backend component with the pointer parameter `|author=scp-wiki-cn theme:greyday の作者`; unlike gp-refresh (its §1), the credit block here names the author, so the pointer is confined to the component parameter, which is the conventional CN-port form for that component (89 canonical files use license-box-backend).
- **Why:** The credit pointer defect family is about the credit block's author field naming nobody while the original names the author; here the field names him, so the family does not bite. The original naming nobody in its own credit block is an original-state fact, recorded rather than repaired.
- **Verify:** Read candidate L11–20 and original L63–65; `grep -n 'AI_Mayca' candidate.txt` for the banner source.
- **Disposition:** No defect. The original's `N/A` credit body is original state; ledger §(c3) raised no P3 charge for this row.

### 2. Includes and components

- **What:** COMPONENT-SWAP with ESCAPED-INCLUDE fires in B7 and B13, both inside the exhibit body: the sample exhibits' component forms were swapped to the JP forms as part of the exhibit translation (adjudicated against the exhibit census; the exhibits' content is otherwise intact). The functional includes are the credit preview pair (§1), the interwiki-style frame (§0), and the license-box pair (§1), all JP forms. B3 also carries INCLUDE-REPOINT for the head-region includes. No include in the file names a page that will not exist at posting; the one stale target is a wikilink exhibit, handled in §7.
- **Why:** Component swaps to the JP component candidates are the standard localization move; EXHIBIT-RESTRUCTURE's sibling labels inside exhibits are adjudicated by census per the standing lesson.
- **Verify:** `grep -n '\[\[include' candidate.txt` and compare each target against the canonical `pages/` listing.
- **Disposition:** No defect; no ledger item covers includes for this row beyond the (e) items.

### 3. Delivery and code loading

- **What:** The candidate has exactly **one** code block (`[[code type="css"]]` at L325–1620), and both delivery lines name /1 (head module L2, frame L7): the address names the block that holds the stylesheet, so the FIX-CODEADDR matching classification holds for this theme, verified by census rather than trusted. Into that block the port folded the original's two further module bodies: the L7–61 module and the tail module (original L1591–1602, the `font-weight: 400` rules), which stand inside the block under two `/* page module css */` markers (candidate L1551–1620, block B81: DELIVERY-MOVE + RESTORATION + HEADERVAR). The tail module's original context deserves a sentence: in the original it sits after `[[/iftags]]`, wrapped in blockquoted lines `>[[ift{$boldmod}gs -版式]]` … `>[[/ift{$boldmod}gs]]` (original L1589/L1604) — inert documentation text around a live, unconditional `[[module css]]`. The candidate delivers the module's rules unconditionally inside /1, which matches the original's functional behavior; the two inert pseudo-gate lines are not reproduced, and the `boldmod=a` usage form remains documented in the exhibit at candidate L68.
- **Why:** Delivery consolidation into the page's own code block is the campaign's standard supplement topology; a parameter gate that is inert in the original creates no obligation to invent a working gate in the port (live behavior is the spec, and the original's gate does nothing).
- **Verify:** `grep -cn '\[\[code' candidate.txt` (1) and original.txt (1, at L372); read original L1587–1604 against candidate L1551–1620.
- **Disposition:** DISPOSITIONED as topology; the pseudo-gate observation is recorded here as an adjudicated non-defect.

### 4. Fonts and assets

- **What:** This is item 60's section; the full re-derivation is in the per-theme record. In brief: the delivered block's header comment (candidate L327–332) records the substitution — the original imported two sandbox webfont CSS files (FlyFlowerSong.txt and NotoSansSC-Light.txt from scpsandboxcn, about 3.5 MB, redistribution terms unclear) — and the block loads instead, from Google Fonts, Noto Sans JP, Noto Serif JP, Zhi Mang Xing and Noto Sans SC (L334–337) plus Font Awesome 6.5.1 (L338). The body rule at L379 now reads `'Noto Sans JP', 'Noto Sans SC', sans-serif` under the fix comment at L378; the string `NotoSansSC-Light` survives only in the two comments (L329, L378). B63 (FONTLOAD-CJK-STACK) is the usage prose at L311–312, updated to promise 本文フォントはNoto Sans JPです， matching the fixed body rule (the original promised Noto Sans SC). B67 (DUPIMPORT-DEL) is adjudicated in the appendix: it is the deletion of the two sandbox imports (original L383–384), i.e. the substitution itself, not a duplicate-import deletion. Two residues of the original's font world stand deliberately: `.fa-unicode span` keeps `'Noto Sans SC'` (a loaded face; FONTSB's recorded deliberate-left), and the title specimen span at L311 names `'FlyFlowerSong'` in an inline style — an exhibit label for the original's calligraphy face, whose delivered substitute in the stylesheet stacks is Zhi Mang Xing; the span is documentation text, not a delivered stack, and is recorded here so a reader is not surprised by it.
- **Why:** Pattern P7 / KB-16 (named-not-loaded faces) at patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa: item 60 was exactly that defect in the body stack, and the fix names only loaded faces. A font named in a delivered stack but loaded nowhere would be a flag; after the fix, no delivered stack names an unloaded face.
- **Verify:** `grep -n 'NotoSansSC-Light' candidate.txt` (two comment lines only); read L327–340 and L375–380; confirm each family named at L379 is loaded at L334–337.
- **Disposition:** FIXED (item 60, supplement; re-derived below). The sandbox imports' removal is part of that fix, with the porter's grounds recorded in the file itself.

### 5. Header, sidebar, and site furniture

- **What:** HEADERVAR fires in B3 (head region) and B81: the folded tail module carries a `:root` (candidate L1555–1560) setting `--header-title: "Site-CN-11"` and a Chinese subtitle — the original second module's own demo values, carried verbatim with the module (§3). They are the theme's documented example configuration inside its source exhibit region, not the port's site furniture choices.
- **Why:** Header/title language is ruling 2 territory; verbatim carriage of a module's demo values is original state, and translating another site's demo name would falsify the specimen.
- **Verify:** Read candidate L1551–1560 against original L1591–1602 and its preceding module content.
- **Disposition:** DISPOSITIONED (ruling 2 family); no furniture defect.

### 6. Text translation

- **What:** TRANSLATION-ANCHORED fires in 23 blocks and TRANS-UNANCHORED in 44 — the exhibit body is the bulk of this file, and the unanchored mass is its specimen prose, resolved by shape in the appendix. CONTENT-STRING fires in B3 and in B77–B79: the latter are item 61's edit-lock strings (candidate L1356, L1368, L1373), re-derived in the per-theme record. COMMENT-TEXT fires in B66/B69 (CSS comment translation inside the delivered block).
- **Why:** CSS `content:` strings in the lock overlay are reader-visible editor UI (KB-18 surface class, patterns @ 9c5e907); untranslated residue there was a class H charge, not a stylistic one.
- **Verify:** `grep -n 'lock-info' candidate.txt` and read the three `content:` lines; compare against `pages/theme:petrifaction-jp.txt` L921/L938 for the accepted wording.
- **Disposition:** FIXED where charged (item 61, supplement; re-derived below).

### 7. Links

- **What:** The two usage exhibits were repointed by the usage sweep (candidate L36 and L68 now name `theme:greyday-jp`; that edit is the stamp's STALE cause, Status table). One stale target remains: the link-style exhibit at candidate L103, `[# 未訪問リンク]（[[[greyday|訪問済みリンク]]]）`, names the CN page name `greyday`, which will not exist on scp-jp. It is a visited-link colour specimen, not an install instruction. FONTSB's lane saw this line as the checker's `link-target-missing` warning (its L103) and left it deliberately, recording that it is not among this theme's ledger items; the later population sweep repointed the two include exhibits in this same file but not this link exhibit.
- **Why:** The sweep's rule (a remaining plain-form reference naming a page that will not exist is a defect) and FONTSB's recorded deliberate-left conflict on this one line; the package records both and flags it rather than silently passing it.
- **Verify:** Read candidate L103 and the FONTSB report's greyday "Deliberately left" paragraph; `git show b5cb724` for what the sweep did and did not touch.
- **Disposition:** **Minor flag** — referred to the coordinator: either repoint the exhibit to `theme:greyday-jp` in a fix lane, or record a standing disposition for link-style exhibits. Not edited here.

### 8. Structure

- **What:** EXHIBIT-RESTRUCTURE fires once (B65), inside the exhibit body; adjudicated against the exhibit census as exhibit alignment, with all specimen elements present on both sides. IFTAGS fires in B2 (the head gate, §0) and B82 (the tail `[[/iftags]]` at candidate L1630, closing the gate opened at L9). B76 is WS-ONLY (§9). B62 is the residue block, adjudicated in the appendix.
- **Why:** Structure labels inside a translated exhibit body are expected heuristic mass; the census, not the label, decides.
- **Verify:** The block list in classification.json against the two files' section maps.
- **Disposition:** No structural defect.

### 9. Formatting only

- **What:** One block, B76, is WS-ONLY: a whitespace-only alignment difference inside the delivered block. It is the only formatting-only change in the pair.
- **Why:** Ground stated from classification.json's label spans, as required.
- **Verify:** classification.json, block B76.
- **Disposition:** No effect; nothing to disposition.

### 10. Porter annotations

- **What:** Two porter annotations stand in the delivered block: the header comment (candidate L327–332) explaining the font substitution and its grounds (sandbox files' size and unclear redistribution terms), and the item-60 fix comment at L378 stating that the original's NotoSansSC-Light load was deleted and is undelivered. Both are accurate against the bytes (§4). COMMENT-TEXT (B66/B69) otherwise covers the base stylesheet's own comments in translation.
- **Why:** Annotations are part of the delivered record; these two carry the fix's reasoning in the file itself, which is what lets a reviewer re-derive item 60 without the lane report.
- **Verify:** Read candidate L327–332 and L378.
- **Disposition:** Recorded; no ledger item covers annotations for this row.

### 11. Dispositions and exceptions

- **What:** Standing dispositions for this row: ledger §(c2) render row DISPOSITIONED in full (hidden-login on page and sample, runtime-hotlink site-theme chain; the sample's credit-modal errors are the preview-form class, KB-32 — `credit:start-preview` has no modal mechanism, GOSIGN-TESTS T2 amendment 2026-11-16). Ledger §(c3) sends this row's localize charges to (e) wholesale, so items 60/61 were the row's only blocking content. FONTSB's two deliberate-lefts (the `.fa-unicode` stack naming a loaded face; the L103 warning) are recorded in its report; §7 re-flags the second under the sweep's later rule.
- **Why:** Cited by record name, as the standing sections require; not re-argued here.
- **Verify:** GOSIGN2-LEDGER.md §(c2)/(c3) rows for theme:greyday-jp; REPORT-GOSIGN2-FIX5-FONTSB.md, greyday section.
- **Disposition:** DISPOSITIONED as cited; the §7 flag is outside these dispositions.

### 12. Verification

- **What:** Verified from the repo alone: original.txt SHA-256 equals the sources.tsv value (5aadae1c…); candidate.txt is byte-identical to the canonical file at 20bb8c0 (cmp clean, SHA-256 6b244210…); `python3 review/build_review.py --check` passes in the worktree; `git diff 3911f7b..HEAD -- pages/theme:greyday-jp.txt` shows exactly the two sweep lines, which is the whole content of the stamp's STALE. FIX5's own control: checker 7/1/2 before and after the FONTSB edit, zero new errors, all 7 pseudo-ref errors unchanged and line-shifted by one.
- **Why:** The R-fix treatment requires the closures to be checkable from the package's bytes; the STALE stamp requires the post-verdict change to be identified, which the git diff does exactly.
- **Verify:** Re-run the commands above.
- **Disposition:** Package complete; the §7 minor flag referred to the coordinator.

## Per-theme record — the FIX5 closures re-derived (ledger items 60 and 61)

**Item 60 [D] — the charge.** The body stack named `'NotoSansSC-Light'` (ledger-time candidate L378), a family loaded nowhere: the file's own comment recorded that its load had been deleted and replaced by `'Noto Sans SC'`, which the body stack did not name. Body JP text therefore matched no loaded face and fell back to the browser default (pattern P7 / KB-16, patterns @ 9c5e907).

**What the fix was supposed to change.** FIX5-FONTSB (commit 3911f7b), re-judged FIXED in supplement items 60–61: rewire the body rule to faces the file actually loads — the JP face first, the substituted SC face as fallback, plus the generic — with a comment recording why.

**Verification against the bytes.** The current body rule (candidate L379) reads `font-family: 'Noto Sans JP', 'Noto Sans SC', sans-serif;` under the fix comment at L378. Both named faces are loaded at the block's head (L334 `'Noto Sans JP'`, L337 `'Noto Sans SC'`, Google Fonts). `NotoSansSC-Light` occurs nowhere as a stack name; its two remaining occurrences are the porter header (L329) and the fix comment (L378), both explaining the substitution. The file's own usage prose now promises the same face the rule delivers (L312, §4). **Item 60 is FIXED on the bytes, as the supplement states.**

**Item 61 [H] — the charge.** Untranslated Chinese edit-lock strings in the candidate's CSS (`div#lock-info::before/::after` `content:`, ledger-time L1355/L1367/L1372) — the exclusive-lock and saving messages shown to editors, the KB-18 surface class. The one instance the campaign had repaired (petrifaction) was repaired by translation; greyday's had not been.

**What the fix was supposed to change.** Translate the three strings using petrifaction's exact accepted Japanese wording, preserving the `\\A` line breaks, the `white-space: pre-wrap` handling and the `<strong>` seconds slot between `::before` and `::after`; no selector or property changes.

**Verification against the bytes.** The three current strings (candidate L1356, L1368, L1373) are Japanese, and the two long ones are byte-identical to petrifaction's accepted lines (`pages/theme:petrifaction-jp.txt` L921 and L938): `編集中の間、他のユーザーによるこのページの編集を防ぐ15分間の排他ロックを取得しています。\\Aロックは` and `保存中です。\\Aこの表示が長い間表示されている場合、編集エリアのテキストを一時的にクリップボードに移しておくことをお勧めします。`; the middle string （秒間の無操作で期限切れになります。) completes the seconds slot as recorded. The supplement's "exact wording" claim is therefore not trusted but checked, and it holds. **Item 61 is FIXED on the bytes, as the supplement states.**

**Prose-vs-bytes note.** The supplement's FIXED verdicts were computed on the pre-sweep file; the sweep's two lines (Status table) touch neither closure, and both closures were re-verified above on the current file, so the STALE stamp does not disturb them.

## Change set outside the two diffed files

The diff covers two files; the port's record is slightly larger. (1) `pages/theme:petrifaction-jp.txt` — not a dependency, but the wording source for item 61's fix; the comparison in the per-theme record is checkable against it in this repo. (2) The decoration sample page used by the render lane for this row (RENDER-ROWS-2, RENDER-S2-F (CN7)), whose credit-modal errors are the preview-form disposition in §11. No fragment or component candidate was created for this theme; its deliveries are its own code block and the population's shared components.

## Multi-wave provenance

The candidate's current state is the product of successive waves: the S2 localization wave produced the initial port (delivery consolidation, exhibit translation, and, as later found, the broken body stack it inherited from the original's deleted load and the untranslated lock strings); FIX5-FONTSB fixed both blocking items (commit 3911f7b); the usage sweep then repointed the two usage exhibits (commit b5cb724), which is the stamp's STALE cause and the file's last change. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2)/(c3) rows and §(e) items 60/61; GOSIGN2-LEDGER-SUPPLEMENT.md items 60–61; REPORT-GOSIGN2-FIX5-FONTSB.md, greyday section. The go-sign re-run over that record is what the Status block certifies.

### Repair landed after this package was built

- Repaired by FIX-GP item 3 (record R/review-scout/FIX-GP.md), landed in commit 9e0c700: the visited-link exhibit at candidate L103 named the plain form greyday while the file's delivery layer uses theme:greyday-jp; it now reads [[[greyday-jp|訪問済みリンク]]], the single -jp insertion of the snippet-drift family. The checker's link-target-missing warn persists in its altered form (it now names greyday-jp), which the fix record adjudicates as the standing resolution-at-posting class. candidate.txt is recopied from the repaired candidate in this refresh; the regenerated stamp reads STALE, no re-judgement is fabricated, and the frozen ledger remains the verdict record.

## Appendix — residue and heuristic adjudication

- **B62** (unlabeled, the pair's one residue block): orig 354–355 → cand at 305, the `[[/div]]` / `[[/collapsible]]` boundary at the source-code exhibit's head. Alignment artifact: both files carry exactly one source-code collapsible (candidate's opens at L324), and no content is missing at either locus.
- **B64/B65** (heuristic; B65 carries EXHIBIT-RESTRUCTURE): exhibit-body alignment inside the translated specimens; census shows all specimen elements present on both sides.
- **B67** (DUPIMPORT-DEL): the label says a duplicated import was deleted; the bytes show the two sandbox webfont imports (original L383–384) removed once each as the font substitution (§4), with Font Awesome's import retained (candidate L338). Adjudicated as a mislabel of the substitution, not a duplicate deletion.
- **B76** (WS-ONLY): §9.
- The 44 TRANS-UNANCHORED blocks are the exhibit body's specimen prose (usage text, sample tables, tab and collapsible specimens), each present in both files; the 23 TRANSLATION-ANCHORED blocks are their anchored counterparts. Resolved by shape, as the standing lessons prescribe.

## License and attribution

- **Title:** 灰日 版式
- **Author:** AI_Mayca
- **Source:** https://scp-wiki-cn.wikidot.com/theme:greyday — revision 16
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
