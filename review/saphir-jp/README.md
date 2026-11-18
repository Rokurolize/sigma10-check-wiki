# Review package — theme:saphir-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:saphir-jp — origin EN, population #132 [GOSIGN2-LEDGER (b) row 132]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now e92d55d70549f1e64ef518cc50b78ba7a1da49417b53d7433e15b3ba39bc5e46); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 0 warns / 2 infos (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 127; GOSIGN2-LEDGER (b) row 132]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page page-overflow 682/685px@320/375 + 989px@768 chromium and 672/675px + 996px@768 webkit (T3: visually confirmed, driven by cross-cutting preview-chrome rate module), runtime-hotlink site-theme chain only; sample credit-modal (preview-form), page-overflow 706/708px@320/375 + 1031/1036px@768 (706/708 = cross-cutting static-credit shape); T3 otherwise clean (sample section 27 bibliography-not-found = possible stale static-cache, not a theme defect); saphir-header/sapphire-logo missing = deferred assets. [RENDER-ROWS-RERUN16 (EN18) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (EN18)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 132, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 132]
- FIX5 re-judgement: item 26 (class B) DISPOSITIONED — FIX5-FURNA (no edit): original rev 14 ships the identical Rate inside its specimen at orig L211; candidate L210 sits inside the format-example block, 186 lines from the credit module at L24; the class-B labelled-specimen exception applies verbatim [GOSIGN2-LEDGER-SUPPLEMENT (a) item 26]
- Computed against: canonical commit cc4b4d8827291483ad7643d0ea2d20fa5f205ca9; candidate file pages/theme:saphir-jp.txt sha256:e92d55d70549f1e64ef518cc50b78ba7a1da49417b53d7433e15b3ba39bc5e46; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (R-disp-11 lane, 2026-11-17)
Candidate: review/saphir-jp/candidate.txt (sha256 3ed94621d2f02020e1cd1d5934ff78aa6174d19c09dfd9ca4df36054f391af48)
Original: theme:saphir — scp-wiki, revision 14 (sha256 d80534f6c6721a501290aebf5ea73ec6e2298a9c80be6b7ee019b5c0a7fb9669)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (generated stamp) | Notes |
|---|---|---|
| T1 source check | FINDINGS (classified) | Baseline 5 errors / 0 warns / 2 infos (pseudo-ref x5); this lane's run on the current file reproduces it exactly (section 12) |
| T2/T3 render | FINDINGS | RERUN16 (EN18) row: page-overflow and runtime-hotlink lines dispositioned as environment-layer (KB-40/KB-33/KB-34); sample credit-modal preview-form (KB-32); bibliography caution (KB-49); deferred assets (KB-58) |
| T4/T5 localize/translation | FINDINGS | Row 132: 3 display-affecting findings (pattern 3 credit fields, fixed by the credit waves; pattern 11 six EN body links, dispositioned sibling class; the duplicate Rate became item 26); no translation residue |
| FIX5 item 26 [B] | DISPOSITIONED | Re-derived on this package's bytes in the per-theme record; the ground holds exactly |

## Provenance

| | |
|---|---|
| Original | theme:saphir, scp-wiki, revision 14 (first-translation reference revision; also the current upstream revision at this lane's check) |
| Mirror | review-mirrors/orig-saphir-rev14.txt, class COPY, sha256 d80534f6c6721a501290aebf5ea73ec6e2298a9c80be6b7ee019b5c0a7fb9669 (equals the sources.tsv value) |
| Candidate | pages/theme:saphir-jp.txt, sha256 3ed94621d2f02020e1cd1d5934ff78aa6174d19c09dfd9ca4df36054f391af48 |
| Kind | single-page theme; the base (flopstyle) is carried by include, not bundled as a layer |
| Production counterpart | none (no pages-existing/ entry for this theme) |

## Summary

The port carries the EN fork of DrGemini's French SAPHIR theme (Lt Flops, 2024) into the SCP-JP Sigma-10 environment. The diff is Tier 2 (491 changed lines over 156 blocks, counted by build_review.py): a head-zone rebuild (preview credit block in; bare Rate and info modules out), delivery moved from the original's tail to the head in the same ungated form, a bunny.net to Google Fonts load change with a Noto Serif JP supplement, and a full prose translation. The theme's one blocking item (26, class B) was dispositioned by FIX5; the per-theme record re-derives that disposition from these bytes and confirms it. Two minor items are recorded for the coordinator: defect flag F1 (a wrong-language link annotation at candidate L63) and observation O1 (the license-box wrapper includes dropped while the licensed content stands).

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

Provenance route: derived from the original at the reference revision. The candidate's credit block names first-translation reference revision 14; the mirror in this package is the campaign's frozen copy of scp-wiki theme:saphir revision 14 (sha256 above); and wd_revisions.py list, run by this lane on 2026-11-17, shows revision 14 is also the current upstream revision (rev14, 2026-09-25, uploading saphir.webp), so the mirror is not stale. The port is not adopted from a production JP counterpart (none exists) and is not a JP original.


## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 39 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DRAFT-HOST | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| FONT-IMPORT | 3 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 80 |
| TRANSLATION-ANCHORED | 33 |
| WS-ONLY | 19 |

Counts: 156 blocks, 61 specific, 78 heuristic, 17 residue, 0 skipped (comment text).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B3: orig 9-34 -> cand 24-33 (body -> body)

Why this instance is right: the original's head zone carried three credit surfaces (a bare Rate at orig L9-10, the info:start/end block at orig L12-23, and the standalone info module at orig L25-31); the JP environment's single rate-bearing form is the preview credit block, so all three collapse into it (cand L24-33). The TASL fields name Lt Flops as copyright holder: he is the author of this fork and of the original page (created rev 0, 2024-05-02, per the wd_revisions.py record this lane ran), and the creation-year field 2024 matches both that record and the original info block's own "Published on 02 May 2024". DrGemini's authorship of the base work is not dropped: it is carried in the translated fork prose (cand L38), in the body credit line (cand L78), in the CSS banner comment (cand L380, "original author: DrGemini"), and in the translated image-license block (cand L956, author DrGemini). The P3 field set was FIXED by the credit waves and checker-verified (ledger register (c3), row moved to (e)); this lane's T1 run shows no credit finding.


## 2. Includes and components

Written from label_spans (the skeleton's per-section pass prints none because every include change rides inside a block whose primary label belongs to another section):

- B1 span (SELF-DELIVERY/IFTAGS): the two base includes are repointed, not restructured: :scp-wiki:theme:flopstyle (hidden div) becomes :scp-jp:theme:flopstyle at cand L2, and component:centered-header-sigma-9 takes the :scp-jp: interwiki form at cand L4. Both move from the original's tail delivery zone to the head with the delivery move (section 3).
- B3: the credit includes are the section 1 swap (info:start/end and info:start-standalone/end-standalone out; credit:start-preview/end-preview in).
- B21 span (DRAFT-HOST): component:image-block keeps its component name; only its name= file address changes host (section 4).
- The iftags gate localizes +theme to the JP tag form (B1 span; KB-08).

No component is added, dropped, or swapped for a JP port; the include census is 1:1 by kind against the original.

## 3. Delivery and code loading

- SELF-DELIVERY (A): Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel.
  Verify: The named delivery resolves on the draft host and serves the current candidate body.
  - B1: orig 1-1 -> cand 1-16 (body -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B21: orig 101-102 -> cand 100-101 (body -> body)
  - B55: orig 213-213 -> cand 212-212 (body -> body)
  - B106: orig 432-432 -> cand 442-442 (code-css -> code-css)

Why this instance is right: the relocation is positional, not structural. The original delivers at the tail (orig L955-969): the hidden flopstyle include, the centered-header include, a [[module CSS]] importing its own /2, and interwiki-style priority=2 naming /2. The candidate delivers the same pieces at the head (cand L1-14), with the head module importing both /1 and /2. The code-block census is unchanged (block 1 = the fonts block, block 2 = the main CSS at 559 lines; the /1 and /2 addresses name the same blocks on both sides), so no self-delivery repoint of the FIX-CODEADDR kind was needed and none was made. The iftags gate stays in render-time text (cand L16), so nothing here is an inert-channel gate. The draft-host form of the two @imports and the interwiki theme= address is the class (iii) draft-stage form (KB-41), dispositioned in section 11; posting rewrites it to the scp-jp host (class (ii)).


## 4. Fonts and assets

- FONT-IMPORT (B): Other font-load change (P5, KB-04): malformed family parameters (a hyphen for a +) make the load fail.
  Verify: KB-04: the family parameter form; the deciding evidence is the load probe (400 vs 200).
  - B85: orig 335-335 -> cand 334-334 (code-css -> code-css)
  - B89: orig 348-348 -> cand 347-347 (code-css -> code-css)

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B93: orig 361-361 -> cand 360-371 (code-css -> code-css)

Why these instances are right: the load change is a host-and-syntax normalization, not a font-program substitution. The original's block 1 loads Merriweather, Special Elite, and Tinos from fonts.bunny.net; the candidate loads the same three families from Google Fonts css2 with explicit axis specifications (Merriweather and Tinos gain the ital,wght axes). No family is dropped and no family is replaced. B93 adds the one genuinely new load, Noto Serif JP, and the serif stacks that can render Japanese gain it as a fallback in the same edit family; that is the KB-16 supplement shape, and the base chain (flopstyle) loads no JP serif to subtract. The FONT-IMPORT (B) class text about malformed family parameters does not apply here: no load failure is recorded for either form in the render rows, whose only asset finding is the deferred header/logo files (KB-58). Assets: the header and logo images are re-addressed to the candidate's own attachment namespace on the draft host (B21/B55/B106 spans, class (ii) posting rewrite); their absence from the check wiki is the deferred-assets state dispositioned at KB-58 (section 11), not a port decision.


## 5. Header, sidebar, site furniture

- HEADERVAR (A): Header/title variables (P9/T6, KB-57): the header text variables are the theme's visible title surface.
  Verify: KB-57: where the value stays in the original's language, the disposition is ruling 2 (section 11).
  - B101: orig 385-385 -> cand 395-395 (code-css -> code-css)

Why this instance is right: B101 is the :root header block. --header-title stays "SAPHIR" (cand L394): an identity string, the organisation's name, covered by ruling 2 and also the credit block's title surface. --header-subtitle "WHEN IN DOUBT, DOUBT" becomes the Japanese watchword (cand L395): the subtitle default is a complete prose sentence, and the theme itself treats it as prose (the GoI specimen closes with it as a sentence), so the port translates it in both places, header variable and specimen. That follows the fleet boundary ruled on 2026-11-17: sentences a reader reads as prose are translated; names and marks stay. No ruling-2 disposition is needed for a value that was in fact translated.


## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B2: orig 4-4 -> cand 19-19 (body -> body)
  - B5: orig 39-39 -> cand 38-38 (body -> body)
  - B7: orig 47-47 -> cand 46-46 (body -> body)
  - B9: orig 55-55 -> cand 54-54 (body -> body)
  - B11: orig 62-62 -> cand 61-61 (body -> body)
  - B12: orig 64-64 -> cand 63-63 (body -> body)
  - B13: orig 66-66 -> cand 65-65 (body -> body)
  - B14: orig 69-69 -> cand 68-68 (body -> body)
  - B15: orig 71-71 -> cand 70-70 (body -> body)
  - B16: orig 73-73 -> cand 72-72 (body -> body)
  - B17: orig 75-75 -> cand 74-74 (body -> body)
  - B18: orig 78-80 -> cand 77-79 (body -> body)
  - B24: orig 115-115 -> cand 114-114 (body -> body)
  - B25: orig 117-117 -> cand 116-116 (body -> body)
  - B26: orig 127-129 -> cand 126-128 (body -> body)
  - B27: orig 131-133 -> cand 130-132 (body -> body)
  - B31: orig 146-146 -> cand 145-145 (body -> body)
  - B33: orig 151-151 -> cand 150-150 (body -> body)
  - B34: orig 153-153 -> cand 152-152 (body -> body)
  - B35: orig 155-155 -> cand 154-154 (body -> body)
  - B36: orig 157-157 -> cand 156-156 (body -> body)
  - B37: orig 159-159 -> cand 158-158 (body -> body)
  - B38: orig 161-161 -> cand 160-160 (body -> body)
  - B39: orig 163-163 -> cand 162-162 (body -> body)
  - B40: orig 165-165 -> cand 164-164 (body -> body)
  - B41: orig 167-167 -> cand 166-166 (body -> body)
  - B42: orig 169-169 -> cand 168-168 (body -> body)
  - B43: orig 171-171 -> cand 170-170 (body -> body)
  - B50: orig 188-188 -> cand 187-187 (body -> body)
  - B51: orig 190-190 -> cand 189-189 (body -> body)
  - B52: orig 192-192 -> cand 191-191 (body -> body)
  - B53: orig 194-194 -> cand 193-193 (body -> body)
  - B58: orig 224-224 -> cand 223-223 (body -> body)
  - B60: orig 228-228 -> cand 227-227 (body -> body)
  - B61: orig 234-234 -> cand 233-233 (body -> body)
  - B62: orig 236-236 -> cand 235-235 (body -> body)
  - B64: orig 243-243 -> cand 242-242 (body -> body)
  - B65: orig 248-248 -> cand 247-247 (body -> body)
  - B66: orig 253-253 -> cand 252-252 (body -> body)
  - B67: orig 257-257 -> cand 256-256 (body -> body)
  - B68: orig 261-261 -> cand 260-260 (body -> body)
  - B69: orig 264-264 -> cand 263-263 (body -> body)
  - B70: orig 267-267 -> cand 266-266 (body -> body)
  - B71: orig 274-274 -> cand 273-273 (body -> body)
  - B72: orig 278-278 -> cand 277-277 (body -> body)
  - B73: orig 282-282 -> cand 281-281 (body -> body)
  - B76: orig 295-295 -> cand 294-294 (body -> body)
  - B81: orig 322-322 -> cand 321-321 (code-css -> code-css)
  - B94: orig 365-365 -> cand 375-375 (code-css -> code-css)
  - B98: orig 378-378 -> cand 388-388 (code-css -> code-css)
  - B100: orig 383-383 -> cand 393-393 (code-css -> code-css)
  - B102: orig 392-392 -> cand 402-402 (code-css -> code-css)
  - B103: orig 409-409 -> cand 419-419 (code-css -> code-css)
  - B105: orig 429-429 -> cand 439-439 (code-css -> code-css)
  - B110: orig 485-485 -> cand 495-495 (code-css -> code-css)
  - B111: orig 495-495 -> cand 505-505 (code-css -> code-css)
  - B112: orig 531-531 -> cand 541-541 (code-css -> code-css)
  - B114: orig 541-541 -> cand 551-551 (code-css -> code-css)
  - B115: orig 547-547 -> cand 557-557 (code-css -> code-css)
  - B116: orig 583-583 -> cand 593-593 (code-css -> code-css)
  - B119: orig 654-654 -> cand 664-664 (code-css -> code-css)
  - B120: orig 716-716 -> cand 726-726 (code-css -> code-css)
  - B127: orig 752-752 -> cand 762-762 (code-css -> code-css)
  - B131: orig 770-770 -> cand 780-780 (code-css -> code-css)
  - B133: orig 825-825 -> cand 835-835 (code-css -> code-css)
  - B134: orig 827-827 -> cand 837-837 (code-css -> code-css)
  - B135: orig 834-834 -> cand 844-844 (code-css -> code-css)
  - B136: orig 844-844 -> cand 854-854 (code-css -> code-css)
  - B137: orig 854-854 -> cand 864-864 (code-css -> code-css)
  - B138: orig 863-863 -> cand 873-873 (code-css -> code-css)
  - B139: orig 865-865 -> cand 875-875 (code-css -> code-css)
  - B141: orig 877-877 -> cand 887-887 (code-css -> code-css)
  - B143: orig 885-885 -> cand 895-895 (code-css -> code-css)
  - B145: orig 893-893 -> cand 903-903 (code-css -> code-css)
  - B149: orig 909-909 -> cand 919-919 (code-css -> code-css)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B4: orig 37-37 -> cand 36-36 (body -> body)
  - B20: orig 94-94 -> cand 93-93 (body -> body)
  - B22: orig 105-106 -> cand 104-105 (body -> body)
  - B23: orig 108-113 -> cand 107-112 (body -> body)
  - B28: orig 135-137 -> cand 134-136 (body -> body)
  - B29: orig 140-141 -> cand 139-140 (body -> body)
  - B30: orig 143-144 -> cand 142-143 (body -> body)
  - B32: orig 148-149 -> cand 147-148 (body -> body)
  - B44: orig 173-173 -> cand 172-172 (body -> body)
  - B45: orig 175-175 -> cand 174-174 (body -> body)
  - B46: orig 177-177 -> cand 176-176 (body -> body)
  - B47: orig 179-179 -> cand 178-178 (body -> body)
  - B48: orig 181-181 -> cand 180-180 (body -> body)
  - B49: orig 183-183 -> cand 182-182 (body -> body)
  - B54: orig 206-206 -> cand 205-205 (body -> body)
  - B57: orig 220-220 -> cand 219-219 (body -> body)
  - B59: orig 226-226 -> cand 225-225 (body -> body)
  - B75: orig 290-290 -> cand 289-289 (body -> body)
  - B79: orig 310-310 -> cand 309-309 (body -> body)
  - B80: orig 316-316 -> cand 315-315 (body -> body)
  - B83: orig 329-329 -> cand 328-328 (code-css -> code-css)
  - B84: orig 331-331 -> cand 330-330 (code-css -> code-css)
  - B87: orig 342-342 -> cand 341-341 (code-css -> code-css)
  - B88: orig 344-344 -> cand 343-343 (code-css -> code-css)
  - B91: orig 355-355 -> cand 354-354 (code-css -> code-css)
  - B92: orig 357-357 -> cand 356-356 (code-css -> code-css)
  - B95: orig 368-370 -> cand 378-380 (code-css -> code-css)
  - B96: orig 372-372 -> cand 382-382 (code-css -> code-css)
  - B97: orig 374-374 -> cand 384-384 (code-css -> code-css)
  - B104: orig 415-418 -> cand 425-428 (code-css -> code-css)
  - B152: orig 933-935 -> cand 943-945 (body -> body)
  - B154: orig 945-948 -> cand 954-957 (body -> body)

Why this mass is right: the 80 TRANS-UNANCHORED and 33 TRANSLATION-ANCHORED blocks are the documentation body, the GoI format specimen, and the formatting specimens, translated one-to-one; the appendix resolves the unanchored queue block by block and finds no restoration, drop, or exhibit change hiding in it (the two structural exceptions, B153 and B155, are adjudicated in section 8). Three translation decisions are worth naming. (1) The bibliography entries (B74, and the B155 span) keep their citation text in English and translate only the framing prose: a bibliographic citation is a reference string, not reader prose. (2) The SAPPHIRE lore paragraphs keep the French society name in French with a Japanese gloss (B14 span), matching the original's own presentation. (3) The CSS comment mass (39 COMMENT-TEXT blocks) is translated in place; comments never render, so this is completeness, not display. The T5 verdict on the row was FINDINGS with no translation residue recorded against the current text.


## 7. Links

- LINK-REPOINT (C): Link target repointed (P11): prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.
  Verify: Probe the target; a repoint needs sameness evidence.
  - B10: orig 57-58 -> cand 56-57 (body -> body)

Why this instance is right, with one exception: B10 is the components list: the flopstyle credit link [[[theme:flopstyle]]] keeps its plain form because the target resolves on production scp-jp (this lane's T1 run with --check-links reports no link-target finding for it; the monotypical ground). The P11 set (six EN body links) was absolutized to scp-wiki.wikidot.com with branch annotations (B2, B12, B18 spans and appendix R7/R8) and dispositioned as the sibling/batch-posting class in register (c3). One annotation in that set is wrong: candidate L63 annotates the link to https://fondationscp.wikidot.com (the French branch) with the annotation for the English version; the original L64 calls the same target the "French SCP Branch". That is defect flag F1 (per-theme record): a one-word correction for the coordinator's fix lane; the package is written against the candidate as it stands.


## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B153: orig 943-943 -> cand at 953 (body -> body)
  - B155: orig 951-952 -> cand 960-960 (body -> body)
  - B156: orig 955-969 -> cand at 963 (body -> body)

No exhibit was dropped or replaced. The EXHIBIT-RESTRUCTURE label fired on three tail blocks (B153, B155, B156) whose content is delivery and license mechanics, not exhibits; the exhibit census (the formatting example, the GoI format example with its footnote and bibliography blocks, the tabview specimen, the Series note) is present on both sides with the same members.


Exhibit decisions, block by block:

- B153 (orig L944, the [[include :scp-wiki:component:license-box-theme]] line, deleted): not an exhibit. The include is the license-box wrapper component; the licensed-content block it wrapped stands in the candidate in the same position with all four fields translated (filename, name, author DrGemini, license CC BY-SA 3.0), so no licensed content was lost. The wrapper's removal is recorded as observation O1 in section 11; a KB-63 drop is not charged, because the block the wrapper existed to present is present.
- B155 (orig L951-952 to cand L960): the presentation-page note and Darwin citation framing, translated (section 6); the label is a false fire on a prose block at the file tail.
- B156 (orig L955-969, deleted at the tail): the original's tail delivery zone, relocated to the head (section 3); nothing in it was an exhibit.
- Bare-Rate reasoning: the candidate's one remaining bare [[module Rate]] (cand L210) stands inside the GoI format specimen and is KEPT, for the reasons re-derived in the per-theme record (item 26): the original ships the identical specimen Rate at orig L211, so deleting it would break specimen parity. The head-zone bare Rate the FIX class actually targets (orig L10) was deleted.


## 9. Formatting only

- WS-ONLY blocks: 19
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

None, verified rather than merely unsigned: the candidate carries no porter-note comments (no bracketed annotation, no translation note). The only comment text the port adds is the translated CSS banner and section comments (section 6, class R1), which are the original's own comments in Japanese, not annotations about the port.

## 11. Dispositions and exceptions

- No derived presence label fired.

The dispositions restated so a reviewer can re-derive them from this package:

- Item 26 [B] (the specimen Rate): DISPOSITIONED by FIX5 (FIX5-FURNA), re-derived in the per-theme record below. Ground: the class-B labelled-specimen exception; the specimen Rate is the original's own, at the original's own position inside its format example, and the head-zone Rate the FIX class targets was deleted.
- Register (c2), RERUN16 (EN18) row, all DISPOSITIONED: page-overflow (682/685px at 320/375 and 989px at 768 in chromium; 672/675px and 996px in webkit) driven by the cross-cutting preview-chrome rate module (KB-40/KB-34 family), and the sample's static-credit replica width (KB-33): environment-layer shapes shared by every theme carrying the preview chrome, not this candidate's CSS. The runtime-hotlink line is the shared site-theme chain (KB-40). The sample credit-modal errors are the preview form's property (credit:start-preview has no modal mechanism; KB-32, GOSIGN-TESTS T2 amendment). The sample bibliography-not-found line is a stale static-cache caution (KB-49). The missing saphir-header/sapphire-logo files are the owner-deferred asset hosting state (KB-58, owner decision 2026-11-16).
- Register (c1): the five T1 pseudo-ref errors are the candidate's own draft-host addresses (KB-41, class (ii)); posting rewrites them to the scp-jp host. The double-rate info is item 26's surface, dispositioned above.
- Register (c3): P3 credit fields FIXED by the credit waves (checker-verified), moving the row to (e); P11 (six EN body links) DISPOSITIONED as the sibling/batch-posting class.
- Draft-host self-delivery (B1/B21/B55/B106 spans): class (iii) draft-stage form, sanctioned (KB-41); not a defect at this stage.
- Observation O1 (not a disposition): the license-box wrapper includes do not survive (B153), while the licensed-content block they wrapped stands translated in place. Recorded so a future reader does not have to re-derive whether content was lost; it was not.


## 12. Verification

- T1: this lane re-ran the checker on the current candidate (uv run scripts/check_source.py pages/theme:saphir-jp.txt --kind theme --translation --check-links, from the skill directory /home/roku/src/SCP-JP/claude-plugins-staff/plugins/scp-jp-staff/skills/theme-component-review): exit 1, 5 errors / 0 warns / 2 infos, identical to the T1-ROWS row 127 baseline. All 5 errors are pseudo-ref on the candidate's own draft-host addresses (L7, L8, L100, L212, L442); the 2 infos are the double-rate note at L210 (item 26's surface, dispositioned) and one !important at L600, inherited from the original's CSS.
- T2/T3: RERUN16 (EN18) row; its full statement is in the generated stamp, and its lines are dispositioned in section 11. Not re-run by this lane (render checks belong to the campaign's render pass; this package's deciding checks are the byte censuses in the per-theme record).
- T4: LOCALIZE-ROWS row 132 (3 display-affecting findings: pattern 3 credit fields, pattern 11 links, and the duplicate Rate that became item 26); the follow-up diff is the FIX5 wave's re-judgement (supplement (d); FIX5-FURNA), re-derived below.
- T5: judged jointly with T4 on this row; no translation residue recorded.
- Package checks, run by this lane: candidate.txt sha256 equals the canonical file's; original.txt sha256 equals the sources.tsv value; the CSS brace-depth scan ends at depth 0 with no negative excursion on both files; the bare-Rate census is original L10 + L211, candidate L210 only.


## Per-theme record — item 26 [B] re-derivation and second-reviewer walk

The blocking item. GOSIGN2-LEDGER (e) item 26 [B]: a duplicate bare [[module Rate]] standing next to the preview credit module, charged as a defined FIX class (delete the bare module) that was executed for the Stage-1 and EN1-EN12 row sets but never for this row; the charging lane noted the bare module sits inside the theme's GoI format example block (candidate L210), away from the credit module at L24, and that no wave removed it or recorded the specimen disposition. FIX5 re-judged it DISPOSITIONED (FIX5-FURNA): the class-B labelled-specimen exception — the module is a labelled exhibit inside the theme's own format example, and the original ships the identical specimen.

Re-derivation from this package's bytes (this lane, 2026-11-17):

1. The original ships the identical bare [[module Rate]] inside its own GoI format specimen: original.txt L211. The full bare-Rate census is original L10 and L211; candidate L210 only (grep on both files).
2. The candidate's L210 sits inside the format-example block (heading at cand L205), five lines into the specimen and 186 lines below the credit module at cand L24 (210 minus 24). It is not adjacent to the credit module in any rendering sense; it is inside a labelled specimen the page presents as copyable format documentation.
3. The head-zone bare Rate the FIX class actually targets (original L10, under the "= **Rating**" heading, beside the info modules) IS deleted in the candidate (block B3). What survives is the specimen, so the charge's premise (an un-removed live duplicate beside the credit module) does not survive contact with the bytes: what remains is specimen parity with the original.
4. The T1 checker's double-rate info fires at candidate L210 with its own specimen caveat (a labelled specimen pairing is acceptable), consistent with the disposition.

Ground confirmed exactly; the disposition stands.

Second-reviewer walk. Is the ground checkable by a reader who did none of the work? The exception's deciding facts are all in this package: the original's specimen Rate (original.txt L211), the candidate's (candidate.txt L210), the deleted head-zone Rate (diff.md, block B3), and the distance from the credit module. One weakness in the campaign record, repaired here: the ledger's charge text and the supplement's disposition sit in different documents, and the charge's position note was the only place the specimen fact appeared before this package; a reader of the candidate alone could still mistake L210 for a leftover. This package removes that ambiguity. Walk outcome: sound.

Defect flags (this lane does not edit candidates):

- F1 (minor): candidate L63 annotates the French branch link (https://fondationscp.wikidot.com) with the annotation for the English version; the original L64 names the same target the French SCP Branch. One-word correction for the coordinator's fix lane.
- O1 (observation, not a defect): the license-box wrapper includes are dropped while the licensed content stands (section 8, block B153). No licensed field was lost; recorded so the shape is not re-charged as a KB-63 drop.

### Repair landed after this package was built

- F1 repaired by FIX-RDISP11 (record R/review-scout/FIX-RDISP11.md), landed in commit cc4b4d8: the annotation on the French branch link at candidate L63 now reads （フランス語版）; the same line's SAPPHIRE（英語版） annotation is unchanged, and a whole-file census confirmed L63 was the only mis-annotated instance. Checker finding output is byte-identical before and after (5 errors / 0 warns / 2 infos, the batch baseline). candidate.txt is recopied from the repaired candidate in this refresh; the regenerated stamp reads STALE, no re-judgement is fabricated, and the frozen ledger remains the verdict record.

## Appendix — residue blocks

### Residue R1 — B6 (residue; orig 45-45 -> cand 44-44, body -> body)
- Removed first line: + How to Use
- Added first line: + 使用方法

Resolution: section 6, class P10. The section heading '+ How to Use' is translated; the heading level (a single '+') is the anchor the classifier's anchor-majority rule missed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R2 — B8 (residue; orig 50-50 -> cand 49-49, body -> body)
- Removed first line: = **##var(--c-keyword)|[[include##** ##var(--c-symbol)|:scp-wiki:theme:saphir##**##var(--c-keyword)|]]##**
- Added first line: = **##var(--c-keyword)|[[include##** ##var(--c-symbol)|:scp-jp:theme:saphir-jp##**##var(--c-keyword)|]]##**

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R3 — B19 (residue; orig 88-88 -> cand 87-87, body -> body)
- Removed first line: + Example Formatting
- Added first line: + 整形例

Resolution: section 6, class P10. The section heading '+ Example Formatting' is translated; the heading level is the anchor the classifier's anchor-majority rule missed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R4 — B56 (residue; orig 215-216 -> cand 214-215, body -> body)
- Removed first line: ++* Title
- Added first line: ++* 表題

Resolution: section 6, class P10. A specimen heading inside the GoI format example translated in place; the heading markup (level and emphasis) is the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R5 — B63 (residue; orig 239-240 -> cand 238-239, body -> body)
- Removed first line: @@++* Title@@
- Added first line: @@++* 表題@@

Resolution: section 6, class P10. The escaped @@...@@ specimen form of the same format heading, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R6 — B74 (residue; orig 287-287 -> cand 286-286, body -> body)
- Removed first line: : darwin : Darwin, C. R. (1874). //The Descent of Man, and Selection in Relation to Sex// (2nd ed.). John Murray: p. 3. (Original work published 1871)
- Added first line: : darwin : Darwin, C. R. (1874). //The Descent of Man, and Selection in Relation to Sex// (2nd ed.). John Murray: p. 3. (原著1871年刊行)

Resolution: section 6, class P10. A bibliography entry: the citation text is kept verbatim (a reference string, not reader prose) and only the framing parenthetical is translated (original-work date note).
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R7 — B77 (residue; orig 298-298 -> cand 297-297, body -> body)
- Removed first line: << [[size 120%]][[[non-prophet-organization-hub|A NON-PROPHET ORGANIZATION]]][[/size]] >>
- Added first line: << [[size 120%]][*https://scp-wiki.wikidot.com/non-prophet-organization-hub 無信仰組織（英語版）][[/size]] >>

Resolution: section 7, class P11. The SAPPHIRE hub link in the format specimen is absolutized to scp-wiki.wikidot.com and annotated as the English version; the target is an EN page, so the annotation is correct here (contrast flag F1 in section 7).
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R8 — B78 (residue; orig 303-303 -> cand 302-302, body -> body)
- Removed first line: @<&lt;&lt;>@ @@[[size 120%]][[[non-prophet-organization-hub|A NON-PROPHET ORGANIZATION]]][[/size]]@@ @<&gt;&gt;>@
- Added first line: @<&lt;&lt;>@ @@[[size 120%]][[*https://scp-wiki.wikidot.com/non-prophet-organization-hub 無信仰組織（英語版）]][[/size]]@@ @<&gt;&gt;>@

Resolution: section 7, class P11. The escaped @@...@@ specimen form of the same hub line, absolutized and annotated identically to B77.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R9 — B82 (residue; orig 327-327 -> cand 326-326, code-css -> code-css)
- Removed first line:  * By
- Added first line:  * 作者

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R10 — B86 (residue; orig 340-340 -> cand 339-339, code-css -> code-css)
- Removed first line:  * By
- Added first line:  * 作者

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R11 — B90 (residue; orig 353-353 -> cand 352-352, code-css -> code-css)
- Removed first line:  * By
- Added first line:  * 作者

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R12 — B99 (residue; orig 380-380 -> cand 390-390, code-css -> code-css)
- Removed first line: /* == COMMON == */
- Added first line: /* == 共通 == */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R13 — B109 (residue; orig 469-469 -> cand 479-479, code-css -> code-css)
- Removed first line: /* == SEARCH == */
- Added first line: /* == 検索 == */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R14 — B113 (residue; orig 539-539 -> cand 549-549, code-css -> code-css)
- Removed first line: /* ==== CONTENT AREA ==== */
- Added first line: /* ==== 本文領域 ==== */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R15 — B117 (residue; orig 620-620 -> cand 630-630, code-css -> code-css)
- Removed first line: /* == FORMATTING | [GENERAL] == */
- Added first line: /* == 整形 | [一般] == */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R16 — B118 (residue; orig 647-647 -> cand 657-657, code-css -> code-css)
- Removed first line: /* == FORMATTING | [SPECIAL] == */
- Added first line: /* == 整形 | [特殊] == */

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R17 — B140 (residue; orig 868-874 -> cand 878-884, code-css -> code-css)
- Removed first line:  *	Dbl-Extra-Small:	≤383.9px
- Added first line:  *	極小:	≤383.9px

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R18 — B2 (heuristic; orig 4-4 -> cand 19-19, body -> body)
- Removed first line: [[[sigma-9-themes|Sigma Themes]]] >> SAPPHIRE Theme Redux
- Added first line: [*https://scp-wiki.wikidot.com/sigma-9-themes Sigmaテーマ（英語版）] >> SAPPHIREテーマRedux
- Note: script delta without the anchor majority

Resolution: sections 6 and 7. The pseudocrumbs line: the sigma-9-themes link is absolutized and annotated (P11), and the theme name in the crumb is partially localized; the name itself is an identity string and stays in Latin form.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R19 — B5 (heuristic; orig 39-39 -> cand 38-38, body -> body)
- Removed first line: = This is a fork of “SAPPHIRE's Theme”, originally created by [[*user DrGemini]].
- Added first line: = これは[[*user DrGemini]]が作成した“SAPPHIRE's Theme”（SCP-FRのThème de SAPHIR）を、[[*user Lt Flops]]がフォークして整えた派生版です。
- Note: script delta without the anchor majority

Resolution: sections 1 and 6. The fork credit line, translated in full: it is one of the places the candidate carries DrGemini's authorship of the base work (section 1).
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R20 — B7 (heuristic; orig 47-47 -> cand 46-46, body -> body)
- Removed first line: = Copy this syntax and paste it onto the top of your page:
- Added first line: = 次の構文をコピーし、ページ上部に貼り付けてください。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R21 — B9 (heuristic; orig 55-55 -> cand 54-54, body -> body)
- Removed first line: = ,,This theme makes use of the following components and their variables:,,
- Added first line: = ,,このテーマは以下のコンポーネントとその変数を使用しています。,,
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R22 — B10 (heuristic; orig 57-58 -> cand 56-57, body -> body)
- Removed first line: * ,,[[[theme:flopstyle|]]] by [[user Lt Flops]],,
- Added first line: * ,,[[[theme:flopstyle]]]、[[user Lt Flops]]作,,

Resolution: section 7. The components list: the flopstyle credit link keeps its plain form because the target resolves on production scp-jp (no link-target finding in this lane's T1 run); the change is the original's empty-label link form gaining its target as label.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R23 — B11 (heuristic; orig 62-62 -> cand 61-61, body -> body)
- Removed first line: = **__What is this theme used for?__**
- Added first line: = **__このテーマは何に使いますか？__**
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R24 — B12 (heuristic; orig 64-64 -> cand 63-63, body -> body)
- Removed first line: = This theme represents the Group of Interest [[[saphir-centre|SAPPHIRE]]] from the **[[[https://fondationscp.wikidot.com/|French SCP Branch]]]**.
- Added first line: = このテーマは、**[*https://fondationscp.wikidot.com SCPフランス支部（英語版）]**の要注意団体[*https://scp-wiki.wikidot.com/saphir-centre SAPPHIRE（英語版）]を表現します。
- Note: script delta without the anchor majority

Resolution: sections 6 and 7. The GoI description line, translated; it carries defect flag F1 (the French branch link annotated as the English version), recorded in the per-theme record. The link target itself is unchanged from the original.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R25 — B13 (heuristic; orig 66-66 -> cand 65-65, body -> body)
- Removed first line: = For further information:
- Added first line: = 詳細は以下を参照してください。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R26 — B14 (heuristic; orig 69-69 -> cand 68-68, body -> body)
- Removed first line: The **Society of the Atheist Partisans of Progress for the Halt of the Irrational and Religious Enemy**, better known as "**SAPPHIRE**" ("SAPHIR" in French, //La Société Athée Pour la Halte de l'Idéologie Religieuse//), is a Group of Interest most established in Western Europe, but also present in Eastern countries, Northern Africa, and the East Coast of the United States.
- Added first line: **神秘主義終焉のための無神論者協会**、通称「**SAPPHIRE**」（フランス語では“SAPHIR”、//La Société Athée Pour la Halte de l'Idéologie Religieuse//）は、主に西ヨーロッパを勢力圏とする要注意団体ですが、東側諸国、北アフリカ、そしてアメリカ合衆国の東海岸地域にも存在しています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R27 — B15 (heuristic; orig 71-71 -> cand 70-70, body -> body)
- Removed first line: The oldest known actions linked to SAPPHIRE date back to 1909, although the organization remained obscure until the 1960s, when SAPPHIRE seemingly went through a major expansion. The precise cause for this is unknown.
- Added first line: 知られている中で最古のSAPPHIRE関連活動は1909年まで遡りますが、SAPPHIREが大幅な発展を遂げたと思われる1960年代まで、この組織は不透明なままでした。この発展の正確な要因は不明です。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R28 — B16 (heuristic; orig 73-73 -> cand 72-72, body -> body)
- Removed first line: SAPPHIRE opposes all forms of belief, religion, and superstition, which they regard as the underlying cause of the woes affecting mankind, as well as SCP objects, which they consider to be the source of the aforementioned beliefs, religions, and superstitions.
- Added first line: SAPPHIREは、あらゆる形態の信仰・宗教・迷信を人類を苦しめる根本原因と見なし、それらに反対しています。また、前述の信仰・宗教・迷信の源と見なしたSCPオブジェクトにも反対しています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R29 — B17 (heuristic; orig 75-75 -> cand 74-74, body -> body)
- Removed first line: In spite of the ideal of rationality and humanism SAPPHIRE claims to adhere to, they do not hesitate to use anomalous means for terrorist purposes, committing attacks against both traditional and occult religions, the primary victims of these attacks often being civilians. Attacks can also be directed against superstitions, targeting [[[scp-227-fr|civilian clairvoyance enthusiasts]]], or rival organizations (including the Foundation).
- Added first line: SAPPHIREは合理性とヒューマニズムの理想を支持すると主張しているにもかかわらず、テロ目的で異常な手段を使用し、伝統的宗教とオカルト宗教の双方へ攻撃を加えることをためらいません。主な犠牲者となるのは往々にして民間人です。攻撃は迷信そのものに向けられることもあり、[*https://scp-wiki.wikidot.com/scp-227-fr 未来予知を愛好する民間人（英語版）]や、財団を含む競合組織も標的となります。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R30 — B18 (heuristic; orig 78-80 -> cand 77-79, body -> body)
- Removed first line: -- Selection from the **[[[saphir-centre|SAPPHIRE Hub]]]**
- Added first line: -- [*https://scp-wiki.wikidot.com/saphir-centre SAPPHIREハブ（英語版）]より抜粋
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R31 — B24 (heuristic; orig 115-115 -> cand 114-114, body -> body)
- Removed first line: = **bold** | //italic// | __underline__ | --strikethrough-- | {{teletype}} | ^^superscript^^,,subscript,,
- Added first line: = **太字** | //斜体// | __下線__ | --取り消し線-- | {{等幅}} | ^^上付き^^,,下付き,,
- Note: script delta without the anchor majority

Resolution: section 6, class P10. The formatting specimen's label words are translated while every markup symbol is kept byte-identical; the specimen still demonstrates the same forms.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R32 — B25 (heuristic; orig 117-117 -> cand 116-116, body -> body)
- Removed first line: = Type 4 hyphens [[span class="keycap"]]@@----@@[[/span]] to create a horizontal rule.
- Added first line: = ハイフン4個[[span class="keycap"]]@@----@@[[/span]]で水平線を作成できます。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R33 — B26 (heuristic; orig 127-129 -> cand 126-128, body -> body)
- Removed first line: [# A link]
- Added first line: [# リンク]
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R34 — B27 (heuristic; orig 131-133 -> cand 130-132, body -> body)
- Removed first line: # numbered list
- Added first line: # 番号付きリスト
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R35 — B31 (heuristic; orig 146-146 -> cand 145-145, body -> body)
- Removed first line: How quaint.
- Added first line: なんとも趣があります。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R36 — B33 (heuristic; orig 151-151 -> cand 150-150, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R37 — B34 (heuristic; orig 153-153 -> cand 152-152, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R38 — B35 (heuristic; orig 155-155 -> cand 154-154, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R39 — B36 (heuristic; orig 157-157 -> cand 156-156, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R40 — B37 (heuristic; orig 159-159 -> cand 158-158, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R41 — B38 (heuristic; orig 161-161 -> cand 160-160, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R42 — B39 (heuristic; orig 163-163 -> cand 162-162, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R43 — B40 (heuristic; orig 165-165 -> cand 164-164, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R44 — B41 (heuristic; orig 167-167 -> cand 166-166, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R45 — B42 (heuristic; orig 169-169 -> cand 168-168, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R46 — B43 (heuristic; orig 171-171 -> cand 170-170, body -> body)
- Removed first line: This is a long tab. It contains a lot of text.
- Added first line: これは長いタブです。大量のテキストが入っています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R47 — B50 (heuristic; orig 188-188 -> cand 187-187, body -> body)
- Removed first line: This is a blockquote.
- Added first line: これは引用ブロックです。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R48 — B51 (heuristic; orig 190-190 -> cand 189-189, body -> body)
- Removed first line: More text
- Added first line: さらにテキスト
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R49 — B52 (heuristic; orig 192-192 -> cand 191-191, body -> body)
- Removed first line: That's a horizontal rule.
- Added first line: これは水平線です。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R50 — B53 (heuristic; orig 194-194 -> cand 193-193, body -> body)
- Removed first line: > Nested blockquote
- Added first line: > 入れ子の引用ブロック
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R51 — B58 (heuristic; orig 224-224 -> cand 223-223, body -> body)
- Removed first line: The SAPPHIRE Format is known in-universe as the “Zetetic Bulletin”.[[footnote]]Fun fact! The Flat Earth Society was originally known as the Universal Zetetic Society. [[/footnote]] For an example of the format in action, see:
- Added first line: SAPPHIREフォーマットは作中では“Zetetic Bulletin”として知られています。[[footnote]]豆知識です。Flat Earth SocietyはもともとUniversal Zetetic Societyとして知られていました。[[/footnote]]実際の使用例として、以下を参照してください。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. The SAPPHIRE Format introduction translated, including its footnote text, which is part of the specimen prose.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R52 — B60 (heuristic; orig 228-228 -> cand 227-227, body -> body)
- Removed first line: Open the format by pasting the following div //before// or //after// the rating module:[[footnote]] If you ask me, it looks cleaner //before//. [[/footnote]]
- Added first line: 評価モジュールの//前//または//後//に次のdivを貼り付けて、フォーマットを開きます。[[footnote]]私に言わせれば、//前//に置いたほうがすっきり見えます。[[/footnote]]
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R53 — B61 (heuristic; orig 234-234 -> cand 233-233, body -> body)
- Removed first line: The SAPPHIRE Format is a mock essay or dissertation. Each paragraph is **indented**[[footnote]] Except for the introductory paragraph. [[/footnote]] and the entire format's text is **justified**. Both these properties are pre-baked into the theme's CSS.
- Added first line: SAPPHIREフォーマットは論考や学位論文を模したものです。各段落は**字下げ**され[[footnote]]導入段落を除きます。[[/footnote]]、フォーマット全体の文章は**両端揃え**になります。この2つの性質はどちらもテーマのCSSにあらかじめ組み込まれています。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R54 — B62 (heuristic; orig 236-236 -> cand 235-235, body -> body)
- Removed first line: Next, indicate the format's title and in-universe author's name (not your own):
- Added first line: 次に、フォーマットの表題と作中著者名を示します。あなた自身の名前ではありません。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R55 — B64 (heuristic; orig 243-243 -> cand 242-242, body -> body)
- Removed first line: Then, a section heading, which is often used several times throughout the format:
- Added first line: 次に、フォーマット全体でよく何度も使われる節見出しです。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R56 — B65 (heuristic; orig 248-248 -> cand 247-247, body -> body)
- Removed first line: @@++++ SECTION HEADING@@
- Added first line: @@++++ 節見出し@@
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R57 — B66 (heuristic; orig 253-253 -> cand 252-252, body -> body)
- Removed first line: For quoted passages:
- Added first line: 引用文には以下を使います。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R58 — B67 (heuristic; orig 257-257 -> cand 256-256, body -> body)
- Removed first line: Text here.
- Added first line: 本文をここに入れます。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R59 — B68 (heuristic; orig 261-261 -> cand 260-260, body -> body)
- Removed first line: Example:
- Added first line: 例として、以下のようになります。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R60 — B69 (heuristic; orig 264-264 -> cand 263-263, body -> body)
- Removed first line: Ignorance more frequently begets confidence than does knowledge: it is those who know little, and not those who know much, who so positively assert that this or that problem will never be solved by science.[((bibcite darwin))]
- Added first line: 無知はしばしば、知識以上に自信を生みます。この問題やあの問題は科学では決して解けないと断言するのは、多くを知る者ではなく、ほとんど知らない者なのです。[((bibcite darwin))]
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R61 — B70 (heuristic; orig 267-267 -> cand 266-266, body -> body)
- Removed first line: If your article has any footnotes or bibliographic citations, place their respective blocks at the end of all inner elements. If you're unsure about how to set up a bibliography, [*https://www.wikidot.com/doc-wiki-syntax:bibliography Wikidot provides a short explanation]. Any bibliography section should come after the footnotes:
- Added first line: 記事に脚注や文献参照がある場合は、対応するブロックを内側の全要素の末尾へ置いてください。参考文献欄の設定方法が分からなければ、[*https://www.wikidot.com/doc-wiki-syntax:bibliography Wikidotが短い説明を用意しています（英語版）]。参考文献欄は必ず脚注の後に置きます。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. The format-closing instructions translated; the embedded Wikidot documentation link is kept as the original's external reference.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R62 — B71 (heuristic; orig 274-274 -> cand 273-273, body -> body)
- Removed first line: Finally, close the format. Include SAPPHIRE's watchword for extra points:
- Added first line: 最後にフォーマットを閉じます。SAPPHIREの標語を入れると加点です。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R63 — B72 (heuristic; orig 278-278 -> cand 277-277, body -> body)
- Removed first line: @@+++* When in doubt, doubt.@@
- Added first line: @@+++* 疑わしいなら、疑え。@@
- Note: script delta without the anchor majority

Resolution: sections 5 and 6. The watchword specimen line, translated to the same value the header variable carries; the escaped @@...@@ specimen form is kept.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R64 — B73 (heuristic; orig 282-282 -> cand 281-281, body -> body)
- Removed first line: And you're done!
- Added first line: これで完了です。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R65 — B76 (heuristic; orig 295-295 -> cand 294-294, body -> body)
- Removed first line: = The following is for a Series and is __not__ a part of the SAPPHIRE Format:
- Added first line: = 以下はシリーズ用であり、SAPPHIREフォーマットの一部ではありません。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R66 — B81 (heuristic; orig 322-322 -> cand 321-321, code-css -> code-css)
- Removed first line: /* ==== FONTS ==== */
- Added first line: /* ==== フォント ==== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R67 — B94 (heuristic; orig 365-365 -> cand 375-375, code-css -> code-css)
- Removed first line: /* ==== SAPPHIRE Theme Redux ==== */
- Added first line: /* ==== SAPPHIREテーマRedux ==== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R68 — B98 (heuristic; orig 378-378 -> cand 388-388, code-css -> code-css)
- Removed first line: /* ==== HEADER AREA ==== */
- Added first line: /* ==== ヘッダー領域 ==== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R69 — B100 (heuristic; orig 383-383 -> cand 393-393, code-css -> code-css)
- Removed first line:     /* = SITE BANNER = */
- Added first line:     /* = サイトバナー = */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R70 — B102 (heuristic; orig 392-392 -> cand 402-402, code-css -> code-css)
- Removed first line:     /* = OVERALL COLOUR DEFINITIONS = */
- Added first line:     /* = 全体の色定義 = */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R71 — B103 (heuristic; orig 409-409 -> cand 419-419, code-css -> code-css)
- Removed first line:     /* = SAPHIR NAV COLOUR DEFINITIONS = */
- Added first line:     /* = SAPHIRナビゲーション色定義 = */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R72 — B105 (heuristic; orig 429-429 -> cand 439-439, code-css -> code-css)
- Removed first line: /* == SITE BANNER == */
- Added first line: /* == サイトバナー == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R73 — B110 (heuristic; orig 485-485 -> cand 495-495, code-css -> code-css)
- Removed first line: /* == TOP MENU == */
- Added first line: /* == トップメニュー == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R74 — B111 (heuristic; orig 495-495 -> cand 505-505, code-css -> code-css)
- Removed first line: /* == LOGIN == */
- Added first line: /* == ログイン == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R75 — B112 (heuristic; orig 531-531 -> cand 541-541, code-css -> code-css)
- Removed first line: /* == SIDE MENU == */
- Added first line: /* == サイドメニュー == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R76 — B114 (heuristic; orig 541-541 -> cand 551-551, code-css -> code-css)
- Removed first line: /* == INFO BAR == */
- Added first line: /* == 情報バー == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R77 — B115 (heuristic; orig 547-547 -> cand 557-557, code-css -> code-css)
- Removed first line: /* == PAGE RATING == */
- Added first line: /* == ページ評価 == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R78 — B116 (heuristic; orig 583-583 -> cand 593-593, code-css -> code-css)
- Removed first line: /* == INFO MODULE == */
- Added first line: /* == 情報モジュール == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R79 — B119 (heuristic; orig 654-654 -> cand 664-664, code-css -> code-css)
- Removed first line: /* == SAPPHIRE GOI FORMAT == */
- Added first line: /* == SAPPHIRE GoIフォーマット == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R80 — B120 (heuristic; orig 716-716 -> cand 726-726, code-css -> code-css)
- Removed first line: /* == SAPPHIRE RATING ALTERATION == */
- Added first line: /* == SAPPHIRE評価表示の変更 == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R81 — B127 (heuristic; orig 752-752 -> cand 762-762, code-css -> code-css)
- Removed first line: /* == SAPPHIRE INFO MODULE ALTERATION == */
- Added first line: /* == SAPPHIRE情報モジュールの変更 == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R82 — B131 (heuristic; orig 770-770 -> cand 780-780, code-css -> code-css)
- Removed first line: /* == NAVIGATION == */
- Added first line: /* == ナビゲーション == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R83 — B133 (heuristic; orig 825-825 -> cand 835-835, code-css -> code-css)
- Removed first line: /* ==== YUI TABS ==== */
- Added first line: /* ==== YUIタブ ==== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R84 — B134 (heuristic; orig 827-827 -> cand 837-837, code-css -> code-css)
- Removed first line: /* == YUI TAB CUSTOMIZATION == */
- Added first line: /* == YUIタブカスタマイズ == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R85 — B135 (heuristic; orig 834-834 -> cand 844-844, code-css -> code-css)
- Removed first line:     /* = Tab Background Colour | [UNSELECTED] = */
- Added first line:     /* = タブ背景色 | [未選択] = */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R86 — B136 (heuristic; orig 844-844 -> cand 854-854, code-css -> code-css)
- Removed first line:     /* = Tab Background Colour | [SELECTED] = */
- Added first line:     /* = タブ背景色 | [選択済み] = */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R87 — B137 (heuristic; orig 854-854 -> cand 864-864, code-css -> code-css)
- Removed first line:     /* = Tab Background Colour | [HOVER] = */
- Added first line:     /* = タブ背景色 | [ホバー] = */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R88 — B138 (heuristic; orig 863-863 -> cand 873-873, code-css -> code-css)
- Removed first line: /* ==== BREAKPOINTS ==== */
- Added first line: /* ==== ブレークポイント ==== */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R89 — B139 (heuristic; orig 865-865 -> cand 875-875, code-css -> code-css)
- Removed first line: /* == BREAKPOINTS KEY == */
- Added first line: /* == ブレークポイント凡例 == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R90 — B141 (heuristic; orig 877-877 -> cand 887-887, code-css -> code-css)
- Removed first line: /* == DBL-EXTRA-SMALL MEDIA QUERY == */
- Added first line: /* == 極小メディアクエリ == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R91 — B143 (heuristic; orig 885-885 -> cand 895-895, code-css -> code-css)
- Removed first line: /* == EXTRA-SMALL MEDIA QUERY == */
- Added first line: /* == 小メディアクエリ == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R92 — B145 (heuristic; orig 893-893 -> cand 903-903, code-css -> code-css)
- Removed first line: /* == SMALL MEDIA QUERY == */
- Added first line: /* == 狭メディアクエリ == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R93 — B149 (heuristic; orig 909-909 -> cand 919-919, code-css -> code-css)
- Removed first line: /* == MEDIUM MEDIA QUERY == */
- Added first line: /* == 中メディアクエリ == */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; the taxonomy's patterns feedback records CSS comments as a known non-finding, and no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R94 — B153 (heuristic; orig 943-943 -> cand at 953, body -> body)
- Removed first line: [[include :scp-wiki:component:license-box-theme]]
- Note: no translated counterpart on the added side; the writer's replaced-vs-dropped call is forced

Resolution: section 8 (exhibit-decision). The license-box wrapper include line; adjudicated there: not an exhibit, and the licensed content it wrapped stands translated in place (observation O1).
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R95 — B155 (heuristic; orig 951-952 -> cand 960-960, body -> body)
- Removed first line: > This presentation page contains an excerpt from //[*https://en.wikisource.org/wiki/The_Descent_of_Man_(Darwin) The Descent of Man, and Selection in Relation to Sex]// (1874) by Charles Darwin (Public Domain).
- Added first line: > このプレゼンテーションページには、チャールズ・ダーウィンの//[*https://en.wikisource.org/wiki/The_Descent_of_Man_(Darwin) The Descent of Man, and Selection in Relation to Sex]//（1874年、パブリックドメイン）からの抜粋が含まれています。
- Note: no translated counterpart on the added side; the writer's replaced-vs-dropped call is forced
- Note: script delta without the anchor majority

Resolution: section 6, class P10. The presentation-page note at the file tail, translated; the EXHIBIT-RESTRUCTURE label on this block is a false fire on a prose block (section 8).
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


## License and attribution

- **Title:** SAPPHIRE Theme Redux
- **Author:** Lt Flops
- **Source:** https://scp-wiki.wikidot.com/theme:saphir — revision 14
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
