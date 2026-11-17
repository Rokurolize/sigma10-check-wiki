# Review package — theme:sodium-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:sodium-jp — origin CN, population #228 [GOSIGN2-LEDGER (b) row 228]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged DISPOSITIONED with grounds by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 9 errors / 3 warns / 0 infos (pseudo-ref×9); standing classes dispositioned in register c1 [T1-ROWS row 259; GOSIGN2-LEDGER (b) row 228]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-login (desktop, both engines) on page and sample + runtime-hotlink site-theme chain; sample credit-modal (preview-form); T3 login-state absence confirmed, rating clear-vote × near-white on white effectively invisible; full-engine coverage. [RENDER-ROWS-G (CN14)]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN14)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 227, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 227]
- FIX5 re-judgement: item 83 (class E) DISPOSITIONED — FIX5-CONTRA (no edit, no commit): charged colour rgb(255,246,240) exists nowhere in the candidate or its base fragment; traced to the shared preview credit module's rendering (KB-32 class); the theme's own rate colours are byte-identical to the CN original [GOSIGN2-LEDGER-SUPPLEMENT (a) item 83]
- Computed against: canonical commit 666f54356acb463c56016c967dc52464b25ba4a2; candidate file pages/theme:sodium-jp.txt sha256:e3fb9787960856916dbc6aa679482903aca244e2e6b67685779dec198658e742; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (R-disp-11 lane, 2026-11-17)
Candidate: review/sodium-jp/candidate.txt (sha256 e3fb9787960856916dbc6aa679482903aca244e2e6b67685779dec198658e742)
Original: theme:sodium — scp-wiki-cn, revision 37 (sha256 252d177c9e0e075192eb6387c8a1c60ac93a92810f871e6f527620bec710129e)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (generated stamp) | Notes |
|---|---|---|
| T1 source check | FINDINGS (classified) | Baseline 9 errors / 3 warns / 0 infos (pseudo-ref x9); this lane's run on the current file reproduces it exactly (section 12); the 3 warns are adjudicated there |
| T2/T3 render | FINDINGS | RENDER-S2-G (CN14), full-engine coverage: hidden-login and runtime-hotlink lines environment-layer (KB-40); sample credit-modal preview-form (KB-32); the clear-vote line was item 83, re-derived in the per-theme record |
| T4/T5 localize/translation | FINDINGS | LOCALIZE-ROWS row 227 (ledger (b) row 228): the headline item (credit concentration in the examples collapsible) is closed by the credit waves; P3 credit fields FIXED (register (c3)); the theme-name notation is a standing T5 item |
| FIX5 item 83 [E] | DISPOSITIONED | FIX5-CONTRA; re-derived on this package's bytes (colour census plus declaration-identity hash) in the per-theme record; the ground holds exactly |

## Provenance

| | |
|---|---|
| Original | theme:sodium, scp-wiki-cn, revision 37 (first-translation reference revision) |
| Mirror | review-mirrors/orig-sodium-rev37.txt, class COPY, sha256 252d177c9e0e075192eb6387c8a1c60ac93a92810f871e6f527620bec710129e (equals the sources.tsv value) |
| Candidate | pages/theme:sodium-jp.txt, sha256 e3fb9787960856916dbc6aa679482903aca244e2e6b67685779dec198658e742; companion delivery pages/fragment:sodium-jp-base-css.txt |
| Kind | K5b-4+K5b-5 (multi-part composition): the original's externally hosted stylesheet is ported as a companion fragment candidate, and the theme candidate delivers it by import |
| Production counterpart | none (no pages-existing/ entry for this theme) |

## Summary

The port moves Sodium (Ankv's CN theme, delivered upstream from an external GitHub Pages stylesheet) into the SCP-JP Sigma-10 environment by vendoring the stylesheet as fragment:sodium-jp-base-css and delivering it from the theme candidate. The diff is Tier 2 (1,986 changed lines over 104 blocks, counted by build_review.py), dominated by the 1,632-line delivery move into the companion fragment; the theme candidate itself is 464 lines of documentation, specimens, gated preset modules, and one T7 credit correction. The theme's one blocking item (83, class E) was dispositioned by FIX5-CONTRA; the per-theme record re-derives it (the charged colour exists in neither file, and the rate sections are declaration-identical) and confirms it. No defect flags. One sources.tsv note correction is reported in section 0 for the coordinator's harvest.

## 0. Header / provenance

- Delivery: code-css -> module-css (body similarity 0.65)
- Delivery: companion:fragment:sodium-jp-base-css.txt -> code-css (body similarity 0.71)
- Delivery: companion:fragment:sodium-jp-base-css.txt -> module-css (body similarity 0.65)

Provenance route: derived from the original at the reference revision, with a companion delivery. The candidate's credit block names first-translation reference revision 37; the mirror in this package is the campaign's frozen copy of scp-wiki-cn theme:sodium revision 37. The original's stylesheet is not part of the page source: it is served from https://3nkv.github.io/Sodium/sodium.min.css (original L2), and the campaign froze its content as the original's code block 1 (original L314-1945) inside the mirror; the ported form of that block is the companion candidate fragment:sodium-jp-base-css, classified alongside this pair (classify_hunks.py --companions). The port is not adopted from a production JP counterpart (none exists) and is not a JP original.

Sources-note correction (for the coordinator's harvest; this lane does not edit sources.tsv): the row's note claims the original was superseded upstream, but its cited artifact diff-sodium-from37.txt (130 bytes) records scp-wiki-cn:theme:sodium rev37 to rev37, no changes. Correct form, the ambrose shape: "Upstream latest remains rev 37; the S2 artifact records rev37 to rev37, no changes; follow-up diff artifact diff-sodium-from37.txt in the campaign record (K5a-i)".


## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 78 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 2 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DELIVERY-MOVE | 6 |
| DRAFT-HOST | 9 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| GLYPH-FORM | 2 |
| HEADERVAR | 3 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| RESTORATION | 1 |
| SELECTOR-CORRECTION | 2 |
| T7-CREDIT-CSS | 4 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 51 |
| TRANSLATION-ANCHORED | 38 |

Counts: 104 blocks, 55 specific, 43 heuristic, 6 residue, 0 skipped (comment text).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B3: orig 7-7 -> cand 12-21 (body -> body)
  - B7: orig 19-20 -> cand 33-36 (body -> body)

- T7-CREDIT-CSS (B): Credit-module CSS supplement (T7, KB-11/KB-12/KB-62): the JP credit module's DOM needs rules the branch original never shipped, or its inherited rules corrected in place.
  Verify: KB-11/KB-12 recipes: confirm the selectors in the candidate and whether the production counterpart carries them (supplement vs inherited).
  - B93: orig 321-1051 -> cand 313-316 (code-css -> code-css)
  - B94: orig 1062-1062 -> cand 327-327 (code-css -> code-css)
  - B95: orig 1067-1067 -> cand 332-332 (code-css -> code-css)

Why these instances are right: the original carried two rate surfaces, a head [[module rate]] inside a [[>]] div (orig L6-8) and a labelled specimen Rate in the examples zone (orig L19-20), plus two full credit-module demonstrations (orig L22-41: the start/more/end set and the standalone set). The JP environment's rate-bearing form is the single preview credit block; the candidate therefore carries exactly one credit block at the head (cand L11-21) and one preview pair inside the examples collapsible (cand L32-37) as the demonstration. The B8 deletion (orig L22-41) is that normalization, and it is the LOCALIZE-ROWS row 227 headline item, closed by the credit waves, not a silent exhibit drop: the collapsible and its other specimens stand. The TASL fields name Ankv as copyright holder with the design reference to EstrellaYoshte's Monotypical carried inside the field, exactly as the original's prose carries it (orig L9); the creation-year field 2026 is confirmed by the page's revision record (rev 0, 2026-04-22, by Ankv; wd_revisions.py list run by this lane), resolving the localize row's "source unconfirmed" note. The T7 supplement (B93/B94/B95/B104 spans) is the index instance of the R6 class: the theme's own rule styles .creditButton p a, but the JP credit component emits a direct-child a, so the same declarations are re-issued for .creditButton > a, both as a source exhibit (cand L310-336) and as the live tail module (cand L440-464), with the porter comment stating the ground. The supplement changes no value; it re-points the selector at the JP DOM.


## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B2: orig 5-5 -> cand 10-10 (body -> body)

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B5: orig 11-15 -> cand 25-29 (body -> body)

Why these instances are right, with one label corrected: the iftags gate localizes the CN theme tag to the JP theme tag (B2, KB-08). B5's COMPONENT-SWAP label does not survive the bytes: the block (orig L10-15 to cand L24-29) is the built-in-features prose and the install instruction, and the only include in it is the theme's own usage specimen, repointed from the CN form to theme:sodium-jp with its span stack's Noto Serif SC becoming JP. No component is swapped anywhere in this port (neither file includes a header component or any other component besides image-block and the credit set), so the label is recorded as a classifier mis-assignment and the block is adjudicated in sections 6 and 7 as prose translation plus a usage-example repoint. The image-block include (B10 span) keeps its component name; only the name= address is re-hosted to the candidate's own attachments (class (ii)).


## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B1: orig 1-2 -> cand 1-7 (module-css -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B65: orig 187-187 -> cand 183-183 (body -> body)
  - B68: orig 199-199 -> cand 195-195 (body -> body)
  - B72: orig 221-221 -> cand 217-217 (body -> body)
  - B75: orig 233-233 -> cand 229-229 (body -> body)
  - B77: orig 247-248 -> cand 243-244 (body -> body)
  - B99: orig 1961-1982 -> cand 352-373 (code-css -> code-css)
  - B102: orig 2001-2001 -> cand 392-392 (module-css -> module-css)

- DELIVERY-MOVE (B): Body relocated between deliveries (topology): where the CSS lives changed (code page to inline module CSS, exhibit to own fragment); the move itself is the change, and internal edits classify separately.
  Verify: Compare the moved body against its counterpart in the mirror or its companion delivery.
  - B92: orig 315-319 -> cand 311-311 (code-css -> code-css)
  - B96: orig 1070-1943 -> cand at 335 (code-css -> body)

Why this topology is right: the original's delivery is a single external @import (orig L1-3, 3nkv.github.io/Sodium/sodium.min.css; kind K5b-5). A JP candidate cannot take the CN maker's host as its base, so the stylesheet is vendored as the companion candidate fragment:sodium-jp-base-css (one [[code type="css"]] block, fragment L5-1636) and the theme candidate imports fragment/1 through two channels (interwiki-style priority=1, cand L1-4, and a module CSS @import, cand L6-8), the dual-channel form the externally based ports use, so the base applies whether or not the interwiki frame is present. The candidate's self-delivery addresses name the fragment's block 1, which is the stylesheet block (the fragment has exactly one code block), so the census is satisfied by construction and no FIX-CODEADDR repoint was needed. The original's 45-line variables block stays in the theme candidate as the variables exhibit (cand L339-383, comments translated), and the four preset modules (darkmode, monochrome, fullscreen-header, customized-title) keep their [[#ifexpr]] gates in render-time text wrapping live [[module css]] blocks (cand L386-437), the same gated form as the original's tail: the gates act, because include-parameter substitution reaches render-time text. The DELIVERY-MOVE mass (B92-B96 and B104 spans) is the 1,632-line stylesheet's relocation into the fragment; its internal edits are classified separately and censused in the per-theme record.


## 4. Fonts and assets

Written from label_spans (FONT-IMPORT fires inside B93, whose primary section is delivery): the font program is carried, not substituted. The fragment's @import set equals the original stylesheet's four loads (Raleway, Ubuntu, Noto Serif, JetBrains Mono), with the serif load localized from Noto Serif SC to Noto Serif JP. Stack rewrites (P7): every Noto Serif SC stack in the fragment and the candidate reads Noto Serif JP; the CN system face Yuanyuan maps to Yu Gothic, a JP system face needing no load; the Ubuntu body stack and the JetBrains Mono code stack are unchanged. Two names are carried as found: 'Nanum Gothic' and FontAwesome are named in stacks in the original's stylesheet and loaded nowhere in either delivery, inherited identically on both sides, so parity holds and no supplement is charged. No font is imported but unused, and no load is duplicated across the include chain (the fragment is imported once per channel). Assets: the theme's image files are re-addressed to the candidate's own attachment namespace on the draft host (class (ii) posting rewrite), the same deferred-hosting state as the population's.

## 5. Header, sidebar, site furniture

- HEADERVAR (A): Header/title variables (P9/T6, KB-57): the header text variables are the theme's visible title surface.
  Verify: KB-57: where the value stays in the original's language, the disposition is ruling 2 (section 11).
  - B70: orig 206-207 -> cand 202-203 (body -> body)

Why these instances are right: HEADERVAR fires in three spans. B70 is the Pataphysics specimen's :root exhibit: the header title takes the JP glyph form of the pataphysics term (a name, kept as a name in its JP form), and the header subtitle, a complete prose sentence ("the god who kills us"), is translated, under the fleet boundary ruled on 2026-11-17 (prose sentences translate; names stay). B99 is the variables exhibit block (orig L1961-1982 to cand L352-373): the theme's own default header variables and logo values, comments translated, values carried (the darkmode logo value is the draft-host re-host of section 3). B93's span is the fragment's header variables inside the moved stylesheet, localized with the move (the fragment's header comment lists the CN-to-JP header wording among its adjustments). No header value contradicts the theme's own specimens.


## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B4: orig 9-9 -> cand 23-23 (body -> body)
  - B11: orig 48-48 -> cand 44-44 (body -> body)
  - B12: orig 50-50 -> cand 46-46 (body -> body)
  - B13: orig 52-52 -> cand 48-48 (body -> body)
  - B14: orig 54-54 -> cand 50-50 (body -> body)
  - B15: orig 56-56 -> cand 52-52 (body -> body)
  - B24: orig 86-86 -> cand 82-82 (body -> body)
  - B26: orig 91-91 -> cand 87-87 (body -> body)
  - B27: orig 93-93 -> cand 89-89 (body -> body)
  - B28: orig 95-95 -> cand 91-91 (body -> body)
  - B29: orig 97-97 -> cand 93-93 (body -> body)
  - B30: orig 99-99 -> cand 95-95 (body -> body)
  - B31: orig 101-101 -> cand 97-97 (body -> body)
  - B32: orig 103-103 -> cand 99-99 (body -> body)
  - B34: orig 108-108 -> cand 104-104 (body -> body)
  - B35: orig 110-110 -> cand 106-106 (body -> body)
  - B36: orig 112-112 -> cand 108-108 (body -> body)
  - B37: orig 114-114 -> cand 110-110 (body -> body)
  - B38: orig 116-116 -> cand 112-112 (body -> body)
  - B39: orig 118-118 -> cand 114-114 (body -> body)
  - B40: orig 120-120 -> cand 116-116 (body -> body)
  - B41: orig 122-122 -> cand 118-118 (body -> body)
  - B42: orig 124-124 -> cand 120-120 (body -> body)
  - B43: orig 126-126 -> cand 122-122 (body -> body)
  - B44: orig 128-128 -> cand 124-124 (body -> body)
  - B45: orig 130-130 -> cand 126-126 (body -> body)
  - B46: orig 132-132 -> cand 128-128 (body -> body)
  - B53: orig 151-151 -> cand 147-147 (body -> body)
  - B54: orig 153-153 -> cand 149-149 (body -> body)
  - B55: orig 155-155 -> cand 151-151 (body -> body)
  - B56: orig 157-157 -> cand 153-153 (body -> body)
  - B57: orig 159-159 -> cand 155-155 (body -> body)
  - B58: orig 161-161 -> cand 157-157 (body -> body)
  - B59: orig 163-163 -> cand 159-159 (body -> body)
  - B60: orig 165-165 -> cand 161-161 (body -> body)
  - B64: orig 185-185 -> cand 181-181 (body -> body)
  - B67: orig 197-197 -> cand 193-193 (body -> body)
  - B71: orig 219-219 -> cand 215-215 (body -> body)
  - B74: orig 231-231 -> cand 227-227 (body -> body)
  - B79: orig 256-256 -> cand 252-252 (body -> body)
  - B81: orig 265-265 -> cand 261-261 (body -> body)
  - B88: orig 306-306 -> cand 302-302 (body -> body)
  - B103: orig 2018-2018 -> cand 409-409 (module-css -> module-css)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B6: orig 17-17 -> cand 31-31 (body -> body)
  - B9: orig 44-44 -> cand 40-40 (body -> body)
  - B16: orig 65-65 -> cand 61-61 (body -> body)
  - B17: orig 67-67 -> cand 63-63 (body -> body)
  - B18: orig 69-69 -> cand 65-65 (body -> body)
  - B19: orig 71-71 -> cand 67-67 (body -> body)
  - B20: orig 73-73 -> cand 69-69 (body -> body)
  - B21: orig 75-75 -> cand 71-71 (body -> body)
  - B22: orig 80-81 -> cand 76-77 (body -> body)
  - B23: orig 83-84 -> cand 79-80 (body -> body)
  - B25: orig 88-89 -> cand 84-85 (body -> body)
  - B33: orig 105-106 -> cand 101-102 (body -> body)
  - B47: orig 134-134 -> cand 130-130 (body -> body)
  - B48: orig 136-136 -> cand 132-132 (body -> body)
  - B49: orig 138-139 -> cand 134-135 (body -> body)
  - B50: orig 141-141 -> cand 137-137 (body -> body)
  - B51: orig 143-143 -> cand 139-139 (body -> body)
  - B52: orig 145-145 -> cand 141-141 (body -> body)
  - B61: orig 169-171 -> cand 165-167 (body -> body)
  - B62: orig 174-175 -> cand 170-171 (body -> body)
  - B63: orig 182-182 -> cand 178-178 (body -> body)
  - B78: orig 254-254 -> cand 250-250 (body -> body)
  - B82: orig 269-270 -> cand 265-266 (body -> body)
  - B83: orig 276-277 -> cand 272-273 (body -> body)
  - B84: orig 283-284 -> cand 279-280 (body -> body)
  - B85: orig 290-291 -> cand 286-287 (body -> body)
  - B86: orig 297-298 -> cand 293-294 (body -> body)
  - B87: orig 304-304 -> cand 300-300 (body -> body)
  - B89: orig 308-308 -> cand 304-304 (body -> body)
  - B90: orig 310-310 -> cand 306-306 (body -> body)
  - B91: orig 313-313 -> cand 309-309 (body -> body)
  - B97: orig 1948-1948 -> cand 339-339 (body -> body)
  - B98: orig 1951-1959 -> cand 342-350 (code-css -> code-css)
  - B100: orig 1984-1986 -> cand 375-377 (code-css -> code-css)
  - B101: orig 1988-1991 -> cand 379-382 (code-css -> code-css)

Why this mass is right: the documentation body and the formatting specimens are translated one-to-one (51 TRANS-UNANCHORED and 38 TRANSLATION-ANCHORED blocks); the appendix resolves the unanchored queue by shape and finds no drop or restoration hiding in it (the two structural blocks, B8 and B10, are adjudicated in sections 1 and 8). Named decisions: (1) the link specimen table (appendix R12) localizes its example URL (baidu.com to example.com) and its <a href> specimen host (scp-wiki-cn to scp-jp), while keeping the deliberate nonexistent-link specimen as a specimen, exactly as the original keeps it; (2) the Pataphysics colour specimen keeps the name string 'Pataphysics' with its colour code (appendix R43); (3) the theme's name takes the standing JP notation in the credit title and body (the T5 notation item for this row), while the CSS banner and variable names keep 'Sodium'. The CSS comment mass inside the moved stylesheet belongs to the companion fragment, classified with the pair; its translations are completeness, not display.


## 7. Links

Written from the bytes (no link signature fired as a primary): the candidate's prose links are three shapes. (1) The credit-field and prose references to theme:monotypical keep the plain form: the target is a live SCP-JP production page, which this lane's T1 run confirms indirectly, since the checker's link-label warns compare the label against the production page's actual title, so the page resolves; under the monotypical ground the link stands and the label difference is recorded, not edited. (2) The usage specimens repoint the theme's own include to theme:sodium-jp (B5 span; appendix R2-R5 for the escaped preset specimens). (3) The fragment's header comment keeps the original stylesheet's URL (3nkv.github.io/Sodium/sodium.min.css) as a provenance citation; it is not a delivery line. No dead prose link was found: the one link-target-missing warn (4o4-n0t-f0und) is the deliberate empty-link specimen, present in the original's specimen table in the same form.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B10: orig 46-46 -> cand 42-42 (body -> body)

- RESTORATION (C): Deleted/emptied structure restored (ledger class I, FIX5): content the port had lost is restored from the original or a named sibling source.
  Verify: The ledger/supplement item for this theme, plus the restored region read against the mirror.
  - B104: orig at 2049 -> cand 440-464 (body -> module-css)

B10's EXHIBIT-RESTRUCTURE label is a false fire on the image-block specimen line (the include's name= address was re-hosted and its caption translated; the specimen stands). B104's RESTORATION label is likewise a mis-assignment: cand L440-464 is the T7 credit supplement module (section 1), newly written for the JP credit DOM, not restored content. Nothing in the ledger charges this theme with a class-I deletion, and this lane's census finds no dropped original content: the one large deletion (B8) is the credit normalization of section 1, and the 1,632-line stylesheet is relocated, not dropped (section 3).


Exhibit decisions: the exhibit census (the examples collapsible, the formatting specimens, the tabview, the preset demonstrations for darkmode, Pataphysics colours, fullscreen header, customized header and transparent background, the source-code and variables collapsibles, and the font specimens) is present on both sides with the same members. The credit demonstrations inside the examples collapsible were replaced, not dropped: the original's two full credit sets and its labelled specimen Rate (orig L19-41) are represented by the single preview pair (cand L32-37), the JP environment's only credit form; that replacement is the LOCALIZE row's headline item, closed by the credit waves (section 1). Bare-Rate reasoning: the candidate carries no bare [[module Rate]] anywhere; the original's head Rate (orig L7) and specimen Rate (orig L20) are both absorbed into the preview credit form, which embeds its own rating module, so no double-widget shape arises.


## 9. Formatting only

- WS-ONLY blocks: 0
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

Two porter annotations, both checked against the bytes. (1) The companion fragment's header comment (fragment L1-3, inside a [-- --] comment): states the delivery mechanism (the fragment's code block is served as local--code/fragment:sodium-jp-base-css/1 and imported by theme:sodium-jp), lists the JP adjustments applied to the stylesheet (Noto Serif SC to JP, CN header wording to JP, the CN system face to Yu Gothic, CN image URLs to candidate attachments, font-weight 700 to bold, shorthand normalization, selector reordering), and notes that theme:sodium-pentasulfide-jp receives this base through its documented two-stage include of theme:sodium-jp. Each listed adjustment is present in the fragment as stated (this lane's census). (2) The T7 comment (candidate L313-315 in the source exhibit and L441-443 in the live module): states that credit:start-preview emits a direct-child a under .creditButton while the theme's rule is written for .creditButton p a, and that the supplement applies the same declarations to the direct child. True against the bytes: the fragment's stylesheet carries the p a rule and the supplement carries the > a rule with identical declarations.

## 11. Dispositions and exceptions

- No derived presence label fired.

The dispositions restated so a reviewer can re-derive them from this package:

- Item 83 [E] (the invisible clear-vote): DISPOSITIONED by FIX5-CONTRA (supplement (a) item 83), re-derived in the per-theme record below. Ground: the charged colour exists in neither the candidate nor its base fragment nor the original; the theme's rate sections are declaration-identical to the original's; the photographed control belongs to the shared preview credit module's rendering (KB-32 class), not to this theme's CSS. The ledger's charge class was KB-28 (a theme-defect class); the disposition's class is KB-32.
- Register (c2), RENDER-S2-G (CN14) row: the hidden-login line (desktop, both engines) and the runtime-hotlink line are environment-layer (KB-40); the sample credit-modal errors are the preview form's property (KB-32); full-engine coverage is a coverage statement, not a finding. The row's one OPEN line (the clear-vote) is item 83 above.
- Register (c1): the nine T1 pseudo-ref errors are the candidate's and fragment's own draft-host addresses (KB-41, class (ii)); posting rewrites them.
- Register (c3): P3 credit fields FIXED by the credit waves (checker-verified).
- Draft-host deliveries (B1/B10/B65/B68/B72/B75/B77/B99/B102 spans): class (iii) draft-stage form, sanctioned (KB-41).
- The theme:monotypical plain-form link stands on the monotypical ground (production page exists; section 7).


## 12. Verification

- T1: this lane re-ran the checker on the current candidate (uv run scripts/check_source.py pages/theme:sodium-jp.txt --kind theme --translation --check-links, from the skill directory /home/roku/src/SCP-JP/claude-plugins-staff/plugins/scp-jp-staff/skills/theme-component-review): exit 1, 9 errors / 3 warns / 0 infos, identical to the T1-ROWS row 259 baseline. All 9 errors are pseudo-ref on draft-host addresses (L7 fragment import; L42, L183, L195, L217, L229 file specimens; L244, L357, L392 url() files). The 3 warns: link-label x2 (the Monotypical label against the production page's title; the target resolves, section 7) and link-target-missing for 4o4-n0t-f0und (the deliberate empty-link specimen, section 8).
- T2/T3: RENDER-S2-G (CN14) row, full-engine coverage; its lines are dispositioned in section 11. Not re-run by this lane.
- T4: LOCALIZE-ROWS row 227; the headline credit-concentration item is closed by the credit waves (section 1); the follow-up diff is the FIX5 re-judgement of item 83 (supplement (a)), re-derived below.
- T5: judged jointly with T4 on this row; the theme-name notation is the standing item, not a defect.
- Package checks, run by this lane: candidate.txt sha256 equals the canonical file's; original.txt sha256 equals the sources.tsv value; the colour census and the rate-section declaration census of the per-theme record were run on these bytes; the companion fragment was classified with the pair (--companions) and its header-comment claims censused.


## Per-theme record — item 83 [E] re-derivation and second-reviewer walk

The blocking item. GOSIGN2-LEDGER (e) item 83 [E]: the rating clear-vote control renders near-white on white, effectively invisible (render T3, both pages), charged as a KB-28 instance (a class-B theme defect whose fix would be to correct the variable binding in the candidate); no fix wave corrected a KB-28 binding for this theme and no original-faithful ground was recorded. FIX5 re-judged it DISPOSITIONED (FIX5-CONTRA, no edit): the charged colour rgb(255,246,240) / #FFF6F0 exists nowhere in the candidate or its base fragment; the invisible control was traced to the shared preview credit module's rendering (KB-32 class); the theme's own rate colours are identical to the CN original's.

Re-derivation from this package's bytes (this lane, 2026-11-17):

1. Colour census: the charged colour occurs 0 times in candidate.txt, 0 times in the companion fragment (pages/fragment:sodium-jp-base-css.txt), and 0 times in original.txt (grep for the rgb triple and the hex form in all three files). The colour the charge names is not a value this theme has ever carried.
2. Rate-section identity: the theme's rate section (original L965-1085, headed by the rate-module comment and containing the .page-rate-widget-box .cancel rules at orig L988-1011) and the fragment's corresponding section (fragment L656-776) have identical declaration lines with comments stripped: 58 declaration lines each, SHA-256 prefix d54c1192ecdd on both sides, and equal colour-token multisets. Only the comments differ (translated). Whatever the theme's rate controls look like, they look like the original's.
3. The theme's own clear-vote colour is dark by construction: the rule .page-rate-widget-box .cancel a sets color: var(--sodium-text-color) (orig L1001-1003), and --sodium-text-color is #252525 in the original's stylesheet variables (orig L355), in the fragment (L46), and in the candidate's variables exhibit (cand L347). A near-white clear-vote cannot be produced by this theme's CSS.
4. The photographed surface is the preview credit module's own widget: the candidate and sample pages render credit:start-preview, whose rating UI is shared chrome (KB-32 class), the same surface the ledger's (c2) row already dispositions for this theme's credit-modal errors.

Ground confirmed exactly; the disposition stands. The charge's class (KB-28, theme defect) is refuted by points 1 and 3; the disposition's class (KB-32, shared preview module) is the only one consistent with the bytes.

Second-reviewer walk. Could a reader who did none of the work check this? The deciding facts are all reproducible from this repo: the colour census is a grep over the two package files plus the companion (a canonical candidate file, named above); the declaration-identity claim names both line ranges and the hash; the dark binding is one grep for --sodium-text-color. One record weakness, repaired here: the supplement's disposition sentence says the colour "exists nowhere in the candidate or its base fragment" but does not name the fragment file or the rate sections' line ranges; this record names them. Walk outcome: sound.

Defect flags: none. The candidate's credit, delivery, gates, and content census all check out (sections 1-10). One sources.tsv note correction is reported in section 0 for the coordinator's harvest (the supersession claim its own cited artifact refutes); sources.tsv is not edited by this lane.

## Appendix — residue blocks

### Residue R1 — B8 (residue; orig 22-41 -> cand at 38, body -> body)

Resolution: section 1. The original's two full credit-module demonstrations (the start/more/end set and the standalone set, orig L22-41), removed by the credit-wave normalization: the JP environment's only credit form is the preview pair the candidate demonstrates in the same collapsible (cand L32-37). This deletion is the LOCALIZE-ROWS row 227 headline item, closed by the credit waves, not a silent exhibit drop.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R2 — B66 (residue; orig 189-189 -> cand 185-185, body -> body)
- Removed first line: @@[[include :scp-wiki-cn:theme:sodium@@
- Added first line: @@[[include theme:sodium-jp@@

Resolution: section 7. An escaped (@@...@@) usage specimen inside a preset demonstration: the theme's own include in the specimen is repointed to theme:sodium-jp (the usage-example sweep class); the specimen's gated preset text is otherwise unchanged.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R3 — B69 (residue; orig 201-201 -> cand 197-197, body -> body)
- Removed first line: @@[[include :scp-wiki-cn:theme:sodium@@
- Added first line: @@[[include theme:sodium-jp@@

Resolution: section 7. Same shape as R2: an escaped usage specimen whose include of the theme itself is repointed to theme:sodium-jp.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R4 — B73 (residue; orig 223-223 -> cand 219-219, body -> body)
- Removed first line: @@[[include :scp-wiki-cn:theme:sodium@@
- Added first line: @@[[include theme:sodium-jp@@

Resolution: section 7. Same shape as R2: an escaped usage specimen whose include of the theme itself is repointed to theme:sodium-jp.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R5 — B76 (residue; orig 235-235 -> cand 231-231, body -> body)
- Removed first line: @@[[include :scp-wiki-cn:theme:sodium@@
- Added first line: @@[[include theme:sodium-jp@@

Resolution: section 7. Same shape as R2: an escaped usage specimen whose include of the theme itself is repointed to theme:sodium-jp.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R6 — B80 (residue; orig 260-261 -> cand 256-257, body -> body)
- Removed first line: [[span style="font-family: 'JetBrains Mono', 'Noto Serif SC', serif"]]@@[[div class="special-hr"]]@@[[/span]]
- Added first line: [[span style="font-family: 'JetBrains Mono', 'Noto Serif JP', serif"]]@@[[div class="special-hr"]]@@[[/span]]

Resolution: sections 4 and 6, class P7. A specimen line whose inline span stack localizes Noto Serif SC to Noto Serif JP; the special-hr specimen it demonstrates is unchanged.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R7 — B4 (heuristic; orig 9-9 -> cand 23-23, body -> body)
- Removed first line: 这是由[[*user Ankv]]制作的美学版式，不与任何 SCP、故事、GoI 格式、设定所挂钩且不基于任何版式。在设计上参考了[[*user EstrellaYoshte]] 的[[[theme:monotypical|单色型版式]]]。
- Added first line: これは[[*user Ankv]]による美的なテーマで、特定のSCP・物語・GoIフォーマット・設定には紐づけられず、既存のどのテーマにも基づいていません。デザインには[[*user EstrellaYoshte]]の[[[theme:monotypical|Monotypicalテーマ]]]を参考にしています。
- Note: script delta without the anchor majority

Resolution: sections 1 and 6. The credit prose paragraph, translated in full; it carries the Ankv authorship and the EstrellaYoshte/Monotypical design reference that the credit field also names.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R8 — B11 (heuristic; orig 48-48 -> cand 44-44, body -> body)
- Removed first line: 可通过五个连字符“@@-----@@”创建水平分割线。若它未被放在其他部件（诸如引用块）中，则会左右延伸贯穿页面。这种将文件分割为多个部分的线就是分割线。
- Added first line: 5個の連字符「@@-----@@」で水平線を作れます。何かの中（引用ブロックなど）に置かれていなければ、左右いっぱいに広がります。ページを複数の節に分けるこの線が水平線です。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R9 — B12 (heuristic; orig 50-50 -> cand 46-46, body -> body)
- Removed first line: 标题可通过在一行字起始处输入 1 至 6 个加号“+”来创建。
- Added first line: 見出しは、行頭に1個から6個のプラス記号「+」を置いて作成できます。
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R10 — B13 (heuristic; orig 52-52 -> cand 48-48, body -> body)
- Removed first line: 一个普通的__下划__**加粗**//斜体//--删除--{{等宽}}__**//--{{字}}--//**__
- Added first line: 普通の__下線__**太字**//斜体//--取り消し--{{等幅}}__**//--{{字}}--//**__
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R11 — B14 (heuristic; orig 54-54 -> cand 50-50, body -> body)
- Removed first line: 另一个普通的 __下划__ **加粗** //斜体// --删除-- {{等宽}} __**//--{{字}}--//**__
- Added first line: もう一つの普通の __下線__ **太字** //斜体// --取り消し-- {{等幅}} __**//--{{字}}--//**__
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R12 — B15 (heuristic; orig 56-56 -> cand 52-52, body -> body)
- Removed first line: | [https://www.baidu.com/ 这是一个链接！] | [[[4o4-n0t-f0und|一个空链接！]]] | [[a href="http://scp-wiki-cn.wikidot.com/"]]一个普通的__下划__**加粗**//斜体//--删除--{{等宽}}__**//--{{链接}}--//**__[[/a]] | [[a href="http://scp-wiki-cn.wikidot.com/"]]另一个普通的 __下划__ **加粗** //斜体// --删除-- {{等宽}} __**//--{{链接}}--//**__[[/a]]
- Added first line: | [https://www.example.com/ これはリンク！] | [[[4o4-n0t-f0und|空のリンク！]]] | [[a href="https://scp-jp.wikidot.com/"]]普通の__下線__**太字**//斜体//--取り消し--{{等幅}}__**//--{{リンク}}--//**__[[/a]] | [[a href="https://scp-jp.wikidot.com/"]]もう一つの普通の __下線__ **太字** //斜体// --取り消し-- {{等幅}} __**//--{{リンク}}--//**__[[/a]]
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: sections 6 and 7. The link specimen table: the example URL is localized (baidu.com to example.com), the <a href> specimen host follows the environment (scp-wiki-cn to scp-jp), and the deliberate nonexistent-link specimen is kept as a specimen, as in the original (the T1 link-target-missing warn on it is adjudicated in section 12).
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R13 — B24 (heuristic; orig 86-86 -> cand 82-82, body -> body)
- Removed first line: 多么精巧绝伦。
- Added first line: なんとも精巧で絶倫です。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R14 — B26 (heuristic; orig 91-91 -> cand 87-87, body -> body)
- Removed first line: 这是一个长的 tab，它有很多文字。
- Added first line: これは長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R15 — B27 (heuristic; orig 93-93 -> cand 89-89, body -> body)
- Removed first line: 这是一个长的 tab，它有很多文字。
- Added first line: これは長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R16 — B28 (heuristic; orig 95-95 -> cand 91-91, body -> body)
- Removed first line: 这是一个长的 tab，它有很多文字。
- Added first line: これは長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R17 — B29 (heuristic; orig 97-97 -> cand 93-93, body -> body)
- Removed first line: 这是一个长的 tab，它有很多文字。
- Added first line: これは長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R18 — B30 (heuristic; orig 99-99 -> cand 95-95, body -> body)
- Removed first line: 这是一个长的 tab，它有很多文字。
- Added first line: これは長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R19 — B31 (heuristic; orig 101-101 -> cand 97-97, body -> body)
- Removed first line: 这是一个长的 tab，它有很多文字。
- Added first line: これは長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R20 — B32 (heuristic; orig 103-103 -> cand 99-99, body -> body)
- Removed first line: 这是一个长的 tab，它有很多文字。
- Added first line: これは長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R21 — B34 (heuristic; orig 108-108 -> cand 104-104, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R22 — B35 (heuristic; orig 110-110 -> cand 106-106, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R23 — B36 (heuristic; orig 112-112 -> cand 108-108, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R24 — B37 (heuristic; orig 114-114 -> cand 110-110, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R25 — B38 (heuristic; orig 116-116 -> cand 112-112, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R26 — B39 (heuristic; orig 118-118 -> cand 114-114, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R27 — B40 (heuristic; orig 120-120 -> cand 116-116, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R28 — B41 (heuristic; orig 122-122 -> cand 118-118, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R29 — B42 (heuristic; orig 124-124 -> cand 120-120, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R30 — B43 (heuristic; orig 126-126 -> cand 122-122, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R31 — B44 (heuristic; orig 128-128 -> cand 124-124, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R32 — B45 (heuristic; orig 130-130 -> cand 126-126, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R33 — B46 (heuristic; orig 132-132 -> cand 128-128, body -> body)
- Removed first line: 这也是一个长的 tab，它有很多文字。
- Added first line: これも長いタブで、たくさんの文字が入っています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. One of the tabview specimen's repeated filler lines, translated in place.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R34 — B53 (heuristic; orig 151-151 -> cand 147-147, body -> body)
- Removed first line: > 这是一个引用块，在一行字的起始处加上“> ”来创建。
- Added first line: > これは引用ブロックで、行頭に「> 」を置いて作成します。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. A blockquote specimen line translated in place; the '>' nesting markers are the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R35 — B54 (heuristic; orig 153-153 -> cand 149-149, body -> body)
- Removed first line: > 更多文字
- Added first line: > もっと文字
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. A blockquote specimen line translated in place; the '>' nesting markers are the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R36 — B55 (heuristic; orig 155-155 -> cand 151-151, body -> body)
- Removed first line: > 一条分割线
- Added first line: > 一本の水平線
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. A blockquote specimen line translated in place; the '>' nesting markers are the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R37 — B56 (heuristic; orig 157-157 -> cand 153-153, body -> body)
- Removed first line: >> 嵌套引用块
- Added first line: >> 入れ子の引用ブロック
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. A blockquote specimen line translated in place; the '>' nesting markers are the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R38 — B57 (heuristic; orig 159-159 -> cand 155-155, body -> body)
- Removed first line: >> 嵌套引用块里的分割线
- Added first line: >> 入れ子の引用ブロックの中の水平線
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. A blockquote specimen line translated in place; the '>' nesting markers are the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R39 — B58 (heuristic; orig 161-161 -> cand 157-157, body -> body)
- Removed first line: >>> 嵌套嵌套引用块
- Added first line: >>> 入れ子の入れ子の引用ブロック
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. A blockquote specimen line translated in place; the '>' nesting markers are the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R40 — B59 (heuristic; orig 163-163 -> cand 159-159, body -> body)
- Removed first line: >>> 嵌套嵌套引用块里的分割线
- Added first line: >>> 入れ子の入れ子の引用ブロックの中の水平線
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. A blockquote specimen line translated in place; the '>' nesting markers are the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R41 — B60 (heuristic; orig 165-165 -> cand 161-161, body -> body)
- Removed first line: >>>> 够了，禁止套娃
- Added first line: >>>> もう十分だ、入れ子はここまでにしよう
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. A blockquote specimen line translated in place; the '>' nesting markers are the anchor.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R42 — B64 (heuristic; orig 185-185 -> cand 181-181, body -> body)
- Removed first line: 本版式亦有一个暗色模式。
- Added first line: このテーマにはダークモードもあります。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R43 — B67 (heuristic; orig 197-197 -> cand 193-193, body -> body)
- Removed first line: 本版式的颜色可以自由搭配，同时可自定义主标题和副标题。以下是一个##5800bd|Pataphysics##主题配色。
- Added first line: このテーマの色は自由に組み合わせられ、主見出しと副見出しもカスタマイズできます。以下は##5800bd|Pataphysics##の配色例です。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. The Pataphysics colour specimen's introduction, translated; the specimen's name string and colour code are kept (section 5).
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R44 — B71 (heuristic; orig 219-219 -> cand 215-215, body -> body)
- Removed first line: 版头的高度可以自定义，因此预设了一个霸屏版头。
- Added first line: ヘッダーの高さは自在にカスタマイズできるため、画面いっぱいのヘッダーがプリセットされています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R45 — B74 (heuristic; orig 231-231 -> cand 227-227, body -> body)
- Removed first line: 版式的背景可插入图片（移动端图片表现可能不佳，因此默认只有版头容纳背景图片）。这是一个透明背景示例，不会配色请不要打我。
- Added first line: テーマの背景には画像を差し込めます（モバイルでは画像の扱いが難しいため、既定ではヘッダーのみが背景画像を持ちます）。これは透明背景の例です。配色が苦手でも責めないでください。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R46 — B79 (heuristic; orig 256-256 -> cand 252-252, body -> body)
- Removed first line: 这里有一条特殊的分割线。
- Added first line: ここに特殊な水平線があります。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R47 — B81 (heuristic; orig 265-265 -> cand 261-261, body -> body)
- Removed first line: 本版式额外提供一些具有个性的盒子。
- Added first line: このテーマでは、個性的なボックスをいくつか追加で提供しています。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class P10. Prose/specimen text translated one-to-one against the mirror; no structural change rides in this block.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R48 — B88 (heuristic; orig 306-306 -> cand 302-302, body -> body)
- Removed first line: 正文字体为 Ubuntu。
- Added first line: 本文の書体は Ubuntu です。
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: sections 4 and 6. A font specimen's caption, translated; the stack it names (Ubuntu) is unchanged on both sides.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


### Residue R49 — B103 (heuristic; orig 2018-2018 -> cand 409-409, module-css -> module-css)
- Removed first line: /* 请填写logo链接，默认无logo */
- Added first line: /* ロゴのリンクを入力してください。既定ではロゴなし */
- Note: porter-visible only; labeled and skipped by design
- Note: script delta without the anchor majority

Resolution: section 6, class R1 (in-CSS text, comment half). A CSS comment translated in place. Comments are porter-visible only and never render, so this is translation completeness, not a display change; no KB entry is proposed.
Assign this block to a section (and write it there) or propose it as a new signature / pattern in the lane report.


