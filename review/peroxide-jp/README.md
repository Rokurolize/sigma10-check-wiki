# Review package — theme:peroxide-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:peroxide-jp — origin CN, population #217 [GOSIGN2-LEDGER (b) row 217]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 37 errors / 0 warns / 2 infos (hotlink×18, foreign-include×17, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 242; GOSIGN2-LEDGER (b) row 217]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 360–366px@320 + sidebar-unreachable (4 combos) + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 216, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 216]
- FIX5 re-judgement: item 71 (class B) FIXED — FIX5-FURNB, commit 25bb0b4: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 71]
- Computed against: canonical commit 25bb0b40f10153f1f8bdda252283bb7aa7a76875; candidate file pages/theme:peroxide-jp.txt sha256:3529500b6540d37d8c76dfa977bfb46b792c9fbca04970e22499746114029f3a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation over the classifier skeleton; the verdict stamp above is generated)
Candidate: review/peroxide-jp/candidate.txt (sha256 3529500b6540d37d8c76dfa977bfb46b792c9fbca04970e22499746114029f3a)
Original: theme:peroxide — scp-wiki-cn, revision 27 (sha256 e532c954ae59923d454b89ddc8bcd23bf057c585581e6b0b3290d86df6d422e5)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: companion:fragment:peroxide-jp-base-css.txt -> code-css (body similarity 0.81)
- Delivery: companion:fragment:peroxide-jp-base-css.txt -> module-css (body similarity 0.67)

Provenance route: derived from the original at the reference revision (rev 27), with the delivery rebuilt for the JP environment; there is no production JP counterpart. The kind is K5b-4+K5b-5: the theme's CSS body is delivered from the two JP companion fragments (section 3). The mirror is review-mirrors/orig-peroxide-rev27.txt (COPY from R/gosign2-lanes/lane-oc-gs-localize-s2-E/orig-peroxide.txt, 14,311 bytes, sha256 e532c954ae59923d454b89ddc8bcd23bf057c585581e6b0b3290d86df6d422e5), byte-identical to original.txt in this package and to the sources.tsv row. One correction to the sources.tsv note is recorded in the lane report: the note claims the original was superseded upstream after rev 27, but the artifact it cites (diff-peroxide-from27.txt in the same lane directory) records rev 27 to rev 27, no changes; the correct form is that upstream latest remains rev 27.


## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DELIVERY-MOVE | 1 |
| DRAFT-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| GLYPH-FORM | 9 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 3 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 32 |
| TRANSLATION-ANCHORED | 40 |

Counts: 79 blocks, 51 specific, 27 heuristic, 1 residue, 0 skipped (comment text).

## Per-theme record — the FIX5 re-derivation

This theme's one blocking item is GOSIGN2-LEDGER section (e) item 71 [B] (ledger (b) row 217): a duplicate bare [[module Rate]] at candidate line 140 stood immediately before credit:start-preview, rendering two rating widgets, because the preview credit module is itself rate-bearing. LOCALIZE-ROWS row 216 states the same fact (the Rate duplication at L140 against the credit, minor but a specification violation). GOSIGN2-LEDGER-SUPPLEMENT re-judges it FIXED (FIX5-FURNB, canonical commit 25bb0b4: the duplicate bare Rate block removed). The verdict stamp above was computed against 25bb0b4 itself.

Re-derived from this package's bytes: a case-insensitive census of rate modules over the whole candidate returns zero. The only rate module in either file is the original's own centered [[module rate]] at original line 84, which the P3 credit swap subsumes; the preview credit at candidate lines 139-154 is the page's only rating widget. The lines around the old position are the version line (candidate line 137) and the credit block, so the removal took the duplicate and nothing else. The fix is present and complete.

The theme's remaining ledger findings are the T1 baseline classes, all dispositioned in ledger c1/c3: hotlink x18 (P5, the cdn.mer.run images, section 11), foreign-include x17 (P1, the :oxygennine: documentation references, section 11), pseudo-ref x2 (class (ii)). Ledger c3 records P1 and P5 DISPOSITIONED; LOCALIZE-ROWS row 216 judges the credit fully equipped and the translation generally good, with the Rate duplication as its one specification violation, closed above.

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B6: orig 83-85 -> cand 139-160 (body -> body)

This instance: the candidate's credit block (candidate lines 139-154) carries title (JP theme name), translator AI, translation year 2026, original title (the CN title, quoted), copyright holder [[*user OxygenNine]], creation year 2026, reference revision 27, and the source link https://scp-wiki-cn.wikidot.com/theme:peroxide, which names the recorded origin host of sources.tsv. The original carries no credit block; its attribution is prose (developed by [[*user OxygenNine]], original line 89) and the GitHub repository, and the field names the same person, so there is no pointer defect. Attribution beyond the fields rides in the credit prose (candidate lines 148-152): the Agent FS better-footnote component credit, the icon sources (Bootstrap Icons, SVG Repo), the font note of section 4, and the CC-BY-SA 4.0 license line with the GitHub source link, matching the original's closing attribution section (original lines 442-449), which the candidate also keeps in translated form at its tail. Author and publication-date fields are absent: the original gives no publication date, and LOCALIZE-ROWS row 216 judges this credit fully equipped.


## 2. Includes and components

- INCLUDE-REPOINT (A): Foreign include repointed (P1, KB-15): includes must name the JP counterpart that actually exists on scp-jp.
  Verify: DEPS record: the repointed target's JP counterpart is verified to exist.
  - B12: orig 121-121 -> cand 187-187 (body -> body)
  - B26: orig 180-180 -> cand 246-246 (body -> body)
  - B28: orig 187-187 -> cand 253-253 (body -> body)

- ESCAPED-INCLUDE (B): Escaped usage-example include repointed (P1, AGENTS.md section 3): escaped examples are judged too, because readers copy them.
  Verify: Read the example as a reader would paste it; the include must resolve on scp-jp.
  - B40: orig 242-242 -> cand 308-308 (body -> body)

This instance: the three INCLUDE-REPOINT blocks (B12, B26, B28) repoint the theme's own examples to :scp-jp: forms where a JP counterpart exists, and ESCAPED-INCLUDE B40 (candidate line 308) is the usage example naming the candidate's own posting name, theme:peroxide-jp, the post-sweep form. The :oxygennine: layout and palette references are not repointed: they are the author's hosted component system, kept as documentation under the named exception of section 11. None of them is a live include: a census of line-initial [[include over the candidate finds only the two interwiki frames and the credit pair, and all 20 :oxygennine: references sit in @@ or {{ }} exhibits or in prose.


## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B2: orig 4-4 -> cand 6-14 (body -> body)

- DELIVERY-MOVE (B): Body relocated between deliveries (topology): where the CSS lives changed (code page to inline module CSS, exhibit to own fragment); the move itself is the change, and internal edits classify separately.
  Verify: Compare the moved body against its counterpart in the mirror or its companion delivery.
  - B5: orig 77-77 -> cand 31-133 (body -> body)

This instance: the topology is rebuilt, because the original delivers its body CSS from outside the page entirely: a ThemePreviewer module with theme_url and a module @import both naming https://oxygennine.github.io/Peroxide/peroxide.css (original lines 4 and 32), plus sidebar interwiki frames at priority=2 (original lines 16-27). The candidate delivers inside the JP environment: frame 1 (candidate lines 1-4) takes the BHL normalize stylesheet from scp-jp.github.io at priority=1; frame 2 (lines 6-9) at priority=2 names the candidate's own code block 1 on the draft host sigma10-jp-test.wdfiles.com; a module CSS (lines 11-14) imports the two companion fragments' first blocks. DELIVERY-MOVE B5: the Interwiki.css body, which the original loads from oxygennine.github.io, is inlined as the candidate's code block 1 ([[code type="css"]], candidate lines 34-133), the very block the priority=2 frame names, so address and content agree and there is no codeaddr question. The split of the main CSS across two fragments is forced by the 200,000-character page limit: the fragments run 111,817 and 110,867 bytes (222,684 in total), and their heads state the split and the provenance. DRAFT-HOST B2: the delivery addresses name the Sigma-10 test host because this candidate posts to the test environment, uniformly across frame and imports. The original's first two lines (comments naming the CN fragment pages, original lines 1-2) have no counterpart: the JP fragment pair supersedes them (appendix R1).


## 4. Fonts and assets

The font signatures did not fire because the loads live in the companion fragment, not in this file: fragment:peroxide-jp-base-css line 15 imports Noto Sans JP, Noto Serif JP, JetBrains Mono, and M PLUS 1 Code from Google Fonts, and the credit block's font note (candidate line 152) states the substitution on the page: the original's Sarasa Gothic SC, zsft-hk, and Noto Serif CJK cannot load from the exception hosts, so Google Fonts equivalents stand in, all under the SIL Open Font License. Every named face is applied inside the fragments' stacks; no face is loaded-but-unapplied or named-but-unloaded. The theme's images stay on the author's cdn.mer.run (section 11).

## 5. Header, sidebar, site furniture

No header, sidebar, or site-furniture signature fired. Ground: the candidate's furniture is the theme's own, carried over: the saving-pages blocker div at candidate lines 24-28 is the original's (its collapsible labels are translated in section 6), and the second-level navigation is documented, not redefined, at candidate lines 465-481. No header variables are set or changed in this file; header behavior lives in the fragments' CSS, whose provenance section 3 records.

## 6. Text translation

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B4: orig 73-73 -> cand 27-27 (body -> body)
  - B10: orig 116-116 -> cand 182-182 (body -> body)
  - B14: orig 129-129 -> cand 195-195 (body -> body)
  - B15: orig 134-134 -> cand 200-200 (body -> body)
  - B16: orig 139-139 -> cand 205-205 (body -> body)
  - B17: orig 144-144 -> cand 210-210 (body -> body)
  - B18: orig 149-149 -> cand 215-215 (body -> body)
  - B19: orig 154-154 -> cand 220-220 (body -> body)
  - B20: orig 159-159 -> cand 225-225 (body -> body)
  - B23: orig 172-172 -> cand 238-238 (body -> body)
  - B24: orig 175-175 -> cand 241-241 (body -> body)
  - B29: orig 193-193 -> cand 259-259 (body -> body)
  - B30: orig 198-198 -> cand 264-264 (body -> body)
  - B31: orig 203-203 -> cand 269-269 (body -> body)
  - B32: orig 208-208 -> cand 274-274 (body -> body)
  - B33: orig 213-213 -> cand 279-279 (body -> body)
  - B34: orig 218-218 -> cand 284-284 (body -> body)
  - B35: orig 223-223 -> cand 289-289 (body -> body)
  - B36: orig 228-228 -> cand 294-294 (body -> body)
  - B37: orig 235-235 -> cand 301-301 (body -> body)
  - B39: orig 239-239 -> cand 305-305 (body -> body)
  - B41: orig 244-248 -> cand 310-314 (body -> body)
  - B42: orig 250-250 -> cand 316-316 (body -> body)
  - B43: orig 252-252 -> cand 318-318 (body -> body)
  - B44: orig 254-254 -> cand 320-320 (body -> body)
  - B45: orig 256-256 -> cand 322-322 (body -> body)
  - B46: orig 258-258 -> cand 324-324 (body -> body)
  - B47: orig 262-262 -> cand 328-328 (body -> body)
  - B48: orig 264-264 -> cand 330-330 (body -> body)
  - B55: orig 306-308 -> cand 372-374 (body -> body)
  - B56: orig 313-314 -> cand 379-380 (body -> body)
  - B58: orig 323-323 -> cand 389-389 (body -> body)
  - B59: orig 325-325 -> cand 391-391 (body -> body)
  - B60: orig 335-335 -> cand 401-401 (body -> body)
  - B67: orig 399-399 -> cand 465-465 (body -> body)
  - B69: orig 408-410 -> cand 474-476 (code-other -> code-other)
  - B70: orig 412-412 -> cand 478-478 (code-other -> code-other)
  - B71: orig 418-418 -> cand 484-484 (body -> body)
  - B73: orig 422-422 -> cand 488-488 (body -> body)
  - B75: orig 426-426 -> cand 492-492 (body -> body)

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B7: orig 90-90 -> cand 165-165 (body -> body)
  - B8: orig 92-92 -> cand 167-167 (body -> body)
  - B9: orig 94-103 -> cand 169-169 (body -> body)
  - B11: orig 118-118 -> cand 184-184 (body -> body)
  - B13: orig 125-125 -> cand 191-191 (body -> body)
  - B21: orig 161-161 -> cand 227-227 (body -> body)
  - B22: orig 164-164 -> cand 230-230 (body -> body)
  - B25: orig 177-177 -> cand 243-243 (body -> body)
  - B27: orig 184-184 -> cand 250-250 (body -> body)
  - B38: orig 237-237 -> cand 303-303 (body -> body)
  - B49: orig 268-270 -> cand 334-336 (body -> body)
  - B50: orig 275-276 -> cand 341-342 (body -> body)
  - B51: orig 281-283 -> cand 347-349 (body -> body)
  - B52: orig 288-289 -> cand 354-355 (body -> body)
  - B53: orig 294-295 -> cand 360-361 (body -> body)
  - B54: orig 300-301 -> cand 366-367 (body -> body)
  - B57: orig 319-320 -> cand 385-386 (body -> body)
  - B62: orig 343-343 -> cand 409-409 (body -> body)
  - B64: orig 351-351 -> cand 417-417 (body -> body)
  - B66: orig 397-397 -> cand 463-463 (body -> body)
  - B68: orig 405-405 -> cand 471-471 (body -> body)
  - B72: orig 420-420 -> cand 486-486 (body -> body)
  - B74: orig 424-424 -> cand 490-490 (body -> body)
  - B76: orig 428-434 -> cand 494-494 (body -> body)
  - B77: orig 438-438 -> cand 498-498 (body -> body)
  - B78: orig 440-440 -> cand 500-500 (body -> body)
  - B79: orig 442-448 -> cand 502-502 (body -> body)

- GLYPH-FORM (B): Shinjitai conversion (R5): retained source-language strings converted to Japanese glyph forms; neither translated nor left untouched, and the reviewer must see it separately.
  Verify: Fold-compare the pair; only glyph forms differ.
  - B61: orig 339-339 -> cand 405-405 (body -> body)
  - B63: orig 347-347 -> cand 413-413 (body -> body)
  - B65: orig 355-355 -> cand 421-421 (body -> body)

This instance: 40 anchored and 32 unanchored translation blocks, one-to-one against the mirror. GLYPH-FORM fired on 9 blocks (B23, B31, B32, B33, B34, B61, B63, B65, B75): retained Chinese strings converted to Japanese glyph forms (R5), in the palette and layout exhibit names and the closing sections. The credit block's original-title field keeps the CN title as a quotation, glyph forms untouched there because it is a citation, not rendered JP text. The unanchored set is resolved by shape in the appendix.


## 7. Links

No LINK signature fired. On the bytes: the predecessor link at candidate line 156 names the CN original by absolute URL ([[[https://scp-wiki-cn.wikidot.com/theme:mox|...]]]) where the original used the same-wiki form [[[theme:mox|...]]] (original line 89); the target is unchanged and the host is the recorded origin host. The credit source link is in section 1. No live link changes host.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B3: orig 16-71 -> cand at 26 (body -> body)

This instance: the documentation exhibits (the layout and palette include samples, candidate lines 187-296) are kept in full, in both :scp-jp: and :oxygennine: forms where the original pairs them. The second code block (candidate line 473, plain [[code]]) is the navigation-list sample, the original's line 407 block carried over. Nothing the original carries is silently dropped: its closing attribution and font sections stand translated at the candidate's tail (lines 494-503), and its print section is rewritten for the new delivery, with the translator's note of section 10 explaining why.


B3 (original lines 16-71 to candidate line 26): replaced, not dropped. That range is the original's delivery head (sidebar frames, ThemePreviewer, the external import module); the candidate's delivery head of section 3 stands in its place, and nothing in the range was exhibit content. The bare-Rate question is the per-theme record: the original's centered rate module (original line 84) is subsumed by the rate-bearing preview credit, and the port's duplicate beside the credit was removed by FIX5-FURNB.


## 9. Formatting only

- WS-ONLY blocks: 0
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

The skeleton prints none, but ANNOTATION fired twice in classification.json's label_spans (B5 and B79), and the bytes agree: the two delivery comments at candidate lines 31 and 33 (the fragment split, and the interwiki block's role as this page's code block 1), riding inside B5, and the translator's note at lines 501-503 (B79) explaining that the JP form drops the ThemePreviewer module, the printFriendly parameter, and the wdfiles fallback, and why. The fragments carry their own provenance comments (section 3).

## 11. Dispositions and exceptions

- FOREIGN-KEPT: 16 occurrence(s), e.g. = {{[[include :oxygennine:peroxide:layout-classic-header]]}} (lines 197-197, 202-202, 207-207, 212-212, 217-217). Class: named exception candidate (KB-54 / KB-15).

FOREIGN-KEPT: 16 exhibited forms by the classifier's count, 20 :oxygennine: references in total per LOCALIZE-ROWS row 216 (the remainder are the @@-escaped pair lines and the prose mention at candidate line 463). The layout and palette component pages are the author's hosted system on his personal wiki; the campaign's named exception (patterns KB-54, FIX2-INCLUDE section 5) keeps them as documentation, because the theme's own delivery is the JP fragment set and no JP counterparts for those component pages exist. The ground is re-derivable from this package: every reference sits in an exhibit or in prose, and none is a live include (section 2). Hotlinks: the 17 display images on cdn.mer.run, the author's own CDN, plus the header image at candidate line 135 (identical URL to original line 79) are P5 DISPOSITIONED in ledger c3, class (ii) (patterns KB-58): the theme's own assets on the author's host, kept. The T1 baseline's pseudo-ref pair is class (ii) posting form.


## 12. Verification

The stamp's PASS was computed against canonical 25bb0b4, the FIX5 commit itself. Checks a reviewer can re-run from this package alone: (1) the sha256 of original.txt equals the sources.tsv row for theme:peroxide-jp, and candidate.txt is byte-identical to pages/theme:peroxide-jp.txt. (2) The item 71 re-derivation: a case-insensitive census of rate modules returns zero in the candidate and one in the original (line 84). (3) The live-include census for :oxygennine: returns zero. (4) The fragment byte counts (111,817 and 110,867) against the 200,000-character limit that forced the split. The stamp carries the T1 baseline (37 errors, all standing classes per section 11) and the T2/T3 FINDINGS (narrow-width overflow, sidebar reachability, the runtime-hotlink chain of the dispositioned images); no re-render was run for this package.

## Appendix — residue blocks

- R1, B1 (residue; original 1-2 to candidate 1-4): the original's CN fragment address comments give way to the candidate's delivery frames; resolved in section 3.
- R2, B3 (heuristic): the delivery-head replacement, resolved in section 8.
- R3-R28, B7, B8, B9, B11, B13, B21, B22, B25, B27, B38, B49, B50, B51, B52, B53, B54, B57, B62, B64, B66, B68, B72, B74, B76, B77, B78 (heuristic, TRANS-UNANCHORED): one-to-one prose translations against the mirror (section 6); B66 is the running-prose mention of the layout-page-content-block include at candidate line 463, part of the section 11 exception set.
