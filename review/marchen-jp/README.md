# Review package — theme:marchen-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:marchen-jp — origin CN, population #205 [GOSIGN2-LEDGER (b) row 205]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged DISPOSITIONED with grounds by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 19 errors / 1 warn / 1 info (pseudo-ref×15, hotlink×4); standing classes dispositioned in register c1 [T1-ROWS row 271; GOSIGN2-LEDGER (b) row 205]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page page-overflow 435px chromium / 436px webkit @320/375, runtime-hotlink site-theme chain + candidate-own cdn.jsdelivr.net (judgment-required), `sidebar-not-opening` [webkit 1366x768]; sample credit-modal (preview-form), same page-overflow (sample T3: cross-cutting static-credit shape), same runtime-hotlink + sample font host, `sidebar-not-opening` [webkit 1366x768]; T3 REAL FINDING on both pages: at webkit 1366x768 the hamburger open control is present but pressing it does not bring the sidebar on-screen, no drawer appears, whereas chromium shows the sidebar open at left (machine line corroborates); mobile ≤375 hamburger opens in both engines; rate/credit/footer/license/JP font fine. [RENDER-ROWS-RERUN16 (CN9) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN9)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 204, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 204]
- FIX5 re-judgement: item 67 (class F) DISPOSITIONED — FIX5-FUNC §2 (no edit): toggle rules candidate L1675-1703 byte-identical to original L865-893 (diff IDENTICAL); failure confined to one engine at one viewport while mobile widths open in both engines [GOSIGN2-LEDGER-SUPPLEMENT (a) item 67]
- Computed against: canonical commit 379eb44032d541453098c3177e0b1e3fc62c5964; candidate file pages/theme:marchen-jp.txt sha256:fc9cd69d676a560b87c93c99df22e8d2a52d16813bf01ed5dc7b4634b3419e41; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (R-disp-8 lane, 2026-11-17)
Candidate: review/marchen-jp/candidate.txt (sha256 fc9cd69d676a560b87c93c99df22e8d2a52d16813bf01ed5dc7b4634b3419e41)
Original: theme:marchen — scp-wiki-cn, revision 35 (sha256 4f2309705c20aa37636d7f1b5c6ce6947a8f849becc0494da3e286f2f613a9e9)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (generated stamp) | Notes |
|---|---|---|
| T1 source check | FINDINGS (classified) | Baseline 19 errors / 1 warn / 1 info (pseudo-ref x15, hotlink x4); this lane's run on the current file reads 17 / 0 / 1 (section 12) |
| T2/T3 render | FINDINGS | The WebKit 1366 sidebar finding is FIX5 item 67, re-derived in the per-theme record; the remaining row lines are dispositioned in register (c2) via RERUN16 |
| T4/T5 localize/translation | FINDINGS | 2 display-affecting findings, both delivery items (LOCALIZE-S2-D): one fixed by repoint, one dispositioned; no translation residue |
| FIX5 item 67 [F] | DISPOSITIONED (FIX5-FUNC section 2, no edit) | Re-derived on this package's bytes in the per-theme record; the ground holds exactly |

## Provenance

| | |
|---|---|
| Original | theme:marchen, scp-wiki-cn, revision 35 (first-translation reference revision) |
| Mirror | review-mirrors/orig-marchen-rev35.txt, class COPY, sha256 4f2309705c20aa37636d7f1b5c6ce6947a8f849becc0494da3e286f2f613a9e9 (equals the sources.tsv value) |
| Candidate | pages/theme:marchen-jp.txt, sha256 fc9cd69d676a560b87c93c99df22e8d2a52d16813bf01ed5dc7b4634b3419e41 |
| Kind | K5b-3 (multi-part composition): the candidate layers over theme:basalt-jp through a bundled base layer (section 3) |
| Production counterpart | none (no SCP-JP production page for this theme) |

## Summary

Marchen is a CN aesthetic theme by Sharia Vanilla, built on the CN Basalt derivative Parallel, and made mainly for the Waldichter GoI format. The port keeps the original's architecture and translates it in full: the remote base fragment the original imported is bundled as the candidate's own first code fragment, the theme's own three fragments shift one number up, every include and asset is repointed or re-hosted, and the prose, specimens, and credit are localized. The theme's one blocking item (item 67, class F) was dispositioned without an edit because the sidebar toggle rules are byte-identical to the original; that ground is re-measured in the per-theme record and holds exactly. Two minor items are flagged there for the coordinator: a plain-form prose link to theme:lumina that does not resolve on SCP-JP, and an annotation nit on the theme:parallel prose link.

## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 10 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 5 |
| DELIVERY-HOST | 6 |
| DRAFT-HOST | 15 |
| EXHIBIT-RESTRUCTURE | 2 |
| GLYPH-FORM | 4 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 11 |
| JPFONT-LOAD | 2 |
| SELF-DELIVERY | 7 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 79 |
| TRANSLATION-ANCHORED | 33 |
| WS-ONLY | 3 |

Counts: 142 blocks, 66 specific, 75 heuristic, 1 residue, 0 skipped (comment text).

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

The provenance route is derivation from the original at the reference revision: the candidate is the campaign's first translation of scp-wiki-cn theme:marchen at revision 35, the revision its credit block records (candidate L281). The mirror is a byte copy of the campaign's frozen S2 cache (class COPY), hash-verified above. The one composition caveat is K5b-3: the original imports its base (fragment:parallel/1) remotely, and the candidate bundles that base layer as its own fragment 1, so the package diff covers the theme's whole delivered file, base layer included; section 3 separates the bundled layer from the theme's own layer throughout.

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B10: orig 270-270 -> cand 274-283 (body -> body)

- T7-CREDIT-CSS (B): Credit-module CSS supplement (T7, KB-11/KB-12/KB-62): the JP credit module's DOM needs rules the branch original never shipped, or its inherited rules corrected in place.
  Verify: KB-11/KB-12 recipes: confirm the selectors in the candidate and whether the production counterpart carries them (supplement vs inherited).
  - B125: orig 768-768 -> cand 774-1578 (code-css -> code-css)

- What: B10 is the whole credit swap. The original's furniture (the bare [[module rate]] at original L270 and the CN credit:start / credit:more / credit:end plus standalone pair, original L273-281) is replaced by the JP preview pair at candidate L274-283 carrying the full field set: title, translator (AI), translation year (2026), original title, holder (Sharia Vanilla), creation year (2025), first-translation reference revision (35), source link. The title and original-title fields read 深林 版式, the CN theme's own name, retained deliberately: the localize lane judged the retention an observation (the credit title and the body are consistent, and the theme's base sibling parallel-jp carries the same 版式 form), and the page's meta-title design string "Märchen Theme" (original L266, candidate L270) is kept as a design string.
- Why: P3/T1. The branch credit module does not render in the JP environment and the bare Rate module is a leftover; the preview credit is the rate-bearing JP form (patterns KB-09, KB-11, KB-12 at patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa).
- Verify: the holder field names Sharia Vanilla, the author the original's own prose credit names (original L283: made by [[*user Sharia Vanilla]] for SCP-CN), so there is no pointer-instead-of-author defect. The source link's host is scp-wiki-cn.wikidot.com, the host sources.tsv records for the original. B125's T7-CREDIT-CSS label is a classifier mislabel adjudicated here: the block is the bundled-layer seam (original L768 to candidate L774-1578, section 3), and this theme carries no credit-module CSS supplement; the credit module's styling arrives with the base layer on both sides.
- Disposition: T1 credit form APPLIED with notation nits recorded by LOCALIZE-S2-D (bare AI translator string, bare holder name without a user link, link text ソース), a campaign-wide notation class, not a defect of this theme.

## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B7: orig 244-244 -> cand 249-249 (body -> body)

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B13: orig 288-288 -> cand 291-291 (body -> body)
  - B15: orig 294-294 -> cand 297-297 (body -> body)
  - B17: orig 300-300 -> cand 303-303 (body -> body)
  - B61: orig 472-472 -> cand 475-475 (body -> body)
  - B63: orig 476-476 -> cand 479-479 (body -> body)
  - B65: orig 480-480 -> cand 483-483 (body -> body)
  - B67: orig 484-484 -> cand 487-487 (body -> body)
  - B74: orig 520-520 -> cand 523-523 (body -> body)
  - B83: orig 551-558 -> cand 554-561 (body -> body)
  - B91: orig 625-625 -> cand 628-628 (body -> body)

- What: B7 localizes the tag gate ([[iftags +版式]] at original L244 becomes [[iftags +テーマ]] at candidate L249, closing at candidate L2286). The COMPONENT-SWAP blocks (B13, B15, B17, B61, B63, B65, B67, B74, B83, B91) are the theme's own usage exhibits: every @@[[include :scp-wiki-cn:theme:marchen ...]]@@ specimen (the theme=, daybreak=, dendrophobia=, pagebook, paging, portable-toc, and selres forms) is repointed to theme:marchen-jp with its parameters unchanged; the INCLUDE-REPOINT label fires inside the same blocks. B20 (original L315 to candidate L318) is the theme-squares include gaining the :scp-jp: prefix; the classifier's EXHIBIT-RESTRUCTURE label on it is a false fire on a one-line repoint inside the usage text. The component:interwiki-style include (candidate L20-23) and the component:image-block includes are unprefixed on both sides, as the original has them.
- Why: P2/T2 (KB-08) for the tag name; T8 include repoints so the exhibits name the page that will exist at posting, in the post-sweep token form.
- Verify: grep the include lines on both sides; every exhibit in the original has its counterpart in the candidate with parameters intact (the exhibit census is in section 8). The multi-line selres include whose first line is the package's one residue block (B81, original L547 to candidate L550) is the same repoint in multi-line form; the signature missed it only because the include spans lines.
- Disposition: T4 pattern 1 APPLIED (notes) per LOCALIZE-S2-D; the unprefixed component includes are recorded there as notes, not findings.

## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B1: orig 4-4 -> cand 4-4 (module-css -> module-css)
  - B2: orig 8-8 -> cand 8-8 (module-css -> module-css)
  - B3: orig 14-14 -> cand 14-14 (module-css -> module-css)
  - B9: orig 251-251 -> cand 255-255 (module-css -> module-css)
  - B124: orig 766-766 -> cand 771-772 (code-css -> code-css)

- SELF-DELIVERY (A): Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel.
  Verify: The named delivery resolves on the draft host and serves the current candidate body.
  - B4: orig at 19 -> cand 19-23 (body -> body)
  - B8: orig 247-247 -> cand at 252 (module-css -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B68: orig 492-493 -> cand 495-496 (body -> body)
  - B126: orig 817-817 -> cand 1627-1627 (code-css -> code-css)
  - B127: orig 819-819 -> cand 1629-1629 (code-css -> code-css)
  - B128: orig 821-821 -> cand 1631-1631 (code-css -> code-css)
  - B129: orig 824-824 -> cand 1634-1634 (code-css -> code-css)
  - B130: orig 827-827 -> cand 1637-1637 (code-css -> code-css)
  - B131: orig 830-830 -> cand 1640-1640 (code-css -> code-css)

- What: the delivery map, side by side. Original: a head [[module css]] inside the {$theme} gate imports the page's own fragments /1 (main layer), /2 (daybreak variant, comment-gated), /3 (dendrophobia variant, comment-gated); fragment 1 (original L765-1390) itself imports the remote base fragment:parallel/1 (original L766). Candidate: the same head module imports /2, /3, /4 (B1, B2, B3), because a new fragment 1 (candidate L770-1572) now carries the base layer: the Parallel base the original imported remotely is bundled into the candidate's own first code block, documented by the porter comment at candidate L768 (section 10). Fragment 1 is delivered at priority 1 by the interwiki-style include inserted in the {$theme} gate (B4, candidate L20-23), and the theme's own main layer (fragment 2, candidate L1574-2200) imports it in turn (candidate L1576). The shifted fragments measure: candidate fragment 4 is byte-identical to original fragment 3 (180 bytes, sha256 0ead9dcd769a79b189fb49d0bb78b275552898f5dbadffd94149ff17dee83e9a on both sides); candidate fragment 3 differs from original fragment 2 by exactly one byte (a trailing space after a selector comma on the #main-content::before line) over 1,467 bytes; candidate fragment 2 is original fragment 1 with its head import repointed (remote fragment to own /1) and its font program swapped (section 4). B124 is that head repoint plus the bundled layer's own Basalt import: FIX4-REPOINT (commit 443c608) replaced the two jsDelivr gh/ Basalt imports with the draft-host address of theme:basalt-jp fragment 1, and FIX4-MOPUP (commit 379eb44) removed the duplicate copy the repoint had written and the duplicate ungated /2 import in the iftags module (B8), both KB-65 duplicate deliveries. B9 is the daybreak import renumbered inside the iftags module (original L251 to candidate L255). B126-B131 (DRAFT-HOST) are image url()s inside fragment 2 re-hosted to the candidate's own local--files.
- Why: P4/T9. A JP theme may not deliver its base from a personal GitHub host or a jsDelivr gh/ path (localize.md section 4 exception list); the campaign's form is to bundle the base as an own fragment and to repoint cross-theme imports to the JP port candidate (owner ruling 1; KB-14, KB-16). Draft-host self-delivery is the sanctioned draft-stage form (KB-41, class (iii)).
- Verify: the self-delivery census passes the FIX-CODEADDR / FIX-NAVLA standard. Counting every code-block form ([[code type="css"]] here), the candidate has four fragments in document order and every address names the block holding the intended CSS: /1 the bundled base layer (801 lines of content, the largest block), /2 the theme's main layer, /3 the daybreak preset, /4 the dendrophobia preset. Every include-parameter gate ({$theme}, {$daybreak}, {$dendrophobia}) sits in render-time page text (the head module and the iftags module are page text, not URL-delivered fragments), so parameter substitution reaches them; the delivery-chain test the parameter-gate family requires is satisfied. The bundled layer's content cannot be byte-verified from this repo (no frozen mirror of fragment:parallel/1's chain exists here); its provenance rests on the porter comment, the original's import at original L766, and the render record.
- Disposition: the ledger's KB-14 line (GOSIGN2-LEDGER L1685) records marchen's Basalt import as FIXED by repoint (FIX4-REPOINT); the (c3) summary line's "delivery class (ii)" phrasing for P4 is a compression that the bytes and L1685 supersede (recorded as a prose-vs-bytes discrepancy in section 11).

## 4. Fonts and assets

none — no signature for this section fired over 142 change blocks.

- What: the skeleton prints none for this section; the label_spans say otherwise. JPFONT-LOAD fires inside B124 and B125. Fragment 2's head loads Noto Serif JP (candidate L1578) where the original loaded Noto Serif SC (original L768), and keeps UnifrakturMaguntia (candidate L1580). The five CSS-BODY singles (B134-B139, section 8's list) are P7 font-stack rewrites riding with that swap: 'Noto Serif SC' becomes 'Noto Serif JP' in five font-family declarations (original L901, L960, L1042, L1060, L1336 to candidate L1711, L1770, L1852, L1870, L2146). The bundled base layer loads Noto Sans SC (candidate L772), the Parallel base's own face, which its stacks name. Assets: every image is re-hosted to the candidate's own local--files (the two image-block specimens, B68 and B27, and the url() set B126-B131), with one exception, the town-background.svg at candidate L2214, whose URL is byte-identical to the original's (original L1404) and is dispositioned in section 11.
- Why: P7 font program (the SC face is the CN glyph form of the same Noto family; the JP face is the posting environment's form) and P5 asset re-hosting.
- Verify: load/apply census. Noto Serif JP: loaded once, applied by the five rewritten stacks and the layer's variables. UnifrakturMaguntia: loaded once, applied. Noto Sans SC: loaded once (bundled layer), applied by the base layer's stacks, which is also the candidate body's --page-font resolution; LOCALIZE-S2-D judged that partial coverage a staff-call observation (pattern 7 TC/SC-equivalent case), and it is not one of the row's two display-affecting findings. No font is named-but-unloaded, no load is duplicated, and no load sits in an inert channel: both loads are in delivered fragments.
- Disposition: T4 pattern 5 APPLIED with the one asset exception dispositioned at P5 (section 11); pattern 7 PARTIAL as a recorded observation.

## 5. Header, sidebar, site furniture

none — no signature for this section fired over 142 change blocks.

- What: the skeleton prints none; the header variables live inside the bundled-layer seam B125 (HEADERVAR fires there). The bundled layer's default :root gives JP header values (candidate L783-788: --title "SCP財団", --subtitle "確保、収容、保護", logo on the candidate's own host), and a :where(:root:lang(cn)) block (candidate L774-779) retains the CN brand strings behind the lang(cn) gate, where they cannot surface on a JP page. Fragment 2's :root converts the GoI title string to Japanese glyph forms (B132: 吟游诗客 to 吟遊詩客, original L833 to candidate L1643) and retains the German slogan string "Märchen erben Fantasien" unchanged (original L834, candidate L1644), an identity string under owner ruling 2. The sidebar surface is item 67's ground and is treated in the per-theme record.
- Why: P9 header variables are the theme's visible title surface; the JP defaults are the posting environment's form, and the lang-gated retention preserves the base component's multilingual structure without exposing CN strings by default.
- Verify: the lang(cn) block is gated by :root:lang(cn) and the ungated :root that follows it carries the JP values, so the cascade on a JP page resolves to the JP strings (LOCALIZE-S2-D pattern 9 records the same reading: kept by design, not counted a defect).
- Disposition: pattern 9 APPLIED with the lang(cn) retention as a recorded observation.

## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B5: orig 238-238 -> cand 243-243 (body -> body)
  - B6: orig 240-240 -> cand 245-245 (body -> body)
  - B11: orig 273-277 -> cand 286-286 (body -> body)
  - B12: orig 279-285 -> cand 288-288 (body -> body)
  - B14: orig 291-291 -> cand 294-294 (body -> body)
  - B16: orig 297-297 -> cand 300-300 (body -> body)
  - B18: orig 303-303 -> cand 306-306 (body -> body)
  - B21: orig 319-319 -> cand 322-322 (body -> body)
  - B22: orig 323-323 -> cand 326-326 (body -> body)
  - B23: orig 327-327 -> cand 330-330 (body -> body)
  - B25: orig 334-334 -> cand 337-337 (body -> body)
  - B28: orig 345-345 -> cand 348-348 (body -> body)
  - B29: orig 349-349 -> cand 352-352 (body -> body)
  - B33: orig 369-369 -> cand 372-372 (body -> body)
  - B35: orig 374-374 -> cand 377-377 (body -> body)
  - B36: orig 376-376 -> cand 379-379 (body -> body)
  - B37: orig 378-378 -> cand 381-381 (body -> body)
  - B38: orig 380-380 -> cand 383-383 (body -> body)
  - B39: orig 382-382 -> cand 385-385 (body -> body)
  - B40: orig 384-384 -> cand 387-387 (body -> body)
  - B41: orig 386-386 -> cand 389-389 (body -> body)
  - B42: orig 388-388 -> cand 391-391 (body -> body)
  - B43: orig 390-390 -> cand 393-393 (body -> body)
  - B44: orig 392-392 -> cand 395-395 (body -> body)
  - B45: orig 394-394 -> cand 397-397 (body -> body)
  - B52: orig 412-412 -> cand 415-415 (body -> body)
  - B53: orig 414-414 -> cand 417-417 (body -> body)
  - B54: orig 423-423 -> cand 426-426 (body -> body)
  - B58: orig 435-435 -> cand 438-438 (body -> body)
  - B59: orig 437-437 -> cand 440-440 (body -> body)
  - B60: orig 439-439 -> cand 442-442 (body -> body)
  - B62: orig 474-474 -> cand 477-477 (body -> body)
  - B64: orig 478-478 -> cand 481-481 (body -> body)
  - B66: orig 482-482 -> cand 485-485 (body -> body)
  - B69: orig 496-496 -> cand 499-499 (body -> body)
  - B70: orig 504-504 -> cand 507-507 (body -> body)
  - B71: orig 512-512 -> cand 515-515 (body -> body)
  - B73: orig 518-518 -> cand 521-521 (body -> body)
  - B75: orig 522-522 -> cand 525-525 (body -> body)
  - B76: orig 527-527 -> cand 530-530 (body -> body)
  - B78: orig 540-540 -> cand 543-543 (body -> body)
  - B79: orig 542-542 -> cand 545-545 (body -> body)
  - B80: orig 544-544 -> cand 547-547 (body -> body)
  - B82: orig 549-549 -> cand 552-552 (body -> body)
  - B84: orig 582-584 -> cand 585-587 (body -> body)
  - B85: orig 596-598 -> cand 599-601 (body -> body)
  - B86: orig 610-610 -> cand 613-613 (body -> body)
  - B87: orig 614-614 -> cand 617-617 (body -> body)
  - B89: orig 621-621 -> cand 624-624 (body -> body)
  - B90: orig 623-623 -> cand 626-626 (body -> body)
  - B92: orig 627-627 -> cand 630-630 (body -> body)
  - B93: orig 630-630 -> cand 633-633 (body -> body)
  - B94: orig 632-632 -> cand 635-635 (body -> body)
  - B95: orig 635-635 -> cand 638-638 (body -> body)
  - B96: orig 640-640 -> cand 643-643 (body -> body)
  - B97: orig 642-642 -> cand 645-645 (body -> body)
  - B100: orig 649-649 -> cand 652-652 (body -> body)
  - B101: orig 654-654 -> cand 657-657 (body -> body)
  - B103: orig 662-662 -> cand 665-665 (body -> body)
  - B104: orig 664-664 -> cand 667-667 (body -> body)
  - B105: orig 668-668 -> cand 671-671 (body -> body)
  - B106: orig 675-675 -> cand 678-678 (body -> body)
  - B107: orig 677-677 -> cand 680-680 (body -> body)
  - B108: orig 679-679 -> cand 682-682 (body -> body)
  - B109: orig 681-681 -> cand 684-684 (body -> body)
  - B111: orig 686-686 -> cand 689-689 (body -> body)
  - B112: orig 688-688 -> cand 691-691 (body -> body)
  - B114: orig 700-700 -> cand 703-703 (body -> body)
  - B121: orig 757-757 -> cand 760-760 (body -> body)
  - B123: orig 763-763 -> cand 766-768 (body -> body)
  - B142: orig 1456-1456 -> cand 2266-2266 (body -> body)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B19: orig 313-313 -> cand 316-316 (body -> body)
  - B26: orig 339-339 -> cand 342-342 (body -> body)
  - B30: orig 353-359 -> cand 356-362 (body -> body)
  - B31: orig 363-364 -> cand 366-367 (body -> body)
  - B32: orig 366-367 -> cand 369-370 (body -> body)
  - B34: orig 371-372 -> cand 374-375 (body -> body)
  - B46: orig 396-396 -> cand 399-399 (body -> body)
  - B47: orig 398-398 -> cand 401-401 (body -> body)
  - B48: orig 400-400 -> cand 403-403 (body -> body)
  - B49: orig 402-402 -> cand 405-405 (body -> body)
  - B50: orig 404-405 -> cand 407-408 (body -> body)
  - B51: orig 407-407 -> cand 410-410 (body -> body)
  - B55: orig 427-429 -> cand 430-432 (body -> body)
  - B56: orig 431-431 -> cand 434-434 (body -> body)
  - B57: orig 433-433 -> cand 436-436 (body -> body)
  - B72: orig 516-516 -> cand 519-519 (body -> body)
  - B77: orig 538-538 -> cand 541-541 (body -> body)
  - B88: orig 619-619 -> cand 622-622 (body -> body)
  - B98: orig 645-645 -> cand 648-648 (body -> body)
  - B99: orig 647-647 -> cand 650-650 (body -> body)
  - B102: orig 660-660 -> cand 663-663 (body -> body)
  - B110: orig 684-684 -> cand 687-687 (body -> body)
  - B113: orig 698-698 -> cand 701-701 (body -> body)
  - B115: orig 702-702 -> cand 705-705 (body -> body)
  - B116: orig 704-704 -> cand 707-707 (body -> body)
  - B117: orig 707-709 -> cand 710-712 (body -> body)
  - B118: orig 715-717 -> cand 718-720 (body -> body)
  - B119: orig 723-725 -> cand 726-728 (body -> body)
  - B120: orig 754-755 -> cand 757-758 (body -> body)
  - B122: orig 761-761 -> cand 764-764 (body -> body)
  - B132: orig 833-833 -> cand 1643-1643 (code-css -> code-css)

- GLYPH-FORM (B): Shinjitai conversion (R5): retained source-language strings converted to Japanese glyph forms; neither translated nor left untouched, and the reviewer must see it separately.
  Verify: Fold-compare the pair; only glyph forms differ.
  - B24: orig 330-330 -> cand 333-333 (body -> body)
  - B140: orig 1392-1392 -> cand 2202-2202 (body -> body)

- What: the translation mass. TRANSLATION-ANCHORED (33 blocks) and TRANS-UNANCHORED (79 blocks, tier C singles resolved in the appendix) cover the full prose body: the theme documentation, the Waldichter GoI excerpt and its specimens, the pagebook / paging / selres usage texts, and every specimen caption, all carried from Chinese to Japanese with no section dropped. GLYPH-FORM fires four times (B24, B116, B132, B140): retained source strings converted to Japanese glyph forms, among them the GoI name (B132, section 5) and the light-preset heading at candidate L2202, whose self-deprecating （？） is the original's own notation (original L1392) kept deliberately. Recorded retentions, all judged observations by LOCALIZE-S2-D: the Chinese proper name 光头强 with a katakana reading note (B142, candidate L2266); the meta-title design string (section 1); the German slogan (section 5).
- Why: P10/T5. Reader-visible text localizes; proper names and identity strings are retained with notes rather than silently rewritten.
- Verify: LOCALIZE-S2-D read the prose in full and found no mechanically detectable untranslated residue; the footnote texts translate with their bodies (five [[footnote]] on each side, section 8).
- Disposition: T5's verdict is FINDINGS jointly with T4, and the two findings are the delivery items of sections 3 and 4; the translation text itself carries no open finding.

## 7. Links

none — no signature for this section fired over 142 change blocks.

- What: no signature fires for this section; the link changes ride inside the translation and credit blocks. Three prose links matter. The Waldichter hub link (candidate L286) is absolutized to the CN original with the （原語版） annotation. The theme:parallel link in the same sentence is absolutized to the CN original without the annotation: the sentence states the original's basis (the CN Parallel), and the candidate's own base relationship is the bundled layer of section 3 rather than an include of theme:parallel-jp, so absolutizing is the right branch and the missing annotation is a notation nit (flag F2 in the per-theme record). The borrowed-code attribution at candidate L760 names plain theme:lumina; that is flag F1.
- Why: prose links follow the snippet audit's classes: a link with a JP counterpart is repointed, a link that specifically means the branch original keeps its target in absolutized, annotated form, and only a link with no counterpart and no such meaning is left as a bare reference.
- Verify: the credit source link is treated in section 1 (recorded host, correct). The two flags carry their probe evidence in the per-theme record.
- Disposition: T4 pattern 11 records the hub and parallel links as allowable outbound references to the originals (LOCALIZE-S2-D, staff-call observations); the lumina link was recorded there as existence-unverified and is resolved by this lane's probe (per-theme record).

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B20: orig 315-315 -> cand 318-318 (body -> body)
  - B27: orig 342-342 -> cand 345-345 (body -> body)

- CSS-BODY (C): Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.
  Verify: Writer review; a recurring shape is a new-signature candidate for the patterns loop.
  - B134: orig 901-901 -> cand 1711-1711 (code-css -> code-css)
  - B135: orig 960-960 -> cand 1770-1770 (code-css -> code-css)
  - B136: orig 1042-1042 -> cand 1852-1852 (code-css -> code-css)
  - B137: orig 1060-1060 -> cand 1870-1870 (code-css -> code-css)
  - B139: orig 1336-1336 -> cand 2146-2146 (code-css -> code-css)

- What: the structural delta is the delivery restructure of section 3 (one code block added; the theme's own fragments renumbered). The two EXHIBIT-RESTRUCTURE blocks are false fires adjudicated here: B20 is a one-line include repoint inside the usage text (section 2) and B27 is the image-block re-host (section 4); the exhibit census is unchanged, and every exhibit the original carries (theme-squares, movie specimen, pagebook, paging, portable-toc, the five selres parts, the warning specimen) is present in the candidate with its parameters intact. The CSS-BODY blocks (B134-B139) are the P7 stack rewrites assigned to section 4. Content presence: both CSS variant modules (daybreak, dendrophobia) survive as fragments 3 and 4 (section 3 measurements); the documentation bodies translate in full (section 6); the file has five [[footnote]] on each side and no [[footnoteblock]] on either side, the original's own shape, so nothing was dropped or escaped there.
- Why: structure changes are limited to the delivery composition the base-bundling requires; exhibits and gated modules are content, and the campaign standard is that documented mechanisms keep their definitions.
- Verify: the gated exhibits were compared form by form: the pagebook gates ({$pagebook-start}, {$paging}, {$pagebook-end}, {$portable-toc}, {$selres-part1..5}) open and close at the same points in render-time text on both sides, and the variant gates sit in the head and iftags modules as the original has them.
- Disposition: no structural finding; the restructure is the K5b-3 composition recorded in section 0.

## 9. Formatting only

- WS-ONLY blocks: 3
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

- What: three WS-ONLY blocks (B133, B138, B141), whitespace-only deltas inside the shifted fragments, and the one-byte trailing-space delta measured in section 3. No re-indentation pairs.
- Why: formatting-only changes carry no mechanism.
- Verify: the classifier's WS-ONLY set is the whole of this section; the brace-depth scan (section 12) confirms no whitespace delta displaced a brace.
- Disposition: none required.

## 10. Porter annotations

none — no signature for this section fired over 142 change blocks.

- What: one porter annotation, B123: the comment at candidate L768 states that the base component "Parallel" (by Dr Hormress, CC BY-SA 3.0) is bundled from fragment:parallel/1 and that the original referenced that fragment by @import from scp-wiki-cn. It is the package's TASL record for the bundled layer, and it is accurate against the bytes: fragment 1 exists as described, and the original's import stands at original L766. The remaining [!-- --] comments in the file are the original's include-parameter gate markers, mechanism rather than annotation.
- Why: a bundled third-party base requires its attribution to travel with the code (owner ruling 3's TASL standard).
- Verify: read candidate L766-772 against original L765-770; the comment's two claims (bundling, the original's remote reference) both check out.
- Disposition: annotation stands as the layer's attribution record; no other porter annotation exists in the file.

## 11. Dispositions and exceptions

- No derived presence label fired.

- Item 67 [F] is restated and re-derived in the per-theme record; its ground (original-identical toggle rules) holds exactly on this package's bytes.
- P4 (delivery): the finding was closed by the FIX4-REPOINT repoint, not retained as original-state delivery. The ledger (c3) line at GOSIGN2-LEDGER L1590 compresses it as "DISPOSITIONED (delivery class (ii))", while the ledger's own KB-14 line (L1685) records the repoint and the current bytes confirm it (no jsDelivr reference remains anywhere in the candidate). This package follows the bytes and L1685; the (c3) phrasing is recorded here as a prose compression, not a ground.
- P5 (assets): the town-background.svg URL (candidate L2214) is byte-identical to the original's (original L1404), an original-state delivery retained inside a preset fragment; DISPOSITIONED class (ii) / KB-58 per the ledger row. The checker still flags it as a hotlink (section 12); the disposition is the campaign's recorded answer for original-state asset URLs.
- Pattern 7 partial coverage (the body stack's Noto Sans SC resolution, section 4) and the :root:lang(cn) retention (section 5) are LOCALIZE-S2-D staff-call observations, retained by design.
- Credit notation nits (section 1) are a campaign-wide class recorded by LOCALIZE-S2-D.
- The sample page's credit-modal errors are the preview form's property (credit:start-preview has no modal mechanism; owner ruling 5), and the row's page-overflow figures (435px chromium / 436px webkit) are the cross-cutting static-credit width family (KB-33).
- Draft-host forms throughout (own local--code and local--files on sigma10-jp-test.wdfiles.com) are class (iii) draft-stage forms (KB-41), rewritten at posting.

## 12. Verification

- Package integrity: original.txt sha256 equals the sources.tsv mirror hash (4f2309705c20aa37636d7f1b5c6ce6947a8f849becc0494da3e286f2f613a9e9); candidate.txt is byte-identical to the canonical pages/theme:marchen-jp.txt (cmp, no output).
- Item 67 re-measurement: candidate L1675-1703 and original L865-893 are byte-identical (861 bytes, sha256 9544c708173e51f6b2b12267a6b2a112879d9b95378b3e1cd70f1290aae8ad2a on both sides); the extended sidebar-surface census is in the per-theme record.
- Shifted-fragment measurements: section 3 (fragment 4 byte-identical, fragment 3 one byte over 1,467).
- Brace depth: a depth scan over all four candidate code blocks ends at depth 0 in each, minimum 0; the original's three blocks likewise. No displaced-brace shape.
- T1 checker (check_source.py --kind theme --translation, run by this lane 2026-11-17 on the canonical file): error 17 / warn 0 / info 1. The 17 errors are 15 pseudo-ref (draft-host references, class (iii)) and 2 hotlink: candidate L2214 (the dispositioned town-background.svg, section 11) and candidate L311, which is the placeholder url(https://...) inside the @@-escaped usage exhibit, an exhibit specimen the original carries in the same form, not a delivery reference. FIX5-FUNC recorded 17 / 1 / 1 at its run; the T1 baseline in the stamp (19 errors) predates the FIX4 repoint, which removed the two jsDelivr hotlinks.
- build_review.py --check: this package is not in the stale set (acceptance run recorded in the batch report).

## Per-theme record — FIX5 item re-derived

### Item 67 [F] — DISPOSITIONED (FIX5-FUNC section 2, no edit)

The blocking item: at WebKit 1366x768 the hamburger open control is present but inert on both measured pages (the candidate page and its sample); Chromium opens the sidebar, and mobile widths open in both engines (RENDER-ROWS-RERUN16 (CN9), recorded in GOSIGN2-LEDGER section (e) item 67). The FIX5 ground: the toggle rules are the original's own, unchanged by the port, so the failure is an engine-specific rendering of an original-identical mechanism, confined to one engine at one viewport.

Re-derivation from this package's bytes. FIX5-FUNC cited candidate L1675-1678 (the .open-menu rule) and L1700-1703 (the @media (max-width: 1024px) override) against original L865-868 and L890-893, with the full window diffed IDENTICAL. Measured here on the whole window: candidate L1675-1703 and original L865-893 are byte-identical, 861 bytes, sha256 9544c708173e51f6b2b12267a6b2a112879d9b95378b3e1cd70f1290aae8ad2a on both sides. The check was then widened past the cited window: every CSS rule whose selector names the sidebar surface (open-menu, mobile-top-bar, side-bar, top-bar) was extracted from both files. The original has 8 such rules; all 8 are present in the candidate byte-identically (selector and declarations). The candidate has 4 further rules of that surface, all inside the bundled base layer (fragment 1), and none of them touches the toggle mechanism (no visibility, display, transform, or positioning declaration on the open-menu control or the drawer). No toggle markup, breakpoint, or z-index was changed anywhere in the port.

Second-reviewer walk. The ground is stated in terms a reader who did none of the work can check from this package alone: the two windows sit in original.txt and candidate.txt, and the hashes above either match or they do not. The engine half of the ground (the failure is confined to WebKit at 1366, with mobile widths opening in both engines) rests on the RERUN16 render record rather than on package bytes, and it is cited by record name in the stamp. A fix would have to alter CSS that is byte-identical to the original, departing from the original to chase one engine's handling of it, with no candidate-side cause anywhere in the delivery chain. The disposition stands.

### Defect flags (candidate not edited by this lane)

- F1 (minor): candidate L760, the borrowed-code attribution sentence names plain [[[theme:lumina|Lumina]]]. theme:lumina does not exist on SCP-JP production (probe of https://scp-jp.wikidot.com/theme:lumina returned 404, 2026-11-17), and no campaign page posts under that name. The sentence credits the EN original work, so the population remedy is the annotation branch (absolutize to the EN original with the （原語版） annotation, the treatment the same file gives the Waldichter hub link at candidate L286), not a repoint to theme:lumina-jp. LOCALIZE-S2-D recorded the link as existence-unverified; the probe resolves it.
- F2 (notation): candidate L286, the theme:parallel prose link is absolutized to the CN original (the right branch, section 7) but carries no （原語版） annotation, where the hub link in the same sentence carries one.

### Sources.tsv note correction (for the coordinator's harvest)

The marchen row's note claims the original was "superseded upstream since the reference revision". Its own cited artifact (gosign2-lanes/lane-oc-gs-localize-s2-D/diff-marchen-from35.txt) records scp-wiki-cn theme:marchen rev 35 to rev 35, no changes, no intervening revisions. The correct form: "Upstream latest remains rev 35; the S2 artifact records rev35 to rev35, no changes; follow-up diff artifact diff-marchen-from35.txt in the campaign record (K5a-i)".

## Appendix — residue and heuristic blocks

The 75 heuristic blocks are translation mass in two shapes, plus the font-stack lines and two seams; the single residue block is an include repoint the signature could not see. Each is assigned here.

- 69 TRANS-UNANCHORED tier-C blocks (B5, B6, B11, B12, B14, B16, B18, B21-B23, B25, B28, B29, B33, B35-B45, B52-B54, B58-B60, B62, B64, B66, B69-B71, B73, B75, B76, B78-B80, B82, B84-B87, B89, B90, B92-B97, B100, B101, B103-B109, B111, B112, B114, B121; original L237-757 to candidate L242-760, body to body): one-line and short-group prose and specimen translations whose line shape changed in translation (script delta without the anchor majority). Assigned to section 6.
- B134-B139 (original L900-1336 to candidate L1710-2146, code-css): the five P7 font-stack rewrite lines. Assigned to section 4.
- B142 (original L1455-1456 to candidate L2265-2266): the retained Chinese proper-name line with its reading note. Assigned to section 6.
- B81 (residue; original L547 to candidate L550): the first line of the multi-line selres include, repointed like its single-line siblings; the signature missed it because the include spans lines. Assigned to section 2.
- B123 and B125 are tier A/B seams rather than appendix mass: the porter annotation (section 10) and the bundled-layer seam carrying the HEADERVAR, JPFONT-LOAD, COMMENT-TEXT, and CONTENT-STRING labels (sections 3, 4, 5).
