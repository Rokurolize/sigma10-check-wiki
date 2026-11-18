# Review package — theme:minimalist-bhl-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:minimalist-bhl-jp — origin EN, population #21 [GOSIGN2-LEDGER (b) row 21]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2f464b3dfae9a5209292e84cedae5c1986597f6a25e084e4bce3f4cd3c6a04a8); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 3 infos (http×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 21; GOSIGN2-LEDGER (b) row 21]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — §15/parallel panel body near-black-on-black unreadable (theme-specific), sample credit-modal, SP overflow 337–419px, CSS load aborted at chromium-375. [RENDER-ROWS-1 (RENDER-B row 21)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-B row 21)]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 21, source LOCALIZE-A]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 21]
- FIX5 re-judgement: item 2 (class E) DISPOSITIONED — FIX5-CONTRB (no edit, no commit): --dark-accent / --swatch-text-general rgb(36,36,36) identical to original rev 107; candidate-side fallbacks touch only credit-button, search and author-link furniture [GOSIGN2-LEDGER-SUPPLEMENT (a) item 2]
- Computed against: canonical commit 1f846a6a8462d9654ff916968145490cdefd4522; candidate file pages/theme:minimalist-bhl-jp.txt sha256:2f464b3dfae9a5209292e84cedae5c1986597f6a25e084e4bce3f4cd3c6a04a8; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (R-disp-8 lane, 2026-11-17)
Candidate: review/minimalist-bhl-jp/candidate.txt (sha256 91ccb1df6404953f2b18a911ea683c71c941a994d4a332808aa0bdbc02258e68)
Original: theme:minimalist-bhl — scp-wiki, revision 107 (sha256 d076f29e54167c0adc56808ccce19a17511162997bd4816470cb34812a7e282a)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (generated stamp) | Notes |
|---|---|---|
| T1 source check | FINDINGS (classified) | 3 errors / 1 warn / 3 infos (http x2, pseudo-ref x1); this lane's run on the current file reproduces the baseline exactly (section 12) |
| T2/T3 render | FINDINGS | The section-15 panel finding is FIX5 item 2, re-derived in the per-theme record; sample credit-modal is the preview form; the rest dispositioned in register (c2) |
| T4/T5 localize/translation | PASS | 0 display-affecting findings [LOCALIZE-A] |
| FIX5 item 2 [E] | DISPOSITIONED (FIX5-CONTRB section 2, no edit) | Re-derived on this package's bytes in the per-theme record; the ground holds exactly |
| Overall stamp | STALE | The candidate changed after the verdict bytes by exactly one snippet-audit line (section 11); the stamp is not carried over, per the standing doctrine |

## Provenance

| | |
|---|---|
| Original | theme:minimalist-bhl, scp-wiki, revision 107 (re-translation reference revision; first translation at revision 104) |
| Mirror | review-mirrors/orig-minimalist-bhl-rev107.txt, class FETCH-REGEN, sha256 d076f29e54167c0adc56808ccce19a17511162997bd4816470cb34812a7e282a (equals the sources.tsv value) |
| Candidate | pages/theme:minimalist-bhl-jp.txt, sha256 91ccb1df6404953f2b18a911ea683c71c941a994d4a332808aa0bdbc02258e68 |
| Production counterpart | theme:minimalist-bhl on SCP-JP (pages-existing/existing:theme-minimalist-bhl.txt); the migration delta over production is recorded on pages/phase17-diff-minimalist-bhl-jp.txt |
| Kind | K6: the production page is a third source; provenance route R4 production adoption (section 0) |

## Summary

Minimalist BHL is an EN Black Highlighter variant by JakdragonX and Pedagon. The JP side already had a production page, translated from revision 104; the candidate adopts that production page (route R4) and brings it to the campaign standard and to revision 107: the credit block is completed to the full field set with both reference revisions recorded, the usage exhibits are escaped, the self-delivery addresses are repointed to the candidate's own page name, three undefined-variable fallbacks and an image-caption merge are applied (the delta the phase17-diff page documents), and three small JP correction modules are appended. The theme's one blocking item (item 2, class E) was dispositioned without an edit because the near-black panel text value is the original's own palette, byte-identical in the candidate; that ground is re-measured in the per-theme record and holds exactly. One defect is flagged there: the candidate escapes its [[footnoteblock]] although it carries two live footnotes, where both the original and the production page keep the block live.

## Class summary

| Label | Blocks |
|---|---|
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 3 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 5 |
| HEADERVAR | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 5 |
| INFO-DEL | 2 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 3 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 22 |
| TRANSLATION-ANCHORED | 19 |
| WS-ONLY | 7 |

Counts: 68 blocks, 44 specific, 21 heuristic, 3 residue, 0 skipped (comment text).

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.
- Production-adoption signal: candidate resembles the production JP counterpart at 0.98 similarity vs 0.87 for the original (R4); declaration is a slot below.

The provenance route is R4 production adoption. The classifier's signal is explicit: the candidate resembles the production JP counterpart at 0.98 similarity against 0.87 for the original. The candidate is the production page (pages-existing/existing:theme-minimalist-bhl.txt, the SCP-JP page translated from revision 104 by walksoldi in 2023) carried into the campaign's posting form and updated to the re-translation reference revision 107; the migration delta over production is itself a campaign record, pages/phase17-diff-minimalist-bhl-jp.txt, whose three hunks (the added re-translation revision field, the image-caption merge, and the three variable fallbacks) all check out against the candidate's bytes in sections 1 and 8. The candidate-versus-production differences beyond that record are enumerated and adjudicated in the per-theme record; they are the credit completion, the exhibit escaping, the storage URL form, the self-delivery repoint, the appended correction modules, and one defect (the escaped footnoteblock).

## 1. Credit and attribution

- INFO-DEL (A): Info-module residue removed (P3, ledger class C): the old info module pair is not part of the JP environment's furniture.
  Verify: Grep the candidate for info:start / info:end includes; none may remain.
  - B7: orig 17-20 -> cand at 21 (body -> body)

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B8: orig 22-25 -> cand 22-33 (body -> body)

- T7-CREDIT-CSS (B): Credit-module CSS supplement (T7, KB-11/KB-12/KB-62): the JP credit module's DOM needs rules the branch original never shipped, or its inherited rules corrected in place.
  Verify: KB-11/KB-12 recipes: confirm the selectors in the candidate and whether the production counterpart carries them (supplement vs inherited).
  - B56: orig 431-431 -> cand 437-437 (code-css -> code-css)
  - B57: orig 439-439 -> cand 445-445 (code-css -> code-css)
  - B68: orig at 877 -> cand 883-899 (body -> body)

- What: the EN info module is removed (INFO-DEL: B7 takes out info:start, and B8 pairs info:end with the replacement) and the candidate carries the preview credit form at candidate L22-33 with the full field set: title （ミニマリストBHLテーマ), translator (walksoldi), translation year (2023), original title, author and holder fields (JakdragonX, Pedagon), creation year (2021), and both reference revisions （初訳 104 / 改訳 107), the only dual-revision field set the two recorded reference revisions require, plus the source link. Against production, whose credit form was shorter, the candidate completes the field set (the production page had no translator, holder, revision, or source-link fields); the phase17-diff page records the added re-translation revision line. The author field drops production's [[*user]] links and keeps the bare names with the copyright mark, a notation delta; the names themselves are present.
- Why: P3/T1. The info module is not part of the JP environment's furniture; the preview credit is the rate-bearing JP form (KB-09, KB-11, KB-12 at patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa).
- Verify: the holder and author fields name JakdragonX and Pedagon, the co-authors the original's info block names (original L20: "co-rewritten by [[*user JakdragonX]] and [[*user Pedagon]]"), so there is no pointer-instead-of-author defect. The source link's host is scp-wiki.wikidot.com, the host sources.tsv records. One attribution line does not survive: the original's acknowledgment (original L22, thanking stormbreath for inspiration and Woedenaz and EstrellaYoshte for their help) is absent from the production page and from the candidate alike; it is a production-side omission the R4 adoption inherited, recorded here because a reviewer comparing the info block will notice it. The theme's creators are credited; the line names contributors, not authors. The T7-CREDIT-CSS blocks are adjudicated where they belong: B56 and B57 are link-selector rules (section 7), and B68 is the appended correction modules (sections 8 and 10), one of which is a credit-dialog correction.
- Disposition: T4/T5 PASS for this theme (LOCALIZE-A); the credit form matches the campaign standard.

## 2. Includes and components

- IFTAGS (A): Tag localization (P2/T2, KB-08): iftags conditions use JP tag names in the JP environment.
  Verify: KB-08 recipe: every iftags condition names JP tags; a bare [[iftags]] line is an anomaly.
  - B1: orig 1-1 -> cand 1-5 (body -> body)

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B9: orig 27-29 -> cand 35-37 (body -> body)

- What: B1 restructures the head gates into the production form: a bare [[iftags]] frame (candidate L1-3) carrying the base include [[include :scp-jp:theme:black-highlighter-theme]], then the body gate [[iftags +テーマ]] (candidate L5). The base include is the ruling-1 repoint of the original's :scp-wiki:theme:black-highlighter-theme. B9 (COMPONENT-SWAP) is the usage snippet pair: the two includes the original shows live in a blockquote (original L28-29) are repointed to :scp-jp: and the self-name gains the -jp suffix, and in the candidate they are @@-escaped exhibits (candidate L36-37) where both the original and production leave them live. B3 and B5, labeled EXHIBIT-RESTRUCTURE, are the two head interwiki-style includes repointed to :scp-jp:component:interwiki-style; the label is a false fire, since these are delivery includes, not exhibits. B64 and B66 are the tail furniture includes (centered-header-bhl, toggle-sidebar-bhl) repointed the same way.
- Why: P2/T2 for the tag name (KB-08); ruling 1 for the base (the JP port of the original's BHL base is the mandated base, and FIX5-CONTRB records that this is not a candidate-side base swap); the exhibit escaping is the posting form for code a reader copies.
- Verify: the bare [[iftags]] frame is KB-08's anomaly form, but it is byte-identical to the production page's frame, an inherited production structure rather than a port-introduced one; the +テーマ gate carries the theme body as the original's +theme gate did. Every include in the original has its repointed counterpart in the candidate (census in section 8).
- Disposition: includes and components stand as the production form plus the campaign repoints; no finding.

## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B2: orig 3-4 -> cand 7-8 (module-css -> module-css)
  - B4: orig 9-9 -> cand 13-13 (body -> body)
  - B6: orig 14-14 -> cand 18-18 (body -> body)
  - B65: orig 871-871 -> cand 877-877 (module-css -> module-css)
  - B67: orig 875-875 -> cand 881-881 (body -> body)

- What: one code block on each side (original L144-865, candidate L151-871) carries the theme's whole CSS, delivered as the page's own fragment 1. The head module's two @imports (B2, original L3-4 to candidate L7-8) are repointed from the EN BHL project's host (nu-scptheme.github.io/Black-Highlighter) to the JP BHL project's host (scp-jp.github.io/Black-Highlighter). The tail delivery (B65, B67): the closing [[module css]] @import and the priority-3 interwiki-style theme= address name the candidate's own fragment on the draft host (candidate L877, L881), repointed from production's addresses, which name the production page's own fragment on scp-jp.wdfiles.com; the original's tail names its own fragment on scp-wiki (original L871). The base theme itself arrives through the frame include of section 2.
- Why: P4/T9 and ruling 1: the JP BHL project host is the base's home in this environment, and a candidate's self-delivery must name its own page, in the sanctioned draft-host form (KB-41, class (iii)).
- Verify: the self-delivery census passes the FIX-CODEADDR standard: exactly one code block exists in the file (counting every [[code]] form; the [[module CSS]] blocks are not fragments), so fragment /1 is the stylesheet, and both tail addresses name it. No include-parameter gate sits inside the URL-delivered fragment; the file's gates are the render-time frames of section 2, so the delivery-chain test is satisfied trivially.
- Disposition: delivery stands; the draft-host form is a class (iii) posting rewrite.

## 4. Fonts and assets

none — no signature for this section fired over 68 change blocks.

- What: neither file loads a font: the BHL base supplies the faces, and the theme's own showcase prose names Poppins and Recursive with fonts.google.com specimen links on both sides. The one image (B12) is re-hosted: the original's EN-hosted Ar6AfDt.webp (original L41) becomes the JP storage PNG (candidate L49), and the header logo variable is re-hosted the same way (section 5). The candidate writes both storage URLs in the http scheme with the colon percent-encoded, where production writes https with a raw colon; that is the T1 http class treated in section 11.
- Why: P5 asset re-hosting (the file must not depend on the EN wiki's file host at posting).
- Verify: no @import or @font-face exists in either file outside the self-delivery and base imports of section 3, so there is no named-but-unloaded face, no duplicated load, and no load in an inert channel inside this file; the stacks that consume the base's faces are the base's own.
- Disposition: T4 pattern 5 stands as applied; the URL scheme form is dispositioned with the T1 classes in section 11.

## 5. Header, sidebar, site furniture

- HEADERVAR (A): Header/title variables (P9/T6, KB-57): the header text variables are the theme's visible title surface.
  Verify: KB-57: where the value stays in the original's language, the disposition is ruling 2 (section 11).
  - B10: orig 31-36 -> cand 39-44 (body -> body)
  - B50: orig 155-157 -> cand 162-164 (code-css -> code-css)

- What: HEADERVAR fires twice. B10 is the usage specimen for header editing: the placeholder strings localize ("title here" to ここにタイトル, "subtitle here" to ここにサブタイトル, "your url here" to ここにURL). B50 is the delivered :root defaults (original L155-157 to candidate L162-164): --header-title "SCP財団" and --header-subtitle "確保 - 収容 - 保護" replace the EN defaults, and --logo-image is re-hosted to JP storage. The top-bar furniture also gains the appended label module of section 8 (labels kept whole at narrow widths).
- Why: P9/T6: the header variables are the theme's visible title surface, and the JP defaults are the posting environment's form of the site name and motto (identity strings, whose JP forms are the population standard).
- Verify: the defaults sit in the delivered fragment's :root, not in an exhibit; the specimen placeholders sit in the escaped usage exhibit and match it form for form.
- Disposition: no finding; T4/T5 PASS covers this surface.

## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B13: orig 43-43 -> cand 51-51 (body -> body)
  - B14: orig 45-45 -> cand 53-53 (body -> body)
  - B15: orig 47-47 -> cand 55-55 (body -> body)
  - B23: orig 71-71 -> cand 79-79 (body -> body)
  - B25: orig 76-76 -> cand 84-84 (body -> body)
  - B27: orig 81-81 -> cand 89-89 (body -> body)
  - B28: orig 83-83 -> cand 91-91 (body -> body)
  - B29: orig 85-85 -> cand 93-93 (body -> body)
  - B30: orig 87-87 -> cand 95-95 (body -> body)
  - B31: orig 89-89 -> cand 97-97 (body -> body)
  - B32: orig 91-91 -> cand 99-99 (body -> body)
  - B33: orig 93-93 -> cand 101-101 (body -> body)
  - B34: orig 95-95 -> cand 103-103 (body -> body)
  - B35: orig 97-97 -> cand 105-105 (body -> body)
  - B36: orig 99-99 -> cand 107-107 (body -> body)
  - B37: orig 101-101 -> cand 109-109 (body -> body)
  - B44: orig 117-119 -> cand 125-127 (body -> body)
  - B45: orig 121-127 -> cand 129-135 (body -> body)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B16: orig 51-52 -> cand 59-60 (body -> body)
  - B17: orig 54-54 -> cand 62-62 (body -> body)
  - B18: orig 56-56 -> cand 64-64 (body -> body)
  - B19: orig 58-58 -> cand 66-66 (body -> body)
  - B20: orig 60-60 -> cand 68-68 (body -> body)
  - B21: orig 62-62 -> cand 70-70 (body -> body)
  - B22: orig 68-69 -> cand 76-77 (body -> body)
  - B24: orig 73-74 -> cand 81-82 (body -> body)
  - B26: orig 78-79 -> cand 86-87 (body -> body)
  - B38: orig 103-103 -> cand 111-111 (body -> body)
  - B39: orig 105-105 -> cand 113-113 (body -> body)
  - B40: orig 107-107 -> cand 115-115 (body -> body)
  - B41: orig 109-109 -> cand 117-117 (body -> body)
  - B42: orig 111-111 -> cand 119-119 (body -> body)
  - B43: orig 113-113 -> cand 121-121 (body -> body)
  - B46: orig 129-131 -> cand 137-139 (body -> body)
  - B47: orig 134-136 -> cand 142-144 (body -> body)
  - B49: orig 143-143 -> cand 150-150 (body -> body)

- What: TRANSLATION-ANCHORED (19 blocks) and TRANS-UNANCHORED (22 blocks, tier C singles resolved in the appendix) cover the documentation body the production page had already translated: the introduction, the usage instructions, the element specimens, and the font showcase. The candidate inherits that translation through the R4 adoption; its own translation-layer delta against production is nil outside the credit completion. Two features deserve a reviewer's eye. The translator's-note footnote (candidate L133, on the tearable/terrible pun) is the JP edition's own annotation, present in production identically; it is a live footnote, which matters for flag F1 in the per-theme record. The code-display collapsible retains one EN specimen sentence ("The monospace font is Recursive.") inside the theme-code display, the production-inherited bilingual specimen structure, present in production in the same form.
- Why: P10/T5, judged PASS by LOCALIZE-A with zero display-affecting findings.
- Verify: the T4/T5 row is a PASS, and the candidate-versus-production diff (per-theme record) shows no prose line changed by the migration outside the credit block and the footnote's author-link notation (section 1's family).
- Disposition: PASS stands.

## 7. Links

none — no signature for this section fired over 68 change blocks.

- What: the two T7-CREDIT-CSS blocks belong here. B56 and B57 are the #page-content link-selector rules (original L431, L439 to candidate L437, L445): the candidate drops the EN-host full-URL exclusions (the scp-wiki.wikidot.com classification-committee-memo and anomaly-classification-system-guide URLs) in favour of path-form exclusions and adds a :not(.cc) exclusion. This is exactly the selector-set delta FIX5-CONTRB recorded (scp-wiki URLs removed from link selectors, .cc exclusion added, none touching panels). The remaining links are specimens: the google.com example link (candidate L53, http, the original's own specimen retained in form) and the fonts.google.com specimen links of the showcase. The credit source link is treated in section 1 (recorded host, correct).
- Why: the link rules must not key on the branch wiki's absolute URLs in the JP environment; the path forms match the same pages on any host.
- Verify: the operative link colours are untouched (the colour census of section 12 covers the palette window; the selector change is in the exclusion list only).
- Disposition: recorded as a localization delta by FIX5-CONTRB; no finding.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B3: orig 7-7 -> cand 11-11 (body -> body)
  - B5: orig 12-12 -> cand 16-16 (body -> body)
  - B12: orig 41-41 -> cand 49-49 (body -> body)
  - B64: orig 868-869 -> cand 874-875 (body -> body)
  - B66: orig 873-873 -> cand 879-879 (body -> body)

- CSS-BODY (C): Unclassified CSS content change: CSS churn with no mechanism signature; kept visible and counted rather than silently passed.
  Verify: Writer review; a recurring shape is a new-signature candidate for the patterns loop.
  - B59: orig 603-603 -> cand 609-609 (code-css -> code-css)
  - B60: orig 841-841 -> cand 847-847 (code-css -> code-css)
  - B63: orig 862-862 -> cand 868-868 (code-css -> code-css)

- What: the EXHIBIT-RESTRUCTURE blocks (B3, B5, B12, B64, B66) are the repoints and re-host of sections 2 to 4; the exhibit census is unchanged and every original exhibit is present. The CSS-BODY blocks are the migration's documented repairs. B59, B60, B63 are the three undefined-variable fallbacks the phase17-diff page records: .creditButton p a gains var(--black-accent, var(--dark-accent)) (candidate L609, original L603 without the fallback), the search input gains var(--light-accent, var(--pale-accent)) (candidate L847, original L841), and the author-block link gains var(--linkColour, var(--link-color)) (candidate L868, original L862). The names on the left are EN-BHL variables the JP base renames; the fallbacks keep the rules working on the JP base. The same record's caption hunk folds the image-caption colour declaration into the parent rule and deletes the separate >p rule (candidate L713-720 zone). B68 appends three small [[module CSS]] correction modules at the file's end (candidate L884-899): a history-form mobile grid fix, a credit-dialog back-link no-wrap fix, and a top-bar label word-break fix, appended per the localize closing rule for JP-side corrections. None of the three carries a colour declaration. Residue B48 is the escaped footnoteblock, flag F1 in the per-theme record.
- Why: the fallbacks and the caption merge are the rev 104 to rev 107 migration's own documented delta (the phase17-diff page is their record); the appended modules are environment corrections of the kind the closing rule sanctions.
- Verify: each fallback line was compared against the original's line at the cited numbers, and the phase17-diff hunks reproduce exactly these three lines plus the caption merge. The footnoteblock flag's evidence is in the per-theme record.
- Disposition: the structural deltas stand as the documented migration; the footnoteblock escape is flagged, not dispositioned.

## 9. Formatting only

- WS-ONLY blocks: 7
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

- What: seven WS-ONLY blocks (B51-B54, B58, B61, B62), whitespace normalisation inside the code block (tabs to spaces over several lines, the normalisation FIX5-CONTRB noted in its colour-declaration diff). No re-indentation pairs.
- Why: formatting only; no mechanism.
- Verify: the palette window of section 12 is byte-identical across the same region, so the normalisation touched no declaration value; the brace-depth scan (section 12) ends at depth 0.
- Disposition: none required.

## 10. Porter annotations

none — no signature for this section fired over 68 change blocks.

- What: the porter annotations in this file are the three English comments heading the appended correction modules (candidate L885, L892, L897: "SCP-JP Wikidot page history: ...", "SCP-JP Wikidot BHL credit otherwise correction: ...", "SCP-JP Wikidot minimalist-bhl top bar labels: ..."). Each states exactly what its module does, and each checks out against its module body (a mobile history-form grid rule, a credit back-link white-space rule, a top-bar word-break rule). The migration's external annotation is the phase17-diff page in this repo (pages/phase17-diff-minimalist-bhl-jp.txt), which documents the delta the candidate embodies.
- Why: appended corrections must say what they are; these do, and the migration delta has its own record page.
- Verify: read candidate L884-899; the comment-to-rule correspondence is one to one.
- Disposition: annotations stand; no annotation in the file states anything the bytes refute.

## 11. Dispositions and exceptions

- No derived presence label fired.

- Item 2 [E] is restated and re-derived in the per-theme record; its ground (the original-identical palette) holds exactly on this package's bytes.
- T1 classes: the two http errors (candidate L49, L164) are the register (c1) class (ii) scheme findings; production writes the same two URLs as https with a raw colon, so the candidate's form is a posting-form delta to note, and the checker's storage-host infos record that the wikidot.com host form redirects. The pseudo-ref error (candidate L877) is the class (iii) draft-host self-delivery. The interwiki-touched warn (candidate L774) records that a guarded selector region differs from the EN module's; the change there is inside the theme's own code block (the link-selector localization of section 7), not in the interwiki module itself.
- The bare [[iftags]] base frame (section 2) is production-identical, an inherited structure.
- The sample credit-modal errors are the preview form's property (owner ruling 5).
- The stamp's STALE overall is the standing doctrine, not a finding against the theme: the candidate changed after the verdict bytes by one line, the snippet audit's repoint of the usage exhibit's self-include to theme:minimalist-bhl-jp (commit 358955e), so the PASS-era verdict is not carried over and the generated stamp says so. No re-judgement is fabricated here; the frozen ledger remains the verdict record for the bytes it judged.

## 12. Verification

- Package integrity: original.txt sha256 equals the sources.tsv mirror hash (d076f29e54167c0adc56808ccce19a17511162997bd4816470cb34812a7e282a); candidate.txt is byte-identical to the canonical pages/theme:minimalist-bhl-jp.txt (cmp, no output).
- Item 2 re-measurement: the palette window (original L158-190, candidate L165-197) is byte-identical, 1,473 bytes, sha256 ebc52eb038e0113a0a77b869d432b8459eb731a904830984b264f2c566cd5440 on both sides; the three fallback lines stand at candidate L609, L847, L868 against original L603, L841, L862; the word "panel" occurs zero times in each file.
- Candidate-versus-production census: the full diff between candidate.txt and pages-existing/existing:theme-minimalist-bhl.txt was enumerated line by line; every hunk is adjudicated in sections 0, 1, 2, 4, 8, or the per-theme record (credit completion, exhibit escapes, storage URL form, the phase17-diff deltas, the self-delivery repoint, the appended modules, the footnoteblock escape).
- Brace depth: the single code block ends at depth 0 on both sides, minimum 0. No displaced-brace shape.
- T1 checker (check_source.py --kind theme --translation, run by this lane 2026-11-17 on the canonical file): error 3 / warn 1 / info 3, identical to the T1 baseline in the stamp and to FIX5-CONTRB's run.
- build_review.py --check: this package is not in the stale set (acceptance run recorded in the batch report).

## Per-theme record — FIX5 item re-derived

### Item 2 [E] — DISPOSITIONED (FIX5-CONTRB section 2, no edit)

The blocking item: on the shared sample, the section-15 / parallel panel body text renders near-black on black and is effectively unreadable; the render lane recorded it as theme-specific, the same mechanism as KB-28 (a port-introduced variable binding is what KB-28 charges). The FIX5 ground: the rendered colour is the theme's own --dark-accent value, and both the value and the text binding that consumes it are identical to the original at revision 107, so there is no port-introduced binding to correct; the candidate-side supplements do not touch the charged surface.

Re-derivation from this package's bytes. The operative declarations: --dark-accent: 36, 36, 36 at original L161 and candidate L168; --swatch-text-general: var(--dark-accent) at original L175 and candidate L182 (with --swatch-text-light bound the same way at original L174, candidate L181). Widened past the cited lines: the whole palette window, original L158-190 against candidate L165-197, is byte-identical, 1,473 bytes, sha256 ebc52eb038e0113a0a77b869d432b8459eb731a904830984b264f2c566cd5440 on both sides, so every colour declaration in the region the charge concerns is the original's. The three candidate-side fallbacks FIX5-CONTRB cited stand exactly where it put them (candidate L609, L847, L868 against original L603, L841, L862) and are the phase17-diff page's documented repairs to credit-button, search-box, and author-link furniture. Two further censuses close the ground. First, the word "panel" occurs zero times in each file: the theme defines no panel selector at all, so the charged surface's background is the shared BHL base and sample construction, and the only contribution this file makes to the pairing is the variable values, all identical. Second, the candidate's three appended correction modules (candidate L884-899) were read for colour declarations and contain none (a grid template, a white-space rule, a word-break rule), so no candidate-side supplement of any kind styles the panels or their text.

Second-reviewer walk. The ground is fully re-derivable from this package: a reader can extract the two windows from original.txt and candidate.txt and compare the hashes, and can census the fallbacks and tail modules at the cited lines. The walk also tested the two ways the ground could fail. A candidate-side change to the panel pairing would have to appear as a colour declaration, a panel selector, or a changed variable value; the censuses show none exists. A base swap that changed the surface would break the ground's premise, but the base is the ruling-1 JP port of the original's own BHL base, the same base the production page uses, and FIX5-CONTRB records it as mandated rather than chosen. What remains is the original's palette composed on the shared sample's panel classes, faithfully reproduced. The disposition stands.

### Defect flags (candidate not edited by this lane)

- F1: candidate L147 escapes its footnoteblock (@@[[footnoteblock]]@@) although the candidate carries two live footnotes, at candidate L51 and candidate L133 (the translator's note), whose render position that block is. The original keeps the block live (original L139) and so does the production page (pages-existing L141); the escape is the candidate's own delta against both. This is the escaped-footnoteblock shape the campaign has repaired elsewhere by unescaping (penumbra, scp-offices-theme, yossistyle). The classifier lists the block as residue B48, with no signature. Flagged with both sides' lines; the repair is one line, for the coordinator's fix queue.

### Candidate-versus-production record (K6 third source)

The full candidate-versus-production diff was enumerated. Beyond the phase17-diff deltas (sections 1 and 8) and flag F1, the deltas are: the credit completion (section 1); the usage exhibits' escaping and the self-name repoint (section 2, the repoint being the snippet audit's line, commit 358955e); the storage URL scheme and colon form (sections 4 and 11); the footnote author-link notation (candidate L51 drops production's [[*user Placeholder McD]] link, the name retained, the same notation family as the credit author field); trailing-space trims on blockquote markers; the self-delivery repoint (section 3); and the three appended modules (section 8). The sources.tsv note "production drift: 一致" is consistent with this census: no unexplained drift exists.

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:minimalist-bhl-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP8, landing `1f846a6` (report `R/review-scout/FIX-RDISP8.md`).** One candidate repair (+1/−1 on this file), postdating this package's build at `358955e` (production-predecessor reference audit, which the as-built `candidate.txt` matches byte-for-byte).
- **Item 1 — escaped footnoteblock unescaped.** The candidate carries two live footnotes (L51 and L133), but its footnoteblock token (as-built L147) stood escaped as `@@[[footnoteblock]]@@`. Both sources keep the token live at the corresponding position — the frozen original L139 and the production page `pages-existing/existing:theme-minimalist-bhl.txt` L141 both read `[[footnoteblock]]`. The escape was the candidate's own delta against both sources; L147 now reads the live token, giving the footnotes a render position.
Checker per the report: plain and links error 3 / warn 1 / info 3 before and after, finding sets byte-identical in both modes; class (i) 0.

## Appendix — residue and heuristic blocks

The 21 heuristic blocks are translation mass in one shape, plus the three documented CSS repairs; the three residue blocks are two seams and the footnoteblock flag. Each is assigned here.

- 18 TRANS-UNANCHORED tier-C blocks (B13-B15, B23, B25, B27-B37, B44, B45; original L42-127 to candidate L50-135, body to body): prose and specimen lines of the documentation body whose line shape changed in translation (script delta without the anchor majority), inherited through the production page's translation. Assigned to section 6.
- B59, B60, B63 (CSS-BODY; original L602-862 to candidate L608-868, code-css): the three variable-fallback repairs. Assigned to section 8.
- B11 (residue; original L38-39 to candidate L46-47): the usage exhibit's closing lines gaining their @@ escapes, the tail of the exhibit-escaping delta. Assigned to section 8.
- B48 (residue; original L139-140 to candidate L147): the footnoteblock line and its following blank, the escape flagged as F1. Assigned to the per-theme record.
- B55 (residue; original L424 to candidate L431): a pairing seam with no content delta; the comment line "/* Okay, now for the links and the body */" stands on both sides (original L425, candidate L431), and the classifier paired the original's preceding blank line against it. Assigned here, closed.

## License and attribution

- **Title:** Minimalist BHL Theme
- **Author:** JakdragonX、Pedagon
- **Source:** https://scp-wiki.wikidot.com/theme:minimalist-bhl — revision 107 (revision date 2026-04-12 05:12:17)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: walksoldi — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
