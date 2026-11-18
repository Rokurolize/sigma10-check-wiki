# Review package — theme:pataphysics-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:pataphysics-jp — origin EN, population #27 [GOSIGN2-LEDGER (b) row 27]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): PASS — baseline 2026-11-16: exit 0, 0 errors / 1 warn / 2 infos (no error codes) [T1-ROWS row 27; GOSIGN2-LEDGER (b) row 27]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — WebKit CC "S", 768px notice×sidebar overlap, sample credit-modal, 884px@768 overflow, notice left-clip, contrast warn, code-token overflow. [RENDER-ROWS-1 (RENDER-C row 27)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 27)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 27, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 27]
- FIX5 re-judgement: item 3 (class A) FIXED — FIX5-FUNC §10, commit 59130a2: L35 credit:start -> credit:start-preview; checker credit-not-preview warning cleared (warn 1 -> 0); spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) item 3; (c) check 7]
- Computed against: canonical commit 59130a21b1612f1f0949594e760aaafbeadcdaac; candidate file pages/theme:pataphysics-jp.txt sha256:ecfe3bbbf40d37615b6f2c1af9ab125bc5da7340587745bce23185ad53609cd5; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation over the classifier skeleton; the verdict stamp above is generated)
Candidate: review/pataphysics-jp/candidate.txt (sha256 ecfe3bbbf40d37615b6f2c1af9ab125bc5da7340587745bce23185ad53609cd5)
Original: theme:pataphysics — scp-wiki, revision 251 (sha256 4b7c886866ba2ceab03c9e8efc5bebaa5d5c9fb364efd3d85cd19a41f80a60e5)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.
- Production-adoption signal: candidate resembles the production JP counterpart at 0.99 similarity vs 0.88 for the original (R4); declaration is a slot below.

Provenance route: adopted from the production JP counterpart (R4), then migrated. The candidate's body similarity is 0.989 against the production page (pages-existing/existing:theme-pataphysics.txt) and 0.878 against the rev 251 mirror, so the port descends from the live JP page, not from a fresh translation of the EN original. The whole candidate-to-production delta is 29 lines, itemized in the companion record pages/phase17-diff-pataphysics-jp.txt: the credit form fix of the per-theme record below, the completed credit fields, the publication-year correction, de-linked user mentions, the image-block file address, and one tail module. The mirror is review-mirrors/orig-pataphysics-rev251.txt (FETCH-REGEN, 19,400 bytes, sha256 4b7c886866ba2ceab03c9e8efc5bebaa5d5c9fb364efd3d85cd19a41f80a60e5), byte-identical to original.txt in this package and to the sources.tsv row.


## Class summary

| Label | Blocks |
|---|---|
| ASSET-REHOST | 4 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 3 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 2 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 15 |
| TRANSLATION-ANCHORED | 20 |
| WS-ONLY | 1 |

Counts: 48 blocks, 31 specific, 15 heuristic, 2 residue, 0 skipped (comment text).

## Per-theme record — the FIX5 re-derivation

This theme's one blocking item is GOSIGN2-LEDGER section (e) item 3 [A] (ledger (b) row 27): the candidate used credit:start where the JP environment requires the preview form, the checker's credit-not-preview warning was unique in the population, and at posting the credit breaks inside the iftags block. GOSIGN2-LEDGER-SUPPLEMENT re-judges it FIXED (FIX5-FUNC section 10, canonical commit 59130a2: line 35 swapped, the warning count going 1 to 0). The verdict stamp above was computed against 59130a2 itself, so the stamped file is the fixed file.

Re-derived from this package's bytes: candidate line 35 reads [[include:scp-jp:credit:start-preview]], and the block closes with :scp-jp:credit:end at line 49, the pair form this file and its production counterpart use; the T1 baseline for the theme is 0 errors. The fix is present, complete, and the only credit-form change the item required.

The theme's remaining ledger findings re-derive as follows. LOCALIZE-ROWS row 27 records four T4 items. (a) The P3 credit form, display-affecting: the same item 3, closed above. (b) A live Rate duplicated in the credit flow: GOSIGN2-LEDGER section (d) item 6 adjudicates this theme's Rate as the labelled paired exhibit exception, and the bytes match that shape: the bare [[module Rate]] at candidate line 30 stands between its exhibit labels (the rating-module label above, the credit exhibit below), inside the theme's own demonstration pair, not beside the live credit block at lines 35-49. (c) The P7 site-title face fallback: ledger c3 records P7 DISPOSITIONED; the file's only font stack, "Carrois Gothic", "Arial", sans-serif (candidate line 341), is byte-identical to the original's (line 338), so no JP face was added and none was promised; the disposition stands on the bytes. (d) The publication date off by one year: production carried 2019; the candidate's credit field for publication date reads 2018-08-19 (line 44), matching the original's info pane (original lines 20-28). Corrected.

## 1. Credit and attribution

- INFO-DEL (A): Info-module residue removed (P3, ledger class C): the old info module pair is not part of the JP environment's furniture.
  Verify: Grep the candidate for info:start / info:end includes; none may remain.
  - B4: orig 19-24 -> cand at 31 (body -> body)
  - B5: orig 26-28 -> cand 32-32 (body -> body)

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B6: orig at 30 -> cand 34-49 (body -> body)

- T7-CREDIT-CSS (B): Credit-module CSS supplement (T7, KB-11/KB-12/KB-62): the JP credit module's DOM needs rules the branch original never shipped, or its inherited rules corrected in place.
  Verify: KB-11/KB-12 recipes: confirm the selectors in the candidate and whether the production counterpart carries them (supplement vs inherited).
  - B46: orig at 722 -> cand 725-733 (body -> code-css)

This instance: the candidate's credit block (candidate lines 35-49) carries the full field set: title (JP theme name), translator Dr Devan, translation year 2018, original title 'Pataphysics Department Theme, author Lt Flops, copyright holder Lt Flops, publication date 2018-08-19, creation year 2018, reference revision 251, and the source link to the EN original. The original carries no credit block; its attribution evidence is the info pane at original lines 20-28 (Author Lt Flops, Published 19 Aug 2018, thanks to stormbreath for code help), and the candidate's naming of Lt Flops as both author and copyright holder matches it exactly, so there is no pointer defect. Attribution beyond the fields: the original's prose at line 40 credits [[*user Woedenaz]] with the animated logo; the candidate's introduction drops that sentence, but the credit survives where the code carries it, in the CSS banner comments at candidate lines 166 and 220 ("Animated Logo by Woedenaz"), and the stormbreath code-help line survives at candidate line 167. The production counterpart also lacks the prose sentence, so the reduction is production lineage under R4, not a porting loss. The INFO-DEL blocks are the original's info module, replaced by this credit block under P3.


## 2. Includes and components

- INCLUDE-REPOINT (A): Foreign include repointed (P1, KB-15): includes must name the JP counterpart that actually exists on scp-jp.
  Verify: DEPS record: the repointed target's JP counterpart is verified to exist.
  - B12: orig 51-51 -> cand 69-69 (body -> body)

This instance: the one INCLUDE-REPOINT and the one ESCAPED-INCLUDE are the same fact seen twice, the usage example at candidate line 69, @@[[include:scp-jp:theme:pataphysics]]@@. It names the production page rather than the candidate's own posting name, and that is correct for kind K6: the candidate is the Sigma-10 migration of the page already posted as theme:pataphysics, so the name a reader copies is the name that resolves. No other include changes; the component includes keep their :scp-jp: forms from production.


## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B1: orig 1-2 -> cand 1-22 (module-css -> module-css)

This instance: delivery topology is inherited unchanged from production. The @import at candidate line 2 and the interwiki-style frame at lines 4-7 (priority=1) both address the production page's own first code block, https://scp-jp.wdfiles.com/local--code_/theme%3Apataphysics/1, and the candidate holds exactly one code block, [[code type="css"]] at line 159, counted over every form (the original likewise holds one, [[code type="CSS"]] at line 156). The named block is the stylesheet itself, so there is no codeaddr question. The head module CSS at lines 11-22 adds production-lineage presentation rules over the original's hue-rotate rules, including a /* JP ONLY */ rule hiding .heritage-rating-module; those rules came with the production page and are recorded here, not re-judged.


## 4. Fonts and assets

- ASSET-REHOST (A): Asset re-hosted to JP storage (P5, KB-17): assets are served from the allowlisted JP hosts in this environment.
  Verify: KB-17 host list; the re-hosted URL serves.
  - B17: orig 78-78 -> cand 86-86 (body -> body)
  - B40: orig 200-200 -> cand 203-203 (code-css -> code-css)
  - B41: orig 235-235 -> cand 238-238 (code-css -> code-css)

This instance: the four ASSET-REHOST blocks repoint the theme's images to JP storage; the load-bearing one is the logo in the image-block exhibit, whose name= becomes the full scp-jp.wdfiles URL for pata-logo.png. sources.tsv records production drift on this asset (the candidate's frozen file differs from production's current file); the difference is recorded here, not silently resolved. Fonts are treated in the per-theme record (P7 dispositioned). The T7-CREDIT-CSS block at candidate lines 725-733 (/* JP ONLY */ .rate-box-with-credit-button.creditButton rules) reads like a campaign supplement but is not one: the selector census is candidate 5, production 5, original 4, so the block is inherited from the production page.


## 5. Header, sidebar, site furniture

No header, sidebar, or site-furniture signature fired over the 48 blocks, and the ground is checkable from classification.json: no HEADERVAR or furniture label appears in any block's label_spans, and every furniture rule in the candidate sits inside the single delivered code block treated in sections 3 and 8, carried over from production.

## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B3: orig 17-17 -> cand 27-29 (body -> body)
  - B8: orig 36-36 -> cand 56-56 (body -> body)
  - B9: orig 38-40 -> cand 58-58 (body -> body)
  - B11: orig 48-48 -> cand 66-66 (body -> body)
  - B13: orig at 53 -> cand 71-71 (body -> body)
  - B14: orig 54-54 -> cand 73-73 (body -> body)
  - B15: orig 56-67 -> cand 75-75 (body -> body)
  - B25: orig 95-95 -> cand 103-103 (body -> body)
  - B26: orig 99-100 -> cand 107-108 (body -> body)
  - B28: orig 108-109 -> cand 116-117 (body -> body)
  - B29: orig 113-113 -> cand 121-121 (body -> body)
  - B31: orig 119-121 -> cand 127-129 (body -> body)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B7: orig 33-33 -> cand 53-53 (body -> body)
  - B10: orig 45-45 -> cand 63-63 (body -> body)
  - B16: orig 72-72 -> cand 80-80 (body -> body)
  - B18: orig 81-81 -> cand 89-89 (body -> body)
  - B19: orig 83-83 -> cand 91-91 (body -> body)
  - B20: orig 85-85 -> cand 93-93 (body -> body)
  - B21: orig 87-87 -> cand 95-95 (body -> body)
  - B22: orig 89-89 -> cand 97-97 (body -> body)
  - B23: orig 91-91 -> cand 99-99 (body -> body)
  - B24: orig 93-93 -> cand 101-101 (body -> body)
  - B27: orig 102-103 -> cand 110-111 (body -> body)
  - B30: orig 115-116 -> cand 123-124 (body -> body)
  - B32: orig 123-125 -> cand 131-133 (body -> body)
  - B33: orig 128-129 -> cand 136-137 (body -> body)
  - B34: orig 131-132 -> cand 139-140 (body -> body)
  - B35: orig 134-135 -> cand 142-143 (body -> body)
  - B36: orig 137-138 -> cand 145-146 (body -> body)
  - B37: orig 140-141 -> cand 148-149 (body -> body)
  - B38: orig 147-147 -> cand 155-155 (body -> body)

- CONTENT-STRING (B): Visible string in CSS (KB-18, R1 reader-visible half): content: strings and string-valued variables render for readers.
  Verify: The string renders in the sample page's DOM text.
  - B43: orig 365-365 -> cand 368-368 (code-css -> code-css)

This instance: the 20 anchored and 15 unanchored blocks are the production page's Japanese text against the EN original's English; the pairing is one-to-one throughout, and the unanchored set is resolved by shape in the appendix. Two rendered-string changes ride inside the CSS: the content: strings naming the department take the JP name (blocks B42 and B44), the same name the credit block gives as the theme's JP title, so the delivered CSS and the credit agree. The phase17 delta also de-links the prose user mentions ([[*user ...]] to plain names) against production; the names themselves are unchanged.


## 7. Links

No LINK signature fired, but the section is not empty on the bytes. The credit source link is treated in section 1. The one remaining link fact is an exhibit residue: the syntax sample at candidate line 121, [http://ja.scp-wiki.net/ ...], keeps the http scheme inside a displayed example. That is a class (ii) posting residue, recorded in section 11; it is not a live link, and no live link in the candidate changes host against the original.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B2: orig 5-14 -> cand at 25 (body -> body)

- CSS-BODY (C): Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.
  Verify: Writer review; a recurring shape is a new-signature candidate for the patterns loop.
  - B42: orig 342-342 -> cand 345-345 (code-css -> code-css)
  - B44: orig 376-376 -> cand 379-379 (code-css -> code-css)
  - B48: orig at 726 -> cand 736-740 (body -> body)

This instance: the IFTAGS pair is the theme's own gate, [[iftags +...]] around the posted body, preserved in place. The three CSS-BODY blocks are production-drift pairs inside the delivered code block (section 3), not port edits. The tail gains one module the original does not have, a narrow-files phone-width fix at candidate lines 736-740 after [[/iftags]]; it is part of the 29-line phase17 delta against production, so it arrived with the migration, and it changes no exhibit.


B39 (original lines 151-156 to candidate line 159): replaced, not dropped. The original closes its body exhibits with a centered stub immediately before its [[code type="CSS"]] block; at the corresponding position the candidate opens its [[code type="css"]] block directly, and the full CSS body follows. B47 (original lines 723-724): the original's closing exhibit bracket at the tail has no counterpart because the candidate's tail is restructured by the inherited T7 block and the tail module; no rendered exhibit content is lost. The bare Rate at candidate line 30 is kept: it is the labelled paired exhibit of the per-theme record, not a widget beside the credit block.


## 9. Formatting only

- WS-ONLY blocks: 1
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

The ANNOTATION signature did not fire, but porter annotations are present and were checked explicitly: the /* JP ONLY */ comments at candidate lines 18 and 725, and the tail module's comment at line 737. Each marks a JP-only rule so a later editor can tell the localization layer from the theme's own CSS; they ride inside the delivery and T7 blocks of sections 3 and 4.

## 11. Dispositions and exceptions

- No derived presence label fired.

Two standing dispositions cover this theme. P7 (fonts): DISPOSITIONED in ledger c3, and the ground is re-derivable from this package alone, since the only font stack is byte-identical on both sides (candidate line 341, original line 338) and neither side loads a JP face. The http exhibit link of section 7 is class (ii): a displayed syntax sample, not a delivery or a live link, so it is recorded here rather than charged. The theme's T1 baseline is otherwise clean: 0 errors, the single credit warning closed by item 3, 2 infos.


## 12. Verification

Checks a reviewer can re-run from this package alone: (1) the sha256 of original.txt equals the sources.tsv row for theme:pataphysics-jp, and candidate.txt is byte-identical to pages/theme:pataphysics-jp.txt in the canonical repo. (2) Candidate line 35 is the preview credit include (the item 3 re-derivation in the per-theme record). (3) The T1 outcome in the stamp, PASS at 0 errors, was computed against canonical 59130a2, the FIX5 commit itself. (4) A brace-depth scan over the delivered code block returns to 0 with no negative dip on both sides. T2/T3: the stamp's render verdict is PASS; no re-render was run for this package.

## Appendix — residue blocks

- R1, B39 (residue; original 151-156 to candidate 159): the exhibit/code boundary pair; resolved in section 8 as replaced, not dropped.
- R2, B47 (residue; original 723-724 to candidate at 735): the original's tail exhibit bracket; resolved in section 8.
- R3-R14, B3, B8, B9, B11, B13, B14, B15, B25, B26, B28, B29, B31 (heuristic, TRANS-UNANCHORED): one-to-one prose translations of the production page's Japanese against the mirror's English, verified line by line against the mirror; no exhibit, include, or delivery content hides in this set (section 6).
- R15-R16, B42, B44 (heuristic, code-css): the content: string translations of section 6.
- R17, B48 (heuristic; candidate 736-740): the tail module addition of section 8.

## License and attribution

- **Title:** 'Pataphysics Department Theme
- **Author:** Lt Flops
- **Source:** https://scp-wiki.wikidot.com/theme:pataphysics — revision 251 (revision date 2023-04-13 05:38:08)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: Dr Devan — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
