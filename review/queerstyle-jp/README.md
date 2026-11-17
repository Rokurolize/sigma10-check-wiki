# Review package — theme:queerstyle-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:queerstyle-jp — origin EN, population #126 [GOSIGN2-LEDGER (b) row 126]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now a82832d74635c81c0c4474aaf60ce40ba2f5717f4661c8ab980a5be8c4726d2c); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 0 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 151; GOSIGN2-LEDGER (b) row 126]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-rate (all combos) + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2); T3 rainbow pride logo overprints the SCP財団 header wordmark and account/search links at 375/320 (both engines, candidate header interference); credit panel dark/blank at 1366. [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN17))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 126, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 126]
- FIX5 re-judgement: items 22 (class F) DISPOSITIONED, 23 (class F) DISPOSITIONED — FIX5-FUNC §5 (no edit): logo rule placement, height and identity unchanged vs original (diff shows only header language, ruling 2, and the asset host); overprint is the original fork's design; observation predates the FIX4-IWA interwiki frame now present at L9-12; the credit area is credit:start-preview (L16-25), whose rendering is a preview-form property (KB-32 class, ledger s(d) item 5); no re-measurement records persistence and no candidate-side cause is pointable. Narrowest disposition of this wave; see s(d) note [GOSIGN2-LEDGER-SUPPLEMENT (a) items 22–23]
- Computed against: canonical commit b1e1fe95acabd16c1f83a1387c750c2bf8ba433e; candidate file pages/theme:queerstyle-jp.txt sha256:a82832d74635c81c0c4474aaf60ce40ba2f5717f4661c8ab980a5be8c4726d2c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete - explanation written by lane R-disp-10, 2026-11-17; all skeleton markers resolved
Candidate: review/queerstyle-jp/candidate.txt (sha256 86c4d603464bf27b0bae451221a480bf670469ef7cd4f923497138607fc7b002)
Original: theme:queerstyle — scp-wiki, revision 51 (sha256 bbe9aaa667c73f6c923061cf92ad24e4d075fca4d14ac9bc957e88ffed0715f2)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

Complete (lane R-disp-10, 2026-11-17). Both blocking items are class F dispositions; each is re-derived from this package's bytes in the Per-theme record below, with the second-reviewer walk the class requires. One minor defect flag (a porter annotation that overstates its font claim, candidate L65) is recorded in section 4 and the Per-theme record. The candidate is not edited by this lane.

## Provenance

| | |
|---|---|
| Original | theme:queerstyle, scp-wiki (EN), revision 51 |
| Original file | original.txt, 155 lines / 3,919 bytes, SHA-256 bbe9aaa667c73f6c923061cf92ad24e4d075fca4d14ac9bc957e88ffed0715f2 (matches review/sources.tsv) |
| Mirror source | campaign mirror store file orig-queerstyle-rev51.txt, from gosign2-lanes/lane-oc-gs-localize-s2-C/orig-queerstyle.txt, fetched 2026-11-16 |
| Candidate | theme:queerstyle-jp, pages/theme:queerstyle-jp.txt |
| Candidate file | candidate.txt, 169 lines / 5,188 bytes, SHA-256 86c4d603464bf27b0bae451221a480bf670469ef7cd4f923497138607fc7b002 (byte-identical to canonical) |
| Route | Derived from the original at the reference revision (first translation, Stage 2 lane EN17, LOCALIZE-S2-C). No production JP counterpart exists to adopt. |
| Wave history | b17d7e4 (Stage 2 EN17 integrate), 1869877 (FIX-CREDIT-D: translator field), 8c62b7b (FIX4-IWA: interwiki frame), 379eb44 (FIX4-MOPUP: KB-65 duplicate-import removal; the stamp's computed-against commit) |
| Change set | diff.md: +52 / -43 lines; 27 classifier blocks (18 specific, 9 heuristic, 0 residue) |

## Summary

Queerstyle is Queerious's fork of Blankstyle, a general-purpose theme with a rainbow pride logo in the header. The port translates the prose, swaps the credit block to the JP preview form, repoints the base and component includes to their JP candidates, re-hosts the logo asset and the font import, appends Noto Sans JP to the theme's own font stacks, and adds the FIX4-IWA interwiki frame. The two blocking items (the logo overprinting the header at mobile widths, and the credit panel rendering dark at 1366) were dispositioned without an edit by FIX5; both grounds re-derive exactly from the bytes in this package. One minor defect is flagged: the porter font note at candidate L65 claims a general Noto Sans JP fallback that only the theme's own .pseudo-div stacks actually have.

## Class summary

| Label | Blocks |
|---|---|
| ASSET-REHOST | 1 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 3 |
| COMPONENT-SWAP | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 3 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 5 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 3 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 3 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 11 |
| TRANSLATION-ANCHORED | 5 |

Counts: 27 blocks, 18 specific, 9 heuristic, 0 residue, 0 skipped (comment text).

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

- Provenance route: derived from the original at revision 51 (first translation). The mirror in this package is the localize lane's capture; its SHA-256 equals the sources.tsv row, and the T4 follow-up (section 12) confirms revision 51 is still the original's current revision, so the mirror is also the current original.
- Delivery census: exactly one [[code type="CSS"]] block on each side, self-delivered as the page's /1 (head [[module CSS]] @import at candidate L6; the interwiki frame at candidate L9-12 names the same page). No relocation between the sides: head module, code block, and tail [[module CSS]] stand in the same order on both sides. The tail module's @import, duplicated identically in the original, was removed by the KB-65 mop-up (379eb44); the tail module now stands empty and delivery is carried by the head module and the frame (section 3).

## 1. Credit and attribution

- BARE-RATE-DEL (B): Duplicate bare Rate removed (KB-09, ledger class B): the preview credit module is already rate-bearing, so a second bare Rate module double-renders the widget.
  Verify: Grep both sources for [[module Rate]]; the candidate must hold none outside labelled exhibits.
  - B4: orig 11-13 -> cand 14-14 (body -> body)

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B5: orig 15-15 -> cand 16-25 (body -> body)

**What (this theme):** the original's bare [[module Rate]] (original L11-13) is deleted (B4); a grep for [[module Rate]] over candidate.txt finds none outside exhibits, so KB-09 holds. The credit block (B5, candidate L16-25) is the population's credit:start-preview form with all 8 TASL fields; the author field names Queerious, matching the original's banner comment and its prose credit, and the creation year reads 2024 (the original's revision 0 is dated 2024-04-15, verified by the localize lane). The translator field reads AI per FIX-CREDIT-D (1869877); the localize report's earlier value is superseded by the current bytes and is carried as a record note in the Per-theme record, not a defect.
**Why:** the preview credit module is the rate-bearing form in this environment (P3); a second bare Rate double-renders the widget (KB-09). Attribution beyond the author field survives: Placeholder McD and HarryBlank are credited in the prose (candidate L27) and in the CSS banner (candidate L88), Woedenaz in the prose (candidate L29) and the banner (candidate L90).
**Verify:** grep both files for [[module Rate]]; read candidate L16-25 against original L14-15 and the banner at original L71-76 / candidate L85-90.
**Disposition:** the theme's only credit CSS, #page-content.creditButton p a (color #373737), is byte-identical (original L115-117 = candidate L130-132); the credit panel's rendering is item 23's ground, re-derived in the Per-theme record.

## 2. Includes and components

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B1: orig 2-2 -> cand 2-2 (body -> body)
  - B12: orig 40-41 -> cand 52-53 (body -> body)

**What (this theme):** B1 repoints the base include at the head (original L2) from the EN original to theme:blankstyle-jp, the campaign's JP candidate of the same theme. B12 repoints the usage-example includes (original L40-41 to candidate L52-53) the same way. The three gated component includes inside the usage region (toggle-sidebar, fade-in, acs-animation) are filed by the classifier under section 8 (B15-B17) and adjudicated there; their targets repoint :scp-wiki: to :scp-jp: with localized gates.
**Why:** a port builds on the JP candidate of its base, never the raw branch delivery (the campaign's cross-theme import ruling).
**Verify:** grep candidate.txt for [[include; every target is a campaign page name or a :scp-jp: include.
**Disposition:** no component was ported by this theme; the base and the components already exist as campaign candidates.

## 3. Delivery and code loading

- DELIVERY-HOST (A): Base/host repoint (P4/T9): deliveries are served from the JP hosts in this environment.
  Verify: Resolve the new host path; a kept old-host line is a class (ii) posting matter, recorded in section 11.
  - B2: orig 6-6 -> cand 6-6 (module-css -> module-css)

- SELF-DELIVERY (A): Own code-delivery import changed (P4): the page's own local--code delivery is its live CSS channel.
  Verify: The named delivery resolves on the draft host and serves the current candidate body.
  - B3: orig 9-9 -> cand 9-12 (body -> body)
  - B27: orig 153-153 -> cand at 168 (module-css -> body)

**What (this theme):** B2 is the head [[module CSS]]: the @import host changes from the original base's delivery host to the JP base's Google Fonts delivery, and the page's own /1 self-delivery stands in the draft-host form (the checker's pseudo-ref line, a standing class). B3 is the FIX4-IWA interwiki frame at candidate L9-12 (priority=1), added by 8c62b7b; it closes the localize lane's pattern 6 for this theme. B27 is the tail [[module CSS]] @import's deletion: the original carried the identical @import twice (head and tail); the KB-65 mop-up (379eb44) removed the tail copy, so the tail module at candidate L167-168 stands empty and the stylesheet is delivered by the head module and the frame.
**Why:** delivery must resolve inside the JP environment (P4). A duplicated @import of the same URL is idempotent, but it is exactly the KB-65 duplicate-load shape, and its removal is why the current checker run reports one pseudo-ref where the baseline reported two (section 12).
**Verify:** read candidate L5-12 and L167-168 against original L5-9 and L152-153; the named /1 block is the page's single code block, which holds the full stylesheet (section 0 census).
**Disposition:** the frame's presence postdates the item 22/23 measurements; that ordering is part of item 23's ground (Per-theme record).

## 4. Fonts and assets

- JPFONT-STACK (B): JP family appended to a stack (P7/T5): the Latin faces have no kana glyphs; the appended JP family is the fallback that renders Japanese.
  Verify: Read the paired font-family lines; Latin families unchanged, JP family appended.
  - B10: orig 34-34 -> cand 46-46 (body -> body)
  - B25: orig 136-136 -> cand 151-151 (code-css -> code-css)
  - B26: orig 141-141 -> cand 156-156 (code-css -> code-css)

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B20: orig 78-78 -> cand 92-93 (code-css -> code-css)

- ASSET-REHOST (A): Asset re-hosted to JP storage (P5, KB-17): assets are served from the allowlisted JP hosts in this environment.
  Verify: KB-17 host list; the re-hosted URL serves.
  - B22: orig 112-112 -> cand 127-127 (code-css -> code-css)

**What (this theme):** B20 changes the font loads at the head of the code block: the Vast Shadow @import moves to Google Fonts (candidate L92), and a Noto Sans JP @import is added (candidate L93, JPFONT-LOAD). B10, B25, B26 append "Noto Sans JP" to the theme's own font-family stacks (the .pseudo-div exhibit stack at candidate L46 and the two code-block stacks at candidate L151 and L156, JPFONT-STACK, P7). B22 re-hosts the pride logo (gp_logo.svg) from scp-wiki.wdfiles.com to scp-jp-storage.wdfiles.com, same filename (candidate L127, ASSET-REHOST, KB-17). Font audit: Vast Shadow is loaded (candidate L92) and applied; Noto Sans JP is loaded (candidate L93) and applied in the theme's own stacks; no family is named but unloaded, and no load is duplicated.
**Defect flag (minor):** the porter note at candidate L65 states that Japanese text falls back to Noto Sans JP, without qualification. Only the theme's own .pseudo-div stacks name Noto Sans JP; body and header glyphs inherit the base blankstyle-jp's Latin-only stacks, so the note overstates the fallback's reach. The localize lane recorded the same overstatement (LOCALIZE-S2-C EN17-2 pattern 7, partial; T5 finding (1)). The remedy is to narrow the note's wording to the theme's own stacks; the candidate is not edited by this lane.
**Why:** the Latin faces carry no kana glyphs, so the theme's own stacks need the JP fallback (P7/T5); the asset re-host puts the logo on an allowlisted JP host (KB-17).
**Verify:** read candidate L92-93, L46, L151, L156 and the note at L65; compare the base's stacks in pages/theme:blankstyle-jp.txt.
**Disposition:** the logo rule itself is untouched; its bytes are item 22's ground (Per-theme record).

## 5. Header, sidebar, site furniture

- HEADERVAR (A): Header/title variables (P9/T6, KB-57): the header text variables are the theme's visible title surface.
  Verify: KB-57: where the value stays in the original's language, the disposition is ruling 2 (section 11).
  - B21: orig 95-96 -> cand 110-111 (code-css -> code-css)

**What (this theme):** B21 changes the two header variables (original L95-96 to candidate L110-111): --header-title and --header-subtitle take their JP-environment values. Nothing else in the header surface changes: the #header h1 and h2 rules are byte-identical, and the @media (max-width: 707px) block is byte-identical (87 bytes).
**Why:** the header variables are the theme's visible title surface (P9/KB-57); where a value stays in the original's language, the ground is the campaign's header/title ruling (names and marks stay as identity strings), recorded in section 11.
**Verify:** diff original L80-113 against candidate L95-128; exactly three lines differ (the two variables and the logo URL, section 4).
**Disposition:** item 22's re-derivation rests on this window; see the Per-theme record.

## 6. Text translation

- TRANS-UNANCHORED (C): Translation-shaped change without anchors (P10, KB-18): restructured lines are the queue where restorations and exhibit changes hide.
  Verify: Writer confirmation against the mirror, line by line.
  - B7: orig 19-19 -> cand 29-31 (body -> body)
  - B9: orig 32-32 -> cand 44-44 (body -> body)
  - B11: orig 37-37 -> cand 49-49 (body -> body)
  - B13: orig 46-46 -> cand 58-58 (body -> body)
  - B14: orig 51-51 -> cand 63-65 (body -> body)
  - B19: orig 72-76 -> cand 86-90 (code-css -> code-css)
  - B23: orig 119-119 -> cand 134-134 (code-css -> code-css)
  - B24: orig 128-128 -> cand 143-143 (code-css -> code-css)

- TRANSLATION-ANCHORED (B): Prose/usage translation (P10, KB-18): reader-visible text localizes; anchored pairs are one-to-one translations.
  Verify: Read the pairs; the anchors (leading token, CSS property, selector, heading level) confirm the pairing.
  - B8: orig 23-28 -> cand 35-40 (body -> body)
  - B18: orig 67-67 -> cand 81-81 (body -> body)

**What (this theme):** the prose body translates one-to-one: 5 TRANSLATION-ANCHORED blocks and the TRANS-UNANCHORED mass (appendix) cover the fork explanation, the usage instructions, and the design notes; the 3 COMMENT-TEXT blocks (B19, B23, B24) are CSS comment translations inside the code block (the banner's author line, the email-component-fix comment, the Pseudogenesis-formats comment). Each pair was read against the mirror line by line; no prose was dropped and no specimen text was silently replaced.
**Why:** reader-visible text localizes (P10, KB-18); CSS comments translate with the file.
**Verify:** read the pairs in diff.md; the appendix assigns every heuristic block.
**Disposition:** the localize lane's T5 findings stand as recorded in the stamp; the font-note overstatement is a porter-annotation matter, filed in section 4.

## 7. Links

- LINK-REPOINT (C): Link target repointed (P11): prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.
  Verify: Probe the target; a repoint needs sameness evidence.
  - B6: orig 17-17 -> cand 27-27 (body -> body)

**What (this theme):** B6 covers the two attribution links in the fork sentence and the pride-logo sentence: both are absolutized to the EN original (candidate L27, theme:blankstyle; candidate L29, component:pride-highlighter, both on scp-wiki.wikidot.com). Both targets were probed on 2026-11-17 and serve 200.
**Why:** both links sit in attribution sentences crediting the original works (the fork's source theme and the logo's component). Under the population's adjudication for attribution sentences, the original target stands. The file applies no original-language annotation anywhere, so there is no internal inconsistency of the shape flagged in another package, where one link in a sentence carried the annotation and its sibling did not.
**Verify:** probe the two URLs; read candidate L27-31 against original L16-19.
**Disposition:** recorded, not a defect. The base include itself is repointed to the JP candidate (section 2); only the prose credit links name the EN originals.

## 8. Structure

- EXHIBIT-RESTRUCTURE (C): Usage/sample exhibits dropped or replaced (R3): a sanctioned replacement and a silent deletion have the same diff shape; the ground must be stated.
  Verify: The exhibit-decision slot for this block, argued from the mirror.
  - B15: orig 55-56 -> cand 69-70 (body -> body)
  - B16: orig 58-59 -> cand 72-73 (body -> body)
  - B17: orig 62-63 -> cand 76-77 (body -> body)

**What (this theme):** the classifier files B15-B17 as EXHIBIT-RESTRUCTURE. Against the bytes they are the usage region's three iftags-gated conditional includes: toggle-sidebar (original L56 to candidate L70), fade-in (original L59 to candidate L73), and acs-animation (original L63 to candidate L77). Each gate localizes (+theme to the JP theme tag, -theme likewise) and each target repoints :scp-wiki: to :scp-jp:. The EXHIBIT-RESTRUCTURE label false-fires on include repoints inside exhibit regions; the exhibit census is unchanged: every sample exhibit the original carries stands in the candidate, and nothing was dropped or replaced.
**Why:** the gates are conditions on delivery furniture, and their conditions must name JP tags in the JP environment (KB-08); the includes take the JP component candidates.
**Verify:** read original L54-63 against candidate L68-77; count the exhibits on both sides.
**Disposition:** exhibit decision below.


Exhibit decision: replaced, none; dropped, none. B15-B17 are gated delivery includes misread as exhibits by the label; the actual exhibits are translation mass (section 6). The bare-Rate deletion (B4) is filed in section 1: the removed Rate stood in the theme's head furniture, not beside an exhibit label, and the preview credit module is rate-bearing (KB-09).

## 9. Formatting only

- WS-ONLY blocks: 0
- Re-indentation: 0 blocks pair up after leading-whitespace normalization

## 10. Porter annotations

One porter annotation: the font note at candidate L65, riding inside B14 (TRANS-UNANCHORED). Its content is adjudicated in section 4 (defect flag F1: the note overstates the Noto Sans JP fallback). No other porter annotations are present.

## 11. Dispositions and exceptions

- Item 22 [F] DISPOSITIONED (FIX5-FUNC section 5, no edit): the rainbow pride logo overprint at 375/320 is the original fork's design; the logo rule's placement, height, and identity are unchanged by the port. Re-derived from this package's bytes in the Per-theme record: the ground holds exactly.
- Item 23 [F] DISPOSITIONED (FIX5-FUNC section 5, no edit): the credit panel's dark/blank rendering at 1366 is a property of the credit:start-preview form (KB-32 class; ruling 5), and the observation predates the FIX4-IWA interwiki frame now at candidate L9-12. Re-derived in the Per-theme record, which also states the walk's reservation: the supplement itself names this the narrowest disposition of the wave, and no post-frame re-measurement exists in the record.
- (c3) LOCALIZE-S2-C P1 DISPOSITIONED: the posting-procedure convention class; no candidate change is the right outcome.
- T1 standing class: the draft-host self-delivery @import (candidate L6) is the checker's pseudo-ref line, dispositioned in register (c1); the T2/T3 record's hidden-rate and runtime-hotlink lines are likewise standing classes in register (c1), as the stamp records.
- Header/title ruling: the header variables' language treatment (section 5) follows the campaign's ruling that names and marks stay as identity strings while prose-sentence defaults translate, as recorded by FIX5-FUNC section 5.

## 12. Verification

- T1 checker (canonical invocation, run by this lane 2026-11-17): exit 1, 1 error / 0 warns / 0 infos. The sole error is the pseudo-ref at candidate L6 (the draft-host self-delivery @import, the standing class in section 11). Baseline (T1-ROWS row 151): exit 1, 2 errors / 1 warn / 0 infos (pseudo-ref x2); the second pseudo-ref was the tail-module @import removed by the KB-65 mop-up (379eb44). The baseline's warn is not itemized in T1-ROWS; the current run reports no warns.
- T2/T3 render: not re-run by this lane. The measurements behind items 22 and 23 stand as recorded (RENDER-ROWS-2, RENDER-S2-C (EN17)); this lane re-derived both dispositions from the package bytes instead (Per-theme record), which is the R-disp standard for class F items.
- T4 follow-up: the original's current revision is still 51; the follow-up diff from revision 51 shows no change, so original.txt is both the reference mirror and the current original.
- Package checks: candidate.txt is byte-identical to pages/theme:queerstyle-jp.txt; original.txt's SHA-256 equals the sources.tsv row; python3 review/build_review.py --check passes for this package (the lane report carries the stale-set comparison).

## Per-theme record - FIX5 items re-derived

### Item 22 [F] - DISPOSITIONED (FIX5-FUNC section 5, no edit)

The blocking item: the rainbow pride logo overprints the header wordmark and the account/search links at 375px and 320px widths, in both engines (GOSIGN2-LEDGER (b) item 22, from RENDER-S2-C (EN17)). The FIX5 ground: the logo rule's placement, height, and identity are unchanged versus the original; the diff shows only header language (the header/title ruling) and the asset host; the overprint is the original fork's design.

Re-derivation from this package's bytes. The unified diff of original L80-113 against candidate L95-128 (the :root and header region) contains exactly three differing lines: --header-title, --header-subtitle, and the gp_logo.svg URL (host re-host only, same filename). The logo rule itself, div#extra-div-1 (original L110-113, candidate L125-128), is byte-identical: selector line, height: 150px line, and closing brace. The @media (max-width: 707px) block is byte-identical (87 bytes). The #header h1/h2 rules are byte-identical. Widening past the window: the selector census is equal (13 on each side), the brace depth ends at 0 on both sides, and every code-block declaration difference in the file is confined to six items: the font import host, the added Noto Sans JP @import, the two header variables, the logo URL, and the two font-family stacks gaining the Noto Sans JP fallback. No placement, height, or stacking value differs anywhere.

Second-reviewer walk. The ground is checkable from this package alone: the three differing lines and the identical logo rule sit in original.txt and candidate.txt, and any reader can re-run the window diff. The engine half of the item (the overprint as rendered at 375/320 in both engines) rests on the RENDER-S2-C record cited in the stamp, not on bytes; the disposition's claim is only that the port did not cause it, and that claim is exactly what the bytes decide. A fix would have to alter CSS that is byte-identical to the original, to change the original fork's own design. The disposition stands.

### Item 23 [F] - DISPOSITIONED (FIX5-FUNC section 5, no edit)

The blocking item: the credit panel renders dark/blank at 1366 (GOSIGN2-LEDGER (b) item 23). The FIX5 ground has two parts: the credit area is the population's credit:start-preview block, whose rendering is a property of the preview form (KB-32 class; ledger (d) item 5; ruling 5), and the measurement predates the FIX4-IWA interwiki frame the candidate now carries.

Re-derivation from this package's bytes. The frame stands at candidate L9-12 (priority=1), added by 8c62b7b, after the measurement was taken. The credit area is exactly the credit:start-preview block at candidate L16-25 with its 8 fields (section 1). The theme's only credit CSS, #page-content.creditButton p a (color #373737), is byte-identical (original L115-117 = candidate L130-132), so the theme contributes no credit styling that differs from the original. No candidate-side cause for a dark panel is pointable from the bytes.

Second-reviewer walk. This is, in the supplement's own words, the narrowest disposition of the wave, and the walk records it at that weight. The byte-checkable half holds: the credit block is the preview form, the frame postdates the measurement, and the theme's credit CSS is unchanged. The other half is a class judgement (preview-form rendering is the form's property, per KB-32 and ruling 5), not a byte fact, and no post-frame re-measurement exists in the record to confirm the panel now renders. The disposition stands on those stated terms; a reviewer who wants more than the class judgement needs a fresh render measurement, which is a campaign-level follow-up, not a defect in this candidate.

### Defect flags (candidate not edited by this lane)

- F1 (minor): candidate L65, the porter font note overstates the Noto Sans JP fallback (section 4). Remedy: narrow the note to the theme's own .pseudo-div stacks.

### Record notes

- The localize lane's report records the credit translator field under its earlier value; FIX-CREDIT-D (1869877) changed the field, and the current bytes carry the campaign's AI attribution. The bytes govern.
- The T1 baseline's single warn (T1-ROWS row 151) is not itemized by kind in the record; the current checker run reports no warns (section 12). No discrepancy is charged.
- The sources.tsv note field for this row is empty; the T4 follow-up confirms revision 51 remains current, so no supersession note arises.

### Repair landed after this package was built

- F1 repaired by FIX-RDISP10 (record R/review-scout/FIX-RDISP10.md), landed in commit b1e1fe9: the porter font note at candidate L65 is narrowed to the theme's own .pseudo-div stacks (its second sentence now states the Noto Sans JP fallback for this theme's pseudo-div styles only); no CSS was touched. One precision from the fix lane: this README's section 4 calls blankstyle-jp's stacks Latin-only, but blankstyle-jp's header and heading stacks do name 'Noto Sans JP' behind Montserrat (its body rule sets no font-family); the defect and remedy are unaffected, since the note claimed the fallback for queerstyle's own delivery, where it exists only in the .pseudo-div stacks. candidate.txt is recopied from the repaired candidate in this refresh; the regenerated stamp reads STALE, no re-judgement is fabricated, and the frozen ledger remains the verdict record.

## Appendix - residue and heuristic blocks

No residue blocks. The 9 heuristic blocks are translation mass in three shapes; each is assigned here. The classifier's prose pairing drifts by one sentence across B6/B7 because the credit block grew the candidate above them; the pairings below are from the files, not the skeleton's first-line display.

- B6, B7 (original L16-19 to candidate L26-31, body): the fork-attribution and pride-logo prose sentences, translated; B6 also carries the two absolutized attribution links. Assigned to sections 6 and 7.
- B9, B11, B13 (original L31-46 to candidate L43-58, body): one-line usage instructions, translated. Assigned to section 6.
- B14 (original L50-51 to candidate L62-65, body): the design-note sentence, translated; the block also carries the added porter font note at candidate L65. Assigned to sections 6 and 10 (the note is defect flag F1, section 4).
- B19, B23, B24 (code-css): CSS comment translations (the banner author line; the email component fix comment; the Pseudogenesis formats comment). Assigned to section 6.
