# Review package — theme:scp-offices-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:scp-offices-theme-jp — origin EN, population #33 [GOSIGN2-LEDGER (b) row 33]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now b21b40a713fbb092055088bb598075fd7be67b74aa31f5e11808f34af01a5ea1); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 2 infos (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 33; GOSIGN2-LEDGER (b) row 33]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — header logo clipped at ≤768, notice left-clip, WebKit rate「価:0」missing + stray "S", sidebar x=0, "ソース" washed out (1.84), sample credit-modal + overflow 337–419px, interwiki box absent. [RENDER-ROWS-1 (RENDER-C row 33)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 33)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 33, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 33]
- FIX5 re-judgement: item 7 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: pattern-7 fix; checker code-multiset identical before/after [GOSIGN2-LEDGER-SUPPLEMENT (a) item 7]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:scp-offices-theme-jp.txt sha256:b21b40a713fbb092055088bb598075fd7be67b74aa31f5e11808f34af01a5ea1; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation over the classifier skeleton; the verdict stamp above is generated)
Candidate: review/scp-offices-theme-jp/candidate.txt (sha256 b21b40a713fbb092055088bb598075fd7be67b74aa31f5e11808f34af01a5ea1)
Original: theme:scp-offices-theme — scp-wiki, revision 58 (sha256 95a9e9447cb64165b8107d3efdc25f00261cd4949a809db64652ccb8228f8db9)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

Provenance route: adopted from the production JP counterpart (R4), the K6 shape recorded in review/sources.tsv. Body similarity (difflib, autojunk off) is 0.970 between the candidate and the production page (pages-existing/existing:theme-scp-offices-theme.txt, 550 lines) against 0.463 between the candidate and the rev 58 mirror, so most of the candidate's distance from the mirror is production drift, not porting. The mirror is review-mirrors/orig-scp-offices-theme-rev58.txt (FETCH-REGEN, 11,957 bytes, sha256 95a9e944…8db9), byte-identical to original.txt in this package and to the sources.tsv row; it is the later of the credit block's two recorded reference revisions (the candidate's credit block records 58 for both first translation and re-translation). The migration delta over production is delivered as a separate instruction page, pages/phase17-diff-scp-offices-theme-jp.txt (change set, below). The stamp above is STALE by design: the candidate changed after the verdict (the usage-example sweep line and the snippet-audit line), so the stamp's findings describe the pre-change file; the per-theme record re-verifies the blocking item on current bytes.

## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 4 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 4 |
| FONT-IMPORT | 1 |
| HEADERVAR | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 5 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 22 |
| TRANSLATION-ANCHORED | 19 |
| WS-ONLY | 66 |

Counts: 121 blocks, 98 specific, 20 heuristic, 3 residue, 0 skipped (comment text).

## Per-theme record — the FIX5 re-derivation

This theme's one blocking item is GOSIGN2-LEDGER section (e) item 7 [D] (ledger (b) row 33): pattern 7, JP body text set in a Latin-only mono stack, display-affecting; at ledger time the candidate named and loaded no JP face. GOSIGN2-LEDGER-SUPPLEMENT re-judges it FIXED (FIX5-FONTSA, canonical commit 8eacd6e: pattern-7 fix, checker code-multiset identical before/after).

Re-derived from this package's bytes and the commit itself: `git show 8eacd6e -- pages/theme:scp-offices-theme-jp.txt` is +6/−1 in the code block — the 日本語フォント porter comment (candidate lines 211–214), the Noto Sans JP load (`@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap')`, candidate line 216), and `'Noto Sans JP'` appended to `--body-font` (candidate line 231: `"JetBrains Mono", Recursive, Consolas, monaco, 'Noto Sans JP', monospace`). All three stand in the current candidate byte-identical to the commit's result. The remaining stacks alias the header font (`--header-font: var(--header-font)` at candidate line 232 is the original's own self-referential line, original line 211, carried verbatim; it is not part of the charge). The fix is present and complete; item 7 holds FIXED on current bytes.

One delivery nuance the reader needs: the fix sits in the page's code block, which in this candidate is the published theme source; the live CSS channel is production's hosted style0.css (section 3), and the migration instruction page for the production page records that font delivery stays on Google Fonts (pages/phase17-diff-scp-offices-theme-jp.txt). The ledger charged the candidate file, and the candidate file is what was fixed.

The theme's remaining ledger findings re-derive as follows (ledger (c3), LOCALIZE-B row): P3 credit fields FIXED in the credit waves (checker-verified) — the current credit block carries ten fields (section 1); P7 is item 7, closed above. The stamp's T4 count of 1 display-affecting finding is item 7.

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B5: orig 41-43 -> cand 47-59 (body -> body)

- BARE-RATE-DEL (B): Duplicate bare Rate removed (KB-09, ledger class B): the preview credit module is already rate-bearing, so a second bare Rate module double-renders the widget.
  Verify: Grep both sources for [[module Rate]]; the candidate must hold none outside labelled exhibits.
  - B5: orig 41-43 -> cand 47-59 (body -> body)

This instance: the original carries no credit block, no license box, and no info module at all (its only includes are the interwiki frames, theme-squares, and the usage exhibits). The candidate's credit block (candidate lines 48–59) carries ten fields: title SCPオフィステーマ, translator 7happy7, translation year 2020, author ©Woedenaz, copyright holder ©Woedenaz, original title SCP Offices Theme, creation year 2019, first-translation reference revision 58, re-translation reference revision 58, and the source link. The author is named, so there is no pointer defect: production's own credit block names the same person as 著者 ©[[*user Woedenaz]] (production line 49); the candidate keeps the plain ©Woedenaz form in both fields and does not carry production's [[*user]] link form, a form difference recorded here, not a misattribution. The translator credit names 7happy7 because this candidate adopts the production page's existing human translation and its credit with it; ruling 3's AI credit applies to campaign translations, and this is not one. The original's bare Rate stood in a [[>]] wrapper at original lines 41–43; it is deleted and the wrapper with it, and the preview credit block that replaces the region is rate-bearing.

## 2. Includes and components

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B14: orig 99-100 -> cand 115-116 (body -> body)

This instance: the include census is short. Head: the candidate adds the base include `[[include :scp-jp:theme:black-highlighter-theme]]` inside an ungated [[iftags]] at candidate lines 1–3; the original has no base include (it imports the BHL stylesheets directly, section 3). The interwiki frames are repointed :scp-wiki: → :scp-jp: (candidate lines 38–46 and 566–568). The theme-squares exhibit include is repointed the same way (candidate line 65). The usage example's two escaped includes (candidate lines 115–116) name `:scp-jp:theme:black-highlighter-theme` and `:scp-jp:theme:scp-offices-theme-jp`, the post-sweep posting-name forms. B14's COMPONENT-SWAP/ESCAPED-INCLUDE pairing is the BHL line of that example.

## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B1: orig 1-4 -> cand 1-9 (body -> body)
  - B120: orig 539-540 -> cand 561-563 (module-css -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B2: orig 6-6 -> cand 11-11 (module-css -> module-css)
  - B8: orig 82-82 -> cand 98-98 (body -> body)
  - B11: orig 91-91 -> cand 107-107 (body -> body)
  - B55: orig 230-230 -> cand 252-252 (code-css -> code-css)

This instance: the delivery topology changes, and the change is the production form. The original imports BHL normalize and BHL itself from nu-scptheme.github.io in its head module (original lines 3–4, frames at priority 1 and 2), and delivers its own code block from scp-wiki.wdfiles.com/local--code/theme%3Ascp-offices-theme/1 in a tail module (original lines 539–541, frame at priority 3). The candidate imports BHL from scp-jp.github.io in the head module (candidate lines 7–8, frames repointed), and its tail module and priority-3 frame import `https://scp-jp.github.io/files/theme/scp-offices-theme/style0.css` (candidate lines 562–568), production's hosted stylesheet, instead of the page's own code block. The single code block (candidate lines 209–558, one [[code type="CSS"]] block; the original likewise has exactly one, original line 194) is therefore the published source exhibit, shown in the "+ テーマコードを表示" collapsible, not the live channel. SELF-DELIVERY B120/B121 are the tail repoint in the differ's pairing. The four DRAFT-HOST lines are the --logo-image and image references to the candidate's own attachments on the draft host (candidate lines 11, 98, 107, 252): they are the T1 baseline's four pseudo-ref errors, class (iii). One of them deserves a note: the BHL logo image at candidate line 107 names black-highlighter-logo.svg inside the candidate's own file folder, where production names the same file under theme%3Ablack-highlighter-theme on scp-jp.wdfiles.com (production line 101); that is the draft-stage attachment form of this candidate, recorded, not probed as a credit link because it is an exhibit image, not a credit or source link.

## 4. Fonts and assets

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B49: orig 193-195 -> cand 208-216 (body -> body)

This instance: B49 is the code block's head. Three things happen there: the JetBrains Mono load moves from fonts.bunny.net (original line 195) to fonts.googleapis.com (candidate line 210), production's form; the FIX5 Noto Sans JP load and its porter comment are added (candidate lines 211–216, the per-theme record above); and the --body-font suffix lands in the Typefaces block (candidate line 231, the classifier's CSS-BODY B51, which is this fix and not unclassified churn). The logo asset is re-hosted from the original's scp-wiki.wdfiles.com folder to the candidate's own draft-host folder (candidate lines 11, 98, 252; section 3). No font is imported that no stack names: JetBrains Mono heads --body-font, Noto Sans JP is its appended fallback, and Recursive/Consolas/monaco are the original's Latin fallbacks carried verbatim.

## 5. Header, sidebar, and site furniture

none — no furniture signature fired over 121 change blocks. Ground: this theme's furniture is BHL's; the candidate's only head-module CSS of its own (the .scp-image-block rules, candidate lines 14–35) is carried from the original (lines 9–29) unchanged apart from the logo line. The two HEADERVAR blocks (B2, B55) are the --logo-image repoints, treated in sections 3 and 4.

## 6. Text translation

- TRANSLATION-ANCHORED (B): Anchored translation (T5): prose paired by structural anchors (headings, list markers) is translated.
  Verify: Spot-check the paired lines; an untranslated anchored line is a flag.
  - B7: orig 48-49 -> cand 64-65 (body -> body)
  - B10: orig 88-90 -> cand 104-106 (body -> body)
  - B12: orig 94-95 -> cand 110-111 (body -> body)
  - B13: orig 96-98 -> cand 112-114 (body -> body)
  - B48: orig 189-189 -> cand 204-204 (body -> body)

This instance: the documentation body and the specimen text are translated throughout; the anchored pairs above are the structurally paired samples. The Typefaces specimen sentence keeps the original's stale text as written (the original says the face in use is "IBM Plex Mono"; the applied face is JetBrains Mono) and carries the porter's translator footnote saying so (candidate line 204; section 10). The CSS comments inside the code block stay in English on both sides (in-CSS text, R1; the one COMMENT-TEXT block, B17, is a comment rewording inside a specimen).

## 7. Links

none — no link-class signature fired over 121 change blocks. Ground: the only source link is the credit block's 元記事リンク (candidate line 58), which names the original page on scp-wiki.wikidot.com, the recorded host in review/sources.tsv; it matches, so there is no host defect. The usage-section prose link to theme:black-highlighter-theme (candidate line 112) names the production BHL page, which is this candidate's actual base (candidate line 2 includes it); it is a recorded prose reference to the production page, not drift.

## 8. Structure

- EXHIBIT-RESTRUCTURE (B): Exhibit restructured (P6): the usage exhibit's frame or layout markup changed.
  Verify: The exhibit still demonstrates the same usage.
  - B3: orig 31-35 -> cand 37-42 (body -> body)
  - B4: orig 36-40 -> cand 43-46 (body -> body)
  - B7: orig 48-49 -> cand 64-65 (body -> body)
  - B121: orig 541-544 -> cand 564-568 (frame -> frame)

This instance: B3/B4 are the interwiki frames and the theme-squares exhibit, repointed, not restructured in content; B121 is the tail frame of section 3. Two structural facts need their own statements. First, the classifier's residue B50 is a real addition: the candidate defines `--offset-from-page-top: 0rem` (candidate line 221). The original uses the variable (original lines 349–350) without defining it anywhere, and production does the same (production lines 353–354); the definition is the migration's deliberate repair, recorded on the phase17-diff instruction page. Second, and this is a defect flag: **the candidate's footnoteblock is escaped**. Original line 537 carries a live `[[footnoteblock]]` and production line 541 carries it live; candidate line 559 reads `@@[[footnoteblock]]@@`. The candidate's one footnote, the translator's note at candidate line 204, is live, so it has no render position, and the literal string displays instead. Same family as caretaker-sigma (the block deleted) and penumbra (escaped, R-fix-8 flag). Flagged for the coordinator; not edited here.

## 9. Formatting only

- WS-ONLY (C): Whitespace-only (heuristic): lines differ in whitespace alone.
  Verify: Byte-compare after whitespace normalization; content must be identical.
  - B20: orig 220-220 -> cand 240-240 (code-css -> code-css)

This instance: the class covers 66 of the 121 blocks and 390 of the 598 changed lines (diff.md's auto-class table). All of it is the code exhibit's tab-to-space re-indentation, which is production's form of the stylesheet; the classifier reports 0 re-indentation pairs because the blocks are counted as whitespace-only directly. No content rides on these blocks.

## 10. Porter annotations

- ANNOTATION (B): Porter annotation (T7): the porter's own note about this port; its universal claims must hold population-wide.
  Verify: A universal claim is checked against the population census, not this file alone.
  - B48: orig 189-189 -> cand 204-204 (body -> body)

This instance: two annotations stand. The translator's footnote at candidate line 204 （訳注： the "IBM Plex Mono" sentence is the original text as written; the face actually applied is JetBrains Mono) rides inside B48 with the translation. The 日本語フォント comment at candidate lines 211–214, added by FIX5 with the JP load, rides inside B49 (section 4). Both claims are file-local and checkable from this package.

## 11. Dispositions and exceptions

- (a) The four draft-host lines (candidate lines 11, 98, 107, 252) are the T1 baseline's four pseudo-ref errors, class (iii) draft-stage form (KB-41): recorded, rewritten at posting, not a defect.
- (b) The render row (ledger (c2) row 33) is DISPOSITIONED: header logo clipped at ≤768px, notice text left-clipped, WebKit rate rendering, sidebar at x=0, a 1.84 contrast sample line, and the sample credit-modal with 337–419px overflow — the narrow-width header clip/collision family and the render-side difference class (KB-35 family), plus the credit-modal preview-form property (owner ruling 5, KB-32). Nothing in the candidate's bytes is charged by them.
- (c) The escaped footnoteblock (section 8) is NOT dispositioned; it is an open defect flag for a repair lane.

## 12. Verification

The theme's own verdict is the stamp above: overall STALE by design (the candidate changed after the verdict; the frozen record remains the verdict for the bytes it judged). Independent checks run for this package: the FIX5 closure is re-derived from the commit and the current bytes in the per-theme record; a fresh T1 run (check_source.py --kind theme --translation, 2026-11-17) on the candidate returns error 4 / warn 0 / info 2, every error the pseudo-ref class (iii) of section 11(a) (the baseline recorded in the stamp additionally carried 1 warn under its link-check configuration); a brace-depth scan of both code blocks ends at depth 0 with no negative excursion; `python3 review/build_review.py --check` lists this package as current after generation (the batch acceptance compares the stale set against the pre-existing refresh population).

Change set outside the two diffed files (K6): pages/phase17-diff-scp-offices-theme-jp.txt (the migration instruction page for the production page: record reference revision 58 in its credit block, define --offset-from-page-top, set the page-options --min-font-size, keep Google Fonts delivery), pages/theme-decoration-sample-scp-offices-theme-jp.txt (the render sample the (c2) row measured), the production page itself (pages-existing/existing:theme-scp-offices-theme.txt) as the third source this package's provenance argument rests on, and the hosted stylesheet scp-jp.github.io/files/theme/scp-offices-theme/style0.css that the tail module delivers.

## Appendix — residue blocks

- B15: orig 101-102 -> cand 117-118 (body -> body) — the specimen heading "+ Examples" becomes "+ 例" and its lead line is translated; section 6.
- B50: orig at 220 -> cand 221-221 (code-css -> code-css) — the `--offset-from-page-top: 0rem` definition; section 8.
- B119: orig 537-537 -> cand 559-559 (body -> body) — the escaped footnoteblock; the defect flag in section 8.
