# Review package — theme:rima-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:rima-jp — origin CN, population #221 [GOSIGN2-LEDGER (b) row 221]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now b2d09d842ee0870b4205380e1935222561f4e8c50d2fe9e80836d99f4b75f8e0); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 19 errors / 3 warns / 2 infos (hotlink×15, foreign-include×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 246; GOSIGN2-LEDGER (b) row 221]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 325px@320 + sidebar-unreachable (4 combos) + candidate-own runtime hosts (cdn.mer.run, oxygennine.wdfiles.com / oxygennine.wikidot.com, scpsandboxcn chain) recorded verbatim; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN12))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 220, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 220]
- FIX5 re-judgement: items 73 (class A) FIXED, 74 (class F) DISPOSITIONED — FIX5-FUNC §9, commit 59130a2: component:excerpts-tool-jp ported from semimonth rev 9 with TASL (ruling 4); three includes repointed; checker foreign-include errors 19 -> 16, the three targeted errors gone FIX5-FUNC §9 (no edit): hover-reveal sidebar block candidate L1181-1250 byte-identical to original L1162-1231 (diff IDENTICAL); neither version carries a .open-menu a; the machine line reflects the original design; spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) items 73–74; (c) check 6]
- Computed against: canonical commit b1e1fe95acabd16c1f83a1387c750c2bf8ba433e; candidate file pages/theme:rima-jp.txt sha256:b2d09d842ee0870b4205380e1935222561f4e8c50d2fe9e80836d99f4b75f8e0; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete - explanation written by lane R-disp-10, 2026-11-17; all skeleton markers resolved
Candidate: review/rima-jp/candidate.txt (sha256 1f56e1f3168fb94999af6738659d830850d107a3ae5330bf00b6d704104d3df8)
Original: theme:rima — scp-wiki-cn, revision 10 (sha256 57f8d90fb7a81ad607f1ec5c9adcc889b0b0b875765bd97737c1a6603d1c825d)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

Complete (lane R-disp-10, 2026-11-17). Item 73 [A] was FIXED by FIX5 (commit 59130a2) and the fix is re-verified from this package's bytes in the Per-theme record. Item 74 [F] is DISPOSITIONED and its ground re-derives exactly. Two defect flags are recorded (a duplicate bare Rate at candidate L27-29, and a duplicated side-menu block at candidate L1337-1339); the candidate is not edited by this lane. One sources.tsv note correction is supplied in the Per-theme record for the coordinator's harvest.

## Provenance

| | |
|---|---|
| Original | theme:rima, scp-wiki-cn (CN), revision 10 |
| Original file | original.txt, 1,316 lines / 43,679 bytes, SHA-256 57f8d90fb7a81ad607f1ec5c9adcc889b0b0b875765bd97737c1a6603d1c825d (matches review/sources.tsv) |
| Mirror source | campaign mirror store file orig-rima-rev10.txt, from gosign2-lanes/lane-oc-gs-localize-s2-E/orig-rima.txt, fetched 2026-11-16 |
| Candidate | theme:rima-jp, pages/theme:rima-jp.txt |
| Candidate file | candidate.txt, 1,338 lines / 47,237 bytes, SHA-256 1f56e1f3168fb94999af6738659d830850d107a3ae5330bf00b6d704104d3df8 (byte-identical to canonical) |
| Kind | K5b-4: the candidate ships a companion file in-repo, pages/component:excerpts-tool-jp.txt, created by the FIX5 wave under ruling 4 (section 2) |
| Route | Derived from the original at the reference revision (first translation, Stage 2 lane CN12, LOCALIZE-S2-E) |
| Wave history | 72e3efa (Stage 2 CN12 integrate), b89741d (rework2-p5), 1869877 (FIX-CREDIT-D), 8c62b7b (FIX4-IWA: interwiki frame), 59130a2 (FIX5-FUNC: item 73 fix; the stamp's computed-against commit) |
| Change set | diff.md (Tier 2): +132 / -110 lines, 242 changed; 89 classifier blocks (40 specific, 44 heuristic, 5 residue) |

## Summary

Rima is the CN Semimonth magazine's theme, built on the Peroxide base. The port swaps the original's ThemePreviewer base delivery for the peroxide-jp candidate include, adds a credit block the original does not carry, translates the prose and specimen text (keeping the masthead specimen's CN text as a standing item), converts retained CN strings to Japanese glyph forms, loads the author's own identified typeface (Afacad Flux) from Google Fonts in place of its CN font-API delivery, and repoints the three live foreign includes to the newly ported component:excerpts-tool-jp (item 73, FIXED). Item 74 (sidebar unreachable on mobile) is dispositioned on a byte-identical hover-reveal block. Two defects are flagged: the original's bare Rate survives beside the rate-bearing credit block, and a side-menu block is duplicated at the tail.

## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| COLON-ENC | 1 |
| COMMENT-TEXT | 2 |
| COMPONENT-SWAP | 3 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 2 |
| CREDIT-PROSE | 2 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 4 |
| FONT-IMPORT | 1 |
| GLYPH-FORM | 5 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 3 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 48 |
| TRANSLATION-ANCHORED | 29 |

Counts: 89 blocks, 40 specific, 44 heuristic, 5 residue, 0 skipped (comment text).

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

- Provenance route: derived from the original at revision 10 (first translation). The mirror's SHA-256 equals the sources.tsv row; the T4 follow-up (section 12) confirms revision 10 is still the original's current revision, so the mirror is also the current original. The sources.tsv note's supersession claim is wrong on its own cited artifact; the correction is in the Per-theme record.
- Structure census: exactly one [[code type="CSS"]] block on each side (original L421-1100, candidate L440-1119; 680 lines each), self-delivered as /1, plus two iftags-gated tail [[module CSS]] blocks on each side. The selector census is equal (102 on each side) with the sole difference :root:lang(cn) to :root:lang(ja). Code-block declaration differences are confined to six items, enumerated in sections 4 and 5. A naive brace counter ends at depth 6 on both sides (the file's strings contain braces); the structure claims here rest on the selector and declaration censuses, not on that counter.

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B3: orig 29-29 -> cand 34-42 (body -> body)
  - B4: orig 31-31 -> cand 44-45 (body -> body)

**What (this theme):** the original carries no credit block; the candidate adds the population's credit:start-preview block (B3, B4; candidate L34-45) with all 8 TASL fields. The author field names [[*user OxygenNine]], the original's author; the creation year reads 2026, the year of the original's own demo issue (dated May 2026 in its specimen text), and the localize lane verified all of its section-3 items present. The block also carries the porter's font note (candidate L44), adjudicated in section 10.
**Defect flag 1:** the candidate keeps the original's bare [[module rate]] at candidate L27-29 (original L22-24, inside its alignment wrapper) beside the rate-bearing credit block, so the page carries two rate widgets. The localize lane judged this exact shape missed (LOCALIZE-S2-E CN12-5 pattern 3), and its batch recommendation 3 names rima for consolidation into the credit module; that recommendation was never executed and never charged in the ledger. The population's rates census removes exactly this shape (the shoebill adjudication; five removals in 1c96ee4), and rima matches none of the keeper exceptions (not a specimen, not a production adoption, and its credit form is the preview form). This lane's checker run independently emits info double-rate at candidate L28. Remedy for the fix queue: remove candidate L27-29 in the shoebill form. The candidate is not edited by this lane.
**Why:** the preview credit module is the rate-bearing form in this environment (P3); a second bare Rate double-renders the widget (KB-09).
**Verify:** grep candidate.txt for [[module; read candidate L27-45 against original L22-31.
**Disposition:** the credit block itself is the standard form; the flag is the leftover Rate, not the block.

## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B88: orig 1243-1243 -> cand 1261-1261 (body -> body)

**What (this theme):** B56-B58 are the item 73 fix: the three live includes of :semimonth:component:excerpts-tool (original L298, L304, L309) now read component:excerpts-tool-jp (candidate L316, L322, L327), with include parameters byte-identical (the CN article titles and text stand as quotations, per FIX5-FUNC's closing note). The companion page pages/component:excerpts-tool-jp.txt exists in the canonical repo (2,979 bytes), ported from semimonth revision 9 with its TASL record (author Etinjat, CC BY-SA 3.0), under ruling 4 (a needed component ports together with its theme). The base delivery swap (residue B1) is adjudicated in the appendix and section 3: the original's ThemePreviewer module (original L1, serving peroxide.css from oxygennine.github.io) is replaced by [[include theme:peroxide-jp]] (candidate L1), and its iftags gate localizes to the JP theme tag. B88 localizes the second tail gate the same way.
**Why:** a live foreign include with no JP counterpart is a posting blocker (the item 73 ground); ruling 4 ports the component rather than parking the theme.
**Verify:** grep candidate.txt for :semimonth: (none remains) and for excerpts-tool-jp (three includes); read the companion file's TASL block.
**Disposition:** item 73 [A] FIXED (FIX5-FUNC section 9, commit 59130a2); the fix is re-verified in the Per-theme record.

## 3. Delivery and code loading

- SELF-DELIVERY (A): Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel.
  Verify: The named delivery resolves on the draft host and serves the current candidate body.
  - B2: orig 13-13 -> cand 13-18 (body -> body)

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B85: orig 1148-1148 -> cand 1167-1167 (module-css -> module-css)

**What (this theme):** B2 is the FIX4-IWA interwiki frame at candidate L13-16 (priority=1), added by 8c62b7b, closing the localize lane's pattern 6. B85 is the tail module's self-delivery @import (original L1148 to candidate L1167): repointed from the CN page's own /code/1 to the draft-host form of the candidate's /1, with the colon percent-encoded (theme%3Arima-jp, the KB-01 form); it is the checker's pseudo-ref line, a standing class. The base is delivered by include (candidate L1), not inlined; the theme's own CSS is delivered by the single code block as /1, and the tail module imports that same /1.
**Why:** delivery must resolve inside the JP environment (P4); addresses must name the candidate's own page.
**Verify:** read candidate L1, L13-16, L1163-1167 against original L1, L12-13, L1146-1148.
**Disposition:** no delivery slot is emptied and no mechanism is dropped; the two gated tail modules stand on both sides with localized gates (sections 2 and 8).

## 4. Fonts and assets

- FONT-IMPORT (B): Other font-load change (P5, KB-04): malformed family parameters (a hyphen for a +) make the load fail.
  Verify: KB-04: the family parameter form; the deciding evidence is the load probe (400 vs 200).
  - B78: orig 424-424 -> cand 443-443 (code-css -> code-css)

- COLON-ENC (A): Unencoded colon encoded (KB-01): a raw colon in a URL path segment breaks the local--code / local--files address.
  Verify: KB-01 recipe: the pair differs only by the %3A encoding.
  - B80: orig 464-464 -> cand 483-483 (code-css -> code-css)

**What (this theme):** B78 replaces the original's ZSFT-fa @font-face (original L424, fontsapi.zeoseven.com) with a Google Fonts @import of Afacad Flux (candidate L443), inside the delivered code block. The substitution is the author's own identification: the original's @font-face carries the CN author's comment naming the face as Afacad Flux, so the candidate loads the same typeface from the JP environment's font host instead of the CN font API. B79 carries the matching stack rewrite (section 5's block): --rima-ui-font (candidate L474) reads 'Afacad Flux', 'Noto Sans JP', sans-serif, against the original's 'ZSFT-fa', 'Sarasa Gothic SC', 'Noto Sans SC', sans-serif; this is a P7 font-stack rewrite, narrated here although the classifier labels the block CONTENT-STRING. Noto Sans JP is not loaded by this file; it is loaded by the base delivery chain (pages/fragment:peroxide-jp-base-css.txt L15 imports Noto Sans JP and Noto Serif JP from Google Fonts, and the base's sans-serif variable names Noto Sans JP first), which the localize lane fetch-verified (LOCALIZE-S2-E pattern 7). Font Awesome 4.3.0 (cdnjs) is kept byte-identical. B80 encodes the colon in a system%3Afiles URL (candidate L483, KB-01); host and files are unchanged.
**Why:** a font named in a stack must be loaded somewhere in the delivery chain; here every named family is (Afacad Flux by this file, Noto Sans JP by the base), no load is duplicated across the chain, and no load sits in an inert channel.
**Verify:** read candidate L443 and L474 against original L424 and the original's stack in the same :root block; read the base fragment's L15.
**Disposition:** the (c3) P5 host class covers the kept third-party hosts (section 11); the font substitution itself is documented above, not dispositioned.

## 5. Header, sidebar, site furniture

**What (this theme):** the skeleton prints none for this section because the header changes ride inside multi-label blocks; from the label spans: B79 (CONTENT-STRING, original L450-455 to candidate L469-474) changes the three header content variables: --p-header-title-content takes the glyph-converted form of the magazine's name, --p-header-slogan-content translates the slogan phrase, and --rima-header-label translates the theme-label string; the same block carries the --rima-ui-font stack rewrite (section 4). B86 (CSS-BODY, original L1149-1150 to candidate L1168-1169) is the tail module's :root:lang(cn) to :root:lang(ja) selector change; its --rima-header-label value ('{$label}') is unchanged. The sidebar surface itself produced no change block at all: the hover-reveal block is byte-identical, which is item 74's ground (Per-theme record).
**Why:** header content strings are reader-visible text (KB-18's reader-visible half); a slogan that is a prose phrase translates, while the masthead specimen's CN text is a separate standing item (section 6).
**Verify:** read candidate L469-474 and L1168-1169 against original L450-455 and L1149-1150.
**Disposition:** item 74's disposition covers the sidebar mechanism; the header strings are ordinary localization.

## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B5: orig 33-33 -> cand 47-47 (body -> body)
  - B6: orig 35-35 -> cand 49-49 (body -> body)
  - B7: orig 37-40 -> cand 51-51 (body -> body)
  - B8: orig 42-42 -> cand 53-53 (body -> body)
  - B9: orig 44-44 -> cand 55-62 (body -> body)
  - B12: orig 74-74 -> cand 92-92 (body -> body)
  - B13: orig 81-81 -> cand 99-99 (body -> body)
  - B14: orig 94-94 -> cand 112-112 (body -> body)
  - B16: orig 99-99 -> cand 117-117 (body -> body)
  - B17: orig 101-101 -> cand 119-119 (body -> body)
  - B18: orig 115-115 -> cand 133-133 (body -> body)
  - B19: orig 127-127 -> cand 145-145 (body -> body)
  - B21: orig 134-134 -> cand 152-152 (body -> body)
  - B22: orig 140-141 -> cand 158-159 (body -> body)
  - B23: orig 145-145 -> cand 163-163 (body -> body)
  - B26: orig 160-160 -> cand 178-178 (body -> body)
  - B29: orig 190-191 -> cand 208-209 (body -> body)
  - B30: orig 199-200 -> cand 217-218 (body -> body)
  - B34: orig 223-223 -> cand 241-241 (body -> body)
  - B38: orig 236-236 -> cand 254-254 (body -> body)
  - B40: orig 248-248 -> cand 266-266 (body -> body)
  - B41: orig 250-251 -> cand 268-269 (body -> body)
  - B42: orig 254-254 -> cand 272-272 (body -> body)
  - B43: orig 256-256 -> cand 274-274 (body -> body)
  - B44: orig 261-261 -> cand 279-279 (body -> body)
  - B45: orig 263-264 -> cand 281-282 (body -> body)
  - B46: orig 267-267 -> cand 285-285 (body -> body)
  - B47: orig 269-269 -> cand 287-287 (body -> body)
  - B50: orig 282-282 -> cand 300-300 (body -> body)
  - B51: orig 284-284 -> cand 302-302 (body -> body)
  - B52: orig 286-286 -> cand 304-304 (body -> body)
  - B53: orig 288-288 -> cand 306-306 (body -> body)
  - B61: orig 324-324 -> cand 338-344 (body -> body)
  - B64: orig 340-340 -> cand 360-360 (body -> body)
  - B65: orig 345-345 -> cand 365-365 (body -> body)
  - B66: orig 353-354 -> cand 373-373 (body -> body)
  - B68: orig 367-367 -> cand 386-386 (body -> body)
  - B69: orig 369-369 -> cand 388-388 (body -> body)
  - B71: orig 385-385 -> cand 404-404 (body -> body)
  - B72: orig 390-390 -> cand 409-409 (body -> body)
  - B73: orig 395-395 -> cand 414-414 (body -> body)
  - B74: orig 400-400 -> cand 419-419 (body -> body)
  - B81: orig 688-688 -> cand 707-707 (code-css -> code-css)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B10: orig 68-68 -> cand 86-86 (body -> body)
  - B11: orig 72-72 -> cand 90-90 (body -> body)
  - B15: orig 97-97 -> cand 115-115 (body -> body)
  - B20: orig 132-132 -> cand 150-150 (body -> body)
  - B24: orig 152-152 -> cand 170-170 (body -> body)
  - B25: orig 157-158 -> cand 175-176 (body -> body)
  - B27: orig 166-168 -> cand 184-186 (body -> body)
  - B28: orig 176-177 -> cand 194-195 (body -> body)
  - B31: orig 212-212 -> cand 230-230 (body -> body)
  - B32: orig 217-217 -> cand 235-235 (body -> body)
  - B33: orig 219-219 -> cand 237-237 (body -> body)
  - B35: orig 225-225 -> cand 243-243 (body -> body)
  - B36: orig 230-230 -> cand 248-248 (body -> body)
  - B37: orig 232-232 -> cand 250-250 (body -> body)
  - B39: orig 238-238 -> cand 256-256 (body -> body)
  - B48: orig 276-276 -> cand 294-294 (body -> body)
  - B49: orig 280-280 -> cand 298-298 (body -> body)
  - B54: orig 292-292 -> cand 310-310 (body -> body)
  - B55: orig 295-295 -> cand 313-313 (body -> body)
  - B60: orig 322-322 -> cand 336-336 (body -> body)
  - B62: orig 330-330 -> cand 350-350 (body -> body)
  - B63: orig 334-334 -> cand 354-354 (body -> body)
  - B67: orig 363-363 -> cand 382-382 (body -> body)
  - B70: orig 379-379 -> cand 398-398 (body -> body)
  - B76: orig 418-418 -> cand 437-437 (body -> body)
  - B77: orig 420-420 -> cand 439-439 (body -> body)
  - B82: orig 936-936 -> cand 955-955 (code-css -> code-css)

- GLYPH-FORM (B): Shinjitai conversion (R5): retained source-language strings converted to Japanese glyph forms; neither translated nor left untouched, and the reviewer must see it separately.
  Verify: Fold-compare the pair; only glyph forms differ.
  - B75: orig 409-410 -> cand 428-429 (body -> body)

- CONTENT-STRING (B): Visible string in CSS (KB-18, R1 reader-visible half): content: strings and string-valued variables render for readers.
  Verify: The string renders in the sample page's DOM text.
  - B79: orig 451-455 -> cand 470-474 (code-css -> code-css)

**What (this theme):** the body translates at scale: 29 TRANSLATION-ANCHORED blocks and the TRANS-UNANCHORED mass (appendix) cover the parameter guide, the specimen articles, and the usage notes; 5 GLYPH-FORM blocks (B35, B37, B39, B48, B75) are shinjitai conversions of retained CN strings (R5), neither translated nor left untouched; 2 COMMENT-TEXT blocks (B81, B82) are CSS comment translations inside the code block. Standing items, kept at their recorded weight: the rima-title masthead specimen keeps its CN text byte-identical (candidate L64-72), which the localize lane flagged as a staff-judgement item and the joint T5 findings left standing; the excerpts' CN titles and text are quotations under the FIX5 note (section 2); the BREAKING and SCP SEMIMONTH content strings are in-universe brand strings kept per the original (LOCALIZE-S2-E pattern 9, note only); the placeholder article title stands in the glyph-converted form the lane recorded.
**Why:** reader-visible text localizes (P10, KB-18); retained source-language strings convert glyph forms separately so a reviewer can see the choice (R5).
**Verify:** read the pairs in diff.md; the appendix assigns every heuristic block.
**Disposition:** the localize lane's T5 findings stand as recorded in the stamp.

## 7. Links

**What (this theme):** no link repoint fired. The prose links: the welcome paragraph (candidate L47) absolutizes the Semimonth hub link to the CN original (the hub the theme was made for) and links the base as plain theme:peroxide-jp, the campaign's own base candidate; the checker warns link-target-missing at L47 because the base is not a production JP page, which is the posting-order class, not a dead reference. The demo text's scp-xxxx placeholder (candidate L237) is the original's own placeholder article name; the checker's second warn sits there and is benign specimen text. The usage exhibit (candidate L49) uses the :scp-jp:-prefixed include form with its label updated from the original's 2025.5 to 2026.5, an observation recorded here; the head delivery include (candidate L1) uses the campaign's bare form.
**Verify:** read candidate L47-49 and L237; re-run the checker (section 12).
**Disposition:** no link in the file names a page that will not exist once the campaign posts; the L47 warn is a posting-order artifact.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B56: orig 298-298 -> cand 316-316 (body -> body)
  - B57: orig 304-304 -> cand 322-322 (body -> body)
  - B58: orig 309-309 -> cand 327-327 (body -> body)
  - B59: orig 314-318 -> cand 332-332 (body -> body)

- CSS-BODY (C): Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.
  Verify: Writer review; a recurring shape is a new-signature candidate for the patterns loop.
  - B86: orig 1150-1150 -> cand 1169-1169 (module-css -> module-css)

**What (this theme):** the classifier files B56-B59 as EXHIBIT-RESTRUCTURE. Against the bytes: B56-B58 are the item 73 include repoints inside the excerpts exhibit region (section 2), and B59 is the FIX5 reader's-note replacement at candidate L332 (the ANNOTATION block, section 10). No exhibit was dropped or replaced: the excerpts exhibits stand with their CN quotation text and byte-identical include parameters. The tail structure is preserved: two iftags-gated [[module CSS]] blocks on each side, their gates localized (B88), with the gate-close seams filed as residue (appendix). One structural defect stands at the tail and is flagged here.
**Defect flag 2:** the candidate carries two [[div class="side-menu"]] [[toc]] [[/div]] blocks (candidate L1333-1335 and L1337-1339) where the original carries one (original L1315-1317); the census is 2 against 1. The localize lane recorded the duplication as port-introduced (LOCALIZE-S2-E pattern 2 and the CN12 supplement note: this file alone gained a small duplicated block); it was never dispositioned or fixed, and residue block B89 sits exactly on the second copy. Remedy for the fix queue: delete the second block (candidate L1337-1339). The candidate is not edited by this lane.
**Why:** a duplicated table-of-contents block renders the side menu twice. Unlike the tail gated modules' toggle-CSS duplication, which the original itself carries on both sides and is therefore inherited, this duplication exists only in the candidate.
**Verify:** grep both files for side-menu; count 1 against 2.
**Disposition:** exhibit decision below.


Exhibit decision: replaced, none; dropped, none. B56-B59 are an include repoint and a reader's-note replacement misread as exhibit changes. The bare Rate at candidate L27-29 stands in the head furniture, not beside an exhibit label; its kept-vs-removed reasoning is defect flag 1 (section 1): it should have been removed, and the flag says so.

## 9. Formatting only

- WS-ONLY blocks: 0
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

Two porter annotations ride inside other labeled blocks. (1) The credit block's font note (candidate L44, inside B4): it states the font programme the port uses; checked against the delivery chain, it is accurate (Afacad Flux loaded by this file, Noto Sans JP by the base chain, section 4). (2) The FIX5 reader's note (candidate L332, B59, the classifier's ANNOTATION block): it tells readers the excerpts tool is the JP port; checked against the bytes, the three includes do read component:excerpts-tool-jp (section 2). No annotation in this file states something the bytes refute.

## 11. Dispositions and exceptions

- Item 73 [A] FIXED (FIX5-FUNC section 9, commit 59130a2): not a disposition; the fix is re-verified in the Per-theme record.
- Item 74 [F] DISPOSITIONED (FIX5-FUNC section 9, no edit): the sidebar-unreachable machine line reflects the original's hover-reveal design; the block is byte-identical. Re-derived in the Per-theme record: the ground holds exactly.
- (c3) LOCALIZE-S2-E P5 DISPOSITIONED, class (ii) / KB-58: the 15 hotlink lines name third-party hosts the original itself uses, and the port changes none of them. Byte ground: the host census is identical on both sides (scpsandboxcn 9, cdn.mer.run 3, oxygennine.wikidot.com 3, x.com 4).
- The (c2) render bundle's other two elements, at exactly their recorded weight: the candidate-own runtime hosts are the same byte-identical census under the P5 / KB-58 disposition above; the 325px-at-320 overflow's operative CSS surface is the same byte-identical code block (section 0 census). The supplement contains no separate re-judgement of the overflow, and none is claimed here.
- T1 standing classes: the pseudo-ref at candidate L1167 (draft-host self-delivery, register (c1)) and the hotlink class above.

## 12. Verification

- T1 checker (canonical invocation, run by this lane 2026-11-17): exit 1, 16 errors / 2 warns / 2 infos. Errors: hotlink x15 (scpsandboxcn x9, cdn.mer.run x3, oxygennine x3; candidate L483 among the oxygennine lines) and pseudo-ref x1 (candidate L1167). Warns: link-target-missing at L47 (the unposted base, section 7) and L237 (the scp-xxxx placeholder). Infos: double-rate at L28 (defect flag 1) and important at L483. Zero foreign-include errors remain: the count is exactly the FIX5 after-state (19 to 16, the three targeted errors gone).
- Baseline discrepancy: T1-ROWS row 246 records the baseline as 19 errors / 3 warns / 2 infos; FIX5-FUNC section 9's own before-run records 19 / 2 / 2. The error counts agree; the warn count differs between the two records and is recorded here rather than resolved (Per-theme record).
- T2/T3 render: not re-run by this lane; the record stands as cited in the stamp. Item 74 is re-derived from bytes (Per-theme record).
- T4 follow-up: diff-rima-from10.txt records revision 10 to revision 10, no change; original.txt is both the reference mirror and the current original.
- Package checks: candidate.txt is byte-identical to pages/theme:rima-jp.txt; original.txt's SHA-256 equals the sources.tsv row; python3 review/build_review.py --check passes for this package (the lane report carries the stale-set comparison).

## Per-theme record - FIX5 items re-derived

### Item 73 [A] - FIXED (FIX5-FUNC section 9, commit 59130a2)

The blocking item: the candidate's live includes named :semimonth:component:excerpts-tool three times, a CN site component with no JP counterpart, a stated live posting blocker (GOSIGN2-LEDGER (b) item 73). The fix ported the component as component:excerpts-tool-jp from semimonth revision 9 with its TASL record (ruling 4) and repointed the three includes.

Re-verification from this package's bytes. The three includes read [[include component:excerpts-tool-jp at candidate L316, L322, L327 (the ledger's L311/317/322 were the pre-fix candidate's line numbers). Their include parameters are byte-identical to the original's (original L298, L304, L309); the CN article titles and text stand as quotations, as FIX5-FUNC's closing note records. No :semimonth:component string remains anywhere in candidate.txt. The companion page exists at pages/component:excerpts-tool-jp.txt (2,979 bytes) with its TASL block (author Etinjat, CC BY-SA 3.0). The FIX5 reader's note stands at candidate L332. This lane's checker run reports zero foreign-include errors (section 12). The fix is complete on the bytes.

### Item 74 [F] - DISPOSITIONED (FIX5-FUNC section 9, no edit)

The blocking item: the render harness reported the sidebar unreachable on all four mobile combinations (GOSIGN2-LEDGER (b) item 74, in the (c2) render bundle). The FIX5 ground: the sidebar mechanism is the original's hover-reveal design, unchanged by the port; the machine line reflects that design.

Re-derivation from this package's bytes. The hover-reveal block (the toggle-sidebar region) at candidate L1181-1250 against original L1162-1231 is byte-identical: 1,834 bytes, SHA-256 03d69e80c59a5279cddcbdae40649a43640c5dd6aafe8f67a6fe4b1e9d691153 on both sides. Neither file contains a .open-menu rule anywhere (census 0 on both sides), so there is no tap-target control for a mobile harness to reach on either side; the original's design reveals the sidebar on hover. Widening past the block: the whole code block's declaration differences are the six items in section 0, none of which touches the sidebar surface.

Second-reviewer walk. The ground is checkable from this package alone: extract the two windows and compare hashes. The render half (the harness's four-combination line) rests on the RENDER-S2-F record cited in the stamp; the disposition's claim is only that the mechanism is the original's own, and the bytes decide that claim exactly. A fix would have to add a control the original does not have, departing from the original's design. The disposition stands.

### Defect flags (candidate not edited by this lane)

- F1: duplicate bare Rate, candidate L27-29 beside the rate-bearing credit block (section 1). Remedy: remove L27-29 in the shoebill form.
- F2: duplicated side-menu block, candidate L1337-1339 duplicating L1333-1335 (section 8). Remedy: delete the second block.

### Record discrepancies and the sources.tsv note correction

- T1 warn count: T1-ROWS row 246 (and the stamp) record the baseline as 19 errors / 3 warns / 2 infos; FIX5-FUNC section 9's own before-run records 19 / 2 / 2. Error and info counts agree everywhere; the warn count differs between records. Recorded, not resolved.
- The ledger's line numbers for item 73's includes (L311/317/322) are the pre-fix candidate's; the fixed includes stand at candidate L316/322/327. No discrepancy of substance.
- Sources.tsv note correction (for the coordinator's harvest): the rima row's note claims the original was "superseded upstream since the reference revision". Its own cited artifact (diff-rima-from10.txt) records scp-wiki-cn theme:rima revision 10 to revision 10, no changes. The correct form: "Upstream latest remains rev 10; the K5a-i artifact records rev10 to rev10, no changes; follow-up diff artifact diff-rima-from10.txt in the campaign record (K5a-i)". The companion-file clause of the note is correct and stands.

### Repairs landed after this package was built

- F1 and F2 repaired by FIX-RDISP10 (record R/review-scout/FIX-RDISP10.md), landed in commit b1e1fe9: the bare [[module rate]] block (old candidate L27-29) is removed in the shoebill form, so the credit:start-preview block is the sole rate-bearing form and the checker's double-rate info is resolved; the duplicated tail side-menu block (old candidate L1337-1339) is deleted, the standalone-block census is now 1, equal to the original, and the file ends with a trailing newline. Checker after-state: 16 errors / 2 warns / 1 info, the same finding multiset as before at shifted line numbers, no new finding of any class. candidate.txt is recopied from the repaired candidate in this refresh; the regenerated stamp reads STALE, no re-judgement is fabricated, and the frozen ledger remains the verdict record.

## Appendix - residue and heuristic blocks

The 5 residue blocks are four seams and one defect; the 44 heuristic blocks are translation mass. Each is assigned here.

Residue:

- B1 (original L1 to candidate L1): the base delivery swap, the original's ThemePreviewer module replaced by [[include theme:peroxide-jp]]. The signature could not see a module-to-include swap. Assigned to sections 2 and 3.
- B83 and B84 (candidate L1122-1123; original L1144-1145): the first tail gate's [[/iftags]] close, split into an added and a removed line by the classifier's alignment. On the bytes, the close tag separates the two tail [[module CSS]] blocks on both sides; its line position shifted with the +19-line growth above it. No structural change. Assigned to section 8.
- B87 (original L1240 to candidate L1259): the second tail module's gate-close seam, the same +19-line shift. Assigned to section 8.
- B89 (original L1318 to candidate L1336-1339): the duplicated side-menu block. This residue is defect flag 2 (section 8), not translation mass, and is not narrated away here.

Heuristic (44 blocks, TRANS-UNANCHORED tier C unless noted):

- B5-B9, B12-B14, B16-B19, B21-B23, B26, B29, B30, B34, B38, B40-B47, B50-B53, B61, B64-B66, B68, B69, B71-B74 (original L32-400 to candidate L46-419, body): one-line and short-group prose and specimen translations whose line shape changed in translation (script delta without the anchor majority). Assigned to section 6.
- B81, B82 (original L687-688 and L935-936 to candidate L706-707 and L954-955, code-css): CSS comment translations inside the code block, also labeled COMMENT-TEXT. Assigned to section 6.
- B4, B59, B75 are tier A/B seams rather than appendix mass: the credit block's tail (section 1; its annotation in section 10), the FIX5 reader's note (sections 8 and 10), and a glyph-form conversion (section 6).
