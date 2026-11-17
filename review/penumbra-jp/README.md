# Review package — theme:penumbra-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:penumbra-jp — origin EN, population #28 [GOSIGN2-LEDGER (b) row 28]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 5dda2aea9d0d113be8adfe82d1106cfc719322902b9553cb7e8290bb3ebea511); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 2 warns / 2 infos (http×2); standing classes dispositioned in register c1 [T1-ROWS row 28; GOSIGN2-LEDGER (b) row 28]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sample T2 incomplete (webkit screenshot pixel-cap ×3, no summary), notice left-clip, faint WebKit CC badge, sample credit-modal; no candidate-CSS defect. [RENDER-ROWS-1 (RENDER-C row 28)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 28)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 28, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 28]
- FIX5 re-judgement: item 4 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: pattern-7 JP font load / stack suffixes; checker code-multiset identical before/after [GOSIGN2-LEDGER-SUPPLEMENT (a) item 4]
- Computed against: canonical commit 6660ec54e07a141648515df0ad6f1659fd2442aa; candidate file pages/theme:penumbra-jp.txt sha256:5dda2aea9d0d113be8adfe82d1106cfc719322902b9553cb7e8290bb3ebea511; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation over the classifier skeleton; the verdict stamp above is generated)
Candidate: review/penumbra-jp/candidate.txt (sha256 4aa146d9183411560f3723dc09383e14692dbb5c8306b732bed6dc1e28411838)
Original: theme:penumbra — scp-wiki, revision 155 (sha256 c5deb23d0c89f9d2b5367dcc75083d78202ae1c2b14f00bfbcc5185c46c69215)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.
- Production-adoption signal: candidate resembles the production JP counterpart at 0.99 similarity vs 0.68 for the original (R4); declaration is a slot below.

Provenance route: adopted from the production JP counterpart (R4). Body similarity is 0.986 against the production page (pages-existing/existing:theme-penumbra.txt) and 0.684 against the rev 155 mirror; the candidate is the production page's Sigma-10 migration, and most of its distance from the mirror is production drift, not porting. The mirror is the later of the credit block's two reference revisions (first translation rev 41, retranslation rev 155). The stamp above is STALE by design: the candidate changed after the verdict (the frame remedy of section 3 and snippet-audit sequelae), so the stamp's findings describe the pre-change file; the per-theme record narrates what changed after. The mirror is review-mirrors/orig-penumbra-rev155.txt (FETCH-REGEN, 36,433 bytes, sha256 c5deb23d0c89f9d2b5367dcc75083d78202ae1c2b14f00bfbcc5185c46c69215), byte-identical to original.txt in this package and to the sources.tsv row.


## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| ASSET-REHOST | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 2 |
| CREDIT-PROSE | 3 |
| CSS-BODY | 129 |
| EXHIBIT-RESTRUCTURE | 4 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 2 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 2 |
| TRANS-UNANCHORED | 53 |
| TRANSLATION-ANCHORED | 12 |

Counts: 214 blocks, 25 specific, 177 heuristic, 12 residue, 0 skipped (comment text).

## Per-theme record — the FIX5 re-derivation

This theme's one blocking item is GOSIGN2-LEDGER section (e) item 4 [D] (ledger (b) row 28): pattern 7, no JP face in any font stack, display-affecting; at ledger time the candidate file had zero JP font references and no JP font load. GOSIGN2-LEDGER-SUPPLEMENT re-judges it FIXED (FIX5-FONTSA, canonical commit 8eacd6e: pattern-7 JP font load and stack suffixes, with the checker's code-multiset identical before and after).

Re-derived from this package's bytes: the candidate imports Noto Sans JP (weights 400 and 700) at line 280, inside the delivered module CSS (the live [[module CSS show="true"]] at line 257), preceded by the porter's comment at lines 276-279 explaining that the Latin faces have no Japanese glyphs. The face is named in delivered stacks at lines 285, 351, 460, 845, 849, 856, 865, and 871. The candidate has no code blocks at all (section 3), so the load sits in the live channel, not in an exhibit. The fix is present and complete.

The theme's remaining ledger findings re-derive as follows (ledger c3: P3 FIXED, P6 FIXED in the frame waves, P7 to item 4). LOCALIZE-ROWS row 28 records: (a) P6, the missing interwiki-style frame: the frame stands at candidate lines 1-3, in its final sub-shape (D) form (section 3). (b) P7: item 4, closed above. (c) P3, stray info-module text in the credit panel plus six missing credit fields, display-affecting: the current credit block (lines 13-27) carries nine fields and no stray text; the two absent fields are treated in section 1. The stamp's T4 count of 2 display-affecting findings is (b) and (c).

Post-verdict changes: the stamp was computed against canonical 20ce2906. Afterwards the frame took its sub-shape (D) remedy in 5d95177, re-applied after a snippet landing reverted it, together with snippet-audit sequelae. Those changes are why the stamp reads STALE; they do not reopen item 4, whose bytes are re-verified above.

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B4: orig 9-13 -> cand 13-13 (body -> body)
  - B7: orig 18-18 -> cand 24-27 (body -> body)

- TASL-FIELDS (A): Credit fields (ruling 3, KB-10): the eight attribution fields are required for the TASL record; campaign translations are credited to AI.
  Verify: Compare the credit block against the mirror's; every added field needs an evidenced value.
  - B5: orig at 15 -> cand 15-20 (body -> body)

- CREDIT-PROSE (C): Translated credit prose (P3/P10): attribution text is reader-visible and localizes with the page.
  Verify: Read the pair in the mirror and the candidate side by side.
  - B6: orig 16-16 -> cand 22-22 (body -> body)

This instance: the candidate's credit block (candidate lines 13-27) carries nine fields: title Penumbra Theme (JP form), translator ukwhatn, translation year 2021, original title Penumbra Theme, copyright holder EstrellaYoshte, creation year 2020, first-translation reference revision 41, retranslation reference revision 155, and the source link. The original carries no credit block (an info module with placeholder text, original lines 9-13); the author is named in prose on both sides (original line 15, candidate line 29), and the copyright-holder field names the same person, so there is no pointer defect. Two fields are absent, author and publication date: the original gives no publication date anywhere, and production's own credit block carries nothing but the placeholder text between the includes, so the candidate's field set is a campaign completion fuller than production, and the T1 baseline charges no credit error (its 2 errors are the http pair of section 11). The CREDIT-PROSE blocks are the banner and prose naming of the author, carried over.


## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B1: orig 1-1 -> cand 1-5 (body -> body)
  - B69: orig 232-233 -> cand 253-253 (body -> body)

This instance: the include census is short. The credit pair is section 1. The usage example at candidate line 33 names the candidate's own posting name, theme:penumbra-jp, the post-sweep form. The image-block at line 50 takes its file from JP storage (section 4). The toggle-sidebar include is repointed :scp-wiki: to :scp-jp: and moved out of the original's hidden tail div into the visible position at candidate line 255, before the CSS module. The prose link at candidate line 29, [[[theme:paperstack|...]]], names the base theme's production page and is byte-identical to production's line; it is recorded prose under the snippet audit, not drift.


## 3. Delivery and code loading

- SELF-DELIVERY (A): Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel.
  Verify: The named delivery resolves on the draft host and serves the current candidate body.
  - B213: orig 1447-1447 -> cand 1233-1239 (module-css -> module-css)

This instance: the delivery topology changes, and the change is the production form. The original delivers its [[code type="CSS"]] block (original line 235) from its own local--code/1, via a tail module @import and an interwiki frame carrying theme= (original lines 1447-1452). The candidate has no code blocks in any form (counted over [[code]], [[code type="css"]], and every other typed form: zero); its CSS is live module CSS, the main block at line 257 with show="true", which also serves as the displayed source, plus three JP correction modules at lines 1232, 1242, and 1250. The frame at lines 1-3 keeps priority=1 and drops the theme= parameter: that is sub-shape (D) of the population audit R/review-scout/FIX-CODEADDR.md, remedy landed in canonical 5d95177. With no code block on the page, a theme= address would name a block that cannot exist; the frame's remaining job is the BHL normalize layer. SELF-DELIVERY B213 is the removed original tail delivery, and no local--code reference remains anywhere in the candidate.


## 4. Fonts and assets

- FONT-IMPORT (B): Other font-load change (P5, KB-04): malformed family parameters (a hyphen for a +) make the load fail.
  Verify: KB-04: the family parameter form; the deciding evidence is the load probe (400 vs 200).
  - B72: orig 248-248 -> cand 272-274 (code-css -> body)

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B73: orig 250-276 -> cand 276-293 (code-css -> body)

This instance: FONT-IMPORT B72 is a re-host. The original loads Fira Code from fonts.bunny.net (original line 248) and Josefin Sans through four @font-face blocks on cdn.jsdelivr.net/gh/SYwaves; the candidate loads Josefin Sans, Roboto, and Fira Code from Google Fonts css2 (candidate lines 272-274). The re-host is production lineage. JPFONT-LOAD B73 is the FIX5 addition of the per-theme record: the Noto Sans JP import at line 280 with its porter comment, inside the delivered module. The two ASSET-REHOST blocks are the image-block file (line 50) and the --lgurl logo (line 1226), both to scp-jp-storage.wdfiles.com and both keeping the http scheme (class (ii), section 11; they are the T1 http pair). No font is named-but-unloaded or loaded-but-unapplied: Roboto applies at line 285 and throughout, Josefin Sans in the header stacks, Fira Code in the monospace stack, Noto Sans JP per item 4.


## 5. Header, sidebar, site furniture

- HEADERVAR (A): Header/title variables (P9/T6, KB-57): the header text variables are the theme's visible title surface.
  Verify: KB-57: where the value stays in the original's language, the disposition is ruling 2 (section 11).
  - B11: orig 26-30 -> cand 39-43 (body -> body)

This instance: HEADERVAR B11 (original lines 26-30 to candidate lines 39-43) is the darkbox :root usage exhibit; the candidate's exhibit values are translated placeholders, because the exhibit teaches JP readers which values to set. The delivered defaults are untouched and identical on both sides: content: var(--header-title, "SCP FOUNDATION") at candidate line 356 (original line 374) and the subtitle "SECURE - CONTAIN - PROTECT" at candidate line 361 (original line 379). Those are identity strings under ruling 2 (patterns KB-57), not prose defaults. The sidebar fact is the toggle-sidebar move of section 2.


## 6. Text translation

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B2: orig 4-4 -> cand 8-8 (body -> body)
  - B3: orig 7-7 -> cand 11-11 (body -> body)
  - B19: orig 49-49 -> cand 65-65 (body -> body)
  - B20: orig 51-51 -> cand 67-67 (body -> body)
  - B21: orig 53-53 -> cand 69-69 (body -> body)
  - B22: orig 55-55 -> cand 71-71 (body -> body)
  - B24: orig 63-64 -> cand 80-81 (body -> body)
  - B25: orig 66-67 -> cand 83-84 (body -> body)
  - B27: orig 71-72 -> cand 88-89 (body -> body)
  - B49: orig 119-119 -> cand 137-137 (body -> body)
  - B54: orig 135-137 -> cand 153-155 (body -> body)
  - B65: orig 212-212 -> cand 230-230 (body -> body)

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B8: orig 20-20 -> cand 29-29 (body -> body)
  - B9: orig 22-22 -> cand 31-31 (body -> body)
  - B10: orig 24-24 -> cand 33-37 (body -> body)
  - B12: orig 33-33 -> cand 46-46 (body -> body)
  - B14: orig 39-39 -> cand 52-52 (body -> body)
  - B15: orig at 41 -> cand 54-54 (body -> body)
  - B17: orig 44-44 -> cand 61-61 (body -> body)
  - B18: orig 46-47 -> cand 63-63 (body -> body)
  - B23: orig 57-57 -> cand 73-74 (body -> body)
  - B26: orig 69-69 -> cand 86-86 (body -> body)
  - B28: orig 74-74 -> cand 91-91 (body -> body)
  - B29: orig 76-76 -> cand 93-93 (body -> body)
  - B30: orig 78-78 -> cand 95-95 (body -> body)
  - B31: orig 80-80 -> cand 97-97 (body -> body)
  - B32: orig 82-82 -> cand 99-99 (body -> body)
  - B33: orig 84-84 -> cand 101-101 (body -> body)
  - B34: orig 86-86 -> cand 103-103 (body -> body)
  - B35: orig 89-90 -> cand 106-106 (body -> body)
  - B36: orig 92-92 -> cand 108-108 (body -> body)
  - B37: orig 94-94 -> cand 110-110 (body -> body)
  - B38: orig 96-96 -> cand 112-112 (body -> body)
  - B39: orig 98-98 -> cand 114-114 (body -> body)
  - B40: orig 100-100 -> cand 116-116 (body -> body)
  - B41: orig 102-102 -> cand 118-118 (body -> body)
  - B42: orig 104-104 -> cand 120-120 (body -> body)
  - B43: orig 106-106 -> cand 122-122 (body -> body)
  - B44: orig 108-108 -> cand 124-124 (body -> body)
  - B45: orig 110-110 -> cand 126-126 (body -> body)
  - B46: orig 112-112 -> cand 128-128 (body -> body)
  - B47: orig 114-114 -> cand 130-130 (body -> body)
  - B48: orig 116-116 -> cand 132-134 (body -> body)
  - B50: orig 125-125 -> cand 143-143 (body -> body)
  - B51: orig 127-127 -> cand 145-145 (body -> body)
  - B52: orig 129-129 -> cand 147-147 (body -> body)
  - B53: orig 131-131 -> cand 149-149 (body -> body)
  - B55: orig 151-151 -> cand 169-169 (body -> body)
  - B56: orig 153-154 -> cand 171-172 (body -> body)
  - B57: orig 156-156 -> cand 174-174 (body -> body)
  - B58: orig 160-160 -> cand 178-178 (body -> body)
  - B59: orig 162-162 -> cand 180-180 (body -> body)
  - B61: orig 171-171 -> cand 189-189 (body -> body)
  - B62: orig 184-184 -> cand 202-202 (body -> body)
  - B63: orig 198-198 -> cand 216-216 (body -> body)
  - B64: orig 210-210 -> cand 228-228 (body -> body)
  - B66: orig 219-221 -> cand 237-240 (body -> body)
  - B68: orig at 231 -> cand 249-251 (body -> body)

This instance: 12 anchored and 53 unanchored translation blocks, plus CSS comment translations, all one-to-one against the mirror; the unanchored prose set is resolved by shape in the appendix. One addition has no original counterpart sentence: candidate line 237 adds "the body is Roboto" to the font specimen exhibit, a translator's completion matching the delivered body stack of section 4; recorded here, not a defect. Nothing in this mass touches an exhibit's structure; the exhibit questions are section 8's.


## 7. Links

No LINK signature fired. On the bytes: the one prose link change is the Paperstack link of section 2 (target kept, link text translated), and the credit source link is in section 1. No live link changes host against the original.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B13: orig 37-37 -> cand 50-50 (body -> body)
  - B70: orig 235-235 -> cand 255-257 (code-css -> body)
  - B212: orig 1442-1443 -> cand 1224-1229 (body -> body)
  - B214: orig 1450-1453 -> cand 1242-1257 (body -> module-css)

- CSS-BODY (C): Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.
  Verify: Writer review; a recurring shape is a new-signature candidate for the patterns loop.
  - B74: orig 279-288 -> cand 296-297 (code-css -> body)
  - B75: orig 290-310 -> cand at 299 (code-css -> body)
  - B76: orig 316-317 -> cand 304-304 (code-css -> body)
  - B77: orig 322-322 -> cand 309-309 (code-css -> body)
  - B78: orig 326-326 -> cand 313-313 (code-css -> body)
  - B79: orig 330-332 -> cand 317-318 (code-css -> body)
  - B81: orig 340-340 -> cand 327-327 (code-css -> body)
  - B82: orig 342-342 -> cand at 329 (code-css -> body)
  - B83: orig 360-363 -> cand at 346 (code-css -> body)
  - B84: orig 369-369 -> cand 351-351 (code-css -> body)
  - B85: orig 375-376 -> cand 357-358 (code-css -> body)
  - B86: orig 380-381 -> cand 362-363 (code-css -> body)
  - B87: orig 385-387 -> cand 367-367 (code-css -> body)
  - B88: orig 392-398 -> cand 372-374 (code-css -> body)
  - B89: orig 400-408 -> cand 376-377 (code-css -> body)
  - B90: orig 411-448 -> cand 380-381 (code-css -> body)
  - B91: orig 451-451 -> cand 384-385 (code-css -> body)
  - B92: orig 453-460 -> cand 387-387 (code-css -> body)
  - B93: orig 462-481 -> cand 389-390 (code-css -> body)
  - B94: orig 484-501 -> cand at 393 (code-css -> body)
  - B95: orig 506-506 -> cand at 397 (code-css -> body)
  - B96: orig 509-510 -> cand 399-400 (code-css -> body)
  - B97: orig 513-513 -> cand 403-403 (code-css -> body)
  - B98: orig 520-520 -> cand at 410 (code-css -> body)
  - B99: orig 533-541 -> cand at 422 (code-css -> body)
  - B100: orig 543-543 -> cand 423-423 (code-css -> body)
  - B101: orig 546-551 -> cand 426-426 (code-css -> body)
  - B102: orig 553-553 -> cand 428-428 (code-css -> body)
  - B103: orig 557-557 -> cand 432-432 (code-css -> body)
  - B104: orig 561-562 -> cand 436-437 (code-css -> body)
  - B105: orig 566-566 -> cand 441-441 (code-css -> body)
  - B106: orig 574-575 -> cand 449-450 (code-css -> body)
  - B107: orig 577-578 -> cand 452-452 (code-css -> body)
  - B108: orig 582-582 -> cand at 456 (code-css -> body)
  - B109: orig 585-586 -> cand 458-464 (code-css -> body)
  - B110: orig 589-589 -> cand at 467 (code-css -> body)
  - B111: orig 591-592 -> cand 468-468 (code-css -> body)
  - B113: orig 596-615 -> cand 471-471 (code-css -> body)
  - B114: orig 620-621 -> cand at 476 (code-css -> body)
  - B116: orig 625-628 -> cand 478-478 (code-css -> body)
  - B117: orig 630-664 -> cand 480-481 (code-css -> body)
  - B118: orig 670-672 -> cand 487-489 (code-css -> body)
  - B119: orig 674-729 -> cand at 491 (code-css -> body)
  - B120: orig 741-741 -> cand 502-503 (code-css -> body)
  - B121: orig 755-756 -> cand 517-519 (code-css -> body)
  - B122: orig 762-762 -> cand 525-525 (code-css -> body)
  - B125: orig 794-794 -> cand 567-567 (code-css -> body)
  - B126: orig 797-797 -> cand 570-570 (code-css -> body)
  - B127: orig 805-805 -> cand 578-578 (code-css -> body)
  - B128: orig 817-818 -> cand 590-591 (code-css -> body)
  - B129: orig 855-855 -> cand 628-628 (code-css -> body)
  - B130: orig 860-860 -> cand 633-633 (code-css -> body)
  - B131: orig 864-864 -> cand 637-637 (code-css -> body)
  - B132: orig 919-920 -> cand 692-693 (code-css -> body)
  - B133: orig 923-924 -> cand 696-697 (code-css -> body)
  - B134: orig 926-927 -> cand 699-700 (code-css -> body)
  - B135: orig 929-932 -> cand at 702 (code-css -> body)
  - B136: orig 959-960 -> cand 728-729 (code-css -> body)
  - B137: orig 965-965 -> cand at 734 (code-css -> body)
  - B138: orig 972-972 -> cand 740-740 (code-css -> body)
  - B139: orig 981-981 -> cand 749-749 (code-css -> body)
  - B140: orig 988-989 -> cand 756-757 (code-css -> body)
  - B141: orig 992-992 -> cand 760-760 (code-css -> body)
  - B142: orig 999-1002 -> cand 767-769 (code-css -> body)
  - B144: orig 1010-1010 -> cand 798-798 (code-css -> body)
  - B145: orig 1012-1012 -> cand 800-800 (code-css -> body)
  - B146: orig 1019-1019 -> cand 807-807 (code-css -> body)
  - B147: orig 1021-1021 -> cand 809-809 (code-css -> body)
  - B148: orig 1026-1026 -> cand 814-814 (code-css -> body)
  - B149: orig 1033-1033 -> cand 821-821 (code-css -> body)
  - B150: orig 1037-1037 -> cand 825-825 (code-css -> body)
  - B151: orig 1042-1042 -> cand 830-830 (code-css -> body)
  - B152: orig 1046-1046 -> cand 834-834 (code-css -> body)
  - B153: orig 1049-1049 -> cand 837-837 (code-css -> body)
  - B154: orig 1056-1057 -> cand 844-845 (code-css -> body)
  - B155: orig 1061-1061 -> cand 849-849 (code-css -> body)
  - B156: orig 1063-1063 -> cand 851-851 (code-css -> body)
  - B157: orig 1068-1068 -> cand 856-856 (code-css -> body)
  - B158: orig 1076-1077 -> cand 864-865 (code-css -> body)
  - B159: orig 1081-1085 -> cand 869-872 (code-css -> body)
  - B160: orig 1087-1087 -> cand 874-874 (code-css -> body)
  - B161: orig 1094-1094 -> cand at 881 (code-css -> body)
  - B162: orig 1099-1099 -> cand 885-885 (code-css -> body)
  - B163: orig 1107-1107 -> cand 893-893 (code-css -> body)
  - B164: orig 1114-1116 -> cand 900-900 (code-css -> body)
  - B165: orig 1118-1118 -> cand at 902 (code-css -> body)
  - B166: orig 1124-1125 -> cand 907-908 (code-css -> body)
  - B167: orig 1131-1131 -> cand 914-914 (code-css -> body)
  - B168: orig 1135-1136 -> cand 918-919 (code-css -> body)
  - B169: orig 1141-1143 -> cand 924-926 (code-css -> body)
  - B170: orig 1157-1157 -> cand 940-940 (code-css -> body)
  - B171: orig 1167-1167 -> cand 950-950 (code-css -> body)
  - B172: orig 1169-1170 -> cand 952-957 (code-css -> body)
  - B173: orig 1173-1173 -> cand at 960 (code-css -> body)
  - B174: orig 1182-1184 -> cand at 968 (code-css -> body)
  - B175: orig 1186-1186 -> cand 969-969 (code-css -> body)
  - B176: orig 1188-1188 -> cand at 971 (code-css -> body)
  - B177: orig 1210-1210 -> cand 992-992 (code-css -> body)
  - B178: orig 1214-1214 -> cand 996-996 (code-css -> body)
  - B179: orig 1221-1221 -> cand 1003-1003 (code-css -> body)
  - B180: orig 1232-1232 -> cand 1014-1014 (code-css -> body)
  - B181: orig 1237-1237 -> cand 1019-1019 (code-css -> body)
  - B182: orig 1242-1242 -> cand 1024-1024 (code-css -> body)
  - B183: orig 1250-1250 -> cand 1032-1032 (code-css -> body)
  - B184: orig 1252-1252 -> cand 1034-1034 (code-css -> body)
  - B185: orig 1256-1256 -> cand 1038-1038 (code-css -> body)
  - B186: orig 1258-1258 -> cand 1040-1040 (code-css -> body)
  - B187: orig 1264-1288 -> cand at 1046 (code-css -> body)
  - B188: orig 1291-1291 -> cand 1048-1048 (code-css -> body)
  - B189: orig 1294-1297 -> cand 1051-1051 (code-css -> body)
  - B190: orig 1301-1301 -> cand 1055-1055 (code-css -> body)
  - B191: orig 1306-1307 -> cand 1060-1061 (code-css -> body)
  - B192: orig 1312-1312 -> cand 1066-1066 (code-css -> body)
  - B194: orig 1318-1322 -> cand 1072-1072 (code-css -> body)
  - B195: orig 1327-1327 -> cand 1077-1077 (code-css -> body)
  - B196: orig 1330-1334 -> cand 1080-1083 (code-css -> body)
  - B197: orig 1341-1341 -> cand 1090-1090 (code-css -> body)
  - B198: orig 1350-1351 -> cand 1099-1100 (code-css -> body)
  - B199: orig 1359-1359 -> cand 1108-1108 (code-css -> body)
  - B200: orig 1361-1370 -> cand at 1110 (code-css -> body)
  - B201: orig 1384-1384 -> cand 1123-1123 (code-css -> body)
  - B202: orig 1401-1401 -> cand at 1140 (code-css -> body)
  - B204: orig 1410-1415 -> cand 1149-1154 (code-css -> body)
  - B205: orig 1417-1417 -> cand 1156-1184 (code-css -> body)
  - B207: orig 1424-1424 -> cand 1193-1195 (code-css -> body)
  - B208: orig 1426-1426 -> cand 1197-1201 (code-css -> body)
  - B209: orig 1429-1429 -> cand 1204-1213 (code-css -> body)
  - B210: orig 1435-1435 -> cand 1219-1219 (code-css -> body)
  - B211: orig 1439-1440 -> cand at 1223 (code-css -> body)

This instance: the 129 CSS-BODY blocks are R4 production drift, not per-block port edits: production's older literal-value CSS and selector forms stand against rev 155's var()-based CSS, which is what the similarity figures say (0.986 to production, 0.684 to the mirror). They are resolved as one shape in the appendix. A brace-depth scan over the delivered CSS returns to 0 with no negative dip on both sides, so the drift carries no structural damage.


B13 (original line 37 to candidate line 50): replaced; the image-block exhibit takes the JP storage file address of section 4, its exhibit role unchanged. B70 (original line 235 to candidate lines 255-257): replaced; the Source Code heading now precedes the live module whose show="true" displays the source, so the exhibit function is preserved by the delivery form of section 3. B212 (original lines 1442-1443 to candidate lines 1224-1229): the tail-region pair; the original's hidden toggle-sidebar div is treated in section 2 and its tail delivery in section 3, and the candidate side is the main module's closing :root block. B214 (original lines 1450-1453 to candidate lines 1242-1257): replaced; the original's interwiki tail frame gives way to the candidate's tail correction modules. B67 is not an exhibit decision and is not resolved here: see the flag in section 11.


## 9. Formatting only

- WS-ONLY blocks: 0
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

- ANNOTATION (B): Porter annotation added (R2): translator notes and editor lines are the porter's voice, listed so they are never mistaken for original content.
  Verify: Each annotation is the porter's addition, absent from the mirror.
  - B71: orig at 246 -> cand 268-269 (body -> body)

This instance: the annotations are the banner line "Edited for SCP-JP by ukwhatn" (candidate line 268, block B71; the TAXONOMY memo's R2 entry names this exact line for this theme), the JP font comment at lines 276-279 riding inside B73, and the three tail-module comments at lines 1233, 1243, and 1251 explaining each JP correction; the credit one carries the retarget rationale (the JP credit module emits the anchor as a direct child of .creditButton, so the EN rules never matched).


## 11. Dispositions and exceptions

- No derived presence label fired.

Class (ii) dispositions: the http pair (image-block file at candidate line 50, --lgurl at line 1226) are JP-storage addresses kept on http, a posting-form residue recorded here rather than charged. The stamp's T2/T3 findings (sample T2 incomplete by the WebKit screenshot pixel cap, notice left-clip, a faint WebKit CC badge, the credit-modal preview form) record no candidate-CSS defect. One open defect is recorded here because it is not a disposition: the escaped footnoteblock. Candidate line 245 reads @@[[footnoteblock]]@@ where the original (line 226) and production (line 231) carry the block live, in identical context (standalone, between rules, after the font exhibits). The candidate's footnote at line 89 is live, so the footnote text has no render position and the literal string displays instead. The ledger charges no item for it; it is flagged in the lane report with both loci, and this package documents the candidate as it stands. This paragraph describes the as-built package: the defect has since been repaired (FIX-RFIX89, landing 6660ec5), and the recopied candidate's L245 is now the live `[[footnoteblock]]`, matching both sources — see Post-package repairs (REFRESH3-E).


### Post-package repairs (REFRESH3-E)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:penumbra-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**Frame sub-shape (D) treated as (B) — already in this package.** For the record chain: this theme is one of FIX-FRAMED.md's twelve live-original files. Its frame was sub-shape (D) — `theme=` named its own /1 code block, which the candidate (zero `[[code]]` blocks; CSS in live `[[module CSS]]`) cannot contain — treated as (B) with the minimal remedy of dropping the `theme=` line and keeping the frame. The remedy landed at 5d95177 and was re-applied at c3e658f after a snippet landing reverted it (with sequelae 358955e and 20ce290). All of those predate this package's build (c92a320): the frame at candidate L1–3 already has no `theme=` parameter, section 3 records the sub-shape, and no frame byte postdates the build.

**FIX-RFIX89 — escaped footnoteblock unescaped (landing 6660ec5).** `FIX-RFIX89.md` item 1 (BATCH-RFIX8 flag): as built, candidate L245 read `@@[[footnoteblock]]@@` (escaped; renders as literal text) where the original (package `original.txt` L226) and production (`pages-existing/existing:theme-penumbra.txt` L231) carry `[[footnoteblock]]` live, standalone in identical context. The candidate's footnote at L89 is live, so the escaped block had no render position and the literal string displayed instead. Commit 6660ec5 unescaped L245 to `[[footnoteblock]]`, one line, matching both sources. The checker finding set is unchanged (error 2 / warn 1 / info 2 before and after, the identical set: http×2 class (ii), interwiki-touched warn, double-rate and important info; class (i) 0 throughout). The recopied candidate now carries the footnoteblock live, so the "open defect" recorded in section 11 and verification item (4) in section 12 describe the as-built candidate and are closed by this repair.

## 12. Verification

The stamp is STALE by design (computed against canonical 20ce2906; the candidate changed after, per-theme record). Checks a reviewer can re-run from this package alone: (1) the sha256 of original.txt equals the sources.tsv row for theme:penumbra-jp, and candidate.txt is byte-identical to pages/theme:penumbra-jp.txt. (2) The item 4 re-derivation: grep the candidate for the Noto Sans JP import (line 280) and its stack occurrences (lines 285, 351, 460, 845, 849, 856, 865, 871). (3) The code-block census over every form returns zero in the candidate. (4) The footnoteblock three-way comparison: original line 226 live, production line 231 live, candidate line 245 escaped (as built; after FIX-RFIX89/6660ec5 the candidate's L245 is live — see Post-package repairs (REFRESH3-E)). (5) Brace depth over the delivered CSS returns to 0 on both sides. No re-render was run for this package.

## Appendix — residue blocks

- R1, B16 (residue; original 42 to candidate 56-59): the darkbox sample region, restructured with its sample text translated (section 6).
- R2, B60 (residue; original 166 to candidate 184): the collapsible show/hide pair, "Example" to its JP form (section 6).
- R3, B67 (residue; original 226-227 to candidate 245): the footnoteblock; not resolved as an exhibit, flagged as a defect in section 11.
- R4-R12, B80, B112, B115, B123, B124, B143, B193, B203, B206 (residue): single-region pairs inside the delivered CSS and its tail, all production drift under the one shape of section 8; the original-side-only entries (B123, B124, B143, B203, B206) are code-channel lines absorbed by the drift restructure, and none carries body content.
- R13-R59, B6, B8, B9, B10, B12, B14, B15, B17, B18, B23, B26, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43, B44, B45, B46, B47, B48, B50, B51, B52, B53, B55, B56, B57, B58, B59, B61, B62, B63, B64, B66, B68 (heuristic, TRANS-UNANCHORED): one-to-one prose translations against the mirror (section 6).
- R60, B70 (heuristic): the Source Code exhibit boundary, resolved in section 8.
- R61-R189, B74, B75, B76, B77, B78, B79, B81, B82, B83, B84, B85, B86, B87, B88, B89, B90, B91, B92, B93, B94, B95, B96, B97, B98, B99, B100, B101, B102, B103, B104, B105, B106, B107, B108, B109, B110, B111, B113, B114, B116, B117, B118, B119, B120, B121, B122, B125, B126, B127, B128, B129, B130, B131, B132, B133, B134, B135, B136, B137, B138, B139, B140, B141, B142, B144, B145, B146, B147, B148, B149, B150, B151, B152, B153, B154, B155, B156, B157, B158, B159, B160, B161, B162, B163, B164, B165, B166, B167, B168, B169, B170, B171, B172, B173, B174, B175, B176, B177, B178, B179, B180, B181, B182, B183, B184, B185, B186, B187, B188, B189, B190, B191, B192, B194, B195, B196, B197, B198, B199, B200, B201, B202, B204, B205, B207, B208, B209, B210, B211 (heuristic, code-css channel): production-drift CSS pairs, the one shape of section 8; the channel change (code-css to body) is the delivery move of section 3, not content loss.
